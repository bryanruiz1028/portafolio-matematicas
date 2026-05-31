# 📖 Guía de estudio — Clase 03: Combinaciones, permutaciones y variaciones

¡Qué tal amigos! Espero que estén muy bien. En esta guía vamos a simplificar el fascinante mundo de la combinatoria. Para dominar estos ejercicios, más que memorizar fórmulas, debemos aprender a analizar las situaciones. Como siempre decimos en clase: el secreto está en hacerle las preguntas correctas al problema.

> [!info] 📌 Conceptos clave
> - **La pregunta de oro:** Todo empieza aquí: **"¿Importa el orden?"**. Si al cambiar la posición de los elementos el resultado es distinto (como en un número de teléfono o un podio), el orden **sí** importa. Si el grupo resultante es el mismo sin importar quién llegó primero (como una ensalada de frutas), el orden **no** importa.
> - **¿Todos o algunos?:** Si usamos el grupo completo de elementos disponibles, estamos ante una **permutación**. Si solo tomamos una parte del total, hablamos de una **variación** o **combinación**.
> - **Sin repetición:** En esta sesión nos enfocamos en casos donde un elemento no puede duplicarse (por ejemplo, una persona no puede ocupar dos asientos al mismo tiempo).
> - **El método de las cajitas:** Es una representación visual del **Principio de Multiplicación**. Es ideal para permutaciones y variaciones, pues nos permite ver cuántas opciones quedan disponibles para cada espacio.

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Combinación (sin repetición)** | Se usa cuando el orden **no importa**. Solo nos interesa quiénes forman el grupo. <br> **Nota:** *¡Cuidado! No se puede usar el método de las cajitas aquí.* <br> $C(n,r) = \frac{n!}{r!(n-r)!}$ |
| **Variación (sin repetición)** | Se usa cuando el orden **sí importa**, pero solo tomamos una parte ($r$) de los elementos totales ($n$). <br> $V(n,r) = \frac{n!}{(n-r)!}$ |
| **Permutación Lineal** | Se usa cuando el orden **sí importa** y utilizamos **todos** los elementos en fila. <br> $P(n) = n!$ |
| **Permutación Circular** | Se usa para organizar elementos en círculo. Para romper la rotación, "fijamos" a una persona en un sitio y movemos al resto. <br> $PC(n) = (n-1)!$ |
| **Permutación con elementos repetidos** | Se usa cuando algunos elementos son idénticos. Aquí $a, b, c$ representan cuántas veces se repite cada elemento. <br> $P = \frac{n!}{a!b!c!...}$ |

---

## Ejemplos Resueltos Adicionales

````ad-example
title: Ejemplo A — Organizando objetos en fila
**Enunciado:** ¿De cuántas maneras diferentes se pueden ubicar 4 autos en una fila de un estacionamiento?

**Procedimiento:**
1. **Paso 1 (Análisis del orden):** ¿Importa el orden? **Sí**. Si el auto azul está en la primera posición es un orden distinto a que esté en la última.
2. **Paso 2 (Elementos):** ¿Se usan todos? **Sí**. Tenemos 4 autos y queremos saber las posiciones de los 4. Esto es una **Permutación Lineal**.
3. **Paso 3 (Cálculo):** Aplicamos $P(4) = 4!$
   - $4! = 4 \times 3 \times 2 \times 1 = 24$

✅ **Resultado:** Existen **24 formas** diferentes de organizar los autos.
````

````ad-example
title: Ejemplo B — Premios en un concurso de talentos
**Enunciado:** De un grupo de 10 finalistas, se elegirán 3 para premios en efectivo: 1er lugar ($100 USD), 2do lugar ($50 USD) y 3er lugar ($25 USD). ¿De cuántas formas se pueden repartir?

**Análisis Pedagógico:**
¿Importa el orden? **¡Claro que sí!** No es lo mismo ser el ganador del grupo {Alex, María, José} y llevarse $100, a que José gane los $100 y Alex los $25. Al cambiar el orden de los nombres, cambia el premio que recibe cada uno. Como tomamos 3 de 10, es una **Variación**.

**Procedimiento:**
- **Método de las cajitas:**
  - Posición 1 ($100): 10 opciones.
  - Posición 2 ($50): 9 opciones (el ganador anterior ya no participa).
  - Posición 3 ($25): 8 opciones.
  - **Cálculo:** $10 \times 9 \times 8 = 720$.
- **Uso de fórmula:** $V(10,3) = \frac{10!}{(10-3)!} = \frac{10!}{7!} = 10 \times 9 \times 8 = 720$.

✅ **Resultado:** Los premios se pueden repartir de **720 maneras** diferentes.
````

---

## Ejercicios de Repaso

````ad-abstract
title: 🟢 Bloque: Fácil
1. ¿Cuántas palabras diferentes (con o sin sentido) se pueden formar con todas las letras de la palabra **LUNA**?
2. Un grupo de 10 estudiantes quiere elegir un comité de 3 personas. Si todos los miembros del comité harán la misma labor (no hay cargos diferenciados), ¿cuántas combinaciones existen?
3. En una oficina hay 20 empleados y se deben elegir a 2 personas para recibir un regalo idéntico. ¿De cuántas formas se pueden seleccionar?
````

````ad-abstract
title: 🟡 Bloque: Medio
1. En un campeonato compiten 8 equipos. ¿De cuántas formas diferentes pueden quedar definidos los puestos de **campeón** y **subcampeón**?
2. Se desea sentar a 5 amigos en una mesa circular para cenar. Aplica la lógica de "fijar" a una persona para calcular de cuántas maneras pueden ubicarse.
3. En una competencia de 10 atletas, se entregan medallas de **oro, plata y bronce**. ¿De cuántas formas pueden repartirse los trofeos si no hay empates?
````

````ad-abstract
title: 🔴 Bloque: Avanzado — Aplicación y Repetición
1. Entre 20 finalistas de un sorteo, se deben repartir dos premios: un primer premio de **$500 USD** y un segundo de **$200 USD**. ¿De cuántas formas pueden quedar los ganadores?
2. **Desafío Conceptual:** Un teatro vende boletos para una fila de 10 asientos. Explica por qué vender **boletos numerados** (asiento 1, asiento 2...) permite más formas de sentarse que vender **boletos de entrada general** (donde solo importa quiénes entran a la fila).
3. ¿Cuántas palabras diferentes se pueden formar con todas las letras de la palabra **MATEMÁTICAS**?
   - *Pista: Cuenta cuántas veces se repite la M, la A y la T, y aplica la fórmula de permutación con repetición.*
````

---

> [!tip] 💡 Consejo de estudio
> Para no fallar, utiliza este árbol de decisión mental:
> 
> 1. **¿Importa el orden?**
>    - **NO** $\rightarrow$ Es una **Combinación**. (Usa la fórmula, no las cajitas).
>    - **SÍ** $\rightarrow$ Pasa a la siguiente pregunta.
> 
> 2. **¿Usas todos los elementos?**
>    - **SÍ** $\rightarrow$ Es una **Permutación**. (Usa $n!$ o $(n-1)!$ si es circular).
>    - **NO** $\rightarrow$ Es una **Variación**. (Usa el método de las cajitas para ganar velocidad).