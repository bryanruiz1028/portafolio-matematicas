# 📖 Guía de estudio — Clase 12: Experimentos aleatorios, espacio muestral y sucesos

## 1. CONCEPTOS FUNDAMENTALES Y LEY DE LAPLACE

Para dominar la probabilidad, primero debemos entender que estamos trabajando con la **incertidumbre**. Aunque no podemos predecir el futuro, las matemáticas nos permiten calcular qué tan posible es que algo ocurra.

| Término | Definición y Notación | Nota Pedagógica |
| :--- | :--- | :--- |
| **Experimento Aleatorio** | Proceso donde hay varios resultados posibles y no se puede predecir con exactitud cuál ocurrirá. | Ejemplo: Lanzar un dado o sacar una carta. |
| **Espacio Muestral ($S$ o $\Omega$)** | Conjunto de **todos** los resultados posibles de un experimento. Se escribe entre llaves `{}`. | Es fundamental listar todos los elementos para no errar en el cálculo. |
| **Evento o Suceso ($E$)** | Uno o varios de los resultados posibles del espacio muestral (un subconjunto). | Puede ser simple (un resultado) o compuesto (varios). |
| **Ley de Laplace** | $P(E) = \frac{\text{Casos favorables}}{\text{Casos posibles}}$ | El resultado siempre está entre $0 \leq P(E) \leq 1$ ($0\%$ a $100\%$). |

---

## 2. MODELADO DE EJERCICIOS (PASO A PASO)

````ad-example
title: Ejemplo A — Lanzamiento de un dado (Modelado Visual)
**El Reto:** Si lanzas un dado convencional de 6 caras, ¿cuál es la probabilidad de obtener un número par?

1. **Definir el Espacio Muestral ($\Omega$):** Identificamos visualmente todas las caras del dado.
   $\Omega = \{1, 2, 3, 4, 5, 6\}$ 
   *Total de casos posibles ($n$) = 6.*

2. **Identificar el Evento ($E$):** Queremos los números pares.
   $E = \{2, 4, 6\}$
   *Total de casos favorables ($f$) = 3.*

3. **Aplicar Ley de Laplace:**
   $P(E) = \frac{3}{6}$

4. **Expresión de resultados (Las tres formas):**
   *   **Fracción:** $1/2$ *(¡Recuerda simplificar siempre!)*.
   *   **Decimal:** $0.5$.
   *   **Porcentaje:** $50\%$.
````

````ad-example
title: Ejemplo B — La rifa de la escuela ($USD)
**Situación Real:** En una urna hay 2 bolas azules ($A$), 3 bolas rojas ($R$) y 2 blancas ($B$). Participar cuesta **$1 USD** y el premio es de **$5 USD** si extraes una roja. ¿Es matemáticamente rentable?

1. **Espacio Muestral Detallado:** Aunque los colores se repiten, cada bola es un objeto único.
   $S = \{A_1, A_2, R_1, R_2, R_3, B_1, B_2\}$ 
   *Total de casos posibles = 7.*

2. **Evento Ganar ($G$):** Extraer una bola roja.
   $G = \{R_1, R_2, R_3\}$ 
   *Total de casos favorables = 3.*

3. **Cálculo:**
   $P(G) = \frac{3}{7} \approx 0.4285 \approx 42.85\%$.

**Análisis de Valor:** Tienes casi un 43% de probabilidad de ganar. En términos de inversión, estás arriesgando $1 por la posibilidad de ganar $5 con una probabilidad alta para ser un juego de azar. ¡Es una apuesta interesante!
````

---

## 3. ENTRENAMIENTO PRÁCTICO

````ad-abstract
title: 🟢 Nivel: Explorador (Fácil)
1. Determina el espacio muestral ($S$) del lanzamiento de una moneda usando las etiquetas $\{C, X\}$ (Cara y Cruz).
2. Si lanzas una moneda, define el conjunto del evento $E$: "Que salga Cara".
3. ¿Cuál es el número total de casos posibles al lanzar una moneda? Justifica tu respuesta.
````

````ad-abstract
title: 🟡 Nivel: Analista (Medio)
1. **Lanzamiento de dos monedas:** Escribe el espacio muestral completo. 
   *Pista pedagógica: Como son dos monedas, el total de resultados es $2 \times 2 = 4$. Usa pares como (C, X).*
2. Del ejercicio anterior, lista los elementos del evento $A$: "Que al menos una moneda sea Cruz".
3. **Combinación:** Si lanzas una moneda y un dado de 6 caras, ¿cuántos resultados posibles hay en total? (Ejemplo: $C1, C2...$). Haz la lista completa.
````

````ad-abstract
title: 🔴 Nivel: Experto (Avanzado — Aplicación $USD)
**El Casino de Naipes:** En una baraja francesa de 52 cartas (dividida en 4 palos: Corazones, Diamantes, Picas y Tréboles), apuestas **$10 USD** a que la carta extraída es un **As**.

1. Calcula la probabilidad de ganar ($P(As)$) en fracción simplificada. (Dato: Hay 4 ases en la baraja).
2. Expresa esa probabilidad en decimal (4 decimales) y porcentaje.
3. **Reto Comparativo:** Si apostaras a que la carta es del palo de **Tréboles** (hay 13 cartas de trébol), ¿cuál sería la probabilidad?
4. **Análisis Crítico:** Comparando ambos resultados, ¿cuál apuesta es más arriesgada para tus $10 USD? Justifica usando los porcentajes obtenidos.
````

---

> [!tip] 💡 Consejo de estudio del Profe
> ¡No confíes solo en tu memoria! Cuando trabajes con experimentos complejos como la baraja francesa (52 cartas) o lanzamientos múltiples, **dibuja diagramas de árbol o tablas**. 
> 
> Recuerda que la baraja tiene **4 palos**: dos rojos (Corazones ♥, Diamantes ♦) y dos negros (Picas ♠, Tréboles ♣). Cada palo tiene 13 cartas. Visualizar esta estructura te ayudará a no olvidar ningún "caso posible" al aplicar la Ley de Laplace.