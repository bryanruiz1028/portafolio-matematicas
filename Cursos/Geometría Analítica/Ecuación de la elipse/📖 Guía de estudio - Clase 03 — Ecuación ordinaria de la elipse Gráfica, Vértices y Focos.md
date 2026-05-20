# 📖 Guía de estudio — Clase 03: Ecuación estándar de la elipse a partir de su gráfica

> [!info] 📌 Conceptos clave
> - **El centro $(h, k)$**: Es el punto medio de la elipse. Se localiza exactamente a la mitad de la distancia entre los dos focos o entre los dos vértices del eje mayor.
> - **Orientación del eje mayor**: Determina la posición de $a^2$. Si el eje mayor es horizontal (paralelo al eje $x$), $a^2$ divide al término con $x$. Si es vertical (paralelo al eje $y$), $a^2$ divide al término con $y$.
> - **Semiejes ($a$ y $b$)**: El valor $a$ es la distancia del centro al vértice más lejano. El valor $b$ es la distancia al vértice más cercano.
> - **Relación pitagórica**: Usamos $a^2 = b^2 + c^2$ para hallar valores faltantes, donde $c$ es la distancia del centro al foco.
> - **⚠️ Advertencia de signos**: Al pasar las coordenadas del centro $(h, k)$ a la ecuación, sus signos **siempre se invierten**. Si $h = 2$, en la fórmula verás $(x - 2)$; si $h = -2$, verás $(x + 2)$.

---

# Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Centro $(h, k)$** | Punto central de la elipse donde se cruzan los ejes. |
| **Semieje mayor ($a$)** | Distancia más larga desde el centro hasta el borde. |
| **Semieje menor ($b$)** | Distancia más corta desde el centro hasta el borde. |
| **Ecuación (Eje horizontal)** | $\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1$ |
| **Ecuación (Eje vertical)** | $\frac{(x - h)^2}{b^2} + \frac{(y - k)^2}{a^2} = 1$ |

---

# Ejemplos Resueltos Adicionales

````ad-example
title: Ejemplo A — Elipse con eje horizontal
**Contexto:** Identificamos una elipse donde los focos y vértices están alineados horizontalmente.

**Paso 1: Identificar el centro $(h, k)$**
En la gráfica, el punto medio entre los vértices se ubica en $(2, 1)$. Por lo tanto, $h = 2$ y $k = 1$.

**Paso 2: Calcular valores de $a$ y $b$**
*   Contamos desde el centro $(2, 1)$ al vértice y hallamos $a = 3$ (entonces $a^2 = 9$).
*   Contamos desde el centro al foco y hallamos $c = 2$ (entonces $c^2 = 4$).
*   **Cálculo de $b^2$:** Usamos la relación $a^2 = b^2 + c^2$:
    $3^2 = b^2 + 2^2 \Rightarrow 9 = b^2 + 4 \Rightarrow 9 - 4 = b^2 \Rightarrow b^2 = 5$.

**Paso 3: Sustitución final**
Al ser horizontal, $a^2$ va bajo $x$:
$\frac{(x - 2)^2}{9} + \frac{(y - 1)^2}{5} = 1$
````

````ad-example
title: Ejemplo B — Diseño de una plaza elíptica ($USD)
**Contexto:** Se diseña una plaza con forma de elipse vertical. El costo de diseño es de $10$ $USD$ por cada unidad del valor del semieje mayor al cuadrado ($a^2$).

**Paso 1: Datos de la gráfica**
Centro en $(-2, 2)$, por lo que $h = -2$ y $k = 2$. Observamos que $a = 3$ (vertical) y $b^2 = 5$.

**Paso 2: Cambio de signos y sustitución**
*   Para $h = -2$: $(x - (-2))^2$ se convierte en $(x + 2)^2$.
*   Para $k = 2$: $(y - 2)^2$ se mantiene con el signo de la fórmula.
*   Como es vertical, $a^2 = 3^2 = 9$ va debajo de $y$:
    $\frac{(x + 2)^2}{5} + \frac{(y - 2)^2}{9} = 1$

**Paso 3: Cálculo del Costo de Diseño**
Si el costo es $\$10$ por unidad de $a^2$:
$Costo = 10 \times 9 = 90$ $USD$.
````

---

# Ejercicios de Repaso

````ad-abstract
title: 🟢 Fácil
Halla la ecuación de una elipse con centro en el origen $(0, 0)$. Su eje mayor es horizontal con $a = 2$ y su semieje menor es $b = 1$.
*(Nota: Recuerda que si el centro es $(0, 0)$, los términos se simplifican a $x^2$ y $y^2$)*.
````

````ad-abstract
title: 🟡 Medio
Determina la ecuación de la elipse con centro en $(3, -2)$. La gráfica muestra un semieje mayor horizontal $a = 4$ y una distancia focal $c = 3$.
**Pista:** Aísla $b^2$ usando la fórmula $b^2 = a^2 - c^2$ antes de sustituir en la ecuación estándar.
````

````ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
Analiza una elipse vertical con centro en $(-3, 0)$, donde $a = 5$ y $b = 3$.
1. **Ecuación:** Escribe la ecuación canónica. *Dato útil:* Como $k = 0$, el término $(y - 0)^2$ se escribe simplemente como $y^2$.
2. **Inversión:** Si cada unidad de los denominadores ($a^2$ y $b^2$) representa una inversión de $1$ $USD$, ¿cuál es el valor total de la inversión sumando ambos denominadores?
````

---

> [!tip] 💡 Consejo de estudio
> Para no confundir $a$ y $b$, utiliza la técnica de **"contar cuadritos"**. Desde el centro, cuenta hacia los lados y luego hacia arriba o abajo hasta tocar el borde de la elipse. **El número más grande siempre será $a$**. No olvides que en la ecuación siempre debes elevar esos valores al cuadrado ($a^2$ y $b^2$).