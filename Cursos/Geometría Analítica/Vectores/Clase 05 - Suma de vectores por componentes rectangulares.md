# Clase 05 — Suma de vectores por componentes rectangulares

#algebra #vectorsumbyrect

> [!info] 🧭 Navegación
> - [[Clase 04]] — Introducción a los vectores
> - [[Índice]] — Curso Completo
> - **Clase 05 — Suma de vectores por componentes rectangulares**
> - [[Clase 06]] — Equilibrio estático y aplicaciones complejas

---

> [!info] 🌍 Relevancia y aplicaciones
> El método de componentes rectangulares es el estándar de oro en física y matemáticas por su absoluta precisión. A diferencia del método gráfico, que depende del pulso y la regla del dibujante, este método utiliza trigonometría para obtener resultados exactos sin importar la complejidad del problema.
> 
> - 💵 **Finanzas**: Se utiliza para modelar flujos de capital multidireccionales. Cada inversión se trata como un vector; sumarlos permite hallar el balance neto y la dirección del crecimiento financiero en $USD.
> - 🏗️ **Ingeniería**: Crucial para el diseño de estructuras. Los ingenieros descomponen las fuerzas de gravedad y viento en ejes $X$ e $Y$ para asegurar que los edificios permanezcan estables.
> - 📊 **Navegación**: Los sistemas de GPS calculan la posición real sumando el vector de movimiento de un vehículo con vectores externos como la corriente marina o la velocidad del viento.

---

> [!note] 📌 ¿Qué es la suma de vectores por componentes?
> Imagina que tienes varias flechas inclinadas. Sumarlas así es difícil porque van "chuecas". Sumar por componentes es como desarmar cada flecha en dos piezas de Lego: una pieza que solo se mueve de forma horizontal (Eje $X$) y otra que solo se mueve de forma vertical (Eje $Y$). 
> 
> Una vez que todas las flechas están "desarmadas", simplemente sumas todas las piezas horizontales entre sí y todas las verticales entre sí. Al final, vuelves a armar una sola flecha grande llamada **Vector Resultante**.

> [!warning] ⚠️ Error común: El origen del ángulo
> Un error típico es usar el ángulo tal cual aparece en problemas tipo "Norte $20^\circ$ Este". Las fórmulas de $X$ e $Y$ solo funcionan directamente si el ángulo nace desde el eje horizontal (Este u Oeste).
> - ❌ **Incorrecto**: Usar $20^\circ$ si sale desde el Norte.
> - ✅ **Correcto**: Usar el ángulo complementario de $70^\circ$ ($90^\circ - 20^\circ$), que es el que toca el eje $X$.

> [!tip] 💡 Truco para recordarlo
> Para no confundir las funciones trigonométricas, usa esta regla mnemotécnica:
> - **X-Co**: El eje $X$ siempre usa **Co**seno $\rightarrow V_x = V \cdot \cos(\theta)$.
> - **Y-Se**: El eje $Y$ siempre usa **Se**no $\rightarrow V_y = V \cdot \sin(\theta)$.
> 
> *Nota: Este truco es universal siempre y cuando te asegures de que tu ángulo toque el eje horizontal ($X$).*

---

### 4. Procedimiento paso a paso

> [!list] 🛠️ Metodología de resolución
> 1. **ANÁLISIS DE SIGNOS Y ÁNGULOS**: Identifica el cuadrante. Si el vector va al Oeste ($O$) o Sur ($S$), su componente será negativa. Asegúrate de que los ángulos nazcan en el eje horizontal (aplica $90^\circ - \text{ángulo}$ si es necesario).
> 2. **DESCOMPOSICIÓN**: Calcula las componentes individuales:
>    - $V_x = V \cdot \cos(\theta)$
>    - $V_y = V \cdot \sin(\theta)$
> 3. **SUMATORIA**: Suma todas las componentes en $X$ para obtener $R_x$ y todas las componentes en $Y$ para obtener $R_y$.
> 4. **RECONSTRUCCIÓN**: Halla la magnitud final con Pitágoras $R = \sqrt{R_x^2 + R_y^2}$ y la dirección con el arco tangente $\theta = \arctan\left(\frac{|R_y|}{|R_x|}\right)$.

---

### 5. Ejemplos prácticos

> [!example] Ejemplo 1: Suma básica (Primer Cuadrante)
> **Problema**: Sumar el vector $\vec{A}$ ($3\text{ m}$, $E 30^\circ N$) y el vector $\vec{B}$ ($4\text{ m}$, $E 73^\circ N$).
> 
> **Componentes de A**:
> - $A_x = 3 \cdot \cos(30^\circ) = 2.59\text{ m}$
> - $A_y = 3 \cdot \sin(30^\circ) = 1.50\text{ m}$
> 
> **Componentes de B**:
> - $B_x = 4 \cdot \cos(73^\circ) = 1.16\text{ m}$
> - $B_y = 4 \cdot \sin(73^\circ) = 3.82\text{ m}$
> 
> **Sumatoria**:
> - $R_x = 2.59 + 1.16 = 3.75\text{ m}$ (Este)
> - $R_y = 1.50 + 3.82 = 5.32\text{ m}$ (Norte)
> 
> **Resultado Final**: 
> - $R = \sqrt{3.75^2 + 5.32^2} = \mathbf{6.50\text{ m}}$

