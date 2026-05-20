# Clase 04 — Resta de polinomios

#algebra #polinomios #resta

> [!info] 🧭 Navegación
> [Anterior (Clase 03)](https://example.com/clase03) | [Índice](https://example.com/indice) | [Siguiente (Fin del curso)](https://example.com/final)

---

> [!info] 🌍 Relevancia y aplicaciones
> La resta de polinomios es la herramienta matemática que nos permite cuantificar el cambio. No se trata solo de números; se trata de responder preguntas vitales como: ¿Cuánto más ganamos hoy que ayer? o ¿Qué espacio exacto queda libre en un plano arquitectónico tras añadir una estructura? Dominar esta operación te permite determinar variaciones, diferencias netas y saldos reales en cualquier sistema expresado mediante variables.

### Ejemplos de uso real
*   **💵 Finanzas:** Si tus ingresos brutos son un polinomio y tus gastos otro, la resta algebraica te entrega el polinomio de la **ganancia neta**.
*   **🏗️ Geometría:** Para calcular el área de una región sombreada, simplemente restamos el polinomio del área menor al polinomio del área mayor.
*   **📊 Comparación:** Es fundamental para comparar ritmos de crecimiento poblacional o niveles de inventario en distintas etapas del tiempo.

---

> [!note] 📌 ¿Cómo se restan polinomios?
> Restar polinomios consiste en sumar al **minuendo** (la cantidad original) el opuesto del **sustrayendo** (la cantidad que quita). 
> 
> **Regla de oro del lenguaje:**
> *   El **sustrayendo** es SIEMPRE la expresión que sigue inmediatamente a la palabra **"restar"**, sin importar el orden en que aparezca en la frase.
> *   Si el ejercicio dice: *"De $A$ restar $B$"*, el sustrayendo es $B$.
> *   Si el ejercicio dice: *"Restar $B$ de $A$"*, el sustrayendo sigue siendo $B$.

> [!warning] ⚠️ Error común
> Muchos estudiantes cometen el error de cambiar únicamente el signo del primer término del sustrayendo. ¡Cuidado! El signo menos afecta a **todo** el polinomio.
> *   **Incorrecto:** $(3x^2 + 2x) - (x^2 - 5x) \neq 3x^2 + 2x - x^2 - 5x$
> *   **Correcto:** $(3x^2 + 2x) - (x^2 - 5x) = 3x^2 + 2x - x^2 + 5x$

> [!tip] 💡 Truco para recordarlo
> 1. **El Multiplicador Invisible:** Imagina que el signo "$-$" antes de un paréntesis es un **$-1$** que se distribuye. Este tiene el "poder" de invertir el signo de cada término dentro del paréntesis.
> 2. **El "1" Invisible:** En álgebra, si el resultado de un coeficiente es $1$ (por ejemplo, $1x$ o $-1a$), el "1" no se escribe. Escribimos simplemente $x$ o $-a$.

---

### Procedimiento paso a paso

```text
PASO 1: Identificar el minuendo y el sustrayendo (el que sigue a "restar").
PASO 2: Escribir la operación con paréntesis: (Minuendo) - (Sustrayendo).
PASO 3: Eliminar los paréntesis cambiando el signo de TODOS los términos del sustrayendo.
PASO 4: Agrupar términos semejantes y ordenar de mayor a menor grado.
```

---

### Ejemplos aplicados

> [!example] Ejemplo 1: Binomios básicos
> **Operación:** $(5x + 3) - (2x + 1)$
> 1. **Planteamiento:** $(5x + 3) - (2x + 1)$
> 2. **Eliminación de paréntesis:** $5x + 3 - 2x - 1$
> 3. **Agrupación:** $(5x - 2x) + (3 - 1)$
> 4. **Resultado final:** $3x + 2$

> [!example] Ejemplo 2: Uso de las palabras "Restar" y "De"
> **Problema:** Restar $(8m + 5n - 2)$ de $(6m - 2n + 5)$
> 1. **Identificación:** El sustrayendo es el que sigue a "restar", es decir, $(8m + 5n - 2)$.
> 2. **Planteamiento con paréntesis:** $(6m - 2n + 5) - (8m + 5n - 2)$
> 3. **Cambio de signos:** $6m - 2n + 5 - 8m - 5n + 2$
> 4. **Reducción:** 
>    - $6m - 8m = -2m$
>    - $-2n - 5n = -7n$
>    - $5 + 2 = 7$
> 5. **Resultado final:** $-2m - 7n + 7$

> [!example] Ejemplo 3: Grado mayor y términos independientes
> **Operación:** $(-3x^2 - 2x + 5) - (5x^2 - 3x - 4)$
> 1. **Planteamiento:** $(-3x^2 - 2x + 5) - (5x^2 - 3x - 4)$
> 2. **Cambio de signos:** $-3x^2 - 2x + 5 - 5x^2 + 3x + 4$
> 3. **Agrupación por grado:**
>    - $(-3x^2 - 5x^2) = -8x^2$
>    - $(-2x + 3x) = 1x \rightarrow x$ (Aplicamos regla del "1" invisible)
>    - $(5 + 4) = 9$
> 4. **Resultado final:** $-8x^2 + x + 9$

> [!example] Ejemplo 4: Aplicación financiera ($USD)
> Los ingresos de un negocio son $(3x^2 + 5x + 10)$ y sus gastos son $(x^2 + 2x + 4)$. ¿Cuál es la ganancia neta?
> 1. **Planteamiento:** $(3x^2 + 5x + 10) - (x^2 + 2x + 4)$
> 2. **Eliminación de paréntesis:** $3x^2 + 5x + 10 - x^2 - 2x - 4$
> 3. **Operación de términos:**
>    - $3x^2 - x^2 = 2x^2$
>    - $5x - 2x = 3x$
>    - $10 - 4 = 6$
> 4. **Resultado:** La ganancia es $2x^2 + 3x + 6$

---

### Ejercicios para el estudiante

> [!abstract] 🟢 Nivel Fácil: Binomios lineales
> 1. $(6x + 4) - (2x + 1)$
> 2. $(10y + 5) - (3y + 2)$
> 3. $(4a + 8) - (a + 4)$
> 4. $(7b - 2) - (2b - 1)$

> [!abstract] 🟡 Nivel Medio: Trinomios con signos negativos
> 1. $(8a - 3b + 4) - (3a - 2b - 5)$
> 2. $(5x^2 - 2x + 3) - (2x^2 + x - 1)$
> 3. $(4m + 3n - 6) - (-2m + n + 2)$
> 4. $(x^2 - 5x + 4) - (x^2 - 2x - 3)$

> [!abstract] 🔴 Nivel Avanzado: Aplicación y fracciones
> 1. Hallar la diferencia entre el área $A = 10x^2 + 5x$ y el área $B = 4x^2 + 2x$.
> 2. Realizar la operación: $(\frac{3}{4}x) - (\frac{1}{2}x)$.
> 3. Restar $(2a - 5)$ de $(\frac{5}{6}a + 10)$.
> 4. Simplificar: $(x^2 + \frac{1}{2}x) - (\frac{1}{2}x^2 + \frac{1}{4}x)$.

---

### Respuestas y autoevaluación

> [!success] Soluciones breves
> **Fácil:** 1) $4x + 3$ | 2) $7y + 3$ | 3) $3a + 4$ | 4) $5b - 1$
> **Medio:** 1) $5a - b + 9$ | 2) $3x^2 - 3x + 4$ | 3) $6m + 2n - 8$ | 4) $-3x + 7$
> **Avanzado:** 1) $6x^2 + 3x$ | 2) $\frac{1}{4}x$ | 3) $-\frac{7}{6}a + 15$ | 4) $\frac{1}{2}x^2 + \frac{1}{4}x$

