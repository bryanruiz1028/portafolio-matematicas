# Clase 16 — Converting a Pure Repeating Decimal to a Fraction | Example 2
#algebra #convertingapure

Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 16 de 22

> [!info] 🧭 Navegación
> ⬅️ [[Clase 15 — Converting a Pure Repeating Decimal to a Fraction | Example 1]] | [[00 - Índice del curso|Índice]] | [[Clase 17 — Converting a Mixed Repeating Decimal to a Fraction]] ➡️

---

## ¿POR QUÉ ES IMPORTANTE ESTA CLASE?

La capacidad de transformar un **decimal periódico** en una **fracción** es vital para garantizar la **precisión matemática**. Mientras que los decimales infinitos obligan a realizar redondeos que acumulan errores, las fracciones preservan el valor exacto en cualquier cálculo complejo.

*   **💵 Aplicación USD:** En el mundo financiero, un precio que fluye perpetuamente como $9.9\overline{9}$ se procesa matemáticamente como un valor entero exacto ($10).
*   **🏗️ Aplicación práctica:** En ingeniería y construcción, el uso de la **fracción** irreducible (como $\frac{15}{11}$) permite cortes y ensambles exactos que un decimal truncado arruinaría.
*   **📊 Situación cotidiana:** Al repartir presupuestos o cuentas donde aparecen **cifras** infinitas, la conversión a **fracción** asegura que el balance final sea de cero, sin perder centavos en el camino.

---

## CONCEPTO CLAVE

Un **Decimal Periódico Puro** es aquel número decimal donde el **periodo** (el grupo de **cifras** que se repite infinitamente) comienza inmediatamente después de la **coma decimal**. En este tipo de números, no hay valores entre la coma y la barra del **periodo**.

> [!warning] ⚠️ Error común
> El fallo más frecuente es olvidar restar la **parte entera** en el **numerador**.
> *   **Incorrecto:** Para $1.\overline{36}$, escribir simplemente $\frac{136}{99}$.
> *   **Correcto:** Se debe restar la **parte entera** (el 1) antes de definir el **numerador**: $(136 - 1) = 135$.

> [!tip] 💡 Truco para recordarlo
> El **denominador** siempre se construye con nueves. La cantidad de nueves es igual al número de **cifras** que tenga el **periodo**. Por ejemplo, si el **periodo** es "36" (dos **cifras**), el **denominador** será 99.

---

## PROCEDIMIENTO PASO A PASO

Para realizar la conversión de forma técnica y exacta, sigue estos pasos:

```text
PASO 1: Escribir el número completo (sin coma decimal y sin barra de periodo).
PASO 2: Restar la parte entera (lo que está a la izquierda de la coma).
PASO 3: Colocar como denominador tantos nueves como cifras tenga el periodo.
PASO 4: Simplificar la fracción resultante hasta su mínima expresión.
```

> [!tip] 💡 Verifica tu resultado
> Siempre puedes comprobar tu trabajo: divide el **numerador** entre el **denominador** en una calculadora; el resultado debe ser exactamente el decimal periódico original.

---

## EJEMPLOS DESARROLLADOS

> [!example] Ejemplo 1: Caso Básico ($1.\overline{36}$)
> 1.  **Número completo:** 136.
> 2.  **Restar parte entera:** $136 - 1 = 135$.
> 3.  **Denominador:** 99 (el **periodo** "36" tiene dos **cifras**).
> 4.  **Simplificación:**
>     *   Sacamos tercera de 135 (45) y de 99 (33) $\rightarrow \frac{45}{33}$.
>     *   Sacamos tercera de 45 (15) y de 33 (11) $\rightarrow$ **$\frac{15}{11}$**

