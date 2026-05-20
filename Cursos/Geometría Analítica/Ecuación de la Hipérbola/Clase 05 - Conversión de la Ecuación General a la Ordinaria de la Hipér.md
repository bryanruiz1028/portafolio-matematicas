# Clase 05 — Conversión de la Ecuación General a la Ordinaria de la Hipérbola y su Gráfica

> [!info] 🧭 Navegación
> **Curso:** Geometría Analítica Avanzada
> **Tags:** #matemáticas #geometría #hipérbola #ecuación-general #clase-05
> **Anterior:** [[Clase 04]] | **Siguiente:** [[Clase 06]]

---

## 1. Relevancia y Aplicaciones
La transición de la forma general a la ordinaria es el proceso de "limpieza algebraica" que nos permite identificar el centro, la orientación y las asíntotas de una hipérbola. Sin esta conversión, la ecuación general es una caja negra que oculta la trayectoria real de los puntos en el plano.

*   **💵 USD:** Se utiliza en modelos de optimización de costos donde la hipérbola define fronteras de eficiencia; el centro de la hipérbola representa el punto de equilibrio teórico entre inversión y riesgo.
*   **🏗️ Práctica:** El sistema de navegación LORAN (Long Range Navigation) se basa en la diferencia de tiempo de recepción de señales de radio, lo que genera hipérbolas cuya intersección define la posición exacta.
*   **📊 Cotidiana:** La observación de las sombras proyectadas por una lámpara circular sobre una superficie plana revela secciones hiperbólicas, cuya apertura depende del ángulo de incidencia de la luz.

---

## 2. Concepto Clave y Trucos Mnemotécnicos

> [!note] Definición
> Convertir la ecuación general ($Ax^2 + Cy^2 + Dx + Ey + F = 0$) a la ordinaria implica agrupar variables y completar trinomios cuadrados perfectos (TCP). Este proceso revela los parámetros $a$ y $b$, esenciales para ubicar el centro $(h, k)$ y los vértices.

> [!warning] ¡Cuidado con el signo negativo!
> El error más frecuente ocurre al factorizar el coeficiente negativo del segundo término. 
> *   **Ejemplo:** Si tienes $-4y^2 - 24y$, al extraer el $-4$, el signo interno **cambia**: $-4(y^2 + 6y)$. Olvidar este cambio de signo desplazará incorrectamente el centro de tu hipérbola.

> [!tip] La Regla de Oro de $a^2$
> En la hipérbola, **$a^2$ siempre es el denominador de la fracción positiva**. A diferencia de la elipse, aquí no importa cuál número es mayor; lo que define a $a^2$ es el signo positivo de su término ($x$ o $y$).

---

## 3. Procedimiento Paso a Paso

```text
PASO 1 → Agrupar términos de x y de y, y trasladar el término independiente (F) al lado derecho.
PASO 2 → Factorizar los coeficientes A y C de los términos cuadráticos como factores comunes.
PASO 3 → Completar el TCP: dividir el término lineal entre 2 y elevar al cuadrado. 
         IMPORTANTE: Para equilibrar la ecuación, suma al lado derecho el valor 
         agregado MULTIPLICADO por el factor común externo.
PASO 4 → Dividir toda la ecuación por el término independiente resultante para igualar a 1 
         y simplificar las fracciones.
```

---

## 4. Ejemplos Prácticos

> [!example] Ejemplo 1: Centro en el origen (0,0)
> **Ecuación:** $-9x^2 + 4y^2 - 36 = 0$
> 1. Transponemos: $-9x^2 + 4y^2 = 36$.
> 2. Dividimos entre 36: $\frac{-9x^2}{36} + \frac{4y^2}{36} = 1$.
> 3. Simplificamos: $-\frac{x^2}{4} + \frac{y^2}{9} = 1$.
> 4. Ordenamos por el positivo: $\frac{y^2}{9} - \frac{x^2}{4} = 1$.
> **Análisis:** Centro $(0,0)$, $a^2=9$ (Hipérbola Vertical), $b^2=4$.

> [!example] Ejemplo 2: Centro $(h, k)$ con balanceo de ecuación
> **Ecuación:** $9x^2 - 4y^2 - 18x - 24y - 63 = 0$
> 1. Agrupamos: $(9x^2 - 18x) + (-4y^2 - 24y) = 63$.
> 2. Factorizamos: $9(x^2 - 2x) - 4(y^2 + 6y) = 63$.
> 3. Completamos: $9(x^2 - 2x + 1) - 4(y^2 + 6y + 9) = 63 + 9(1) - 4(9)$.
> 4. Simplificamos derecha: $63 + 9 - 36 = 36$.
> 5. Forma ordinaria: $\frac{9(x-1)^2}{36} - \frac{4(y+3)^2}{36} = 1 \rightarrow \frac{(x-1)^2}{4} - \frac{(y+3)^2}{9} = 1$.
> **Análisis:** Centro $(1, -3)$, hipérbola horizontal con $a=2$ y $b=3$.

> [!example] Ejemplo 3: Caso Avanzado (División Inversa)
> **Ecuación:** $10x^2 - 3y^2 - 40x - 6y + 22 = 0$
> 1. Factorizamos y completamos: $10(x-2)^2 - 3(y+1)^2 = 15$.
> 2. Dividimos entre 15: $\frac{10(x-2)^2}{15} - \frac{3(y+1)^2}{15} = 1$.
> 3. Técnica de simplificación: Como 10 no divide exactamente a 15, dividimos numerador y denominador por 10:
>    $\frac{10/10}{15/10} = \frac{1}{1.5}$.
> **Resultado:** $\frac{(x-2)^2}{1.5} - \frac{(y+1)^2}{5} = 1$.

