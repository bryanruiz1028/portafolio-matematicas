# 📖 Guía de estudio — Clase 07: Función Exponencial

¡Hola! Qué gusto saludarte. Hoy vamos a explorar uno de los temas más fascinantes de las matemáticas: la **Función Exponencial**. Verás que es muy sencillo identificarla y graficarla si sigues estos pasos. ¡Empecemos!

> [!info] 📌 Conceptos clave
> 1. **Ubicación de la variable:** En este tipo de funciones, la variable $x$ siempre está "volando" en el **exponente**. Si la $x$ estuviera en la base, sería una función de otro tipo.
> 2. **Condiciones críticas de la base ($a$):** La base $a$ debe ser siempre un número **positivo** ($a > 0$) y **distinto de $1$** ($a \neq 1$). 
>    * *¿Por qué $a \neq 1$?* Porque si la base fuera $1$, obtendríamos $f(x) = 1^x = 1$, lo cual es simplemente una línea recta horizontal y no una curva exponencial.
> 3. **Comportamiento gráfico:** 
>    * Es **creciente** si la base es mayor que $1$ ($a > 1$).
>    * Es **decreciente** si la base está entre $0$ y $1$ ($0 < a < 1$).
> 4. **Análisis estándar:** Por defecto, estas funciones nunca tocan el eje $X$. Su dominio son todos los números reales ($\mathbb{R}$) y su rango son los reales positivos.

### Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Función Exponencial** | Tiene la forma general $f(x) = a^x$. |
| **Base ($a$)** | Es la constante que sostiene al exponente. Debe cumplir $a > 0$ y $a \neq 1$. **Nota:** Una base negativa entre paréntesis, como $(-3)^x$, no es una función; pero un negativo fuera, como $-3^x$, es una reflexión. |
| **Asíntota Horizontal** | Es la recta a la que la función **se acerca infinitamente pero nunca la toca**. Para la función base, es el eje $X$ ($y = 0$). |
| **Dominio** | Todos los valores posibles de entrada para $x$. En estas funciones, son todos los reales ($\mathbb{R}$). |
| **Rango** | Valores de salida ($y$). En la función base, son los reales positivos $(0, \infty)$. **Pro Tip:** El rango puede cambiar si la función se desplaza hacia arriba o hacia abajo. |

---

### Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A — Función Creciente
**Problema:** Graficar y analizar la función $f(x) = 2^x$.

**Proceso:**
1. **Identificación:** La base es $a = 2$. Como $2 > 1$, ¡atención!, ya sabemos que la gráfica será creciente (subirá de izquierda a derecha).
2. **Tabla de valores:** Vamos a calcular algunos puntos clave para nuestra gráfica:

| $x$ | $f(x) = 2^x$ | Punto $(x, y)$ |
| :--- | :--- | :--- |
| $-2$ | $2^{-2} = \frac{1}{2^2} = \frac{1}{4} = 0,25$ | $(-2, 0,25)$ |
| $0$ | $2^0 = 1$ | $(0, 1)$ |
| $2$ | $2^2 = 4$ | $(2, 4)$ |

3. **Conclusión:** La curva corta el eje $Y$ en $1$. Nota que al usar valores negativos de $x$, el resultado se hace muy pequeño ($0,25$), acercándose al eje $X$ pero sin tocarlo jamás.
```

```ad-example
title: Ejemplo B — Aplicación Real: Crecimiento de inversión ($USD)
**Escenario:** Imagina que inviertes $1 USD y tu dinero se duplica mágicamente cada año. Esto se representa como $f(x) = 1 \cdot 2^x$, donde $x$ es el tiempo en años.

**Cálculo de montos aplicando la lógica de potencias:**
- **Año $1$:** $f(1) = 1 \cdot 2^1 = 2$ USD.
- **Año $2$:** $f(2) = 1 \cdot 2^2 = 2 \cdot 2 = 4$ USD.
- **Año $3$:** $f(3) = 1 \cdot 2^3 = 2 \cdot 2 \cdot 2 = 8$ USD.

**Observación pedagógica:** El crecimiento es acelerado porque en cada paso multiplicas por la base. Como ves, el exponente indica cuántas veces multiplicamos la base por sí misma.
```

---

### Ejercicios de Repaso

```ad-abstract
title: 🟢 Fácil — Identificación
Identifica cuáles de las siguientes expresiones son realmente funciones exponenciales:
1. $y = 3^x$
2. $y = (-2)^x$
3. $y = x^2$
4. $f(x) = (\frac{1}{2})^x$

**Nota sobre la "Trampa de la Base":** Recuerda que si el signo negativo está dentro del paréntesis de la base, como en el caso 2, la expresión no se considera una función válida porque no se puede graficar de forma continua.
```

```ad-abstract
title: 🟡 Medio — Análisis de Comportamiento
Dadas las funciones $f(x) = 5^x$ y $g(x) = (0,5)^x$:
1. Determina cuál es creciente y cuál es decreciente comparando sus bases con el número $1$.
2. Indica cuál es el rango de ambas funciones si sabemos que no tienen desplazamientos verticales.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
Un plan de ahorro especial triplica tu monto inicial mensualmente, siguiendo la función $f(x) = 3^x$.
1. ¿Cuánto dinero ($USD) habrás acumulado al finalizar el mes $4$?
   * *Pista:* Debes calcular $3^4$, es decir, $3 \cdot 3 \cdot 3 \cdot 3$.
2. En esta situación práctica, ¿cuál sería el dominio lógico para el tiempo $x$?
   * *Ayuda:* Piensa si en la vida real podemos tener meses negativos ($x < 0$).
```

---

> [!tip] 💡 Consejo de estudio
> Para identificar una función exponencial al instante, busca siempre que la **"$x$" esté volando en el exponente**. Si la "$x$" está abajo en el suelo (como base), ¡es una función de otro tipo! Además, asegúrate siempre de que la base sea un número "bueno" (positivo y que no sea $1$).