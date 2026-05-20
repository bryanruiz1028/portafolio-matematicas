# 📖 Guía de estudio — Clase 02: Métodos de Solución para Sistemas de Ecuaciones 3x3

[!info] **📌 Conceptos clave**
¡Hola, jóvenes matemáticos! Antes de sumergirnos en los cálculos, repasemos los pilares de esta sesión:
*   **Orden obligatorio:** En el método de determinantes, el caos es tu enemigo. Las ecuaciones deben estar estrictamente organizadas: primero los términos con $x$, luego $y$, después $z$ y, tras el igual, el término independiente.
*   **Lógica de Cramer:** Este método utiliza "Determinantes" ($\Delta$). Imagina que cada incógnita es una proporción del sistema general, donde sustituimos su columna específica por los resultados del sistema.
*   **Esencia de la Reducción (Eliminación):** Aquí jugamos a "simplificar para vencer". Combinamos parejas de ecuaciones para eliminar una variable dos veces, transformando un complejo sistema de 3x3 en uno de 2x2.
*   **Verificación final:** ¡No te confíes! Un error de signo puede arruinarlo todo. Siempre sustituye tus resultados ($x, y, z$) en las ecuaciones originales para confirmar que la igualdad se cumpla.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Sistema de 3x3** | Un conjunto de tres ecuaciones lineales con tres incógnitas que deben satisfacerse simultáneamente. |
| **Determinante del Sistema ($\Delta$)** | Un número único calculado usando solo los coeficientes numéricos de las variables $x, y$ y $z$. |
| **Método de Sarrus** | Técnica para resolver determinantes de 3x3 repitiendo las dos primeras filas (o columnas) y restando el producto de las diagonales secundarias al de las principales. |
| **Cálculo de Incógnitas** | Las fórmulas maestras de Cramer: <br> $x = \frac{\Delta x}{\Delta}$, $y = \frac{\Delta y}{\Delta}$, $z = \frac{\Delta z}{\Delta}$ |

## Ejemplos resueltos adicionales

```ad-example
title: **Ejemplo A: Método de Cramer (Sarrus) paso a paso**
**Sistema a resolver:**
1) $x + 2y + z = 7$
2) $3x + y + z = 5$
3) $2x + 3y - z = 3$

**Paso 1: Hallar $\Delta$ (Determinante del Sistema)**
Colocamos los coeficientes y repetimos las dos primeras filas. ¡Ojo con los signos negativos!
$\Delta = \begin{vmatrix} 1 & 2 & 1 \\ 3 & 1 & 1 \\ 2 & 3 & -1 \\ 1 & 2 & 1 \\ 3 & 1 & 1 \end{vmatrix} \implies \text{Diagonales Principales: } (1\cdot1\cdot-1) + (3\cdot3\cdot1) + (2\cdot2\cdot1) = -1 + 9 + 4 = 12$
$\text{Diagonales Secundarias: } (1\cdot1\cdot2) + (1\cdot3\cdot1) + (-1\cdot2\cdot3) = 2 + 3 - 6 = -1$
**Cálculo:** $\Delta = 12 - (-1) = 13$.

**Paso 2: Hallar $\Delta x$ (Sustitución de columna)**
Cambiamos la columna de $x$ por los términos independientes **(7, 5, 3)**:
$\Delta x = \begin{vmatrix} \mathbf{7} & 2 & 1 \\ \mathbf{5} & 1 & 1 \\ \mathbf{3} & 3 & -1 \\ \mathbf{7} & 2 & 1 \\ \mathbf{5} & 1 & 1 \end{vmatrix} \implies \begin{matrix} \text{P: } (7\cdot1\cdot-1) + (5\cdot3\cdot1) + (3\cdot2\cdot1) = -7 + 15 + 6 = 14 \\ \text{S: } (1\cdot1\cdot3) + (1\cdot3\cdot7) + (-1\cdot2\cdot5) = 3 + 21 - 10 = 14 \end{matrix}$
**Cálculo:** $\Delta x = 14 - 14 = 0$.

**Paso 3: Resultados finales**
Siguiendo el mismo proceso para $\Delta y$ (26) y $\Delta z$ (39):
$x = \frac{0}{13} = 0$; $y = \frac{26}{13} = 2$; $z = \frac{39}{13} = 3$. **Resultado: (0, 2, 3)**.
```

