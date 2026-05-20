# Clase 02 — Multiplicación de Expresiones Algebraicas: Monomios y Polinomios

#algebra #multiplicacionde
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 4

> [!info] 🧭 Navegación
> ◀ **Anterior**: [[Clase 01 - Suma y Resta de Expresiones Algebraicas]]
> 🔽 **Índice**: [[00 - Índice del curso]]
> ▶ **Siguiente**: [[Clase 03 - Multiplicación de Polinomio por Polinomio]]

---

## 🌍 Relevancia y aplicaciones

¡Bienvenido! Hoy vas a aprender a dominar el **código secreto** que utilizan los ingenieros para construir rascacielos y los analistas financieros para predecir el éxito de una empresa. Multiplicar expresiones algebraicas es la herramienta que nos permite calcular cómo cambian varias dimensiones o valores al mismo tiempo.

*   💵 **$USD**: Es la clave para proyectar ingresos totales cuando tanto el precio de un producto como la cantidad de clientes son variables que cambian cada mes.
*   🏗️ **Práctica**: En arquitectura, se usa para determinar superficies y volúmenes de estructuras cuyos diseños dependen de una medida base variable.
*   📊 **Cotidiana**: Permite planificar presupuestos de gran escala, ajustando costos automáticamente cuando hay incrementos proporcionales en los materiales.

---

## 📌 Concepto Clave

Antes de empezar, recordemos qué estamos multiplicando:
*   **Monomio:** Una expresión de un solo término (ej. $3x^2$).
*   **Polinomio:** Una expresión con varios términos unidos por suma o resta (ej. $2x + 5$ es un binomio; $x^2 - 3x + 1$ es un trinomio).

> [!note] 📌 ¿Qué es la Multiplicación Algebraica?
> Es la operación para obtener un producto uniendo factores. Se basa en tres pilares: aplicar la **Ley de los Signos**, multiplicar los **coeficientes** (números) y aplicar la propiedad de potencias de igual base, lo que significa **sumar los exponentes** de las letras iguales.

> [!tip] 💡 La regla del "1 Invisible"
> Este es el secreto de los expertos: 
> 1. Si una letra no tiene un número al lado, su coeficiente es **1** (ej. $x = 1x$).
> 2. Si una letra no tiene exponente visible, su exponente es **1** (ej. $m = m^1$).
> ¡Nunca los olvides al realizar tus cálculos!

> [!warning] ⚠️ Error común
> No confundas las reglas de la suma con las de la multiplicación:
> *   ❌ **Error**: Sumar coeficientes en lugar de multiplicarlos ($4x \cdot 2x = 6x^2$).
> *   ❌ **Error**: Sumar exponentes de letras que son diferentes ($a^2 \cdot b^3 = ab^5$).
> *   ✅ **Correcto**: Se multiplican números y se suman exponentes de letras iguales ($4x \cdot 2x = 8x^2$).

> [!tip] 💡 Truco para recordarlo: El método "S-N-L"
> Para que no se te escape nada, sigue siempre este orden:
> 1. **S**ignos: ¿Más por menos? ¿Menos por menos?
> 2. **N**úmeros: Multiplica los coeficientes (recuerda el 1 invisible).
> 3. **L**etras: Escribe la letra y suma sus exponentes.

---

## Procedimiento Paso a Paso

```text
PASO 1: Multiplicar los SIGNOS (Iguales = (+), Diferentes = (-)).
PASO 2: Multiplicar los NÚMEROS (Si no hay, usa el 1).
PASO 3: Sumar EXPONENTES de letras iguales. 
        Nota: Si sumas un exponente negativo, se resta (ej: 5 + (-2) = 3).
PASO 4: Escribir las LETRAS "solteras" (sin pareja) tal cual aparecen.
```

---

## Bloques de Ejemplos

> [!example] Ejemplo 1: Monomio por Monomio (Básico)
> **Operación:** $(5x^2)(3x^5)$
> *   **S:** $(+)$ por $(+)$ da **$+$**.
> *   **N:** $5 \times 3 = \mathbf{15}$.
> *   **L:** $x^2 \cdot x^5 = x^{(2+5)} = \mathbf{x^7}$.
> **Resultado:** $15x^7$

> [!example] Ejemplo 2: Fracciones y Signos
> **Operación:** $\left(-\frac{2}{3}x^6\right)\left(\frac{3}{5}x^7\right)$
> *   **S:** $(-)$ por $(+)$ da **$-$**.
> *   **N:** $\frac{2 \times 3}{3 \times 5} = \frac{6}{15}$. Simplificamos dividiendo ambos entre 3: $\frac{6 \div 3}{15 \div 3} = \mathbf{\frac{2}{5}}$.
> *   **L:** $x^6 \cdot x^7 = x^{(6+7)} = \mathbf{x^{13}}$.
> **Resultado:** $-\frac{2}{5}x^{13}$ (⚠️ *Nota: Siempre simplifica tus fracciones al final*).

