# 📖 Guía de estudio — Clase 02: Multiplicación de números imaginarios

> [!info] 📌 Conceptos clave
> Para dominar la multiplicación de números imaginarios y evitar errores comunes, ten en cuenta los siguientes fundamentos pedagógicos:
> - **Definición de la unidad imaginaria:** La letra $i$ representa la raíz cuadrada de un número negativo fundamental: $i = \sqrt{-1}$. Por consecuencia, su valor elevado al cuadrado es siempre $i^2 = -1$.
> - **La Regla de Oro (Advertencia):** No intentes unir raíces de números negativos directamente bajo una sola raíz. La propiedad distributiva $\sqrt{a} \cdot \sqrt{b} = \sqrt{a \cdot b}$ **solo es válida para números reales positivos**. Si ignoras esto y multiplicas los negativos directamente, obtendrás un signo incorrecto en el resultado final (por ejemplo, obtendrías $\sqrt{15}$ en lugar del correcto $-\sqrt{15}$).
> - **Procedimiento estándar:** Primero debes expresar cada raíz negativa en términos de la unidad imaginaria ($bi$) y, una vez que los términos sean "reales acompañados de $i$", realiza la multiplicación.
> - **Manejo de raíces no exactas:** Si las raíces no tienen un resultado entero, primero extrae la unidad $i$ de cada una y luego une las raíces de los números positivos restantes en una sola raíz para simplificar.
> - **Potencias básicas a recordar:**
> 	- $i^2 = -1$
> 	- $i^3 = -i$ (resultado de multiplicar $i^2 \cdot i$).

---

### 2. Tabla de Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Unidad Imaginaria** | $i = \sqrt{-1}$ |
| **Potencia Cuadrática** | $i^2 = -1$ |
| **Número Complejo** | $a + bi$ (donde $a$ es la parte real y $bi$ la imaginaria) |
| **Conjugado de un complejo** | $a - bi$ (misma parte real, pero la parte imaginaria cambia de signo) |

---

### 3. Ejemplos Resueltos Adicionales

> [!example] Ejemplo A: Caso Básico
> **Operación:** $\sqrt{-4} \cdot \sqrt{-9}$
> 
> 1. **Expresar en términos de $i$:** Transformamos las raíces negativas sabiendo que $\sqrt{-1} = i$.
>    $\sqrt{-4} = \sqrt{4} \cdot \sqrt{-1} = 2i$
>    $\sqrt{-9} = \sqrt{9} \cdot \sqrt{-1} = 3i$
> 2. **Multiplicar coeficientes y unidades:**
>    $(2 \cdot 3) \cdot (i \cdot i) = 6i^2$
> 3. **Sustituir la potencia:** Aplicamos la definición $i^2 = -1$.
>    $6 \cdot (-1)$
> 4. **Resultado final:** $-6$

> [!example] Ejemplo B: Aplicación Real (Metáfora Financiera USD)
> **Problema:** En un modelo de riesgo, se multiplican dos "factores de ajuste" representados por $\sqrt{-25}$ y $\sqrt{-4}$ para calcular un impacto en el presupuesto. 
> *Nota: Aunque en la contabilidad tradicional no se usan números imaginarios, este ejercicio ayuda a visualizar cómo los factores negativos operan en sistemas complejos.*
> 
> **Procedimiento:**
> 1. **Conversión:**
>    $\sqrt{-25} = 5i$
>    $\sqrt{-4} = 2i$
> 2. **Multiplicación:** 
>    $5i \cdot 2i = 10i^2$
> 3. **Cálculo del impacto:**
>    $10 \cdot (-1) = -10$
> 
> **Resultado:** El ajuste final representa una reducción de $-10$ USD.

---

### 4. Ejercicios de Repaso

> [!abstract] Bloque 🟢 Fácil: Iniciación
> 1. Expresa como unidad imaginaria: $\sqrt{-16}$.
> 2. Realiza la siguiente operación: $5 \cdot 3i$.
> 3. Convierte a formato imaginario: $\sqrt{-100}$.

> [!abstract] Bloque 🟡 Medio: Operaciones Combinadas
> 1. Resuelve la multiplicación: $\sqrt{-2} \cdot \sqrt{-8}$.
> 2. Calcula el producto (recuerda unir las raíces positivas al final): $\sqrt{-3} \cdot \sqrt{-12}$.
> 3. Simplifica la siguiente división cancelando las unidades $i$: $\frac{\sqrt{-9}}{\sqrt{-16}}$.

> [!abstract] Bloque 🔴 Avanzado: Impacto de Tres Factores
> **Enunciado:** Un sistema de análisis detecta tres fluctuaciones críticas representadas por los factores $\sqrt{-2}$, $\sqrt{-3}$ y $\sqrt{-4}$. Calcula el producto de estos tres términos para determinar el "impacto financiero total".
> 
> **Instrucciones:**
> - Convierte cada término a su forma con $i$ antes de operar.
> - Utiliza la identidad $i^3 = -i$.
> - Expresa tu resultado final en la **forma radical más simple** (ejemplo: $a\sqrt{b}i$).

---

### 5. Consejo de Estudio

> [!tip] 💡 Consejo de estudio
> Para no perderte con los signos negativos ni cometer errores de radicación, adopta el hábito del "profe Alex": **Antes de realizar cualquier cálculo, extrae la unidad $i$ de la raíz.** Escribir siempre la $i$ fuera de la raíz te permitirá trabajar con números reales de forma segura y evitará que "desaparezcan" signos negativos por error.