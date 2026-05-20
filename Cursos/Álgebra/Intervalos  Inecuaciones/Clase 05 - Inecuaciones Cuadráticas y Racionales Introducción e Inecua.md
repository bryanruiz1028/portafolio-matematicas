# Clase 05 — Inecuaciones Cuadráticas y Racionales: Introducción e Inecuaciones de Segundo Grado

**Etiquetas:** #matemáticas #álgebra #inecuaciones #educación #secundaria

---
[[Clase 04 — Inecuaciones Lineales]] | **Clase 05** | [[Clase 06 — Inecuaciones Racionales]]
---

## 1. Relevancia y Aplicaciones

Las inecuaciones de segundo grado nos permiten determinar rangos de viabilidad donde una condición se cumple, siendo esenciales para identificar zonas de seguridad o ganancia en modelos que no son lineales. A diferencia de las ecuaciones, no buscamos un valor único, sino el conjunto de intervalos que satisfacen la desigualdad.

- **💵 Aplicación $USD:** Determinar el rango de precios de venta necesarios para asegurar una utilidad neta positiva (ganancias).
- **🏗️ Aplicación práctica:** Calcular los límites de tensión y carga en una estructura para que la flexión se mantenga dentro de los márgenes de resistencia.
- **📊 Situación cotidiana:** Gestionar presupuestos variables donde el costo total depende del cuadrado del consumo (como en ciertas tarifas eléctricas o logísticas).

## 2. Concepto Clave e Identificación

> [!note] Definición
> Una inecuación cuadrática o de segundo grado es aquella donde el mayor exponente de la variable es 2 ($x^2$) o resulta de la multiplicación de dos factores lineales (ej. $(x+1)(x-4)$). Su forma estándar es $ax^2 + bx + c > 0$ (o $<, \leq, \geq$).

> [!warning] Error Común: ¡No despejes como una ecuación lineal!
> El error más frecuente es intentar "despejar" la $x^2$ aplicando raíz cuadrada directamente (ej. de $x^2 > 4$ concluir solo $x > 2$). Esto es incorrecto porque se pierde el intervalo negativo. El método correcto siempre requiere **factorización y análisis de signos**.

> [!tip] Truco Mnemotécnico: El Sol y el Suelo
> Para recordar qué sector de la recta numérica elegir según el signo final:
> - **Boca grande ($> 0$)**: Busca el **Sol** (sectores con signo **Positivo** $+$).
> - **Boca chica ($< 0$)**: Busca el **Suelo** (sectores con signo **Negativo** $-$).

## 3. Procedimiento Paso a Paso

> [!abstract] Algoritmo de Resolución
> 1. **PASO 1 (Ordenar):** Trasladar todos los términos a la izquierda para dejar el cero a la derecha de la desigualdad.
> 2. **PASO 2 (Factorizar):** Convertir el trinomio en un producto de dos factores lineales (usando aspa simple o trinomio de la forma $ax^2+bx+c$).
> 3. **PASO 3 (Puntos Críticos):** Igualar cada factor a cero para hallar los valores frontera en la recta numérica.
> 4. **PASO 4 (Análisis de Signos):** Ubicar los puntos en la recta, dividirla en intervalos y evaluar el signo de cada sector (Método del Cementerio).

## 4. Ejemplos Desarrollados

> [!ad-example] Ejemplo 1: Caso Básico
> **Resolver:** $x^2 - 3x - 10 > 0$
> 1. **Factorización:** Buscamos números que multiplicados den $-10$ y sumados $-3$: $(x-5)(x+2) > 0$.
> 2. **Puntos Críticos:** $x-5=0 \Rightarrow x=5$; $x+2=0 \Rightarrow x=-2$.
> 3. **Análisis de Signos:**
>    - Para $(-\infty, -2)$, probamos con $-3$: $(-3-5)(-3+2) = (-)(- ) = (+)$.
>    - Para $(-2, 5)$, probamos con $0$: $(0-5)(0+2) = (-)(+) = (-)$.
>    - Para $(5, \infty)$, probamos con $6$: $(6-5)(6+2) = (+)(+) = (+)$.
> 4. **Resultado:** Como buscamos $> 0$ (positivos): $(-\infty, -2) \cup (5, \infty)$.

