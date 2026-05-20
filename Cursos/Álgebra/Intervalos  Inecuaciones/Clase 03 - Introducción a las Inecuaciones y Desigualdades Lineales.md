# Clase 03 — Introducción a las Inecuaciones y Desigualdades Lineales
tags: #algebra #inequalitiesint
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 9

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | | [[Clase 04|Clase 04 ➡]]

## 1. ¿Por qué es importante esta clase?
Las inecuaciones son herramientas matemáticas fundamentales para comparar expresiones que no son iguales, permitiéndonos establecer **límites y rangos** de valores en lugar de una solución única. Mientras que una ecuación busca un punto exacto, la inecuación define un conjunto de posibilidades.

**Aplicaciones prácticas:**
*   💵 **Finanzas:** Determinar si el costo de una compra (ej. $x + 1$) excede un presupuesto máximo de $10 USD para mantener la rentabilidad.
*   🏗️ **Ingeniería:** Calcular los límites de carga en una viga estructural para asegurar que el peso sea menor o igual a su capacidad de resistencia.
*   📊 **Vida cotidiana:** Establecer rangos de velocidad permitidos en una carretera o monitorear que la temperatura de un refrigerador no suba de un máximo crítico.

## 2. Concepto clave
Basándonos en la metodología del **Profe Alex**, una **inecuación** es una desigualdad entre dos expresiones algebraicas conectadas por los signos: mayor que ($>$), menor que ($<$), mayor o igual que ($\geq$) o menor o igual que ($\leq$).

### 💡 El secreto de la lectura lógica
Para dominar las inecuaciones, debemos traducir el lenguaje algebraico al lenguaje común:
- **La Regla de la Variable:** Siempre leeremos la $x$ como **"los números"**. 
- **Ejemplo:** $x > 5$ se lee como *"los números mayores que cinco"*. Esto facilita enormemente la creación de intervalos y gráficas.

> [!warning] El error del 90% de los estudiantes
> A diferencia de las ecuaciones, si multiplicas o divides ambos lados de una inecuación por un **número negativo**, el sentido de la desigualdad **debe cambiar** obligatoriamente. Si no lo haces, la solución será totalmente errónea.

> [!tip] La técnica del "-1" (Recomendada)
> Para evitar confusiones con los signos, si al final del despeje la $x$ tiene un coeficiente negativo (ej. $-2x < 8$), multiplica toda la inecuación por $-1$. Esto hará que la $x$ sea positiva, pero recuerda: **se cambian los signos de todos los términos y se voltea el símbolo de la desigualdad**.

## 3. Procedimiento paso a paso
Para resolver inecuaciones lineales (de primer grado) de forma profesional y sin errores, seguiremos este orden lógico:

```text
PASO 1: Identificación y Limpieza
- Verifique que el exponente máximo de "x" sea 1.
- Elimine denominadores: Calcule el MCM y divídalo por cada denominador antes de multiplicar.
- Elimine paréntesis usando la propiedad distributiva.

PASO 2: Transposición Estratégica
- Mueva los términos con "x" SIEMPRE a la izquierda y las constantes a la derecha. 
- ¿Por qué? Porque si "x" está a la izquierda, el símbolo de la desigualdad apuntará 
  hacia la misma dirección que la flecha en la gráfica (ej. x > 2 apunta a la derecha).

PASO 3: Reducción de términos
- Sume o reste los términos semejantes en cada lado de la desigualdad.

PASO 4: Despeje y "Técnica del -1"
- Deje la "x" sola. Si el coeficiente de x es negativo, aplique la Técnica del -1 antes de pasar a dividir.

PASO 5: Verificación (Paso Maestro)
- Elija un número dentro del intervalo resultante y sustitúyalo en la inecuación 
  original para confirmar que la desigualdad se cumple.
```

## 4. Ejemplos Prácticos

### Ejemplo 1: Básico (Lectura y Gráfica)
**Resolver:** $7x + 5 < 2x - 10$
1. **Transposición:** $7x - 2x < -10 - 5$
2. **Reducción:** $5x < -15$
3. **Despeje:** $x < \frac{-15}{5} \Rightarrow x < -3$
*   **Lectura:** "Los números menores que -3".
*   **Intervalo:** $(-\infty, -3)$ — Usamos paréntesis porque el -3 no está incluido (círculo abierto).

