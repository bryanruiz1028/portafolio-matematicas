# Clase 01 — Introducción a las Funciones y Evaluación Matemática

tags: #algebra #quesunafuncion
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 12

> [!info] 🧭 Navegación
> ⬅️ Anterior: [[00 - Índice del curso]] | Siguiente: [[Clase 02 — Gráficas de funciones]]

---

¿Qué tal amigas y amigos? Espero que estén muy bien. En esta clase vamos a entrar al fascinante mundo de las funciones, un concepto que verás desde hoy hasta la universidad.

### ¿Por qué es importante esta clase?
Las funciones nos permiten entender cómo una cantidad cambia respecto a otra, dándonos el superpoder de predecir resultados exactos mediante leyes matemáticas. Es como aprender a leer el lenguaje oculto que mueve todo a nuestro alrededor.

*   💵 **Aplicación $USD:** El cobro en un estacionamiento, donde el precio total a pagar depende directamente de los minutos que utilices el servicio.
*   🏗️ **Aplicación práctica:** La relación entre la edad y la estatura; conforme pasan los años, nuestro cuerpo sigue un patrón de crecimiento predecible.
*   📊 **Situación cotidiana:** El cálculo de la distancia que recorres en tu bicicleta basándote en el tiempo transcurrido y la velocidad que mantienes.

---

### Concepto clave

> [!note] **¿Qué es una función?**
> Es una **asociación** o "máquina" matemática que relaciona dos conjuntos. A cada elemento de entrada (**Dominio / Variable Independiente**) le corresponde un **único** elemento de salida (**Rango / Variable Dependiente**). Evaluar una función es como hacerle una pregunta a la máquina: "Si ingreso este valor, ¿cuál es el resultado?".

#### Tipos de Funciones
Según cómo se conecten los elementos del conjunto de partida con los de llegada:
*   **Inyectiva (1 a 1):** Cada elemento del conjunto de llegada recibe, como máximo, una sola flecha. No puede haber dos entradas distintas con la misma salida.
*   **Sobreyectiva (No sobra):** Todo el conjunto de llegada está cubierto; no queda ningún elemento "solo". Todos los elementos de llegada son imagen de al menos uno de partida.
*   **Biyectiva:** ¡Es el combo completo! La función es inyectiva y sobreyectiva al mismo tiempo.

> [!warning] **Error Común**
> ¡Mucho cuidado! El error más frecuente es no usar **paréntesis** al sustituir números negativos o expresiones. Sin ellos, podrías aplicar mal las leyes de signos o las potencias, arruinando todo el procedimiento.

> [!tip] **Trucos del Profe Alex**
> *   **Inyectiva:** Recuerda la "Regla del 1": máximo una flecha de llegada por cada elemento.
> *   **Sobreyectiva:** Recuerda "No sobra nada" en el conjunto de llegada.

---

### Procedimiento paso a paso

Para evaluar sin errores, incluso en las funciones más difíciles, aplica este método:

```text
1. Identificar la variable a sustituir (la 'x').
2. Reemplazar la variable por un paréntesis vacío: f( ) = ( )^2 - 3( ) - 2.
3. Colocar el valor o expresión dentro de los paréntesis.
4. Resolver operaciones en orden: Potencias -> Multiplicaciones -> Sumas/Restas.
```

---

### Ejemplos de Evaluación

**Ejemplo 1 (Básico):**
Evaluar $f(x) = 3x - 2$ para $f(2)$.
*   $f(2) = 3(2) - 2$
*   $f(2) = 6 - 2$
*   **Resultado:** ✅ 4. (Esto significa que la gráfica de la función pasa por el punto $(2, 4)$).

**Ejemplo 2 (Signos):**
Evaluar $f(x) = 3x - 2$ para $f(-3)$.
*   $f(-3) = 3(-3) - 2$
*   $f(-3) = -9 - 2$
*   **Resultado:** ✅ -11. (Recuerda: sumamos los negativos y el resultado sigue siendo negativo).

