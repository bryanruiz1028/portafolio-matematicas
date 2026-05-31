# 📋 Planificación Didáctica — Axiomas de Probabilidad y Sucesos Mutuamente Excluyentes

## 1. Tema
**Fundamentos Axiomáticos de la Probabilidad: Sucesos Mutuamente Excluyentes y Espacios Muestrales Discretos.** Esta sesión establece la transición rigurosa entre la teoría de conjuntos y el cálculo estocástico, fundamentando la comprensión del azar a través de la Ley de Laplace y los axiomas de aditividad en experimentos con y sin reemplazo.

## 2. Metodología
Se implementará el **Aprendizaje Colaborativo Formal** para facilitar la construcción social del significado matemático frente a la incertidumbre. Los estudiantes trabajarán en grupos de 4 (Líder, Secretario, Calculador, Verificador), resolviendo retos experimentales basados en los modelos de monedas, dados y urnas presentados por el Profe Alex, promoviendo la discusión técnica y la validación de resultados grupales.

---

## 3. Secuencia Didáctica

### 3.1. 🔵 ANTICIPACIÓN — 20 min

> [!abstract] Reto de Predicción y Espacio Muestral
> El docente inicia lanzando una moneda y plantea: "¿Podemos predecir con 100% de certeza el resultado?". A partir de la definición del Profe Alex, se establecen los pilares del azar:
> - **Experimento Aleatorio:** Proceso donde existen varios resultados posibles y el resultado exacto es impredecible.
> - **Espacio Muestral (S):** El conjunto total de resultados. Para la moneda: $S = \{cara, sello\}$.
> - **Evento o Suceso:** Subconjunto del espacio muestral (ej. que caiga solo cara).

> [!note] Enfoque DUA: Representación y Activación
> **Qué:** Activación de esquemas previos sobre incertidumbre.
> **Cómo:** Registro visual en pizarra del espacio muestral. Uso de múltiples medios de representación (símbolos y palabras) para definir el conjunto $S$, permitiendo que los estudiantes propongan sus propios códigos visuales para los resultados.

### 3.2. 🟡 CONSTRUCCIÓN — 40 min

> [!example] Construcción del Conocimiento y Axiomatización
> 
> **Experimento 1: Dados y la Ley de Laplace**
> Definición de $S = \{1, 2, 3, 4, 5, 6\}$. Aplicación de la **Ley de Laplace**: $P(A) = \frac{\text{casos favorables}}{\text{casos posibles}}$.
> *Desafío Cognitivo:* Calcular la probabilidad de obtener un **Número Primo** ($A = \{2, 3, 5\}$). 
> - Resultado: $P(A) = 3/6 = 1/2 = 50\%$.
> 
> **Experimento 2: Urnas, Aditividad y la Variable de Reemplazo**
> Basado en una urna con 3 bolas rojas y 4 azules ($S_{total} = 7$):
> 1. **Sucesos Mutuamente Excluyentes (Lógica de la "O"):** Se explica que si un evento es "sacar roja" y otro es "sacar azul", al ser excluyentes se aplica el **Axioma de Aditividad (Unión)**: $P(R \cup A) = P(R) + P(A)$. La palabra clave **"O"** implica suma.
> 2. **Con Reemplazo vs. Sin Reemplazo:** 
>    - *Con reemplazo:* El espacio muestral se mantiene constante ($S=7$). Los eventos son independientes.
>    - *Sin reemplazo:* Al extraer una bola, el espacio muestral cambia (el denominador pasa de 7 a 6). El docente debe enfatizar cómo esto altera la probabilidad del segundo suceso.
> 
> **Visualización Estructural (Diagrama de Árbol para 2 monedas)**
> Se modela la **intersección (Lógica de la "Y")** mediante la multiplicación de ramas:
> - **Moneda 1**
> 	- Cara (1/2)
> 		- **Moneda 2: Cara** (1/2) $\to$ Probabilidad Final: $1/4$ ($25\%$)
> 		- **Moneda 2: Sello** (1/2) $\to$ Probabilidad Final: $1/4$ ($25\%$)
> 	- Sello (1/2)
> 		- **Moneda 2: Cara** (1/2) $\to$ Probabilidad Final: $1/4$ ($25\%$)
> 		- **Moneda 2: Sello** (1/2) $\to$ Probabilidad Final: $1/4$ ($25\%$)
> *Axioma fundamental:* La suma de todas las ramas terminales debe agotar la unidad ($\sum P = 1$).

> [!note] Enfoque DUA: Acción y Expresión
> **Qué:** Aplicación de conceptos de independencia y dependencia.
> **Cómo:** Uso de "dibujos espectaculares" (estilo Profe Alex) y códigos de colores para diferenciar las bolas en la urna y los palos en la baraja francesa (corazones, diamantes, tréboles, picas). Trabajo en parejas para calcular la probabilidad de intersección ("Y") frente a la unión ("O").

### 3.3. 🟢 CONSOLIDACIÓN — 20 min

> [!success] Ticket de Salida: Verificación de Axiomas
> Los estudiantes resuelven de forma individual:
> 1. En una baraja de 52 cartas, ¿cuál es la probabilidad de sacar un **As O un Rey**? (Sucesos excluyentes).
> 2. Si en una urna de 3 rojas y 4 azules extraigo dos bolas **sin reemplazo**, ¿cuál es la probabilidad de que la primera sea roja **Y** la segunda sea azul?
> 3. Identificar el **Evento Complementario** ($P(A^c)$): Si la probabilidad de sacar roja es $3/7$, ¿cuál es la probabilidad de "No sacar roja"? Demostrar que $P(A) + P(A^c) = 1$.

> [!note] Enfoque DUA: Evaluación
> **Qué:** Verificación de la comprensión de los axiomas de aditividad y complementariedad.
> **Cómo:** Autoevaluación inmediata mediante la resolución del ticket de salida con retroalimentación correctiva del docente.

---

## 4. Recursos

| Recurso | Tipo | Uso Pedagógico en Clase |
| :--- | :--- | :--- |
| **Pizarra y Marcadores** | Visual | Representación de diagramas de árbol y cálculo de la sumatoria de probabilidades terminales. |
| **Dados de 6 caras** | Físico | Comprobación empírica de la Ley de Laplace mediante el suceso de "Números Primos". |
| **Baraja de Naipes (52)** | Físico | Análisis de subconjuntos (letras vs. números) y cálculo de la unión de sucesos excluyentes. |
| **Urnas y Bolas de Colores** | Manipulativo | Demostración táctil de la diferencia entre extracción con reemplazo y sin reemplazo (cambio de denominador). |
| **Fichas de Trabajo** | Impreso | Guía estructurada para calcular intersecciones de eventos independientes vs. uniones de eventos excluyentes. |