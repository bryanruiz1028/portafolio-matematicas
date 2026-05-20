# 04 — Prompts del Portafolio (uso diario)

> **Objetivo:** Crear cursos completos con el menor número de prompts posible.
> **Flujo actual:** YouTube → NotebookLM → Obsidian (todo automatizado por Claude).

---

## 🟢 PROMPT ÚNICO — Crear un curso completo (con presentaciones)

Copia, **solo edita la URL** y pega en el chat nuevo:

```
Lee C:\Users\braya\OneDrive\Documentos\4 portafolio\RESUMEN PARA NUEVO CHAT.md

Luego ejecuta:
cd "C:\Users\braya\OneDrive\Documentos\4 portafolio" && python crear_curso_notebooklm.py "URL_PLAYLIST" --auto
```

**Ejemplo real:**
```
Lee C:\Users\braya\OneDrive\Documentos\4 portafolio\RESUMEN PARA NUEVO CHAT.md

Luego ejecuta:
cd "C:\Users\braya\OneDrive\Documentos\4 portafolio" && python crear_curso_notebooklm.py "https://www.youtube.com/playlist?list=PLeySRPnY35dGmEVikvufQdL8CLtpwDD7Z" --auto
```

> ✅ **El script detecta nombre y materia automáticamente** desde el mapa de cursos usando la URL.
> ✅ **Sin `--skip-slides`** = genera las presentaciones PDF incluidas en el mismo run.
> Solo necesitas `--nombre` y `--materia` si el URL **no** está en el mapa.

**Si el URL no está en el mapa:**
```
cd "C:\Users\braya\OneDrive\Documentos\4 portafolio" && python crear_curso_notebooklm.py "URL" --auto --nombre "NOMBRE SIN TILDES" --materia "MATERIA"
```

> ⚠️ **Sin tildes ni ñ en `--nombre` y `--materia`** (evita errores de encoding en Windows).

**El script hace TODO automáticamente:**
1. Extrae videos con yt-dlp
2. Agrupa en clases (target = videos ÷ 4, máx 5 por clase, fusión greedy)
3. Crea cuaderno NotebookLM y sube los videos
4. Genera clases, guías, evaluaciones (estudiante + docente) y planificaciones DUA
5. Genera presentaciones PDF (12 diapositivas por clase)
6. Descarga todo a `Cursos/[Materia]/[Nombre]/`
7. Actualiza `Cursos/00 - Mapa de cursos.md`: estado del curso + inventario detallado

---

## 🟡 Prompts opcionales (solo si los necesitas)

### Crear curso SIN presentaciones (para no gastar el rate limit de slides)

```
cd "C:\Users\braya\OneDrive\Documentos\4 portafolio" && python crear_curso_notebooklm.py "URL" --auto --skip-slides
```

> El curso se crea completo (clases, guías, evaluaciones, planificaciones) pero **sin PDFs**.
> El script guarda un `.meta.json` con toda la info necesaria para generarlos después.

### Generar presentaciones de un curso ya creado

```
cd "C:\Users\braya\OneDrive\Documentos\4 portafolio" && python crear_curso_notebooklm.py --solo-slides "Álgebra/Nombre del curso"
```

> Lee el `.meta.json`, detecta qué presentaciones faltan y las genera.
> Puedes ejecutarlo varias veces — saltea las que ya existen.

---

### Alinear planificaciones con el currículo

Úsalo **después de crear el curso**, una vez que las planificaciones ya están generadas.

```
Alinea las planificaciones del curso [NOMBRE DEL CURSO] con el currículo.

Ruta del curso: C:\Users\braya\OneDrive\Documentos\4 portafolio\Cursos\[Materia]\[Nombre del curso]\

Lee primero:
C:\Users\braya\OneDrive\Documentos\4 portafolio\DESTREZAS E INDICADORES DE EVALUACIÓN\📚 Destrezas e Indicadores - Matemática.md

Luego lee cada archivo 📋 Planificación - Bloque X del curso y para cada uno:
1. Identifica qué destreza(s) del documento corresponden al tema del bloque
2. Selecciona el indicador de evaluación si existe (si no existe, ponlo como —)
3. Sugiere el grado (8°, 9° o 10°) según la progresión: 8°=enteros Z · 9°=racionales Q · 10°=reales R
4. Añade al final del archivo una sección ## [N]. Currículo con esta tabla:

| | Código | Descripción |
|--|--------|------------|
| **Criterio** | CE.M.4.X | [descripción del criterio] |
| **Destreza principal** | M.4.X.X `X°` | [descripción de la destreza] |
| **Destreza secundaria** | M.4.X.X `X°` | [si aplica, si no omitir esta fila] |
| **Indicador** | I.M.4.X.X | [descripción del indicador, o — si no existe] |
| **Grado sugerido** | X° | [justificación de 1 línea] |

REGLA: Solo usa códigos que existan en el archivo de destrezas. No inventes códigos.
```

> **Ejemplo ya aplicado:** Curso "Solución de ecuaciones - Primer grado y Racionales" ✅

---

### Si la sesión de NotebookLM expira

```
notebooklm login
```

Ejecuta en terminal. Cuando termines de loguearte escribe "listo" y Claude continúa.

---

### Regenerar un material puntual

```
Regenera la [Clase / Presentación / Guía de estudio] N° [X] del curso [Nombre].
```

---

### Continuar un curso a medias

```
Continúa el curso [Nombre].
Lee Cursos/[Materia]/[Nombre]/00 - Índice del curso.md y completa lo que falte.
```

---

## 📋 Reglas que Claude sigue automáticamente

