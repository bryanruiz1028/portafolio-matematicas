# Clase 06 — Gráfica y elementos de la elipse a partir de su ecuación general

#algebra #graphandelement
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 6 de 6

> [!info] 🧭 Navegación
> [[Clase 05|⬅ Clase 05]] | [[00 - Índice del curso|Índice]] | **Clase 06** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]

---

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> Comprender la transición de una ecuación general "desordenada" a una representación gráfica es vital para el análisis de sistemas dinámicos. Esta competencia permite a estudiantes y profesionales interpretar datos abstractos para modelar fenómenos físicos con precisión geométrica.
> 
> *   **💵 [aplicación con $USD]:** Evaluación de costos en proyectos de urbanismo; por ejemplo, determinar el presupuesto de pavimentación para una plaza elíptica basándose en el área calculada desde su ecuación de diseño.
> *   **🏗️ [aplicación práctica]:** Ingeniería y arquitectura en la construcción de arcos de puentes o el diseño de techos en galerías susurrantes, donde la acústica depende de la ubicación exacta de los focos.
> *   **📊 [situación cotidiana]:** Análisis de las órbitas de satélites de telecomunicaciones, permitiendo predecir su posición exacta para mantener la cobertura de señales globales.

---

## Concepto clave

> [!note] 📌 ¿Qué es Gráfica y elementos de la elipse a partir de su ecuación general?
> Es el proceso de transformar la ecuación general de la elipse ($Ax^2 + Cy^2 + Dx + Ey + F = 0$) a su forma canónica u ordinaria. Al realizar esta conversión, podemos identificar los parámetros fundamentales para su representación gráfica: el centro $(h, k)$, la longitud del **semieje mayor ($a$)**, el **semieje menor ($b$)** y la **orientación del eje focal**.
> 
> **Fórmulas auxiliares necesarias:**
> 1. **Relación pitagórica:** $c^2 = a^2 - b^2$ (para hallar la distancia focal).
> 2. **Lado Recto ($LR$):** $LR = \frac{2b^2}{a}$ (determina el ancho de la elipse en los focos).

> [!warning] ⚠️ Error común
> Un error frecuente es no aplicar el cambio de signo al extraer las coordenadas del centro desde la ecuación canónica. Recuerda: en $(x - h)^2$ y $(y - k)^2$, los valores de $h$ y $k$ tienen el signo opuesto al que aparece en el paréntesis.

> [!tip] 💡 Truco para recordarlo
> Para determinar la orientación, busca siempre el denominador más grande; ese será siempre $a^2$. Si el **semieje mayor** está bajo la $x$, la elipse es horizontal. Si está bajo la $y$, es vertical. Recuerda: la **"A"** es de **"Alargado"**.

---

## Procedimiento paso a paso

```text
PASO 1 → Agrupar términos de x y y en el lado izquierdo. Trasladar el término independiente al lado derecho de la igualdad.
PASO 2 → Factorizar el coeficiente de los términos cuadráticos. Completar el Trinomio Cuadrado Perfecto (TCP). 
         ¡IMPORTANTE!: Al equilibrar la ecuación, el valor sumado al lado derecho debe ser el producto del factor externo por el término agregado (Factor × TCP_agregado).
PASO 3 → Simplificar a binomios al cuadrado. Dividir toda la ecuación por el número resultante a la derecha para igualar a 1.
PASO 4 → Identificar centro (h, k), semiejes (a, b) y distancia focal (c). Calcular el Lado Recto para precisar el trazo.
```

---

## Ejemplos

### Ejemplo 1: Caso Básico (Centro 0,0)
**Ecuación:** $x^2 + 4y^2 - 16 = 0$
1. Movemos el término independiente: $x^2 + 4y^2 = 16$.
2. Dividimos entre 16 para igualar a 1: $\frac{x^2}{16} + \frac{4y^2}{16} = \frac{16}{16}$.
3. Simplificamos: $\frac{x^2}{16} + \frac{y^2}{4} = 1$.
*   **Elementos:** $a^2 = 16 \rightarrow a = 4$ | $b^2 = 4 \rightarrow b = 2$.
*   **Orientación:** Horizontal (el semieje mayor está en el eje $x$).

### Ejemplo 2: Caso con signos (Centro h,k)
**Ecuación:** $4x^2 - 40x + 9y^2 + 54y + 145 = 0$
1. Agrupamos y movemos el 145: $(4x^2 - 40x) + (9y^2 + 54y) = -145$.
2. Factorizamos coeficientes: $4(x^2 - 10x) + 9(y^2 + 6y) = -145$.
3. Completamos TCP y **equilibramos**:
   $4(x^2 - 10x + 25) + 9(y^2 + 6y + 9) = -145 + \mathbf{(4 \times 25)} + \mathbf{(9 \times 9)}$
   $4(x-5)^2 + 9(y+3)^2 = -145 + 100 + 81 \rightarrow 4(x-5)^2 + 9(y+3)^2 = 36$.
4. Dividimos entre 36: $\frac{(x-5)^2}{9} + \frac{(y+3)^2}{4} = 1$.
*   **Centro:** $(5, -3)$.

