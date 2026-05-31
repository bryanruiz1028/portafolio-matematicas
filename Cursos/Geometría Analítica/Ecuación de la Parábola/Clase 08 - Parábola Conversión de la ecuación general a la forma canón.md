# Clase 08 — Parábola: Conversión de la ecuación general a la forma canónica u ordinaria

#algebra #parabolaconvert

> [!info] 🧭 Navegación
> - ⬅️ **Clase anterior:** [Clase 07 — Elementos de la Parábola](...)
> - 🏠 **Índice:** [Curso de Geometría Analítica](...)
> - ➡️ **Próxima clase:** [Clase 09 — Gráfica de la parábola desde la forma canónica](...)

---

## 1. ¿Por qué es importante esta clase?

Como especialistas en Geometría Analítica, sabemos que la información en su estado "bruto" suele ser poco útil. La **ecuación general** de la parábola nos confirma su existencia, pero oculta sus propiedades geométricas vitales. Realizar la conversión a la **forma canónica (u ordinaria)** es un proceso de "revelación algebraica" que nos permite identificar instantáneamente el vértice, la orientación y la distancia focal.

**Aplicaciones en el mundo real:**
- 💵 **Aplicación $USD:** En finanzas, los modelos de costos marginales o análisis de volatilidad suelen seguir funciones cuadráticas. Encontrar el vértice de la parábola permite identificar el punto de equilibrio o el costo mínimo de producción, optimizando la rentabilidad del capital invertido.
- 🏗️ **Aplicación práctica:** El diseño de infraestructuras críticas, como puentes colgantes o reflectores parabólicos, requiere la forma canónica para ubicar con precisión milimétrica el receptor en el foco o los puntos de tensión máxima en los cables.
- 📊 **Situación cotidiana:** En la física del deporte, la trayectoria de un balón es una parábola. Convertir su ecuación general a canónica permite predecir el punto más alto del vuelo y el alcance exacto del lanzamiento.

---

## 2. Concepto clave

Convertir la ecuación es, en esencia, un proceso de reordenamiento de datos. Pasamos de una expresión igualada a cero a una estructura factorizada que expone los parámetros de la curva.

> [!note] 📌 Definiciones
> - **Ecuación General:** $Ax^2 + Dx + Ey + F = 0$ (si el eje es vertical) o $Cy^2 + Dx + Ey + F = 0$ (si el eje es horizontal).
> - **Ecuación Canónica:** $(x-h)^2 = 4p(y-k)$ o $(y-k)^2 = 4p(x-h)$.
>   - El punto $(h, k)$ es el **Vértice**.
>   - El coeficiente $4p$ representa el **Lado Recto**, y $p$ es el **Parámetro** que define la distancia del vértice al foco.

> [!warning] ⚠️ El Principio de la Balanza
> Al completar el **Trinomio Cuadrado Perfecto (TCP)**, es imperativo sumar el mismo valor numérico en ambos lados de la igualdad. Si olvidas añadir el número en el lado derecho, la "balanza" de la ecuación se rompe y el resultado será geométricamente incorrecto.

> [!tip] 💡 Truco: La Regla de la "Mitad al Cuadrado"
> Para completar el TCP, identifica el **término lineal de la misma variable** que estás agrupando (el término con exponente 1). Toma su coeficiente ($b$), divídelo entre 2 y eleva el resultado al cuadrado: $\mathbf{(\frac{b}{2})^2}$.

---

## 3. Procedimiento paso a paso

Para realizar una conversión rigurosa y sin errores, aplicaremos la metodología secuencial del Profe Alex:

