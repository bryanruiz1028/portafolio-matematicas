# Clase 06 — Ecuaciones racionales con denominadores polinomios — parte 1

#algebra #ecuaciones

Curso: [[00 - Índice del curso]] | Bloque II | Lección 06 de 11

> [!info] 🧭 Navegación
> ◀️ [[Clase 05 - Ecuaciones racionales con denominadores monomios]] | 🏠 [[00 - Índice del curso]] | [[Clase 07 - Ecuaciones racionales parte 2]] ▶️

---

¡Hola! Qué gusto saludarte de nuevo. Hoy daremos un paso muy importante en nuestro camino por el álgebra. No te preocupes si al principio ves expresiones más largas; vamos a ir paso a paso, como siempre, para que domines este tema con total confianza. ¡Empecemos!

## RELEVANCIA: ¿Por qué es importante esta clase?

Las ecuaciones racionales no son solo teoría; son la base de la **gestión financiera moderna**. Se utilizan para modelar situaciones donde una cantidad fija debe distribuirse entre variables que cambian, como los rendimientos de inversión o la repartición de costos compartidos.

**Ejemplo práctico ($USD):**
Imagina que un grupo de inversores planea repartir una ganancia de **$10,000 USD**. El monto que recibe cada uno depende de cuántos socios activos haya ($x$) y de una serie de gastos operativos fijos. Si la estructura de costos es polinómica, necesitarás resolver una ecuación racional para saber exactamente cuánto dinero le corresponde a cada inversor. Dominar esto te da una ventaja competitiva en el análisis de escenarios económicos.

---

## CONCEPTO CLAVE

### Definición
Una **ecuación racional con denominador polinomio** es aquella donde la incógnita ($x$) aparece en el denominador formando parte de un binomio o trinomio (por ejemplo, $x+2$ o $x^2-9$). A diferencia de las clases anteriores, aquí el denominador tiene sumas o restas que debemos manejar con cuidado.

### Error Común ⚠️
1.  **El peligro del signo negativo:** Cuando hay un signo "menos" antes de una fracción, ese signo afecta a **todos** los términos del numerador una vez que eliminamos los denominadores. ¡Es el error número uno en los exámenes!
2.  **Términos "olvidados":** Es vital multiplicar **cada término** de la ecuación por el Mínimo Común Múltiplo (MCM), incluso aquellos que son números enteros (como un $1$ o un $2$) y no parecen fracciones.

### Truco / Atajo 💡
*   **Productos Cruzados:** Si tienes una sola fracción a cada lado ($\frac{a}{b} = \frac{c}{d}$), simplemente multiplica en cruz: $a(d) = c(b)$.
*   **Factorización Estratégica:** Antes de calcular el MCM, revisa si hay términos cuadráticos. Factorizar una diferencia de cuadrados como $x^2-1$ en $(x+1)(x-1)$ te ahorrará muchísimo trabajo de cálculo.

---

## PROCEDIMIENTO PASO A PASO

Sigue este orden para resolver cualquier ejercicio de forma organizada:

```text
PASO 1: Factorizar denominadores cuadráticos para identificar los factores base.
PASO 2: Hallar el MCM de todos los denominadores (toma los factores repetidos una sola vez).
PASO 3: Multiplicar cada término por el MCM para limpiar la ecuación de fracciones.
PASO 4: Resolver la ecuación resultante (ya sea lineal o cuadrática).
PASO 5: Verificar la solución. El valor de x NO puede hacer que ningún denominador sea cero.
```

> [!tip] Profe Tip: Verificación Veloz
> Antes de hacer toda la sustitución matemática para verificar, haz una "prueba visual": mira los denominadores originales. Si tu solución $x$ hace que cualquier denominador sea $0$, esa solución es inválida (indeterminación). ¡Es el truco más rápido para descartar errores!

---

## EJEMPLOS DESARROLLADOS

> [!example] Ejemplo 1: Productos cruzados
> **Resolver:** $\frac{2}{4x-1} = \frac{3}{4x+1}$
> 1.  **Cruzamos:** $2(4x + 1) = 3(4x - 1)$
> 2.  **Distribuimos:** $8x + 2 = 12x - 3$
> 3.  **Agrupamos:** $8x - 12x = -3 - 2 \Rightarrow -4x = -5$
> 4.  **Despejamos:** $x = \frac{-5}{-4} = \frac{5}{4}$
> 5.  **Verificación:** Como $4(5/4) \pm 1$ no es cero, la solución es válida.

> [!example] Ejemplo 2: El peligro del número entero
> **Resolver:** $\frac{3}{x+1} = \frac{x}{x-1} - 1$
> 1.  **MCM:** $(x+1)(x-1)$.
> 2.  **Multiplicamos:** $3(x-1) = x(x+1) - 1(x+1)(x-1)$
> > [!warning] ¡Cuidado aquí!
> > Al multiplicar el "$-1$" por el MCM, se genera una diferencia de cuadrados $(x^2-1)$. El signo menos de afuera cambiará los signos internos: $-(x^2 - 1) = -x^2 + 1$. ¡No lo olvides!
> 3.  **Resolvemos:** $3x - 3 = x^2 + x - x^2 + 1 \Rightarrow 3x - 3 = x + 1$
> 4.  **Resultado:** $2x = 4 \Rightarrow x = 2$.