### Ejemplo 3: Caso Avanzado (Eje Vertical)
**Ecuación:** $25x^2 + 4y^2 - 100 = 0$
1. Traslado y división: $25x^2 + 4y^2 = 100 \rightarrow \frac{x^2}{4} + \frac{y^2}{25} = 1$.
2. Análisis: El valor $a^2 = 25$ se encuentra bajo el término $y$.
*   **Orientación:** Vertical, debido a que el **semieje mayor** coincide con la ordenada.

### Ejemplo 4: Aplicación económica ($USD)
Se requiere pavimentar una plaza elíptica cuya ecuación es $\frac{(x-5)^2}{9} + \frac{(y+3)^2}{4} = 1$. El costo por unidad cuadrada es de $\$10$ USD.
1. Identificamos semiejes: $a = 3$, $b = 2$.
2. Área ($A = \pi \cdot a \cdot b$): $A = 3.1416 \times 3 \times 2 \approx 18.8496$ u².
3. Costo total: $18.8496 \times 10 = \$188.50$ USD (redondeado).

---

## Ejercicios para el estudiante

### Bloque 🟢 Fácil (Centro 0,0)
1. $9x^2 + 16y^2 - 144 = 0$
2. $4x^2 + 25y^2 - 100 = 0$
3. $x^2 + 9y^2 - 9 = 0$
4. $16x^2 + 4y^2 - 64 = 0$

### Bloque 🟡 Medio (Centro h,k)
1. $9x^2 - 18x + 4y^2 + 16y - 11 = 0$
2. $4x^2 + 16x + 25y^2 - 50y - 59 = 0$
3. $16x^2 + 64x + 9y^2 - 54y + 1 = 0$
4. $4x^2 - 24x + 9y^2 + 18y + 9 = 0$

### Bloque 🔴 Avanzado (Lado Recto y Focos)
*Para estos ejercicios, exprese $c$ en forma radical y decimal.*
1. Calcule $LR$ y Focos de: $x^2 + 4y^2 - 4 = 0$.
2. Calcule $LR$ y Focos de: $25x^2 + 9y^2 - 225 = 0$.
3. Determine las coordenadas exactas de los focos: $4(x-1)^2 + 9(y-2)^2 = 36$.
4. Obtenga todos los elementos ($a, b, c, LR$) de: $9x^2 + 25y^2 - 225 = 0$.

### ✅ Respuestas
*   **Fácil:** 1) $\frac{x^2}{16} + \frac{y^2}{9} = 1$; 2) $\frac{x^2}{25} + \frac{y^2}{4} = 1$; 3) $\frac{x^2}{9} + y^2 = 1$; 4) $\frac{x^2}{4} + \frac{y^2}{16} = 1$.
*   **Medio:** 1) $\frac{(x-1)^2}{4} + \frac{(y+2)^2}{9} = 1$; 2) $\frac{(x+2)^2}{25} + \frac{(y-1)^2}{4} = 1$; 3) $\frac{(x+2)^2}{9} + \frac{(y-3)^2}{16} = 1$; 4) $\frac{(x-3)^2}{9} + \frac{(y+1)^2}{4} = 1$.
*   **Avanzado:** 
    1) $LR=1, F(\pm\sqrt{3}, 0) \approx (\pm1.73, 0)$. 
    2) $LR=3.6, F(0, \pm4)$. 
    3) $c=\sqrt{5} \approx 2.24$, $F(1 \pm 2.24, 2)$. 
    4) $a=5, b=3, c=4, LR=3.6$.

---

## Mini-prueba de autoevaluación

1.  **¿Cómo identificamos el semieje mayor ($a$) en la ecuación canónica?**
    a) Es el denominador que aparece primero.
    b) Es el denominador que acompaña a la variable $y$.
    c) Es el denominador con el valor numérico más alto.
    d) Es el resultado de sumar ambos denominadores.

2.  **En la expresión $\frac{(x+4)^2}{25} + \frac{(y-2)^2}{9} = 1$, ¿cuál es el centro?**
    a) $(4, -2)$
    b) $(-4, 2)$
    c) $(25, 9)$
    d) $(-4, -2)$

3.  **Un área elíptica tiene $a=10$ m y $b=5$ m. Si el mantenimiento cuesta $\$2$ USD por m², ¿cuál es el costo total aproximado usando $\pi \approx 3.14$?**
    a) $\$157$ USD
    b) $\$314$ USD
    c) $\$628$ USD
    d) $\$1,000$ USD

**Respuestas:**
1. **c)** $a^2$ siempre es el valor mayor entre los denominadores.
2. **b)** Aplicando el cambio de signo reglamentario.
3. **b)** Área $= 3.14 \times 10 \times 5 = 157$ m². Costo $= 157 \times 2 = \$314$.

---

## Notas para el próximo tema
Finalizamos el estudio de la elipse. En la siguiente sesión, integraremos estos conocimientos para resolver problemas de intersección de cónicas y optimización, preparándonos para el análisis de la hipérbola.

> [!info] 🧭 Navegación
> [[Clase 05|⬅ Clase 05]] | [[00 - Índice del curso|Índice]] | **Clase 06** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]