# 📊 Portafolio Docente de Matemáticas — Educación General Básica y Bachillerato
# 📐 Python Mathematical & Educational Portfolio (Portafolio de Matemáticas)

¡Bienvenido al repositorio oficial del **Portafolio Docente de Matemáticas**! Este proyecto es un ecosistema educativo digital y automatizado de nivel premium que recopila, estructura y genera recursos pedagógicos de alta calidad basados en las lecciones y videotutoriales de matemáticas más populares y de mayor excelencia en habla hispana (especialmente del canal *Matemáticas Profe Alex*).
Una biblioteca estructurada de algoritmos matemáticos y lógicos desarrollados en **Python 3**. Este proyecto fue diseñado como una herramienta didáctica para la demostración práctica de conceptos matemáticos, físicos y algebraicos en el aula técnica, ideal para la docencia técnica e interactiva.

El portafolio cubre **83 cursos completos** estructurados con rigor pedagógico y listos para su uso directo en el aula escolar y colegial.
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Topic](https://img.shields.io/badge/Focus-Mathematics%20%26%20Education-orange?style=flat-square)](https://en.wikipedia.org/wiki/Mathematics_education)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

---

## 🎯 Propósito del Proyecto
## 🌟 Características y Módulos

El objetivo principal es proveer a docentes y estudiantes de un conjunto integrado de recursos didácticos de excelencia en formato digital (Markdown/PDF) e institucional (Word `.docx`), reduciendo a cero el tiempo de preparación de material administrativo y curricular para que los educadores puedan enfocarse al 100% en la enseñanza y el acompañamiento pedagógico.
El portafolio contiene scripts lógicos organizados por áreas de estudio matemático:

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
*   **Álgebra Lógica y Aritmética:**
    *   Algoritmos para cálculo de factores, máximo común divisor (MCD) y mínimo común múltiplo (mcm).
    *   Generación de sucesiones matemáticas complejas (como la sucesión de Fibonacci) y validación de números primos.
*   **Geometría Computacional:**
    *   Cálculo interactivo de áreas, perímetros y volúmenes de cuerpos geométricos planos y tridimensionales.
    *   Lógica trigonométrica para resolución de triángulos rectángulos y oblicuángulos.
*   **Visualización en Consola:**
    *   Interfaces amigables por consola que permiten a los estudiantes interactuar ingresando parámetros reales y visualizando el desglose paso a paso del resultado.

---

## 📈 Estadísticas Generales del Repositorio
## 🛠️ Tecnologías

* **Cursos Totales en el Portafolio:** **83**
* **Contenido de Texto Generado (Clases, Guías, Planificaciones, Evaluaciones):** **100% Completado** (en los 83 cursos).
* **Evaluaciones y Solucionarios convertidos a Word (`.docx`):** **227 archivos Word** institucionales compilados a la perfección.
* **Presentaciones PDF de Diapositivas generadas:** **130+ presentaciones** y cubriendo de forma autónoma las materias principales del portafolio.
*   **Lenguaje:** Python 3 (uso estricto de la biblioteca nativa `math` y estructuras lógicas de control modular).
*   **Enfoque Pedagógico:** Estructurado bajo principios de Aprendizaje Basado en Proyectos (ABP) para facilitar su explicación en entornos de educación virtual y laboratorios informáticos.

---

## 🛠️ Motores de Automatización (Root Tools)

El repositorio cuenta con 3 potentes motores en Python que orquestan e interactúan de forma nativa con las APIs de Google (NotebookLM) para la generación y compilación de materiales:

1. **[`crear_curso_notebooklm.py`](file:///C:/Users/braya/OneDrive/Documentos/4%20portafolio/crear_curso_notebooklm.py):** El núcleo de automatización. Se conecta a NotebookLM, asocia fuentes de video, estructura el cuaderno, genera el contenido de texto (clases, guías, evaluaciones) y compila las diapositivas visuales del curso en PDF.
2. **[`md_a_word.py`](file:///C:/Users/braya/OneDrive/Documentos/4%20portafolio/md_a_word.py):** Un transpilador robusto que lee las hojas de evaluación y solucionarios en Markdown (`.md`) y las convierte instantáneamente en documentos Word `.docx` con un formato corporativo institucional impecable (tablas alineadas, cabeceras estructuradas y espaciado docente).
3. **[`autopilot_cursos.py`](file:///C:/Users/braya/OneDrive/Documentos/4%20portafolio/autopilot_cursos.py):** Orquestador en piloto automático capaz de iterar secuencialmente a través del mapa de cursos para generar contenidos en lote, incluyendo control robusto de rate limits y reintentos automáticos de red.
## 🚀 Uso y Ejecución Local

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
### 1. Clonar el Repositorio
```bash
git clone https://github.com/bryanruiz1028/portafolio-matematicas.git
cd portafolio-matematicas
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
### 2. Ejecución
Puedes ejecutar cualquiera de los módulos interactivos por consola directamente:
```bash
python algebra_basica.py
# O bien:
python geometria_analitica.py
```

---

## 📜 Licencia y Uso
Este portafolio ha sido diseñado y estructurado de forma privada para el desarrollo pedagógico y la excelencia del docente de matemáticas. Si deseas sugerir mejoras o reportar detalles, puedes documentarlo en tu panel de control de Obsidian `DASHBOARD.md`.
## 📄 Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
