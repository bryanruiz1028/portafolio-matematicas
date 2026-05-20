# Clase 04 — Resolución de Inecuaciones Lineales de 3 Miembros

#algebra #solvingmembered

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 4 de 9

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [[Clase 03 - Inecuaciones de Primer Grado]]
> ⬆️ **Inicio:** [[00 - Índice del curso]]
> ➡️ **Siguiente:** [[Clase 05 - Sistemas de Inecuaciones Lineales]]

---

> [!info] 🌍 Relevancia y aplicaciones
> Las inecuaciones de 3 miembros nos permiten modelar situaciones donde una variable está limitada por un mínimo y un máximo simultáneamente, definiendo un rango de validez.
> 
> *   **💵 $USD:** Útil para modelar presupuestos donde el gasto total debe fluctuar estrictamente entre dos valores límite para mantener la rentabilidad.
> *   **🏗️ Construcción:** Fundamental para el control de calidad, estableciendo márgenes de tolerancia donde las medidas de una pieza deben estar entre un mínimo y un máximo para ser aceptadas.
> *   **📊 Situación cotidiana:** Para determinar rangos de temperatura segura, como en el almacenamiento de vacunas o alimentos, donde el clima debe ser mayor a $X$ pero menor a $Y$.

---

> [!note] 📌 ¿Qué es Resolviendo Inecuaciones de 3 Miembros?
> Es una expresión matemática que contiene dos signos de desigualdad, lo que divide la estructura en tres partes: **izquierda**, **centro** y **derecha**. El objetivo es aislar la variable (generalmente en el centro) para encontrar el intervalo de valores que satisface ambas condiciones al mismo tiempo.

> [!warning] ⚠️ Error común
> El error más grave es aplicar una operación de despeje (como restar o dividir) solo en dos de los miembros. Al ser una estructura triple, cualquier cambio debe replicarse en **los tres miembros** para no invalidar el resultado.

> [!tip] 💡 Truco para recordarlo
> **La Regla de la Balanza Triple:** Imagina una balanza con tres platos. Para mantener el equilibrio total, lo que le hagas al plato del centro, debes hacérselo obligatoriamente a los dos extremos. 
> *Nota: Este truco aplica únicamente cuando la variable está aislada en el centro; si hay variables en los extremos, usaremos el método de separación.*

---

### Procedimiento Paso a Paso

```text
PASO 1 → Diagnóstico: Identificar si la variable 'x' está únicamente en el miembro del centro o si aparece también en los extremos.

PASO 2 → Método Simultáneo (x solo en el centro): Aplicar operaciones inversas en los tres miembros a la vez. Es el camino más rápido para casos básicos.

PASO 3 → Método de Separación (Método Universal): Si hay variables en los extremos, se debe separar la expresión en dos inecuaciones independientes: 
   - Inecuación A: Miembros Izquierda y Centro.
   - Inecuación B: Miembros Centro y Derecha.
   *Importante: El miembro del centro se repite en ambas inecuaciones.*

PASO 4 → Intersección y Gráfica: Resolver ambas partes, buscar la zona donde se cruzan (intersección) en la recta numérica y escribir la solución en intervalo.
```

---

### Ejemplos Prácticos

> [!example] Ejemplo 1: Caso Básico (Video 1)
> **Problema:** Resolver $3 < x + 1 < 7$
> 1. Restamos 1 en los tres miembros simultáneamente:
>    $3 - 1 < x + 1 - 1 < 7 - 1$
> 2. Resultado: $2 < x < 6$
> 3. **Gráfica:** Círculos huecos en 2 y 6 (intervalo abierto).
> 4. **Intervalo:** $(2, 6)$

> [!example] Ejemplo 2: Coeficientes y Signos (Video 1)
> **Problema:** Resolver $5 \le 3x - 7 < 14$
> 1. Sumamos 7 en los tres miembros: $12 \le 3x < 21$
> 2. Dividimos entre 3: $4 \le x < 7$
> 3. **Intervalo:** $[4, 7)$
> *Recordatorio: Si dividiéramos por un número negativo, ambos signos de desigualdad deben invertirse.*

