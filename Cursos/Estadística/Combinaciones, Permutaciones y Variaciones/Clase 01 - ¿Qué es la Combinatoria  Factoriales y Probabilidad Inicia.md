# Clase 01 — ¿Qué es la Combinatoria? | Factoriales y Probabilidad Inicial

#algebra #queescombinatoria

[!info] 🧭 Navegación
*   [[Índice de Combinatoria|Índice]]
*   **Clase 01: Introducción y Factoriales**
*   [[Clase 02 — Permutaciones y Variaciones|Siguiente: Clase 02 →]]

---

[!info] 🌍 Relevancia y aplicaciones
La combinatoria es la rama de las matemáticas que estudia los métodos para contar y organizar elementos de un conjunto de forma eficiente. Nos permite descubrir cuántas agrupaciones distintas se pueden crear sin tener que enumerarlas una por una.

*   **Menús y costos:** Determinar el precio final de todas las combinaciones de platos posibles en un restaurante para fijar promociones ($USD).
*   **Construcción y diseño:** Organizar materiales de obra o planos arquitectónicos para optimizar el espacio y los recursos.
*   **Selección de Comités:** Calcular el presupuesto administrativo ($USD) necesario para evaluar cada posible formación de un equipo de trabajo.

---

[!note] 📌 ¿Qué es la Combinatoria?
¡Hola! Para nosotros, la combinatoria será la **"matemática del conteo inteligente"**. Su objetivo es estudiar las diferentes formas en las que podemos agrupar u ordenar elementos (como sabores de helado, estudiantes o carros).

*   **Experimento Aleatorio:** Es aquel donde no podemos predecir el resultado final, aunque se repita muchas veces (ejemplo: lanzar un dado o una moneda). Siempre tiene varias opciones.
*   **Espacio Muestral ($S$ o $\Omega$):** Es el conjunto de **todos** los resultados posibles. Se escribe entre llaves `{ }`.
*   **Evento o Suceso:** Son uno o varios de los resultados que nos interesan dentro del espacio muestral.
    *   *Ejemplo lúdico:* Si lanzas un dado, el espacio muestral es `{1, 2, 3, 4, 5, 6}`. Un evento sería "que salga un múltiplo de 2", cuyos elementos son `{2, 4, 6}`.

[!warning] ⚠️ Error común
No confundas el **Espacio Muestral** (todas las opciones posibles) con un **Evento** (solo lo que buscas). Si lanzas una moneda, el espacio muestral es `{Cara, Cruz}`, pero el evento es solo una de esas caras.

[!tip] 💡 Truco para recordarlo
El signo `!` (Factorial) indica que el número está "bajando las escaleras" multiplicándose. Pero cuidado: los factoriales solo existen para **números naturales** (enteros positivos y el cero). ¡No existen factoriales de fracciones como $3/4!$!

---

## 4. Procedimiento Paso a Paso: Operaciones con Factoriales

Para calcular y simplificar factoriales como un profesional, sigue estos pasos:

```text
1. Identificar el número mayor: En una fracción, localiza el factorial más grande.
2. Descomponer hacia abajo: Escribe el número mayor multiplicándolo por sus 
   anteriores (n × (n-1) × ...).
3. Simplificación inteligente: Si hay una división, detén la descomposición cuando 
   llegues al factorial del denominador. Si hay dos factoriales abajo, elige el 
   más grande para simplificar primero.
4. "¡Táchalos!": Cancela los factoriales idénticos arriba y abajo.
5. Resultado final: Multiplica los números restantes.
```

---

## 5. Ejemplos Prácticos de Aplicación

```ad-example
**Ejemplo 1: Espacio Muestral (Moneda y Dado)**
**Problema:** Determinar el espacio muestral de lanzar una moneda y un dado a la vez.
**Solución:** Combinamos las 2 caras de la moneda (C, X) con los 6 números del dado.
$$S = \{ (C,1), (C,2), (C,3), (C,4), (C,5), (C,6), (X,1), (X,2), (X,3), (X,4), (X,5), (X,6) \}$$
Total de resultados: 12.
```

```ad-example
**Ejemplo 2: Notación Factorial de 5**
**Problema:** Calcular $5!$.
**Solución:** Multiplicamos desde el 5 hasta llegar al 1.
$$5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$$
```

```ad-example
**Ejemplo 3: Simplificación Factorial**
**Problema:** Simplificar la operación $\frac{15!}{13!}$.
**Solución:** Descomponemos el 15 hasta el 13 y aplicamos la técnica de "tachar":
$$\frac{15 \times 14 \times 13!}{13!} = 15 \times 14 = 210$$
```

