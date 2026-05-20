# 📖 Guía de estudio — Clase 03: Multiplicación de expresiones algebraicas

¡Qué tal, amigos! Espero que estén muy bien. Hoy vamos a profundizar en el arte de multiplicar polinomios. No se asusten por ver muchas letras; si seguimos un orden lógico y recordamos un par de trucos, verán que es un proceso muy sencillo y mecánico. ¡Vamos a por ello!

> [!info] 📌 Conceptos clave
> 1. **Orden de la multiplicación:** Para no perdernos, siempre multiplicamos en este orden: primero los **signos**, segundo los **números** (coeficientes) y tercero las **letras**.
> 2. **Ley de los exponentes:** Cuando multiplicamos letras iguales, la base se mantiene y los exponentes se suman ($x^a \cdot x^b = x^{a+b}$).
> 3. **Propiedad distributiva:** Se trata de una fiesta donde "todos bailan con todos". Multiplicamos cada término del primer paréntesis por cada uno de los términos del segundo.
> 4. **Reducción de términos semejantes:** Al final, agrupamos los términos que tienen las mismas letras y exponentes. Aquí es donde aplicamos la lógica de "debo y tengo".

## Sección: Fórmulas y definiciones importantes

| Término | Definición / Fórmula | Aplicación |
| :--- | :--- | :--- |
| **Regla de los signos** | Signos iguales dan (+); signos diferentes dan (-). | Determina el signo del nuevo término antes de tocar los números. |
| **Producto de potencias** | $x^n \cdot x^m = x^{n+m}$ | Al multiplicar $x^2 \cdot x^3 = x^5$. **Nota:** Si una letra no tiene exponente, hay un **1 invisible**. |
| **Términos semejantes** | Términos con idénticas letras y exponentes. | Usamos la lógica de "debo" (negativo) y "tengo" (positivo) para la suma o resta final. |
| **Orden alfabético** | Propiedad conmutativa: el orden de factores no altera el producto. | Escribimos $xy$ en lugar de $yx$ para identificar rápidamente los términos semejantes. |

---

## Sección: Ejemplos resueltos adicionales

Comencemos analizando el caso más común en los exámenes: el producto de dos binomios. Presten mucha atención al orden de los pasos.

```ad-example
title: Ejemplo A — Binomio por Binomio
**Ejercicio:** Resolver $(3x + 2y)(5x - 4y)$

* **Paso 1: Multiplicar el primer término ($3x$) por todo el segundo paréntesis.**
  - $(3x)(5x) = 15x^2$ (Positivo, 3*5=15, x*x=x²)
  - $(3x)(-4y) = -12xy$ (Más por menos es menos, 3*4=12, letras x y y)

* **Paso 2: Multiplicar el segundo término ($2y$) por todo el segundo paréntesis.**
  - $(2y)(5x) = +10xy$ (Ordenamos alfabéticamente: $xy$ en lugar de $yx$)
  - $(2y)(-4y) = -8y^2$ (Más por menos es menos, 2*4=8, y*y=y²)

* **Paso 3: Reducción de términos semejantes.**
  - Tenemos los términos centrales: $-12xy + 10xy$.
  - Aplicando la lógica del Profe Alex: **"Debo 12 y tengo 10"**. Como pago 10, quedo debiendo 2. El resultado es $-2xy$.

**Resultado final:** $15x^2 - 2xy - 8y^2$
```

Ahora, elevemos un poco el nivel aplicando el álgebra a un problema de finanzas y situaciones reales. Verán que el álgebra es una herramienta poderosa para calcular costos.

```ad-example
title: Ejemplo B — Aplicación de Costos ($USD)
**Enunciado:** El precio unitario de un artículo financiero es $(x + 3)$ dólares y la cantidad comprada es de $(2x - 5)$ unidades. Exprese el costo total como un polinomio.

* **Planteamiento:** Multiplicamos el precio por la cantidad: $(x + 3)(2x - 5)$
* **Desarrollo:**
  1. $(x)(2x) = 2x^2$
  2. $(x)(-5) = -5x$
  3. $(3)(2x) = +6x$
  4. $(3)(-5) = -15$
* **Reducción:** Operamos $-5x + 6x$. "Debo 5 y tengo 6", por lo tanto, me queda 1 positivo ($+1x$).
* **Resultado (Costo Total):** La expresión de la función de costo es $C(x) = 2x^2 + x - 15$ USD.
```

---

## Sección: Ejercicios de repaso

¡Es tu turno de practicar! Recuerda ir paso a paso, cuidando los signos como si fueran tesoros.

```ad-abstract
title: 🟢 Nivel: Fácil
1. $(x + 5)(x + 2)$
2. $(a - 3)(a + 4)$
3. $(y - 1)(y - 6)$
```

```ad-abstract
title: 🟡 Nivel: Medio
1. $(\frac{2}{3}x^2 + 1)(3x - 6)$
2. $(\frac{1}{5}x - 2)(\frac{1}{2}x + 10)$
3. $(\frac{2}{3}x^2)(\frac{1}{5}x - \frac{1}{2})$
```

```ad-abstract
title: 🔴 Nivel: Avanzado — Aplicación con $USD
**Problema de Dimensiones y Volumen:**
Una caja de ahorros física tiene dimensiones representadas por los factores $(x+3)$, $(2x-5)$, y $(3x-1)$. Calcula la expresión del volumen total ($V$) en dólares o unidades cúbicas multiplicando los tres factores.

*Sugerencia: Multiplica primero los dos primeros factores, simplifica el resultado usando "debo/tengo", y luego multiplica ese nuevo polinomio por el tercer factor $(3x-1)$.*
```

---

## Sección: Consejo de estudio

> [!tip] 💡 Consejo de estudio
> Para obtener resultados profesionales y evitar errores de último minuto, sigue siempre estas dos reglas de oro:
> 1. **Organización final:** Ordena tu resultado de forma descendente respecto a una letra (por ejemplo, desde la $x^3$, pasando por $x^2$, hasta la $x$ sola). ¡Se ve mucho más elegante y es más fácil de revisar!
> 2. **Verificación de signos:** Antes de sumar o restar términos semejantes, detente un segundo. Verifica que los signos de la multiplicación inicial sean correctos. Un solo signo mal colocado al principio arruinará todo tu esfuerzo final. ¡Tómate tu tiempo!