# Clase 04 — Multiplicación y división de fracciones algebraicas
tags: #algebra #multiplicaciondefracciones #divisiondefracciones
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 4 de 4

> [!info] 🧭 Navegación
> [[Clase 03|⬅ Clase 03]] | [[00 - Índice del curso|Índice]] | **Clase 04** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]

## 1. ¿Por qué es importante esta clase?
Dominar la multiplicación y división de fracciones algebraicas es fundamental porque permite **reducir expresiones masivas a fórmulas simples y manejables**. Esta habilidad es la base para resolver problemas complejos en campos técnicos y financieros:

*   **Ingeniería y Construcción:** Se utiliza para el ajuste de escalas en planos. Una escala como $1:50$ es en realidad una fracción. Al ajustar dimensiones, multiplicamos o dividimos estas fracciones algebraicas para asegurar que las piezas encajen en el mundo real.
*   **Finanzas y Economía ($USD):** Se usa para hallar el **costo unitario**. Si el presupuesto total de un proyecto está representado por una expresión $A$ y la cantidad de unidades por una expresión $B$, la operación $A \div B$ nos da el precio exacto por unidad en dólares. 
*   **Situación Cotidiana:** En la industria alimentaria, se usa para ajustar proporciones de ingredientes en recetas industriales cuando el volumen de producción cambia dinámicamente.

---

## 2. Concepto clave
Multiplicar y dividir fracciones algebraicas es, en esencia, la misma operación. Según la pedagogía del Profe Alex, la división es simplemente multiplicar por el **inverso multiplicativo**.

> [!info] Definición para expertos
> *   **Multiplicar:** Es "unir" los numeradores y los denominadores en una sola fracción para simplificar factores comunes.
> *   **Dividir:** Es multiplicar la primera fracción por el **Inverso Multiplicativo** de la segunda (es decir, invertir la segunda fracción: el numerador pasa a ser denominador y viceversa).

> [!warning] Error común: El peligro de las sumas
> **NUNCA simplifiques términos que se están sumando o restando.** Solo puedes simplificar "bloques" completos (factores) que estén multiplicando. 
> 
> **Prueba numérica del error:** 
> Si tenemos $\frac{10+5}{5}$, el resultado real es $\frac{15}{5} = 3$. 
> Si cometieras el error de "tachar" el $5$ de arriba con el de abajo, te quedaría $10+1=11$. 
> Como $3 \neq 11$, queda demostrado que **no se simplifican sumas**.

**Truco Técnico:** Para convertir cualquier división en una multiplicación fácil, simplemente aplica el inverso multiplicativo a la segunda fracción.

---

## 3. Procedimiento paso a paso
Para resolver cualquier operación con éxito y evitar trabajar con polinomios gigantescos, sigue este orden universal. **El secreto es simplificar ANTES de multiplicar.**

```text
1. INVERTIR: Si es división, invierte la segunda fracción y cambia a multiplicación.
2. FACTORIZAR: Descompone numeradores y denominadores (Factor Común, Diferencia de Cuadrados, Trinomios).
3. SIMPLIFICAR: Tacha factores idénticos (uno de arriba con uno de abajo).
4. MULTIPLICAR: Une los factores que sobrevivieron para el resultado final.
```

---

## 4. Ejemplos Desarrollados

### Ejemplo 1: Multiplicación de Monomios
Calcular: $\frac{3x^2}{2y} \cdot \frac{y}{6x}$

1.  **Simplificar números:** Sacamos tercera de $3$ (es $1$) y tercera de $6$ (es $2$).
2.  **Simplificar letras:** La $y$ del numerador se simplifica con la $y$ del denominador ($y \div y = 1$). Una $x$ de abajo elimina una potencia del $x^2$ de arriba (queda solo $x$).
3.  **Multiplicar sobrantes:**
    *   Arriba: $1 \cdot x \cdot 1 = x$
    *   Abajo: $2 \cdot 1 \cdot 2 = 4$
    *   **Resultado:** $\frac{x}{4}$

### Ejemplo 2: Multiplicación con Polinomios
Calcular: $\left(\frac{x^2-1}{x^2+2x+1}\right) \cdot \left(\frac{x^2+2x}{x^2+x-2}\right)$

1.  **Factorizar (con chequeo mental):**
    *   $x^2-1 \rightarrow (x+1)(x-1)$ (Diferencia de cuadrados).
    *   $x^2+2x+1 \rightarrow (x+1)^2$ (Trinomio Cuadrado Perfecto: la raíz de $x^2$ es $x$, la de $1$ es $1$, y $2 \cdot x \cdot 1 = 2x$).
    *   $x^2+2x \rightarrow x(x+2)$ (Factor común $x$).
    *   $x^2+x-2 \rightarrow (x+2)(x-1)$ (Trinomio de la forma $x^2+bx+c$).
