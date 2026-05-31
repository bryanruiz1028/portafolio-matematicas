# Clase 06 — Diagramas de Árbol: Probabilidad Paso a Paso

tags: #algebra #diagramaderbol
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 6 de 9

> [!info] 🧭 Navegación
> [[Clase 05 — Probabilidad Simple]] | **Clase 06 — Diagramas de Árbol** | [[Clase 07 — Probabilidad Condicional]]

## ¿Por qué es importante esta clase?
El diagrama de árbol es una herramienta visual que nos permite organizar de forma lógica todos los resultados posibles de un experimento, facilitando la comprensión del **espacio muestral**. Su dominio es clave para:

*   💵 **Finanzas:** Calcular el riesgo en inversiones de múltiples etapas (ej. si el mercado sube en el paso A, ¿qué probabilidad hay de que baje en el paso B?).
*   🏗️ **Control de Calidad:** Identificar la probabilidad de fallos en procesos de producción donde una pieza debe superar varias estaciones de inspección.
*   📊 **Vida Cotidiana:** Tomar decisiones informadas, como elegir la ruta de transporte más eficiente analizando transbordos y posibles retrasos.

> [!note] 📌 ¿Qué es un Diagrama de Árbol?
> Imagina que estás frente a un mapa de caminos. Cada vez que llegas a un cruce, tienes que elegir hacia dónde ir. Un diagrama de árbol es un dibujo que muestra todos esos caminos posibles y hacia dónde te llevan. Es como dibujar las ramas de un árbol para visualizar todas las formas en las que un juego o un experimento pueden terminar.

> [!warning] ⚠️ Error común
> Un error frecuente es olvidar que la suma de las probabilidades en las **ramas** que nacen de un mismo punto (**nodos**) siempre debe ser igual a 1. Además, recuerda que al avanzar por un camino debes multiplicar las probabilidades, no sumarlas.

> [!tip] 💡 Truco para recordarlo
> Utiliza la "Regla de los Sentidos" que aprendimos en los videos:
> *   Si sigues el camino hacia adelante (ramas sucesivas), **MULTIPLICAS**.
> *   Si juntas varios caminos finales que te sirven, **SUMAS** los resultados.

## Procedimiento paso a paso

```text
PASO 1: Identificar los eventos sucesivos (ej. primer lanzamiento, segundo lanzamiento).
PASO 2: Dibujar las ramas iniciales para el primer evento y asignar su probabilidad en fracción.
PASO 3: Ramificar los eventos subsiguientes desde cada final anterior (nodos).
PASO 4: Multiplicar las probabilidades a lo largo de cada "camino" para obtener la probabilidad total.
```

**Nota del experto:** Al movernos horizontalmente por las **ramas**, estamos calculando la **intersección** (Evento A Y Evento B). Matemáticamente, la palabra "Y" se traduce como una multiplicación, lo que genera una **probabilidad compuesta**.

## Ejemplos de clase

> [!example] Ejemplo 1: El Lanzamiento de 2 Monedas (Básico)
> Al lanzar dos monedas, cada una tiene una probabilidad de $1/2$ para cara (C) y $1/2$ para sello (S). Estos son **eventos independientes**.
> *   **Ruta para "Cara y Cara":** Tomamos la rama de la primera moneda ($1/2$) y la multiplicamos por la rama de la segunda ($1/2$).
> *   **Cálculo:** $1/2 \times 1/2 = 1/4$.
> *   **Resultado:** La probabilidad de obtener dos caras es del **25%**.

> [!example] Ejemplo 2: Moneda y Dado (Combinado)
> ¿Cuál es la probabilidad de obtener "Cara y el número 3"?
> *   **Evento 1 (Moneda):** Probabilidad de Cara = $1/2$.
> *   **Evento 2 (Dado):** Probabilidad de sacar un 3 = $1/6$.
> *   **Cálculo:** $1/2 \times 1/6 = 1/12$.
> *   **Resultado:** Aproximadamente **8.3%**.
> *   *Recordatorio:* No olvides que el dado tiene 6 caras; el denominador siempre representa el total del **espacio muestral**.

> [!example] Ejemplo 3: Urna Sin Reemplazo (Avanzado)
> Tenemos una urna con 5 bolas rojas y 4 azules (Total = 9). Extraemos dos bolas **sin reemplazo**. Esto crea **eventos dependientes**.
> *   **Primera bola roja:** La probabilidad es $5/9$.
> *   **Segunda bola roja:** Al no devolver la primera bola, dejamos un "huequito" en la urna. Ahora quedan solo 4 bolas rojas "favorables" y un total de 8 bolas. La probabilidad es $4/8$.
> *   **Cálculo:** $5/9 \times 4/8 = 20/72$.
> *   **Simplificación:** $5/18$ (aprox. 27.7%).

