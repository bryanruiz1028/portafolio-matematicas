# Clase 08 — Raíz de una Raíz e Introducción a la Racionalización

#algebra #radicalizacion

[[Clase 07|⬅ Clase 07]] | [[00 - Índice del curso|Índice]] | [[Clase 09|Clase 09 ➡]]

> [!info] 🌍 Relevancia y aplicaciones
> La simplificación de raíces nos permite manejar cálculos complejos con precisión absoluta antes de recurrir a los decimales. En el mundo real, esto es fundamental para:
> 
> - 💵 **USD:** Imagina repartir un presupuesto de inversión representado por la raíz cuadrada de la raíz cúbica de $1,000,000. Simplificar la expresión nos permite conocer el monto exacto antes de ejecutar el gasto.
> - 🏗️ **Construcción:** En ingeniería, el cálculo de tensiones en vigas depende de dimensiones con potencias y raíces anidadas. Reducir estas expresiones asegura la estabilidad estructural.
> - 📊 **Cotidiano:** Simplificación de fórmulas de crecimiento poblacional o interés compuesto, donde las tasas se aplican sobre periodos que son raíces de otros periodos.

> [!note] 📌 ¿Qué es Raíz de una Raíz?
> Para un estudiante de 12 años, podemos decir que tener una raíz dentro de otra es como si las "fuerzas" de las raíces se unieran para actuar sobre un mismo número. En lugar de resolverlas por separado, multiplicamos sus índices para crear una sola raíz que haga el trabajo de ambas.
> 
> **Regla Matemática:**
> Se conserva la cantidad subradical (la base) y se multiplican los índices de los radicales para obtener un único índice resultante.
> 
> > [!warning] ⚠️ Error común
> > El error más frecuente es **sumar** los índices en lugar de **multiplicarlos**. Recuerda que los índices de las raíces funcionan bajo reglas multiplicativas cuando están anidados, no aditivas.
> 
> > [!tip] 💡 Truco para recordarlo
> > "Raíz sobre raíz, los índices multiplico y soy feliz".

### Procedimiento paso a paso

```text
1. Identificar los índices de todas las raíces (si no hay número escrito, el índice es 2).
2. Multiplicar los índices entre sí para definir el nuevo radical único.
3. Simplificar el exponente de la base con el nuevo índice (dividiendo ambos por el mismo número) si es posible.
4. Si hay factores externos atrapados entre raíces, introducirlos a la raíz más interna elevándolos al índice de esta antes de multiplicar los índices de las raíces.
```

### Bloques de ejemplos prácticos

> [!example] Ejemplo 1: Operación Básica
> **Problema:** Resuelve $\sqrt[3]{\sqrt{x}}$
> - **Paso 1:** Identificamos índices. La raíz externa es 3 y la interna es 2 (raíz cuadrada).
> - **Paso 2:** Multiplicamos: $3 \times 2 = 6$.
> - **Resultado:** $\sqrt[6]{x}$

> [!example] Ejemplo 2: Simplificación de Exponente
> **Problema:** Resuelve $\sqrt[3]{\sqrt[2]{a^2}}$
> - **Paso 1:** Índice resultante: $3 \times 2 = 6$. Obtenemos $\sqrt[6]{a^2}$.
> - **Paso 2:** Simplificamos el índice (6) y el exponente (2) sacando mitad a ambos ($6 \div 2 = 3$ y $2 \div 2 = 1$).
> - **Resultado:** $\sqrt[3]{a}$

> [!example] Ejemplo 3: Factor Interno (Anidado Complejo)
> **Problema:** Resolver $\sqrt{x \sqrt[3]{x}}$
> - **Paso 1:** Introducimos la $x$ externa en la raíz cúbica elevándola al índice 3: $\sqrt{\sqrt[3]{x^3 \cdot x}}$.
> - **Paso 2:** Simplificamos la cantidad subradical sumando exponentes: $\sqrt{\sqrt[3]{x^4}}$.
> - **Paso 3:** Multiplicamos índices: $2 \times 3 = 6$. Resultado parcial: $\sqrt[6]{x^4}$.
> - **Paso 4:** Simplificamos sacando mitad al índice y al exponente.
> - **Resultado:** $\sqrt[3]{x^2}$

