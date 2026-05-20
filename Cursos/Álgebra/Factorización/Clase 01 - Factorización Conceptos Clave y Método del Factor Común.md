# Clase 01 — Factorización: Conceptos Clave y Método del Factor Común

#algebra #quesfactorizar

---
**Navegación:** [Bloque 1] | **Lección 1 de 10**
---

## Relevancia y Aplicaciones

```ad-info
title: ¿Para qué sirve la factorización?
Factorizar no es solo un ejercicio de clase; es la llave para simplificar problemas que parecen imposibles y encontrar los **ceros de la función** (los puntos exactos donde una gráfica cruza el eje horizontal).

*   **💵 $USD:** En el mundo de los negocios, se usa para calcular ganancias. Por ejemplo, al analizar el precio de venta de camisetas, factorizar la fórmula de ingresos nos permite ver en qué precios la ganancia es exactamente cero (punto de equilibrio).
*   **🏗️ Práctica:** Los ingenieros y arquitectos la utilizan para diseñar estructuras estables, como puentes, donde necesitan simplificar ecuaciones de resistencia.
*   **📊 Cotidiana:** Es vital en medicina, física y química para crear modelos que explican desde cómo se propaga un virus hasta cómo se mueve un proyectil.
```

## Conceptos Clave

```ad-note
title: ¿Qué es factorizar?
Factorizar es como "desarmar" un juguete o un número en sus piezas originales. Es el proceso de descomponer una expresión en **factores** (números o letras que se están multiplicando). 
**Recuerda:** El resultado de una factorización debe ser **siempre una multiplicación**.
*Ejemplo:* Si tienes el 12, sus factores primos son $2 \times 2 \times 3$. En álgebra, hacemos lo mismo con letras y números.
```

```ad-warning
title: ¡Cuidado con el término fantasma!
Un error muy frecuente es pensar que si extraes todo un término como factor común, este desaparece. **¡Error!** Siempre queda un **1**.
*¿Por qué?* Porque matemáticamente cualquier término está multiplicado por 1 (ej. $m^3 = m^3 \cdot 1$). Al dividir $m^3 / m^3$, el resultado es 1. ¡Nunca dejes ese espacio vacío dentro del paréntesis!
```

```ad-tip
title: El truco del exponente más pequeño
Para encontrar el factor común de una letra que se repite en varios términos, no te compliques: elige siempre la letra que tenga el **exponente más pequeño**. Esa es la máxima cantidad que puedes "sacar" de todos los términos a la vez.
```

## Procedimiento Paso a Paso: Método Extendido

Para factorizar usando el "Método UNO" (Extendido) del Profe Alex, sigue estos 5 pasos lógicos:

```text
1. Identificar Términos: Separa la expresión y descompone los coeficientes 
   (números) en sus factores primos (usando la mitad, tercera, quinta, etc.).
2. Extender Variables: Escribe las letras según su exponente. 
   (Ejemplo: x³ = x · x · x).
3. Identificar Repetidos: Encierra en un círculo los números y letras 
   que aparezcan en TODOS los términos del polinomio.
4. Construir el Resultado: Escribe esos factores repetidos fuera de un 
   paréntesis. Dentro, coloca lo que sobró de cada término con su signo.
5. Verificación (¡Fundamental!): Multiplica el factor común por los 
   términos del paréntesis. Si obtienes la expresión original, ¡está perfecto!
```

## Ejemplos Prácticos

```ad-example
title: Ejemplo 1: Extracción Básica
**Factorizar:** $2ac + 3ab$
1. **Factores:** El primer término tiene $\{2, a, c\}$ y el segundo $\{3, a, b\}$.
2. **Común:** La letra $a$ es el único factor repetido.
3. **Resultado:** **$a(2c + 3b)$**
```

