# 📖 Guía de estudio — Clase 09: Ecuación de la recta: Punto y Perpendicularidad

> [!info] 📌 Conceptos clave
> - **Validar la relación de perpendicularidad:** Dos rectas son perpendiculares si, al intersectarse, forman un ángulo de 90°. Matemáticamente, esto ocurre cuando el producto de sus pendientes es igual a -1 ($m_1 \cdot m_2 = -1$).
> - **Transformar mediante el método "Opuesta y Recíproca":** Para hallar la pendiente perpendicular ($m_2$) de forma rápida, se invierte la fracción de la pendiente original ($m_1$) y se le cambia el signo. 
> - **Utilizar el modelo Punto-Pendiente:** Cuando conocemos un punto $(x_1, y_1)$ y la pendiente $m$, la ecuación $y - y_1 = m(x - x_1)$ es el puente más eficiente para construir la nueva recta.
> - **Identificar la pendiente según el formato:** 
> 	- En la **forma explícita** ($y = mx + b$), el valor de $m$ es el coeficiente que acompaña a $x$. 
> 	- En la **forma general** ($Ax + By + C = 0$), la pendiente se extrae mediante la fórmula $m = -A/B$.

---

## 📏 Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Rectas Perpendiculares** | Rectas que se cruzan formando un ángulo recto (90°). |
| **Condición de Pendientes** | $m_1 \cdot m_2 = -1$ |
| **Ecuación Punto-Pendiente** | $y - y_1 = m(x - x_1)$ |
| **Pendiente (Forma General)** | $m = -\frac{A}{B}$ (extraída de $Ax + By + C = 0$) |
| **Forma Explícita** | $y = mx + b$ |

---

## 📝 Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A — Caso básico de perpendicularidad
**Enunciado:** Hallar la ecuación de la recta perpendicular a $y = 2x + 3$ que pasa por el punto $(-4, 2)$.

**Paso 1: Identificar la pendiente original ($m_1$).**
En $y = 2x + 3$, la pendiente $m_1 = 2$ (o $\frac{2}{1}$). Como es positiva, visualmente la recta es ascendente; nuestra perpendicular deberá ser descendente (negativa).

**Paso 2: Hallar la pendiente perpendicular ($m_2$).**
Aplicamos "opuesta y recíproca": Invertimos $\frac{2}{1} \rightarrow \frac{1}{2}$ y cambiamos signo (+) $\rightarrow$ (-).
$m_2 = -\frac{1}{2}$.

**Paso 3: Aplicar la fórmula punto-pendiente.**
Usamos el punto $(-4, 2)$, donde $x_1 = -4$ y $y_1 = 2$:
$y - 2 = -\frac{1}{2}(x - (-4))$
$y - 2 = -\frac{1}{2}(x + 4)$

**Paso 4: Despejar a la forma explícita.**
$y - 2 = -\frac{1}{2}x - 2$
$y = -\frac{1}{2}x - 2 + 2$
$y = -\frac{1}{2}x$

**Paso 5: Comprobación (Verificación del punto).**
Sustituimos el punto $(-4, 2)$ en nuestra respuesta:
$2 = -\frac{1}{2}(-4) \rightarrow 2 = \frac{4}{2} \rightarrow 2 = 2$.
¡El resultado es correcto!
```

```ad-example
title: Ejemplo B — Aplicación en infraestructura y costos ($USD)
**Enunciado:** Una constructora debe instalar un cableado perpendicular a una vía cuya trayectoria es $y = -\frac{2}{3}x + 4$. El cableado debe pasar por el punto $(0, 0)$. Si cada unidad del plano equivale a 1 metro y el costo de instalación es de $15 USD por metro, determine la ecuación y el costo de un tramo de 8 metros.

**Paso 1: Pendiente perpendicular.**
$m_1 = -\frac{2}{3} \rightarrow$ Opuesta y recíproca: $m_2 = \frac{3}{2}$.

**Paso 2: Construir la ecuación.**
Como pasa por el origen $(0, 0)$, el valor de $b$ es 0.
$y - 0 = \frac{3}{2}(x - 0) \implies y = \frac{3}{2}x$.

**Paso 3: Análisis financiero.**
Longitud requerida: 8 metros.
Costo unitario: $15 USD/m.
Costo total = $8 \times 15 = 120 USD$.
```

---

## ✍️ Ejercicios de Repaso

```ad-abstract
title: Nivel Verde (Fácil)
1. Si una recta tiene una pendiente $m = 4$, determina la pendiente $m_\perp$ de cualquier recta perpendicular a ella.
2. Hallar la pendiente perpendicular a la recta $y = -\frac{3}{5}x + 8$.
3. Escribe la ecuación explícita de la recta perpendicular a $y = \frac{1}{2}x - 5$ que pasa por el punto $(0, 10)$.
```

```ad-abstract
title: Nivel Amarillo (Medio)
*Tip: Identifica primero los valores de $A$ y $B$ para usar la fórmula $m = -A/B$.*

1. Dada la recta $5x - 2y + 4 = 0$, identifica $A$ y $B$, halla su pendiente $m_1$ y luego determina la $m_2$ perpendicular.
2. Halla la ecuación de la recta perpendicular a $4x + 2y - 1 = 0$ que pasa por el punto $(3, -2)$. Identifica $A$ y $B$ antes de operar.
3. Determina la ecuación perpendicular a $x - 3y + 6 = 0$ que pase por el punto $(1, 1)$. **Entrega el resultado final en Forma General ($Ax + By + C = 0$).**
```

```ad-abstract
title: Nivel Rojo (Avanzado — Aplicación $USD)
1. Un acueducto sigue la ruta $y = -3x + 10$. Se debe conectar una tubería perpendicular en el punto $(6, 2)$. Halla la ecuación de la tubería. Si el costo del material es de $25 USD por metro y el tramo mide 12 metros, ¿cuál es el presupuesto total?
2. Se diseña una vía perpendicular a la recta $2x + 5y - 7 = 0$. La vía cruza por el punto $(0, 4)$. Una empresa de consultoría cobra una tarifa fija de $500 USD más un bono de $50 USD por cada unidad del valor de la pendiente $m$ resultante. ¿Cuál es el costo total de la consultoría?
3. Una cerca de seguridad debe ser perpendicular a la línea $3x + 9y - 2 = 0$ y pasar por el punto $(2, 4)$. 
   - a) Halla la ecuación en **Forma General**.
   - b) Si el costo de mantenimiento es de $10 USD por cada unidad del intercepto con el eje $y$ (punto $b$), calcula dicho costo basado en la forma explícita de tu resultado.
```

---

## 💡 Consejo de estudio
> [!tip] 💡 El truco de la inversión rápida
> No te compliques siempre despejando la fórmula $m_1 \cdot m_2 = -1$. Usa el truco mental: **"Voltea y cambia el signo"**. 
> - Si tienes un entero como $4$, piensa en $\frac{4}{1}$ y cámbialo a $-\frac{1}{4}$.
> - Si tienes una fracción como $\frac{2}{3}$, cámbiala a $-\frac{3}{2}$.
> - Si tienes $-\frac{5}{7}$, cámbiala a $\frac{7}{5}$.
> ¡Este pequeño paso te ahorrará minutos valiosos en tus exámenes!