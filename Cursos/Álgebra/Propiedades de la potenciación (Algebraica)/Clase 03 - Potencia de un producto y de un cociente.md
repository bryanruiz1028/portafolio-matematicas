# Clase 03 — Potencia de un producto y de un cociente

#algebra #potencyofaproduct

[[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | [[Clase 04|Clase 04 ➡]]

---

### ¿Por qué es importante esta clase?

Esta propiedad permite "desarmar" problemas complejos, distribuyendo el trabajo para simplificar la solución.
Es la herramienta clave para escalar valores en finanzas, ingeniería y ciencias de manera exacta.
Ayuda a identificar cuándo es válido aplicar leyes de potencias, evitando errores en sumas y restas.

*   **💵 Aplicación $USD:** Se utiliza para calcular el crecimiento de una inversión (interés compuesto) o para escalar presupuestos cuando el costo y la cantidad aumentan proporcionalmente.
*   **🏗️ Aplicación práctica:** En arquitectura y diseño, ayuda a calcular cómo cambia el área o el volumen de una estructura cuando se aplican factores de escala a sus dimensiones.
*   **📊 Situación cotidiana:** Es esencial en la ciencia para simplificar fórmulas de física o química donde varias variables están elevadas a una misma potencia.

---

> [!note] Concepto Clave: Distribución del Exponente
> **¿Qué es?** 
> La potencia de un producto o de un cociente nos indica que, cuando tenemos una multiplicación o una división dentro de un paréntesis elevada a un exponente, ese exponente se le debe "entregar" o distribuir a cada factor o término de la operación.
> - **Producto:** $(a \cdot b)^n = a^n \cdot b^n$
> - **Cociente:** $(\frac{a}{b})^n = \frac{a^n}{b^n}$ o también escrito como $(a \div b)^n = a^n \div b^n$.
> 
> > [!warning] Error común
> > ¡Cuidado! Estas propiedades **NUNCA** se aplican si hay una suma o resta dentro del paréntesis. Por ejemplo: $(a + b)^n$ **NO ES IGUAL** a $a^n + b^n$. Esta propiedad es exclusiva de la multiplicación y división.
> 
> > [!tip] Truco del Jefe
> > Imagina que el **exponente es el jefe** y el paréntesis es la **oficina**. El jefe entra y le reparte el mismo trabajo (el exponente) a todos los empleados que están multiplicando o dividiendo dentro de la oficina.

---

### Procedimiento Paso a Paso

```markdown
1. Identificar: Verifica que solo haya multiplicaciones o divisiones dentro del paréntesis.
2. Distribuir: Entrega el exponente externo a cada base (número o letra).
3. Multiplicar: Si una base ya tiene exponente, aplica "Potencia de una potencia" (multiplica los exponentes).
4. Resolver: Calcula el valor final de los coeficientes numéricos (ej. 5³ = 125).
```

---

### Ejemplos Resueltos

> [!ad-example] Ejemplo 1: Caso Básico
> **Problema:** Resolver $(x \cdot y)^3$
> **Solución:**
> Al ser un producto, el "jefe" (3) se reparte a cada factor:
> **Resultado:** $x^3 y^3$

> [!ad-example] Ejemplo 2: Caso con Signos (Regla Profe Alex)
> **Problema:** Resolver $(-\frac{x}{y})^4$ y $(-\frac{x}{y})^3$
> **Solución:**
> 1. Si el exponente es **par** (como el 4), el resultado siempre es **positivo**:
>    $(-\frac{x}{y})^4 = \frac{x^4}{y^4}$
> 2. Si el exponente es **impar** (como el 3), el resultado conserva el **negativo**:
>    $(-\frac{x}{y})^3 = -\frac{x^3}{y^3}$

> [!ad-example] Ejemplo 3: Caso Avanzado (Combinado)
> **Problema:** Simplificar $\frac{(2a^2b^3)^2}{a^3b}$
> **Solución:**
> 1. Distribuimos el exponente superior multiplicando: $\frac{2^2 \cdot a^{2\cdot2} \cdot b^{3\cdot2}}{a^3b} = \frac{4a^4b^6}{a^3b}$
> 2. Aplicamos la técnica de "eliminación": restamos los exponentes donde haya más para mantener resultados positivos.
>    - Para **a**: $4 - 3 = 1$ (queda arriba).
>    - Para **b**: $6 - 1 = 5$ (queda arriba).
> **Resultado:** $4ab^5$

> [!ad-example] Ejemplo 4: Aplicación $USD
> **Problema:** El costo de un servicio escala según $(C \cdot U)^2$, donde $C$ es el costo base y $U$ la cantidad de usuarios. Si $C=5$ y $U=10$, ¿cuál es el valor total?
> **Solución:**
> 1. Distribuimos: $(C \cdot U)^2 = C^2 \cdot U^2$
> 2. Sustituimos: $5^2 \cdot 10^2 = 25 \cdot 100$
> **Resultado:** 2,500 $USD.

---

### Ejercicios para el Estudiante

> [!ad-abstract] ¡A practicar!
> **🟢 Nivel Fácil (Distribución simple)**
> 1. $(m \cdot n)^{10}$
> 2. $(a \cdot b \cdot c)^5$
> 3. $(\frac{x}{z})^7$
> 4. $(3x)^2$
> 
> **🟡 Nivel Medio (Potencia de potencia y signos)**
> 5. $(-3x^2)^3$
> 6. $(-2a^3b^2)^4$
> 7. $(\frac{m^4}{n^2})^5$
> 8. $(\frac{-1}{3y^3})^2$
> 
> **🔴 Nivel Avanzado ($USD y simplificación)**
> 9. Simplifica: $\frac{(x^2y^3)^4}{x^5y^2}$
> 10. Simplifica: $\frac{(2a^3b)^3}{4a^2b^2}$
> 11. Un presupuesto $P$ se define como $(\frac{100C}{P})^2$. Simplifica la expresión en términos de costo $C$ y presupuesto $P$.
> 12. El valor de una inversión $I$ con usuarios $U$ es $\frac{(I^2 \cdot U)^3}{I \cdot U^2}$. Reduce la expresión al máximo.

---

> [!ad-success] Respuestas para el Docente
> 1. $m^{10}n^{10}$
> 2. $a^5b^5c^5$
> 3. $\frac{x^7}{z^7}$
> 4. $9x^2$
> 5. $-27x^6$ (Exponente impar conserva el negativo).
> 6. $16a^{12}b^8$ (Exponente par convierte a positivo).
> 7. $\frac{m^{20}}{n^{10}}$
> 8. $\frac{1}{9y^6}$ **(Nota: El negativo desaparece porque el exponente 2 es par).**
> 9. $x^3y^{10}$
> 10. $2a^7b$
> 11. $\frac{10000C^2}{P^2}$
> 12. $I^5U$

---

### Mini-Prueba de Autoevaluación

> [!ad-question] ¿Qué tanto aprendiste?
> 1. **Conceptual:** ¿Es correcto decir que $(x - 4)^2 = x^2 - 16$? Justifica tu respuesta basándote en la regla del "jefe en la oficina".
> 2. **Procedimental:** Resuelve la expresión $(\frac{3a^3}{b^2})^3$.
> 3. **Aplicación $USD:** El presupuesto de una startup se escala mediante la fórmula $\frac{(4B)^3}{B^2}$, donde $B$ es el presupuesto inicial. ¿Cuál es la forma simplificada?
>    - A) $12B$
>    - B) $64B^5$
>    - C) $64B$

---

> [!tip] Próximo paso
> ¡Excelente trabajo! Has dominado cómo distribuir y simplificar potencias. Prepárate para la **Clase 04**, donde exploraremos el comportamiento de los **Exponentes Negativos y el Exponente Cero**, herramientas clave para nunca dejar un resultado a medias.

[[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | [[Clase 04|Clase 04 ➡]]