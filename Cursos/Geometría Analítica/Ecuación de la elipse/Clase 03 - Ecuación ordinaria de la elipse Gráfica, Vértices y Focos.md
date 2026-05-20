# Clase 03 — Ecuación ordinaria de la elipse: Gráfica, Vértices y Focos

**Tags:** #algebra #standardequation #ecuacion_ordinaria

**[[Clase 02]] | [[Índice]] | [[Clase 04]]**

---

### 1. RELEVANCIA Y APLICACIONES

La elipse es mucho más que un "círculo aplastado". Es la trayectoria que siguen los planetas y la curva que permite que estructuras masivas se mantengan en pie. En esta clase, aprenderás a traducir esta forma visual en una estructura algebraica precisa.

*   **$USD (Finanzas):** En paisajismo decorativo, el costo de materiales para bordes elípticos se calcula mediante la longitud de sus ejes. Un error en la ecuación puede significar un desperdicio de miles de dólares en materiales como mármol o acero inoxidable.
*   **Ingeniería:** Los arcos elípticos en puentes son preferidos por su capacidad para distribuir cargas de forma más uniforme que los arcos circulares. La ecuación ordinaria permite calcular los puntos exactos de tensión máxima.
*   **Cotidiano:** ¿Alguna vez has susurrado en un extremo de una sala y te han escuchado perfectamente al otro lado? Eso ocurre en las "galerías de susurros", donde la forma elíptica del techo hace que las ondas de sonido que salen de un **foco** reboten directamente hacia el otro **foco**.

---

### 2. CONCEPTO CLAVE: LA ECUACIÓN CANÓNICA/ORDINARIA

Para nosotros, la ecuación ordinaria será el **"ADN de la elipse"**: una fórmula que contiene toda la información genética (centro, tamaño y orientación) de la figura.

Dependiendo de hacia dónde se "estire" la elipse, utilizaremos uno de estos dos modelos:

| Orientación | Modelo Matemático | Características Clave |
| :--- | :--- | :--- |
| **Horizontal** | $\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1$ | $a^2$ (el número mayor) está bajo la $x$. |
| **Vertical** | $\frac{(x-h)^2}{b^2} + \frac{(y-k)^2}{a^2} = 1$ | $a^2$ (el número mayor) está bajo la $y$. |

> [!warning] **¡Cuidado con los signos del Centro $(h, k)$!**
> Al insertar las coordenadas del centro en la ecuación, sus signos siempre cambian debido al negativo de la fórmula.
> **Ejemplo:** Si el centro es $(-2, 5)$, la sustitución es $(x - (-2))^2$, lo que se convierte en $(x + 2)^2$. Por otro lado, la coordenada $k = 5$ se verá como $(y - 5)^2$.

> [!tip] **Regla de Oro: El parámetro $a$ manda**
> En una elipse, la distancia $a$ (del centro al vértice) es **siempre** mayor que $b$ y $c$. Por lo tanto, en la ecuación final, $a^2$ será siempre el denominador más grande.

---

### 3. PROCEDIMIENTO PASO A PASO

¡No te compliques! Si tienes una gráfica o puntos específicos, sigue esta receta de 4 pasos para obtener tu ecuación:

```ad-abstract
title: Pasos Universales para Armar la Ecuación
1. **Identificar la orientación:** Observa si el eje mayor (la parte más larga) es paralelo al eje $x$ o al eje $y$.
2. **Calcular el Centro $(h, k)$:** Es el punto medio entre los dos focos o entre los dos vértices. Usa la lógica: el centro está justo a la mitad de la distancia total.
3. **Determinar $a$ y $c$:** 
   - $a$ = distancia del centro a cualquier vértice del eje mayor.
   - $c$ = distancia del centro a cualquier foco.
4. **Calcular $b^2$ y ensamblar:** Usa la relación pitagórica $b^2 = a^2 - c^2$. Luego, sustituye $h, k, a^2$ y $b^2$ en el modelo que elegiste en el paso 1.
```

---

### 4. EJEMPLOS PRÁCTICOS

