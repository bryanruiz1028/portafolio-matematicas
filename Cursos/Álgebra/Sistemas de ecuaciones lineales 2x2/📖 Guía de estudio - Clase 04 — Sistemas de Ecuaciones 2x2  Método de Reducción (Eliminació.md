# 📖 Guía de estudio — Clase 04: Sistemas de Ecuaciones 2x2 (Método de Reducción)

¡Hola! Qué alegría saludarte. Hoy vamos a dominar juntos el **Método de Reducción** (también conocido como eliminación). No te preocupes si al principio parece un laberinto; es más fácil de lo que parece y, paso a paso, verás que es como resolver un rompecabezas donde las piezas encajan perfectamente. ¡Empecemos con entusiasmo!

> [!info] 📌 Conceptos clave
> Para que este método sea tu mejor aliado, recuerda siempre estos cuatro pilares fundamentales:
> 1. **Orden ante todo:** Las ecuaciones deben estar organizadas. Asegúrate de que las $x$, las $y$ y los números estén en la misma columna (formato: $Ax + By = C$).
> 2. **Búsqueda de Opuestos:** El objetivo es que una variable tenga el mismo número (coeficiente) pero con signo contrario (por ejemplo, $+5y$ y $-5y$).
> 3. **La Suma Mágica:** Al sumar las ecuaciones verticalmente, la variable con signos opuestos se eliminará, dejándote el camino libre para resolver una sola incógnita.
> 4. **El Regreso a Casa:** Una vez que encuentres el valor de una variable, sustitúyela en cualquiera de las ecuaciones originales para hallar la que falta.

---

### 📊 Tabla de Referencia Técnica

| Término | Definición / Fórmula |
| :--- | :--- |
| **Método de Reducción** | Proceso que consiste en sumar o restar las ecuaciones del sistema para "eliminar" una de las variables y simplificar el trabajo. |
| **Mínimo Común Múltiplo (MCM)** | Es el número clave que buscamos entre los **coeficientes** de una variable para lograr que ambos sean iguales y así poder eliminarlos fácilmente. |
| **Punto de Intersección** | Es la solución final $(x, y)$. Es el "punto de equilibrio perfecto" donde ambas ecuaciones se cumplen al mismo tiempo. |

---

### 📝 Ejemplos Resueltos

```ad-example
title: Ejemplo A — Caso con multiplicación simple
¡Excelente trabajo llegando hasta aquí! Vamos a ver cómo resolver un sistema básico paso a paso.
**Sistema:**
1) $2x + y = 8$
2) $x - 4y = -5$

**Paso 1: Preparación (Multiplicación)**
Queremos eliminar la $y$. En la ec. (2) tenemos $-4y$. Para que en la ec. (1) aparezca un $+4y$, multiplicaremos toda la primera ecuación por **4**:
*   $4 \cdot (2x + y = 8) \longrightarrow \mathbf{8x + 4y = 32}$

**Paso 2: Suma de ecuaciones**
Ahora sumamos la nueva ecuación con la segunda original. ¡Mira cómo desaparece la $y$!
  $8x + 4y = 32$
+ $x - 4y = -5$
--------------
  $9x + 0 = 27$

**Paso 3: Resolver la incógnita**
$9x = 27 \implies x = 27 / 9 \implies \mathbf{x = 3}$

**Paso 4: Sustitución**
Reemplazamos $x = 3$ en la primera ecuación original:
$2(3) + y = 8 \implies 6 + y = 8 \implies y = 8 - 6 \implies \mathbf{y = 2}$

**Resultado:** El punto de intersección es **(3, 2)**. ¡Lo lograste!
```

```ad-example
title: Ejemplo B — Aplicación en compras (USD)
Imagina que estás en la papelería. Vamos a usar el MCM para encontrar precios reales.
**Problema:** El costo de 6 cuadernos ($x$) menos el valor de 5 lápices ($y$) da un balance de **-9 USD**. Por otro lado, 4 cuadernos y 3 lápices cuestan **13 USD**.
1) $6x - 5y = -9$
2) $4x + 3y = 13$

**Paso 1: Encontrar el MCM de los coeficientes**
Eliminaremos la $x$. El MCM de 6 y 4 es **12**. 
*   Multiplicamos la ec. (1) por **2** para obtener $12x$.
*   Multiplicamos la ec. (2) por **-3** para obtener $-12x$. (💡 *Recuerda: ¡Necesitamos signos diferentes!*)

**Paso 2: Multiplicación y Suma**
1) $2 \cdot (6x - 5y = -9) \longrightarrow 12x - 10y = -18$
2) $-3 \cdot (4x + 3y = 13) \longrightarrow -12x - 9y = -39$

Sumamos verticalmente:
  $12x - 10y = -18$
+ $-12x - 9y = -39$
------------------
  $0 - 19y = -57$

**Paso 3: Resolver**
$-19y = -57$ (Aplicamos cambio de signo: $19y = 57$)
$y = 57 / 19 \implies \mathbf{y = 3}$ USD (Precio de cada lápiz).

**Paso 4: Sustitución**
Usamos la ec. (2): $4x + 3(3) = 13 \implies 4x + 9 = 13 \implies 4x = 4 \implies \mathbf{x = 1}$ USD.

**Resultado:** Cada cuaderno cuesta **1 USD** y cada lápiz **3 USD**.
```

---

### ✍️ Sistema de Práctica Gradual

```ad-abstract
title: 🟢 Fácil
Resuelve eliminando la variable $y$:
1) $2x - 6y = 4$
2) $3x + 2y = 17$
*💡 Ayuda: Multiplica la segunda ecuación por 3 para que las "y" se cancelen.*
```

```ad-abstract
title: 🟡 Medio
Encuentra el MCM para eliminar la variable que prefieras:
1) $4x + 2y = -4$
2) $3x - 3y = 21$
*💡 Pista: Si buscas eliminar la "y", el MCM es 6.*
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
**Reto de Inventario:** Un comerciante de artículos escolares está revisando sus registros de costos, pero sus notas están un poco desordenadas. Ayúdale a encontrar los valores unitarios de los productos $x$ e $y$ resolviendo el siguiente sistema:

*   "El costo de 11 unidades de $x$ y 9 unidades de $y$, restándoles 2 USD de descuento, nos deja un balance de 0": **$11x + 9y - 2 = 0$**
*   "Por otro lado, el valor de 13 unidades de $x$ es igual al valor de 15 unidades de $y$ menos 2 USD": **$13x = 15y - 2$**

**Tu misión:** Ordena ambas ecuaciones al formato ($X, Y = \text{número}$) y aplica el método de reducción. ¡Tú puedes con este reto!
```

---

> [!tip] 💡 Consejo de estudio
> **La técnica del -1:** Si al sumar las ecuaciones te encuentras con algo como $-19y = -57$, ¡no te compliques con los signos al dividir! Simplemente multiplica toda la fila por $-1$ para cambiar los signos de ambos lados: $19y = 57$. Esto hace que la operación sea más limpia y evita esos pequeños errores que a veces nos quitan puntos.

¡Felicidades por completar esta guía! La práctica constante es el secreto para convertirte en un maestro del álgebra. Sigue practicando y verás cómo estos sistemas se vuelven automáticos para ti. ¡A por ello!