# 📖 Guía de estudio — Clase 04: Ecuaciones exponenciales mediante cambio de variable

> [!info] 📌 Conceptos clave
> - **Propiedades de potencias:** Se utilizan para desglosar los términos de la ecuación. El objetivo fundamental es separar la base que contiene la variable $x$ de los coeficientes numéricos para facilitar su manipulación.
> - **Sustitución (Cambio de variable):** Técnica que consiste en reemplazar una expresión exponencial recurrente (como $2^x$ o $3^x$) por una variable auxiliar ($u$, $t$ o $m$). Esto transforma una estructura compleja en una ecuación lineal o cuadrática mucho más sencilla de resolver.
> - **Estructuras cuadráticas:** Se identifican cuando un término presenta la forma $a^{2x}$, la cual debe reescribirse como $(a^x)^2$ para evidenciar el trinomio de segundo grado.
> - **Reversión del cambio:** Tras hallar el valor de la variable auxiliar, es imperativo retomar la igualdad original. La meta final del proceso es determinar el valor de $x$, no el de la variable temporal.

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| Separación de suma en exponente | $a^{x+n} = a^x \cdot a^n$ |
| Separación de resta en exponente | $a^{x-n} = \frac{a^x}{a^n}$ |
| Potencia de una potencia (forma cuadrática) | $a^{2x} = (a^x)^2$ |
| Exponente cero (el "comodín") | $a^0 = 1$ (Esencial para igualar bases cuando un término es la unidad). |

## Ejemplos Resueltos

> [!example] Ejemplo A: Resolución de ecuación lineal mediante sustitución
> **Problema:** Resolver $2^{x+1} + 2^x + 2^{x-1} = 28$
> 
> **Procedimiento:**
> 1. **Separación de términos:** Aplicamos las propiedades de potencias para aislar $2^x$:
>    $2^x \cdot 2^1 + 2^x + \frac{2^x}{2} = 28$
> 2. **Sustitución:** Definimos la variable auxiliar $t = 2^x$. La ecuación se transforma en:
>    $2t + t + \frac{t}{2} = 28$
> 3. **Resolución de la ecuación resultante:** Para eliminar el denominador y facilitar el despeje, multiplicamos todos los términos de la ecuación por $2$:
>    $4t + 2t + t = 56$
>    $7t = 56$
>    $t = \frac{56}{7} \implies t = 8$
> 4. **Reversión del cambio e igualación de bases:** Retomamos la definición original de $t$:
>    $2^x = 8$
>    Expresamos $8$ como potencia de base $2$: $2^x = 2^3$
>    Al igualar las bases, concluimos que los exponentes deben ser iguales: $x = 3$.

> [!example] Ejemplo B: Aplicación en crecimiento de capital (USD)
> **Problema:** El flujo de caja de una inversión en dólares sigue la estructura $3^{2x} - 28(3^x) + 27 = 0$, donde $x$ representa el tiempo transcurrido en años. Determine los periodos exactos en los que se alcanzan los puntos de equilibrio (resultado igual a $0$).
> 
> **Procedimiento:**
> 1. **Reescritura de la potencia:** Identificamos la estructura cuadrática:
>    $(3^x)^2 - 28(3^x) + 27 = 0$
> 2. **Sustitución:** Sea $u = 3^x$. Obtenemos el trinomio:
>    $u^2 - 28u + 27 = 0$
> 3. **Factorización del trinomio:** Buscamos dos números que multiplicados den $27$ y sumados den $-28$:
>    $(u - 27)(u - 1) = 0$
>    Esto nos da dos posibles valores para $u$: $u_1 = 27$ y $u_2 = 1$.
> 4. **Reversión para hallar el tiempo ($x$):**
>    - **Caso 1:** $3^x = 27 \implies 3^x = 3^3 \implies x = 3$ años.
>    - **Caso 2:** $3^x = 1 \implies 3^x = 3^0 \implies x = 0$ años (momento de la inversión inicial).
> 
> **Resultado:** Los puntos de equilibrio en la inversión de USD ocurren al inicio ($x = 0$) y al tercer año ($x = 3$).

## Ejercicios de Repaso

> [!abstract] 🟢 Nivel Fácil: Ecuaciones lineales
> 1. $3^{x+1} + 3^x = 36$
> 2. $2^{x+2} + 2^x = 20$
> 3. $5^x + 5^{x-1} = 30$

> [!abstract] 🟡 Nivel Medio: Ecuaciones cuadráticas
> 1. $2^{2x} - 6(2^x) + 8 = 0$
> 2. $3^{2x} - 12(3^x) + 27 = 0$
> 3. $5^{2x} - 130(5^x) + 625 = 0$

> [!abstract] 🔴 Nivel Avanzado: Problemas aplicados (USD)
> **Pista pedagógica:** En problemas financieros, identifica primero la expresión exponencial recurrente (ej. $u = 2^x$) para visualizar la estructura del modelo antes de operar.
> 1. El rendimiento de una cuenta de ahorros genera alertas de auditoría según la ecuación $2^{2x} - 10(2^x) + 16 = 0$. Determine los periodos de tiempo $x$ (expresados en meses) en los que ocurren dichas alertas.
> 2. Una proyección de mercado internacional en USD define el retorno de inversión mediante la igualdad $5^{2x} - 30(5^x) + 125 = 0$. Calcule los valores de $x$ que representan el factor de tiempo necesario para alcanzar estas metas financieras.

> [!tip] 💡 Consejo de estudio
> Aplica la estrategia pedagógica de **"dividir el tablero"**: realiza el cambio de variable y la resolución de la ecuación auxiliar ($u$ o $t$) en una columna separada. Esta es una **estrategia metacognitiva** fundamental para evitar el error más común: detenerse al hallar el valor de la variable auxiliar. 
> 
> **Paso final obligatorio:** No olvides realizar siempre la **comprobación**. Sustituye el valor final de $x$ en la ecuación original para verificar que la igualdad se mantenga. Si la igualdad se cumple, tu proceso ha sido exitoso.