# Clase 04 — El Cubo de un Binomio y el Triángulo de Pascal

#algebra #cubeofabinomial

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [Clase 03 — Binomios al Cuadrado](clase-03.md) | 🏠 **Inicio:** [Índice de Álgebra](indice-algebra.md) | ➡️ **Siguiente:** [Clase 05 — Cocientes Notables](clase-05.md)

---

## 1. ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> El cubo de un binomio es una herramienta fundamental para expandir expresiones algebraicas a su tercera potencia sin necesidad de realizar multiplicaciones largas y repetitivas. Esencial para calcular volúmenes y entender el crecimiento en potencias superiores.
> 
> **Aplicación USD:** Imagina que diseñas un contenedor cúbico cuyas dimensiones están expresadas como $(x + 2)$ metros. Para calcular el costo de envío basado en el volumen total, necesitas desarrollar este binomio. Si el costo por metro cúbico transportado es de **$5 USD**, la expresión desarrollada te permitirá conocer el presupuesto exacto según el valor de $x$.
> 
> **Aplicación Práctica:** Se utiliza en el diseño de estructuras tridimensionales y en ingeniería civil para determinar la resistencia de materiales en volúmenes variables.
> 
> **Situación Cotidiana:** Ayuda a modelar el crecimiento exponencial, similar a cómo se calculan los intereses compuestos en ahorros o la expansión de poblaciones biológicas en un espacio tridimensional.

---

## 2. Concepto Clave

El **Cubo de un Binomio** es el resultado de multiplicar un binomio por sí mismo tres veces: $(a + b)^3 = (a + b)(a + b)(a + b)$. Para un estudiante de 12 años, podemos verlo como una receta que nos ahorra el trabajo de multiplicar término a término, dándonos el resultado final de forma directa.

> [!warning] ⚠️ Error común
> Muchos estudiantes creen que $(a + b)^3 = a^3 + b^3$. ¡Cuidado! Esto es falso. Al elevar al cubo, se generan términos intermedios (los triples productos) que son vitales para que el resultado sea matemáticamente correcto.

> [!tip] 💡 Truco para recordarlo
> Fíjate en cómo se mueven los exponentes según las enseñanzas del Profe Alex:
> 1. El primer término empieza en potencia 3 y baja: **3, 2, 1, 0** (hasta desaparecer).
> 2. El segundo término empieza en potencia 0 (no está) y sube: **0, 1, 2, 3**.
> 3. Los coeficientes de los términos centrales siempre son **3**.

---

## 3. Procedimiento paso a paso

> [!todo] Pasos para el éxito (Método Profe Alex)
> 1. **Identificar:** Determina claramente cuál es el primer término ($a$) y el segundo término ($b$).
> 2. **Estructurar:** Escribe la fórmula vacía. Si es suma ($+$), todos son positivos. Si es resta ($-$), los signos se intercalan: **(+) (–) (+) (–)**.
> 3. **Potencias:** Resuelve primero las potencias de cada término individualmente.
> 4. **Multiplicar:** Realiza las multiplicaciones finales entre coeficientes numéricos.
> 5. **Verificación:** Comprueba que los exponentes sigan la secuencia lógica (3, 2, 1, 0) para el primer término y (0, 1, 2, 3) para el segundo.

---

## 4. Ejemplos Desarrollados

> [!example] Ejemplo 1: Básico (Suma)
> **Desarrollar:** $(x + 5)^3$
> 1. **Planteamiento:** $(x)^3 + 3(x)^2(5) + 3(x)(5)^2 + (5)^3$
> 2. **Potencias:** $x^3 + 3(x^2)(5) + 3(x)(25) + 125$
> 3. **Resultado:** $x^3 + 15x^2 + 75x + 125$

> [!example] Ejemplo 2: Signos Intercalados (Resta)
> **Desarrollar:** $(3 - m)^3$
> 1. **Estructura:** $(3)^3 - 3(3)^2(m) + 3(3)(m)^2 - (m)^3$
> 2. **Potencias:** $27 - 3(9)(m) + 3(3)(m^2) - m^3$
> 3. **Resultado:** $27 - 27m + 9m^2 - m^3$
> *Verificación:* Los signos son (+, -, +, -) y los exponentes de $m$ suben (0, 1, 2, 3).

> [!example] Ejemplo 3: Avanzado (Potencia de una potencia)
> **Desarrollar:** $(2x^2y - 3z^3)^3$
> 1. **Sustitución:** $(2x^2y)^3 - 3(2x^2y)^2(3z^3) + 3(2x^2y)(3z^3)^2 - (3z^3)^3$
> 2. **Cálculo de Potencias:**
>    - $(2x^2y)^3 \rightarrow$ Coeficiente: $2^3=8$. Variables: $x^{2\cdot3}=x^6$, $y^3$. Resultado: $8x^6y^3$.
>    - $(2x^2y)^2 \rightarrow 4x^4y^2$.
>    - $(3z^3)^2 \rightarrow 9z^6$.
>    - $(3z^3)^3 \rightarrow 27z^9$.
> 3. **Multiplicación final:** $8x^6y^3 - 3(4x^4y^2)(3z^3) + 3(2x^2y)(9z^6) - 27z^9$
> 4. **Resultado:** $8x^6y^3 - 36x^4y^2z^3 + 54x^2yz^6 - 27z^9$
> > [!info] Recordatorio: Ley de Exponentes
> > Cuando elevas una potencia a otra potencia, los exponentes se multiplican: $(x^a)^b = x^{a \cdot b}$.

