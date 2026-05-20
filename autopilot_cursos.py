"""
autopilot_cursos.py — v4
========================
Crea todos los cursos pendientes del mapa en automático.

USO — un solo comando:
    python autopilot_cursos.py

QUÉ HACE (en orden):
  1. Completa slides faltantes de cursos ya creados
  2. Convierte evaluaciones .md a .docx Word (si faltan)
  3. Crea cursos nuevos (⏳ Por hacer) sin slides
  4. Al final genera las slides de los nuevos cursos
  Si el rate limit se alcanza → 3 pitidos, guarda progreso y para
  Al día siguiente: notebooklm login → python autopilot_cursos.py

MEJORAS v4:
  - Verifica COMPLETITUD de cursos antes de crear nuevos:
      ✅ Clases .md generadas
      ✅ Slides .pdf completas
      ✅ Evaluación .md generada
      ✅ Evaluación convertida a .docx (Word)
  - Convierte automáticamente evaluaciones pendientes a Word
  - Orden: slides → word → cursos nuevos
"""

import subprocess, sys, json, os, re, time, winsound
from pathlib import Path
from datetime import timedelta

MD_A_WORD = Path(r"C:\Users\braya\OneDrive\Documentos\4 portafolio\md_a_word.py")

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

VAULT       = Path(r"C:\Users\braya\OneDrive\Documentos\4 portafolio")
MAPA        = VAULT / "Cursos" / "00 - Mapa de cursos.md"
SCRIPT      = VAULT / "crear_curso_notebooklm.py"
ESTADO_JSON = VAULT / ".autopilot_estado.json"
LOG_FILE    = VAULT / "autopilot.log"
ENV         = {**os.environ, "PYTHONIOENCODING": "utf-8"}

SECCIONES = [
    # Materias avanzadas OMITIDAS: Trigonometría, Cálculo, Física, Repaso General
    # Álgebra avanzada también omitida (cursos complejos nivel 🔴9)
    ("## Aritmética",          "Aritmética"),
    ("## Álgebra",             "Álgebra"),
    ("## Geometría",           "Geometría"),
    ("## Estadística",         "Estadística"),
]
# "## Álgebra avanzada" detiene el parser antes de procesar esos cursos complejos
STOP_HEADERS = {"## 🎯", "## ⚠️", "## 📊", "## 🗺️", "## Notas", "## Álgebra avanzada"}

# ── Helpers ──────────────────────────────────────────────────────────────────

def log(msg):
    ts = time.strftime("%H:%M:%S")
    linea = f"[{ts}] {msg}"
    print(linea)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(linea + "\n")

def beep_alerta():
    for _ in range(3):
        winsound.Beep(1000, 400); time.sleep(0.2)

def beep_ok():
    winsound.Beep(800, 300)

def fmt_tiempo(segundos):
    return str(timedelta(seconds=int(segundos)))

# ── Detección de rate limit ───────────────────────────────────────────────────
# IMPORTANTE: solo se llama cuando exit_code != 0
# Así evitamos falsos positivos con el texto informativo del script
RATE_LIMIT_SLIDES = [
    "RPC LIST_ARTIFACTS failed",
    "quota exceeded",
    "too many requests",
    "error 429",
    "rate_limit_exceeded",
]
RATE_LIMIT_INFORMES = [
    "RPC CREATE_ARTIFACT failed",
]

def es_rate_limit(texto):
    """Rate limit de slides (llamar solo cuando rc != 0)."""
    t = texto.lower()
    return any(s.lower() in t for s in RATE_LIMIT_SLIDES)

def es_rate_limit_informes(texto):
    """Rate limit de informes (textos/clases). Puede ocurrir con rc == 0."""
    t = texto.lower()
    return any(s.lower() in t for s in RATE_LIMIT_INFORMES)

def es_sesion_expirada(texto):
    t = texto.lower()
    return any(s in t for s in ["sesión expirada", "session expired", "notebooklm login"])

# ── Estado de progreso ────────────────────────────────────────────────────────

def cargar_estado():
    if ESTADO_JSON.exists():
        data = json.loads(ESTADO_JSON.read_text(encoding="utf-8-sig"))
        # Compatibilidad con v1
        if "contenido_ok" not in data:
            data["contenido_ok"] = data.get("completados", [])
        if "slides_ok" not in data:
            data["slides_ok"] = []
        return data
    return {"contenido_ok": [], "slides_ok": [], "errores": []}

def guardar_estado(e):
    ESTADO_JSON.write_text(json.dumps(e, ensure_ascii=False, indent=2), encoding="utf-8")

# ── Parsear mapa ──────────────────────────────────────────────────────────────

