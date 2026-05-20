# Clase 04 — Ecuación Cuadrática: Fórmula General y Completación de Cuadrados

#algebra #ecuacioncuadratica

[[Clase 03]] | [[Indice_Curso]] | [[Clase 05]]

> [!info] 🧭 Navegación
> Las ecuaciones cuadráticas son herramientas esenciales para predecir el futuro de un movimiento o la rentabilidad de un negocio.
> - 💵 **USD:** Permiten hallar el "punto de equilibrio", ese momento exacto donde tu negocio deja de perder dinero y tus ganancias cubren todos tus gastos.
> - 🏗️ **Práctica:** Se utilizan en arquitectura para calcular áreas exactas y diseñar estructuras curvas estables.
> - 📊 **Cotidiana:** Modelan la trayectoria de una pelota o un proyectil, determinando su altura máxima y el momento en que tocará el suelo.

> [!note] La "Llave Maestra"
> Para un estudiante de secundaria, la Fórmula General es como una **llave maestra**. No importa qué tan complejo sea el "candado" (la ecuación), esta fórmula lo abrirá siempre. Tu única misión es identificar tres números mágicos: **a**, **b** y **c**, y dejar que la fórmula haga el trabajo por ti.

> [!warning] La Trampa del Signo de "b"
> El error más peligroso ocurre al inicio: $-b$. Si el valor de $b$ en tu ecuación ya es negativo (ej. $b = -5$), la fórmula dice que debes poner el opuesto. ¡Menos por menos da más! En ese caso, comenzarías con $+5$.

> [!tip] Técnica de "Los Paréntesis Vacíos"
> Para no perderte entre tantos signos, Profe Alex recomienda escribir la fórmula dejando "huecos" con paréntesis antes de poner los números:
> $x = \frac{-(\quad) \pm \sqrt{(\quad)^2 - 4(\quad)(\quad)}}{2(\quad)}$
> Luego, simplemente "rellena" cada paréntesis con su valor y su signo original. Esto evita confusiones fatales con los signos negativos.

### Procedimiento Estandarizado (Método Profe Alex)

```text
PASO 1: Simplificar operaciones (resolver paréntesis, binomios o eliminar denominadores).
PASO 2: Ordenar e igualar a cero siguiendo el formato estándar: ax² + bx + c = 0.
PASO 3: Identificar coeficientes (a, b, c) respetando estrictamente sus signos.
PASO 4: Calcular el Discriminante (D = b² - 4ac). Si es negativo, no hay solución real.
PASO 5: Sustituir en la fórmula general y resolver las dos posibles raíces (x1, x2).
```

### Bloque de Ejemplos Resueltos

> [!abstract] Ejemplo 1: Caso Básico
> **Ecuación:** $3x^2 + 5x + 1 = 0$
> 1. **Identificación:** $a = 3, b = 5, c = 1$.
> 2. **Sustitución:** $x = \frac{-5 \pm \sqrt{5^2 - 4(3)(1)}}{2(3)}$
> 3. **Resultado:** $x = \frac{-5 \pm \sqrt{25 - 12}}{6} = \frac{-5 \pm \sqrt{13}}{6}$.
> *Valores aproximados:* $x_1 \approx -0.232$, $x_2 \approx -1.434$.

> [!abstract] Ejemplo 2: Aplicando Paréntesis en Negativos
> **Ecuación:** $2x^2 - x - 5 = 0$
> 1. **Identificación:** $a = 2, b = -1, c = -5$. (Si la $x$ no tiene número, su coeficiente es 1).
> 2. **Sustitución con "Huecos":** $x = \frac{-(-1) \pm \sqrt{(-1)^2 - 4(2)(-5)}}{2(2)}$
> 3. **Resultado:** $x = \frac{1 \pm \sqrt{1 + 40}}{4} = \frac{1 \pm \sqrt{41}}{4}$.
> *Valores aproximados:* $x_1 \approx 1.85$, $x_2 \approx -1.35$.

> [!abstract] Ejemplo 3: El Peligro del Binomio y el Signo Menos
> **Ecuación:** $(2x-3)^2 - (x+5)^2 = -23$
> 1. **Expansión:** $(4x^2 - 12x + 9) - (x^2 + 10x + 25) = -23$.
> 2. **La Trampa del Signo:** El menos fuera del segundo paréntesis cambia **todo** adentro:
>    $4x^2 - 12x + 9 - x^2 - 10x - 25 = -23$.
> 3. **Simplificación:** $3x^2 - 22x - 16 = -23 \rightarrow 3x^2 - 22x + 7 = 0$.
> 4. **Fórmula:** Con $a=3, b=-22, c=7$, obtenemos $x_1 = 7$ y $x_2 = 1/3$.

