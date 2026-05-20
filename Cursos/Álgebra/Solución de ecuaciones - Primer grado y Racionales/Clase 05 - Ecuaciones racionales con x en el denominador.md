# Clase 05 — Ecuaciones racionales con x en el denominador

`#matemáticas` `#álgebra` `#ecuaciones_racionales` `#pkm`

---
**Navegación:** [[Clase 04]] | **Clase 05** | [[Clase 06]]

---

## ¿Por qué es importante esta clase?

Las ecuaciones racionales son herramientas esenciales para modelar situaciones de proporcionalidad inversa, especialmente cuando la incógnita representa una unidad de reparto o una tasa de participación en un proceso.

**Ejemplo financiero:**
Imagina que una organización destina un fondo total de **$1000 USD** para ser repartido equitativamente entre un grupo desconocido de personas ($x$). El monto que recibe cada individuo se expresa mediante la fracción $1000/x$. Si el monto individual cambia o se suma a otros fondos, para determinar cuántas personas participan en el reparto, es necesario transformar la ecuación racional en una ecuación lineal multiplicando por el MCM para despejar la incógnita del denominador.

## Concepto clave

*   **Definición:** Una ecuación racional es aquella donde la incógnita aparece en el denominador. El objetivo didáctico es transformar esta expresión en una ecuación lineal mediante la eliminación de denominadores, utilizando el principio de igualdad.
*   **Error crítico:** **El fallo más común es multiplicar únicamente las fracciones por el MCM y olvidar multiplicar los términos constantes o enteros.** Recuerda: para mantener la igualdad, **todos** los términos de la ecuación deben ser multiplicados por el MCM.
*   **Truco de experto:** Siempre que existan variables con exponentes distintos en los denominadores, para construir el MCM debemos elegir la variable con el exponente más grande.

## Procedimiento paso a paso

Para resolver estas ecuaciones con la metodología del "profe Alex", aplica sistemáticamente estos pasos:

```text
1. Obtener el MCM de los coeficientes numéricos de los denominadores.
2. Agregar la variable "x" al MCM (usando el mayor exponente presente).
3. Multiplicar cada término de la ecuación original por este MCM resultante.
4. Simplificar cada término para eliminar los denominadores y resolver la ecuación lineal.
```

## Ejemplos de la Clase

> [!example] **Ejemplo 1: Fundamentos de resolución**
> **Ecuación:** $\frac{1}{x} + \frac{1}{2x} = \frac{3}{10}$
> 1. **Determinar MCM:** El MCM de 2 y 10 es 10. Agregamos la variable: **$10x$**.
> 2. **Multiplicación de términos:**
>    - $10x \cdot (\frac{1}{x}) = 10$ (la variable $x$ se cancela).
>    - $10x \cdot (\frac{1}{2x}) = 5$ (la $x$ se cancela y dividimos 10 entre 2).
>    - $10x \cdot (\frac{3}{10}) = 3x$ (dividimos 10 entre 10, resultando en 1, que multiplica a $3x$).
> 3. **Resolución:** $10 + 5 = 3x \rightarrow 15 = 3x \rightarrow x = 5$.

> [!example] **Ejemplo 2: Complejidad y simplificación avanzada**
> **Ecuación:** $\frac{2}{3x} - \frac{5}{x} = \frac{7}{10} - \frac{3}{2x} + 1$
> 1. **Determinar MCM:** El MCM de 3, 10 y 2 es 30. Agregamos la variable: **$30x$**.
> 2. **Simplificación término a término:**
>    - $30x \cdot (\frac{2}{3x}) = 10 \cdot 2 = 20$
>    - $30x \cdot (\frac{5}{x}) = 30 \cdot 5 = 150$
>    - $30x \cdot (\frac{7}{10}) = 3x \cdot 7 = 21x$
>    - $30x \cdot (\frac{3}{2x}) = 15 \cdot 3 = 45$
>    - $30x \cdot (1) = 30x$ (término entero multiplicado por el MCM).
> 3. **Ecuación resultante:** $20 - 150 = 21x - 45 + 30x$
> 4. **Resolución:** $-130 = 51x - 45 \rightarrow -130 + 45 = 51x \rightarrow -85 = 51x$.
> 5. **Resultado:** $x = -85/51$. Dividimos ambos términos por 17 para obtener la fracción irreducible: **$x = -5/3$**.