def leer_cursos():
    cursos = []
    materia_actual = ""
    en_tabla = False

    for line in MAPA.read_text(encoding="utf-8").split("\n"):
        if line.startswith("##"):
            en_tabla = False
            for header, mat in SECCIONES:
                if line.startswith(header):
                    materia_actual = mat
                    en_tabla = True
                    break
            for stop in STOP_HEADERS:
                if line.startswith(stop):
                    en_tabla = False; materia_actual = ""
            continue

        if not en_tabla or "Ver playlist" not in line:
            continue

        m_url = re.search(r'https://www\.youtube\.com/playlist\?list=[A-Za-z0-9_-]+', line)
        if not m_url:
            continue
        url = m_url.group(0)

        m_num = re.match(r'\|\s*(\d+)\s*\|', line)
        num = int(m_num.group(1)) if m_num else 0

        nombre = ""
        m_wiki = re.search(r'\\\|([^|\\^\]]+)\]\]', line)
        if m_wiki:
            nombre = m_wiki.group(1).strip()
        else:
            cols = [c.strip() for c in line.split("|")]
            if len(cols) >= 3:
                raw = cols[2].strip().rstrip("\\").strip()
                if raw and "[[" not in raw and not raw.startswith("*"):
                    nombre = raw

        cols_nv = [c.strip() for c in line.split("|") if c.strip()]
        estado  = cols_nv[-1] if cols_nv else ""

        if nombre and url:
            cursos.append({"num": num, "nombre": nombre, "url": url,
                           "materia": materia_actual, "estado": estado})

    return sorted(cursos, key=lambda c: c["num"])

def curso_tiene_contenido(c):
    """Verifica que el curso realmente generó archivos (al menos 1 Clase .md).
    Busca en TODAS las materias por si el curso fue guardado en carpeta diferente."""
    carpetas = VAULT / "Cursos"
    nombre_norm = c["nombre"].lower()
    for mat in carpetas.iterdir():
        if not mat.is_dir():
            continue
        for d in mat.iterdir():
            if d.is_dir() and d.name.lower() == nombre_norm:
                return len(list(d.glob("Clase*.md"))) > 0
    return False

def cursos_pendientes(cursos, estado):
    resultado = []
    for c in cursos:
        if "⏳" not in c["estado"]:
            continue
        if c["url"] not in estado["contenido_ok"]:
            resultado.append(c)
            continue
        # Estaba marcado como ok pero no tiene archivos → reintentar
        if not curso_tiene_contenido(c):
            log(f"⚠️  {c['nombre']} marcado ok pero sin archivos — reintentando")
            estado["contenido_ok"].remove(c["url"])
            resultado.append(c)
    return resultado

def cursos_sin_word(_cursos_ignorado=None):
    """Escanea filesystem: cursos con evaluación .md pero sin .docx."""
    carpetas = VAULT / "Cursos"
    result = []
    for mat in sorted(carpetas.iterdir()):
        if not mat.is_dir():
            continue
        for curso in sorted(mat.iterdir()):
            if not curso.is_dir() or not (curso / ".meta.json").exists():
                continue
            mds = list(curso.glob("*Evaluaci*.md")) + list(curso.glob("*evaluaci*.md"))
            if not mds:
                continue
            for md in mds:
                nombre_limpio = re.sub(r'[^\w\s\-]', '', md.stem).strip()
                nombre_limpio = re.sub(r'\s+', ' ', nombre_limpio)
                docx = md.parent / (nombre_limpio + '.docx')
                if not docx.exists():
                    result.append({
                        "nombre": curso.name,
                        "materia": mat.name,
                        "_carpeta": str(curso),
                        "_md": str(md),
                    })
                    break  # un entry por curso
    return result

def cursos_sin_slides(_cursos_ignorado=None, estado=None):
    """Escanea filesystem: cursos con .meta.json pero slides incompletas."""
    carpetas = VAULT / "Cursos"
    slides_ok = (estado or {}).get("slides_ok", [])
    result = []
    for mat in sorted(carpetas.iterdir()):
        if not mat.is_dir():
            continue
        for curso in sorted(mat.iterdir()):
            if not curso.is_dir() or not (curso / ".meta.json").exists():
                continue
            clave = f"{mat.name}/{curso.name}"
            if clave in slides_ok:
                continue
            n_clases = len(list(curso.glob("Clase*.md")))
            n_slides = len(list(curso.glob("*.pdf")))
            if n_clases == 0:
                continue
            # Detectar formato par (Clase XX-YY)
            es_par = any(re.search(r'Clase \d+-\d+', f.stem)
                         for f in curso.glob("Clase*.md"))
            esperados = (n_clases + 1) // 2 if es_par else n_clases
            if n_slides < esperados:
                result.append({
                    "nombre": curso.name,
                    "materia": mat.name,
                    "url": "",
                    "estado": "",
                    "_carpeta": str(curso),
                    "_clases": esperados,
                    "_slides": n_slides,
                })
    return result

