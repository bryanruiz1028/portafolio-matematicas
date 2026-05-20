# Clase 07 — Inecuaciones Racionales: Casos Avanzados y Fracciones Comparadas
tags: #algebra #rationalinequal
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 7 de 9

> [!info] 🧭 Navegación
> [[Clase 06|⬅ Clase 06]] | [[00 - Índice del curso|Índice]] | **Clase 07** | [[Clase 08|Clase 08 ➡]]

---

> [!info] 🌍 Relevancia y aplicaciones
> Las inecuaciones racionales nos permiten comparar razones y proporciones donde la variable principal está en el denominador. Dominar este tema es fundamental para:
> - **💵 Aplicación $USD:** Modelar el costo promedio por producto. Si tienes una inversión fija y costos variables, puedes calcular cuántas unidades producir para que el costo unitario sea menor a un límite establecido.
> - **🏗️ Aplicación práctica:** En ingeniería civil, permite calcular rangos de seguridad y resistencia de materiales cuando las cargas se distribuyen de forma fraccionaria sobre una estructura.
> - **📊 Situación cotidiana:** Comparar ofertas de servicios (telefonía, internet) que combinan una tarifa base fija con un costo por uso, permitiéndote identificar el punto exacto donde una oferta se vuelve más económica que otra.

---

### Concepto clave

> [!note] 📌 ¿Qué es una inecuación racional?
> Para un estudiante de 12 años: "Es una comparación (usando mayor que $>$ o menor que $<$) entre dos expresiones matemáticas que tienen la letra 'x' tanto en la parte de arriba (numerador) como en la parte de abajo (denominador)".

> [!warning] ⚠️ Error común
> **NUNCA** pases a multiplicar una expresión que contenga 'x' al otro lado de la desigualdad. **La x no es un número fijo**, por lo tanto, no conocemos su signo. Si esa expresión resultara ser negativa, el signo de la desigualdad debería invertirse, y al no saberlo, arruinaríamos el proceso. Lo correcto es pasar todo a un lado restando o sumando para dejar un cero al otro lado.

> [!tip] 💡 Truco para recordarlo: La "Regla del Piso Prohibido"
> El denominador de una fracción **NUNCA** puede ser cero (la división por cero no existe). Por lo tanto, los puntos críticos que provengan del denominador **siempre** llevarán paréntesis abierto `(` o `)`, indicando que ese valor no se incluye en la solución, incluso si la inecuación tiene el signo "o igual" ($\le$ o $\ge$).

---

### Procedimiento paso a paso

```text
PASO 1 → Mover todos los términos a un lado de la desigualdad para dejar el cero al otro.
PASO 2 → Asegurar que los factores sean lineales (grado 1) o identificar factores 
         cuadráticos que no se pueden factorizar.
PASO 3 → Hallar puntos críticos igualando tanto el numerador como el denominador a cero.
PASO 4 → Graficar en la recta numérica, analizar signos por sectores (considerando 
         exponentes pares y coeficientes negativos) y escribir la solución en intervalos.
```

---

### Ejemplos Detallados

#### Ejemplo 1: Múltiples factores en el numerador (Video 4)
**Problema:** Resuelva $\frac{(x+4)(x+2)}{x-1} \leq 0$
1. **Puntos Críticos:** 
   - Numerador: $x+4=0 \rightarrow x=-4$; $x+2=0 \rightarrow x=-2$ (Se incluyen con corchete `[` por ser $\leq$).
   - Denominador: $x-1=0 \rightarrow x=1$ (Se excluye con paréntesis `)` por la "Regla del Piso Prohibido").
2. **Análisis:** Al ubicar -4, -2 y 1 en la recta, evaluamos sectores. Para ser $\leq 0$, buscamos los tramos negativos.
3. **Resultado:** $(-\infty, -4] \cup [-2, 1)$.

#### Ejemplo 2: Términos al cuadrado (Video 6)
**Problema:** Resuelva $\frac{4x-3}{x^2} \leq 0$
1. **Propiedad clave:** Cualquier número elevado al cuadrado es **siempre positivo o cero**. 
2. **Puntos Críticos:** $x=3/4$ (numerador) y $x=0$ (denominador).
3. **Análisis de Expertos:** Como $x^2$ siempre es positivo en su dominio, el signo de la fracción depende solo del numerador ($4x-3$). Sin embargo, debemos excluir el $0$ **específicamente** porque está en el denominador y lo anularía, no porque los cuadrados no puedan ser cero.
4. **Resultado:** $(-\infty, 0) \cup (0, 3/4]$.

