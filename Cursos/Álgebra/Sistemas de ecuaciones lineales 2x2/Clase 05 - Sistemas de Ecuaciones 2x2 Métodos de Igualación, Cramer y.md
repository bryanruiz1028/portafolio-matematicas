# Clase 05 — Sistemas de Ecuaciones 2x2: Métodos de Igualación, Cramer y Fracciones

#algebra #sistemasdeecuac

Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 5 de 8

> [!info] 🧭 Navegación
> *   Anterior: [[Clase 04 — Método de Sustitución]]
> *   Índice: [[00 - Índice del curso]]
> *   **Clase 05 — Sistemas de Ecuaciones 2x2: Métodos de Igualación, Cramer y Fracciones**

---

### ¿Por qué es importante esta clase?

En la vida real, los datos no siempre vienen en números enteros. Aprender a manejar sistemas con fracciones y desorden te permite resolver problemas técnicos y financieros donde las condiciones no son evidentes a simple vista.

*   **💵 [aplicación con $USD]:** Comparar presupuestos donde los gastos se expresan como fracciones de un dólar o calcular el pago de una "deuda" (números negativos) con tasas variables.
*   **🏗️ [aplicación práctica]:** En ingeniería, se usa para equilibrar fuerzas aplicadas en diferentes ángulos o proporciones (fracciones).
*   **📊 [situación cotidiana]:** Determinar la cantidad exacta de ingredientes en una receta o productos en una compra conjunta basándose en proporciones de peso.

---

### Concepto Clave

> [!note] ¿Qué es un sistema 2x2?
> Imagina que tienes un puzzle con dos pistas (ecuaciones). Resolverlo es encontrar el valor exacto de $x$ e $y$ donde ambas condiciones se cumplen al mismo tiempo. Es el punto donde las dos historias coinciden.

> [!warning] ¡Alto! El orden es fundamental en Cramer
> Un error común es aplicar determinantes sin organizar las piezas. Antes de empezar, tus ecuaciones deben tener la forma $Ax + By = C$. Si tienes algo como $15x + 11y - 32 = 0$, ¡mueve ese $-32$ al otro lado como $+32$ inmediatamente!

> [!tip] Regla mnemotécnica: El Método del Espejo
> En la igualación, "espejamos" (despejamos) la misma variable en ambas ecuaciones. Al final, las dos expresiones se miran frente a frente a través del signo igual ($Expresión 1 = Expresión 2$), como si una fuera el reflejo de la otra.

---

### Procedimiento paso a paso para eliminar fracciones

Para que un sistema sea fácil de resolver, primero "limpiamos" las fracciones usando el Mínimo Común Múltiplo (MCM):

```text
PASO 1 → Identificar el MCM de los denominadores de la ecuación.
PASO 2 → Multiplicar cada término de la ecuación por el MCM.
PASO 3 → El MCM "cancela" al de abajo y el resultado multiplica al de arriba.
PASO 4 → Resolver el sistema resultante (ya con números enteros) por tu método favorito.

PRO-TIP: ¡No olvides multiplicar también los números que no tienen fracción!
```

---

### Ejemplos Prácticos

> [!ad-example] Ejemplo 1: Método de Igualación
> **Sistema:**
> 1) $7x + 4y = 13$
> 2) $5x - 2y = 19$
> 
> *   **Despejamos $x$:**
>     *   En (1): $x = \frac{13 - 4y}{7}$
>     *   En (2): $x = \frac{19 + 2y}{5}$
> *   **Igualamos:** $\frac{13 - 4y}{7} = \frac{19 + 2y}{5}$
> *   **Cruzamos productos:** $5(13 - 4y) = 7(19 + 2y)$
> *   **Resultado:** $65 - 20y = 133 + 14y \rightarrow -34y = 68 \rightarrow y = -2$.
> *   **Sustitución final:** $x = 3$.

> [!ad-example] Ejemplo 2: Método de Cramer (Determinantes)
> **Sistema desordenado:**
> $15x + 11y - 32 = 0$
> $7y - 8 = 9x$
> 
> 1. **Ordenamos:** 
>    (1) $15x + 11y = 32$
>    (2) $-9x + 7y = 8$
> 2. **Determinante del Sistema ($\Delta$):** $(15 \cdot 7) - (11 \cdot -9) = 105 - (-99) = 105 + 99 = 204$.
> 3. **Determinante de $x$ ($\Delta x$):** $(32 \cdot 7) - (11 \cdot 8) = 224 - 88 = 136$.
> 4. **Determinante de $y$ ($\Delta y$):** $(15 \cdot 8) - (32 \cdot -9) = 120 - (-288) = 120 + 288 = 408$.
> 5. **Cálculo de variables:**
>    *   $x = \frac{136}{204}$ (Simplificamos: $\frac{68}{102} \rightarrow \frac{34}{51} \rightarrow \frac{2}{3}$).
>    *   $y = \frac{408}{204} = 2$.
> 
> **Nota pedagógica:** Observa cómo el signo negativo de la fórmula y el signo del número se convierten en suma: $120 - (-288) = 408$.

