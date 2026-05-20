# Clase 01 — Ecuaciones Cuadráticas de Segundo Grado
tags: #algebra #quadraticequations
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 8

> [!info] 🧭 Navegación
> ⬅️ **Anterior**: [[00 - Introducción al Álgebra]]
> ➡️ **Siguiente**: [[02 - Fórmula General]]

---

## 2. RELEVANCIA Y APLICACIÓN
Las ecuaciones de segundo grado son aquellas que pueden expresarse en su forma estándar: **$ax^2 + bx + c = 0$** (donde $a \neq 0$). Su importancia radica en que nos permiten modelar situaciones donde el cambio no es constante, sino que depende del cuadrado de una variable, permitiéndonos encontrar puntos de equilibrio o raíces mediante la identificación de sus coeficientes ($a$, $b$ y $c$).

**¿Dónde se aplican?**
Estas ecuaciones son la base para entender las **parábolas**, figuras geométricas que describen desde el vuelo de un balón hasta la forma de las antenas satelitales.

*   **💵 Aplicación USD:** Cálculo de ingresos totales en ventas masivas. Si el costo de producción y la demanda varían, la utilidad se modela con una ecuación cuadrática para hallar el precio en dólares que maximiza la ganancia.
*   **🏗️ Aplicación práctica:** Diseño de trayectorias balísticas y cálculo de áreas de terrenos rectangulares donde se conoce la relación entre sus lados.
*   **📊 Situación cotidiana:** Determinación de aceleraciones y tiempos en física, o el equilibrio entre oferta y demanda en mercados competitivos.

---

## 3. CONCEPTO CLAVE

> [!note] Definición: Ecuaciones de Segundo Grado
> Una ecuación es de segundo grado cuando el máximo exponente de la incógnita es **2**. En el conjunto de los números reales, estas ecuaciones pueden tener **2, 1 o ninguna solución**.

> [!warning] Error Común: ¡Iguala a Cero primero!
> Según el método del "Profe Alex", nunca intentes factorizar si la ecuación no está igualada a cero. Debes transponer todos los términos a un solo lado.
> 
> ❌ $x^2 + 5x = -6$
> ✅ $x^2 + 5x + 6 = 0$

> [!tip] Truco: Regla de los Signos y el "Número Mayor"
> Al factorizar trinomios $x^2 + bx + c$:
> 1. El signo del **primer paréntesis** es el signo de $b$.
> 2. El signo del **segundo paréntesis** es el producto de los signos de $b$ y $c$.
> 3. **Regla de Oro:** Siempre coloca el **número mayor** en el primer paréntesis y el **menor** en el segundo. Esto garantiza que los signos funcionen correctamente.

---

## 4. PROCEDIMIENTO PASO A PASO
Para resolver por factorización (trinomios del tipo $x^2 + bx + c = 0$), sigue este flujo:

```text
PASO 1: Igualar a cero y ordenar en forma descendente (ax² + bx + c = 0).
PASO 2: Abrir dos paréntesis y distribuir la raíz de x² (x) en cada uno.
PASO 3: Aplicar signos y buscar dos números que multiplicados den 'c' 
        y sumados/restados den 'b'. ¡Pon el mayor primero!
PASO 4: Aplicar la Propiedad del Producto Cero (si A * B = 0, entonces A=0 o B=0) 
        para despejar x1 y x2.
```

> [!tip] 🔍 La Firma del Experto: ¡Verifica!
> Una vez halladas $x_1$ y $x_2$, sustitúyelas en la ecuación original. Si el resultado es $0=0$, tu ejercicio es correcto. Por ejemplo, si $x = -3$ en $x^2 + 5x + 6 = 0$:
> $(-3)^2 + 5(-3) + 6 = 9 - 15 + 6 = 0$. ✅

---

## 5. BLOQUES DE EJEMPLOS

> [!example] Ejemplo 1: Caso Básico
> **Ecuación:** $x^2 + 5x + 6 = 0$
> 1. Buscamos números que multiplicados den $6$ y sumados den $5$: **3 y 2**.
> 2. Factorización: $(x + 3)(x + 2) = 0$
> 3. Soluciones: $x + 3 = 0 \rightarrow x_1 = -3$ | $x + 2 = 0 \rightarrow x_2 = -2$.

> [!example] Ejemplo 2: Signos Negativos
> **Ecuación:** $x^2 - 6x - 16 = 0$
> 1. Signos: Primero $(-)$, segundo $(- \times - = +)$.
> 2. Números que multiplicados den $16$ y restados den $6$: **8 y 2**.
> 3. Aplicamos regla del mayor: $(x - 8)(x + 2) = 0$
> 4. Soluciones: $x_1 = 8$, $x_2 = -2$.

