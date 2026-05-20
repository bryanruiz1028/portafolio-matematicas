# Clase 07 — Funciones Exponenciales, Logarítmicas y a Trozos
tags: #algebra #exponentialfunc #logarithms #piecewise
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 7 de 12

---

**1. NAVEGACIÓN SUPERIOR**
« [[Clase 06 — Funciones Lineales y Cuadráticas]] | **Clase 07** | [[Clase 08 — Ecuaciones Exponenciales y Logarítmicas]] »

---

**2. RELEVANCIA Y APLICACIONES**

> [!info] 🌍 Relevancia y aplicaciones
> Las funciones exponenciales modelan cambios donde la rapidez de crecimiento depende del valor actual, permitiendo predecir la expansión de virus, el crecimiento poblacional o el interés compuesto en finanzas.
> 
> - **Aplicación $USD:** Esencial para calcular el rendimiento de ahorros en dólares; si el interés se capitaliza, el dinero crece de forma exponencial.
> - **Aplicación Práctica:** Utilizada en ingeniería para el diseño de cables suspendidos (catenarias) y en ciencias para medir el decaimiento radiactivo de materiales.
> - **Situación Cotidiana:** Explica la "viralidad" de una noticia en redes sociales, donde el número de personas que comparten la información crece exponencialmente en segundos.

---

**3. CONCEPTO CLAVE**

### Función Exponencial
Se define como $f(x) = a^x$. Para un estudiante de 12 años, la diferencia visual clave es que **la variable $x$ ya no está en el suelo (la base), sino en el aire (el exponente)**. 

Para que sea una función exponencial válida, la base $a$ debe cumplir:
1. Ser positiva ($a > 0$).
2. Ser distinta de uno ($a \neq 1$).

> [!warning] ⚠️ Error común (Profe Alex)
> No confundas el signo de la función con el de la base:
> - **$-3^x$**: La base es $3$ (positiva) y el signo menos es una transformación externa. **Es función exponencial**.
> - **$(-3)^x$**: La base es $-3$ (negativa). Al intentar graficarla, los valores saltan y no forman una curva continua. **No es función exponencial**.

### El Puente Logarítmico
La función logarítmica es la inversa de la exponencial. Conceptualmente, un logaritmo responde a la pregunta: **"¿Cuál es el exponente que falta?"**. Si $2^x = 8$, el logaritmo nos dice que $x=3$.

> [!tip] 💡 Truco para recordarlo
> - Si la base es "grande" ($a > 1$), la función **sube** (creciente).
> - Si la base es "pequeña" ($0 < a < 1$, como $0.5$ o $1/2$), la función **baja** (decreciente).

---

**4. PROCEDIMIENTO PASO A PASO**

Para analizar y graficar estas funciones, sigue este protocolo técnico:

1. **Análisis de la Base:**
   - Determina si $a > 1$ (crece) o $0 < a < 1$ (decrece).
2. **Dominio y Rango:**
   - **Exponencial:** El dominio es siempre $\mathbb{R}$ porque la gráfica se extiende infinitamente a izquierda y derecha. El rango depende de la asíntota $k$.
   - **Logarítmica:** El rango es siempre $\mathbb{R}$. El dominio se halla haciendo el argumento $> 0$.
3. **Identificación de Asíntotas:**
   - **Exponencial:** Asíntota Horizontal en la recta $y = k$ (desplazamiento vertical).
   - **Logarítmica:** Asíntota Vertical en la recta $x = h$ (donde el argumento se anula).
4. **Cálculo con Calculadora (Cambio de Base):**
   - Para evaluar logaritmos de cualquier base en calculadora, usa la fórmula: $\frac{\log(\text{argumento})}{\log(\text{base})}$.
5. **Evaluación de Puntos Críticos:**
   - Si es una **función a trozos**, verifica el intervalo observando si incluye el signo "igual" ($\leq, \geq$) para saber en qué "pieza" evaluar.

---

**5. EJEMPLOS RESUELTOS**

> [!example] Ejemplo 1: Graficación Básica
> **Función:** $f(x) = 2^x$
> - **Base:** $2$ ($> 1$), por lo tanto es creciente.
> - **Corte en Y:** $2^0 = 1$. Punto $(0, 1)$.
> - **Asíntota:** Horizontal en $y = 0$ (Eje X).
> - **Dominio:** $\mathbb{R}$ | **Rango:** $(0, \infty)$.

> [!example] Ejemplo 2: Transformaciones
> **Función:** $g(x) = -2^{x+1} + 3$
> - **Reflejo:** El signo $(-)$ exterior refleja la función hacia abajo.
> - **Traslación:** El $+1$ la mueve 1 unidad a la izquierda; el $+3$ la sube 3 unidades.
> - **Asíntota:** Horizontal en $y = 3$.
> - **Rango:** Como apunta hacia abajo desde la asíntota, el Rango es $(-\infty, 3)$.

