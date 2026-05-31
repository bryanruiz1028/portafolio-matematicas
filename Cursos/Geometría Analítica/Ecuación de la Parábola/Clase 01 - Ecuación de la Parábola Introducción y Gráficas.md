# Clase 01 — Ecuación de la Parábola: Introducción y Gráficas
tags: #algebra #equationofapara
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 9

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]

## 1. ¿Por qué es importante esta clase?
La parábola no es solo una línea curva en tu cuaderno; es la forma en la que la naturaleza y la tecnología optimizan la energía y el movimiento. Desde el arco que describe un balón al ser lanzado hasta la precisión con la que una antena recibe señales del espacio, entender su ecuación es la llave para modelar el mundo real.

*   💵 **Aplicación con $USD:** En el mundo de las finanzas, las gráficas de precios suelen seguir trayectorias parabólicas. El vértice puede representar el punto máximo de ganancias de una inversión o el "valle" (precio mínimo) donde una acción en dólares toca fondo antes de una gran recuperación.
*   🏗️ **Aplicación práctica:** Es el diseño fundamental de las antenas satelitales (donde las ondas rebotan directo al foco) y de los puentes colgantes, donde los cables se curvan para sostener toneladas de peso.
*   📊 **Situación cotidiana:** Cualquier objeto que lances (una piedra, una pelota o un proyectil) dibujará siempre una parábola en el aire debido a la gravedad.

---

## 2. Concepto clave

> [!note] 📌 ¿Qué es la Ecuación de una parábola?
> Imagina que dejas un "rastro de migas de pan" que forma una curva perfecta. Una **parábola** es el lugar geométrico (el camino) de todos los puntos que están a la **misma distancia** de un punto fijo llamado `$F$` (**Foco**) y de una línea recta llamada `$D$` (**Directriz**). Tú estás justo en medio cuando te ubicas en el **Vértice** `$V$`.

> [!warning] ⚠️ Error común
> Muchos estudiantes confunden la distancia `$p$` con el ancho total de la curva.
> ❌ **Incorrecto:** Pensar que el lado recto mide lo mismo que `$p$`.
> ✅ **Correcto:** La distancia `$p$` es solo el tramo del `$V$` al `$F$`. El **Lado Recto** completo mide `$4p$`. ¡Es cuatro veces más grande!

> [!tip] 💡 Atajo secreto: "Fui Volando"
> Para que nunca olvides el orden de los elementos sobre el eje de simetría, recuerda la frase: **"Fui Volando"** (**F**oco - **V**értice - **D**irectriz). El Vértice `$V$` siempre es el mediador, viviendo exactamente a la mitad de camino entre el Foco y la Directriz.

---

## 3. Procedimiento paso a paso

> [!todo] 🛠️ Guía visual para graficar y hallar la ecuación
> 1. **Ubicar `$V$` y `$F$`:** Márcalos en el plano cartesiano. Esto te dirá si la parábola es "acostada" (horizontal) o "de pie" (vertical).
> 2. **Determinar la distancia `$p$`:** Mide cuántas unidades hay entre el vértice y el foco. Recuerda que `$p$` siempre es una **distancia positiva**. La dirección de apertura (arriba, abajo, izquierda, derecha) decidirá el signo en la fórmula.
> 3. **Calcular el Lado Recto (`$4p$`):** Multiplica tu `$p$` por 4. Esto define qué tan "abierta" es la curva. Marca dos puntos a los lados del foco (a una distancia de `$2p$` cada uno).
> 4. **Trazar y cerrar:** Une el vértice con los extremos del lado recto y dibuja la directriz al lado opuesto del foco, a la misma distancia `$p$`.

---

## 4. Ejemplos de aplicación

```ad-example
title: Ejemplo 1 — Movimiento en el Eje X (Apertura Horizontal)
**Datos:** Vértice $V(3,1)$ y Foco $F(1,1)$.
1. **Análisis:** Al graficar, vemos que el foco está a la **izquierda** del vértice. Esto significa que la parábola abre hacia el eje $X$ negativo.
2. **Distancia $p$:** La distancia entre $x=3$ y $x=1$ es $2$. Por lo tanto, $p = 2$.
3. **Ecuación:** Usamos la fórmula horizontal negativa:
$(y - k)^2 = -4p(x - h) \implies (y - 1)^2 = -4(2)(x - 3) \implies (y - 1)^2 = -8(x - 3)$.
```

