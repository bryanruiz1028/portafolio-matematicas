# Clase 02 — Jerarquía de las operaciones | Ejemplo 4 + Jerarquía de las operaciones | Ejemplo 6 + Conviértete en el mejor en matemáticas

#algebra #jerarquadelasop

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 3

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | | [[Clase 03|Clase 03 ➡]]

---

## RELEVANCIA Y APLICACIONES

La jerarquía de las operaciones es el cimiento de la precisión matemática; sin ella, una misma expresión podría tener múltiples interpretaciones erróneas. Según el Profe Alex, dominar este orden estricto garantiza que cualquier cálculo, por complejo que sea, resulte en un valor unívoco y exacto.

*   **💵 Aplicación USD:** En la gestión financiera, calcular una factura con descuentos e impuestos requiere jerarquía. Por ejemplo, si tienes $5$ artículos de $\sqrt{16}$ USD, sumas $3$ recargos de $(5-8)^2$ USD y aplicas un ajuste de $\sqrt{3^2 \times 2 + 7}$ USD, el orden determina si tu saldo es correcto o una pérdida.
*   **🏗️ Aplicación práctica:** En la ingeniería y arquitectura, las fórmulas de resistencia de materiales dependen de potencias y raíces. Un error al sumar antes de elevar al cuadrado puede comprometer la estabilidad de toda una estructura.
*   **📊 Situación cotidiana:** Al dividir gastos grupales que incluyen compras individuales (potencias) y reembolsos (restas), la jerarquía permite que la repartición de dinero sea justa y transparente para todos los participantes.

---

## CONCEPTO CLAVE

> [!note] 📌 ¿Qué es Jerarquía de las operaciones?
> Es el conjunto de reglas e instrucciones que determinan el orden estricto en el que deben ejecutarse las operaciones en una expresión combinada. Su propósito pedagógico es estandarizar los procesos para que cualquier persona, en cualquier lugar, obtenga el mismo resultado.

> [!warning] ⚠️ Error común
> ❌ **Incorrecto:** Resolver de izquierda a derecha de forma lineal sin considerar el tipo de operación (ej. sumar antes de multiplicar).
> ✅ **Correcto:** Priorizar los niveles superiores (Potencias/Raíces) antes que los inferiores (Sumas/Restas), respetando siempre los signos de agrupación.

> [!tip] 💡 Truco para recordarlo
> La clave es la estrategia de **"adentro hacia afuera"**. Siempre comienza resolviendo lo que está más profundamente anidado en los signos de agrupación y escala hacia las operaciones más externas.

---

## PROCEDIMIENTO PASO A PASO

Para abordar cualquier ejercicio, te sugiero seguir esta ruta de resolución lógica:

```text
PASO 0 → Separar la expresión en términos (usando los signos + y - fuera de agrupaciones).
PASO 1 → Resolver Signos de agrupación (paréntesis (), corchetes [], llaves {}).
PASO 2 → Resolver Potencias y raíces.
PASO 3 → Resolver Multiplicaciones y divisiones.
PASO 4 → Resolver Sumas y restas (el paso final).
```

---

## SECCIÓN DE EJEMPLOS RESUELTOS

### Ejemplo 1 (Caso Básico)
**Ejercicio:** $3 \times 5^2 + 2(3+4) - 5\sqrt{3^2 + 8 \times 2}$

**Ruta de Solución:**
1.  **Separación en términos:** Identificamos tres términos principales separados por los signos $+$ y $-$.
2.  **Término 1 ($3 \times 5^2$):** Primero la potencia: $5^2 = 25$. Luego la multiplicación: $3 \times 25 = \mathbf{75}$.
3.  **Término 2 ($2(3+4)$):** Primero la operación interna: $3+4 = 7$. Luego multiplicamos: $2 \times 7 = \mathbf{14}$.
4.  **Término 3 ($5\sqrt{3^2 + 8 \times 2}$):** Dentro de la raíz resolvemos la potencia $3^2 = 9$ y la multiplicación $8 \times 2 = 16$. Sumamos $9+16 = 25$. La raíz es $\sqrt{25} = 5$. Finalmente: $5 \times 5 = \mathbf{25}$.
5.  **Verificación Final:** Sumamos y restamos los resultados de cada término: $75 + 14 - 25 = \mathbf{64}$.

---

### Ejemplo 2 (Caso con Signos)
**Ejercicio:** $5\sqrt{16} + 3(5-8)^2 + \sqrt{3^2 \times 2 + 7}$

**Ruta de Solución:**
1.  **Separación en términos:** Tenemos tres bloques definidos por las sumas.
2.  **Término 1:** Resolvemos la raíz $\sqrt{16} = 4$. Multiplicamos $5 \times 4 = \mathbf{20}$.
3.  **Término 2:** Resolvemos el paréntesis $(5-8) = -3$. Elevamos al cuadrado: $(-3)^2 = 9$. Luego $3 \times 9 = \mathbf{27}$.
4.  **Término 3:** Dentro de la raíz: $3^2 = 9$, luego $9 \times 2 = 18$ y $18+7 = 25$. La $\sqrt{25} = \mathbf{5}$.
5.  **Verificación Final:** $20 + 27 + 5 = \mathbf{52}$.