> [!example] Ejemplo 2: Ajuste de signos y ángulos
> **Problema**: $\vec{A}$ ($5\text{ m}$, $N 20^\circ E$) y $\vec{B}$ ($6\text{ m}$, $O 40^\circ S$).
> 
> **Análisis**: 
> - Para $\vec{A}$, el ángulo sale del Norte, usamos el complementario: $90^\circ - 20^\circ = 70^\circ$.
> - Para $\vec{B}$, el vector está en el tercer cuadrante (Oeste y Sur), por lo que $B_x$ y $B_y$ serán negativos.
> 
> **Cálculos**:
> - $A_x = 5 \cdot \cos(70^\circ) = 1.71\text{ m}$ | $A_y = 5 \cdot \sin(70^\circ) = 4.69\text{ m}$
> - $B_x = -6 \cdot \cos(40^\circ) = -4.59\text{ m}$ | $B_y = -6 \cdot \sin(40^\circ) = -3.85\text{ m}$
> 
> **Sumatoria**:
> - $R_x = 1.71 - 4.59 = -2.88\text{ m}$ (Oeste)
> - $R_y = 4.69 - 3.85 = 0.84\text{ m}$ (Norte)
> 
> **Resultado**: 
> - $R = \sqrt{(-2.88)^2 + (0.84)^2} = \mathbf{3.00\text{ m}}$

> [!example] Ejemplo 3: Sistema de tres vectores
> **Problema**: Sumar $\vec{A}$ ($4\text{ m}$, $O 32^\circ N$), $\vec{B}$ ($5\text{ m}$, $S 15^\circ E$) y $\vec{C}$ ($3\text{ m}$, $E 24^\circ N$).
> 
> **Ajuste**: En $\vec{B}$, el ángulo sale del Sur, usamos $75^\circ$ ($90^\circ - 15^\circ$).
> 
> **Tabla de componentes**:
> - $\vec{A}: A_x = -3.39\text{ m}, A_y = 2.11\text{ m}$
> - $\vec{B}: B_x = 1.29\text{ m}, B_y = -4.82\text{ m}$
> - $\vec{C}: C_x = 2.74\text{ m}, C_y = 1.22\text{ m}$
> 
> **Resultantes**: 
> - $R_x = -3.39 + 1.29 + 2.74 = 0.64\text{ m}$ (Este)
> - $R_y = 2.11 - 4.82 + 1.22 = -1.49\text{ m}$ (Sur)
> 
> **Final**: $R = \mathbf{1.62\text{ m}}$, Dirección: $\mathbf{E 66.75^\circ S}$.

> [!example] Ejemplo 4: Aplicación en Balance Financiero ($USD$)
> **Contexto**: Una empresa realiza tres movimientos de capital. El término "Sureste" implica una bisectriz exacta de $45^\circ$.
> 1. Inversión $\vec{A}$: $4\text{ USD}$ al Sureste ($45^\circ$).
> 2. Flujo $\vec{B}$: $6\text{ USD}$ al Norte ($90^\circ$ sobre el eje $Y$).
> 3. Gasto $\vec{C}$: $8.2\text{ USD}$ al $S 55^\circ O$ (Ajustado a $35^\circ$ desde el Oeste).
> 
> **Cálculos**:
> - $\vec{A}: A_x = 4\cos(45^\circ) = 2.82, A_y = -2.82$
> - $\vec{B}: B_x = 0, B_y = 6$
> - $\vec{C}: C_x = -8.2\cos(35^\circ) = -6.71, C_y = -8.2\sin(35^\circ) = -4.70$
> 
> **Estado Neto**: 
> - $R_x = 2.82 - 6.71 = -3.89\text{ USD}$
> - $R_y = -2.82 + 6 - 4.70 = -1.52\text{ USD}$
> 
> **Resultado**: Magnitud $\mathbf{4.17\text{ USD}}$ con dirección $\mathbf{O 21.34^\circ S}$.

---

### 6. Ejercicios para el estudiante

> [!abstract] 🟢 Nivel Fácil
> Hallar la magnitud resultante de los siguientes pares de vectores (1er cuadrante):
> 1. $\vec{A} = 5\text{m}, E 20^\circ N$ y $\vec{B} = 3\text{m}, E 20^\circ N$.
> 2. $\vec{A} = 10\text{m}, E$ y $\vec{B} = 5\text{m}, N$.
> 3. $\vec{A} = 2\text{m}, E 45^\circ N$ y $\vec{B} = 2\text{m}, E 45^\circ N$.
> 4. $\vec{A} = 6\text{m}, E 30^\circ N$ y $\vec{B} = 8\text{m}, E 60^\circ N$.

