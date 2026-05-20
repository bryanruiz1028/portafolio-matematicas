#!/bin/bash

set -e  # Salir si hay error

NOTEBOOK_ID="82d8b1db-2caf-4f20-b03f-e03f60de1000"
COURSE_DIR="/c/Users/braya/OneDrive/Documentos/4 portafolio/Cursos/Geometría/Teorema de Pitágoras"
export PYTHONIOENCODING=utf-8

echo "🚀 GENERACIÓN COMPLETA DEL CURSO — TEOREMA DE PITÁGORAS"
echo "======================================================"
echo "Tiempo estimado: 90-120 minutos"
echo ""

# ==================== CLASES 2-8 ====================
echo "📚 GENERANDO CLASES 2-8..."

declare -a class_configs=(
  "2|Verificar si un triángulo es rectángulo"
  "3|Encontrar lados desconocidos (Hipotenusa y Catetos)"
  "4|Curiosidades y propiedades especiales"
  "5|Ejercicios progresivos de aplicación"
  "6|Aplicaciones — Perímetro y área de triángulos equiláteros"
  "7|Aplicaciones — Área de un rombo"
  "8|Cálculo de raíces cuadradas sin calculadora"
)

for config in "${class_configs[@]}"; do
  IFS='|' read -r class_num title <<< "$config"

  echo "  ⏳ Clase $class_num: $title"

  prompt="Genera la Clase $class_num completa en español sobre $title.
Usa Obsidian/Admonition boxes (ad-note, ad-example, ad-question, ad-success).
Incluye:
- ¿Por qué es importante? (ejemplos en \$USD)
- Concepto clave (nota, warning, tip)
- Procedimiento con 4-5 ejemplos
- Ejercicios 🟢 Fácil 🟡 Medio 🔴 Avanzado
- Respuestas para docente
- Mini-prueba (3 preguntas)
- Navegación con wikilinks"

  output=$(PYTHONIOENCODING=utf-8 notebooklm generate report --format custom --language es --notebook "$NOTEBOOK_ID" --append "$prompt" --json 2>&1)
  task_id=$(echo "$output" | grep -o '"task_id":"[^"]*"' | head -1 | cut -d'"' -f4)

  if [ ! -z "$task_id" ]; then
    echo "  ✓ Task ID: ${task_id:0:8}..."

    # Esperar a que se complete
    echo "  ⏳ Esperando completitud..."
    notebooklm artifact wait "$task_id" --notebook "$NOTEBOOK_ID" --timeout 900 2>&1 | tail -1

    # Descargar
    filename="Clase $(printf '%02d' $class_num) - $title.md"
    notebooklm download report "$COURSE_DIR/$filename" -a "$task_id" -n "$NOTEBOOK_ID" 2>&1 | tail -1
    echo "  ✓ Descargada: $filename"
    echo ""
  else
    echo "  ✗ Error generando Clase $class_num"
  fi
done

# ==================== PRESENTACIONES 1-8 ====================
echo "📊 GENERANDO PRESENTACIONES 1-8..."

declare -a presentation_titles=(
  "1|Introducción al Teorema de Pitágoras"
  "2|Verificar si un triángulo es rectángulo"
  "3|Encontrar lados desconocidos"
  "4|Curiosidades y propiedades"
  "5|Ejercicios progresivos"
  "6|Triángulos equiláteros"
  "7|Área de un rombo"
  "8|Raíces sin calculadora"
)

for config in "${presentation_titles[@]}"; do
  IFS='|' read -r class_num title <<< "$config"

  echo "  ⏳ Presentación $class_num: $title"

  prompt="Presentación PROYECTOR — Clase $class_num: $title
