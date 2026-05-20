# Clase 03 — Hierarchy of Operations | Example 2 + Hierarchy of Operations | Example 5

#algebra #hierarchyofoper

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 3

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]

---

> [!info] 🌍 Relevancia y aplicaciones
> El orden de las operaciones es el conjunto de reglas que garantiza que todos obtengamos el mismo resultado al resolver un cálculo. Sin esta jerarquía, la interpretación de fórmulas matemáticas sería ambigua, derivando en errores críticos en áreas técnicas y financieras.
> - 💵 **Cálculo de presupuestos en $USD:** Permite aplicar correctamente descuentos sobre el total o sobre artículos específicos, evitando pagar de más en compras múltiples.
> - 🏗️ **Fórmulas de ingeniería:** Una potencia mal aplicada (ej. calcular el área de una superficie) altera la resistencia calculada de una estructura, poniendo en riesgo la integridad de la construcción.
> - 📊 **Situaciones cotidianas:** Determinar el pago exacto de servicios con tarifas base y cargos variables por consumo que pueden estar potenciados o divididos.

---

> [!note] 📌 ¿Qué es Hierarchy of Operations?
> Es el **orden de prioridad** que debemos seguir para resolver una expresión matemática correctamente. Para un estudiante de 12 años, esto significa entender que hay operaciones más "fuertes" que deben atenderse antes que las "débiles". El método más efectivo es la **Separación en Términos**, donde los signos de suma y resta actúan como fronteras que dividen el problema en secciones manejables.

> [!warning] ⚠️ Error común
> Un error muy frecuente es realizar una multiplicación antes que una potencia por leer de izquierda a derecha.
> - ❌ **Incorrecto:** $5 \times 2^3 = 10^3 = 1000$
> - ✅ **Correcto:** $5 \times 2^3 = 5 \times 8 = 40$

> [!tip] 💡 Truco para recordarlo
> Utiliza el enfoque del **Profe Alex**: visualiza la operación como un archipiélago. Las "islas" son los términos, y los signos `+` y `-` (que están fuera de paréntesis) son los **bordes** o fronteras. Resuelve cada isla por separado y, al final, une los resultados.

---

## Procedimiento Paso a Paso

```text
PASO 1 → Separar la expresión en términos (los signos + y - fuera de paréntesis son los BORDES).
PASO 2 → Resolver signos de agrupación (paréntesis y corchetes) desde adentro hacia afuera.
PASO 3 → Resolver potencias y raíces dentro de cada término.
PASO 4 → Resolver multiplicaciones y divisiones dentro de cada término.
PASO 5 → Realizar sumas y restas finales de los resultados de cada término (consolidación).
```

---

## Ejemplos Prácticos

> [!example] Ejemplo 1: Caso básico
> **Ejercicio:** $3^2 - 2 \cdot 3$
> 1. **Separar términos:** El signo `-` es el **borde**. Tenemos dos islas: $(3^2)$ y $(2 \cdot 3)$.
> 2. **Resolver potencia (Primer término):** $3^2 = 9$.
> 3. **Resolver multiplicación (Segundo término):** $2 \cdot 3 = 6$.
> 4. **Resultado final:** $9 - 6 = 3$.

> [!example] Ejemplo 2: Caso con signos
> **Ejercicio:** $-5 \cdot (-2) + 5^2$
> 1. **Separar términos:** El signo `+` es el **borde**.
>    - Término 1: $-5 \cdot (-2)$
>    - Término 2: $5^2$
> 2. **Multiplicación (Ley de signos):** En el primer término, el `-` de $(-2)$ es un **signo del número**. Menos por menos es más: $-5 \cdot (-2) = 10$.
> 3. **Potencia:** En el segundo término, $5^2 = 25$.
> 4. **Resultado final:** $10 + 25 = 35$.
> > [!warning] ⚠️ Nota
> > Es vital distinguir: el signo `+` central es una operación (borde), mientras que los signos `-` dentro de los paréntesis o al inicio son propiedad del número.

> [!example] Ejemplo 3: Caso avanzado (Raíces compuestas)
> **Ejercicio:** $\sqrt{3^2 \cdot 5 - 24 + 15}$
> 1. **Identificar "islas" internas:** Antes de sacar la raíz, resolvemos lo de adentro separando en términos internos:
>    - **Isla A:** $3^2 \cdot 5$. Primero la potencia: $9 \cdot 5 = 45$.
>    - **Isla B:** $- 24$. (No tiene operaciones pendientes).
>    - **Isla C:** $+ 15$. (No tiene operaciones pendientes).
> 2. **Consolidar interior:** $\sqrt{45 - 24 + 15}$.
>    - Operamos de izquierda a derecha: $45 - 24 = 21$.
>    - Luego: $21 + 15 = 36$.
> 3. **Raíz final:** $\sqrt{36} = 6$.

