# Resumen del proyecto — Para nuevo chat

## Contexto
- Docente de matemáticas construyendo portafolio digital en **Obsidian**
- Vault: `C:\Users\braya\OneDrive\Documentos\4 portafolio\`
- Fuente: canal YouTube **"Matemáticas profe Alex"** — 28 cursos / 481 lecciones
- Email: brayanruiz1028@gmail.com | Sistema: Windows 11 + OneDrive

---

## Estado del proyecto

| Métrica | Valor |
|---------|-------|
| Cursos completados | **7 / 28** |
| Aritmética | Números enteros ✅ · Números decimales ✅ · Fracciones ✅ · Jerarquía ✅ · Notación Científica ✅ · Razones y proporciones ✅ (16 clases · 16 guías · 8 slides · 3 eval · 3 plan) |
| Álgebra | Suma y resta de expresiones algebraicas ✅ · Solución de ecuaciones ✅ |
| Geometría | Teorema de Pitágoras ✅ |
| Geometría Analítica | Plano Cartesiano ✅ |

### Próximos cursos sugeridos
1. Lenguaje Algebraico
2. Ángulos
3. Monomios y polinomios

---

## Reglas críticas de formato

1. **NUNCA usar HTML con estilos inline** → usar siempre admonitions: `> [!info]`, `> [!note]`, `> [!warning]`, `> [!tip]`
2. **Navegación** con wikilinks `[[]]` al inicio Y al final de cada clase
3. **Ejercicios progresivos**: siempre 🟢 Fácil → 🟡 Medio → 🔴 Avanzado
4. **Aplicaciones** siempre con `$USD`
5. **Dataview**: NO usar `UNION` — usar tablas Markdown manuales
6. **Botones**: NO funcionan para navegación — usar wikilinks en callouts
7. **TÍTULOS SIEMPRE EN ESPAÑOL** — nombres de archivos, encabezados `# Clase XX —`, guías, evaluaciones y presentaciones deben estar en español. Si el video fuente está en inglés, traducir el título. Esto aplica a TODO: nombres de archivo, contenido generado por NotebookLM y metadatos.

---

## Reglas de creación de cursos

7. **CURACIÓN AUTOMÁTICA** — Extraer títulos, mostrar tabla de fusiones/omisiones y **proceder sin esperar aprobación**
8. **Script**: `crear_curso_notebooklm.py` automatiza TODO. Comando exacto a ejecutar:
   ```
   cd "C:\Users\braya\OneDrive\Documentos\4 portafolio" && python crear_curso_notebooklm.py "URL" --auto --skip-slides
   ```
   El script **detecta nombre y materia automáticamente** desde el mapa de cursos usando la URL.
   Si el URL no está en el mapa: agregar `--nombre "Nombre sin tildes" --materia "Materia"`.
   Flags: `--auto` = curación sin input | `--skip-slides` = sin PDFs | `--solo-slides "Materia/Nombre"` = solo PDFs después.
   Al terminar, actualiza automáticamente `Cursos/00 - Mapa de cursos.md` con el inventario generado.
9. **Granularidad**: presentaciones y guías **por clase** · evaluaciones y planificaciones **por bloque**
10. **Idioma**: español en todos los materiales

---

## Herramientas disponibles

| Herramienta                                   | Estado | Uso                                   |
| --------------------------------------------- | ------ | ------------------------------------- |
| `notebooklm-py` CLI v0.3.4                    | ✅      | Generar materiales desde YouTube      |
| `yt-dlp`                                      | ✅      | Extraer videos de playlists           |
| Chrome extension (`mcp__Claude_in_Chrome__*`) | ✅      | Navegar YouTube cuando WebFetch falla |
| Script `crear_curso_notebooklm.py`            | ✅      | Automatización completa del curso     |

> **Si la sesión de NotebookLM expira:** ejecutar `notebooklm login` en terminal.
> **Encoding en Windows:** usar siempre `encoding='utf-8'` en subprocesos Python.

---

## Estructura de carpeta de un curso generado

```
Cursos/[Materia]/[Nombre]/
├── 00 - Índice del curso.md
├── Clase 01 - [Título].md
├── 📊 Presentación - Clase 01 — [Título].pdf   ← por clase
├── 📖 Guía de estudio - Clase 01 — [Título].md ← por clase
├── 📝 Evaluacion - Bloque 1 — [Tema].md         ← por bloque (estudiante)
├── 📋 Respuestas Docente - Bloque 1 — [Tema].md ← por bloque (docente)
└── 📋 Planificacion - Bloque 1 — [Tema].md      ← por bloque (DUA)
```

---

## Referencia detallada (leer solo si lo necesitas)

- Prompts completos, plantillas, flujo NotebookLM paso a paso → `[[REFERENCIA - Creación de cursos]]`
- Applets GeoGebra verificados → `[[REFERENCIA - GeoGebra Applets]]`
- Guía NotebookLM → `[[🤖 Guía - NotebookLM y presentaciones]]`
