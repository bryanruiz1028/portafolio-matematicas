"""
crear_curso_notebooklm.py
=========================
Automatiza la creación completa de un curso en NotebookLM desde una playlist de YouTube.

USO:
    # Curso completo (con presentaciones)
    python crear_curso_notebooklm.py "https://youtube.com/playlist?list=XXXX"

    # Sin presentaciones — para no gastar el rate limit de slides
    python crear_curso_notebooklm.py "https://youtube.com/playlist?list=XXXX" --skip-slides

    # Solo generar las presentaciones de un curso ya creado
    python crear_curso_notebooklm.py --solo-slides "Cursos/Álgebra/Nombre del curso"

DEPENDENCIAS:
    pip install notebooklm-py yt-dlp

QUÉ HACE:
    1. Extrae todos los videos del playlist con yt-dlp
    2. Curación automática (muestra propuesta y procede sin esperar)
    3. Crea el cuaderno en NotebookLM
    4. Agrega los videos como fuentes
    5. Genera: clases, guías, evaluaciones, planificaciones (+ presentaciones si no --skip-slides)
    6. Descarga todo a la carpeta del curso
    7. Crea el 00 - Índice del curso.md
    8. Guarda .meta.json para poder generar presentaciones después con --solo-slides
"""

import subprocess
import sys
import json
import os
import time
import re
from pathlib import Path

# Force UTF-8 for stdout, stderr AND stdin (avoids cp1252 issues on Windows)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8", errors="replace")

# ─────────────────────────────────────────────
#  CONFIGURACIÓN
# ─────────────────────────────────────────────
VAULT_PATH = Path(r"C:\Users\braya\OneDrive\Documentos\4 portafolio")
CURSOS_PATH = VAULT_PATH / "Cursos"
ENCODING_ENV = {**os.environ, "PYTHONIOENCODING": "utf-8"}

# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────

def run(cmd, capture=True):
    """Ejecuta un comando notebooklm y devuelve el JSON de salida."""
    result = subprocess.run(
        cmd, capture_output=capture, text=True,
        encoding="utf-8", errors="replace", env=ENCODING_ENV
    )
    if result.returncode != 0:
        print(f"  ❌ Error: {result.stderr[:200]}")
        return None
    if capture and result.stdout.strip():
        try:
            # The CLI sometimes prepends 'Matched: ...' lines before the JSON
            # Find the first '{' or '[' to locate the JSON portion
            txt = result.stdout.strip()
            json_start = next((i for i, c in enumerate(txt) if c in ('{', '[')), 0)
            return json.loads(txt[json_start:])
        except json.JSONDecodeError:
            return result.stdout
    return result

def nlm(*args):
    """Atajo para ejecutar notebooklm con argumentos."""
    return run(["notebooklm"] + list(args))

def wait_artifact(artifact_id, notebook_id, timeout=900):
    """Espera a que un artefacto esté completado."""
    result = run(["notebooklm", "artifact", "wait",
                  artifact_id, "--notebook", notebook_id,
                  "--timeout", str(timeout)])
    return result is not None

def sanitize_filename(name):
    """Remove/replace characters invalid in Windows filenames."""
    import re
    return re.sub(r'[\\/:*?"<>|]', '', name).strip()

def clean_surrogates(s):
    """Remove lone surrogate characters that break JSON serialization."""
    return s.encode('utf-16', 'surrogatepass').decode('utf-16', 'replace').encode('utf-8', 'replace').decode('utf-8')

def _norm(s):
    """Normaliza string: minúsculas, sin tildes, sin espacios extra."""
    import unicodedata, re
    s_clean = unicodedata.normalize("NFD", s.lower().strip()).encode("ascii", "ignore").decode()
    s_clean = re.sub(r'[\\/*?:"<>|]', ' ', s_clean)
    s_clean = re.sub(r'\s+', ' ', s_clean)
    return s_clean.strip()

def resolve_folder_name(parent: Path, name: str) -> str:
    """
    Devuelve el nombre real de una subcarpeta dentro de `parent` que coincida
    con `name` al normalizar tildes y mayúsculas. Si no existe ninguna coincidencia,
    devuelve `name` tal cual (se creará nueva).
    """
    if parent.exists():
        for child in parent.iterdir():
            if child.is_dir() and _norm(child.name) == _norm(name):
                return child.name
    return name

def separador(titulo):
    print(f"\n{'='*60}")
    print(f"  {titulo}")
    print(f"{'='*60}")

# ─────────────────────────────────────────────
#  PASO 1: EXTRAER VIDEOS CON YT-DLP
# ─────────────────────────────────────────────

def extraer_videos(playlist_url):
    separador("EXTRAYENDO VIDEOS DEL PLAYLIST")
    print(f"  URL: {playlist_url}")

    try:
        result = subprocess.run(
            ["yt-dlp", "--flat-playlist", "--print", "%(title)s|||%(id)s",
             playlist_url],
            capture_output=True, text=True, encoding="utf-8", errors="replace", env=ENCODING_ENV
        )
        if result.returncode != 0:
            print("  ❌ yt-dlp falló. Instálalo con: pip install yt-dlp")
            sys.exit(1)

        videos = []
        for i, line in enumerate(result.stdout.strip().split("\n"), 1):
            if "|||" in line:
                title, vid_id = line.split("|||", 1)
                videos.append({
                    "num": i,
                    "title": title.strip(),
                    "id": vid_id.strip(),
                    "url": f"https://www.youtube.com/watch?v={vid_id.strip()}"
                })

        print(f"\n  Encontrados {len(videos)} videos:\n")
        for v in videos:
            print(f"    {v['num']:2}. {v['title']}")

        return videos

    except FileNotFoundError:
        print("  ❌ yt-dlp no está instalado. Ejecuta: pip install yt-dlp")
        sys.exit(1)

# ─────────────────────────────────────────────
#  PASO 2: CURACIÓN (AUTOMÁTICA O DESDE ARCHIVO)
# ─────────────────────────────────────────────

OMITIR_KEYWORDS = [
    'curso completo', 'repaso', 'preuniversitar', 'suscr',
    'canal', 'bienvenid', 'presentacion', 'presentación'
]