> [!example] Ejemplo 4: Aplicación $USD
> **Problema:** Compras 3 suscripciones de $15 USD cada una, tienes un cupón de descuento de $10 USD y un cargo extra de $5 USD al cuadrado por envío.
> 1. **Formular expresión:** $3 \cdot 15 - 10 + 5^2$
> 2. **Términos (Islas):** $(3 \cdot 15)$, $(-10)$, $(5^2)$.
> 3. **Resolución:**
>    - Multiplicación: $3 \cdot 15 = 45$
>    - Potencia: $5^2 = 25$
>    - Operación combinada: $45 - 10 + 25$
> 4. **Resultado:** $35 + 25 = 60$. El total a pagar es **$60 USD**.

---

## Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Fácil (Potencias simples)
> 1. $4^2 + 2 \cdot 5$
> 2. $3 \cdot 4 - 2^2$
> 3. $10 + 5^2 \div 5$
> 4. $2^3 - 3 \cdot 2$

> [!abstract] 🟡 Nivel Medio (Raíces y paréntesis)
> 1. $10 - (2+3)^2 + \sqrt{25}$
> 2. $\sqrt{49} \cdot 2 + (10 - 8)^3$
> 3. $5^2 - \sqrt{16} \cdot 3 + 2$
> 4. $(4 + 1)^2 \div 5 - \sqrt{9}$

> [!abstract] 🔴 Nivel Avanzado (Problemas USD)
> 1. Tienes $100 USD. Gastas $2^4$ USD en comida y luego compras 3 camisas de $12 USD cada una. ¿Cuánto dinero te queda?
> 2. Una deuda de $50 USD se reduce con 2 pagos de $5^2$ USD, pero se suma un cargo administrativo de $\sqrt{64}$ USD. ¿Cuál es el saldo final de la deuda?
> 3. Un ahorro de $10 USD al cuadrado se divide equitativamente entre 4 personas. Si a cada una se le descuentan $3 USD de comisión bancaria, ¿cuánto recibe cada una?
> 4. Compras un equipo de $200 USD con un descuento de $10^2$ USD, pero debes pagar un impuesto de envío de $2 \cdot 15$ USD. ¿Cuál es el total final a pagar?

> [!success] ✅ Respuestas (Solo para el docente)
> **Fácil:** 1) 26 | 2) 8 | 3) 15 | 4) 2
> **Medio:** 1) -10 | 2) 22 | 3) 15 | 4) 2
> **Avanzado:** 1) $48 | 2) $8 | 3) $22 | 4) $130

---

## Mini-prueba de Autoevaluación

> [!question] Pregunta 1: Conceptual
> ¿Qué operación tiene mayor prioridad (se resuelve primero) en el siguiente término: $7 \cdot 4^2$?
> - A) Multiplicación
> - B) Potencia
> - C) Suma
> - D) Resta
>
> **Respuesta:** **B**. Según la jerarquía, las potencias se resuelven antes que las multiplicaciones dentro de un mismo término.

> [!question] Pregunta 2: Procedimental
> Resuelve la siguiente expresión: $20 \div (2 + 3) \cdot 2^2$
> - A) 16
> - B) 10
> - C) 4
> - D) 8
>
> **Respuesta:** **A**. 
> 1. Paréntesis: $20 \div 5 \cdot 2^2$.
> 2. Potencia: $20 \div 5 \cdot 4$.
> 3. Multiplicación/División (de izquierda a derecha): $4 \cdot 4 = 16$.

> [!question] Pregunta 3: Aplicación USD
> Si una suscripción cuesta $2^3$ USD por mes y decides pagar 12 meses por adelantado, pero recibes un descuento único de $20 USD por pronto pago, ¿cuál es la expresión correcta para el total?
> - A) $(2^3 \cdot 12) - 20$
> - B) $2^3 \cdot (12 - 20)$
> - C) $2^3 + 12 - 20$
>
> **Respuesta:** **A**. Primero debes calcular el costo total de los meses ($2^3$ que es 8, multiplicado por 12) y al resultado restarle el descuento único. ($96 - 20 = 76$ USD).

---

> [!tip] 💡 En la próxima clase
> Ahora que dominas la jerarquía básica y la separación en términos, el siguiente nivel es aprender a manejar **signos de agrupación múltiples**, como el uso combinado de paréntesis `()`, corchetes `[]` y llaves `{}` para organizar operaciones aún más complejas.

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]