#### Ejemplo 3: Fracciones Homogéneas (Video 7)
**Problema:** Resuelva $\frac{x}{4-2x} \geq \frac{3}{4-2x}$
1. **Procedimiento:** Restamos las fracciones: $\frac{x-3}{4-2x} \geq 0$.
2. **Puntos Críticos:** $x=3$ (numerador) y $x=2$ (denominador).
3. **Advertencia de Signos:** Nota que el coeficiente de $x$ en el denominador ($4-2x$) es **negativo**. Esto significa que el comportamiento de los signos en los sectores no seguirá el patrón estándar $+/-$ si usas trucos rápidos. Al evaluar un número mayor a 2 (como 2.5), el denominador se vuelve negativo, alterando el resultado del sector.
4. **Resultado:** $(2, 3]$.

#### Ejemplo 4: Aplicación Costo de Producción ($USD)
**Problema:** El costo unitario es $C(x) = \frac{10x + 50}{x}$. ¿Cuándo es el costo $\leq 15$ USD?
1. **Planteamiento:** $\frac{10x + 50}{x} - 15 \leq 0 \rightarrow \frac{10x + 50 - 15x}{x} \leq 0 \rightarrow \frac{-5x + 50}{x} \leq 0$.
2. **Puntos Críticos:** $x=10$ y $x=0$.
3. **Interpretación Lógica:** En economía, la producción $x$ debe ser mayor a cero ($x > 0$). Esto simplifica el análisis, ya que ignoramos cualquier intervalo negativo. El costo es menor o igual a 15 USD cuando se producen 10 o más unidades.
4. **Resultado:** $[10, \infty)$.

---

### Ejercicios para el estudiante

> [!abstract] 🟢 Nivel Fácil
> 1. $\frac{x-5}{x+2} > 0$
> 2. $\frac{x}{x-3} \leq 0$

> [!abstract] 🟡 Nivel Medio
> 1. $\frac{(x+5)(x-3)}{2x+1} \geq 0$
> 2. $\frac{2x-1}{(3x+4)^2} \geq 0$

> [!abstract] 🔴 Nivel Avanzado
> 1. $\frac{3x}{x+1} \leq \frac{5}{x+1} + 2$
> 2. **Costo unitario:** Determine el rango de ventas $x$ para que el costo unitario $\frac{20x + 100}{x-5}$ sea menor a 25 USD (considere $x > 5$).

> [!success] ✅ Soluciones (Para el docente)
> - **Fácil:** 1) $(-\infty, -2) \cup (5, \infty)$ | 2) $[0, 3)$
> - **Medio:** 
>   1) $[-5, -1/2) \cup [3, \infty)$ 
>   2) $[1/2, \infty)$. *(Nota: El punto $-4/3$ se excluye por el denominador y no afecta al intervalo de positivos que inicia en $1/2$)*.
> - **Avanzado:** 
>   1) $(-1, 7]$. *(Logística: Tras mover términos y simplificar, se obtiene $\frac{x-7}{x+1} \leq 0$)*.
>   2) $(45, \infty)$.

---

### Mini-prueba de autoevaluación

> [!question] Pregunta 1
> ¿Qué sucede con un punto crítico que proviene del denominador en una inecuación de tipo $\geq$?
> - **Respuesta:** Siempre debe ser abierto (no incluido) debido a la "Regla del Piso Prohibido" para evitar la indeterminación.

> [!question] Pregunta 2
> Si tenemos $(x-1)^2$ en el denominador, ¿qué signo tendrá ese factor en el análisis de sectores?
> - **Respuesta:** Siempre será positivo (excepto en $x=1$ donde la expresión no existe), por lo que no cambiará el signo de la inecuación al pasar por sus sectores.

> [!question] Pregunta 3
> Problema rápido de producción: Si $\frac{x-10}{x} < 0$ y sabemos que $x > 0$, ¿cuál es el rango de unidades?
> - **Respuesta:** El intervalo $(0, 10)$.

---

> [!tip] 💡 En la próxima clase
> Veremos cómo resolver inecuaciones racionales con **denominadores distintos** (no homogéneos), aplicando el Mínimo Común Múltiplo para unificar la expresión en una sola fracción.

> [!info] 🧭 Navegación
> [[Clase 06|⬅ Clase 06]] | [[00 - Índice del curso|Índice]] | **Clase 07** | [[Clase 08|Clase 08 ➡]]