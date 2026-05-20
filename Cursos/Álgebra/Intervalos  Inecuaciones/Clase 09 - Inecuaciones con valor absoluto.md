# Clase 09 — Inecuaciones con valor absoluto

> [!info] 🧭 Navegación
> [[Clase 08 — Inecuaciones Lineales]] | [[Índice del Curso]] | [[Clase 10 — Inecuaciones Complejas]]

> [!info] 🌍 Relevancia y aplicaciones
> ¡Qué tal amigos! El valor absoluto es fundamental porque nos permite medir distancias y márgenes de error. No nos importa si la diferencia es a favor o en contra, lo que nos interesa es qué tan lejos estamos de nuestro objetivo.
> - 💵 **[USD]:** Determina el rango de fluctuación permitido en el precio de una divisa antes de ejecutar una orden.
> - 🏗️ **[Práctica]:** Establece la tolerancia técnica en las medidas de una pieza de construcción para que encaje con precisión.
> - 📊 **[Cotidiana]:** Define la diferencia de temperatura aceptable en un termostato antes de que se encienda el aire acondicionado.

> [!note] 📌 ¿Qué es Inecuaciones con valor absoluto?
> Resolver estas inecuaciones consiste en buscar todos los valores cuya **distancia al cero** cumple una condición (ser menor o mayor que un número). Recuerden que el valor absoluto básicamente "quita el signo", dejando solo la magnitud. 
> 
> **¡Ojo con esto!** La clave está en los paréntesis y corchetes:
> - Si usamos `<` o `>`, usamos **paréntesis ( )** (intervalo abierto, no incluye el número).
> - Si usamos `≤` o `≥`, usamos **corchetes [ ]** (intervalo cerrado, incluye el número).

> [!warning] ⚠️ Error común
> **¡Pilas aquí!** El error más grave es resolverlo como una ecuación normal y dar un solo número. Siempre existen dos partes en la solución. Además, nunca olviden que si el valor absoluto debe ser "menor que un negativo" (ej. $|x| < -5$), la respuesta es el **conjunto vacío**, porque una distancia nunca es negativa.

> [!tip] 💡 Truco para recordarlo
> - **Menor que (< / ≤):** Se crea un **"Sándwich"**. La solución es un solo intervalo atrapado entre dos valores. (Relacionado con la intersección "y").
> - **Mayor que (> / ≥):** Se crean **"Dos alas"**. La solución son dos intervalos que se alejan hacia los infinitos. (Relacionado con la unión "o").

---

### PROCEDIMIENTO PASO A PASO

Para resolver inecuaciones con valor absoluto, identifique el signo y siga estos pasos:

```text
SI EL SIGNO ES "MENOR QUE" (< o ≤) — EL SÁNDWICH:
PASO 1 → Verifique que el número 'a' sea positivo.
PASO 2 → Plantee la inecuación doble: -a ≤ expresión ≤ a.
PASO 3 → Despeje la 'x' operando en los tres lados de la desigualdad.
PASO 4 → Exprese el resultado en notación de intervalo (bloque único).

SI EL SIGNO ES "MAYOR QUE" (> o ≥) — LAS DOS ALAS:
PASO 1 → Plantee dos casos: (expresión < -a) O (expresión > a).
PASO 2 → Despeje la 'x' en cada inecuación por separado.
PASO 3 → Exprese el resultado como la unión (U) de los dos intervalos.
```

---

### BLOQUES DE EJEMPLOS PRÁCTICOS

#### Ejemplo 1 (Caso Básico: Dos Alas)
**Problema:** Resolver $|x| > 3$
*   **Explicación:** Buscamos números cuya distancia al cero sea mayor a 3. Esto ocurre para los números muy grandes a la derecha o muy "pequeños" a la izquierda.
*   **Planteamiento:** $x < -3$ o $x > 3$.
*   ✅ **Resultado:** $(-\infty, -3) \cup (3, \infty)$.

#### Ejemplo 2 (Caso con signos: Sándwich)
**Problema:** Resolver $|x - 3| \leq 12$
*   **Despeje:** Como es "menor o igual", aplicamos el sándwich:
    $$-12 \leq x - 3 \leq 12$$
*   Para dejar la $x$ sola, el $-3$ pasa a sumar a ambos lados:
    $$-12 + 3 \leq x \leq 12 + 3$$
    $$-9 \leq x \leq 15$$
