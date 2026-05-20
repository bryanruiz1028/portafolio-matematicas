# Clase 02 — División de un polinomio entre un monomio

tags: #algebra #dividingapolyno
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 7

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | | [[Clase 03|Clase 03 ➡]]

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> La división de un polinomio entre un monomio permite modelar la distribución de recursos y el cálculo de costos unitarios cuando trabajamos con cantidades desconocidas representadas por variables ($x$).
> - 💵 **[Aplicación USD]**: Permite hallar el precio de un solo artículo cuando el costo total de un paquete con múltiples productos está expresado como una suma de variables (ej. $3x^2 + 6x$ USD) y se divide entre la cantidad total de artículos ($3x$).
> - 🏗️ **[Práctica]**: Es esencial en ingeniería para despejar dimensiones; por ejemplo, hallar la base de una estructura si conocemos su área total (polinomio) y su altura (monomio).
> - 📊 **[Cotidiana]**: Facilita el ajuste de presupuestos dinámicos donde los gastos compartidos varían según el número de participantes o el tiempo.

## Concepto clave

> [!note] 📌 ¿Qué es la división de un polinomio entre un monomio?
> Según la metodología del "profe Alex", esta operación consiste en fraccionar el polinomio original para dividir **cada uno de los términos del dividendo** (arriba) de forma independiente entre el **divisor único** (abajo).

> [!warning] ⚠️ Error común: El olvido del "1" y los paréntesis
> 1. **El resultado "Cero":** Si al dividir un término el numerador y el denominador son idénticos, el resultado es **1**, nunca cero. (Ej: $5x/5x = 1$).
> 2. **Exponentes Binomiales:** Al restar un exponente que tiene dos términos (ej. $n-1$), es obligatorio usar paréntesis. El signo menos de la resta afectará a ambos términos del binomio, cambiando sus signos.

> [!tip] 💡 Truco para recordarlo
> Sigue rigurosamente el mantra: **"Signos, Números y Letras"**.
> 1. Determina el signo final (Ley de signos).
> 2. Divide los coeficientes (División normal o simplificación).
> 3. Resta los exponentes de las letras iguales.

## Procedimiento paso a paso

```text
PASO 1 → Separar cada término del polinomio dividiéndolo individualmente por el monomio.
PASO 2 → Aplicar ley de signos para cada fracción resultante.
PASO 3 → Dividir los coeficientes numéricos. Si son fracciones, aplicar la "Ley de la Oreja" 
         (extremos para el numerador, medios para el denominador).
PASO 4 → Restar los exponentes de las letras iguales (Arriba - Abajo).
         *IMPORTANTE: Si el exponente de abajo es un binomio (ej. n-1), 
         úsense paréntesis: Arriba - (n - 1) para distribuir el signo negativo.
```

## Ejemplos prácticos (Sintetizados de la fuente)

```ad-example
title: Ejemplo 1: Básico (Uso del "1")
**Problema:** Dividir $(x^5 + x^2y^2) \div x^2$

**Solución:**
1. Separamos: $\frac{x^5}{x^2} + \frac{x^2y^2}{x^2}$
2. Primer término: $x^{5-2} = x^3$
3. Segundo término: Las $x^2$ arriba y abajo son iguales, se simplifican a 1. Queda $1 \cdot y^2$.
**Resultado:** $x^3 + y^2$
```

```ad-example
title: Ejemplo 2: Con signos y varios términos
**Problema:** Dividir $(12a^2b^5 - 24a^3b^4 - 18a^4b^2) \div 6a^2b^2$

**Solución:**
1. $+12/6 = 2$; $a^2$ se eliminan; $b^{5-2} = b^3 \rightarrow 2b^3$
2. $-24/6 = -4$; $a^{3-2} = a^1$; $b^{4-2} = b^2 \rightarrow -4ab^2$
3. $-18/6 = -3$; $a^{4-2} = a^2$; $b^2$ se eliminan $\rightarrow -3a^2$
**Resultado:** $2b^3 - 4ab^2 - 3a^2$
```