> [!example] Ejemplo 3: Monomio por Polinomio (Propiedad Distributiva)
> **Operación:** $-3m^2 (5m - 7mn + 9n)$
> Aquí el monomio "visita" a cada término del paréntesis usando **S-N-L**:
> 1. **Monomio por 1er término:** $(-3m^2)(5m^1)$ 
>    $\to$ S: $(-)$, N: $15$, L: $m^{(2+1)} = m^3$. Resultado: **$-15m^3$**.
> 2. **Monomio por 2do término:** $(-3m^2)(-7m^1n^1)$ 
>    $\to$ S: $(+)$, N: $21$, L: $m^{(2+1)}n^1 = m^3n$. Resultado: **$+21m^3n$**.
> 3. **Monomio por 3er término:** $(-3m^2)(9n^1)$ 
>    $\to$ S: $(-)$, N: $27$, L: $m^2n^1$. Resultado: **$-27m^2n$**.
> **Resultado final:** $-15m^3 + 21m^3n - 27m^2n$

> [!example] Ejemplo 4: Aplicación Real con $USD
> **Problema:** El precio de una suscripción es $(2x + 5)$ USD. Si se venden $(3x)$ suscripciones, ¿cuál es el ingreso total?
> **Solución:** Multiplicamos cantidad por precio: $(3x^1) \cdot (2x^1 + 5)$
> *   $(3x)(2x) = \mathbf{6x^2}$
> *   $(3x)(5) = \mathbf{15x}$
> **Resultado:** El ingreso total es $(6x^2 + 15x)$ USD.

---

## Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Fácil
> 1. $(4a^3)(2a^4)$
> 2. $(-5b^2)(3b^6)$
> 3. $(x^2y)(x^3y^4)$ (Recuerda que los números son 1)
> 4. $(-2m^1)(-8m^3)$

> [!abstract] 🟡 Nivel Medio
> 1. $\frac{1}{2}x^2(4x - 6)$
> 2. $(-3a^2)(\frac{2}{3}a^1 + 5b^1)$ (Aplica S-N-L con cuidado en la fracción)
> 3. $5mn(2m^2 - 3n^2)$
> 4. $(-x^3)(x^2 - 4x + 2)$

> [!abstract] 🔴 Nivel Avanzado
> 1. Un panel solar rectangular mide $(4x^2 - 2x + 1)$ cm de largo y $(3x)$ cm de ancho. ¿Cuál es su área?
> 2. Si el costo de un componente es $(x^2 - 5x + 10)$ USD y compras $(2x)$ unidades, ¿cuál es el costo total?
> 3. $-\frac{3}{4}a^2b (8a - 4b + 12)$
> 4. Multiplica el monomio $(-2xy^2)$ por el trinomio $(-3x^2 + 5xy - y^2)$.

> [!success] Soluciones (Para el docente)
> **Fácil:** 1) $8a^7$, 2) $-15b^8$, 3) $x^5y^5$, 4) $16m^4$.
> **Medio:** 1) $2x^3 - 3x^2$, 2) $-2a^3 - 15a^2b$, 3) $10m^3n - 15mn^3$, 4) $-x^5 + 4x^4 - 2x^3$.
> **Avanzado:** 1) $12x^3 - 6x^2 + 3x$, 2) $2x^3 - 10x^2 + 20x$ USD, 3) $-6a^3b + 3a^2b^2 - 9a^2b$, 4) $6x^3y^2 - 10x^2y^3 + 2xy^4$.

---

## Mini-prueba de Autoevaluación

> [!question] Pregunta 1
> Al multiplicar $x^4 \cdot x^2$, ¿el resultado es $x^8$ o $x^6$?
> **Respuesta:** Es **$x^6$**. Los exponentes se **suman** ($4+2=6$), no se multiplican.

> [!question] Pregunta 2
> Resuelve mentalmente: $(-4x^3)(2x^{-1})$
> **Respuesta:** $-8x^2$. 
> **Explicación:** S: $(-)(+) = -$; N: $4 \times 2 = 8$; L: Sumamos $3 + (-1)$, que es lo mismo que $3 - 1 = 2$.

> [!question] Pregunta 3
> Si una entrada al cine cuesta $x$ USD y van $(x + 8)$ personas, ¿cuál es el gasto total?
> **Respuesta:** $x^2 + 8x$ USD.
> **Explicación:** Multiplicamos el precio por cada término: $x(x) + x(8)$.

---

> [!tip] 💡 En la próxima clase
> Ya dominas cómo un monomio afecta a todo un grupo. Prepárate, porque en la siguiente lección veremos **Multiplicación de Polinomio por Polinomio**, donde aprenderás a multiplicar grupos grandes de términos entre sí. ¡Nos vemos allá!

> [!info] 🧭 Navegación
> ◀ **Anterior**: [[Clase 01 - Suma y Resta de Expresiones Algebraicas]]
> 🔽 **Índice**: [[00 - Índice del curso]]
> ▶ **Siguiente**: [[Clase 03 - Multiplicación de Polinomio por Polinomio]]