# Clase 02 — Sumatoria y Notación Sigma: Aplicación y Resolución de Problemas

#algebra #summationsigman

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | | [[Clase 03|Clase 03 ➡]]

---

## 1. Relevancia y Aplicaciones

La notación sigma ($\Sigma$) es una de las herramientas más poderosas del álgebra para simplificar el lenguaje matemático. En lugar de escribir largas cadenas de sumas, utilizamos este símbolo para condensar procesos repetitivos de manera elegante y eficiente.

> [!info] 🌍 Relevancia y aplicaciones
> - **💵 Aplicación en $USD**: Es esencial para calcular el interés compuesto o ahorros programados. Si ahorras una cantidad que crece exponencialmente (como duplicar el monto cada día), la notación sigma te permite visualizar el capital total acumulado con una sola fórmula.
> - **🏗️ Aplicación Práctica**: En el mundo de la construcción, se emplea para calcular la cantidad de materiales necesarios en estructuras con dimensiones progresivas, como el número de vigas en un puente de niveles variables o los bloques en una pirámide.
> - **📊 Situación Cotidiana**: Desde sumar los pasos diarios registrados en tu teléfono hasta las calorías consumidas en una semana, la notación sigma organiza grandes volúmenes de datos estadísticos de forma compacta.

---

## 2. Conceptos Fundamentales

Para dominar esta herramienta, debemos entender que el símbolo $\Sigma$ funciona como una "máquina de procesar números" con instrucciones muy precisas.

> [!note] 📌 ¿Qué es Summation - Sigma Notation?
> Es una forma abreviada de escribir una suma de muchos términos usando la letra griega $\Sigma$. Funciona bajo tres componentes: un **límite inferior** (donde empezamos), un **límite superior** (donde nos detenemos) y una **fórmula** que define cada término. Imagínalo como un ascensor: el número de abajo indica en qué piso entras y el de arriba en qué piso te bajas.

> [!warning] ⚠️ Error común
> El error más grave es no respetar la **Variable de Control**. Si debajo del símbolo aparece $k=1$, solo debes reemplazar la letra $k$ en la fórmula. Si ves otras letras (como una $x$ o una $a$) que no coinciden con la variable de control, trátalas como constantes: **no cambies su valor**, simplemente déjalas como están mientras sustituyes la variable indicada.

> [!tip] 💡 Truco para recordarlo
> - El número de **abajo** es el "Suelo": es el punto de partida de tu caminata.
> - El número de **arriba** es el "Techo": es donde pones las manos y dejas de sumar.

---

## 3. Procedimiento Resolutivo

Como su profesor, les sugiero seguir siempre este orden lógico para evitar errores aritméticos. Aquí aplicamos el rigor de la jerarquía de operaciones.

```text
PASO 1 → Identificar la variable de control, el límite inferior y el superior.
PASO 2 → Reemplazar la variable en la fórmula por cada número entero de la secuencia.
PASO 3 → Resolver las operaciones de cada término siguiendo la jerarquía (PEMDAS): 
         Primero potencias, luego multiplicaciones y finalmente sumas o restas.
PASO 4 → Sumar todos los resultados individuales para obtener el valor total.
```

> [!important] **Nota Didáctica sobre PEMDAS**
> Dentro de cada término de la sumatoria, debemos respetar el orden de las operaciones. Nunca restes antes de elevar al cuadrado, ni multipliques antes de resolver un paréntesis. La precisión en cada término garantiza el éxito del total.

---

## 4. Ejemplos Desarrollados

Basados en las metodologías del curso, analicemos estos cuatro casos:

> [!example] **Ejemplo 1 — Caso Básico**
> Resuelve: $\sum_{i=1}^{4} 3i$
> - **Desarrollo**: Sustituimos $i$ por $\{1, 2, 3, 4\}$.
> - **Operación**: $3(1) + 3(2) + 3(3) + 3(4)$
> - **Términos**: $3 + 6 + 9 + 12$
> ✅ **Resultado final**: $30$

> [!example] **Ejemplo 2 — Potencias y límites variables**
> Resuelve: $\sum_{i=3}^{5} (i^2 - 2)$
> - Para $i=3$: $(3^2 - 2) = 9 - 2 = 7$
> - Para $i=4$: $(4^2 - 2) = 16 - 2 = 14$
> - Para $i=5$: $(5^2 - 2) = 25 - 2 = 23$
> - **Suma**: $7 + 14 + 23$
> ✅ **Resultado final**: $44$