> [!example] Ejemplo 3: Método para $ax^2 + bx + c$ ($a > 1$)
> **Ecuación:** $3x^2 + 2x - 8 = 0$
> 1. Multiplicamos todo por $a$ ($3$), dejando el centro indicado: $(3x)^2 + 2(3x) - 24 = 0$.
> 2. Factorizamos como trinomio simple: $(3x + 6)(3x - 4) = 0$.
> 3. **División obligatoria:** Para equilibrar, dividimos por $a$ ($3$):
>    $$\frac{(3x + 6)(3x - 4)}{3} = \frac{3(x + 2)(3x - 4)}{3} = (x + 2)(3x - 4)$$
> 4. Soluciones: $x_1 = -2$, $x_2 = 4/3$.

> [!example] Ejemplo 4: Incompleta y Finanzas (USD)
> **Problema:** Una startup calcula que su punto de equilibrio se da cuando $4x^2 - 100 = 0$ (donde $x$ es el precio en USD).
> 1. Despeje directo: $4x^2 = 100 \rightarrow x^2 = 25$.
> 2. Raíz cuadrada: $x = \pm \sqrt{25}$.
> 3. Soluciones: $x_1 = 5$ USD, $x_2 = -5$ USD. El precio lógico es **5 USD**.

---

## 6. EJERCICIOS PRÁCTICOS

> [!abstract] Actividades de Práctica
> **Nivel Verde (Fácil)**
> 1. $x^2 + 7x + 10 = 0$
> 2. $x^2 - 9x + 20 = 0$
> 3. $x^2 + 8x + 12 = 0$
> 4. $x^2 - 10x + 21 = 0$
> 
> **Nivel Amarillo (Medio)**
> 5. $x^2 - x - 42 = 0$
> 6. $x^2 + 2x - 15 = 0$
> 7. $x^2 - 5x - 24 = 0$
> 8. $x^2 + 3x - 28 = 0$
> 
> **Nivel Rojo (Avanzado)**
> 9. $2x^2 + 9x + 4 = 0$
> 10. $3x^2 - 5x - 2 = 0$
> 11. $x^2 - 144 = 0$ (Resolver por diferencia de cuadrados).
> 12. **💵 Reto USD:** Una tienda de software modela su ingreso marginal con $x^2 - 625 = 0$. Determine el valor positivo de $x$ (precio en USD) necesario para estabilizar la cuenta.

---

## 7. SOLUCIONARIO PARA EL DOCENTE

> [!success] Respuestas Directas
> *   **Verde:** 1) $x=\{-5, -2\}$; 2) $x=\{5, 4\}$; 3) $x=\{-6, -2\}$; 4) $x=\{7, 3\}$
> *   **Amarillo:** 5) $x=\{7, -6\}$; 6) $x=\{-5, 3\}$; 7) $x=\{8, -3\}$; 8) $x=\{4, -7\}$
> *   **Rojo:** 9) $x=\{-1/2, -4\}$; 10) $x=\{2, -1/3\}$; 11) $x=\{12, -12\}$; 12) **$x = 25$ USD**

---

## 8. AUTOEVALUACIÓN

> [!question] Comprueba tu aprendizaje
> **1. Si una ecuación cuadrática no toca el eje X al graficarse, ¿cuántas soluciones reales tiene?**
> a) 2 | b) 1 | c) Ninguna
> 
> **2. ¿Cuál es el primer paso correcto para factorizar $x^2 - 8x = -15$?**
> a) Abrir paréntesis. | b) Sumar 15 a ambos lados. | c) Sacar raíz a $x^2$.
> 
> **3. En el problema $x^2 - 144 = 0$, si $x$ representa una longitud en USD para un marco decorativo, ¿cuál es el valor real aplicable?**
> a) 12 USD | b) -12 USD | c) 144 USD

---

## 9. CIERRE Y NAVEGACIÓN FINAL
¡Excelente trabajo! Has dominado la resolución por factorización y comprendido por qué es vital el orden y la igualación a cero. Sin embargo, no todos los trinomios son fáciles de factorizar. Por ello, en la próxima clase conocerás la "llave maestra" del álgebra: la **Fórmula General**.

> [!info] 🧭 Navegación
> ⬅️ **Anterior**: [[00 - Introducción al Álgebra]]
> ➡️ **Siguiente**: [[02 - Fórmula General]]