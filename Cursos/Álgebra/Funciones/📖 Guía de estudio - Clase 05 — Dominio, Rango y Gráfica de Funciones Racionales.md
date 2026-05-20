# 📖 Guía de estudio — Clase 05: Dominio, rango y gráfica de funciones racionales

> [!info] 📌 Conceptos clave
> ¡Hola, equipo! Antes de empezar, recuerda que las funciones racionales no son monstruos, ¡son solo divisiones con una $x$ en el denominador! Aquí lo más importante:
> - **La Regla de Oro:** ¡Prohibido dividir por cero! El denominador **nunca** puede ser igual a $0$. De aquí nacen las asíntotas y los huecos.
> - **Paso 0 — Factorizar:** Como dice el Profe Alex, "lo primero es factorizar". Esto nos dirá si un valor es una Asíntota Vertical (AV) o simplemente un "hueco" en el camino.
> - **Asíntotas:** Son líneas guía. Las **Verticales** son muros que la función jamás toca. Las **Horizontales** nos dicen qué hace la función cuando $x$ se va al infinito. **¡Ojo con el mito!** Las asíntotas horizontales sí se pueden cruzar en la parte central de la gráfica; solo son "límites" en los extremos.
> - **Relación clave:** El dominio y el rango son los "permisos" de la función. El dominio nos dice qué valores de $x$ podemos usar, y el rango nos dice qué valores de $y$ resultan.

---

### 2. TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula | Nota de Caso (Profe Alex) |
| :--- | :--- | :--- |
| **Paso 0: Factorización** | Simplificar la expresión para identificar factores comunes que se cancelan. | **Esencial:** Evita errores antes de calcular asíntotas. |
| **Asíntota Vertical (AV)** | Se halla igualando el denominador (tras simplificar) a cero. | Si un factor se cancela, no es AV, es un **Hueco**. |
| **Asíntota Horizontal (AH)** | Describe el comportamiento final de la función en los extremos. | **Caso 1:** Grados iguales $\to y = \frac{coef. principal N}{coef. principal D}$<br>**Caso 2:** Grado $N < D \to y = 0$. |
| **Dominio** | $\mathbb{R} - \{ \text{valores que anulan el denominador original} \}$. | Incluye tanto las AV como los Huecos. |
| **Rango** | $\mathbb{R} - \{ \text{Asíntota Horizontal} \}$ (Generalmente). | Se debe verificar si hay "huecos" que afecten la $y$. |
| **Ceros / Cortes** | **Corte en $y$:** Evaluar $f(0)$.<br>**Corte en $x$:** Igualar el numerador a cero. | Ayudan a saber por dónde pasan las curvas. |

---

### 3. EJEMPLOS RESUELTOS ADICIONALES

````ad-example
title: Ejemplo A — Caso de exponentes iguales (Caso 1)
¡Vamos paso a paso con la función: $f(x) = \frac{2x-5}{x-3}$!

**Paso 0: ¿Podemos factorizar?**
En este caso, ni el numerador ni el denominador se pueden simplificar más. ¡Seguimos!

**Paso 1: ¡Busquemos la Asíntota Vertical (AV)!**
Igualamos el denominador a cero:
$x - 3 = 0 \implies x = 3$
*La función tiene un muro prohibido en $x = 3$.*

**Paso 2: Busquemos la Asíntota Horizontal (AH)**
Como los grados son iguales (Grado 1 arriba y abajo), dividimos los coeficientes:
$y = \frac{2}{1} \implies y = 2$

**Paso 3: Puntos de corte (Los ceros)**
- **Corte en $y$ ($x=0$):** $f(0) = \frac{2(0)-5}{0-3} = \frac{-5}{-3} \approx 1.67$
- **Corte en $x$ ($y=0$):** $2x - 5 = 0 \implies 2x = 5 \implies x = 2.5$

**Paso 4: Bosquejo de la gráfica**
La gráfica tiene dos ramas. Una viene desde la izquierda, pasa por $(0, 1.67)$, cruza el eje $x$ en $2.5$ y baja pegadita a la AV ($x=3$). La otra rama aparece arriba a la derecha.

✅ **Dominio:** $\mathbb{R} - \{3\}$
✅ **Rango:** $\mathbb{R} - \{2\}$
````

````ad-example
title: Ejemplo B — Costo promedio de producción (Aplicación Real)
**Problema:** Una fábrica de calculadoras tiene costos fijos. El costo promedio por unidad al producir $x$ artículos es: $C(x) = \frac{50x + 200}{x}$.

**Paso 1: Análisis del Dominio**
Matemáticamente, $x \neq 0$. Pero en la vida real, ¡no puedes producir calculadoras negativas! Así que el dominio tiene sentido para $x > 0$.

**Paso 2: ¿Qué pasa si producimos millones de calculadoras? (AH)**
Buscamos la AH (grados iguales):
$y = \frac{50}{1} \implies y = 50$

**Interpretación Práctica:**
¡No te dejes engañar! Aunque produzcas una cantidad infinita de calculadoras, el costo promedio nunca bajará de **$\$50$**. Ese valor representa el **suelo de costos fijos** (materiales mínimos, energía, etc.). La AH es el límite de eficiencia de la fábrica.
````

---

### 4. EJERCICIOS DE REPASO

````ad-abstract
title: 🟢 Fácil — Identificación rápida
¡Para calentar motores! Identifica las AV y AH de:
1. $f(x) = \frac{x + 5}{x - 2}$
2. $g(x) = \frac{3x}{x + 1}$
````

````ad-abstract
title: 🟡 Medio — El Caso 2 y el "Hueco"
Dada la función $f(x) = \frac{x - 3}{x^2 - 9}$:
1. **Paso 0:** Factoriza el denominador. ¿Qué notas con el factor $(x - 3)$?
2. Identifica si existe una AV o un "hueco" en $x = 3$.
3. Determina la AH (Recuerda: Grado $N < D$).
4. Define el Dominio y Rango.
````

````ad-abstract
title: 🔴 Avanzado — Aplicación financiera con "Hueco"
Un modelo de beneficio neto es $B(x) = \frac{(x - 4)(x + 1)}{x - 4}$, donde $x$ es la inversión en miles de USD.
1. Simplifica la función. ¿Qué tipo de gráfica queda?
2. El modelo contable dice que si $x = 4$ hay un error. ¿Es una asíntota o un hueco?
3. **Interpretación:** Si la inversión es exactamente $\$4,000$, el modelo se rompe (indeterminación). Explica por qué, basándote en que el beneficio esperado justo antes y después de ese punto tiende a $\$5,000$.
````

---

### 5. CONSEJO DE ESTUDIO

> [!tip] 💡 La "Tabla de Valores Inteligente"
> ¡Este es el secreto del Profe Alex para que tus gráficas queden perfectas! No elijas números al azar. Una vez que encuentres tu **Asíntota Vertical (AV)**, elige siempre:
> - **Dos valores a la izquierda** (muy cerquita).
> - **Dos valores a la derecha** (muy cerquita).
> 
> Por ejemplo, si tu AV es $x = 3$, evalúa en $2.8, 2.9$ y en $3.1, 3.2$. Esto te dirá inmediatamente si la curva se dispara hacia arriba ($+\infty$) o hacia abajo ($-\infty$). ¡No más dibujos adivinados!