# 📖 Guía de estudio — Clase 05: Sistemas de Ecuaciones Lineales 2x2

> [!info] 📌 Conceptos clave
> - **Ordenamiento del sistema:** Para que los métodos funcionen, las ecuaciones deben estar organizadas en la forma $ax + by = c$. Las incógnitas ($x, y$) van a la izquierda y el término independiente (el número solo) a la derecha.
> - **Eliminación de fracciones:** Si ves fracciones, no te asustes. Usamos el Mínimo Común Múltiplo (MCM) de los denominadores para multiplicar **toda la ecuación** y convertirla en una con números enteros.
> - **Método de Cramer (Determinantes):** Es un camino directo que usa "multiplicaciones cruzadas". Se calcula restando el producto de la diagonal secundaria al producto de la diagonal principal.
> - **Verificación obligatoria:** Una solución solo es válida si, al sustituir los valores hallados, se cumple la igualdad en **ambas** ecuaciones originales. Si solo cumple una, el ejercicio está mal resuelto.

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Mínimo Común Múltiplo (en sistemas)** | Es el número clave por el cual se multiplica **cada uno de los términos** de una ecuación para eliminar los denominadores y trabajar solo con enteros. |
| **Determinante del Sistema ($\Delta$)** | Se obtiene con los coeficientes de $x$ y $y$. Se calcula: (Diagonal Principal) - (Diagonal Secundaria). |
| **Método de Igualación** | Consiste en despejar la misma incógnita en las dos ecuaciones para luego igualar ambas expresiones y encontrar el valor de una variable. |
| **Verificación** | Proceso de sustituir los valores $(x, y)$ en el sistema inicial para comprobar que los dos lados de la igualdad den el mismo resultado. |

## Ejemplos Resueltos Adicionales

````ad-example title: Ejemplo A — Eliminación de fracciones en sistemas 2x2 
Imagina que tienes este sistema que parece complicado por las fracciones:
1) $\frac{1}{2}x - y = -5$
2) $x + \frac{1}{3}y = -3$

**Paso 1: Hallar el MCM de cada ecuación.**
Siguiendo la lógica del Profe Alex, cuando hay un solo denominador, ese número **es** nuestro multiplicador clave:
- En la ec. 1, el MCM es **2**.
- En la ec. 2, el MCM es **3**.

**Paso 2: Multiplicar toda la ecuación por su MCM.**
Debemos multiplicar cada término para no alterar la igualdad:
- Ec. 1: $2 \cdot (\frac{1}{2}x) - 2 \cdot (y) = 2 \cdot (-5) \rightarrow$ El 2 de arriba se cancela con el 2 de abajo.
- Ec. 2: $3 \cdot (x) + 3 \cdot (\frac{1}{3}y) = 3 \cdot (-3) \rightarrow$ El 3 de arriba se cancela con el 3 de abajo.

**Paso 3: Sistema resultante sin fracciones.**
Ahora tenemos un sistema mucho más amigable:
- $x - 2y = -10$
- $3x + y = -9$
````

````ad-example title: Ejemplo B — Aplicación de Cramer en compras ($USD)
**Problema:** En una papelería escolar, el precio de un cuaderno ($x$) y un bolígrafo ($y$) en dólares se rige por:
1) $15x + 11y = 32$
2) $-9x + 7y = 8$

**Paso 1: Calcular el determinante del sistema ($\Delta$):**
Multiplicamos cruzado los coeficientes de las letras:
$\Delta = (15 \cdot 7) - (11 \cdot -9)$
$\Delta = 105 - (-99)$  <-- *Paso clave: menos por menos es más*
$\Delta = 105 + 99 = \mathbf{204}$

**Paso 2: Calcular el determinante de $x$ ($\Delta_x$):**
Cambiamos la columna de $x$ por los resultados (32 y 8):
$\Delta_x = (32 \cdot 7) - (11 \cdot 8)$
$\Delta_x = 224 - 88 = \mathbf{136}$

**Paso 3: Calcular el determinante de $y$ ($\Delta_y$):**
Cambiamos la columna de $y$ por los resultados (32 y 8):
$\Delta_y = (15 \cdot 8) - (32 \cdot -9)$
$\Delta_y = 120 - (-288)$ <-- *Observa bien la ley de signos aquí*
$\Delta_y = 120 + 288 = \mathbf{408}$

**Resultados finales:**
$x = \frac{\Delta_x}{\Delta} = \frac{136}{204} = \mathbf{\frac{2}{3}}$ (precio del cuaderno)
$y = \frac{\Delta_y}{\Delta} = \frac{408}{204} = \mathbf{2}$ (precio del bolígrafo)
````

## Ejercicios de Repaso

````ad-abstract title: 🟢 Fácil 
Comprueba si los valores propuestos son la solución real de cada sistema (Verificación):
1. $x + 6y = 27$ ; $7x - 3y = 9$. ¿Es $(3, 4)$ la solución?
2. $3x - 4y + 23 = 0$ ; $6y + 11x = 19$. ¿Es $(-1, 5)$ la solución?
3. $x + y = 6$ ; $x - 4y = -5$. ¿Es $(2, 4)$ la solución?
````

````ad-abstract title: 🟡 Medio 
Transforma estos sistemas "difíciles" en sistemas enteros utilizando el método del MCM explicado por el Profe Alex:
1. $\frac{2}{3}x - \frac{3}{4}y = \frac{1}{6}$
   $\frac{y}{8} - \frac{5x}{6} = 12$

2. $\frac{x}{6} + \frac{3y}{4} = 2$
   $\frac{2x}{5} + 3y = \frac{3}{10}$
````

````ad-abstract title: 🔴 Avanzado — Aplicación con $USD 
Un administrador de una tienda de tecnología tiene sus registros de costos desordenados. Los precios en dólares ($) de dos componentes ($x$ e $y$) están representados así:
1. $10x + 18y + 11 = 0$
2. $16x - 5 = 9y$

**Instrucción:** Primero, ordena el sistema a la forma $ax + by = c$. Luego, utiliza el método de Cramer para hallar el costo exacto de cada componente.
````

> [!tip] 💡 Consejo de estudio
> Si decides usar el método de igualación, busca siempre despejar la incógnita que tenga **coeficientes positivos** en ambas ecuaciones; esto te ahorrará muchos errores con los signos. Lo más importante: cuando uses el MCM para quitar fracciones, asegúrate de **multiplicar absolutamente todos los términos**, incluyendo el número que está después del igual (el término independiente). ¡No lo olvides!