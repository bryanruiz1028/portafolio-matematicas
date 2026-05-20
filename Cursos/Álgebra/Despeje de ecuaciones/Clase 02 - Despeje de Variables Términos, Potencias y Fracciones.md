# Clase 02 — Despeje de Variables: Términos, Potencias y Fracciones
tags: #algebra #solvingequation
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 3

---

### 1. NAVEGACIÓN
[[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | [[Clase 03|Clase 03 ➡]]

---

### 2. RELEVANCIA Y APLICACIONES

> [!info] 🧭 Navegación
> En esta sesión aprenderás a dominar el despeje cuando existen múltiples términos, potencias o denominadores. Construiremos sobre la base de las operaciones inversas para resolver ecuaciones más robustas.

> [!info] 🌍 Relevancia y aplicaciones
> El despeje es la "llave maestra" que nos permite hallar valores ocultos en la vida real.
> *   **💵 Aplicación USD:** Si conoces el total pagado por un lote de productos y los impuestos fijos, puedes despejar para hallar el **precio unitario** original.
> *   **🏗️ Aplicación práctica:** En ingeniería, el **Teorema de Pitágoras** se usa para calcular la longitud de cables o soportes despejando uno de sus lados.
> *   **📊 Situación cotidiana:** Si viajas a una velocidad constante y sabes la distancia, despejas el **tiempo** para planificar tu llegada exacta.

---

### 3. CONCEPTO CLAVE Y ERRORES COMUNES

Despejar no es solo mover números; es aplicar una jerarquía lógica para "liberar" a la variable de sus acompañantes.

> [!note] **La Regla de la Cebolla (Jerarquía Inversa)**
> Imagina que la variable es el corazón de una cebolla. Para llegar a ella, debes quitar las capas desde la más externa a la más interna. 
> *   **Matemáticas normales (PEMDAS):** Paréntesis → Exponentes → Multiplicación/División → Suma/Resta.
> *   **Al despejar:** Hacemos lo opuesto. Primero quitamos lo que suma/resta (capas externas) y al final lo que multiplica/divide o tiene potencia (núcleo).

> [!warning] **¡Cuidado con el dueño del signo!**
> Un error crítico es pensar que el signo de una operación pertenece al número que tiene *atrás*. 
> **Regla de oro:** El signo le pertenece al término que viene **después** de él.
> *   En $2 - x = y$, el signo menos le pertenece a la $x$. El $2$ no tiene signo visible, por lo que es **positivo ($+2$)** y está sumando. Para moverlo, debe pasar al otro lado restando.

> [!warning] **El error de la raíz prohibida**
> En expresiones como $\sqrt{b^2 + c^2}$, **jamás** puedes cancelar la raíz con los cuadrados individuales. La raíz solo se cancela si afecta a un único término o a todo el conjunto mediante un paréntesis. Si hay una suma dentro, la raíz se queda ahí.

---

### 4. PROCEDIMIENTO PASO A PASO

Antes de mover cualquier cosa, debemos poner orden en la ecuación.

```text
PASO 0: SIMPLIFICAR. Sustituye valores conocidos y resuelve operaciones aritméticas 
        pendientes (ej: si tienes 3 * 2, conviértelo en 6 antes de despejar).
PASO 1: IDENTIFICAR TÉRMINOS. Cuenta cuántos grupos hay separados por + o -.
PASO 2: MOVER TÉRMINOS SOBRANTES. Pasa los términos que no contienen la variable 
        al otro lado (Suma ↔ Resta).
PASO 3: TRATAR DENOMINADORES. 
        • Si el denominador afecta a TODO el lado de la ecuación: Pásalo a multiplicar PRIMERO.
        • Si el denominador afecta solo a UN TÉRMINO: Mueve los otros términos PRIMERO.
PASO 4: DESPEGAR EL NÚCLEO. Quita multiplicaciones (pasan a dividir) y potencias 
        (pasan como raíz).
```

---

### 5. EJEMPLOS RESUELTOS

> [!example] **Ejemplo 1: El signo fantasma**
> Despejar $x$ en: $2 - x = y$
> 1. Identificamos que el $2$ es positivo ($+2$). Pasa restando: $-x = y - 2$.
> 2. Queremos el valor de $x$, no de $-x$. Multiplicamos todo por $-1$ (o simplemente cambiamos todos los signos de la ecuación).
> *   **Resultado:** $x = -y + 2$ (que es lo mismo que $x = 2 - y$).

> [!example] **Ejemplo 2: Teorema de Pitágoras**
> Despejar $b$ en: $a^2 = b^2 + c^2$
> 1. El término $c^2$ está sumando, pasa restando: $a^2 - c^2 = b^2$.
> 2. Aplicamos raíz cuadrada para eliminar la potencia: $\sqrt{a^2 - c^2} = b$.
> *   **Nota pedagógica:** Aquí se deja la raíz expresada. No intentes quitar los cuadrados de $a$ y $c$ porque están restándose.

> [!example] **Ejemplo 3: Aplicación Financiera (USD)**
> Si $Total = Precio + (Tarifa \times Tiempo)$, halla el $Precio$ si $Total=18, Tarifa=3, Tiempo=2$.
> 1. **Paso 0 (Sustituir y Simplificar):** $18 = Precio + (3 \times 2) \rightarrow 18 = Precio + 6$.
> 2. **Despejar:** El 6 está sumando, pasa restando: $18 - 6 = Precio$.
> *   **Resultado:** $Precio = 12$ USD.

---

### 6. EJERCICIOS PARA EL ESTUDIANTE

> [!abstract] **Práctica de Consolidación**
>
> **🟢 Nivel Fácil (Un paso)**
> 1. Despejar $a$: $a + 5 = b$
> 2. Despejar $x$: $y = x - 10$
> 3. Despejar $m$: $m + n = 20$
> 4. Despejar $h$: $z = h - 15$
>
> **🟡 Nivel Medio (Física y Geometría)**
> 5. Despejar $v$ en: $a = \frac{v - v_i}{t}$
> 6. Despejar $x$ en: $3x + 4 = y$
> 7. Despejar $b$ en: $y = mx + b$
> 8. Despejar $v_i$ en: $v = v_i + at$
>
> **🔴 Nivel Avanzado (USD y Costos)**
> 9. **Repartición de gastos:** Si el costo por persona se calcula como $\frac{Total + 5}{2} = 3y - 4$, despeja el **Total** ($x$).
> 10. **Presupuesto base:** Si $x = \frac{2y - 10}{5} + 3$, despeja el gasto variable $y$.
> 11. **Inversión promedio:** Despejar $a$ en $C = \frac{a + b}{2}$.
> 12. **Cálculo de ahorro:** Si $10 = \frac{x - 20}{4} + 5$, ¿cuánto es el valor de $x$?

---

### 7. RESPUESTAS PARA EL DOCENTE

> [!success] **Solucionario con Pasos Intermedios**
> 1. $a = b - 5$
> 2. $x = y + 10$
> 3. $m = 20 - n$
> 4. $h = z + 15$
> 5. $at = v - v_i \rightarrow v = at + v_i$
> 6. $3x = y - 4 \rightarrow x = \frac{y - 4}{3}$
> 7. $b = y - mx$
> 8. $v_i = v - at$
> 9. $Total + 5 = 2(3y - 4) \rightarrow Total = 6y - 8 - 5 \rightarrow Total = 6y - 13$
> 10. $x - 3 = \frac{2y - 10}{5} \rightarrow 5(x - 3) = 2y - 10 \rightarrow \frac{5x - 15 + 10}{2} = y \rightarrow y = \frac{5x - 5}{2}$
> 11. $2C = a + b \rightarrow a = 2C - b$
> 12. $10 - 5 = \frac{x - 20}{4} \rightarrow 5 \times 4 = x - 20 \rightarrow 20 + 20 = x \rightarrow x = 40$

---

### 8. MINI-PRUEBA DE AUTOEVALUACIÓN

> [!question] **¿Qué tanto aprendiste?**
> 1. **Para despejar $a$ en $v = v_i + at$, ¿qué mueves primero?**
>    a) La $t$, porque está al final.
>    b) La $v_i$, porque es un término independiente que suma.
>    c) Ambos al mismo tiempo.
>
> 2. **Si tienes $-x = 10$, ¿cuál es el valor de $x$?**
>    a) $10$
>    b) $1/10$
>    c) $-10$
>
> 3. **Problema USD:** Tienes $50$ USD de presupuesto total. La fórmula es $50 = x + 2(15)$. ¿Cuánto vale el gasto base $x$?
>    a) $20$ USD
>    b) $35$ USD
>    c) $80$ USD

---

### 9. CIERRE Y PRÓXIMO TEMA

> [!tip] 💡 En la próxima clase
> ¡Felicidades! Ya sabes cómo pelar las capas externas de la "cebolla algebraica". En la **Clase 03**, enfrentaremos el reto final: ¿qué pasa cuando la variable aparece en ambos lados del igual o está protegida por **paréntesis**? Aprenderemos a agrupar y romper paréntesis de forma profesional.

---
[[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | [[Clase 03|Clase 03 ➡]]