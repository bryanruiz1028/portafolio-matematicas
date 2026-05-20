# #algebra #solvingthequadr

[[Clase 05|⬅ Clase 05]] | [[00 - Índice del curso|Índice]] | **Clase 06** | | [[Clase 07|Clase 07 ➡]]

# Clase 06 — Resolución de Ecuaciones Cuadráticas: Práctica Avanzada y Métodos Alternativos

## 1. ¿Por qué es importante esta clase?
> [!info] 🌍 Relevancia y aplicaciones
> Las ecuaciones cuadráticas permiten modelar fenómenos donde el cambio no es lineal, como las trayectorias parabólicas de proyectiles y la optimización de recursos para maximizar beneficios. Son la base para entender sistemas que dependen del cuadrado de una variable.

- 💵 **Finanzas:** Calcula el punto de equilibrio para que una inversión de $USD genere ganancias exactas según el modelo de Profe Alex.
- 🏗️ **Ingeniería:** Determina dimensiones críticas y puntos de resistencia en estructuras parabólicas y diseños arquitectónicos.
- 📊 **Situación cotidiana:** Predice con precisión el tiempo de caída de un objeto considerando la aceleración constante de la gravedad.

## 2. Concepto clave
> [!note] 📌 ¿Qué es la Ecuación Cuadrática?
> Es una igualdad de la forma $ax^2 + bx + c = 0$, caracterizada porque el exponente máximo de la incógnita es 2. Además de la fórmula general, el método de **Po-Shen Loh** nos permite resolver estas ecuaciones encontrando el "Centro" ($C$) de las raíces y su "Distancia" ($u$).
> 
> [!warning] ⚠️ Error común
> ❌ **Incorrecto:** Intentar resolver sin igualar la ecuación a cero o ignorar el coeficiente $a$. | ✅ **Correcto:** Antes de aplicar Po-Shen Loh, **debes asegurar que el coeficiente de $x^2$ sea 1**. Si $a \neq 1$, divide toda la ecuación entre $a$ obligatoriamente.
> 
> [!tip] 💡 Truco para recordarlo (Po-Shen Loh)
> El Centro ($C$) es el promedio de las raíces. Se halla tomando el coeficiente de $x$ ($b$), cambiándole el signo y dividiéndolo entre 2: $C = -b/2$.

## 3. Procedimiento paso a paso
Sintetiza el procedimiento de resolución usando el método de Po-Shen Loh, priorizando la relación conceptual de las raíces:

```
PASO 1 → Igualar la ecuación a cero. Si el coeficiente de x² no es 1, divide toda la ecuación entre 'a'.
PASO 2 → Hallar el Centro (C): Toma el coeficiente de x, cambia su signo y divídelo por 2 (C = -b/2).
PASO 3 → Plantear la relación de las raíces: (C - u)(C + u) = c. 
         Esta relación (producto de raíces) nos permite hallar la distancia 'u' mediante la forma simplificada: C² - u² = c.
PASO 4 → Calcular las soluciones finales sumando y restando la distancia 'u' al Centro: x = C ± u.
```

## 4. Ejemplos de Práctica

```ad-example
title: Ejemplo 1 — Caso Básico: Trinomio Cuadrado Perfecto (Práctica 2)
Utiliza la ecuación simplificada $9x^2 - 42x + 49 = 0$.
**Paso 1:** Identificar si es un Trinomio Cuadrado Perfecto (TCP). Calculamos $\sqrt{9x^2} = 3x$ y $\sqrt{49} = 7$.
**Paso 2:** Verificamos el término central: $2 \cdot (3x) \cdot (7) = 42x$. ¡Coincide!
**Paso 3:** Factorizamos directamente como $(3x - 7)^2 = 0$.
✅ **Resultado:** $3x - 7 = 0 \implies x = 7/3$.
```

```ad-example
title: Ejemplo 2 — Caso con Signos y Expansión (Práctica 3)
Utiliza $(x+7)(2x-1) = 4x-11$.
**Pasos:** 
1. Expandir binomios: $2x^2 - x + 14x - 7 = 4x - 11$.
2. Simplificar e igualar a cero: $2x^2 + 9x + 4 = 0$.
3. Al no ser $a=1$, podemos usar la fórmula general o factorización por aspa.
✅ **Resultado:** $x_1 = -4, x_2 = -1/2$. ⚠️ *Nota: Ten cuidado extremo al trasponer términos; un error de signo cambia toda la solución.*
```

```ad-example
title: Ejemplo 3 — Caso Avanzado: Reducibles (Práctica 4)
Utiliza la ecuación fraccionaria $\frac{5x-8}{x+1} = \frac{7x-4}{x+2}$.
**Pasos:** 
1. Productos cruzados: $(5x-8)(x+2) = (7x-4)(x+1)$.
2. Expandir: $5x^2 + 2x - 16 = 7x^2 + 3x - 4$.
3. Reducir a la forma estándar: $2x^2 + x + 12 = 0$.
✅ **Resultado:** Al aplicar el discriminante ($b^2 - 4ac$), obtenos $1^2 - 4(2)(12) = -95$. Al ser negativo, la ecuación **no tiene solución real**.
```

