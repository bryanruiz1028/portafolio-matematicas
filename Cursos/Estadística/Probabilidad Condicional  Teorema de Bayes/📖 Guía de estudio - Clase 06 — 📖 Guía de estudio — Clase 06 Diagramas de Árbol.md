# 📖 Guía de estudio — Clase 06: Diagramas de Árbol

> [!info] 📌 Conceptos clave
> 1. **Definición Pedagógica:** Un diagrama de árbol es un mapa visual que desglosa todos los resultados posibles de un experimento. Se lee de izquierda a derecha, donde cada "nivel" representa un evento o paso cronológico.
> 2. **Lógica de Conectores:** 
>    - Se utiliza la **Regla de la Multiplicación** al recorrer un camino (Evento A **Y** Evento B).
>    - Se utiliza la **Regla de la Suma** al considerar diferentes caminos finales que cumplen una condición (Resultado 1 **O** Resultado 2).
> 3. **Independencia vs. Dependencia:**
>    - **Con reemplazo:** Los eventos son independientes. Las probabilidades se mantienen constantes en cada nivel.
>    - **Sin reemplazo:** Los eventos son dependientes. La primera extracción altera el espacio muestral para la segunda (si había $n$ objetos, ahora hay $n-1$).
> 4. **Check de Seguridad:** En cualquier nodo, la suma de las ramas que brotan de él **siempre** debe ser exactamente 1 (o 100%). Si la suma no coincide, el árbol está mal planteado.

## Fórmulas y definiciones importantes

| Término | Definición / Lógica Operativa |
| :--- | :--- |
| **Diagrama de Árbol** | Representación gráfica secuencial de un espacio muestral. Cada nodo es un punto de decisión o azar. |
| **Intersección (Y)** | La probabilidad de que ocurran varios eventos en cadena. Se calcula multiplicando las ramas: $P(A \cap B) = P(A) \times P(B \vert A)$. |
| **Unión (O)** | La probabilidad de que ocurra un resultado final u otro. Se calcula sumando las probabilidades totales de cada camino seleccionado. |
| **Eventos Dependientes** | Escenarios donde la probabilidad del segundo evento está condicionada por lo que ocurrió en el primero (típico en extracciones "sin reemplazo"). |

## Ejemplos resueltos

> [!example] Ejemplo A — Lanzamiento de dos monedas
> **Enunciado:** Se lanza una moneda dos veces. ¿Cuál es la probabilidad de obtener dos caras (C)?
> 
> **Visualización del Árbol:**
> - **Lanzamiento 1:**
> 	- Cara (1/2)
> 	- Sello (1/2)
> - **Lanzamiento 2 (si salió Cara en el primero):**
> 	- Cara (1/2) → **Camino: C y C**
> 	- Sello (1/2)
> 
> **Cálculo:**
> Multiplicamos las probabilidades del camino deseado:
> $P(C \cap C) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$
> 
> ✅ **Resultado:** 1/4 = **0.25** = **25%**. 
> *Nota: Como los eventos son independientes, la probabilidad de la segunda moneda no cambia.*

> [!example] Ejemplo B — Moneda y Dado (Premio $USD)
> **Enunciado:** Un juego paga un premio si al lanzar una moneda y un dado obtienes "Cara" **Y** un número mayor a 3. ¿Cuál es la probabilidad de ganar?
> 
> **Desglose Pedagógico:**
> 1. **Probabilidad Moneda (Cara):** $P(C) = 1/2$.
> 2. **Probabilidad Dado (>3):** Los números a favor son $\{4, 5, 6\}$. 
>    $P(>3) = \frac{\text{casos a favor}}{\text{casos totales}} = \frac{3}{6} = \frac{1}{2}$.
> 3. **Cálculo de la Intersección:**
>    $P(\text{Ganar}) = P(C) \times P(>3) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$.
> 
> ✅ **Resultado:** 1/4 o **25%** de probabilidad de ganar el premio.

## Ejercicios de repaso

> [!abstract] 🟢 Nivel: Inicial
> 1. Dibuja el diagrama de árbol para el lanzamiento de 3 monedas. Calcula la probabilidad de que los tres resultados sean idénticos (C-C-C o S-S-S).
> 2. Si un nodo tiene tres ramas y dos de ellas suman 0.75, ¿cuál es la probabilidad de la tercera rama para que el diagrama sea válido?
> 3. En el lanzamiento de una moneda, calcula la probabilidad de obtener Cara **Y** luego Sello.

> [!abstract] 🟡 Nivel: Medio
> 1. Una urna contiene 3 bolas rojas y 4 azules. Si se extraen dos bolas **con reemplazo**, ¿cuál es la probabilidad de que ambas sean del mismo color? (Recuerda: puede ser Roja-Roja **O** Azul-Azul).
> 2. En el experimento de moneda y dado, calcula la probabilidad de obtener "Sello" **Y** un número par en el dado.
> 3. Utilizando un diagrama de árbol, demuestra por qué la probabilidad de obtener "al menos una cara" en dos lanzamientos es del 75%.

> [!abstract] 🔴 Nivel: Avanzado (Aplicación Financiera)
> 1. **Riesgo de Inversión:** Una urna tiene 5 bolas rojas y 4 azules. Un jugador paga **$10 USD** para entrar al juego y extraer dos bolas **sin reemplazo**. Si extrae dos bolas rojas, recupera su dinero y gana un premio. ¿Cuál es la probabilidad exacta de ganar? *(Ojo: en la segunda extracción quedan 8 bolas en total).* (R: 5/18)
> 2. En el escenario anterior (sin reemplazo), ¿cuál es la probabilidad de obtener una bola de cada color en cualquier orden? (R: 5/9)
> 3. **Análisis de Recompensa:** Si el premio por sacar dos bolas azules (sin reemplazo) es de **$50 USD**, pero la probabilidad de lograrlo es baja, calcúlala primero para decidir si vale la pena el riesgo de los $10 USD de entrada. (R: 1/6 o 16.6%)

> [!tip] 💡 Error común a evitar
> El error más frecuente en eventos **sin reemplazo** es no reducir el denominador en el segundo nivel del árbol. Si empiezas con 9 bolas totales, las ramas del segundo nivel deben tener siempre un denominador de 8, ya que una bola ya ha sido extraída y no "regresa" al espacio muestral.