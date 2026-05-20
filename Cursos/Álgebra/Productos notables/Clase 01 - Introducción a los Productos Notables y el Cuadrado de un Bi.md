# Clase 01 — Introducción a los Productos Notables y el Cuadrado de un Binomio

tags: #algebra #productosnotables
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 6

> [!info] 🧭 Navegación
> Anterior: [[00 - Índice del curso]] | **Siguiente: [[Clase 02 - Binomio con término común]]**

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> Los productos notables son "atajos" matemáticos que nos permiten encontrar el resultado de multiplicaciones específicas por simple inspección, sin necesidad de realizar todo el proceso distributivo, lo que ahorra tiempo y evita errores en álgebra avanzada.

*   💵 **Finanzas:** Se utiliza en fórmulas de interés compuesto donde el crecimiento de una inversión se proyecta elevando binomios al cuadrado o al cubo en términos de $USD.
*   🏗️ **Construcción:** Fundamental para calcular la expansión de áreas superficiales cuando las dimensiones de un terreno cuadrado aumentan proporcionalmente.
*   📊 **Situación cotidiana:** Estimación rápida de cambios en presupuestos cuando dos variables (como precio y cantidad) sufren incrementos simultáneos.

---

## Concepto clave

> [!note] 📌 ¿Qué es Productos notables?
> ¡Qué tal amigos! Para entenderlo fácil: los productos notables son multiplicaciones con reglas fijas que podemos resolver "de memoria". Es como un truco de magia matemático que nos permite escribir la respuesta directamente sin hacer todas las cuentas intermedias.

### Origen Geométrico (¿Por qué funciona?)
Para entender la fórmula $(a + b)^2$, imagina un cuadrado cuyo lado mide $a + b$. Al calcular su área total, el cuadrado se divide en cuatro figuras:
1. Un cuadrado pequeño de área $a^2$.
2. Un cuadrado más grande de área $b^2$.
3. **Dos rectángulos idénticos** de área $a \cdot b$ cada uno.
Al sumar todo, obtenemos: $a^2 + ab + ab + b^2 = a^2 + 2ab + b^2$. ¡De aquí sale el famoso "doble producto"!

> [!tip] 🧠 Recordatorio de Potenciación
> Antes de avanzar, recuerda la regla de **Potencia de una Potencia**: para elevar una potencia a otro exponente, los exponentes se multiplican.
> $$(x^a)^b = x^{a \cdot b}$$
> *Ejemplo:* $(m^2)^2 = m^{2 \cdot 2} = m^4$. ¡Ten esto presente para los ejercicios avanzados!

> [!warning] ⚠️ Error común
> ¡Mucho cuidado aquí! El cuadrado **no se distribuye** si hay una suma o resta.
> ❌ Incorrecto: $(a + b)^2 = a^2 + b^2$
> ✅ Correcto: $(a + b)^2 = a^2 + 2ab + b^2$

> [!tip] 💡 Regla mnemotécnica
> "El cuadrado del primero, el doble del primero por el segundo, y el cuadrado del último".

---

## Procedimiento paso a paso

Para resolver el cuadrado de un binomio, sigue estos pasos técnicos. **Ojo con los signos:** el término central siempre hereda el signo del binomio, mientras que el tercer término siempre será positivo.

> [!info] Metodología Estructurada
> 1. **PASO 1:** Elevar el primer término al cuadrado: $(\text{término}_1)^2$.
> 2. **PASO 2:** Calcular el **doble producto**. Multiplicamos 2 por el primero y por el segundo: $2 \cdot (\text{término}_1) \cdot (\text{término}_2)$.
> 3. **PASO 3:** Elevar el segundo término al cuadrado (siempre es positivo): $(\text{término}_2)^2$.
> 4. **PASO 4:** Escribir el trinomio resultante en orden.

---

## Ejemplos resueltos

```ad-example
**Ejemplo 1 (Básico):** Resuelve $(x + 3)^2$
1. Cuadrado del primero: $x^2$
2. Doble del primero por el segundo: $2(x)(3) = 6x$
3. Cuadrado del segundo: $3^2 = 9$
**Resultado:** $x^2 + 6x + 9$
```

```ad-example
**Ejemplo 2 (Signos):** Resuelve $(4a - 5b)^2$
*¡Ojo con el signo! Como el binomio es una resta, el término central será negativo.*
1. Cuadrado del primero: $(4a)^2 = 16a^2$
2. Doble del primero por el segundo (hereda el signo negativo): $-2(4a)(5b) = -40ab$
3. Cuadrado del segundo (siempre positivo): $(-5b)^2 = 25b^2$
**Resultado:** $16a^2 - 40ab + 25b^2$
```

