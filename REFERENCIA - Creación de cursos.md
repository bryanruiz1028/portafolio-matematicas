# Referencia completa — Creación de cursos con NotebookLM

> **Este archivo lo lee Claude solo cuando lo necesita.** No se carga en cada chat.

---

## Cuadernos NotebookLM activos

| Curso | Notebook ID |
|-------|------------|
| Suma y resta de expresiones algebraicas (v2) | `048d6677-3ad5-430c-b031-edbfb7091842` |
| Solución de ecuaciones - Primer grado y Racionales | *(ver 🤖 Guía - NotebookLM)* |

---

## Flujo completo con NotebookLM

```
PASO 0  → Curación automática (yt-dlp + agrupación por concepto)
           Mostrar tabla Video→Clase y proceder SIN esperar aprobación

PASO 1  → notebooklm create "Nombre" --json → guardar notebook_id

PASO 2  → notebooklm source add --notebook ID "https://youtube.com/watch?v=ID" --json
           (un source por video; guardar source_id de cada uno)

PASO 3  → notebooklm source list --notebook ID --json → esperar status: "ready"

PASO 4  → Generar CLASES (1 por clase, fuentes del grupo)
           notebooklm generate report --format custom --language es
             --notebook ID -s SRC1 -s SRC2 "[PROMPT_CLASE]" --json

PASO 5  → Generar PRESENTACIONES (1 por clase)
           notebooklm generate slide-deck --language es
             --notebook ID -s SRC1 -s SRC2 "[PROMPT_PRESENTACION]" --json

PASO 6  → Generar GUÍAS DE ESTUDIO (1 por clase)
           notebooklm generate report --format study-guide --language es
             --notebook ID -s SRC1 -s SRC2 --json

PASO 7  → Generar EVALUACIONES (1 por bloque, todos los sources del bloque)
           notebooklm generate report --format custom --language es
             --notebook ID -s [sources bloque] "[PROMPT_EVALUACION]" --json

PASO 7b → Generar PLANIFICACIONES DUA (1 por bloque)
           notebooklm generate report --format custom --language es
             --notebook ID -s [sources bloque] "[PROMPT_PLANIFICACION]" --json

PASO 8  → Esperar artefactos: notebooklm artifact wait ID --notebook NB --timeout 900

PASO 9  → Descargar: notebooklm download report "ruta.md" -a ID
                     notebooklm download slide-deck "ruta.pdf" -a ID

PASO 10 → Crear 00 - Índice del curso.md con wikilinks a todos los archivos
```

---

## Prompt — CLASES

```
"Genera la Clase [N] completa en español sobre [TEMA].
Usa EXACTAMENTE este formato Obsidian/Admonition (no lo cambies):

# Clase [N] — [Título]
tags: #algebra #[tema]
Curso: [[00 - Índice del curso]] | Bloque [B] | Lección [N] de [TOTAL]

> [!info] 🧭 Navegación
> [[Clase [N-1]|⬅ Clase [N-1]]] | [[00 - Índice del curso|Índice]] | **Clase [N]** | [[Clase [N+1]|Clase [N+1] ➡]]

## ¿Por qué es importante esta clase?
> [!info] 🌍 Relevancia ... (ejemplos con $USD)

## Concepto clave
> [!note] 📌 ...
> [!warning] ⚠️ Error común ...
> [!tip] 💡 Truco ...

## Procedimiento paso a paso
[bloque de código con PASOS]
[4 bloques ad-example con ejemplos resueltos, el último con $USD]

## Ejercicios para el estudiante
[ad-abstract 🟢 Fácil, 🟡 Medio, 🔴 Avanzado con $USD]
[ad-success Respuestas para el docente]

## Mini-prueba de autoevaluación
[3 bloques ad-question con opciones a/b/c/d y respuesta]

## Notas para el próximo tema
> [!tip] 💡 En la próxima clase ...

> [!info] 🧭 Navegación final (igual que la inicial)"
```

---

## Prompt — PRESENTACIONES (proyector)

> Estructura de 12 diapositivas pedagógicas. Cada slide tiene un propósito específico.

