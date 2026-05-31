# Clase 05 — Multiplicación de radicales de igual y diferente índice

#algebra #multiplicacionde-radicales

Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 5 de 14

> [!info] 🧭 Navegación
> ◀ [[Clase 04 — Introducción a los radicales]] | [[Clase 06 — División de radicales]] ▶

---

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> La multiplicación de raíces permite modelar situaciones de crecimiento en áreas geométricas complejas y finanzas avanzadas, facilitando la simplificación de cálculos con potencias fraccionarias en un solo radical.

* 💵 Aplicación con $USD$: Cálculo de intereses compuestos o depreciación de activos financieros donde las tasas son raíces.
* 🏗️ Aplicación práctica: Diseño de estructuras arquitectónicas que usan la proporción áurea (basada en $\sqrt{5}$).
* 📊 Situación cotidiana: Ajuste de escalas en fotografía y diseño gráfico profesional.

---

## Concepto clave

> [!note] 📌 ¿Qué es Multiplicación de radicales de igual índice?
> Imagina que cada raíz es una cárcel. Para que dos números puedan juntarse en una sola raíz, ambos deben estar en el mismo tipo de cárcel; es decir, deben tener exactamente el mismo índice. Si los índices son diferentes, no hablan el mismo idioma y no pueden mezclarse hasta que los igualemos.

> [!warning] ⚠️ Error común
> ❌ Intentar multiplicar $\sqrt{x} \cdot \sqrt[3]{x}$ poniendo todo dentro de una raíz de forma directa.
> ✅ Hallar primero el Mínimo Común Índice (MCI) para que ambas raíces tengan la misma condena antes de unirlas.

> [!tip] 💡 Truco para recordarlo
> La Técnica del Preso: El índice de la raíz representa los años de condena que exige la cárcel. El exponente del número es cuántos años lleva el preso cumplidos. Para que un factor pueda salir de la raíz y ser libre, sus años cumplidos (exponente) deben ser iguales o mayores a los años de condena (índice).

---

## Procedimiento paso a paso

Para multiplicar radicales de forma efectiva, sigue esta secuencia lógica:

```text
PASO 1 → Hallar el Mínimo Común Múltiplo (MCM) de los índices para obtener el MCI.
PASO 2 → Amplificar los índices y los exponentes internos multiplicándolos por el factor necesario.
PASO 3 → Multiplicar las cantidades subradicales y los coeficientes externos (si existen).
PASO 4 → Simplificar extrayendo factores de la raíz aplicando la condena del preso.
```

---

## Bloques de ejemplos prácticos

```ad-example
title: Ejemplo 1 (Caso Básico - Igual Índice)
Multiplicar: $\sqrt[3]{x^2} \cdot \sqrt[3]{x^5}$

1. Unir en una sola raíz: Como el índice es el mismo ($3$), los introducimos en la misma cárcel: $\sqrt[3]{x^2 \cdot x^5}$.
2. Sumar exponentes: Aplicamos propiedades de potencias: $\sqrt[3]{x^{2+5}} = \sqrt[3]{x^7}$.
3. Aplicar la técnica del preso: La condena es de $3$ años. Dividimos los $7$ años del preso en grupos de $3$: $\sqrt[3]{x^3 \cdot x^3 \cdot x^1}$.
4. Extraer: Dos grupos de $x$ cumplen su condena y salen de la cárcel.
Resultado final: $x^2 \sqrt[3]{x}$.
```

```ad-example
title: Ejemplo 2 (Caso con Números - Igual Índice)
Multiplicar: $\sqrt{12} \cdot \sqrt{6}$

Nota pedagógica: Es mejor descomponer los números en sus factores primos antes de multiplicar. Si multiplicamos $12 \cdot 6$, obtendríamos $72$, y es mucho más difícil encontrar qué factores salen de la raíz cuando trabajamos con números grandes.

1. Descomponer en factores primos:
   $12 = 2^2 \cdot 3$
   $6 = 2 \cdot 3$
2. Unir en una sola raíz cuadrada: $\sqrt{2^2 \cdot 3 \cdot 2 \cdot 3}$.
3. Agrupar por años de condena (índice $2$): $\sqrt{2^2 \cdot 3^2 \cdot 2^1}$.
4. Extraer: El factor $2$ y el factor $3$ salen porque sus exponentes igualan la condena. El último $2$ se queda dentro.
5. Multiplicar fuera: $2 \cdot 3 = 6$.
Resultado final: $6 \sqrt{2}$.
```

```ad-example
title: Ejemplo 3 (Caso Avanzado - Diferente Índice)
Multiplicar: $5\sqrt{150x^2y^2} \cdot 3\sqrt[4]{5x^3y^4}$

1. Factores primos de $150$: $2 \cdot 3 \cdot 5^2$.
2. Hallar MCI de los índices $2$ y $4$: $MCM(2, 4) = 4$.
3. Amplificar la primera raíz (multiplicando índice y exponentes por $2$):
   $5\sqrt[4]{(2 \cdot 3 \cdot 5^2 x^2 y^2)^2} = 5\sqrt[4]{2^2 \cdot 3^2 \cdot 5^4 x^4 y^4}$.
4. Multiplicar coeficientes y raíces:
   Fuera: $5 \cdot 3 = 15$.
   Dentro: $\sqrt[4]{(2^2 \cdot 3^2 \cdot 5^4 x^4 y^4) \cdot (5^1 x^3 y^4)} = \sqrt[4]{2^2 \cdot 3^2 \cdot 5^5 x^7 y^8}$.
5. Extraer (Condena de $4$ años):
   $5^5 = 5^4 \cdot 5^1 \to$ Sale un $5$.
   $x^7 = x^4 \cdot x^3 \to$ Sale una $x$.
   $y^8 = (y^4)^2 \to$ Salen dos $y$ ($y^2$).
6. Finalizar: $15 \cdot 5 \cdot x \cdot y^2 \sqrt[4]{2^2 \cdot 3^2 \cdot 5 \cdot x^3} = 75xy^2 \sqrt[4]{4 \cdot 9 \cdot 5 \cdot x^3}$.
Resultado final: $75xy^2 \sqrt[4]{180x^3}$.
```

