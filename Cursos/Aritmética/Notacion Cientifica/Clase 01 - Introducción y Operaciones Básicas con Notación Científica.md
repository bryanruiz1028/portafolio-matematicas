# Clase 01 — Introducción y Operaciones Básicas con Notación Científica
tags: #algebra #notacincientfic
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 3

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]

¡Qué tal amigos! Espero que estén muy bien. Bienvenidos al curso de Notación Científica. Hoy vamos a aprender a simplificar esos números que tienen tantos ceros que hasta nos marean, usando un método sencillo y lógico.

## 1. Importancia y Aplicaciones
La notación científica es una forma abreviada de escribir cantidades para evitar el manejo de excesivos ceros. Se utiliza para representar números "gigantes" o "pequeñísimos" de manera que podamos leerlos y operarlos fácilmente.

*   **Aplicación Financiera:** Permite manejar presupuestos nacionales de gran escala, como cifras de **7 mil millones** de dólares ($7 \times 10^9$), facilitando cálculos sin perderse entre tantos ceros.
*   **Aplicación en Ciencia:** Es vital para medir cosas microscópicas, como **fracciones pequeñísimas de un metro** (ej. 0.000000001 m), que en notación científica se lee mucho más rápido.
*   **Situación Cotidiana:** Nos ahorra el trabajo de contar manualmente cada cero en una cifra larga, evitando errores comunes al transcribir datos.

## 2. Concepto Clave
Para que un número esté correctamente escrito en notación científica, debe seguir esta estructura:
$$a \times 10^n$$

*   **El coeficiente "a":** Debe ser un número entre 1 y 10. **Pilas con esto:** el número puede ser el 1, pero **nunca puede llegar a ser 10**. Por ejemplo, 35.6 no sirve porque es mayor a 10.
*   **La base 10:** El exponente $n$ nos indica el "valor posicional". Por ejemplo, $10^2$ es un 1 con dos ceros (100), mientras que $10^{-1}$ representa un número pequeño (0.1).
*   **Truco del Profe Alex:** 
    *   **Números pequeños:** Son los que empiezan con **0.** (cero punto algo). Su exponente siempre será **negativo**.
    *   **Números grandes:** Son todos los demás. Su exponente siempre será **positivo**.

## 3. Procedimiento: La Lógica de Compensación
Para convertir cualquier número, el secreto está en mantener la balanza equilibrada. El punto decimal **siempre debe quedar a la derecha de la primera cifra que no sea cero**.

```text
PASO 1 → Identificar si es "grande" o "pequeño" (¿empieza con 0.?) para saber el signo del exponente.
PASO 2 → Ubicar el punto decimal. Si no lo ves (número entero), está al final.
PASO 3 → Mover el punto hasta la derecha de la primera cifra no nula.
PASO 4 → ¡Compensación!: 
         - Si mueves el punto a la IZQUIERDA, el número se hace más CHICO, 
           así que el exponente debe ser POSITIVO (para agrandarlo).
         - Si mueves el punto a la DERECHA, el número se hace más GRANDE, 
           así que el exponente debe ser NEGATIVO (para achicarlo).
```

## 4. Ejemplos Prácticos

> [!example] Ejemplo 1: Caso básico (Número grande)
> **Convertir 5000 a notación científica:**
> 1. El punto está al final: `5000.`
> 2. Movemos el punto 3 lugares a la izquierda: `5.000`
> 3. Como movimos a la izquierda (achicamos el número), el exponente es $+3$.
> 4. Borramos los ceros finales que ya no sirven: **$5 \times 10^3$**

> [!example] Ejemplo 2: Signos (Número pequeño)
> **Convertir 0.000572 a notación científica:**
> 1. Movemos el punto hacia la derecha hasta después del 5 (la primera cifra no nula).
> 2. Se desplazó 4 lugares: `5.72`
> 3. Al ser un número pequeño (empieza con 0.), el exponente es negativo: **$5.72 \times 10^{-4}$**

> [!example] Ejemplo 3: Multiplicación
> **Calcular $(2 \times 10^5) \times (3 \times 10^4)$:**
> 1. Multiplicamos los coeficientes: $2 \times 3 = 6$.
> 2. Sumamos los exponentes: $5 + 4 = 9$.
> 3. Resultado: **$6 \times 10^9$**

> [!example] Ejemplo 4: Aplicación Presupuestaria
> **Convertir 530 millones de dólares:**
> 1. Escribimos el número completo: `530,000,000`
> 2. Movemos el punto 8 espacios a la izquierda para que quede después del 5: `5.3`
> 3. Resultado: **$5.3 \times 10^8$ USD**

## 5. Ejercicios para el Estudiante

**Nivel Fácil**
1. Escribir $795$ en notación científica.
2. Escribir $0.03$ en notación científica.

**Nivel Medio**
3. Resolver la división: $(8 \times 10^6) / (4 \times 10^2)$.

**Nivel Avanzado ($USD)**
4. Divide un presupuesto de $1.43 \times 10^6$ USD entre $8.3 \times 10^2$ personas (redondea a 4 cifras decimales).

---
**Respuestas comentadas:**
1. **$7.95 \times 10^2$**: El punto se corrió 2 veces a la izquierda.
2. **$3 \times 10^{-2}$**: El punto se corrió 2 veces a la derecha.
3. **$2 \times 10^4$**: Dividimos $8/4=2$ y restamos exponentes $6-2=4$.
4. **$1.722 \times 10^3$**: 
   - Primero divides: $1.43 / 8.3 = 0.1722$.
   - Restas exponentes: $10^{6-2} = 10^4$.
   - Resultado inicial: $0.1722 \times 10^4$.
   - **Ajuste:** Como el punto debe estar después del 1, corremos la coma a la derecha (**agrandamos** el número a 1.722), así que debemos **achicar** el exponente ($4 - 1 = 3$).

## 6. Autoevaluación

1. **¿Cuál es la condición para el coeficiente "a"?**
   a) Debe ser mayor a 10.
   b) Debe ser $\ge 1$ y $< 10$ (el 10 no se incluye).
   c) Puede ser cualquier número decimal.

2. **Pilas: En una división, si el exponente de arriba es 6 y el de abajo es -5, ¿qué sucede?**
   a) $6 - (-5) = 11$.
   b) $6 - 5 = 1$.
   c) Se multiplican y da -30.

3. **¿Cómo se ve "1 millón" ($1,000,000$) en notación científica?**
   a) $1 \times 10^6$
   b) $1 \times 10^{-6}$
   c) $10 \times 10^5$

## 7. Cierre y Próximo Tema
¡Felicidades por terminar la primera clase! Ya sabes cómo convertir números y hacer operaciones básicas de multiplicación y división. Recuerda que la clave es la **compensación**: si mueves la coma para un lado, ajustas el exponente para el otro para mantener el equilibrio.

En la **Clase 02**, subiremos el nivel con la **Suma y Resta de Notación Científica**, donde aprenderemos qué hacer cuando los exponentes no son iguales. ¡Nos vemos en la próxima!

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]