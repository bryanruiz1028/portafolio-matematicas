# Clase 03 — Trinomio al cuadrado y Cubo de un binomio

#algebra #trinomioalcuadr
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 6

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | [[Clase 04|Clase 04 ➡]]

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> El dominio de estos productos notables permite agilizar el cálculo de superficies compuestas y volúmenes tridimensionales. Al comprender la estructura de estas fórmulas, se eliminan procesos de multiplicación extensos y repetitivos, optimizando la resolución de problemas algebraicos complejos.
> 
> - 💵 **Finanzas:** Proyección de crecimiento de ahorros en dólares ($USD) mediante el uso de potencias para calcular intereses compuestos o variaciones presupuestarias.
> - 🏗️ **Construcción:** Cálculo de materiales necesarios para estructuras cúbicas o superficies que combinan tres dimensiones o medidas distintas.
> - 📊 **Estadística:** Simplificación de fórmulas de varianza y modelos matemáticos que involucran el desarrollo de trinomios al cuadrado en el análisis de datos.

> [!note] 📌 ¿Qué es Trinomio al cuadrado y Cubo de un binomio?
> - **Trinomio al cuadrado:** Es el desarrollo de una expresión de tres términos elevada a la potencia 2. Su resultado es igual a la suma de los cuadrados de cada término individual, más el doble producto de todas las combinaciones posibles de parejas entre ellos.
> - **Cubo de un binomio:** Es el desarrollo de una suma o resta de dos términos elevada a la potencia 3. El resultado es un polinomio de cuatro términos. 
> 
> **Nota Didáctica:** Tal como explica el Profe Alex, el cubo de un binomio $(a+b)^3$ se deriva de multiplicar el cuadrado del binomio por el binomio original: $(a+b)^2 \cdot (a+b)$. Conocer el producto notable nos permite saltar directamente al resultado final sin realizar la distributiva larga.

> [!warning] ⚠️ Error común
> Nunca asumas que la potencia se distribuye directamente: $(x+y+z)^2 \neq x^2+y^2+z^2$ y $(a+b)^3 \neq a^3+b^3$. Faltan los términos intermedios (dobles y triples productos). 
> 
> **Ojo con los signos en el cubo:** En la resta $(a-b)^3$, el tercer término siempre es **positivo** ($+3ab^2$) porque la base negativa se eleva a una potencia par. Los signos se intercalan: (+, -, +, -).

> [!tip] 💡 Truco para recordarlo
> - **Para el Cubo:** Usa la técnica de **exponentes descendentes/ascendentes**. El primer término baja su potencia (3, 2, 1, 0) mientras el segundo la sube (0, 1, 2, 3). Los coeficientes centrales siempre serán 3 (Estructura 1-3-3-1).
> - **Para el Trinomio:** Recuerda la regla: **"Todos los cuadrados + todas las parejas por dos"**. Los cuadrados siempre son positivos; el signo de los dobles productos dependerá de la ley de signos de la pareja multiplicada.

## Procedimiento Paso a Paso (Síntesis Técnica)

### 1. Trinomio al Cuadrado
```markdown
PASO 1 → Elevar cada uno de los tres términos al cuadrado (siempre resultan positivos).
PASO 2 → Identificar las tres parejas posibles: (1º, 2º), (1º, 3º) y (2º, 3º).
PASO 3 → Multiplicar cada pareja entre sí y luego por 2, respetando la ley de signos.
PASO 4 → Organizar el polinomio final (generalmente los cuadrados primero).
```

### 2. Cubo de un Binomio
```markdown
PASO 1 → Elevar el primer término al cubo.
PASO 2 → Multiplicar 3 por el cuadrado del primer término por el segundo término.
PASO 3 → Multiplicar 3 por el primer término por el cuadrado del segundo término.
PASO 4 → Elevar el segundo término al cubo.
NOTA SOBRE SIGNOS: 
- Si es suma (+), todos los términos son positivos.
- Si es resta (-), los signos se intercalan: (+, -, +, -).
```

## Ejemplos Prácticos

> [!example] Ejemplo 1: Básico (Trinomio al cuadrado)
> **Desarrollar $(x+y+3)^2$**
> 1. **Cuadrados:** $x^2 + y^2 + (3)^2 \rightarrow x^2 + y^2 + 9$
> 2. **Dobles productos (parejas):**
>    - $2(x)(y) = 2xy$
>    - $2(x)(3) = 6x$
>    - $2(y)(3) = 6y$
> **Resultado:** $x^2 + y^2 + 9 + 2xy + 6x + 6y$

> [!example] Ejemplo 2: Gestión de Signos (Trinomio al cuadrado)
> **Desarrollar $(3x - 2y - 5)^2$**
> 1. **Cuadrados (siempre positivos):** $(3x)^2 + (-2y)^2 + (-5)^2 = 9x^2 + 4y^2 + 25$
> 2. **Parejas con ley de signos:**
>    - $2(3x)(-2y) = -12xy$
>    - $2(-2y)(-5) = +20y$
>    - $2(3x)(-5) = -30x$
> **Resultado:** $9x^2 + 4y^2 + 25 - 12xy + 20y - 30x$

