# Clase 09 — Graficando la parábola a partir de su ecuación general

#algebra #graphingaparabo
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 9 de 9

> [!info] 🧭 Navegación
> ◀ [[Clase 08 — Ecuación de la parábola]] | [[00 - Índice del curso]] | Fin del curso ▶

---

> [!info] 🌍 Relevancia y aplicaciones
> El dominio de la transición entre la **Ecuación General** y su representación gráfica es el puente definitivo entre el álgebra abstracta y la realidad física. Esta habilidad permite a ingenieros y científicos predecir el comportamiento exacto de ondas y trayectorias.
> 
> *   **💵 Aplicación USD:** En el análisis financiero de oferta y demanda, las parábolas permiten identificar el "punto de equilibrio" o el **costo mínimo** de producción para maximizar utilidades en presupuestos corporativos.
> *   **🏗️ Aplicación práctica:** Es el estándar para diseñar la curvatura de los cables en puentes colgantes, asegurando que la tensión se distribuya de forma óptima.
> *   **📊 Situación cotidiana:** La trayectoria de un chorro de agua en una fuente ornamental sigue exactamente estas leyes matemáticas; graficarla permite ajustar la presión para que el agua caiga justo donde se desea.

---

> [!note] 📌 ¿Qué es Graficando una parábola dada la ecuación general?
> Imagina que tienes una habitación desordenada; la **Ecuación General** es ese desorden donde todos los muebles (términos) están en un solo lado igualados a cero. Graficar consiste en "ordenar" la habitación para pasar a la **Forma Canónica u Ordinaria**. Esta forma nos revela de inmediato el "corazón" de la curva: su vértice y hacia qué dirección se abre.

> [!warning] ⚠️ Error común
> ❌ **Incorrecto:** Extraer las coordenadas del vértice $(h, k)$ directamente de los paréntesis de la ecuación canónica manteniendo los signos originales.
> ✅ **Correcto:** Debes **invertir siempre el signo** de los números que acompañan a $x$ y $y$ al identificar el vértice. Si la ecuación dice $(x - 5)$, la coordenada $h$ es $+5$.

> [!tip] 💡 Truco para recordarlo
> Para saber el eje de apertura sin dudar, busca la variable que **no** tiene el exponente cuadrado. Esa letra es la "jefa": si la $y$ es lineal, la parábola abre verticalmente (eje Y); si la $x$ es lineal, abre horizontalmente (eje X).

---

### 4. METODOLOGÍA (Procedimiento paso a paso)

```text
PASO 1 → AGRUPAR: Coloca los términos de la variable al cuadrado en el lado 
         izquierdo y traslada el resto (variable lineal y constante) al derecho.
PASO 2 → COMPLETAR: Divide el coeficiente de la variable lineal entre 2 y elévalo 
         al cuadrado. Suma este valor en AMBOS LADOS. Esto "balancea" la balanza 
         matemática y crea un Trinomio Cuadrado Perfecto.
PASO 3 → FACTORIZAR: Convierte el trinomio en un binomio al cuadrado. En el lado 
         derecho, factoriza el coeficiente de la variable lineal (incluso si es 
         negativo) para aislar el parámetro 4p.
PASO 4 → IDENTIFICAR: Determina el Vértice V(h, k), el signo de apertura y 
         calcula p (p = valor factorizado / 4).
PASO 5 → GRAFICAR: Ubica el Vértice y el Foco (a distancia p). Usa el Lado Recto 
         (4p) para marcar dos puntos guía: muévete una distancia de 2p hacia 
         cada lado del foco perpendicularmente al eje de simetría.
```

---

### 5. BLOQUE DE EJEMPLOS RESUELTOS

> [!example] Ejemplo 1: Caso Básico (Apertura Vertical)
> **Ecuación:** $x^2 + 10x - 12y - 1 = 0$
> 1. **Agrupamos:** $x^2 + 10x = 12y + 1$
> 2. **Completamos:** Mitad de 10 es 5; $5^2 = 25$. Sumamos 25 en ambos lados:
>    $x^2 + 10x + 25 = 12y + 1 + 25$
> 3. **Factorizamos:** **$(x + 5)^2 = 12(y + 2)$**
> 4. **Análisis:** El Vértice es **$V(-5, -2)$**. Como $4p = 12$, entonces **$p = 3$**. 
> 5. **Gráfico:** Abre hacia arriba. El **Lado Recto (LR)** es 12; desde el foco, contamos 6 unidades a la izquierda y 6 a la derecha para trazar la anchura.

> [!example] Ejemplo 2: Manejo de Signos Negativos
> **Ecuación:** $y^2 + 6y + 4x + 17 = 0$
> 1. **Agrupamos:** $y^2 + 6y = -4x - 17$
> 2. **Completamos:** Mitad de 6 es 3; $3^2 = 9$.
>    $y^2 + 6y + 9 = -4x - 17 + 9 \Rightarrow (y + 3)^2 = -4x - 8$
> 3. **Factorización Crítica:** Extraemos el $-4$ completo: **$(y + 3)^2 = -4(x + 2)$**
> 4. **Análisis:** Vértice en **$V(-2, -3)$**. Como el valor de $4p$ es negativo y la $x$ manda, abre hacia la **izquierda**.

