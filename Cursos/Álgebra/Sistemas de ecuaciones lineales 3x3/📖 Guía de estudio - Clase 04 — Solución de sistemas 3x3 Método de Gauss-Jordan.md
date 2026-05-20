# 📖 Guía de estudio — Clase 04: Solución de sistemas 3x3 mediante el método de Gauss-Jordan

> [!info] 📌 Conceptos clave
> - **Gauss vs. Gauss-Jordan:** Mientras que el método de Gauss busca crear ceros solo debajo de la diagonal (forma triangular), el método de **Gauss-Jordan** va más allá y transforma la matriz de coeficientes en una **matriz identidad**.
> - **Orden de las variables:** Antes de escribir la matriz, es fundamental que todas las ecuaciones estén organizadas en el mismo orden: primero los términos con $x$, luego $y$, después $z$, y al otro lado del igual el término independiente.
> - **Objetivo:** Convertir la matriz original en una diagonal de unos ($1$) rodeada de ceros ($0$). Esto nos permite leer la respuesta directamente.
> - **Operaciones permitidas:** Podemos sumar, restar, multiplicar o dividir filas completas para alcanzar nuestro objetivo.

## 2. Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Matriz Identidad** | Es aquella donde la diagonal principal está formada por $1s$ y todos los demás elementos son $0s$. |
| **Término Independiente** | Es el número que no tiene letra y se encuentra al lado derecho de la igualdad. |
| **Mínimo Común Múltiplo (MCM)** | Herramienta necesaria para eliminar denominadores. Multiplicamos toda la ecuación por el MCM para trabajar con números enteros. |
| **Operación de Fila** | Procedimiento matemático entre filas, por ejemplo: $F_2 - F_1$ o $F_3 / 2$. |

## 3. Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A (Caso básico paso a paso)
**Sistema de ecuaciones:**
1) $x - y + 3z = 13$
2) $x + y + z = 11$
3) $2x + 2y - z = 7$

**Paso 1: Conversión a matriz aumentada**
$\begin{pmatrix} 1 & -1 & 3 & | & 13 \\ 1 & 1 & 1 & | & 11 \\ 2 & 2 & -1 & | & 7 \end{pmatrix}$

**Paso 2: Crear ceros en la primera columna (usando la fila 1)**
- Para $F_2$: Hacemos $F_2 - F_1$. Resultado: $(0, 2, -2, -2)$.
- Para $F_3$: Hacemos $F_3 - 2F_1$. Resultado: $(0, 4, -7, -19)$.
Nueva matriz: $\begin{pmatrix} 1 & -1 & 3 & | & 13 \\ 0 & 2 & -2 & | & -2 \\ 0 & 4 & -7 & | & -19 \end{pmatrix}$

**Paso 3: Crear ceros en la segunda columna (usando la fila 2)**
Para eliminar el $4$ de la $F_3$, usamos la diagonal principal de la segunda fila ($2$):
- Operación: $F_3 - 2F_2$.
- Cálculo: $(0, 4, -7, -19) - 2(0, 2, -2, -2) = (0, 0, -3, -15)$.

**Paso 4: Finalizar la identidad**
Siguiendo con la eliminación de los valores superiores y dividiendo cada fila para obtener los $1s$ en la diagonal, llegamos a:
**Resultado final:** $x = 2, y = 4, z = 5$.
```

```ad-example
title: Ejemplo B (Aplicación real: Compras escolares)
**Contexto:** Un estudiante compra libretas ($x$), esferos ($y$) y borradores ($z$). El sistema describe los costos totales de diferentes combinaciones de estos útiles:

**Sistema:**
1) $2x + 3y + 4z = 3$
2) $2x + 6y + 8z = 5$
3) $4x + 9y - 4z = 4$

**Procedimiento:**
Se aplica Gauss-Jordan transformando la matriz hasta que cada variable quede despejada. Por ejemplo, tras los primeros pasos, se nota que $y$ y $z$ tienen valores fraccionarios que representan centavos.

**Resultado en moneda (USD):**
- Precio de cada **libreta** ($x$): \$0.50
- Precio de cada **esfero** ($y$): \$0.33
- Precio de cada **borrador** ($z$): \$0.25
```

## 4. Ejercicios de Repaso

```ad-abstract
title: 🟢 Fácil
Resuelve el siguiente sistema utilizando el método de Gauss-Jordan. Tu meta inicial es obtener ceros en la primera columna usando la fila 1 como guía:
$x + y + z = -6$
$2x + y - z = -1$
$x - 2y + 3z = -6$
```

```ad-abstract
title: 🟡 Medio
¡Cuidado! Este sistema está desordenado. Primero organiza las letras ($x, y, z$) y los términos independientes antes de construir tu matriz:
$z + y + x = -6$
$-2x + y - z = -1$
$3z + x - 2y = -6$
```

```ad-abstract
title: 🔴 Avanzado (Aplicación con fracciones)
Usa el método del **Mínimo Común Múltiplo (MCM)** para convertir estas ecuaciones a números enteros. Luego, aplica Gauss-Jordan para resolver el sistema:
1) $\frac{x}{3} + \frac{y}{4} + \frac{z}{3} = 21$ 
2) $\frac{x}{5} + \frac{y}{6} - \frac{z}{3} = 0$ 
3) $\frac{x}{10} - \frac{y}{3} + \frac{z}{6} = -1$
```

## 5. Consejo de Estudio

> [!tip] 💡 Técnica de simplificación
> Si en cualquier paso del proceso notas que todos los números de una fila (incluyendo el resultado tras la línea) son múltiplos de un mismo número, **divídela inmediatamente**. Por ejemplo, si una fila es $(0, 2, -2, -2)$, puedes dividirla toda por $2$ para obtener $(0, 1, -1, -1)$. ¡Esto hará que tus cálculos sean mucho más rápidos y evitará errores con números grandes!