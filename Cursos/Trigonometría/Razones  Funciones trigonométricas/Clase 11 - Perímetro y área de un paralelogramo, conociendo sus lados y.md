# Perímetro y área de un paralelogramo, conociendo sus lados y el ángulo interno

---
**Curso:** Geometría y Trigonometría  
**Etiquetas:** #algebra #perimeterandarea  
**Nivel:** Secundaria (12-15 años)

---

> [!info] 🧭 Navegación
> ⬅️ [[Clase 10]] | 🏠 [[Índice]] | [[Clase 12]] ➡️

---

### ¿Por qué es importante esta clase?

En el mundo real, no todo son rectángulos perfectos. Los arquitectos y diseñadores a menudo trabajan con paralelogramos inclinados para crear estructuras modernas o para medir terrenos que no tienen esquinas de 90°.

*   Permite calcular con total precisión la superficie de cualquier figura de cuatro lados con lados opuestos paralelos, sin importar su inclinación.
*   **Aplicación en $USD:** Es fundamental para presupuestar materiales. Por ejemplo, calcular el costo de alfombrar una oficina con diseño de paralelogramo sabiendo que el metro cuadrado de alfombra cuesta $25.00 USD.
*   **Construcción y Arquitectura:** Se utiliza para determinar la cantidad de pintura necesaria para fachadas vanguardistas o el área de paneles solares dispuestos en ángulos específicos.
*   **Situación cotidiana:** Medir el área real de un jardín o un retazo de tela para un diseño de moda donde los cortes son oblicuos.

---

### Concepto Clave

Un paralelogramo tiene dos dimensiones principales: la base ($b$) y la altura ($h$). El problema surge cuando conocemos la medida de los lados, pero no la altura real (la distancia vertical). En estos casos, el lado inclinado no es la altura. Para resolverlo, trazamos una línea vertical desde un vértice para formar un **triángulo rectángulo**. 

En este triángulo, el lado inclinado del paralelogramo actúa como la **Hipotenusa**, y la altura ($h$) que buscamos es el **Cateto Opuesto** al ángulo interno dado. Por ello, utilizamos la razón trigonométrica **Seno** ($SOH$):
$$\sin(\theta) = \frac{\text{Cateto Opuesto}}{\text{Hipotenusa}} \rightarrow \sin(\theta) = \frac{h}{\text{lado}}$$

> [!warning] ⚠️ Error común
> Un error muy frecuente es multiplicar los dos lados adyacentes para hallar el área (lado $\cdot$ lado). **¡Esto es incorrecto!** Esa operación solo funciona en rectángulos. En un paralelogramo inclinado, siempre debes hallar la altura ($h$) primero.

> [!tip] 💡 Truco para recordarlo
> Utiliza la regla: **"La altura es el opuesto"**. Como la altura es el cateto opuesto al ángulo, siempre se "estira" usando el **Seno**. Imagina que el **Seno** es el hilo que endereza el lado inclinado para medir qué tan alto llega.

---

### Procedimiento paso a paso

```text
PASO 1: Identificar la base ($b$) y el lado inclinado que será nuestra hipotenusa.
PASO 2: Trazar la altura ($h$) desde un vértice superior hacia la base, formando un triángulo rectángulo interno.
PASO 3: Calcular la altura usando la función Seno: $h = \text{lado inclinado} \cdot \sin(\text{ángulo})$.
PASO 4: Calcular el Área ($A = b \cdot h$) y el Perímetro ($P = 2 \cdot (\text{base} + \text{lado})$).
```

---

### Ejemplos Prácticos

> [!example] Ejemplo 1: Cálculo Básico
> **Datos:** Base ($b$) = 10.00 m, Lado inclinado = 7.00 m, Ángulo = 60°.
> 1. **Hallamos la altura ($h$):**
>    $h = 7.00 \cdot \sin(60°) \approx 6.06 \text{ m}$
> 2. **Calculamos el área ($A$):**
>    $A = 10.00 \cdot 6.06 = 60.60 \text{ m}^2$
> 3. **Calculamos el perímetro ($P$):**
>    $P = 10.00 + 10.00 + 7.00 + 7.00 = 34.00 \text{ m}$

> [!example] Ejemplo 2: Detalles Técnicos (Configuración)
> **Datos:** Base ($b$) = 14.00 cm, Lado inclinado = 9.00 cm, Ángulo = 56°.
> *   **Nota del Docente:** Verifica que tu calculadora esté en modo **DEG** o **D** (Grados).
> 1. **Altura ($h$):** $h = 9.00 \cdot \sin(56°) = 7.46 \text{ cm}$.
> 2. **Área ($A$):** $A = 14.00 \cdot 7.46 = 104.44 \text{ cm}^2$.
> 3. **Perímetro ($P$):** $P = 2 \cdot (14.00 + 9.00) = 46.00 \text{ cm}$.

> [!example] Ejemplo 3: Ángulo de 30° (Consistencia)
> **Datos:** Base ($b$) = 12.00 cm, Lado inclinado = 8.00 cm, Ángulo = 30°.
> 1. **Altura ($h$):** $h = 8.00 \cdot \sin(30°) = 4.00 \text{ cm}$ (el $\sin(30°)$ es exactamente 0.50).
> 2. **Área ($A$):** $A = 12.00 \cdot 4.00 = 48.00 \text{ cm}^2$.
> 3. **Perímetro ($P$):** $P = 2 \cdot (12.00 + 8.00) = 40.00 \text{ cm}$.

