# 📖 Guía de estudio — Clase 03: Gráfica de una parábola a partir de su ecuación ordinaria

> [!info] 📌 Conceptos clave
> ¡Qué tal, amigos! Para que graficar parábolas sea pan comido, primero debemos entender qué nos dice la ecuación. Aquí tienes los puntos vitales:
> - **¡Truco rápido de identificación!:** Sabemos que es una parábola porque verás que una letra (la $x$ o la $y$) tiene el "cuadradito" ($^2$) y la otra no. ¡Así de simple!
> - **¿Hacia dónde abre?:** Mira la letra que **no** está al cuadrado y el signo del número que está afuera. 
> 	- Si la letra sola es la $y$: Abre hacia **arriba** (+) o hacia **abajo** (-).
> 	- Si la letra sola es la $x$: Abre hacia la **derecha** (+) o hacia la **izquierda** (-).
> - **El Vértice $(V)$:** Sacamos las coordenadas $(h, k)$ de los números junto a $x$ e $y$, pero ¡ojo!, siempre **cambiándoles el signo**. 
> - **La regla del cero:** Si una variable está sola (como $x^2$ o $y^2$), significa que su coordenada en el vértice es **0**. Por ejemplo, en $x^2$, la $h = 0$.
> - **El Parámetro $(p)$:** Es la distancia mágica. Es la separación entre el vértice y el foco, y también entre el vértice y la directriz. **Recuerda: $p$ siempre es una distancia positiva.**
> - **El Eje de Simetría:** Es la línea invisible que parte la parábola en dos partes igualitas. Pasa justo por el vértice y el foco.

---

### 📏 Fórmulas y Definiciones Importantes

| Elemento | Definición / Cálculo | Función en la Gráfica |
| :--- | :--- | :--- |
| **Vértice $(V)$** | $(h, k)$ con signos cambiados. Si no hay número, es $0$. | Es el punto de partida donde nace la curva. |
| **Lado Recto ($4p$)** | Es el número total que está fuera del paréntesis. | Indica el ancho total de la parábola a la altura del foco. |
| **Parámetro $(p)$** | Se calcula dividiendo: $p = \frac{\text{Número externo}}{4}$. | Nos dice cuántos pasos caminar para hallar el foco y la directriz. |
| **Foco $(F)$** | Punto ubicado a distancia $p$ del vértice. | Siempre vive "dentro" de la barriga de la parábola. |
| **Directriz** | Recta perpendicular al eje de simetría a distancia $p$. | Es la línea de referencia que queda "a las espaldas" de la curva. |
| **Eje de Simetría** | Recta que pasa por $V$ y $F$. | Divide la parábola a la mitad (su ecuación es $x=h$ o $y=k$). |

---

### 📝 Ejemplos Resueltos al estilo "Profe Alex"

> [!example] Ejemplo A: Caso Vertical
> **Ecuación:** $(x - 3)^2 = 4(y - 2)$
> 
> 1. **Vértice:** Cambiamos signos. $V = (3, 2)$.
> 2. **Apertura:** La letra lineal es $y$ y el 4 es positivo. ¡Abre hacia **arriba**!
> 3. **Cálculo de $p$:** Sabemos que $4p = 4$. Entonces $p = 4 / 4$, lo que nos da **$p = 1$**.
> 4. **Eje de Simetría:** Como abre hacia arriba, el eje es vertical y pasa por $x=3$.
> 5. **Ubicación de puntos (Usando la distancia $p$):** 
>    - **Foco:** Caminamos 1 unidad hacia arriba desde el vértice: $F = (3, 2 + 1) = (3, 3)$.
>    - **Directriz:** Caminamos 1 unidad hacia abajo del vértice: $y = 2 - 1 \implies y = 1$.
>    - **Lado Recto:** Mide 4. Desde el foco, marcamos 2 unidades a la izquierda y 2 a la derecha para saber por dónde pasar el trazo.

> [!example] Ejemplo B: Caso Horizontal (Diseño de Reflector)
> **Contexto:** Un ingeniero diseña un reflector usando la ecuación: $(y - 2)^2 = 8(x + 3)$.
> 
> 1. **Vértice:** Cambiamos signos de los acompañantes. $V = (-3, 2)$.
> 2. **Apertura:** La letra lineal es $x$ y el 8 es positivo. Abre hacia la **derecha**.
> 3. **Cálculo de $p$:** Si $4p = 8$, entonces $p = 8 / 4$, así que **$p = 2$**.
> 4. **Eje de Simetría:** Es la línea horizontal que pasa por $y = 2$.
> 5. **Ubicación de puntos:**
>    - **Foco:** Contamos 2 unidades a la derecha del vértice: $F = (-3 + 2, 2) = (-1, 2)$.
>    - **Directriz:** Contamos 2 unidades a la izquierda del vértice: $x = -3 - 2 \implies x = -5$.
>    - **Lado Recto:** Mide 8. Desde el foco, contamos 4 unidades hacia arriba y 4 hacia abajo.

---

### ✏️ Ejercicios de Repaso

> [!abstract] ¡A practicar!
> 
> **Nivel Fácil (🟢)**
> *Identifica el vértice, la dirección de apertura y el eje de simetría:*
> 1. $(x + 4)^2 = 12(y - 1)$
> 2. $(y - 5)^2 = 16(x + 2)$
> 3. $(x - 2)^2 = -4(y + 3)$
> 
> **Nivel Medio (🟡)**
> *Calcula el parámetro $p$, las coordenadas del foco y la ecuación de la directriz:*
> 4. $(y + 1)^2 = -8(x - 4)$
> 5. $(x - 1)^2 = 20(y + 2)$
> 6. $(y - 3)^2 = 4(x - 1)$
> 
> **Nivel Avanzado (🔴)**
> *Reto de precisión para infraestructura:*
> 7. Grafica la parábola $x^2 = -1(y + 3)$. Determina el foco y la directriz. 
> 
> > [!tip] **Pista de precisión (Scaffolding)**
> > - Recuerda que al no haber número con la $x$, su coordenada es $0$.
> > - Como el número externo es 1, tu parámetro será $p = 1/4$ (o $0.25$). 
> > - **Truco:** Para graficar esto, divide el cuadrito de tu cuaderno en 4 partes pequeñas. ¡Así ubicarás el foco a un solo "cuartito" de distancia con total exactitud!

---

> [!tip] 💡 Consejo de estudio: El "Dibujo Feo" o Auxiliar
> Antes de pasar al plano cartesiano limpio, haz un **boceto rápido a mano alzada**. No tiene que ser bonito, solo dibuja un puntito para el vértice y una curva hacia donde indique la letra lineal.
> 
> Este "dibujo feo" es tu brújula: te dirá visualmente si para hallar el foco debes **sumar o restar** las unidades de $p$. ¡Es la mejor forma de no equivocarse con los signos negativos!