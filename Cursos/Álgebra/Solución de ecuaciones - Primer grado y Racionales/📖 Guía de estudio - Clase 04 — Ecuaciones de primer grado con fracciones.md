# Guía de Estudio: Resolución de Ecuaciones de Primer Grado con Fracciones

Esta guía ha sido diseñada para facilitar el aprendizaje del proceso de resolución de ecuaciones que contienen números fraccionarios. El objetivo principal es transformar una ecuación compleja con fracciones en una más sencilla con números enteros utilizando el método del Mínimo Común Múltiplo (MCM).

---

## 1. Conceptos Clave y Procedimiento General

Para resolver ecuaciones de primer grado con fracciones, se sigue un proceso lógico que garantiza la eliminación de los denominadores para trabajar con mayor comodidad.

### El Número Clave: Mínimo Común Múltiplo (MCM)
El primer paso es identificar todos los denominadores de la ecuación y encontrar su **Mínimo Común Múltiplo (MCM)**. Este número es el "número clave" que permitirá simplificar la ecuación.
*   **Proceso:** Se toman los denominadores y se descomponen en sus factores primos (mitad, tercera, quinta, etc.) hasta que todos lleguen a 1.
*   **Resultado:** El producto de esos factores primos es el MCM.

### Regla de Oro de la Multiplicación
Una vez hallado el MCM, se debe **multiplicar cada uno de los términos de la ecuación** por este número. 
*   **¡Importante!:** Incluso los términos que no tienen denominador (números enteros o variables solas) deben multiplicarse por el MCM para mantener la igualdad.

### Eliminación de Denominadores
Existen dos formas de eliminar el denominador una vez multiplicado por el MCM:
1.  **Simplificación:** Sacar mitad, tercera, etc., al MCM y al denominador hasta que el denominador se convierta en 1.
2.  **División Directa:** Dividir el MCM entre el denominador. El resultado se multiplica por el numerador de ese término.

### Manejo de Binomios y Signos
Cuando el numerador de una fracción es un **binomio** (por ejemplo, $x + 2$), el resultado de la división del MCM entre el denominador debe multiplicar a ambos términos del binomio (propiedad distributiva). 
*   **Atención a los signos:** Si hay un signo menos antes de una fracción, ese signo afectará a todo el resultado de la multiplicación del binomio, cambiando los signos de sus términos internos.

---

## 2. Ejemplo Resuelto Paso a Paso

**Ecuación a resolver:**
$$\frac{x + 2}{12} - \frac{2x - 3}{9} = \frac{4 - 3x}{18} + \frac{x}{6}$$

### Paso 1: Hallar el MCM de los denominadores (12, 9, 18, 6)

| Número | Factores Primos |
| :--- | :--- |
| 12, 9, 18, 6 | Mitad: 6, 9, 9, 3 |
| 6, 9, 9, 3 | Mitad: 3, 9, 9, 3 |
| 3, 9, 9, 3 | Tercera: 1, 3, 3, 1 |
| 1, 3, 3, 1 | Tercera: 1, 1, 1, 1 |

**MCM:** $2 \times 2 \times 3 \times 3 = \mathbf{36}$

### Paso 2: Multiplicar cada término por 36 y simplificar
Dividimos 36 entre cada denominador y multiplicamos por el numerador:
1.  $36 \div 12 = 3 \rightarrow 3(x + 2)$
2.  $36 \div 9 = 4 \rightarrow 4(2x - 3)$
3.  $36 \div 18 = 2 \rightarrow 2(4 - 3x)$
4.  $36 \div 6 = 6 \rightarrow 6(x)$

**La ecuación queda:**
$$3(x + 2) - 4(2x - 3) = 2(4 - 3x) + 6x$$

### Paso 3: Aplicar propiedad distributiva
*   $3x + 6 - 8x + 12 = 8 - 6x + 6x$
*(Nota: $-4$ por $-3$ se convierte en $+12$; $-6x + 6x$ se eliminan entre sí).*

### Paso 4: Agrupar términos (X a la izquierda, números a la derecha)
$$3x - 8x = 8 - 6 - 12$$
$$-5x = -10$$

### Paso 5: Despejar la X
Como la X está acompañada por un número negativo, se recomienda multiplicar toda la ecuación por $-1$:
$$5x = 10$$
$$x = \frac{10}{5}$$
$$\mathbf{x = 2}$$

---

## 3. Preguntas de Repaso (Respuesta Corta)

1.  **¿Cuál es el primer paso fundamental para resolver una ecuación con fracciones según el método estudiado?**
    *   *Respuesta:* Hallar el Mínimo Común Múltiplo (MCM) de todos los denominadores.
2.  **¿Qué sucede si un término de la ecuación no tiene denominador visible?**
    *   *Respuesta:* También debe multiplicarse por el MCM, ya que todos los términos de la ecuación deben ser afectados por igual.
3.  **Si al final del proceso el término con la incógnita es negativo (ej. $-7x = 21$), ¿qué técnica se recomienda aplicar?**
    *   *Respuesta:* Multiplicar toda la expresión por $-1$ para cambiar los signos y facilitar el despeje.
4.  **¿Qué ocurre con el denominador después de simplificarlo con el MCM?**
    *   *Respuesta:* Se convierte en 1, por lo cual ya no es necesario escribirlo, transformando la fracción en un número entero.
5.  **¿Cómo se maneja un signo negativo que precede a una fracción con un binomio en el numerador?**
    *   *Respuesta:* El signo negativo debe multiplicar a todo el resultado de la operación del binomio, cambiando el signo de cada uno de sus términos.

---

## 4. Temas para Reflexión y Análisis (Preguntas de Ensayo)

1.  **La importancia del equilibrio en las igualdades matemáticas:** Explique por qué es obligatorio multiplicar absolutamente todos los términos de una ecuación por el MCM, incluso aquellos que ya son números enteros. ¿Qué sucedería con la igualdad si olvidamos multiplicar un término?
2.  **Estrategias de simplificación:** Compare el método de "simplificar sacando mitad/tercera" frente al método de "dividir el MCM entre el denominador". ¿En qué casos considera que uno es más rápido que el otro y por qué?
3.  **El rol de los signos en el álgebra:** Analice los errores comunes que pueden surgir al trabajar con signos negativos en ecuaciones fraccionarias, especialmente cuando hay paréntesis involucrados. ¿Cómo puede un solo error de signo afectar el resultado final?

---

## 5. Glosario de Términos Importantes

*   **Binomio:** Expresión algebraica que consta de dos términos conectados por un signo de suma o resta (ejemplo: $3x - 5$).
*   **Denominador:** El número inferior en una fracción que indica en cuántas partes se divide el todo.
*   **Mínimo Común Múltiplo (MCM):** El número más pequeño que es múltiplo de dos o más números. Se usa para encontrar un denominador común.
*   **Numerador:** El número superior en una fracción que indica cuántas partes de la unidad se toman.
*   **Propiedad Distributiva:** Regla matemática que permite multiplicar un número por una suma o resta dentro de un paréntesis, multiplicando cada término individualmente.
*   **Simplificar:** Proceso de reducir una fracción o expresión a su forma más sencilla dividiendo el numerador y el denominador por un mismo número.
*   **Términos Semejantes:** Aquellos términos que tienen la misma variable elevada al mismo exponente (ejemplo: $15x$ y $3x$), los cuales pueden sumarse o restarse entre sí.