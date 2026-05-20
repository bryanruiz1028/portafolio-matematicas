# 📖 Guía de estudio — Clase 02: Gráfica de la Hipérbola a partir de su Ecuación Ordinaria

> [!info] 📌 Conceptos clave
> - **Identificación de la Orientación:** El eje principal (o **Eje Real**) es paralelo al eje de la variable cuya fracción es positiva. Si la fracción con $x$ es positiva, la hipérbola abre hacia los lados (horizontal); si la fracción con $y$ es positiva, abre hacia arriba y abajo (vertical).
> - **Determinación del Centro $(h, k)$:** Se extraen los valores que acompañan a $x$ e $y$ aplicando el opuesto aditivo (cambiando el signo). Recuerda: $h$ siempre acompaña a $x$ y $k$ siempre acompaña a $y$.
> - **Relación de Denominadores:** A diferencia de la elipse, en la hipérbola $a^2$ **siempre** es el denominador de la fracción positiva, sin importar si es el número mayor o menor. El denominador de la fracción negativa es $b^2$.
> - **Teorema de Pitágoras para la Hipérbola:** Para hallar la distancia focal ($c$), usamos la relación $c = \sqrt{a^2 + b^2}$.
> - **Lado Recto (LR):** Define el ancho de las ramas en los focos. Para graficar con precisión, se debe contar la mitad del valor del lado recto ($LR/2$) hacia cada lado del foco.

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Centro $(h, k)$** | Punto de simetría central. Se obtiene invirtiendo los signos de la ecuación: $(x-h)$ y $(y-k)$. |
| **Valor de $a$ (Semieje Real)** | Distancia del centro a los **vértices**. Se calcula como $\sqrt{\text{denominador positivo}}$. |
| **Valor de $b$ (Semieje Imaginario)** | Distancia para construir el rectángulo guía. Se calcula como $\sqrt{\text{denominador negativo}}$. |
| **Valor de $c$ (Distancia Focal)** | Distancia del centro a los **focos**. Se calcula con $c = \sqrt{a^2 + b^2}$. |
| **Lado Recto (LR)** | Longitud del segmento perpendicular al eje real que pasa por los focos. $LR = \frac{2b^2}{a}$. |

## Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A — Eje Principal Paralelo al Eje X (Horizontal)
**Enunciado:** Graficar la hipérbola $\frac{(x-5)^2}{25} - \frac{(y+2)^2}{16} = 1$.

**Pasos Pedagógicos:**
1. **Centro:** Al extraer los valores y cambiar signos, el centro se ubica en **$C(5, -2)$**.
2. **Dimensiones:** 
   - $a = \sqrt{25} = 5$ (Unidades a contar en el eje $X$ por ser la fracción positiva).
   - $b = \sqrt{16} = 4$ (Unidades a contar en el eje $Y$).
3. **Cálculo de $c$:** $c = \sqrt{25 + 16} = \sqrt{41} \approx 6.4$.
4. **Lado Recto:** $LR = \frac{2(16)}{5} = 6.4$. Para graficar, usamos $LR/2 = 3.2$.

**Resultado Final:** 
- **Vértices:** Al ser horizontal, sumamos/restamos $a$ a la coordenada $h$: $V_1(0, -2)$ y $V_2(10, -2)$.
- **Focos:** Sumamos/restamos $c$ a la coordenada $h$: $F_1(-1.4, -2)$ y $F_2(11.4, -2)$.
```

```ad-example
title: Ejemplo B — Aplicación en Análisis Financiero $USD
**Enunciado:** Una empresa modela sus proyecciones de flujo de caja mediante la ecuación $\frac{(y+2)^2}{9} - \frac{(x-4)^2}{25} = 1$, donde $y$ representa la utilidad neta en miles de $USD.

**Análisis del Especialista:**
1. **Orientación:** La fracción positiva contiene a $y$, indicando un **Eje Transverso vertical**. Esto significa que los cambios para hallar vértices y focos se aplicarán a la coordenada $k$ del centro.
2. **Centro:** El punto de equilibrio base es **$C(4, -2)$**.
3. **Parámetros:** $a = \sqrt{9} = 3$ y $b = \sqrt{25} = 5$.
4. **Interpretación de Vértices:** Los vértices representan los límites críticos del modelo:
   - **Límite de Ganancia:** $V_1(4, -2+3) = (4, 1)$. Indica una ganancia mínima de **$1,000 USD**.
   - **Límite de Pérdida:** $V_2(4, -2-3) = (4, -5)$. Indica una pérdida máxima manejable de **$5,000 USD**.
5. **Focos:** Con $c = \sqrt{9+25} \approx 5.8$, los focos se ubican en $F_1(4, 3.8)$ y $F_2(4, -7.8)$.
```

## Ejercicios de Repaso

```ad-abstract
title: 🟢 Nivel: Fácil
Dada la ecuación $\frac{(x-3)^2}{16} - \frac{(y-1)^2}{9} = 1$:
1. Identifique las coordenadas del centro.
2. Calcule los valores de $a$, $b$ y $c$.
3. Determine si el eje real es horizontal o vertical.
```

```ad-abstract
title: 🟡 Nivel: Medio
Para la hipérbola $\frac{(y+1)^2}{16} - \frac{(x-3)^2}{9} = 1$, realice lo siguiente:
1. Obtenga el centro, los vértices y los focos.
2. Calcule la medida del Lado Recto (LR).
3. ¿Cuántas unidades debe contar desde el foco hacia los lados para marcar los puntos extremos de la curva?
```

```ad-abstract
title: 🔴 Nivel: Avanzado (Mercado de Divisas)
En un análisis de mercado, se utiliza la ecuación $\frac{x^2}{20} - \frac{(y-6)^2}{14} = 1$ para describir la volatilidad de una divisa.
1. Determine el centro (considere el caso donde $x$ no tiene un número restando).
2. Calcule las coordenadas exactas de los focos utilizando $c = \sqrt{a^2 + b^2}$.
3. Explique por qué esta hipérbola es horizontal a pesar de que $20$ no es un cuadrado perfecto entero.
```

> [!tip] 💡 Consejo de estudio del Profe Alex
> ¡No te lances a dibujar a ciegas! Primero, identifica la fracción positiva y escribe en grande si es **Paralela a X** o **Paralela a Y**. Antes de trazar las ramas de la hipérbola, construye el **rectángulo guía** usando los valores de $a$ y $b$, y traza las asíntotas cruzando sus esquinas. Finalmente, usa el **$LR/2$** para saber qué tan abierta debe estar la curva en la zona de los focos. Esto garantiza un dibujo geométricamente exacto.