# Clase 07 — Ley de Senos y Cosenos: Resolución de Triángulos

#algebra #lawofsinesandco
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 7 de 9

> [!info] 🧭 Navegación
> ⬅️ [[Clase 06 - Ley de Senos]] | 🏠 [[00 - Índice del curso]] | ➡️ [[Clase 08 - Aplicaciones Avanzadas]]

---

> [!info] 🌍 Relevancia y aplicaciones
> ¡Bienvenido, explorador! Hoy aprenderás a dominar las "herramientas universales" de la trigonometría. A diferencia del Teorema de Pitágoras, que es como una llave que solo abre puertas cuadradas (triángulos rectángulos), las Leyes de Senos y Cosenos son llaves maestras para **cualquier tipo de triángulo**.
> 
> * **💵 $USD:** Vital para calcular perímetros de terrenos irregulares y determinar presupuestos exactos de cercado.
> * **🏗️ Práctica:** Indispensable en arquitectura para diseñar techos inclinados o puentes donde no existen ángulos de 90°.
> * **📊 Cotidiana:** Es la tecnología matemática detrás de tu GPS para calcular distancias entre tres puntos en el mapa.

---

> [!note] 📌 ¿Qué es Law of Sines and Cosines?
> Estas leyes son fórmulas que conectan los lados de un triángulo con los ángulos opuestos. Imagínalas como un "kit de rescate": cuando Pitágoras no puede ayudarte porque no hay un ángulo recto, estas leyes entran en acción para encontrar cualquier dato faltante. 
> 
> **El Secreto de la Transición:** Generalmente, usamos la Ley de Cosenos para "desbloquear" el triángulo y, una vez que tenemos una pareja completa (lado y ángulo opuesto), saltamos a la Ley de Senos porque es mucho más rápida de calcular.

> [!warning] ⚠️ Error común
> No intentes forzar la **Ley de Senos** si no tienes una "pareja completa" (un lado y su ángulo opuesto conocidos). Si los datos están "desconectados", como en los casos SAS o SSS, tu punto de partida obligatorio es la **Ley de Cosenos**.

> [!tip] 💡 Truco para recordarlo: La Regla del Sándwich
> ¿Cómo saber si usar Cosenos? Si ves un ángulo "atrapado" justo en medio de dos lados conocidos (Lado-Ángulo-Lado), tienes un **Sándwich**. Como el ángulo no tiene a su lado opuesto para formar una pareja, la Ley de Cosenos es la única herramienta que puede "abrir" el sándwich para hallar el lado que falta.

---

### 📥 Procedimiento Paso a Paso

Como Arquitectos de Contenido, seguiremos esta ruta lógica para no perdernos en el proceso:

```text
PASO 1 → Identificar datos: ¿Tengo una "pareja completa" (Lado y su Ángulo opuesto)?
PASO 2 → Elegir Ley: 
         - Si NO hay pareja: Empezar con Ley de Cosenos.
         - Tip de Experto: En casos de 3 lados (SSS), halla siempre el ÁNGULO MÁS GRANDE primero.
PASO 3 → Calcular: Usa la calculadora en modo grados (DEG). 
         ¡Ojo con el signo negativo en el denominador de la fórmula de cosenos!
PASO 4 → Completar: Halla el resto usando la suma de 180° o Ley de Senos para ganar velocidad.
```

---

### 📝 Ejemplos Guiados

#### Ejemplo 1: El Caso del Sándwich (SAS)
*Datos: Ángulo $A=112^\circ$, lado $b=7m$, lado $c=4m$.*

1.  **Paso 1: Vamos a descubrir el lado "a":** Como el ángulo $A$ está entre los lados $b$ y $c$, usamos Cosenos: $a^2 = 7^2 + 4^2 - 2(7)(4) \cos(112^\circ)$.
    *   **Resultado:** $a = 9.27m$.
2.  **Paso 2: Busquemos el ángulo $B$:** Ahora que tenemos la pareja completa ($a$ y $A$), usamos Senos por rapidez: $\frac{\text{sen}(B)}{7} = \frac{\text{sen}(112^\circ)}{9.27}$.
    *   **Resultado:** $B = 44.43^\circ$.
3.  **Paso 3: El cierre estratégico:** Usamos la regla de los $180^\circ$ para el ángulo $C$: $180^\circ - 112^\circ - 44.43^\circ = 23.57^\circ$.

