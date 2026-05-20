# 🤖 Guía — NotebookLM: cuadernos y presentaciones por curso

tags: #guia #notebooklm #presentaciones #automatizacion
Creado: 2026-04-25
Autor: Claude Code (claude-sonnet-4-6)

---

## ¿Qué es esta guía?

Explica cómo se integró **Google NotebookLM** con el portafolio docente para generar presentaciones automáticas por curso y por bloque temático. Incluye el proceso realizado, comandos exactos y recomendaciones para futuras sesiones.

---

## 🔧 Herramientas instaladas

| Herramienta | Versión | Ubicación |
|-------------|---------|-----------|
| `notebooklm-py` (CLI Python) | 0.3.4 | `C:\...\Python313\Scripts\notebooklm.exe` |
| Skill `notebooklm` (Claude Code) | — | `C:\Users\braya\.agents\skills\notebooklm` |
| Autenticación Google | Activa | `C:\Users\braya\.notebooklm\storage_state.json` |

> [!warning] Si la autenticación expira
> Ejecutar en terminal: `notebooklm login`
> Esto abre el navegador para volver a iniciar sesión con Google.

---

## ✅ Proceso realizado — Curso "Suma de expresiones algebraicas"

### Resultado

- **Cuaderno NotebookLM creado:** "Suma de expresiones algebraicas"
  - ID: `3d0c55ad-dc89-47d8-98b4-a17f017b8c22`
- **11 fuentes cargadas** (todas las clases, evaluaciones, índice y planificación)
- **2 presentaciones generadas** (una por bloque)

### Paso 1 — Crear el cuaderno

```bash
PYTHONIOENCODING=utf-8 notebooklm create "Nombre del curso" --json
```

Guarda el `id` del resultado — lo necesitas en todos los pasos siguientes.

### Paso 2 — Agregar fuentes (archivos .md del curso)

```bash
PYTHONIOENCODING=utf-8 notebooklm source add --notebook "ID_CUADERNO" "ruta/al/archivo.md" --json
```

- NotebookLM acepta archivos `.md` directamente.
- Guarda el `source_id` de cada archivo — lo necesitas para las presentaciones por bloque.
- Repite este comando para cada archivo del curso.

### Paso 3 — Verificar que todas las fuentes estén listas

```bash
PYTHONIOENCODING=utf-8 notebooklm source list --notebook "ID_CUADERNO" --json
```

Espera a que todas digan `"status": "ready"` antes de generar presentaciones.

### Paso 4 — Generar presentaciones por bloque

```bash
PYTHONIOENCODING=utf-8 notebooklm generate slide-deck \
  --notebook "ID_CUADERNO" \
  -s "SOURCE_ID_CLASE_01" \
  -s "SOURCE_ID_CLASE_02" \
  -s "SOURCE_ID_EVALUACION" \
  -s "SOURCE_ID_INDICE" \
  "Título de la presentación" \
  --json
```

- Usa `-s` para pasar solo las fuentes del bloque correspondiente.
- Incluir siempre el `Índice del curso` como fuente extra de contexto.
- El comando devuelve un `task_id`. La generación tarda **10–20 minutos**.

### Paso 5 — Verificar el estado de las presentaciones

```bash
PYTHONIOENCODING=utf-8 notebooklm artifact list --notebook "ID_CUADERNO" --json
```

