#!/bin/bash

NOTEBOOK_ID="82d8b1db-2caf-4f20-b03f-e03f60de1000"
COURSE_DIR="/c/Users/braya/OneDrive/Documentos/4 portafolio/Cursos/Geometría/Teorema de Pitágoras"
TASKS_FILE="$COURSE_DIR/tasks_ids.txt"

export PYTHONIOENCODING=utf-8

echo "🚀 INICIANDO GENERACIÓN DE CURSO COMPLETO"
echo "=========================================="
echo "Notebook: $NOTEBOOK_ID"
echo "Ruta: $COURSE_DIR"
echo ""

# Crear archivo para almacenar IDs de tareas
> "$TASKS_FILE"

# ==================== CLASES ====================
echo "📚 Generando CLASES 2-8..."

generate_clase() {
  local class_num=$1
  local title=$2

  local prompt="Genera Clase $class_num: $title. Formato Obsidian/Admonition con ejemplos en USD."

  local output=$(notebooklm generate report --format custom --language es --notebook "$NOTEBOOK_ID" --append "$prompt" --json 2>&1)
  local task_id=$(echo "$output" | grep -o '"task_id":"[^"]*"' | cut -d'"' -f4)

  if [ ! -z "$task_id" ]; then
    echo "clase:$class_num:$task_id" >> "$TASKS_FILE"
    echo "  ✓ Clase $class_num: $task_id"
  else
    echo "  ✗ Clase $class_num: Error"
  fi
}

generate_clase 2 "Verificar si un triángulo es rectángulo" &
generate_clase 3 "Encontrar lados desconocidos" &
generate_clase 4 "Curiosidades y propiedades especiales" &
generate_clase 5 "Ejercicios progresivos de aplicación" &
generate_clase 6 "Triángulos equiláteros" &
generate_clase 7 "Área de un rombo" &
generate_clase 8 "Raíces sin calculadora" &

wait
echo ""

# ==================== PRESENTACIONES ====================
echo "📊 Generando PRESENTACIONES 1-8..."

generate_presentacion() {
  local class_num=$1
  local title=$2

  local prompt="Presentación para PROYECTOR: $title. Bold/ExtraBold, contraste fuerte, máximo 5 líneas, con ejemplo USD."

  local output=$(notebooklm generate slide-deck --language es --notebook "$NOTEBOOK_ID" --append "$prompt" --json 2>&1)
  local task_id=$(echo "$output" | grep -o '"task_id":"[^"]*"' | cut -d'"' -f4)

  if [ ! -z "$task_id" ]; then
    echo "presentacion:$class_num:$task_id" >> "$TASKS_FILE"
    echo "  ✓ Presentación $class_num: $task_id"
  fi
}

generate_presentacion 1 "Introducción" &
generate_presentacion 2 "Verificar rectángulo" &
generate_presentacion 3 "Encontrar lados" &
generate_presentacion 4 "Curiosidades" &
generate_presentacion 5 "Ejercicios" &
generate_presentacion 6 "Triángulos equiláteros" &
generate_presentacion 7 "Área rombo" &
generate_presentacion 8 "Raíces" &

wait
echo ""

# ==================== GUÍAS ====================
echo "📖 Generando GUÍAS DE ESTUDIO 1-8..."

generate_guia() {
  local class_num=$1

  local output=$(notebooklm generate report --format study-guide --language es --notebook "$NOTEBOOK_ID" --append "Guía Clase $class_num" --json 2>&1)
  local task_id=$(echo "$output" | grep -o '"task_id":"[^"]*"' | cut -d'"' -f4)

  if [ ! -z "$task_id" ]; then
    echo "guia:$class_num:$task_id" >> "$TASKS_FILE"
    echo "  ✓ Guía $class_num: $task_id"
  fi
}

for i in {1..8}; do
  generate_guia $i &
done

wait
echo ""

# ==================== EVALUACIONES ====================
echo "📝 Generando EVALUACIONES (Bloques 1-3)..."

generate_evaluacion() {
  local bloque=$1
  local tema=$2

  local prompt="Evaluación formativa Bloque $bloque: $tema. Dos documentos separados (estudiante + docente con respuestas y rúbrica). 10 preguntas variadas."

  local output=$(notebooklm generate report --format custom --language es --notebook "$NOTEBOOK_ID" --append "$prompt" --json 2>&1)
  local task_id=$(echo "$output" | grep -o '"task_id":"[^"]*"' | cut -d'"' -f4)

  if [ ! -z "$task_id" ]; then
    echo "evaluacion:$bloque:$task_id" >> "$TASKS_FILE"
    echo "  ✓ Evaluación Bloque $bloque: $task_id"
  fi
}

generate_evaluacion 1 "Conceptos fundamentales" &
generate_evaluacion 2 "Aplicaciones geométricas" &
generate_evaluacion 3 "Problemas complejos" &

wait
echo ""

# ==================== PLANIFICACIONES DUA ====================
echo "📋 Generando PLANIFICACIONES DUA (Bloques 1-3)..."

generate_planificacion() {
  local bloque=$1
  local tema=$2

  local prompt="Planificación DUA Bloque $bloque: $tema. Secuencia didáctica (Anticipación 20min, Construcción 40min, Consolidación 20min). Admonitions boxes. Incluir recursos."

  local output=$(notebooklm generate report --format custom --language es --notebook "$NOTEBOOK_ID" --append "$prompt" --json 2>&1)
  local task_id=$(echo "$output" | grep -o '"task_id":"[^"]*"' | cut -d'"' -f4)

  if [ ! -z "$task_id" ]; then
    echo "planificacion:$bloque:$task_id" >> "$TASKS_FILE"
    echo "  ✓ Planificación Bloque $bloque: $task_id"
  fi
}

generate_planificacion 1 "Conceptos fundamentales" &
generate_planificacion 2 "Aplicaciones geométricas" &
generate_planificacion 3 "Ejercicios avanzados" &

wait
echo ""

echo "=========================================="
echo "✓ $(grep -c ':' "$TASKS_FILE") tareas iniciadas"
echo "📌 IDs guardados en: tasks_ids.txt"
echo ""
echo "⏳ Esperando generación de artefactos..."
echo "⏸️  Esto puede tomar 60-90 minutos..."