```
"Crea una presentación de clase para PROYECTOR sobre: [TEMA]
Nivel: Básica Superior (12-15 años) | Idioma: español | Clase [N]

REGLAS GENERALES (aplican en todas las diapositivas):
- Máximo 5 líneas de texto por diapositiva — una sola idea por slide
- Texto grande y legible desde el fondo del aula
- Fondo oscuro + texto claro (alto contraste para proyector)
- Sin efectos sutiles, sin gradientes — todo sólido y visible
- Las ecuaciones son el elemento visual principal: grandes, centradas, destacadas

ESTRUCTURA OBLIGATORIA — crea exactamente estas diapositivas en este orden:

SLIDE 1 — PORTADA
Título: [TEMA]
Subtítulo: 'Matemáticas | Básica Superior'
Elemento visual: ícono o número grande relacionado al tema

SLIDE 2 — ¿POR QUÉ LO APRENDEMOS?
Título: '¿Para qué sirve esto en la vida real?'
2-3 ejemplos concretos y cotidianos (uno con precios en $USD)
Frase motivadora breve

SLIDE 3 — CONCEPTO CLAVE
Título: '¿Qué es [tema]?'
Definición en UNA oración simple (lenguaje de 12 años)
Recuadro destacado con la idea esencial
NO incluir fórmulas aquí todavía

SLIDE 4 — LA REGLA / FÓRMULA
Solo la fórmula o regla principal, tamaño muy grande y centrada
Etiqueta cada parte de la fórmula con su nombre
Recuadro de color que la enmarca

SLIDE 5 — ERROR FRECUENTE
Título: '⚠️ Error que TODOS cometen'
Mostrar: ❌ Lo incorrecto | ✅ Lo correcto
Explicación en 1 línea de por qué ocurre el error

SLIDES 6, 7, 8 — EJEMPLO RESUELTO PASO A PASO
Una diapositiva por paso (no comprimas todos los pasos en una)
Slide 6: Enunciado del problema + Paso 1
Slide 7: Paso 2 + Paso 3 (con el paso anterior en gris/tenue para contexto)
Slide 8: Resultado final destacado + verificación

SLIDE 9 — SEGUNDO EJEMPLO (aplicación con $USD)
Problema con contexto de dinero o situación cotidiana
Resultado en 3-4 pasos visibles

SLIDE 10 — ¡TU TURNO!
Título: '¡Ahora tú!'
1 ejercicio nivel fácil (🟢) visible para que los estudiantes resuelvan en clase
Espacio visual que simula 'hoja en blanco' para trabajar
NO mostrar la respuesta en esta diapositiva

SLIDE 11 — RESPUESTA Y CIERRE
Solución del ejercicio anterior con pasos clave
Recuadro: 'Lo que aprendimos hoy' — 3 puntos clave en bullets
Frase: 'En la próxima clase: [tema siguiente relacionado]'

SLIDE 12 — RESUMEN VISUAL
Mapa o esquema visual que conecte los conceptos de la clase
Sin texto largo — solo palabras clave con flechas o conexiones"
```

---

## Prompt — EVALUACIONES (por bloque)

```
"Genera una EVALUACIÓN FORMATIVA en español sobre [TEMA DEL BLOQUE].
Produce DOS DOCUMENTOS SEPARADOS en este orden:

═══════════════════════════════════════
DOCUMENTO 1 — VERSIÓN ESTUDIANTE
═══════════════════════════════════════

# EVALUACIÓN FORMATIVA: [TEMA]
Nombre: _______ Curso: _______ Fecha: _______ Puntaje: ___/10

SECCIÓN I   — Selección múltiple Q1-Q3 (3pts): 4 opciones a/b/c/d. "Respuesta: ___" tras cada una.
SECCIÓN II  — Verdadero o Falso Q4-Q5 (2pts): "Respuesta: ___" tras cada una.
SECCIÓN III — Completar espacios Q6-Q7 (2pts): mín. 3 blancos misma oración. Banco a/b/c/d/e debajo.
SECCIÓN IV  — Relacionar columnas Q8 (1pt): tabla 4 filas col. R vacía.
SECCIÓN V   — Resolver ejercicio Q9 (1pt): UN ejercicio 🟢 Fácil con espacio para procedimiento.
SECCIÓN VI  — Aplicación $USD Q10 (1pt): problema cotidiano con espacio para resolución.
NO incluir respuestas en este documento.

═══════════════════════════════════════
DOCUMENTO 2 — RESPUESTAS Y MATERIAL DOCENTE
═══════════════════════════════════════

# RESPUESTAS DOCENTE: [TEMA]
- Respuestas Q1-Q10 con justificación breve
- Procedimiento resuelto Q9 y Q10
- Rúbrica: Logrado / En proceso / Por lograr por sección
- Escala: 10=100% Excelente|8-9=Muy bueno|6-7=Satisfactorio|4-5=En proceso|<4=Necesita refuerzo"
```

