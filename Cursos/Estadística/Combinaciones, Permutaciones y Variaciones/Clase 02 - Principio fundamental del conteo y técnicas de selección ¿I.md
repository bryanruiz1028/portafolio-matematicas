# Clase 02 — Principio fundamental del conteo y técnicas de selección: ¿Importa el orden?

tags: #algebra #fundamentalprin
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 6

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | | [[Clase 03|Clase 03 ➡]]

## 1. Importancia y Relevancia
Saber si el orden importa o no es como tener un superpoder para entender cómo funciona el mundo. No es solo para pasar el examen; es para tomar mejores decisiones.

- 💵 **Comprar inteligentemente ($USD):** Si tienes un presupuesto para videojuegos o ropa, saber cuántas combinaciones puedes armar te ayuda a que tu dinero rinda más.
- 🏗️ **Protegiendo tus cuentas:** ¿Alguna vez te has preguntado por qué te piden mayúsculas y números en tu clave de Instagram o Roblox? Es para que haya millones de combinaciones y nadie la adivine.
- 📊 **En tus hobbies:** Se usa para organizar desde un torneo de FIFA entre amigos hasta para saber cuántas pizzas diferentes puedes pedir en tu lugar favorito.

## 2. Concepto Clave: Principio de Multiplicación
¡Qué tal, amigos! Espero que estén muy bien. Hoy vamos a entender esto de una forma súper sencilla. Imaginen que tienen que realizar dos actividades seguidas.

**Definición:**
Si un evento $A$ puede ocurrir de $m$ formas y un evento $B$ de $n$ formas, el total de maneras en que pueden ocurrir ambos es $m \times n$. La clave es que los eventos ocurren juntos o uno tras otro; están conectados por la letra **"Y"**.

> [!warning] ⚠️ ¿Multiplicar o Sumar? (Eventos "O" vs "Y")
> Muchos se confunden aquí, pero es muy fácil si usas la lógica del transporte del video:
> - **Principio de Suma (Evento O):** Usamos la suma cuando las opciones son **excluyentes** (es decir, eliges una cosa o la otra, pero no las dos al tiempo). 
> 	- *Ejemplo:* Si para ir al colegio tienes $2$ bicicletas y $3$ rutas de bus, tienes $2 + 3 = 5$ formas de llegar. No te vas en bus y bici a la vez, ¿verdad?
> - **Principio de Multiplicación (Evento Y):** Usamos la multiplicación cuando los eventos ocurren simultáneamente. 
> 	- *Ejemplo:* Si tienes $3$ pantalones **Y** $4$ camisas, el total de pintas es $3 \times 4 = 12$.

**Truco para recordar:**
Para saber si debes multiplicar, busca la **"Y"**. La letra "y" parece una "x" de multiplicación que alguien estiró hacia arriba. **"Y" de Multiplicar.**

## 3. Procedimiento Paso a Paso para Identificar la Técnica
Antes de usar fórmulas locas, usa este "algoritmo mental" que te salvará la vida. Es la táctica de los dos pasos:

```text
PASO 1: ¿Importa el orden? 
        Táctica: Intercambia dos elementos. 
        ¿El resultado final es diferente? 
        - NO: Es una COMBINACIÓN (¡Ya terminaste!).
        - SÍ: El orden sí importa. Pasa al paso 2.

PASO 2: ¿Se usan TODOS los elementos del grupo?
        - SÍ: Es una PERMUTACIÓN.
        - NO (Solo algunos): Es una VARIACIÓN.
```

> [!tip] Atajo del Profe
> Cuando la respuesta es que **SÍ importa el orden**, puedes resolver casi todo usando el **"Método de las cajitas"**, sin necesidad de memorizar fórmulas de Variación.

## 4. Ejemplos de Aplicación

> [!example] Ejemplo 1: El equipo de clase (Variación)
> De un grupo de $8$ estudiantes, elegiremos un Presidente, un Vicepresidente y un Secretario.
> **Análisis:** ¿Importa el orden? **SÍ**. No es lo mismo ser el jefe (Presidente) que el que toma notas (Secretario). Como solo elegimos a $3$ de los $8$, es una Variación.

> [!example] Ejemplo 2: Claves seguras (Método de las cajitas)
> Diseñamos una clave con $3$ letras y $2$ números (usando $26$ letras y $10$ dígitos).
> **Visualización:**
> | Letra 1 | Letra 2 | Letra 3 | Número 1 | Número 2 |
> | :---: | :---: | :---: | :---: | :---: |
> | $[ 26 ]$ | $[ 26 ]$ | $[ 26 ]$ | $[ 10 ]$ | $[ 10 ]$ |
> 
> **Cálculo:** $26 \times 26 \times 26 \times 10 \times 10 = 1,757,600$ claves. El orden importa porque la clave "ABC12" no abre tu cuenta si pones "CBA21".