DISEÑO:
- Tipografía: Bold/ExtraBold, 20-40px
- Contraste fuerte (fondo oscuro + texto claro)
- Máximo 5 líneas por slide
- Incluir ejemplo con \$USD
- Sin gradientes/sombras
Nivel: Básica Superior"

  output=$(PYTHONIOENCODING=utf-8 notebooklm generate slide-deck --language es --notebook "$NOTEBOOK_ID" --append "$prompt" --json 2>&1)
  task_id=$(echo "$output" | grep -o '"task_id":"[^"]*"' | head -1 | cut -d'"' -f4)

  if [ ! -z "$task_id" ]; then
    echo "  ✓ Task ID: ${task_id:0:8}..."

    # Esperar y descargar
    notebooklm artifact wait "$task_id" --notebook "$NOTEBOOK_ID" --timeout 900 2>&1 | tail -1
    filename="Presentación - Clase $(printf '%02d' $class_num).pdf"
    notebooklm download slide-deck "$COURSE_DIR/$filename" -a "$task_id" -n "$NOTEBOOK_ID" 2>&1 | tail -1
    echo "  ✓ Descargada: $filename"
    echo ""
  fi
done

# ==================== GUÍAS DE ESTUDIO 1-8 ====================
echo "📖 GENERANDO GUÍAS DE ESTUDIO 1-8..."

for class_num in {1..8}; do
  echo "  ⏳ Guía $class_num"

  output=$(PYTHONIOENCODING=utf-8 notebooklm generate report --format study-guide --language es --notebook "$NOTEBOOK_ID" --append "Guía de estudio Clase $class_num. Lenguaje simple para Básica Superior (12-15 años)." --json 2>&1)
  task_id=$(echo "$output" | grep -o '"task_id":"[^"]*"' | head -1 | cut -d'"' -f4)

  if [ ! -z "$task_id" ]; then
    echo "  ✓ Task ID: ${task_id:0:8}..."

    notebooklm artifact wait "$task_id" --notebook "$NOTEBOOK_ID" --timeout 900 2>&1 | tail -1
    filename="Guía de estudio - Clase $(printf '%02d' $class_num).md"
    notebooklm download report "$COURSE_DIR/$filename" -a "$task_id" -n "$NOTEBOOK_ID" 2>&1 | tail -1
    echo "  ✓ Descargada: $filename"
    echo ""
  fi
done

# ==================== EVALUACIONES FORMATIVAS ====================
echo "📝 GENERANDO EVALUACIONES FORMATIVAS (BLOQUES 1-3)..."

declare -a evaluation_topics=(
  "1|Conceptos fundamentales del Teorema de Pitágoras"
  "2|Aplicaciones geométricas"
  "3|Problemas y ejercicios complejos"
)

for config in "${evaluation_topics[@]}"; do
  IFS='|' read -r bloque tema <<< "$config"

  echo "  ⏳ Evaluación Bloque $bloque: $tema"

  prompt="EVALUACIÓN FORMATIVA — Bloque $bloque: $tema
Genera DOS DOCUMENTOS separados:

DOCUMENTO 1 — VERSIÓN ESTUDIANTE
# EVALUACIÓN FORMATIVA: $tema
Nombre: __________ Curso: __________ Fecha: __________

10 preguntas / 10 puntos:
- Sección I: 3 selección múltiple (3pts)
- Sección II: 2 V/F (2pts)
- Sección III: 2 completar (2pts)
- Sección IV: 1 relacionar (1pt)
- Sección V: 1 resolver 🟢 (1pt)
- Sección VI: 1 aplicación \$USD (1pt)

DOCUMENTO 2 — RESPUESTAS DOCENTE
- Respuestas con justificación
- Rúbrica: Logrado/En proceso/Por lograr
- Escala: 10=100% | 8-9=Muy bueno | 6-7=Satisfactorio | <6=Necesita refuerzo"

  output=$(PYTHONIOENCODING=utf-8 notebooklm generate report --format custom --language es --notebook "$NOTEBOOK_ID" --append "$prompt" --json 2>&1)
  task_id=$(echo "$output" | grep -o '"task_id":"[^"]*"' | head -1 | cut -d'"' -f4)

  if [ ! -z "$task_id" ]; then
    echo "  ✓ Task ID: ${task_id:0:8}..."

    notebooklm artifact wait "$task_id" --notebook "$NOTEBOOK_ID" --timeout 900 2>&1 | tail -1
    filename="Evaluación - Bloque $(printf '%02d' $bloque) — $tema.md"
    notebooklm download report "$COURSE_DIR/$filename" -a "$task_id" -n "$NOTEBOOK_ID" 2>&1 | tail -1
    echo "  ✓ Descargada: $filename"
    echo ""
  fi