#### Ejemplo 2: El Peligro del Signo Negativo (SSS)
*Datos: lado $a=7.5$, lado $b=11$, lado $c=5$.*

1.  **Estrategia:** El lado más largo es $b=11$, así que buscaremos el ángulo $B$ primero para evitar errores.
2.  **Zona de Riesgo:** Al despejar la fórmula: $\cos(B) = \frac{b^2 - a^2 - c^2}{-2ac}$. 
    *   Al sustituir: $\cos(B) = \frac{11^2 - 7.5^2 - 5^2}{-2(7.5)(5)}$. Es vital mantener el signo negativo en el denominador ($-75$).
    *   **Resultado:** $B = 122^\circ$.

#### Ejemplo 3: Evaluación Rápida (SSS)
*Datos: lado $a=25, b=21.5, c=30$.*

1.  Calculamos el ángulo $A$ con Ley de Cosenos $\rightarrow A = 55.14^\circ$.
2.  Calculamos el ángulo $B$ con Ley de Senos $\rightarrow B = 44.88^\circ$.
3.  El ángulo $C$ se obtiene por resta $\rightarrow 79.98^\circ$.

#### Ejemplo 4: Aplicación Presupuestaria 💵
*Datos: Ángulo $A=115^\circ$, lado $b=6cm$, lado $c=9cm$.*

*   **Problema:** Si un material de diseño cuesta $1.50 USD por cm lineal, ¿cuánto cuesta bordear esta pieza?
*   **Paso 1:** Hallar lado $a$ (Cosenos) $\rightarrow a = 12.75cm$.
*   **Paso 2:** Perímetro total $\rightarrow 6 + 9 + 12.75 = 27.75cm$.
*   **Paso 3:** Costo final $\rightarrow 27.75 \times 1.50 = 41.625$. Redondeando a formato financiero: **$41.63 USD**.

---

### ✏️ Ejercicios para el Estudiante

*   **🟢 Fácil:** Encuentra la longitud del lado $a$ si tienes $A=112^\circ, b=7, c=4$.
*   **🟡 Medio:** Resuelve el triángulo completo (todos los lados y ángulos) si $A=115^\circ, b=6, c=9$.
*   **🔴 Avanzado:** Tienes una pieza con lados $a=15, b=17, c=23$. Resuelve todos sus ángulos.
    *   **Reto Financiero:** Una máquina de corte láser cobra $5.00 USD por cada grado de rotación del **ángulo más pequeño**. ¿Cuál es el costo de ese ángulo?

> [!check] ✅ Respuestas de Verificación
> *   **Nivel Fácil:** $a = 9.27$.
> *   **Nivel Medio:** $a = 12.75$, $B = 25.25^\circ$, $C = 39.75^\circ$.
> *   **Nivel Avanzado:** Ángulos $A=30.47^\circ$, $B=45.92^\circ$, $C=103.61^\circ$. 
> *   **Resultado del Reto:** El ángulo más pequeño es $A$ ($30.47^\circ$). El costo es $30.47 \times 5 = \mathbf{152.35 USD}$.

---

### 🧠 Mini-Prueba de Autoevaluación

1.  **¿Cuándo es OBLIGATORIO empezar con la Ley de Cosenos?**
    *   En los casos SSS (tres lados conocidos) y SAS (dos lados y el ángulo que forman), porque no existe ninguna pareja lado-ángulo completa para usar Senos.
2.  **Si en el Ejemplo 1 ya conocemos dos ángulos ($112^\circ$ y $44.43^\circ$), ¿cuál es el método más rápido para el tercero?**
    *   Restar ambos de $180^\circ$, obteniendo $23.57^\circ$.
3.  **Adaptación $USD:** Si una cortadora industrial cobra $2.00 USD por cada grado de apertura de un ángulo que mide $35^\circ$, ¿cuál es el costo del servicio?
    *   $35 \times 2 = \mathbf{70.00 USD}$.

---

> [!tip] 💡 En la próxima clase
> ¡Excelente trabajo hoy! Ahora que sabes "desbloquear" cualquier triángulo, en la Clase 08 aplicaremos estos conocimientos para calcular **áreas y perímetros** en situaciones de ingeniería del mundo real.

> [!info] 🧭 Navegación
> ⬅️ [[Clase 06 - Ley de Senos]] | 🏠 [[00 - Índice del curso]] | ➡️ [[Clase 08 - Aplicaciones Avanzadas]]