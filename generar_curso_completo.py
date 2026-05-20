#!/usr/bin/env python3
import subprocess
import json
import os
import time
from pathlib import Path

NOTEBOOK_ID = "82d8b1db-2caf-4f20-b03f-e03f60de1000"
VAULT_PATH = r"C:\Users\braya\OneDrive\Documentos\4 portafolio"
COURSE_PATH = Path(VAULT_PATH) / "Cursos" / "Geometría" / "Teorema de Pitágoras"
COURSE_PATH.mkdir(parents=True, exist_ok=True)

tasks = {
    "clases": [],
    "presentaciones": [],
    "guias": [],
    "evaluaciones": [],
    "planificaciones": []
}

def run_notebooklm(cmd):
    """Ejecutar comando notebooklm con encoding UTF-8"""
    env = os.environ.copy()
    env['PYTHONIOENCODING'] = 'utf-8'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, env=env, cwd=VAULT_PATH)
    return result.returncode, result.stdout, result.stderr

def generate_clases():
    """Generar las 7 clases restantes (2-8)"""
    print("\n🎓 Generando CLASES 2-8...")

    clases_config = [
        (2, "Verificar si un triángulo es rectángulo"),
        (3, "Encontrar lados desconocidos (Hipotenusa y Catetos)"),
        (4, "Curiosidades y propiedades especiales"),
        (5, "Ejercicios progresivos de aplicación"),
        (6, "Aplicaciones — Perímetro y área de triángulos equiláteros"),
        (7, "Aplicaciones — Área de un rombo"),
        (8, "Cálculo de raíces cuadradas sin calculadora"),
    ]

    for class_num, title in clases_config:
        prompt = f"""Genera la Clase {class_num} completa en español sobre {title}.
Usa Obsidian/Admonition boxes (ad-note, ad-example, ad-question, ad-success, ad-abstract).
Incluye:
- ¿Por qué es importante? (con ejemplos en USD)
- Concepto clave (nota, warning, tip)
- Procedimiento paso a paso (4-5 ejemplos)
- Ejercicios 🟢 Fácil 🟡 Medio 🔴 Avanzado
- Respuestas para docente
- Mini-prueba (3 preguntas)
- Navegación inicial y final con wikilinks."""

        cmd = f'PYTHONIOENCODING=utf-8 notebooklm generate report --format custom --language es --notebook {NOTEBOOK_ID} --json <<\'EOF\'\n{prompt}\nEOF'

        returncode, stdout, stderr = run_notebooklm(cmd)
        if returncode == 0:
            try:
                data = json.loads(stdout)
                tasks["clases"].append({
                    "class": class_num,
                    "title": title,
                    "task_id": data.get("task_id"),
                    "status": data.get("status")
                })
                print(f"  ✓ Clase {class_num}: {data.get('task_id', 'N/A')[:8]}...")
            except:
                print(f"  ✗ Clase {class_num}: Error parsing JSON")
        else:
            print(f"  ✗ Clase {class_num}: Error")

def generate_presentaciones():
    """Generar 8 presentaciones para proyector"""
    print("\n📊 Generando PRESENTACIONES 1-8...")

    clases_config = [
        (1, "Introducción al Teorema de Pitágoras"),
        (2, "Verificar si un triángulo es rectángulo"),
        (3, "Encontrar lados desconocidos"),
        (4, "Curiosidades y propiedades"),
        (5, "Ejercicios progresivos"),
        (6, "Triángulos equiláteros"),
        (7, "Área de un rombo"),
        (8, "Raíces sin calculadora"),
    ]

    for class_num, title in clases_config:
        prompt = f"""Presentación para PROYECTOR — Clase {class_num}: {title}

DISEÑO OBLIGATORIO:
- Tipografía: Bold/ExtraBold, mínimo 20-40px
- Contraste fuerte: fondo oscuro/claro con texto muy visible
- Máximo 5 líneas por diapositiva
- Incluir ejemplo con \$USD
- Sin gradientes, sombras ni efectos sutiles
- Barras y separadores: 10-14px, redondeadas

Nivel: Básica Superior (12-15 años)"""

        cmd = f'PYTHONIOENCODING=utf-8 notebooklm generate slide-deck --language es --notebook {NOTEBOOK_ID} --json <<\'EOF\'\n{prompt}\nEOF'

        returncode, stdout, stderr = run_notebooklm(cmd)
        if returncode == 0:
            try:
                data = json.loads(stdout)
                tasks["presentaciones"].append({
                    "class": class_num,
                    "task_id": data.get("task_id"),
                })
                print(f"  ✓ Presentación {class_num}: {data.get('task_id', 'N/A')[:8]}...")
            except:
                print(f"  ✗ Presentación {class_num}: Error parsing JSON")

