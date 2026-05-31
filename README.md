# 📊 Portafolio Docente de Matemáticas — Educación General Básica y Bachillerato

¡Bienvenido al repositorio oficial del **Portafolio Docente de Matemáticas**! Este proyecto es un ecosistema educativo digital y automatizado de nivel premium que recopila, estructura y genera recursos pedagógicos de alta calidad basados en las lecciones y videotutoriales de matemáticas más populares y de mayor excelencia en habla hispana (especialmente del canal *Matemáticas Profe Alex*).

El portafolio cubre **83 cursos completos** estructurados con rigor pedagógico y listos para su uso directo en el aula escolar y colegial.

---

## 🎯 Propósito del Proyecto

El objetivo principal es proveer a docentes y estudiantes de un conjunto integrado de recursos didácticos de excelencia en formato digital (Markdown/PDF) e institucional (Word `.docx`), reduciendo a cero el tiempo de preparación de material administrativo y curricular para que los educadores puedan enfocarse al 100% en la enseñanza y el acompañamiento pedagógico.

---

## 📚 Componentes por Curso

Cada uno de los **83 cursos** en el portafolio está estructurado dentro de la carpeta [Cursos/](file:///C:/Users/braya/OneDrive/Documentos/4%20portafolio/Cursos/) organizado por áreas y contiene de manera sistemática los siguientes componentes:

1. **📖 Clases Curadas (`Clase XX - ...`)**: Lecciones desarrolladas paso a paso en español con explicaciones claras, teoría concisa y ejemplos prácticos clasificados en tres niveles de dificultad pedagógica:
   - 🟢 **Fácil** (Fundamentación y bases)
   - 🟡 **Medio** (Ejercicios prácticos típicos de examen)
   - 🔴 **Avanzado** (Retos cognitivos de alta complejidad)
2. **📖 Guías de Estudio (`Guía de estudio - Clase XX`)**: Guías didácticas e interactivas diseñadas para que el estudiante ejercite de forma autónoma el tema expuesto en cada clase.
3. **📝 Evaluaciones del Estudiante (`📝 Evaluación - Bloque X`)**: Hojas de evaluación listas para imprimir y aplicar, en formato Markdown y Word (`.docx`).
4. **📋 Respuestas y Solucionarios del Docente (`📋 Respuestas Docente - Bloque X`)**: Respuestas completamente desarrolladas con rúbricas detalladas para el docente (en Markdown y Word `.docx`).
5. **📋 Planificaciones Curriculares (`📋 Planificación - Bloque X`)**: Documentos metodológicos y curriculares organizados por bloques didácticos que detallan destrezas, criterios de evaluación y estrategias de aprendizaje.
6. **📊 Presentaciones en Diapositivas (PDF) (`📊 Presentación - Clase XX`)**: Láminas visuales y pedagógicas listas para proyectarse en la pizarra o compartirse con los estudiantes, generadas en formato PDF interactivo.

---

## 📈 Estadísticas Generales del Repositorio

* **Cursos Totales en el Portafolio:** **83**
* **Contenido de Texto Generado (Clases, Guías, Planificaciones, Evaluaciones):** **100% Completado** (en los 83 cursos).
* **Evaluaciones y Solucionarios convertidos a Word (`.docx`):** **227 archivos Word** institucionales compilados a la perfección.
* **Presentaciones PDF de Diapositivas generadas:** **130+ presentaciones** y cubriendo de forma autónoma las materias principales del portafolio.

---

## 🛠️ Motores de Automatización (Root Tools)

El repositorio cuenta con 3 potentes motores en Python que orquestan e interactúan de forma nativa con las APIs de Google (NotebookLM) para la generación y compilación de materiales:

1. **[`crear_curso_notebooklm.py`](file:///C:/Users/braya/OneDrive/Documentos/4%20portafolio/crear_curso_notebooklm.py):** El núcleo de automatización. Se conecta a NotebookLM, asocia fuentes de video, estructura el cuaderno, genera el contenido de texto (clases, guías, evaluaciones) y compila las diapositivas visuales del curso en PDF.
2. **[`md_a_word.py`](file:///C:/Users/braya/OneDrive/Documentos/4%20portafolio/md_a_word.py):** Un transpilador robusto que lee las hojas de evaluación y solucionarios en Markdown (`.md`) y las convierte instantáneamente en documentos Word `.docx` con un formato corporativo institucional impecable (tablas alineadas, cabeceras estructuradas y espaciado docente).
3. **[`autopilot_cursos.py`](file:///C:/Users/braya/OneDrive/Documentos/4%20portafolio/autopilot_cursos.py):** Orquestador en piloto automático capaz de iterar secuencialmente a través del mapa de cursos para generar contenidos en lote, incluyendo control robusto de rate limits y reintentos automáticos de red.

---

## 📁 Estructura Limpia del Repositorio

El repositorio se encuentra limpio y optimizado, conteniendo únicamente los elementos de producción esenciales:

```
├── .gitignore
├── DASHBOARD.md                        # Obsidian: Estadísticas globales de avance
├── REFERENCIA - Creación de cursos.md  # Obsidian: Documentación técnica del flujo
├── RESUMEN PARA NUEVO CHAT.md          # Obsidian: Resumen de contexto rápido para IA
├── 🤖 Guía - NotebookLM y presentaciones.md # Guía de uso de APIs de diapositivas
├── crear_curso_notebooklm.py           # Script principal: Generador de cursos
├── md_a_word.py                        # Script principal: Compilador de Word (.docx)
├── autopilot_cursos.py                 # Script principal: Orquestador masivo
├── README.md                           # Ficha técnica del portafolio
├── Cursos/                             # Base de datos curricular (83 cursos)
│   ├── Aritmética/
│   ├── Álgebra/
│   ├── Geometría/
│   ├── Geometría Analítica/
│   ├── Estadística/
│   └── Trigonometría/
```

---

## ⚖️ Guía de Uso Rápido (Consola)

### Requisitos Previos:
- Python 3.10 o superior.
- Tener instalada la herramienta CLI oficial de NotebookLM.
- Iniciar sesión en NotebookLM:
  ```powershell
  notebooklm login
  ```

### Comandos Clave:

#### 1. Generar un curso completo en piloto automático (Texto + Word):
```powershell
python crear_curso_notebooklm.py "URL_DE_PLAYLIST_YOUTUBE" --auto --skip-slides
```

#### 2. Compilar evaluaciones de un curso de Markdown a Word (.docx) en lote:
```powershell
python md_a_word.py --todos "Cursos/Álgebra/Nombre del curso" --sin-ia
```

#### 3. Generar y descargar únicamente las presentaciones de diapositivas PDF:
```powershell
$env:PYTHONIOENCODING="utf-8"; python crear_curso_notebooklm.py --solo-slides "Álgebra/Nombre del curso"
```

---

## 📜 Licencia y Uso
Este portafolio ha sido diseñado y estructurado de forma privada para el desarrollo pedagógico y la excelencia del docente de matemáticas. Si deseas sugerir mejoras o reportar detalles, puedes documentarlo en tu panel de control de Obsidian `DASHBOARD.md`.
