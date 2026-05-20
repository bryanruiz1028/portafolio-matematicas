# 📖 Guía de estudio — Clase 02: División de un polinomio entre un monomio

> [!info] 📌 Conceptos clave
> Para dominar la división de un polinomio entre un monomio, es fundamental aplicar los siguientes principios pedagógicos basados en el método del Profe Alex:
> 1. **La regla distributiva:** Dividimos cada uno de los términos del polinomio (numerador) de forma individual por el monomio divisor (denominador).
> 2. **Orden jerárquico de operación:** En cada término, operamos siguiendo estrictamente este orden: **Signos** $\rightarrow$ **Coeficientes** $\rightarrow$ **Letras**.
> 3. **Propiedad de los exponentes:** Al dividir letras iguales, se restan los exponentes (numerador menos denominador): $x^a \div x^b = x^{a-b}$.
> 4. **Exponentes literales y el uso de paréntesis:** Cuando el exponente del divisor es un binomio (ej. $n+1$), al restar debemos usar paréntesis porque el signo menos cambiará los signos de todo el binomio: $-(n+1) = -n - 1$.
> 5. **Principio de la unidad:** Si al dividir, todos los elementos de un término son idénticos arriba y abajo, el resultado es **1** (neutro multiplicativo), nunca 0.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Notación de división** | Se puede presentar como fracción $\frac{P}{M}$, con el símbolo $\div$, o con dos puntos $:$. |
| **División de potencias** | $x^a \div x^b = x^{(a-b)}$. |
| **Ley de Signos** | Signos iguales = $(+)$; Signos diferentes = $(-)$. |
| **Regla de la Oreja** | $\frac{a/b}{c/d} = \frac{a \cdot d}{b \cdot c}$. (Extremos arriba, medios abajo). ¡Simplifica el resultado si es posible! |
| **Resta con binomios** | $x^{m+2} \div x^{m-1} = x^{(m+2) - (m-1)} = x^{m+2-m+1} = x^3$. |

## Ejemplos resueltos

```ad-example
title: Ejemplo A — Exponentes enteros y simplificación a la unidad
**Problema:** Dividir $(x^5 + x^2y^2) \div x^2$

**Procedimiento:**
1. **Separar términos:** $\frac{x^5}{x^2} + \frac{x^2y^2}{x^2}$
2. **Operar cada uno:**
   - Término 1: $x^{5-2} = x^3$.
   - Término 2: El factor $x^2$ está arriba y abajo; se **simplifican a 1**. Como $1 \cdot y^2 = y^2$, el término resultante es $y^2$.

✅ **Resultado:** $x^3 + y^2$
```

```ad-example
title: Ejemplo B — Aplicación económica ($USD) con coeficientes enteros
**Problema:** Una empresa reparte una ganancia de $(12a^2b^5 - 24a^3b^4)$ USD equitativamente entre $(6a^2b^2)$ socios. ¿Cuánto recibe cada uno?

**Procedimiento:**
1. **Dividir coeficientes y signos:**
   - $12 \div 6 = 2$
   - $-24 \div 6 = -4$
2. **Restar exponentes:**
   - Término 1: $a^{2-2}b^{5-2} \rightarrow a^0b^3$. Como $a^0 = 1$, queda $2b^3$.
   - Término 2: $a^{3-2}b^{4-2} \rightarrow a^1b^2$. Queda $-4ab^2$.

✅ **Resultado:** $(2b^3 - 4ab^2)$ USD
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel: Fácil
1. **Resta simple:** $(9x^4 - 6x^3) \div 3x^2$
2. **Coeficientes enteros:** $(15a^5 + 10a^2) \div 5a$
3. **Simplificación total:** $(m^2n - mn) \div mn$

**Solucionario:**
1. $3x^2 - 2x$
2. $3a^4 + 2a$
3. $m - 1$
```

```ad-abstract
title: 🟡 Nivel: Medio
1. **Exponentes literales:** $(x^{n+1} + x^n) \div x^n$
2. **Regla de la oreja:** $(\frac{1}{2}a^3 + \frac{1}{4}a^2) \div \frac{1}{2}a$
3. **Divisor negativo:** $(20y^3 - 10y^2) \div -5y$

**Solucionario:**
1. $x + 1$
2. $a^2 + \frac{1}{2}a$
3. $-4y^2 + 2y$
```

```ad-abstract
title: 🔴 Nivel: Avanzado — Aplicación de Costo Unitario
**Problema:** El costo total de una fábrica es $(\frac{4}{5}x^{n+3} - \frac{2}{3}x^{n+2} + 10x^{n+1})$ USD para producir $(\frac{2}{5}x^{n+1})$ unidades. Encuentre la expresión del costo unitario.

**Desglose del procedimiento:**
1. **Término 1:** $(\frac{4}{5} \div \frac{2}{5}) x^{(n+3)-(n+1)} = \frac{4 \cdot 5}{5 \cdot 2}x^2 = \frac{20}{10}x^2 = 2x^2$
2. **Término 2:** $(-\frac{2}{3} \div \frac{2}{5}) x^{(n+2)-(n+1)} = -\frac{2 \cdot 5}{3 \cdot 2}x^1 = -\frac{10}{6}x = -\frac{5}{3}x$
3. **Término 3:** $(10 \div \frac{2}{5}) x^{(n+1)-(n+1)} = \frac{10 \cdot 5}{1 \cdot 2}x^0 = \frac{50}{2} = 25$

✅ **Solucionario:** $(2x^2 - \frac{5}{3}x + 25)$ USD
```

> [!tip] 💡 Consejo de estudio
> ¡No olvides el orden! Verifica siempre el **signo** antes de cualquier cálculo. Si al operar notas que un término es idéntico arriba y abajo, recuerda que su división es **1**. Nunca dejes un espacio vacío; ese 1 es el que sostiene la estructura de tu polinomio. ¡Sigue practicando!