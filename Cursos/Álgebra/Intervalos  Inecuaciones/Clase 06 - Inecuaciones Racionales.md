# Clase 06 — Inecuaciones Racionales

tags: #algebra #inecuacionesrac
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 6 de 9

> [!info] 🧭 Navegación
> - Clase Anterior: [[Clase 05 — Inecuaciones Cuadráticas]]
> - Índice: [[00 - Índice del curso]]
> - Siguiente Clase: [[Clase 07 — Inecuaciones con Valor Absoluto]]

---

> [!info] 🌍 Relevancia y aplicaciones
> Las inecuaciones racionales nos permiten modelar situaciones donde comparamos razones, tasas de cambio o proporciones que dependen de una variable en el denominador. Son herramientas vitales para la toma de decisiones basada en límites críticos.
> 
> - **💵 Aplicación $USD:** Se aplican en el análisis de **costo promedio por unidad** ($C/x$). Por ejemplo, determinar cuántas unidades $x$ deben producirse para que el costo unitario sea inferior a un presupuesto de $15 USD.
> - **🏗️ Aplicación práctica:** En ingeniería civil y de materiales, se usan para asegurar que las **proporciones de mezclas** (como cemento/arena) se mantengan dentro de rangos seguros de resistencia.
> - **📊 Situación cotidiana:** Permite resolver problemas de **tiempo compartido** o velocidad promedio, como calcular el tiempo necesario para completar una tarea cuando la eficiencia de un equipo varía.

---

> [!note] 📌 ¿Qué es Inecuaciones racionales?
> Una inecuación racional es una desigualdad donde la variable incógnita (usualmente $x$) se encuentra en el **denominador** de una fracción. Resolverla implica encontrar los intervalos de valores de $x$ que hacen que la división resultante sea positiva, negativa o igual a cero, según lo indique el signo de la desigualdad ($\leq, <, \geq, >$).

> [!warning] ⚠️ Error común
> **NUNCA multipliques cruzado** para eliminar denominadores que contengan variables. 
> *¿Por qué?* Si multiplicas la inecuación $\frac{1}{x} < 2$ por $x$, y resulta que $x$ es un número negativo, el signo de la desigualdad debería invertirse. Como no conocemos el valor de $x$ de antemano, no podemos saber si debemos girar el signo o no. El único camino seguro es **igualar a cero** y analizar los signos por intervalos.

> [!tip] 💡 Truco para recordarlo
> **"El suelo de la fracción es lava":** Matemáticamente, la división entre cero no existe (es una indefinición). Por eso, el denominador **nunca** puede ser cero. Esto significa que los puntos críticos que provengan del denominador siempre llevarán **paréntesis (abierto)** en la solución final, sin importar que la inecuación tenga el signo "o igual" ($\leq$ o $\geq$).

---

### PROCEDIMIENTO PASO A PASO

Para resolver inecuaciones racionales con éxito, sigue esta secuencia lógica:

1.  **Igualar a cero:** Mueve todos los términos a un lado de la desigualdad de modo que en el otro lado quede un $0$.
2.  **Factorización total:** Factoriza tanto el numerador como el denominador hasta obtener factores lineales (donde $x$ no tenga exponentes).
3.  **Hallar Puntos Críticos (PC):** Identifica los valores que hacen cero a cada factor de arriba y de abajo.
4.  **Ubicación en la recta:** Dibuja los **PC** en la recta numérica para dividirla en intervalos.
5.  **Análisis de signos:** Prueba un valor de cada intervalo en la expresión original para determinar si el resultado es positivo (+) o negativo (-) y elige los intervalos que cumplan con la desigualdad.

---

### EJEMPLOS DESARROLLADOS

```ad-example
title: Ejemplo 1: Caso Básico
**Resolver:** $\frac{x+4}{x-3} > 0$

1. **Puntos Críticos:** 
   - Numerador: $x + 4 = 0 \Rightarrow$ **PC: -4**
   - Denominador: $x - 3 = 0 \Rightarrow$ **PC: 3**
2. **Análisis:** Queremos los intervalos positivos ($>0$).
   - Intervalo $(-\infty, -4)$: Probamos $x = -5 \Rightarrow (-)/(-) = +$ (Sirve)
   - Intervalo $(-4, 3)$: Probamos $x = 0 \Rightarrow (+)/(-) = -$ (No sirve)
   - Intervalo $(3, \infty)$: Probamos $x = 4 \Rightarrow (+)/(+) = +$ (Sirve)
3. **Solución:** $(-\infty, -4) \cup (3, \infty)$
```

```ad-example
title: Ejemplo 2: Inclusión de Signos
**Resolver:** $\frac{x-2}{x+1} \leq 0$

1. **Puntos Críticos:** **PC: 2** (arriba) y **PC: -1** (abajo).
2. **Inclusión:** Debido al signo $\leq$, el valor de arriba ($2$) se incluye con **corchete**. El valor de abajo ($-1$) es "lava", por lo que siempre se queda con **paréntesis**.
3. **Análisis:** Buscamos resultados negativos o cero.
4. **Solución:** $(-1, 2]$
```

```ad-example
title: Ejemplo 3: Variable Negativa (Caso Avanzado)
**Resolver:** $\frac{4x-3}{3-x} \leq 0$

1. **Puntos Críticos:** **PC: 3/4** (arriba) y **PC: 3** (abajo).
2. **Análisis de signos:** ¡Atención! La $x$ negativa en el denominador $(3-x)$ invierte el orden habitual de los signos.
   - Si $x=0$ (izquierda): $(-)/(+) = -$ (**Sirve**)
   - Si $x=1$ (centro): $(+)/(+) = +$ (No sirve)
   - Si $x=4$ (derecha): $(+)/(-) = -$ (**Sirve**)
> [!tip] Pro-Tip
> Cuando una variable $x$ tiene signo negativo, los signos en la recta no suelen alternar de la forma clásica $(+ , - , +)$. Siempre verifica con un número de prueba.
3. **Solución:** $(-\infty, 3/4] \cup (3, \infty)$
```

