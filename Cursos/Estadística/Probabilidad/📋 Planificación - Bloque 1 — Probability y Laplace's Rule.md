# 📋 Planificación Didáctica — Probability y Laplace's Rule

**1. Tema**
Probability y Laplace's Rule
`#planificacion #dua #probabilityylap`

**2. Metodología**
**Aprendizaje colaborativo formal**: El aula se organizará en grupos pequeños heterogéneos para realizar experimentos aleatorios directos, tales como el lanzamiento de monedas y dados. El docente actuará como guía experto, instruyendo en la técnica didáctica de "escribir primero el denominador" —puesto que el espacio muestral proporciona la clave para identificar luego los casos favorables— y supervisando la aplicación rigurosa de los axiomas de probabilidad.

---

**3. Secuencia Didáctica**

**3.1 🔵 ANTICIPACIÓN — 20 min**

> [!abstract] Actividad de inicio
> Se presentará el concepto de **Experimento Aleatorio** mediante un reto de predicción: se lanzará una moneda y un dado de seis caras. Se preguntará: "¿Podemos asegurar el resultado antes de que ocurra?". 
> A partir de la discusión, definiremos el **Espacio Muestral ($S$ o $\Omega$)** como el conjunto de todos los resultados lógicos posibles:
> - Moneda: $S = \{cara, cruz\}$.
> - Dado: $S = \{1, 2, 3, 4, 5, 6\}$.
> Se establecerá que, aunque el resultado individual es incierto, el conjunto de posibilidades es finito y conocido.

> [!note] Enfoque DUA
> **Qué:** Activación de conocimientos previos sobre azar y predicción.
> **Cómo:** Lluvia de ideas y registro visual en la pizarra. Se utilizarán marcadores de colores para diferenciar los elementos del espacio muestral (ej. rojo para pares, azul para impares), facilitando la discriminación visual de los datos.

**3.2 🟡 CONSTRUCCIÓN — 40 min**

> [!example] Actividades centrales
> 1. **Regla de Laplace**: Se formaliza la probabilidad de un evento simple: $P(A) = \frac{\text{Casos favorables}}{\text{Casos posibles}}$.
> 2. **Modelado con la Urna**: En una urna con 7 bolas (4 Rojas, 2 Azules, 1 Amarilla), calcularemos la probabilidad de extraer una bola roja:
>    - $P(R) = \frac{4}{7} \approx 0.5714 = 57.14\%$.
>    *(Instrucción: Siempre escribir el denominador 7 primero).*
> 3. **Axiomas y Teoremas**:
>    - **Axiomas (Verdades evidentes)**:
>        - **Positividad**: $P(A) \ge 0$.
>        - **Certeza**: $P(S) = 1$.
>        - **Unión de Mutuamente Excluyentes**: Si $A$ y $B$ no pueden ocurrir a la vez, $P(A \cup B) = P(A) + P(B)$. Ej: $P(\text{par o impar}) = \frac{3}{6} + \frac{3}{6} = 1$.
>    - **Teoremas (Derivados)**:
>        - **Evento Imposible**: $P(\emptyset) = 0$ (Ej: Sacar una bola negra de la urna de 7 bolas).
>        - **Evento Complementario**: $P(A^c) = 1 - P(A)$.
> 4. **Eventos Compuestos (Baraja)**: En una baraja de 52 cartas, la probabilidad de sacar una "Letra" ($A, J, Q, K$ en los 4 palos) es $P = \frac{16}{52}$, que simplificado es $\frac{4}{13}$.

> [!note] Enfoque DUA
> **Qué:** Comprensión de la Regla de Laplace y clasificación de eventos (seguro, probable, imposible).
> **Cómo:** Trabajo en parejas resolviendo fichas. Es obligatorio simplificar fracciones (ej. $\frac{4}{8} \to \frac{1}{2}$) y expresar resultados en fracción, decimal y porcentaje.
> **Por qué:** El uso de marcadores de distintos colores para el numerador (favorables) y denominador (posibles) permite transformar la abstracción numérica en una representación visual comparable.

**3.3 🟢 CONSOLIDACIÓN — 20 min**

> [!success] Actividad de cierre
> 1. **Reto de los Dos Dados**: Calcular la probabilidad de que la suma de dos dados sea 7. 
>    - Espacio muestral: $6 \times 6 = 36$ casos.
>    - Casos favorables: $\{(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)\}$.
>    - Resultado: $P(\text{suma 7}) = \frac{6}{36} = \frac{1}{6} \approx 0.1666 = 16.66\%$.
>    - Aplicación de Teorema: $P(\text{suma NO sea 7}) = 1 - \frac{1}{6} = \frac{5}{6} \approx 83.33\%$.
> 2. **El Dado Cargado**: Si un dado se truca para que los pares salgan el doble de veces que los impares, el espacio muestral cambia a 9 casos: $S = \{1, 2, 2, 3, 4, 4, 5, 6, 6\}$. 
>    - $P(2) = \frac{2}{9}$. 
>    - $P(\text{Par}) = \frac{2+2+2}{9} = \frac{6}{9} = \frac{2}{3}$.

> [!note] Enfoque DUA
> **Qué:** Producto final: resolución del reto de probabilidad de eventos no equiprobables y complementarios.
> **Cómo:** Socialización en la pizarra y proceso de autocorrección guiada. Se enfatiza que la suma de todas las probabilidades del espacio muestral debe ser siempre $1$ o $100\%$.

---

**4. Recursos**

| Recurso | Tipo | Uso en la clase |
| :--- | :--- | :--- |
| **Pizarra** | Físico | Modelado de la técnica de Laplace (denominador primero) y diagramas de Venn. |
| **Marcadores de Colores** | Físico | Codificación visual: un color para casos favorables y otro para el total de casos. |
| **Fichas de Trabajo** | Impreso | Ejercicios con la baraja de 52 cartas (13 corazones, picas, tréboles, diamantes; cartas A, J, Q, K). |
| **Dados y Monedas** | Físico | Ejecución de experimentos para contrastar probabilidad teórica frente a frecuencia observada. |
| **Impresora** | Físico | Generación de tablas de contingencia para el experimento de los dos dados ($6 \times 6$). |