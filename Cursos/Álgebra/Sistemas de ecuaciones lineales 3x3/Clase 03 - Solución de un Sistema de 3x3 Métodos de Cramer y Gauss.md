# Clase 03 — Solución de un Sistema de 3x3: Métodos de Cramer y Gauss

#algebra #solucindeunsist

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 4

> [!info] 🧭 Navegación
> - **Anterior:** [[Clase 02 — Sistemas de 2x2: Sustitución, Igualación y Reducción]]
> - **Siguiente:** [[Clase 04 — Aplicaciones Avanzadas y Método de Gauss-Jordan]]

---

## Relevancia y aplicaciones: ¿Por qué resolver 3 incógnitas?

¡Hola, futuro experto en álgebra! Resolver un sistema de 3x3 es como ser un detective matemático. Imagina que tienes **3 pistas** (ecuaciones) para encontrar **3 tesoros escondidos** ($x, y, z$). Si solo tuvieras dos pistas, no podrías asegurar el valor del tercer tesoro; por eso, para tres letras, ¡necesitamos tres ecuaciones!

Esta herramienta no solo vive en los libros, es fundamental para:
* 💵 **$USD:** Calcular el precio de tres divisas distintas o el costo de tres servicios bancarios cuando se contratan en paquetes conjuntos.
* 🏗️ **Práctica en Construcción:** Determinar las cantidades exactas de cemento, arena y cal necesarias para que una mezcla sea perfecta. ¡Un error aquí y la pared se cae!
* 📊 **Vida Cotidiana:** Repartir un presupuesto fijo en una tienda para comprar tres tipos de artículos diferentes sin que sobre ni falte un solo centavo.

---

## Concepto clave y trucos didácticos

Un sistema de **3x3** es simplemente un equipo de 3 ecuaciones que trabajan juntas. Para ganarle al sistema, debemos ser ordenados.

> [!warning] ⚠️ Error común
> El enemigo número uno es el **desorden**. Nunca empieces a calcular sin antes verificar que todas las ecuaciones estén alineadas como soldados: $x + y + z = \text{Término Independiente}$. Además, ¡mucho ojo con los signos! Un solo "más" que debió ser "menos" y el resultado se perderá.

> [!tip] 💡 Truco para recordarlo
> - **Regla de Sarrus (Cramer):** Es la "Regla de las Diagonales". Repite las dos primeras filas abajo para que ninguna diagonal se quede sin pareja.
> - **Método de Gauss:** Es la "Escalera de Ceros". Usamos la primera fila como nuestro "pivote" o base de ataque para eliminar las $x$ de las filas de abajo, repitiendo el proceso hasta que quede un escalón limpio.

---

## Procedimiento paso a paso

```text
PASO 1 → Ordenar las ecuaciones (X, Y, Z = Resultado).
PASO 2 → Elegir arma: Determinantes (Cramer) o Escalera (Gauss).
PASO 3 → Ejecutar: 
         - Cramer: Calcular Deltas (Δ, Δx, Δy, Δz).
         - Gauss: Operar filas (F2 - n*F1) para crear ceros.
PASO 4 → Hallar valores: Dividir deltas o despejar la escalera.
PASO 5 → Verificar: Reemplazar en la ecuación original.
```

---

## Ejemplos prácticos

> [!example] Ejemplo 1: El Método de Cramer (Determinantes)
> Resolvamos el sistema del Video 1:
> 1) $x + 4y + 5z = 11$
> 2) $3x - 2y + z = 5$
> 3) $4x + y - 3z = -26$
> 
> **¡Manos a la obra!** Así calculamos los determinantes:
> * **Determinante del Sistema ($\Delta$):** Usando los coeficientes, obtenemos **112**.
> * **Determinante de $x$ ($\Delta x$):** Cambiamos la columna de $x$ por los resultados ($11, 5, -26$). Obtenemos **-224**.
> * **Valor de $x$:** $x = \Delta x / \Delta = -224 / 112 = -2$.
> * *Resultado:* **$x = -2$**. ¡Fácil y rápido!

> [!example] Ejemplo 2: El arte de los signos en Gauss
> Veamos este sistema del Video 2:
> 1) $x + 2y + z = 7$
> 2) $3x + y + z = 5$
> 3) $2x + 3y - z = 3$
> 
> Aquí usamos la Fila 1 para "atacar" a las demás. Al transformar la Fila 2 ($F_2 - 3F_1$), el término independiente se calcula así: **$5 - 3(7) = -16$**. ¡No te rindas con los signos negativos!
> *Resultado final:* **$x = 0, y = 2, z = 3$**.