```ad-example
title: Ejemplo 4: Aplicación Real $USD
**Problema:** Determinar cuándo el costo $\frac{2}{x+3}$ es menor o igual a la oferta $\frac{5}{2x-1}$.

1. **Igualar a cero:** $\frac{2}{x+3} - \frac{5}{2x-1} \leq 0$
2. **Operación (Carita feliz):** 
   $$\frac{2(2x-1) - 5(x+3)}{(x+3)(2x-1)} \leq 0 \Rightarrow \frac{4x - 2 - 5x - 15}{(x+3)(2x-1)} \leq 0$$
3. **Simplificación:** $\frac{-x - 17}{(x+3)(2x-1)} \leq 0$
4. **Puntos Críticos:** **PC: -17** (arriba), **PC: -3** y **PC: 1/2** (abajo).
5. **Solución:** $[-17, -3) \cup (1/2, \infty)$
```

---

### EJERCICIOS PARA EL ESTUDIANTE

```ad-abstract
title: 📝 Hoja de Trabajo

**🟢 Nivel Fácil (Lineales simples)**
1. $\frac{x-1}{x-5} > 0$
2. $\frac{x+2}{x+6} < 0$
3. $\frac{x-8}{x+2} \geq 0$
4. $\frac{x}{x-4} \leq 0$

**🟡 Nivel Medio (Inclusión y compuestos)**
5. $\frac{2x-4}{x+3} \geq 0$
6. $\frac{x+5}{3x-1} \leq 0$
7. $\frac{x^2-x-12}{x^2-1} \geq 0$
8. $\frac{x^2-3x-10}{x^2-2x} > 0$

**🔴 Nivel Avanzado (Aplicación $USD)**
9. Determine el rango de producción $x$ para que el costo unitario $\frac{4}{x-3}$ sea menor o igual a $\frac{1}{x+2}$.
10. Determine los valores de $x$ tales que: $\frac{5}{x+1} > \frac{2}{x-2}$
11. Resuelva la comparación de presupuestos: $\frac{3}{2x-4} \leq \frac{1}{x+1}$
12. Una empresa halla que su balance es favorable si $\frac{10}{x+5} \geq \frac{5}{x}$. Determine el intervalo.
```

> [!success] ✅ Respuestas para el Docente (Soluciones exactas)
> 1. $(-\infty, 1) \cup (5, \infty)$ | 2. $(-6, -2)$ | 3. $(-\infty, -2) \cup [8, \infty)$ | 4. $[0, 4)$
> 5. $(-\infty, -3) \cup [2, \infty)$ | 6. $[-5, 1/3)$ | 7. $(-\infty, -3] \cup (-1, 1) \cup [4, \infty)$ | 8. $(-\infty, -2) \cup (0, 2) \cup (5, \infty)$
> 9. $(-\infty, -11/3] \cup (-2, 3)$ | 10. $(-1, 2) \cup (4, \infty)$ | 11. $(-\infty, -7] \cup (-1, 2)$ | 12. $(-5, 0) \cup [5, \infty)$

---

### AUTOEVALUACIÓN Y CIERRE

```ad-question
title: Pregunta 1: Teoría
¿Por qué el punto crítico del denominador nunca se incluye en la solución final?
- a) Porque el signo de la inecuación siempre es estricto.
- b) Porque la división entre cero es una indefinición matemática (lava).
- c) Porque los números negativos no pueden estar abajo.
- d) Solo se excluye si la inecuación es de tipo "mayor que".

**Respuesta correcta: b.** Cualquier valor que haga cero el denominador rompe la operación matemática.
```

```ad-question
title: Pregunta 2: Procedimiento
En la inecuación $\frac{x-5}{x+3} \leq 0$, ¿cómo se representan los puntos críticos en el resultado?
- a) 5 con corchete y -3 con corchete.
- b) 5 con paréntesis y -3 con paréntesis.
- c) 5 con corchete y -3 con paréntesis.
- d) -5 con paréntesis y 3 con corchete.

**Respuesta correcta: c.** El 5 es del numerador (incluido por el $\leq$) y el -3 es del denominador (siempre excluido).
```

```ad-question
title: Pregunta 3: Problema rápido $USD
Se requiere que el beneficio $\frac{x-1}{x+2}$ sea negativo para aplicar un descuento. ¿Qué intervalo de $x$ lo cumple?
- a) $x > 1$
- b) $x < -2$
- c) $(-2, 1)$
- d) $(-\infty, -2) \cup (1, \infty)$

**Respuesta correcta: c.** Al analizar los puntos críticos **PC: 1** y **PC: -2** en la recta, el intervalo central da como resultado un signo negativo $(-)/(+) = -$.
```

> [!tip] 💡 En la próxima clase
> Expandiremos nuestro dominio de los intervalos al estudiar **Inecuaciones con Valor Absoluto**, donde una sola expresión puede esconder dos inecuaciones distintas.

---

> [!info] 🧭 Navegación
> - Clase Anterior: [[Clase 05 — Inecuaciones Cuadráticas]]
> - Índice: [[00 - Índice del curso]]
> - Siguiente Clase: [[Clase 07 — Inecuaciones con Valor Absoluto]]