# Clase 02 — Solución de Sistemas de Ecuaciones 3x3: Método de Reducción y Determinantes (Cramer)

tags: #algebra #solucindeunsist
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 4

> [!info] 🧭 Navegación
> [[Clase 01 — Sistemas 2x2]] | **Clase 02 — Sistemas 3x3** | [[Clase 03 — Casos Especiales]]

---

## 1. Importancia y Aplicaciones

> [!info] 🌍 Relevancia y aplicaciones
> Resolver un **sistema** de $3 \times 3$ es vital para modelar situaciones de la vida real donde tres **variables** distintas interactúan para producir un resultado equilibrado.
> - **💵 Aplicación $USD:** Permite calcular el costo exacto de tres productos diferentes (como el precio de un lápiz $x$, un cuaderno $y$ y un borrador $z$) basándose en tres compras distintas.
> - **🏗️ Aplicación práctica:** Es fundamental en ingeniería para calcular el equilibrio de fuerzas en estructuras o determinar las mezclas exactas de materiales en construcción.
> - **📊 Situación cotidiana:** Ayuda a gestionar inventarios complejos o a repartir presupuestos limitados entre tres departamentos de manera precisa.

---

## 2. Concepto Clave y Pedagogía

> [!note] 📌 ¿Qué es Solución de un sistema de 3x3?
> Imagina que tienes tres acertijos que usan las mismas tres **incógnitas** ($x, y, z$). Resolver el **sistema** significa encontrar los valores numéricos únicos que hacen que las tres **ecuaciones** sean verdaderas al mismo tiempo. Es como encontrar la combinación exacta de una caja fuerte de tres diales.

> [!warning] ⚠️ Error común
> **❌ Incorrecto:** Empezar a resolver sin organizar los términos de las **ecuaciones**.
> **✅ Correcto:** Asegúrate de que las **ecuaciones** sigan el orden $x, y, z = \text{término independiente}$. En la **regla de Cramer**, este orden es **obligatorio** para no arruinar el cálculo de los **determinantes**; en el **método de reducción**, es una práctica recomendada para evitar confusiones.

> [!tip] 💡 Truco para recordarlo
> Para que el **procedimiento** sea más sencillo, elige siempre para eliminar la **variable** que tenga un **coeficiente** $1$ o $-1$ (es decir, la letra que aparece "sola"). ¡Esto te ahorrará muchos cálculos difíciles!

---

## 3. Procedimiento Paso a Paso (Reducción)

```text
PASO 1: Elegir una variable para eliminar. Combinar la ecuación (1) con la (2), 
        y luego la (1) con la (3) [o (2) con (3)] para eliminar la misma letra 
        dos veces. Así obtendrás un nuevo sistema de 2x2.
PASO 2: Resolver el sistema de 2x2 resultante mediante el método de 
        reducción para hallar los valores de las dos primeras variables.
PASO 3: Sustituir los dos valores hallados en cualquier ecuación original 
        para encontrar el valor de la tercera variable (incógnita).
PASO 4: VERIFICACIÓN (Crucial): Sustituir los tres valores ($x, y, z$) en las 
        ecuaciones iniciales para confirmar que la igualdad se cumple.
```

---

## 4. Ejemplos Prácticos

```ad-example
title: Ejemplo 1: Método de Reducción Básico
**Sistema:**
(1) $x + 2y + z = 7$
(2) $3x + y + z = 5$
(3) $2x + 3y - z = 3$

**Procedimiento:**
Al combinar la (1) con la (3), la $z$ se elimina directamente ($+z - z = 0$). Luego, al combinar la (2) con la (3), eliminamos nuevamente la $z$. Al resolver el **sistema de 2x2** resultante, hallamos los valores.
**Resultado:** $(0, 2, 3)$. Es decir: $x = 0$, $y = 2$, $z = 3$.
```

```ad-example
title: Ejemplo 2: Reducción con Multiplicación de Signos
**Sistema:**
(1) $5x - 2y + z = 24$
(2) $2x + 5y - 2z = -14$
(3) $x - 4y + 3z = 26$

**Procedimiento:**
Para eliminar $z$, multiplicamos la **ecuación** (1) por $2$ antes de combinarla con la (2). Luego, multiplicamos la (1) por $-3$ antes de combinarla con la (3) para igualar los **coeficientes** con signos opuestos.
**Resultado:** $(3, -2, 5)$. Es decir: $x = 3$, $y = -2$, $z = 5$.
```

```ad-example
title: Ejemplo 3: Caso Avanzado - Variables Faltantes
**Sistema:**
(1) $3x + 2y = -4$
(2) $2x + 2y + 3z = 4$
(3) $3x - 2y - z = -10$

**Análisis pedagógico:**
A la **ecuación** (1) le falta la **variable** $z$. ¡Esto es una ventaja! No la toques todavía. Combina la (2) y la (3) (multiplicando la (3) por $3$) para eliminar la $z$. La nueva **ecuación** resultante tendrá solo $x$ e $y$, formando un **sistema de 2x2** perfecto con la **ecuación** (1).
**Resultado:** $(-2, 1, 2)$. Es decir: $x = -2$, $y = 1$, $z = 2$.
```

