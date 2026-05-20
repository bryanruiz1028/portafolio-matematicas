# Clase 08 — Inecuaciones con Valor Absoluto

#algebra #absolutevaluein
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 8 de 9

> [!info] 🧭 Navegación
> [[Clase 07|⬅ Clase 07]] | [[00 - Índice del curso|Índice]] | **Clase 08** | [[Clase 09|Clase 09 ➡]]

---

### 🌍 Relevancia y aplicaciones

> [!info] 🌍 Relevancia y aplicaciones
> Las inecuaciones con valor absoluto son la herramienta matemática para definir **rangos de tolerancia**. En el mundo real, nada es exacto; estas expresiones nos permiten calcular qué tan lejos podemos alejarnos de un valor ideal sin causar un error.

*   **💵 Aplicación USD:** Determinación de variaciones aceptables en el tipo de cambio o fluctuaciones permitidas en un presupuesto financiero.
*   **🏗️ Aplicación práctica:** Margen de error en la fabricación de componentes (ej. una viga que debe medir $10m$ con una tolerancia de $\pm 2cm$).
*   **📊 Situación cotidiana:** Configuración de alertas de temperatura o el margen de tolerancia en los radares de velocidad.

---

### 📌 ¿Qué es Inecuaciones con Valor Absoluto?

> [!note] 📌 ¿Qué es Inecuaciones con Valor Absoluto?
> Imagina que estás en el número $0$ de una recta numérica. El valor absoluto es tu **distancia** hasta ese origen. Como es una distancia, **jamás puede ser negativa**. 
> 
> Resolver una inecuación con valor absoluto significa encontrar todos los números cuya distancia al centro cumpla una condición:
> - Si buscamos $|x| < 5$, queremos números cuya distancia al cero sea **menor** a 5 (están "atrapados" cerca del centro).
> - Si buscamos $|x| > 5$, queremos números cuya distancia sea **mayor** a 5 (se alejan hacia los extremos).

> [!warning] ⚠️ Error común
> **❌ Incorrecto:** Ignorar la parte negativa y resolver solo $x + 3 > 5$.
> **✅ Correcto:** Dividir el problema en dos casos. Además, recuerda la regla de oro del Profe Alex: si el valor absoluto se compara con un número negativo:
> 1. $|x| < -2$ $\rightarrow$ **Conjunto vacío ($\emptyset$)** (Una distancia nunca es menor que un negativo).
> 2. $|x| > -2$ $\rightarrow$ **Todos los Reales ($\mathbb{R}$)** (Cualquier distancia siempre será mayor que un negativo).

> [!tip] 💡 Truco para recordarlo
> *   **Menor que ($<$ o $\leq$):** Es un **Sándwich** (Intersección). Los valores están encerrados entre el negativo y el positivo: $-a \leq x \leq a$.
> *   **Mayor que ($>$ o $\geq$):** Es una **Explosión** (Unión $\cup$). Los valores "escapan" hacia afuera: $x < -a$ **o** $x > a$.

---

### 📋 Procedimiento paso a paso

```text
PASO 1: Identificar el signo. ¿Es "Menor que" (Sándwich) o "Mayor que" (Explosión)?
PASO 2: Aplicar la propiedad lógica:
        - Si es ">", separar en dos casos usando el conector "O" (∪).
        - Si es "<", colocar la expresión entre el valor negativo y el positivo.
PASO 3: Despejar la incógnita "x" realizando las mismas operaciones en todos los lados.
PASO 4: Expresar el resultado en notación de intervalo o conjunto.
```

---

### 📖 Ejemplos Prácticos

#### Ejemplo 1: Caso Básico (Explosión)
**Ejercicio:** $|x + 5| \geq 3$
1.  **Propiedad:** Como es $\geq$, usamos la Unión ($\cup$):
    $x + 5 \leq -3 \quad \cup \quad x + 5 \geq 3$
2.  **Despeje:**
    *   $x \leq -3 - 5 \Rightarrow x \leq -8$
    *   $x \geq 3 - 5 \Rightarrow x \geq -2$
3.  **Resultado:** $(-\infty, -8] \cup [-2, \infty)$.

#### Ejemplo 2: Caso con Signos (Práctica)
**Ejercicio:** $|3x - 2| > 4$
1.  **Separación:** $3x - 2 < -4 \quad \cup \quad 3x - 2 > 4$.
2.  **Caso Izquierdo:** $3x < -4 + 2 \Rightarrow 3x < -2 \Rightarrow x < -\frac{2}{3}$.
3.  **Caso Derecho:** $3x > 4 + 2 \Rightarrow 3x > 6 \Rightarrow x > \frac{6}{3} \Rightarrow x > 2$.
4.  **Intervalo:** $(-\infty, -\frac{2}{3}) \cup (2, \infty)$.

