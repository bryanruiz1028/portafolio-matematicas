# Clase 04 — Multiplicación de números enteros y Valor absoluto

tags: #algebra #howtomultiplyin
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 4 de 8

> [!info] 🧭 Navegación
> [[Clase 03]] | **Clase 04** | [[00 - Índice del curso|Índice]]

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> La multiplicación de enteros y el valor absoluto permiten modelar el crecimiento o decrecimiento repetido de una magnitud, así como medir distancias exactas sin importar el sentido del movimiento. Son herramientas esenciales para proyectar balances financieros, calcular fuerzas estructurales y entender fenómenos físicos de cambio exponencial.

- **💵 Aplicación USD:** Calcular el monto total de una deuda acumulada. Por ejemplo, si se deben 5 USD a 4 personas diferentes, la multiplicación permite determinar el saldo negativo total de forma instantánea.
- **🏗️ Aplicación práctica:** Determinar la profundidad final de una cimentación cuando una máquina excavadora desciende niveles constantes bajo el suelo (niveles negativos).
- **📊 Situación cotidiana:** Analizar variaciones en estados de cuenta bancarios tras retiros automáticos sucesivos o calcular promedios de variaciones de temperatura.

## Concepto clave

> [!note] 📌 ¿Qué es la multiplicación de enteros?
> Para un estudiante de 12 años, multiplicar es simplemente sumar un mismo número varias veces (por ejemplo, tener una deuda de 5 USD tres veces). 
> 
> **La Regla de Oro:** Para saber si hay una multiplicación, **mira fuera del paréntesis**. No busques el signo dentro; observa el espacio *entre* los números o paréntesis. Si no hay un signo de suma (+) o resta (-) separándolos, entonces es una multiplicación.
> 
> **💡 Tip de Especialista:** En álgebra, dejamos de usar la "x" para multiplicar porque se confunde con la variable $x$. En su lugar, usamos un punto ($\cdot$) o simplemente paréntesis pegados: `(a)(b)`.

### Demostración de la Ley de los Signos
¿Por qué "menos por menos es más"? No es magia, es lógica matemática:

- **Lógica de Euler (La Deuda):** Euler explicaba que un número negativo es una deuda. Si multiplicas un saldo negativo por un número positivo, tienes esa deuda varias veces (Negativo). Pero, si multiplicas un negativo por otro negativo, es equivalente a **"quitar una deuda"**, lo que financieramente se traduce en una ganancia o un estado positivo.
- **Razonamiento de Cauchy y Laplace (Propiedad Distributiva):** Ellos demostraron que para que la matemática sea coherente, debe cumplirse que $(-a) \cdot [(-b) + b] = 0$. Como ya sabemos que $(-a) \cdot (b) = -ab$, para que la suma final dé cero, el resultado de $(-a) \cdot (-b)$ tiene que ser obligatoriamente $+ab$ (positivo).

> [!warning] ⚠️ Error común
> Muchos estudiantes confunden la **suma de negativos** con la **multiplicación**.
> - **Suma:** $-5 - 3 = -8$ (Debo 5 y pido prestado 3, sigo debiendo).
> - **Multiplicación:** $(-5)(-3) = +15$ (Se aplica la Ley de los Signos).

> [!tip] 💡 Truco para recordarlo
> - **Signos iguales** ($+ \cdot +$ o $- \cdot -$) resultan en **Positivo (+)**.
> - **Signos diferentes** ($+ \cdot -$ o $- \cdot +$) resultan en **Negativo (-)**.

## Procedimiento paso a paso

```text
1. IDENTIFICAR la operación: Observar si hay ausencia de signos operativos 
   (+ o -) entre los factores o paréntesis (mirar por fuera).
2. RESOLVER operaciones internas: Si hay barras de valor absoluto, resolver 
   lo que está dentro hasta obtener un solo número.
3. DETERMINAR el signo: Aplicar la Ley de los Signos al conjunto de factores.
4. MULTIPLICAR valores: Multiplicar los valores absolutos de los números.
5. APLICAR el signo: Colocar el signo determinado en el paso 3 al resultado.
```

## Bloque de ejemplos detallados

> [!example] Ejemplo 1: Básico (Signos iguales)
> Operación: $5 \cdot 3$
> - Ambos factores son positivos (iguales).
> - El signo resultante es positivo.
> - Multiplicamos los valores: $5 \times 3 = 15$.
> **Resultado: 15**

