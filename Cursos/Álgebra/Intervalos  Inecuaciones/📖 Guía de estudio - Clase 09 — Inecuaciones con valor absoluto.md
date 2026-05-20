# 📖 Guía de estudio — Clase 09: Inecuaciones con valor absoluto

> [!info] 📌 Conceptos clave
> - **Definición de valor absoluto:** Se interpreta como la **distancia** de un número respecto al cero en la recta numérica. En la práctica, consiste en eliminar el signo del número, pues una distancia siempre es positiva o cero.
> - **Requisito de positividad:** Para aplicar las fórmulas de resolución rápida, el número constante ($a$) debe ser **positivo**. Esto es lógico, ya que una distancia nunca puede ser menor que un número negativo.
> - **Comparación con números negativos:** Si tienes $|x| < \text{negativo}$, la solución es el **conjunto vacío (Ø)** (nada es menor que un negativo). Si tienes $|x| > \text{negativo}$, la solución son **todos los números reales ($\mathbb{R}$)**, pues cualquier valor absoluto positivo siempre será mayor que un negativo.
> - **Diferencia lógica:** El caso "menor que" busca una **intersección** (los valores están "atrapados" en el centro). El caso "mayor que" busca una **unión** (los valores escapan hacia los extremos de la recta).

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula | Aplicación Visual (Recta Numérica) |
| :--- | :--- | :--- |
| **Valor Absoluto $|x|$** | Distancia al cero o eliminar el signo. | El valor de $|5|$ es 5 y de $|-5|$ es 5. |
| **Caso $|x| < a$ (o $\leq$)** | $-a < x < a$ | Sombreado **entre** $-a$ y $a$ (segmento central). |
| **Caso $|x| > a$ (o $\geq$)** | $x < -a \cup x > a$ | Sombreado hacia las flechas de los **extremos** (dos semirrectas). |

## Ejemplos Resueltos Adicionales

> [!example] Ejemplo A: Resolución de $|x - 3| \leq 12$
> 1. **Paso 1 (Eliminar barras):** Aplicamos la fórmula para "menor o igual", encerrando el contenido entre el negativo y el positivo del número: $-12 \leq x - 3 \leq 12$.
> 2. **Paso 2 (Despejar la incógnita):** El 3 que está restando pasa a sumar a ambos extremos de la inecuación para mantener el equilibrio: $-12 + 3 \leq x \leq 12 + 3$. Esto nos da $-9 \leq x \leq 15$.
> 3. **Paso 3 (Resultado final):** La solución son todos los números desde el -9 hasta el 15.
>    - **Intervalo:** **$[-9, 15]$**
> 
> *Nota pedagógica: Si la x tuviera un coeficiente (ej. $|2x - 3|$), el último paso sería dividir todos los términos por ese número.*

> [!example] Ejemplo B: Aplicación en Precios de Mercado (USD)
> Supongamos que un producto tiene un precio ideal de $50 USD y se acepta una variación máxima de $5 USD. Esto se expresa como $|x - 50| \leq 5$.
> 1. **Planteamiento:** $-5 \leq x - 50 \leq 5$.
> 2. **Despeje:** Sumamos 50 en todos los lados: $50 - 5 \leq x \leq 50 + 5$.
> 3. **Rango aceptable:** $45 \leq x \leq 55$. El precio puede oscilar en el intervalo **$[45, 55]$**.

## Ejercicios de Repaso

> [!abstract] Nivel Fácil (Verde)
> 1. $|x| < 8$
> 2. $|x| \geq 7$
> 3. $|x| \leq 10$

> [!abstract] Nivel Medio (Amarillo)
> 1. $|2x - 3| < 7$
> 2. $|3x + 1| \geq 10$
> 
> *💡 Tip: No olvides que si pasas a dividir un número negativo, debes invertir la dirección de los signos de desigualdad.*

> [!abstract] Nivel Avanzado (Rojo)
> **Problema de Presupuesto:** Un analista financiero determina que una inversión es riesgosa si la diferencia entre el gasto real ($x$) y el presupuesto de $100 USD es mayor a una desviación de $20 USD. 
> - Plantea y resuelve: $|x - 100| > 20$. 
> - Determina los rangos de gasto que se consideran riesgosos (donde la inversión "se escapa" del control).

> [!tip] 💡 Consejo de estudio
> Para recordar cómo abrir las barras de valor absoluto, usa la técnica del Profe Alex:
> 
> 1. **Si es "Menor que" ($<$ o $\leq$):** El número está **atrapado**. Escribe $-a$ a la izquierda, $a$ a la derecha y el contenido en el centro.
> 2. **Si es "Mayor que" ($>$ o $\geq$):** Se divide en dos **colas** separadas. 
>    - La primera parte es igual a la original pero sin barras ($x > a$).
>    - La segunda parte requiere **voltear el signo** de la desigualdad y **cambiar el signo** del número ($x < -a$).
> 
> **¡Cuidado!** Siempre verifica si el número del lado derecho es negativo antes de empezar; podrías ahorrarte todo el procedimiento si aplicas la lógica de "conjunto vacío" o "todos los reales".