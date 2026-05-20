#!/bin/bash

NOTEBOOK_ID="82d8b1db-2caf-4f20-b03f-e03f60de1000"
COURSE_DIR="/c/Users/braya/OneDrive/Documentos/4 portafolio/Cursos/Geometría/Teorema de Pitágoras"
TASKS_FILE="$COURSE_DIR/tasks_ids.txt"

export PYTHONIOENCODING=utf-8

echo "📥 DESCARGANDO TODOS LOS MATERIALES DEL CURSO"
echo "=============================================="

# Función para descargar por tipo
download_by_type() {
  local type=$1
  local extension=$2

  echo ""
  echo "Descargando $type..."

  grep "^${type}:" "$TASKS_FILE" | while IFS=':' read -r tipo_line class_or_bloque task_id; do
    case $type in
      "clase")
        local filename="Clase $(printf '%02d' $class_or_bloque) - Contenido.md"
        notebooklm download report "$COURSE_DIR/$filename" -a "$task_id" -n "$NOTEBOOK_ID" 2>&1 | grep -E "Downloaded|Error" &
        ;;
      "presentacion")
        local filename="Presentación - Clase $(printf '%02d' $class_or_bloque).pdf"
        notebooklm download slide-deck "$COURSE_DIR/$filename" -a "$task_id" -n "$NOTEBOOK_ID" 2>&1 | grep -E "Downloaded|Error" &
        ;;
      "guia")
        local filename="Guía de estudio - Clase $(printf '%02d' $class_or_bloque).md"
        notebooklm download report "$COURSE_DIR/$filename" -a "$task_id" -n "$NOTEBOOK_ID" 2>&1 | grep -E "Downloaded|Error" &
        ;;
      "evaluacion")
        local filename="Evaluación - Bloque $(printf '%02d' $class_or_bloque).md"
        notebooklm download report "$COURSE_DIR/$filename" -a "$task_id" -n "$NOTEBOOK_ID" 2>&1 | grep -E "Downloaded|Error" &
        ;;
      "planificacion")
        local filename="Planificación - Bloque $(printf '%02d' $class_or_bloque).md"
        notebooklm download report "$COURSE_DIR/$filename" -a "$task_id" -n "$NOTEBOOK_ID" 2>&1 | grep -E "Downloaded|Error" &
        ;;
    esac
  done

  wait
}

# Descargar todos los tipos
download_by_type "clase" "md"
download_by_type "presentacion" "pdf"
download_by_type "guia" "md"
download_by_type "evaluacion" "md"
download_by_type "planificacion" "md"

echo ""
echo "=============================================="
echo "✓ Descarga completada"
echo ""
echo "📂 Archivos disponibles en:"
echo "   $COURSE_DIR"
ls -lh "$COURSE_DIR" | grep -E "\.(md|pdf)$" | wc -l
echo "   archivos descargados"
