# 📖 Guía de estudio — Clase 06: Gráfica de la Hipérbola dada su Ecuación General

> [!info] 📌 Conceptos clave
> 1.  **Ecuación General:** Se presenta como $Ax^2 + By^2 + Dx + Ey + F = 0$. En este estado, los elementos geométricos están "ocultos", por lo que es imperativo transformarla a la forma canónica.
> 2.  **Conversión a Canónica:** Proceso algebraico basado en completar el trinomio cuadrado perfecto (TCP) para las variables $x$ y $y$.
> 3.  **Identificación de Elementos:** A partir de la forma canónica, extraemos el centro $(h, k)$, las distancias $a$ (semieje real) y $b$ (semieje imaginario).
> 4.  **Orientación y Eje Real:** La orientación está determinada por la **variable positiva** en la ecuación canónica. Esta variable define el **Eje Real (o Transverso)**. Si la fracción positiva contiene a $x$, la hipérbola es horizontal; si contiene a $y$, es vertical.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Centro $(h, k)$** | Punto de equilibrio de la curva. $h$ se asocia a $x$, $k$ a $y$ (siempre con signo opuesto al de la ecuación). |
| **Semieje Real ($a$)** | Distancia del centro al vértice. Se obtiene de $\sqrt{a^2}$. **Nota:** $a^2$ siempre es el denominador de la fracción positiva. |
| **Semieje Imaginario ($b$)** | Distancia del centro a los extremos del rectángulo guía. Se obtiene de $\sqrt{b^2}$ (denominador de la fracción negativa). |
| **Distancia Focal ($c$)** | Distancia del centro a los focos. Se rige por la relación pitagórica: $c = \sqrt{a^2 + b^2}$. |
| **Lado Recto ($LR$)** | Ancho de la curva en los focos. Fórmula: $LR = \frac{2b^2}{a}$. |
| **Asíntotas (Horizontal)** | Rectas guía cuando el eje real es horizontal: $y - k = \pm \frac{b}{a}(x - h)$. |
| **Asíntotas (Vertical)** | Rectas guía cuando el eje real es vertical: $y - k = \pm \frac{a}{b}(x - h)$. |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Hipérbola con eje real vertical
**Enunciado:** Graficar la hipérbola dada por la ecuación $-12x^2 + 8y^2 - 32y - 64 = 0$.

**Paso 1: Organizar y completar trinomios.**
- Agrupamos términos de la misma variable y movemos el término independiente: $8(y^2 - 4y) - 12x^2 = 64$.
- Completamos el TCP para $y$: Tomamos la mitad de 4 ($2$) y elevamos al cuadrado ($4$).
- $8(y^2 - 4y + 4) - 12x^2 = 64 + (8 \times 4)$. 
- *Nota de diseño:* Sumamos 32 al lado derecho porque el 4 está multiplicado por el factor común 8.
- Factorizamos: $8(y - 2)^2 - 12x^2 = 96$.

**Paso 2: Obtener la forma canónica.**
- Dividimos toda la expresión entre 96 para igualar a 1: $\frac{8(y - 2)^2}{96} - \frac{12x^2}{96} = 1$.
- **Simplificación:** Para la fracción de $y$, dividimos numerador y denominador entre 8 ($96 \div 8 = 12$). Para $x$, dividimos entre 12 ($96 \div 12 = 8$).
- Ecuación final: $\frac{(y - 2)^2}{12} - \frac{x^2}{8} = 1$.

**Paso 3: Extraer elementos.**
- **Centro:** $(0, 2)$.
- **$a = \sqrt{12} = 2\sqrt{3} \approx 3.46$.**
- **$b = \sqrt{8} = 2\sqrt{2} \approx 2.82$.**
- **$c = \sqrt{12 + 8} = \sqrt{20} = 2\sqrt{5} \approx 4.47$.**

✅ **Resultado:** Dado que $y$ es el término positivo, el eje real es vertical. La hipérbola abre hacia arriba y abajo desde $(0, 2)$.
```

```ad-example
title: Ejemplo B — Aplicación de modelado de costos (USD)
**Enunciado:** Una zona de costos logísticos se define por $-5x^2 - 10x + y^2 + 6y + 9 = 0$. Encuentra el centro de dicha zona.

**Pasos:**
1.  **Agrupar:** $-5(x^2 + 2x) + (y^2 + 6y) = -9$.
2.  **Completar TCP:**
    - Para $x$: $-5(x^2 + 2x + 1)$. Restamos $5$ al otro lado ($-5 \times 1$).
    - Para $y$: $(y^2 + 6y + 9)$. Sumamos $9$ al otro lado.
    - $-5(x + 1)^2 + (y + 3)^2 = -9 - 5 + 9 \rightarrow -5(x + 1)^2 + (y + 3)^2 = -5$.
3.  **Forma canónica:** Dividimos entre $-5$: $\frac{-5(x + 1)^2}{-5} + \frac{(y + 3)^2}{-5} = \frac{-5}{-5}$.
    - $(x + 1)^2 - \frac{(y + 3)^2}{5} = 1$.
4.  **Identificar Centro:** Al cambiar signos de los valores junto a $x$ y $y$, obtenemos $h = -1$, $k = -3$.

✅ **Resultado:** El centro de costos se ubica en $(-1, -3)$. Al ser $x$ el término positivo, la hipérbola tiene orientación horizontal ($a = 1$).
```

> [!check] Checkpoint de aprendizaje
> ¿Sabías que en la hipérbola $a^2$ no es necesariamente el número mayor? A diferencia de la elipse, $a^2$ es simplemente el denominador de la variable que no tiene el signo menos delante. ¡Verifica siempre los signos antes de asignar $a$ y $b$!

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil — Práctica de Video 3
Dada la ecuación general $12x^2 - 9y^2 - 18y - 117 = 0$:
1. Transfórmala a su forma canónica (Pista: el término independiente pasará a ser $108$ tras completar el cuadrado).
2. Identifica las coordenadas del centro $(h, k)$.
3. Determina si el eje real es horizontal o vertical basándote en la variable positiva.
```

```ad-abstract
title: 🟡 Medio — Práctica de Video 4
Dada la ecuación $x^2 + 6x - 4y^2 + 8y + 1 = 0$:
1. Determina las coordenadas del **centro** completando los cuadrados.
2. Encuentra los valores exactos de $a, b$ y $c$ (exprésalos como radicales simplificados si es necesario).
3. Calcula la longitud del Lado Recto ($LR$).
4. A partir del centro, determina las coordenadas de los dos vértices.
```

```ad-abstract
title: 🔴 Avanzado — Análisis de Satélite
La trayectoria de un satélite sigue la curva $-12x^2 + 8y^2 - 32y - 64 = 0$ (del Ejemplo A).
1. Calcula la coordenada exacta del **foco superior**.
2. Determina la distancia total entre las estaciones base situadas en los vértices (Distancia $2a$).
3. Escribe las ecuaciones de las dos asíntotas que rigen la trayectoria del satélite.
4. Describe cómo dibujarías el rectángulo guía basándote en los valores de $a$ y $b$.
```

> [!tip] 💡 Consejo del Profesor
> El error más común de mis alumnos es olvidar que el número sumado para completar el trinomio debe multiplicarse por el factor común antes de agregarlo al otro lado de la igualdad. Si tienes un $-5$ fuera del paréntesis y agregas un $1$ dentro, debes "restar 5" al otro lado. ¡Presta mucha atención a los signos!