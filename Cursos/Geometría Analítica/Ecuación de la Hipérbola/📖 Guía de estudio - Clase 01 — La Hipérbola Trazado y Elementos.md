# 📖 Guía de estudio — Clase 01: La Hipérbola: Elementos y Trazado

> [!info] 📌 Conceptos clave
> La hipérbola se define y reconoce mediante los siguientes fundamentos técnico-pedagógicos:
> - **Lugar geométrico:** Es el conjunto de puntos tales que el valor absoluto de la diferencia de sus distancias a dos puntos fijos (focos) es constante e igual a la distancia entre los vértices ($|d_1 - d_2| = 2a$).
> - **Identificación algebraica:** Para que una ecuación sea una hipérbola, debe tener ambas variables ($x$ e $y$) al cuadrado y sus coeficientes deben tener **signos opuestos**.
> - **La "Regla de la Fracción Positiva":** A diferencia de la elipse, $a^2$ siempre es el denominador de la fracción con signo positivo, independientemente de si es mayor o menor que $b^2$.
> - **Orientación:** El eje real será paralelo al eje de la variable que se encuentre en la fracción positiva.
> - **Traslación:** La presencia de términos $(x - h)$ y $(y - k)$ indica que el centro se ha desplazado del origen $(0,0)$ al punto $(h, k)$.

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Centro ($h, k$)** | Punto medio de la hipérbola. En la ecuación, se identifican $h$ y $k$ cambiando los signos de los números que acompañan a $x$ e $y$. |
| **Vértices (distancia $a$)** | Distancia desde el centro hasta cada vértice sobre el eje real. Se obtiene como $a = \sqrt{\text{denominador positivo}}$. |
| **Focos (distancia $c$)** | Distancia desde el centro a los focos. Se cumple que $c > a$, por lo que los focos siempre están "dentro" de las ramas. |
| **Eje Real ($2a$)** | Segmento que une ambos vértices. Es la distancia total sobre la que se abre la hipérbola. |
| **Eje Imaginario ($2b$)** | Distancia $b = \sqrt{\text{denominador negativo}}$. Define el ancho del rectángulo guía perpendicular al eje real. |
| **Distancia Focal ($2c$)** | Longitud total del segmento que une ambos focos. |
| **Relación Pitagórica** | $c^2 = a^2 + b^2$. Esencial para hallar la ubicación de los focos. |
| **Lado Recto ($LR$)** | $LR = \frac{2b^2}{a}$. Medida de la cuerda vertical/horizontal que pasa por los focos y toca la curva. |
| **Asíntotas** | Rectas imaginarias que pasan por las diagonales del rectángulo guía. La hipérbola se aproxima a ellas infinitamente sin tocarlas. |

## Ejemplos Resueltos

```ad-example
title: Ejemplo A: Análisis de una hipérbola horizontal con centro en (0,0)
**Ejercicio:** Analizar la ecuación $\frac{x^2}{16} - \frac{y^2}{9} = 1$.

1. **Orientación:** La variable $x$ está en la fracción positiva; la hipérbola es **horizontal**.
2. **Cálculo de parámetros:**
   - $a^2 = 16 \implies a = 4$.
   - $b^2 = 9 \implies b = 3$.
   - $c^2 = 16 + 9 = 25 \implies c = 5$.
3. **Centro:** Al no haber traslaciones en el numerador, el centro es $(0,0)$.
4. **Nota Pedagógica:** Observa que $c (5) > a (4)$. Esto confirma que los focos están situados a 5 unidades del centro, quedando protegidos por la curvatura de las ramas de la hipérbola.
```

```ad-example
title: Ejemplo B: Aplicación en Ingeniería Civil (USD)
**Contexto:** Se proyecta una torre de enfriamiento con perfil hiperbólico bajo la ecuación $\frac{y^2}{144} - \frac{x^2}{25} = 1$. El presupuesto para el revestimiento del **eje real** ($2a$) es de $150 USD por unidad lineal.

1. **Identificar parámetros:** El denominador positivo es $144$, por tanto $a^2 = 144 \implies a = 12$.
2. **Calcular Eje Real:** La distancia total del eje real es $2a = 2 \times 12 = 24$ unidades.
3. **Análisis de costo:** El costo se basa en la longitud total del eje donde se soporta la estructura principal.
4. **Cálculo final:** $24 \text{ unidades} \times 150 \text{ USD} = 3,600 \text{ USD}$.

**Resultado:** El costo de revestimiento del eje real de la estructura es de **3,600 USD**.
```

## Ejercicios de Repaso

```ad-abstract
title: Nivel Fácil (Verde)
Determina el centro $(h, k)$ y los valores de $a$ y $b$ en las siguientes ecuaciones:
1. $\frac{x^2}{100} - \frac{y^2}{64} = 1$
2. $\frac{y^2}{49} - \frac{x^2}{36} = 1$
3. $\frac{(x-2)^2}{81} - \frac{(y+5)^2}{16} = 1$
```

```ad-abstract
title: Nivel Medio (Amarillo)
Calcula la distancia focal ($c$) y la medida del lado recto ($LR$) para las siguientes hipérbolas:
1. $\frac{x^2}{16} - \frac{y^2}{9} = 1$
2. $\frac{y^2}{144} - \frac{x^2}{25} = 1$
3. $\frac{x^2}{9} - \frac{y^2}{16} = 1$
```

```ad-abstract
title: Nivel Avanzado (Rojo)
Un componente de precisión aeronáutica sigue la trayectoria $\frac{(x-4)^2}{9} - \frac{(y+3)^2}{16} = 1$.
1. Determina las coordenadas exactas del centro $(h, k)$.
2. Calcula la distancia $c$ (desde el centro al foco).
3. **Impacto Económico:** Si el costo de producción es de $500 USD por cada unidad de distancia del parámetro $a$ (semieje real) y $200 USD por cada unidad del parámetro $b$ (semieje imaginario):
   - ¿Cuál es el costo del parámetro $a$?
   - ¿Cuál es el costo del parámetro $b$?
   - ¿Cuál es el costo total de los parámetros básicos de la pieza en **USD**?
```

> [!tip] 💡 Consejo de estudio
> Para dominar el trazado, recuerda siempre dibujar primero el **rectángulo guía** usando $a$ y $b$. Las diagonales de este rectángulo son tus asíntotas. El error más común es confundirla con la elipse: recuerda que en la hipérbola el signo **negativo** es el que manda y define el eje imaginario, y que el valor de $c$ siempre será la hipotenusa de tu relación pitagórica ($c > a$).