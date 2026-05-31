# Clase 02 — Gráfica y ecuación de la parábola: Foco y directriz

tags: #algebra #graphandequatio
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 9

> [!info] 🧭 Navegación
> ◀ [[Clase 01 — Introducción a la parábola]] | [[00 - Índice del curso]] | [[Clase 03 — Parábolas con vértice (h, k)]] ▶

---

## Relevancia y aplicaciones

Entender el foco y la directriz es como descubrir el "ADN" de la parábola. Esta relación matemática es lo que permite que una señal de satélite o la luz de un faro se concentren en un solo punto con precisión milimétrica.

* 💵 **Aplicación con $USD**: En telecomunicaciones, diseñar antenas parabólicas con el foco exacto reduce la pérdida de señal, lo que permite usar equipos menos costosos y optimizar la inversión en infraestructura.
* 🏗️ **Aplicación práctica**: Los reflectores de los telescopios y los faros de los autos colocan su fuente de luz en el foco para que los rayos salgan perfectamente paralelos, iluminando grandes distancias.
* 📊 **Situación cotidiana**: El chorro de agua de una fuente o el lanzamiento de un balón describen parábolas donde la gravedad actúa como el motor que define su apertura respecto a un foco invisible.

---

## Concepto clave

> [!note] 📌 ¿Qué es una parábola?
> Imagina que la parábola es como un **reflector o un paraguas gigante**. Técnicamente, es el conjunto de puntos que están a la misma distancia de un punto fijo llamado **Foco** y de una línea recta llamada **Directriz**. El **Vértice** es el punto de inicio de la curva y siempre se encuentra justo a la mitad del camino entre el foco y la directriz.

> [!warning] ⚠️ Error común
> Muchos estudiantes confunden el signo negativo de la ecuación con la medida de la distancia.
> ❌ **Incorrecto**: En $y^2 = -16x$, decir que la distancia $p$ es $-4$.
> ✅ **Correcto**: El parámetro $p$ representa una **distancia**, por lo tanto, siempre lo tratamos como un valor positivo ($p=4$) para ubicar puntos. El signo "$-$" de la ecuación solo sirve para indicarnos que la parábola abre hacia la izquierda o hacia abajo.

> [!tip] 💡 Truco para recordarlo
> Para saber hacia dónde abre la parábola sin memorizar tablas, usa esta regla: **"La parábola siempre abraza a la letra que está solita"** (la que no tiene el cuadrado).
> - Si la **Y** está solita y es positiva: abre hacia arriba (eje Y positivo).
> - Si la **X** está solita y es negativa: abre hacia la izquierda (eje X negativo).

---

## Procedimiento paso a paso

```text
PROCESO DE GRAFICACIÓN (Vértice en el origen)

PASO 1: Análisis visual. Identifica la letra "solita" (lineal) y su signo.
        Esto te dirá si la parábola abre hacia arriba, abajo, derecha o izquierda.

PASO 2: Calcular el parámetro "p". Iguala el número que acompaña a la letra 
        lineal a "4p". Despeja p (p = número / 4). Recuerda: p es una distancia.

PASO 3: Ubicación de elementos. Marca el Vértice en (0,0). Desde ahí, muévete 
        "p" unidades hacia donde abre la curva para hallar el Foco, y "p" 
        unidades en sentido opuesto para trazar la Directriz.

PASO 4: Amplitud (Lado Recto). El Lado Recto (LR) es igual a 4p. 
        ¡Punto clave!: Divide el LR entre 2 y cuenta esa cantidad hacia cada 
        lado del foco para saber qué tan abierta es la parábola antes de trazar.
```

---

## Ejemplos desarrollados

> [!example] Ejemplo 1: Caso Básico
> **Ecuación:** $x^2 = 8y$
> 1. **Apertura:** La letra solita es $y$ (positiva), así que abre hacia **arriba**.
> 2. **Parámetro:** $4p = 8 \implies p = 2$.
> 3. **Ubicación:** El vértice es $(0,0)$. El foco está 2 unidades arriba: $F(0, 2)$. La directriz es la línea horizontal 2 unidades abajo: $y = -2$.
> 4. **Trazado:** El Lado Recto es 8. Desde el foco, contamos **4 unidades a la derecha y 4 a la izquierda** para marcar los puntos extremos y unir con el vértice.

> [!example] Ejemplo 2: Caso con Signos
> **Ecuación:** $y^2 = -12x$
> 1. **Apertura:** La letra solita es $x$ (negativa), abre hacia la **izquierda**.
> 2. **Parámetro:** $4p = 12 \implies p = 3$. (Usamos 12 positivo porque es una distancia).
> 3. **Ubicación:** $V(0,0)$. El foco está 3 unidades a la izquierda: $F(-3, 0)$. La directriz es la línea vertical 3 unidades a la derecha: $x = 3$.
> 4. **Trazado:** Como el Lado Recto es 12, nos movemos **6 unidades hacia arriba y 6 hacia abajo** desde el foco para dar la amplitud correcta.