> [!example] **Ejemplo 3: Práctica de validación**
> **Ecuación:** $\frac{1}{2x} + \frac{1}{4} = \frac{1}{10x} + \frac{1}{5}$
> 1. **MCM:** El MCM de 2, 4, 10 y 5 es 20. Incluimos la variable: **$20x$**.
> 2. **Multiplicación y reducción:**
>    - $10 + 5x = 2 + 4x$
> 3. **Despeje:**
>    - $5x - 4x = 2 - 10$
>    - **$x = -8$**

> [!example] **Ejemplo 4: Aplicación financiera ($USD)**
> **Problema:** Un bono de $300 USD se reparte entre $x$ empleados. Si se suma a un incentivo adicional de $150 USD repartido entre el doble de ese personal ($2x$), el total por beneficiario es de $75 USD. ¿Cuántos empleados hay?
> **Ecuación:** $\frac{300}{x} + \frac{150}{2x} = 75$
> 1. **MCM:** En este caso es **$2x$**.
> 2. **Multiplicación:**
>    - $2x \cdot (\frac{300}{x}) + 2x \cdot (\frac{150}{2x}) = 2x \cdot 75$
>    - $600 + 150 = 150x$
>    - $750 = 150x$
> 3. **Resultado:** $x = 750 / 150 \rightarrow$ **$x = 5$**. Hay 5 empleados.

## Ejercicios para el estudiante

> [!abstract] **🟢 Nivel Fácil**
> Resuelve la siguiente ecuación racional:
> $\frac{1}{x} + \frac{1}{3x} = \frac{4}{9}$

> [!abstract] **🟡 Nivel Medio**
> Resuelve la siguiente ecuación con términos constantes:
> $\frac{1}{x} - \frac{1}{2x} = \frac{5}{4} - \frac{2}{x} + 2$

> [!abstract] **🔴 Nivel Avanzado (Aplicación $USD)**
> Un fondo de inversión de $600 USD se divide entre $x$ inversores. Si se le suma una comisión de gestión de $200/x$ por cada uno y el total resultante por persona es de $40 USD, ¿cuál es el número total de inversores? (Pista: Estructura la ecuación como la suma de montos por persona igual al total individual).

> [!success] **Respuestas**
> 1. **$x = 3$** (MCM: $9x$)
> 2. **$x = 10/13$** (MCM: $4x$, ecuación resultante: $4 - 2 = 5x - 8 + 8x$)
> 3. **$x = 20$** (Ecuación: $\frac{600}{x} + \frac{200}{x} = 40$)

## Mini-prueba de autoevaluación

> [!question] **Pregunta 1**
> ¿Cuál es el primer paso indispensable según la metodología estudiada?
> A) Despejar la variable $x$ de forma inmediata.
> B) Hallar el MCM de los denominadores y añadir la variable $x$.
> C) Sumar los numeradores y denominadores directamente.
> D) Ignorar los denominadores y resolver solo la parte superior.
> **Respuesta correcta: B**

> [!question] **Pregunta 2**
> Al multiplicar el término racional $\frac{7}{2x}$ por un MCM de $14x$, ¿cuál es el resultado simplificado?
> A) $49x$
> B) $98$
> C) $49$
> D) $7$
> **Respuesta correcta: C**

> [!question] **Pregunta 3**
> En la ecuación $\frac{2}{x} = 1$, ¿cuál es el valor de $x$?
> A) $x = 1$
> B) $x = 0.5$
> C) $x = 2$
> D) $x = -2$
> **Respuesta correcta: C**

## Notas para el próximo tema

> [!tip] **Hacia la Clase 06**
> En la próxima sesión, elevaremos el nivel de análisis para abordar ecuaciones donde los denominadores ya no son monomios, sino **binomios** (por ejemplo, $x + 1$ o $x - 3$). Es vital que domines la multiplicación de todos los términos por el MCM antes de avanzar.

---
**Navegación:** [[Clase 04]] | **Clase 05** | [[Clase 06]]