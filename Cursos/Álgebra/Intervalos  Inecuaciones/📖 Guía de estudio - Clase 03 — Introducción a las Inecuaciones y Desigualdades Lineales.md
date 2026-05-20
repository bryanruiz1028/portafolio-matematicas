# 📖 Guía de estudio — Clase 03: Introducción a las Inecuaciones Lineales

> [!info] 📌 Conceptos clave
> Una **inecuación** es una relación de desigualdad entre dos expresiones algebraicas. A diferencia de las ecuaciones, donde buscamos un valor único, aquí buscamos un conjunto de valores que satisfagan la condición.
> 
> *   **Identificación:** Una inecuación es **lineal** (o de primer grado) si el máximo exponente de la variable es $1$. No debe haber variables multiplicándose entre sí ($x^2$) ni variables en los denominadores; si la variable aparece abajo, se trata de una *inecuación racional*, la cual requiere un método de resolución distinto.
> *   **Resolver:** Es hallar el conjunto de valores que hacen verdadera la desigualdad. Generalmente, este conjunto es infinito.
> *   **Representación:** La solución se presenta de tres formas:
>     1. **Desigualdad final:** (Ej. $x < -3$).
>     2. **Gráfico:** Representación visual en la recta numérica. Para facilitar esto, leemos la $x$ como *"los números"*. Ejemplo: $x < -3$ se lee como *"los números menores que $-3$"*.
>     3. **Intervalo:** Notación formal del conjunto (Ej. $(-\infty, -3)$).

## 2. Fórmulas y definiciones importantes

| Término | Símbolo / Definición | Nota Importante |
| :--- | :--- | :--- |
| **Símbolos de desigualdad** | $>$, $<$, $\geq$, $\leq$ | Son el núcleo de la inecuación; definen la relación de orden en lugar de una igualdad. |
| **Punto abierto** | Huequito (sin rellenar) | Se utiliza con los símbolos estrictos $>$ o $<$ e indica que el valor límite **no** se incluye. |
| **Punto cerrado** | Punto relleno | Se utiliza con $\geq$ o $\leq$ e indica que el valor límite **sí** es parte de la solución. |
| **Regla de Oro (Negativos)** | Cambio de dirección | Al multiplicar o dividir por un número negativo, el sentido de la desigualdad **se invierte**. Esto se visualiza mejor al "Multiplicar por $-1$". |
| **m.c.m.** | Mínimo Común Múltiplo | Es la herramienta pedagógica clave para eliminar denominadores, multiplicando cada término por este valor. |

## 3. Ejemplos resueltos adicionales

> [!example] Ejemplo A — Inecuación Lineal Simple
> **Problema:** Resolver $7x + 5 < 2x - 10$
> 
> **Paso a paso:**
> 1. **Agrupar variables:** Pasamos el $2x$ a la izquierda restando: $7x - 2x + 5 < -10$.
> 2. **Agrupar constantes:** Pasamos el $5$ a la derecha restando: $5x < -10 - 5$.
> 3. **Simplificar:** $5x < -15$.
> 4. **Despejar:** Como el $5$ es positivo, pasa a dividir sin cambiar el signo: $x < \frac{-15}{5} \Rightarrow x < -3$.
> 
> **Comprobación:**
> Si elegimos un número del intervalo solución, como $x = -4$:
> $7(-4) + 5 < 2(-4) - 10 \Rightarrow -28 + 5 < -8 - 10 \Rightarrow -23 < -18$. **(Verdadero)**
> 
> ✅ **Resultado:** $x < -3$ | Intervalo: $(-\infty, -3)$.

> [!example] Ejemplo B — Aplicación de presupuesto en $USD$
> **Problema:** Una empresa compara dos costos operativos. El Plan A tiene un costo de $3x + 15$ y el Plan B de $x + 45$, donde $x$ es el costo por unidad producida. ¿Para qué valores de $x$ el Plan A es más costoso que el Plan B?
> 
> **Resolución:**
> 1. **Planteamiento:** $3x + 15 > x + 45$.
> 2. **Trasponer términos:** $3x - x > 45 - 15$.
> 3. **Simplificar:** $2x > 30$.
> 4. **Despejar:** $x > 15$.
> 
> **Comprobación:**
> Probemos con $x = 20$ (dentro del rango):
> $3(20) + 15 > 20 + 45 \Rightarrow 60 + 15 > 65 \Rightarrow 75 > 65$. **(Verdadero)**
> 
> ✅ **Solución:** El Plan A es más caro cuando el costo por unidad es superior a $\$15$. Intervalo: $(15, \infty)$.

## 4. Ejercicios de repaso

```ad-abstract
title: 🟢 Bloque: Fácil (Despeje directo)
1. $x + 3 > 5$
2. $x - 4 \leq 10$
3. $2x < 8$
```

```ad-abstract
title: 🟡 Bloque: Medio (Propiedad distributiva y negativos)
1. $4(2x - 1) \leq 3x + 6$
2. $2(x - 4) \leq 5x + 10$
3. $-2x + 4 > 10$
```

```ad-abstract
title: 🔴 Bloque: Avanzado (Fracciones y m.c.m.)
1. $\frac{5x-3}{6} + \frac{x-5}{18} > \frac{x+1}{3}$
2. $\frac{2x}{3} - \frac{1}{4} \leq \frac{x}{6} + \frac{5}{12}$
3. $\frac{x}{5} + \frac{1}{2} < \frac{3x}{4} - \frac{9}{10}$
```

## 5. Consejo de estudio

> [!tip] 💡 Consejo de estudio
> Para evitar errores críticos al trabajar con valores negativos, utiliza la técnica de **"Multiplicar por $-1$"**. 
> Si al final de tu despeje obtienes $-3x \leq 12$, antes de pasar el número a dividir, multiplica toda la expresión por $-1$. Esto transformará los signos y **volteará automáticamente** el símbolo de la desigualdad: $3x \geq -12$. 
> 
> Finalmente, para la representación gráfica, recuerda siempre el truco de lectura: lee la $x$ como **"los números"**. Así, $x \geq 5$ se interpreta como *"los números mayores o iguales a 5"*, lo que te indica inmediatamente que la flecha en la recta numérica debe ir hacia la derecha y el punto debe estar relleno.