> [!example] Ejemplo 4: Aplicación USD
> **Problema:** Calcular el costo de un material cuyo gramo vale $\sqrt{\sqrt{625}}$ USD.
> - **Paso 1:** Multiplicamos índices: $2 \times 2 = 4$, obteniendo $\sqrt[4]{625}$.
> - **Paso 2:** Descomponemos 625 en factores primos: $625 = 5^4$.
> - **Paso 3:** La expresión es $\sqrt[4]{5^4}$. Como el índice y el exponente son iguales, se cancelan.
> - **Resultado:** 5 USD.

---

### Introducción a la Racionalización

Racionalizar es el proceso de **eliminar los radicales del denominador** de una fracción para facilitar las operaciones. Según el Profe Alex, "para eliminar una raíz obligatoriamente debe estar el exponente igual al índice de la raíz". Esta es la "llave" que abre el candado del radical (ejemplo: $\sqrt[5]{3^5} = 3$).

Existen cuatro tipos principales de expresiones a racionalizar:
1. Denominador con un solo término de raíz cuadrada ($\sqrt{x}$).
2. Denominador con un solo término de raíz de índice mayor a 2 ($\sqrt[n]{x^m}$).
3. Denominador con dos términos (donde uno o ambos tienen raíz).
4. Denominador con tres términos.

---

### Ejercicios para el estudiante

> [!abstract] 🟢 Nivel Fácil: Multiplicación Directa
> 1. $\sqrt{\sqrt{\sqrt{x}}}$
> 2. $\sqrt[3]{\sqrt[4]{y}}$
> 3. $\sqrt[5]{\sqrt[3]{a}}$
> 4. $\sqrt[2]{\sqrt[5]{b}}$

> [!abstract] 🟡 Nivel Medio: Simplificación
> 1. $\sqrt[4]{\sqrt[3]{x^6}}$
> 2. $\sqrt[2]{\sqrt[3]{a^2}}$
> 3. $\sqrt[5]{\sqrt[2]{b^{10}}}$
> 4. $\sqrt[3]{\sqrt[3]{z^9}}$

> [!abstract] 🔴 Nivel Avanzado: Aplicación Financiera (USD)
> 1. Una ganancia se define como $\sqrt{\sqrt{81}}$ USD. Simplifica.
> 2. El costo de un activo es $\sqrt[3]{\sqrt{64}}$ USD. Calcula el valor real.
> 3. Un bono rinde $\sqrt{\sqrt{\sqrt{256}}}$ USD. Simplifica a un número entero.
> 4. Se debe repartir una deuda de $\sqrt[3]{\sqrt[2]{a^6}}$ USD entre "$a$" personas. ¿Cuánto paga cada una?

> [!success] Respuestas para el Docente
> **Fácil:** 1. $\sqrt[8]{x}$ | 2. $\sqrt[12]{y}$ | 3. $\sqrt[15]{a}$ | 4. $\sqrt[10]{b}$
> **Medio:** 1. $\sqrt{x}$ | 2. $\sqrt[3]{a}$ | 3. $b$ | 4. $z$
> **Avanzado:** 
> 1. 3 USD ($\sqrt[4]{3^4} = 3$)
> 2. 2 USD ($\sqrt[6]{2^6} = 2$)
> 3. 2 USD ($\sqrt[8]{2^8} = 2$)
> 4. 1 USD (Cálculo: $\sqrt[6]{a^6} = a$. Luego, la deuda $a$ dividida entre $a$ personas: $a / a = 1$).

---

### Autoevaluación y Cierre

> [!question] Pregunta Conceptual
> ¿Qué operación se debe realizar con los índices de las raíces cuando una se encuentra dentro de otra?
> *Respuesta: Multiplicación.*

> [!question] Pregunta Procedimental
> ¿Cómo se simplifica la expresión $\sqrt[10]{x^5}$?
> *Respuesta: Dividiendo el índice y el exponente por su máximo común divisor (5), resultando en $\sqrt{x}$.*

> [!question] Pregunta de Aplicación
> Si un producto cuesta $\sqrt{\sqrt{16}}$ USD, ¿cuál es su precio final?
> *Respuesta: 2 USD.*

> [!tip] 💡 En la próxima clase
> Utilizaremos estos conocimientos sobre índices y exponentes para **racionalizar denominadores con un solo término**. Aprenderemos a multiplicar por el factor necesario para que el exponente alcance al índice y así eliminar la raíz.

[[Clase 07|⬅ Clase 07]] | [[00 - Índice del curso|Índice]] | [[Clase 09|Clase 09 ➡]]