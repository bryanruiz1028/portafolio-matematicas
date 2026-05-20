# 📖 Guía de estudio — Clase 06: Inecuaciones Racionales

> [!info] 📌 Conceptos clave
> Una inecuación racional es una desigualdad donde la variable $x$ se encuentra en el denominador. Para dominarlas, un experto debe considerar:
> 1. **Referencia a cero:** No se puede resolver sin que un lado de la desigualdad sea exactamente cero. Si hay términos en ambos lados, debemos trasponerlos.
> 2. **Puntos Críticos (PC):** Valores que anulan el numerador o el denominador. Dividen la recta numérica en sectores de prueba.
> 3. **Regla de Exclusión Absoluta:** Los PC del denominador **nunca** se incluyen en la solución (usamos paréntesis `(`), ya que la división por cero genera una indefinición o "error".
> 4. **Lógica de Signos:** Determinamos si la expresión total es positiva ($>0, \geq 0$) o negativa ($<0, \leq 0$) analizando la interacción de signos entre numerador y denominador.

> [!tip] ⚡ Truco Pedagógico: Lógica "Pro-Sign"
> Para ahorrar tiempo en el análisis de la recta numérica, observa el signo de la $x$:
> *   **Si $x$ es positiva** (ej. $x-5$): A la izquierda del PC es $(-)$ y a la derecha es $(+)$.
> *   **Si $x$ es negativa** (ej. $3-x$): El comportamiento se invierte; a la izquierda del PC es $(+)$ y a la derecha es $(-)$.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Inecuación Racional** | Estructura de división $\frac{P(x)}{Q(x)} \gtrless 0$, donde $Q(x)$ contiene la variable $x$. |
| **PC (Numerador)** | Se halla igualando el numerador a cero. Se incluye en la solución (corchete `[` ) solo si existe el signo "igual" ($\geq, \leq$). |
| **PC (Denominador)** | Se halla igualando el denominador a cero. **Siempre se excluye** (paréntesis `(` ) para evitar el error matemático de división por cero. |
| **Factor Común** | Se usa cuando todos los términos tienen $x$. Ejemplo: $x^2 - 2x = x(x-2)$. |
| **Factorización de Trinomios** | Para $x^2 + bx + c$, buscamos $(x+a)(x+b)$ donde $a \cdot b = c$ y $a + b = b$. |
| **Resta de Fracciones (Carita Feliz)** | Para casos avanzados: $\frac{a}{b} - \frac{c}{d} = \frac{(a \cdot d) - (b \cdot c)}{b \cdot d}$. |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Caso Básico (Análisis de Sectores)
**Problema**: Resuelva la inecuación $\frac{x+4}{x-3} > 0$.

1. **Identificación**: Al ser $>0$, buscamos los intervalos donde la expresión sea **positiva**.
2. **Puntos Críticos**:
   - Numerador: $x+4 = 0 \implies x = -4$
   - Denominador: $x-3 = 0 \implies x = 3$
3. **Gráfica y Análisis de Signos**: Ubicamos $-4$ y $3$. Probamos valores en los 3 sectores:
   - **Sector 1** $(-\infty, -4)$: Probamos $x=-5 \implies \frac{(-5)+4}{(-5)-3} = \frac{(-)}{(-)} = \mathbf{+}$
   - **Sector 2** $(-4, 3)$: Probamos $x=0 \implies \frac{(0)+4}{(0)-3} = \frac{(+)}{(-)} = \mathbf{-}$
   - **Sector 3** $(3, \infty)$: Probamos $x=4 \implies \frac{(4)+4}{(4)-3} = \frac{(+)}{(+)} = \mathbf{+}$
✅ **Resultado**: $(-\infty, -4) \cup (3, \infty)$.
```

```ad-example
title: Ejemplo B — Aplicación Real: Análisis de Inversión
**Problema**: El beneficio por unidad de un proyecto se modela como $\frac{2x-10}{x-1} \leq 0$, donde $x$ son unidades producidas (en cientos). Determine el rango de producción para que la rentabilidad sea negativa o cero (fase de inversión inicial).

1. **Análisis**: El símbolo $\leq 0$ nos indica que buscamos sectores **negativos**.
2. **Puntos Críticos**:
   - Numerador: $2x-10 = 0 \implies x=5$ (Punto incluido `[` por ser $\leq$).
   - Denominador: $x-1 = 0 \implies x=1$ (Punto excluido `(` por regla de denominador).
3. **Evaluación de Signos**:
   - Izquierda de 1: $\frac{(-)}{(-)} = \mathbf{+}$
   - Entre 1 y 5: $\frac{(-)}{(+)} = \mathbf{-}$ (¡Este es nuestro sector!)
   - Derecha de 5: $\frac{(+)}{(+)} = \mathbf{+}$
✅ **Interpretación**: La solución es el intervalo $(1, 5]$. Esto significa que produciendo entre **101 y 500 unidades**, la empresa se mantiene en fase de inversión. El valor $x=1$ se excluye porque anula el denominador.
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel Fácil
1. $\frac{x-1}{x-5} < 0$
2. $\frac{x+2}{x-4} \geq 0$
3. $\frac{x}{x+3} > 0$
```

```ad-abstract
title: 🟡 Nivel Medio (Factorización y Signos)
1. $\frac{3-x}{x+2} \leq 0$ (Aplica el truco "Pro-Sign" para la $x$ negativa en el numerador).
2. $\frac{x^2-x-12}{x^2-1} > 0$ (Factoriza el trinomio arriba y la diferencia de cuadrados abajo).
3. $\frac{x^2-2x}{x+5} \geq 0$ (Aplica Factor Común en el numerador).
```

```ad-abstract
title: 🔴 Nivel Avanzado (Problemas de Aplicación $USD)
1. **Costos de Proveedores**: El Proveedor A ofrece un costo de $\frac{2}{x+3}$ y el Proveedor B de $\frac{5}{2x-1}$. ¿Para qué rango de producción $x$ el costo del Proveedor A es menor o igual al del Proveedor B? 
   *Pista: Resuelva $\frac{2}{x+3} \leq \frac{5}{2x-1}$ usando la Carita Feliz.*
2. **Punto de Equilibrio**: Una fábrica determina que su margen de pérdida está dado por $\frac{x-10}{x}$. Si la gerencia exige que este margen sea $\geq 1$ para considerar viable la operación, halle el rango de unidades $x$.
3. **Fluctuación de Precios**: En un análisis de mercado, se comparan dos índices de inflación: $I_1 = \frac{4}{x-3}$ e $I_2 = \frac{1}{x+2}$. Determine cuándo el primer índice supera al segundo ($I_1 > I_2$).
```

> [!tip] 💡 Consejo de Oro del Especialista
> Antes de trazar tu solución final, **dibuja siempre una 'X' o un círculo abierto sobre el Punto Crítico del denominador** en tu recta numérica. No importa si la inecuación tiene una raya abajo ($\geq, \leq$), esa 'X' te recordará visualmente que ese número **jamás** puede llevar corchete.