# Clase 10 — Operaciones con Funciones: Resta, Multiplicación y División
tags: #algebra #restadefunciones #multiplicaciondefunciones #divisiondefunciones
Curso: [[00 - Índice del curso]] | Bloque 3 | Lección 10 de 12

> [!info] 🧭 Navegación
> [[Clase 09|⬅ Clase 09]] | [[00 - Índice del curso|Índice]] | **Clase 10** | | [[Clase 11|Clase 11 ➡]]

## 1. ¿Por qué es importante esta clase?

Operar funciones nos permite fusionar diferentes reglas matemáticas para crear un modelo único que describa situaciones complejas. En lugar de analizar datos aislados, unimos las expresiones para obtener respuestas directas sobre el comportamiento de un fenómeno.

*   **Relevancia:** Permite combinar modelos; por ejemplo, al restar la función de Costos a la de Ingresos, generamos la función de Utilidad (ganancia).
*   **USD:** En finanzas, calculamos la ganancia neta en dólares operando las funciones que representan las entradas y salidas de dinero de un negocio.
*   **Práctica:** La multiplicación es esencial para calcular áreas (largo $\times$ ancho) cuando las dimensiones varían, y la división permite hallar tasas de cambio o razones entre magnitudes.
*   **Cotidiana:** Se aplica al calcular descuentos: restamos la función del descuento al precio base para conocer el valor final a pagar.

## 2. Concepto clave

*   **Definición:** Operar funciones es generar una nueva expresión matemática a partir de dos o más funciones originales. En la resta y multiplicación, operamos los términos según las reglas algebraicas; en la **división**, la operación se expresa como una **fracción** donde el objetivo principal es simplificar mediante la factorización.
*   **Aviso de error (Warning):** ¡Cuidado con el signo negativo! En la resta, el signo menos afecta a **todos** los términos de la segunda función. Es obligatorio usar paréntesis para asegurar que cada término cambie de signo al "quitar los paréntesis".
*   **Truco (Tip):** En la multiplicación, los exponentes de bases iguales se suman ($x^a \cdot x^b = x^{a+b}$). En la división, antes de operar, debemos **factorizar** (buscar factor común, trinomios o diferencia de cuadrados) para "cancelar" factores idénticos arriba y abajo.
*   **Nota Pro (División):** Si después de organizar y buscar factorizaciones no es posible simplificar nada (como en $\frac{3x+1}{2x^2-3x}$), la fracción misma es el resultado final. No fuerces simplificaciones que no existen.

## 3. Procedimiento paso a paso

Para resolver estas operaciones sin errores, sigue este flujo de trabajo universal:

```text
1. IDENTIFICAR Y ESCRIBIR: Escribe las funciones protegidas por paréntesis, 
   colocando el signo de la operación (+, -, ·, /) entre ellas.
2. ORGANIZAR: Antes de operar o factorizar, ordena los términos de mayor a 
   menor exponente (ej. x², luego x, luego el número). ¡Es vital para no perderse!
3. EJECUTAR LA OPERACIÓN:
   - Resta: "Quitar paréntesis" cambiando el signo de todo el segundo polinomio.
   - Multiplicación: Aplicar propiedad distributiva término a término.
   - División: Acomodar como fracción y buscar factores comunes o trinomios.
4. SIMPLIFICAR Y ORDENAR: Reduce términos semejantes y escribe el resultado 
   final en orden descendente.
```

## 4. Ejemplos de aplicación

### Ejemplo 1: Resta básica (Lineal)
Dadas $f(x) = 3x + 2$ y $g(x) = 2x - 1$, halla $f(x) - g(x)$:
1. Escribimos con paréntesis: $(3x + 2) - (2x - 1)$
2. Quitamos paréntesis (cambio de signos): $3x + 2 - 2x + 1$
3. Reducimos términos semejantes: $(3x - 2x) + (2 + 1) = \mathbf{x + 3}$

### Ejemplo 2: Resta con cambios de signo múltiples
Si $f(x) = 2x^2 - 3x + 1$ y $g(x) = x^2 + 6x - 2$, halla $f(x) - g(x)$:
1. Planteamos: $(2x^2 - 3x + 1) - (x^2 + 6x - 2)$
2. Aplicamos el negativo: $2x^2 - 3x + 1 - x^2 - 6x + 2$
3. Agrupamos y resolvemos: $\mathbf{x^2 - 9x + 3}$

### Ejemplo 3: División avanzada (Factorización)
Divide $f(x) = x^2 + 4x + 3$ entre $h(x) = x^2 - 9$:
1. Expresamos como fracción: $\frac{x^2 + 4x + 3}{x^2 - 9}$
2. Factorizamos (Trinomio arriba, Diferencia de cuadrados abajo):
   $\frac{(x+3)(x+1)}{(x+3)(x-3)}$