```ad-example
title: Ejemplo 1: De la Gráfica (Centro en Eje X)
**Datos:** Gráfica con centro en $(-3, 0)$. El eje mayor es vertical y mide $10$ unidades (del centro al extremo hay $5$). El eje menor mide $6$ unidades (del centro al lado hay $3$).
- **Paso 1:** Es vertical, por lo tanto $a^2$ va debajo de $y$.
- **Paso 2:** Centro $(h, k) = (-3, 0)$.
- **Paso 3:** $a = 5$ y $b = 3$.
- **Paso 4:** Sustituimos. Como $k = 0$, el término $(y - 0)^2$ se simplifica a $y^2$.
**Ecuación:** $\frac{(x+3)^2}{9} + \frac{y^2}{25} = 1$
```

```ad-success
title: Ejemplo 2: Vértices y Focos Horizontales
**Datos:** Vértices en $V_1(-1, 1)$ y $V_2(5, 1)$. Focos en $F_1(0, 1)$ y $F_2(4, 1)$.
- **Paso 1:** Los puntos comparten la misma $y=1$. Es **Horizontal**.
- **Paso 2:** Centro en el punto medio. Entre $x=-1$ y $x=5$ hay 6 unidades. La mitad es 3. El centro está en $(2, 1)$.
- **Paso 3:** $a = |5 - 2| = 3$. $c = |4 - 2| = 2$.
- **Paso 4:** $b^2 = a^2 - c^2 \Rightarrow b^2 = 3^2 - 2^2 = 9 - 4 = 5$.
**Ecuación:** $\frac{(x-2)^2}{9} + \frac{(y-1)^2}{5} = 1$
```

```ad-info
title: Ejemplo 3: Elipse Vertical con Detalles de Focos
**Datos:** Vértices en $V_1(-2, 5)$ y $V_2(-2, -1)$. Focos en $F_1(-2, 4)$ y $F_2(-2, 0)$.
- **Paso 1:** Alineación vertical (la $x$ es constante en $-2$). $a^2$ va bajo la $y$.
- **Paso 2:** Centro $(h, k)$. Punto medio entre focos: $k = (4 + 0) / 2 = 2$. Centro $= (-2, 2)$.
- **Paso 3:** $a$ es la distancia del centro $(-2, 2)$ al vértice $(-2, 5)$, así que $a = 3$. 
- **Paso 4:** $c$ es la distancia del centro al foco $F_1(-2, 4)$, así que $c = |4 - 2| = 2$.
- **Paso 5:** $b^2 = a^2 - c^2 = 3^2 - 2^2 = 5$.
**Ecuación:** $\frac{(x+2)^2}{5} + \frac{(y-2)^2}{9} = 1$
```

```ad-example
title: Ejemplo 4: Aplicación Presupuestaria ($USD)
Se diseña una claraboya elíptica. Los vértices están en $(0, 2)$ y $(0, -2)$. Se requiere un refuerzo de acero en el semieje mayor que cuesta **$5.50 USD** por unidad lineal.
- **Análisis:** El centro es $(0,0)$. El semieje mayor $a$ es la distancia de $(0,0)$ a $(0,2)$, es decir, $a = 2$.
- **Costo:** $2 \text{ unidades} \times 5.50 \text{ USD} = 11.00 \text{ USD}$ por cada semieje.
- **Ecuación:** Si $b=1$, tenemos $\frac{x^2}{1} + \frac{y^2}{4} = 1$.
```

---

### 5. EJERCICIOS PARA EL ESTUDIANTE

**Nivel Fácil (Identificación)**
1. Escribe la ecuación: centro $(0,0)$, $a=4$ (horizontal) y $b=2$.
2. Dada una gráfica con centro $(0,0)$, $a=2$ (horizontal) y $b=1$, halla su ecuación.
3. Si una elipse tiene $h=0$ y $k=3$, ¿cómo se escribe el numerador del término con $y$?
4. Identifica el centro de la elipse: $\frac{(x-5)^2}{16} + \frac{(y+8)^2}{25} = 1$.