> [!example] Ejemplo 3: Caso Avanzado con Fracciones
> **Ecuación:** $4x^2 + 4x - 48y - 143 = 0$
> 1. **Simplificamos:** Dividimos todo entre 4 para dejar $x^2$ sin coeficiente:
>    $x^2 + x - 12y - \frac{143}{4} = 0$
> 2. **Agrupamos y completamos:** Coeficiente de $x$ es 1. Mitad es $\frac{1}{2}$, al cuadrado es $\frac{1}{4}$.
>    $x^2 + x + \frac{1}{4} = 12y + \frac{143}{4} + \frac{1}{4}$
>    $(x + \frac{1}{2})^2 = 12y + \frac{144}{4} \Rightarrow (x + \frac{1}{2})^2 = 12y + 36$
> 3. **Resultado:** **$(x + \frac{1}{2})^2 = 12(y + 3)$**
> 4. **Análisis:** $V(-\frac{1}{2}, -3)$, abre hacia arriba con $p=3$.

> [!example] Ejemplo 4: Aplicación Económica (Mínimo de Costos)
> Un sistema de logística de bajo costo ($15 USD por envío) sigue la trayectoria de costos: $x^2 - 8x - 8y + 32 = 0$, donde $y$ es el costo en cientos de USD.
> 1. **Proceso:** $x^2 - 8x + 16 = 8y - 32 + 16 \Rightarrow (x - 4)^2 = 8(y - 2)$
> 2. **Vértice:** $V(4, 2)$. 
> 3. **Interpretación USD:** El **costo mínimo** de la operación es de **200 USD** (representado por $k=2$), y se alcanza cuando el nivel de producción o envíos ($x$) es de 4 unidades.

---

### 6. EJERCICIOS DE PRÁCTICA

**Verde (Fácil): Identificación de Elementos**
1. Determina $V$ y sentido de apertura: $(x - 1)^2 = 8(y + 2)$
2. Determina $V$ y sentido de apertura: $(y + 5)^2 = -4x$
3. Determina $V$ y sentido de apertura: $x^2 = 12(y - 3)$
4. Encuentra el valor de $p$ si el Lado Recto es 16.

**Amarillo (Medio): Transformación de Ecuaciones**
1. Convierte a canónica: $x^2 - 8x - 8y + 32 = 0$
2. Convierte a canónica: $y^2 + 2y - 12x + 37 = 0$
3. Convierte a canónica: $x^2 + 10x - 12y + 1 = 0$
4. Convierte a canónica: $y^2 - 6y + 8x + 1 = 0$

**Rojo (Avanzado USD): Desafíos Financieros y Técnicos**
1. Una antena de satélite de $120 USD tiene una sección $y^2 - 12x = 0$. Si el receptor debe ir en el foco, ¿en qué coordenada $(x, y)$ se debe colocar?
2. Un soporte para puente de $25,000 USD sigue la forma $x^2 - 20y = 0$. ¿Cuál es la distancia focal $p$ que define su resistencia?
3. Una rampa de patinaje profesional de $500 USD tiene la ecuación $x^2 + 4x - 4y + 8 = 0$. Identifica el punto más bajo (vértice) para su mantenimiento.
4. El chorro de una fuente de lujo de $1,200 USD sigue la ecuación $x^2 - 6x + 4y + 13 = 0$. Determina la altura máxima (coordenada $k$ del vértice).

> [!success] Respuestas para el docente
> **Verde:** 1. $V(1, -2)$ Arriba | 2. $V(0, -5)$ Izquierda | 3. $V(0, 3)$ Arriba | 4. $p = 4$.
> **Amarillo:** 1. $(x-4)^2=8(y-2)$ | 2. $(y+1)^2=12(x-3)$ | 3. $(x+5)^2=12(y-2)$ | 4. $(y-3)^2=-8(x-1)$.
> **Rojo:** 1. Foco en $(3, 0)$ | 2. $p = 5$ unidades | 3. $V(-2, 1)$ | 4. $V(3, -1)$ [Altura máxima en $y = -1$].

---

### 7. AUTOEVALUACIÓN (Mini-prueba)

1. **Conceptual:** Según la definición de lugar geométrico, si un punto está a 5 unidades del foco, ¿a qué distancia debe estar de la directriz?
2. **Procedimental:** En la ecuación $(y - 4)^2 = 20(x - 2)$, ¿cuántas unidades debes moverte hacia arriba y hacia abajo desde el foco para marcar los puntos del Lado Recto?
3. **Aplicación USD:** Una empresa determina que sus pérdidas se modelan con $(x-10)^2 = 4(y-50)$. ¿Cuál es el valor mínimo de pérdida (vértice) en USD?

---

> [!tip] 💡 En la próxima clase
> Exploraremos las aplicaciones avanzadas de la parábola en la vida real, desde radares militares hasta la concentración de energía solar.

> [!info] 🧭 Navegación
> ◀ [[Clase 08 — Ecuación de la parábola]] | [[00 - Índice del curso]] | Fin del curso ▶