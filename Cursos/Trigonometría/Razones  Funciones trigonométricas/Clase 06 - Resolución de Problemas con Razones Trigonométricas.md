# Clase 06 — Resolución de Problemas con Razones Trigonométricas

#algebra #trigonometria
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 6 de 12

> [!info] 🧭 Navegación
> ◀ **Anterior:** [[Clase 05 - Razones Trigonométricas en Triángulos Rectángulos]]
> ▶ **Siguiente:** [[Clase 07 - Problemas de Varios Triángulos y Leyes de Senos/Cosenos]]

---

### 🌍 Relevancia y aplicaciones
¡Qué tal, amigos! Bienvenidos a una de las sesiones más útiles de la trigonometría. Hoy aprenderemos que estas fórmulas no son solo números, sino la llave para medir el mundo físico sin necesidad de tocarlo.

*   **💵 Aplicación $USD:** En arquitectura, un cálculo preciso de los ángulos mediante razones trigonométricas permite optimizar el uso de vigas y paneles. Al evitar el desperdicio de materiales con mediciones exactas, se pueden ahorrar miles de dólares en presupuestos de construcción a gran escala.
*   **🏗️ Aplicación práctica:** Los ingenieros civiles utilizan estas herramientas para determinar la estabilidad de grúas telescópicas o la inclinación segura de rampas y escaleras, garantizando que las estructuras soporten el peso necesario sin colapsar.
*   **📊 Situación cotidiana:** ¿Alguna vez has querido saber la altura de un edificio o de un árbol muy alto? No necesitas una cinta métrica gigante; basta con medir su sombra en el suelo y el ángulo del sol para obtener la altura exacta con una simple operación.

---

### 📌 ¿Qué son las Razones Trigonométricas?
> [!note] 📌 Definición sencilla
> Imagina un triángulo rectángulo (el que tiene una esquina en forma de "L"). Las razones trigonométricas son comparaciones entre sus lados. Dependiendo de qué lado dividas entre cuál, obtendrás un valor constante para cada ángulo.
> 
> ```text
>        /|
>       / |
>    H /  | O (Cateto Opuesto)
>     /   |
>    /θ___|
>      A (Cateto Adyacente)
> ```
> Las tres principales son: **Seno** ($sen$), **Coseno** ($cos$) y **Tangente** ($tan$).

> [!warning] ⚠️ Error común
> **¡Configura tu calculadora!** Antes de empezar, verifica que tu calculadora esté en modo **Grados** (aparecerá una **"D"** o **"DEG"** de *Degrees*). Si está en modo Radianes (RAD) o Gradianes (GRA), todos tus cálculos serán incorrectos. ¡Es el error más común, no dejes que te pase a ti!

> [!tip] 💡 Truco para recordarlo
> ¡Me alegra que estés practicando! Para no olvidar nunca las fórmulas, usa la mnemotecnia **SOH CAH TOA**:
> *   **SOH:** $Sen(\theta) = \frac{\text{Opuesto}}{\text{Hipotenusa}}$
> *   **CAH:** $Cos(\theta) = \frac{\text{Adyacente}}{\text{Hipotenusa}}$
> *   **TOA:** $Tan(\theta) = \frac{\text{Opuesto}}{\text{Adyacente}}$

---

### Procedimiento Paso a Paso

```text
PASO 1: Esbozar el diagrama. Dibuja la situación con líneas y puntos.
        Identifica el ángulo de elevación (mirar hacia arriba) 
        o de depresión (mirar hacia abajo desde la horizontal).
PASO 2: Identificar datos conocidos. Anota los valores de los catetos, 
        la hipotenusa o el ángulo θ que te da el problema.
PASO 3: Selección de la razón. Aplica SOH CAH TOA para elegir la 
        función que conecte tus datos con la incógnita.
PASO 4: Resolución técnica. Despeja la incógnita y usa la calculadora 
        en modo DEG para hallar el resultado final.
```

---

### Ejemplos Prácticos

#### Ejemplo 1: El Faro (Distancia horizontal)
Desde la cima de un faro de $7 \text{ m}$ de alto, se observa una lancha con un ángulo de depresión de $12^\circ$. ¿Cuál es la distancia entre la lancha y el pie del faro?
*   **Datos:** Cateto Opuesto (altura) = $7 \text{ m}$; Ángulo = $12^\circ$. Buscamos el Cateto Adyacente ($x$).
*   **Razón:** Tangente ($tan$).
*   **Cálculo:** $tan(12^\circ) = \frac{7}{x} \implies x = \frac{7}{tan(12^\circ)}$.
*   **Resultado:** $x \approx 32,93 \text{ metros}$.

#### Ejemplo 2: La Escalera (Hallar el ángulo)
Una escalera de $3 \text{ m}$ de largo está apoyada en una pared. Si su base está a $1,2 \text{ m}$ de la pared, ¿qué ángulo forma con el suelo?
*   **Datos:** Hipotenusa = $3 \text{ m}$; Cateto Adyacente = $1,2 \text{ m}$. Buscamos el ángulo ($\theta$).
*   **Razón:** Coseno ($cos$).
*   **Cálculo:** $cos(\theta) = \frac{1,2}{3}$. Aplicamos la función inversa: $\theta = cos^{-1}(0,4)$.
*   **Resultado:** $\theta \approx 66,42^\circ$.

