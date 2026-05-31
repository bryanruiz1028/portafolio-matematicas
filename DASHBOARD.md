# 📊 Dashboard — Progreso del proyecto

tags: #dashboard #progreso #proyecto

---

## 📈 Estadísticas generales

| Métrica | Valor | Porcentaje |
|---------|-------|-----------|
| Cursos completados | 8 / 28 | 28.6% |
| Lecciones completadas | 235 / 481 | 48.9% |
| Cursos Aritmética | 5 / 6 | 83.3% |
| Cursos Álgebra | 2 / 7 | 28.6% |
| Cursos Geometría | 1 / 5 | 20.0% |
| Cursos Geometría Analítica | 1 / 3 | 33.3% |

---

## 🎯 Cursos por materia

### ✅ Completados
- Teorema de Pitágoras (Geometría) — 13 lecciones
- [[Cursos/Aritmética/Números enteros/00 - Índice del curso|Números enteros]] (Aritmética) — 26 videos → 11 clases + 11 guías de estudio + 5 evaluaciones (NotebookLM)
- Números decimales (Aritmética) — 26 lecciones
- Fracciones (Aritmética) — 77 lecciones
- Suma de expresiones algebraicas (Álgebra) — 7 clases
- Plano Cartesiano (Geometría Analítica) — 4 clases
- [[Cursos/Aritmética/Razones y proporciones/00 - Índice del curso|Razones y proporciones / Regla de tres]] (Aritmética) — 57 videos → 10 clases curadas + 4 evaluaciones
- [[Cursos/Álgebra/Caída libre/00 - Índice del curso|Caída libre]] (Álgebra) — 12 videos → 4 clases + 4 guías de estudio + 1 evaluación + 1 planificación + 2 slides

### ⏳ En progreso
- (Ninguno)

### ⏭️ Próximos (recomendados por velocidad)
1. Jerarquía de operaciones (Aritmética) — 8 lecciones
2. Lenguaje Algebraico (Álgebra) — 7 lecciones
3. Ángulos (Geometría) — 6 lecciones

---

## 📚 Materia con más avance

```dataview
TABLE file.folder AS Materia
FROM "Cursos"
WHERE contains(file.path, "00 - Índice")
SORT file.folder ASC
```

---

## 🔗 Accesos rápidos

| Sección | Enlace |
|---------|--------|
| Mapa de cursos | [[Cursos/00 - Mapa de cursos]] |
| Biblioteca de Prompts | [[BIBLIOTECA DE PROMPT/00 - Índice]] |
| Portafolio Matemáticas | [[Matemáticas Básica Superior/00 - Índice]] |
| Números enteros | [[Cursos/Aritmética/Números enteros/00 - Índice del curso]] |
| Teorema de Pitágoras | [[Cursos/Geometría/Teorema de Pitágoras/00 - Índice del curso]] |

---

## ⚡ Última actualización

- **Fecha:** 2026-04-26
- **Cursos completados:** Números enteros — recreado con NotebookLM (26 videos → 11 clases, 11 guías de estudio, 5 evaluaciones formativas)
- **Progreso actual:** 7/28 cursos completados, 223/481 lecciones (46.4%)
- **Próxima meta:** Jerarquía de operaciones (Aritmética) o Lenguaje Algebraico (Álgebra)