done

# ==================== PLANIFICACIONES DUA ====================
echo "📋 GENERANDO PLANIFICACIONES DUA (BLOQUES 1-3)..."

declare -a planning_topics=(
  "1|Conceptos fundamentales del Teorema de Pitágoras"
  "2|Aplicaciones geométricas"
  "3|Ejercicios y problemas complejos"
)

for config in "${planning_topics[@]}"; do
  IFS='|' read -r bloque tema <<< "$config"

  echo "  ⏳ Planificación Bloque $bloque: $tema"

  prompt="📋 PLANIFICACIÓN DIDÁCTICA DUA — Bloque $bloque: $tema
Nivel: Básica Superior | Duración: 80 minutos

# 📋 Planificación — $tema
tags: #planificacion #dua

## Tema / Metodología
Colaborativo formal, 2-3 líneas

## Secuencia Didáctica

### 🔵 ANTICIPACIÓN (20 min)
> [!abstract] Actividad de inicio (qué y cómo)
> [!note] Enfoque DUA: - **Qué:** / - **Cómo:**

### 🟡 CONSTRUCCIÓN (40 min)
> [!example] Actividades centrales
> [!note] Enfoque DUA

### 🟢 CONSOLIDACIÓN (20 min)
> [!success] Actividad de cierre
> [!note] Enfoque DUA

## Recursos
| Recurso | Tipo | Uso |
| Pizarra | Base | Explicaciones |
| Marcadores | Base | Escritura |
| Fichas | Apoyo | Ejercicios |
| Impresora | Distribución | Materiales |
| [Recurso adicional] | Propuesto | [Uso] |"

  output=$(PYTHONIOENCODING=utf-8 notebooklm generate report --format custom --language es --notebook "$NOTEBOOK_ID" --append "$prompt" --json 2>&1)
  task_id=$(echo "$output" | grep -o '"task_id":"[^"]*"' | head -1 | cut -d'"' -f4)

  if [ ! -z "$task_id" ]; then
    echo "  ✓ Task ID: ${task_id:0:8}..."

    notebooklm artifact wait "$task_id" --notebook "$NOTEBOOK_ID" --timeout 900 2>&1 | tail -1
    filename="Planificación - Bloque $(printf '%02d' $bloque) — $tema.md"
    notebooklm download report "$COURSE_DIR/$filename" -a "$task_id" -n "$NOTEBOOK_ID" 2>&1 | tail -1
    echo "  ✓ Descargada: $filename"
    echo ""
  fi
done

echo "======================================================"
echo "✅ GENERACIÓN COMPLETADA"
echo "======================================================"
echo ""
echo "📊 RESUMEN DE ARCHIVOS GENERADOS:"
echo ""

cd "$COURSE_DIR"
echo "CLASES:"
ls -1 Clase\ *.md 2>/dev/null | wc -l
echo "archivos"
echo ""

echo "PRESENTACIONES:"
ls -1 Presentación\ *.pdf 2>/dev/null | wc -l
echo "archivos"
echo ""

echo "GUÍAS DE ESTUDIO:"
ls -1 Guía\ *.md 2>/dev/null | wc -l
echo "archivos"
echo ""

echo "EVALUACIONES:"
ls -1 Evaluación\ *.md 2>/dev/null | wc -l
echo "archivos"
echo ""

echo "PLANIFICACIONES:"
ls -1 Planificación\ *.md 2>/dev/null | wc -l
echo "archivos"
echo ""

echo "📂 TOTAL DE ARCHIVOS:"
ls -1 | wc -l
echo "archivos en la carpeta del curso"
echo ""
echo "✨ ¡Curso listo para usar en Obsidian!"