### Ejemplo 2: Aplicación de la Técnica del -1
**Resolver:** $3x \geq 5x + 8$
1. **Transposición:** $3x - 5x \geq 8$
2. **Reducción:** $-2x \geq 8$
3. **Aplicar Técnica del -1:** Multiplicamos todo por $-1$: $2x \leq -8$ (Note cómo cambió el sentido).
4. **Despeje:** $x \leq \frac{-8}{2} \Rightarrow x \leq -4$
*   **Lectura:** "Los números menores o iguales que -4".
*   **Intervalo:** $(-\infty, -4]$ — Usamos corchete porque el -4 sí está incluido (círculo cerrado).

### Ejemplo 3: Fracciones con MCM
**Resolver:** $\frac{5x-3}{6} + \frac{x-5}{18} > \frac{x+1}{3}$
1. **MCM de 6, 18 y 3:** Es **18**.
2. **División del MCM por denominadores:**
   - $18 \div 6 = 3$
   - $18 \div 18 = 1$
   - $18 \div 3 = 6$
3. **Multiplicación de numeradores:** $3(5x - 3) + 1(x - 5) > 6(x + 1)$
4. **Operación:** $15x - 9 + x - 5 > 6x + 6 \Rightarrow 16x - 14 > 6x + 6$
5. **Transposición y Reducción:** $16x - 6x > 6 + 14 \Rightarrow 10x > 20$
6. **Resultado:** $x > 2$
*   **Intervalo:** $(2, \infty)$

### Ejemplo 4: Aplicación Presupuesto ($USD)
Como vimos en la introducción, si un gasto $x$ más una comisión de $\$1$ debe superar los $\$10$ para una promoción:
**Inecuación:** $x + 1 > 10 \Rightarrow x > 9$.
*   **Solución:** El gasto debe pertenecer al intervalo $(9, \infty)$ dólares.

## 5. Ejercicios para el estudiante

### 🟢 Nivel Fácil (Despeje directo)
1. $3x - 3 > 15$
2. $x + 5 \leq 12$
3. $2x > 10$
4. $4x - 8 < 0$

### 🟡 Nivel Medio (Paréntesis y Coeficientes Negativos)
1. $2(3x + 5) \leq x - 1$
2. $-3x + 4 > 10$
3. $5(x - 2) \geq 2(x + 4)$
4. $-(x + 3) < 5$

### 🔴 Nivel Avanzado (Fracciones y Contexto Real)
1. $\frac{2x}{3} - \frac{x}{4} \geq 5$
2. $\frac{x-1}{2} + \frac{x+1}{3} < 4$
3. $\frac{3x-2}{5} \leq \frac{x}{2}$
4. **Problema Financiero:** Si un servicio tiene un cargo fijo de $\$15$ USD y cada artículo adicional cuesta $\$2$ USD, ¿cuántos artículos ($x$) se pueden adquirir si el presupuesto total debe ser estrictamente menor a $\$45$ USD? Plantee la inecuación $2x + 15 < 45$ y resuelva.

---
### ✅ Respuestas para el docente
*   **Fácil:** 1. $(6, \infty)$ | 2. $(-\infty, 7]$ | 3. $(5, \infty)$ | 4. $(-\infty, 2)$
*   **Medio:** 1. $(-\infty, -11/5]$ | 2. $(-\infty, -2)$ | 3. $[6, \infty)$ | 4. $(-8, \infty)$
*   **Avanzado:** 1. $[12, \infty)$ | 2. $(-\infty, 21/5)$ | 3. $(-\infty, 4]$ | 4. $[0, 15)$ artículos (Nota: El límite es 15, pero el contexto financiero implica números positivos).

## 6. Mini-prueba de autoevaluación
1. **¿Qué representa un círculo cerrado (punto relleno) en la gráfica de una inecuación?**
   - a) Que el número no es parte de la solución.
   - b) Que la inecuación incluye los signos $\leq$ o $\geq$ y el número es parte de la solución.
   - c) Que el infinito es positivo.

2. **Si multiplicas la inecuación $-x < 5$ por $-1$, el resultado es:**
   - a) $x < -5$
   - b) $x > -5$
   - c) $-x > -5$

3. **Un presupuesto de "máximo $\$50$ USD" para un gasto $x$ se representa como:**
   - a) $x < 50$
   - b) $x \geq 50$
   - c) $x \leq 50$

## 7. Notas para el próximo tema
¡Felicidades! Has dominado las bases de las desigualdades. En la **Clase 04**, subiremos de nivel hacia las **Inecuaciones Cuadráticas**. Allí aprenderemos por qué el método de transposición simple no es suficiente y descubriremos el famoso "Método del Cementerio" o de puntos críticos para analizar signos en parábolas.

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | | [[Clase 04|Clase 04 ➡]]