> [!example] Ejemplo 3: Gauss Avanzado (Estrategia de Intercambio)
> En este sistema:
> 1) $5x - 2y + z = 24$
> 2) $2x + 5y - 2z = -14$
> 3) $x - 4y + 3z = 26$
> 
> **Truco de experto:** Como la Fila 3 empieza con un "1", ¡vamos a intercambiarla con la Fila 1! Al tener un "1" arriba a la izquierda, las multiplicaciones para hacer ceros abajo son pan comido.
> *Resultado final:* **$x = 3, y = -2, z = 5$**.

> [!example] Ejemplo 4: Aplicación en Inversión ($USD)
> Una casa de cambio opera con tres monedas ($x, y, z$). Las condiciones de compra son:
> $x + y - z = 1$
> $2x + 3y + z = -2$
> $5x - y + 2z = 4$
> 
> Aplicando Cramer:
> * $\Delta = 25$
> * $\Delta x = 25 \rightarrow x = 1$
> * $\Delta y = -25 \rightarrow y = -1$
> * $\Delta z = -25 \rightarrow z = -1$
> **Interpretación:** El valor de la moneda $x$ es **1 USD**. (Nota: Los valores negativos representan deudas o salidas en el flujo de caja).

---

## Ejercicios para el estudiante

¡Es tu turno de brillar! Elige tu método favorito y resuelve:

🟢 **Nivel Fácil (Usa Gauss):**
$x + y - z = -3$
$3x - y + 2z = 9$
$2x - 2y - 3z = 0$

🟡 **Nivel Medio (Usa Cramer):**
$x + y - z = 1$
$2x + 3y + z = -2$
$5x - y + 2z = 4$

🟡 **Nivel Medio 2 (Refuerzo Gauss):**
$x + 2y + z = 7$
$3x + y + z = 5$
$2x + 3y - z = 3$

🔴 **Nivel Avanzado (Reto $USD):**
Un inversor tiene tres fondos. Las condiciones de equilibrio son:
$4x + 2y + 3z = 8$
$3x + 4y + 2z = -1$
$2x - y + 5z = 3$
*Pista: Intenta intercambiar filas para que los cálculos no te mareen.*

---

```ad-success
title: Respuestas para el docente
* **🟢 Fácil:** $x = 1, y = -2, z = 2$.
* **🟡 Medio 1:** $x = 1, y = -1, z = -1$.
* **🟡 Medio 2:** $x = 0, y = 2, z = 3$.
* **🔴 Avanzado:** $x = 2, y = -1, z = 3$. *(Se recomienda intercambiar la Fila 1 por la Fila 3 para trabajar con números más pequeños).*
```

---

## Autoevaluación

**1. Al preparar tu matriz de Gauss, ¿cuál es el orden sagrado de las columnas?**
a) Resultados, luego $x, y, z$.
b) $x, y, z$ y, tras la línea del "igual", el término independiente.
c) Al azar, el orden no afecta el resultado.

**2. Si la Fila 1 empieza con $5x$ y la Fila 3 con $1x$, ¿qué te dicta tu instinto de experto?**
a) Multiplicar todo por 5 y sufrir con números grandes.
b) Intercambiar la Fila 1 con la Fila 3 para que el "1" sea mi base de ataque.
c) Borrar la fila con el "1".

**3. En un problema de divisas, si $\Delta y = -25$ y el determinante del sistema $\Delta = 25$, ¿cuánto vale $y$?**
a) $1$
b) $0$
c) $-1$

> [!check] Soluciones de Autoevaluación
> 1. **b)** Es el estándar para que la "escalera" funcione.
> 2. **b)** El "1" es el mejor aliado para hacer ceros rápidamente.
> 3. **c)** Aplicando la fórmula: $-25 / 25 = -1$.

---

> [!tip] 💡 En la próxima clase
> ¡Lo has logrado! Ya dominas el 3x3. En la próxima lección veremos el **Método de Gauss-Jordan**, donde llevaremos la escalera al siguiente nivel para obtener los resultados directamente en la matriz.

> [!info] 🧭 Navegación
> - **Anterior:** [[Clase 02 — Sistemas de 2x2: Sustitución, Igualación y Reducción]]
> - **Siguiente:** [[Clase 04 — Aplicaciones Avanzadas y Método de Gauss-Jordan]]