**Ejemplo 3 (Avanzado/Expresiones):**
Evaluar $f(x) = x^2 - 3x - 2$ para $f(2x + 1)$.
1.  **Sustituimos:** $(2x + 1)^2 - 3(2x + 1) - 2$
2.  **Binomio al cuadrado:** $(2x)^2 + 2(2x)(1) + 1^2 = 4x^2 + 4x + 1$
3.  **Distribuimos el -3:** $-3(2x) - 3(1) = -6x - 3$
4.  **Agrupamos todo:** $4x^2 + 4x + 1 - 6x - 3 - 2$
*   **Resultado:** ✅ $4x^2 - 2x - 4$.

**Ejemplo 4 (Aplicación $USD):**
El costo de un estacionamiento es $f(t) = 0.50t + 2.00$ ($t$ en minutos). Evaluar para 30 minutos.
*   $f(30) = 0.50(30) + 2.00$
*   $f(30) = 15.00 + 2.00$
*   **Resultado:** ✅ $17.00 USD.

---

### Ejercicios para el estudiante

```ad-abstract
title: Verde (Fácil)
1. Evalúa $f(5)$ en $f(x) = 2x + 3$.
2. Evalúa $g(0)$ en $g(x) = 10x - 8$.
3. Evalúa $h(1)$ en $h(x) = -4x + 2$.
4. Evalúa $f(10)$ en $f(x) = \frac{x}{2} + 5$.
```

```ad-abstract
title: Amarillo (Medio)
1. Evalúa $g(-2)$ en $g(x) = x^2 - 5x + 1$.
2. Evalúa $f(-1)$ en $f(x) = 3x^2 + 2x - 4$.
3. Evalúa $h(-3)$ en $h(x) = (x + 4)^2$.
4. Evalúa $g(2)$ en $g(x) = -x^2 + 3$.
```

```ad-abstract
title: Rojo (Avanzado $USD)
El costo de producción de "x" artículos en dólares es $C(x) = 2x^2 + 5x + 10$.
1. Calcula el costo para 4 artículos.
2. Calcula el costo para 10 artículos.
3. Si la producción sube de 2 a 4 artículos, ¿cuánto aumenta el costo?
4. Evalúa $C(a + 1)$ y simplifica la expresión resultante.
```

```ad-success
title: Respuestas
**Verde:** 1) 13, 2) -8, 3) -2, 4) 10.
**Amarillo:** 1) 15, 2) -3, 3) 1, 4) -1.
**Rojo:** 1) $62 USD, 2) $260 USD, 3) Aumenta $34 USD (de $28 a $62), 4) $2a^2 + 9a + 17$.
```

---

### Mini-prueba de autoevaluación

```ad-question
title: Pregunta 1: Conceptual
¿Qué condición es obligatoria para que una relación sea función?
*Respuesta: Que a cada elemento del dominio le corresponda un único (solo uno) elemento en el rango.*
```

```ad-question
title: Pregunta 2: Procedimental
En la función racional $f(x) = \frac{1}{x}$, ¿por qué el número 0 no puede estar en el dominio?
*Respuesta: Porque en una división el cero nunca puede estar en el **denominador**, ya que la operación no está definida.*
```

```ad-question
title: Pregunta 3: Aplicación
Si una función de costo es $f(x) = 20x + 5$ en $USD, ¿qué representa el 5 si $x$ son los productos?
*Respuesta: Representa un costo fijo o base (como el mantenimiento o renta) que se paga sin importar cuántos artículos se produzcan.*
```

---

### Cierre y Navegación Inferior

> [!tip] **Próximo tema**
> ¡Excelente trabajo! Ahora que ya sabes manejar la "máquina" de funciones, en la **Clase 02** aprenderás a graficar estos resultados para visualizar el comportamiento de las funciones lineales. ¡Allá nos vemos!

> [!info] 🧭 Navegación
> ⬅️ Anterior: [[00 - Índice del curso]] | Siguiente: [[Clase 02 — Gráficas de funciones]]