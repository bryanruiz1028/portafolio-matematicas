# 📖 Guía de estudio — Clase 11: Función Compuesta

¡Hola! Soy tu profesor de matemáticas y en esta guía vamos a dominar la **función compuesta**. No te dejes intimidar por la notación; verás que es como un proceso de ensamblaje en una fábrica donde el producto de una máquina pasa a ser la materia prima de la siguiente. Recuerda siempre: ¡la práctica hace al maestro!

> [!info] 📌 Conceptos clave
> La **función compuesta** es la aplicación sucesiva de dos procesos. Imagina dos máquinas: la primera máquina ($f$) recibe una entrada $x$ y entrega un resultado. Ese resultado, en lugar de ser el final, se convierte en el "alimento" o entrada de una segunda máquina ($g$). 
> 
> - **Notación:** Se escribe $(g \circ f)(x)$, que se lee "g compuesta con f", y su definición operativa es $g(f(x))$.
> - **El orden importa:** La composición **no es conmutativa**. Esto significa que $(f \circ g)(x)$ suele ser muy diferente a $(g \circ f)(x)$.
> - **⚠️ ¡Cuidado con el símbolo!:** No confundas el círculo pequeño de la composición ($\circ$) con el punto de la multiplicación ($\cdot$). $(g \circ f)$ significa evaluar una dentro de otra; $(g \cdot f)$ significa multiplicar sus resultados.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Composición ($g \circ f$)** | Evaluar la función interna primero y usar ese resultado como la variable de la función externa: $g(f(x))$. |
| **Binomio al Cuadrado** | Fundamental para potencias: $(a + b)^2 = a^2 + 2ab + b^2$. *(¡No olvides el término del medio!)* |
| **Autocomposición** | Una función puede aplicarse a sí misma: $(f \circ f)(x) = f(f(x))$. |
| **Dominio de la Compuesta** | Son las $x$ en el dominio de $f$ tales que su imagen $f(x)$ pertenece al dominio de $g$. |

---

## Ejemplos resueltos

```ad-example
title: Ejemplo A — Sustitución Lineal Básica
Hallemos $(f \circ g)(x)$ usando $f(x) = 2x + 1$ y $g(x) = 4x - 2$.

**1. Reemplazar la función interna:** $f(g(x)) = f(4x - 2)$.
**2. Preparar la externa con paréntesis grandes:** $2(\quad) + 1$.
**3. Sustituir y distribuir:** $2(4x - 2) + 1 = 8x - 4 + 1$.
✅ **Resultado:** $8x - 3$.
```

```ad-example
title: Ejemplo B — Aplicación Cuadrática y Binomio
Hallemos $(f \circ g)(x)$ para $f(x) = x^2 + 2x - 1$ y $g(x) = 3x + 4$. Aquí aplicaremos el **binomio al cuadrado**.

**1. Identificar la estructura:** $f(g(x)) = f(3x + 4)$.
**2. Sustituir en cada "x" de la función externa:**
$(3x + 4)^2 + 2(3x + 4) - 1$
**3. Desarrollar el binomio y distribuir:**
- $(3x + 4)^2 = (3x)^2 + 2(3x)(4) + 4^2 = 9x^2 + 24x + 16$
- $2(3x + 4) = 6x + 8$
**4. Unir y reducir términos semejantes:**
$9x^2 + 24x + 16 + 6x + 8 - 1$
✅ **Resultado:** $9x^2 + 30x + 23$.
```

---

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil — Nivel Iniciación
Halla la composición $(g \circ f)(x)$ para los siguientes pares:
1. $f(x) = 3x - 1$ y $g(x) = 2x + 3$
2. $f(x) = x + 5$ y $g(x) = 4x$
3. $f(x) = 2x - 4$ y $g(x) = x + 10$
*Respuestas: 1) $6x + 1$; 2) $4x + 20$; 3) $2x + 6$*
```

```ad-abstract
title: 🟡 Medio — Cuadráticas y Autocomposición
Resuelve lo pedido aplicando el desarrollo algebraico correcto:
1. Si $f(x) = x^2 + 2$ y $g(x) = 3x + 1$, halla $(f \circ g)(x)$.
2. Si $f(x) = x^2 - 3$, halla la autocomposición $(f \circ f)(x)$.
3. Si $f(x) = x^2 + x$ y $g(x) = x - 1$, halla $(g \circ f)(x)$.
*Respuestas: 1) $9x^2 + 6x + 3$; 2) $x^4 - 6x^2 + 6$; 3) $x^2 + x - 1$*
```

```ad-abstract
title: 🔴 Avanzado — Aplicación y Racionales
1. **Impuestos y Envío:** Un producto cuesta $x$. Se aplica un impuesto del 10% ($f(x) = 1.10x$) y luego un envío de 5 USD ($g(x) = x + 5$). Halla el costo total $(g \circ f)(x)$.
2. **Costos Repartidos:** Halla $(g \circ f)(x)$ si $f(x) = \sqrt{x+1}$ y $g(x) = \frac{2x}{x-4}$. 
*Respuestas: 1) $1.10x + 5$; 2) $\frac{2\sqrt{x+1}}{\sqrt{x+1}-4}$*
```

---

> [!tip] 💡 El Consejo de Oro del Profe Alex
> **"Usa paréntesis grandes al sustituir"**. Este no es solo un consejo estético, es tu mejor defensa contra errores de signos. 
> 
> **Mira este error común:** Si tienes que evaluar $-3x$ con $x = (2x+1)$, muchos escriben $-3 \cdot 2x + 1 = -6x + 1$. ¡MAL! 
> Lo correcto es usar paréntesis: $-3(2x + 1) = -6x - 3$. 
> El paréntesis obliga al signo negativo a distribuirse a **toda** la expresión. ¡No ahorres tinta en los paréntesis!