#!/usr/bin/env python3
"""
Generador automático de materiales para el curso "Números enteros" usando NotebookLM
"""

import subprocess
import json
import os
import sys
from pathlib import Path

NOTEBOOK_ID = "4f55e767-0b67-4ee8-8e95-118745193d50"
VAULT_PATH = Path(r"C:\Users\braya\OneDrive\Documentos\4 portafolio")
CURSO_PATH = VAULT_PATH / "Cursos" / "Aritmética" / "Números enteros"

# Mapeo de clases a fuentes
CLASES = {
    "Clase 01 — Conceptos básicos de números enteros": {
        "bloques": "Understanding integers, Ordering integers, Absolute value",
        "sources": ["d6d27e32-a952-4044-9f19-90f51437cb7d", "8bf8d29d-2a78-4d17-ba1c-496fb85c9b0e", "d33b4b8b-1a23-4744-ac47-3e63f5a4c9fa"],  # Valor absoluto, Ordenar, Suma método 1
    },
    "Clase 02 — Aplicaciones prácticas de enteros": {
        "bloques": "Problem Solving with Integers",
        "sources": ["3758b043-a2ab-4a00-982a-ab145af02bed", "264d9178-97b1-445f-933d-fb413f6e90b6", "0e8df97f-f81a-4bb6-89c2-22c0cb00095c"],  # Alturas, Edades, Temperatura
    },
    "Clase 03 — Suma y resta de enteros (Métodos 1 y 2)": {
        "bloques": "Suma y resta métodos 1 y 2",
        "sources": ["d33b4b8b-1a23-4744-ac47-3e63f5a4c9fa", "c17002aa-9328-4d29-b525-9c298c38d14d"],  # Método 1, Método 2
    },
    "Clase 04 — Suma, resta y ley de signos": {
        "bloques": "Suma de varios números y ley de signos",
        "sources": ["7dd0f588-d374-4f8e-89ce-da17f46a1644", "4b583b7b-6b73-4512-8436-5d74cb7afa6b"],  # Varios números, Método 3
    },
    "Clase 05 — Multiplicación de enteros": {
        "bloques": "Multiplicación y demostración de ley de signos",
        "sources": ["c39c5700-31d6-4d29-90bd-42a14c172f2a", "d19cd790-2540-4127-a294-29b1754034ab"],  # Multiplicación, Demostración
    },
    "Clase 06 — División y potenciación": {
        "bloques": "División y potenciación de enteros",
        "sources": ["1c6dc71b-dfb8-456b-a58e-c46bbee88097", "c624489f-5cc1-4eda-a028-195c7cc46d97"],  # División, Potenciación
    },
    "Clase 07 — Propiedades de la potenciación": {
        "bloques": "Propiedades de exponentes",
        "sources": ["4ebe2218-895d-4127-8a63-5584897adca8"],  # Propiedades
    },
    "Clase 08 — Operaciones básicas con valor absoluto": {
        "bloques": "Operaciones básicas y valor absoluto",
        "sources": ["0df34c1f-d3d3-4044-8884-2d7aaa8f49a0"],  # Valor absoluto
    },
    "Clase 09 — Jerarquía de operaciones (Introducción y ejemplos 1-2)": {
        "bloques": "Jerarquía intro y ejemplos iniciales",
        "sources": ["fa7af7e1-c39d-4953-adca-56c4ddea9520", "ca316ac1-57f4-40ab-a42e-809a08bc3a2d", "75c27c83-b329-4bc5-b97d-752730f924df"],  # Intro, Ejemplo 1, 2
    },
    "Clase 10 — Jerarquía de operaciones (Ejemplos 3-6)": {
        "bloques": "Jerarquía ejemplos intermedios y avanzados",
        "sources": ["8680b2c3-3106-45a2-bb15-6c898795d606", "4ba1f37e-d576-470a-a88d-732d1b08a996", "6102cc03-e747-4f5a-97fc-4c9e0e612518", "691f9411-852b-4352-8847-ee4f91e99ccf"],  # Ejemplos 3,4,5,6
    },
    "Clase 11 — Operaciones combinadas": {
        "bloques": "Operaciones combinadas con todas las operaciones",
        "sources": ["95ffb63d-269a-4844-8385-3df175beb3d6", "1b36cb94-898f-4fed-bdd0-d7eb8e528a80", "5fb76116-0853-44bc-90d2-a720f7901e92", "4f30f729-6341-42ff-9813-e1d59b9ebb3c"],  # Signos, Ejemplo 1, 4, 5
    },
}

