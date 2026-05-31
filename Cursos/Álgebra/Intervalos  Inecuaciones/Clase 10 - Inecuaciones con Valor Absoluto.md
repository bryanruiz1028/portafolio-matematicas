# Clase 10 — Inecuaciones con Valor Absoluto

> [!info] 🧭 Navegación
> ⬅️ [Clase 09 — Introducción al Valor Absoluto](Clase09) | [🏠 Índice del Curso](Indice)

---

### 1. Importancia de las Inecuaciones con Valor Absoluto

Como especialistas en matemáticas, entendemos que en el mundo real rara vez buscamos un valor exacto; lo que buscamos es un **rango de tolerancia** o un margen de error aceptable. Las inecuaciones con valor absoluto son la herramienta matemática para definir esos límites.

*   **Economía y Finanzas (USD):** Se aplican para establecer márgenes de fluctuación en presupuestos. Si un presupuesto en dólares se define como $|x - 100| \leq 10$, estamos diciendo que el gasto real puede oscilar entre los 90 USD y los 110 USD sin salirse de lo previsto.
*   **Construcción e Ingeniería:** Esencial para la fabricación de piezas. Una viga de acero puede tener una medida nominal, pero la inecuación define el error máximo permitido (tolerancia) para que la estructura sea segura.
*   **Vida Cotidiana:** El termostato de un aire acondicionado utiliza este concepto. Si se programa a $24^\circ \text{C}$ con un margen de $|x - 24| < 1$, el sistema solo se activará cuando la temperatura se aleje más de un grado del objetivo.

---

### 2. Concepto Clave: La Distancia en la Recta Numérica

La forma más sencilla de comprender una inecuación con valor absoluto es mediante **el dibujo (la recta numérica)**. El valor absoluto representa la **distancia al cero**.

*   Si $|x| < a$, buscamos los números cuya distancia al cero sea pequeña, es decir, que estén **"atrapados" en medio** de $-a$ y $a$.
*   Si $|x| > a$, buscamos los números que se alejan del cero, es decir, que están en los **extremos** (más allá de $a$ y más allá de $-a$).

> [!warning] Alerta Pedagógica: ¡Cuidado con los Negativos!
> Antes de operar, observa el signo del número fuera del valor absoluto. Como el valor absoluto siempre es positivo o cero:
> 1.  **$|x| < \text{negativo}$ (ej. $|x| < -5$):** La solución es el **conjunto vacío ($\emptyset$)**. Es imposible que una distancia sea menor que un número negativo.
> 2.  **$|x| > \text{negativo}$ (ej. $|x| > -5$):** La solución son **todos los reales ($\mathbb{R}$)**. Cualquier distancia siempre será mayor que un número negativo.

> [!tip] Regla Mnemotécnica de Profe Alex
> *   **Menor que ($<$ o $\leq$):** La solución se queda **"en medio"** (un solo intervalo continuo).
> *   **Mayor que ($>$ o $\geq$):** La solución se va a los **"extremos"** (dos intervalos separados, unidos por el símbolo **$\cup$**).

---

### 3. Procedimiento Paso a Paso (Caso "Menor que")

Para resolver inecuaciones del tipo $|x| \leq a$, donde $a$ es positivo, sigue esta secuencia lógica:

```text
1. Identificar: Confirmar que el valor 'a' es positivo.
2. Plantear: Eliminar las barras de valor absoluto colocando la expresión central 
   entre el valor negativo y el positivo: -a ≤ x ≤ a.
3. Despejar: Aislar la variable realizando la misma operación (suma/resta) 
   en los tres sectores de la inecuación.
4. Dividir: Si la variable tiene un coeficiente, dividir todo por dicho número.
   ¡ATENCIÓN!: Si divides por un número NEGATIVO, debes invertir el sentido 
   de ambos signos de la inecuación.
5. Verificar: Elige un número del intervalo obtenido y sustitúyelo en la 
   inecuación original para confirmar que se cumple la desigualdad.
```

---

### 4. Ejemplos Prácticos

> [!example] Ejemplo 1: Caso Mayor que (Extremos)
> **Resolver:** $|x| \geq 7$
> *   **Análisis:** Al ser "mayor o igual", buscamos los extremos.
> *   **Desarrollo:** $x \leq -7$ **O** $x \geq 7$.
> *   **Notación de Intervalo:** $(-\infty, -7] \cup [7, \infty)$.

