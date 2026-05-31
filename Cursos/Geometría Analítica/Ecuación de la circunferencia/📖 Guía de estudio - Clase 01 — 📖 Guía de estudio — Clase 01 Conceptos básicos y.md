# 📖 Guía de estudio — Clase 01: Conceptos básicos y ecuación de la circunferencia

> [!info] 📌 Conceptos clave
> Para dominar el estudio de la circunferencia, es fundamental asimilar estos cuatro pilares extraídos del análisis técnico:
> 1. **Definición geométrica:** Una circunferencia es el conjunto de puntos en un plano que equidistan (están a la misma distancia) de un punto fijo llamado centro.
> 2. **Datos vitales:** Para definir y graficar cualquier circunferencia, solo necesitamos conocer dos elementos: el **Centro** (un punto de coordenadas $(h, k)$) y el **Radio** (una distancia $r$).
> 3. **Requisitos de la ecuación canónica:** La expresión $(x - h)^2 + (y - k)^2 = r^2$ es válida solo si los coeficientes de $x^2$ e $y^2$ son iguales a $1$ y el signo que separa los paréntesis es positivo.
> 4. **Vínculo con el diámetro:** El diámetro es el segmento que une dos puntos extremos pasando por el centro. Por ello, el centro es el **punto medio** del diámetro y el radio es exactamente la mitad de su longitud ($r = D/2$).

## 2. TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Circunferencia** | Puntos del plano cuya distancia a un centro es constante. |
| **Centro ($h, k$)** | El punto fijo en el plano cartesiano que actúa como eje. |
| **Radio ($r$)** | Distancia medida desde el centro hacia cualquier punto del borde. |
| **Relación Radio/Diámetro** | El radio es la mitad del diámetro ($r = \frac{D}{2}$); el centro es el punto medio. |
| **Ecuación Canónica** | $(x - h)^2 + (y - k)^2 = r^2$ |
| **Punto Medio (Centro)** | $C = \left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$ |

---

## 3. EJEMPLOS RESUELTOS ADICIONALES

```ad-example
title: Ejemplo A — Hallar la ecuación dado el Centro y Radio
**Enunciado:** Determinar la ecuación de la circunferencia con centro en $(2, 1)$ y radio $r = 3$.

**Paso 1: Sustitución en la fórmula**
Identificamos los valores del centro $(h, k)$ y el radio $r$:
*   $h = 2$
*   $k = 1$
*   $r = 3$

Sustituimos en $(x - h)^2 + (y - k)^2 = r^2$:
$(x - 2)^2 + (y - 1)^2 = 3^2$

**Paso 2: Resolución del radio al cuadrado**
Calculamos $3^2 = 9$:
$(x - 2)^2 + (y - 1)^2 = 9$

**Resultado final:** ✅ $(x - 2)^2 + (y - 1)^2 = 9$
```

```ad-example
title: Ejemplo B — Aplicación en diseño de infraestructura
**Enunciado:** Se debe delimitar una zona de seguridad circular para un cajero automático. El centro es el origen $(0, 0)$ y el radio debe ser de $4$ metros. Si el costo del cordón de seguridad es de $2.50\text{ USD}$ por metro de radio lineal, halle la ecuación y el costo total.

**Paso 1: Planteamiento de la ecuación**
Al estar el centro en $(0, 0)$, las coordenadas $h$ y $k$ son nulas ($x^2 + y^2 = r^2$):
$x^2 + y^2 = 4^2$
$x^2 + y^2 = 16$

**Paso 2: Cálculo del costo**
Multiplicamos el radio por el precio unitario:
$4\text{ metros} \times 2.50\text{ USD/m} = 10.00\text{ USD}$

**Resultado final:** ✅ Ecuación: $x^2 + y^2 = 16$ | Costo: $10.00\text{ USD}$
```

---

## 4. EJERCICIOS DE REPASO GRADUADOS

```ad-abstract
title: 🟢 Nivel Fácil
color: 0, 200, 0
1. Identifique el centro $(h, k)$ y el radio $r$ de la siguiente circunferencia: $(x - 3)^2 + (y + 2)^2 = 25$.
2. Escriba la ecuación canónica de una circunferencia cuyo centro es el origen $(0, 0)$ y su radio es $r = 7$.
3. Describa brevemente cómo graficaría manualmente una circunferencia de centro $(1, 1)$ y radio $2$, mencionando el uso del compás.
```

```ad-abstract
title: 🟡 Nivel Medio
color: 255, 200, 0
1. Obtenga la ecuación de la circunferencia con centro en $(-\frac{1}{2}, 4)$ y radio $r = 3$. ¡Cuidado con el signo de la fracción!
2. Si una circunferencia tiene la ecuación $(x - 5)^2 + (y - 2)^2 = 20$, determine el valor exacto del radio ($\sqrt{n}$) y su aproximación decimal.
3. Analice si las siguientes ecuaciones representan una circunferencia. Justifique su respuesta basándose en los coeficientes:
   - a) $4x^2 + 4y^2 = 16$
   - b) $2x^2 + 5y^2 = 20$
   - c) $x^2 + y^2 = 10$
```

```ad-abstract
title: 🔴 Nivel Avanzado (Aplicación con $USD)
color: 200, 0, 0
1. **Producción de monedas:** Una moneda conmemorativa tiene un diámetro cuyos extremos son los puntos $A(-3, -2)$ y $B(5, 0)$.
   - Calcule las coordenadas del centro usando la fórmula de punto medio.
   - Determine la medida del radio.
   - Escriba la ecuación canónica resultante.
   - Si cada unidad de radio lineal cuesta $1.25\text{ USD}$ en materiales, ¿cuál es el costo de producción? (Use $r \approx 4.12$ y exprese el resultado con dos decimales).

2. **Análisis técnico:** Determine si la ecuación $5x^2 + 3y^2 + 10x = 0$ es una circunferencia. Justifique su respuesta analizando específicamente los coeficientes de los términos cuadráticos $x^2$ e $y^2$.
```

---

> [!tip] 💡 Consejo de estudio
> El error más común es el manejo de los signos. Recuerda: **al pasar del punto del centro $(h, k)$ a la ecuación, los signos se invierten** debido al negativo de la fórmula $(x - h)$.
> - Si el centro tiene $h = \mathbf{-3}$, en la ecuación verás $(x \mathbf{+ 3})$.
> - Si la ecuación muestra $(y \mathbf{- 5})$, la coordenada $k$ del centro es $\mathbf{+5}$.
> ¡Verifica siempre este cambio antes de graficar!