```ad-example
title: Ejemplo 2 — Movimiento en el Eje Y (Apertura Vertical)
**Datos:** Vértice $V(0,-1)$ y Foco $F(0,1)$.
1. **Análisis:** El foco está **arriba** del vértice. Abre hacia el eje $Y$ positivo.
2. **Distancia $p$:** De $y=-1$ a $y=1$ hay $2$ unidades. Así que $p = 2$.
3. **Ecuación:** Al ser vertical positiva, la $x$ va al cuadrado:
$(x - h)^2 = 4p(y - k) \implies (x - 0)^2 = 4(2)(y - (-1)) \implies x^2 = 8(y + 1)$.
```

```ad-example
title: Ejemplo 3 — Caso con Fracciones (Apertura hacia abajo)
**Datos:** Vértice $V(0, 3/2)$ y Foco $F(0, 1)$.
1. **Distancia $p$:** Restamos las coordenadas: $3/2 - 1 = 1/2$. Entonces $p = 0.5$.
2. **Dirección:** Como el foco ($y=1$) está por debajo del vértice ($y=1.5$), abre hacia **abajo**.
3. **Ecuación:** $x^2 = -4p(y - k) \implies x^2 = -4(1/2)(y - 3/2) \implies x^2 = -2(y - 3/2)$.
```

```ad-example
title: Ejemplo 4 — Recuperación de Activos ($USD)
**Situación:** El precio de una acción toca su punto más bajo en $V(2, -2)$ y sube pasando por un foco en $F(2, -0.5)$.
1. **Análisis:** Abre hacia **arriba** (recuperación de precio). $p = |-0.5 - (-2)| = 1.5$.
2. **Lado Recto ($LR$):** $4p = 6$. Los puntos extremos del $LR$ están a 3 unidades del foco: $L(-1, -0.5)$ y $R(5, -0.5)$.
3. **Ecuación de tendencia:** $(x - 2)^2 = 4(1.5)(y + 2) \implies (x - 2)^2 = 6(y + 2)$.
```

---

## 5. Ejercicios para el estudiante

```ad-abstract
title: 🟢 Fácil — Elementos básicos
Dados el Vértice $V(0,0)$ y el Foco $F(2,0)$:
1. ¿Cuánto mide la distancia $p$?
2. ¿Hacia qué dirección abre la parábola?
```

```ad-abstract
title: 🟡 Medio — Ecuación canónica
Halla la ecuación canónica y la longitud del Lado Recto ($LR$) para:
1. Una parábola con $V(1,2)$ y $F(1,5)$.
2. Una parábola con $V(-2,1)$ y $F(-4,1)$.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
Un analista financiero detecta que el "suelo" de una criptomoneda está en $V(5, 10)$ y su foco está en $F(5, 11)$. Si el precio sigue una trayectoria parabólica ascendente, determina la ecuación y el ancho del Lado Recto que proyecta su crecimiento.
```

```ad-success
title: ✅ Respuestas (para el docente)
**Fácil:** 
1. $p = 2$.
2. Abre hacia la derecha (eje $X$ positivo).

**Medio:** 
1. $p = 3$, abre hacia arriba (Vertical). Ecuación: $(x - 1)^2 = 12(y - 2)$. $LR = 12$.
2. $p = 2$, abre hacia la izquierda (Horizontal). Ecuación: $(y - 1)^2 = -8(x + 2)$. $LR = 8$.

**Avanzado:** 
$p = 1$, abre hacia arriba. Ecuación: $(x - 5)^2 = 4(y - 10)$. $LR = 4$.
```

---

## 6. Mini-prueba de autoevaluación

```ad-question
title: 🧪 Pregunta 1 (Conceptual)
Según la regla "Fui Volando", ¿cuál es el elemento que siempre se encuentra exactamente en medio de los otros dos?
a) El Foco.
b) La Directriz.
c) El Vértice.
d) El Lado Recto.
```

```ad-question
title: 🧪 Pregunta 2 (Procedimental)
Si una parábola tiene su Vértice en $(0,0)$ y su Foco en $(0, -3)$, ¿cuál es su ecuación?
a) $y^2 = -12x$
b) $x^2 = -12y$
c) $x^2 = 12y$
d) $y^2 = 12x$
```

```ad-question
title: 🧪 Pregunta 3 (Aplicación $USD)
Un análisis indica que el Lado Recto ($4p$) de una tendencia de precios es $12$. Si el vértice es $(0, 10)$ y la curva abre hacia arriba, ¿en qué coordenada $y$ se ubica el foco?
a) $y = 13$
b) $y = 7$
c) $y = 16$
d) $y = 22$
```

---

## 7. Notas para el próximo tema
> [!tip] 💡 En la próxima clase
> Hoy aprendimos la **Ecuación Canónica**, que es genial porque nos muestra el vértice y el foco a simple vista. Sin embargo, en el mundo real, los datos suelen venir "desordenados". En la próxima clase aprenderemos la **Ecuación General de la Parábola**, donde desarrollaremos los binomios para entender la curva en su forma más pura.

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]