# 📖 Guía de estudio — Clase 03: Sistemas de Ecuaciones Lineales 2x2 (Método de Determinantes)

> [!info] 📌 Conceptos clave
> El método de determinantes, también conocido como **Regla de Cramer**, es un procedimiento matemático sistemático y sumamente sencillo para resolver sistemas de ecuaciones. Sus fundamentos son:
> 1. **Importancia del Orden:** Antes de operar, el sistema debe estar organizado en la forma $ax + by = c$ (incógnitas $x$ e $y$ a la izquierda, término independiente a la derecha).
> 2. **Determinante del Sistema ($\Delta$):** Es un valor numérico obtenido de los coeficientes de las incógnitas. Según el autor o el libro, también lo verás representado como $D$ o $det$.
> 3. **Proceso de "Cambio":** Para hallar los determinantes específicos ($\Delta_x$ y $\Delta_y$), se sustituye la columna de la incógnita deseada por la de los términos independientes.
> 4. **Operación Final:** El valor de cada incógnita se encuentra dividiendo su determinante específico entre el determinante del sistema ($\Delta$).

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Sistema Ordenado** | Estructura necesaria donde las variables están alineadas: $ax + by = c$. |
| **Determinante ($\Delta$ o $D$)** | Valor resultante de la resta de productos de las diagonales: $(a \cdot d) - (b \cdot c)$. |
| **Regla de Cramer** | Fórmulas finales para las soluciones: $x = \frac{\Delta_x}{\Delta}$ e $y = \frac{\Delta_y}{\Delta}$. |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Caso básico (Números enteros)
**Enunciado:** Resolver el sistema:
$7x + 4y = 13$
$5x - 2y = 19$

**Paso 1: Cálculo del determinante del sistema ($\Delta$)**
Usamos los coeficientes de $x$ (7 y 5) y de $y$ (4 y -2):
$\Delta = (7 \cdot -2) - (4 \cdot 5) = -14 - 20 = -34$

**Paso 2: Cálculo de $\Delta_x$ (Cambiamos $x$ por independientes)**
$\Delta_x = (13 \cdot -2) - (4 \cdot 19) = -26 - 76 = -102$

**Paso 3: Cálculo de $\Delta_y$ (Cambiamos $y$ por independientes)**
$\Delta_y = (7 \cdot 19) - (13 \cdot 5) = 133 - 65 = 68$

**Paso 4: División final**
$x = \frac{-102}{-34} = 3$
$y = \frac{68}{-34} = -2$
✅ **Resultado:** $x = 3, y = -2$
```

```ad-example
title: Ejemplo B — Aplicación real $USD (Contexto cotidiano)
**Enunciado:** El costo de 3 libretas ($x$) menos el descuento de 1 lápiz ($y$) es 1 USD; mientras que 2 libretas más 3 lápices cuestan 8 USD.
$3x - 1y = 1$
$2x + 3y = 8$

**Desarrollo:**
1. **Cálculo de $\Delta$:** $(3 \cdot 3) - (-1 \cdot 2) = 9 - (-2) = 9 + 2 = 11$.
2. **Cálculo de $\Delta_x$:** $(1 \cdot 3) - (-1 \cdot 8) = 3 - (-8) = 3 + 8 = 11$.
3. **Cálculo de $\Delta_y$:** $(3 \cdot 8) - (1 \cdot 2) = 24 - 2 = 22$.

**Valores finales:**
$x = \frac{11}{11} = 1$ USD
$y = \frac{22}{11} = 2$ USD
✅ **Resultado:** Cada libreta cuesta **1 USD** y cada lápiz **2 USD**.
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
1. Para el siguiente sistema extraído de la práctica:
   $2x + 8y = -2$
   $x - 2y = 5$
   Identifica los coeficientes y verifica si el sistema ya se encuentra **ordenado**.
2. Calcula únicamente el **determinante del sistema ($\Delta$)** para las ecuaciones del Ejemplo A.
```

```ad-abstract
title: 🟡 Medio
**Planteamiento:** Utiliza el sistema de práctica de la fuente:
$2x + 8y = -2$
$x - 2y = 5$

**Tarea:** Halla el valor de la incógnita $y$. 
*¡Mucho ojo!* Al calcular $\Delta_y$, asegúrate de manejar la resta correctamente: $10 - (-2) = 10 + 2 = 12$. No olvides que el signo menos de la fórmula es independiente del signo del número.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
**Planteamiento:** Resuelve el siguiente sistema con resultados fraccionarios:
$4x + 5y = 5$
$-4x - 10y = -7$

**Tarea:** 
1. Calcula $\Delta$, $\Delta_x$ y $\Delta_y$.
2. Expresa los resultados como fracciones simplificadas ($3/4$ y $2/5$).
3. Convierte las fracciones a centavos de dólar ($0.75$ USD y $0.40$ USD).
✅ **Meta:** Demuestra que dominas los signos y la simplificación.
```

> [!tip] 💡 Consejo de estudio
> Tal como advierte el **profe Alex**: "Siempre a ese resultado le tenemos que restar el otro". Para evitar errores, cuando el segundo producto sea negativo, escribe siempre el menos de la fórmula y luego el número entre paréntesis. Por ejemplo: $9 - (-2)$ se convierte en $9 + 2 = 11$. ¡Este pequeño detalle salvará tu examen!