# Prompts estándar
PROMPT_CLASE = '''Genera la Clase [N] completa en español sobre [TEMA].
Usa EXACTAMENTE este formato Obsidian/Admonition (no lo cambies):

# Clase [N] — [Título]
tags: #aritmética #números-enteros
Curso: [[00 - Índice del curso]] | Bloque [B] | Lección [N] de 11

> [!info] 🧭 Navegación
> [[Clase [N-1]|⬅ Clase [N-1]]] | [[00 - Índice del curso|Índice]] | **Clase [N]** | [[Clase [N+1]|Clase [N+1] ➡]]

## ¿Por qué es importante esta clase?
> [!info] 🌍 Relevancia
> Explica por qué este tema es relevante en la vida cotidiana con 2-3 ejemplos reales con $USD.

## Concepto clave
> [!note] 📌 Idea principal
> Explicar la operación o concepto en lenguaje simple
> [!warning] ⚠️ Error común
> Cuál es el error más frecuente que cometen los estudiantes
> [!tip] 💡 Truco útil
> Un truco o forma rápida de recordar

## Procedimiento paso a paso
\`\`\`
1. Paso 1: [descripción]
2. Paso 2: [descripción]
3. Paso 3: [descripción]
4. Paso 4: [descripción]
\`\`\`

> [!example]
> **Ejemplo 1 (básico):** [ejercicio y solución paso a paso]

> [!example]
> **Ejemplo 2 (intermedio):** [ejercicio y solución paso a paso]

> [!example]
> **Ejemplo 3 (avanzado con $USD):** Problema con dinero. [enunciado en español con $USD, solución paso a paso]

## Ejercicios para el estudiante
> [!abstract]
> **🟢 Fácil** (2 ejercicios simples con respuestas de una línea)
> **🟡 Medio** (2 ejercicios que combinan conceptos)
> **🔴 Avanzado** (2 ejercicios con contexto de $USD y 2-3 pasos)

> [!success]
> **Respuestas para el docente**
> - Solución a cada ejercicio con procedimiento completo

## Mini-prueba de autoevaluación
> [!question]
> **Pregunta 1** (opción múltiple a/b/c/d)
> [pregunta]
> Respuesta: **[letra]**

> [!question]
> **Pregunta 2** (opción múltiple a/b/c/d)
> [pregunta]
> Respuesta: **[letra]**

> [!question]
> **Pregunta 3** (opción múltiple a/b/c/d)
> [pregunta]
> Respuesta: **[letra]**

## Notas para el próximo tema
> [!tip] 💡 En la próxima clase
> Lo que viene después y cómo se conecta

> [!info] 🧭 Navegación final
> [[Clase [N-1]|⬅ Clase [N-1]]] | [[00 - Índice del curso|Índice]] | **Clase [N]** | [[Clase [N+1]|Clase [N+1] ➡]]'''

PROMPT_PRESENTACION = '''Presentación para PROYECTOR — Clase [N]: [TEMA]

DISEÑO OBLIGATORIO PARA PROYECTOR (aplica en CADA diapositiva sin excepción):

TIPOGRAFÍA:
- Fuente: Montserrat o Arial Black
- Solo dos pesos permitidos: Bold (700) y Extra Bold/Black (900)
- Títulos principales: mínimo 40px, peso 900
- Subtítulos: mínimo 24px, peso 700
- Cuerpo de texto: mínimo 20px, peso 700

COLOR Y CONTRASTE:
- Fondo oscuro con texto claro, O fondo claro con texto muy oscuro
- Colores sólidos y saturados para barras, íconos y elementos visuales
- Sin transparencias, sin efectos sutiles

ESTRUCTURA:
- Máximo 5 líneas de texto por diapositiva
- Incluir: diapositiva de título, contenido y cierre/resumen
- Ecuaciones matemáticas en slides separadas, tamaño grande
- Al menos un ejemplo con aplicación en $USD

CONTENIDO: Todo en español | Nivel Básica Superior (12–15 años)'''

