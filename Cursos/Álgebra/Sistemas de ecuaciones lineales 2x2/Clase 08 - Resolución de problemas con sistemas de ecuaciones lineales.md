# Clase 08 — Resolución de problemas con sistemas de ecuaciones lineales 2x2

tags: #algebra #solvingproblems

[[Clase 07]] | [[Índice]]

---

> [!info] 🌍 ¡Qué tal amigas y amigos! ¿Por qué esto es importante?
> ¿Alguna vez has contado las monedas que tienes en el bolsillo o has intentado calcular cuántas preguntas debías responder bien para pasar un examen? ¡Para eso sirven los sistemas 2x2! No son solo números en un papel, son situaciones que te pasan a ti todos los días.
> - **En tus finanzas:** Para saber exactamente cuántos billetes de cada valor tienes sin tener que contarlos uno por uno.
> - **En tus exámenes:** Para entender cómo los aciertos y los errores afectan tu puntaje final.
> - **En el tiempo:** Para descubrir edades ocultas basándote en cómo pasan los años para todos.

---

> [!note] 📌 ¿Qué es resolver un problema con sistemas 2x2?
> Es como "traducir" una historia de nuestro idioma al lenguaje de las matemáticas. El secreto del Profe Alex es **darle nombre a las incógnitas**: en lugar de usar siempre $x$ o $y$, usamos letras que nos recuerden de qué hablamos (como $C$ para "Correctas"). Resolverlo es encontrar esos dos valores que hacen que toda la historia tenga sentido.

> [!warning] ⚠️ Cuidado con este error común
> Al usar el método de reducción, muchos estudiantes olvidan multiplicar **toda** la ecuación. Si eliges multiplicar por -2, debes multiplicar la primera letra, la segunda letra **y también el número que está después del igual**. Si olvidas el número independiente, ¡el resultado será un caos!

> [!tip] 💡 Truco para no perderte
> ¡Usa letras sugerentes! Si el problema habla de monedas de **D**os y monedas de **C**inco, usa $D$ y $C$. Así, cuando al final obtengas $C = 24$, sabrás de inmediato que tienes 24 monedas de cinco, sin tener que volver a leer todo el problema.

---

### PROCEDIMIENTO PASO A PASO

Para resolver cualquier reto, sigue este camino sistemático:

```text
1. Identificar y nombrar incógnitas: Usa letras iniciales (Ej: B para Billetes).
2. Traducir al lenguaje algebraico: Escribe las 2 ecuaciones que cuenta la historia.
3. Resolver por el método de reducción: Multiplica para eliminar una variable y despejar la otra.
4. Verificar con la lógica del problema: ¡No solo con la ecuación! Mira si los números encajan en el relato original.
```

---

### EJEMPLOS PRÁCTICOS

> [!example] Ejemplo 1: El caso de las monedas (Nivel Básico)
> Un hombre tiene 39 monedas en su bolsillo: unas de $2 y otras de $5. Si en total tiene $150, ¿cuántas tiene de cada una?
> 
> **1. Nombres:** $D = \text{monedas de dos}$, $C = \text{monedas de cinco}$.
> **2. Ecuaciones:**
> - Cantidad: $D + C = 39$
> - Dinero: $2D + 5C = 150$
> **3. Reducción:** Multiplicamos la Ec. 1 por $-2$:
>   $-2D - 2C = -78$
>   $2D + 5C = 150$
>   Suma: $3C = 72 \rightarrow C = 24$
> **4. Verificación lógica:** Si tiene 24 monedas de $5 ($120) y 15 monedas de $2 ($30), sumamos $120 + 30 = 150$. ¡Exacto!
> **Resultado:** 15 monedas de $2 y 24 monedas de $5.

> [!example] Ejemplo 2: El examen de Valentina (Signos opuestos)
> En un test de 50 preguntas, Valentina obtuvo 152 puntos. Cada acierto suma 5 puntos y cada fallo resta 2.
> 
> **1. Nombres:** $C = \text{correctas}$, $I = \text{incorrectas}$.
> **2. Ecuaciones:**
> - Total preguntas: $C + I = 50$
> - Puntaje: $5C - 2I = 152$ (Restamos $2I$ porque los fallos quitan puntos).
> **3. Reducción:** Multiplicamos la Ec. 1 por $2$:
>   $2C + 2I = 100$
>   $5C - 2I = 152$
>   Suma: $7C = 252 \rightarrow C = 36$
> **4. Verificación:** 36 correctas (180 pts) menos 14 incorrectas (28 pts) nos da 152. ¡Perfecto!
> **Resultado:** 36 correctas y 14 incorrectas.

> [!example] Ejemplo 3: Edades de Paola y Andrea (Nivel Avanzado)
> Paola tiene 23 años más que su hija Andrea. Dentro de 7 años, la edad de Paola será el doble que la de Andrea.
> 
> **1. Nombres:** $P = \text{Paola (actual)}$, $A = \text{Andrea (actual)}$.
> **2. Ecuaciones:**
> - Relación actual: $P = A + 23 \rightarrow \mathbf{P - A = 23}$ (Ec. 1 ordenada).
> - En 7 años: $(P + 7) = 2(A + 7)$
> **3. Simplificación (Paso clave):**
>   $P + 7 = 2A + 14$ (Aplicamos propiedad distributiva $2 \times A$ y $2 \times 7$).
>   $P - 2A = 14 - 7 \rightarrow \mathbf{P - 2A = 7}$ (Ec. 2 ordenada).
> **4. Reducción:** Cambiamos signos a la Ec. 2:
>   $P - A = 23$
>   $-P + 2A = -7$
>   Suma: $A = 16$. Si Andrea tiene 16, Paola tiene $16+23=39$.
> **Resultado:** Andrea tiene 16 años y Paola 39 años.