> [!tip] 🔍 Pro-Tip: El poder de los paréntesis
> Fíjate en la diferencia que explica el Profe Alex:
> *   $(-3)^2 = (-3) \times (-3) = \mathbf{9}$ (El signo está dentro y se eleva).
> *   $-3^2 = -(3 \times 3) = \mathbf{-9}$ (Solo el número se eleva, el signo se mantiene).

---

### Ejemplo 3 (Caso Avanzado)
**Ejercicio:** $6 \times 3^2 - \{5 - [4 \times 3(-12)(-1) - 3 \times 4^2]\}$

**Ruta de Solución:**
1.  **Separación en términos:** Término 1 ($6 \times 3^2$) y Término 2 (toda la expresión dentro de las llaves $\{\}$).
2.  **Término 1:** $6 \times 9 = \mathbf{54}$.
3.  **Análisis de Signos de Agrupación:** Debemos resolver el corchete `[]` antes que la llave `{}`.
    *   **Dentro del Corchete:** Tenemos dos sub-términos:
        *   Multiplicación múltiple: $4 \times 3 \times (-12) \times (-1) = \mathbf{144}$.
        *   Potencia y multiplicación: $3 \times 4^2 = 3 \times 16 = \mathbf{48}$.
        *   Resultado del corchete: $[144 - 48] = \mathbf{96}$.
4.  **Resolución de la Llave:** Ahora resolvemos $\{5 - [96]\} = \mathbf{-91}$.
5.  **Verificación Final:** $54 - (-91) = 54 + 91 = \mathbf{145}$.

---

### Ejemplo 4 (Aplicación USD)
**Problema:** Una constructora calcula el costo de materiales mediante la expresión: $5\sqrt{16} + 3(5-8)^2 + \sqrt{3^2 \times 2 + 7}$. Si el resultado final debe multiplicarse por $1,000$ USD para obtener el presupuesto real, ¿a cuánto asciende la obra?

*   **Análisis:** Identificamos que la estructura matemática es idéntica al Ejemplo 2.
*   **Cálculo:** Siguiendo la jerarquía, obtenemos el valor base de $52$.
*   **Resultado:** $52 \times 1,000 = \mathbf{52,000}$ **USD**.

---

## EJERCICIOS PARA EL ESTUDIANTE

### 🟢 Fácil (Nivel Inicial)
1.  $10 + 2 \times 5$
2.  $(6 - 4)^3 + 5$
3.  $\sqrt{25} + 3^2$
4.  $20 \div 2 + 4 \times 2$

### 🟡 Medio (Práctica del Video 4)
1.  $3 - (2 \times 4^2 - 5^2) + 7 \times 3\sqrt{29+35}$
2.  $(3 + 5^2 - 8 \times 4)^2 - (3 - 5)(4 - 2^2) + 1$

### 🔴 Avanzado (Práctica del Video 6)
1.  $5 + 2 \times 4^2 - \{7 \times 3 - 2[3 \times 2^4 - 2^5] + [4 \times 3^2 + (4 \times 5^2 - (3^2 \times 2^3 - 2 \times 6 \times 4)) - 3]\}$

> [!info] 💡 Estrategia para el nivel avanzado
> No te dejes intimidar por la extensión. Aplica la técnica de **Separación en Términos** incluso dentro de los paréntesis más pequeños. Resuelve primero $(3^2 \times 2^3 - 2 \times 6 \times 4)$ y avanza hacia afuera.

> [!success] ✅ Respuestas
> **Fácil:** 1) $20$ | 2) $13$ | 3) $14$ | 4) $18$
> **Medio:** 1) $122$ | 2) $17$
> **Avanzado:** 1) $52$

---

## MINI-PRUEBA DE AUTOEVALUACIÓN

**1. Según la jerarquía, ¿cuál es el orden correcto de ejecución?**
a) Sumas, Multiplicaciones, Potencias, Paréntesis.
b) Paréntesis, Multiplicaciones, Potencias, Sumas.
c) Paréntesis, Potencias, Multiplicaciones, Sumas.
d) Raíces, Paréntesis, Restas, Divisiones.
*Respuesta: **c)**. Los signos de agrupación mandan, seguidos por el nivel de exponentes, luego productos y finalmente adiciones.*

**2. ¿Cuál es el valor de $\sqrt{3^2 + 4^2}$?**
a) $7$
b) $5$
c) $25$
d) $14$
*Respuesta: **b)**. Primero resolvemos las potencias internas ($9 + 16 = 25$) y al final la raíz ($\sqrt{25} = 5$).*

**3. Si un presupuesto en USD se define por $2 \times 10 - 5$, ¿qué estamos calculando?**
a) El doble de la diferencia entre 10 y 5.
b) La resta de 5 al producto de 2 por 10.
c) La suma de 2 y 10, menos 5.
d) El producto de 2 por la resta de 10 y 5.
*Respuesta: **b)**. La multiplicación tiene prioridad sobre la resta, por lo que primero calculamos el total ($20$) y luego restamos el gasto ($5$).*

---

## CIERRE Y NAVEGACIÓN FINAL

> [!tip] 💡 En la próxima clase
> Llevaremos la jerarquía al siguiente nivel integrando **fracciones y números racionales**. Veremos cómo los signos de agrupación afectan a los denominadores y numeradores en operaciones combinadas.

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | | [[Clase 03|Clase 03 ➡]]