> [!example] Ejemplo 3: Caso Avanzado con Separación (Video 3)
> **Problema:** Resolver $-16 \le 3x + 2 < -5x + 10$
> Como hay variables en los extremos, separamos repitiendo el centro:
> *   **Parte A:** $-16 \le 3x + 2 \implies -18 \le 3x \implies -6 \le x$
> *   **Parte B:** $3x + 2 < -5x + 10 \implies 8x < 8 \implies x < 1$
> **Intersección:** Los valores que son $\ge -6$ y al mismo tiempo $< 1$.
> **Resultado:** $[-6, 1)$

> [!example] Ejemplo 4: Aplicación en Producción y Ganancia $USD (Video 4)
> **Problema:** El costo operativo y la proyección de ingresos en dólares para un producto están definidos por $1 + 4x \le 5x - 9 \le 10x + 6$, donde $x$ son unidades. ¿Cuál es el rango de producción para asegurar la rentabilidad?
> 1. **Separación:**
>    - $1 + 4x \le 5x - 9 \implies 10 \le x$
>    - $5x - 9 \le 10x + 6 \implies -15 \le 5x \implies -3 \le x$
> 2. **Análisis:** Buscamos la intersección de $x \ge 10$ y $x \ge -3$. El área común comienza en 10.
> 3. **Conclusión:** El rango de producción para asegurar la rentabilidad es de 10 unidades en adelante, permitiendo una ganancia proyectada dentro de los márgenes establecidos. Intervalo: $[10, \infty)$.

---

### Ejercicios para el Estudiante

```ad-abstract
title: 🟢 Nivel Fácil
1. $5 < x - 2 < 10$
2. $-3 \le x + 4 \le 8$
3. $10 < 2x < 20$
4. $0 \le x / 3 \le 2$
```

```ad-abstract
title: 🟡 Nivel Medio
1. $1 \le -2x + 5 < 9$
2. $4 < 3x - 2 \le 13$
3. $-10 \le \frac{x+2}{2} \le 5$
4. $5 < -x + 1 < 12$
```

```ad-abstract
title: 🔴 Nivel Avanzado (Aplicación $USD)
1. Un fabricante determina que sus ingresos $I$ deben cumplir: $2x + 10 \le 4x < 3x + 20$.
2. Presupuesto de evento: $100 \le 5x + 50 \le 500 - 10x$.
3. Rango de inversión: $-x + 40 \le 2x + 10 \le x + 100$.
4. Análisis de costos: $3x - 5 < 2x + 4 < 4x - 8$.
```

```ad-success
title: ✅ Respuestas
**Fácil:** 1. $(7, 12)$ | 2. $[-7, 4]$ | 3. $(5, 10)$ | 4. $[0, 6]$
**Medio:** 1. $(-2, 2]$ | 2. $(2, 5]$ | 3. $[-22, 8]$ | 4. $(-11, -4)$
**Avanzado:** 1. $[5, 20)$ | 2. $[10, 30]$ | 3. $[10, 90]$ | 4. $(6, 9)$
```

---

### Autoevaluación (Mini-Prueba)

1.  **¿Qué ocurre con los signos de desigualdad al multiplicar los tres miembros por un número negativo?**
    *   *Respuesta:* Ambos signos deben invertirse (ej. de $<$ a $>$ y de $\le$ a $\ge$) para mantener la veracidad de la expresión.
2.  **Si despejas $8 < 2x < 12$, ¿cuál es el intervalo resultante?**
    *   *Respuesta:* $(4, 6)$. Dividimos cada miembro entre 2.
3.  **¿Por qué se dice que el método de separación es el "universal"?**
    *   *Respuesta:* Porque funciona en todos los casos, incluyendo aquellos donde la variable aparece en más de un miembro, permitiendo hallar la intersección exacta.

---

> [!tip] 💡 En la próxima clase
> Conectaremos estos conceptos con los **Sistemas de Inecuaciones Lineales**, donde trabajaremos con múltiples restricciones independientes para resolver problemas de optimización más complejos.

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [[Clase 03 - Inecuaciones de Primer Grado]]
> ⬆️ **Inicio:** [[00 - Índice del curso]]
> ➡️ **Siguiente:** [[Clase 05 - Sistemas de Inecuaciones Lineales]]