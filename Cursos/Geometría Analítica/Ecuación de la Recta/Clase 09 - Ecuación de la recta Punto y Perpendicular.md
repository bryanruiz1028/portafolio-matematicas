# Clase 09 — Ecuación de la recta: Punto y Perpendicular

#algebra #equationofaline
[[00 - Índice del curso]] | Bloque 3 | Lección 9 de 11

> [!info] 🧭 Navegación
> ◀ [[Clase 08 — Ecuación de la recta: Punto y Paralela]] | [[00 - Índice del curso]] | [[Clase 10 — Distancia de un punto a una recta]] ▶

---

## 1. ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> La perpendicularidad no es solo un concepto geométrico; es la base de la estabilidad estructural y la precisión tecnológica. Sin ángulos de 90°, los edificios colapsarían y nuestros sistemas de navegación fallarían.
> 
> - **Aplicación USD:** En ingeniería, la trayectoria más corta entre un punto y una línea de suministro (electricidad, fibra óptica o gas) es siempre la perpendicular. Calcular esta ruta correctamente permite minimizar el uso de materiales, ahorrando miles de dólares ($USD) en cables y tuberías.
> - **Aplicación Práctica:** El diseño urbano depende de cruces perpendiculares para maximizar la visibilidad y seguridad en las intersecciones viales.
> - **Situación Cotidiana:** ¿Has usado una escuadra para armar un mueble o diseñar un logo? Ese instrumento garantiza que dos líneas sean perpendiculares, evitando que tus proyectos queden "fuera de escuadra".

---

## 2. Concepto clave

> [!note] 📌 ¿Qué es la ecuación de una recta dado un punto y una perpendicular?
> Para definir una recta nueva que sea perpendicular a otra, necesitamos dos piezas de información: el punto por donde pasa y la **pendiente**. El truco está en que la pendiente de nuestra nueva recta debe ser la "opuesta y recíproca" de la original. Es decir, para que cruce formando 90°, debemos transformar la pendiente conocida.

> [!warning] ⚠️ Error común
> El error más típico es usar la misma pendiente de la recta original. Si usas la misma, estarás trazando una **paralela**. Para una perpendicular, las pendientes deben cumplir que su producto sea $-1$ ($m_1 \cdot m_2 = -1$).
> - ❌ **Incorrecto:** $m_1 = 2 \rightarrow m_2 = 2$ (Esto es para paralelas).
> - ✅ **Correcto:** $m_1 = 2 \rightarrow m_2 = -1/2$ (Esto es para perpendiculares).

> [!tip] 💡 Truco para recordarlo: "Gira y Cambia"
> Para obtener la pendiente perpendicular ($m_2$) sin complicaciones, aplica estos dos pasos:
> 1. **Gira:** Invierte la fracción (lo que está arriba pasa abajo y viceversa).
> 2. **Cambia:** Cambia el signo (si es positivo, ponlo negativo; si es negativo, ponlo positivo).
> *Ejemplo: Si $m = 3/4$, "Gira" a $4/3$ y "Cambia" a $-4/3$.*

---

## 3. Procedimiento paso a paso

Sigue este algoritmo lógico para resolver cualquier ejercicio:

```text
PASO 1: Identificar la pendiente (m1) de la recta dada.
        - Si es y = mx + b, m1 es el número junto a la x.
        - Si es Ax + By + C = 0, usa la fórmula m = -A/B.

PASO 2: Calcular la pendiente perpendicular (m2).
        - Aplica el truco "Gira y Cambia" para que m1 * m2 = -1.

PASO 3: Sustituir en la fórmula punto-pendiente.
        - Usa m2 y el punto dado (x1, y1) en: y - y1 = m2(x - x1).

PASO 4: Simplificar a la forma deseada.
        - Despeja 'y' para la forma explícita o iguala a cero para la general.
```

---

## 4. Ejemplos Desarrollados

> [!example] Ejemplo 1: Básico (Pendientes enteras)
> **Problema:** Hallar la recta que pasa por $(-4, 2)$ y es perpendicular a $y = 2x + 3$.
> 1. **m1:** La pendiente dada es $2$ (o $2/1$).
> 2. **m2:** Aplicando "Gira y Cambia", obtenemos $m_2 = -1/2$.
> 3. **Ecuación:** $y - 2 = -1/2(x - (-4)) \Rightarrow y - 2 = -1/2(x + 4)$.
> 4. **Desarrollo:** $y - 2 = -1/2x - 2 \Rightarrow y = -1/2x - 2 + 2$.
> **Resultado:** $y = -1/2x$.

> [!example] Ejemplo 2: Signos y Fracciones
> **Problema:** Pasa por $(3, 4)$ y es perpendicular a $y = -2/3x + 1$.
> 1. **m1:** La pendiente es $-2/3$.
> 2. **m2:** Invertimos y cambiamos signo: $m_2 = 3/2$.
> 3. **Ecuación:** $y - 4 = 3/2(x - 3) \Rightarrow y - 4 = 3/2x - 9/2$.
> 4. **Operación:** $y = 3/2x - 9/2 + 8/2 \Rightarrow y = 3/2x - 1/2$.
> **Resultado:** $y = 3/2x - 1/2$.

> [!example] Ejemplo 3: De Forma General a General
> **Problema:** Pasa por $(2, 3)$ y es perpendicular a $-4x + 6y - 5 = 0$.
> 1. **m1:** $m_1 = -A/B = -(-4)/6 = 4/6 = 2/3$.
> 2. **m2:** La perpendicular es $m_2 = -3/2$.
> 3. **Ecuación:** $y - 3 = -3/2(x - 2) \Rightarrow y - 3 = -3/2x + 3$.
> 4. **Forma General:** $3/2x + y - 6 = 0$. 
> 5. **Optimización:** Multiplicamos toda la ecuación por $2$ para eliminar fracciones y dejarla "estéticamente correcta":
> **Resultado Final:** $3x + 2y - 12 = 0$. (Comprobación: $3(2) + 2(3) - 12 = 6 + 6 - 12 = 0$).

