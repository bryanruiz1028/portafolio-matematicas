# Clase 03 — Multiplicación de polinomios y varios factores

#algebra #multiplicacinde
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 4

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | | [[Clase 04|Clase 04 ➡]]

---

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> La multiplicación algebraica permite modelar situaciones donde varias dimensiones cambian a la vez. Es la herramienta para calcular el tamaño real de una habitación cuando solo tienes las fórmulas de sus paredes o proyectar ganancias financieras complejas.

*   **💵 [Finanzas]:** Cálculo de intereses compuestos o utilidades en $USD al variar precios y cantidades.
*   **🏗️ [Construcción]:** Determinación de áreas de terrenos o superficies de construcción con dimensiones variables.
*   **📊 [Situación cotidiana]:** Estimación de costos totales al comprar múltiples productos con diferentes impuestos aplicados.

---

## Concepto clave

> [!note] 📌 ¿Qué es Multiplicación de expresiones algebraicas?
> Multiplicar polinomios es como "repartir" cada término del primer grupo con todos los del segundo. En este proceso, multiplicas los números normalmente, pero con las letras, dejas la misma base y **sumas los numeritos de arriba (exponentes)**.

> [!warning] ⚠️ Error común
> No multipliques los exponentes; la regla dice que se deben sumar.
> *   ❌ **Incorrecto:** $x^2 \cdot x^3 = x^6$
> *   ✅ **Correcto:** $x^2 \cdot x^3 = x^5$

> [!tip] 💡 Truco para recordarlo
> Sigue siempre el orden **"S-C-L"** en cada multiplicación individual para no olvidar nada:
> 1. **S**ignos (Ley de signos).
> 2. **C**oeficientes (Multiplicar los números).
> 3. **L**etras (Sumar exponentes de letras iguales).

---

## Procedimiento paso a paso

```text
PASO 1 → Multiplicar signos (usando ley de signos).
PASO 2 → Multiplicar coeficientes numéricos. 
         (Si hay fracciones: numerador x numerador / denominador x denominador).
         (Si hay enteros: poner un /1 debajo para facilitar el cálculo).
PASO 3 → Sumar exponentes de las letras iguales (propiedad de potencias).
PASO 4 → Agrupar y reducir términos semejantes (letras y exponentes idénticos).
PASO 5 → Ordenar el polinomio resultante (normalmente de mayor a menor exponente).
```

---

## Ejemplos prácticos

### Ejemplo 1: Caso Básico (Binomio por Binomio)
Multiplicar: $(3x + 2y)(5x - 4y)$

1.  **Distribuir el primer término ($3x$):**
    *   $(3x)(5x)$: **S:** (+)(+)=+, **C:** $3 \cdot 5=15$, **L:** $x^1 \cdot x^1 = x^2 \rightarrow$ **$15x^2$**
    *   $(3x)(-4y)$: **S:** (+)(-)=-, **C:** $3 \cdot 4=12$, **L:** $x \cdot y = xy \rightarrow$ **$-12xy$**
2.  **Distribuir el segundo término ($2y$):**
    *   $(2y)(5x) = \mathbf{10xy}$ (ordenado alfabéticamente).
    *   $(2y)(-4y) = \mathbf{-8y^2}$
3.  **Reducción de términos semejantes:**
    $-12xy + 10xy = -2xy$
4.  **Resultado final:** $15x^2 - 2xy - 8y^2$

### Ejemplo 2: Caso con Signos y Fracciones
Multiplicar: $(\frac{2}{3}x^2 - \frac{1}{5}x)(\frac{3}{2}x^2 - 4)$

*   **Término 1:** $(\frac{2}{3}x^2)(\frac{3}{2}x^2) = \frac{6}{6}x^4 = \mathbf{x^4}$
*   **Término 2:** $(\frac{2}{3}x^2)(-\frac{4}{1}) = \mathbf{-\frac{8}{3}x^2}$
*   **Término 3:** $(-\frac{1}{5}x)(\frac{3}{2}x^2) = \mathbf{-\frac{3}{10}x^3}$
*   **Término 4:** $(-\frac{1}{5}x)(-\frac{4}{1}) = \mathbf{+\frac{4}{5}x}$
*   **Resultado ordenado (Paso 5):** $x^4 - \frac{3}{10}x^3 - \frac{8}{3}x^2 + \frac{4}{5}x$