3. Simplificamos el factor repetido $(x+3)$:
   **Resultado:** $\mathbf{\frac{x+1}{x-3}}$  *(Nota: Válido para $x \neq 3$ y $x \neq -3$)*.

### Ejemplo 4: Multiplicación de Ingresos (USD)
Si el precio fijo de un producto es $P(x) = 15$ USD y la cantidad vendida es $Q(x) = 4x^2 - 2x$, halla el ingreso $I(x)$:
1. Operamos: $15 \cdot (4x^2 - 2x)$
2. Distribuimos: $(15 \cdot 4)x^2 - (15 \cdot 2)x$
3. **Resultado:** $I(x) = \mathbf{60x^2 - 30x}$

## 5. Ejercicios para el estudiante

### Nivel Verde (Fácil)
1. Si $f(x) = 5x + 10$ y $g(x) = 2x + 4$, halla $f(x) - g(x)$.
2. Multiplica $f(x) = 2x$ por $g(x) = 5x - 3$.
3. Resta $(2x^2 + 4x) - (2x^2 - 5x)$.
4. Si $h(x) = 3$, calcula $h(x) \cdot (x^2 + 2)$.

### Nivel Amarillo (Medio)
5. Divide $f(x) = 4x^2 + 2x$ entre $g(x) = 2x$ (Usa factor común).
6. Divide $f(x) = x^2 + x - 12$ entre $g(x) = x - 3$ (Factoriza el trinomio).
7. Multiplica $(x + 1)$ por $(x^2 - 2x + 4)$.
8. Halla la resta de $g(x) = 3x^2 - 5$ menos $f(x) = 4x^2 + x$.

### Nivel Rojo (Avanzado - Aplicación USD)
9. Una tienda tiene ingresos $I(x) = 3x^2 + 2x$ y costos $C(x) = 2x^2 - 3x - 5$. Halla la utilidad $U(x) = I(x) - C(x)$. *(¡Cuidado con los signos!)*.
10. Divide $f(x) = \frac{x+3}{x-1}$ entre $g(x) = \frac{4}{x-1}$ usando la **"Ley de la oreja"**.
11. Halla el resultado de multiplicar $f(x) = (x+5)$ por $g(x) = (x+5)$.
12. Divide $f(x) = x - 3$ entre $g(x) = x^2 + x - 12$. *(Pista: El numerador no puede quedar vacío)*.

---
### Respuestas para el docente
1. $3x + 6$ | 2. $10x^2 - 6x$ | 3. $9x$ | 4. $3x^2 + 6$ | 5. $2x + 1$ | 6. $x + 4$ | 7. $x^3 - x^2 + 2x + 4$ | 8. $-x^2 - x - 5$ | 9. $x^2 + 5x + 5$ | 10. $\frac{x+3}{4}$ | 11. $x^2 + 10x + 25$ | 12. $\frac{1}{x+4}$

## 6. Mini-prueba de autoevaluación

**1. Al realizar la resta $f(x) - g(x)$, ¿cuál es el error más común que debemos evitar?**
a) Olvidar sumar los exponentes.
b) Cambiar el signo solo al primer término de $g(x)$ y no a todos.
c) Multiplicar las funciones en lugar de restarlas.
d) No ordenar los términos al final.

**2. ¿Cuál es el requisito indispensable que menciona el Profe Alex antes de empezar a factorizar en una división?**
a) Que todos los signos sean positivos.
b) Que los polinomios ya estén organizados (de mayor a menor grado).
c) Que no existan términos independientes.
d) Multiplicar el numerador por el denominador.

**3. Si el precio unitario es $P(x) = 4x$ y vendemos una cantidad $Q(x) = 2x$, ¿cuál es la función de ingreso en USD?**
a) $8x$
b) $6x^2$
c) $8x^2$
d) $42x$

---
**Clave de respuestas:**
1. **b** (El uso de paréntesis es vital para afectar a toda la expresión).
2. **b** (Sin orden, es muy difícil identificar trinomios o factores comunes).
3. **c** (Se multiplican coeficientes $4 \cdot 2 = 8$ y se suman exponentes $x^1 \cdot x^1 = x^2$).

## 7. Notas para el próximo tema

En la siguiente clase estudiaremos la **Composición de Funciones**. Es fundamental no confundirla con la multiplicación. Mientras que en la multiplicación usamos un **punto** ($f \cdot g$), en la composición usamos un **círculo** ($f \circ g$). Componer no es multiplicar expresiones, sino "inyectar" o meter una función dentro de la otra, reemplazando cada $x$ por la expresión completa de la segunda función.

> [!info] 🧭 Navegación
> [[Clase 09|⬅ Clase 09]] | [[00 - Índice del curso|Índice]] | **Clase 10** | | [[Clase 11|Clase 11 ➡]]