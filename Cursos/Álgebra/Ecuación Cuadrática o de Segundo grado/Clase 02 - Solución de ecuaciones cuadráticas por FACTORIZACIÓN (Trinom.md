# Clase 02 — Solución de ecuaciones cuadráticas por FACTORIZACIÓN (Trinomios y Simplificación)

tags: #algebra #solutionofthequ
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 8

> [!info] 🧭 Navegación
> ◀️ [[Clase 01 - Introducción a las ecuaciones cuadráticas]]
> 📋 [[00 - Índice del curso]]
> ▶️ [[Clase 03 - Fórmula General]]

---

> [!info] 🌍 Relevancia y aplicaciones
> La factorización es una herramienta poderosa que nos permite descomponer problemas complejos para encontrar dimensiones, puntos de equilibrio y trayectorias de forma eficiente. Al "desarmar" una expresión, podemos ver sus raíces y entender el comportamiento de un fenómeno sin usar fórmulas complicadas. ¡Es como tener rayos X para las matemáticas!
> 
> * 💵 **Cálculo de ingresos:** Determinar el precio de venta ($USD) óptimo para que una empresa maximice sus ganancias o no tenga pérdidas.
> * 🏗️ **Arquitectura:** Calcular dimensiones exactas de estructuras donde el área total depende de una variable al cuadrado.
> * 📊 **Optimización:** Encontrar el momento exacto en que una inversión financiera llega a su punto de retorno positivo.

---

> [!note] 📌 ¿Qué es la Solución de ecuaciones cuadráticas por FACTORIZACIÓN?
> ¡Qué tal amigos! Espero que estén muy bien. Factorizar una ecuación es como **desarmar un rompecabezas**. En lugar de ver la ecuación como un bloque de números sumados y restados, la separamos en los "pedazos" (llamados factores) que la formaron originalmente. Si logramos que uno de esos pedazos sea igual a $0$, ¡ya tenemos la solución!

> [!warning] ⚠️ Error común
> No olvides que el error más frecuente es intentar factorizar antes de **igualar la ecuación a cero**. Recuerda: la lógica de los factores solo funciona si el lado derecho de la igualdad es $0$.

> [!tip] 💡 Truco para recordarlo
> **Regla de los Signos en los Paréntesis:** 
> 1. El signo del primer paréntesis es siempre el signo del segundo término ($b$).
> 2. El signo del segundo paréntesis es el resultado de **multiplicar** los signos del segundo y tercer término ($b \cdot c$).

---

### Procedimiento Paso a Paso

Para resolver cualquier ecuación, seguiremos este orden metódico. ¡No te preocupes si cometes errores al principio, así se aprende!

1.  **PASO 1:** Resolver operaciones previas (como la propiedad distributiva).
2.  **PASO 2:** Pasar todos los términos a un solo lado de la igualdad para **igualar a cero**.
3.  **PASO 3:** Simplificar términos semejantes ($x^2$, $x$, e independientes). Si puedes, divide toda la ecuación por un mismo número para **"dejar la $x^2$ solita"** (con coeficiente $1$), ¡será mucho más fácil!
4.  **PASO 4:** Factorizar y despejar:
    *   (a) Identificar el método adecuado (Trinomio simple, TCP o $ax^2$).
    *   (b) Igualar cada factor a cero y encontrar los valores de $x$.

---

### Bloque de Ejemplos Resueltos

````ad-example
title: Ejemplo 1: Caso Básico con Simplificación
**Ecuación:** $2x^2 - 8x + 6 = 0$

1. **Simplificación:** Para que la $x^2$ quede solita, dividimos toda la ecuación entre $2$:
   $x^2 - 4x + 3 = 0$
2. **Factorización:** Hacemos dos paréntesis. El primer signo es $(-)$ y el segundo es $(- \cdot + = -)$. Buscamos números que multiplicados den $3$ y sumados den $4$:
   $(x - 3)(x - 1) = 0$
3. **Solución:**
   * $x - 3 = 0 \rightarrow \mathbf{x_1 = 3}$
   * $x - 1 = 0 \rightarrow \mathbf{x_2 = 1}$
````

````ad-example
title: Ejemplo 2: Trinomio Cuadrado Perfecto (TCP)
**Ecuación:** $9x^2 - 42x + 49 = 0$

1. **Verificación:** ¡Es un TCP! ¿Cómo lo sé?
   * Raíz de $9x^2$ es $3x$.
   * Raíz de $49$ es $7$.
   * El doble producto $2 \cdot (3x) \cdot (7) = 42x$ (el término central).
2. **Factorización:** Se escribe como un binomio al cuadrado:
   $(3x - 7)^2 = 0$
3. **Solución:**
   $3x - 7 = 0 \rightarrow 3x = 7 \rightarrow \mathbf{x = 7/3}$

> [!important] Nota importante
> Recuerda que cuando tenemos un cuadrado igualado a cero, obtenemos una única solución real (o dos raíces iguales). No busques una segunda respuesta diferente aquí.
````

````ad-example
title: Ejemplo 3: Caso Avanzado (ax² + bx + c)
**Ecuación:** $2x^2 - 5x - 12 = 0$

1. **Multiplicación:** Multiplicamos todo por el coeficiente principal ($2$) para prepararlo:
   $(2x)^2 - 5(2x) - 24 = 0$
2. **Factorización inicial:** Buscamos números que multiplicados den $-24$ y restados den $-5$. Son $-8$ y $+3$:
   $(2x - 8)(2x + 3)$
3. **Paso de equilibrio (División):** ¡Cuidado aquí! Como multiplicamos por $2$ al inicio, debemos dividir ahora para balancear la ecuación. Dividimos el primer paréntesis porque es el que se deja simplificar entre $2$:
   $\frac{(2x - 8)}{2}(2x + 3) = 0 \rightarrow (x - 4)(2x + 3) = 0$
4. **Solución:**
   * $x - 4 = 0 \rightarrow \mathbf{x_1 = 4}$
   * $2x + 3 = 0 \rightarrow \mathbf{x_2 = -3/2}$
````

````ad-example
title: Ejemplo 4: Aplicación en Costos ($USD)
**Problema:** Una microempresa determina que su costo de operación diario es $x^2 - 4x + 3 = 0$, donde $x$ es el precio en dólares de un producto. ¿A qué precios el costo se iguala a cero?

**Solución:** 
Factorizamos la expresión como en el Ejemplo 1:
$(x - 3)(x - 1) = 0$
Los precios que satisfacen la ecuación son **$1$ USD** y **$3$ USD**.
````

---

### Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Fácil
> Resuelva las siguientes ecuaciones de la forma $x^2 + bx + c = 0$:
> 1. $x^2 + 5x + 6 = 0$
> 2. $x^2 - 7x + 12 = 0$
> 3. $x^2 + 2x - 8 = 0$
> 4. $x^2 - x - 20 = 0$

> [!abstract] 🟡 Nivel Medio
> Resuelva aplicando propiedad distributiva y simplificación antes de factorizar:
> 1. $x(x + 3) = 10$
> 2. $x(2x - 5) = 3x - 6$ (Sugerencia: divide entre $2$ para simplificar al final)
> 3. $3(x^2 - 2) = x^2 + 2$
> 4. $(x + 2)(x + 1) = 6$

> [!abstract] 🔴 Nivel Avanzado (Aplicación $USD)
> Una tienda deportiva analiza sus finanzas con la función $3x^2 + 7x - 6 = 0$, donde $x$ es la inversión en publicidad en cientos de dólares. Encuentre el valor de $x$ positivo que estabiliza la ecuación.

> [!success] ✅ Respuestas
> **Fácil:** 1) $x = -2, -3$; 2) $x = 4, 3$; 3) $x = 2, -4$; 4) $x = 5, -4$.
> **Medio:** 1) $x = 2, -5$; 2) $x = 3, 1$; 3) $x = 2, -2$; 4) $x = 1, -4$.
> **Avanzado:** $x = 2/3$ (La raíz $x = -3$ se descarta porque no podemos invertir dinero negativo).

---

### Mini-Prueba de Autoevaluación

> [!question] Pregunta 1
> ¿Cuál es el requisito indispensable antes de elegir un método de factorización?
> *   **Respuesta:** Que la ecuación esté correctamente ordenada e igualada a cero ($0$).

> [!question] Pregunta 2
> Si al sacar raíces de los extremos de un trinomio y multiplicarlas por $2$ obtienes el término central, ¿cómo se llama ese caso?
> *   **Respuesta:** Trinomio Cuadrado Perfecto (TCP).

> [!question] Pregunta 3
> En una ecuación de precio $x^2 - 5x + 6 = 0$, ¿qué valores de $x$ (en dólares) hacen que la ecuación se cumpla?
> *   **Respuesta:** $x = 3$ y $x = 2$.

---

> [!tip] 💡 En la próxima clase
> Exploraremos la **Fórmula General**, el método definitivo para resolver ecuaciones donde la factorización se vuelve difícil o imposible con números enteros. ¡Nos vemos en la próxima!

> [!info] 🧭 Navegación
> ◀️ [[Clase 01 - Introducción a las ecuaciones cuadráticas]]
> 📋 [[00 - Índice del curso]]
> ▶️ [[Clase 03 - Fórmula General]]