```text
PASO 1: Identificar la variable cuadrática (x² o y²). Agrupar los términos de esa 
        variable a la izquierda y trasladar todo lo demás a la derecha del igual.
PASO 2: Normalizar la variable cuadrática. El coeficiente de x² o y² debe ser 1. 
        Si es distinto, dividir CADA término de la ecuación por dicho coeficiente.
PASO 3: Completar el Trinomio Cuadrado Perfecto (TCP). Sumar (b/2)² en ambos 
        lados para mantener el equilibrio de la ecuación.
PASO 4: Factorizar el lado izquierdo como un binomio al cuadrado. En el lado 
        derecho, sacar como factor común el coeficiente de la variable lineal 
        (aunque no sea divisor exacto, "a las malas") para que la variable 
        quede con coeficiente 1 dentro del paréntesis.
```

---

## 4. Ejemplos de clase

> [!example] Ejemplo 1: Caso Base con $x^2$
> **Ecuación inicial:** $x^2 - 6x - 12y - 15 = 0$
> 1. Agrupamos $x$ a la izquierda: $x^2 - 6x = 12y + 15$
> 2. Completamos TCP: Mitad de $6 = 3$; $3^2 = \mathbf{9}$.
>    $x^2 - 6x + \mathbf{9} = 12y + 15 + \mathbf{9}$
> 3. Simplificamos derecha: $x^2 - 6x + 9 = 12y + 24$
> 4. Factorizamos (Lado Recto $4p = 12$): **$(x - 3)^2 = 12(y + 2)$**

> [!example] Ejemplo 2: Caso con Variable $y^2$ y Signos
> **Ecuación inicial:** $y^2 + 16y - 15x + 79 = 0$
> 1. Agrupamos $y$ a la izquierda: $y^2 + 16y = 15x - 79$
> 2. Completamos TCP: Mitad de $16 = 8$; $8^2 = \mathbf{64}$.
>    $y^2 + 16y + \mathbf{64} = 15x - 79 + \mathbf{64}$
> 3. Simplificamos derecha: $y^2 + 16y + 64 = 15x - 15$
> 4. Factorizamos (Lado Recto $4p = 15$): **$(y + 8)^2 = 15(x - 1)$**

> [!example] Ejemplo 3: Coeficiente Principal $> 1$
> **Ecuación inicial:** $2x^2 - 12x - 2y + 14 = 0$
> 1. Dividimos cada término entre $2$: $\frac{2x^2}{2} - \frac{12x}{2} - \frac{2y}{2} + \frac{14}{2} = \frac{0}{2}$
>    Obtenemos: $x^2 - 6x - y + 7 = 0$
> 2. Agrupamos: $x^2 - 6x = y - 7$
> 3. Completamos TCP: $(\frac{6}{2})^2 = \mathbf{9}$.
>    $x^2 - 6x + \mathbf{9} = y - 7 + \mathbf{9}$
> 4. Factorizamos: **$(x - 3)^2 = 1(y + 2)$** (Donde $4p = 1$).

> [!example] Ejemplo 4: Aplicación Real ($USD)
> El costo de producción de un componente tecnológico se modela mediante: $C = y^2 - 10y - 4x + 45$. Halle la forma canónica para ubicar el vértice.
> 1. Reordenamos: $y^2 - 10y = 4x - 45$
> 2. Completamos TCP: $(\frac{10}{2})^2 = \mathbf{25}$.
>    $y^2 - 10y + \mathbf{25} = 4x - 45 + \mathbf{25}$
> 3. Simplificamos: $y^2 - 10y + 25 = 4x - 20$
> 4. Factorizamos: **$(y - 5)^2 = 4(x - 5)$**
> 
> **Interpretación técnica:** El vértice está en $(5, 5)$. Dado que $4p = 4$ (positivo) y la variable cuadrática es $y$, la parábola abre hacia la derecha. Esto indica que $x = 5$ es el valor mínimo de inversión/producción requerido para que el modelo comience a operar en este cuadrante.

---

## 5. Ejercicios para el estudiante

> [!abstract] 🟢 Nivel Fácil (Coeficiente principal = 1)
> 1. $x^2 + 8x + 8y + 8 = 0$
> 2. $x^2 - 4x - 12y - 8 = 0$
> 3. $x^2 + 10x + 4y + 13 = 0$
> 4. $x^2 - 2x - 8y + 17 = 0$