```ad-example
title: Ejemplo 3: Avanzado (Fracciones y Exponentes Algebraicos)
**Problema:** Dividir $(\frac{1}{2}x^{m+2} - \frac{2}{3}x^{m+1}) \div \frac{2}{3}x^{m-1}$

**Solución:**
1. **Fracción 1:** $(\frac{1}{2} \div \frac{2}{3})$. Por "Ley de la Oreja" ($1 \cdot 3 / 2 \cdot 2$) = $\frac{3}{4}$.
   *Exponente:* $(m+2) - (m-1) = m + 2 - m + 1 = 3$. Resultado: $\frac{3}{4}x^3$.
2. **Fracción 2:** $(\frac{2}{3} \div \frac{2}{3}) = 1$.
   *Exponente:* $(m+1) - (m-1) = m + 1 - m + 1 = 2$. Resultado: $-x^2$.
**Resultado:** $\frac{3}{4}x^3 - x^2$
```

```ad-example
title: Ejemplo 4: Aplicación USD
**Problema:** Un presupuesto total de $(10x^2 + 5x)$ USD debe repartirse equitativamente entre $5x$ empleados. ¿Cuál es el bono para cada uno?

**Solución:**
1. $10x^2 \div 5x = (10/5) \cdot x^{2-1} = 2x$
2. $5x \div 5x = 1$ (Todo número dividido por sí mismo es 1).
**Resultado:** Cada empleado recibe $(2x + 1)$ USD.
```

## Ejercicios para el estudiante

```ad-abstract
title: 🟢 Nivel Fácil
1. $(8x^4 + 4x^2) \div 2x^2$
2. $(15a^3 - 5a^2) \div 5a$
3. $(x^3y^2 + x^2y^3) \div x^2y^2$
4. $(12m^6 + 6m^4) \div 6m^3$
```

```ad-abstract
title: 🟡 Nivel Medio (Exponentes literales)
1. $(x^{a+2} + x^{a+1}) \div x^a$
2. $(16x^5y^3 - 8x^2y^2) \div (-4x^2y)$
3. $(m^{x+4} - m^{x+2}) \div m^2$
4. $(a^5b^4 - a^3b^2) \div a^2b^2$
```

```ad-abstract
title: 🔴 Nivel Avanzado (USD y Fracciones)
1. Un fondo de $(\frac{3}{4}x^3 + \frac{1}{2}x^2)$ USD se divide entre $\frac{1}{2}x$ departamentos. Hallar el presupuesto por departamento.
2. Dividir $(\frac{2}{5}x^{n+3} - \frac{1}{3}x^{n+2}) \div \frac{1}{5}x^{n-1}$.
3. Se pagaron $(24a^3b^2 + 12a^2b)$ USD por $12a^2b$ licencias de software. ¿Cuál es el costo por licencia?
4. $(x^{2n} + x^n) \div x^n$
```

> [!tip] 💡 Tip del docente para verificación
> Para estar 100% seguro de tu respuesta, multiplica tu resultado por el divisor. Si el producto es igual al polinomio original (el dividendo), ¡tu ejercicio es correcto!

```ad-success
title: ✅ Soluciones (Para el docente)
**Fácil:** 1) $4x^2+2$ | 2) $3a^2-a$ | 3) $x+y$ | 4) $2m^3+m$
**Medio:** 1) $x^2+x$ | 2) $-4x^3y^2+2y$ | 3) $m^{x+2}-m^x$ | 4) $a^3b^2-a$
**Avanzado:** 1) $(\frac{3}{2}x^2 + x)$ USD | 2) $2x^4 - \frac{5}{3}x^3$ | 3) $(2ab+1)$ USD | 4) $x^n+1$
```

## Mini-prueba de autoevaluación

```ad-question
title: Pregunta 1
¿Qué ocurre cuando restamos un exponente binomial como $(n-1)$ en el divisor?
**Respuesta:** Se deben usar paréntesis para restar. El signo negativo cambia los signos internos: $-(n-1) = -n+1$.
```

```ad-question
title: Pregunta 2
Resuelve mentalmente: $(-20x^5) \div (-5x^5)$
a) $4$
b) $-4x$
c) $4x^0$
**Respuesta:** a) $4$. (Signos: $-\div- = +$; Números: $20/5 = 4$; Letras: $x^5/x^5 = 1$).
```

```ad-question
title: Pregunta 3
Si una empresa factura $(12x^2 + 6x)$ USD por $6x$ servicios, ¿cuál es el costo de cada servicio?
**Respuesta:** $(2x + 1)$ USD. Explicación: $12x^2/6x = 2x$ y $6x/6x = 1$.
```

## Notas para el próximo tema
Una vez dominada la división entre un monomio, el siguiente paso es la **División entre Polinomios (Método Largo)**. Aquí aplicaremos un algoritmo similar a la división aritmética de varias cifras, pero utilizando el orden de los grados de las variables.

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | | [[Clase 03|Clase 03 ➡]]