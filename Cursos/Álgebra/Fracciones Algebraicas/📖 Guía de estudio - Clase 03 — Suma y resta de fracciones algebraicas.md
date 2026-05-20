# 📖 Guía de estudio — Clase 03: Suma y resta de fracciones algebraicas

> [!info] 📌 Conceptos clave
> ¡Hola! Bienvenido a esta guía. Para dominar la suma y resta de fracciones algebraicas, recuerda que la clave no es memorizar, sino entender el proceso. Aquí tienes los 4 pilares fundamentales:
> 1. **Identificar el tipo de fracción:** Las **homogéneas** tienen el mismo denominador y se operan directamente. Las **heterogéneas** tienen denominadores distintos y requieren un paso extra para igualarlas.
> 2. **Paso 1 — Hallar el MCM:** Es el corazón del proceso. Si hay polinomios, **primero factoriza**. El MCM será el producto de los factores comunes y no comunes con su mayor exponente.
> 3. **Paso 2 — Amplificar:** Multiplicamos el numerador y el denominador de cada fracción por lo que le "falta" para convertirse en el MCM.
> 4. **Paso 3 — Operar y Simplificar:** Sumamos o restamos los numeradores (¡dejando la operación indicada primero!) y simplificamos el resultado final si es posible.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Fracciones Homogéneas** | Son aquellas con denominadores idénticos. Solo se operan los numeradores: $\frac{a}{c} \pm \frac{b}{c} = \frac{a \pm b}{c}$. |
| **Mínimo Común Múltiplo (MCM)** | En monomios: producto de coeficientes (MCM numérico) y letras al mayor exponente. En polinomios: **se debe factorizar primero**; el MCM es el producto de todos los factores presentes al mayor exponente. |
| **Amplificación** | Proceso de multiplicar toda la fracción (arriba y abajo) por un mismo factor para obtener una fracción equivalente con el denominador común deseado. |
| **Simplificación final** | **¡Ojo aquí!** Solo puedes simplificar términos que se estén **multiplicando** (factores). Si hay sumas o restas, primero debes factorizar el resultado final para ver qué se puede cancelar. |

## Ejemplos resueltos adicionales

> [!example] Ejemplo A — Caso Básico (Monomios Heterogéneos)
> **Problema:** Resuelve paso a paso la suma: $\frac{x}{3a^2b^2} + \frac{x}{2a^2b}$
> 
> ¡No te preocupes! Vamos a hacerlo con calma siguiendo los pasos del Profe Alex:
> 
> *   **Paso 1: Hallar el MCM.**
>     *   Números (3 y 2): El MCM es $6$.
>     *   Letras ($a^2b^2$ y $a^2b$): Tomamos las de mayor exponente, es decir, $a^2b^2$.
>     *   **MCM Final** = $6a^2b^2$.
> 
> *   **Paso 2: Amplificar numeradores.**
>     *   Fracción 1: Para que $3a^2b^2$ llegue a ser $6a^2b^2$, le falta multiplicar por $2$. Numerador: $x \cdot (2) = 2x$.
>     *   Fracción 2: Para que $2a^2b$ llegue a ser $6a^2b^2$, le falta multiplicar por $3b$. Numerador: $x \cdot (3b) = 3bx$.
> 
> *   **Paso 3: Operar y Simplificar.**
>     Dejamos la operación indicada sobre el denominador común:
>     $$\frac{2x + 3bx}{6a^2b^2}$$
>     Para un acabado profesional, factorizamos el numerador (factor común $x$):
>     $$\frac{x(2 + 3b)}{6a^2b^2}$$

> [!example] Ejemplo B — Aplicación con contexto ($USD)
> **Problema:** Un estudiante compra dos artículos. El primero cuesta $\frac{x+1}{3x}$ y el segundo $\frac{x-1}{2x}$. ¿Cuál es el gasto total en dólares?
> 
> *   **Lógica:** Sumamos ambos precios. Como los denominadores son distintos, buscamos el MCM.
> *   **Desarrollo:**
>     1. **Hallar el MCM:** Entre $3x$ y $2x$, el MCM es $6x$.
>     2. **Amplificar (Paso vital):**
>        *   Artículo 1: Multiplicamos por $2 \rightarrow \frac{2(x+1)}{6x}$.
>        *   Artículo 2: Multiplicamos por $3 \rightarrow \frac{3(x-1)}{6x}$.
>     3. **Dejar la operación indicada:** Usamos paréntesis para proteger los numeradores.
>        $$\frac{2(x+1) + 3(x-1)}{6x}$$
>     4. **Resolver y reducir:**
>        $$\frac{2x + 2 + 3x - 3}{6x} = \frac{5x - 1}{6x}$$
> *   **Resultado:** El gasto total es $\frac{5x - 1}{6x}$ USD. ¡Excelente trabajo!

## Ejercicios de repaso

> [!abstract] 🟢 Nivel: Fácil (Fracciones Homogéneas)
> Recuerda: deja el mismo denominador y suma/resta lo de arriba.
> 1. $\frac{7}{3a} + \frac{2}{3a} - \frac{5}{3a}$
> 2. $\frac{2x+3}{5y} + \frac{x-1}{5y}$
> 3. $\frac{3a-2}{b^2} - \frac{a+4}{b^2}$ (¡Cuidado con el signo menos antes del paréntesis!)

> [!abstract] 🟡 Nivel: Medio (Fracciones Heterogéneas)
> Primero halla el MCM de los monomios, amplifica y resuelve:
> 1. $\frac{5}{4x} + \frac{2}{3x^2}$
> 2. $\frac{b}{10a} - \frac{3}{5a^2}$
> 3. $\frac{x+2}{3x} + \frac{4}{2x^2}$

> [!abstract] 🔴 Nivel: Avanzado (Aplicación con Polinomios)
> ¡Aquí es donde te vuelves un experto! Estos problemas tienen denominadores diferentes que son polinomios.
> 1. **El Vuelto:** Tienes un presupuesto de $\frac{5}{x-3}$ dólares. Si compras un dulce que cuesta $\frac{2}{x+2}$ dólares, ¿cuál es el saldo restante? (Pista: El MCM será $(x-3)(x+2)$).
> 2. **Saldo Pendiente:** Una deuda total es de $\frac{x}{x+1}$ dólares. Si ya pagaste $\frac{3}{x-1}$ dólares, ¿qué expresión representa lo que aún debes?

> [!tip] 💡 Consejo de estudio: La regla de "Dejar Indicado"
> El error más grave en álgebra es olvidar que un signo negativo $(-)$ antes de una fracción afecta a **todo** el numerador. Para evitar esto, sigue el consejo del Profe Alex:
> 
> 1. **Usa paréntesis siempre:** Al unir las fracciones, escribe el numerador entre paréntesis.
> 2. **Deja la operación indicada:** No multipliques ni restes mentalmente en el primer paso. Escribe: $\frac{-(x+5)}{\dots}$ antes de convertirlo en $\frac{-x-5}{\dots}$.
> 3. **No simplifiques sumas:** Nunca canceles una $x$ arriba y abajo si está sumando. Solo simplifica cuando hayas factorizado y todo esté multiplicando.