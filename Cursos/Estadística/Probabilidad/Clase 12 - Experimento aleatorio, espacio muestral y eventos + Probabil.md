# Clase 12 — Experimento aleatorio, espacio muestral y eventos + Probabilidad simple con dados y cartas

`#algebra #randomexperimen`

[[Clase 11|⬅ Clase 11]] | [[00 - Índice del curso|Índice]] | [[00 - Índice del curso|Fin del curso ➡]]

---

## 1. ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> La probabilidad es la herramienta matemática que nos permite medir qué tan posible es que algo ocurra, permitiéndonos tomar decisiones informadas bajo total incertidumbre.
> 
> *   💵 **Aplicación USD:** Si inviertes $\$100$ USD en una rifa con $1,000$ boletos, la probabilidad te indica que tienes solo un $0.10\%$ de éxito ($1/1,000$). ¿Es una inversión inteligente o un gasto arriesgado?
> *   🏗️ **Aplicación práctica:** Es el pilar fundamental para el diseño de juegos de mesa equilibrados y la organización de sorteos transparentes.
> *   📊 **Situación cotidiana:** Te permite predecir con exactitud tus opciones de éxito al lanzar una moneda, un dado o buscar una carta específica en un mazo.

---

## 2. Conceptos Clave (Definiciones)

Para dominar el azar, primero debemos nombrar sus partes con precisión:

*   **Experimento Aleatorio:** Es cualquier acción donde no se puede predecir el resultado final con seguridad, incluso si conocemos todas las opciones (ej. lanzar un dado).
*   **Espacio Muestral ($S$ o $\Omega$):** Es el conjunto de **todos** los resultados posibles. Siempre se escribe entre llaves $\{ \}$.
    *   *Ejemplo:* En una moneda, $S = \{ \text{cara, cruz} \}$.
*   **Evento o Suceso:** Es un subconjunto del espacio muestral; es decir, uno o varios resultados que nos interesan. Se representan con letras mayúsculas ($A, B, C...$).
    *   *Ejemplo:* En un dado, el evento $A$ podría ser "obtener un número par" $\rightarrow A = \{2, 4, 6\}$.

> [!warning] ⚠️ Error común
> Muchos estudiantes olvidan listar todos los elementos individuales cuando hay objetos repetidos. Si en una bolsa hay $3$ bolas azules, en tu espacio muestral no debes escribir "azul" una sola vez, sino identificar cada una: $\{A_1, A_2, A_3\}$. Esto es vital para que el cálculo sea correcto.

> [!tip] 💡 Truco para recordarlo
> Piensa en un restaurante:
> *   **Espacio Muestral ($S$):** Es **"El Menú"** (contiene todo lo que el restaurante puede ofrecer).
> *   **Evento ($A$):** Es **"Tu Pedido"** (lo que tú seleccionas de ese menú).

---

## 3. Procedimiento Paso a Paso (Ley de Laplace)

Para calcular la probabilidad de un evento simple, aplicamos la **Ley de Laplace**:

```text
PASO 1: Identificar el número total de casos posibles (Denominador).
PASO 2: Contar cuántos casos son favorables al evento solicitado (Numerador).
PASO 3: Escribir la probabilidad como fracción: P(A) = Casos Favorables / Casos Posibles.
PASO 4: Convertir a decimal (dividiendo) y a porcentaje (multiplicando por 100).
```

---

## 4. Ejemplos Desarrollados

> [!example] Ejemplo 1: El dado básico
> **Pregunta:** Probabilidad de lanzar un dado y obtener el número $3$.
> *   Casos posibles: $6$ ($\{1, 2, 3, 4, 5, 6\}$).
> *   Casos favorables: $1$ ($\{3\}$).
> *   **Cálculo:** $P(A) = \frac{1}{6} \approx 0.1667 \rightarrow \mathbf{16.67\%}$

> [!example] Ejemplo 2: Lógica de "menor que"
> **Pregunta:** Probabilidad de sacar menos de $4$ en un dado.
> *   Casos favorables: $3$ ($\{1, 2, 3\}$).
> *   **Cálculo:** $P(A) = \frac{3}{6} = \frac{1}{2} = 0.50 \rightarrow \mathbf{50.00\%}$

> [!example] Ejemplo 3: La baraja francesa
> **Pregunta:** Probabilidad de sacar un As en una baraja de $52$ cartas.
> *   Casos posibles: $52$.
> *   Casos favorables: $4$ (As de corazones, diamantes, picas y tréboles).
> *   **Cálculo:** $P(A) = \frac{4}{52} = \frac{1}{13} \approx 0.0769 \rightarrow \mathbf{7.69\%}$

> [!example] Ejemplo 4: Aplicación USD
> **Pregunta:** En un concurso, ganas un premio de $\$50$ USD si al sacar una carta de una baraja de $52$, esta es de **Tréboles**. ¿Qué probabilidad tienes de ganar?
> *   Casos favorables: $13$ (hay $13$ cartas de cada palo).
> *   **Cálculo:** $P(A) = \frac{13}{52} = \frac{1}{4} = 0.25 \rightarrow \mathbf{25.00\%}$

