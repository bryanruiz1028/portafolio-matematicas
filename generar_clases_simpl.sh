#!/bin/bash

NOTEBOOK_ID="82d8b1db-2caf-4f20-b03f-e03f60de1000"
COURSE_DIR="/c/Users/braya/OneDrive/Documentos/4 portafolio/Cursos/Geometría/Teorema de Pitágoras"
export PYTHONIOENCODING=utf-8

echo "📚 GENERANDO CLASES 2-8 (de forma simple y robusta)"
echo "=================================================="
echo ""

# Función para generar una clase
generar_clase() {
  local num=$1
  local titulo=$2

  echo "🔄 Clase $num: $titulo"

  # Generar y guardar JSON en archivo temporal
  local json_tmp="/tmp/clase_${num}_output.json"

  notebooklm generate report \
    --format custom \
    --language es \
    --notebook "$NOTEBOOK_ID" \
    --append "Clase $num sobre $titulo. Usa Obsidian/Admonition. Incluye: importancia con USD, conceptos, procedimiento con ejemplos, ejercicios 🟢🟡🔴, respuestas, mini-prueba, navegación." \
    --json > "$json_tmp" 2>&1

  # Extraer task_id de forma más robusta
  local task_id=$(cat "$json_tmp" | grep -o 'task_id":"[^"]*' | head -1 | cut -d'"' -f2)

  if [ -z "$task_id" ]; then
    echo "  ❌ Error: No se pudo extraer task_id"
    echo "  📄 Output: $(cat $json_tmp | head -5)"
    return 1
  fi

  echo "  ✓ Task ID: $task_id"

  # Esperar a que se complete
  echo "  ⏳ Esperando completitud..."
  notebooklm artifact wait "$task_id" --notebook "$NOTEBOOK_ID" --timeout 900 >/dev/null 2>&1

  if [ $? -ne 0 ]; then
    echo "  ❌ Error esperando artifact"
    return 1
  fi

  # Descargar
  local filename="Clase $(printf '%02d' $num) - $titulo.md"
  echo "  💾 Descargando: $filename"

  notebooklm download report "$COURSE_DIR/$filename" -a "$task_id" -n "$NOTEBOOK_ID" >/dev/null 2>&1

  if [ -f "$COURSE_DIR/$filename" ]; then
    local size=$(du -h "$COURSE_DIR/$filename" | cut -f1)
    echo "  ✅ OK ($size)"
    rm -f "$json_tmp"
    return 0
  else
    echo "  ❌ Error descargando"
    return 1
  fi
}

# Generar clases 2-8
generar_clase 2 "Verificar si un triángulo es rectángulo" &
wait $!

generar_clase 3 "Encontrar lados desconocidos" &
wait $!

generar_clase 4 "Curiosidades y propiedades especiales" &
wait $!

generar_clase 5 "Ejercicios progresivos de aplicación" &
wait $!

generar_clase 6 "Aplicaciones — Triángulos equiláteros" &
wait $!

generar_clase 7 "Aplicaciones — Área de un rombo" &
wait $!

generar_clase 8 "Cálculo de raíces sin calculadora" &
wait $!

echo ""
echo "=================================================="
echo "✅ Clases 2-8 generadas"
echo ""
ls -lh "$COURSE_DIR"/Clase\ *.md 2>/dev/null | wc -l
echo "archivos de clases"
