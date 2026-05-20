# 📖 Guía de estudio — Clase 02: Unión de Intervalos

> [!info] **📌 Conceptos clave**
> 1. **Definición matemática:** La unión de dos conjuntos $A$ y $B$ (representada como $A \cup B$) es el conjunto de todos los números que pertenecen a $A$, a $B$, o a ambos. Lógicamente se define como: $\{x \mid x \in A \lor x \in B\}$.
> 2. **Símbolo de unión:** Se utiliza el carácter $\cup$, que indica la agrupación o "suma visual" de los elementos de los intervalos involucrados.
> 3. **Interpretación gráfica:** En la recta numérica, la unión comprende toda la zona donde exista **al menos una línea** de color. No es necesario que las líneas se crucen; basta con que haya presencia de color en ese punto.
> 4. **Extremos y marcadores:** Para representar si un número está incluido, usamos un **punto negro** (corchete $[ ]$). Si el número no está incluido, usamos un **huequito** (paréntesis $( )$).

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Unión ($A \cup B$)** | Conjunto de elementos que cumplen la condición lógica: $x \in A \lor x \in B$. |
| **Intervalo Abierto** | Representado por un "huequito" o paréntesis: $(a, b)$. Indica que el extremo no forma parte del conjunto. |
| **Intervalo Cerrado** | Representado por un "punto negro" o corchete: $[a, b]$. Indica que el extremo sí está incluido en el conjunto. |
| **Regla de la Gráfica** | Método práctico donde el resultado es el trazo total que abarca desde donde inicia la primera línea hasta donde termina la última, considerando los vacíos si existen. |

## Ejemplos resueltos adicionales

```ad-example
**Ejemplo A — Caso básico (Traslape)**
**Enunciado:** Hallar la unión de los intervalos $A = (-3, 2)$ y $B = (1, 5]$.

**Resolución:**
1. **Paso 1 (Graficar):** Dibujamos en la recta el intervalo $A$ (desde $-3$ con huequito hasta $2$ con huequito). Luego, dibujamos el intervalo $B$ (desde $1$ con huequito hasta $5$ con punto negro).
2. **Paso 2 (Identificar presencia de color):** La primera línea comienza en $-3$. Aunque en $2$ hay un huequito en el intervalo $A$, ese punto está cubierto por la línea del intervalo $B$. La última línea termina en $5$.
3. **Paso 3 (Resultado final):** La unión cubre todo desde el $-3$ (abierto) hasta el $5$ (cerrado).

✅ **Resultado:** $(-3, 5]$
```

```ad-example
**Ejemplo B — Aplicación con contexto real ($USD)**
**Enunciado:** Una tienda ofrece descuentos en dos rangos de precios. Rango $A$: de $10$ a $50$ USD (abierto). Rango $B$: de $40$ a $100$ USD (cerrado). ¿Cuál es el intervalo total de precios con descuento?

**Resolución:**
1. **Representación:** Definimos $A = (10, 50)$ y $B = [40, 100]$.
2. **Lógica de unión:** Al graficar, notamos que ambos intervalos se **solapan** entre el $40$ y el $50$. 
3. **Paso visual:** La "presencia de color" comienza justo después del $10$ y continúa sin interrupciones hasta el $100$.
4. **Resultado:** El rango total es desde $10$ (excluido) hasta $100$ (incluido).

✅ **Resultado:** $(10, 100]$
```

## Ejercicios de repaso

```ad-abstract
**🟢 Nivel: Fácil**
Resuelve las siguientes uniones de intervalos con traslape simple:
1. $[0, 4] \cup [2, 6]$
2. $(-5, 1) \cup (-2, 4)$
3. $[1, 7] \cup (3, 10)$
```

```ad-abstract
**🟡 Nivel: Medio**
Resuelve los siguientes ejercicios de unión múltiple o intervalos disjuntos:
1. $A \cup B \cup C$ donde $A = (-3, 2)$, $B = (1, 5]$ y $C = [3, 8]$.
2. $[-10, -5] \cup [0, 5]$
   *   *Nota pedagógica:* Si al graficar observas que las líneas no se tocan (hay un vacío), el resultado se expresa simplemente escribiendo ambos intervalos conectados por el símbolo $\cup$.
3. $(-2, 0) \cup [0, 4]$
```

```ad-abstract
**🔴 Nivel: Avanzado — Aplicación con $USD**
**Contexto:** Un inversionista compra acciones si el precio está entre $5$ y $15$ USD (abierto) o entre $12$ y $25$ USD (cerrado). 
1. Si el precio es exactamente $12$ USD, ¿está incluido en la unión? 
   *   **Justificación:** Sí, porque para que un número pertenezca a la unión, basta con que esté en **al menos uno** de los conjuntos. Dado que $12$ pertenece al intervalo cerrado $[12, 25]$, automáticamente forma parte de la unión.
2. Expresa el rango total de compra en notación de intervalos.
   *   **Resultado:** $(5, 25]$
```

> [!tip] **💡 Consejo de estudio del Profe Alex**
> Para dominar la unión, utiliza siempre colores diferentes para cada intervalo en tu recta numérica. 
> 
> *   **El secreto visual:** La unión es la "suma" de todos los colores. Si ves color (ya sea de una sola línea o de varias sobrepuestas), ese tramo pertenece a la respuesta. 
> *   **Evita confusiones:** A diferencia de la intersección (donde buscas el "cruce de cables"), en la unión solo te importa la existencia de al menos una línea. 
> *   **Recordatorio importante:** No utilices el truco del borrador aquí; ese método es exclusivo para la **resta o diferencia** de intervalos. En la unión, ¡todo lo que tenga color se queda!