> [!example] Ejemplo 4: Aplicación de Costos ($USD)
> **Problema:** Una empresa de telecomunicaciones debe conectar una estación en el punto $(1, 0)$ con una fibra óptica principal representada por $2x + 5y + 1 = 0$ usando la ruta perpendicular (la más corta). Calcula la ecuación y el presupuesto si la obra requiere 5 unidades de distancia a un costo de $100 USD por unidad.
> 1. **m1:** $m_1 = -A/B = -2/5$.
> 2. **m2:** La conexión perpendicular tendrá $m_2 = 5/2$.
> 3. **Ecuación:** $y - 0 = 5/2(x - 1) \Rightarrow y = 5/2x - 5/2$.
> 4. **Presupuesto:** Si la distancia es de 5 unidades: $5 \text{ unidades} \times \$100 \text{ USD/unidad} = \$500 \text{ USD}$.
> **Resultado:** La trayectoria sigue $y = 2.5x - 2.5$ con un costo total de $500 USD.

---

## 5. Ejercicios para el estudiante

> [!abstract] 🟢 Nivel Verde (Fácil)
> 1. Pasa por $(1, 2)$ y es perpendicular a $y = 3x - 1$.
> 2. Pasa por $(0, 5)$ y es perpendicular a $y = -2x + 4$.
> 3. Pasa por $(2, 2)$ y es perpendicular a $y = x + 10$.
> 4. Pasa por $(4, 1)$ y es perpendicular a $y = 4x$.

> [!abstract] 🟡 Nivel Amarillo (Medio)
> 1. Pasa por $(-1, 3)$ y es perpendicular a $2x - 4y + 5 = 0$.
> 2. Pasa por $(2, -2)$ y es perpendicular a $y = -3/4x + 2$.
> 3. Pasa por $(0, 0)$ y es perpendicular a $5x + 2y - 1 = 0$.
> 4. Pasa por $(3, 3)$ y es perpendicular a $x + y = 0$.

> [!abstract] 🔴 Nivel Rojo (Avanzado)
> 1. Una antena está en $(1, 1)$. Debe conectarse a un cable $3x - 2y + 4 = 0$ de forma perpendicular. Hallar la ecuación.
> 2. Calcula la ecuación perpendicular desde $(-2, 4)$ a $y = 1/2x + 1$. Si cada unidad de longitud en el plano cuesta $150 USD, ¿cuál es el costo si la conexión mide 4 unidades?
> 3. Un tren de alta velocidad debe ser perpendicular a una vía secundaria $y = -5x + 1$. Si la nueva vía pasa por $(10, 2)$, halla su ecuación y el costo de materiales para un tramo de 10 unidades a $500 USD cada una.
> 4. Determina la ecuación general de la recta perpendicular a $4x + 6y - 2 = 0$ que pasa por $(0, -3)$. Si el costo de mantenimiento es de $250 USD por cada unidad de longitud, calcula el total para 10 unidades.

> [!success] ✅ Respuestas para el docente
> **Verde:** 1) $y = -1/3x + 7/3$ | 2) $y = 1/2x + 5$ | 3) $y = -x + 4$ | 4) $y = -1/4x + 2$
> **Amarillo:** 1) $y = -2x + 1$ | 2) $y = 4/3x - 14/3$ | 3) $y = 2/5x$ | 4) $y = x$
> **Rojo:** 
> 1) $y = -2/3x + 5/3$
> 2) $y = -2x$. Costo: $4 \times 150 = \$600 \text{ USD}$.
> 3) $y = 1/5x$. Costo: $10/5 \text{ (simplificado)} \rightarrow 10 \times 500 = \$5000 \text{ USD}$.
> 4) $3x - 2y - 6 = 0$. Costo: $10 \times 250 = \$2500 \text{ USD}$.

---

## 6. Mini-prueba de autoevaluación

> [!question] Pregunta 1
> Si una recta tiene pendiente $m = -4$, ¿cuál debe ser la pendiente de una recta perpendicular?
> **Respuesta:** $1/4$. La explicación es que $(-4) \cdot (1/4) = -1$, cumpliendo la condición de perpendicularidad.

> [!question] Pregunta 2
> ¿Cuál es la pendiente perpendicular a la recta $3x + 2y - 5 = 0$?
> **Respuesta:** $m = 2/3$. Primero hallamos $m_1 = -A/B = -3/2$. Al aplicar "Gira y Cambia" obtenemos $2/3$.

> [!question] Pregunta 3
> Si una trayectoria perpendicular cuesta $200 USD/km y la ecuación resultante es $y = 1x$ pasando por $(1,1)$, ¿es realmente perpendicular a $y = -x + 5$?
> **Respuesta:** Sí. Las pendientes son $m_1 = 1$ y $m_2 = -1$. Como $1 \cdot (-1) = -1$, se confirma que son perpendiculares y la trayectoria es la de menor costo para el presupuesto.

---

## 7. Notas finales y Navegación

> [!tip] 💡 En la próxima clase
> Ya dominas cómo encontrar la ecuación de una recta perpendicular. En la siguiente sesión, daremos el paso final: aprender a calcular la **distancia exacta** entre un punto y una recta. Esto te permitirá calcular presupuestos reales sin depender de que te den la distancia como un dato extra.

> [!info] 🧭 Navegación
> ◀ [[Clase 08 — Ecuación de la recta: Punto y Paralela]] | [[00 - Índice del curso]] | [[Clase 10 — Distancia de un punto a una recta]] ▶