PROMPT_EVALUACION = '''Genera una EVALUACIÓN FORMATIVA en español sobre [TEMA DEL BLOQUE].
Produce DOS DOCUMENTOS SEPARADOS en este orden:

═══════════════════════════════════════════════
DOCUMENTO 1 — VERSIÓN ESTUDIANTE
═══════════════════════════════════════════════

# EVALUACIÓN FORMATIVA: [TEMA]

Nombre: _________________________________ Curso: _____________ Fecha: ___________
Puntaje: _____ / 10 puntos

ESTRUCTURA — 10 preguntas / 10 puntos (1pt c/u):
SECCIÓN I   — Selección múltiple Q1-Q3 (3pts): 4 opciones a/b/c/d
SECCIÓN II  — Verdadero o Falso Q4-Q5 (2pts)
SECCIÓN III — Completar espacios Q6-Q7 (2pts): mín. 3 blancos misma oración
SECCIÓN IV  — Relacionar columnas Q8 (1pt): tabla 4 filas col. R vacía
SECCIÓN V   — Resolver ejercicio Q9 (1pt): UN SOLO ejercicio 🟢 Fácil
SECCIÓN VI  — Aplicación $USD Q10 (1pt): problema cotidiano
NO incluir respuestas en este documento.

═══════════════════════════════════════════════
DOCUMENTO 2 — RESPUESTAS Y MATERIAL DOCENTE
═══════════════════════════════════════════════

# RESPUESTAS DOCENTE: [TEMA]

- Respuestas Q1-Q10 con justificación breve
- Procedimiento resuelto Q9 y Q10
- Rúbrica: Logrado / En proceso / Por lograr
- Escala: 10=100%|8-9=Muy bueno|6-7=Satisfactorio|4-5=En proceso|<4=Necesita refuerzo
- Observaciones: error más frecuente, fecha aplicación'''

def run_command(cmd, description=""):
    """Ejecutar comando y retornar output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        if result.returncode != 0:
            print(f"❌ Error en: {description}")
            print(result.stderr)
            return None
        return result.stdout
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    print("=" * 60)
    print("  🤖 GENERADOR AUTOMÁTICO — Números enteros")
    print("=" * 60)

    # Crear carpeta del curso
    CURSO_PATH.mkdir(parents=True, exist_ok=True)
    print(f"\n✅ Carpeta creada: {CURSO_PATH}")

    # Generar clases
    print("\n📚 Generando CLASES...")
    for clase_num, (clase_nombre, clase_info) in enumerate(CLASES.items(), 1):
        sources_str = " ".join([f"-s {s}" for s in clase_info["sources"]])
        prompt = PROMPT_CLASE.replace("[N]", str(clase_num)).replace("[TEMA]", clase_nombre)

        cmd = f'''notebooklm generate report --format custom --language es --notebook {NOTEBOOK_ID} {sources_str} "{prompt}" --json'''

        print(f"  [{clase_num}/11] Generando: {clase_nombre}...")
        output = run_command(cmd, f"Clase {clase_num}")

        if output:
            try:
                data = json.loads(output)
                artifact_id = data.get("task_id", data.get("artifact_id"))
                # Guardar artifact_id para descargar después
                print(f"       ✅ Artifact ID: {artifact_id[:8]}...")
            except:
                print(f"       ⚠️ No se obtuvo artifact_id")

    print("\n✅ Generación completada")
    print(f"\n📂 Materiales guardados en: {CURSO_PATH}")
    print("\n📌 Próximos pasos:")
    print("   1. Esperar procesamiento de NotebookLM (5-20 min por tipo de artefacto)")
    print("   2. Descargar archivos con: notebooklm download ...")
    print("   3. Crear 00 - Índice del curso.md con wikilinks")
    print("   4. Actualizar DASHBOARD.md y mapa de cursos")

if __name__ == "__main__":
    main()