```ad-example
title: **Ejemplo B: Método de Reducción (Contexto de Compra)**
**Situación:** En el mercado compramos frutas. El costo total se expresa en estas ecuaciones:
1) $x + 2y + z = 7$ (1 manzana, 2 peras, 1 banano)
2) $3x + y + z = 5$ (3 manzanas, 1 pera, 1 banano)
3) $2x + 3y - z = 3$ (2 manzanas, 3 peras y devolvemos 1 banano por crédito)

**Paso 1: Eliminar $z$ para crear un sistema 2x2**
*   **Pareja 1 (Ecs. 1 y 3):** Como tenemos $+z$ y $-z$, sumamos directo:
    $(x + 2y + z) + (2x + 3y - z) = 7 + 3 \implies \mathbf{3x + 5y = 10}$ (Ecuación 4)
*   **Pareja 2 (Ecs. 2 y 3):** Nuevamente sumamos para eliminar $z$:
    $(3x + y + z) + (2x + 3y - z) = 5 + 3 \implies \mathbf{5x + 4y = 8}$ (Ecuación 5)

**Paso 2: Resolver el sistema 2x2 resultante**
Tenemos:
4) $3x + 5y = 10$
5) $5x + 4y = 8$
Multiplicamos la (4) por $4$ y la (5) por $-5$ para eliminar $y$:
$12x + 20y = 40$
$-25x - 20y = -40$
Suma: $-13x = 0 \implies \mathbf{x = 0}$ (La manzana es gratis hoy).

**Paso 3: Sustituir para hallar el resto**
En Ec. 4: $3(0) + 5y = 10 \implies 5y = 10 \implies \mathbf{y = 2}$ (Pera: $2 USD).
En Ec. 1: $0 + 2(2) + z = 7 \implies 4 + z = 7 \implies \mathbf{z = 3}$ (Banano: $3 USD).
```

## Ejercicios de repaso

```ad-abstract
title: **Nivel Fácil (🟢)**
Resuelve por reducción. ¡Aprovecha que a la primera ecuación ya le falta una variable!
1) $3x + 2y = -4$
2) $2x + 2y + 3z = 4$
3) $3x - 2y - z = -10$
*(Pista: Elimina la $z$ entre la 2 y la 3 para obtener otra ecuación con $x$ e $y$).*
```

```ad-abstract
title: **Nivel Medio (🟡)**
Calcula los valores de las incógnitas usando el **Método de Cramer**:
1) $x + y + z = 11$
2) $x - y + 3z = 13$
3) $2x + 2y - z = 7$
*(Dato del Profe: El determinante del sistema $\Delta$ es 6).*
```

```ad-abstract
title: **Nivel Avanzado (🔴)**
Un proveedor de tecnología vende componentes ($x, y, z$). Determina el precio de cada uno en **USD** resolviendo este sistema extraído de la práctica del Profe Alex:
1) $4x + 2y + 3z = 8$
2) $3x + 4y + 2z = -1$
3) $2x - y + 5z = 3$
**Reto:** Los resultados deben ser $x = 5, y = -3, z = -2$. ¡Cuidado extremo con los signos al multiplicar las diagonales!
```

[!tip] **💡 Consejo del Profe Alex**
¿Quieres saber si vas por buen camino en medio de un examen? Observa la **divisibilidad**. En los ejercicios escolares, los determinantes de las incógnitas ($\Delta x, \Delta y, \Delta z$) suelen ser múltiplos exactos del determinante del sistema ($\Delta$). Si al dividir no obtienes un número entero o una fracción muy simple, detente y revisa tus sumas en las diagonales de Sarrus. ¡El 90% de los errores son signos!