---

## Prompt — PLANIFICACIONES DUA (por bloque)

```
"Actua como un profesor experto en [MATERIA].
Tema: [TEMA DEL BLOQUE]
Recursos disponibles: pizarra, marcadores, fichas, impresora. Agrega 1 recurso adicional facil de conseguir.

Genera en formato Obsidian con admonitions:

# Planificacion Didactica - [TEMA]
tags: #planificacion #dua #[tag]
Nivel: Basica Superior (12-15 anos) | Duracion: 80 minutos

## 1. Tema / ## 2. Metodologia (colaborativo formal, 2-3 lineas)

## 3. Secuencia Didactica

### ANTICIPACION - 20 min
> [!abstract] Actividad de inicio
> [!note] Enfoque DUA: - **Que:** / - **Como:**

### CONSTRUCCION - 40 min
> [!example] Actividades centrales (incluye ejemplo con numeros reales del tema)
> [!note] Enfoque DUA

### CONSOLIDACION - 20 min
> [!success] Actividad de cierre
> [!note] Enfoque DUA

## 4. Recursos
| Recurso | Tipo | Uso en la clase |"
```

---

## Estructura de evaluaciones formativas (formato antiguo — 12 preguntas)

> Solo para cursos generados sin NotebookLM. Los cursos nuevos usan el prompt de arriba (10 preguntas).

| Sección | Tipo | Preguntas | Pts |
|---------|------|-----------|-----|
| I | Selección múltiple | Q1-Q3 | 3 |
| II | Verdadero/Falso | Q4-Q5 | 2 |
| III | Completar espacios | Q6-Q7 | 2 |
| IV | Relacionar columnas | Q8 | 1 |
| V | Resolver 🟢 | Q9 | 1 |
| VI | Aplicación $USD | Q10 | 1 |

---

## Plantilla de clase — estructura de secciones

1. Encabezado + tags + Navegación inicial
2. ¿Por qué es importante? — `[!info]` + ejemplos cotidianos con $USD
3. Concepto clave — `[!note]` + `[!warning]` + `[!tip]`
4. Procedimiento paso a paso + ejemplos (`ad-example`)
5. Ejercicios para el estudiante (🟢🟡🔴 en `ad-abstract`)
6. Respuestas para el docente (`ad-success`)
7. Mini-prueba de autoevaluación (3 × `ad-question`)
8. Notas para el próximo tema
9. Navegación final

---

## Plugins de Obsidian instalados

| Plugin | Función |
|--------|---------|
| Admonition | Cajas visuales (`ad-note`, `ad-example`, etc.) |
| Dataview | Consultas dinámicas en DASHBOARD |
| Templater | Plantillas automáticas |
| Kanban | Tablero de planificación |
| Excalidraw | Diagramas matemáticos |

---

## Chrome extension — flujo YouTube

```
1. mcp__Claude_in_Chrome__navigate → URL de la playlist
2. mcp__Claude_in_Chrome__get_page_text → extrae títulos
3. Si falla → mcp__Claude_in_Chrome__javascript_tool
   con: document.querySelectorAll('yt-formatted-string#video-title')
```

---

## Calculadoras embebidas (GeoGebra / Desmos)

```html
<!-- GeoGebra -->
<iframe src="https://www.geogebra.org/material/iframe/id/{{ID}}/width/600/height/400/border/888888"
  width="600" height="400" style="border:1px solid #ccc; border-radius:4px;"></iframe>

<!-- Desmos -->
<iframe src="https://www.desmos.com/calculator/{{ID}}?embed"
  width="600" height="400" style="border:1px solid #ccc; border-radius:4px;"></iframe>
```

**Applets GeoGebra verificados — Plano Cartesiano:**

| Tema | ID |
|------|-----|
| Coordenadas en el plano | `FCgTM92z` |
| Traslación | `ePuHUmeU` |
| Reflexión y Rotación | `nkkvG2aK` |
| Homotecia (con slider k) | `q7p3kkgh` |
| Rotación en el origen | `rthPu2Mm` |

> Si el iframe aparece en blanco: Obsidian → Configuración → Editor → desactivar "Modo restringido"