# ── Ejecutar subproceso con output en tiempo real ────────────────────────────

def run(cmd, mostrar_output=True):
    """
    Ejecuta comando y devuelve (exit_code, output_texto).
    Muestra el output línea a línea mientras corre.
    """
    proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True, encoding="utf-8", errors="replace",
        env=ENV, cwd=str(VAULT)
    )
    lineas = []
    for linea in proc.stdout:
        if mostrar_output:
            print(linea, end="", flush=True)
        lineas.append(linea)
    proc.wait()
    return proc.returncode, "".join(lineas)

# ── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    t_inicio = time.time()
    tiempos_cursos = []  # para estimar tiempo restante

    print("\n" + "="*58)
    print("  🤖 AUTOPILOT DE CURSOS  v4")
    print("  Orden: 1) Slides → 2) Word → 3) Cursos nuevos → 4) Slides nuevas")
    print("="*58)

    cursos = leer_cursos()
    estado = cargar_estado()

    # ── Fase 1: completar slides de cursos ya creados ─────────────────
    sin_slides = cursos_sin_slides(estado=estado)
    log(f"Cursos existentes sin slides completas: {len(sin_slides)}")

    slides_rate_limit = False  # bandera para saber si el RL bloqueó slides

    for i, c in enumerate(sin_slides, 1):
        falta = c.get("_clases", "?") - c.get("_slides", 0)
        log(f"[{i}/{len(sin_slides)}] Slides: {c['nombre']} ({c['materia']}) — faltan {falta}")
        ruta = c.get("_carpeta") or f"{c['materia']}/{c['nombre']}"

        for intento in range(1, 3):
            rc, out = run([sys.executable, str(SCRIPT), "--solo-slides", ruta])

            if rc == 0:
                break

            if es_sesion_expirada(out):
                log("❌ Sesión expirada. Ejecuta: notebooklm login")
                guardar_estado(estado)
                beep_alerta()
                return

            if es_rate_limit(out):
                log("⚠️  Rate limit de slides — pasando a crear cursos nuevos")
                slides_rate_limit = True
                break

            if intento == 1:
                log(f"  ⚠️ Error — reintentando en 30s...")
                time.sleep(30)
            else:
                log(f"❌ Error en slides de {c['nombre']} — saltando")

        if slides_rate_limit:
            break

        if rc == 0:
            clave = f"{c['materia']}/{c['nombre']}"
            estado["slides_ok"].append(clave)
            guardar_estado(estado)
            log(f"✅ Slides de {c['nombre']} completas")

        time.sleep(3)

    if sin_slides and not slides_rate_limit:
        log("✅ Todos los cursos existentes tienen slides completas")
    elif slides_rate_limit:
        log("⚠️  Rate limit de slides activo — continuando de todas formas")

    # ── Fase 1b: convertir evaluaciones .md → .docx Word ─────────────
    sin_word = cursos_sin_word()
    log(f"Evaluaciones sin Word: {len(sin_word)}")

    for i, c in enumerate(sin_word, 1):
        log(f"[{i}/{len(sin_word)}] Word: {c['nombre']} ({c['materia']})")
        carpeta_curso = c.get("_carpeta") or str(VAULT / "Cursos" / c["materia"] / c["nombre"])
        rc, out = run([sys.executable, str(MD_A_WORD), "--todos",
                       carpeta_curso, "--sin-ia"])
        if rc == 0:
            log(f"✅ Word de {c['nombre']} listo")
        else:
            log(f"⚠️  Error Word en {c['nombre']} — continuando")
        time.sleep(2)

    if not sin_word:
        log("✅ Todos los cursos tienen evaluaciones Word")

    # ── Fase 2: crear cursos nuevos — SOLO si no quedan slides pendientes ─
    sin_slides_aun = cursos_sin_slides(estado=estado)
    if sin_slides_aun:
        log(f"⛔ Aún quedan {len(sin_slides_aun)} cursos con slides incompletas — no se crean cursos nuevos")
        for c in sin_slides_aun:
            log(f"   · {c['materia']}/{c['nombre']}: {c['_slides']}/{c['_clases']} slides")
        beep_alerta()
        print("\n" + "="*58)
        print("  ⛔ CURSOS NUEVOS EN ESPERA")
        print(f"  Faltan slides en {len(sin_slides_aun)} cursos existentes.")
        print(f"  Mañana ejecuta: python autopilot_cursos.py")
        print("="*58 + "\n")
        if ESTADO_JSON.exists():
            ESTADO_JSON.unlink()
        return

    pendientes = cursos_pendientes(cursos, estado)
    ya_hechos  = len(estado["contenido_ok"])

    log(f"Cursos por crear: {len(pendientes)}  |  Ya hechos antes: {ya_hechos}")

    for i, c in enumerate(pendientes, 1):
        t_curso = time.time()

        # Progreso + estimación
        if tiempos_cursos:
            avg = sum(tiempos_cursos) / len(tiempos_cursos)
            restante = avg * (len(pendientes) - i + 1)
            eta = f"  ⏱ ~{fmt_tiempo(restante)} restante"
        else:
            eta = ""

        log(f"[{i}/{len(pendientes)}] {c['nombre']} ({c['materia']}){eta}")

        # Intentar hasta 2 veces ante errores transitorios
        for intento in range(1, 3):
            rc, out = run([sys.executable, str(SCRIPT), c["url"], "--auto", "--skip-slides"])

            if rc == 0:
                # Verificar rate limit de informes aunque el exit code sea 0
                if es_rate_limit_informes(out):
                    log("⚠️  Rate limit de INFORMES detectado — deteniendo")
                    guardar_estado(estado)
                    beep_alerta()
                    print("\n" + "!"*58)
                    print("  ⚠️  RATE LIMIT DE INFORMES ALCANZADO")
                    print(f"  Progreso guardado ({len(estado['contenido_ok'])} cursos ok).")
                    print(f"  Mañana ejecuta:")
                    print(f"    notebooklm login")
                    print(f"    python autopilot_cursos.py")
                    print("!"*58 + "\n")
                    return
                break  # éxito real

            # Falló — ¿es rate limit o sesión expirada?
            if es_sesion_expirada(out):
                log("❌ Sesión expirada. Ejecuta: notebooklm login")
                guardar_estado(estado)
                beep_alerta()
                return

            if es_rate_limit(out):
                log("⚠️  Rate limit detectado — deteniendo")
                guardar_estado(estado)
                beep_alerta()
                print("\n" + "!"*58)
                print("  ⚠️  RATE LIMIT ALCANZADO")
                print(f"  Progreso guardado ({len(estado['contenido_ok'])} cursos ok).")
                print(f"  Mañana ejecuta:")
                print(f"    notebooklm login")
                print(f"    python autopilot_cursos.py")
                print("!"*58 + "\n")
                return

            if intento == 1:
                log(f"  ⚠️ Error en intento 1 — reintentando en 30s...")
                time.sleep(30)
            else:
                log(f"❌ Error persistente en {c['nombre']} — saltando")
                estado.setdefault("errores", []).append(c["nombre"])
                guardar_estado(estado)

        if rc == 0:
            # Verificar que realmente se generaron archivos
            if not curso_tiene_contenido(c):
                log(f"⚠️  {c['nombre']} terminó sin archivos — posible rate limit de informes")
                log(f"   Deteniendo para no desperdiciar cuota...")
                guardar_estado(estado)
                beep_alerta()
                print("\n" + "!"*58)
                print("  ⚠️  POSIBLE RATE LIMIT DE INFORMES")
                print(f"  El curso terminó sin generar archivos.")
                print(f"  Mañana ejecuta:")
                print(f"    notebooklm login")
                print(f"    python autopilot_cursos.py")
                print("!"*58 + "\n")
                return
            else:
                estado["contenido_ok"].append(c["url"])
                guardar_estado(estado)
                elapsed = time.time() - t_curso
                tiempos_cursos.append(elapsed)
                log(f"✅ {c['nombre']} listo en {fmt_tiempo(elapsed)}")

        time.sleep(5)

    # ── Fin ───────────────────────────────────────────────────────────
    total_tiempo = time.time() - t_inicio
    beep_ok()

    print("\n" + "="*58)
    print("  🎉 ¡TODO LISTO!")
    print(f"  Cursos creados   : {len(estado['contenido_ok'])}")
    print(f"  Slides generadas : {len(estado['slides_ok'])}")
    print(f"  Word generados   : {len(sin_word)}")
    print(f"  Errores saltados : {len(estado.get('errores', []))}")
    print(f"  Tiempo total     : {fmt_tiempo(total_tiempo)}")
    print("="*58 + "\n")

    if ESTADO_JSON.exists():
        ESTADO_JSON.unlink()

if __name__ == "__main__":
    main()