> [!example] **Ejemplo 3 — Caso Avanzado con Fracciones (Método MCM)**
> Resuelve: $\sum_{i=1}^{5} \frac{i^2+6}{i}$
> Siguiendo el método de **homogeneización de fracciones** del video:
> 1. Términos enteros: $i=1 \to 7$; $i=2 \to 5$; $i=3 \to 5$. Suma parcial = $17$.
> 2. Términos fraccionarios: $i=4 \to \frac{11}{2}$; $i=5 \to \frac{31}{5}$.
> 3. **Homogeneización**: El MCM de $1, 2$ y $5$ es $10$.
>    - $\frac{17}{1} = \frac{170}{10}$; $\frac{11}{2} = \frac{55}{10}$; $\frac{31}{5} = \frac{62}{10}$.
> 4. **Suma final**: $\frac{170 + 55 + 62}{10} = \frac{287}{10}$
> ✅ **Resultado final**: $28.7$

> [!example] **Ejemplo 4 — Inversión Exponencial ($USD)**
> Calcula el total de una inversión que crece según la fórmula $3^i$ durante 3 días: $\sum_{i=1}^{3} 3^i$.
> - Día 1: $3^1 = 3$ $USD$
> - Día 2: $3^2 = 9$ $USD$
> - Día 3: $3^3 = 27$ $USD$
> ✅ **Total**: $39$ $USD$.
> *Este crecimiento exponencial es la base del interés compuesto en finanzas.*

---

## 5. Práctica Independiente

Pon a prueba tu precisión. Recuerda aplicar la jerarquía de operaciones en cada paso.

> [!abstract] 🟢 Nivel Fácil
> 1. $\sum_{i=1}^{3} 2i$
> 2. $\sum_{k=1}^{4} (k+2)$
> 3. $\sum_{j=1}^{3} 3j$
> 4. $\sum_{i=1}^{4} (i+1)$

> [!abstract] 🟡 Nivel Medio
> 1. $\sum_{k=1}^{3} (k^2 - 1)$
> 2. $\sum_{i=2}^{4} (i^2 + 2)$
> 3. $\sum_{j=0}^{3} 2^j$
> 4. $\sum_{k=3}^{5} (k^2 - k)$

> [!abstract] 🔴 Nivel Avanzado
> 1. $\sum_{i=1}^{3} \frac{i+1}{i}$
> 2. $\sum_{i=1}^{3} (i^3 - 2i)$
> 3. Ahorro total en $USD de 4 días si cada día ahorras $\frac{2^i}{2}$ dólares: $\sum_{i=1}^{4} \frac{2^i}{2}$.
> 4. $\sum_{i=1}^{4} \frac{i^2}{2}$

> [!success] ✅ Respuestas para el docente
> - **Fácil**: 1) $12$; 2) $18$; 3) $18$; 4) $14$.
> - **Medio**: 1) $11$; 2) $29$; 3) $15$; 4) $38$.
> - **Avanzado**: 1) $\frac{29}{6} \approx 4.83$; 2) $24$; 3) $15$ $USD$; 4) $15$.

---

## 6. Autoevaluación

> [!question] Pregunta 1 (Teórica)
> ¿Qué indica el número ubicado en la parte superior del símbolo $\Sigma$?
> > [!check] Respuesta
> > Indica el **límite superior**, que representa el último valor entero que la variable de control debe tomar antes de finalizar la operación.

> [!question] Pregunta 2 (Procedimental)
> Calcula mentalmente la sumatoria $\sum_{i=1}^{3} (i+10)$.
> > [!check] Respuesta
> > **Resultado: 33.** El proceso es: $(1+10) + (2+10) + (3+10) = 11 + 12 + 13 = 36$.

> [!question] Pregunta 3 (Aplicación $USD)
> Si una inversión diaria sigue la sumatoria $\sum_{i=1}^{2} 10i$ en dólares, ¿cuál es el monto total acumulado?
> > [!check] Respuesta
> > **30 USD.** Explicación: Reemplazamos $i$ por 1 y 2: $10(1) + 10(2) = 10 + 20 = 30$.

---

## 7. Cierre y Conexión

> [!tip] 💡 En la próxima clase
> El "método largo" que usamos hoy es útil para pocos términos. Sin embargo, ¿qué pasaría si tuviéramos que sumar del 1 al 1,000? En la siguiente sesión descubriremos las **Fórmulas Especiales de Sumatoria** para resolver problemas masivos en segundos.

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | | [[Clase 03|Clase 03 ➡]]