---

## 5. Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Fácil: Moneda y Dado
> 1. Escribe el espacio muestral ($S$) de lanzar una moneda y un dado simultáneamente (usa la notación $C$ para cara y $X$ para cruz).
> 2. ¿Cuál es la probabilidad de que la moneda caiga en "Cara" y el dado en "$6$"?
> 3. ¿Cuál es la probabilidad de que la moneda sea "Cruz" y el dado sea un número par?
> 4. Si lanzas solo la moneda, ¿cuál es la probabilidad de obtener "Cara"?

> [!abstract] 🟡 Nivel Medio: La Urna Mágica
> En una urna hay $1$ bola roja ($R$), $2$ azules ($A$) y $3$ blancas ($B$). Si extraes una sola bola al azar:
> 1. Escribe el espacio muestral completo identificando cada bola individualmente.
> 2. ¿Cuál es la probabilidad de que la bola **no** sea blanca?
> 3. ¿Cuál es la probabilidad de que la bola sea azul?
> 4. ¿Cuál es la probabilidad de que sea roja o blanca?

> [!abstract] 🔴 Nivel Avanzado (USD): Sorteo de Cartas
> Se ofrece un premio de $\$200$ USD bajo las siguientes condiciones con una baraja francesa ($52$ cartas):
> 1. Probabilidad de ganar si la condición es sacar una carta roja.
> 2. Probabilidad de ganar si la condición es sacar una letra ($As, J, Q$ o $K$).
> 3. Probabilidad de ganar si la condición es sacar específicamente el Rey de Picas.
> 4. ¿Qué es más probable: ganar con una carta de corazones o ganar con una carta que sea un número **menor a 3** ($Ases$ no cuentan)?

---

## 6. Solucionario para el Docente

> [!success] Respuestas Rápidas [R]
> **Fácil:** 
> 1. $S = \{C1, C2, C3, C4, C5, C6, X1, X2, X3, X4, X5, X6\}$. Total: $12$ elementos.
> 2. $P(A) = \frac{1}{12} \approx \mathbf{8.33\%}$.
> 3. $P(A) = \frac{3}{12} = \frac{1}{4} = \mathbf{25.00\%}$.
> 4. $P(A) = \frac{1}{2} = \mathbf{50.00\%}$.
> 
> **Medio:**
> 1. $S = \{R_1, A_1, A_2, B_1, B_2, B_3\}$. Total: $6$ elementos.
> 2. $P(A) = \frac{3}{6} = \frac{1}{2} = \mathbf{50.00\%}$.
> 3. $P(A) = \frac{2}{6} = \frac{1}{3} \approx \mathbf{33.33\%}$.
> 4. $P(A) = \frac{4}{6} = \frac{2}{3} \approx \mathbf{66.67\%}$.
> 
> **Avanzado:**
> 1. $P(A) = \frac{26}{52} = \frac{1}{2} = \mathbf{50.00\%}$.
> 2. $P(A) = \frac{16}{52} = \frac{4}{13} \approx \mathbf{30.77\%}$.
> 3. $P(A) = \frac{1}{52} \approx \mathbf{1.92\%}$.
> 4. **Corazones** ($\frac{13}{52} = 25.00\%$) es más probable que **Menor a 3** (solo los $2$ de cada palo $\rightarrow \frac{4}{52} \approx 7.69\%$).

---

## 7. Autoevaluación

> [!question] Pregunta 1: Conceptual
> Al definir el "Espacio Muestral" del lanzamiento de un dado, nos referimos a:
> a) Solo el número que deseamos obtener.
> b) El conjunto completo $S = \{1, 2, 3, 4, 5, 6\}$.
> c) La probabilidad de que el resultado sea un número primo.

> [!question] Pregunta 2: Procedimental
> ¿Cuál es la probabilidad de obtener un número primo ($2, 3, 5$) al lanzar un dado?
> a) $\frac{1}{6}$
> b) $\frac{3}{6} = 50.00\%$
> c) $\frac{6}{6} = 100.00\%$

> [!question] Pregunta 3: Aplicación USD
> Si participas en un juego de cartas donde ganas si extraes una "Letra" ($16$ casos favorables de $52$), ¿cuál es tu porcentaje exacto de éxito redondeado a dos decimales?
> a) $7.69\%$
> b) $25.00\%$
> c) $30.77\%$

---

> [!tip] 💡 En la próxima clase
> Una vez dominados el espacio muestral y la probabilidad simple, daremos el siguiente paso hacia la **Combinatoria Avanzada**. Entender cómo se organizan los elementos es la clave para resolver experimentos donde los resultados se multiplican.

[[Clase 11|⬅ Clase 11]] | [[00 - Índice del curso|Índice]] | [[00 - Índice del curso|Fin del curso ➡]]