> [!example] Ejemplo 3: Caso Avanzado (Hallar ecuación y gráfica)
> **Datos:** Foco $(3, -1)$ y Directriz $y = 3$.
> 1. **Dibujo Auxiliar:** Antes de calcular, imagina o dibuja rápido: el foco está abajo y la directriz es una línea horizontal arriba. Esto nos dice que la parábola abre hacia **abajo**.
> 2. **Vértice:** Está a la mitad entre el foco ($y = -1$) y la directriz ($y = 3$). La distancia total es 4, así que $p = 2$. El vértice se ubica en $(3, 1)$.
> 3. **Ecuación:** Al abrir hacia abajo, usamos $(x - h)^2 = -4p(y - k)$.
>    Sustituyendo: $(x - 3)^2 = -4(2)(y - 1) \implies (x - 3)^2 = -8(y - 1)$.

> [!example] Ejemplo 4: Aplicación económica ($USD)
> **Problema:** Un reflector parabólico tiene la ecuación $x^2 = 20y$. El costo de fabricación es de $\$5.00$ por cada unidad de longitud del Lado Recto. ¿Cuál es el costo total?
> 1. **Lado Recto (LR):** ¡Recuerda el truco! En la ecuación $x^2 = 20y$, el número que acompaña a la letra solita **ya es el Lado Recto** ($4p$). Por lo tanto, $LR = 20$.
> 2. **Cálculo:** Multiplicamos la longitud por el precio: $20 \text{ unidades} \times \$5.00 = \$100.00$.
> 3. **Resultado:** El costo total de fabricación es de $\$100.00$ USD.

---

## Ejercicios para el estudiante

> [!success] Bloque Verde: Identificación (Fácil)
> 1. Dada $x^2 = 4y$, ¿hacia dónde abre la parábola?
> 2. Dada $y^2 = -16x$, ¿cuál es el valor del Lado Recto ($4p$)?
> 3. Si la directriz es $y = 5$ y el vértice es $(0,0)$, ¿hacia dónde abre la parábola? (Pista: No puede tocar la directriz).
> 4. En la ecuación $y^2 = 20x$, ¿cuál es la distancia focal $p$?

> [!warning] Bloque Amarillo: Graficación (Medio)
> Realiza la gráfica completa (V, F, D y LR) para las siguientes ecuaciones:
> 1. $x^2 = 12y$
> 2. $y^2 = 8x$
> 3. $x^2 = -4y$
> 4. $y^2 = -24x$

> [!danger] Bloque Rojo: Aplicación (Avanzado)
> 1. El mantenimiento de una antena con ecuación $y^2 = 16x$ cuesta $\$10$ USD por cada unidad del parámetro $p$. ¿Cuál es el costo?
> 2. Halla la ecuación de la parábola con Foco $(3, -1)$ y Directriz $x = -1$. (Identifica primero si es horizontal o vertical mediante un dibujo auxiliar).
> 3. Una superficie cuesta $\$2.50$ USD por unidad de Lado Recto. Si la ecuación es $x^2 = 40y$, ¿cuál es el costo?
> 4. Si el costo de una pieza es $C = 15p$, y la directriz está en $x = -3$ con vértice en $(0,0)$, halla $C$.

> [!check] Bloque de Éxito: Respuestas
> **Fácil:** 1. Arriba | 2. 16 (las distancias son positivas) | 3. Abajo | 4. $p = 5$.
> **Medio:** 1. $F(0,3), y=-3$ | 2. $F(2,0), x=-2$ | 3. $F(0,-1), y=1$ | 4. $F(-6,0), x=6$.
> **Avanzado:** 1. $\$40$ USD ($p=4$) | 2. $(y+1)^2 = 8(x-1)$ | 3. $\$100$ USD ($LR=40$) | 4. $\$45$ USD ($p=3$).

---

## Autoevaluación y cierre

> [!question] ¿Dónde se ubica siempre el foco respecto a la curva?
> a) Justo encima de la directriz.
> b) En el punto medio entre el vértice y el eje X.
> c) Siempre "dentro" o abrazado por la curvatura de la parábola.
> d) En cualquier coordenada aleatoria del plano.
> **Respuesta correcta: c.** Pedagógicamente decimos que la parábola "protege" al foco.

> [!question] Si tenemos la ecuación $y^2 = 2x$, ¿cuál es el valor de la distancia focal $p$?
> a) 2
> b) 0.5
> c) 4
> d) 1
> **Respuesta correcta: b.** Igualamos $4p = 2$, por lo tanto $p = 2/4 = 0.5$.

> [!question] Un ingeniero cobra $\$100$ USD por unidad de distancia focal ($p$). Si la directriz es $y=4$ y el vértice $(0,0)$, ¿cuánto cobrará?
> a) $\$100$ USD
> b) $\$400$ USD
> c) $\$200$ USD
> d) $\$800$ USD
> **Respuesta correcta: b.** El parámetro $p$ es la distancia absoluta entre el vértice y la directriz $|V - D|$. Aquí, $p = 4$. El costo es $4 \times 100 = 400$.

> [!tip] 💡 En la próxima clase
> Ya dominas las parábolas que nacen en el centro $(0,0)$. En la siguiente lección, aprenderemos a "mudarlas" a cualquier parte del plano cartesiano usando el vértice $(h, k)$. ¡No faltes!

---
> [!info] 🧭 Navegación
> ◀ [[Clase 01 — Introducción a la parábola]] | [[00 - Índice del curso]] | [[Clase 03 — Parábolas con vértice (h, k)]] ▶