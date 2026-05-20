# Clase 06 — Multiplicación por Escalar y Ángulo entre Vectores

#algebra #vectores

`[[Clase 05]] | [[Índice]] | [[Fin del curso]]`

---

### 1. RELEVANCIA Y APLICACIONES

> [!info] 🌍 Relevancia y aplicaciones
> Multiplicar un vector por un escalar nos permite ajustar su magnitud, ya sea para aumentar o reducir su alcance. Es la herramienta clave en física para duplicar una fuerza o ajustar velocidades sin perder el rumbo.
> 
> **Aplicación $USD:** Imagina un "vector de precios" unitarios para productos básicos: $\vec{p} = (10, 20)$ dólares. Si una empresa triplica su pedido (escalar $k=3$), el nuevo vector resultante $(30, 60)$ nos indica el presupuesto total necesario para cada rubro.
> 
> **Ingeniería y Videojuegos:** Se usa para alargar la trayectoria de un proyectil o escalar el tamaño de un objeto manteniendo su proporción.
> 
> **Situación Cotidiana:** El "zoom" de los mapas digitales (GPS) escala todas las distancias representadas para que puedas ver más territorio o más detalle.

---

### 2. CONCEPTOS CLAVE

> [!note] 📏 ¿Qué es multiplicar por un escalar?
> Es la operación de "estirar" o "encoger" una flecha (vector) usando un número (escalar). 
> - Si $k > 1$, el vector crece (se alarga).
> - Si $0 < k < 1$, el vector se reduce (se encoge).
> - Si $k = 1$, el vector permanece igual (identidad).
> - Si $k = 0$, el vector se anula (se convierte en un punto).

> [!warning] ⚠️ El efecto del signo negativo
> Multiplicar por un número negativo **cambia el sentido** (hacia dónde apunta la punta de la flecha) pero **no cambia la dirección** (la inclinación de la línea). Según el Profe Alex, el vector sigue "viviendo" en la misma línea recta, pero gira $180^\circ$.
> - **En coordenadas geográficas:** El negativo "voltea" los puntos cardinales (Norte $\leftrightarrow$ Sur, Este $\leftrightarrow$ Oeste).

> [!tip] 💡 Truco para recordarlo
> Piensa en el escalar como el botón de **zoom** de una cámara: el número es el nivel de aumento. Si el número es negativo, es como si giraras la cámara para mirar exactamente hacia atrás en la misma calle.

---

### 3. PROCEDIMIENTO PASO A PASO

```text
PARA MULTIPLICAR UN VECTOR POR UN ESCALAR (k):
1. Forma de Componentes: Multiplica 'k' por la componente 'x' y luego por la 'y'.
   Resultado: (k * x, k * y).
2. Forma Geográfica: Multiplica el valor absoluto de 'k' por la magnitud.
   * Si k es negativo: Cambia los puntos cardinales a sus opuestos (N->S, E->O).

PARA CALCULAR EL ÁNGULO ENTRE DOS VECTORES (A y B):
Paso 1: Hallar el Producto Punto (Ax*Bx + Ay*By).
Paso 2: Calcular magnitudes de A y B (Raíz de la suma de cuadrados).
       *Profe Alex recomienda: Deja el resultado como raíz para máxima precisión.
Paso 3: Sustituir en la fórmula: Cos(θ) = (Producto Punto) / (|A| * |B|).
Paso 4: Despejar el ángulo: θ = cos⁻¹ (resultado anterior).
       *Nota: Configura tu calculadora en modo 'DEG' (grados).
```

---

### 4. EJEMPLOS PRÁCTICOS

> [!example] Ejemplo 1: Caso Básico (Video 3)
> Multiplicar el vector $\vec{a} = (3, 2)$ por el escalar $k = 2$.
> - **Operación:** $2 \cdot (3, 2) = (2 \cdot 3, 2 \cdot 2)$
> - **Resultado:** $(6, 4)$
> *Interpretación:* El vector se alargó al doble manteniendo su inclinación y sentido.

> [!example] Ejemplo 2: Escalar Negativo y Cuadrantes (Video 4)
> Multiplicar el vector $\vec{a} = (-2, 1)$ por el escalar $k = -3$.
> - **Operación:** $-3 \cdot (-2, 1) = (6, -3)$
> - **Visualización:** El vector original estaba en el **Cuadrante II** (Izquierda, Arriba). Al multiplicarlo por $-3$, el resultado $(6, -3)$ ahora está en el **Cuadrante IV** (Derecha, Abajo). ¡Se invirtió totalmente!