> [!ad-example] Ejemplo 3: Verificación (¡Chequeo doble!)
> Si hallamos que $x = 3, y = 4$ para el sistema:
> (1) $x + 6y = 27$
> (2) $7x - 3y = 9$
> 
> Debes comprobar **ambas** ecuaciones:
> *   En (1): $3 + 6(4) = 3 + 24 = 27$ (Correcto: $27 = 27$).
> *   En (2): $7(3) - 3(4) = 21 - 12 = 9$ (Correcto: $9 = 9$).
> 
> Si solo verificas una y la otra falla, ¡tu solución no es correcta!

> [!ad-example] Ejemplo 4: Fracciones y $USD
> **Contexto:** El costo de media unidad de $A$ menos una deuda de $B$ es igual a una pérdida de $5$ USD.
> (1) $\frac{x}{2} - y = -5$ ($MCM = 2$) $\rightarrow x - 2y = -10$
> (2) $3x + \frac{y}{3} = -9$ ($MCM = 3$) $\rightarrow 9x + y = -27$

---

### Ejercicios para el estudiante

> [!success] 🟢 Nivel Fácil: Igualación
> Resuelve por igualación:
> 1. $x + y = 5$ ; $x - y = 1$
> 2. $2x + y = 7$ ; $x + y = 4$
> 3. $3x + 2y = 12$ ; $x + y = 5$
> 4. $x + 3y = 10$ ; $2x + y = 5$

> [!warning] 🟡 Nivel Medio: Cramer con ordenamiento
> Ordena y resuelve por determinantes:
> 1. $10x + 18y + 11 = 0$ ; $16x - 9y = -5$
> 2. $3x = 2y + 5$ ; $x + y = 10$
> 3. $5y - 12 = -2x$ ; $x - y = 1$
> 4. $2x + 3y = 8$ ; $x - 2y = -3$

> [!danger] 🔴 Nivel Avanzado: Fracciones y MCM
> Elimina denominadores (usa MCM $3, 4, 6$ u $8$) y resuelve:
> 1. $\frac{x}{6} + \frac{y}{4} = 2$ ; $\frac{x}{3} + \frac{y}{8} = 2$
> 2. $\frac{5x}{12} + y = 9$ ; $x + \frac{3y}{4} = 15$
> 3. $\frac{x+3}{3} - \frac{y-4}{6} = 0$ ; $\frac{x}{2} + \frac{y}{5} = 3$
> 4. $\frac{x}{3} + y = \frac{4}{3}$ ; $x - \frac{y}{2} = \frac{1}{2}$

> [!check] ✅ Respuestas (Uso Docente)
> **Fácil:** 1) $x=3, y=2$; 2) $x=3, y=1$; 3) $x=2, y=3$; 4) $x=1, y=3$
> **Medio:** 1) $x=-1/2, y=-1/3$; 2) $x=5, y=5$; 3) $x=17/7, y=10/7$; 4) $x=1, y=2$
> **Avanzado:** 1) $x=4, y=16/3$; 2) $x=12, y=4$; 3) $x=4, y=5$; 4) $x=1, y=1$

---

### Mini-prueba de autoevaluación

> [!question] Pregunta 1
> Si al verificar tu sistema, una ecuación da $10 = 10$ pero la otra da $5 = 0$, ¿qué debes concluir?
> *   a) La solución es correcta porque una ecuación funcionó.
> *   b) Hay un error; la solución debe cumplir ambas igualdades.
> *   c) El sistema no tiene solución.

> [!question] Pregunta 2
> ¿Cuál es el MCM para eliminar las fracciones de $\frac{x}{3} + \frac{y}{4} = 2$?
> *   a) $7$
> *   b) $12$
> *   c) $6$

> [!question] Pregunta 3
> Si un producto cuesta $\frac{x}{2}$ y el producto B cuesta $y$ USD, y la suma es una deuda de $10$ USD, ¿cuál es la ecuación simplificada?
> *   a) $x + 2y = -10$
> *   b) $x + 2y = -20$
> *   c) $x + y = -20$

---

> [!tip] Próximo paso
> ¡Felicidades! Ya sabes resolver sistemas complejos. En la **Clase 06**, aprenderemos qué sucede cuando las líneas son paralelas y el sistema no tiene solución (Sistemas Inconsistentes).

> [!info] 🧭 Navegación
> *   Anterior: [[Clase 04 — Método de Sustitución]]
> *   Índice: [[00 - Índice del curso]]
> *   **Clase 05 — Sistemas de Ecuaciones 2x2: Métodos de Igualación, Cramer y Fracciones**