> [!example] Ejemplo 4: Aplicación USD
> Una empresa modela su beneficio marginal con la curva $8x^2 - 12y^2 + 112x + 120y - 4 = 0$, donde $x$ es la inversión y $y$ el retorno en miles de dólares.
> 1. Factorización y balanceo: $8(x^2 + 14x + 49) - 12(y^2 - 10y + 25) = 4 + 392 - 300$.
> 2. Simplificación: $8(x+7)^2 - 12(y-5)^2 = 96$.
> 3. Dividimos entre 96: $\frac{(x+7)^2}{12} - \frac{(y-5)^2}{8} = 1$.
> **Análisis:** El centro de operaciones se ubica en $(-7, 5)$, indicando el punto de referencia para los cálculos de rentabilidad.

---

## 5. Ejercicios para el Estudiante

> [!abstract] Práctica Dirigida
> ### Nivel Fácil (Centro en el origen)
> 1. $16y^2 - 9x^2 = 144$
> 2. $25x^2 - 4y^2 - 100 = 0$
> 3. $y^2 - x^2 - 25 = 0$
> 4. $9y^2 - 16x^2 - 144 = 0$
> 
> ### Nivel Medio (Centro h, k)
> 1. $16x^2 - 9y^2 + 32x + 36y - 164 = 0$
> 2. $9x^2 - 16y^2 - 54x + 64y - 127 = 0$
> 3. $4y^2 - 9x^2 + 16y + 18x - 29 = 0$
> 4. $-x^2 + y^2 - 4x + 6y - 4 = 0$
> 
> ### Nivel Avanzado (Contexto USD)
> 1. **Análisis de Mercado:** Una curva de oferta y demanda sigue la ecuación $5x^2 - 4y^2 + 20x + 8y - 4 = 0$. Determine el centro $(h, k)$ de estabilidad.
> 2. **Límite de Beneficios:** El margen operativo de una startup se define por $2x^2 - 3y^2 - 12x - 12y - 6 = 0$. Encuentre la forma ordinaria.
> 3. **Presupuesto:** La frontera de inversión de un proyecto se rige por $7x^2 - 9y^2 + 14x + 36y - 92 = 0$. Halle el centro y los radios $a$ y $b$.
> 4. **Zona de Ganancia:** Determine la región de apertura de la hipérbola de producción $6y^2 - 10x^2 + 12y + 40x - 94 = 0$.

---

## 6. Respuestas para el Docente

> [!success] Clave de Respuestas Completa
> **Nivel Fácil:** 
> 1) $\frac{y^2}{9}-\frac{x^2}{16}=1$ | 2) $\frac{x^2}{4}-\frac{y^2}{25}=1$ | 3) $\frac{y^2}{25}-\frac{x^2}{25}=1$ | 4) $\frac{y^2}{16}-\frac{x^2}{9}=1$
> 
> **Nivel Medio:** 
> 1) $\frac{(x+1)^2}{9}-\frac{(y-2)^2}{16}=1$, C$(-1,2)$
> 2) $\frac{(x-3)^2}{16}-\frac{(y-2)^2}{9}=1$, C$(3,2)$
> 3) $\frac{(y+2)^2}{9}-\frac{(x-1)^2}{4}=1$, C$(1,-2)$
> 4) $\frac{(y+3)^2}{9}-\frac{(x+2)^2}{9}=1$, C$(-2,-3)$
> 
> **Nivel Avanzado:**
> 1) $\frac{(x+2)^2}{4}-\frac{(y-1)^2}{5}=1$, C$(-2,1)$
> 2) $\frac{(x-3)^2}{6}-\frac{(y+2)^2}{4}=1$, C$(3,-2)$
> 3) $\frac{(x+1)^2}{9}-\frac{(y-2)^2}{7}=1$, C$(-1,2)$
> 4) $\frac{(y+1)^2}{10}-\frac{(x-2)^2}{6}=1$, C$(2,-1)$

---

## 7. Mini-Prueba de Autoevaluación

> [!question] Evaluación Rápida
> 1. **Conceptual:** En la forma ordinaria, ¿qué nos indica el hecho de que el término con la variable $x$ sea el negativo?
>    *   *R: Indica que el eje real es vertical (la hipérbola abre hacia arriba y hacia abajo).*
> 2. **Procedimental:** Al resolver $5(x^2 + 8x)$, ¿qué valor exacto se debe sumar al lado derecho si completamos el TCP con un $16$?
>    *   *R: Se debe sumar $80$ (el producto de $5 \times 16$).*
> 3. **Aplicación USD:** Si una hipérbola de costos tiene $a=4$ y $b=3$, calcule el lado recto ($LR$) que mide el margen de fluctuación de precios.
>    *   *R: $LR = \frac{2b^2}{a} = \frac{2(9)}{4} = 4.5$.*

---

## 8. Cierre de Clase

> [!tip] Próxima Estación
> Con los valores de $a$, $b$ y el centro $(h, k)$ dominados, en la **[[Clase 06]]** aprenderemos a trazar las **asíntotas**, las guías maestras que controlan el comportamiento de la hipérbola en el infinito.

> [!info] 🧭 Navegación
> **Anterior:** [[Clase 04]] | **Siguiente:** [[Clase 06]]