Cuando el `status` sea `completed`, las presentaciones están disponibles en [notebooklm.google.com](https://notebooklm.google.com).

### Paso 6 — Descargar (opcional)

```bash
# Descargar como PDF
PYTHONIOENCODING=utf-8 notebooklm download slide-deck ./presentacion-bloque1.pdf \
  -a "ARTIFACT_ID" --notebook "ID_CUADERNO"

# Descargar como PPTX editable
PYTHONIOENCODING=utf-8 notebooklm download slide-deck ./presentacion-bloque1.pptx \
  -a "ARTIFACT_ID" --notebook "ID_CUADERNO" --format pptx
```

---

## 📋 IDs del curso procesado

### Cuaderno: Suma de expresiones algebraicas
**Notebook ID:** `3d0c55ad-dc89-47d8-98b4-a17f017b8c22`

| Archivo | Source ID |
|---------|-----------|
| 00 - Índice del curso.md | `8fd04591-1cab-40f6-8181-bf6ee2c7b0ec` |
| Clase 01 | `ff8516cb-add3-481b-8af0-cae470388a1b` |
| Clase 02 | `21a2d64d-90f8-4799-890b-20a9168682d3` |
| Clase 03 | `2a729304-3281-4b9a-8f37-dc55fe81a154` |
| Clase 04 | `36909fbf-1b38-4628-86b1-706e40cbb90d` |
| Clase 05 | `af45fedd-b458-437e-9607-449473dbc123` |
| Clase 06 | `04a9d344-dd02-47d6-be5f-c58588d8ccaf` |
| Clase 07 | `29249880-b861-48ff-9678-9973cee199f6` |
| 📝 Evaluación Bloque 1 | `307ac6f8-ef50-413f-a3de-71fd08498821` |
| 📝 Evaluación Bloque 2 | `eb198751-772c-476c-9a9b-f26ec2287c33` |
| 📋 Planificación | `118f7fef-1555-473d-a355-f45337ef9805` |

| Presentación | Artifact ID | Estado |
|--------------|-------------|--------|
| Bloque 1 — Fundamentos | `7feb1aa9-c294-45f1-8278-b18f9838de5c` | ✅ completado |
| Bloque 2 — Polinomios y signos | `805592e7-fcaa-4734-aa67-9428599011be` | ✅ completado |
| Guía estudio Bloque 1 | `37b7ae1b-91aa-4af4-84a3-ddfc6c0b4d10` | ✅ completado |
| Guía estudio Bloque 2 | `9dd63167-1f55-43ff-b40b-2218afe2ec5d` | ✅ completado |

---

## 📋 IDs del curso procesado (v2 — YouTube)

### Cuaderno: Suma y resta de expresiones algebraicas (YouTube)
**Notebook ID:** `048d6677-3ad5-430c-b031-edbfb7091842`
**Carpeta:** `Cursos/Álgebra/Suma y resta de expresiones algebraicas/`

| Video | Título | Source ID | Bloque |
|-------|--------|-----------|--------|
| 1 | Suma \| Introducción | `9c906dff-df8f-46c3-bd8a-fff899222a12` | B1 |
| 2 | Suma \| Ejemplo 1 Monomios | `a6f900a4-e633-4d0e-af23-12c167d87794` | B1 |
| 3 | Suma \| Ejemplo 2 Polinomios | `1274a4cf-f612-40d6-846f-fb128f3d3a69` | B1 |
| 4 | Suma \| Ejemplo 3 Fracciones | `57e3cc3f-6338-44d3-a2a1-9a9d99af9b4a` | B1 |
| 5 | Resta \| Introducción | `785dcd80-145b-4a0d-afca-ba9f6bd9a771` | B2 |
| 6 | Resta \| Ejemplo 1 Monomios | `28370539-b701-4551-b063-3c4b71a5f070` | B2 |
| 7 | Resta \| Ejemplo 2 Polinomios | `32811f79-9c7e-4622-a72c-f1bfb879e2dc` | B2 |
| 8 | Resta \| Ejemplo 3 Polinomios | `69a40cb2-31b0-42d5-9df5-c245e0d16f24` | B2 |

| Artefacto | Artifact ID | Estado |
|-----------|-------------|--------|
| 📊 Presentación Clase 01 — Suma: Intro y monomios | `21e2c105-79e7-447a-93e3-6c57ac67fe98` | ✅ completado |
| 📊 Presentación Clase 02 — Suma: Polinomios y fracciones | `734e94bc-26c9-4eae-b21e-53b070239dd6` | ✅ completado |
| 📊 Presentación Clase 03 — Resta: Intro y monomios | `69d6c778-2899-450e-8233-6a4f21774a92` | ✅ completado |
| 📊 Presentación Clase 04 — Resta: Polinomios | `bd35f141-b671-4f69-bb87-bdd3148b4cf3` | ✅ completado |
| 📖 Guía estudio Clase 01 — Suma: Intro y monomios | `21d6b93c-ad31-4b5d-b52c-12f95ffa0b6e` | ✅ completado |
| 📖 Guía estudio Clase 02 — Suma: Polinomios y fracciones | `0af2f6d6-567d-4b55-b23a-e960c3fdb3b9` | ✅ completado |
| 📖 Guía estudio Clase 03 — Resta: Intro y monomios | `c266c0b1-e615-455f-9c27-51a4b0086423` | ✅ completado |
| 📖 Guía estudio Clase 04 — Resta: Polinomios | `df45af1a-d43b-4bc6-82c3-f076e5ab3f1a` | ✅ completado |
| 📝 Evaluación Bloque 1 | `380b87fb-c1a3-4f32-bb30-ed8782f8ad0f` | ✅ completado |
| 📝 Evaluación Bloque 2 | `3dbae8e2-9063-4c11-b7b9-17ab2d5ff111` | ✅ completado |
| ~~Presentación Bloque 1~~ (reemplazada) | `b39fd765-0520-44a1-ae32-f6f1f6500786` | ♻️ reemplazado por clase |
| ~~Presentación Bloque 2~~ (reemplazada) | `6ef01a61-5d63-442a-abc0-dde492be0e2d` | ♻️ reemplazado por clase |
| ~~Guía estudio Bloque 1~~ (reemplazada) | `0e46f84b-73bd-4091-bfd1-e07fb66e2100` | ♻️ reemplazado por clase |
| ~~Guía estudio Bloque 2~~ (reemplazada) | `21a57daa-5db6-4e30-a933-66849691ac0b` | ♻️ reemplazado por clase |

---

## ⚡ Nota técnica importante — Windows

En Windows, el CLI tiene un error de encoding con caracteres especiales (tildes, emojis). Siempre usar:

```bash
PYTHONIOENCODING=utf-8 notebooklm [comando]
```

O para PowerShell:

```powershell
$env:PYTHONIOENCODING="utf-8"; notebooklm [comando]
```

---

## 💡 Recomendaciones para futuros cursos

### 🥇 Hacer inmediatamente (alto impacto)

> [!tip] 1. Automatizar el proceso con un script
> Crear un script Python o Bash que reciba la carpeta del curso y ejecute todos los pasos automáticamente: crear cuaderno, agregar fuentes, esperar y generar presentaciones por bloque. Ahorraría 30–40 min por curso.

> [!tip] 2. Usar NotebookLM para chatear con el curso
> Una vez cargado el cuaderno, usar:
> ```bash
> PYTHONIOENCODING=utf-8 notebooklm ask --notebook "ID" "¿Cuáles son los conceptos más difíciles del Bloque 1?"
> ```
> Esto permite preparar clases, generar actividades extra y resolver dudas directamente desde el portafolio.

> [!tip] 3. Generar también una guía de estudio por bloque
> Además de las presentaciones, generar un `study-guide` por bloque:
> ```bash
> PYTHONIOENCODING=utf-8 notebooklm generate report --format study-guide \
>   --notebook "ID" -s "SOURCE_IDs_del_bloque"
> ```
> Sirve como hoja de repaso para el estudiante.

### 🥈 Hacer a mediano plazo

> [!note] 4. Crear cuadernos para los 4 cursos completados restantes
> Los siguientes cursos ya tienen archivos listos para subir a NotebookLM:
> - Números enteros (`Cursos/Aritmética/Números enteros/`)
> - Números decimales (`Cursos/Aritmética/Números decimales/`)
> - Fracciones (`Cursos/Aritmética/Fracciones/`)
> - Teorema de Pitágoras (`Cursos/Geometría/Teorema de Pitágoras/`)

> [!note] 5. Generar podcast de audio por bloque
> NotebookLM puede crear un podcast explicativo del contenido:
> ```bash
> PYTHONIOENCODING=utf-8 notebooklm generate audio \
>   --notebook "ID" -s "SOURCE_IDs_del_bloque" \
>   "Explica los conceptos del Bloque 1 como repaso para estudiantes de secundaria"
> ```
> Útil como material de repaso antes de evaluaciones.

> [!note] 6. Guardar las presentaciones en la carpeta del portafolio
> Crear una carpeta `presentaciones/[Curso]/` y descargar los slide decks en PPTX para editarlos si es necesario. La carpeta `presentaciones/` ya existe en la raíz del vault.

### 🥉 Hacer a largo plazo

> [!info] 7. Agregar evaluaciones formativas al cuaderno
> Incluir los archivos `📝 Evaluación - Bloque X.md` como fuentes ayuda a NotebookLM a generar preguntas de práctica más alineadas al curso.

> [!info] 8. Integrar con el flujo de creación de nuevos cursos
> Al finalizar un nuevo curso (después del Paso 0 de curación y creación de clases), agregar como Paso 8 en el flujo:
> 1. Crear cuaderno NotebookLM
> 2. Agregar todos los archivos del curso
> 3. Generar presentaciones por bloque
> 4. Guardar IDs en esta guía

---

## 🔗 Flujo completo resumido

```
Carpeta del curso (archivos .md)
        ↓
notebooklm create "Nombre"          → obtener notebook_id
        ↓
notebooklm source add (× N archivos) → obtener source_ids por bloque
        ↓
notebooklm source list               → esperar status: ready
        ↓
notebooklm generate slide-deck       → una por bloque (con -s por fuentes)
        ↓
notebooklm artifact list             → esperar status: completed
        ↓
Ver en notebooklm.google.com  ·  O descargar PDF/PPTX
```

---

## 🔗 Referencias

- [[RESUMEN PARA NUEVO CHAT]] — Contexto general del portafolio
- [[DASHBOARD]] — Progreso general del proyecto
- Skill instalada: `C:\Users\braya\.agents\skills\notebooklm\SKILL.md`
- Documentación CLI: `notebooklm --help`