```ad-example
title: Ejemplo 4 — Aplicación real con $USD
Un modelo de inversión sigue la estructura $x^2 - 10x + 21 = 0$, donde $x$ representa el capital necesario para el equilibrio.
**Pasos (Método Po-Shen Loh):** 
1. Centro $C = -(-10)/2 = 5$.
2. Relación de distancia: $(5 - u)(5 + u) = 21 \implies 25 - u^2 = 21$.
3. Resolver $u$: $u^2 = 4 \implies u = 2$.
4. Soluciones: $x = 5 \pm 2$.
✅ **Resultado:** Los puntos de equilibrio se alcanzan con una inversión de **$3 USD** y **$7 USD**.
```

## 5. Ejercicios para el estudiante

```ad-abstract
title: 🟢 Fácil — Método de Po-Shen Loh
Resuelve encontrando el Centro ($C$) y la distancia ($u$):
1. $x^2 + 8x + 12 = 0$
2. $x^2 + 4x - 5 = 0$
3. $x^2 - 10x + 21 = 0$
4. $x^2 - 6x + 8 = 0$
```

```ad-abstract
title: 🟡 Medio — Operaciones y Simplificación (Práctica 2 y 3)
1. $4x(2x-11) + 25 = -(24 + 2x + x^2)$
2. $(2x-3)^2 - 5 = (x+2)^2 + 4$
3. $5(x^2 + 2x - 15) - 3 = 2x(3x + 1) - x^2 + 12$
4. $(x-3)^2 - (2x+5)^2 = 16$
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD y Reducibles (Práctica 4)
1. Resuelve la ecuación fraccionaria de ingresos: $\frac{1}{24} + \frac{x+2}{x+3} = \frac{x+4}{x+5}$. Determina el valor de $x$ en $USD$.
2. Calcula $x$ mediante productos cruzados: $\frac{x+6}{6x+6} = \frac{x-4}{-6}$.
3. Determina si una inversión con modelo $2x^2 + x + 12 = 0$ tiene un punto de equilibrio real basándote en el discriminante.
4. $x^2 + 9x - 90 = 0$ aplicado a un balance de caja.
```

```ad-success
title: ✅ Respuestas (para el docente)
- **🟢 Fácil:** 1. $x=-6, -2$ | 2. $x=-5, 1$ | 3. $x=3, 7$ | 4. $x=2, 4$
- **🟡 Medio:** 1. $x=7/3$ | 2. $x=4, -1/2$ | 3. $x=-15, 6$ | 4. $x=0, -26/3$
- **🔴 Avanzado:** 1. $x=3, -11$ | 2. $x=2, -11$ | 3. No tiene solución real ($D = -95$) | 4. $x=6, -15$
```

## 6. Mini-prueba de autoevaluación

```ad-question
title: 🧪 Pregunta 1
¿Cuál es el valor del "Centro" ($C$) en el método de Po-Shen Loh para la ecuación $x^2 + 8x + 12 = 0$?
a) 8
b) -8
c) 4
d) -4
✅ **Respuesta:** d) -4. Se toma el coeficiente 8, se le cambia el signo (-8) y se divide entre 2. Conceptualmente, $C = -b/2a$.
```

```ad-question
title: 🧪 Pregunta 2
En la demostración de la fórmula general, ¿cuál es el proceso algebraico que permite agrupar las $x$ en un solo término?
a) Carita feliz
b) Completar el trinomio cuadrado perfecto
c) División sintética
d) Despeje directo de $c$
✅ **Respuesta:** b) Completar el trinomio cuadrado perfecto. Es el paso que transforma $ax^2 + bx$ en una expresión de potencia única.
```

```ad-question
title: 🧪 Pregunta 3
Si al calcular un balance de inversión en $USD obtenemos un valor de $-95$ dentro de la raíz cuadrada (discriminante), ¿qué significa para el negocio?
a) Inversión con pérdidas
b) No hay un punto de equilibrio real
c) El equilibrio es $95 USD
d) Debemos multiplicar por -1
✅ **Respuesta:** b) No hay solución real. En términos prácticos, el modelo no intersecta el eje $x$, por lo que no existe un valor real para ese equilibrio.
```

## 7. Notas para el próximo tema
> [!tip] 💡 En la próxima clase
> Una vez dominada la resolución, exploraremos la **Naturaleza de las Raíces**. Aprenderemos a usar el discriminante ($D = b^2 - 4ac$) para predecir si una ecuación tiene dos soluciones, una sola, o ninguna en el campo real antes de siquiera empezar a resolverla.