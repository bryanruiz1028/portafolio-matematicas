# Clase 05 — Dominio, Rango y Gráfica de Funciones Racionales

tags: #algebra #dominiorangoygr
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 5 de 12

> [!info] 🧭 Navegación
> [[Clase 04|⬅ Clase 04]] | [[00 - Índice del curso|Índice]] | **Clase 05** | | [[Clase 06|Clase 06 ➡]]

## ¿Por qué es importante esta clase?
> [!info] 🌍 Relevancia y aplicaciones
> Las funciones racionales modelan comportamientos que se acercan a un límite sin alcanzarlo (asíntotas). Son vitales para predecir escenarios donde los recursos son limitados o las variables guardan una relación de proporcionalidad inversa.
> 
> - 💵 **Aplicación $USD:** Permiten calcular el **costo promedio por producto** ($C = \text{Costo Total} / \text{Unidades}$). Al producir más, los costos fijos se diluyen y el costo promedio se acerca al costo variable, que actúa como una asíntota horizontal.
> - 🏗️ **Aplicación práctica:** Se usan en planificación urbana para determinar la **densidad poblacional** ideal en función del área disponible, evitando el colapso de servicios.
> - 📊 **Situación cotidiana:** El **reparto de un presupuesto fijo**; entre más personas participen, menos dinero recibe cada una, pero la cantidad individual nunca llegará a ser cero ni negativa.

## Concepto clave
> [!note] 📌 ¿Qué es una Función Racional?
> Para un estudiante de 12 años: Es una función que parece una fracción donde obligatoriamente hay una $x$ en la parte de abajo (denominador). Matemáticamente, es el cociente de dos polinomios.
> 
> Las **asíntotas** son como "muros" invisibles que la gráfica intenta tocar pero nunca alcanza. Es vital distinguir entre dos tipos de restricciones en el denominador:
> 1. **Asíntota Vertical:** Ocurre cuando un factor del denominador hace que la función se dispare al infinito y ese factor **no se puede simplificar**.
> 2. **Hueco (Punto de discontinuidad):** Ocurre cuando un factor que hace cero al denominador **se simplifica** con uno igual en el numerador. La función parece "saltarse" ese punto.

> [!warning] ⚠️ Error común
> ❌ **Incorrecto:** Creer que cualquier valor que haga cero el denominador es automáticamente una asíntota vertical.
> ✅ **Correcto:** Primero debes factorizar. Si el factor desaparece al simplificar, es un **hueco**; si permanece abajo, es una **asíntota vertical**.

> [!tip] 💡 Truco para recordarlo
> Usa la regla de la **"División Prohibida"**: Como en matemáticas es imposible dividir entre cero, cualquier valor de $x$ que provoque un cero en el denominador genera un conflicto gráfico, creando ya sea un "muro" (asíntota) o un "bache" (hueco).

## Procedimiento paso a paso
Sigue este orden para desmenuzar cualquier función racional:

```text
PASO 1 → Factorizar numerador y denominador para identificar posibles huecos (simplificación).
PASO 2 → Hallar Asíntotas Verticales (igualar lo que quede en el denominador a cero y despejar x).
PASO 3 → Hallar Asíntota Horizontal (comparar grados del numerador y denominador).
PASO 4 → Calcular "Ceros" (Intersección en X haciendo y=0; Intersección en Y haciendo x=0).
PASO 5 → Crear tabla de valores y trazar la gráfica respetando las asíntotas y huecos.
```

---

## Ejemplos de los 3 Casos

```ad-example
title: Ejemplo 1 — Caso 1: Grados iguales (Básico)
**Función:** $f(x) = \frac{2x - 5}{x - 3}$
- **Asíntota Vertical (AV):** $x - 3 = 0 \Rightarrow x = 3$.
- **Asíntota Horizontal (AH):** Grados iguales ($x^1$), dividimos coeficientes principales: $y = \frac{2}{1} = 2$.
- **Cortes:** 
    - En $y$: $f(0) = \frac{-5}{-3} \approx 1.67$. Punto $(0, 1.67)$.
    - En $x$: $2x - 5 = 0 \Rightarrow x = 2.5$. Punto $(2.5, 0)$.
- ✅ **Resultado:** Dominio: $\mathbb{R} - \{3\}$ | Rango: $\mathbb{R} - \{2\}$.
```

```ad-example
title: Ejemplo 2 — Caso 1: Grados iguales (Cuadrático)
**Función:** $f(x) = \frac{x^2 - 3x - 4}{2x^2 + 4x}$
- **Factorización:** $f(x) = \frac{(x-4)(x+1)}{2x(x+2)}$. No hay factores comunes, no hay huecos.
- **Asíntotas Verticales:** $x = 0$ y $x = -2$.
- **Asíntota Horizontal:** Grados iguales ($x^2$), entonces $y = \frac{1}{2} = 0.5$.
- ✅ **Resultado:** La gráfica tiene dos muros verticales en $x = 0$ y $x = -2$.
```

