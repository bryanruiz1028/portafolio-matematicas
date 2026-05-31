# 📖 Guía de estudio — Clase 02: Gráfica y ecuación de la parábola: foco y directriz

> [!info] 📌 Conceptos clave
> 1. **Orientación:** Para identificar hacia dónde abre la parábola, observa la variable que **no** está elevada al cuadrado y su signo. Si es $y$ positiva, abre hacia arriba; si es $y$ negativa, hacia abajo. Si es $x$ positiva, abre a la derecha; si es $x$ negativa, a la izquierda.
> 2. **Parámetro ($p$) y Signos:** El parámetro $p$ es la distancia (siempre positiva) entre el vértice ($V$) y el foco ($F$). Sin embargo, al escribir la ecuación, el signo de $4p$ será positivo si abre hacia arriba/derecha y negativo si abre hacia abajo/izquierda.
> 3. **Relación de Distancias:** El vértice ($V$) es el punto medio entre el foco y la directriz. El coeficiente de la variable lineal en la ecuación equivale al Lado Recto ($LR = |4p|$), que indica el ancho de la parábola en el foco.
> 4. **Ubicación del Vértice:** En ecuaciones canónicas simples como $x^2 = 4py$ o $y^2 = 4px$, el vértice se ubica en el origen $(0,0)$. En ecuaciones con desplazamientos $(h, k)$, el vértice se traslada a dicho punto.

## Fórmulas y definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Vértice ($V$)** | Punto de origen $(0,0)$ o coordenadas de desplazamiento $(h, k)$. |
| **Foco ($F$)** | Punto interior ubicado sobre el eje de simetría a una distancia $p$ del vértice. |
| **Directriz ($d$)** | Recta fija exterior a la parábola, perpendicular al eje de simetría. |
| **Parámetro ($p$)** | Distancia absoluta entre el vértice y el foco (o entre el vértice y la directriz). |
| **Lado Recto ($LR$)** | Longitud de la cuerda que pasa por el foco: $LR = |4p|$. |
| **Eje de Simetría** | Recta que pasa por $V$ y $F$, dividiendo a la parábola en dos partes simétricas. |
| **Ecuación (Vertical)** | $x^2 = 4py$ (Abre hacia arriba/abajo). |
| **Ecuación (Horizontal)** | $y^2 = 4px$ (Abre hacia la derecha/izquierda). |

## Ejemplos resueltos adicionales

```ad-example title: Ejemplo A — Gráfica desde la ecuación canónica
**Enunciado:** Graficar la parábola dada por la ecuación $x^2 = 8y$.

**Paso a paso:**
1. **Paso 0 — Dibujo auxiliar:** La variable no cuadrática es $y$ y el signo es positivo. Hacemos un boceto rápido de una parábola que abre hacia **arriba** (eje $Y$ positivo).
2. **Identificar elementos:** Como la ecuación es de la forma $x^2 = 4py$, el vértice está en $V(0,0)$.
3. **Calcular el parámetro ($p$):** Igualamos el coeficiente lineal: $4p = 8$. Despejando, $p = 8 / 4 = 2$.
4. **Ubicar coordenadas:** 
   - El foco $F$ está 2 unidades arriba del vértice: $F(0, 2)$.
   - La directriz $d$ es la recta 2 unidades debajo del vértice: $y = -2$.
5. **Calcular el lado recto ($LR$):** $LR = 8$. Desde el foco, contamos 4 unidades a la izquierda y 4 a la derecha para marcar los puntos extremos y trazar la curva.
```

```ad-example title: Ejemplo B — Costo de diseño de antena parabólica
**Enunciado:** Un ingeniero diseña una antena cuya sección transversal sigue la forma $y^2 = 12x$. Si el material del receptor (ubicado en el foco) cuesta $15.50 USD por cada unidad de distancia desde el vértice, ¿cuál es el costo total del receptor?

**Paso a paso:**
1. **Paso 0 — Dibujo auxiliar:** La ecuación $y^2 = 12x$ tiene la variable $x$ lineal y positiva; el boceto muestra que abre hacia la **derecha**.
2. **Determinar el parámetro ($p$):** Igualamos $4p = 12$, por lo tanto, $p = 12 / 4 = 3$.
3. **Análisis técnico:** El problema indica que el receptor está en el foco y se cobra por la distancia desde el vértice. Por definición, la distancia entre el vértice y el foco es el parámetro $p$. Por lo tanto, la distancia a cobrar es de 3 unidades.
4. **Calcular costo total:** Multiplicamos la distancia ($p = 3$) por el costo unitario: $3 \times 15.50$.
5. **✅ Resultado:** El costo total del receptor es $46.50 USD.
```

## Ejercicios de repaso

```ad-abstract title: 🟢 Fácil
1. Dada la ecuación $x^2 = 16y$, ¿cuánto vale el parámetro $p$?
2. ¿Hacia qué dirección (arriba, abajo, izquierda, derecha) abre la parábola $y^2 = -8x$?
3. Si el parámetro $p = 5$ y la parábola abre hacia arriba con vértice en $(0,0)$, ¿cuál es la coordenada del foco $F$?
```

```ad-abstract title: 🟡 Medio
1. Encuentra la ecuación de la parábola que tiene su foco en $F(0, -3)$ y su directriz en la recta $y = 3$.
2. Calcula la longitud del lado recto ($LR$) para la parábola $y^2 = 20x$.
3. Realiza un bosquejo mental e indica la ecuación de la directriz para la parábola $x^2 = -4y$.
```

```ad-abstract title: 🔴 Avanzado — Aplicación con $USD
1. Un reflector parabólico tiene su foco ubicado a 2 metros del vértice. Si el soporte estructural que atraviesa el foco de extremo a extremo de la parábola (lado recto) cuesta $100 USD por cada metro de longitud, ¿cuál es el presupuesto total necesario para dicho soporte?
*(Pista: Identifica $p$, calcula la longitud del lado recto $|4p|$ y multiplica por el costo unitario).*
```

> [!tip] 💡 Consejo de estudio
> Aplica siempre el **"Paso 0: Dibujo auxiliar"**. Antes de realizar cálculos numéricos, haz un boceto rápido de la orientación. Esto te permitirá visualizar correctamente si debes sumar o restar el parámetro $p$ para hallar el foco o la directriz, evitando errores comunes con los signos negativos.