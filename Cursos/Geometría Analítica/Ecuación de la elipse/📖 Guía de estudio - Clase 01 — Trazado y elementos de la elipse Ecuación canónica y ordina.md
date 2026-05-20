# 📖 Guía de estudio — Clase 01: Trazo y elementos de la elipse

### 1. RESUMEN DE CONCEPTOS CLAVE

> [!info] 📌 Conceptos clave
> * **Definición geométrica:** La elipse es el conjunto de puntos en un plano cuya suma de distancias a dos puntos fijos (focos) es siempre la misma. Esta suma constante es igual a la longitud del eje mayor ($2a$).
> * **La analogía de la "pita" (cuerda):** Al fijar una cuerda a dos puntillas (focos) y tensarla con un lápiz, el trazo resultante es una elipse. La longitud total de esa cuerda estirada representa siempre la medida del eje mayor.
> * **Relación fundamental:** Los parámetros $a, b$ y $c$ forman un triángulo rectángulo donde el **semieje mayor ($a$) es la hipotenusa**. Esto ocurre porque la distancia de un foco al extremo del eje menor es exactamente $a$. De ahí surge nuestra fórmula: $a^2 = b^2 + c^2$.
> * **Orientación visual:** El número mayor en el denominador de la ecuación siempre es $a^2$. 
>     * Si $a^2$ está bajo la $x \rightarrow$ La elipse es **Horizontal**.
>     * Si $a^2$ está bajo la $y \rightarrow$ La elipse es **Vertical**.

---

### 2. FÓRMULAS Y DEFINICIONES IMPORTANTES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Semieje mayor ($a$)** | Distancia del centro al vértice más lejano. |
| **Semieje menor ($b$)** | Distancia del centro al vértice más cercano. |
| **Semieje focal ($c$)** | Distancia del centro a cada foco. |
| **Eje mayor** | Segmento total entre vértices lejanos. Medida: $2a$. |
| **Eje menor** | Segmento total entre vértices cercanos. Medida: $2b$. |
| **Eje focal** | Distancia total entre ambos focos. Medida: $2c$. |
| **Relación de Pitágoras** | $a^2 = b^2 + c^2$ (donde $a$ es el valor más grande). |
| **Lado Recto (LR)** | Ancho de la elipse en los focos. Fórmula: $LR = \frac{2b^2}{a}$. |
| **Ecuación Canónica** | Con Centro $(0,0)$: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ o $\frac{x^2}{b^2} + \frac{y^2}{a^2} = 1$. |

---

### 3. EJEMPLOS RESUELTOS ADICIONALES

```ad-example
title: Ejemplo A — Identificación de elementos
**Problema:** Dada la ecuación $\frac{x^2}{25} + \frac{y^2}{9} = 1$, identifica sus elementos y orientación.

**Paso a paso:**
1. **Identificar $a^2$ y $b^2$:** El número mayor es $a^2$. Entonces, $a^2 = 25$ y $b^2 = 9$.
2. **Calcular semiejes:** Extraemos raíces cuadradas. $a = \sqrt{25} = 5$ y $b = \sqrt{9} = 3$.
3. **Orientación:** Como el $25$ ($a^2$) está debajo de la $x^2$, la elipse es **horizontal**.
4. **Vértices:** Al ser horizontal con centro $(0,0)$, los vértices principales están en $(\pm 5, 0)$.
```

```ad-example
title: Ejemplo B — Diseño de una mesa elíptica
**Problema:** Un carpintero cobra $10 USD por cada decímetro (dm) de longitud del eje mayor. Si la mesa sigue la ecuación $\frac{x^2}{16} + \frac{y^2}{4} = 1$, ¿cuánto cobrará?

**Resolución:**
1. **Hallar $a$ (en dm):** El denominador mayor es $16$, por lo que $a^2 = 16$. Calculamos $a = \sqrt{16} = 4$ dm.
2. **Calcular el eje mayor:** La longitud total es $2a$, es decir, $2 \times 4 \text{ dm} = 8$ dm.
3. **Cálculo del costo:** Multiplicamos la longitud por el precio: $8 \text{ dm} \times 10 \text{ USD/dm} = \mathbf{80 \text{ USD}}$.
```

---

### 4. EJERCICIOS DE REPASO

```ad-abstract
title: Nivel Verde (Fácil)
Identifica los valores de los semiejes $a$ y $b$ en las siguientes ecuaciones:
1. $\frac{x^2}{100} + \frac{y^2}{64} = 1$
2. $\frac{x^2}{4} + \frac{y^2}{49} = 1$
```

```ad-abstract
title: Nivel Amarillo (Medio)
Dada la elipse con centro en el origen $\frac{x^2}{25} + \frac{y^2}{16} = 1$:
1. Calcula la distancia focal ($c$) usando la relación de Pitágoras ($a^2 = b^2 + c^2$).
2. Calcula la medida del Lado Recto (LR).
```

```ad-abstract
title: Nivel Rojo (Avanzado - Aplicación $USD)
Se desea cercar la línea del eje mayor de un jardín elíptico cuya ecuación es $\frac{x^2}{64} + \frac{y^2}{36} = 1$. Si el metro de cerca cuesta $50 USD, ¿cuál es el costo total del cercado para esa línea específica?
```

**¡No te rindas!** Si al resolver los ejercicios los resultados te dan decimales, no te asustes: en la geometría de la vida real es muy común. ¡Vas por excelente camino! 🚀

---

### 5. CONSEJO DE ESTUDIO

> [!tip] 💡 Consejo de estudio
> Para no olvidar la importancia de "$a$", asóciala con la letra **"Alfa"** (la primera y más grande). En la elipse, el número más grande en el denominador siempre será tu $a^2$. Ese número es el "jefe": si está debajo de la $X$, la elipse se extiende horizontalmente; si está bajo la $Y$, se estira verticalmente. ¡El número mayor siempre manda en la orientación!