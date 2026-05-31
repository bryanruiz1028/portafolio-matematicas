# Clase 04 — Razones trigonométricas: Cálculo de lados, ángulos y aplicaciones complejas

> [!info] 🧭 Navegación
> [[Clase 03 — Introducción a la Trigonometría]] | [[Índice de Contenidos]] | [[Clase 05 — Resolución completa de triángulos]]

---

> [!info] 🌍 Relevancia y aplicaciones
> El dominio de las razones trigonométricas permite transformar ángulos en medidas físicas reales, una habilidad fundamental en diversos campos técnicos:
> - 🏗️ **Topografía y Construcción:** Determinación exacta de la longitud de vigas de soporte o la inclinación de rampas sin necesidad de medirlas manualmente en estructuras peligrosas.
> - 📊 **Navegación y Distancias:** Cálculo de rutas directas mediante la triangulación de posiciones entre dos puntos fijos.
> - 💵 **Gestión Financiera de Proyectos:** Estimación precisa del costo de materiales (como acero, cableado o tubería) al multiplicar la longitud calculada por el precio unitario en USD, evitando el desperdicio de presupuesto.

---

> [!note] 📌 ¿Qué son las Razones trigonométricas?
> Son herramientas matemáticas que establecen una relación fija entre los ángulos de un triángulo rectángulo y la medida de sus lados. Para un estudiante, esto significa que si conoces un ángulo y al menos un lado, puedes "descubrir" mágicamente cuánto miden todos los demás componentes del triángulo.

> [!warning] ⚠️ Error común y Regla de Oro
> 1. **Modo de la calculadora:** Verifica que en la pantalla aparezca una **D** o **DEG** (Degrees). Si ves una **R** (Radianes), tus cálculos fallarán.
> 2. **Identificación de catetos:** El cateto **opuesto** siempre está frente al ángulo; el **adyacente** está "pegado" a él.
> 3. **El "Intercambio" Algebraico:** Si la incógnita $x$ está en el denominador (abajo), como en $\cos(A) = \frac{b}{x}$, la $x$ y la función trigonométrica simplemente **intercambian lugares**: $x = \frac{b}{\cos(A)}$. ¡No multipliques directamente si la $x$ está abajo!

> [!tip] 💡 Truco para recordarlo
> Memoriza la palabra **SOH-CAH-TOA**:
> - **SOH:** $\sin(\theta) = \frac{\text{Opuesto}}{\text{Hipotenusa}}$
> - **CAH:** $\cos(\theta) = \frac{\text{Adyacente}}{\text{Hipotenusa}}$
> - **TOA:** $\tan(\theta) = \frac{\text{Opuesto}}{\text{Adyacente}}$

---

### Procedimiento técnico para la resolución

```text
1. Identificar el triángulo rectángulo (debe poseer un ángulo de 90°).
2. Nombrar los lados (Hipotenusa, Opuesto, Adyacente) respecto al ángulo de referencia.
3. Seleccionar la fórmula (SOH-CAH-TOA) comparando los datos conocidos ("lo que tengo") con la incógnita ("lo que busco").
4. Despejar la variable y realizar el cálculo utilizando la calculadora científica.
```

---

### Ejemplos Resueltos

> [!example] Ejemplo 1: Cálculo de lado (Incógnita en el numerador)
> **Datos:** Ángulo $= 32^\circ$, Hipotenusa $= 10\text{m}$. Hallar Cateto Opuesto ($x$).
> 1. **Fórmula:** Tenemos Hipotenusa y buscamos Opuesto $\rightarrow$ Usamos $\sin$.
> 2. **Planteamiento:** $\sin(32^\circ) = \frac{x}{10}$
> 3. **Despeje:** El 10 pasa a multiplicar: $10 \cdot \sin(32^\circ) = x$
> 4. **Resultado:** $x \approx 5.30\text{m}$

> [!example] Ejemplo 2: Cálculo de lado (Incógnita en el denominador)
> **Datos:** Ángulo $= 59^\circ$, Cateto Adyacente $= 23\text{m}$. Hallar Hipotenusa ($x$).
> 1. **Fórmula:** Tenemos Adyacente y buscamos Hipotenusa $\rightarrow$ Usamos $\cos$.
> 2. **Planteamiento:** $\cos(59^\circ) = \frac{23}{x}$
> 3. **Despeje (El Intercambio):** Como $x$ está abajo, intercambia con el coseno: $x = \frac{23}{\cos(59^\circ)}$
> 4. **Resultado:** $x \approx 44.65\text{m}$

> [!example] Ejemplo 3: Cálculo de un ángulo y formato DMS
> **Datos:** Cateto Opuesto $= 5\text{m}$, Hipotenusa $= 8\text{m}$. Hallar ángulo ($\theta$).
> 1. **Fórmula:** Tenemos Opuesto e Hipotenusa $\rightarrow$ Usamos $\sin$.
> 2. **Planteamiento:** $\sin(\theta) = \frac{5}{8}$
> 3. **Inversa:** $\theta = \arcsin\left(\frac{5}{8}\right)$. En la calculadora: `SHIFT` + `sin` + `(5 ÷ 8)`.
> 4. **Resultado Decimal:** $\theta \approx 38.68^\circ$.
> 5. **Conversión técnica:** Para obtener Grados, Minutos y Segundos, presiona la tecla `° ' "` inmediatamente después de obtener el resultado.
>    - **Resultado DMS:** $38^\circ 40' 56''$.

