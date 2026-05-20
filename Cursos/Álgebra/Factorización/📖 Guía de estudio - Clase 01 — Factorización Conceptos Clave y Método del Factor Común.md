# 📖 Guía de estudio — Clase 01: ¿Qué es factorizar y cómo encontrar el factor común?

> [!info] 📌 Conceptos clave
> 1. **Factor vs. Producto:** Los **factores** son los números o letras que se multiplican entre sí. El **producto** es el resultado final de esa operación (ej. en $3 \cdot 2 = 6$, el 3 y el 2 son factores, y el 6 es el producto).
> 2. **Factorizar:** Es el proceso de descomponer una expresión matemática para escribirla como una multiplicación. Su objetivo es transformar sumas o restas en productos equivalentes.
> 3. **Factores primos:** Son números divisibles solo por sí mismos y por la unidad (2, 3, 5, 7, etc.). Descomponer una expresión hasta sus factores primos es la forma **más correcta e ideal** de factorizar, pues permite llegar a los elementos más básicos.
> 4. **Factor común:** Es la letra o número que se repite en todos los términos de un polinomio. Es el elemento que "comparten" todos los sumandos.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Factor** | Cada elemento que compone una multiplicación. |
| **Producto** | El resultado final de multiplicar factores. |
| **Factor Común** | Letra o número que aparece de forma idéntica en cada término de un polinomio. |
| **Factorización de Monomio** | Descomposición total en factores primos y potencias (ej. $6x^2 = 2 \cdot 3 \cdot x \cdot x$). |
| **Ceros de la función** | Puntos donde la ganancia o el resultado es nulo ($y=0$); se hallan igualando cada factor obtenido a cero. |

## Ejemplos resueltos adicionales

> [!example] Ejemplo A: Caso Básico (Método de forma extendida)
> **Problema:** Factorizar la expresión $6x^2y^3 - 8xy^5$
> 
> **Paso 1: Descomposición total**
> Descomponemos los coeficientes (números) en factores primos y extendemos las variables:
> - $6x^2y^3 = 2 \cdot 3 \cdot x \cdot x \cdot y \cdot y \cdot y$
> - $8xy^5 = 2 \cdot 2 \cdot 2 \cdot x \cdot y \cdot y \cdot y \cdot y \cdot y$
> 
> **Paso 2: Aplicación de la lógica del "Exponente menor"**
> Identificamos qué elementos se repiten. Para las letras, siempre elegimos la que tenga el exponente más pequeño en la expresión original:
> - El número común es **2**.
> - Entre $x^2$ y $x$, elegimos **$x$** (es el exponente menor).
> - Entre $y^3$ y $y^5$, elegimos **$y^3$** (es el exponente menor).
> - **Factor Común:** $2xy^3$
> 
> **Paso 3: Resultado final compactado**
> Colocamos el factor común fuera de un paréntesis y dentro escribimos lo que no se repitió:
> **Resultado:** $2xy^3 (3x - 4y^2)$

> [!example] Ejemplo B: Aplicación real (Ganancias en USD)
> **Enunciado:** Una empresa determina que su ganancia depende del precio de venta $V$. La expresión de ganancia es $-V^2 + 10V$.
> 
> **Paso 1: Extraer el factor común**
> La letra $V$ está en ambos términos. Aplicando la regla del menor exponente, extraemos $V$.
> **Expresión factorizada:** $V(-V + 10)$
> 
> **Paso 2: Interpretación de los "Ceros"**
> Para saber cuándo la empresa no gana dinero, igualamos cada factor a cero:
> 1.  **Primer factor:** $V = 0$. Esto significa que si el precio es **0 USD**, la ganancia es nula.
> 2.  **Segundo factor:** $-V + 10 = 0 \rightarrow V = 10$.
> 
> **Conclusión:** La ganancia es cero en dos puntos: cuando no se cobra nada ($0$ USD) y cuando el precio sube a **10 USD** (punto de equilibrio donde los costos igualan los ingresos).

## Ejercicios de repaso

> [!abstract] 🟢 Nivel Fácil
> 1. Utiliza el método de descomposición (o "escalera") para hallar los factores primos de: **12**, **20** y **15**.
> 2. Identifica el factor común en la expresión: $2ac + 3ab$.

> [!abstract] 🟡 Nivel Medio
> 1. Factoriza el binomio: $2x^2y + 3xy$.
> 2. Factoriza el siguiente polinomio: $m^5n^2 - m^4n + m^3$.
>    > [!warning] **Pista de experto:** 
>    > Recuerda la regla del **"1 invisible"**. Si extraes todo el término $m^3$ como factor común, ese espacio no queda vacío ni desaparece; debe quedar un **1** en su lugar dentro del paréntesis.

> [!abstract] 🔴 Nivel Avanzado (Aplicación)
> 1. El modelo de ingresos de un negocio está definido por $100x - 5x^2$ (donde $x$ es el precio). 
>    - Factoriza la expresión extrayendo el máximo factor común (número y letra).
>    - Halla los **"Ceros"** de este modelo de ingresos para determinar a qué precios el ingreso sería igual a cero dólares.

> [!tip] 💡 Consejo de estudio: La Multiplicación de Verificación
> Como profesor, siempre te recomendaré comprobar tu trabajo. Para saber si factorizaste bien, aplica la **propiedad distributiva**: multiplica tu factor común por cada término dentro del paréntesis. Si el resultado es idéntico a la expresión original, ¡tu proceso es impecable!