> [!example] Ejemplo 2: Con signos diferentes
> Operación: $(-3)(5)$
> - Miramos fuera del paréntesis: no hay signo entre el -3 y el 5, es multiplicación.
> - Negativo por Positivo = Negativo (Signos diferentes).
> - Multiplicamos valores: $3 \times 5 = 15$.
> **Resultado: -15**

> [!example] Ejemplo 3: Avanzado (Múltiples factores y valor absoluto)
> Operación: $|7 - 9| \cdot (-2)(5)(-3)$
> 1. Resolvemos el valor absoluto primero (actúa como grupo): $|7 - 9| = |-2| = 2$.
> 2. La operación queda: $2 \cdot (-2) \cdot (5) \cdot (-3)$.
> 3. Seguimos la cadena de signos paso a paso:
>    - $(2) \cdot (-2) = -4$
>    - $(-4) \cdot (5) = -20$
>    - $(-20) \cdot (-3) = +60$ (Menos por menos es más).
> **Resultado: 60**

> [!example] Ejemplo 4: Aplicación USD (Deuda)
> Problema: "Debo 5 USD a cada uno de mis 3 hermanos".
> - Representación: $3$ (personas) $\cdot -5$ (deuda individual).
> - Signo: Positivo por negativo = Negativo.
> - Valor: $3 \times 5 = 15$.
> **Resultado: -15 USD (Tienes un saldo total de -15 dólares)**

## Ejercicios para el estudiante

> [!abstract] 🟢 Nivel Fácil
> 1. $7 \cdot 8$
> 2. $(-4) \cdot (-9)$
> 3. $|-15|$
> 4. $6 \cdot (-2)$

> [!abstract] 🟡 Nivel Medio
> 1. $-(-8)$ (Recuerda: es como multiplicar $-1 \cdot -8$).
> 2. $(-3)(2)(-4)$
> 3. $-( -10 - 5 )$ (Resuelve el interior primero).
> 4. $(-1)(-1)(-1)(-1)(-1)$ (Cuenta cuántos negativos hay).

> [!abstract] 🔴 Nivel Avanzado (USD)
> 1. Un comerciante pierde 6 USD por cada producto roto. Si rompe 5 productos, ¿cuál es su balance?
> 2. $|-12 + 4| \cdot (-3)$
> 3. $5 \cdot |10 - 15| \cdot (-2)$
> 4. Tienes un balance de -10 USD en tu cuenta y el banco triplica esa deuda por falta de pago. Expresa el resultado final.

> [!success] ✅ Respuestas
> 1. **Fácil:** 1) 56, 2) 36, 3) 15, 4) -12.
> 2. **Medio:** 1) 8, 2) 24, 3) 15, 4) -1.
> 3. **Avanzado:** 1) -30 USD, 2) -24, 3) -50, 4) -30 USD.

## Mini-prueba de autoevaluación

> [!question] 🧪 Pregunta 1
> ¿Cómo identificas correctamente una multiplicación en la expresión $5(-4)$?
> a) Mirando el signo negativo dentro del paréntesis.
> b) Porque hay un signo de suma invisible.
> c) Observando que no hay ningún signo operativo (+ o -) entre el 5 y el paréntesis.
> d) Porque el resultado debe ser negativo.
> **Respuesta correcta: c.** Según la pedagogía de Profe Alex, la clave es mirar el espacio exterior entre los factores.

> [!question] 🧪 Pregunta 2
> Aplica la Ley de los Signos: ¿Cuál es el resultado de $(-6) \cdot (-4) \cdot (-1)$?
> a) 24
> b) -24
> c) 11
> d) -11
> **Respuesta correcta: b.** Paso a paso: $(-6 \cdot -4) = +24$. Luego, $(+24 \cdot -1) = -24$.

> [!question] 🧪 Pregunta 3
> Si tienes un saldo bancario de -20 USD y esta cantidad se multiplica por 4, ¿cuál es tu situación financiera final?
> a) Tienes 80 USD de ganancia.
> b) Debes 16 USD.
> c) Debes 80 USD.
> d) Tu saldo es 0.
> **Respuesta correcta: c.** Operación: $4 \cdot (-20) = -80$ USD. El signo negativo indica deuda.

## Notas para el próximo tema

> [!tip] 💡 En la próxima clase
> Ahora que dominas la multiplicación, pasaremos a la **División de números enteros**. Te darás cuenta de que la Ley de los Signos se aplica exactamente de la misma manera. ¡Nos vemos en la Clase 05!

> [!info] 🧭 Navegación
> [[Clase 03]] | **Clase 04** | [[00 - Índice del curso|Índice]]