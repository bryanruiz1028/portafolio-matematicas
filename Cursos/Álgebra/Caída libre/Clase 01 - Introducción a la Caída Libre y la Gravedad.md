# Clase 01 — Introducción a la Caída Libre y la Gravedad
tags: #fisica #caidalibreintrod #cinematica
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 4

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02 - Caída libre Identificación de datos y fórmulas|Clase 02 ➡]]

---

### 1. Relevancia y Aplicaciones: ¿Por qué importa esto?

Comprender la caída libre no es solo resolver ecuaciones; es entender cómo proteger lo que valoramos. En el mundo real, la aceleración de la gravedad determina si un objeto sobrevive a un impacto o se convierte en pérdida total.

> [!info] 🌍 Aplicaciones y Análisis de Riesgo
- 💵 **Evaluación de Daños (USD):** Imagina un smartphone de **$800 USD**. Si cae desde una altura considerable, la gravedad lo acelera constantemente. Si la velocidad de impacto supera un "umbral de daño", el costo de reparación será igual al valor del equipo.
- 🏗️ **Ingeniería de Seguridad:** El diseño de grúas y arneses depende de predecir la fuerza de impacto tras una caída accidental.
- 📊 **Logística con Drones:** Calcular la velocidad con la que un paquete llega al suelo es vital para decidir qué tipo de amortiguación necesita la mercancía.

---

### 2. Concepto Clave: ¿Qué es la Caída Libre?

La **caída libre** es el movimiento de un objeto cuando la **única** influencia que actúa sobre él es la gravedad. En nuestro día a día, el aire actúa como un freno (resistencia), pero en la física pura, ignoramos ese freno para entender la esencia del movimiento.

> [!note] 📌 Definición Pedagógica
> Según Galileo Galilei, en el vacío, todos los objetos caen con la misma aceleración. No importa si es un martillo pesado o una pluma ligera: ¡caen al mismo tiempo!

> [!tip] 🧠 El "Pro-Tip" de Einstein
> Aunque solemos decir que la gravedad es una "fuerza invisible", Einstein nos enseñó que en realidad es la **curvatura del espacio-tiempo** causada por la masa de la Tierra. ¡Es como si los objetos pesados hundieran una sábana elástica y las cosas rodaran hacia ese hundimiento!

> [!warning] ⚠️ Experimento en casa: El celular y la servilleta
> Si sueltas un celular y una servilleta extendida, el celular llega primero por la resistencia del aire. **Pero intenta esto:** Pon la servilleta **encima** del celular y suéltalos. Verás que caen exactamente al mismo tiempo porque el celular le "abre paso" a la servilleta, eliminando el aire de su camino.

---

### 3. La Gravedad: 10 vs 9.8 y la Lógica de Signos

La aceleración de la gravedad ($g$) en la Tierra es de aproximadamente $9.8 \text{ m/s}^2$. 

*   **Para precisión científica:** Usamos $9.8$.
*   **Para cálculos rápidos (o si tenemos "pereza"):** Usamos $10 \text{ m/s}^2$. Esto significa que cada segundo que pasa, el objeto aumenta su velocidad en $10 \text{ m/s}$.

#### 📏 Nota Pedagógica: ¿Positivo o Negativo?
Para que no te confundas con los signos, aplicaremos la lógica del Profe Alex:
1.  **Si el objeto solo cae:** Como todos los vectores (distancia, velocidad y gravedad) van hacia abajo, tratamos todo como **positivo** por conveniencia.
2.  **Si el objeto se lanza hacia arriba:** El objeto sube (positivo) pero la gravedad lo frena hacia abajo (negativa). Aquí la gravedad **resta** velocidad cada segundo.

---

### 4. Procedimiento Paso a Paso (Cálculo de Velocidad Final)

Para calcular la velocidad final ($v_f$) a partir de una velocidad inicial ($v_i$):

1.  **Identificar $v_i$:** Si el problema dice "se deja caer" o "se suelta", $v_i = 0$.
2.  **Determinar el tiempo ($t$):** ¿Cuántos segundos dura la caída?
3.  **Elegir la precisión de $g$:** $10$ para estimación, $9.8$ para exactitud.
4.  **Calcular:** Multiplica el tiempo por la gravedad y súmalo (si cae) o réstalo (si sube) a la velocidad inicial.

---

### 5. Ejemplos Prácticos

