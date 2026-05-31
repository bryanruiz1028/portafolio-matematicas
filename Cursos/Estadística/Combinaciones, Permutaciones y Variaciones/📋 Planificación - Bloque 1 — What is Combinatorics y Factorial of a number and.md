# Planificación Didáctica — What is Combinatorics y Factorial of a number and its properties

tags: #planificacion #dua #whatiscombinato  
Nivel: Básica Superior (12–15 años) | Duración: 80 minutos

---

## 1. Tema
What is Combinatorics y Factorial of a number and its properties

---

## 2. Metodología
Se implementará el enfoque de **Aprendizaje Colaborativo Formal**, organizando a los estudiantes en "estaciones de resolución" y parejas heterogéneas. La mediación docente se centrará en guiar la discusión heurística sobre la relevancia del orden en diversos arreglos, utilizando el razonamiento lógico derivado del "método de las cajitas". Los estudiantes deberán discernir de forma autónoma si un evento es una combinación, variación o permutación basándose en el análisis de la población ($n$) y la muestra ($r$).

---

## 3. Secuencia Didáctica

### 🔵 ANTICIPACIÓN — 20 min

> [!abstract] Actividad de inicio
> 1. **Modelado de Espacio Muestral:** Iniciamos con el lanzamiento de dos monedas de uso común. Los estudiantes deben identificar todas las posibilidades (Cara-Cara, Cara-Cruz, Cruz-Cara, Cruz-Cruz). Se introduce el **Principio Fundamental del Conteo** observando que $2 \times 2 = 4$ resultados posibles.
> 2. **El Reto de los Vehículos:** Utilizando materiales del aula, se pide a los estudiantes que imaginen tres carros (rojo, azul y negro) haciendo fila en un estacionamiento. Deben listar todas las formas posibles de ordenarlos. Tras el ejercicio, el docente aclarará que existen exactamente **6 permutaciones** posibles ($3 \times 2 \times 1$).
> 3. **Pregunta Detonadora:** "¿Cómo podríamos calcular las formas de organizar 10 carros o 30 estudiantes en una fila sin tener que listar cada opción manualmente?".

> [!note] Enfoque DUA
> - **Qué:** Activar conocimientos previos sobre el conteo lógico y el espacio muestral.
> - **Cómo:** Realizar la actividad de forma grupal en plenaria, utilizando la pizarra para representar visualmente los resultados de las monedas y los carros.
> - **Por qué:** Proporcionar múltiples medios de representación para que el concepto de "orden" sea concreto antes de la formalización matemática.

---

### 🟡 CONSTRUCCIÓN — 40 min

> [!example] Actividades centrales
> 1. **Definición de Factorial y Variables:** Se define el factorial de un número ($n!$) como la secuencia multiplicativa descendente hasta la unidad (ej. $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$). Se formalizan las variables: **$n$ (Población total)** y **$r$ (Muestra o elementos seleccionados)**. Se destaca la propiedad fundamental $n! = n \times (n-1)!$, esencial para simplificar cálculos complejos.
> 2. **El Método de las Cajitas:** Se aplica esta lógica multiplicativa en dos escenarios:
>    - **Permutaciones (Carrera):** Para 5 corredores, se dibujan 5 cajitas. En la primera hay 5 opciones, en la segunda 4, y así hasta completar $5!$.
>    - **Variaciones con repetición (Placas):** Se analiza el diseño de una placa con 2 letras y 1 dígito ($26 \times 26 \times 10$). Se explica que aquí el orden importa y los elementos pueden repetirse.
> 3. **Árbol de Decisión:** Se introducen las preguntas críticas:
>    - *¿Importa el orden?* Si la respuesta es **SÍ**, es una Variación o Permutación (se usa el método de las cajitas). Si es **NO**, es una Combinación (donde el resultado se divide por $r!$ para eliminar duplicados).
>    - *¿Se usan todos los elementos?* Si $n = r$, hablamos de una Permutación; si $n > r$, es una Variación.

> [!note] Enfoque DUA
> - **Qué:** Construcción de fórmulas de conteo a partir de la lógica de multiplicación.
> - **Cómo:** Trabajo en parejas utilizando fichas físicas que representen los elementos ($n$) para ser colocados táctilmente en las "cajitas" de decisión.
> - **Por qué:** Ofrecer opciones para la acción y la expresión mediante el uso de manipulativos físicos que refuercen la comprensión del principio multiplicativo.

---

### 🟢 CONSOLIDACIÓN — 20 min

> [!success] Actividad de cierre
> 1. **Reto Comparativo:** Los estudiantes deben resolver dos problemas contrastantes:
>    - *Caso A:* Seleccionar un "Comité de 3 estudiantes de un grupo de 10" (No importa el orden $\rightarrow$ Combinación).
>    - *Caso B:* Elegir "Presidente, Vicepresidente y Secretario de un grupo de 10" (Sí importa el orden $\rightarrow$ Variación).
> 2. **Simplificación Factorial:** Se entrena la habilidad de simplificar fracciones factoriales para agilizar resultados, por ejemplo: $\frac{10!}{7!} = 10 \times 9 \times 8 = 720$.
> 3. **Análisis Final:** Breve discusión sobre el caso de los "Sabores de Helado". ¿Si pido vainilla y chocolate, el orden en que se colocan las bolas cambia el helado? Se concluye que es una combinación.

> [!note] Enfoque DUA
> - **Qué:** Aplicación de conceptos en contextos reales y toma de decisiones lógicas.
> - **Cómo:** Evaluación formativa mediante una hoja de trabajo con problemas diversificados (deportes, comités, combinaciones de sabores).

---

## 4. Recursos

| Recurso | Tipo | Uso en la clase |
| :--- | :--- | :--- |
| Pizarra | Físico | Modelado del "método de las cajitas" y desarrollo de fórmulas. |
| Marcadores | Físico | Codificación por colores para diferenciar $n$ (población) de $r$ (muestra). |
| Fichas | Manipulativo | Representar físicamente los objetos para "llenar" las cajitas de decisión. |
| Monedas | Físico | Demostración táctil del espacio muestral y el principio multiplicativo. |
| Guía de Ejercicios | Impreso | Problemas basados en los casos de Alex: helados, placas, comités y carreras. |