> [!example] Ejemplo 2: Caso Menor que (En medio)
> **Resolver:** $|x - 3| \leq 12$
> 1.  Planteamos: $-12 \leq x - 3 \leq 12$
> 2.  Sumamos 3 en los tres sectores: $-12 + 3 \leq x \leq 12 + 3$
> 3.  Resultado: $-9 \leq x \leq 15$.
> *   **Notación de Intervalo:** $[-9, 15]$.

> [!example] Ejemplo 3: Despeje Avanzado
> **Resolver:** $|2x - 3| < 7$
> 1.  Planteamos: $-7 < 2x - 3 < 7$
> 2.  Sumamos 3: $-4 < 2x < 10$
> 3.  Dividimos entre 2: $-2 < x < 5$
> *   **Verificación:** Si tomamos $x = 0$ (que está en el rango): $|2(0) - 3| = |-3| = 3$. Como $3 < 7$, es correcto.
> *   **Notación de Intervalo:** $(-2, 5)$.

> [!example] Ejemplo 4: Aplicación en USD
> **Problema:** Un producto de 10 USD tiene una variación permitida de $|x - 10| \leq 0.5$.
> 1.  Planteamos: $-0.5 \leq x - 10 \leq 0.5$
> 2.  Sumamos 10: $9.5 \leq x \leq 10.5$
> *   **Resultado:** El rango de precio aceptable es $[9.50, 10.50]$ USD.

---

### 5. Ejercicios para el Estudiante

**🟢 Nivel Fácil (Visualización)**
1.  $|x| < 8$
2.  $|x| > 8$
3.  $|x| \leq 10$
4.  $|x| \geq 10$

**🟡 Nivel Medio (Despeje)**
5.  $|x - 5| \leq 2$
6.  $|x + 4| < 10$
7.  $|3x - 6| < 12$
8.  $|2x + 8| \leq 20$

**🔴 Nivel Avanzado (Aplicación y Análisis)**
9.  **Presupuesto:** Un proyecto tiene un presupuesto base de 500 USD con una variación permitida de $|x - 500| \leq 50$. Expresa el rango en notación de intervalo.
10. **Inversión:** Una acción de 20 USD fluctúa según $|x - 20| \leq 2.5$. ¿Cuál es el precio mínimo y máximo?
11. **Análisis Crítico:** Determina la solución de $|x + 15| > -4$ justificando tu respuesta según las reglas de valor absoluto.
12. **Control de Alarma:** Un sensor de presión activa una alarma si $|p - 30| > 5$. ¿En qué intervalos de presión se activará la alarma?

---

### 6. Respuestas y Autoevaluación

> [!success] Solucionario
> 1.  **$(-8, 8)$**
> 2.  **$(-\infty, -8) \cup (8, \infty)$**
> 3.  **$[-10, 10]$**
> 4.  **$(-\infty, -10] \cup [10, \infty)$**
> 5.  **$[3, 7]$**
> 6.  **$(-14, 6)$**
> 7.  **$(-2, 6)$**
> 8.  **$[-14, 6]$**
> 9.  **$[450, 550]$** USD.
> 10. Mínimo: **17.5 USD**, Máximo: **22.5 USD**.
> 11. **$\mathbb{R}$ (Todos los números reales)**. Un valor absoluto siempre arroja un resultado positivo o cero, por lo tanto, siempre será mayor que -4.
> 12. **$(-\infty, 25) \cup (35, \infty)$**. La alarma suena en los extremos.

#### Mini-prueba de salida
1.  **¿Cuál es la solución de $|x| < -10$?**
    a) $x < 10$
    b) $x > -10$
    c) $\emptyset$ (Conjunto vacío)
    d) $\mathbb{R}$ (Todos los reales)

2.  **Si resolvemos $|x| \geq 7$, el resultado gráfico representa:**
    a) Un solo segmento entre -7 y 7.
    b) Dos flechas que apuntan hacia los extremos desde -7 y 7.
    c) Únicamente los puntos -7 y 7.
    d) No se puede graficar.

3.  **Un margen de error en un presupuesto de 100 USD se expresa como $|x - 100| \leq 15$. ¿Cuál es el gasto mínimo aceptable?**
    a) 115 USD
    b) 100 USD
    c) 85 USD
    d) 15 USD

---

### 7. Cierre del Bloque

¡Felicidades por completar esta sesión! Con el dominio de las inecuaciones con valor absoluto, cerramos oficialmente el **Bloque 3**. Ahora tienes la capacidad de traducir problemas de tolerancia y rangos del mundo real al lenguaje algebraico, utilizando tanto el despeje como la interpretación visual en la recta numérica.

> [!info] 🧭 Navegación Final
> ⬅️ [Clase 09 — Introducción al Valor Absoluto](Clase09) | [🏁 Fin del Bloque 3](Indice)