# 📖 Guía de estudio — Clase 01: Ecuación de la parábola

### 1. 📌 Conceptos clave

> [!info] **Lo que debes dominar**
> - **¿Qué es una parábola?**: ¡No es solo una curva! Es el lugar geométrico donde cada uno de sus puntos está a la misma distancia de un punto "mágico" llamado **foco** ($F$) y de una línea recta llamada **directriz** ($D$).
> - **Mnemotecnia "Fui Volando"**: Para que nunca te pierdas en el plano, recuerda el orden **F - V - D** (Foco, Vértice, Directriz). El Vértice ($V$) es siempre el **punto medio**; está justo a la mitad del camino entre el foco y la directriz.
> - **El Parámetro ($p$)**: Es la distancia que hay del vértice al foco. ¡Ojo! Es la misma distancia que hay del vértice a la directriz.
> - **Lado Recto ($4p$)**: Es lo que determina qué tan "abierta" o "cerrada" se ve la parábola. Se calcula como cuatro veces el parámetro.

---

### 2. Fórmulas y definiciones importantes

¡Fíjate bien! Antes de tocar una fórmula, lo más importante es saber hacia dónde abre la "boquita" de la parábola.

| Término | Definición / Fórmula |
| :--- | :--- |
| **Vértice ($V$)** | El punto $(h, k)$. Es el "pico" o extremo de la curva. |
| **Foco ($F$)** | Punto de referencia situado siempre en el interior de la parábola. |
| **Directriz ($D$)** | Recta de referencia situada fuera de la parábola, perpendicular al eje de simetría. |
| **Parámetro ($p$)** | Distancia exacta desde $V$ hasta $F$ (o de $V$ a $D$). |
| **Lado Recto ($LR$)** | Ancho de la parábola en el foco. Fórmula: $|4p|$. |
| **Ecuación (Eje X)** | $(y - k)^2 = \pm 4p(x - h)$ *(Abre horizontal: derecha + / izquierda -)* |
| **Ecuación (Eje Y)** | $(x - h)^2 = \pm 4p(y - k)$ *(Abre vertical: arriba + / abajo -)* |

---

### 3. Ejemplos resueltos

```ad-example
title: Ejemplo A: El Caso Básico
**Datos:** $V(2, 4)$ y $F(1, 4)$

1. **Identificamos $h$ y $k$**: Del vértice $V(2, 4)$, tenemos $h = 2$ y $k = 4$.
2. **Calculamos $p$**: La distancia entre la $x$ del vértice (2) y la $x$ del foco (1) es **1**. Entonces, $p = 1$.
3. **¿Hacia dónde abre?**: ¡No te compliques! Si el foco (1) está a la izquierda del vértice (2), la parábola abre hacia la **izquierda**. Esto significa que usaremos el signo **negativo** en el eje X.
4. **Sustituimos**: 
   $(y - 4)^2 = -4(1)(x - 2)$
   **Resultado final:** $(y - 4)^2 = -4(x - 2)$
```

```ad-example
title: Ejemplo B: Aplicación en Antenas Satelitales
**Contexto**: En las telecomunicaciones, encontrar el valor exacto de $p$ es vital para que la señal de la antena no se pierda. Si el foco está mal ubicado, ¡no hay internet!
**Datos**: $V(0, 3/2)$ y $F(0, 1)$. El costo de ajuste es de $10 USD por cada unidad de $p$.

1. **Cálculo de $p$**: No te asustes con las fracciones. Restamos las coordenadas diferentes ($y$): $1.5 - 1 = 0.5$ (o $1/2$). El parámetro $p$ es **1/2**.
2. **Orientación**: Como el foco ($y=1$) está por debajo del vértice ($y=1.5$), la parábola abre hacia **abajo** (negativo en Y).
3. **Ecuación**: $(x - 0)^2 = -4(1/2)(y - 3/2) \Rightarrow \mathbf{x^2 = -2(y - 1.5)}$.
4. **Costo de precisión**: Si cada unidad de $p$ cuesta $10 USD:
   $0.5 \times 10 USD = \mathbf{5 USD}$ es el costo del ajuste técnico.
```

---

### 4. Ejercicios de repaso

```ad-abstract
title: 🟢 Bloque Fácil (Para calentar motores)
1. Hallar el valor de $p$ si el vértice es $V(3, 1)$ y el foco es $F(1, 1)$.
2. Si $V$ está en $(0, -1)$ y $F$ está en $(0, 1)$, ¿hacia qué dirección abre la parábola?
```

```ad-abstract
title: 🟡 Bloque Medio (¡Tú puedes!)
1. Encuentra la ecuación canónica con $V(-2, 2)$ y $F(-1, 2)$.
2. Imagina el plano y dime la ecuación si $V(-2, 1)$ y $F(-2, -1)$.
```

```ad-abstract
title: 🔴 Bloque Avanzado: El Desafío del Arquitecto
Un arquitecto diseña un arco para un puente con $V(2, -2)$ y $F(2, -1.5)$. El cable de refuerzo se colocará exactamente en el **lado recto**. Si el metro de cable cuesta $1.50 USD:
1. Calcula la longitud del lado recto ($LR$).
2. Calcula el costo total de los cables para esa sección del arco.
```

---

### 5. 💡 Consejo de estudio

> [!tip] **Visualiza antes de calcular**
> ¡Regla de oro! Antes de escribir cualquier fórmula, dibuja un pequeño plano cartesiano y ubica el Vértice y el Foco. La parábola siempre "abraza" al foco. 
> 
> Usa la técnica **"Fui Volando" (F-V-D)** como un movimiento físico: si empiezas en el Foco y pasas volando por el Vértice, seguirás en línea recta hasta aterrizar en la Directriz. Esto te ayudará a verificar que el signo de tu ecuación y la posición de tu directriz sean correctos. ¡Si lo dibujas, no te equivocas!