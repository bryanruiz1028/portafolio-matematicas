# Clase 02 — Reflection in the plane | Axial Symmetry + Reflection in the plane | Central Symmetry + Rotation in the Cartesian Plane + Homothecy | How to trace it

#algebra #reflectioninthe

> [!info] 🧭 Navegación
> *   **Anterior:** [[Clase 01]]
> *   **Principal:** [[Índice]]
> *   **Siguiente:** [[Clase 03]]

---

> [!info] 🌍 Relevancia y aplicaciones
> Las transformaciones geométricas son el lenguaje con el que el cerebro organiza el espacio. Nos permiten entender cómo los objetos se mueven, rotan o cambian de escala sin perder su identidad matemática.
> 
> *   💵 **Aplicación USD:** El símbolo del dólar ($) posee una simetría axial intrínseca en su diseño vertical. Además, cuando un diseñador escala un pequeño icono de precio para una valla publicitaria gigante, utiliza la **Homotecia** para asegurar que las proporciones del valor monetario no se distorsionen.
> *   🏗️ **Aplicación Práctica:** En arquitectura, la **Homotecia** (o semejanza) permite que los planos de una casa representen fielmente una construcción real, manteniendo los ángulos pero variando las distancias de forma proporcional.
> *   📊 **Situación Diaria:** Un espejo de baño realiza una simetría axial cada mañana, mientras que las manecillas de un reloj ejecutan rotaciones constantes alrededor de un centro fijo.

---

> [!note] 📌 Conceptos Clave para Básica Superior
> En geometría, dividimos las transformaciones en dos grandes familias:
> 
> 1.  **Transformaciones Isométricas:** (Del griego *iso*: igual, *metría*: medida). Son movimientos donde la figura **no cambia de tamaño ni forma**, solo de posición.
>     *   **Simetría Axial:** El "efecto espejo" respecto a una línea (eje).
>     *   **Simetría Central:** Reflejo respecto a un punto fijo. Equivale a dar media vuelta (180°).
>     *   **Rotación:** Girar como un planeta alrededor del sol (punto central) siguiendo un ángulo y sentido.
> 2.  **Transformación Isomórfica (Semejanza):**
>     *   **Homotecia:** "Cambio de tamaño". La figura conserva su forma (ángulos), pero sus dimensiones aumentan o disminuyen respecto a un centro, multiplicando las distancias por una razón ($r$).

> [!warning] ⚠️ Error común
> Muchos estudiantes confunden los signos al reflejar. Recuerda: en una reflexión sobre el eje **Y**, la figura salta horizontalmente, por lo que **solo cambia el signo de X**. En la **Simetría Central**, al ser una "vuelta total" respecto al origen, **ambos signos (x, y) deben invertirse**.

> [!tip] 💡 Trucos para recordar las reglas
> *   **Para Rotación 90°:** Usa el truco **"Intercambia y Voltea"**. Si tienes $(x, y)$, cambia de lugar los números a $(y, x)$ y luego cámbiale el signo al nuevo primer número: $(-y, x)$.
> *   **Para Simetría Central:** Es el **"Espejo Total"**. Todo cambia de bando: $(x, y) \to (-x, -y)$.

---

### PROCEDIMIENTO PASO A PASO: Cómo trazar una Homotecia

Para realizar una homotecia perfecta como un profesional (basado en el método de "Profe Alex"), sigue estos pasos:

```text
OBJETIVO: Trazar una Homotecia de una figura con razón r = 2
PASO 1: Identifica el Centro de Homotecia y traza líneas rectas que partan de él y pasen por cada vértice de la figura original.
PASO 2: Con una regla, mide la distancia exacta DESDE EL CENTRO hasta cada vértice (ej. Distancia Centro-A = 29 unidades).
PASO 3: Multiplica esa distancia por la razón (r). Si r = 2, calculamos 29 * 2 = 58 unidades.
PASO 4: Marca el nuevo punto (A') sobre la misma línea, midiendo siempre DESDE EL CENTRO la nueva distancia (58 unidades).
PASO 5: Une los nuevos puntos (A', B', C'...) en el mismo orden de la figura original.
PASO 6: VERIFICACIÓN: Comprueba que cada lado de la nueva figura sea PARALELO al lado correspondiente de la figura original. Si no son paralelos, hubo un error de medida.
```

---

### 5. EJEMPLOS PRÁCTICOS

> [!example] Ejemplo 1: Reflexión Axial sobre el Eje Y
> Reflejar el punto $A(3, 5)$.
> *   **Regla:** $(-x, y)$.
> *   **Proceso:** El valor de $x$ es $3$, su opuesto es $-3$. El valor de $y$ se mantiene.
> *   **Resultado:** $A'(-3, 5)$.