### Ejemplo 3: Caso Avanzado (Varios Factores)
Multiplicar: $(x + 3)(2x - 5)(3x - 1)$

1.  **Multiplicar los dos primeros paréntesis:**
    $(x + 3)(2x - 5) = 2x^2 - 5x + 6x - 15 = \mathbf{2x^2 + x - 15}$
2.  **Multiplicar el resultado por el tercer factor:**
    $(2x^2 + x - 15)(3x - 1)$
    $= 6x^3 - 2x^2 + 3x^2 - x - 45x + 15$
3.  **Reducción y orden final:**
    **$6x^3 + x^2 - 46x + 15$**

### Ejemplo 4: Aplicación Real ($USD)
**Problema:** Si el precio de un artículo es $(2x + 5)$ $USD y se compran $(x - 1)$ unidades, ¿cuál es el polinomio del costo total?

*   **Operación:** $(2x + 5)(x - 1)$
*   **Desarrollo:** $2x^2 - 2x + 5x - 5$
*   **Resultado:** $2x^2 + 3x - 5$ $USD

---

## Ejercicios y Autoevaluación

```ad-abstract
title: 🟢 Nivel Fácil (Binomios)
1. $(x + 2)(x + 5)$
2. $(a - 3)(a + 4)$
3. $(2x + 1)(x - 6)$
4. $(m + n)(m - n)$
```

```ad-abstract
title: 🟡 Nivel Medio (Fracciones)
1. $(\frac{1}{2}x + 4)(\frac{2}{3}x - 2)$
2. $(\frac{3}{4}a^2 - 1)(2a + \frac{1}{3})$
3. $(\frac{2}{5}m - \frac{1}{2})(\frac{5}{2}m + 4)$
4. $(\frac{1}{3}x^2 + x)(\frac{3}{4}x - \frac{1}{2})$
```

```ad-abstract
title: 🔴 Nivel Avanzado (Varios Factores y $USD)
1. $(x + 1)(x + 2)(x + 3)$
2. $(2a - 1)(a + 2)(3a - 4)$
3. Un terreno mide $(3x + 2)$ de largo y $(x + 4)$ de ancho. Expresa su área.
4. El ahorro mensual de un estudiante es $(x + 10)$ $USD. ¿Cuánto ahorra en $(x - 2)$ meses?
```

```ad-success
title: ✅ Respuestas para el docente
**Fácil:** 1. $x^2+7x+10$ | 2. $a^2+a-12$ | 3. $2x^2-11x-6$ | 4. $m^2-n^2$
**Medio:** 1. $\frac{1}{3}x^2+\frac{5}{3}x-8$ | 2. $\frac{3}{2}a^3+\frac{1}{4}a^2-2a-\frac{1}{3}$ | 3. $m^2+\frac{7}{20}m-2$ | 4. $\frac{1}{4}x^3+\frac{7}{12}x^2-\frac{1}{2}x$
**Avanzado:** 1. $x^3+6x^2+11x+6$ | 2. $6a^3+5a^2-17a+8$ | 3. $3x^2+14x+8$ | 4. $x^2+8x-20$ $USD
```

### Mini-prueba

```ad-question
title: 1. Conceptual
¿Qué se hace con los exponentes de letras iguales al multiplicar?
A) Multiplicarlos.
B) Restarlos.
C) Sumarlos.
```

```ad-question
title: 2. Procedimental
¿Cuál es el resultado de $(x + 1)(x - 1)$?
A) $x^2 + 1$
B) $x^2 - 1$
C) $2x$
```

```ad-question
title: 3. Aplicación $USD
Si un ahorro mensual es $(x + 10)$ $USD, ¿cuánto se ahorra en $(x - 2)$ meses?
A) $x^2 + 8x - 20$ $USD
B) $x^2 - 12x - 20$ $USD
C) $2x + 8$ $USD
```

---

## Cierre y navegación final

> [!tip] 💡 En la próxima clase
> Ahora que sabes multiplicar y manejar varios factores, aprenderás la operación inversa: la **división de expresiones algebraicas**.

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | | [[Clase 04|Clase 04 ➡]]