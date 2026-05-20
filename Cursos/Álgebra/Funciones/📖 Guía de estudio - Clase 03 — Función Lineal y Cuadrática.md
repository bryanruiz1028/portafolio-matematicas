# 📖 Guía de estudio — Clase 03: Gráfica de la función lineal

```ad-info
title: 📌 Conceptos clave
- **Identificación:** Una función es lineal cuando la variable $x$ tiene exponente 1 (o 0), no está en el denominador ni dentro de una raíz.
- **Representación gráfica:** Toda función lineal genera una línea recta en el plano cartesiano.
- **Tipos de rectas:** Las funciones pueden ser **oblicuas** (inclinadas, contienen la variable $x$) u **horizontales** (paralelas al eje $x$, no contienen la variable $x$).
- **¡Importante!:** Las rectas **verticales** no son funciones, por lo que no las estudiaremos en este apartado.
- **Dominio y Rango:** El dominio siempre son todos los números reales. El rango son todos los reales en funciones oblicuas, pero en las horizontales es únicamente el valor de la constante $\{b\}$.
```

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Función Lineal** | Expresión de la forma $y = ax + b$ o $f(x) = ax + b$. Su representación siempre es una línea recta. |
| **Dominio** | Conjunto de todos los valores que puede tomar $x$. En funciones lineales, son todos los números reales ($\mathbb{R}$). |
| **Rango** | Conjunto de valores resultantes en $y$. En oblicuas son todos los reales ($\mathbb{R}$); en horizontales es solo el conjunto unitario del valor constante $\{b\}$. |
| **Función Horizontal** | Tipo de función lineal sin inclinación que carece de la variable $x$ (ejemplo: $y = 3$). |

## Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A — Graficar f(x) = 2x - 1
Para graficar con precisión, seguiremos este proceso de 3 pasos:

**Paso 1: Crear tabla de valores**
Elegimos valores sencillos para $x$ (0, 1, 2) y calculamos cada imagen:
- Para $x = 0 \Rightarrow f(0) = 2(0) - 1 = -1$ $\rightarrow$ Punto $(0, -1)$
- Para $x = 1 \Rightarrow f(1) = 2(1) - 1 = 1$ $\rightarrow$ Punto $(1, 1)$
- Para $x = 2 \Rightarrow f(2) = 2(2) - 1 = 3$ $\rightarrow$ Punto $(2, 3)$

**Paso 2: Ubicar puntos en el plano**
Dibujamos los tres puntos $(0, -1)$, $(1, 1)$ y $(2, 3)$ en el plano cartesiano.

**Paso 3: Trazar la recta**
Unimos los puntos usando una regla para formar la recta.

✅ **Resultado:** Una recta oblicua.
```

```ad-example
title: Ejemplo B — Costo de un servicio
**Problema:** Un técnico cobra una base fija de $10 USD más $5 USD por cada hora de trabajo. La función es $y = 5x + 10$.

**Cálculo de valores:**
- **0 horas:** $y = 5(0) + 10 = 10 \rightarrow$ **$10.00 USD**
- **1 hora:** $y = 5(1) + 10 = 15 \rightarrow$ **$15.00 USD**
- **2 horas:** $y = 5(2) + 10 = 20 \rightarrow$ **$20.00 USD**

✅ **Resultado:** El costo total aumenta de forma constante según las horas trabajadas.
```

## Ejercicios de Repaso

```ad-abstract
title: 🟢 Fácil
Indica si las siguientes ecuaciones representan una función lineal (Sí/No):
1. $f(x) = 5x + 3$
2. $g(x) = \frac{2}{x}$
3. $h(x) = x^2 - 4$

**Pista (Solucionario):** La (1) es lineal. La (2) es una función **Racional** y la (3) es una **Cuadrática**; por lo tanto, no son lineales.
```

```ad-abstract
title: 🟡 Medio
Dada la ecuación $2y - 4x = 6$:
1. **Despeja la variable $y$:** (Recuerda que despejamos para que sea mucho más fácil calcular la tabla de valores).
2. **Realiza una tabla de valores** con $x = 0, 1, 2$.
3. **Grafica la función** y determina su dominio y rango.

*Nota de ayuda:* El despeje correcto es $y = \frac{6 + 4x}{2}$, que simplificado es **$y = 2x + 3$**.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
**Problema de "Ahorro Semanal":**
Un estudiante comienza sus ahorros con $20 USD y decide agregar $5 USD cada semana.
1. **Escribe la función lineal** que representa el ahorro total ($y$) según las semanas ($x$). *(Usa la estructura $y = ax + b$)*.
2. **Genera una tabla de valores** para las semanas 0, 1, 2 y 3.
3. **Representa gráficamente** el crecimiento del ahorro.

*Dato:* La función requerida es $y = 5x + 20$.
```

```ad-tip
title: 💡 Consejo de estudio
Para asegurar que tu gráfica sea impecable, sigue la estrategia del **"profe Alex"**: utiliza siempre **al menos 3 puntos** en tu tabla de valores. Estos tres puntos funcionan como una señal de seguridad: si al unirlos no forman una línea recta perfecta, sabrás de inmediato que hubo un error de cálculo en alguno de ellos y podrás corregirlo a tiempo.
```