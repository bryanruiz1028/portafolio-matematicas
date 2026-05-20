# Clase 07 — Propiedades de la potenciación | Propiedades combinadas | Ejemplo 5 + Propiedades de la potenciación | Propiedades combinadas Ejemplo 7 + Potencias con base negativa

`[[Clase 06]] | [[00 - Índice del curso]]`

---

## 1. Relevancia y Aplicaciones

Dominar la simplificación de potencias y el manejo de bases negativas es fundamental para el álgebra avanzada, ya que permite reducir expresiones complejas a formas mínimas y precisas. Sin esta base, los errores de signo y la acumulación de números masivos dificultan la resolución de ecuaciones y funciones de mayor nivel.

*   💵 **[Aplicación USD]:** El crecimiento exponencial de una inversión o deuda en dólares se representa mediante potencias; comprender cómo descomponer la base permite calcular intereses acumulados de forma más eficiente sin usar calculadoras complejas.
*   🏗️ **[Aplicación práctica]:** En el diseño estructural, el cálculo de áreas o volúmenes en estructuras complejas se facilita descomponiendo medidas en sus factores primos para simplificar las fórmulas de resistencia.
*   📊 **[Situación cotidiana]:** Las potencias se utilizan para medir la escala de fenómenos naturales o digitales, donde un pequeño cambio en el exponente representa una diferencia masiva en la magnitud de los datos.

---

## 2. Concepto Clave y Errores Comunes

### Regla de oro para signos
La regla fundamental para entender bases negativas depende de un solo elemento: el paréntesis. Si hay **paréntesis**, el signo negativo forma parte de la base y se multiplica tantas veces como indique el exponente. Si **no hay paréntesis**, el signo negativo es externo y no se ve afectado por la potencia.

> [!warning] ⚠️ Error común: El efecto del paréntesis
> Basado en las lecciones del "profe Alex", observa la diferencia crucial:
> *   $(-3)^2 = (-3) \cdot (-3) = 9$ (El signo se repite, el resultado es positivo).
> *   $-3^2 = -(3 \cdot 3) = -9$ (El signo negativo está "afuera esperando", solo el 3 se eleva).

> [!tip] 💡 Truco para recordarlo
> **"Pareja positiva, impar negativo"**: Si la base negativa tiene paréntesis y el exponente es **par** (2, 4, 6...), el resultado será **positivo**. Si el exponente es **impar** (3, 5, 7...), el resultado conservará el signo **negativo**.

---

## 3. Procedimiento Paso a Paso

Para resolver operaciones combinadas complejas, siga esta metodología sistemática:

1.  **Descomposición de bases:** Convierta cualquier base que no sea un número primo (como 6, 12, 9, 10, 15) en sus factores primos. Ejemplo: $6 = 2 \cdot 3$.
2.  **Distribución y Potencia de Potencia:** Aplique el exponente a cada factor obtenido. Si una base ya tenía exponente, multiplíquelos (ej. $(2^2)^3 = 2^6$).
3.  **Agrupación de bases iguales:** En el numerador y denominador por separado, sume los exponentes de las bases que sean idénticas.
4.  **Simplificación final:** Reste los exponentes de las bases iguales (exponente de arriba menos exponente de abajo). Si el exponente resultante es negativo, mueva la potencia al denominador para mantenerlo positivo.

---

## 4. Ejemplos Resueltos

### Ejemplo 1: Diferencia básica de signos
*   $(-3)^2 = (-3) \cdot (-3) = 9$
*   $-3^2 = -(3 \cdot 3) = -9$

### Ejemplo 2: Signo externo complejo
Para resolver $-(-3)^2$:
1.  Mantenemos el signo externo: $- (...)$
2.  Resolvemos el paréntesis: $(-3) \cdot (-3) = 9$
3.  Resultado final: $- (9) = -9$

