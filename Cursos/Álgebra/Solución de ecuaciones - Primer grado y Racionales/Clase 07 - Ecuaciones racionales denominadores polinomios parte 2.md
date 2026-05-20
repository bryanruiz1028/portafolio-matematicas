# Clase 07 — Ecuaciones racionales con denominadores polinomios — parte 2

---
[[Clase 06 — Ecuaciones racionales básicas]] | [[Clase 08 — Verificación y soluciones extrañas]]
---

> [!info] 🌍 **¿Por qué es importante esta clase?**
> En el mundo financiero, la rentabilidad no siempre es lineal. Resolver estas ecuaciones nos permite modelar **tasas de rendimiento** y **costos unitarios variables** donde el denominador representa factores dinámicos (como el volumen de producción o el riesgo). Por ejemplo, se utilizan para calcular el punto exacto en el que dos inversiones con diferentes estructuras de crecimiento alcanzan un equilibrio financiero.

### Conceptos Clave

> [!note] 📌 **Ecuaciones Racionales Avanzadas**
> Son aquellas donde los denominadores son polinomios (trinomios o binomios complejos). La clave del éxito no está en operar de inmediato, sino en realizar una **factorización exhaustiva** para identificar el Mínimo Común Múltiplo (MCM). Sin factorizar, el proceso se vuelve algebraicamente inmanejable.

> [!warning] ⚠️ **¡Cuidado con el colapso del modelo!**
> El error más crítico es olvidar verificar la solución final. Si obtienes, por ejemplo, $x=2$ y uno de tus denominadores originales era $(x-2)$, estarías dividiendo por cero. En un contexto real, esto significa que tu modelo financiero colapsa. Estas se conocen como **soluciones extrañas** y deben ser descartadas.

> [!tip] 💡 **Truco de Experto**
> Observa con atención: casi siempre, los factores de los denominadores más simples (los binomios) están "escondidos" dentro de los denominadores más complejos (los trinomios). Úsalos como una pista para factorizar más rápido.

---

### Procedimiento Paso a Paso

```text
PASO 1: Factorizar todos los denominadores (Trinomios x² + bx + c, 
        diferencia de cuadrados o factor común numérico).
PASO 2: Identificar el MCM utilizando todos los factores encontrados 
        sin repetirlos (a menos que tengan potencias distintas).
PASO 3: Multiplicar toda la ecuación por el MCM para eliminar las 
        fracciones y convertirla en una ecuación lineal o cuadrática.
PASO 4: Resolver la ecuación resultante y verificar obligatoriamente 
        que el resultado no anule ningún denominador original.
```

---

### Bloques de Ejemplos Técnicos

#### Ejemplo 6 — Caso Ecuación Cuadrática
**Ecuación:** $\frac{5x+1}{x^2-4} - \frac{1}{x+2} = \frac{x}{x-2}$

1.  **Factorización:** Identificamos que $x^2-4$ es una diferencia de cuadrados: $(x+2)(x-2)$.
2.  **MCM:** El MCM es $(x+2)(x-2)$.
3.  **Eliminación y Distribución Crítica:** Multiplicamos cada término.
    $$(5x+1) - 1(x-2) = x(x+2)$$
    *Atención aquí:* El signo negativo afecta a todo el paréntesis.
    $$5x + 1 - x + 2 = x^2 + 2x$$
4.  **Resolución Cuadrática:** Agrupamos términos: $4x + 3 = x^2 + 2x \rightarrow 0 = x^2 - 2x - 3$.
5.  **Resultado:** Factorizamos el trinomio resultante $(x-3)(x+1) = 0$. Obtenemos **$x=3$** y **$x=-1$**.

#### Ejemplo 7 — Caso con Factor Común Numérico
**Ecuación:** $\frac{3x-1}{x^2+7x+12} = \frac{1}{2x+6} + \frac{7}{6x+24}$

1.  **Factorización:**
    *   Trinomio: $(x+4)(x+3)$.
    *   Binomios: $2(x+3)$ y $6(x+4)$.
2.  **MCM:** Para los números 2 y 6, el MCM es 6 (ya que el 6 contiene al 2). El MCM total es $6(x+4)(x+3)$.
3.  **Expansión Lineal Detallada:** Multiplicamos todo por el MCM:
    $$6(3x-1) = 3(x+4) + 7(x+3)$$
    $$18x - 6 = 3x + 12 + 7x + 21$$
    $$18x - 6 = 10x + 33$$