```ad-example
title: Ejemplo 4 (Aplicación Real con $USD$)
El costo de una acción es $\sqrt{2}$ USD y se multiplica por un factor de riesgo de $\sqrt[3]{2}$. ¿Cuál es el costo final?

1. Identificar índices: $2$ y $3$. El $MCM$ es $6$.
2. Amplificar para llegar a índice $6$:
   $\sqrt{2} = \sqrt[6]{2^3}$
   $\sqrt[3]{2} = \sqrt[6]{2^2}$
3. Multiplicar: $\sqrt[6]{2^3 \cdot 2^2} = \sqrt[6]{2^5}$.
4. Calcular potencia: $2^5 = 32$.
Resultado final: $\sqrt[6]{32}$ USD.
```

---

## Ejercicios para el estudiante

```ad-abstract
title: Nivel Fácil (Igual índice)
1. $\sqrt{x} \cdot \sqrt{x^3}$
2. $\sqrt[3]{a^2} \cdot \sqrt[3]{a^4}$
3. $\sqrt[5]{b} \cdot \sqrt[5]{b^9}$
4. $\sqrt{x^5} \cdot \sqrt{x}$
```

```ad-abstract
title: Nivel Medio (Diferente índice)
1. $\sqrt{x} \cdot \sqrt[3]{x}$
2. $\sqrt[3]{a^2} \cdot \sqrt[4]{a}$
3. $\sqrt[2]{3} \cdot \sqrt[3]{3^2}$
4. $\sqrt[4]{x^3} \cdot \sqrt[2]{x}$
```

```ad-abstract
title: Nivel Avanzado (Problemas USD)
1. Una inversión inicial de $\sqrt{5}$ USD se multiplica por un factor de crecimiento de $\sqrt[3]{5}$.
2. El precio de un activo es $\sqrt[4]{2}$ USD y aumenta por un factor de riesgo de $\sqrt[3]{2}$.
3. Un costo base de $\sqrt{3}$ USD se multiplica por un índice de mercado de $\sqrt[6]{3}$.
4. El valor residual de una cuenta es $\sqrt[5]{x}$ USD y se multiplica por un factor de escala de $\sqrt{x}$.
```

```ad-success
title: ✅ Respuestas (para el docente)
Fácil: 1. $x^2$ | 2. $a^2$ | 3. $b^2$ | 4. $x^3$
Medio: 1. $\sqrt[6]{x^5}$ | 2. $\sqrt[12]{a^{11}}$ | 3. $3\sqrt[6]{3}$ | 4. $x\sqrt[4]{x}$
Avanzado: 1. $\sqrt[6]{5^5}$ USD | 2. $\sqrt[12]{2^7}$ USD | 3. $\sqrt[3]{3^2}$ USD (Simplificando $\sqrt[6]{3^4}$ entre $2$) | 4. $\sqrt[10]{x^7}$ USD
```

---

## Mini-prueba de autoevaluación

```ad-question
title: Pregunta 1 (Conceptual)
¿Cuál es la condición indispensable para introducir dos cantidades subradicales bajo el mismo signo de raíz?
Respuesta: Deben tener el mismo índice. Si son distintos, se debe transformar las raíces al Mínimo Común Índice antes de operar.
```

```ad-question
title: Pregunta 2 (Procedimental)
Si multiplicas $\sqrt[2]{a}$ por $\sqrt[3]{a}$, ¿cuál es el nuevo índice común y cómo quedan los exponentes internos?
Respuesta: El índice común es $6$. Los exponentes se amplifican multiplicando por el factor que llevó al índice a $6$, resultando en $\sqrt[6]{a^3} \cdot \sqrt[6]{a^2} = \sqrt[6]{a^5}$.
```

```ad-question
title: Pregunta 3 (Aplicación USD)
Si el costo final de una operación es $\sqrt[4]{x^9}$ USD, ¿cuántos factores salen de la cárcel?
Respuesta: Salen dos factores $x$, porque el exponente $9$ permite cumplir dos condenas de $4$ años ($4+4=8$). Queda $x^2 \sqrt[4]{x}$ USD.
```

---

## Notas para el próximo tema

> [!tip] 💡 En la próxima clase
> Estudiaremos la división de radicales. Verás que es el proceso hermano de la multiplicación y también requiere que las raíces compartan el mismo índice para poder realizar la operación dentro de una sola cárcel.

> [!info] 🧭 Navegación
> ◀ [[Clase 04 — Introducción a los radicales]] | [[Clase 06 — División de radicales]] ▶