```ad-example
**Ejemplo 4: Los Carros de Colección ($USD)**
**Problema:** Tienes 3 carros (Azul, Rojo, Negro). ¿De cuántas formas puedes ordenarlos? Si cada configuración cuesta $10 USD exhibirla, ¿cuál es el costo total?
**Solución:** 
1. Como son 3 elementos, calculamos $3! = 3 \times 2 \times 1 = 6$ formas. 
2. Esto se puede visualizar con un **Diagrama de Árbol**, donde cada rama es una opción (Azul-Rojo-Negro, Azul-Negro-Rojo, etc.).
3. Costo: $6 \text{ formas} \times 10 \text{ USD} = 60 \text{ USD}$.
```

---

## 6. Sección de Ejercicios para el Estudiante

```ad-abstract
**🟢 Nivel Fácil: Identificación**
1. Escribe el espacio muestral de lanzar una moneda.
2. Escribe el espacio muestral de lanzar un dado.
3. Una urna tiene **1 bola roja, 2 azules y 3 blancas**. ¿Cuál es el espacio muestral total? (Diferencia las bolas, ej: $A_1, A_2$).
4. Si lanzas un dado, escribe los elementos del evento: "Obtener un número par".
```

```ad-abstract
**🟡 Nivel Medio: Operaciones con Factoriales**
1. Calcula el valor total de $4!$.
2. Simplifica la expresión $\frac{8!}{7!}$ usando la técnica de cancelación.
3. Expresa la operación $10 \times 9!$ como un solo factorial.
4. Resuelve la división $\frac{6!}{4!}$.
```

```ad-abstract
**🔴 Nivel Avanzado: Aplicación y Costos ($USD)**
1. **Helados:** Una heladería ofrece 7 sabores. Si quieres un helado de 3 bolas de diferentes sabores y cada combinación cuesta $5 USD, identifica la población ($n$) y la muestra ($r$).
2. **Comités:** De un grupo de 10 estudiantes se eligen 3 para un comité. Si organizar cada selección posible cuesta $15 USD, define $n$ y $r$.
3. **Coleccionista:** Tienes 3 carros de colección. Si cambiar el orden de la repisa cuesta $2 USD por cada nueva posición, ¿cuánto cuesta probar todas las órdenes posibles?
4. **Urna Mágica:** En la urna con 1 roja (R), 2 azules ($A_1, A_2$) y 3 blancas ($B_1, B_2, B_3$), define el evento "Sacar una bola que NO sea blanca".
```

```ad-success
**Respuestas para el Docente**
*   **Fácil:** 1. $S=\{C, X\}$ | 2. $S=\{1,2,3,4,5,6\}$ | 3. $S=\{R, A_1, A_2, B_1, B_2, B_3\}$ | 4. $E=\{2, 4, 6\}$.
*   **Medio:** 1. $24$ | 2. $8$ | 3. $10!$ | 4. $30$.
*   **Avanzado:** 1. $n=7, r=3$ | 2. $n=10, r=3$ | 3. $3! = 6$ formas $\times 2 \text{ USD} = 12 \text{ USD}$ | 4. $E=\{R, A_1, A_2\}$.
```

---

## 7. Autoevaluación (Mini-prueba)

```ad-question
**Pregunta 1: ¿Qué es un experimento aleatorio?**
a) Un experimento donde siempre conocemos el resultado de antemano.
b) Un experimento donde no se puede predecir el resultado exacto.
c) Una operación que solo suma números factoriales.
d) Un evento que ocurre solo una vez en la vida.
```

```ad-question
**Pregunta 2: ¿Cuál es el valor de $0!$?**
a) 0
b) 1 (Por definición/propiedad matemática).
c) No existe.
d) 10
```

```ad-question
**Pregunta 3: En el ejemplo de los helados de 3 bolas (Chocolate, Vainilla y Chicle), si el vendedor cambia el orden de las bolas al servirlas, ¿importa el orden para el resultado final del producto?**
a) Sí, porque el sabor cambia según la posición.
b) No, porque son los mismos sabores (el orden no importa en esta combinación).
c) Solo si el costo en $USD aumenta.
d) Depende de si los sabores se pueden repetir.
```

---

[!tip] 💡 En la próxima clase
Daremos el gran salto: aprenderemos a diferenciar cuándo **el orden sí importa** (Permutaciones) y qué pasa cuando podemos elegir el mismo sabor varias veces (Variaciones con repetición). ¡Trae tu calculadora!

[!info] 🧭 Navegación
*   [[Índice de Combinatoria|Índice]]
*   **Clase 01: Introducción y Factoriales**
*   [[Clase 02 — Permutaciones y Variaciones|Siguiente: Clase 02 →]]