> [!abstract] 🟡 Nivel Medio
> Resuelve ajustando ángulos y signos:
> 1. $\vec{A} = 7\text{m}, O 16^\circ S$ y $\vec{B} = 4\text{m}, N 14^\circ O$.
> 2. $\vec{A} = 12\text{m}, S 30^\circ E$ y $\vec{B} = 5\text{m}, E 10^\circ N$.
> 3. $\vec{A} = 8\text{m}, N 45^\circ E$ y $\vec{B} = 8\text{m}, S 45^\circ O$.
> 4. $\vec{A} = 15\text{m}, O 60^\circ N$ y $\vec{B} = 10\text{m}, E 30^\circ S$.

> [!abstract] 🔴 Nivel Avanzado (Transacciones $USD$)
> Determina el vector de capital resultante (Magnitud y Dirección):
> 1. Inv. A: $100\text{ USD}$ ($E 30^\circ N$); Inv. B: $50\text{ USD}$ ($O 45^\circ S$); Inv. C: $80\text{ USD}$ ($N$).
> 2. Gasto A: $200\text{ USD}$ ($S$); Gasto B: $150\text{ USD}$ ($O 20^\circ N$); Inv. C: $300\text{ USD}$ ($E 60^\circ N$).
> 3. Flujo A: $50\text{ USD}$ ($S 10^\circ O$); Flujo B: $50\text{ USD}$ ($N 10^\circ E$); Flujo C: $100\text{ USD}$ ($E$).
> 4. Riesgo A: $10\text{ USD}$ ($O$); Riesgo B: $20\text{ USD}$ ($N$); Riesgo C: $30\text{ USD}$ ($E 45^\circ S$).

> [!success] ✅ Respuestas (Para el docente)
> **Fácil**: 1) $8\text{m}$ | 2) $11.18\text{m}$ | 3) $4\text{m}$ | 4) $13.54\text{m}$.
> **Medio**: 1) $4.77\text{m}$ ($O 39.05^\circ N$) | 2) $11.80\text{m}$ | 3) $0\text{m}$ | 4) $6.70\text{m}$.
> **Avanzado**:
> 1. $R_x = 51.25, R_y = 94.64 \rightarrow R = 107.65\text{ USD}, E 61.57^\circ N$.
> 2. $R_x = 9.04, R_y = 111.12 \rightarrow R = 111.49\text{ USD}, E 85.35^\circ N$.
> 3. $R_x = 100, R_y = 0 \rightarrow R = 100\text{ USD}, E$.
> 4. $R_x = 11.21, R_y = -1.21 \rightarrow R = 11.28\text{ USD}, E 6.16^\circ S$.

---

### 7. Autoevaluación

> [!question] Pregunta 1
> ¿Qué función trigonométrica corresponde a la componente horizontal ($X$) si el ángulo se mide desde el eje $X$?
> - a) Seno
> - b) Coseno
> - c) Tangente
> - d) Arcotangente
> 
> **Respuesta correcta: b**. El coseno relaciona el cateto adyacente (eje $X$) con la hipotenusa.

> [!question] Pregunta 2
> Identifica el ángulo correcto para los cálculos si se da una dirección "$S 25^\circ O$".
> - a) $25^\circ$
> - b) $115^\circ$
> - c) $65^\circ$
> - d) $90^\circ$
> 
> **Respuesta correcta: c**. Para que el ángulo nazca del eje $X$ (Oeste), restamos $90^\circ - 25^\circ = 65^\circ$.

> [!question] Pregunta 3
> Si un balance financiero tiene $R_x = 30\text{ USD}$ y $R_y = 40\text{ USD}$, ¿cuál es la magnitud neta?
> - a) $70\text{ USD}$
> - b) $10\text{ USD}$
> - c) $50\text{ USD}$
> - d) $1200\text{ USD}$
> 
> **Respuesta correcta: c**. Por Pitágoras: $\sqrt{30^2 + 40^2} = \sqrt{900 + 1600} = \sqrt{2500} = 50$.

---

> [!tip] 💡 En la próxima clase
> Aplicaremos esta suma de componentes para resolver sistemas en equilibrio. En la **Clase 06**, aprenderás que si la sumatoria de todos estos vectores es cero ($\sum \vec{F} = 0$), el objeto no se mueve. ¡Prepárate para la estática!

> [!info] 🧭 Navegación
> - [[Clase 04]] — Introducción a los vectores
> - [[Índice]] — Curso Completo
> - **Clase 05 — Suma de vectores por componentes rectangulares**
> - [[Clase 06]] — Equilibrio estático y aplicaciones complejas