```ad-example
title: Ejemplo 2: Método Extendido y Factores Primos
**Factorizar:** $6x^2y^2 - 8xy^5$
1. **Números:** Descomponemos $6 = 2 \cdot 3$ y $8 = 2 \cdot 2 \cdot 2$. El común es **2**.
2. **Variables extendidas:**
   * Término 1: $2 \cdot 3 \cdot (x \cdot x) \cdot (y \cdot y)$
   * Término 2: $2 \cdot 2 \cdot 2 \cdot (x) \cdot (y \cdot y \cdot y \cdot y \cdot y)$
3. **Comunes:** Un $2$, una $x$, y dos $y$ ($y^2$). Factor común: **$2xy^2$**.
4. **Resultado:** **$2xy^2(3x - 4y^3)$**
```

```ad-example
title: Ejemplo 3: El caso del "1" y tres términos
**Factorizar:** $3m^5n^2 - 6m^4n + m^3$
1. **Común:** La letra $m$ se repite. El exponente más pequeño es $m^3$.
2. **Extracción:**
   * Del primer término queda $3m^2n^2$.
   * Del segundo queda $-6mn$.
   * Del tercero, como sacamos el $m^3$ completo, queda el **1**.
3. **Resultado:** **$m^3(3m^2n^2 - 6mn + 1)$**
```

```ad-example
title: Ejemplo 4: Aplicación en Negocios ($USD)
**Problema:** Una empresa analiza sus ganancias con la fórmula $G = -V^2 + 70V - 600$ ($V$ es el precio en USD).
1. Al factorizar (usando métodos avanzados de trinomios), obtenemos: **$(-V + 10)(V - 60)$**.
2. **Interpretación:** Los ceros de la función son $V=10$ y $V=60$. Esto significa que si venden el producto a **10 USD** o **60 USD**, la ganancia es **cero** (puntos de equilibrio).
```

## Ejercicios

```ad-abstract
title: Batería de Ejercicios Progresivos
**Verde (Fácil):**
1. $2x + 2y$
2. $ax + ay$
3. $m^2 + m$
4. $5b + 5c$

**Amarillo (Medio):**
5. $10x^4 + 20x^2$
6. $6a^2b + 9ab^2$
7. $x^2y - xy^2$
8. $15m^3 - 5m^2$

**Rojo (Avanzado $USD):**
9. Una tienda tiene costos de envío expresados como $12V^2 + 6V$. Factoriza para hallar el factor común de los envíos.
10. Los ingresos de un software se modelan como $100x - 50x^2$. Simplifica la expresión.
11. El costo de materiales de una fábrica es $8a^3b^2 - 4a^2b^3$. Encuentra el factor común de producción.
12. Una empresa de tecnología calcula sus impuestos con $25x^5 + 50x^3 - 5x^2$. Factoriza la expresión.
```

```ad-success
title: Soluciones (Uso docente)
1. $2(x + y)$ | 2. $a(x + y)$ | 3. $m(m + 1)$ | 4. $5(b + c)$
5. $10x^2(x^2 + 2)$ | 6. $3ab(2a + 3b)$ | 7. $xy(x - y)$ | 8. $5m^2(3m - 1)$
9. $6V(2V + 1)$ | 10. $50x(2 - x)$ | 11. $4a^2b^2(2a - b)$ | 12. $5x^2(5x^3 + 10x - 1)$
```

## Autoevaluación

```ad-question
title: Pregunta 1
¿Qué es un factor en álgebra según lo aprendido?
A) El resultado de una suma o resta.
B) Cada uno de los elementos (números o letras) que se multiplican.
C) El número que queda después de simplificar todo a cero.
```

```ad-question
title: Pregunta 2
Si aplicas la regla del "exponente más pequeño", ¿cuál es el factor común de $5x^3 + 15x^2$?
A) $5x$
B) $5x^2$
C) $5x^3$
```

```ad-question
title: Pregunta 3
En el ejemplo de $G = (-V + 10)(V - 60)$, ¿qué sucede si el precio de venta $V$ es de 60 USD?
A) La empresa obtiene su máxima ganancia.
B) La ganancia es exactamente cero (no hay utilidad ni pérdida).
C) El costo de producción se duplica.
```

---
**Próximo tema:** *Clase 02 — Factorización por Factor Común: Método Rápido y Mental.*

**Navegación:** [Bloque 1] | **Lección 1 de 10**
---