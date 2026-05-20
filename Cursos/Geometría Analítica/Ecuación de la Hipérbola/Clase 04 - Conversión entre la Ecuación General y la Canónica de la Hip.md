# Clase 04 — Conversión entre la Ecuación General y la Canónica de la Hipérbola

tags: #algebra #convertingfromt
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 4 de 7

> [!info] 🧭 Navegación
> [[Clase 03 — Elementos y Ecuación Canónica]] | [[00 - Índice del curso]] | [[Clase 05 — Gráfica de la Hipérbola desde su Ecuación]]

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> Dominar la conversión de ecuaciones es lo que permite a un ingeniero o arquitecto pasar de un listado de datos fríos (forma general) a un mapa de construcción real (forma canónica). Sin este proceso, no podríamos localizar con precisión los puntos de retorno de un satélite o el punto exacto de resistencia de una columna.
> 
> *   **💵 [aplicación con $USD]:** Modelado de curvas de oferta y demanda en mercados de alta volatilidad, donde los precios de activos fluctúan siguiendo trayectorias hiperbólicas.
> *   **🏗️ [aplicación práctica]:** Diseño de torres de enfriamiento y estructuras hiperboloides; la ecuación general nos da la resistencia del material, pero la canónica nos dice dónde colocar los soportes.
> *   **📊 [situación cotidiana]:** Sistemas de posicionamiento global (GPS) y triangulación de señales; se utiliza la diferencia de tiempos para convertir ecuaciones generales en coordenadas útiles.

## Concepto clave

> [!note] El cambio de "traje" de la hipérbola
> Imagina que la hipérbola es una persona. La **Ecuación General** es como su traje de gala: está organizada, igualada a cero y lista para una base de datos (fines algebraicos). Pero la **Ecuación Canónica** (u Ordinaria) es su traje de trabajo: nos revela de inmediato su centro $(h, k)$, su orientación y qué tan abierta es (fines geométricos). Cambiamos el "traje" para que nos sea más útil, pero la identidad (su lugar en el plano) nunca cambia.

> [!warning] ⚠️ Error común: El signo del factor común
> El error más grave ocurre al completar el trinomio. Si el factor común que extraes es negativo (lo cual es obligatorio para la segunda variable de la hipérbola), ese signo **afecta** al número que sumas al otro lado de la balanza. Si olvidas multiplicar el nuevo término por el factor común (incluyendo su signo), la balanza se rompe y la hipérbola se deforma.

> [!tip] 💡 Truco para recordarlo
> Regla mnemotécnica: **"Carita feliz para expandir, completar para reducir"**. Usamos el método de la mariposa para llegar a la forma General y completamos cuadrados para llegar a la Canónica.

## Procedimiento paso a paso

Sigue esta secuencia lógica para transformar de forma General a Canónica:

```text
PASO 1 → Agrupar: Junta los términos con 'x' y los términos con 'y'. Pasa el número solo (término independiente) al lado derecho del igual.
PASO 2 → Factor común: Saca como factor común el número que acompaña a x² y a y². ¡OJO! En la hipérbola, uno de estos factores DEBE ser negativo para que las variables tengan signos distintos.
PASO 3 → Completar y Equilibrar: En cada paréntesis, toma el número de la variable lineal, divídelo entre 2 y elévalo al cuadrado (B/2)². Suma este valor dentro y, al otro lado del igual, suma ese mismo valor MULTIPLICADO por el factor común de afuera.
PASO 4 → Simplificar: Divide toda la ecuación por el número resultante a la derecha para obtener un "1" y simplifica las fracciones.
```

## Ejemplos guiados

> [!example] Ejemplo 1 (Caso Básico - Centro en el origen)
> **Problema:** Transforma $4x^2 - 9y^2 - 36 = 0$ a su forma canónica.
> 1. Movemos el término independiente: $4x^2 - 9y^2 = 36$.
> 2. Dividimos todo entre $36$ para obtener el $1$: $\frac{4x^2}{36} - \frac{9y^2}{36} = \frac{36}{36}$.
> 3. Simplificamos:
>    - $\frac{4}{36}$ tiene cuarta: $1$ y $9 \rightarrow \frac{x^2}{9}$.
>    - $\frac{9}{36}$ tiene novena: $1$ y $4 \rightarrow \frac{y^2}{4}$.
> **Resultado:** $\frac{x^2}{9} - \frac{y^2}{4} = 1$.

> [!example] Ejemplo 2 (Caso con Centro $(h,k)$)
> **Problema:** Convierte $-4x^2 + 7y^2 + 8x + 42y + 31 = 0$ a canónica.
> 1. Agrupamos: $(-4x^2 + 8x) + (7y^2 + 42y) = -31$.
> 2. Factorizamos coeficientes: $-4(x^2 - 2x) + 7(y^2 + 6y) = -31$.
> 3. Completamos: 
>    - Para $x$: $(\frac{2}{2})^2 = 1$. Sumamos $1 \cdot (-4) = -4$ al lado derecho.
>    - Para $y$: $(\frac{6}{2})^2 = 9$. Sumamos $9 \cdot (7) = 63$ al lado derecho.
>    - Ecuación: $-4(x-1)^2 + 7(y+3)^2 = -31 - 4 + 63 \rightarrow 28$.
> 4. Dividimos entre $28$ y simplificamos: $-\frac{(x-1)^2}{7} + \frac{(y+3)^2}{4} = 1$.
> **Resultado:** $\frac{(y+3)^2}{4} - \frac{(x-1)^2}{7} = 1$.