```ad-example
**Ejemplo 3 (Avanzado):** Resuelve $(5m^2 + 3n^3)^2$
1. Cuadrado del primero: $(5m^2)^2 = 25m^4$ (multiplicamos exponentes: $2 \times 2$)
2. Doble del primero por el segundo: $2(5m^2)(3n^3) = 30m^2n^3$
3. Cuadrado del segundo: $(3n^3)^2 = 9n^6$ (multiplicamos exponentes: $3 \times 2$)
**Resultado:** $25m^4 + 30m^2n^3 + 9n^6$
```

```ad-example
**Ejemplo 4 (Aplicación $USD):** Un panel solar cuadrado tiene un lado que mide $(x + 2)$ metros. Si el costo por metro cuadrado es de $10 USD, ¿cuál es el costo total del panel?
1. Hallamos el área elevando el lado al cuadrado: $(x + 2)^2 = x^2 + 4x + 4$
2. Multiplicamos el área por el precio unitario: $10 \cdot (x^2 + 4x + 4)$
**Resultado:** El costo total es $10x^2 + 40x + 40$ USD.
```

---

## Ejercicios para el estudiante

```ad-abstract
**🟢 Nivel Fácil**
1. $(m + 1)^2$
2. $(x + 5)^2$
3. $(a + 2)^2$
4. $(y + 10)^2$
```

```ad-abstract
**🟡 Nivel Medio**
1. $(2x + 3y)^2$
2. $(a^2 - 4)^2$
3. $(3m - 5n)^2$
4. $(4b + 1)^2$
```

```ad-abstract
**🔴 Nivel Avanzado**
1. $(5x^3 + 2y^4)^2$
2. Una lona cuadrada tiene un lado de $(3x + 2)$ metros. Exprese su área total como un trinomio.
3. $(2a^2b - 3c^3)^2$
4. Si el costo de una superficie cuadrada de lado $(x + 8)$ metros es de $5 USD por cada metro cuadrado, ¿cuál es la expresión del costo total?
```

```ad-success
**Solucionario Compacto**
**Fácil:** 1) $m^2+2m+1$ | 2) $x^2+10x+25$ | 3) $a^2+4a+4$ | 4) $y^2+20y+100$
**Medio:** 1) $4x^2+12xy+9y^2$ | 2) $a^4-8a^2+16$ | 3) $9m^2-30mn+25n^2$ | 4) $16b^2+8b+1$
**Avanzado:** 
1) $25x^6+20x^3y^4+4y^8$
2) $9x^2+12x+4$
3) $4a^4b^2-12a^2bc^3+9c^6$
4) $5x^2+80x+320$ (Área $x^2+16x+64$ multiplicada por 5).
```

---

## Mini-prueba de autoevaluación

```ad-question
**Pregunta 1:** ¿Por qué aparece un "2" en el término central de la fórmula $(a+b)^2$?
**Respuesta:** Porque geométricamente, al expandir el cuadrado, se forman dos rectángulos idénticos de área $a \cdot b$.
```

```ad-question
**Pregunta 2:** ¿Cuál es el resultado de $(2x - 3)^2$?
a) $4x^2 - 9$
b) $4x^2 - 6x + 9$
c) $4x^2 - 12x + 9$
d) $2x^2 - 12x + 6$
**Respuesta correcta: c.** Explicación: El primer término es $(2x)^2 = 4x^2$, el doble producto es $2(2x)(-3) = -12x$, y el último es $(-3)^2 = 9$.
```

```ad-question
**Pregunta 3:** Si una baldosa de lado $(x+1)$ cuesta $2 USD por unidad de área, ¿cuál es su precio?
**Respuesta:** El precio es $2x^2 + 4x + 2$ USD. Se obtiene de $2 \cdot (x+1)^2 = 2(x^2 + 2x + 1)$.
```

---

## Notas para el próximo tema

> [!tip] 💡 En la próxima clase
> Veremos el **Producto de binomios con término común**. Aprenderemos a identificar casos como $(x+a)(x+b)$ y entenderemos por qué, a diferencia de hoy, los términos no comunes no resultan en un doble producto exacto, sino en una suma. ¡No te lo pierdas!

> [!info] 🧭 Navegación
> Anterior: [[00 - Índice del curso]] | **Siguiente: [[Clase 02 - Binomio con término común]]**