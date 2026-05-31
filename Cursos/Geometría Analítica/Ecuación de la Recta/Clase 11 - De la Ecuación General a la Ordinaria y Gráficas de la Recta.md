# Clase 11 — De la Ecuación General a la Ordinaria y Gráficas de la Recta

#algebra #pasardelaecuaci

Curso: [[00 - Índice del curso]] | Bloque 3 | Lección 11 de 11

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [[Clase 10 — Ecuación de la Recta]] | 🏠 **Inicio:** [[00 - Índice del curso]]

---

> [!info] 🌍 Relevancia y aplicaciones
> Convertir la ecuación de una recta a su forma ordinaria es como "quitarle el disfraz" a la función: nos permite identificar visualmente hacia dónde va la línea y dónde comienza nuestro conteo en el eje vertical.
> *   **💵 [Costo de suscripciones]:** En un servicio de streaming, permite ver que el cargo fijo mensual es el punto de corte ($b$) y el costo por cada perfil extra es la pendiente ($m$).
> *   **🏗️ [Construcción]:** Ayuda a los arquitectos a calcular la inclinación exacta de una rampa de acceso basándose en los datos del plano general de la obra.
> *   **📊 [Movimiento]:** Facilita entender la velocidad constante de un vehículo al observar directamente su pendiente en la ecuación de movimiento.

---

> [!note] 📌 ¿Qué es Pasar de la ecuación General (Fundamental) a la Ordinaria (pendiente-ordenada)?
> Es el proceso de realizar un **despeje** para que la variable $y$ quede totalmente sola. Al hacer esto, la ecuación nos "confiesa" dos secretos fundamentales: la inclinación ($m$) y el punto de cruce en el eje vertical ($b$).
> 
> > [!tip] 💡 El Secreto del Profe Alex: La Fórmula Directa
> > Si tienes prisa y no quieres despejar, puedes hallar la pendiente ($m$) directamente desde la ecuación general ($Ax + By + C = 0$) usando:
> > $$m = \frac{-A}{B}$$
> > ¡Es un atajo asombroso para ahorrar tiempo!

> [!warning] ⚠️ ¡Mucho ojo con esto!
> 1. **Cambio de Signos:** Al mover términos al otro lado del signo igual ($=$), ¡debes invertir su signo! Lo positivo pasa negativo y lo negativo pasa positivo.
> 2. **Diferencia de letras:** No confundas la **$B$ mayúscula** (el número que acompaña a la $y$ en la ecuación general) con la **$b$ minúscula** (el punto donde la recta corta al eje $y$ en la forma ordinaria). ¡Son cosas distintas!

> [!tip] 💡 Truco para recordarlo
> "La $y$ quiere estar sola para mostrarte el camino (la pendiente) y la meta (el punto de corte)".

---

### PROCEDIMIENTO PASO A PASO

Para transformar $Ax + By + C = 0$ a $y = mx + b$, sigue estos pasos con mucha atención:

```text
PASO 1 → Identificar los términos que tienen la "x" y el número que está solo (la constante).
PASO 2 → Mover esos términos al lado derecho del igual cambiando sus signos.
PASO 3 → Despejar la "y" dividiendo cada término del lado derecho entre el coeficiente que acompañaba a la "y".
PASO 4 → Simplificar las fracciones para que la pendiente (m) y el corte (b) se vean claros.
```

---

### BLOQUE DE EJEMPLOS (CON EL MÉTODO DEL PROFE ALEX)

> [!example] Ejemplo 1: El Despeje Paso a Paso
> **Problema:** Convierte $5x + 2y - 3 = 0$ a la forma ordinaria.
> 1. Primero, dejamos el término con $y$ en su lugar y movemos el resto:
>    $$2y = -5x + 3$$ (Nota cómo el $5x$ pasó a ser negativo y el $-3$ pasó a ser positivo).
> 2. Ahora, el número **2** que multiplica a la $y$ pasa a dividir a **cada** término del otro lado:
>    $$y = \frac{-5x}{2} + \frac{3}{2}$$
> 3. **Resultado:** $y = -\frac{5}{2}x + \frac{3}{2}$.
> *Aquí la pendiente es $m = -5/2$ y el corte es $b = 3/2$.*

> [!example] Ejemplo 2: Gráfica Perfecta con Tabla de Valores
> **Problema:** Grafica la recta $-2x + y + 3 = 0$.
> 1. **Despejamos $y$:** $y = 2x - 3$.
> 2. **Creamos la tabla:** El Profe Alex recomienda **3 puntos** para verificar que nuestra línea sea perfectamente recta.
> 
> | Valor de $x$ | Operación: $y = 2x - 3$ | Punto $(x, y)$ |
> | :--- | :--- | :--- |
> | 0 | $y = 2(0) - 3 = -3$ | $(0, -3)$ |
> | 1 | $y = 2(1) - 3 = -1$ | $(1, -1)$ |
> | 2 | $y = 2(2) - 3 = 1$ | $(2, 1)$ |
> 
> *Si al graficarlos puedes unirlos con una regla sin que ninguno se salga, ¡tu ejercicio está correcto!*