> [!example] Ejemplo 3 (De Canónica a General)
> **Problema:** Convierte $\frac{(x+7)^2}{12} - \frac{(y-5)^2}{8} = 1$.
> 1. Carita feliz (MCM $12 \cdot 8 = 96$): $\frac{8(x+7)^2 - 12(y-5)^2}{96} = 1$.
> 2. Pasamos el $96$: $8(x^2 + 14x + 49) - 12(y^2 - 10y + 25) = 96$.
> 3. Distribuimos: $8x^2 + 112x + 392 - 12y^2 + 120y - 300 = 96$.
> 4. Igualamos a cero: $8x^2 - 12y^2 + 112x + 120y - 4 = 0$.
> **Resultado:** $8x^2 - 12y^2 + 112x + 120y - 4 = 0$.

> [!example] Ejemplo 4 (Aplicación Real con $USD)
> **Problema:** Una maquinaria de $\$28,000$ USD se deprecia según $-7x^2 + 4y^2 + 24y + 8 = 0$, donde $y$ es el valor (en miles) y $x$ el tiempo (años). Halla la forma canónica e interpreta su centro.
> 1. Agrupamos y movemos el $8$: $-7x^2 + 4(y^2 + 6y) = -8$.
> 2. Completamos cuadrado para $y$: $(\frac{6}{2})^2 = 9$. Sumamos $9 \cdot 4 = 36$ al lado derecho.
> 3. Ecuación: $-7x^2 + 4(y+3)^2 = 28$.
> 4. Dividimos entre $28$: $-\frac{x^2}{4} + \frac{(y+3)^2}{7} = 1$.
> **Interpretación:** El centro en $(0, -3)$ indica que el modelo matemático sitúa el inicio de la depreciación máxima fuera del tiempo positivo, sugiriendo que la maquinaria pierde su valor útil de forma acelerada tras el primer año.

## Ejercicios y autoevaluación

> [!abstract] | green Nivel 1: Fácil (Centro en el origen)
> 1. $2x^2 - 5y^2 - 10 = 0$
> 2. $6y^2 - 12x^2 - 72 = 0$
> 3. $x^2 - y^2 - 1 = 0$
> 4. $9x^2 - 4y^2 - 36 = 0$

> [!abstract] | yellow Nivel 2: Medio (Completar cuadrados)
> 1. $10x^2 - 5y^2 - 40x - 40y - 90 = 0$
> 2. $12x^2 - 6y^2 - 96x + 120 = 0$
> 3. $4y^2 - 7x^2 + 24y - 8 = 0$
> 4. $9y^2 - 16x^2 - 162y - 128x - 151 = 0$

> [!abstract] | red Nivel 3: Avanzado (Contexto Financiero)
> 1. Un gasto logístico de $\$1,008$ USD sigue la forma: $-9x^2 + 16y^2 - 72x - 288y + 1008 = 0$. Pasa a canónica.
> 2. Halla la forma general si el centro es $(4, 9)$ y los parámetros son $a^2=12, b^2=8$ (horizontal).
> 3. Un activo de $\$25,000$ USD fluctúa según $\frac{(y-9)^2}{9} - \frac{(x+4)^2}{16} = 1$. Encuentra su forma general.

> [!success] Soluciones para el Docente
> *   **Nivel 1:** 1) $\frac{x^2}{5} - \frac{y^2}{2} = 1$ | 2) $\frac{y^2}{12} - \frac{x^2}{6} = 1$ | 3) $\frac{x^2}{1} - \frac{y^2}{1} = 1$ | 4) $\frac{x^2}{4} - \frac{y^2}{9} = 1$.
> *   **Nivel 2:** 1) $\frac{(x-2)^2}{5} - \frac{(y+4)^2}{10} = 1$ | 2) $\frac{(x-4)^2}{6} - \frac{y^2}{12} = 1$ | 3) $\frac{(y+3)^2}{7} - \frac{x^2}{4} = 1$ | 4) $\frac{(y-9)^2}{16} - \frac{(x+4)^2}{9} = 1$.
> *   **Nivel 3:** 1) $\frac{(y-9)^2}{9} - \frac{(x+4)^2}{16} = 1$ | 2) $8x^2 - 12y^2 - 64x + 216y - 928 = 0$ | 3) $16y^2 - 9x^2 - 288y - 72x + 1008 = 0$.

## Mini-prueba de autoevaluación

> [!question] Pregunta 1
> Si en la ecuación general solo aparecen $x^2$ y $y^2$ sin términos lineales, ¿qué podemos afirmar del centro?
> *Respuesta: El centro de la hipérbola se encuentra en el origen $(0,0)$.*

> [!question] Pregunta 2
> Al completar el cuadrado en $-5y^2 - 40y$, ¿qué valor equilibras al otro lado tras sumar $16$ en el paréntesis?
> *Respuesta: Se debe sumar $-80$, ya que $16 \cdot (-5) = -80$.*

> [!question] Pregunta 3
> Si una inversión de $\$144,000$ USD sigue la forma $\frac{y^2}{9} - \frac{x^2}{16} = 1$, ¿cuál es su término independiente $F$?
> *Respuesta: $F = -144$ (al multiplicar por el MCM y pasar todo a un lado).*

## Notas para el próximo tema

> [!tip] 💡 En la próxima clase
> Utilizaremos estas conversiones para extraer los valores de $a$, $b$ y $c$. Con ellos, aprenderemos a graficar las asíntotas, que son las "paredes invisibles" que guían la forma de nuestra hipérbola.

> [!info] 🧭 Navegación
> [[Clase 03 — Elementos y Ecuación Canónica]] | [[00 - Índice del curso]] | [[Clase 05 — Gráfica de la Hipérbola desde su Ecuación]]