> [!example] Ejemplo 3: Dominio Logarítmico
> **Función:** $y = \log_3(2x - 4)$
> - **Cálculo del Dominio:** $2x - 4 > 0 \implies 2x > 4 \implies x > 2$.
> - **Dominio:** $(2, \infty)$. **Asíntota Vertical:** Recta $x = 2$.
> - **Evaluación en $x=3$:** $\log_3(2(3)-4) = \log_3(2)$. En calculadora: $\frac{\log(2)}{\log(3)} \approx 0.63$.

> [!example] Ejemplo 4: Aplicación Financiera $USD
> **Problema:** Un capital de $100 USD se duplica cada año.
> - **Función:** $f(x) = 100(2^x)$.
> - **Cálculo a los 3 años:** $f(3) = 100(2^3) = 100(8) = 800$.
> - **Resultado:** Tras 3 años, el ahorro asciende a $800 USD.

---

**6. EJERCICIOS PARA EL ESTUDIANTE**

> [!abstract] 🟢 Nivel Fácil
> 1. Identifica si $f(x) = (-5)^x$ es una función exponencial. Justifica usando la teoría de la base.
> 2. Halla el punto de corte con el eje $y$ de $f(x) = 10^x$.
> 3. Determina si $g(x) = (1/4)^x$ es creciente o decreciente.
> 4. ¿Cuál es el dominio de la función $f(x) = 7^x$?

> [!abstract] 🟡 Nivel Medio (Funciones a Trozos)
> Dada la función: $f(x) = \begin{cases} x - 7 & \text{si } x \leq -3 \\ x^2 + 1 & \text{si } -3 < x < 5 \\ 2x & \text{si } x \geq 5 \end{cases}$
> *Tip: Mira con cuidado dónde está el signo "igual" para elegir la fórmula correcta.*
> 1. Calcula $f(-4)$.
> 2. Calcula $f(-3)$.
> 3. Calcula $f(0)$.
> 4. Calcula $f(5)$.

> [!abstract] 🔴 Nivel Avanzado ($USD)
> Determina el Dominio y el Rango de las siguientes funciones:
> 1. $f(x) = -3^{x+2} + 5$
> 2. $g(x) = 4^{x-1} - 2$
> 3. $h(x) = -(0.5)^x - 1$
> 4. Un fondo de inversión de $500 USD pierde la mitad de su valor cada año: $V(t) = 500(0.5)^t$. Halla su valor en el año 2.

> [!success] Solucionario para el docente
> - **Fácil:** 1. No, base negativa no es función exponencial. 2. (0, 1). 3. Decreciente ($1/4 < 1$). 4. Todos los Reales ($\mathbb{R}$).
> - **Medio:** 1. -11. 2. -10 (se usa $x-7$ por el $\leq$). 3. 1. 4. 10 (se usa $2x$ por el $\geq$).
> - **Avanzado:** 1. Dom $\mathbb{R}$, Ran $(-\infty, 5)$. 2. Dom $\mathbb{R}$, Ran $(-2, \infty)$. 3. Dom $\mathbb{R}$, Ran $(-\infty, -1)$. 4. $125 USD.

---

**7. MINI-PRUEBA DE AUTOEVALUACIÓN**

> [!question] Pregunta 1
> Según la definición del Profe Alex, ¿por qué la base $a$ no puede ser 1?
> a) Porque sería un número negativo.
> b) Porque daría una línea recta (función constante) en lugar de una curva.
> c) Porque no se puede elevar al cuadrado.

> [!question] Pregunta 2
> ¿Cuál es el rango de la función $f(x) = \log_5(x+10)$?
> a) $(-10, \infty)$
> b) $(0, \infty)$
> c) Todos los Reales ($\mathbb{R}$)

> [!question] Pregunta 3
> Si una cuenta en $USD crece según $f(x) = 50(2^x)$, ¿cuál es el saldo tras 4 periodos?
> a) $400 USD
> b) $800 USD
> c) $1600 USD

---

**8. CIERRE Y NOTAS PRÓXIMO TEMA**

> [!tip] 💡 Conexión con Clase 08
> Dominar la identificación de la base y el uso del logaritmo como "exponente faltante" será vital en la [[Clase 08 — Ecuaciones Exponenciales y Logarítmicas]], donde aprenderemos a despejar la $x$ del "aire" usando propiedades algebraicas.

---
**NAVEGACIÓN INFERIOR**
« [[Clase 06 — Funciones Lineales y Cuadráticas]] | **Clase 07** | [[Clase 08 — Ecuaciones Exponenciales y Logarítmicas]] »