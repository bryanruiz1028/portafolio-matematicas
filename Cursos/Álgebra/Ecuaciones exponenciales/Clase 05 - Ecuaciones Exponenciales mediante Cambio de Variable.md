# Clase 05 — Ecuaciones Exponenciales mediante Cambio de Variable
#algebra #exponentialequa
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 5 de 8

> [!info] 🧭 Navegación
> [[Clase 04|⬅ Clase 04]] | [[00 - Índice del curso|Índice]] | **Clase 05** | [[Clase 06|Clase 06 ➡]]

---

### ¿POR QUÉ ES IMPORTANTE ESTA CLASE?
Resolver ecuaciones donde la incógnita está en el exponente puede parecer un desafío imposible. Esta técnica nos permite "simplificar" lo complejo, transformando expresiones exponenciales en ecuaciones cuadráticas que ya sabemos dominar.

*   💵 **Aplicación USD:** Cálculo de "Puntos de Equilibrio" en finanzas, determinando el tiempo exacto en que una inversión iguala a sus costos operativos.
*   🏗️ **Aplicación práctica:** Modelado de crecimiento biológico, permitiendo predecir cuándo una población de bacterias alcanzará un tamaño crítico.
*   📊 **Situación cotidiana:** Proyecciones de viralidad en redes sociales para entender cuándo la propagación de una noticia se estabilizará.

---

### CONCEPTO CLAVE (DEFINICIÓN Y TRUCOS)

> [!note] 📌 ¿Qué es el Cambio de Variable?
> Imagina que te enfrentas a un "monstruo" matemático difícil de combatir. El cambio de variable es como ponerle un **disfraz de algo más sencillo**. Sustituimos la parte exponencial por una letra (como $m$, $u$ o $t$) para convertir la ecuación en una de segundo grado. Una vez que derrotamos a la ecuación simple, le quitamos el disfraz para recuperar el valor original de $x$.

> [!warning] ⚠️ Errores comunes
> 1. **Olvidar quitar el "disfraz":** El error más fatal es hallar el valor de la variable auxiliar (ej. $m=8$) y no terminar el proceso para hallar $x$.
> 2. **Resultados negativos:** Al deshacer el cambio, recuerda que una base positiva elevada a cualquier exponente **nunca** dará un resultado negativo (ej. $2^x = -4$ no tiene solución).
> 3. **Coeficientes olvidados:** Si la ecuación resultante es $3m^2 - 10m + 3 = 0$, no intentes factorizar de forma simple; usa la fórmula general o factorización para $ax^2 + bx + c$.
>
> *   ❌ **Incorrecto:** Terminar en $m = 8$.
> *   ✅ **Correcto:** $2^x = 8 \implies 2^x = 2^3 \implies x = 3$.

> [!tip] 💡 Truco para recordarlo
> **"Si una base es el cuadrado de la otra, el cambio de variable es la maniobra."**
> Observa las bases: si ves un $2^x$ y un $4^x$ (que es $(2^2)^x$), o un $3^x$ y un $9^x$ (que es $(3^2)^x$), el cambio de variable es tu mejor aliado.

---

### PROCEDIMIENTO PASO A PASO

```latex
PASO 1a: Identificar la relación entre bases. Reconocer si una base es potencia de otra: $4^x = (2^x)^2$.
PASO 1b: Separar exponentes. Usar propiedades de potencias para eliminar sumas o restas: $2^{x+2} = 2^x \cdot 2^2$.
PASO 2:  Sustitución. Reemplazar la expresión exponencial por una variable auxiliar (ej. $m = 2^x$).
PASO 3:  Resolver la cuadrática. Hallar los valores de la variable auxiliar usando factorización o fórmula general.
PASO 4:  Volver a la variable original. Aplicar el principio de "Bases iguales, exponentes iguales" para hallar $x$.
```

---

### EJEMPLOS PRÁCTICOS

> [!example] Ejemplo 1: Caso Básico (Video 4)
> **Ecuación:** $4^x - 4 \cdot 2^x - 32 = 0$
> 1. Transformamos la base mayor: $(2^x)^2 - 4 \cdot 2^x - 32 = 0$.
> 2. Hacemos el cambio $2^x = m$: $m^2 - 4m - 32 = 0$.
> 3. Factorizamos: $(m - 8)(m + 4) = 0$.
> 4. Obtenemos $m = 8$ y $m = -4$.
> 5. Deshacemos el cambio:
>    * $2^x = 8 \implies 2^x = 2^3 \implies \mathbf{x = 3}$ (Bases iguales, exponentes iguales).
>    * $2^x = -4 \implies$ **Sin solución real** (una base positiva no produce resultados negativos).

> [!example] Ejemplo 2: Caso con Exponentes Negativos (Video 6)
> **Ecuación:** $2^x + 2^{1-x} = 3$
> 1. Aplicamos propiedad de división para la resta en el exponente: $2^x + \frac{2^1}{2^x} = 3$.
> 2. Cambiamos $2^x = t$: $t + \frac{2}{t} = 3$.
> 3. Multiplicamos toda la ecuación por $t$ para eliminar el denominador: $t^2 + 2 = 3t$.
> 4. Ordenamos a forma cuadrática: $t^2 - 3t + 2 = 0$.
> 5. Factorizamos: $(t - 2)(t - 1) = 0$, resultando en $t = 2$ y $t = 1$.
> 6. Volvemos a $x$:
>    * $2^x = 2^1 \implies \mathbf{x = 1}$.
>    * $2^x = 1 \implies 2^x = 2^0 \implies \mathbf{x = 0}$.

