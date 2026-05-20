# 📖 Guía de estudio — Clase 03: Potencia de un producto y de un cociente

> [!info] 📌 Conceptos clave
> - **Potencia de un producto:** Cuando tenemos una multiplicación elevada a un exponente, dicho exponente se distribuye a cada uno de los factores de la operación.
> - **Potencia de un cociente:** En una división, ya sea expresada como fracción ($\frac{a}{b}$) o con el símbolo de división ($a \div b$), el exponente se aplica tanto al dividendo como al divisor.
> - **Regla de los signos:** Si la base es negativa, el resultado será positivo si el exponente es par, y negativo si el exponente es impar.
> - **Potencia de una potencia:** Cuando una base con exponente se eleva a otra potencia, los exponentes se multiplican. Esta regla suele ser el "segundo paso" en simplificaciones complejas.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Potencia de un producto** | $(a \cdot b)^n = a^n \cdot b^n$ |
| **Potencia de un cociente (Fracción)** | $(\frac{a}{b})^n = \frac{a^n}{b^n}$ |
| **Potencia de un cociente (División)** | $(a \div b)^n = a^n \div b^n$ |
| **Potencia de una potencia** | $(a^m)^n = a^{m \cdot n}$ |

**Nota didáctica:** El paréntesis es fundamental porque indica que el exponente afecta a toda la expresión interna. Una vez que aplicamos la propiedad y distribuimos el exponente al dividendo y al divisor, el paréntesis ya no es necesario y puede eliminarse.

## Ejemplos resueltos adicionales

> [!example] Ejemplo A — Caso Básico (Cociente)
> **Ejercicio:** Resolver $(\frac{2m^3}{n})^4$
> 
> **Paso a paso:**
> 1. **Elevar el coeficiente numérico:** Aplicamos el exponente al número 2. ($2^4 = 2 \cdot 2 \cdot 2 \cdot 2 = 16$).
> 2. **Paso de Potencia de una potencia (Numerador):** Para la variable $m^3$, multiplicamos sus exponentes ($3 \cdot 4 = 12$), obteniendo $m^{12}$.
> 3. **Aplicar el exponente al denominador:** La base $n$ (con exponente imaginario 1) queda como $n^4$.
> 
> **Resultado final:** $\frac{16m^{12}}{n^4}$

> [!example] Ejemplo B — Caso con aplicación real USD (Producto)
> **Enunciado:** Un fondo de inversión triplica el capital de un usuario ($3x$). Si este crecimiento se repite durante 3 periodos consecutivos, ¿cuál es el balance final?
> 
> **Resolución:**
> - Expresamos la situación como una potencia de un producto: $(3x)^3$.
> - **Paso 1:** Distribuimos el exponente a cada factor: $3^3 \cdot x^3$.
> - **Paso 2:** Resolvemos la potencia numérica: $3 \cdot 3 \cdot 3 = 27$.
> 
> ✅ **Resultado:** $27x^3$ USD

## Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel Básico
Simplifica las siguientes expresiones de aplicación directa:
1. $(m \cdot n)^{10}$
2. $(\frac{a}{b})^5$
3. $(x \cdot y \cdot z)^2$
```

```ad-abstract
title: 🟡 Nivel Medio
Resuelve aplicando reglas de signos y potencia de una potencia:
1. $(-x \cdot y)^6$ (Aplica la regla de exponente par).
2. $(a^2 \cdot b^3)^5$
3. $(-\frac{a}{b})^3$ (Aplica la regla de exponente impar).
```

```ad-abstract
title: 🔴 Nivel Avanzado — Aplicación con USD
Simplifica las expresiones combinadas para determinar el saldo neto en USD:
1. Simplifica $\frac{x^2 y^7}{x^2 y^2}$ para hallar la ganancia neta en USD.
2. Determina el valor final simplificando la expresión: $\frac{2(a^2b)^3}{4ab^2}$ USD.
3. Resuelve la siguiente operación de intereses complejos: $\frac{(-2x^3)^2 \cdot y^4}{2x^2}$ USD.
```

> [!tip] 💡 Consejo de estudio
> Para dominar la simplificación de cocientes y evitar los exponentes negativos, utiliza la estrategia de **"tachar"** variables. Compara visualmente cuántas letras tienes arriba y cuántas abajo; resta las cantidades mentalmente y **coloca el resultado siempre donde había más letras originalmente**. Si tienes $y^7$ arriba y $y^2$ abajo, tachas las 2 de abajo con 2 de las 7 de arriba, y el resultado ($y^5$) se queda arriba. ¡Esto garantiza exponentes positivos siempre!