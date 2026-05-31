# Clase 03 — Graficando una parábola desde su ecuación ordinaria
tags: #algebra #graphingaparabo
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 9

[!info] 🧭 Navegación
[« Clase Anterior](Clase_02) | [Índice del Curso](00_Indice) | [Próxima Clase »](Clase_04)

---

## 🌍 Relevancia y aplicaciones

[!info] **¿Por qué aprender a graficar parábolas?**
Graficar una parábola desde su forma ordinaria es la manera más eficiente de visualizar el comportamiento de sistemas físicos y financieros mediante puntos críticos.

*   💵 **Aplicación con $USD**: En economía, el vértice de una parábola modela el **punto de equilibrio** o el **punto de rendimientos decrecientes**. Permite identificar con precisión el costo mínimo de producción o el ingreso máximo posible.
*   🏗️ **Aplicación práctica**: Es esencial en la ingeniería de vanguardia para diseñar reflectores parabólicos y puentes colgantes, donde el foco es el punto exacto donde se concentra la energía o se distribuyen las tensiones.
*   📊 **Situación cotidiana**: Cada vez que lanzas un objeto al aire, su trayectoria describe una parábola. Graficarla permite predecir el impacto y la altura máxima de un balón o un proyectil.

---

## 📌 ¿Qué es graficar una parábola usando la ecuación ordinaria?

[!note] **Definición**
La **ecuación ordinaria (o canónica)** es aquella que nos muestra "a simple vista" los elementos más importantes: el vértice $(h, k)$ y la distancia focal $p$. Es como leer las coordenadas de un tesoro directamente en el mapa sin tener que hacer cálculos complejos.

[!warning] **⚠️ Error común: El cambio de signo**
¡Mucho cuidado aquí! El error más frecuente de los estudiantes es extraer $h$ y $k$ con el mismo signo que ven en la ecuación. Recuerda que la fórmula tiene un signo negativo por defecto, por lo que **siempre debes usar el opuesto**.
*   ❌ **Incorrecto**: $(x - 3)^2 \rightarrow h = -3$
*   ✅ **Correcto**: $(x - 3)^2 \rightarrow h = 3$
*   ❌ **Incorrecto**: $(y + 5)^2 \rightarrow k = 5$
*   ✅ **Correcto**: $(y + 5)^2 \rightarrow k = -5$

[!tip] **💡 Truco para recordarlo: La "Letra No Cuadrada"**
Para saber hacia dónde abre la parábola, fíjate en la variable que **no** tiene el exponente 2:
*   Si la **$y$** no está al cuadrado: Abre hacia **arriba (+)** o **abajo (-)**.
*   Si la **$x$** no está al cuadrado: Abre hacia la **derecha (+)** o **izquierda (-)**.

---

## 🚀 Procedimiento paso a paso (El Método "Profe Alex")

Sigue estos 4 pasos críticos para que tu gráfica sea perfecta:

```text
PASO 1: Identifica el vértice (h, k) extrayendo los números de los 
        paréntesis y cambiando sus signos. (Recuerda: h va con x, k con y).
        
PASO 2: Haz un "DIBUJO AUXILIAR" (un boceto rápido). Mira qué letra NO 
        está al cuadrado y su signo para saber la orientación. Esto te 
        dirá si el foco va arriba, abajo, a la izquierda o derecha.

PASO 3: Calcula el parámetro "p". Toma el número que está fuera del 
        paréntesis y divídelo entre 4. (Ese número es 4p).

PASO 4: Traza el "LADO RECTO". Desde el foco, muévete una distancia de 
        2p (la mitad del coeficiente total) hacia cada lado para marcar 
        los puntos por donde pasará la curva.
```

---

## 📖 Ejemplos desarrollados

### Ejemplo 1: Caso Básico (Abre hacia arriba)
**Ecuación:** $(x - 3)^2 = 4(y - 2)$
1.  **Vértice:** Cambiamos signos: $V(3, 2)$.
2.  **Orientación:** La letra no cuadrada es $y$ y el 4 es positivo. ¡Hacemos el dibujo auxiliar! Abre hacia **arriba**.
3.  **Parámetro ($p$):** $4p = 4$, entonces $p = 4/4 = 1$.
4.  **Gráfico:** El foco está 1 unidad arriba del vértice en $(3, 3)$. Para el Lado Recto, nos movemos $2p$ (2 unidades) a la derecha e izquierda del foco.

### Ejemplo 2: Caso con Signos (Abre a la derecha)
**Ecuación:** $(y - 2)^2 = 8(x + 3)$
1.  **Vértice:** Cambiamos signos: $V(-3, 2)$. (Recuerda que $h$ siempre sale del paréntesis de $x$).
2.  **Orientación:** La letra no cuadrada es $x$ y el 8 es positivo. Abre hacia la **derecha**.
3.  **Parámetro ($p$):** $4p = 8$, entonces $p = 2$.
4.  **Gráfico:** El foco está 2 unidades a la derecha del vértice en $(-1, 2)$. La directriz es una línea vertical 2 unidades a la izquierda del vértice ($x = -5$).

### Ejemplo 3: Caso Avanzado (Valores en Cero y Fracciones)
**Ecuación:** $x^2 = -1(y + 3)$
1.  **Vértice:** Como $x$ no tiene compañero, $h = 0$. Con $y$ cambiamos signo: $k = -3$. $V(0, -3)$.
2.  **Orientación:** La variable no cuadrada es $y$ con signo negativo. Abre hacia **abajo**.
3.  **Parámetro ($p$):** $4p = 1$, entonces $p = 1/4 = 0.25$.
4.  **Gráfico detallado:**
    *   **Foco:** Bajamos $1/4$ desde $-3$. Coordenada: $(0, -13/4)$ o $(0, -3.25)$.
    *   **Directriz:** Subimos $1/4$ desde $-3$. Ecuación: $y = -11/4$ o $y = -2.75$.

