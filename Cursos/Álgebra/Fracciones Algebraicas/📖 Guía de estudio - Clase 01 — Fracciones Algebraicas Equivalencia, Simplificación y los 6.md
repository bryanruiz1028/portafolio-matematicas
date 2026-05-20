# 📖 Guía de estudio — Clase 01: Métodos de Factorización y Fracciones Algebraicas

> [!info] 📌 Conceptos clave
> 1. **Prioridad del Factor Común:** Antes de intentar cualquier otro método, verifica si existe un factor que se repita en todos los términos. Este paso es el más rápido y se aplica a expresiones de cualquier número de términos.
> 2. **Conteo de términos:** Observar la estructura es vital. Si tienes $2$ términos, busca una Diferencia de Cuadrados o Suma/Diferencia de Cubos. Si tienes $3$ términos, enfócate en los tipos de trinomios.
> 3. **Lógica de potencias:** Para aplicar métodos específicos, identifica si los coeficientes son cuadrados perfectos (como $4, 9, 16$) o cubos perfectos (como $8, 27, 64$), y si los exponentes de las variables son divisibles por $2$ o $3$.
> 4. **Verificación de fracciones:** Dos fracciones algebraicas son equivalentes si el resultado de la **multiplicación de extremos y medios** es idéntico; es decir, el producto cruzado debe generar la misma expresión en ambos lados.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Factor Común** | Se extrae el máximo común divisor ($MCD$) de los coeficientes y la variable con el menor exponente. Se divide cada término original por este factor. |
| **Diferencia de Cuadrados** | Dos términos restándose con raíz cuadrada exacta: $a^2 - b^2 = (a - b)(a + b)$. |
| **Suma / Diferencia de Cubos** | Aplicable a raíces cúbicas. **Regla de signos:** El primer paréntesis lleva el mismo signo que el original; el segundo paréntesis tiene el término medio con signo opuesto y el último siempre positivo: $a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)$. |
| **Trinomio Cuadrado Perfecto** | Los extremos tienen raíces cuadradas exactas y el término central es el doble producto de estas: $a^2 \pm 2ab + b^2 = (a \pm b)^2$. |
| **Trinomio $x^2 + bx + c$** | Se buscan dos números que **multiplicados** den $c$ y **sumados o restados** (según los signos de los paréntesis) den $b$. |
| **Fracciones Equivalentes** | Dos fracciones $\frac{a}{b} = \frac{c}{d}$ son equivalentes si la multiplicación de **extremos y medios** se cumple: $a \cdot d = b \cdot c$. |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Factor Común
**Ejercicio:** Factorizar $5m^2 + 15m^3$

**Paso 1: Hallar el factor común.**
- **Coeficientes:** El $MCD$ entre $5$ y $15$ es $5$ (ambos son divisibles por $5$).
- **Variables:** Tomamos la letra que se repite con el menor exponente: $m^2$.
- **Factor común total:** $5m^2$.

**Paso 2: Dividir cada término entre el factor.**
- Primer término: $5m^2 \div 5m^2 = 1$.
- Segundo término: $15m^3 \div 5m^2 = 3m$ (según la ley de exponentes: $3 - 2 = 1$).

**Resultado final:** $5m^2(1 + 3m)$
```

```ad-example
title: Ejemplo B — Simplificación en contexto real $USD
**Ejercicio:** Un costo total se representa como $12x^3$ $USD$ y se divide entre $4x^2$ unidades. Simplifica la expresión para hallar el costo unitario.

**Paso 1: Simplificar coeficientes.**
Dividimos los números normalmente: $12 \div 4 = 3$.

**Paso 2: Simplificar variables (Lógica de cancelación).**
Restamos los exponentes porque estamos "cancelando" factores idénticos. Pensamos en $\frac{x \cdot x \cdot x}{x \cdot x}$. Al simplificar dos $x$ arriba y abajo, nos queda una sola $x$ en el numerador:
$x^{3-2} = x^1$.

**Resultado:** El costo simplificado es $3x$ $USD$ por unidad.
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
1. Identifica el factor común en la expresión: $3a + 3b$.
2. Factoriza la siguiente diferencia de cuadrados: $x^2 - y^2$.
3. Extrae el factor común (número y letra) de: $10x^2 - 5x$.
```

```ad-abstract
title: 🟡 Medio
1. Factoriza el trinomio de la forma $x^2 + bx + c$: $x^2 + 5x + 6$.
2. Verifica si las fracciones $\frac{x}{2}$ y $\frac{3x}{6}$ son equivalentes usando la multiplicación de extremos y medios.
3. Resuelve el trinomio: $x^2 - 7x + 10$.
```

```ad-abstract
title: 🔴 Avanzado
1. Factoriza el trinomio $2x^2 + 5x - 3$ utilizando el método de multiplicar y dividir toda la expresión por $a = 2$.
2. Simplifica el siguiente monomio y deja los exponentes positivos: $\frac{24a^5b^2c}{16a^2b^5}$.
3. **Problema de equivalencia:** Una empresa determina que su costo unitario es $\frac{x^2+5x+6}{x+2}$ $USD$, mientras que otra sostiene que es $x+3$ $USD$. Demuestra si ambas expresiones son equivalentes aplicando la multiplicación de extremos y medios (considera $x+3$ como $\frac{x+3}{1}$).
```

> [!tip] 💡 Consejo de estudio
> Como profesor, te garantizo que la clave del éxito en los exámenes es **contar los términos antes de operar**. Si ves solo $2$ términos, no pierdas tiempo buscando trinomios. Si ves $3$ términos, ignora las reglas de cubos. Esta clasificación inicial reduce tus opciones de error y te permite aplicar la fórmula correcta de inmediato, ahorrando minutos valiosos.