> [!example] Ejemplo 3: Factores repetidos y verificación exacta
> **Resolver:** $\frac{2x}{x-1} + \frac{3x+1}{x-1} = 2$
> 1.  **MCM:** Es simplemente $(x-1)$.
> 2.  **Multiplicamos:** $2x + 3x + 1 = 2(x - 1) \Rightarrow 5x + 1 = 2x - 2$
> 3.  **Resultado:** $3x = -3 \Rightarrow x = -1$.
> 4.  **Verificación Matemática:** Sustituimos $x = -1$ en la original:
>     $\frac{2(-1)}{-1-1} + \frac{3(-1)+1}{-1-1} = \frac{-2}{-2} + \frac{-2}{-2} = 1 + 1 = 2$.
>     **$2 = 2$**. ¡Comprobado!

> [!example] Ejemplo 4: Aplicación Financiera (Caso Cuadrático)
> **Problema:** Un fondo de **$10,000 USD** se distribuye según la ecuación: $\frac{8}{x+6} + \frac{12-x}{x-6} = 1$.
> 1.  **MCM:** $(x+6)(x-6)$.
> 2.  **Multiplicar por MCM:** $8(x-6) + (12-x)(x+6) = (x+6)(x-6)$
> 3.  **Operamos:** $8x - 48 + (12x + 72 - x^2 - 6x) = x^2 - 36$
> 4.  **Igualamos a cero:** $0 = 2x^2 - 14x - 60$.
> 5.  **Fórmula General:** $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
>     *   Discriminante: $(-14)^2 - 4(2)(-60) = 196 + 480 = 676$.
>     *   Raíz: $\sqrt{676} = 26$.
>     *   $x_1 = \frac{14 + 26}{4} = \frac{40}{4} = 10$.
>     *   $x_2 = \frac{14 - 26}{4} = \frac{-12}{4} = -3$.
> *En finanzas, el tiempo o socios suelen ser positivos, por lo que la solución lógica es $x = 10$.*

---

## EJERCICIOS PARA EL ESTUDIANTE

> [!abstract] 🟢 Nivel Fácil
> Resuelve aplicando productos cruzados:
> $\frac{3}{2x-2} = \frac{2}{x+3}$

> [!abstract] 🟡 Nivel Medio
> Halla el valor de $x$ asegurándote de multiplicar todos los términos por el MCM:
> $\frac{x}{x+2} + \frac{3}{x+4} = 1$

> [!abstract] 🔴 Nivel Avanzado
> **Reto Presupuestario ($USD):** Un departamento de tesorería debe ajustar un flujo de caja basado en la siguiente relación de capital: $\frac{x+2}{x-1} - \frac{x+3}{x+1} = \frac{8}{x^2-1}$. Encuentra el valor de $x$ para equilibrar el presupuesto.
> *Ayuda: Recuerda que $x^2-1 = (x+1)(x-1)$.*

---

## RESPUESTAS Y AUTOEVALUACIÓN

### Soluciones para el docente:
*   **Fácil:** $x = 13$
*   **Medio:** $x = 2$
*   **Avanzado:** $x = 3$ (Procedimiento: $(x+2)(x+1) - (x+3)(x-1) = 8 \Rightarrow (x^2+3x+2) - (x^2+2x-3) = 8 \Rightarrow x+5=8 \Rightarrow x=3$).

### Mini-prueba de autoevaluación:
1.  **¿Cuál es el MCM de $(x+2)$ y $(x+2)$?**
    *   *Respuesta:* Es solo $(x+2)$. No se multiplican entre sí si son idénticos.
2.  **¿Por qué es fundamental el Paso 5 (Verificación)?**
    *   *Respuesta:* Porque una solución matemáticamente correcta puede ser lógicamente imposible si hace que el denominador sea cero (división por cero).
3.  **Si tengo $-(2x - 4)$ tras eliminar un denominador, ¿cuál es el resultado correcto?**
    *   *Respuesta:* $-2x + 4$. El signo menos cambia a ambos términos.

---

## CIERRE Y NAVEGACIÓN FINAL

¡Excelente trabajo hoy! Has dominado la base de las ecuaciones racionales con polinomios. Recuerda que la clave es el orden y no olvidar esos signos negativos traicioneros. ¡Nos vemos en la próxima lección para subir el nivel!

> [!tip] Próxima Clase
> En la **Clase 07**, veremos casos avanzados donde tendremos que factorizar trinomios y manejar potencias más altas. ¡Sigue así, vas por muy buen camino!

> [!info] 🧭 Navegación
> ◀️ [[Clase 05 - Ecuaciones racionales con denominadores monomios]] | 🏠 [[00 - Índice del curso]] | [[Clase 07 - Ecuaciones racionales parte 2]] ▶️