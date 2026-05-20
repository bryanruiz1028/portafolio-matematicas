# Clase 04 — Operaciones Combinadas con Números Enteros y Jerarquía de Operaciones

#algebra #operacionescomb
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 4 de 4

> [!info] 🧭 Navegación
> [[Clase 03|⬅ Clase 03]] | [[00 - Índice del curso|Índice]] | **Clase 04** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]

---

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> La jerarquía de operaciones es el "código de conducta" de las matemáticas. Sin estas reglas, un mismo cálculo podría dar múltiples resultados, lo que provocaría fallos catastróficos en la programación de computadoras, la construcción de puentes y el manejo de dinero a nivel mundial.

*   **💵 Finanzas:** Permite calcular correctamente el saldo final de una cuenta tras aplicar múltiples compras, impuestos y descuentos en el orden legal y lógico.
*   **🏗️ Construcción:** Es vital para calcular áreas complejas donde primero se deben elevar dimensiones al cuadrado antes de multiplicar por la cantidad de materiales.
*   **📊 Situación cotidiana:** Al dividir una cuenta de restaurante entre amigos, agrupando gastos comunes y sumando propinas de forma equitativa.

---

## Concepto clave

> [!note] 📌 ¿Qué es Operaciones combinadas con números enteros?
> Son ejercicios donde se mezclan sumas, restas, multiplicaciones, divisiones, potencias y raíces. Para un estudiante de 12 años, es como seguir una receta: no puedes hornear el pastel antes de mezclar los ingredientes. Debemos seguir un orden estricto llamado **Jerarquía de Operaciones**.

> [!warning] ⚠️ Error común
> El error más grave es resolver de izquierda a derecha por simple hábito de lectura.
> 
> **Ejemplo del Profe Alex:** $2 + 3 + 4 \times 0$
> *   ❌ **Incorrecto:** $2+3=5 \rightarrow 5+4=9 \rightarrow 9 \times 0 = \mathbf{0}$
> *   ✅ **Correcto:** Primero la multiplicación: $4 \times 0 = 0$. Luego las sumas: $2+3+0 = \mathbf{5}$

> [!tip] 💡 Truco para recordarlo: La Pirámide de Poder
> Para que no se te olvide, visualiza la jerarquía como una pirámide de prioridades:
> 
> 1.  **PARENTESIS** `( ) [ ] { }` (El "Escudo Protector": lo de adentro va primero).
> 2.  **POTENCIAS Y RAÍCES** `x²  √` (Las fuerzas especiales).
> 3.  **MULTIPLICACIÓN Y DIVISIÓN** `×  ÷` (El equipo de avance).
> 4.  **SUMA Y RESTA** `+  -` (La base, lo último que se resuelve).
> 
> **Nota técnica sobre los negativos:** ¡Cuidado! $-3^2$ no es lo mismo que $(-3)^2$. 
> - En $-3^2$, el exponente **solo** afecta al 3 (Resultado: $-9$).
> - En $(-3)^2$, el exponente afecta a todo el paréntesis (Resultado: $9$).

---

## Procedimiento Paso a Paso

Para resolver operaciones complejas, sigue estos pasos en orden:

```text
1. Resolver operaciones dentro de PARÉNTESIS.
2. Resolver POTENCIAS y RAÍCES.
3. Resolver MULTIPLICACIONES y DIVISIONES.
4. Resolver SUMAS y RESTAS.

*REGLA DE ORO: Si hay dos operaciones del mismo nivel (ej. multiplicación y división), se resuelven de IZQUIERDA A DERECHA.*
```

---

## Ejemplos Resueltos

```ad-example
title: Ejemplo 1 (Básico)
**Ejercicio:** $17 - 5 \times 2 + \sqrt{5+2^2}$

1. **Potencia dentro de raíz:** $2^2 = 4$. Queda $\sqrt{5+4}$.
2. **Suma dentro de raíz:** $5+4 = 9$. Queda $\sqrt{9}$.
3. **Resolver raíz:** $\sqrt{9} = 3$. La expresión es: $17 - 5 \times 2 + 3$.
4. **Multiplicación:** $5 \times 2 = 10$. La expresión es: $17 - 10 + 3$.
5. **Sumas y restas (Izquierda a derecha):** $17 - 10 = 7 \rightarrow 7 + 3 = 10$.
**Resultado:** 10
```

```ad-example
title: Ejemplo 2 (Con Signos y Raíces)
**Ejercicio:** $\sqrt{25} \times \sqrt{9} - 7 \times 2 + 15$

1. **Raíces:** $\sqrt{25} = 5$ y $\sqrt{9} = 3$. Queda: $5 \times 3 - 7 \times 2 + 15$.
2. **Multiplicaciones:** $5 \times 3 = 15$ y $7 \times 2 = 14$. Queda: $15 - 14 + 15$.
3. **Sumas y restas:** $15 - 14 = 1 \rightarrow 1 + 15 = 16$.
**Resultado:** 16
```