> [!example] Ejemplo 4: Compra de computadora ($USD)
> Se compró una computadora de $990 con 65 billetes de $10 y $20.
> 
> **1. Nombres:** $D = \text{billetes de 10}$, $V = \text{billetes de 20}$.
> **2. Ecuaciones:**
> - Cantidad: $D + V = 65$
> - Dinero: $10D + 20V = 990$
> **3. Reducción:** Multiplicamos la Ec. 1 por $-10$:
>   $-10D - 10V = -650$
>   $10D + 20V = 990$
>   Suma: $10V = 340 \rightarrow V = 34$
> **4. Verificación:** 34 billetes de $20 ($680) + 31 billetes de $10 ($310) = $990.
> **Resultado:** 31 billetes de $10 y 34 billetes de $20.

---

### EJERCICIOS PARA EL ESTUDIANTE

> [!abstract] 📝 Hoja de Trabajo
> 
> **Nivel Verde (Fácil)**
> 1. Un joven tiene 45 monedas de $1 y $2. Si suma $70 en total, ¿cuántas monedas tiene de cada una?
> 2. En una alcancía hay 60 monedas de $5 y $10, sumando un total de $450.
> 3. Se pagó una cuenta de $200 con 25 billetes de $5 y $10. ¿Cuántos de cada uno se entregaron?
> 4. Un sobre contiene 30 billetes de $20 y $50. Si el total es $1140, ¿cuántos billetes hay de cada uno?
> 
> **Nivel Amarillo (Medio)**
> 1. Felipe presentó un examen de 100 preguntas. Dejó 3 sin responder (es decir, **solo respondió 97**). Por cada acierto suma 3 puntos y por cada error resta 1. Si obtuvo 151 puntos, ¿cuántas respondió bien?
> 2. En un concurso, cada acierto gana 10 puntos y cada error pierde 5. Tras 20 preguntas, el puntaje es 125.
> 3. Un estudiante responde 40 preguntas; gana 4 puntos por acierto y pierde 1 por error. Su nota es 100.
> 4. En un test de 80 ítems, cada acierto vale 2 puntos y cada fallo quita 0.5. Puntaje final: 110.
> 
> **Nivel Rojo (Avanzado)**
> 1. Valentina tiene el doble de edad que su hermano Camilo. Hace 4 años, la edad de Valentina era el triple que la de Camilo. Calcula las edades actuales.
> 2. La suma de las edades de dos hermanos es 30. Dentro de 5 años, el mayor duplicará la edad que el menor tenía hace 2 años.
> 3. Un padre tiene 40 años y su hijo 10. ¿Cuántos años deben pasar para que el padre tenga el triple de edad que el hijo?
> 4. La diferencia de edad entre dos primos es de 15 años. Hace 10 años, el mayor tenía el cuádruple de la edad del menor.

> [!success] ✅ Respuestas para verificar
> - **Monedas Fácil:** (1) 20 de $1 y 25 de $2.
> - **Felipe (Examen):** 62 correctas y 35 incorrectas. (Recuerda: $C + I = 97$).
> - **Valentina y Camilo:** Camilo tiene 8 años y Valentina tiene 16 años.

---

### MINI-PRUEBA DE AUTOEVALUACIÓN

> [!question] Pregunta 1: Conceptual
> ¿Por qué es fundamental que las ecuaciones estén "ordenadas" (letras alineadas) antes de sumar?
> > [!success] Respuesta
> > Porque el método de reducción solo funciona si sumas "peras con peras" y "manzanas con manzanas". Si las letras no están alineadas, no podrás eliminar ninguna variable.

> [!question] Pregunta 2: Procedimental
> En un sistema de billetes de $10 ($D$) y $20 ($V$), si tengo la ecuación $D + V = 65$, ¿qué gano al multiplicarla por $-10$?
> > [!success] Respuesta
> > Obtienes $-10D$, que al sumarse con el $10D$ de la ecuación de dinero, se eliminará por completo, permitiéndote encontrar el valor de $V$ rápidamente.

> [!question] Pregunta 3: Aplicación rápida
> Si tengo 10 billetes en total ($10 y $5) y sumo $85, ¿cuántos tengo de $10?
> > [!success] Respuesta
> > Tienes 7 billetes de $10 ($70) y 3 de $5 ($15). ¡Mentalmente también se puede!

---

> [!tip] 💡 ¡Excelente trabajo!
> Me alegra mucho que hayas llegado hasta aquí. Has demostrado que puedes tomar problemas de la vida real y dominarlos con el álgebra. ¡Felicidades! Has completado el bloque de sistemas 2x2. En la próxima clase, exploraremos nuevos horizontes algebraicos. ¡Sigue con ese mismo juicio!

[[Clase 07]] | [[Índice]]