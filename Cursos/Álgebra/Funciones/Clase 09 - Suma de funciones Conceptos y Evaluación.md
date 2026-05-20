# Clase 09 — Suma de funciones: Conceptos y Evaluación

#algebra #sumoffunctions

```ad-info
title: 🧭 Navegación
⬅️ **Anterior:** [[Clase 08 — Introducción a las funciones]]
⬆️ **Índice:** [[Índice de Álgebra]]
```

---

```ad-abstract
title: 🌍 Relevancia y aplicaciones
¿Por qué es importante aprender a sumar funciones? En el mundo real, los fenómenos rara vez ocurren de forma aislada. Sumar funciones nos permite:
- **💵 Aplicación USD:** Combinar una función de ingresos con una de costos para obtener la utilidad total de una empresa.
- **🏗️ Aplicación práctica:** En ingeniería, calcular la superposición de fuerzas o tensiones que actúan simultáneamente sobre una estructura.
- **📊 Situación cotidiana:** Determinar el gasto mensual total sumando facturas de diferentes servicios (luz, agua, internet), cada una con su propia tarifa y comportamiento.
```

---

### 3. Definición y Errores Comunes

```ad-note
title: 📌 ¿Qué es la Suma de funciones?
Sumar funciones es, en esencia, "fusionar" sus reglas o fórmulas en una sola. Si tienes una función $f(x)$ y otra $g(x)$, la nueva función $(f+g)(x)$ se obtiene sumando sus términos:
$$(f+g)(x) = f(x) + g(x)$$
**Punto clave:** Esta operación solo es válida para los valores de $x$ que están en la **intersección** de sus dominios (donde ambas funciones existen al mismo tiempo).
```

```ad-warning
title: ⚠️ Error común
El error más frecuente es olvidar los **paréntesis** al sustituir las funciones. Sin ellos, es muy fácil equivocarse con los signos negativos o fallar al agrupar términos múltiples. ¡Protege siempre tus funciones antes de operar!
```

```ad-tip
title: 💡 Truco para recordarlo
**"Términos iguales se hacen amigos"**: Para simplificar el resultado, busca aquellos términos que tengan la misma letra y el mismo exponente para agruparlos (sumarlos o restarlos entre sí).
```

---

### 4. Metodología Procedimental

Sigue estos pasos lógicos para resolver cualquier suma de funciones sin perderte:

```text
PASO 1 → Identificar claramente las fórmulas de f(x) y g(x).
PASO 2 → Plantear la suma (f + g)(x) protegiendo cada función con paréntesis.
PASO 3 → Eliminar paréntesis y agrupar términos semejantes (mismo exponente).
PASO 4 → Organizar el polinomio resultante de mayor a menor exponente y simplificar.
```

---

### 5. Bloque de Ejemplos Desarrollados

```ad-example
title: Ejemplo 1: Suma Básica (Lineal y Cuadrática)
**Dadas:** $f(x) = 3x + 2$ y $g(x) = 2x^2 + 5x - 6$
1. **Planteamos:** $(3x + 2) + (2x^2 + 5x - 6)$
2. **Agrupamos:**
   - Términos $x^2$: Solo $2x^2$.
   - Términos $x$: $3x + 5x = 8x$.
   - Independientes: $2 - 6 = -4$.
**Resultado:** $(f+g)(x) = 2x^2 + 8x - 4$
```

```ad-example
title: Ejemplo 2: Funciones Racionales (Fracciones)
**Dadas:** $f(x) = \frac{x+2}{2x+3}$ y $g(x) = 3x + 1$
1. Para sumar, ponemos un $1$ debajo de $g(x)$ y aplicamos el **método de la "carita feliz"** (multiplicación cruzada).
2. Multiplicamos cruzado: $(x+2)(1) + (2x+3)(3x+1)$.
3. Multiplicamos denominadores: $(2x+3)(1)$.
4. Al desarrollar los binomios y simplificar el numerador:
**Resultado:** $(f+g)(x) = \frac{6x^2 + 12x + 5}{2x+3}$
```

```ad-example
title: Ejemplo 3: Análisis de Dominio (Intersección)
**Dadas:** $f(x) = \frac{3}{x-2}$ y $g(x) = \sqrt{x+2}$
- **Dominio de f:** Todos los reales excepto $x = 2$ (porque el denominador no puede ser cero).
- **Dominio de g:** Todos los números $x \geq -2$ (porque no hay raíces cuadradas de negativos en los reales).
- **Intersección:** La suma solo existe donde ambos dominios se cruzan. Es decir, desde $-2$ hasta el infinito, pero excluyendo el número $2$.
*Nota visual:* En la recta numérica, esto se ve como el intervalo $[-2, 2) \cup (2, \infty)$.
```

```ad-example
title: Ejemplo 4: Evaluación en un punto (Aplicación USD)
**Contexto:** Costo de producción $f(x) = 3x + 2$ y costo de transporte $g(x) = 2x^2 + 5x - 6$. Calcular el costo total para $x = 3$ unidades.
1. Evaluamos $f(3) = 3(3) + 2 = 11$.
2. Evaluamos $g(3) = 2(3)^2 + 5(3) - 6 = 18 + 15 - 6 = 27$.
3. Sumamos los resultados finales: $11 + 27 = 38$.
**Resultado:** El costo total es **38 USD**.
```

---

### 6. Práctica y Respuestas

**Instrucción:** Puedes elegir dos caminos: 1) Sumar las funciones y luego evaluar el número, o 2) Evaluar el número en cada función por separado y luego sumar los resultados. ¡Ambos caminos llevan a la misma respuesta!

*   **🟢 Fácil:** Si $f(x) = 2x^2+3x-5$ y $g(x) = \sqrt{x+6}$, halla $(f+g)(-2)$.
*   **🟡 Medio:** Evalúa la suma de $G(x) = \sqrt{x+6}$ y $H(x) = \frac{2x+1}{x^2-2x+1}$ en el punto $x = 3$.
*   **🔴 Avanzado ($USD):** Dadas $f(x) = 2x^2+3x-5$ y $h(x) = \frac{2x+1}{x^2-2x+1}$, calcula el valor de $(f+h)(-5)$.

```ad-success
title: ✅ Respuestas Correctas
1. **Resultado:** $(f+g)(-2) = -1$
2. **Resultado:** $(G+H)(3) = \frac{19}{4}$ (o $4.75$)
3. **Resultado:** $(f+h)(-5) = \frac{119}{4}$ (o $29.75$)
*(Nota: En el ejercicio avanzado, $f(-5) = 30$ y $h(-5) = -1/4$. Al sumarlos: $30 - 0.25 = 29.75$)*.
```

---

### 7. Autoevaluación y Cierre

```ad-question
title: Test de comprensión rápida
1. Si sumamos una función con denominador $(x-2)$, ¿qué valor de $x$ queda prohibido en el dominio?
2. ¿Es obligatorio simplificar los términos semejantes al final?
3. Si sabemos que $f(2) = 10$ y $g(2) = 5$, ¿cuánto es $(f+g)(2)$?
```

**Respuestas rápidas:** 
1. El valor $x = 2$. 
2. Sí, por rigor académico y para facilitar cálculos futuros. 
3. Exactamente $15$.

**Cierre:** ¡Excelente trabajo! Has dominado la suma de funciones y su evaluación. Esta es la base para entender cómo interactúan diferentes modelos. Prepárate, porque en la **Clase 10** veremos la **Resta de funciones**, donde los signos negativos intentarán ponerte trampas. ¡Nos vemos allá!