> [!example] Ejemplo 3: El almuerzo de amigos (Combinación)
> De $8$ amigos, seleccionamos a $3$ para un almuerzo gratis.
> **Análisis:** ¿Importa el orden? **NO**. Si eligen a Alex, Blanca y Carlos, los tres van a comer lo mismo. Si los nombran en otro orden, el grupo que se sienta a la mesa es exactamente el mismo. Es una **Combinación**.

> [!example] Ejemplo 4: Combos en el Mall ($USD)
> Tienes $15$ USD. Un combo trae $1$ hamburguesa (hay $3$ tipos) **Y** $1$ bebida (hay $4$ tipos). 
> **Análisis:** Aplicamos $m \times n$:
> $3 \text{ (hamburguesas)} \times 4 \text{ (bebidas)} = 12$ formas de armar tu combo. El precio no cambia cuántas opciones tienes, ¡pero sí te ayuda a saber qué puedes comprar!

## 5. Ejercicios Prácticos

### 🟢 Fácil (Principio de multiplicación simple)
1. Lanzas un dado de $6$ caras y una moneda. ¿Cuántos resultados hay?
2. Tienes $5$ pares de tenis y $3$ gorras diferentes. ¿De cuántas formas puedes combinarlos?
3. Un menú tiene $2$ opciones de sopa y $5$ de plato fuerte. ¿Cuántos almuerzos diferentes existen?
4. En un edificio hay $3$ puertas de entrada y $2$ ascensores. ¿De cuántas formas llegas al segundo piso?

### 🟡 Medio (Identificar si importa el orden)
5. Se eligen $2$ equipos de fútbol de entre $10$ para representar al país (ambos van al mismo torneo). ¿Importa el orden? ¿Qué técnica es?
6. En una carrera de $10$ carros, hay trofeos distintos para el 1er y 2do lugar. ¿Importa el orden? ¿Qué técnica es?
7. Un profesor elige a $3$ alumnos de $30$ para que lo ayuden a borrar el tablero. ¿Importa el orden?
8. Debes crear un código de $4$ colores usando $6$ colores disponibles. ¿Importa el orden?

### 🔴 Avanzado ($USD y selección múltiple)
9. **El helado del video:** Una heladería tiene $7$ sabores. Pides $3$ bolas en un vaso. Si no te importa cuál bola queda arriba o abajo (porque te las comerás todas igual), ¿cuántas combinaciones hay? (Pista: Es Combinación).
10. Tienes $50$ USD. Puedes elegir una mochila ($3$ modelos: $\$20, \$25, \$30$) **Y** una cartuchera ($2$ modelos: $\$5, \$10$). ¿Cuántas formas tienes de elegir tu equipo escolar?
11. Un bar de jugos cobra $\$5$ USD por batido. Tienes $5$ frutas y debes elegir $3$ para tu mezcla. ¿Cuántos batidos diferentes existen?
12. En un torneo de tenis con $4$ jugadores, apuestas $\$10$ USD a quién queda de 1er lugar y quién de 2do. ¿Cuántas apuestas diferentes puedes hacer?

> [!success] ✅ Soluciones (Haz clic para ver)
> 1. $12$ | 2. $15$ | 3. $10$ | 4. $6$ | 5. No importa (Combinación) | 6. Sí importa (Variación) | 7. No importa (Combinación) | 8. Sí importa (Variación) | 9. $35$ formas | 10. $6$ formas | 11. Combinación ($10$ formas) | 12. Variación ($12$ formas).

## 6. Autoevaluación (Mini-prueba)

> [!question] Pregunta 1
> Si al cambiar de posición dos elementos del grupo (como dos amigos en una lista para ir a cine), el resultado se considera "el mismo grupo", estamos ante:
> - a) Una Variación.
> - b) Una Permutación.
> - c) Una Combinación.
> - d) El Principio de Suma.

> [!question] Pregunta 2
> ¿Cuántas claves de $2$ letras se pueden formar si **no** se pueden repetir letras y el orden es importante? (Usa $26$ letras).
> - a) $52$
> - b) $650$
> - c) $676$
> - d) $26$

> [!question] Pregunta 3
> Tienes tres billetes de $\$5$ USD (todos diferentes por su serie) y dos billetes de $\$10$ USD (también diferentes). Si debes elegir un billete de $\$5$ **Y** uno de $\$10$ para pagarle a un amigo, ¿de cuántas formas puedes elegir los billetes?
> - a) $5$ formas.
> - b) $6$ formas.
> - c) $2$ formas.
> - d) $25$ formas.

*(Respuestas: 1-c, 2-b, 3-b)*

## 7. Cierre y Conexión

> [!tip] 💡 En la próxima clase
> Ya eres un experto identificando cuándo importa el orden. En la **Clase 03** daremos el siguiente paso: aprenderemos las fórmulas matemáticas para calcular **Combinaciones sin repetición**, para que puedas resolver ejercicios con grupos de $100$ o $200$ personas en segundos.

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | | [[Clase 03|Clase 03 ➡]]