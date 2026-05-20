# Clase 10 — Factorización: Trinomio $ax^2 + bx + c$ y Completación de Cuadrados
tags: #algebra #factorización
Curso: [[00 - Índice del curso]] | Bloque 3 | Lección 10 de 10

> [!info] 🧭 Navegación
> [[Clase 09 — Factorización: Diferencia de Cuadrados y Cubos | ← Clase Anterior]] | [[00 - Índice del curso | 🏠 Índice]] | [[Clase 11 — Ecuaciones Cuadráticas | Clase Siguiente →]]

---

### 2. RELEVANCIA Y APLICACIONES

> [!info] 🌍 Relevancia y aplicaciones
> Factorizar no es más que desarmar una estructura para entender cómo fue construida. En esta clase, aprenderemos a dominar trinomios que parecen complejos, dándoles una forma mucho más amigable.
> 
> *   **Finanzas ($USD):** Permite descomponer una función de ingresos totales en dos factores: el **precio unitario** y la **cantidad de productos** vendidos (ej. si el ingreso es $2x^2+5x+3$, sus factores nos dicen cuánto cuesta cada unidad).
> *   **Ingeniería y Arquitectura:** Esencial para calcular el punto de equilibrio en estructuras de soporte y analizar trayectorias parabólicas en puentes.
> *   **Situaciones Cotidianas:** Útil para optimizar el espacio al distribuir cajas o muebles en un área rectangular cuando solo conocemos el área total en términos de una variable $x$.

---

### 3. CONCEPTO CLAVE

> [!note] 📌 ¿Qué es Factorización?
> Imagina que tienes el número 6; puedes escribirlo como $2 \times 3$. En Álgebra hacemos lo mismo: **factorizar es escribir una expresión algebraica como una multiplicación de factores**. Es el proceso inverso a multiplicar paréntesis.

> [!warning] ⚠️ Error común
> *   **Saltarse el Factor Común:** ¡Regla de oro! Antes de cualquier método, mira si todos los términos tienen algo en común (letra o número).
> *   **Confusión de signos:** Al buscar los números mágicos, recuerda que el signo del segundo término y la multiplicación de signos de los paréntesis mandan.
> *   **Olvidar el orden:** El trinomio siempre debe estar ordenado de mayor a menor exponente.

> [!tip] 💡 Truco para recordarlo
> Para el método de $ax^2 + bx + c$, usa la lógica de la **"Balanza Matemática"**: Si multiplicas toda la expresión por un número para que sea más fácil, debes dividirla por ese mismo número al final. Así, la balanza se mantiene en equilibrio y no alteras el valor original.

---

### 4. PROCEDIMIENTO PASO A PASO: TRINOMIO $ax^2 + bx + c$

Este método se usa cuando la $x^2$ tiene un número $a$ acompañándola (ejemplo: $5x^2$). La estrategia maestra de Profe Alex es **transformar este trinomio en uno más sencillo** (del tipo $x^2 + bx + c$).

1.  **Paso 1: Identificación y Regla del Exponente Doble**
    Asegúrate de que esté ordenado. **Tip del Profe Alex:** El exponente del primer término debe ser el **doble** del segundo (ej. si tienes $x^{10}$, el del medio debe ser $x^5$). Identifica el valor de $a$.
2.  **Paso 2: Multiplicar y Dividir por $a$**
    Multiplicamos todo el trinomio por $a$ y lo dividimos por $a$ para no alterar la expresión.
3.  **Paso 3: Dejar el término central "Indicado"**
    *   El primer término queda como $(ax)^2$.
    *   **¡Ojo aquí!** En el término central, **no multipliques**. Deja el número $b$ afuera y el $(ax)$ entre paréntesis. Ejemplo: $7(5x)$.
    *   En el tercer término ($c$), sí realiza la multiplicación por $a$.
4.  **Paso 4: Los Números Mágicos (Factorización)**
    Abrimos dos paréntesis, ambos con el término $(ax)$. Buscamos dos números que:
    *   Multiplicados den el nuevo valor de $c$.
    *   Sumados o restados den el valor original de $b$.
    *   **Regla obligatoria:** Debes colocar **primero el número mayor** y luego el menor en los paréntesis. 
    *   *Truco:* Si el número es muy grande, usa la **descomposición en factores primos** para encontrar la pareja.
5.  **Paso 5: Simplificación Final**
    Dividimos el denominador simplificando con los paréntesis que sean divisibles de forma exacta por $a$.

---

### 5. PROCEDIMIENTO PASO A PASO: COMPLETACIÓN DE CUADRADOS

Este método es útil cuando un trinomio no se deja factorizar fácilmente. Queremos "completar" lo que falta para tener un **Trinomio Cuadrado Perfecto (TCP)**.

*   **El paso clave:** Toma el coeficiente $b$ (el que acompaña a la $x$), divídelo entre 2 y elévalo al cuadrado: $\left(\frac{b}{2}\right)^2$.
*   **La Balanza:** Sumamos y restamos ese resultado en la expresión. Al sumar creamos el TCP, y al restar mantenemos la expresión original sin cambios de valor.
*   **Resultado:** Los primeros tres términos se convierten en $(x \pm \frac{b}{2})^2$.

---

### 6. EJEMPLOS PRÁCTICOS

> [!example] Ejemplo 1: Proceso Estándar ($5x^2 + 7x + 2$)
> 1. Multiplicamos y dividimos por 5: $\frac{(5x)^2 + 7(5x) + 10}{5}$ (Nota que el $7(5x)$ queda indicado).
> 2. Buscamos números que multiplicados den $10$ y sumados $7$: son $5$ y $2$.
> 3. Escribimos los factores (mayor primero): $\frac{(5x + 5)(5x + 2)}{5}$.
> 4. Simplificamos: Al primer paréntesis $(5x+5)$ le sacamos quinta (lo dividimos entre 5).
> **Resultado:** $(x + 1)(5x + 2)$.

