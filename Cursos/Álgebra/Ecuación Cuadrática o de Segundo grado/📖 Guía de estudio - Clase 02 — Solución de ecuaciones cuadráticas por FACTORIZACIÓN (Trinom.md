# 📖 Guía de estudio — Clase 02: Solución de ecuaciones cuadráticas por factorización

> [!info] 📌 Conceptos clave
> Para dominar las ecuaciones de segundo grado por factorización, sigue estos pilares fundamentales del Profe Alex:
> *   **Simplificación inicial:** ¡No te apresures! Primero resuelve paréntesis y multiplicaciones (propiedad distributiva) para ver la ecuación real.
> *   **Igualación a cero ($= 0$):** Es el paso de oro. Debes pasar todos los términos a un solo lado de la igualdad, cambiando sus signos, hasta que el otro lado quede en cero.
> *   **Identificación de términos:** Asegúrate de tener el término cuadrático ($x^2$), el lineal ($x$) y el independiente (el número sin letra).
> *   **Principio de los dos factores:** Si multiplicas dos paréntesis y el resultado es cero ($A \cdot B = 0$), significa que el primer paréntesis es cero **o** el segundo lo es. ¡Esto nos da las dos soluciones!

---

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula (Factorización) | Nota del Profe |
| :--- | :--- | :--- |
| **Ecuación Estándar** | $ax^2 + bx + c = 0$ | ¡Cuidado! Antes de empezar, asegúrate de que esté ordenada y sea igual a cero. |
| **Trinomio $x^2 + bx + c$** | $(x + m)(x + n) = 0$ | Buscamos dos números que multiplicados den $c$ y sumados o restados den $b$. |
| **Trinomio Cuadrado Perfecto (TCP)** | $a^2 \pm 2ab + b^2 = \mathbf{(a \pm b)^2}$ | **Prueba lógica:** Saca raíces al 1ero y 3ero. Si el doble producto de esas raíces es igual al término central, ¡es un TCP! |
| **Trinomio $ax^2 + bx + c$** | Método de multiplicación por el coeficiente $a$. | Este método es un "puente": multiplicamos por $a$ para convertirlo en un trinomio simple y poder usar los dos paréntesis. |

---

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Simplificación y Trinomio Simple
**Enunciado:** $x(2x-5) = 3(x-2)$

**Paso 1: Resolver operaciones (Propiedad distributiva)**
Multiplicamos los términos:
$2x^2 - 5x = 3x - 6$

**Paso 2: Igualar a cero (Transposición de términos)**
Pasamos todo al lado izquierdo. Nota cómo **cambian los signos**:
$2x^2 - 5x \mathbf{ - 3x + 6} = 0$

**Paso 3: Reducir términos semejantes**
$2x^2 \mathbf{ - 8x } + 6 = 0$

**Paso 4: Simplificar la ecuación (Estrategia Profe Alex)**
Como todos los números son pares, dividimos toda la ecuación entre **2** para trabajar con números más pequeños:
$x^2 - 4x + 3 = 0$

**Paso 5: Factorizar el trinomio**
Buscamos dos números que multiplicados den $+3$ y sumados den $-4$. Los números son $-3$ y $-1$:
$(x - 3)(x - 1) = 0$

**Paso 6: Hallar las soluciones**
*   $x - 3 = 0 \rightarrow \mathbf{x_1 = 3}$
*   $x - 1 = 0 \rightarrow \mathbf{x_2 = 1}$

**Resultado:** Las soluciones son $x_1 = 3$ y $x_2 = 1$.
```

```ad-example
title: Ejemplo B — Aplicación de costos en $USD
**Enunciado:** El costo de producción de una serie de artículos está dado por la ecuación $x^2 + 7x - 18 = 0$, donde $x$ es la cantidad de artículos. Encuentra el número de artículos producidos.

**Paso 1: Factorizar**
Buscamos dos números que multiplicados den $-18$ y que **restados** den $+7$:
*   $(+9) \times (-2) = -18$
*   $9 - 2 = 7$
La factorización queda: **$(x + 9)(x - 2) = 0$**

**Paso 2: Resolver para x**
*   $x + 9 = 0 \rightarrow x = -9$
*   $x - 2 = 0 \rightarrow x = 2$

**Paso 3: Análisis de contexto real**
¡Atención aquí! En la vida real no puedes producir "-9" artículos. Por lógica, descartamos el valor negativo.

**✅ Resultado:** Se deben producir **2 artículos**.
```

---

## Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel Fácil: Factorización Directa
Resuelve estas ecuaciones donde el coeficiente de $x^2$ es 1:
1. $x^2 - 2x - 8 = 0$
2. $x^2 + 5x + 6 = 0$
3. $x^2 - x - 12 = 0$
```

```ad-abstract
title: 🟡 Nivel Medio: Operaciones Previas
Primero simplifica, iguala a cero y luego factoriza:
1. $x(x + 3) = 10$
2. $(x - 1)(x + 2) = 4$
```

```ad-abstract
title: 🔴 Nivel Avanzado: Aplicación con $USD
Un terreno tiene un precio por metro cuadrado $x$ definido por la ecuación: $3x^2 + 7x = 6$.
Para hallar el valor de $x$ en dólares, usa el método del coeficiente $a$ ($a=3$):
1. **Iguala a cero:** $3x^2 + 7x - 6 = 0$.
2. **Multiplica por 3:** Al multiplicar el término lineal, **mantén la operación indicada** (es decir, escribe $7(3x)$ en lugar de 21) para facilitar la factorización.
3. **Factoriza y resuelve:** Indica cuál es el valor positivo válido para el precio en USD.
```

---

> [!tip] 💡 Consejo de estudio
> **¡La comprobación es tu mejor amiga!** Una vez que encuentres tus valores de $x$, sustitúyelos en la ecuación original. Si al final obtienes una igualdad verdadera (como $0 = 0$), significa que tu trabajo es impecable. ¡Confía en el proceso, la matemática no miente!