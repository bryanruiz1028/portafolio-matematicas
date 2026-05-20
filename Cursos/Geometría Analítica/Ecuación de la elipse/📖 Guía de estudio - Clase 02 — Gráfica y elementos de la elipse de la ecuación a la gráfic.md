# 📖 Guía de estudio — Clase 02: Gráfica y elementos de la elipse a partir de la ecuación canónica

Esta guía detalla los procedimientos para identificar, calcular y graficar los elementos de una elipse utilizando su ecuación canónica u ordinaria, siguiendo el método de conteo visual en el plano cartesiano.

> [!info] 📌 Conceptos clave
> 1.  **Identificación de parámetros ($a$ y $b$):** En la ecuación, los denominadores son los cuadrados de los semiejes. El valor $a^2$ es **siempre el número mayor** ($a > b$). Para graficar, extraemos la raíz cuadrada para obtener los valores lineales de $a$ y $b$.
> 2.  **Orientación de la elipse:** Se determina observando dónde se ubica el denominador mayor ($a^2$):
>     *   Si $a^2$ está bajo la $x$, el eje mayor es paralelo al eje $X$ (elipse **horizontal** o "más gorda").
>     *   Si $a^2$ está bajo la $y$, el eje mayor es paralelo al eje $Y$ (elipse **vertical** o "más flaca").
> 3.  **El Centro $(h, k)$:** Se extrae de los términos $(x-h)$ y $(y-k)$ aplicando un **cambio de signo**.
>     *   *Nota importante:* Si la variable está sola (ej. $x^2$ o $y^2$), la coordenada correspondiente es $0$.
> 4.  **Elementos auxiliares ($c$ y $LR$):** El valor $c$ es la distancia focal. El Lado Recto ($LR$) determina el ancho de la elipse sobre los focos para dar precisión al trazo manual.

---

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Centro $(h, k)$** | Punto central. Se invierten los signos de los números junto a $x$ e $y$. Si la variable está sola, ese valor es $0$. |
| **Semieje mayor ($a$)** | $a = \sqrt{a^2}$. Es la distancia del centro a los vértices principales ($V_1, V_2$). |
| **Semieje menor ($b$)** | $b = \sqrt{b^2}$. Es la distancia del centro a los vértices secundarios ($B_1, B_2$). |
| **Distancia focal ($c$)** | $c = \sqrt{a^2 - b^2}$. Es la distancia del centro a cada foco ($F_1, F_2$). |
| **Lado Recto ($LR$)** | $LR = \frac{2b^2}{a}$. Se grafican $\frac{LR}{2}$ unidades a cada lado del foco (perpendicular al eje mayor). |

---

## Ejemplos resueltos

```ad-example
title: Ejemplo A — Caso con centro fuera del origen
**Enunciado:** Graficar la elipse de la ecuación $\frac{(x-3)^2}{16} + \frac{(y+1)^2}{4} = 1$ y hallar todos sus vértices.

**Resolución paso a paso:**
1. **Identificar el centro:** Cambiamos los signos de $-3$ y $+1$. El centro es $C(3, -1)$.
2. **Determinar parámetros y orientación:** El denominador mayor es $16$ ($a^2$) y está bajo $x$. La elipse tiene su eje mayor paralelo al eje $X$ (**Horizontal**).
   - $a = \sqrt{16} = 4$
   - $b = \sqrt{4} = 2$
3. **Calcular distancia focal ($c$):** $c = \sqrt{16 - 4} = \sqrt{12} \approx 3.46$.
4. **Calcular Lado Recto ($LR$):** $LR = \frac{2(4)}{4} = 2$. Usaremos $1$ unidad hacia arriba y $1$ hacia abajo desde cada foco.
5. **Graficar mediante el "Método de Conteo":**
   - **Vértices principales ($V$):** Desde el centro $C(3, -1)$, contamos $a=4$ unidades a la derecha y $4$ a la izquierda: $V_1(7, -1)$ y $V_2(-1, -1)$.
   - **Vértices secundarios ($B$):** Desde el centro, contamos $b=2$ unidades hacia arriba y $2$ hacia abajo: $B_1(3, 1)$ y $B_2(3, -3)$.
   - **Focos ($F$):** Desde el centro, contamos $c \approx 3.46$ unidades a la derecha e izquierda: $F_1(6.46, -1)$ y $F_2(-0.46, -1)$.
```

```ad-example
title: Ejemplo B — Aplicación real: Diseño de un parque elíptico ($USD)
**Enunciado:** Una plaza elíptica sigue la ecuación $\frac{x^2}{25} + \frac{y^2}{9} = 1$ (en metros). El costo del césped es $\$12 \, USD/m^2$. Hallar la ubicación de las fuentes (focos), el área y el presupuesto.

**Resolución:**
1. **Parámetros:** Centro en $(0, 0)$. $a = \sqrt{25} = 5$, $b = \sqrt{9} = 3$. Es horizontal.
2. **Fuentes (Focos):** $c = \sqrt{25 - 9} = \sqrt{16} = 4$. 
   - **Coordenadas:** Al contar $4$ unidades desde el origen: $F_1(4, 0)$ y $F_2(-4, 0)$.
3. **Área ($A$):** $A = \pi \cdot a \cdot b = \pi \cdot 5 \cdot 3 = 15\pi \approx 47.12 \, m^2$.
4. **Presupuesto:** $47.12 \, m^2 \cdot \$12 \, USD = \$565.44 \, USD$.

**Resultado:** Fuentes en $(4, 0)$ y $(-4, 0)$; Presupuesto total: $\$565.44 \, USD$.
```

---

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
1. Dada la ecuación $\frac{x^2}{9} + \frac{y^2}{4} = 1$, identifica el centro y los valores de $a$ y $b$.
2. ¿Hacia qué eje es paralela una elipse si su ecuación es $\frac{x^2}{10} + \frac{y^2}{25} = 1$?
3. Encuentra el valor de $c$ si $a^2 = 25$ y $b^2 = 9$.
```

```ad-abstract
title: 🟡 Medio
1. A partir de la ecuación $\frac{(x+4)^2}{20} + \frac{y^2}{9} = 1$, halla el centro y los vértices principales (usa $\sqrt{20} \approx 4.5$).
2. Calcula la medida del Lado Recto ($LR$) para la elipse $\frac{(x-2)^2}{25} + \frac{(y-3)^2}{9} = 1$.
3. Determina las coordenadas de los focos y los vértices secundarios para una elipse con centro en $(-1, 3)$, $a=5$ y $b=3$, siendo horizontal.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
1. Una pista de patinaje tiene la ecuación $\frac{x^2}{100} + \frac{y^2}{64} = 1$. Se debe cercar el perímetro. Si el metro de valla cuesta $\$25 \, USD$, ¿cuál es el costo total?
   - *Pista:* Usa la fórmula $P \approx 2\pi \sqrt{\frac{a^2+b^2}{2}}$. Calcula primero la fracción dentro de la raíz.
2. Si se instalan dos parlantes en los focos de la pista anterior, ¿cuáles son las coordenadas exactas de los parlantes?
```

---

> [!tip] 💡 Consejo de estudio
> Para no confundir $a$ con $b$, antes de calcular, identifica la orientación. Mira los denominadores:
> - Si el mayor está bajo $x$: Anota **"Horizontal (más gorda)"**. El eje mayor es paralelo al eje $X$.
> - Si el mayor está bajo $y$: Anota **"Vertical (más flaca)"**. El eje mayor es paralelo al eje $Y$.
> Esto te guiará para saber si debes realizar el "conteo" de unidades hacia los lados o hacia arriba y abajo.