> [!ad-example] Ejemplo 2: Caso con Intervalo Cerrado ($\leq$)
> **Resolver:** $x^2 - 2x - 24 \leq 0$
> 1. **Factorización:** $(x-6)(x+4) \leq 0$.
> 2. **Puntos Críticos:** $x = 6$ y $x = -4$.
> 3. **Análisis:** Al ser $\leq 0$, buscamos el sector negativo. El punto crítico se incluye (corchetes) porque el signo igual está presente.
> 4. **Resultado:** $[-4, 6]$.

> [!ad-example] Ejemplo 3: Factorización de Trinomio $ax^2 + bx + c$
> **Resolver:** $2x^2 - 5x > -2$
> 1. **Ordenar:** $2x^2 - 5x + 2 > 0$.
> 2. **Factorizar (Método de multiplicación por coeficiente principal):**
>    - Multiplicamos y dividimos por 2: $\frac{(2x)^2 - 5(2x) + 4}{2}$
>    - Buscamos números que multiplicados den 4 y sumados $-5$: $\frac{(2x-4)(2x-1)}{2}$
>    - Simplificamos la fracción: $\frac{2(x-2)(2x-1)}{2} = (x-2)(2x-1)$.
> 3. **Puntos Críticos:** $x=2$ y $x=1/2$.
> 4. **Resultado:** Por ser $> 0$, tomamos extremos: $(-\infty, 1/2) \cup (2, \infty)$.

> [!ad-example] Ejemplo 4: Aplicación Económica ($USD)
> **Problema:** Un fabricante compara los costos de dos procesos. La viabilidad se da cuando: $x^2 + 3x \leq -x^2 - 2x + 3$, donde $x$ es el precio en dólares.
> 1. **Ordenar:** $2x^2 + 5x - 3 \leq 0$.
> 2. **Factorizar:** $(x+3)(2x-1) \leq 0$.
> 3. **Puntos Críticos:** $x = -3$ y $x = 0.5$.
> 4. **Interpretación Matemática:** El intervalo es $[-3, 0.5]$.
> 5. **Análisis Crítico (Realidad Económica):** Un precio no puede ser negativo ni cero en este contexto. Por lo tanto, el rango de precios permitidos en dólares es $(0, 0.50]$.

## 5. Ejercicios y Solucionario

- **🟢 Verde (Fácil):** $x^2 - 2x - 63 \geq 0$
- **🟡 Amarillo (Medio):** $x^2 - 11x + 24 < 0$
- **🔴 Rojo (Avanzado):** Hallar el rango de valores para $2x^2 + 5x \geq x^2 + x + 12$.

**Respuestas:**
1. **Fácil:** $(-\infty, -7] \cup [9, \infty)$ (Factorizado como $(x-9)(x+7) \geq 0$).
2. **Medio:** $(3, 8)$ (Factorizado como $(x-8)(x-3) < 0$).
3. **Avanzado:** $(-\infty, -6] \cup [2, \infty)$ (Resulta en $x^2 + 4x - 12 \geq 0 \Rightarrow (x+6)(x-2) \geq 0$).

## 6. Autoevaluación

1. **¿Cuál de las siguientes expresiones representa una inecuación de segundo grado?**
   - a) $3x + 1 > x - 5$
   - b) $(x+2)(x-3) \geq 0$
   - c) $x/4 < 10$

2. **Si los puntos críticos de una inecuación son $x=3$ y $x=8$, y buscamos el sector negativo, ¿cuál es la solución si el signo es $<$?**
   - a) $(3, 8)$
   - b) $[3, 8]$
   - c) $(-\infty, 3) \cup (8, \infty)$

3. **En el método de puntos críticos, si elegimos un número de prueba y el resultado es cero, ¿qué significa?**
   - a) Que el sector es positivo.
   - b) Que hemos evaluado justamente en un punto crítico.
   - c) Que la inecuación no tiene solución.

*(Soluciones: 1-b, 2-a, 3-b. Nota para la Q2: se usa paréntesis porque el signo $<$ es estrictamente menor).*

## 7. Cierre y Próximos Pasos

> [!tip] Preparación para la Clase 06
> En la siguiente sesión abordaremos las **Inecuaciones Racionales**. Verás que el método de puntos críticos sigue siendo nuestro mejor aliado, pero con un desafío adicional: la variable $x$ aparecerá en el denominador, lo que nos obligará a considerar restricciones de dominio (el denominador nunca puede ser cero).

---
[[Clase 04 — Inecuaciones Lineales]] | **Clase 05** | [[Clase 06 — Inecuaciones Racionales]]