> [!abstract] Ejemplo 4: El Truco del MCM en Presupuestos
> **Situación:** Una variable de costo fraccionaria $\frac{1}{15}x^2 - \frac{1}{5}x - \frac{2}{3} = 0$.
> 1. **MCM (15):** Multiplicamos cada término para eliminar los denominadores.
>    - $(15 \div 15) \cdot 1 = 1x^2$
>    - $(15 \div 5) \cdot 1 = 3x$
>    - $(15 \div 3) \cdot 2 = 10$
> 2. **Nueva Ecuación:** $x^2 - 3x - 10 = 0$.
> 3. **Resolución:** $a=1, b=-3, c=-10$. El discriminante es $9 - 4(1)(-10) = 49$.
> 4. **Resultado:** $x_1 = 5$ USD, $x_2 = -2$ (valor descartado en finanzas).

### Ejercicios para el Estudiante

**Nivel Verde (Fácil)**
1. $x^2 + 3x + 2 = 0$
2. $x^2 - 5x + 6 = 0$
3. $x^2 + 4x - 3 = 0$
4. $3x^2 + 4x - 3 = 0$

**Nivel Amarillo (Medio - Trasposición)**
1. $x^2 + 3x = -2x^2 + 5$
2. $3x^2 + 5x + 2 = 8x^2 + 8$
3. $x^2 + 4x = 3$
4. $2x^2 + 7x = 6$

**Nivel Rojo (Avanzado - Aplicación Real)**
1. $(2x+4)(2x-3) = (x+4)(x-1)$ (Ecuación de costos de producción).
2. $\frac{1}{5}x^2 - \frac{1}{2}x - \frac{3}{10} = 0$ (Presupuesto con fracciones).
3. $(3x+2)^2 - (x+5) = 16$ (Optimización de áreas cuadradas).
4. $2x^2 - 5x - 3 = 0$ (Cálculo de punto de equilibrio).

> [!success] Respuestas para el Docente
> - **Verde:** 1) $x = \{-1, -2\}$; 2) $x = \{3, 2\}$; 3) $x \approx \{0.64, -4.64\}$; 4) $x \approx \{0.53, -1.86\}$.
> - **Amarillo:** 1) $3x^2 + 3x - 5 = 0 \rightarrow x \approx \{0.82, -1.82\}$; 2) $5x^2 - 5x + 6 = 0$ (Sin solución real); 3) $x \approx \{0.64, -4.64\}$; 4) $x \approx \{0.71, -4.21\}$.
> - **Rojo:** 1) $3x^2 - x - 8 = 0 \rightarrow x \approx \{1.81, -1.47\}$; 2) $x = \{3, -0.5\}$; 3) $9x^2 + 11x - 17 = 0 \rightarrow x \approx \{0.88, -2.11\}$; 4) $x = \{3, -0.5\}$.

### Autoevaluación

1. **Conceptual:** Para que un trinomio sea un Trinomio Cuadrado Perfecto (TCP), ¿qué deben tener en común el primer y tercer término?
   - A) Deben ser números primos.
   - B) Deben tener raíz cuadrada exacta y el mismo signo.
   - C) Deben sumar lo mismo que el término central.

2. **Procedimental:** Si identificamos $a=2, b=-1, c=-5$, ¿cuál es el valor del discriminante ($b^2 - 4ac$)?
   - A) 39
   - B) -39
   - C) 41

3. **Aplicación:** Al eliminar denominadores en $\frac{1}{5}x^2 - \frac{1}{2}x - \frac{3}{10} = 0$ usando el MCM (10), ¿qué ecuación obtenemos?
   - A) $2x^2 - 5x - 3 = 0$
   - B) $x^2 - x - 3 = 0$
   - C) $5x^2 - 2x - 10 = 0$

**Notas para el próximo tema:** En la siguiente sesión aprenderemos a "fabricar nuestro propio candado" mediante la **Completación de Cuadrados**. Si el término $b$ es una fracción, utilizaremos la **"Ley del Sándwich"** (extremos y medios) para dividirlo entre 2 antes de elevarlo al cuadrado:
$$\frac{\frac{b}{1}}{\frac{2}{1}} \rightarrow \text{multiplicar extremos y medios}.$$

[[Clase 03]] | [[Indice_Curso]] | [[Clase 05]]