```ad-example
title: Ejemplo 4: Regla de Cramer (Determinantes) con $USD
**Contexto:** Tres productos con precios $x, y, z$. Usamos el **sistema** del Ejemplo 1.
1. Se construye la **matriz** y se halla el **determinante del sistema** ($\Delta$) repitiendo las dos primeras filas (**método de Sarrus**).
2. Se calculan los **determinantes** de cada **incógnita** ($\Delta_x, \Delta_y, \Delta_z$) sustituyendo la columna correspondiente por los **términos independientes**.
**Valores obtenidos:**
- $\Delta = 13$
- $\Delta_x = 0$
- $\Delta_y = 26$
- $\Delta_z = 39$
**Cálculo final:** $x = \frac{0}{13} = 0$; $y = \frac{26}{13} = 2$; $z = \frac{39}{13} = 3$.
**Resultado:** $(0, 2, 3)$.
```

---

## 5. Ejercicios y Autoevaluación

```ad-abstract
title: 🟢 Nivel Fácil (Variable Directa)
1. $x + y + z = 6$; $x - y + z = 2$; $2x + y - z = 1$
2. $3x + 2y + z = 1$; $5x + 3y + z = 3$; $x + y - z = 1$
3. $x + 2y - z = -3$; $3x + y + z = 10$; $2x - y + z = 5$
4. $x + y + z = 4$; $2x - y + z = 2$; $x - y - z = -2$
```

```ad-abstract
title: 🟡 Nivel Medio (Requiere Multiplicación)
1. $2x + 3y + z = 1$; $3x - 2y - 4z = -3$; $5x - y - z = 4$
2. $x + 2y + 3z = 9$; $4x + 5y + 6z = 24$; $3x + y - 2z = 4$
3. $2x - y + z = 3$; $x + 2y - z = -3$; $x - 3y + 2z = 6$
4. $3x + 2y + z = 4$; $2x - y + 2z = -1$; $x + y - z = 1$
```

```ad-abstract
title: 🔴 Nivel Avanzado (Problemas $USD y Variables Faltantes)
1. $2x + y = 7$; $x + 2y + z = 12$; $y + 2z = 11$
2. 3 Lápices ($x$) + 2 Cuadernos ($y$) = $11. 2 Cuadernos ($y$) + 1 Borrador ($z$) = $9. 1 Lápiz + 1 Cuaderno + 1 Borrador = $6.
3. $x + z = 5$; $2x - y = 4$; $y + 3z = 11$
4. Un sistema con **determinantes**: $\Delta = 6, \Delta_x = 12, \Delta_y = 24, \Delta_z = 30$. Hallar $(x, y, z)$.
```

> [!success] ✅ Respuestas para el docente
> **Nivel Fácil:**
> 1. $(1, 2, 3)$ | 2. $(1, -1, 0)$ | 3. $(2, -1, 3)$ | 4. $(1, 1, 2)$
> **Nivel Medio:**
> 1. $(1, 0, -1)$ | 2. $(3, 0, 2)$ | 3. $(1, -2, -1)$ | 4. $(1, 0, 1)$
> **Nivel Avanzado:**
> 1. $(2, 3, 4)$ | 2. $(1, 4, 1)$ | 3. $(3, 2, 2)$ | 4. $(2, 4, 5)$
> *Nota: ¡No olvides animar a tus alumnos a realizar la **verificación** en cada ejercicio!*

### Mini-prueba
```ad-question
title: Pregunta 1
¿Por qué es obligatorio ordenar las **ecuaciones** antes de aplicar la **regla de Cramer**?
```
```ad-question
title: Pregunta 2
Si en el **método de reducción** la **ecuación** (1) no tiene la **variable** $y$, ¿qué paso debes seguir con las **ecuaciones** (2) y (3)?
```
```ad-question
title: Pregunta 3
Si en un cálculo de costos obtienes un **determinante del sistema** $\Delta = 13$ y un **determinante** $\Delta_x = 0$, ¿cuál es el precio final del producto $x$?
```

---

## 6. Cierre y Navegación Final

> [!tip] 💡 En la próxima clase
> Ahora que dominas los sistemas con solución única, exploraremos los **Casos Especiales**: ¿qué sucede cuando un **sistema** tiene soluciones infinitas o no tiene ninguna solución?

> [!info] 🧭 Navegación
> [[Clase 01 — Sistemas 2x2]] | **Clase 02 — Sistemas 3x3** | [[Clase 03 — Casos Especiales]]