> [!example] Ejemplo 3: Ángulo entre Vectores (Video 1)
> Hallar el ángulo entre $\vec{a} = (5, 2)$ y $\vec{b} = (3, 6)$.
> 1. **Producto Punto:** $(5\cdot3) + (2\cdot6) = 15 + 12 = \mathbf{27}$.
> 2. **Magnitudes:** 
>    - $|\vec{a}| = \sqrt{5^2 + 2^2} = \sqrt{29}$
>    - $|\vec{b}| = \sqrt{3^2 + 6^2} = \sqrt{45}$
> 3. **Coseno:** $\cos(\theta) = \frac{27}{\sqrt{29} \cdot \sqrt{45}} \approx 0.74741$
> 4. **Ángulo Final:** $\theta = \cos^{-1}(0.74741) = \mathbf{41.63^\circ}$

> [!example] Ejemplo 4: Coordenadas Geográficas (Video 4)
> Escalar el vector $\vec{b} = 3\text{ m, Sur } 30^\circ \text{ Oeste}$ por $k = -2$.
> 1. Multiplicamos magnitud: $2 \cdot 3 = 6\text{ m}$.
> 2. Aplicamos el negativo: Sur pasa a **Norte** y Oeste pasa a **Este**.
> - **Resultado:** $6\text{ m, Norte } 30^\circ \text{ Este}$.

---

### 5. EJERCICIOS PARA EL ESTUDIANTE

> [!abstract] Actividades de Práctica
> **Verde (Fácil):**
> 1. $3 \cdot (1, 4)$
> 2. $2 \cdot (5, -2)$
> 3. $5 \cdot \vec{v}$ donde $\vec{v} = 12\text{ m, Norte}$.
> 4. $10 \cdot (-1, 2)$
> 
> **Amarillo (Medio):**
> 1. $-2 \cdot (3, 4)$. Calcula también la magnitud del resultado.
> 2. $-5 \cdot (-2, -1)$. Aproxima la magnitud final a dos decimales.
> 3. Calcula el ángulo entre $\vec{u} = (1, 0)$ y $\vec{v} = (0, 1)$.
> 4. Halla el ángulo entre $\vec{m} = (-3, 7)$ y $\vec{n} = (-5, -2)$.
> 
> **Rojo (Avanzado):**
> 1. **Dron en Viento:** Un dron se desplaza según $\vec{d} = (2, 5)$. Si una ráfaga de viento duplica su velocidad pero invierte su sentido ($k = -2$), ¿cuál es su nuevo vector de desplazamiento?
> 2. **Presupuesto $USD:** El vector de costo de materiales es $\vec{c} = (100, 200)$ USD. Si debido a una crisis el costo se escala por $k = 1.5$, ¿cuál es el nuevo vector de inversión?
> 3. **Diseño Arquitectónico:** Un arquitecto diseña dos vigas representadas por vectores cuyo producto punto es $0$. ¿Qué ángulo forman estas vigas y cómo se le llama técnicamente a esa relación?
> 4. **Ruta de Entrega:** Un mensajero tiene un vector de ruta $\vec{r} = 40\text{ km, Sur } 20^\circ \text{ Este}$. Si debe realizar la ruta de regreso exacta pero al triple de distancia ($k = -3$), ¿cuál es su nuevo vector?

> [!success] Respuestas (Docente)
> **Verde:** 1. (3, 12); 2. (10, -4); 3. 60 m, Norte; 4. (-10, 20).
> **Amarillo:** 1. (-6, -8), Mag=10; 2. (10, 5), Mag=$\sqrt{125} \approx 11.18$; 3. $90^\circ$; 4. $88.6^\circ$.
> **Rojo:** 1. (-4, -10); 2. (150, 300) USD; 3. $90^\circ$, son perpendiculares; 4. $120\text{ km, Norte } 20^\circ \text{ Oeste}$.

---

### 6. MINI-PRUEBA DE AUTOEVALUACIÓN

> [!question] Autoevaluación rápida
> 1. **¿Qué le sucede a la dirección y al sentido de un vector al multiplicarlo por $-1$?**
>    - *Respuesta:* La dirección (inclinación) se mantiene igual, pero el sentido se invierte $180^\circ$.
> 2. **Si el producto punto de dos vectores es cero, ¿qué podemos afirmar sobre ellos?**
>    - *Respuesta:* Que son perpendiculares y forman un ángulo de exactamente $90^\circ$.
> 3. **Si escalamos un vector de precios $\vec{p} = (5, 8)$ USD por un factor $k=100$, ¿cuál es el costo resultante?**
>    - *Respuesta:* (500, 800) USD.

---

### 7. CIERRE Y PRÓXIMO TEMA

> [!tip] 💡 En la próxima clase
> Ahora que sabemos estirar y encoger vectores, aprenderemos a combinarlos mediante la **Suma de Vectores en 3D**. Veremos cómo estas operaciones simples permiten crear las trayectorias de los aviones y los movimientos de personajes en el espacio tridimensional.

`[[Clase 05]] | [[Índice]] | [[Fin del curso]]`