> [!example] Ejemplo 3: Estructura 1-3-3-1 (Cubo de binomio)
> **Desarrollar $(a+b)^3$**
> Siguiendo la reducción de exponentes y coeficientes:
> - $1(a^3b^0) = a^3$
> - $3(a^2b^1) = 3a^2b$
> - $3(a^1b^2) = 3ab^2$
> - $1(a^0b^3) = b^3$
> **Resultado:** $a^3 + 3a^2b + 3ab^2 + b^3$

> [!example] Ejemplo 4: Aplicación USD (Presupuesto de Riesgo)
> **Contexto:** El costo de un proyecto se define por $5a^2 + 3b^3 - ab$ en $USD$. Para un fondo de contingencia, se requiere elevar esta expresión al cuadrado.
> 1. **Cuadrados:** $(5a^2)^2 + (3b^3)^2 + (-ab)^2 = 25a^4 + 9b^6 + a^2b^2$
> 2. **Dobles productos:**
>    - $2(5a^2)(3b^3) = 30a^2b^3$
>    - $2(3b^3)(-ab) = -6ab^4$
>    - $2(5a^2)(-ab) = -10a^3b$
> **Expresión final:** $25a^4 + 9b^6 + a^2b^2 + 30a^2b^3 - 6ab^4 - 10a^3b$

## Sección de Ejercicios

> [!abstract] 🟢 Nivel Fácil
> 1. Desarrollar $(a + b + 1)^2$
> 2. Desarrollar $(x + 2)^3$
> 3. Desarrollar $(m + n + 2)^2$
> 4. Desarrollar $(y + 1)^3$

> [!abstract] 🟡 Nivel Medio
> 1. Desarrollar $(2m + 3 n + 5)^2$
> 2. Desarrollar $(a - b)^3$
> 3. Desarrollar $(3x - 2y + 1)^2$
> 4. Desarrollar $(2x - 3)^3$

> [!abstract] 🔴 Nivel Avanzado (USD)
> 1. Un contenedor cúbico tiene una arista de $(x + 5)$ metros. Si el costo de almacenamiento es de $1 USD por metro cúbico, determine la expresión del costo total.
> 2. Calcule el área de un terreno cuadrado cuyos lados miden $(2a + b + 3c)$ metros.
> 3. Desarrollar $(5a^3 - 4b^3 - 2ab)^2$ aplicado a un cálculo de materiales en $USD$.
> 4. Desarrollar el volumen de un cubo de arista $(3x - 2)$.

> [!success] Respuestas
> **Fácil:**
> 1. $a^2 + b^2 + 1 + 2ab + 2a + 2b$
> 2. $x^3 + 6x^2 + 12x + 8$
> 3. $m^2 + n^2 + 4 + 2mn + 4m + 4n$
> 4. $y^3 + 3y^2 + 3y + 1$
> 
> **Medio:**
> 1. $4m^2 + 9n^2 + 25 + 12mn + 20m + 30n$
> 2. $a^3 - 3a^2b + 3ab^2 - b^3$
> 3. $9x^2 + 4y^2 + 1 - 12xy + 6x - 4y$
> 4. $8x^3 - 36x^2 + 54x - 27$
> 
> **Avanzado:**
> 1. Costo $= x^3 + 15x^2 + 75x + 125$ $USD.
> 2. Área $= 4a^2 + b^2 + 9c^2 + 4ab + 12ac + 6bc$
> 3. **Desglose:**
>    - (Squares: $25a^6 + 16b^6 + 4a^2b^2$) + (Pairs: $-40a^3b^3 - 20a^4b + 16ab^4$)
>    - **Expresión Final:** $25a^6 + 16b^6 + 4a^2b^2 - 40a^3b^3 - 20a^4b + 16ab^4$
> 4. $27x^3 - 54x^2 + 36x - 8$

## Autoevaluación

> [!question] Pregunta 1
> ¿Cuántos términos resultan del desarrollo completo de un trinomio al cuadrado antes de simplificar?
> **Respuesta:** Resultan 6 términos (3 cuadrados de cada término y 3 dobles productos de las parejas).

> [!question] Pregunta 2
> En el desarrollo de $(a - b)^3$, ¿por qué el tercer término ($+3ab^2$) es positivo si se trata de una resta?
> **Respuesta:** Porque en el tercer paso se multiplica $3(a)(-b)^2$. Al elevar el segundo término negativo al cuadrado, el resultado es positivo, lo que define el signo del término completo.

> [!question] Pregunta 3
> Si el precio de un activo está dado por $(x + 1)^3$ $USD, y $x = 2$, ¿cuál es el valor total?
> **Respuesta:** $27 USD. (Cálculo directo: $(2+1)^3 = 3^3 = 27$. Desarrollo: $2^3 + 3(2^2)(1) + 3(2)(1^2) + 1^3 = 8 + 12 + 6 + 1 = 27$).

> [!tip] 💡 En la próxima clase
> Ahora que dominas el desarrollo de potencias, en la **Clase 04** aprenderemos el proceso inverso aplicado a casos especiales: **Suma y diferencia de cubos**.

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | [[Clase 04|Clase 04 ➡]]