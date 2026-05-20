# 📖 Guía de estudio — Clase 04: Gráfica de la función cuadrática

> [!info] 📌 Conceptos clave
> La **función cuadrática** es una función de segundo grado donde el **máximo exponente de la variable $x$ es 2**. Su representación gráfica no es una línea recta, sino una curva simétrica llamada **parábola**.
> 
> *   **Vértice:** Es el punto más importante. Es el "punto de giro" donde la función cambia de dirección. Es obligatorio calcularlo para graficar correctamente.
> *   **Concavidad:** Determina si la parábola parece un "valle" (abre hacia arriba si $a$ es positivo) o una "montaña" (abre hacia abajo si $a$ es negativo).
> *   **Dominio:** Siempre son todos los números reales ($\mathbb{R}$), pues la gráfica se extiende infinitamente a los lados.
> *   **Rango:** A diferencia del dominio, el rango está limitado. Comienza (o termina) en la coordenada $y$ del vértice y se extiende hacia el infinito, dependiendo de hacia dónde abra la parábola.

---

### Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Función Cuadrática** | Forma general: $y = ax^2 + bx + c$ (con $a \neq 0$). |
| **Vértice (Coordenada $x$)** | Se halla con la fórmula: $x = \frac{-b}{2a}$ |
| **Vértice (Coordenada $y$)** | Se obtiene sustituyendo el valor de $x$ encontrado en la función original. |
| **Concavidad** | Si $a > 0$, es **cóncava hacia arriba** (valle). Si $a < 0$, es **cóncava hacia abajo** (montaña). |

---

### Ejemplos resueltos adicionales

> [!example] Ejemplo A: Caso Básico
> **Función:** $y = 2x^2 - 4x - 1$
> 
> **1. Identificar coeficientes:** $a = 2$, $b = -4$, $c = -1$.
> **2. Calcular el vértice ($x$):** $x = \frac{-(-4)}{2(2)} = \frac{4}{4} = 1$.
> **3. Tabla de valores:** Ponemos el $x=1$ en el centro y elegimos dos valores a la izquierda y dos a la derecha.
> 
| $x$ | Procedimiento ($y = 2x^2 - 4x - 1$) | $y$ |
| :--- | :--- | :--- |
| -1 | $2(-1)^2 - 4(-1) - 1 = 2 + 4 - 1$ | **5** |
| 0 | $2(0)^2 - 4(0) - 1 = 0 - 0 - 1$ | **-1** |
| **1** | $2(1)^2 - 4(1) - 1 = 2 - 4 - 1$ | **-3 (Vértice)** |
| 2 | $2(2)^2 - 4(2) - 1 = 8 - 8 - 1$ | **-1** |
| 3 | $2(3)^2 - 4(3) - 1 = 18 - 12 - 1$ | **5** |
> 
> **Resultado:** El vértice es $(1, -3)$. Como $a=2$ es positivo, la parábola abre hacia arriba.

> [!example] Ejemplo B: Aplicación Real ($USD)
> **Contexto:** El balance financiero $y$ (en $USD) de una microempresa según las unidades producidas $x$ se modela con: $y = x^2 - 6x + 5$. Aquí, un valor negativo de $y$ representa una pérdida o saldo en contra.
> 
> **1. Vértice ($x$):** $x = \frac{-(-6)}{2(1)} = 3$ unidades.
> **2. Tabla de valores centrada en $x=3$:**
> 
| $x$ (unidades) | Procedimiento ($y = x^2 - 6x + 5$) | $y$ (Saldo $USD) |
| :--- | :--- | :--- |
| 1 | $(1)^2 - 6(1) + 5 = 1 - 6 + 5$ | **0** |
| 2 | $(2)^2 - 6(2) + 5 = 4 - 12 + 5$ | **-3** |
| **3** | $(3)^2 - 6(3) + 5 = 9 - 18 + 5$ | **-4 (Saldo mínimo)** |
| 4 | $(4)^2 - 6(4) + 5 = 16 - 24 + 5$ | **-3** |
| 5 | $(5)^2 - 6(5) + 5 = 25 - 30 + 5$ | **0** |
> 
> **Resultado:** Al producir 3 unidades, la empresa alcanza su punto más bajo (un saldo de $-4$ USD). A partir de la 4ta unidad, el saldo comienza a subir nuevamente debido a que la parábola abre hacia arriba ($a=1$).

---

### Ejercicios de repaso

> [!abstract] 🟢 Nivel: Fácil
> **1. Identificación:** ¿Cuáles de estas son funciones cuadráticas? Justifica usando las reglas (exponente máximo 2, no $x$ en el denominador).
> *   a) $y = 3x^2 - 5x + 2$
> *   b) $y = \frac{2}{x^2} + 4$
> *   c) $y = x^3 - x^2 + 1$
> 
> **2. Coeficientes:** En la función $y = x^2 - 8x + 12$, identifica los valores de $a, b$ y $c$.
> 
> *Pista: En (b) la $x$ está en el denominador, y en (c) el exponente máximo es 3; por tanto, no cumplen la regla.*

> [!abstract] 🟡 Nivel: Medio
> Dada la función $y = x^2 - 4$:
> 1. Encuentra la coordenada $x$ del vértice.
> 2. Construye una tabla de 5 valores centrada en el vértice.
> 3. ¿Hacia dónde abre la parábola?

> [!abstract] 🔴 Nivel: Avanzado (Aplicación $USD)
> El gasto operativo mensual de una tienda se define por $y = 2x^2 - 8x + 6$, donde $y$ es el gasto en $USD y $x$ el tiempo en meses.
> 1. Calcula el vértice (mes y gasto mínimo).
> 2. Si el valor de $y$ es negativo, considéralo un ahorro o crédito a favor.
> 3. Indica la concavidad y justifica: ¿El gasto aumentará o disminuirá después de pasar el mes del vértice?

---

> [!tip] 💡 Consejo de estudio
> Para graficar rápido y sin errores, **nunca elijas números al azar**. La estrategia del "profe Alex" es calcular siempre el **vértice primero** y ponerlo en el centro de tu tabla. Gracias a la **simetría** de la parábola, notarás que los valores de $y$ se repiten para los puntos que están a la misma distancia del vértice (por ejemplo, en el Ejemplo A, para $x=0$ y $x=2$, el resultado es el mismo: $-1$). ¡Esto te ahorrará mucho tiempo de cálculo!