> [!abstract] 🟡 Nivel Medio (Términos en $y^2$ y signos negativos)
> 5. $y^2 + 6y - 8x + 33 = 0$
> 6. $y^2 - 10y - 4x + 1 = 0$
> 7. $y^2 + 4y + 12x - 20 = 0$
> 8. $y^2 - 8y + 16x + 48 = 0$

> [!abstract] 🔴 Nivel Avanzado (Análisis de inversión y Fracciones)
> 9. La trayectoria de un dron de entrega de $500 USD sigue la ecuación $y^2 - y - 3x - 10.25 = 0$. Conviértela a su forma canónica para identificar su vértice y el valor de $4p$ (Sugerencia: $10.25 = \frac{41}{4}$).
> 10. Un arco para un puente de $1M USD sigue la ecuación $x^2 + 2x - 6y + 19 = 0$.
> 11. $3x^2 - 12x - 12y - 24 = 0$
> 12. $2y^2 + 4y - 10x + 22 = 0$

---

## 6. Solucionario para el docente

> [!success] Respuestas y Procedimientos Clave
> 1. $(x + 4)^2 = -8(y - 1)$
> 2. $(x - 2)^2 = 12(y + 1)$
> 3. $(x + 5)^2 = -4(y - 3)$
> 4. $(x - 1)^2 = 8(y - 2)$
> 5. $(y + 3)^2 = 8(x - 3)$
> 6. $(y - 5)^2 = 4(x + 6)$
> 7. $(y + 2)^2 = -12(x - 2)$
> 8. $(y - 4)^2 = -16(x + 2)$
> 9. $(y - \frac{1}{2})^2 = 3(x + \frac{7}{2})$. Vértice: $(-\frac{7}{2}, \frac{1}{2})$, $4p = 3$.
> 10. $(x + 1)^2 = 6(y - 3)$
> 11. **Paso 1 (División entre 3):** $x^2 - 4x - 4y - 8 = 0 \rightarrow (x - 2)^2 = 4(y + 3)$
> 12. **Paso 1 (División entre 2):** $y^2 + 2y - 5x + 11 = 0 \rightarrow (y + 1)^2 = 5(x - 2)$

---

## 7. Mini-prueba de autoevaluación

> [!question] Pregunta 1
> En la ecuación $x^2 + 10x + Ey + F = 0$, ¿qué valor debe sumarse a ambos lados para completar el Trinomio Cuadrado Perfecto?
> - a) $10$
> - b) $25$
> - c) $100$
> - d) $5$

> [!question] Pregunta 2
> ¿Cuál es la forma canónica de la ecuación $x^2 - 6x - 8y - 7 = 0$?
> - a) $(x-3)^2 = 8(y+2)$
> - b) $(x+3)^2 = 8(y-2)$
> - c) $(x-3)^2 = 8(y-2)$
> - d) $(x-6)^2 = 8(y+7)$

> [!question] Pregunta 3 (Aplicación $USD)
> Una empresa modela sus activos mediante la parábola $(y-2)^2 = 4(x-1)$. ¿Cuál es el vértice o punto de inflexión de este modelo financiero?
> - a) $(2, 1)$
> - b) $(-1, -2)$
> - c) $(1, 2)$
> - d) $(4, 1)$

---

## 8. Notas para el próximo tema

> [!tip] 💡 Hacia la representación gráfica
> En la próxima sesión utilizaremos la **forma canónica** obtenida hoy como nuestra herramienta principal. Aprenderemos a extraer el valor de $p$ para localizar el foco y la directriz, permitiéndonos realizar gráficas precisas de cualquier sección parabólica.

---
> [!info] 🧭 Navegación
> - ⬅️ **Clase anterior:** [Clase 07 — Elementos de la Parábola](...)
> - 🏠 **Índice:** [Curso de Geometría Analítica](...)
> - ➡️ **Próxima clase:** [Clase 09 — Gráfica de la parábola desde la forma canónica](...)