```ad-example
title: Ejemplo 3 (Avanzado - Ejemplo 7 del Profe Alex)
**Ejercicio:** $\sqrt{5(7-5)^2 - 4} + 3^2(2^3 - 5)$

1. **Paréntesis internos:** $(7-5)=2$ y $(2^3-5) = (8-5) = 3$.
2. **Potencias:** $2^2=4$ y $3^2=9$.
3. **Dentro de la raíz (Multiplicación):** $\sqrt{5 \times 4 - 4} = \sqrt{20 - 4}$.
4. **Dentro de la raíz (Resta):** $\sqrt{16}$.
5. **Raíz y Multiplicación externa:** $\sqrt{16} = 4$ y el otro término es $9 \times 3 = 27$.
6. **Suma final:** $4 + 27 = 31$.
**Resultado:** 31
```

```ad-example
title: Ejemplo 4 (Aplicación real $USD)
**Problema:** Tienes $100 USD. Compras 3 camisetas de $15 USD cada una y recibes un descuento que equivale a la $\sqrt{64}$ USD. ¿Cuánto dinero te queda?

**Operación:** $100 - (3 \times 15 - \sqrt{64})$
1. **Raíz dentro del paréntesis:** $\sqrt{64} = 8$.
2. **Multiplicación dentro del paréntesis:** $3 \times 15 = 45$.
3. **Resta dentro del paréntesis (Gasto neto):** $45 - 8 = 37$.
4. **Resta final:** $100 - 37 = 63$.
**Resultado:** Te quedan 63 USD.
```

---

## Ejercicios para el Estudiante

```ad-abstract
title: 🟢 Nivel Fácil
1. $10 + 5 \times 2$
2. $20 - 4 \times 3 + 2$
3. $8 + \sqrt{16} - 3$
4. $15 \div 3 + 4$
```

```ad-abstract
title: 🟡 Nivel Medio
1. $2 \times (5 + 3) - 10$
2. $\sqrt{25} \times 2 + 3^2$
3. $(10 - 2^2) \times 3$
4. $5 + \sqrt{15 - 6} \times 2$
```

```ad-abstract
title: 🔴 Nivel Avanzado
1. $3^2 - (-3^2)$
2. $100 - [ 5 \times (2^3 - 1) ]$
3. Compras 4 cuadernos a $5 USD c/u y 2 lápices a $1 USD c/u. Pagas con un billete de $50 USD. ¿Cuál es el cambio?
4. $-25 - [ \sqrt{25} - (-5)^2 ]$
```

```ad-success
title: Clave de Respuestas (Docente)
*   **Fácil:** 1) 20 | 2) 10 | 3) 9 | 4) 9
*   **Medio:** 1) 6 | 2) 19 | 3) 18 | 4) 11
*   **Avanzado:** 
    1) **18**. Explicación: $3^2 = 9$. Luego, $(-3^2)$ es $-(3 \times 3) = -9$. La operación queda $9 - (-9) = 9 + 9 = 18$.
    2) **65**. ($100 - [5 \times 7]$).
    3) **28 USD**. ($50 - [4 \times 5 + 2 \times 1]$).
    4) **-5**. ($-25 - [5 - 25] \rightarrow -25 - [-20] \rightarrow -25 + 20$).
```

---

## Mini-prueba de Autoevaluación

```ad-question
title: Pregunta 1
Según la jerarquía de operaciones, si tienes una suma y una multiplicación juntas, ¿cuál se debe resolver primero?
```

```ad-question
title: Pregunta 2
¿Cuál es el resultado de $2 + 3 + 4 \times 0$?
- A) 0
- B) 5
- C) 9
- D) 7
```

```ad-question
title: Pregunta 3 (El Desafío del Profe Alex)
¿Cuál es el resultado de $3^2 - (-3^2)$?
**Explicación técnica:** Recuerda que en el primer término el exponente afecta solo al 3 ($9$). En el segundo término, el cuadrado está dentro del paréntesis afectando solo al 3, dejando el signo negativo intacto dentro del paréntesis ($ -9 $). ¿Qué sucede cuando restas un número negativo?
```

---

## Cierre y Navegación Final

> [!tip] 💡 En la próxima clase
> ¡Felicidades por completar el Bloque 1! Ahora que dominas la jerarquía de operaciones y los números enteros, tienes los cimientos sólidos para entrar al mundo de las **Ecuaciones**. Usaremos estas mismas reglas para despejar incógnitas y resolver problemas del mundo real.

> [!info] 🧭 Navegación
> [[Clase 03|⬅ Clase 03]] | [[00 - Índice del curso|Índice]] | **Clase 04** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]