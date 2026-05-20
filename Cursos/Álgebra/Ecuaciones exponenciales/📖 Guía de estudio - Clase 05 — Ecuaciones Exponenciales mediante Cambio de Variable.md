# 📖 Guía de estudio — Clase 05: Ecuaciones Exponenciales por Cambio de Variable

> [!info] 📌 Conceptos clave
> Para dominar este método, basándonos en las enseñanzas del "Profe Alex", debemos aprender a simplificar lo complejo. Aquí tienes los pilares fundamentales:
> - **¿Cuándo usar el cambio de variable?**: Identifica bases donde una es el cuadrado de la otra (ej. $2$ y $4$, $3$ y $9$, $5$ y $25$). También es la señal ideal cuando ves exponentes con signo opuesto ($x$ y $-x$).
> - **Transformación a forma cuadrática**: El objetivo es que la ecuación se vea como $am^2 + bm + c = 0$. ¡Es como disfrazar la ecuación exponencial de una ecuación de segundo grado!
> - **El "Regreso" Obligatorio**: Hallar el valor de la variable auxiliar ($m, u, t$) es solo la mitad del camino. Siempre, sin falta, debes volver a la variable original $x$.
> - **La Regla del 1**: ¡Truco vital! Recuerda que el número $1$ puede escribirse como cualquier base elevada a la cero ($a^0 = 1$). Esto te salvará cuando despejes soluciones como $2^x = 1$.
> - **Restricción Real**: Si al intentar regresar a $x$ llegas a algo como $2^x = -4$, ¡detente! Una base positiva elevada a cualquier exponente nunca dará un resultado negativo. Esa solución se descarta.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Potencia de potencia** | Permite transformar $4^x$ en $(2^2)^x$. Por propiedad, podemos intercambiar los exponentes: $(2^x)^2$. Así visualizamos el término al cuadrado. |
| **Producto de bases iguales** | Usamos $a^{x+n} = a^x \cdot a^n$. **¡OJO!** Jamás multipliques el coeficiente por la base si esta tiene un exponente variable. Ejemplo: $3 \cdot 2^x$ **NO** es $6^x$. |
| **Cociente de bases iguales** | Usamos $a^{x-n} = \frac{a^x}{a^n}$. Es fundamental para "bajar" las potencias con exponente negativo al denominador. |
| **El exponente cero** | **$a^0 = 1$**. Si tu variable auxiliar es igual a 1 (ej. $m = 1$), entonces $a^x = a^0$, lo que significa que $x = 0$. |
| **Variable Auxiliar** | Es una letra ($m, u, t$) que usamos para sustituir la expresión exponencial (ej. $2^x = m$) y facilitar la factorización. |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Caso básico de sustitución
**Ecuación:** $4^x - 4 \cdot 2^x - 32 = 0$

1. **Paso 1 (Transformación):** Escribimos $4^x$ como $(2^x)^2$. La ecuación ahora es: $(2^x)^2 - 4 \cdot 2^x - 32 = 0$.
2. **Paso 2 (¡Hagamos el truco!):** Sustituimos $2^x$ por $m$ para que la ecuación se vea mucho más amigable: $m^2 - 4m - 32 = 0$.
3. **Paso 3 (Factorización):** Buscamos dos números que multiplicados den $-32$ y sumados den $-4$. ¡Son $-8$ y $4$!
   $(m - 8)(m + 4) = 0$
4. **Paso 4 (Valores de m):** Igualamos cada paréntesis a cero: $m = 8$ y $m = -4$.
5. **Paso 5 (Regreso a x):** 
   - Si $m = 8 \implies 2^x = 8 \implies 2^x = 2^3$. Entonces **$x = 3$**.
   - Si $m = -4 \implies 2^x = -4$. **¡Cuidado!** No hay solución real aquí.

✅ **Resultado: x = 3**
```

```ad-example
title: Ejemplo B — Aplicación financiera en $USD
**Problema:** El crecimiento de una inversión sigue la ecuación $2^x + 2^{1-x} = 3$, donde $x$ es el tiempo en meses. ¿En qué meses el valor alcanza el objetivo?

1. **Paso 1 (Separar exponentes):** Aplicamos la propiedad de cociente: $2^x + \frac{2^1}{2^x} = 3$. Esto es lo mismo que $2^x + \frac{2}{2^x} = 3$.
2. **Paso 2 (Sustitución):** Llamemos $2^x = t$. La ecuación queda: $t + \frac{2}{t} = 3$.
3. **Paso 3 (Destruir el denominador):** Multiplicamos cada término por $t$ para eliminarlo de la parte de abajo:
   $t(t) + t(\frac{2}{t}) = 3(t) \implies t^2 + 2 = 3t$.
4. **Paso 4 (Forma cuadrática):** Ordenamos: $t^2 - 3t + 2 = 0$.
5. **Paso 5 (Factorización):** $(t - 2)(t - 1) = 0$. Así que $t = 2$ y $t = 1$.
6. **Paso 6 (Regreso a x):**
   - Si $t = 2 \implies 2^x = 2^1 \implies \mathbf{x = 1}$.
   - Si $t = 1 \implies 2^x = 1$. Aplicamos la **Regla del 1**: $2^x = 2^0 \implies \mathbf{x = 0}$.

✅ **Resultado: Mes 0 y Mes 1.**
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil (Sustitución directa)
1. Resuelve $9^x - 10 \cdot 3^x + 9 = 0$. (Pista: Usa $3^x = u$ y recuerda la regla del $3^0$).
2. Resuelve $25^x - 6 \cdot 5^x + 5 = 0$.
3. Resuelve $4^x - 6 \cdot 2^x + 8 = 0$.
```

```ad-abstract
title: 🟡 Medio (Uso de propiedades de exponentes)
1. Resuelve $4^x + 2^5 = 3 \cdot 2^{x+2}$. (¡Atención! No multipliques $3 \cdot 2$, primero separa $2^x \cdot 2^2$).
2. Resuelve $9^x + 27 = 12 \cdot 3^x$.
3. Resuelve $2^x + 2^{2-x} = 5$.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
1. El bono de una cuenta digital sigue la ecuación $7^x + 7^{2-x} = 50$. Determina los niveles $x$ para ganar el bono. (Pista de tutor: Recuerda que $7^2 = 49$ al separar la fracción).
2. Resuelve $3^x + 3^{1-x} = 4$.
3. Resuelve $5^x + 5^{2-x} = 26$.
```

> [!tip] 💡 Consejo de estudio del Profe Alex
> Si el término al cuadrado ($m^2$) está solo (tiene coeficiente 1), **usa siempre el método de los dos paréntesis** para factorizar. Es mucho más rápido, seguro y eficiente para tus exámenes que aplicar la fórmula general. ¡Ahorra tiempo y evita errores de signos!