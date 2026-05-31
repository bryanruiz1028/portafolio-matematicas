# Guía de estudio — Clase 03: Introducción a las Progresiones Geométricas

¡Hola! Qué alegría saludarte. Hoy vamos a explorar el fascinante mundo de las progresiones geométricas. No te preocupes si al principio parece un reto; verás que, con paciencia y práctica, dominarás estas secuencias en poco tiempo. ¡Vamos a aprender juntos!

> [!info] 📌 Conceptos clave
> * **Definición:** Una progresión geométrica es una sucesión de números donde cada término (a partir del segundo) se obtiene multiplicando el anterior por una cantidad fija y constante llamada **razón** ($r$).
> * **Elementos básicos:** Para identificarla, necesitamos conocer el primer término ($a_1$) y la razón ($r$).
> * **Identificación de la razón:** Se obtiene dividiendo cualquier término entre su anterior ($r = \frac{a_n}{a_{n-1}}$). Un detalle vital: si la razón es negativa ($r < 0$), los signos de la progresión se irán alternando entre positivo y negativo.
> * **Clasificación:** 
>     * **Creciente:** Los valores aumentan. Esto ocurre si $a_1 > 0$ y $r > 1$, o también en el caso curioso donde el primer término es negativo ($a_1 < 0$) y la razón está entre $0$ y $1$ ($0 < r < 1$).
>     * **Decreciente:** Los valores disminuyen.
>     * **Alternada:** Los signos cambian en cada paso porque $r < 0$.

---

## 2. TABLA DE FÓRMULAS Y DEFINICIONES

| Elemento / Símbolo | Definición / Fórmula |
| :--- | :--- |
| **Razón ($r$)** | Cantidad constante por la que se multiplica. Para términos consecutivos: $r = \frac{a_n}{a_{n-1}}$. Para términos **no consecutivos**: $r = \sqrt[n-1]{\frac{a_n}{a_1}}$. |
| **Término general ($a_n$)** | También llamado término enésimo, permite hallar cualquier número en la secuencia: $a_n = a_1 \cdot r^{n-1}$. |
| **Primer término ($a_1$)** | Es el valor inicial de la sucesión y el punto de partida para aplicar cualquier fórmula. |
| **Posición ($n$)** | Representa el lugar que ocupa el número en la secuencia (por ejemplo, si buscamos el décimo número, $n = 10$). |

---

## 3. EJEMPLOS RESUELTOS ADICIONALES

> [!example] Ejemplo A — Hallar la razón y el término siguiente
> Dada la progresión: $3, 6, 12, 24...$
> 
> * **Paso 1: Hallar la razón ($r$).**
>   Dividimos el segundo término entre el primero: $6 / 3 = 2$.
>   Verificamos con el siguiente: $12 / 6 = 2$. Por lo tanto, la razón constante es $r = 2$.
> * **Paso 2: Hallar el quinto término ($a_5$).**
>   Simplemente multiplicamos el último término conocido por la razón: $24 \cdot 2 = 48$.
> 
> **Resultado:** La razón es $2$ y el quinto término es $48$. ✅

> [!example] Ejemplo B — Crecimiento de ahorros en USD
> Un estudiante ahorra $4$ USD el primer día y cada día duplica la cantidad anterior ($r = 2$). ¿Cuánto dinero ahorrará el cuarto día?
> 
> * **Datos:** $a_1 = 4$, $r = 2$, $n = 4$.
> * **Cálculo:**
>   Usamos la fórmula: $a_4 = 4 \cdot 2^{4-1}$
>   $a_4 = 4 \cdot 2^{3}$ *(Recuerda: primero resolvemos la potencia $2^3$, luego multiplicamos)*.
>   $a_4 = 4 \cdot 8 = 32$
> 
> **Resultado:** El cuarto día ahorrará $32$ USD. ✅

---

## 4. EJERCICIOS DE REPASO

> [!abstract] 🟢 Nivel: Fácil
> 1. Identifica la razón ($r$) en la siguiente progresión: $5, 10, 20, 40...$
> 2. Halla los siguientes dos términos de la progresión: $1, 5, 25...$
> 3. Determina si la progresión $80, 40, 20...$ es creciente o decreciente.

> [!abstract] 🟡 Nivel: Medio
> 1. Calcula el término $a_5$ de una progresión donde $a_1 = 4$ y $r = 3$.
> 2. Encuentra la razón de una progresión donde $a_1 = 4$ y $a_4 = 108$. *(Pista: utiliza la raíz cúbica porque $n-1 = 3$)*.
> 3. Simplifica la expresión del término general ($a_n$) para una progresión donde $a_1 = 1$ y $r = 5$.

> [!abstract] 🔴 Nivel: Avanzado — Aplicación con USD
> 1. Un videojuego cuesta $108$ USD. Si empiezas con $4$ USD y cada nivel que pasas triplicas tu dinero ($r = 3$), ¿en qué nivel tendrás exactamente el costo del juego? *(Pista: $a_n = 108$, $a_1 = 4$. Debes encontrar el valor de $n$)*.
> 2. Si una inversión de $200$ USD se reduce a la mitad cada mes ($r = 1/2$), ¿cuánto dinero queda al cuarto mes? *(Utiliza la fórmula: $a_4 = 200 \cdot (1/2)^{4-1}$)*.
> 3. Determina si una progresión con $a_1 = 2$ y $r = -5$ es alternada y escribe sus primeros 4 términos.

---

## 5. CONSEJO DE ESTUDIO

> [!tip] 💡 Consejo de estudio
> **¡Cuidado con la jerarquía de operaciones!** Al usar la fórmula $a_n = a_1 \cdot r^{n-1}$, es fundamental que primero resuelvas la potencia y al final multipliques por el primer término. Nunca multipliques $a_1 \cdot r$ antes de elevarlo al exponente; eso cambiaría totalmente el resultado.
> 
> Además, presta mucha atención a los signos: si la base (la razón) es negativa, recuerda que $(-5)^2$ es $25$, mientras que $-5^2$ es $-25$. ¡Usa siempre paréntesis para proteger tus números negativos! Verifica siempre la razón dividiendo el segundo término para el primero y luego el tercero para el segundo para asegurar que la constante se mantiene.

¡Mucho éxito en tu práctica! Recuerda que cada ejercicio que resuelves te hace más hábil en matemáticas. ¡Tú puedes!