#### Mini-prueba de salida

> [!question] Pregunta 1
> ¿Cuál es el resultado de $(4x^2 + 3x - 2) - (x^2 + x - 5)$?
> a) $3x^2 + 2x - 7$
> b) $3x^2 + 2x + 3$
> c) $5x^2 + 4x - 7$
> d) $3x^2 + 4x + 3$
> **Respuesta:** **b**. Al cambiar los signos del sustrayendo tenemos $-x^2 - x + 5$. Sumando: $4x^2 - x^2 = 3x^2$; $3x - x = 2x$; $-2 + 5 = 3$.

> [!question] Pregunta 2
> Resuelve la resta: $(7a + 2b) - (3a - 5b)$.
> **Respuesta:** $4a + 7b$. Recuerda que el $-5b$ cambia su signo a $+5b$ por efecto del negativo exterior.

> [!question] Pregunta 3
> Problema de inventario: Los ingresos son $(5x + 20)$ y los gastos son $(2x + 8)$. ¿Cuál es la utilidad?
> **Respuesta:** $3x + 12$.

---

> [!tip] 💡 Has completado el Bloque 2
> ¡Felicidades! Has dominado la resta de polinomios y el manejo de los signos en el sustrayendo. Esta es la base para resolver ecuaciones complejas. En la siguiente clase, subiremos de nivel con la **multiplicación de expresiones algebraicas**.

> [!info] 🧭 Navegación
> [Anterior (Clase 03)](https://example.com/clase03) | [Índice](https://example.com/indice) | [Siguiente (Fin del curso)](https://example.com/final)