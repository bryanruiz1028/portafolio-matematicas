# 📖 Guía de estudio — Clase 07: Ecuación de las Asíntotas de la Hipérbola

> [!info] 📌 Conceptos clave
> Para dominar las asíntotas, debemos entender que no son solo líneas "de adorno", sino las guías que definen el camino de nuestra hipérbola:
> 1. **Naturaleza de las asíntotas:** Son dos líneas rectas que se cruzan exactamente en el centro de la hipérbola. Actúan como límites: las ramas de la hipérbola se acercan a ellas infinitamente, pero nunca las tocan.
> 2. **El Centro $(h, k)$:** Es nuestro punto de anclaje. Para hallarlo, simplemente **cambiamos el signo al número que acompaña a $x$ y al que acompaña a $y$** dentro de los paréntesis.
> 3. **La Pendiente ($m$):** Representa el "avance vertical" sobre el "avance horizontal" (Rise/Run). En la hipérbola, esto es siempre la distancia en $y$ ($\Delta y$) dividida por la distancia en $x$ ($\Delta x$).
> 4. **Flexibilidad metodológica:** Podemos usar la **Fórmula Punto-Pendiente** (clásica y conceptual) o el método de **Igualación a cero** (un atajo algebraico). Este segundo método funciona porque, en el infinito, el valor "1" de la ecuación se vuelve insignificante frente a los valores crecientes de $x$ e $y$.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
|---------|----------------------|
| **Centro $(h, k)$** | Es el punto por donde pasan ambas rectas. Lo identificamos mirando los números junto a $x$ e $y$ y **cambiándoles el signo**. |
| **Distancia en $y$ ($\Delta y$)** | Es la raíz cuadrada del denominador que está debajo de la variable $y$: $\sqrt{\text{denominador de } y}$. |
| **Distancia en $x$ ($\Delta x$)** | Es la raíz cuadrada del denominador que está debajo de la variable $x$: $\sqrt{\text{denominador de } x}$. |
| **Pendiente ($m$)** | Se define como $m = \pm \frac{\Delta y}{\Delta x}$. Indica cuánto sube o baja la recta por cada unidad que avanza en $x$. |
| **Fórmula Punto-Pendiente** | Estructura principal: $y - k = \pm \frac{\Delta y}{\Delta x}(x - h)$. |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Centro en el origen $(0,0)$
**Ecuación:** $\frac{x^2}{9} - \frac{y^2}{4} = 1$

1. **Identificar elementos:** 
   - El centro es $(0,0)$ porque no hay números sumando a $x$ o $y$.
   - $\Delta y = \sqrt{4} = 2$.
   - $\Delta x = \sqrt{9} = 3$.
2. **Sustituir en la fórmula:** ¡No te asustes! Al ser el centro $(0,0)$, la fórmula se simplifica mucho: $y = \pm \frac{\Delta y}{\Delta x}x$.
   - $y = \pm \frac{2}{3}x$.
3. **Resultado:** 
   - Asíntota 1: $y = \frac{2}{3}x$ ✅
   - Asíntota 2: $y = -\frac{2}{3}x$ ✅
```

```ad-example
title: Ejemplo B — Aplicación económica en Proyectos $USD
**Contexto:** Un analista de costos modela el límite de gastos mediante la hipérbola $\frac{(x-5)^2}{25} - \frac{(y+2)^2}{16} = 1$, donde $x$ es la inversión e $y$ el gasto (en miles de $USD).

1. **Hallar el centro:** Cambiamos los signos. $h=5, k=-2$. Centro: $(5, -2)$.
2. **Calcular distancias:** $\Delta y = \sqrt{16} = 4$; $\Delta x = \sqrt{25} = 5$.
3. **Aplicar fórmula y despejar:** La estructura es $y + 2 = \pm \frac{4}{5}(x - 5)$.
   - **Camino (+) Pendiente Positiva:**
     $y + 2 = \frac{4}{5}(x - 5) \Rightarrow y + 2 = \frac{4}{5}x - 4 \Rightarrow y = \frac{4}{5}x - 6$.
   - **Camino (-) Pendiente Negativa:**
     $y + 2 = -\frac{4}{5}(x - 5) \Rightarrow y + 2 = -\frac{4}{5}x + 4 \Rightarrow y = -\frac{4}{5}x + 2$.
4. **Resultado y análisis:** Las fronteras son $y = 0.8x - 6$ e $y = -0.8x + 2$. 
**Interpretación:** A medida que la inversión $x$ crece, el gasto $y$ nunca superará ni bajará de estas líneas límite; son el "techo" y "piso" presupuestario del proyecto. ✅
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil — Centro en el origen
Halla las ecuaciones de las asíntotas para las siguientes hipérbolas:
1. $\frac{x^2}{100} - \frac{y^2}{36} = 1$
2. $\frac{x^2}{25} - \frac{y^2}{4} = 1$
3. $\frac{y^2}{49} - \frac{x^2}{64} = 1$
```

```ad-abstract
title: 🟡 Medio — Centro desplazado y raíces inexactas
Encuentra las ecuaciones **despejando totalmente la variable $y$**:
1. $\frac{(x-3)^2}{9} - \frac{(y+1)^2}{16} = 1$
2. **Raíz no exacta:** $\frac{(x+2)^2}{30} - \frac{(y-4)^2}{25} = 1$ *(Sugerencia: $\sqrt{30} \approx 5.47$. Resultado: $y \approx \pm 0.91(x+2) + 4$)*.
3. $\frac{(y-2)^2}{49} - \frac{(x+1)^2}{30} = 1$
```

```ad-abstract
title: 🔴 Avanzado — Análisis de Mercado
Un modelo de equilibrio de precios sigue la ecuación $\frac{(x-10)^2}{16} - \frac{(y-5)^2}{9} = 1$.
**Despeja la variable $y$** para encontrar las dos funciones lineales que representan el comportamiento del precio $y$ ($USD) cuando el volumen de transacciones $x$ es extremadamente alto.
```

> [!tip] 💡 Consejo del Profe Alex
> Si usas el **Método de Igualación a cero**, recuerda que al sacar la raíz cuadrada para eliminar los cuadrados, **siempre surge el signo $\pm$** porque toda raíz cuadrada tiene dos soluciones posibles (una positiva y una negativa). Para verificar rápido: la pendiente siempre será $\frac{\sqrt{\text{lo que esté bajo } y}}{\sqrt{\text{lo que esté bajo } x}}$, sin importar el orden de la ecuación. ¡No te compliques memorizando $a$ y $b$, solo fíjate en las variables!