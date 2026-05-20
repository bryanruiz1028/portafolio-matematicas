#!/bin/bash

NOTEBOOK_ID="82d8b1db-2caf-4f20-b03f-e03f60de1000"

# IDs de los 10 primeros videos (omitiendo los 3 duplicados)
VIDEO_IDS=(
  "5Imh8A4CRsI"
  "cJAxWOZuqaE"
  "uJ5YDrls9yc"
  "ViQI54Sy6rE"
  "by2Mfjybn70"
  "Ev4zMeZGwgU"
  "Vs1-YgEoz9o"
  "YLBIkGDbPTE"
  "5H7UXORD0-I"
  "hBGLgGU7DvE"
)

# Agregar cada video
for VIDEO_ID in "${VIDEO_IDS[@]}"; do
  echo "Agregando video: $VIDEO_ID"
  PYTHONIOENCODING=utf-8 notebooklm source add "https://youtube.com/watch?v=$VIDEO_ID" \
    --notebook "$NOTEBOOK_ID" \
    --json 2>&1 | grep -E '"(id|title)"' &
done

wait
echo "Todos los videos han sido agregados"
