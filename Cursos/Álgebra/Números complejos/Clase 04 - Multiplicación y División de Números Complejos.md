# Clase 04 — Multiplicación y División de Números Complejos

**Anterior:** [[Clase 03]] | **Siguiente:** [[Clase 05]]

---

¡Qué tal amigas y amigos! Espero que estén muy bien. Hoy vamos a aprender a realizar operaciones con números complejos de una forma supremamente fácil y detallada. Veremos que, aunque parezcan conceptos de otro mundo, se manejan de forma muy similar al álgebra que ya conocemos, pero con un par de trucos especiales que nos facilitarán la vida.

## ¿Por qué es importante esta clase?

Los números complejos son una herramienta fundamental que permite resolver ecuaciones que no tienen solución en el conjunto de los números reales. En el campo de la ingeniería y las ciencias, facilitan el modelado de fenómenos oscilatorios y dinámicos que los números tradicionales no pueden capturar por sí solos.

*   **💰 Dinero (USD):** Se utilizan en modelos financieros avanzados para calcular intereses compuestos donde la tasa presenta oscilaciones; representar flujos de capital como $10 + 2i$ permite modelar variaciones estacionales en el mercado.
*   **🏗️ Construcción:** Son esenciales en el análisis de estructuras y el estudio de ondas, permitiendo a los ingenieros predecir cómo vibrará un edificio ante diferentes fuerzas sísmicas o de viento.
*   **📶 Situación cotidiana:** Cada vez que utilizas tu señal de Wi-Fi o escuchas procesamiento de audio digital, los números complejos están trabajando para filtrar interferencias y que la información llegue nítida.

---

> [!note] **Concepto Clave: Multiplicación de Complejos Conjugados**
> El **conjugado** de un número complejo es simplemente su "gemelo", pero con el signo de la parte imaginaria cambiado. Si tienes $a + bi$, su conjugado es $a - bi$. 
> 
> > [!warning] **Error común**
> > El error más frecuente es cambiar el signo de la parte real en lugar de la imaginaria, o confundir el valor de $i^2$. Recuerda siempre: **$i^2 = -1$**. Nunca lo reemplaces por $1$ positivo.
> 
> > [!tip] **Truco: El atajo del cuadrado**
> > Para multiplicar un complejo por su conjugado, no necesitas hacer toda la propiedad distributiva. Usa la fórmula rápida: **$a^2 + b^2$**. El resultado siempre será un número real positivo y habrás eliminado la $i$.

---

## Procedimiento Paso a Paso: División de Complejos

Para dividir complejos, el objetivo fundamental es **eliminar la unidad imaginaria ($i$) del denominador** para que el resultado final tenga la forma estándar $a + bi$.

```text
PASO 1 → Identificar el conjugado del denominador (cambiar signo a la parte imaginaria).
PASO 2 → Multiplicar tanto el numerador como el denominador por dicho conjugado.
PASO 3 → Resolver las multiplicaciones:
         - Numerador: Aplicar propiedad distributiva.
         - Denominador: Aplicar el "atajo del cuadrado" (a² + b²).
PASO 4 → Reemplazar i² por -1, simplificar términos y separar en parte real e imaginaria.
```

---

## Ejemplos Prácticos

> [!example] **Ejemplo 1: División Detallada**
> **Calcular:** $\frac{6 + 4i}{3 - 5i}$
> 1. Multiplicamos arriba y abajo por el conjugado del denominador $(3 + 5i)$.
> 2. **Denominador (Atajo):** Aplicamos $a^2 + b^2 \rightarrow 3^2 + 5^2 = 9 + 25 = 34$.
> 3. **Numerador (Distributiva):** $18 + 30i + 12i + 20i^2 = 18 + 42i + 20(-1) = 18 - 20 + 42i = -2 + 42i$.
> 4. **Resultado final:** $\frac{-2}{34} + \frac{42i}{34}$.
> 5. **Simplificado:** $-\frac{1}{17} + \frac{21}{17}i$.