2.  **Simplificar:** Se eliminan los factores idénticos $(x-1)$ y $(x+2)$. También un $(x+1)$ de arriba con uno de los dos que hay abajo.
3.  **Resultado:** $\frac{x}{x+1}$

### Ejemplo 3: División Avanzada (Simplificación precisa)
Calcular: $\frac{x^3-x}{2x^2+6x} \div \frac{5x^2-5x}{2x+6}$

1.  **Invertir:** $\frac{x^3-x}{2x^2+6x} \cdot \frac{2x+6}{5x^2-5x}$
2.  **Factorizar:**
    *   $x^3-x = x(x+1)(x-1)$
    *   $2x^2+6x = 2x(x+3)$
    *   $2x+6 = 2(x+3)$
    *   $5x^2-5x = 5x(x-1)$
3.  **Simplificar Factores:** 
    *   El factor $(x+3)$ arriba y abajo se simplifica.
    *   El factor $(x-1)$ arriba y abajo se simplifica.
    *   **Ojo aquí:** El factor numérico $2$ del numerador ($2(x+3)$) se simplifica con el factor numérico $2$ del denominador ($2x(x+3)$).
    *   La $x$ que multiplica arriba ($x(x+1)$) se simplifica con la $x$ que acompaña al $2$ abajo ($2x$).
4.  **Resultado:** $\frac{x+1}{5x}$

### Ejemplo 4: Aplicación Financiera ($USD)
Supongamos que el costo total de producción de un software es $\frac{x^2-4}{5}$ USD. Para hallar el costo por licencia, debemos dividir este total por un factor de distribución de $\frac{x+2}{10}$ licencias. ¿Cuál es el costo unitario?

1.  **Planteamiento:** $\frac{x^2-4}{5} \div \frac{x+2}{10}$
2.  **Inverso Multiplicativo y Factorización:** $\frac{(x+2)(x-2)}{5} \cdot \frac{10}{x+2}$
3.  **Simplificar:** El factor $(x+2)$ se elimina. El número $10$ en el numerador dividido por $5$ en el denominador nos da un factor de $2$ arriba.
4.  **Resultado Final:** $2(x-2)$ USD por licencia.

---

## 5. Ejercicios para el estudiante

*   **🟢 Fácil:** $\frac{10a}{3b} \cdot \frac{9b^2}{5a^2}$
*   **🟡 Medio:** $\frac{x^2-9}{x^2-x-6} \div \frac{x+3}{4x-8}$ 
    *(Pista: Busca la Diferencia de Cuadrados y un factor común oculto en el denominador de la derecha).*
*   **🔴 Avanzado ($USD):** Una empresa tiene una utilidad neta de $\frac{x^2+5x+6}{x}$ USD. Si deciden repartirla entre $\frac{x+3}{2}$ socios, ¿cuántos dólares recibe cada socio?

### ✅ Respuestas para el docente:
*   **Fácil:** $\frac{6b}{a}$
*   **Medio:** $4$ (Todos los factores algebraicos se simplifican a $1$).
*   **Avanzado:** $\frac{2(x+2)}{x}$ USD.

---

## 6. Mini-prueba de autoevaluación

1.  **¿Cuál es el nombre técnico de "darle la vuelta" a la segunda fracción en una división?**
    a) Factor común.
    b) Inverso multiplicativo.
    c) Simplificación cruzada.

2.  **Según el Profe Alex, si al simplificar una multiplicación todos los términos del numerador y denominador se tachan, el resultado es:**
    a) $0$
    b) $1$
    c) No tiene solución.

3.  **En la expresión $\frac{x+5}{x}$, ¿podemos simplificar las $x$?**
    a) No, porque la $x$ de arriba es un término de una suma, no un factor.
    b) Sí, porque están en posiciones opuestas.
    c) Solo si multiplicamos por $USD$.

---

## 7. Notas para el próximo tema
Has aprendido a reducir expresiones complejas mediante la multiplicación y división, lo cual es como "limpiar el terreno" antes de construir. En la próxima clase, utilizaremos estas herramientas para resolver **Ecuaciones Fraccionarias**, donde buscaremos el valor exacto de la incógnita $x$ en problemas de ingeniería y finanzas.

> [!info] 🧭 Navegación
> [[Clase 03|⬅ Clase 03]] | [[00 - Índice del curso|Índice]] | **Clase 04** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]