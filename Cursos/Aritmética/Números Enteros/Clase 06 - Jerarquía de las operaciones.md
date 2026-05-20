# Clase 06 — Jerarquía de las operaciones
tags: #algebra #jerarquadelasop
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 6 de 8

> [!info] 🧭 Navegación
> Anterior: [[Clase 05 - Ley de los Signos]]
> Índice: [[00 - Índice del curso]]
> Siguiente: [[Clase 07 - Signos de Agrupación Avanzados]]

---

## ¿Por qué es importante esta clase?

La jerarquía de las operaciones no es una regla arbitraria, sino un **lenguaje universal** y un **acuerdo matemático** fundamental. Sin este orden preestablecido, una misma expresión matemática podría interpretarse de múltiples formas, generando resultados distintos según quien la resuelva. Este consenso garantiza que la comunicación científica, financiera y técnica sea precisa en cualquier parte del mundo.

> [!info] 🌍 Relevancia y aplicaciones
> 1.  💵 **Aplicación USD:** Permite calcular presupuestos exactos al combinar ahorros previos con la compra de múltiples artículos (por ejemplo, sumar un saldo inicial y restar el producto de cantidad por precio).
> 2.  🏗️ **Aplicación Práctica:** En ingeniería y construcción, es vital para calcular áreas totales donde se deben sumar diversas superficies rectangulares obtenidas mediante multiplicaciones previas.
> 3.  📊 **Situación cotidiana:** Ayuda en el reparto equitativo de recursos tras una compra masiva, permitiendo restar gastos operativos o descuentos antes de realizar la división final entre los beneficiarios.

---

## CONCEPTO CLAVE

> [!note] 📌 ¿Qué es Jerarquía de las operaciones?
> Es el orden estricto acordado para resolver operaciones combinadas. Su objetivo es que todos, al enfrentarnos a la misma expresión, obtengamos el mismo resultado unívoco.

> [!warning] ⚠️ Error común
> El error más frecuente es resolver las operaciones simplemente de izquierda a derecha, ignorando la prioridad de los operadores.
> *   **Operación:** $5 + 2 \times 3$
> *   **Incorrecto:** $7 \times 3 =$ **21** (Se sumó primero, lo cual es un error).
> *   **Correcto:** $5 + 6 =$ **11** (La multiplicación siempre se resuelve antes que la suma).

> [!tip] 💡 Truco para recordarlo: "Muros y Ejercicios Aparte"
> Como enseña el Profe Alex, la estrategia más potente es **"Separar en términos"**. Utiliza los signos **+** y **-** (que estén fuera de paréntesis o raíces) como si fueran **muros infranqueables**. 
> 
> **Cada término es como un ejercicio aparte.** Al ver la expresión como pequeños problemas independientes separados por muros, dejas de sentirte abrumado por la longitud de la operación y te aseguras de no mezclar números que pertenecen a términos distintos hasta el final.

---

## PROCEDIMIENTO PASO A PASO

Para resolver cualquier expresión, respeta estrictamente este orden de prioridad:

```text
1. SIGNOS DE AGRUPACIÓN: (paréntesis), [corchetes], {llaves}. 
   Se resuelven siempre de ADENTRO HACIA AFUERA.
2. POTENCIAS Y RAÍCES.
3. MULTIPLICACIONES Y DIVISIONES:
   *Si hay varias del mismo nivel, resuelve de IZQUIERDA A DERECHA.
4. SUMAS Y RESTAS:
   *Si hay varias del mismo nivel, resuelve de IZQUIERDA A DERECHA.
```

---

## EJEMPLOS DESARROLLADOS

> [!example] Ejemplo 1: Operación Básica y Separación
> **Problema:** $7 - 2 \times 5 - 16 \div 2$
> 1. **Separar en términos:** Los signos $-$ actúan como muros. Tenemos 3 ejercicios independientes:
>    *   Término 1: (**7**)
>    *   Término 2: (**2 \times 5**)
>    *   Término 3: (**16 \div 2**)
> 2. **Resolver cada término:** 
>    *   El **7** baja igual. 
>    *   $2 \times 5 =$ **10**. 
>    *   $16 \div 2 =$ **8**.
> 3. **Resultado final:** $7 - 10 - 8 =$ **-11**.