### Ejemplo 3: Simplificación avanzada (Ejemplo 7)
Simplificar: $\frac{6^3 \cdot 12^4 \cdot 9^5}{2^4 \cdot 10^3 \cdot 15^2}$

1.  **Descomponer en primos:**
    *   $6^3 = (2 \cdot 3)^3 = 2^3 \cdot 3^3$
    *   $12^4 = (2^2 \cdot 3)^4 = 2^8 \cdot 3^4$
    *   $9^5 = (3^2)^5 = 3^{10}$
    *   $10^3 = (2 \cdot 5)^3 = 2^3 \cdot 5^3$
    *   $15^2 = (3 \cdot 5)^2 = 3^2 \cdot 5^2$
2.  **Agrupar Numerador:** $2^{3+8} \cdot 3^{3+4+10} = 2^{11} \cdot 3^{17}$
3.  **Agrupar Denominador:** $2^{4+3} \cdot 3^2 \cdot 5^{3+2} = 2^7 \cdot 3^2 \cdot 5^5$
4.  **Restar exponentes:**
    *   Para la base 2: $2^{11-7} = 2^4$
    *   Para la base 3: $3^{17-2} = 3^{15}$
    *   Para la base 5: Queda en el denominador como $5^5$.
    *   **Resultado:** $\frac{2^4 \cdot 3^{15}}{5^5}$

### Ejemplo 4: Aplicación USD
Un capital crece según el factor $6^4$. Descomponiendo la base podemos simplificar el cálculo mental del monto en USD:
*   $6^4 = (2 \cdot 3)^4 = 2^4 \cdot 3^4$
*   $2^4 = 16$ y $3^4 = 81$
*   $16 \cdot 81 = 1296$. El factor multiplicador es 1296.

---

## 5. Ejercicios y Autoevaluación

### Niveles de Dificultad
*   🟢 **Fácil:**
    1. $(-4)^2$
    2. $-4^2$
    3. $(-2)^4$
    4. $-(-3)^2$
*   🟡 **Medio:**
    1. Simplificar $6^2 \cdot 3^3$
    2. Simplificar $9^2 \cdot 3^2$
    3. Simplificar $12^2 \cdot 2^2$
    4. Reducir $\frac{6^3}{2^2}$
*   🔴 **Avanzado:**
    1. $\frac{10^2 \cdot 15^2}{5^3}$
    2. $\frac{27^2 \cdot 3^4}{9^3}$
    3. $\frac{6^4 \cdot 12^2}{2^6 \cdot 3^5}$
    4. $\frac{10^3 \cdot 25}{5^4 \cdot 2^2}$

> [!success] ✅ Respuestas para el docente
> **Fácil:** 1) 16, 2) -16, 3) 16, 4) -9.
> **Medio:** 1) $2^2 \cdot 3^5$, 2) $3^6$, 3) $2^6 \cdot 3^2$, 4) $2 \cdot 3^3$.
> **Avanzado:** 1) $180$, 2) $81$, 3) $12$, 4) $10$.
> **Mini-prueba:** 1) Positivo, 2) Se restan, 3) 1000 ($2^3 \cdot 5^3 = (2 \cdot 5)^3 = 10^3$).

### Mini-prueba de autoevaluación
1.  Si tenemos $(-5)^{10}$, ¿el resultado es positivo o negativo?
2.  ¿Qué operación se realiza con los exponentes al simplificar $\frac{2^{10}}{2^3}$?
3.  Si una transacción de $10 USD se multiplica por un factor de $2^3 \cdot 5^3$, ¿cuál es el factor total?

---

## 6. Cierre y Conexión

La capacidad de descomponer números en sus **factores primos** es la herramienta maestra para el siguiente bloque del curso: **Simplificación de fracciones algebraicas y radicación**. Sin dominar esta técnica, el álgebra superior se vuelve innecesariamente difícil.

`[[Clase 06]] | [[00 - Índice del curso]]`

---