> [!example] Ejemplo 1: El objeto soltado (Estimación rápida)
> Se deja caer una pelota y tarda 3 segundos en impactar. ¿Velocidad final?
> - **Lógica:** $v_i = 0$. Cada segundo gana $10 \text{ m/s}$.
> - **Cálculo:** $10 \times 3 = \mathbf{30 \text{ m/s}}$.

> [!example] Ejemplo 2: Lanzamiento vertical (Signos)
> Lanzas una piedra hacia arriba a $40 \text{ m/s}$. ¿Cuánto tarda en llegar al punto más alto?
> - **Lógica:** La gravedad ($g = -10$) quita $10 \text{ m/s}$ cada segundo.
> - **Proceso:** Seg 1: $30$ | Seg 2: $20$ | Seg 3: $10$ | Seg 4: $0$.
> - **Resultado:** Tarda **4 segundos** en detenerse (punto más alto).

> [!example] Ejemplo 3: Cálculo de Altura ($y$)
> Un objeto cae por 2 segundos ($g = 9.8$). ¿Desde qué altura cayó?
> - **Fórmula:** $y = \frac{g \cdot t^2}{2}$ (Usamos $y$ porque es el eje vertical).
> - **Cálculo:** $y = \frac{9.8 \cdot 2^2}{2} = \frac{9.8 \cdot 4}{2} = 9.8 \cdot 2 = \mathbf{19.6 \text{ m}}$.

> [!example] Ejemplo 4 (Riesgo USD): Umbral de Daño
> Un sensor de precisión de **$150 USD** tiene un **umbral de daño** de $40 \text{ m/s}$ (si impacta más rápido, se rompe). Si cae desde un dron y tarda 5 segundos en llegar al suelo ($g=10$):
> 1. **Velocidad de impacto:** $10 \cdot 5 = 50 \text{ m/s}$.
> 2. **Resultado:** Como $50 \text{ m/s} > 40 \text{ m/s}$, el sensor se destruye y se pierden los **$150 USD**.

---

### 6. Ejercicios para el Estudiante

> [!abstract] Ejercicios de Aplicación
> 🟢 **Nivel Verde:** Dejas caer una moneda desde un puente y tarda 2.5 segundos en tocar el agua. ¿Cuál es su velocidad final usando $g = 10$?
> 
> 🟡 **Nivel Amarillo:** Un objeto se suelta desde un edificio y tarda 4 segundos en caer. Calcula la altura exacta ($y$) usando la gravedad precisa de $9.8 \text{ m/s}^2$.
> 
> 🔴 **Nivel Rojo (Análisis USD):** Una empresa compra un sensor de velocidad de **$50 USD** que solo se activa si alcanza los **25 m/s**. Si lo dejamos caer para probarlo, ¿cuántos segundos debe caer como mínimo para que la inversión de $50 USD valga la pena y el sensor se active? ($g=10$).

> [!success] Soluciones
> 1. $25 \text{ m/s}$.
> 2. $78.4$ metros.
> 3. $2.5$ segundos.

---

### 7. Mini-prueba de Autoevaluación

> [!question] 1. Si realizamos el experimento del Apolo 15 (martillo y pluma) en la Luna:
> - **A)** El martillo cae primero porque la gravedad de la Luna es débil.
> - **B)** Ambos caen al mismo tiempo porque no hay resistencia del aire.
> - **C)** La pluma flota eternamente.

> [!question] 2. Un objeto se deja caer y alcanza una velocidad de $30 \text{ m/s}$ ($g=10$). ¿Cuál fue su tiempo de caída?
> - **A)** 3 segundos.
> - **B)** 30 segundos.
> - **C)** 1 segundo.

> [!question] 3. En una simulación de riesgo, cada metro de altura aumenta el costo de seguro en **$5 USD**. Si un objeto cae durante 2 segundos ($g=10$):
> - **A)** Altura $10 \text{ m} \to$ Seguro: $\$50 USD$.
> - **B)** Altura $20 \text{ m} \to$ Seguro: $\$100 USD$.
> - **C)** Altura $5 \text{ m} \to$ Seguro: $\$25 USD$.

---

### 8. Cierre y Próximo Tema

> [!tip] 💡 Conexión con el movimiento acelerado
> La caída libre es simplemente un caso especial de **Movimiento Uniformemente Acelerado**. En la próxima clase, aprenderemos a combinar las 3 fórmulas principales para resolver cualquier problema, sin importar qué datos nos den.

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02 - Caída libre Identificación de datos y fórmulas|Clase 02 ➡]]