> [!example] Ejemplo 2: Caso con cifras grandes ($421.\overline{36}$)
> 1.  **Número completo:** 42136.
> 2.  **Restar parte entera:** $42136 - 421 = 41715$.
> 3.  **Denominador:** 99.
> 4.  **Simplificación por tercera:**
>     *   *Criterio de divisibilidad:* Sumamos las **cifras** de 41715 ($4+1+7+1+5 = 18$). Como 18 es múltiplo de 3, podemos **simplificar**.
>     *   $\frac{41715 \div 3}{99 \div 3} = \frac{13905}{33}$.
>     *   Nuevamente, $1+3+9+0+5 = 18$, dividimos por 3:
>     *   **Resultado final: $\frac{4635}{11}$**

> [!example] Ejemplo 3: El "Caso Raro" del Periodo 9 ($5.\overline{9}$)
> 1.  **Operación:** $\frac{59 - 5}{9} = \frac{54}{9}$.
> 2.  **Resultado:** $54 \div 9 = 6$.
> 
> *Explicación pedagógica:* Matemáticamente, un **periodo** 9 infinito equivale exactamente al siguiente número entero. Es como en los comercios: si un artículo cuesta $999.99$, se entiende que el valor real es $1000$. Aquí, $5.\overline{9}$ **es** exactamente 6.

> [!example] Ejemplo 4: Aplicación USD ($12.\overline{9}$)
> Si un producto tiene un precio teórico de $12.\overline{9}$ USD:
> *   Convertimos: $\frac{129 - 12}{9} = \frac{117}{9}$.
> *   Al dividir: $117 \div 9 = 13$.
> **Conclusión:** El precio real a pagar son **13 USD**.

---

## EJERCICIOS PARA EL ESTUDIANTE

### Nivel: Fácil
1. $0.\overline{7}$
2. $0.\overline{5}$
3. $0.\overline{2}$
4. $0.\overline{8}$

### Nivel: Medio (Con parte entera > 0)
1. $2.\overline{15}$
2. $3.\overline{21}$
3. $1.\overline{45}$
4. $4.\overline{12}$

### Nivel: Avanzado (Periodo 9 / Aplicación)
1. $1.\overline{9}$
2. $24.\overline{9}$
3. $9.\overline{9}$
4. $0.\overline{9}$

> [!success] ✅ Respuestas
> **Fáciles:** 1) $\frac{7}{9}$ | 2) $\frac{5}{9}$ | 3) $\frac{2}{9}$ | 4) $\frac{8}{9}$
> **Medios:** 1) $\frac{71}{33}$ | 2) $\frac{106}{33}$ | 3) $\frac{16}{11}$ | 4) $\frac{136}{33}$
> **Avanzados:** 1) 2 | 2) 25 | 3) 10 | 4) 1

---

## MINI-PRUEBA DE AUTOEVALUACIÓN

**1. ¿Qué define técnicamente a un decimal como "periódico puro"?**
*Respuesta:* Que el **periodo** inicia inmediatamente después de la **coma decimal**, sin ninguna otra cifra de por medio.

**2. ¿Cuál es la fracción irreducible de $0.\overline{4}$?**
*Respuesta:* $\frac{4}{9}$. Siguiendo el proceso: número (4) menos **parte entera** (0) sobre un nueve por tener una cifra periódica.

**3. Si una factura indica un cobro de $19.\overline{9}$ euros, ¿es correcto decir que el precio es "casi" 20 euros?**
*Respuesta:* No. Es correcto decir que el precio **es exactamente** 20 euros. Matemáticamente, la conversión $\frac{199 - 19}{9} = \frac{180}{9}$ da como resultado el entero 20. No es una aproximación, es una identidad.

---

> [!tip] 💡 En la próxima clase
> Prepárate para el siguiente nivel: estudiaremos los **Decimales Periódicos Mixtos**. Aprenderás cómo manejar esas cifras "rebeldes" que aparecen entre la coma y el periodo, y cómo afectan al **denominador** agregando ceros junto a los nueves.

> [!info] 🧭 Navegación
> ⬅️ [[Clase 15 — Converting a Pure Repeating Decimal to a Fraction | Example 1]] | [[00 - Índice del curso|Índice]] | [[Clase 17 — Converting a Mixed Repeating Decimal to a Fraction]] ➡️