```ad-example
title: Ejemplo 3 — Caso 2: Denominador de mayor grado (Con Hueco)
**Función:** $f(x) = \frac{x - 4}{x^2 - 2x - 8}$
- **Factorización:** $\frac{x - 4}{(x - 4)(x + 2)}$. 
- **Hueco:** El factor $(x-4)$ se simplifica, generando un **hueco** en $x = 4$.
- **Análisis:** La función se comporta como $f(x) = \frac{1}{x+2}$.
- **Asíntotas:** $AV: x = -2$ | $AH: y = 0$ (grado del denominador es mayor).
- ✅ **Resultado:** Gráfica con $AV$ en $x = -2$ y un punto vacío en $(4, 1/6)$.
```

```ad-example
title: Ejemplo 4 — Caso 3: Numerador de mayor grado (Lineal con huecos)
**Función:** $f(x) = \frac{2x^3 - 4x^2 - 6x}{x^2 - 2x - 3}$
- **Factorización:** $\frac{2x(x-3)(x+1)}{(x-3)(x+1)}$.
- **Simplificación:** Se eliminan $(x-3)$ y $(x+1)$. Queda la función lineal $y = 2x$.
- **Nota especial:** A diferencia de las asíntotas oblicuas (donde no se puede simplificar), aquí la función es una línea recta con **huecos** en $x = 3$ y $x = -1$.
- ✅ **Resultado:** Dominio: $\mathbb{R} - \{3, -1\}$ | Rango: $\mathbb{R} - \{6, -2\}$.
```

---

## Ejercicios para el estudiante

```ad-abstract
title: 🟢 Fácil — Identificación de Asíntotas
Determine la Asíntota Vertical ($AV$) de:
1. $f(x) = \frac{1}{x - 5}$
2. $f(x) = \frac{x + 2}{x - 1}$
3. $f(x) = \frac{5}{2x + 4}$
4. $f(x) = \frac{3x}{x + 9}$
```

```ad-abstract
title: 🟡 Medio — Funciones con Grados Iguales
Halle la Asíntota Horizontal ($AH$) e identifique huecos:
1. $f(x) = \frac{4x - 2}{2x + 8}$
2. $f(x) = \frac{x^2 - 1}{x^2 - 4}$
3. $f(x) = \frac{2x + 1}{x + 1}$
4. $f(x) = \frac{x^2 + x}{x^2 - 1}$
```

```ad-abstract
title: 🔴 Avanzado — Aplicación y Análisis
1. **Negocios:** Un costo promedio es $C(x) = \frac{5x + 500}{x}$. Halle la $AH$ e interprétela.
2. Encuentre el hueco de $f(x) = \frac{x^2 - 9}{x - 3}$.
3. Analice el dominio y rango de $f(x) = \frac{x}{x^2 - 1}$.
4. Ubique el hueco y la $AV$ de $f(x) = \frac{x - 1}{x^2 - 1}$.
```

```ad-success
title: ✅ Respuestas (para el docente)
- **🟢 Fácil:** 1. $x=5$ | 2. $x=1$ | 3. $x=-2$ | 4. $x=-9$
- **🟡 Medio:** 1. $y=2$ | 2. $y=1$ | 3. $y=2$ | 4. Hueco en $x=-1$, $AH: y=1$
- **🔴 Avanzado:** 
	1. $y=5$ (Costo mínimo por unidad es $\$5$ USD). 
	2. Hueco en $x=3$, no hay $AV$. 
	3. $Dom: \mathbb{R}-\{-1,1\}$, $Rango: \mathbb{R}$. 
	4. Hueco en $x=1$, $AV: x=-1$.
```

---

## Mini-prueba de autoevaluación

```ad-question
title: 🧪 Pregunta 1
¿Qué ocurre gráficamente cuando un factor se simplifica en el numerador y denominador?
a) Se genera una asíntota vertical.
b) Se crea un hueco (punto vacío) en la gráfica.
c) La función se vuelve constante.
d) La asíntota horizontal desaparece.
**✅ Respuesta:** b) — El valor de $x$ sigue estando fuera del dominio, pero no tiende al infinito.
```

```ad-question
title: 🧪 Pregunta 2
Si el grado del numerador es MENOR que el del denominador, la asíntota horizontal es:
a) $y = 1$
b) No existe.
c) $y = 0$
d) $y = x$
**✅ Respuesta:** c)
```

```ad-question
title: 🧪 Pregunta 3
En $C(x) = \frac{10x + 200}{x}$, ¿cuál es el costo mínimo posible por unidad?
a) $\$200$
b) $\$10$
c) $\$0$
d) $\$20$
**✅ Respuesta:** b) — Es el valor de la $AH$ ($10/1$).
```

## Notas para el próximo tema
> [!tip] 💡 En la próxima clase
> Ahora que dominamos los huecos y las asíntotas horizontales, en la **Clase 06** exploraremos las **Asíntotas Oblicuas**. Estas aparecen únicamente cuando el grado del numerador es exactamente uno mayor que el del denominador y los factores **no se pueden simplificar**.

> [!info] 🧭 Navegación
> [[Clase 04|⬅ Clase 04]] | [[00 - Índice del curso|Índice]] | **Clase 05** | | [[Clase 06|Clase 06 ➡]]