> [!example] Ejemplo 3: Caso con Descomposición de Sumas (Video 5)
> **Ecuación:** $4^x + 2^5 = 3 \cdot 2^{x+2}$
> 1. **Paso crucial:** Descomponemos $2^{x+2}$ como $2^x \cdot 2^2$.
> 2. Reescribimos: $(2^x)^2 + 32 = 3 \cdot (2^x \cdot 4) \implies (2^x)^2 + 32 = 12 \cdot 2^x$.
> 3. Cambio $2^x = m$: $m^2 - 12m + 32 = 0$.
> 4. Factorizamos: $(m - 8)(m - 4) = 0 \implies m = 8, m = 4$.
> 5. Deshacemos el cambio:
>    * $2^x = 8 \implies 2^x = 2^3 \implies \mathbf{x = 3}$.
>    * $2^x = 4 \implies 2^x = 2^2 \implies \mathbf{x = 2}$.

> [!example] Ejemplo 4: Aplicación Real (Punto de Equilibrio en USD)
> Una startup tecnológica proyecta que sus ingresos mensuales crecen según la función $4^t$, donde $t$ es el tiempo en meses. Sus costos operativos fijos y variables siguen la función $4 \cdot 2^t + 32$. ¿En qué mes los ingresos igualarán a los costos (Punto de Equilibrio)?
> * **Igualamos funciones:** $4^t = 4 \cdot 2^t + 32 \implies 4^t - 4 \cdot 2^t - 32 = 0$.
> * Al resolver (como en el Ejemplo 1), la variable auxiliar nos da $m = 8$ (el valor negativo se descarta).
> * $2^t = 8 \implies 2^t = 2^3 \implies \mathbf{t = 3}$.
> * **Resultado:** La empresa alcanzará su punto de equilibrio en el **mes 3**.

---

### EJERCICIOS PARA EL ESTUDIANTE

> [!abstract] Taller de Práctica
> **🟢 Nivel Fácil (Directas)**
> 1. $9^x - 10 \cdot 3^x + 9 = 0$
> 2. $4^x - 6 \cdot 2^x + 8 = 0$
> 3. $25^x - 6 \cdot 5^x + 5 = 0$
> 4. $4^x - 3 \cdot 2^x + 2 = 0$
>
> **🟡 Nivel Medio (Separar Exponentes)**
> 5. $9^x + 27 = 4 \cdot 3^{x+1}$
> 6. $4^x + 16 = 10 \cdot 2^x$
> 7. $9^x - 3^x - 6 = 0$
> 8. $7^x + 7^{2-x} = 50$ (Pista: Usa el método del Ejemplo 2).
>
> **🔴 Nivel Avanzado (Coeficientes y Fracciones)**
> 9. $3 \cdot 9^x - 10 \cdot 3^x + 3 = 0$ (Requiere manejar coeficientes en la cuadrática).
> 10. $2 \cdot 4^x - 5 \cdot 2^x + 2 = 0$
> 11. $2^x + 2^{2-x} = 5$
> 12. Un análisis de mercado en USD determina que el precio de un activo sigue la ecuación $3^x + 3^{2-x} = 10$. Halla los valores de $x$ que satisfacen el equilibrio de mercado.

> [!success] Solucionario (Para el docente)
> 1. $x=0, x=2$ | 2. $x=1, x=2$ | 3. $x=0, x=1$ | 4. $x=0, x=1$
> 5. $x=1, x=2$ | 6. $x=1, x=3$ | 7. $x=1$ (se descarta $m=-2$) | 8. $x=0, x=2$
> 9. $x=-1, x=1$ (Valores de $m$: $3$ y $1/3$) | 10. $x=-1, x=1$ | 11. $x=0, x=2$ | 12. $x=0, x=2$

---

### MINI-PRUEBA DE AUTOEVALUACIÓN

> [!question] ¿Cuánto has aprendido?
> **1. ¿Qué propiedad es fundamental para resolver $2^{x+3}$ antes de hacer el cambio de variable?**
> a) Potencia de una potencia.
> b) Producto de potencias de igual base ($2^x \cdot 2^3$).
> c) Cociente de potencias.
>
> **2. Si tras resolver la cuadrática obtienes $m = 1/9$ para una ecuación con cambio $3^x = m$, ¿cuál es el valor de $x$?**
> a) $x = -2$.
> b) $x = 2$.
> c) No tiene solución.
>
> **3. ¿Por qué descartamos soluciones como $2^x = -8$?**
> a) Porque los exponentes no pueden ser negativos.
> b) Porque una base positiva elevada a cualquier potencia real siempre es positiva.
> c) Porque el Profe Alex dice que el 8 debe ser positivo.

> [!check] Respuestas y Explicaciones
> 1. **b)** Debemos separar la suma del exponente para que la variable quede sola.
> 2. **a)** $3^x = 1/9 \implies 3^x = 3^{-2} \implies x = -2$.
> 3. **b)** Es una propiedad intrínseca de las funciones exponenciales de base positiva.

---

> [!tip] 💡 En la próxima clase
> ¿Qué pasa si no podemos igualar las bases? Por ejemplo: $2^x = 7$. En la Clase 06 descubriremos la herramienta definitiva: **Los Logaritmos**.

> [!info] 🧭 Navegación
> [[Clase 04|⬅ Clase 04]] | [[00 - Índice del curso|Índice]] | **Clase 05** | [[Clase 06|Clase 06 ➡]]