> [!example] Ejemplo 2: Simetría Central (Transformación Isométrica)
> Aplicar simetría central a $B(-2, -4)$ respecto al origen.
> *   **Regla:** $(-x, -y)$.
> *   **Proceso:** Cambiamos signos a ambos: $-2 \to 2$ y $-4 \to 4$.
> *   **Resultado:** $B'(2, 4)$.

> [!example] Ejemplo 3: Rotación de 90° (Sentido Antihorario)
> Rotar el punto $C(2, 5)$ respecto al origen.
> *   **Regla:** $(-y, x)$.
> *   **Proceso:** Intercambiamos $(5, 2)$ y volteamos el signo del primero: $(-5, 2)$.
> *   **Resultado:** $C'(-5, 2)$.

> [!example] Ejemplo 4: Homotecia y Diseño de Precio (USD)
> Una etiqueta de precio rectangular tiene un vértice en $(2, 2)$. Queremos ampliarla para un cartel con una razón $r=3$ desde el origen.
> *   **Cálculo:** Multiplicamos cada coordenada por $r$: $(2 \cdot 3, 2 \cdot 3)$.
> *   **Nueva Posición:** El vértice ahora estará en $(6, 6)$. Las dimensiones de la etiqueta también se habrán triplicado.

---

### 6. EJERCICIOS PARA EL ESTUDIANTE

> [!abstract] 🟢 Fácil: Simetría Axial
> Encuentra las coordenadas reflejadas sobre el **eje X** (Regla: mantiene $x$, cambia signo de $y$):
> 1. $A(4, 6)$
> 2. $B(-3, 2)$
> 3. $C(5, -5)$
> 4. $D(0, 3)$

> [!abstract] 🟡 Medio: Rotación y Simetría Central
> Determina la posición final usando el centro en el origen:
> 1. Aplica simetría central al punto $(5, 5)$.
> 2. Rota el punto $(6, 0)$ en 180°.
> 3. Rota el punto $(-3, 4)$ en 90° positivos.
> 4. Aplica simetría central al punto $(-1, -8)$.

> [!abstract] 🔴 Avanzado: Homotecia y Lógica Inversa
> 1. Un logo de USD en la posición $(4, 6)$ se escala por $r=0.5$. ¿Cuál es su nueva posición?
> 2. Si un billete se escala con $r=1.5$, ¿cuál es la nueva posición del punto $(10, 20)$?
> 3. Una figura se reduce de tamaño. El punto original es $(12, 8)$ y el transformado es $(3, 2)$. ¿Cuál es la razón $r$ de la homotecia?
> 4. **Lógica Inversa:** Un diseño gráfico en $(4, 8)$ termina en $(1, 2)$ tras una Homotecia. ¿Cuál es el valor de la razón $r$?

> [!success] Respuestas [R] para el docente
> **Fácil:** 1. (4, -6) | 2. (-3, -2) | 3. (5, 5) | 4. (0, -3).
> **Medio:** 1. (-5, -5) | 2. (-6, 0) | 3. (-4, -3) | 4. (1, 8).
> **Avanzado:** 1. (2, 3) | 2. (15, 30) | 3. $r = 0.25$ | 4. $r = 0.25$.

---

### 7. AUTOEVALUACIÓN (Mini-prueba)

> [!question] Pregunta 1
> Si aplicamos una simetría axial y luego una rotación, ¿cómo se clasifican estas transformaciones?
> A) Isomórficas, porque la figura cambia.
> B) Isométricas, porque la figura conserva su tamaño y forma.
> C) De escala, porque se alejan del origen.
> **Respuesta:** B. Ambas mantienen las medidas originales de la figura.

> [!question] Pregunta 2
> ¿Qué paso es fundamental para verificar que una Homotecia se trazó correctamente?
> A) Que la figura sea de distinto color.
> B) Que los lados de la figura imagen sean paralelos a los de la preimagen.
> C) Que la figura rote 90 grados.
> **Respuesta:** B. La verificación de paralelismo asegura que la transformación fue proporcional.

> [!question] Pregunta 3
> En una gráfica financiera, un icono de "$" en $(10, 10)$ se traslada a $(5, 5)$ mediante una homotecia. ¿Cuál fue la razón?
> A) $r = 2$ (Ampliación).
> B) $r = 0.5$ (Reducción).
> C) $r = -1$ (Inversión).
> **Respuesta:** B. Al dividir las coordenadas por la mitad, la razón es $0.5$, indicando una reducción.

---

> [!tip] 💡 En la próxima clase
> Exploraremos la **Traslación**, el movimiento más puro: deslizar figuras por el plano sin girarlas ni cambiar su tamaño.

> [!info] 🧭 Navegación
> *   **Anterior:** [[Clase 01]]
> *   **Principal:** [[Índice]]
> *   **Siguiente:** [[Clase 03]]

---