# Clase 02 — Potencias con Exponentes Negativos y Propiedades de la Potenciación

**tags:** #algebra #potenciaconexpo
**Curso:** [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 4

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | | [[Clase 03|Clase 03 ➡]]

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> Entender los exponentes negativos nos permite trabajar con cantidades muy pequeñas o valores que decrecen proporcionalmente, facilitando el manejo de fracciones complejas mediante reglas algebraicas sencillas.

*   💵 **$USD:** Cálculo de depreciación; por ejemplo, si un activo pierde la mitad de su valor cada año, usamos potencias negativas para hallar su precio residual.
*   🏗️ **Ingeniería:** Aplicación de escalas de reducción en planos, donde las dimensiones se transforman mediante factores de potencia inversa.
*   📊 **Situaciones cotidianas:** Representación de tamaños en el mundo microscópico, como el grosor de una membrana celular o el tamaño de un virus.

## Concepto clave: Potencia con exponente negativo

> [!note] 📌 ¿Qué es Potencia con exponente negativo?
> Una potencia con exponente negativo $a^{-n}$ es igual a $1/a^n$. Esto no es magia, surge de la **propiedad del cociente de potencias de bases iguales**. Por ejemplo, si tienes $a^2 / a^5$, la regla dice que restamos los exponentes: $2 - 5 = -3$. Pero si lo escribes desarrollado, tachas dos "a" arriba y dos abajo, y te quedan tres "a" en la parte de abajo. Por eso, $a^{-3}$ es lo mismo que $1/a^3$. El signo negativo es simplemente una instrucción para "mudar" la base al denominador.

> [!warning] ⚠️ Error común
> 1. **Paréntesis:** Recuerda que $(-3)^2$ es $(-3) \cdot (-3) = 9$ (el exponente afecta al signo), pero $-3^2$ es $-(3 \cdot 3) = -9$ (el signo está afuera). ¡El exponente solo afecta a lo que tiene inmediatamente debajo!
> 2. **Base Cero:** La base $a$ **nunca puede ser cero** cuando el exponente es negativo. Como $a^{-n}$ se convierte en una fracción con la base abajo ($1/a^n$), si $a$ fuera cero, estaríamos dividiendo por cero, lo cual es imposible en matemáticas.

> [!tip] 💡 Truco para recordarlo
> Para "positivizar" un exponente, **invierte la base** inmediatamente. Si la base es un entero como $5$, imagina que tiene un $1$ abajo y voltéalo a $1/5$. Si es una fracción como $2/3$, voltéala a $3/2$. Al hacer este giro, el exponente cambia de negativo a positivo al instante.

## Procedimiento paso a paso

```text
PASO 1 → Identificar si la base es una fracción (a/b) o un entero (a).
PASO 2 → Invertir la base:
         - Si es entero: a se convierte en 1/a.
         - Si es fracción: a/b se convierte en b/a.
PASO 3 → Cambiar el signo del exponente a positivo.
PASO 4 → Si es "Potencia de una potencia", multiplica los exponentes 
         (m * n) antes de aplicar la inversión para simplificar.
```

## Ejemplos prácticos

> [!example] Ejemplo 1: Caso básico
> Resolver $5^{-3}$.
> 1. Invertimos la base (entero 5): $1/5$.
> 2. El exponente $-3$ pasa a ser $3$: $1/5^3$.
> 3. Calculamos: $1 / (5 \cdot 5 \cdot 5) =$ **$1/125$**.

> [!example] Ejemplo 2: Signos y Paréntesis
> ¿Es lo mismo $(-2)^4$ que $-2^4$?
> *   $(-2)^4$: La base es $-2$. Al ser exponente par, el resultado es positivo: **$16$**.
> *   $-2^4$: El menos no está afectado por el exponente. Calculamos $2^4 = 16$ y mantenemos el signo: **$-16$**.

> [!example] Ejemplo 3: Potencia de una potencia
> Resolver $(x^2)^3$ y $(a^{-2})^4$.
> 1. Para $(x^2)^3$: Multiplicamos $2 \cdot 3$. Resultado: **$x^6$**.
> 2. Para $(a^{-2})^4$: Multiplicamos $-2 \cdot 4 = -8$. Esto nos da $a^{-8}$.
> 3. Aplicamos la regla: **$1/a^8$**.

> [!example] Ejemplo 4: Aplicación USD
> Un producto de $1000 USD pierde la mitad de su valor cada año. Su valor tras 3 años se expresa como $1000 \cdot 2^{-3}$.
> *   Aquí, $2^{-3}$ significa multiplicar por **$1/2$ tres veces** (o dividir por $2$ tres veces).
> *   $1000 \cdot (1/2^3) = 1000 \cdot (1/8)$.
> *   Resultado: **$125 USD$**.

## Ejercicios para el estudiante

> [!abstract] 🟢 Nivel Fácil (Conversión simple)
> 1. Expresa $4^{-2}$ con exponente positivo.
> 2. Expresa $10^{-3}$ con exponente positivo.
> 3. Calcula el valor final de $3^{-2}$.
> 4. Convierte $a^{-7}$ en una fracción.

> [!abstract] 🟡 Nivel Medio (Potencia de potencia y negativos)
> 1. Resuelve $(x^{-2})^3$.
> 2. Resuelve $(5^2)^{-2}$.
> 3. Simplifica $(a^{-3})^{-2}$.
> 4. Simplifica $(x^3)^2 \cdot x^{-4}$. *(Pista: Primero multiplica exponentes en el paréntesis, luego suma las bases iguales).*

> [!abstract] 🔴 Nivel Avanzado (Fracciones y variables)
> 1. Resuelve $(3/4)^{-2}$.
> 2. Resuelve $(a/b)^{-3}$.
> 3. Simplifica $[(x^2)^{-3}] / x^{-5}$.
> 4. Calcula el valor de $(1/2)^{-4}$.

> [!success] Respuestas para el docente
> **Fácil:** 1) $1/4^2$; 2) $1/10^3$; 3) $1/9$; 4) $1/a^7$.
> **Medio:** 1) $1/x^6$; 2) $1/625$; 3) $a^6$; 4) $x^2$.
> **Avanzado:** 1) $16/9$; 2) $b^3/a^3$; 3) $1/x$; 4) $16$.

## Autoevaluación

> [!question] Pregunta 1
> ¿Cuál es el resultado de $a^0$ siempre que la base $a$ sea diferente de cero?
> a) $0$
> b) $a$
> c) $1$
> d) No se puede calcular
> **Validación:** **c) 1.** Por propiedad, cualquier base (excepto cero) elevada a la cero es uno.

> [!question] Pregunta 2
> ¿Cómo se convierte $(2/5)^{-3}$ a exponente positivo?
> a) $( -2/-5 )^3$
> b) $( 5/2 )^3$
> c) $2/5^3$
> d) $(-5/2)^3$
> **Validación:** **b).** Se invierte la fracción (la base) y el exponente cambia de signo.

> [!question] Pregunta 3
> Si una inversión de $800 USD se calcula como $800 \cdot 2^{-2}$, ¿cuál es su valor?
> a) $400 USD$
> b) $200 USD$
> c) $1600 USD$
> d) $100 USD$
> **Validación:** **b) 200 USD.** Porque $800 \cdot (1/2^2) = 800 / 4 = 200$.

> [!tip] 💡 En la próxima clase
> Ya sabes cómo "darle la vuelta" a las potencias negativas. En la siguiente sesión, combinaremos todas las propiedades para resolver operaciones largas con paréntesis y fracciones.

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | | [[Clase 03|Clase 03 ➡]]