def generate_guias():
    """Generar 8 guías de estudio"""
    print("\n📖 Generando GUÍAS DE ESTUDIO 1-8...")

    clases = list(range(1, 9))

    for class_num in clases:
        prompt = f"Guía de estudio para Clase {class_num}. Lenguaje simple, Básica Superior."

        cmd = f'PYTHONIOENCODING=utf-8 notebooklm generate report --format study-guide --language es --notebook {NOTEBOOK_ID} --append "{prompt}" --json'

        returncode, stdout, stderr = run_notebooklm(cmd)
        if returncode == 0:
            try:
                data = json.loads(stdout)
                tasks["guias"].append({
                    "class": class_num,
                    "task_id": data.get("task_id"),
                })
                print(f"  ✓ Guía {class_num}: {data.get('task_id', 'N/A')[:8]}...")
            except:
                print(f"  ✗ Guía {class_num}: Error parsing JSON")

def generate_evaluaciones():
    """Generar evaluaciones formativas (por bloque)"""
    print("\n📝 Generando EVALUACIONES FORMATIVAS (bloques 1-3)...")

    bloques = [
        (1, "Introducción y conceptos básicos"),
        (2, "Aplicaciones prácticas"),
        (3, "Ejercicios avanzados"),
    ]

    for bloque_num, tema in bloques:
        prompt = f"""Genera EVALUACIÓN FORMATIVA: {tema} (Bloque {bloque_num})
Produce DOS DOCUMENTOS SEPARADOS:

DOCUMENTO 1 — VERSIÓN ESTUDIANTE
# EVALUACIÓN FORMATIVA: {tema}
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
- Rúbrica
- Escala de calificación"""

        cmd = f'PYTHONIOENCODING=utf-8 notebooklm generate report --format custom --language es --notebook {NOTEBOOK_ID} --append "{prompt}" --json'

        returncode, stdout, stderr = run_notebooklm(cmd)
        if returncode == 0:
            try:
                data = json.loads(stdout)
                tasks["evaluaciones"].append({
                    "bloque": bloque_num,
                    "task_id": data.get("task_id"),
                })
                print(f"  ✓ Evaluación Bloque {bloque_num}: {data.get('task_id', 'N/A')[:8]}...")
            except:
                print(f"  ✗ Evaluación {bloque_num}: Error")

def generate_planificaciones():
    """Generar planificaciones DUA (por bloque)"""
    print("\n📋 Generando PLANIFICACIONES DUA (bloques 1-3)...")

    bloques = [
        (1, "Conceptos fundamentales del Teorema de Pitágoras"),
        (2, "Aplicaciones geométricas"),
        (3, "Problemas y ejercicios complejos"),
    ]

    for bloque_num, tema in bloques:
        prompt = f"""Planificación Didáctica DUA — Bloque {bloque_num}: {tema}
Nivel: Básica Superior | Duración: 80 minutos

Formato:
# 📋 Planificación — {tema}
tags: #planificacion #dua

## Tema / Metodología (colaborativo)

## Secuencia Didáctica

### 🔵 ANTICIPACIÓN (20 min)
> [!abstract] Actividad inicio
> [!note] Enfoque DUA

### 🟡 CONSTRUCCIÓN (40 min)
> [!example] Actividades centrales
> [!note] Enfoque DUA

### 🟢 CONSOLIDACIÓN (20 min)
> [!success] Cierre
> [!note] Enfoque DUA

## Recursos
Pizarra, Marcadores, Fichas, Impresora + 1 adicional sugerido."""

        cmd = f'PYTHONIOENCODING=utf-8 notebooklm generate report --format custom --language es --notebook {NOTEBOOK_ID} --append "{prompt}" --json'

        returncode, stdout, stderr = run_notebooklm(cmd)
        if returncode == 0:
            try:
                data = json.loads(stdout)
                tasks["planificaciones"].append({
                    "bloque": bloque_num,
                    "task_id": data.get("task_id"),
                })
                print(f"  ✓ Planificación Bloque {bloque_num}: {data.get('task_id', 'N/A')[:8]}...")
            except:
                print(f"  ✗ Planificación {bloque_num}: Error")

def main():
    print("=" * 60)
    print("🚀 GENERANDO CURSO COMPLETO — TEOREMA DE PITÁGORAS")
    print("=" * 60)
    print(f"📁 Notebook: {NOTEBOOK_ID[:8]}...")
    print(f"💾 Ruta: {COURSE_PATH}")

    # Generar todos en paralelo
    generate_clases()
    time.sleep(2)
    generate_presentaciones()
    time.sleep(2)
    generate_guias()
    time.sleep(2)
    generate_evaluaciones()
    time.sleep(2)
    generate_planificaciones()

    # Guardar configuración de tareas
    with open(COURSE_PATH / "generacion_tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 60)
    print(f"✓ {sum(len(v) for v in tasks.values())} tareas iniciadas")
    print("=" * 60)
    print(f"\n📌 IDs de tareas guardados en: generacion_tasks.json")
    print("\n⏳ Esperando generación de todos los artefactos...")
    print("⏸️  Esto puede tomar 60-90 minutos...")

if __name__ == "__main__":
    main()