#### Ejemplo 3: Persona y Torre (Altura total)
Una persona de $1,72 \text{ m}$ de altura está a $8 \text{ m}$ de una torre. Observa la punta con un ángulo de elevación de $61^\circ$. ¿Cuánto mide la torre?
*   **Datos del triángulo:** Cateto Adyacente = $8 \text{ m}$; Ángulo = $61^\circ$. Hallamos la altura parcial ($x$).
*   **Cálculo:** $tan(61^\circ) = \frac{x}{8} \implies x = 8 \cdot tan(61^\circ) \approx 14,43 \text{ m}$.
*   **Punto clave:** La altura de la torre es la suma de la altura visual más la de la persona: $14,43 \text{ m} + 1,72 \text{ m} = 16,15 \text{ m}$.
*   **Resultado:** La torre mide $16,15 \text{ m}$.

#### Ejemplo 4: Los Edificios ($USD)
Desde un edificio, Adriana observa otro edificio a $70 \text{ m}$ de distancia. El ángulo de elevación a la azotea es de $32^\circ$ y el de depresión a la base es de $41^\circ$.
*   **Parte inferior:** $70 \cdot tan(41^\circ) \approx 60,85 \text{ m}$.
*   **Parte superior:** $70 \cdot tan(32^\circ) \approx 43,74 \text{ m}$.
*   **Altura total:** $60,85 + 43,74 = 104,59 \text{ m}$.
*   **Presupuesto:** Si pintar cada metro lineal de altura cuesta $\$15 \text{ USD}$, el costo total es $104,59 \cdot 15 = \mathbf{\$1.568,85 \text{ USD}}$.

---

### ¡Es tu turno de brillar! Pon a prueba lo aprendido

> [!abstract] 🟢 Nivel Fácil
> Un avión de reconocimiento vuela a $2.300 \text{ m}$ de altura y localiza un barco con un ángulo de depresión de $28^\circ$. Calcula la **distancia directa (diagonal)** entre el avión y el barco enemigo.

> [!abstract] 🟡 Nivel Medio
> Una escalera de $3,2 \text{ m}$ se apoya en una pared a una altura de $2,5 \text{ m}$. ¿A qué **distancia de la pared** se encuentra la base de la escalera? (Usa el ángulo formado con el suelo para resolverlo mediante razones trigonométricas).

> [!abstract] 🔴 Nivel Avanzado ($USD)
> Desde una torre de control de $45 \text{ m}$ de altura, se observa un avión que vuela a $950 \text{ m}$ de altura total con un ángulo de elevación de $52^\circ$ desde la visual de la torre. 
> 1. Calcula la distancia directa (hipotenusa) entre la torre y el avión. 
> 2. Si se debe instalar un cable de comunicación que cuesta $\$2,5 \text{ USD}$ por metro, ¿cuál es el presupuesto total para el cable?

> [!success] ??? ✅ Respuestas
> *   **Fácil:** $4.899,12 \text{ m}$ (Hipotenusa).
> *   **Medio:** $1,99 \text{ m}$.
> *   **Avanzado:** Distancia = $1.148,46 \text{ m}$. Costo total = $\$2.871,15 \text{ USD}$.

---

### Mini-Prueba de Autoevaluación

> [!question] Pregunta 1
> Si observas un objeto que se encuentra por debajo de tu línea horizontal de visión, ¿qué ángulo estás utilizando?
> a) Elevación
> b) Depresión
> c) Ángulo Recto

> [!question] Pregunta 2
> ¿Qué razón trigonométrica debes elegir si conoces el **Cateto Opuesto** y necesitas hallar la **Hipotenusa**?
> a) Seno
> b) Coseno
> c) Tangente

> [!question] Pregunta 3
> Un poste de $10 \text{ m}$ proyecta una sombra de $10 \text{ m}$. Esto significa que el ángulo de elevación del sol es de $45^\circ$ (ya que $tan(\theta) = 10/10 = 1$). Si un técnico cobra $\$10 \text{ USD}$ por cada grado de inclinación medido para calibrar un panel solar, ¿cuánto es el cobro total?
> a) $\$45 \text{ USD}$
> b) $\$450 \text{ USD}$
> c) $\$100 \text{ USD}$

---

> [!tip] 💡 En la próxima clase
> ¡Excelente trabajo hoy! Ahora que dominas los problemas con un solo triángulo, en la siguiente clase aprenderemos a conectar varios para resolver estructuras complejas y exploraremos la **Ley de Senos y Cosenos** para cuando no tenemos ángulos rectos.

> [!info] 🧭 Navegación
> ◀ **Anterior:** [[Clase 05 - Razones Trigonométricas en Triángulos Rectángulos]]
> ▶ **Siguiente:** [[Clase 07 - Problemas de Varios Triángulos y Leyes de Senos/Cosenos]]