### Ejemplo 4: Aplicación $USD (Costo Mínimo)
**Problema:** Una empresa de software modela sus costos operativos mensuales mediante $(x - 10)^2 = 2(y - 500)$, donde $x$ es el número de servidores activos y $y$ es el costo en $USD.
1.  **Análisis:** El vértice es $V(10, 500)$.
2.  **Interpretación:** La parábola abre hacia arriba, por lo que el vértice es el **punto de costo mínimo**. El gasto mínimo es de **$500 USD** y se alcanza operando exactamente **10 servidores**.

---

## ✍️ Ejercicios para el estudiante

### 🟢 Verdes (Fáciles)
1. Hallar vértice y orientación de: $(x - 1)^2 = 4(y - 1)$.
2. Determinar el vértice y hacia dónde abre: $(y + 4)^2 = 16(x - 2)$.
3. Calcular el valor de $p$ para la ecuación: $(x + 5)^2 = 20(y - 3)$.
4. Indicar el vértice de la parábola: $x^2 = 8(y + 2)$.

### 🟡 Amarillos (Medios)
5. Graficar y hallar el foco de: $(y + 2)^2 = -8x$.
6. Determinar la ecuación de la directriz de: $(x - 3)^2 = 4(y + 0)$.
7. Hallar el parámetro $p$ (en fracción) para: $(y - 1)^2 = 1(x + 2)$.
8. Realizar el dibujo auxiliar y graficar: $y^2 = -12(x - 5)$.

### 🔴 Rojos (Avanzados - Contexto $USD)
9. El balance de una startup en $USD sigue la ecuación $(x - 100)^2 = 400(y + 1000)$, donde $x$ es ventas y $y$ es utilidad. Grafique el foco y la directriz. ¿Qué representa el vértice en este contexto financiero?
10. Se diseña un fondo de inversión cuya curva de riesgo es $(y - 50)^2 = 20(x - 10)$. Si el "punto objetivo" es el foco, halle sus coordenadas y grafique la directriz económica.
11. Un modelo de pérdidas por inflación sigue la forma $x^2 = -1(y + 500)$. Calcule la coordenada exacta del foco (en fracción) y determine si la directriz está por encima o por debajo del presupuesto base ($y = 0$).
12. Un reflector de costos marginales tiene la ecuación $y^2 = 40(x - 5)$. Grafique el foco y determine la longitud del Lado Recto para entender la amplitud de la variabilidad del costo en $USD.

---

## ✅ Respuestas para el docente

[!success] **Solucionario rápido**
1. $V(1, 1)$, Abre arriba. | 2. $V(2, -4)$, Abre derecha. | 3. $p = 5$. | 4. $V(0, -2)$.
5. $V(0, -2)$, Foco $(-2, -2)$. | 6. $y = -1$ (Vértice $(3,0)$, $p=1$). | 7. $p = 1/4$. | 8. $V(5, 0)$, Abre izquierda, $p=3$.
9. $V(100, -1000)$. El vértice representa la utilidad mínima (o pérdida máxima controlada). Foco $(100, -900)$.
10. $V(10, 50)$, $p=5$, Abre derecha. Foco $(15, 50)$. Directriz $x = 5$.
11. $V(0, -500)$, $p=1/4$. Foco $(0, -2001/4)$ o $(0, -500.25)$. Directriz $y = -1999/4$ o $-499.75$. Está por debajo del presupuesto base.
12. $V(5, 0)$, $p=10$, Abre derecha. Foco $(15, 0)$. Lado Recto $= 40$.

---

## 🧠 Mini-prueba de autoevaluación

[!question] **Pregunta 1: Procedimiento**
¿Por qué es vital hacer el "Dibujo Auxiliar" antes de colocar el foco en el plano real?
*R: Porque evita confundir la dirección del parámetro $p$. Si la parábola abre a la izquierda, el dibujo auxiliar nos recuerda que el foco debe restarse a la coordenada $h$.*

[!question] **Pregunta 2: El parámetro p**
En la ecuación $(y - 3)^2 = 2(x + 1)$, ¿cuál es el valor de $p$ y cuánto debes moverte desde el foco para trazar el Lado Recto?
*R: $p = 0.5$ (ya que $2/4 = 0.5$). Debes moverte $2p$, es decir, 1 unidad hacia arriba y 1 unidad hacia abajo del foco.*

[!question] **Pregunta 3: Aplicación $USD**
Si el vértice de una parábola de ingresos es $V(500, 2000)$ y abre hacia abajo, ¿cuál es el ingreso máximo?
*R: El ingreso máximo es de $2000 USD, logrado al vender 500 unidades.*

---

[!tip] **💡 En la próxima clase**
Aprenderemos la **Ecuación General de la Parábola**. Descubriremos cómo transformar esas ecuaciones largas y desordenadas (como $Ax^2 + Dx + Ey + F = 0$) a la forma ordinaria que dominaste hoy usando el método de completar el cuadrado. ¡No te lo pierdas!

---

[!info] 🧭 Navegación
[« Clase Anterior](Clase_02) | [Índice del Curso](00_Indice) | [Próxima Clase »](Clase_04)