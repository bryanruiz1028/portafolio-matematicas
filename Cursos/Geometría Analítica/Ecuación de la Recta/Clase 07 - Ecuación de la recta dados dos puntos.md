# Clase 07 — Ecuación de la recta dados dos puntos

#algebra #equationofaline

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [Clase 06 — Ecuación punto-pendiente](link_clase_06) | 🏠 **Inicio:** [Curso de Álgebra](link_curso) | ➡️ **Siguiente:** [Clase 08 — Gráfica de funciones lineales](link_clase_08)

---

## 🌍 Relevancia y aplicaciones

> [!info] 🌍 Relevancia y aplicaciones
> Calcular la trayectoria entre dos puntos permite modelar el comportamiento de un fenómeno constante y predecir resultados futuros basándose en una tendencia. Es la herramienta fundamental para entender cómo cambia una variable respecto a otra en cualquier sistema lineal.
> 
> *   **Costo de suscripciones ($USD):** Determinar el precio total basándose en un costo de conexión (punto 1) y el consumo acumulado (punto 2).
> *   **Ingeniería y Construcción:** Calcular la inclinación o pendiente exacta ($m$) necesaria para rampas de acceso uniendo la altura inicial con la final.
> *   **Situaciones cotidianas:** Estimar el consumo de combustible por kilómetro basándose en dos mediciones de distancia y litraje en un viaje.

---

## Concepto Clave y Reglas

> [!note] Definición para principiantes
> Imagina que tienes dos puntos exactos en un mapa (plano cartesiano). Encontrar la ecuación de la recta es como descubrir la **"regla mágica"** que permite unir esos dos puntos con una línea infinita y perfecta.

> [!warning] ⚠️ Error común: El choque de signos
> El error más frecuente ocurre al restar coordenadas negativas. La fórmula tiene un signo "menos" por defecto; si la coordenada también es negativa, debes aplicar ley de signos: **menos por menos es más**.
> *Ejemplo:* Si tienes $y_2 - y_1$ donde $y_2 = 3$ y $y_1 = -1$, la operación es $3 - (-1) = 3 + 1 = 4$. ¡No los restes!

> [!tip] 💡 El Método de Profe Alex (vs. El método tradicional)
> Muchos libros usan una "fórmula monstruo" llena de letras: $y - y_1 = \frac{y_2 - y_1}{x_2 - x_1}(x - x_1)$.
> **¡Evita ese laberinto!** Es mucho más fácil y seguro usar el método de dos pasos:
> 1.  Calculas la **pendiente** ($m$) por separado.
> 2.  Usas la fórmula **punto-pendiente** (más corta y conocida).

---

## Procedimiento paso a paso

```text
PASO 1 → Etiquetar los puntos como (x1, y1) y (x2, y2).
PASO 2 → Calcular la pendiente (m) con la fórmula: m = (y2 - y1) / (x2 - x1).
PASO 3 → Utilizar la fórmula punto-pendiente: y - y1 = m(x - x1).
PASO 4 → Despejar "y" para obtener la forma simplificada: y = mx + b.
```

---

## Ejemplos Desarrollados

```ad-example
title: Ejemplo 1: Básico
**Puntos:** $A(5, 2)$ y $B(3, 6)$

1. **Cálculo de $m$:**
   $m = \frac{6 - 2}{3 - 5} = \frac{4}{-2} = -2$
2. **Ecuación Punto-Pendiente (usando punto A):**
   $y - 2 = -2(x - 5)$
3. **Despeje de $y$:**
   $y - 2 = -2x + 10$
   $y = -2x + 10 + 2$
   **Resultado:** $y = -2x + 12$
```

```ad-example
title: Ejemplo 2: Manejo de Signos Negativos
**Puntos:** $A(-3, -1)$ y $B(-1, 3)$

1. **Cálculo de $m$ (Cuidado con los signos):**
   $m = \frac{3 - (-1)}{-1 - (-3)} = \frac{3 + 1}{-1 + 3} = \frac{4}{2} = 2$
2. **Ecuación Punto-Pendiente:**
   $y - (-1) = 2(x - (-3))$
   $y + 1 = 2(x + 3)$
3. **Despeje de $y$:**
   $y + 1 = 2x + 6$
   $y = 2x + 6 - 1$
   **Resultado:** $y = 2x + 5$
```

