# 📖 Guía de estudio — Clase 10: Distancia de un punto a una recta

¡Hola! Bienvenido a una nueva sesión. Hoy vamos a dominar un truco matemático súper útil para encontrar la ruta más corta entre un punto y una recta. Verás que, siguiendo los pasos lógicos, este concepto se vuelve muy sencillo. ¡Vamos a por ello!

> [!info] 📌 Conceptos clave
> 1.  La **distancia** es el trayecto más corto entre un punto y una recta. Para que sea la mínima, el segmento debe ser **perpendicular** a la recta, es decir, formar un ángulo de 90°.
> 2.  Para aplicar la fórmula, la recta **debe** estar escrita en su **forma general** ($Ax + By + C = 0$). ¡Pilas! Esto significa que debe estar igualada a cero.
> 3.  Usamos los coeficientes **$A$**, **$B$** y **$C$** de la recta y las coordenadas **$(x, y)$** del punto. **Tip de Profe:** Si ves que la $x$ o la $y$ están "solas", recuerda que su coeficiente es **1** (o **-1** si tiene un signo menos).
> 4.  ¡Ojo! Usamos el **valor absoluto** ($| |$) en el numerador para que nunca nos dé una distancia negativa. ¡Las distancias siempre son resultados positivos!

## Fórmulas y definiciones importantes

| **Término** | **Fórmula / Definición** |
| :--- | :--- |
| **Ecuación General de la Recta** | $Ax + By + C = 0$ |
| **Fórmula de Distancia ($d$)** | $d = \frac{|Ax + By + C|}{\sqrt{A^2 + B^2}}$ |
| **Punto conocido** | Coordenadas $(x_1, y_1)$ desde donde se mide la distancia. |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Aplicación directa de la fórmula
**Problema:** Hallar la distancia del punto $(3, -2)$ a la recta $3x - 4y + 1 = 0$.

**Paso 1: Identificar valores.**
*   Coeficientes de la recta: **$A = 3$**, **$B = -4$**, **$C = 1$**.
*   Coordenadas del punto: **$x = 3$**, **$y = -2$**.

**Paso 2: Sustituir en la fórmula.**
$d = \frac{|(3)(3) + (-4)(-2) + 1|}{\sqrt{3^2 + (-4)^2}}$

**Paso 3: Operaciones aritméticas.**
*   Numerador: $|9 + 8 + 1| = |18| = 18$.
*   Denominador: $\sqrt{9 + 16} = \sqrt{25} = 5$.
*   División: $18 / 5 = 3,6$.

**Resultado:** La distancia es **3,6** unidades.
```

```ad-example
title: Ejemplo B — Optimización de costos de instalación ($USD)
**Escenario:** Una constructora instalará una tubería desde un punto de control en $( -3, 2)$ hasta una vía principal ($3x - 4y - 3 = 0$). El costo es de **$150 USD** por unidad de distancia.

**Paso 1: Calcular la distancia mínima.**
*   Numerador: $|3(-3) + (-4)(2) - 3| = |-9 - 8 - 3| = |-20| = 20$.
*   Denominador: $\sqrt{3^2 + (-4)^2} = \sqrt{25} = 5$.
*   Distancia: $20 / 5 = \mathbf{4}$ **unidades**.

**Paso 2: Calcular el costo total.**
*   Costo = $4 \text{ unidades} \times \$150 \text{ USD} = \$600 \text{ USD}$.

**Resultado:** El costo total de la obra será de **$600 USD**.
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel: Fácil
Calcula la distancia de los siguientes puntos a sus rectas (ya en forma general):
1. Punto $(2, 3)$ y la recta $4x + 3y + 1 = 0$.
2. Punto $(1, -1)$ y la recta $3x - 4y + 2 = 0$.
3. Punto $(0, 5)$ y la recta $5x + 12y + 3 = 0$.
```

```ad-abstract
title: 🟡 Nivel: Medio
Primero, transforma las ecuaciones a su **forma general** ($Ax + By + C = 0$) pasando todo a un solo lado y luego halla la distancia:
1. Punto $(1, 2)$ y la recta $y = 2x + 5$.
2. Punto $(-2, 4)$ y la recta $3y = 4x - 1$.
3. Punto $(3, 0)$ y la recta $y = -x + 4$.
```

```ad-abstract
title: 🔴 Nivel: Avanzado — Aplicación con $USD
**Problema de presupuesto:** Se conectará una antena en $(1, 4)$ con una carretera cuya trayectoria es $y = \frac{2}{3}x + 2$.
1. Convierte la ecuación a su **forma general**. **Tip de Profe Alex:** Multiplica cada término por el denominador (3) para dejar la ecuación limpia y sin fracciones.
2. Calcula la **distancia** (aproxima a un decimal).
3. Si el cable cuesta **$200 USD** por unidad, ¿cuál es el presupuesto total?
```

> [!tip] 💡 Consejo de estudio
> Para no liarte con los signos y calcular más rápido, haz como yo: escribe los valores de **$A, B, C$** y, justo debajo, los de **$x, y$**. Así verás las multiplicaciones verticales de forma clarísima antes de sumarlas en el numerador. 

¡Sigue practicando con entusiasmo! Cada ejercicio que resuelves te hace más hábil en el mundo de las matemáticas. ¡Tú puedes!