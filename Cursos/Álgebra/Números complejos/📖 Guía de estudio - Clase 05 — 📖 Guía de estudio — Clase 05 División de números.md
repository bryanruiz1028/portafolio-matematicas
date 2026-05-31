# 📖 Guía de estudio — Clase 05: División de números complejos

> [!info] 📌 Conceptos clave
> - **El conjugado de un número complejo:** Se define como el mismo número, pero invirtiendo el signo de su **parte imaginaria**. Si tenemos $a + bi$, su conjugado será $a - bi$.
> - **Propiedad fundamental de $i$:** En todo desarrollo algebraico de complejos, la unidad imaginaria elevada al cuadrado debe sustituirse por su valor real: $i^2 = -1$.
> - **Objetivo de la división:** El propósito técnico de la división es eliminar la unidad imaginaria del denominador. Esto se logra multiplicando tanto el numerador como el denominador por el conjugado del denominador, convirtiendo así el divisor en un número real.

### TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Conjugado ($\bar{z}$ o $|z|$)** | Se representa con una línea superior o barras laterales. Consiste en cambiar el signo del término que contiene la $i$. |
| **Producto por el conjugado** | $(a + bi)(a - bi) = a^2 - (bi)^2 = a^2 + b^2$. El resultado es siempre un número real (desaparece la $i$). |
| **Potencia fundamental** | $i^2 = -1$. Identidad clave para simplificar tras realizar la propiedad distributiva. |

---

### EJEMPLOS RESUELTOS ADICIONALES

````ad-example
title: Ejemplo A — División simple 
**Ejercicio:** Resolver la división de $Z_1 = -4 + 5i$ entre $Z_2 = 8 - 2i$.

1. **Planteamiento:** Multiplicamos numerador y denominador por el conjugado del denominador ($8 + 2i$):
   $$\frac{-4 + 5i}{8 - 2i} \cdot \frac{8 + 2i}{8 + 2i}$$

2. **Numerador (Propiedad distributiva):**
   $$(-4 \cdot 8) + (-4 \cdot 2i) + (5i \cdot 8) + (5i \cdot 2i)$$
   $$-32 - 8i + 40i + 10i^2$$
   **Sustitución de $i^2$:** $-32 + 32i + 10(-1) \implies -32 + 32i - 10 = -42 + 32i$

3. **Denominador (Producto notable):**
   Aplicamos $(a - bi)(a + bi) = a^2 - (bi)^2$:
   $$(8)^2 - (2i)^2 = 64 - (4i^2)$$
   **Sustitución de $i^2$:** $64 - 4(-1) = 64 + 4 = 68$

4. **Simplificación final:**
   $$\frac{-42 + 32i}{68} = -\frac{42}{68} + \frac{32}{68}i$$
   Extrayendo mitad en ambas fracciones obtenemos el resultado exacto: **$-\frac{21}{34} + \frac{8}{17}i$**
````

````ad-example
title: Ejemplo B — Aplicación de costos complejos en $USD 
**Escenario:** En un análisis de costos técnicos, un valor total de $(-12 + 24i)$ USD debe distribuirse entre un factor de riesgo representado por el complejo $(2 - 2i)$.

1. **Planteamiento:**
   $$\frac{-12 + 24i}{2 - 2i} \cdot \frac{2 + 2i}{2 + 2i}$$

2. **Desarrollo del numerador:**
   $$-24 - 24i + 48i + 48i^2$$
   $$-24 + 24i + 48(-1) \implies -24 + 24i - 48 = -72 + 24i$$

3. **Desarrollo del denominador:**
   $$(2)^2 - (2i)^2 = 4 - 4(-1) = 4 + 4 = 8$$

4. **Resultado final:**
   $$\frac{-72}{8} + \frac{24}{8}i = -9 + 3i$$
   El costo resultante es **$-9 + 3i$** USD. *Nota pedagógica: En contextos técnicos, la parte real e imaginaria pueden representar diferentes vectores de costo (fijos vs. variables).*
````

---

### EJERCICIOS DE REPASO

````ad-abstract
title: 🟢 Fácil 
Halla el conjugado ($\bar{z}$) de los siguientes números (recuerda cambiar solo el signo de la parte imaginaria):
1. $z = 3 + 2i$
2. $z = -5 - 4i$
3. $z = 8i$
````

````ad-abstract
title: 🟡 Medio 
Resuelve las siguientes divisiones siguiendo los pasos de simplificación vistos en clase:
1. $\frac{2 + 3i}{1 - 2i}$
2. $\frac{5 - i}{2 + i}$
````

````ad-abstract
title: 🔴 Avanzado — Aplicación con $USD 
**Problema de Deuda Compartida:** Una inversión en un fondo de riesgo está valorada en $(20 + 40i)$ USD. Si este valor se divide entre un factor de impacto de $(3 + i)$, ¿cuál es el resultado de la operación?

*(Solución para autoevaluación: $10 + 10i$)*
````

---

> [!tip] 💡 Consejo de estudio: La Regla de la Parte Imaginaria
> Es un error común intentar cambiar los signos de ambos números. Para hallar el conjugado, **solo se debe cambiar el signo del término que acompaña a la $i$**. Si el número estuviera desordenado (ejemplo: $5i + 3$), su conjugado sería $-5i + 3$. La parte real siempre mantiene su signo original. No te guíes solo por "el signo del centro", sino por identificar correctamente la parte imaginaria.