def auto_curar_videos(videos, nombre_curso="", materia=""):
    """
    Curación automática sin input del usuario.

    Algoritmo mejorado (3 pasos):
      1. Agrupa por tema base normalizado (lowercase + antes del ' | ')
         → Evita duplicados por mayúsculas/minúsculas.
      2. Fusiona grupos adyacentes pequeños hasta alcanzar el objetivo:
         target = max(2, min(20, n_activos // 4))
         → Cursos grandes: ~4 videos/clase · Cursos pequeños: 2-3 clases.
      3. Divide grupos que excedieron 4 videos en sub-clases de 3-4.

    Bloques: 1 bloque (≤4 clases) · 2 bloques (5-9) · 3 bloques (10+).
    """
    separador("CURACIÓN AUTOMÁTICA")
    from collections import OrderedDict

    # ── Paso 1: Filtrar y agrupar por tema base normalizado ───────────
    grupos = OrderedDict()   # base_lower → [video_nums]
    bases_display = {}       # base_lower → primer título encontrado (para mostrar)
    omitidos = []
    activos = []

    for v in videos:
        titulo_lower = v['title'].lower()
        if any(kw in titulo_lower for kw in OMITIR_KEYWORDS):
            omitidos.append(v['num'])
            continue
        activos.append(v)

        # Tema base: texto antes del primer ' | ', en minúsculas (evita duplicados por case)
        raw_base = v['title'].split(' | ')[0].strip() if ' | ' in v['title'] else v['title'].strip()
        base_key = raw_base.lower()

        if base_key not in grupos:
            grupos[base_key] = []
            bases_display[base_key] = raw_base  # guardar versión con capitalización original
        grupos[base_key].append(v['num'])

    # ── Paso 2: Calcular objetivo de clases ───────────────────────────
    n_activos = len(activos)
    TARGET = max(2, min(20, n_activos // 4))
    MAX_POR_CLASE = 5   # permite fusiones 2+3 y 3+2; clases de hasta 5 videos son OK

    # ── Paso 3: Lista inicial de segmentos ────────────────────────────
    segs = [list(nums) for nums in grupos.values()]  # orden del playlist

    # ── Paso 4: Fusionar segmentos adyacentes hasta llegar al TARGET ──
    # Estrategia greedy: siempre fusionar el par adyacente cuya unión
    # sea la más pequeña y no supere MAX_POR_CLASE.
    while len(segs) > TARGET:
        mejor_i = -1
        mejor_suma = MAX_POR_CLASE + 1

        for i in range(len(segs) - 1):
            s = len(segs[i]) + len(segs[i + 1])
            if s <= MAX_POR_CLASE and s < mejor_suma:
                mejor_i = i
                mejor_suma = s

        if mejor_i == -1:
            break  # No hay más pares fusionables sin superar MAX_POR_CLASE

        segs[mejor_i] = segs[mejor_i] + segs[mejor_i + 1]
        segs.pop(mejor_i + 1)

    # ── Paso 5: Dividir segmentos que excedan MAX_POR_CLASE ──────────
    # División inteligente: distribuye uniformemente para evitar restos de 1 video
    def _split_uniforme(nums, max_size):
        n = len(nums)
        if n <= max_size:
            return [nums]
        n_chunks = (n + max_size - 1) // max_size  # ceiling
        base = n // n_chunks
        resto = n % n_chunks
        result, i = [], 0
        for c in range(n_chunks):
            size = base + (1 if c < resto else 0)
            result.append(nums[i:i + size])
            i += size
        return result

    clases_list = []
    for seg in segs:
        clases_list.extend(_split_uniforme(seg, MAX_POR_CLASE))

    # ── Paso 6: Convertir a dict {clase_num: [video_nums]} ────────────
    clases = {i + 1: nums for i, nums in enumerate(clases_list)}
    total = len(clases)

    # ── Paso 7: Generar bloques ───────────────────────────────────────
    if total <= 4:
        bloques = {1: list(clases.keys())}
    elif total <= 9:
        mitad = total // 2
        bloques = {
            1: list(range(1, mitad + 1)),
            2: list(range(mitad + 1, total + 1)),
        }
    else:  # 10+ clases → 3 bloques
        tercio = total // 3
        bloques = {
            1: list(range(1, tercio + 1)),
            2: list(range(tercio + 1, 2 * tercio + 1)),
            3: list(range(2 * tercio + 1, total + 1)),
        }

    # ── Mostrar resultado ─────────────────────────────────────────────
    print(f"\n  {n_activos} videos activos → {total} clases (objetivo era {TARGET})")
    print(f"  {len(omitidos)} omitidos | {len(bloques)} bloques\n")
    for c_num, v_nums in sorted(clases.items()):
        titulos = [videos[v - 1]['title'][:55] for v in v_nums if v <= len(videos)]
        print(f"    Clase {c_num:2} ({len(v_nums)} vid): {titulos[0][:50]}")
        for t in titulos[1:]:
            print(f"               + {t[:50]}")
    if omitidos:
        print(f"\n    Omitidos ({len(omitidos)}):")
        for vn in omitidos:
            print(f"      → {videos[vn-1]['title'][:50]}")
    for b, cs in bloques.items():
        print(f"\n    Bloque {b}: clases {cs}")
    print(f"\n  Procediendo automáticamente...")
    return nombre_curso, materia, clases, bloques, omitidos


def curar_desde_json(ruta_json, videos):
    """Carga la curación desde un archivo JSON generado por Claude."""
    data = json.loads(Path(ruta_json).read_text(encoding="utf-8"))
    nombre_curso = data.get("nombre_curso", "")
    materia      = data.get("materia", "")
    clases  = {int(k): v for k, v in data["clases"].items()}
    bloques = {int(k): v for k, v in data["bloques"].items()}
    omitidos = data.get("omitidos", [])

    separador("CURACIÓN DESDE ARCHIVO")
    print(f"  Curso: {nombre_curso} | Materia: {materia}")
    print(f"  {len(clases)} clases, {len(bloques)} bloques")
    return nombre_curso, materia, clases, bloques, omitidos

# ─────────────────────────────────────────────
#  PASO 3: CREAR CUADERNO Y AGREGAR FUENTES
# ─────────────────────────────────────────────

def crear_cuaderno_y_fuentes(nombre_curso, videos, clases, omitidos):
    separador("CREANDO CUADERNO EN NOTEBOOKLM")

    # Verificar si ya existe un cuaderno con este nombre para no duplicar
    lista = nlm("list", "--json")
    nb_id = None
    notebooks = lista.get("notebooks", []) if isinstance(lista, dict) else (lista if isinstance(lista, list) else [])
    if notebooks:
        for nb in notebooks:
            if nb.get("title", "").strip() == nombre_curso.strip():
                nb_id = nb.get("id")
                print(f"  ♻️  Cuaderno ya existe: {nombre_curso}")
                print(f"     ID: {nb_id} — reutilizando")
                break

    if not nb_id:
        data = nlm("create", nombre_curso, "--json")
        if not data:
            sys.exit(1)
        nb_id = data["notebook"]["id"]
        print(f"  ✅ Cuaderno creado: {nombre_curso}")
        print(f"     ID: {nb_id}")

    # Solo agregar videos que están en alguna clase
    usados = set()
    for vids in clases.values():
        usados.update(vids)

    source_map = {}
    # Si el cuaderno ya existía, intentar cargar source_map desde .meta.json
    _mat = _detectar_materia(nombre_curso)
    _nom = resolve_folder_name(CURSOS_PATH / _mat, sanitize_filename(nombre_curso)) if _mat else sanitize_filename(nombre_curso)
    meta_path = CURSOS_PATH / _mat / _nom / ".meta.json"
    if meta_path.exists():
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            if meta.get("nb_id") == nb_id and meta.get("source_map"):
                source_map = {int(k): v for k, v in meta["source_map"].items()}
                print(f"  ♻️  source_map cargado desde .meta.json ({len(source_map)} fuentes)")
        except Exception:
            pass

    # Verificar si nos faltan videos en source_map
    faltantes = usados - set(source_map.keys())
    if not faltantes:
        print(f"  ✅ Todas las fuentes ({len(usados)}) ya están en el source_map")
        return nb_id, source_map

    print(f"  ⚠️  Faltan {len(faltantes)} fuentes por agregar al source_map...")

    separador("AGREGANDO VIDEOS COMO FUENTES")

    # Agregar videos faltantes
    for v in videos:
        if v["num"] in faltantes:
            safe_title = clean_surrogates(v['title'])
            print(f"  Agregando video {v['num']}: {safe_title[:50]}...")
            result = nlm("source", "add", "--notebook", nb_id, v["url"], "--json")
            if result and "source" in result:
                source_map[v["num"]] = result["source"]["id"]
                print(f"  ✅ Source ID: {result['source']['id'][:8]}...")
            time.sleep(1)

    # Esperar a que todas las fuentes estén listas
    print("\n  Esperando que las fuentes se procesen...")
    time.sleep(20)
    sources = nlm("source", "list", "--notebook", nb_id, "--json")
    if sources:
        ready = sum(1 for s in sources["sources"] if s["status"] == "ready")
        print(f"  ✅ {ready}/{len(sources['sources'])} fuentes listas")

    return nb_id, source_map


def _detectar_materia(nombre_curso):
    """Busca en CURSOS_PATH qué subcarpeta contiene el curso (comparación sin tildes)."""
    if CURSOS_PATH.exists():
        for mat in CURSOS_PATH.iterdir():
            if not mat.is_dir():
                continue
            for child in mat.iterdir():
                if child.is_dir() and _norm(child.name) == _norm(nombre_curso):
                    return mat.name
    return ""

# ─────────────────────────────────────────────
#  PASO 4: GENERAR TODOS LOS MATERIALES
# ─────────────────────────────────────────────

PROMPT_CLASE = """Genera la Clase {num} completa en español sobre {tema}.
IMPORTANTE: Todo el contenido DEBE estar en español. Si el tema está en inglés, tradúcelo al español en el título principal.
Usa EXACTAMENTE el formato Obsidian/Admonition del portafolio docente:

# Clase {num:02d} — [TÍTULO EN ESPAÑOL del tema]
tags: #algebra #{tag}
Curso: [[00 - Índice del curso]] | Bloque {bloque} | Lección {num} de {total}

> [!info] 🧭 Navegación
> {nav_prev}[[00 - Índice del curso|Índice]] | **Clase {num:02d}** | {nav_next}

## ¿Por qué es importante esta clase?
> [!info] 🌍 Relevancia y aplicaciones
> [2-3 líneas de aplicaciones reales]
- 💵 [aplicación con $USD]
- 🏗️ [aplicación práctica]
- 📊 [situación cotidiana]

## Concepto clave
> [!note] 📌 ¿Qué es {tema_corto}?
> [definición simple para estudiantes de 12 años]
> [!warning] ⚠️ Error común
> ❌ Incorrecto: [...] | ✅ Correcto: [...]
> [!tip] 💡 Truco para recordarlo
> [regla mnemotécnica]

## Procedimiento paso a paso
```
PASO 1 → [acción]
PASO 2 → [acción]
PASO 3 → [acción]
PASO 4 → [acción]
```

```ad-example
title: Ejemplo 1 — [caso básico]
[enunciado] → Paso 1: [...] Paso 2: [...] ✅ Resultado: [...]
```
```ad-example
title: Ejemplo 2 — [caso con signos]
[enunciado] → Pasos → ✅ Resultado → ⚠️ Nota: [error a evitar]
```
```ad-example
title: Ejemplo 3 — [caso avanzado]
[enunciado] → Pasos → ✅ Resultado
```
```ad-example
title: Ejemplo 4 — Aplicación real con $USD
[problema con precios en dólares] → Pasos → ✅ Resultado
```

## Ejercicios para el estudiante
```ad-abstract
title: 🟢 Fácil — [subtítulo]
1. [...] 2. [...] 3. [...] 4. [...]
```
```ad-abstract
title: 🟡 Medio — [subtítulo]
1. [...] 2. [...] 3. [...] 4. [...]
```
```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
1. [...] 2. [...] 3. [...] 4. [...]
```
```ad-success
title: ✅ Respuestas (para el docente)
🟢 Fácil: 1.[R] 2.[R] 3.[R] 4.[R]
🟡 Medio: 1.[R] 2.[R] 3.[R] 4.[R]
🔴 Avanzado: 1.[R] 2.[R] 3.[R] 4.[R]
```

## Mini-prueba de autoevaluación
```ad-question
title: 🧪 Pregunta 1
[pregunta conceptual] a) [...] b) [...] c) [...] d) [...]
✅ Respuesta: [letra] — [explicación]
```
```ad-question
title: 🧪 Pregunta 2
[pregunta procedimental] a/b/c/d → ✅ Respuesta: [letra]
```
```ad-question
title: 🧪 Pregunta 3
[aplicación $USD] a/b/c/d → ✅ Respuesta: [letra]
```

## Notas para el próximo tema
> [!tip] 💡 En la próxima clase
> [conexión con la siguiente clase]

> [!info] 🧭 Navegación
> {nav_prev}[[00 - Índice del curso|Índice]] | **Clase {num:02d}** | {nav_next}"""

PROMPT_GUIA = """Genera la Guía de estudio de la Clase {num} sobre {tema_corto} para estudiantes de Básica Superior.
Lenguaje simple y claro, en español. Usa formato Obsidian/Admonition.
IMPORTANTE: El título principal DEBE estar en español. Si el tema está en inglés, tradúcelo.

# 📖 Guía de estudio — Clase {num:02d}: [TÍTULO EN ESPAÑOL]

> [!info] 📌 Conceptos clave
> [resumen de los conceptos más importantes de la clase en 3-5 puntos]

## Fórmulas y definiciones importantes
| Término | Definición / Fórmula |
|---------|----------------------|
| [término 1] | [definición o fórmula] |
| [término 2] | [definición o fórmula] |
| [término 3] | [definición o fórmula] |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — [caso básico]
[enunciado] → Paso 1: [...] Paso 2: [...] ✅ Resultado: [...]
```
```ad-example
title: Ejemplo B — [caso con aplicación real $USD]
[enunciado con contexto cotidiano] → Pasos → ✅ Resultado
```

## Ejercicios de repaso
```ad-abstract
title: 🟢 Fácil
1. [...] 2. [...] 3. [...]
```
```ad-abstract
title: 🟡 Medio
1. [...] 2. [...] 3. [...]
```
```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
1. [...] 2. [...] 3. [...]
```

> [!tip] 💡 Consejo de estudio
> [estrategia práctica para dominar este tema]"""

def _calcular_n_slides(n_videos):
    """Calcula el número de diapositivas según cuántos videos cubre la clase."""
    # 1 video → 9 slides · 2 → 11 · 3 → 13 · 4 → 14 · 5+ → 15
    return min(15, 7 + n_videos * 2)


def _prompt_presentacion(num, tema, n_videos):
    n_slides  = _calcular_n_slides(n_videos)
    # Ejemplos resueltos disponibles (descontando 8 slides fijas: 5 apertura + 3 cierre)
    slides_ejemplos = n_slides - 8
    n_ejemplos = max(1, slides_ejemplos // 2)   # cada ejemplo ocupa ~2 slides
    include_usd = n_videos >= 3                 # ejemplo con $USD solo si hay ≥3 videos

    ejemplos_texto = f"{n_ejemplos} ejemplo(s) resuelto(s) paso a paso (una diapositiva por paso)"
    if include_usd:
        ejemplos_texto += "\n  + 1 ejemplo adicional con contexto de dinero ($USD)"

    return f"""Crea una presentación de clase para PROYECTOR sobre: {tema}
Nivel: Básica Superior (12-15 años) | Idioma: español | Clase {num:02d}
TOTAL DE DIAPOSITIVAS: exactamente {n_slides} (la clase cubre {n_videos} video(s))

REGLAS GENERALES (aplican en todas las diapositivas):
- Máximo 5 líneas de texto por diapositiva — una sola idea por slide
- Texto grande y legible desde el fondo del aula
- Fondo oscuro + texto claro (alto contraste para proyector)
- Sin efectos sutiles, sin gradientes — todo sólido y visible
- Las ecuaciones son el elemento visual principal: grandes, centradas, destacadas

ESTRUCTURA OBLIGATORIA — exactamente en este orden:

SLIDE 1 — PORTADA
  Título: {tema} | Subtítulo: "Matemáticas | Básica Superior"

SLIDE 2 — ¿POR QUÉ LO APRENDEMOS?
  2-3 ejemplos cotidianos (uno con precios en $USD) · Frase motivadora

SLIDE 3 — CONCEPTO CLAVE
  Definición en UNA oración simple (lenguaje de 12 años) · Sin fórmulas todavía

SLIDE 4 — LA REGLA / FÓRMULA
  Solo la fórmula principal, grande y centrada · Etiqueta cada parte

SLIDE 5 — ERROR FRECUENTE
  ❌ Lo incorrecto | ✅ Lo correcto · Explicación en 1 línea

SLIDES 6 a {n_slides - 3} — EJEMPLOS RESUELTOS
  {ejemplos_texto}
  Último slide de cada ejemplo: resultado final + verificación

SLIDE {n_slides - 2} — ¡TU TURNO!
  1 ejercicio fácil (🟢) · Espacio visual de "hoja en blanco" · SIN mostrar respuesta

SLIDE {n_slides - 1} — RESPUESTA Y CIERRE
  Solución del ejercicio · "Lo que aprendimos hoy" en 3 bullets
  Frase: "En la próxima clase: [tema siguiente relacionado]"

SLIDE {n_slides} — RESUMEN VISUAL
  Esquema o mapa con los conceptos clave · Solo palabras clave con flechas"""

PROMPT_EVALUACION = """Genera una EVALUACIÓN FORMATIVA en español sobre {tema_bloque}.
Produce DOS DOCUMENTOS SEPARADOS en este orden exacto:

═══════════════════════════════════════════════
DOCUMENTO 1 — VERSIÓN ESTUDIANTE
═══════════════════════════════════════════════

# EVALUACIÓN FORMATIVA: {tema_bloque}

Nombre: _________________________________ Curso: _____________ Fecha: ___________

Puntaje: _____ / 10 puntos

---

ESTRUCTURA OBLIGATORIA — 10 preguntas / 10 puntos (1pt cada una):

SECCIÓN I — Selección múltiple Q1-Q3 (3pts): 4 opciones a/b/c/d. Espacio "Respuesta: ___" tras cada pregunta.
SECCIÓN II — Verdadero o Falso Q4-Q5 (2pts): escribir V o F. Espacio "Respuesta: ___" tras cada pregunta.
SECCIÓN III — Completar espacios Q6-Q7 (2pts): mínimo 3 blancos en la MISMA oración. Banco de palabras a/b/c/d/e debajo.
SECCIÓN IV — Relacionar columnas Q8 (1pt): tabla Markdown 4 filas con columna R vacía para que el estudiante escriba. Nota: 4/4=1pt | 2-3/4=0.5pt | 0-1/4=0pt.
SECCIÓN V — Resolver ejercicio Q9 (1pt): UN SOLO ejercicio nivel 🟢 Fácil. Espacio para procedimiento y resultado.
SECCIÓN VI — Aplicación con $USD Q10 (1pt): problema cotidiano con dinero. Espacio para expresión matemática, procedimiento y resultado.

NO incluir respuestas en este documento. Solo preguntas y espacios en blanco.

═══════════════════════════════════════════════
DOCUMENTO 2 — RESPUESTAS Y MATERIAL DOCENTE
═══════════════════════════════════════════════

# RESPUESTAS DOCENTE: {tema_bloque}

Incluir:
- Respuestas completas Q1 a Q10 con justificación breve
- Procedimiento resuelto de Q9 y Q10
- Rúbrica: tabla con niveles Logrado / En proceso / Por lograr por sección
- Escala: 10=100% Excelente | 8-9=Muy bueno | 6-7=Satisfactorio | 4-5=En proceso | <4=Necesita refuerzo
- Sección "Observaciones del docente" con campos: error más frecuente, sección con menor rendimiento, fecha de aplicación."""

PROMPT_PLANIFICACION = """Actúa como un profesor experto en {materia}.
Voy a impartir una clase sobre el tema: {tema_bloque}

Los recursos disponibles en el aula son: pizarra, marcadores, fichas e impresora.
Agrega UN recurso adicional que sea fácil de conseguir para el docente o el estudiante.

Genera el documento EXACTAMENTE en este formato Obsidian con admonitions:

# 📋 Planificación Didáctica — {tema_bloque}

tags: #planificacion #dua #{tag}
Nivel: Básica Superior (12–15 años) | Duración: 80 minutos

---

## 1. Tema
{tema_bloque}

---

## 2. Metodología
[Aprendizaje colaborativo formal: describe en 2–3 líneas el enfoque específico para este tema y cómo se organiza el aula]

---

## 3. Secuencia Didáctica

### 🔵 ANTICIPACIÓN — 20 min

> [!abstract] Actividad de inicio
> [Actividad motivadora o contextual: juego, reto, situación problema, pregunta detonadora, etc. Describe el qué y el cómo. Incluye el cuándo solo si es relevante para la actividad.]

> [!note] Enfoque DUA
> - **Qué:** [qué aprenderán o activarán]
> - **Cómo:** [de qué manera se realiza — individual, parejas, grupo]
> - **Por qué:** [incluir solo si la actividad lo requiere]

---

### 🟡 CONSTRUCCIÓN — 40 min

> [!example] Actividades centrales
> [Actividades donde los estudiantes aplican, experimentan o resuelven con acompañamiento docente. Describe el qué, el cómo. Incluye el cuándo solo si la actividad lo requiere.]

> [!note] Enfoque DUA
> - **Qué:** [qué hacen o construyen los estudiantes]
> - **Cómo:** [individual, parejas o grupos — con qué recursos]
> - **Por qué:** [incluir solo si la actividad lo requiere]

---

### 🟢 CONSOLIDACIÓN — 20 min

> [!success] Actividad de cierre
> [Reto final, reflexión, socialización o producto. Describe el qué y el cómo. Incluye el cuándo solo si aplica.]

> [!note] Enfoque DUA
> - **Qué:** [producto o resultado esperado]
> - **Cómo:** [cómo se evalúa, socializa o presenta]
> - **Por qué:** [incluir solo si aplica]

---

## 4. Recursos

| Recurso | Tipo | Uso en la clase |
|---------|------|----------------|
| Pizarra | Físico | [uso específico en este tema] |
| Marcadores | Físico | [uso específico en este tema] |
| Fichas | Impreso | [uso específico en este tema] |
| Impresora | Físico | [uso específico en este tema] |
| [recurso adicional sugerido] | [Físico/Digital] | [uso específico] |"""

def generar_materiales(nb_id, source_map, clases, bloques, videos, materia="Matemáticas", skip_slides=False, carpeta=None):
    separador("GENERANDO MATERIALES")
    total_clases = len(clases)
    task_ids = {}

    def _existe(patron_glob):
        """Devuelve True si ya hay al menos un archivo que coincida con el glob en carpeta."""
        if carpeta is None:
            return False
        matches = list(carpeta.glob(patron_glob))
        return len(matches) > 0

    # Calcular qué bloque pertenece cada clase
    clase_a_bloque = {}
    for b_num, clase_ids in bloques.items():
        for c_id in clase_ids:
            clase_a_bloque[c_id] = b_num

    for clase_num, video_nums in sorted(clases.items()):
        sources_clase = [source_map[v] for v in video_nums if v in source_map]
        if not sources_clase:
            continue

        video_titulos = [clean_surrogates(videos[v-1]["title"]) for v in video_nums if v <= len(videos)]
        tema = " + ".join(video_titulos)
        tema_corto = video_titulos[0].split("|")[0].strip() if video_titulos else tema
        tag = re.sub(r'[^a-zA-Z]', '', tema_corto.lower().replace(" ", ""))
        bloque_num = clase_a_bloque.get(clase_num, 1)

        nav_prev = f"[[Clase {clase_num-1:02d}|⬅ Clase {clase_num-1:02d}]] | " if clase_num > 1 else ""
        nav_next = f"| [[Clase {clase_num+1:02d}|Clase {clase_num+1:02d} ➡]]" if clase_num < total_clases else "| 📋 [[00 - Índice del curso|Fin del curso ➡]]"

        prompt = PROMPT_CLASE.format(
            num=clase_num, tema=tema, tema_corto=tema_corto,
            tag=tag[:15], bloque=bloque_num, total=total_clases,
            nav_prev=nav_prev, nav_next=nav_next
        )

        src_args = []
        for sid in sources_clase:
            src_args += ["-s", sid]

        # Clase y Guía en llamadas separadas
        if _existe(f"Clase {clase_num:02d} - *.md"):
            print(f"\n  ⏭️  Clase {clase_num:02d} ya existe, omitiendo...")
        else:
            print(f"\n  📝 Generando Clase {clase_num:02d}...")
            r_clase = nlm("generate", "report", "--format", "custom", "--language", "es",
                          "--notebook", nb_id, *src_args, prompt, "--json")
            if r_clase:
                task_ids[f"clase_{clase_num:02d}"] = {
                    "task_id": r_clase["task_id"], "sources": sources_clase,
                    "tema": tema, "tema_corto": tema_corto, "clase_num": clase_num
                }

        prompt_guia = PROMPT_GUIA.format(num=clase_num, tema_corto=tema_corto)
        if _existe(f"* Guía de estudio - Clase {clase_num:02d}*"):
            print(f"  ⏭️  Guía Clase {clase_num:02d} ya existe, omitiendo...")
        else:
            print(f"  📖 Generando Guía Clase {clase_num:02d}...")
            r_guia = nlm("generate", "report", "--format", "custom", "--language", "es",
                         "--notebook", nb_id, *src_args, prompt_guia, "--json")
            if r_guia:
                task_ids[f"guia_{clase_num:02d}"] = {
                    "task_id": r_guia["task_id"], "sources": sources_clase,
                    "tema": tema_corto, "clase_num": clase_num
                }

    # Presentaciones: 1 por cada 2 clases (ahorra 50% de llamadas slide-deck)
    if not skip_slides:
        clases_lista = sorted(clases.items())
        for i in range(0, len(clases_lista), 2):
            par = clases_lista[i:i+2]
            clase_ini = par[0][0]
            clase_fin = par[-1][0]

            label = f"Clases {clase_ini:02d}-{clase_fin:02d}" if clase_ini != clase_fin else f"Clase {clase_ini:02d}"
            if _existe(f"* Presentación - {label}*.pdf"):
                print(f"  ⏭️  Presentación {label} ya existe, omitiendo...")
                continue

            # Reunir todos los videos y fuentes del par
            all_vid_nums = [v for _, vids in par for v in vids]
            sources_par  = [source_map[v] for v in all_vid_nums if v in source_map]
            src_args_par = []
            for sid in sources_par:
                src_args_par += ["-s", sid]

            # Tema combinado (primer título de cada clase)
            temas_par = []
            for cn, vids in par:
                titulos = [clean_surrogates(videos[v-1]["title"]) for v in vids if v <= len(videos)]
                temas_par.append(titulos[0].split("|")[0].strip() if titulos else f"Clase {cn}")
            tema_par = " + ".join(temas_par)

            n_vid_total = len(all_vid_nums)
            print(f"  📊 Generando Presentación {label} ({n_vid_total} videos → {_calcular_n_slides(n_vid_total)} slides)...")
            prompt_pres = _prompt_presentacion(clase_ini, tema_par, n_vid_total)
            r = nlm("generate", "slide-deck", "--language", "es",
                    "--notebook", nb_id, *src_args_par, prompt_pres, "--json")
            if r:
                task_ids[f"pres_{clase_ini:02d}_{clase_fin:02d}"] = {
                    "task_id": r["task_id"],
                    "tema": tema_par,
                    "clase_ini": clase_ini,
                    "clase_fin": clase_fin,
                }
    else:
        print("  ⏭️  Presentaciones omitidas (--skip-slides)")

    # Evaluaciones por bloque
    for bloque_num, clase_ids in sorted(bloques.items()):
        sources_bloque = []
        temas_bloque = []
        for c_id in clase_ids:
            for v in clases.get(c_id, []):
                if v in source_map:
                    sources_bloque.append(source_map[v])
            if c_id <= len(videos):
                temas_bloque.append(videos[c_id-1]["title"].split("|")[0].strip())

        if not sources_bloque:
            continue

        src_args = []
        for sid in sources_bloque:
            src_args += ["-s", sid]

        tema_bloque = " y ".join(temas_bloque[:2])
        tag_plan = re.sub(r'[^a-zA-Z]', '', tema_bloque.lower().replace(" ", ""))[:15]

        if _existe(f"* Evaluación - Bloque {bloque_num}*"):
            print(f"\n  ⏭️  Evaluación Bloque {bloque_num} ya existe, omitiendo...")
        else:
            print(f"\n  📝 Generando Evaluación Bloque {bloque_num}...")
            prompt_eval = PROMPT_EVALUACION.format(tema_bloque=tema_bloque)
            r = nlm("generate", "report", "--format", "custom", "--language", "es",
                    "--notebook", nb_id, *src_args, prompt_eval, "--json")
            if r:
                task_ids[f"eval_bloque_{bloque_num}"] = {
                    "task_id": r["task_id"], "bloque_num": bloque_num,
                    "tema": tema_bloque
                }

        if _existe(f"* Planificación - Bloque {bloque_num}*"):
            print(f"\n  ⏭️  Planificación Bloque {bloque_num} ya existe, omitiendo...")
        else:
            print(f"\n  📋 Generando Planificación Bloque {bloque_num}...")
            prompt_plan = PROMPT_PLANIFICACION.format(
                materia=materia, tema_bloque=tema_bloque, tag=tag_plan
            )
            r = nlm("generate", "report", "--format", "custom", "--language", "es",
                    "--notebook", nb_id, *src_args, prompt_plan, "--json")
            if r:
                task_ids[f"plan_bloque_{bloque_num}"] = {
                    "task_id": r["task_id"], "bloque_num": bloque_num,
                    "tema": tema_bloque
                }

    return task_ids

# ─────────────────────────────────────────────
#  PASO 5: ESPERAR Y DESCARGAR
# ─────────────────────────────────────────────

def _extraer_titulo_es(ruta_md, clase_num):
    """
    Lee el archivo .md descargado y extrae el título español del primer
    encabezado '# Clase XX — Título' o '# Título'.
    Si no encuentra nada, devuelve un fallback vacío para que el llamador
    use el título del video.
    """
    if not ruta_md.exists():
        return ""
    try:
        for linea in ruta_md.read_text(encoding="utf-8").splitlines():
            linea = linea.strip()
            if linea.startswith("#") and not linea.startswith("##"):
                # Quitar el/los '#' iniciales
                titulo = linea.lstrip("#").strip()
                # Quitar prefijo "Clase XX —" o "Clase XX:" si está
                titulo = re.sub(r'^[Cc]lase\s+\d+\s*[—\-:]+\s*', '', titulo).strip()
                if titulo:
                    return titulo
    except Exception:
        pass
    return ""


def esperar_y_descargar(nb_id, task_ids, nombre_curso, materia):
    separador("ESPERANDO ARTEFACTOS")

    materia_real = resolve_folder_name(CURSOS_PATH, materia)
    nombre_real  = resolve_folder_name(CURSOS_PATH / materia_real, sanitize_filename(nombre_curso))
    carpeta = CURSOS_PATH / materia_real / nombre_real
    carpeta.mkdir(parents=True, exist_ok=True)
    print(f"  Carpeta de destino: {carpeta}\n")

    for key, info in task_ids.items():
        task_id = info["task_id"]
        print(f"  ⏳ Esperando {key}...")
        ok = wait_artifact(task_id, nb_id)

        if not ok:
            print(f"  ❌ Falló: {key}")
            continue

        if key.startswith("clase_"):
            n = info["clase_num"]
            # Descargar a nombre temporal y extraer título español del contenido
            ruta_tmp = carpeta / f"_clase_tmp_{n:02d}.md"
            nlm("download", "report", str(ruta_tmp), "-a", task_id, "--notebook", nb_id)
            titulo_es = _extraer_titulo_es(ruta_tmp, n)
            nombre_archivo = f"Clase {n:02d} - {sanitize_filename(titulo_es[:60])}.md"
            ruta = carpeta / nombre_archivo
            if ruta_tmp.exists():
                ruta_tmp.replace(ruta)
            print(f"  ✅ {nombre_archivo}")

        elif key.startswith("pres_"):
            ini = info["clase_ini"]
            fin = info["clase_fin"]
            label = f"Clases {ini:02d}-{fin:02d}" if ini != fin else f"Clase {ini:02d}"
            nombre_archivo = f"📊 Presentación - {label} — {sanitize_filename(info['tema'][:45])}.pdf"
            ruta = carpeta / nombre_archivo
            nlm("download", "slide-deck", str(ruta), "-a", task_id, "--notebook", nb_id)
            print(f"  ✅ {nombre_archivo}")

        elif key.startswith("guia_"):
            n = info["clase_num"]
            # Descargar a nombre temporal y extraer título español del contenido
            ruta_tmp = carpeta / f"_guia_tmp_{n:02d}.md"
            nlm("download", "report", str(ruta_tmp), "-a", task_id, "--notebook", nb_id)
            titulo_es = _extraer_titulo_es(ruta_tmp, n)
            nombre_archivo = f"📖 Guía de estudio - Clase {n:02d} — {sanitize_filename(titulo_es[:50])}.md"
            ruta = carpeta / nombre_archivo
            if ruta_tmp.exists():
                ruta_tmp.replace(ruta)
            print(f"  ✅ {nombre_archivo}")

        elif key.startswith("eval_bloque_"):
            b = info["bloque_num"]
            tema_eval = sanitize_filename(info["tema"][:50])
            # Descargar archivo temporal
            ruta_tmp = carpeta / f"_eval_tmp_bloque{b}.md"
            nlm("download", "report", str(ruta_tmp), "-a", task_id, "--notebook", nb_id)

            # Dividir en 2 documentos separados
            if ruta_tmp.exists():
                contenido = ruta_tmp.read_text(encoding="utf-8")

                # Intentar múltiples separadores posibles (NotebookLM puede variar el formato)
                separadores = [
                    "DOCUMENTO 2 — RESPUESTAS Y MATERIAL DOCENTE",
                    "# RESPUESTAS DOCENTE:",
                    "RESPUESTAS DOCENTE:",
                ]
                sep_encontrado = None
                for sep in separadores:
                    if sep in contenido:
                        sep_encontrado = sep
                        break

                if sep_encontrado:
                    partes = contenido.split(sep_encontrado, 1)
                    # Documento estudiante (limpio para imprimir)
                    archivo_estudiante = f"📝 Evaluación - Bloque {b} — {tema_eval}.md"
                    contenido_estudiante = partes[0].strip().rstrip("*").rstrip("-").strip()
                    (carpeta / archivo_estudiante).write_text(
                        contenido_estudiante, encoding="utf-8"
                    )
                    # Documento docente (respuestas + rúbrica)
                    archivo_docente = f"📋 Respuestas Docente - Bloque {b} — {tema_eval}.md"
                    encabezado_docente = f"# RESPUESTAS DOCENTE: {tema_eval}\n\n> [!warning] ⚠️ Solo para uso del docente — No distribuir a estudiantes\n\n"
                    (carpeta / archivo_docente).write_text(
                        encabezado_docente + partes[1].strip(), encoding="utf-8"
                    )
                    ruta_tmp.unlink()  # borrar temporal
                    print(f"  ✅ {archivo_estudiante}")
                    print(f"  ✅ {archivo_docente}")
                else:
                    # Si no encontró separador, guardar como archivo único
                    nombre_archivo = f"📝 Evaluación - Bloque {b} — {tema_eval}.md"
                    ruta_tmp.replace(carpeta / nombre_archivo)
                    print(f"  ✅ {nombre_archivo} (sin separar — revisar manualmente)")

        elif key.startswith("plan_bloque_"):
            b = info["bloque_num"]
            tema_plan = sanitize_filename(info["tema"][:50])
            nombre_archivo = f"📋 Planificación - Bloque {b} — {tema_plan}.md"
            ruta = carpeta / nombre_archivo
            nlm("download", "report", str(ruta), "-a", task_id, "--notebook", nb_id)
            print(f"  ✅ {nombre_archivo}")

    return carpeta

# ─────────────────────────────────────────────
#  GUARDAR / CARGAR METADATOS DEL CURSO
# ─────────────────────────────────────────────

def guardar_meta(carpeta, nb_id, source_map, clases, bloques, videos, nombre_curso, materia, playlist_url=""):
    """Guarda los metadatos del curso para poder generar slides después."""
    meta = {
        "nb_id": nb_id,
        "nombre_curso": nombre_curso,
        "materia": materia,
        "playlist_url": playlist_url,
        "source_map": {str(k): v for k, v in source_map.items()},
        "clases": {str(k): v for k, v in clases.items()},
        "bloques": {str(k): v for k, v in bloques.items()},
        "videos": videos,
    }
    meta_path = carpeta / ".meta.json"
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  ✅ Metadatos guardados: .meta.json")

def cargar_meta(carpeta):
    """Carga los metadatos guardados del curso."""
    meta_path = Path(carpeta) / ".meta.json"
    if not meta_path.exists():
        print(f"  ❌ No se encontró .meta.json en {carpeta}")
        print(f"     Este archivo se crea automáticamente al crear el curso con --skip-slides.")
        sys.exit(1)
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    # Restaurar claves enteras
    meta["source_map"] = {int(k): v for k, v in meta["source_map"].items()}
    meta["clases"]     = {int(k): v for k, v in meta["clases"].items()}
    meta["bloques"]    = {int(k): v for k, v in meta["bloques"].items()}
    return meta

# ─────────────────────────────────────────────
#  DETECCIÓN AUTOMÁTICA EN MAPA DE CURSOS
# ─────────────────────────────────────────────

# Orden importa: "Geometría Analítica" ANTES de "Geometría"
_SECCIONES_MAPA = [
    ("## Geometría Analítica", "Geometría Analítica"),
    ("## Aritmética",          "Aritmética"),
    ("## Álgebra",             "Álgebra"),
    ("## Geometría",           "Geometría"),
    ("## Trigonometría",       "Trigonometría"),
    ("## Estadística",         "Estadística"),
    ("## Repaso",              "Repaso"),
]
_TOTALES_MAPA = {
    "Aritmética": 6, "Álgebra": 8, "Geometría": 5,
    "Geometría Analítica": 3, "Trigonometría": 3, "Estadística": 3,
}

def detectar_curso_desde_url(playlist_url):
    """
    Busca en 00 - Mapa de cursos.md si el URL corresponde a un curso conocido.
    Devuelve (nombre_curso, materia) o ("", "") si no lo encuentra.
    Maneja tanto nombres plain text como wikilinks [[path\\|display]].
    """
    mapa_path = CURSOS_PATH / "00 - Mapa de cursos.md"
    if not mapa_path.exists():
        return "", ""

    mat_actual = ""
    for line in mapa_path.read_text(encoding="utf-8").split("\n"):
        for header, mat in _SECCIONES_MAPA:
            if line.startswith(header):
                mat_actual = mat
                break
        if playlist_url in line and "|" in line:
            # Buscar en la línea COMPLETA para no romper wikilinks
            # Caso 1: wikilink con display name — [[path\|DisplayName]]
            m = re.search(r'\\\|([^|\\^\]]+)\]\]', line)
            if m:
                return m.group(1).strip(), mat_actual
            # Caso 2: nombre plain text — split por | y tomar columna 2
            cols = [c.strip() for c in line.split("|")]
            if len(cols) >= 3:
                nombre = cols[2].strip()
                nombre = nombre.rstrip("\\").strip()
                if nombre and not nombre.startswith("*") and "[[" not in nombre:
                    return nombre, mat_actual
    return "", ""


def actualizar_mapa_cursos(nombre_curso, materia, carpeta, playlist_url="", skip_slides=False):
    """
    Al terminar un curso, actualiza 00 - Mapa de cursos.md:
    - Agrega wikilink al nombre del curso
    - Registra el inventario de materiales generados en la columna Estado
    - Recalcula las estadísticas del proyecto
    """
    mapa_path = CURSOS_PATH / "00 - Mapa de cursos.md"
    if not mapa_path.exists():
        print("  ⚠️ No se encontró 00 - Mapa de cursos.md — actualizar manualmente.")
        return

    separador("ACTUALIZANDO MAPA DE CURSOS")

    # ── 1. Contar materiales generados en la carpeta ──────────────────
    clases_n = len(list(carpeta.glob("Clase *.md")))
    guias_n  = len([f for f in carpeta.iterdir()
                    if "Gu" in f.name and "estudio" in f.name.lower()])
    evals_n  = len([f for f in carpeta.iterdir()
                    if "Evaluaci" in f.name and "Respuestas" not in f.name])
    plans_n  = len([f for f in carpeta.iterdir() if "Planificaci" in f.name])
    slides_n = len(list(carpeta.glob("*.pdf")))

    partes = []
    if clases_n > 0: partes.append(f"✅ {clases_n} clases")
    if guias_n  > 0: partes.append(f"✅ {guias_n} guías")
    if evals_n  > 0: partes.append(f"✅ {evals_n} eval.")
    if plans_n  > 0: partes.append(f"✅ {plans_n} plan.")
    if slides_n > 0:
        partes.append(f"✅ {slides_n} slides")
    elif skip_slides:
        partes.append("⏳ slides pendientes")

    tiene_base = clases_n > 0 and guias_n > 0 and evals_n > 0 and plans_n > 0
    if tiene_base and slides_n > 0:
        icono = "✅ Completado"
    elif tiene_base:
        icono = "⚠️ Sin slides"
    elif clases_n > 0:
        icono = "🔄 Parcial"
    else:
        icono = "❌ Error"

    estado_celda = icono + " · " + " · ".join(partes) if partes else icono
    wikilink = f"[[Cursos/{materia}/{nombre_curso}/00 - Índice del curso\\|{nombre_curso}]]"

    # ── 2. Editar el archivo línea por línea ──────────────────────────
    lines = mapa_path.read_text(encoding="utf-8").split("\n")
    nuevo = []
    actualizado = False
    mat_actual = ""

    for line in lines:
        for header, mat in _SECCIONES_MAPA:
            if line.startswith(header):
                mat_actual = mat
                break

        # Buscar la fila SOLO dentro de la sección de materia correcta,
        # tanto por URL como por nombre (en formato wikilink o texto plano)
        en_seccion_correcta = (mat_actual == materia)
        nombre_en_linea = (
            nombre_curso in line and "|" in line
        )
        es_fila = (
            not actualizado
            and en_seccion_correcta
            and nombre_en_linea
            and (
                (playlist_url and playlist_url in line)
                or f"|{nombre_curso}]]" in line
                or f"| {nombre_curso} |" in line
                or f"| {nombre_curso}]]" in line
            )
        )

        if es_fila:
            # Reemplazar Estado (última celda: | contenido | al final de línea)
            line = re.sub(
                r'\|[^|]*\|\s*$',
                f'| {estado_celda} |',
                line.rstrip()
            )
            # Añadir wikilink al nombre si aún no lo tiene
            if '[[' not in line:
                line = re.sub(
                    r'^(\|\s*\d+\s*\|\s*)([^|[\n]+?)(\s*\|)',
                    rf'\1{wikilink}\3',
                    line
                )
            actualizado = True

        nuevo.append(line)

    # ── 3. Recalcular estadísticas ────────────────────────────────────
    if actualizado:
        conteos = {k: 0 for k in _TOTALES_MAPA}
        mat_cur = ""
        for line in nuevo:
            for header, mat in _SECCIONES_MAPA:
                if line.startswith(header):
                    mat_cur = mat
                    break
            if mat_cur in conteos and "|" in line:
                cols = [c.strip() for c in line.split("|")]
                if len(cols) >= 2 and cols[1].isdigit():
                    ultima = cols[-1] or cols[-2]
                    if any(e in ultima for e in ("✅", "⚠️", "🔄")):
                        conteos[mat_cur] += 1

        total_comp = sum(conteos.values())

        for i, line in enumerate(nuevo):
            if "Cursos completados (con carpeta local)" in line:
                nuevo[i] = re.sub(r'\*\*\d+ / \d+\*\*', f'**{total_comp} / 28**', line)
            for mat, tot in _TOTALES_MAPA.items():
                if f"{mat} completada" in line:
                    nuevo[i] = re.sub(
                        r'\d+ / \d+ cursos', f'{conteos[mat]} / {tot} cursos', line
                    )

        mapa_path.write_text("\n".join(nuevo), encoding="utf-8")
        print(f"  ✅ Mapa actualizado: {nombre_curso}")
        print(f"     Estado: {icono}")
        if partes:
            print(f"     {' | '.join(partes)}")
    else:
        print(f"  ⚠️ No se encontró '{nombre_curso}' en el mapa de cursos.")
        print(f"     Agrégalo manualmente o verifica que el URL esté en el mapa.")

    # Siempre regenerar el inventario detallado al final
    regenerar_inventario_detallado()


def regenerar_inventario_detallado():
    """
    Escanea todas las carpetas de cursos y regenera la sección
    '## 📊 Inventario detallado' en 00 - Mapa de cursos.md.
    Se llama automáticamente al terminar cada curso.
    """
    mapa_path = CURSOS_PATH / "00 - Mapa de cursos.md"
    if not mapa_path.exists():
        return

    filas = []
    for indice in sorted(CURSOS_PATH.rglob("00 - Índice del curso.md")):
        carpeta = indice.parent
        materia = carpeta.parent.name
        nombre  = carpeta.name

        clases_n  = len(list(carpeta.glob("Clase *.md")))
        guias_n   = len([f for f in carpeta.iterdir()
                         if "Gu" in f.name and "estudio" in f.name.lower()])
        evals_n   = len([f for f in carpeta.iterdir()
                         if "Evaluaci" in f.name and "Respuestas" not in f.name])
        plans_n   = len([f for f in carpeta.iterdir()
                         if "Planificaci" in f.name])
        slides_n  = len(list(carpeta.glob("*.pdf")))
        resps_n   = len([f for f in carpeta.iterdir() if "Respuestas" in f.name])

        wikilink = f"[[Cursos/{materia}/{nombre}/00 - Índice del curso\\|{nombre}]]"

        faltantes = []
        if clases_n > 0:
            if guias_n < clases_n:
                faltantes.append(f"{clases_n - guias_n} guía(s)")
            if evals_n == 0:
                faltantes.append("evals")
            if plans_n == 0:
                faltantes.append("planif")
            if slides_n == 0:
                faltantes.append(f"{clases_n} slides")
            elif slides_n < clases_n:
                faltantes.append(f"{clases_n - slides_n} slides")
            if evals_n > 0 and resps_n < evals_n:
                faltantes.append(f"{evals_n - resps_n} resp. docente")

        falta_str  = " · ".join(faltantes) if faltantes else "—"
        slides_str = str(slides_n) if slides_n >= clases_n > 0 else (
            f"{slides_n}/{clases_n}" if slides_n > 0 else "—"
        )
        evals_str  = str(evals_n) if evals_n > 0 else "—"
        plans_str  = str(plans_n) if plans_n > 0 else "—"

        filas.append(
            f"| {wikilink} | {materia} | {clases_n} | {guias_n} "
            f"| {evals_str} | {plans_str} | {slides_str} | {falta_str} |"
        )

    if not filas:
        return

    bloque_nuevo = "\n".join([
        "## 📊 Inventario detallado — Cursos con carpeta local",
        "",
        "> [!info] Actualización automática",
        "> Esta sección se regenera cada vez que termina un curso con `crear_curso_notebooklm.py`.",
        "",
        "| Curso | Materia | Clases | Guías | Evals | Planif | Slides | ⚠️ Falta |",
        "|-------|---------|--------|-------|-------|--------|--------|----------|",
        *filas,
        "",
    ])

    contenido = mapa_path.read_text(encoding="utf-8")

    if "## 📊 Inventario detallado" in contenido:
        contenido = re.sub(
            r'## 📊 Inventario detallado.*?(?=\n---\n|\n## )',
            bloque_nuevo,
            contenido,
            flags=re.DOTALL,
        )
    else:
        contenido = contenido.replace(
            "\n## Estadísticas del proyecto",
            "\n" + bloque_nuevo + "\n---\n\n## Estadísticas del proyecto",
        )

    mapa_path.write_text(contenido, encoding="utf-8")
    print("  ✅ Inventario detallado regenerado en el mapa de cursos.")


# ─────────────────────────────────────────────
#  MODO --solo-slides
# ─────────────────────────────────────────────

def generar_solo_slides(ruta_curso, forzar_pares=False):
    """Genera las presentaciones faltantes de un curso ya creado."""
    carpeta = VAULT_PATH / ruta_curso if not Path(ruta_curso).is_absolute() else Path(ruta_curso)
    if not carpeta.exists():
        # Intentar como ruta relativa desde CURSOS_PATH
        carpeta = CURSOS_PATH / ruta_curso
    if not carpeta.exists():
        print(f"  ❌ Carpeta no encontrada: {ruta_curso}")
        sys.exit(1)

    separador(f"GENERANDO PRESENTACIONES — {carpeta.name}")

    meta    = cargar_meta(carpeta)
    nb_id   = meta["nb_id"]
    clases  = meta["clases"]
    videos  = meta["videos"]
    source_map = meta["source_map"]

    # Verificar autenticación
    auth = nlm("auth", "check", "--json")
    if not auth or not auth.get("checks", {}).get("sid_cookie"):
        print("  ❌ Sesión expirada. Ejecuta: notebooklm login")
        sys.exit(1)

    # Detectar qué presentaciones ya existen
    existentes = {f.name for f in carpeta.iterdir() if "Presentaci" in f.name and f.suffix == ".pdf"}
    print(f"  Presentaciones ya existentes: {len(existentes)}")

    # Auto-detectar formato: 1 por clase o 1 por par
    # Si se pasa --pares, forzar formato par sin importar lo que exista
    if forzar_pares:
        uno_por_clase = False
    else:
        # Si existe alguna con "Clase XX —" (singular) → formato 1 por clase
        # Si existe alguna con "Clases XX-YY" → formato par
        uno_por_clase = any(
            re.search(r'Presentaci[oó]n - Clase \d+', e) and "Clases" not in e
            for e in existentes
        )
        if existentes and not uno_por_clase:
            uno_por_clase = False  # par
        elif not existentes:
            uno_por_clase = False  # sin existentes: usar formato par por defecto
    print(f"  Modo: {'1 presentación por clase' if uno_por_clase else '1 presentación por cada 2 clases'}")

    task_ids = {}
    clases_lista = sorted(clases.items())

    if uno_por_clase:
        # ── Formato 1 por clase ──────────────────────────────────────
        for clase_num, video_nums in clases_lista:
            label = f"Clase {clase_num:02d}"
            ya_existe = any(f"Presentaci" in e and label in e for e in existentes)
            if ya_existe:
                print(f"  ⏭️  {label} — ya existe, saltando")
                continue

            vid_nums = video_nums
            sources_clase = [source_map[v] for v in vid_nums if v in source_map]
            if not sources_clase:
                continue
            src_args = []
            for sid in sources_clase:
                src_args += ["-s", sid]

            titulos = [clean_surrogates(videos[v-1]["title"]) for v in vid_nums if v <= len(videos)]
            tema = titulos[0].split("|")[0].strip() if titulos else f"Clase {clase_num}"
            n_vid = len(vid_nums)

            print(f"  📊 Generando Presentación {label}: {tema[:45]} ({n_vid} videos → {_calcular_n_slides(n_vid)} slides)...")
            prompt_pres = _prompt_presentacion(clase_num, tema, n_vid)
            r = nlm("generate", "slide-deck", "--language", "es",
                    "--notebook", nb_id, *src_args, prompt_pres, "--json")
            if r and isinstance(r, dict) and "task_id" in r:
                task_ids[f"pres_{clase_num:02d}"] = {
                    "task_id": r["task_id"], "tema": tema,
                    "clase_ini": clase_num, "clase_fin": clase_num,
                }
                print(f"     Task: {r['task_id'][:8]}...")
            else:
                print(f"  ❌ Error al lanzar {label}")
    else:
        # ── Formato 1 por par ────────────────────────────────────────
        for i in range(0, len(clases_lista), 2):
            par = clases_lista[i:i+2]
            clase_ini = par[0][0]
            clase_fin = par[-1][0]
            label = f"Clases {clase_ini:02d}-{clase_fin:02d}" if clase_ini != clase_fin else f"Clase {clase_ini:02d}"

            ya_existe = any(f"Presentaci" in e and label in e for e in existentes)
            if ya_existe:
                print(f"  ⏭️  {label} — ya existe, saltando")
                continue

            all_vid_nums = [v for _, vids in par for v in vids]
            sources_par  = [source_map[v] for v in all_vid_nums if v in source_map]
            if not sources_par:
                continue
            src_args_par = []
            for sid in sources_par:
                src_args_par += ["-s", sid]

            temas_par = []
            for cn, vids in par:
                titulos = [clean_surrogates(videos[v-1]["title"]) for v in vids if v <= len(videos)]
                temas_par.append(titulos[0].split("|")[0].strip() if titulos else f"Clase {cn}")
            tema_par  = " + ".join(temas_par)
            n_vid_tot = len(all_vid_nums)

            print(f"  📊 Generando Presentación {label}: {tema_par[:40]} ({n_vid_tot} videos → {_calcular_n_slides(n_vid_tot)} slides)...")
            prompt_pres = _prompt_presentacion(clase_ini, tema_par, n_vid_tot)
            r = nlm("generate", "slide-deck", "--language", "es",
                    "--notebook", nb_id, *src_args_par, prompt_pres, "--json")
            if r and isinstance(r, dict) and "task_id" in r:
                task_ids[f"pres_{clase_ini:02d}_{clase_fin:02d}"] = {
                    "task_id": r["task_id"], "tema": tema_par,
                    "clase_ini": clase_ini, "clase_fin": clase_fin,
                }
                print(f"     Task: {r['task_id'][:8]}...")
            else:
                print(f"  ❌ Error al lanzar {label}")

    if not task_ids:
        print("\n  ✅ Todas las presentaciones ya existen. Nada que generar.")
        return

    print(f"\n  {len(task_ids)} presentaciones en cola. Esperando...")

    for key, info in task_ids.items():
        task_id = info["task_id"]
        ini  = info["clase_ini"]
        fin  = info["clase_fin"]
        tema = info["tema"]
        label = f"Clases {ini:02d}-{fin:02d}" if ini != fin else f"Clase {ini:02d}"
        print(f"\n  ⏳ Esperando presentación {label}...")
        wait_artifact(task_id, nb_id, timeout=900)
        nombre_archivo = f"📊 Presentación - {label} — {sanitize_filename(tema[:45])}.pdf"
        ruta = carpeta / nombre_archivo
        nlm("download", "slide-deck", str(ruta), "-a", task_id, "--notebook", nb_id)
        if ruta.exists():
            print(f"  ✅ {nombre_archivo} ({ruta.stat().st_size // 1024} KB)")
        else:
            print(f"  ❌ No se pudo descargar: {nombre_archivo}")

    separador("✅ PRESENTACIONES COMPLETADAS")
    total = len(list(carpeta.glob("*.pdf")))
    print(f"  Total PDFs en la carpeta: {total}")
    print(f"  Carpeta: {carpeta}\n")

    # Actualizar mapa de cursos: ahora tiene slides → puede pasar a ✅ Completado
    nombre_curso = meta.get("nombre_curso", carpeta.name)
    materia      = meta.get("materia", "")
    playlist_url = meta.get("playlist_url", "")
    actualizar_mapa_cursos(nombre_curso, materia, carpeta, playlist_url, skip_slides=False)

# ─────────────────────────────────────────────
#  PASO 6: CREAR ÍNDICE
# ─────────────────────────────────────────────

def crear_indice(carpeta, nombre_curso, nb_id, videos, clases, bloques, materia):
    separador("CREANDO ÍNDICE DEL CURSO")

    archivos_clase = sorted([f for f in carpeta.iterdir() if f.name.startswith("Clase")])
    archivos_pres  = sorted([f for f in carpeta.iterdir() if "Presentación" in f.name])
    archivos_guia  = sorted([f for f in carpeta.iterdir() if "Guía de estudio" in f.name])
    archivos_eval  = sorted([f for f in carpeta.iterdir() if "Evaluación" in f.name and "Respuestas" not in f.name])
    archivos_plan  = sorted([f for f in carpeta.iterdir() if "Planificación" in f.name])

    tabla_clases = ""
    for c_num, v_nums in sorted(clases.items()):
        titulos = [videos[v-1]["title"] for v in v_nums if v <= len(videos)]
        archivo = next((f for f in archivos_clase if f"Clase {c_num:02d}" in f.name), None)
        link = f"[[{archivo.stem}|{c_num:02d}]]" if archivo else str(c_num)
        tabla_clases += f"| {link} | {' + '.join(titulos)[:60]} | ⏳ |\n"

    tabla_materiales = ""
    for c_num in sorted(clases.keys()):
        p = next((f for f in archivos_pres if f"Clase {c_num:02d}" in f.name), None)
        g = next((f for f in archivos_guia if f"Clase {c_num:02d}" in f.name), None)
        p_link = f"[[{p.stem}]]" if p else "—"
        g_link = f"[[{g.stem}]]" if g else "—"
        tabla_materiales += f"| Clase {c_num:02d} | {p_link} | {g_link} |\n"

    tabla_bloques = ""
    for b_num in sorted(bloques.keys()):
        e = next((f for f in archivos_eval if f"Bloque {b_num}" in f.name), None)
        p = next((f for f in archivos_plan if f"Bloque {b_num}" in f.name), None)
        e_link = f"[[{e.stem}|📝 Evaluación]]" if e else "—"
        p_link = f"[[{p.stem}|📋 Planificación]]" if p else "—"
        clases_str = ", ".join(str(c) for c in bloques[b_num])
        tabla_bloques += f"| Bloque {b_num} | Clases {clases_str} | {e_link} | {p_link} |\n"

    contenido = f"""# {nombre_curso} — Índice del curso

tags: #{materia.lower()} #notebooklm #youtube
Generado con NotebookLM: 2026-04-25
Cuaderno NotebookLM ID: `{nb_id}`

> [!info] 🤖 Curso generado con NotebookLM
> Este curso fue generado automáticamente desde {len([v for vids in clases.values() for v in vids])} videos de YouTube usando NotebookLM.
> Cada clase, presentación y guía fue generada por IA basándose en el contenido de los videos.

---

## Estructura por clases

| Clase | Tema | Estado |
|-------|------|--------|
{tabla_clases}
---

## 📂 Materiales por clase

| Clase | 📊 Presentación | 📖 Guía de estudio |
|-------|----------------|-------------------|
{tabla_materiales}
---

## 📝 Recursos por bloque

| Bloque | Clases | Evaluación | Planificación |
|--------|--------|-----------|--------------|
{tabla_bloques}
---

## 📈 Progreso

| Métrica | Valor |
|---------|-------|
| Clases generadas | {len(clases)} / {len(clases)} |
| Presentaciones | {len(archivos_pres)} |
| Guías de estudio | {len(archivos_guia)} |
| Evaluaciones | {len(archivos_eval)} |
| Planificaciones | {len(archivos_plan)} |

---

## 🔗 Conexiones

- [[Cursos/00 - Mapa de cursos|Mapa de cursos]]
- [[DASHBOARD|Dashboard general]]
- [[🤖 Guía - NotebookLM y presentaciones|Guía NotebookLM]]
"""

    indice_path = carpeta / "00 - Índice del curso.md"
    indice_path.write_text(contenido, encoding="utf-8")
    print(f"  ✅ Índice creado: {indice_path}")

# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────

def main():
    args = sys.argv[1:]

    # ── Modo --solo-slides ──────────────────────────────────────────
    if "--solo-slides" in args:
        args.remove("--solo-slides")
        forzar_pares = "--pares" in args
        if forzar_pares:
            args.remove("--pares")
        if not args:
            print("USO: python crear_curso_notebooklm.py --solo-slides \"Álgebra/Nombre del curso\" [--pares]")
            sys.exit(1)
        generar_solo_slides(args[0], forzar_pares=forzar_pares)
        return

    # ── Modo normal (crear curso) ───────────────────────────────────
    skip_slides  = "--skip-slides"  in args
    modo_auto    = "--auto"         in args
    for flag in ["--skip-slides", "--auto"]:
        if flag in args: args.remove(flag)

    # Extraer --nombre, --materia, --curacion
    def pop_arg(flag):
        if flag in args:
            idx = args.index(flag)
            val = args[idx+1] if idx+1 < len(args) else ""
            args.pop(idx); args.pop(idx)
            return val
        return ""

    nombre_arg   = pop_arg("--nombre")
    materia_arg  = pop_arg("--materia")
    curacion_arg = pop_arg("--curacion")

    if not args:
        print("USO:")
        print('  python crear_curso_notebooklm.py "URL" --auto --nombre "Nombre" --materia "Materia" [--skip-slides]')
        print('  python crear_curso_notebooklm.py "URL" --curacion curacion.json [--skip-slides]')
        print('  python crear_curso_notebooklm.py --solo-slides "Materia/Nombre del curso"')
        sys.exit(1)

    playlist_url = args[0]

    print("\n" + "="*60)
    print("  CREADOR DE CURSOS — NotebookLM + YouTube")
    modos = []
    if skip_slides: modos.append("sin presentaciones")
    if modo_auto:   modos.append("curación automática")
    if modos: print(f"  MODO: {' | '.join(modos)}")
    print("="*60)

    # ── Detección automática de nombre y materia desde el mapa ────────
    if not nombre_arg and not materia_arg:
        det_nombre, det_materia = detectar_curso_desde_url(playlist_url)
        if det_nombre:
            print(f"\n  🔍 Detectado en el mapa de cursos:")
            print(f"     Nombre  : {det_nombre}")
            print(f"     Materia : {det_materia}")
            print(f"  → Procediendo con estos datos. Usa --nombre/--materia para cambiarlos.")
            nombre_arg = det_nombre
            materia_arg = det_materia
        else:
            print(f"\n  ⚠️  URL no encontrada en el mapa de cursos.")
            print(f"     Usa --nombre \"Nombre del curso\" --materia \"Materia\"")
    elif nombre_arg:
        print(f"\n  📝 Usando nombre especificado: \"{nombre_arg}\" | Materia: {materia_arg or '(no especificada)'}")

    # Verificar autenticación
    print("\n  Verificando autenticación NotebookLM...")
    auth = nlm("auth", "check", "--json")
    if not auth or not auth.get("checks", {}).get("sid_cookie"):
        print("  ❌ Sesión expirada. Ejecuta: notebooklm login")
        sys.exit(1)
    print("  ✅ Autenticado correctamente")

    videos = extraer_videos(playlist_url)

    # Elegir modo de curación
    if curacion_arg:
        nombre_curso, materia, clases, bloques, omitidos = curar_desde_json(curacion_arg, videos)
    elif modo_auto:
        nombre_curso, materia, clases, bloques, omitidos = auto_curar_videos(
            videos, nombre_arg, materia_arg)
    else:
        # Fallback: si no se pasó --auto ni --curacion, usar auto igual
        print("  ⚠️  Ni --auto ni --curacion especificado. Usando curación automática.")
        nombre_curso, materia, clases, bloques, omitidos = auto_curar_videos(
            videos, nombre_arg, materia_arg)

    # Aplicar nombre y materia desde argumentos si no vienen de la curación
    if nombre_arg and not nombre_curso:
        nombre_curso = nombre_arg
    if materia_arg and not materia:
        materia = materia_arg
    if not nombre_curso:
        nombre_curso = input("  Nombre del curso: ").strip()
    if not materia:
        materia = input("  Materia: ").strip()

    nb_id, source_map = crear_cuaderno_y_fuentes(nombre_curso, videos, clases, omitidos)
    carpeta = CURSOS_PATH / materia / sanitize_filename(nombre_curso)
    task_ids = generar_materiales(nb_id, source_map, clases, bloques, videos, materia, skip_slides=skip_slides, carpeta=carpeta)
    carpeta = esperar_y_descargar(nb_id, task_ids, nombre_curso, materia)
    guardar_meta(carpeta, nb_id, source_map, clases, bloques, videos, nombre_curso, materia, playlist_url)
    crear_indice(carpeta, nombre_curso, nb_id, videos, clases, bloques, materia)
    actualizar_mapa_cursos(nombre_curso, materia, carpeta, playlist_url, skip_slides)

    separador("CURSO COMPLETADO")
    print(f"\n  Carpeta: {carpeta}")
    print(f"  Archivos generados: {len(list(carpeta.iterdir()))}")
    if skip_slides:
        print(f"\n  Las presentaciones NO fueron generadas.")
        print(f"  Cuando el rate limit se resetee, ejecuta:")
        print(f'  python crear_curso_notebooklm.py --solo-slides "{materia}/{nombre_curso}"')
    print(f"\n  Abre Obsidian: Cursos/{materia}/{nombre_curso}/\n")

if __name__ == "__main__":
    main()