> [!example] Ejemplo 4: Aplicación económica ($USD)
> **Situación:** Un jardín tiene base de 15.00 m, lado de 10.00 m y un ángulo de 50°. El césped cuesta $12.50 USD por $m^2$.
> 1. **Altura ($h$):** $h = 10.00 \cdot \sin(50°) = 7.66 \text{ m}$.
> 2. **Área ($A$):** $A = 15.00 \cdot 7.66 = 114.90 \text{ m}^2$.
> 3. **Costo Total:** $114.90 \text{ m}^2 \cdot 12.50 \text{ USD} = \$1,436.25 \text{ USD}$.

---

### Ejercicios para el estudiante

> [!abstract] 🟢 Nivel Verde (Fácil)
> Calcula la altura ($h$) y el área ($A$) redondeando a dos decimales:
> 1. $b = 8.00 \text{ m}$, Lado $= 5.00 \text{ m}$, Ángulo $= 45°$.
> 2. $b = 10.00 \text{ cm}$, Lado $= 6.00 \text{ cm}$, Ángulo $= 60°$.
> 3. $b = 20.00 \text{ m}$, Lado $= 12.00 \text{ m}$, Ángulo $= 30°$.
> 4. $b = 15.00 \text{ cm}$, Lado $= 8.00 \text{ cm}$, Ángulo $= 70°$.

> [!abstract] 🟡 Nivel Amarillo (Medio)
> Calcula el perímetro ($P$) y el área ($A$) redondeando a dos decimales:
> 1. $b = 12.50 \text{ m}$, Lado $= 9.00 \text{ m}$, Ángulo $= 52°$.
> 2. $b = 18.00 \text{ cm}$, Lado $= 11.00 \text{ cm}$, Ángulo $= 40°$.
> 3. $b = 7.20 \text{ m}$, Lado $= 4.50 \text{ m}$, Ángulo $= 65°$.
> 4. $b = 25.00 \text{ cm}$, Lado $= 15.00 \text{ cm}$, Ángulo $= 35°$.

> [!abstract] 🔴 Nivel Rojo (Avanzado - $USD)
> 1. **Valla Publicitaria:** Base 6.00 m, Lado 4.00 m, Ángulo 75°. Pintura cuesta $18.00 USD por $m^2$. ¿Costo total?
> 2. **Terreno:** Base 40.00 m, Lado 30.00 m, Ángulo 55°. Cercar (Perímetro) cuesta $10.00 USD/m y sembrar (Área) cuesta $5.00 USD/m². Calcula ambos costos.
> 3. **Salón de Eventos:** Base 22.00 m, Lado 14.00 m, Ángulo 80°. Alfombrar cuesta $22.50 USD/m². ¿Presupuesto total?
> 4. **Panel Solar:** Base 2.00 m, Lado 1.50 m, Ángulo 60°. Fabricación cuesta $150.00 USD/m². ¿Costo unitario?

---

### Respuestas (para el docente)

| Nivel | Ejercicio | Altura ($h$) | Área ($A$) | Perímetro ($P$) | Resultado Especial / Costo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Verde** | 1 | 3.54 | 28.32 | - | - |
| | 2 | 5.20 | 52.00 | - | - |
| | 3 | 6.00 | 120.00 | - | - |
| | 4 | 7.52 | 112.80 | - | - |
| **Amarillo**| 1 | 7.09 | 88.63 | 43.00 | - |
| | 2 | 7.07 | 127.26 | 58.00 | - |
| | 3 | 4.08 | 29.38 | 23.40 | - |
| | 4 | 8.60 | 215.00 | 80.00 | - |
| **Rojo** | 1 | 3.86 | 23.16 | - | **$416.88 USD** |
| | 2 | 24.57 | 982.80 | 140.00 | **Cerca: $1,400 / Siembra: $4,914** |
| | 3 | 13.79 | 303.38 | - | **$6,826.05 USD** |
| | 4 | 1.30 | 2.60 | - | **$390.00 USD** |

---

### Mini-prueba de autoevaluación

> [!question] Pregunta 1
> ¿Cuál es la razón trigonométrica que relaciona la altura ($h$) y el lado inclinado en un paralelogramo?
> A) Coseno
> B) Tangente
> **C) Seno**

> [!question] Pregunta 2
> Si un paralelogramo tiene un lado inclinado de 20.00 cm y un ángulo de 30°, ¿cuál es su altura?
> **A) 10.00 cm**
> B) 17.32 cm
> C) 20.00 cm

> [!question] Pregunta 3
> Se desea pavimentar un patio de $50.00 \text{ m}^2$ (área ya calculada). Si el costo es de $20.00 USD por $m^2$, ¿cuál es el total?
> A) $100.00 USD
> **B) $1,000.00 USD**
> C) $10,000.00 USD

---

> [!tip] 💡 En la próxima clase
> Ahora que dominas el uso del Seno para hallar alturas y áreas en cuadriláteros, en la próxima sesión exploraremos cómo aplicar estos mismos principios para resolver áreas de polígonos regulares y la introducción a la Ley del Seno en triángulos.

> [!info] 🧭 Navegación
> ⬅️ [[Clase 10]] | 🏠 [[Índice]] | [[Clase 12]] ➡️