> [!example] Ejemplo 4: Rentabilidad en $USD
> Un juego cuesta **$20 USD** de entrada. Si lanzas dos monedas y obtienes "Cara-Cara", ganas **$100 USD**. ¿Vale la pena jugar?
> *   **Análisis:** La probabilidad de "Cara-Cara" es $1/4$ (25%).
> *   **Interpretación:** Esto significa que ganarás 1 de cada 4 veces.
> *   **Ganancia Neta:** Si juegas 4 veces, inviertes $80 USD ($20 \times 4) y recibes $100 USD (el premio de la única vez que ganas). Al final, tienes una **ganancia neta de $20 USD** sobre 4 juegos ($5 USD por juego).
> *   **Conclusión:** El juego es estadísticamente rentable.

## Ejercicios para el estudiante

> [!abstract] 🟢 Nivel Fácil: Monedas
> 1. Dibuja el diagrama de árbol para el lanzamiento de 2 monedas.
> 2. ¿Cuál es la probabilidad de obtener al menos un Sello?
> 3. ¿Cuál es la probabilidad de que ambas monedas caigan del mismo lado?
> 4. ¿Cuál es la probabilidad de obtener "Sello-Cara" en ese orden exacto?

> [!abstract] 🟡 Nivel Medio: Moneda y Dado
> 1. Calcula la probabilidad de obtener "Sello y un número par".
> 2. Calcula la probabilidad de obtener "Cara y un número menor que 3".
> 3. ¿Cuántos resultados posibles totales existen en este diagrama?
> 4. ¿Qué es más probable: sacar "Cara y el 6" o "Sello y un número impar"?

> [!abstract] 🔴 Nivel Avanzado: Urnas y $USD
> En una urna hay 5 bolas rojas y 4 azules. Extraes dos bolas **con reemplazo**.
> 1. Calcula la probabilidad de que ambas sean rojas.
> 2. Calcula la probabilidad de sacar exactamente una de cada color (en cualquier orden).
> 3. **Problema $USD:** Un seguro contra "Pérdida por Azules" cuesta $10 USD. Si extraes dos bolas azules (con reemplazo), el seguro te paga $50 USD. ¿Es este un negocio rentable para la aseguradora a largo plazo?
> 4. Si el experimento fuera **sin reemplazo**, ¿cuál sería la probabilidad de sacar dos rojas?

## Respuestas para el docente

> [!success] Solucionario
> *   **Fácil:** 2) $3/4$ (75%); 3) $2/4 = 1/2$ (50%); 4) $1/4$ (25%).
> *   **Medio:** 1) $1/2 \times 3/6 = 3/12 = 1/4$ (25%); 2) $1/2 \times 2/6 = 2/12 = 1/6$ (16.6%); 3) 12 resultados; 4) "Sello e impar" ($1/4$) es más probable que "Cara y 6" ($1/12$).
> *   **Avanzado:**
>     1. $5/9 \times 5/9 = 25/81$ (30.8%).
>     2. $(5/9 \times 4/9) + (4/9 \times 5/9) = 40/81$ (49.3%).
>     3. Probabilidad (Azul-Azul) = $4/9 \times 4/9 = 16/81$. Pago esperado: $16/81 \times \$50 = \$9.87$. Como el pago esperado ($9.87) es menor que la prima ($10), la aseguradora gana dinero.
>     4. $5/9 \times 4/8 = 5/18$ (27.7%).

## Mini-Prueba de Autoevaluación

> [!question] Pregunta 1: Teoría
> Si un nodo tiene tres ramas y dos de ellas tienen probabilidades de 0.2 y 0.5, ¿cuál es la probabilidad de la tercera rama?

> [!question] Pregunta 2: Cálculo
> En el experimento Moneda + Dado, ¿cuál es la probabilidad exacta de sacar "Sello y un 5"?

> [!question] Pregunta 3: Aplicación $USD
> Una urna tiene 3 bolas rojas y 4 azules. Extraes dos con reemplazo. Si pagas $15 USD por participar y el premio por sacar "dos azules" es de $70 USD, ¿es este un juego justo para el jugador? (Calcula la probabilidad primero).

> [!tip] 💡 En la próxima clase
> Ahora que dominas el arte de dibujar rutas, veremos qué ocurre cuando el primer resultado altera drásticamente las opciones del segundo. Nos sumergiremos en la **Probabilidad Condicional** y analizaremos a fondo los desafíos **sin reemplazo**.

> [!info] 🧭 Navegación
> [[Clase 05 — Probabilidad Simple]] | **Clase 06 — Diagramas de Árbol** | [[Clase 07 — Probabilidad Condicional]]