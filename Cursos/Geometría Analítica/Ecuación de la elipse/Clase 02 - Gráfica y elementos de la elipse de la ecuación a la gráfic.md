# Clase 02 — Gráfica y elementos de la elipse: de la ecuación a la gráfica y viceversa

#algebra #graphandelement
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 6

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | [[Clase 03|Clase 03 ➡]]

---

> [!info] 🌍 Relevancia y aplicaciones
> La elipse es la firma geométrica del universo: desde las órbitas de los planetas hasta la arquitectura de las "galerías de susurros", donde el sonido emitido en un foco se refleja con precisión quirúrgica en el otro. Dominar su ecuación es la llave para entender fenómenos físicos y optimizar costos en el diseño industrial.
> 
> *   💵 **Costos de fabricación:** En la producción de mobiliario de diseño, el costo de los materiales de acabado (como cantos de PVC o metal) se calcula sobre el perímetro o los diámetros de la pieza; una mesa elíptica de lujo puede requerir un refuerzo cuyo costo es de **$85 USD** por metro lineal.
> *   🏗️ **Ingeniería y Puentes:** Los arcos elípticos permiten distribuir las cargas de compresión de manera más eficiente que los circulares en puentes y estadios.
> *   📊 **Iluminación Quirúrgica:** Las lámparas de quirófano utilizan reflectores elípticos para concentrar la luz en un foco específico, minimizando las sombras durante una operación.

---

> [!note] 📌 ¿Qué es la ecuación ordinaria de la elipse?
> Es la herramienta analítica que nos permite "leer" la figura sin verla. Su estructura se basa en dos fracciones igualadas a la unidad:
> $$\frac{(x-h)^2}{\text{denominador}} + \frac{(y-k)^2}{\text{denominador}} = 1$$
> Donde:
> 1.  **Centro $(h, k)$:** Es el punto de equilibrio de la figura. **Regla de oro:** Al extraer $h$ y $k$ de la ecuación para graficar, siempre debemos invertir sus signos.
> 2.  **Semiajes ($a$ y $b$):** Los denominadores no son $a$ y $b$, sino sus cuadrados ($a^2$ y $b^2$). El **Semieje Mayor ($a$)** es la distancia del centro al vértice más lejano, y el **Semieje Menor ($b$)** es la distancia al vértice más cercano.

> [!warning] ⚠️ Error común
> El error más grave es asumir que $a$ siempre está debajo de $x$. ¡Falso! En la elipse, **$a^2$ es siempre el número mayor**. Si el número más grande está bajo la $y$, entonces $a^2$ está bajo la $y$.

> [!tip] 💡 Truco para recordarlo
> Para determinar la orientación visual de la elipse:
> *   Si el número mayor ($a^2$) está bajo la **X** $\rightarrow$ Elipse **Horizontal** ("acostada").
> *   Si el número mayor ($a^2$) está bajo la **Y** $\rightarrow$ Elipse **Vertical** ("alargada").

---

### 🛠️ Procedimiento paso a paso para graficar

```text
PASO 1 → Identificar el CENTRO (h, k) cambiando los signos de la ecuación.
         (Ejemplo: Si ves (x+4), h es -4).
PASO 2 → Determinar SEMIAJES:
         - a = raíz cuadrada del denominador mayor.
         - b = raíz cuadrada del denominador menor.
         - Calcular c (distancia focal) con Pitágoras: c = √(a² - b²).
PASO 3 → Calcular el LADO RECTO (LR = 2b² / a). 
         IMPORTANTE: Para graficar, usa LR/2 para marcar puntos a cada 
         lado del foco de forma perpendicular al eje mayor.
PASO 4 → Ubicar el centro, contar distancias (a, b, c), posicionar puntos 
         del LR y trazar la curva con suavidad.
```

---

### 📝 Ejemplos prácticos

> [!example] Ejemplo 1: Caso Horizontal (Ecuación a Gráfica)
> **Ecuación:** $\frac{(x-3)^2}{16} + \frac{(y+1)^2}{4} = 1$
> *   **Análisis:** 16 es el mayor y está bajo $x \rightarrow$ Horizontal.
> *   **Centro:** Invertimos signos: **$(3, -1)$**.
> *   **Parámetros:** $a^2 = 16 \Rightarrow \mathbf{a = 4}$ (semieje mayor). $b^2 = 4 \Rightarrow \mathbf{b = 2}$ (semieje menor).
> *   **Vértices:** Desde $(3, -1)$ contamos 4 unidades a derecha e izquierda: $V_1(7, -1)$ y $V_2(-1, -1)$.

> [!example] Ejemplo 2: Caso Vertical
> **Ecuación:** $\frac{(x+4)^2}{9} + \frac{(y-2)^2}{25} = 1$
> *   **Análisis:** 25 es el mayor y está bajo $y \rightarrow$ **Vertical**.
> *   **Centro:** Invertimos signos: **$(-4, 2)$**.
> *   **Parámetros:** $a = \sqrt{25} = 5$ y $b = \sqrt{9} = 3$.
> *   **Focos ($c$):** $c = \sqrt{25 - 9} = \sqrt{16} = 4$. Contamos 4 unidades hacia arriba y abajo del centro: $F_1(-4, 6)$ y $F_2(-4, -2)$.