> [!example] Ejemplo 2: Signos y Paréntesis
> **Problema:** $-3(-2)(-5) + 5(-4)$
> 1. **Término 1:** Una cadena de multiplicaciones. Aplicamos ley de signos: $(- \times - = +)$ y luego $(+ \times - = -)$.
>    *   $3 \times 2 \times 5 = 30$. Resultado del término: **-30**.
> 2. **Término 2:** Multiplicación simple $5 \times (-4)$.
>    *   $(+ \times - = -)$. Resultado del término: **-20**.
> 3. **Resultado final:** $-30 - 20 =$ **-50**.

> [!example] Ejemplo 3: Potencias y Raíces
> **Problema:** $2(3^2) - 5(2^3)$
> 1. **Prioridad:** Primero resolvemos las potencias antes de cualquier multiplicación.
>    *   $3^2 = 9$.
>    *   $2^3 = 8$.
> 2. **Multiplicar:** Ahora procesamos los términos:
>    *   $2 \times 9 =$ **18**.
>    *   $5 \times 8 =$ **40**.
> 3. **Resultado final:** $18 - 40 =$ **-22**.

> [!example] Ejemplo 4: Aplicación USD (Lógica de Prioridad)
> **Contexto:** Tienes **$75** USD en tu cuenta. Recibes un bono de **$14** USD, pero compras **3** artículos que cuestan **$25** USD cada uno.
> 1. **Representación:** $75 + 14 - (3 \times 25)$
> 2. **Análisis:** Aunque la suma está a la izquierda, el producto $3 \times 25$ representa el gasto total y debe resolverse con prioridad.
> 3. **Operación:** $75 + 14 - 75$ (o $89 - 75$).
> 4. **Resultado final:** Te quedan **$14** USD.

---

## EJERCICIOS PARA EL ESTUDIANTE

> [!abstract] 🟢 Bloque Verde (Fácil)
> 1. $4 \times 8 - 12$
> 2. $5 + 3 \times 4$
> 3. $20 \div 2 - 5$
> 4. $10 - 2 \times 3$

> [!abstract] 🟡 Bloque Amarillo (Medio)
> 5. $3 + 2(4^2) - 5$
> 6. $2(5 - 3)^2 + 10$
> 7. $\sqrt{16} + 3(2^2)$
> 8. $8 - (10 \div 2) + 3^2$

> [!abstract] 🔴 Bloque Rojo (Avanzado - Lógica USD)
> 9. $100 - [2(15 + 5) - (10 \div 2)]$
> 10. $50 + \{[3(10 - 2)] - 4^2\}$
> 11. $200 - [3(40) + \sqrt{100}]$
> 12. $10 + 2\{[5(3^2)] - 40\}$

> [!success] ✅ Soluciones para el Docente
> 1. **20** | 2. **17** | 3. **5** | 4. **4** | 5. **30** | 6. **18** | 7. **16** | 8. **12** | 9. **65** | 10. **58** | 11. **70** | 12. **20**

---

## MINI-PRUEBA DE AUTOEVALUACIÓN

> [!question] Pregunta 1
> En una expresión compleja que no contiene signos de agrupación, ¿cuál es el último nivel de operaciones que se debe resolver?
> **Respuesta:** Las sumas y las restas.

> [!question] Pregunta 2
> Resuelve paso a paso la siguiente expresión: $2^3 + \sqrt{25} \times 2$
> **Paso 1 (Potencias/Raíces):** $8 + 5 \times 2$
> **Paso 2 (Multiplicación):** $8 + 10$
> **Resultado:** **18**.

> [!question] Pregunta 3
> Un comerciante tiene **$100** USD. Paga **$20** de transporte y luego adquiere **2** cajas de mercancía a **$15** USD cada una. ¿Qué expresión representa correctamente su saldo final siguiendo la jerarquía?
> A) $(100 - 20 - 2) \times 15$
> B) $100 - 20 - 2 \times 15$
> **Respuesta correcta:** **B**. La multiplicación del costo por las cajas tiene prioridad sobre las restas del saldo total.

---

> [!tip] 💡 En la próxima clase
> Utilizaremos estos mismos principios para trabajar con **ecuaciones algebraicas**, donde aprenderás que para "despejar" una incógnita, a menudo aplicamos la jerarquía en orden inverso.

> [!info] 🧭 Navegación
> Anterior: [[Clase 05 - Ley de los Signos]]
> Índice: [[00 - Índice del curso]]
> Siguiente: [[Clase 07 - Signos de Agrupación Avanzados]]