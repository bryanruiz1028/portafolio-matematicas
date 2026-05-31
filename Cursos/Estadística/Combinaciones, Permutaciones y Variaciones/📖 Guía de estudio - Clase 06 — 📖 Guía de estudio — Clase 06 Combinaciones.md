# 📖 Guía de estudio — Clase 06: Combinaciones

> [!info] 📌 Conceptos clave
> *   **La Regla de Oro:** En las combinaciones **no importa el orden**. Si al intercambiar los elementos el resultado es el mismo grupo (ej. Equipo A vs Equipo B es lo mismo que B vs A), estamos ante una combinación.
> *   **Diferenciación:** A diferencia de las variaciones o permutaciones, aquí lo único que nos interesa es la selección de los integrantes, no su posición o jerarquía.
> *   **Combinación sin repetición:** Se aplica cuando los elementos son únicos y no pueden ser seleccionados más de una vez para formar un mismo grupo (como elegir personas para un comité o números en un sorteo).
> *   **Identificación de variables:** Es fundamental determinar correctamente **$n$** (el total de elementos disponibles o población) y **$r$** (la cantidad de elementos que tomaremos para nuestro grupo o muestra).

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Combinación ($C$ o $nCr$)** | Técnica de conteo donde el orden no influye en el resultado. Se expresa como: $$C(n, r) = \binom{n}{r} = \frac{n!}{r! (n-r)!}$$ |
| **$n$ (Población)** | El número total de objetos o personas disponibles para elegir. |
| **$r$ (Muestra)** | El número de elementos que formarán el subgrupo seleccionado. |
| **Factorial (!)** | Producto de números enteros descendentes. Según el **"Método de Simplificación de Profe Alex"**, se debe descomponer el factorial mayor del numerador hasta alcanzar el factorial más grande del denominador para cancelarlos directamente y facilitar el cálculo manual. |

## Ejemplos Resueltos Adicionales

````ad-example
title: Ejemplo A — Torneo de equipos
**Problema:** En un torneo con 16 equipos, todos juegan contra todos en una sola cancha. ¿Cuántos partidos se jugarán?

1.  **Identificación:** $n = 16$ (equipos totales); $r = 2$ (un partido requiere 2 equipos).
2.  **Prueba del orden:** *¿Es el partido Equipo A vs Equipo B distinto al partido B vs A?* No, es el mismo encuentro. **Orden no importa = Combinación.**
3.  **Planteamiento:** $C(16, 2) = \frac{16!}{2!(16-2)!} = \frac{16!}{2! \cdot 14!}$
4.  **Simplificación (Método Alex):** Descomponemos el 16 hasta llegar al 14:
    $$\frac{16 \cdot 15 \cdot 14!}{2 \cdot 1 \cdot 14!} = \frac{16 \cdot 15}{2}$$
5.  **Resultado:** $8 \cdot 15 = 120$ partidos. ¡Así de sencillo es organizar un torneo!
````

````ad-example
title: Ejemplo B — Probabilidades en la Lotería
**Problema:** Un juego de lotería requiere elegir 6 números entre el 1 y el 49. ¿Cuántas combinaciones posibles existen?

1.  **Identificación:** $n = 49$; $r = 6$. Marcar el 5 y luego el 8 es igual a marcar el 8 y luego el 5.
2.  **Cálculo:** Aplicamos $C(49, 6)$. Al simplificar el $49!$ hasta el $43!$, realizamos las operaciones restantes.
3.  **Resultado:** Existen exactamente **13,983,816** combinaciones posibles.
4.  **Reflexión Pedagógica:** Para garantizar ganar, deberías comprar casi 14 millones de cartones. Como indica el autor, si el costo de los cartones supera el premio, **no es un juego rentable**. La matemática nos ayuda a tomar mejores decisiones financieras.
````

## Ejercicios de Repaso

````ad-abstract
title: 🟢 Fácil
*¡Comencemos con lo básico para calentar motores! En estos casos, solo debes aplicar la fórmula directa.*

1.  Tienes un estante con 6 libros de matemáticas y quieres llevarte 2 para estudiar el fin de semana. ¿De cuántas formas puedes elegirlos?
2.  Si hay 3 libros de física disponibles y solo puedes seleccionar 2, ¿cuántas combinaciones diferentes puedes formar?
3.  Un estudiante debe elegir 3 libros de historia de una colección de 5. ¿Cuántas opciones de selección tiene?
````

````ad-abstract
title: 🟡 Medio
*💡 **Pro-tip:** Cuando veas la conjunción "y" (ej. hombres **y** mujeres), significa que debes calcular las combinaciones por separado y luego **multiplicar** los resultados.*

1.  **Comisión Mixta:** Se requiere formar un equipo con 5 hombres (de un total de 12) **y** 5 mujeres (de un total de 10). ¿Cuántas comisiones distintas se pueden crear?
2.  **Selección de Biblioteca:** Un alumno elige 2 libros de matemáticas entre 6 disponibles **y** 2 libros de física entre 3 disponibles. Calcula el total de opciones.
3.  **Consejo Escolar:** El grupo A tiene 7 miembros, el B tiene 10 y el C tiene 9. Si se debe elegir una comisión con 3 miembros de cada grupo, ¿cuántas formas posibles existen?
````

````ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
*💡 **Pro-tip:** Recuerda aplicar el principio multiplicativo en problemas complejos. ¡Atención a los totales!*

1.  **Inversión en Naipes:** En una baraja de 52 cartas, hay 2,598,960 manos posibles de 5 cartas. Si cada apuesta de 5 cartas cuesta $1 USD, ¿cuánto dinero necesitarías para comprar absolutamente todas las manos posibles?
2.  **Mano de Figuras:** ¿Cuántos juegos de 5 cartas se pueden formar seleccionando exactamente 2 figuras (de las 12 disponibles) **y** 3 cartas simples (de las 36 disponibles)?
3.  **La Mano Compleja:** Calcula cuántas combinaciones de 5 cartas se pueden obtener si la mano debe tener: 2 figuras (de 12), 1 as (de 4) **y** 2 cartas simples (de 36). *(Nota: Verifica que el total de cartas seleccionadas sea 5).*
````

> [!tip] 💡 Consejo de estudio
> Para no confundirte nunca entre combinaciones y otros métodos, usa la **"Prueba del Orden"**: imagina que eliges dos elementos, A y B. Ahora cambia sus lugares a B y A. Si después del cambio la situación **es la misma** (como un equipo de trabajo o un apretón de manos), usa **Combinaciones**. Si la situación cambia (como un podio de 1er y 2do lugar o una clave bancaria), entonces no es una combinación.