> [!example] Ejemplo 2: Manejo de Signos ($3x^2 - 5x - 2$)
> 1. Multiplicamos y dividimos por 3: $\frac{(3x)^2 - 5(3x) - 6}{3}$.
> 2. Buscamos números que multiplicados den $-6$ y restados den $-5$: son $-6$ y $+1$.
> 3. Factores: $\frac{(3x - 6)(3x + 1)}{3}$.
> 4. Simplificamos el primer paréntesis entre 3: $(x - 2)(3x + 1)$.
> **Resultado:** $(x - 2)(3x + 1)$.

> [!example] Ejemplo 3: Completación de Cuadrados ($x^2 + 6x$)
> 1. Identificamos $b = 6$.
> 2. Calculamos la mitad al cuadrado: $\left(\frac{6}{2}\right)^2 = 3^2 = 9$.
> 3. Sumamos y restamos 9: $x^2 + 6x + 9 - 9$.
> 4. Los primeros tres forman el TCP: $(x + 3)^2 - 9$.
> **Resultado:** $(x + 3)^2 - 9$.

> [!example] Ejemplo 4: Aplicación Real en $USD
> El costo total de producir $x$ artículos es $2x^2 + 5x + 3$ dólares. Factoriza para entender los componentes.
> 1. Aplicamos el método multiplicando por 2: $\frac{(2x)^2 + 5(2x) + 6}{2}$.
> 2. Números que multiplicados den $6$ y sumados $5$: son $3$ y $2$.
> 3. Factores: $\frac{(2x + 3)(2x + 2)}{2}$. Simplificamos el segundo paréntesis: $(2x + 3)(x + 1)$.
> **Interpretación:** El costo total es el producto de un factor de costo fijo/variable $(2x+3)$ por la cantidad de unidades más una base $(x+1)$.

---

### 7. EJERCICIOS PARA EL ESTUDIANTE

> [!abstract] 🟢 Nivel Fácil: Calentamiento
> 1. Factor común: $5a^2 + 15a$.
> 2. Identificación: ¿Es $x^2 + 10x + 25$ un TCP?
> 3. Trinomio básico: $2x^2 + 5x + 2$ (Usa $a=2$).
> 4. $3x^2 + 4x + 1$.

> [!abstract] 🟡 Nivel Medio: Trinomios $ax^2 + bx + c$
> 5. $6x^2 - 7x + 2$.
> 6. $5x^2 + 13x - 6$.
> 7. $4x^2 + 15x + 9$.
> 8. $2x^2 + 3x - 2$.

> [!abstract] 🔴 Nivel Avanzado: Aplicaciones y Completación
> 9. Completa el cuadrado para: $x^2 - 10x + 15$.
> 10. Usa descomposición de factores para hallar los números de: $20x^2 + 7x - 6$.
> 11. **Problema $USD:** Si el área de una oficina es $3x^2 + 17x + 10$ $m^2$, halla las expresiones para el largo y el ancho.
> 12. **Configuración de Ecuación:** Una empresa tiene ingresos de $R = 2x^2 + 7x + 3$. Si se sabe que el precio por unidad es $(2x + 1)$, factoriza para hallar la cantidad de unidades vendidas.

> [!success] ✅ Soluciones para el Docente
> 1. $5a(a + 3)$ | 2. Sí, es $(x + 5)^2$ | 3. $(2x + 1)(x + 2)$ | 4. $(3x + 1)(x + 1)$
> 5. $(3x - 2)(2x - 1)$ | 6. $(5x - 2)(x + 3)$ | 7. $(4x + 3)(x + 3)$ | 8. $(2x - 1)(x + 2)$
> 9. $(x - 5)^2 - 10$ | 10. $(4x + 3)(5x - 2)$ | 11. $(3x + 2)(x + 5)$ | 12. $(x + 3)$ unidades.

---

### 8. MINI-PRUEBA DE AUTOEVALUACIÓN

> [!question] Pregunta 1
> Al factorizar $ax^2 + bx + c$, ¿por qué dejamos el término central indicado como $b(ax)$?
> A) Por estética matemática.
> B) Para que se parezca al trinomio $x^2 + bx + c$ y sea fácil hallar los números mágicos.
> C) Porque no se puede multiplicar un número por una letra.
> **Respuesta:** B.

> [!question] Pregunta 2
> ¿Cuál es el paso fundamental para completar el cuadrado en $x^2 + 8x$?
> A) Sumar 8 y restar 8.
> B) Multiplicar por 8.
> C) Sumar 16 y restar 16 (la mitad de 8 al cuadrado).
> **Respuesta:** C.

> [!question] Pregunta 3
> Si factorizamos un modelo de costos de $5x^2 + 11x + 2$ $USD, ¿cuál es uno de sus factores?
> A) $(5x + 1)$
> B) $(5x + 5)$
> C) $(x + 5)$
> **Respuesta:** A (El resultado es $(5x+1)(x+2)$).

---

### 9. NOTAS FINALES Y NAVEGACIÓN

> [!tip] 💡 En la próxima clase
> ¡Excelente trabajo! Has dominado los métodos más potentes de factorización. En la próxima clase, usaremos todo esto para resolver **Ecuaciones Cuadráticas**. ¡Verás que factorizar es la llave maestra para encontrar el valor de $x$!

> [!info] 🧭 Navegación
> [[Clase 09 — Factorización: Diferencia de Cuadrados y Cubos | ← Clase Anterior]] | [[00 - Índice del curso | 🏠 Índice]] | [[Clase 11 — Ecuaciones Cuadráticas | Clase Siguiente →]]