> [!example] Ejemplo 4: Aplicación USD
> **Problema:** Un depósito cúbico tiene un lado de $(x + 2)$ metros. El costo de impermeabilización es de $5 USD por metro cúbico. Hallar la expresión del costo total.
> 1. **Volumen:** $(x + 2)^3 = x^3 + 6x^2 + 12x + 8$ $m^3$.
> 2. **Costo Total:** Multiplicamos cada término por $5 USD$.
> 3. **Resultado:** $5x^3 + 30x^2 + 60x + 40$ USD.

---

## 5. El Triángulo de Pascal y Binomio de Newton

El Triángulo de Pascal es una pirámide numérica donde cada número es la suma de los dos que tiene encima.

*   **La Fila del Cubo:** La fila `1 3 3 1` nos da exactamente los coeficientes que necesitamos para el binomio al cubo.
*   **Utilidad:** Para potencias mayores como $(a+b)^4$ o $(a+b)^5$, no necesitas multiplicar horas; solo bajas una fila en el triángulo para obtener los nuevos coeficientes (ej. `1 4 6 4 1`).
*   **Dato curioso:** La suma de los números de cada fila siempre es una potencia de 2 ($2^n$). Para la fila del cubo ($1+3+3+1$), la suma es $8$, que es $2^3$.

---

## 6. Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Verde (Fácil)
> 1. $(a + 1)^3$
> 2. $(x + 2)^3$
> 3. $(y - 1)^3$
> 4. $(m + 3)^3$

> [!abstract] 🟡 Nivel Amarillo (Medio)
> 1. $(2x + 3y)^3$
> 2. $(3a - 2b)^3$
> 3. $(5x^2 + 1)^3$
> 4. $(4m - n^2)^3$

> [!abstract] 🔴 Nivel Rojo (Avanzado - Aplicación USD)
> 1. Un cubo tiene lado $(x + 1)$. Si el costo de material es **$10 USD** por $m^3$, ¿cuál es el costo total?
> 2. Un contenedor mide $(2x + 3)$ de lado. Si el transporte cuesta **$2 USD** por $m^3$, halla la expresión del costo.
> 3. Un tanque de lado $(a + 2)$ se llena con químico de **$3 USD** el $m^3$. Expresa el valor total.
> 4. Desarrolla $(y^2 + 4)^3$ y determina el costo si se cobra **$1 USD** por unidad de volumen.

> [!success] Sección de Respuestas (Para el Docente)
> **Verde:**
> 1. $a^3+3a^2+3a+1$ | 2. $x^3+6x^2+12x+8$ | 3. $y^3-3y^2+3y-1$ | 4. $m^3+9m^2+27m+27$
>
> **Amarillo:**
> 1. $8x^3+36x^2y+54xy^2+27y^3$ | 2. $27a^3-54a^2b+36ab^2-8b^3$
> 3. $125x^6+75x^4+15x^2+1$ | 4. $64m^3-48m^2n^2+12mn^4-n^6$
>
> **Rojo (Expresiones en USD):**
> 1. $10x^3+30x^2+30x+10$ USD
> 2. $16x^3+144x^2+432x+216$ USD (Cálculo: $2 \cdot [8x^3+36x^2+54x+27]$)
> 3. $3a^3+18a^2+36a+24$ USD
> 4. $y^6+12y^4+48y^2+64$ USD

---

## 7. Mini-prueba de Autoevaluación

> [!question] Pregunta 1
> ¿Cuáles son los coeficientes de un binomio elevado al cubo según el Triángulo de Pascal?
> *Respuesta: 1, 3, 3, 1.*

> [!question] Pregunta 2
> ¿Cuál es el resultado de elevar el término $(3x^2)$ al cubo?
> *Respuesta: $27x^6$. (Recuerda: $3^3=27$ y $2\cdot3=6$)*

> [!question] Pregunta 3
> Si un cubo de lado $(x+1)$ tiene un costo de volumen de **$1 USD**, ¿cuánto cuesta si $x=1$?
> *Respuesta: $8 USD. (Desarrollo: $1^3+3(1)^2+3(1)+1 = 1+3+3+1 = 8$)*

---

## 8. Cierre y Navegación Final

> [!tip] 💡 En la próxima clase
> Ahora que dominas el cubo de un binomio, exploraremos los **Cocientes Notables**, donde aprenderemos a realizar divisiones exactas de forma instantánea reconociendo patrones similares a los de hoy.

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [Clase 03 — Binomios al Cuadrado](clase-03.md) | 🏠 **Inicio:** [Índice de Álgebra](indice-algebra.md) | ➡️ **Siguiente:** [Clase 05 — Cocientes Notables](clase-05.md)