> [!example] **Ejemplo 2: Multiplicación con Signos**
> **Calcular:** $Z_1 \cdot Z_2$ donde $Z_1 = -3 - 5i$ y $Z_2 = 7 - 9i$
> 1. Aplicamos distributiva: $(-3 \cdot 7) + (-3 \cdot -9i) + (-5i \cdot 7) + (-5i \cdot -9i)$.
> 2. Esto nos da: $-21 + 27i - 35i + 45i^2$.
> 3. Reemplazamos $i^2$ por $-1$: $-21 - 8i + 45(-1) = -21 - 8i - 45$.
> 4. **Resultado:** $-66 - 8i$.

> [!example] **Ejemplo 3: Suma y Resta (Fidelidad al Origen)**
> **Calcular:** $(7 + 2i) - (5 + 9i)$
> 1. El signo negativo cambia los signos de los términos dentro del segundo paréntesis: $7 + 2i - 5 - 9i$.
> 2. Agrupamos reales con reales e imaginarios con imaginarios: $(7 - 5) + (2i - 9i)$.
> 3. **Resultado:** $2 - 7i$.

> [!example] **Ejemplo 4: Aplicación Financiera ($USD)**
> **Situación:** Una empresa suma dos flujos de capital: $C_1 = 10 + 2i$ y $C_2 = 15 - 8i$.
> 1. Sumamos las partes reales: $10 + 15 = 25$.
> 2. Sumamos las partes imaginarias: $2i - 8i = -6i$.
> 3. **Balance final:** $25 - 6i$ USD (Donde 25 es la base fija y -6i representa el ajuste de riesgo).

---

## Ejercicios para el Estudiante

> [!abstract] **Nivel Verde (Fácil)**
> 1. $(5 + 2i) + (4 + 7i)$
> 2. $(10 + 15i) + (3 - 6i)$
> 3. $(7 + 2i) - (5 + 9i)$
> 4. $(-1 + i) - (-3 + 2i)$

> [!abstract] **Nivel Amarillo (Medio)**
> 1. Multiplica el complejo $(3 + 2i)$ por su propio conjugado.
> 2. Resuelve la división: $\frac{3i}{6 + 2i}$
> 3. Multiplica el complejo $(2 - 3i)$ por su propio conjugado.
> 4. Resuelve la división: $\frac{1 + i}{2 - 3i}$

> [!abstract] **Nivel Rojo (Avanzado)**
> Un proyecto de inversión reporta un beneficio total de $100 + 40i$ USD distribuido en un periodo de tiempo complejo de $2 + 2i$ unidades. ¿Cuál es el beneficio promedio por unidad de tiempo? (Pista: Divide el beneficio entre el tiempo).

> [!success] **Respuestas para el Docente**
> **Verde:** 1) $9+9i$; 2) $13+9i$; 3) $2-7i$; 4) $2-i$.
> **Amarillo:** 1) $13$; 2) $\frac{3}{20} + \frac{9}{20}i$; 3) $13$; 4) $-\frac{1}{13} + \frac{5}{13}i$.
> **Rojo:** $35 - 15i$ USD.

---

## Autoevaluación

> [!question] **Pregunta 1**
> Si el número complejo es $-4 + 8i$, ¿qué sucede con el signo de la parte imaginaria al buscar su conjugado?
> *Respuesta: Cambia al signo opuesto, por lo que el conjugado es $-4 - 8i$.*

> [!question] **Pregunta 2**
> ¿Cuál es el valor por el que debemos sustituir siempre $i^2$ para simplificar la expresión?
> *Respuesta: Siempre se sustituye por $-1$.*

> [!question] **Pregunta 3**
> Si sumas un flujo de activos de $50 + 10i$ USD con una deuda (flujo negativo) de $20 + 5i$ USD, ¿cuál es el saldo resultante?
> *Respuesta: $(50 - 20) + (10i - 5i) = 30 + 5i$ USD.*

---

### Notas para el próximo tema
¡Felicidades por completar esta clase! Ahora que ya dominas las cuatro operaciones básicas (suma, resta, multiplicación y división), estamos listos para dar el siguiente paso lógico. En la próxima sesión exploraremos las **Potencias de $i$**, donde descubriremos el asombroso comportamiento cíclico de la unidad imaginaria. ¡Nos vemos en la próxima clase!

**Anterior:** [[Clase 03]] | **Siguiente:** [[Clase 05]]