> [!example] Ejemplo 4: Aplicación compleja (Dos Triángulos y Costo USD)
> **Problema:** Dos triángulos rectángulos comparten una pared/altura ($x$). El primero tiene un ángulo de $60^\circ$ y base de $40\text{m}$. El segundo tiene un ángulo de $55^\circ$ y base desconocida ($y$).
> 1. **Triángulo 1 (Hallar altura común):** 
>    $\tan(60^\circ) = \frac{x}{40} \rightarrow x = 40 \cdot \tan(60^\circ) \approx 69.28\text{m}$.
> 2. **Triángulo 2 (Hallar base $y$):** 
>    $\tan(55^\circ) = \frac{69.28}{y} \rightarrow y = \frac{69.28}{\tan(55^\circ)} \approx 48.51\text{m}$.
> 3. **Aplicación Financiera:** Si el material para la base $y$ cuesta $\$15.50$ USD por metro:
>    $48.51\text{m} \cdot 15.50\text{ USD/m} \approx \$751.91$ USD.

---

### Ejercicios Prácticos

> [!abstract] Niveles de dificultad
>
> **Nivel Verde (Fácil - Variable arriba)**
> 1. Hallar el cateto adyacente si el ángulo es $65^\circ$ y la hipotenusa es $15\text{m}$.
> 2. Hallar el cateto opuesto si el ángulo es $35^\circ$ y el cateto adyacente mide $9\text{cm}$.
> 3. Calcular el cateto opuesto si la hipotenusa es $10\text{m}$ y el ángulo es $32^\circ$.
> 4. Determinar el cateto adyacente si el ángulo es $35^\circ$ y el opuesto es $6.3\text{cm}$.
>
> **Nivel Amarillo (Medio - Variable abajo / Ángulos)**
> 1. Hallar la hipotenusa si el cateto adyacente mide $23\text{m}$ y el ángulo es $59^\circ$.
> 2. Hallar el cateto adyacente si el cateto opuesto mide $14\text{cm}$ y el ángulo es $51^\circ$.
> 3. Hallar la hipotenusa si el cateto adyacente mide $24.72\text{m}$ y el ángulo es $29^\circ$.
> 4. Hallar el ángulo $\theta$ si el cateto opuesto mide $5\text{m}$ y la hipotenusa $8\text{m}$.
>
> **Nivel Rojo (Avanzado - Multietapa y Costos)**
> 1. Se desea unir dos postes con un cable. El primer poste forma un triángulo con ángulo de elevación de $60^\circ$ y base de $40\text{m}$ para hallar la altura $x$. Usa esa altura para hallar la base $y$ de un segundo poste con ángulo de $55^\circ$.
> 2. **Presupuesto de Obra:** Calcula el costo de una viga de acero que actúa como hipotenusa en un soporte con ángulo de $59^\circ$ y base (adyacente) de $23\text{m}$. El costo es de $\$120$ USD por metro lineal.
> 3. Un cable de $22\text{m}$ (hipotenusa) sostiene una antena. Si la base del cable está a $12\text{m}$ del centro (adyacente), ¿cuál es el ángulo de inclinación $\theta$ en DMS?

> [!success] Solucionario para el docente
> - **Verde:** 1) $6.34\text{m}$; 2) $6.30\text{cm}$; 3) $5.30\text{m}$; 4) $9.00\text{cm}$.
> - **Amarillo:** 1) $44.65\text{m}$; 2) $11.33\text{cm}$; 3) $28.26\text{m}$; 4) $38.68^\circ$.
> - **Rojo:** 
> 	- 1) Base $y \approx 48.51\text{m}$ (calculando primero altura $x \approx 69.28\text{m}$).
> 	- 2) Costo Total: **$\$5,358$ USD** (Longitud viga $H \approx 44.65\text{m} \times 120$ USD).
> 	- 3) $56^\circ 56' 39''$ (usando $\cos^{-1}(12/22)$).

---

### Autoevaluación

> [!question] Pregunta 1
> Si necesitas calcular el **Cateto Opuesto** y conoces la **Hipotenusa**, ¿cuál razón debes usar?
> A) $\cos$
> B) $\sin$
> C) $\tan$

> [!question] Pregunta 2
> Al despejar $x$ en la ecuación $\cos(59^\circ) = \frac{23}{x}$, el paso correcto es:
> A) $x = 23 \cdot \cos(59^\circ)$
> B) $x = \frac{\cos(59^\circ)}{23}$
> C) $x = \frac{23}{\cos(59^\circ)}$

> [!question] Pregunta 3
> Si una base calculada mide $48.51\text{ metros}$ y el costo por metro es de $\$15.50$ USD, ¿cuál es el presupuesto final aproximado?
> A) $\$751.91$ USD
> B) $\$741.50$ USD
> C) $\$630.15$ USD

---

> [!tip] 💡 En la próxima clase
> Ahora que dominas el cálculo de piezas individuales, aprenderemos la **Resolución completa de triángulos**, integrando el Teorema de Pitágoras y la suma de ángulos internos para hallar todos los datos de una figura.

> [!info] 🧭 Navegación
> [[Clase 03 — Introducción a la Trigonometría]] | [[Índice de Contenidos]] | [[Clase 05 — Resolución completa de triángulos]]