**Nivel Medio (Cálculo)**
5. Hallar la ecuación: Vértices $(-3, -2)$ y $(7, -2)$, Focos $(-2, -2)$ y $(6, -2)$.
6. Hallar la ecuación: Vértices $(3, 2)$ y $(3, -6)$, Focos $(3, 1)$ y $(3, -5)$.
7. Escribe la ecuación con centro $(-3, 0)$, $a=5$ (vertical) y $b=3$.
8. Calcula $b^2$ si el centro es $(2, -2)$, el vértice es $(7, -2)$ y el foco es $(6, -2)$.

**Nivel Avanzado (Contextualizado)**
9. Una estructura elíptica tiene vértices en $(-2, 4)$ y $(-2, 0)$. Si la distancia focal $c$ es $1$, determina $b^2$ y la ecuación.
10. Diseña la ecuación: centro $(-1, -1)$, vertical, $a=4$ y $b^2=7$.
11. **Problema $USD:** Un arquitecto refuerza el eje mayor completo de una ventana elíptica con vértices en $(3, 2)$ y $(3, -6)$. Si el material cuesta **$5.50 USD** por unidad, ¿cuál es el costo total del refuerzo? (Calcula la distancia entre vértices primero).
12. Encuentra la ecuación: centro en el origen, eje mayor horizontal de longitud $10$ y eje menor de longitud $6$.

---

### 6. RESPUESTAS Y AUTOEVALUACIÓN

**Clave de Respuestas:**
1. $\frac{x^2}{16} + \frac{y^2}{4} = 1$
2. $\frac{x^2}{4} + y^2 = 1$
3. $(y-3)^2$
4. Centro $(5, -8)$
5. $\frac{(x-2)^2}{25} + \frac{(y+2)^2}{9} = 1$
6. $\frac{(x-3)^2}{7} + \frac{(y+2)^2}{16} = 1$ (Nota: $a=4, c=3 \Rightarrow b^2 = 16-9=7$)
7. $\frac{(x+3)^2}{9} + \frac{y^2}{25} = 1$
8. $b^2 = 9$ (donde $a=5$ y $c=4$)
9. $b^2 = 3$, Ec: $\frac{(x+2)^2}{3} + \frac{(y-2)^2}{4} = 1$
10. $\frac{(x+1)^2}{7} + \frac{(y+1)^2}{16} = 1$
11. Distancia eje mayor = $|2 - (-6)| = 8$ unidades. Costo: $8 \times 5.50 = 44.00 \text{ USD}$.
12. $\frac{x^2}{25} + \frac{y^2}{9} = 1$ (Si el eje mide $10$, entonces $a=5$).

> [!question] **Mini-Prueba de Autoevaluación**
> 1. **¿Bajo qué término se ubica $a^2$ en una elipse vertical?**
>    - a) Bajo $(x-h)^2$
>    - b) Bajo $(y-k)^2$
> 2. **Si el semieje mayor $a=5$ y la distancia focal $c=3$, ¿cuánto vale $b^2$?**
>    - a) $16$
>    - b) $4$
> 3. **Si un semieje mayor mide $10$ unidades y el material cuesta $5.50 USD$ por unidad, el costo de ese semieje es:**
>    - a) $55.00 USD$
>    - b) $110.00 USD$
>
> *Retroalimentación: 1-b ($a^2$ siempre acompaña al eje mayor), 2-a ($25-9=16$), 3-a ($10 \times 5.50 = 55$).*

---

### 7. CIERRE Y PRÓXIMO TEMA

Has dominado cómo construir la ecuación de la elipse cuando los datos son claros y ordenados. Sin embargo, en los exámenes y en la vida profesional, las ecuaciones a menudo aparecen "desordenadas" o expandidas.

En la **Clase 04**, daremos el gran salto hacia la **Ecuación General de la Elipse**, donde aprenderás a usar el desarrollo de binomios para identificar una elipse incluso cuando parece un simple polinomio largo. ¡Nos vemos en la siguiente sesión!

**[[Clase 02]] | [[Índice]] | [[Clase 04]]**