> [!example] Ejemplo 3: Raíces no exactas (Semieje en $k=0$)
> **Ecuación:** $\frac{(x+4)^2}{20} + \frac{y^2}{9} = 1$
> *   **Centro:** Como $y$ no tiene número acompañante, $k = 0$. Centro en **$(-4, 0)$**.
> *   **Parámetros:** $a = \sqrt{20} \approx \mathbf{4.5}$. $b = \sqrt{9} = 3$.
> *   **Graficación:** Para situar los vértices mayores, nos movemos aproximadamente 4.5 unidades desde el centro sobre el eje X.

> [!example] Ejemplo 4: Aplicación Real ($USD)
> **Problema:** Una empresa fabrica espejos elípticos de seguridad. El costo de pulir el borde del **eje mayor** (el diámetro más largo) es de **$150 USD** por unidad de longitud. Si la ecuación del espejo es $\frac{x^2}{16} + \frac{y^2}{4} = 1$, ¿cuál es el presupuesto para esta tarea?
> *   **Solución:** 
>     1. Identificamos $a^2 = 16$, por lo tanto, el semieje mayor $a = 4$.
>     2. El eje mayor completo (diámetro) es $2a = 2(4) = 8$ unidades.
>     3. Presupuesto: $8 \text{ unidades} \times 150 \text{ USD} = \mathbf{1,200 \text{ USD}}$.

---

### ✏️ Ejercicios para el estudiante

> [!abstract] 🟢 Nivel Fácil: Identificación
> Extrae el centro $(h, k)$ y los valores de los semiajes $a$ y $b$:
> 1. $\frac{x^2}{25} + \frac{y^2}{9} = 1$
> 2. $\frac{x^2}{4} + \frac{y^2}{16} = 1$
> 3. $\frac{x^2}{100} + \frac{y^2}{64} = 1$
> 4. $\frac{x^2}{49} + \frac{y^2}{81} = 1$

> [!abstract] 🟡 Nivel Medio: De Gráfica a Ecuación
> Escribe la ecuación canónica asumiendo centro en $(0,0)$:
> 1. Eje mayor horizontal de 10 unidades, eje menor de 4.
> 2. Vértice mayor en $(0, 5)$ y vértice menor en $(1, 0)$.
> 3. Semieje $a=6$ sobre el eje Y, semieje $b=2$ sobre el eje X.
> 4. Elipse horizontal con $a=3$ y $b=1$.

> [!abstract] 🔴 Nivel Avanzado: Aplicaciones en $USD
> 1. Una cerca elíptica tiene semiejes $a=5m$ y $b=3m$. Si reforzar el diámetro menor cuesta **$120 USD** por metro, ¿cuánto cuesta el refuerzo total?
> 2. En un auditorio elíptico con $a=10$ y $b=8$, el costo de cableado entre ambos focos ($2c$) es de **$200 USD** por unidad. ¿Cuál es el costo total?
> 3. Halla el costo de un marco para el diámetro mayor de la elipse $\frac{x^2}{36} + \frac{y^2}{16} = 1$ si el precio es **$50 USD** por unidad.
> 4. Estima el costo de una mesa elíptica $\frac{x^2}{4} + \frac{y^2}{1} = 1$ cuyo soporte central cuesta **$300 USD** por cada unidad de área aproximada ($Area \approx 3 \times a \times b$).

> [!success] ✅ Respuestas (Para el docente)
> *   **Fácil:** 1. $C(0,0), a=5, b=3$ | 2. $C(0,0), a=4, b=2$ | 3. $C(0,0), a=10, b=8$ | 4. $C(0,0), a=9, b=7$.
> *   **Medio:** 1. $\frac{x^2}{25} + \frac{y^2}{4} = 1$ | 2. $\frac{x^2}{1} + \frac{y^2}{25} = 1$ | 3. $\frac{x^2}{4} + \frac{y^2}{36} = 1$ | 4. $\frac{x^2}{9} + \frac{y^2}{1} = 1$.
> *   **Avanzado:** 1. **$720 USD** ($2b=6, 6 \times 120$) | 2. **$2,400 USD** ($c=6, dist=12, 12 \times 200$) | 3. **$600 USD** ($2a=12, 12 \times 50$) | 4. **$1,800 USD** ($3 \times 2 \times 1 \times 300$).

---

### 🧠 Mini-prueba de autoevaluación

> [!question] Pregunta 1: Si los denominadores son 49 (bajo Y) y 25 (bajo X), ¿qué orientación tiene la elipse?
> **Respuesta:** Vertical. El denominador mayor ($a^2 = 49$) está bajo la variable $Y$.

> [!question] Pregunta 2: Si el semieje mayor mide 5 y el menor 4, ¿a qué distancia del centro están los focos?
> **Respuesta:** A 3 unidades. Se aplica $c = \sqrt{5^2 - 4^2} = \sqrt{25 - 16} = 3$.

> [!question] Pregunta 3: El diámetro mayor de una elipse mide 10 metros. Si el costo de material es de $100 USD por metro, ¿cuál es el costo del diámetro?
> **Respuesta:** $1,000 USD. El diámetro mayor es $2a$, por lo que $10 \times 100 = 1,000$.

---

> [!tip] 💡 En la próxima clase
> Hemos dominado la forma ordinaria y su gráfica. En la Clase 03, daremos el siguiente paso: aprenderemos a expandir estos binomios para llegar a la **Ecuación General de la elipse**.

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | [[Clase 03|Clase 03 ➡]]