> [!example] Ejemplo 3: Rectas Paralelas
> **Problema:** Halla la ecuación de la recta que pasa por $(-2, 5)$ y es paralela a $-2x + y - 4 = 0$.
> 1. **Buscamos la pendiente ($m$):** Usamos el atajo del Profe Alex en la ecuación original donde $A = -2$ y $B = 1$.
>    $$m = \frac{-(-2)}{1} = \frac{2}{1} = 2$$
> 2. **Lógica de paralelas:** Como son paralelas, la nueva pendiente es **exactamente la misma** ($m_1 = m_2 = 2$).
> 3. **Fórmula Punto-Pendiente:** Usamos el punto $(-2, 5)$ y $m = 2$.
>    $$y - 5 = 2(x - (-2))$$
>    $$y - 5 = 2(x + 2)$$
>    $$y - 5 = 2x + 4$$
> 4. **Resultado final (Forma General):** Pasamos todo a la izquierda para igualar a cero:
>    $$-2x + y - 9 = 0$$

> [!example] Ejemplo 4: Aplicación en $USD (Streaming)
> **Problema:** Un servicio cuesta $10 USD fijos más $2 USD por dispositivo extra. La ecuación general es $2x - y + 10 = 0$. ¿Cuál es el costo base?
> 1. Despejamos la $y$: $-y = -2x - 10$.
> 2. Como la $y$ no puede ser negativa, multiplicamos todo por $-1$:
>    $$y = 2x + 10$$
> 3. **Conclusión:** El costo base (punto de corte $b$) es de **$10 USD**, y aumenta **$2 USD** por cada dispositivo extra ($x$).

---

### EJERCICIOS PARA EL ESTUDIANTE

**🟢 Nivel Fácil: Despeje Directo**
Convierte a forma ordinaria ($y = mx + b$):
1. **$x - y + 5 = 0$**
2. **$3x + y - 2 = 0$**
3. **$-x + y - 10 = 0$**
4. **$4x - y + 1 = 0$**

**🟡 Nivel Medio: Identifica y Grafica**
Encuentra $m$ y $b$, luego realiza una tabla de 3 puntos para graficar:
1. **$2x + 2y - 4 = 0$**
2. **$6x - 3y + 9 = 0$**
3. **$x + 2y - 6 = 0$**
4. **$-3x + y + 5 = 0$**

**🔴 Nivel Avanzado: Paralelas y $USD**
1. Halla la ecuación de la recta paralela a **$2x - y + 5 = 0$** que pasa por el origen $(0, 0)$.
2. Halla la ecuación de la recta paralela a **$-4x + y - 2 = 0$** que pasa por el punto $(1, 2)$.
3. Una cuenta de ahorros inicia con **$50 USD** y sumas **$10 USD** cada mes. Escribe la ecuación general y luego pásala a ordinaria.
4. Un plan móvil tiene la ecuación general **$0.5x - y + 15 = 0$** ($x$ son minutos). ¿Cuál es el cargo fijo mensual en USD?

**✅ Respuestas para el docente**
*Fáciles:* 1. $y=x+5$ | 2. $y=-3x+2$ | 3. $y=x+10$ | 4. $y=4x+1$.
*Medios:* 1. $m=-1, b=2$ | 2. $m=2, b=3$ | 3. $m=-1/2, b=3$ | 4. $m=3, b=-5$.
*Avanzados:* 1. $y=2x$ | 2. $y=4x-2$ | 3. $10x - y + 50 = 0 \rightarrow y = 10x + 50$ | 4. $15 USD$.

---

### MINI-PRUEBA DE AUTOEVALUACIÓN

1. **¿Qué información nos da el valor de $b$ en la ecuación $y = mx + b$?**
   *Respuesta: Indica el lugar exacto donde la recta cruza el eje vertical (Y).*
2. **Si una recta tiene la ecuación $-3x + y + 5 = 0$, ¿cuál es la pendiente de cualquier recta paralela a ella?**
   *Respuesta: La pendiente es 3 (porque al despejar obtenemos $y = 3x - 5$).*
3. **Usando la ecuación $y = 5x + 20$ (donde $y$ es el costo en USD y $x$ son los meses), ¿cuál es el costo total al cabo de 5 meses?**
   *Respuesta: $45 USD$ ($y = 5(5) + 20 = 25 + 20$).*

---

> [!tip] 💡 En la próxima clase
> ¡Felicidades! Has llegado al final del Bloque 3 y del curso. Has aprendido a dominar las rectas, sus ecuaciones y sus aplicaciones reales. Te invitamos a repasar el **Índice del curso** para consolidar todo lo aprendido. ¡Sigue practicando, el álgebra es tu superpoder!

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [[Clase 10 — Ecuación de la Recta]] | 🏠 **Inicio:** [[00 - Índice del curso]]