*   **¡Pilas!** Usamos corchetes porque el signo incluye el "igual".
*   ✅ **Resultado:** $[-9, 15]$.

#### Ejemplo 3 (Caso Avanzado)
**Problema:** Resolver $|2x - 3| < 7$
*   **Planteamiento:** $-7 < 2x - 3 < 7$
*   **Paso 1 (Sumar 3 en todo lado):** $-7 + 3 < 2x < 7 + 3 \implies -4 < 2x < 10$
*   **Paso 2 (Dividir entre 2):** Como el 2 es positivo, los signos no cambian:
    $$\frac{-4}{2} < x < \frac{10}{2}$$
    $$-2 < x < 5$$
*   ✅ **Resultado:** $(-2, 5)$.

#### Ejemplo 4 (Aplicación USD)
**Problema:** Un producto cuesta $50 USD, pero su precio fluctúa en un margen de máximo $5 USD.
*   **Planteamiento de la inecuación:** $|x - 50| \leq 5$
*   **Resolución:** $-5 \leq x - 50 \leq 5$. Sumamos 50 en ambos lados:
    $$50 - 5 \leq x \leq 50 + 5$$
    $$45 \leq x \leq 55$$
*   ✅ **Resultado:** $[45, 55]$. El precio puede estar entre los 45 y los 55 dólares.

---

### EJERCICIOS PARA EL ESTUDIANTE

> [!abstract] 🟢 Nivel Fácil
> 1. $|x| < 8$
> 2. $|x| > 12$
> 3. $|x| \leq 5$
> 4. $|x| \geq 9$

> [!abstract] 🟡 Nivel Medio
> 1. $|x - 4| \leq 6$
> 2. $|x + 3| < 10$
> 3. $|x - 2| \geq 5$
> 4. $|x + 7| > 3$

> [!abstract] 🔴 Nivel Avanzado
> 1. **Finanzas:** Un activo de $100 USD fluctúa según $|x - 100| \leq 2$. Halle el rango.
> 2. **Tolerancia técnica:** Una pieza de 10 cm tiene una tolerancia de $|x - 10| \leq 0.05$. Halle el rango permitido.
> 3. **Operativo:** Resolver $|3x - 6| < 9$.
> 4. **Operativo:** Resolver $|2x + 4| \geq 10$.

> [!success] ✅ Respuestas para el docente
> - **Fácil:** 1. (-8, 8) | 2. (-∞, -12) U (12, ∞) | 3. [-5, 5] | 4. (-∞, -9] U [9, ∞)
> - **Medio:** 1. [-2, 10] | 2. (-13, 7) | 3. (-∞, -3] U [7, ∞) | 4. (-∞, -10) U (-4, ∞)
> - **Avanzado:** 1. [98, 102] USD | 2. [9.95, 10.05] cm | 3. (-1, 5) | 4. (-∞, -7] U [3, ∞)

---

### MINI-PRUEBA DE AUTOEVALUACIÓN

> [!question] Pregunta 1: El caso del vacío
> ¿Cuál es el conjunto solución de $|x| < -10$?
> **Respuesta:** **Conjunto vacío (Ø)**. ¡Pilas! No existen distancias menores a un número negativo. El valor absoluto siempre da un resultado positivo o cero.

> [!question] Pregunta 2: El caso de los Reales
> ¿Qué sucede si tenemos $|x| > -3$?
> **Respuesta:** La solución son **Todos los números Reales ($\mathbb{R}$)**. Como cualquier valor absoluto será positivo o cero, siempre será mayor que cualquier número negativo.

> [!question] Pregunta 3: Procedimiento de despeje
> Si resolvemos $|x - 5| \leq 10$, ¿por qué sumamos 5 a ambos extremos del sándwich?
> **Respuesta:** Para mantener el equilibrio de la inecuación. Lo que se hace en el centro para dejar a la $x$ sola, debe hacerse obligatoriamente en el lado izquierdo y el derecho.

---

> [!tip] 💡 En la próxima clase
> Como siempre, por último, les cuento que en la siguiente clase veremos ejercicios más difíciles donde la $x$ tiene coeficientes negativos. ¡Ahí es donde debemos tener cuidado con el sentido de la desigualdad!

> [!info] 🧭 Navegación
> [[Clase 08 — Inecuaciones Lineales]] | [[Índice del Curso]] | [[Clase 10 — Inecuaciones Complejas]]