# 📖 Guía de estudio — Clase 08: Solución de problemas con sistemas de ecuaciones lineales 2x2

¡Qué tal amigas y amigos! Espero que estén muy bien. Qué alegría saludarlos y ver que siguen con ese gran juicio aprendiendo matemáticas. Hoy vamos a convertirnos en expertos traduciendo situaciones de la vida real al lenguaje de las ecuaciones. ¡Empecemos de una vez!

> [!info] 📌 Conceptos clave
> *   **Nombres intuitivos de variables:** En lugar de usar siempre $x$ o $y$ (que a veces resultan un poco "despectivas" o frías), usamos letras que nos recuerden de qué hablamos (ej. $C$ para correctas, $A$ para Andrea). ¡Esto hace que al final no se nos olvide qué estábamos buscando!
> *   **Traducción al lenguaje algebraico:** Es el arte de convertir frases como "el doble de la edad" o "billetes de diez" en expresiones matemáticas.
> *   **Estrategia de reducción (eliminación):** Es nuestro método estrella. Buscamos que una variable tenga el mismo número pero signo diferente en ambas ecuaciones para "desaparecerla" al sumar.
> *   **Verificación lógica:** ¡Fundamental! No basta con que nos dé un número; debemos leer el problema original y ver si esos resultados tienen sentido en la historia que nos contaron.

## Fórmulas y Definiciones Importantes

A continuación, una tablita para que tengas a la mano los términos que usaremos en nuestra "super llave":

| Término | Definición / Fórmula |
| :--- | :--- |
| **Variable (Incógnita)** | Letra que representa un valor que no conocemos. Usar letras relacionadas al nombre del objeto facilita la interpretación final. |
| **Sistema 2x2** | Dos ecuaciones con dos incógnitas. Se deben organizar (letras bajo letras) dentro de una **llave {** para resolverlas juntas. |
| **Método de Reducción** | Multiplicar una ecuación para eliminar una variable. Recuerda: para despejar, es mejor decir **"dividir toda la ecuación"** entre el coeficiente. |
| **Verificación** | Proceso de comprobar los resultados no solo en las ecuaciones, sino en la lógica del **enunciado original**. |

---

## Ejemplos Resueltos Adicionales

````ad-example
title: Ejemplo A — Puntaje en un examen
**Problema:** En un test de 50 preguntas, Valentina obtuvo 152 puntos. Por cada acierto se suman 5 puntos y por cada fallo se restan 2 puntos. ¿Cuántas respondió bien y cuántas mal?

*   **Paso 1: Nombres de variables**
    *   $C$: Número de respuestas **C**orrectas.
    *   $I$: Número de respuestas **I**ncorrectas.
*   **Paso 2: Planteamiento de ecuaciones**
    1.  $C + I = 50$ (Total de preguntas respondidas).
    2.  $5C - 2I = 152$ (Puntos ganados menos puntos perdidos).
*   **Paso 3: Resolución por reducción**
    *   Multiplicamos la ecuación (1) por 2 para eliminar la $I$: $2C + 2I = 100$.
    *   Sumamos con la ecuación (2):
        $(2C + 5C) + (2I - 2I) = 100 + 152$
        $7C = 252$
    *   **Dividimos toda la ecuación entre 7:** $C = 252 / 7 \rightarrow \mathbf{C = 36}$.
    *   Si respondió 36 bien de 50 totales: $50 - 36 = \mathbf{I = 14}$.
*   **Paso 4: Resultado final**
    ✅ **Valentina respondió 36 preguntas correctas y 14 incorrectas.**
````

````ad-example
title: Ejemplo B — Compra con billetes de denominación específica
**Problema:** Se compró un computador de \$990 pagando con 65 billetes de \$10 y \$20. ¿Cuántos billetes de cada tipo se entregaron?

*   **Paso 1: Nombres de variables**
    *   $D$: Billetes de **D**iez dólares.
    *   $V$: Billetes de **V**einte dólares.
*   **Paso 2: Planteamiento de ecuaciones**
    1.  $D + V = 65$ (Total de billetes).
    2.  $10D + 20V = 990$ (Valor total del dinero).
*   **Paso 3: Resolución por reducción**
    *   Multiplicamos la ecuación (1) por -10: $-10D - 10V = -650$.
    *   Sumamos con la ecuación (2):
        $(-10D + 10D) + (-10V + 20V) = -650 + 990$
        $10V = 340$
    *   **Dividimos toda la ecuación entre 10:** $V = 34$.
    *   Sustituimos: $D + 34 = 65 \rightarrow \mathbf{D = 31}$.
*   **Paso 4: Resultado final**
    ✅ **Se entregaron 31 billetes de \$10 y 34 billetes de \$20.**
````

---

## Ejercicios de Repaso

```ad-abstract
title: 🟢 Fácil
1. Un hombre tiene 39 monedas en su bolsillo, unas de $2 y otras de $5. Si en total tiene $150, plantea el sistema para hallar cuántas tiene de cada una.
2. En una alcancía hay 20 monedas. Algunas son de $1 y otras de $2. Si el total ahorrado es $30, ¿cuántas monedas hay de $2?
3. Se compraron 10 artículos entre lápices ($2) y esferos ($5). Si se pagó en total $35, ¿cuántos lápices y esferos se compraron?
```

```ad-abstract
title: 🟡 Medio
*Pista: Para problemas de edades, define primero las edades actuales y luego escribe cómo serían en el futuro (ej. $A+7$) o pasado (ej. $C-4$) antes de armar la ecuación.*

1. Paola tiene 23 años más que su hija Andrea. Dentro de 7 años, la edad de Paola será el doble que la de Andrea. Calcula las edades actuales de ambas.
2. La edad de Valentina es el doble que la de su hermano Camilo. Hace 4 años, la edad de Valentina era el triple que la de Camilo. Halla sus edades actuales.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
1. **Reto Lógico:** Un computador cuesta $990 y se paga con 65 billetes de $10 y $20. Si el comprador hubiera entregado el doble de los billetes de $10 que calculaste originalmente (manteniendo igual los de $20), ¿cuánto dinero le sobraría después de pagar el computador?
2. **El caso de Felipe:** En un examen de 100 preguntas, Felipe dejó 3 sin responder. Obtuvo 151 puntos. Si por cada acierto se suman 3 puntos y por cada fallo se resta 1 punto, ¿cuántas respondió correctamente? (*Recuerda: las no respondidas no cuentan para el puntaje ni para el sistema de 2x2*).
```

---

> [!tip] 💡 Consejo de estudio
> ¡Excelente esfuerzo por llegar hasta aquí! Te felicito por tu dedicación. Un pequeño consejo de amigo: antes de rayar papel con álgebra, intenta un **cálculo lógico o mental**. Trata de estimar números que cumplan la primera condición y verifica si se acercan a la realidad del problema. Esto te dará "olfato matemático" para saber si tu respuesta final tiene sentido común. ¡Sigue así, qué juicio!