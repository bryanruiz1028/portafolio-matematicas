# Clase 02 — Progresiones Aritméticas: Término General y Suma de Términos

#algebra #arithmeticprogr

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 4

> [!info] 🧭 Navegación
> ◄ [[Clase 01]] | ▲ [[00 - Índice del curso]] | ► [[Clase 03]]

---

### ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> Con estas progresiones, vas a poder adivinar el futuro de una lista de números sin tener que contarlos uno por uno. También te sirven para calcular totales acumulados de forma súper rápida.
> 
> * **💵 [aplicación con $USD]:** Ayuda a crear planes de ahorro donde el depósito sube una cantidad fija cada semana, permitiéndote saber cuánto dinero tendrás al final del año.
> * **🏗️ [aplicación práctica]:** Sirve para calcular materiales en filas, como los ladrillos de una pared o los asientos de un cine, sin perder tiempo.
> * **📊 [situación cotidiana]:** Es ideal para organizar los tiempos de un entrenamiento deportivo o para entender cómo avanzan los días en un calendario.

---

### Concepto clave

> [!note] 📌 ¿Qué es una Progresión Aritmética?
> Es una lista de números donde cada término se obtiene **sumando siempre la misma cantidad** al número anterior. A esa cantidad fija la llamamos **diferencia** ($d$).

> [!warning] ⚠️ Error común
> **Incorrecto:** Pensar que la diferencia solo puede ser positiva o que los números se multiplican.
> **Correcto:** La diferencia puede ser **negativa** (la serie va hacia abajo) y siempre se trata de **sumar o restar**, nunca de multiplicar.

> [!tip] 💡 Truco para recordarlo
> La **D**iferencia es el **D**edo que siempre suma lo mismo.

---

### Procedimiento paso a paso

Para encontrar el término general ($a_n$) usamos el método de ajuste del Profe Alex:

```text
PASO 1 → Hallar la diferencia (d) entre los términos.
PASO 2 → Escribir la diferencia junto a la letra n (ejemplo: 4n).
PASO 3 → Reemplazar n por 1 y comparar el resultado con el primer término real.
PASO 4 → Ajustar sumando o restando la cantidad necesaria para llegar al valor real.
```

Para calcular la suma de los primeros términos ($S_n$):

```text
PASO 1 → Identificar el primer término (a1) y cuántos términos sumaremos (n).
PASO 2 → Calcular el valor del último término (an) usando la fórmula del paso anterior.
PASO 3 → Sumar el primero y el último: (a1 + an).
PASO 4 → Multiplicar por n, dividir entre 2 y ¡listo!
```

---

### Ejemplos Prácticos

> [!example] Ejemplo 1: Caso Básico
> Secuencia: 5, 7, 9, 11...
> 1. Diferencia: 2.
> 2. Escribimos: **2n**.
> 3. Probamos con n=1: **2(1) = 2**.
> 4. Ajuste: Para llegar de 2 a 5, sumamos 3.
> **Resultado:** El término general es **2n + 3**.

> [!example] Ejemplo 2: Caso con Signos (Bajando)
> Secuencia donde la diferencia es -5 y el primer término es 10.
> 1. Escribimos: **-5n**.
> 2. Probamos con n=1: **-5(1) = -5**.
> 3. Ajuste: Para pasar de -5 a 10 positivo, sumamos 15.
> **Resultado:** El término general es **-5n + 15**.

> [!example] Ejemplo 3: Suma de Términos
> Sumar los primeros 10 términos de: 9, 14, 19... (d=5).
> 1. Término general: **5n + 4**.
> 2. Término 10 ($a_{10}$): **5(10) + 4 = 54**.
> 3. Suma: $S_{10} = \frac{(9 + 54) \cdot 10}{2} = \frac{63 \cdot 10}{2} = 315$.
> **Resultado:** La suma es **315**.

> [!example] Ejemplo 4: Aplicación ahorro $USD
> Ahorras $10 USD la semana 1 y subes $2 USD cada semana.
> 1. Término general: **2n + 8**.
> 2. Semana 20: **2(20) + 8 = 48 USD**.
> 3. Total en 20 semanas: $S_{20} = \frac{(10 + 48) \cdot 20}{2} = 58 \cdot 10 = 580$.
> **Resultado:** Ahorras **48 USD** esa semana y llevas **580 USD** en total.

---

### Ejercicios para el estudiante

> [!abstract] Nivel Verde (Fácil)
> Encuentra el término general:
> 1. 4, 7, 10, 13...
> 2. 10, 20, 30, 40...
> 3. 2, 6, 10, 14...
> 4. 1, 6, 11, 16...

> [!abstract] Nivel Amarillo (Medio)
> 1. Si **a5 = 23** y **d = 4**, halla el término general.
> 2. Secuencia: 15, 12, 9, 6... Halla **an**.
> 3. Secuencia: -8, -6, -4, -2... Halla **an**.
> 4. Halla el término **a100** de la secuencia: 5, 8, 11...

> [!abstract] Nivel Rojo (Avanzado)
> 1. Una deuda de $500 USD sube $5 USD cada mes. ¿Cuánto debes en el mes 12?
> 2. Suma los primeros 50 números pares (2, 4, 6...).
> 3. Ahorro de $20 USD iniciales subiendo $10 USD por mes. ¿Total en 24 meses?
> 4. Si la suma de 10 términos es 155 y **a1 = 2**, ¿cuánto vale **a10**?

> [!success] ✅ Respuestas (para el docente)
> **Verde:** 1) **3n + 1** | 2) **10n** | 3) **4n - 2** | 4) **5n - 4**.
> **Amarillo:** 1) **4n + 3** | 2) **-3n + 18** | 3) **2n - 10** | 4) **302**.
> **Rojo:** 1) **555 USD** | 2) **2550** | 3) **3240 USD** | 4) **29**.

---

### Mini-prueba de autoevaluación

> [!question] Pregunta 1
> ¿Qué define a una progresión aritmética?
> **Respuesta:** Que existe una diferencia constante que siempre se suma o resta.
> **Explicación:** Si los números saltan de forma desordenada o multiplicando, no es aritmética.

> [!question] Pregunta 2
> ¿Cuál es el término general de: 12, 10, 8, 6...?
> **Respuesta:** **-2n + 14**.
> **Explicación:** La diferencia es -2. Al probar n=1, nos da -2. Para llegar a 12, sumamos 14.

> [!question] Pregunta 3
> Si una deuda de $100 USD aumenta $10 USD por semana, ¿cuánto debes en la semana 5?
> **Respuesta:** **140 USD**.
> **Explicación:** La fórmula es **10n + 90**. Para n=5: **10(5) + 90 = 140**.

---

### Notas para el próximo tema

> [!tip] 💡 En la próxima clase
> Veremos las Progresiones Geométricas. Prepárate, porque aquí ya no sumaremos, sino que multiplicaremos por una razón constante.

> [!info] 🧭 Navegación
> ◄ [[Clase 01]] | ▲ [[00 - Índice del curso]] | ► [[Clase 03]]