4.  **Resultado:** $8x = 39 \rightarrow$ **$x = 39/8$**.

#### Ejemplo 8 — Caso de Tres Trinomios y Verificación
**Ecuación:** $\frac{4}{x^2+4x+3} + \frac{2}{x^2+x-6} = \frac{3}{x^2-x-2}$

1.  **Factorización:** $(x+3)(x+1)$, $(x+3)(x-2)$ y $(x-2)(x+1)$.
2.  **MCM:** $(x+3)(x+1)(x-2)$.
3.  **Ecuación resultante:** $4(x-2) + 2(x+1) = 3(x+3)$.
    $$4x - 8 + 2x + 2 = 3x + 9 \rightarrow 6x - 6 = 3x + 9 \rightarrow 3x = 15 \rightarrow x = 5$$
4.  **Modelado de Verificación:** Sustituimos $x=5$ en la ecuación simplificada (paso 3):
    $4(5-2) + 2(5+1) = 3(5+3)$
    $4(3) + 2(6) = 3(8) \rightarrow 12 + 12 = 24 \rightarrow \mathbf{24 = 24}$.
    En la ecuación original simplificada, esto equivale a demostrar la identidad **$1/6 = 1/6$**. ¡Correcto!

#### Ejemplo 9 — Aplicación Práctica: Costo por Transacción ($USD)
**Contexto:** En un sistema de ventas masivas, el costo variable por transacción se modela con la ecuación: $\frac{2}{x^2-x-6} - \frac{3}{x^2-2x-3} = \frac{6}{x^2+3x+2}$. El denominador representa un factor de costo dinámico que cambia de forma no lineal con el volumen de ventas $x$ (en miles de unidades).

1.  **Factorización y MCM:** Los denominadores son $(x-3)(x+2)$, $(x-3)(x+1)$ y $(x+2)(x+1)$. El MCM es $(x-3)(x+2)(x+1)$.
2.  **Ecuación Lineal:** $2(x+1) - 3(x+2) = 6(x-3)$.
3.  **Resolución:** $2x+2 - 3x-6 = 6x-18 \rightarrow -x-4 = 6x-18 \rightarrow 14 = 7x \rightarrow x=2$.
**Conclusión:** El punto de equilibrio del costo ocurre a las **2,000 unidades**.

---

### Ejercicios para el Estudiante

*   🟢 **Fácil:** Resuelve $\frac{2x}{x+2} - \frac{x-1}{x-2} = \frac{1-9x}{x^2-4}$
*   🟡 **Medio:** Resuelve $\frac{2}{x+2} - \frac{1}{2x-1} = \frac{5}{(x+2)(2x-1)}$
*   🔴 **Avanzado (Distribución de Presupuesto):** Un analista financiero debe distribuir un fondo de emergencia basándose en la ecuación: $\frac{2}{x^2-x-6} - \frac{3}{x^2-2x-3} = \frac{6}{x^2+3x+2}$. Si $x$ representa el excedente presupuestario necesario para que la operación sea eficiente, determine dicho valor en USD por unidad.

---

> [!success] **Respuestas para el Docente**
> *   🟢 $x=3, x=-1$ (Nota: Ambas son válidas tras verificar).
> *   🟡 $x=1$
> *   🔴 $x=2$ USD/unidad.

---

### Mini-prueba de Autoevaluación
1.  **¿Cuál es el beneficio principal de factorizar antes de calcular el MCM?**
    *   Simplifica la expresión y permite ver factores repetidos, evitando multiplicar por términos innecesarios.
2.  **¿Qué ocurre matemáticamente si tu solución final es $x=3$ y tienes un denominador $(x-3)$?**
    *   Se produce una división por cero (indeterminación), por lo que la solución se descarta.
3.  **¿Por qué multiplicamos toda la ecuación por el MCM?**
    *   Para cancelar todos los denominadores y trabajar con una ecuación lineal o cuadrática mucho más sencilla.

---

> [!tip] 💡 **Próximo paso**
> En la Clase 08, nos enfocaremos exclusivamente en el arte de la **verificación**. Aprenderás a cazar "soluciones extrañas" antes de que arruinen tus cálculos en un examen o modelo real.

---
[[Clase 06 — Ecuaciones racionales básicas]] | [[Clase 08 — Verificación y soluciones extrañas]]