```ad-example
title: Ejemplo 3: Avanzado (Fracciones)
**Puntos:** $A(-1, -\frac{5}{2})$ y $B(\frac{2}{3}, -\frac{5}{3})$

1. **Cálculo de $m$ (Método Carita Feliz):**
   Numerador: $-\frac{5}{3} - (-\frac{5}{2}) = -\frac{5}{3} + \frac{5}{2} = \frac{-10 + 15}{6} = \frac{5}{6}$
   Denominador: $\frac{2}{3} - (-1) = \frac{2}{3} + \frac{3}{3} = \frac{5}{3}$
   División (Ley del Sándwich): $\frac{5 \cdot 3}{6 \cdot 5} = \frac{15}{30} = \frac{1}{2}$
   **$m = \frac{1}{2}$**
2. **Ecuación Punto-Pendiente:**
   $y - (-\frac{5}{2}) = \frac{1}{2}(x - (-1)) \to y + \frac{5}{2} = \frac{1}{2}(x + 1)$
3. **Despeje de $y$:**
   $y = \frac{1}{2}x + \frac{1}{2} - \frac{5}{2} \to y = \frac{1}{2}x - \frac{4}{2}$
   **Resultado:** $y = \frac{1}{2}x - 2$
```

```ad-example
title: Ejemplo 4: Aplicación en USD (Precio Unitario)
**Problema:** Si 5 artículos cuestan $12 USD y 10 artículos cuestan $22 USD, halla la ecuación.

1. **Puntos:** $(5, 12)$ y $(10, 22)$
2. **Cálculo de $m$:**
   $m = \frac{22 - 12}{10 - 5} = \frac{10}{5} = 2$
   *Interpretación: El precio por unidad es de $2 USD.*
3. **Ecuación:**
   $y - 12 = 2(x - 5) \to y - 12 = 2x - 10$
4. **Despeje final:**
   $y = 2x - 10 + 12$
   **Resultado:** $y = 2x + 2$
```

---

## Ejercicios y Autoevaluación

```ad-abstract
title: Ejercicio Verde (Fácil)
Hallar la ecuación de la recta que pasa por:
$A(0, -1)$ y $B(2, 5)$
```

```ad-abstract
title: Ejercicio Amarillo (Medio)
Hallar la ecuación de la recta que pasa por:
$A(-2, 2)$ y $B(1, -7)$
```

```ad-abstract
title: Ejercicio Rojo (Avanzado)
Hallar la ecuación de la recta que pasa por:
$A(\frac{3}{4}, -\frac{3}{2})$ y $B(\frac{4}{3}, -\frac{1}{3})$
```

```ad-success
title: Respuestas
*   **Verde:** $y = 3x - 1$
*   **Amarillo:** $y = -3x - 4$
*   **Rojo:** $y = 2x - 3$
```

---

## Mini-prueba de autoevaluación

```ad-question
title: Pregunta 1: Orientación
Si al calcular la pendiente el resultado es un número negativo (ej. $m = -3$), ¿qué significa esto respecto a la inclinación de la recta?
```

```ad-question
title: Pregunta 2: Signos
¿Cuál es el resultado de la operación $y_2 - y_1$ si $y_2 = 5$ y $y_1 = -4$?
```

```ad-question
title: Pregunta 3: Concepto Económico
En ventas, si 2 productos cuestan $10 USD y 4 productos cuestan $20 USD, ¿qué representa físicamente el valor de la pendiente $m = 5$?
```

---

## Cierre y Navegación Final

> [!tip] 💡 En la próxima clase
> Aprenderemos cómo graficar estas funciones de manera ultra rápida utilizando únicamente la **ordenada al origen** ($b$) y el movimiento de la pendiente ($m$), sin necesidad de tablas de valores.

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [Clase 06 — Ecuación punto-pendiente](link_clase_06) | 🏠 **Inicio:** [Curso de Álgebra](link_curso) | ➡️ **Siguiente:** [Clase 08 — Gráfica de funciones lineales](link_clase_08)