#### Ejemplo 3: Caso Avanzado (Fracción)
**Ejercicio:** $|\frac{3x - 1}{4}| \geq 5$
1.  **Simplificar:** El $4$ (positivo) pasa multiplicando: $|3x - 1| \geq 20$.
2.  **Separación:** $3x - 1 \leq -20 \quad \cup \quad 3x - 1 \geq 20$.
3.  **Solución Izquierda:** $3x \leq -19 \Rightarrow x \leq -\frac{19}{3}$.
4.  **Solución Derecha:** $3x \geq 21 \Rightarrow x \geq 7$.
5.  **Resultado:** $(-\infty, -\frac{19}{3}] \cup [7, \infty)$.

#### Ejemplo 4: Aplicación Real ($USD)
**Situación:** El costo operativo $x$ de un producto en dólares debe cumplir $|\frac{2x + 4}{3}| \leq 6$ para ser rentable.
1.  **Sándwich:** $-6 \leq \frac{2x + 4}{3} \leq 6$.
2.  **Despeje Multilateral:**
    *   Multiplicar por $3$: $-18 \leq 2x + 4 \leq 18$.
    *   Restar $4$: $-22 \leq 2x \leq 14$.
    *   Dividir por $2$: $-11 \leq x \leq 7$.
3.  **Conclusión:** El costo $x$ debe estar en el rango de $[-11, 7]$ dólares para cumplir la norma.

---

### 📝 Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Fácil
> 1. $|x - 2| < 5$
> 2. $|x + 4| \leq 10$
> 3. $|x - 1| > 3$
> 4. $|x + 7| \geq 2$

> [!abstract] 🟡 Nivel Medio
> 1. $|2x + 1| \geq 7$
> 2. $|3x - 5| < 4$
> 3. $|\frac{x + 2}{2}| \leq 4$
> 4. $|4x + 2| > 10$

> [!abstract] 🔴 Nivel Avanzado (Aplicación USD)
> 1. Un bono de productividad varía según $|x - 50| \leq 10$. Hallar el pago mínimo y máximo.
> 2. El margen de error de un presupuesto de construcción es $|2x - 100| \leq 20$.
> 3. La fluctuación de una criptomoneda se define por $|\frac{x - 10}{2}| < 5$.
> 4. Un ahorro programado para una empresa debe cumplir $|x + 15| \geq 60$.

> [!success] ✅ Respuestas para el Docente
> *   **Fácil:** 1) $(-3, 7)$ | 2) $[-14, 6]$ | 3) $(-\infty, -2) \cup (4, \infty)$ | 4) $(-\infty, -9] \cup [-5, \infty)$
> *   **Medio:** 1) $(-\infty, -4] \cup [3, \infty)$ | 2) $(\frac{1}{3}, 3)$ | 3) $[-10, 6]$ | 4) $(-\infty, -3) \cup (2, \infty)$
> *   **Avanzado:** 1) $[40, 60]$ | 2) $[40, 60]$ | 3) $(0, 20)$ | 4) $(-\infty, -75] \cup [45, \infty)$

---

### 🧠 Mini-Prueba de Autoevaluación

> [!question] Pregunta 1 (Conceptual)
> ¿Cuál es el conjunto solución de $|x + 3| < -2$ y de $|x + 3| > -2$?
> **Respuesta:** Para $|x + 3| < -2$ es $\emptyset$ (vacio), porque una distancia no puede ser menor a algo negativo. Para $|x + 3| > -2$ son todos los números reales ($\mathbb{R}$), porque cualquier distancia siempre será mayor que $-2$.

> [!question] Pregunta 2 (Procedimental)
> Al resolver $|ax + b| > c$, ¿qué conectores lógicos usamos?
> **Respuesta:** Se usa la Unión ($\cup$). Las inecuaciones resultantes son $ax + b < -c$ **O** $ax + b > c$.

> [!question] Pregunta 3 (Aplicación $USD)
> Si la ganancia de una inversión es $|x - 100| \leq 5$, ¿cuál es el rango de ganancia?
> **Respuesta:** $x \in [95, 105]$. Aplicando el sándwich: $-5 \leq x - 100 \leq 5$, sumamos 100 y obtenemos el rango.

---

### 💡 En la próxima clase
En la **Clase 09**, cerraremos nuestro bloque de inecuaciones. Utilizaremos todo lo aprendido sobre valores absolutos y desigualdades para resolver **problemas complejos de modelado**, donde tú mismo construirás las ecuaciones a partir de situaciones reales de ingeniería y finanzas.

> [!info] 🧭 Navegación
> [[Clase 07|⬅ Clase 07]] | [[00 - Índice del curso|Índice]] | **Clase 08** | [[Clase 09|Clase 09 ➡]]