No necesitas escribirlas — las ejecuta leyendo el RESUMEN:

- ✅ Curación automática (tabla de fusiones → procede sin esperar aprobación)
- ✅ Presentaciones y guías **por clase** (12 diapositivas fijas por presentación)
- ✅ Evaluaciones **por bloque** (10 preguntas, 2 archivos: estudiante + docente)
- ✅ Planificaciones DUA **por bloque** (Anticipación / Construcción / Consolidación)
- ✅ Idioma español · Formato Obsidian/Admonition · Sin HTML inline
- ✅ Aplicaciones con `$USD` · Ejercicios progresivos 🟢🟡🔴
- ✅ Mapa de cursos se actualiza solo al terminar (estado + inventario + estadísticas)

**Estructura fija de las 12 diapositivas:**
Portada · Aplicaciones reales · Concepto · Fórmula · Error frecuente · Paso a paso ×3 · Ejemplo $USD · ¡Tu turno! · Respuesta+cierre · Resumen visual

---

## 📂 Archivos clave del proyecto

| Archivo | Para qué |
|---------|----------|
| `RESUMEN PARA NUEVO CHAT.md` | Contexto que Claude lee al inicio |
| `crear_curso_notebooklm.py` | Script principal — automatiza todo |
| `Cursos/00 - Mapa de cursos.md` | 28 cursos + estado + inventario detallado |
| `🤖 Guía - NotebookLM y presentaciones.md` | IDs de cuadernos y artefactos por curso |
| `DESTREZAS E INDICADORES DE EVALUACIÓN/` | Currículo oficial para alinear planificaciones |

---

---

## 📄 Convertir evaluaciones Markdown a Word (.docx)

> **Script:** `md_a_word.py` — convierte automáticamente los archivos `📝 Evaluación*.md` a documentos Word con encabezado institucional, cuadrícula, puntaje por pregunta e instrucciones por sección.

### Convertir un solo archivo

```
python -X utf8 md_a_word.py "Cursos\Materia\Curso\📝 Evaluación - Bloque X — Tema.md"
```

> Con reescritura IA (adapta lenguaje a "usted", elimina referencias externas).

```
python -X utf8 md_a_word.py "Cursos\Materia\Curso\📝 Evaluación - Bloque X — Tema.md" --sin-ia
```

> Sin IA — generación rápida, texto sin adaptar.

### Convertir todas las evaluaciones de una carpeta

```
python -X utf8 md_a_word.py --todos "Cursos\Materia"
```

> Busca todos los `Evaluaci*.md` dentro de la carpeta de forma recursiva.
> **Omite automáticamente** los que ya tienen `.docx` generado.

**Ejemplo — procesar una materia completa:**
```
cd "C:\Users\braya\OneDrive\Documentos\4 portafolio" && python -X utf8 md_a_word.py --todos "Cursos\Álgebra"
```

---

### Qué genera el script automáticamente

| Elemento | Detalle |
|----------|---------|
| **Encabezado institucional** | ESCUELA DE EDUCACIÓN BÁSICA "CARIBE" centrado con acuerdo ministerial y ubicación |
| **Datos del estudiante** | Nombre / Curso / Fecha / Puntaje — una sola vez, sin duplicados |
| **Título de la evaluación** | Tomado del `# H1` del markdown |
| **Secciones** | Sin "SECCIÓN I:", sin puntajes en el título — solo el nombre (ej: *Selección Múltiple*) |
| **Instrucciones** | Si la sección no las tiene, agrega automáticamente la instrucción correspondiente en cursiva |
| **Numeración** | Preguntas renumeradas secuencialmente: `1)  2)  3)  ...` |
| **Puntaje por pregunta** | Calculado por sección y mostrado en azul al final de cada pregunta — siempre visible |
| **Cuadrícula** | Reemplaza las líneas de "Procedimiento" por una cuadrícula de cuadros pequeños (0.32 cm) |
| **Filtros automáticos** | Elimina referencias al "Profe Alex", bloque "Identificación:", viñetas duplicadas |

---

### Prompt interno que usa la IA (referencia)

> Este prompt es el que el script envía internamente a Claude Code al reescribir cada evaluación. No es necesario copiarlo — el script lo aplica solo.

```
Eres un editor de evaluaciones escolares de matemáticas para Ecuador (educación básica).
Reescribe el siguiente texto de evaluación siguiendo estas reglas ESTRICTAS:

1. Usa SIEMPRE "usted" para dirigirte al estudiante (nunca "tú").
2. Lenguaje simple y claro para estudiantes de educación básica.
3. ELIMINA COMPLETAMENTE cualquier referencia a: "Profe Alex", "Alex", "el profesor",
   "según el video", "como se explicó", "según se indicó", "explicada por", "indicada por",
   "vista en clase" o cualquier frase que mencione una fuente externa. Reemplaza esa parte
   de la oración con lenguaje institucional neutro. Por ejemplo:
   - "según la jerarquía explicada por el Profe Alex" → "según la jerarquía de las operaciones"
   - "como se vio en el video" → (eliminar completamente esa frase)
4. NO cambies: fórmulas matemáticas, nombres de secciones, puntajes, opciones a/b/c/d,
   tablas, bancos de palabras, líneas de respuesta (____), números de preguntas.
5. Mantén el mismo número de preguntas y secciones.
6. Devuelve SOLO el texto reescrito, sin explicaciones ni comentarios.
```

---

*Actualizado: 2026-05-14 — Script md_a_word.py · Conversión masiva con --todos · Instrucciones automáticas por sección*
