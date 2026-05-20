# 📖 Guía de estudio — Clase 02: Simplificación de fracciones algebraicas

> [!info] 📌 Conceptos clave
> - **Prioridad de la factorización:** ¡Recuerda! Antes de intentar simplificar cualquier expresión, es obligatorio convertir los polinomios en factores (multiplicaciones). No podemos "tachar" términos que estén sumando o restando directamente sin antes haber factorizado.
> - **Fracciones equivalentes:** Una fracción no cambia su valor si se amplifica (multiplicando) o se simplifica (dividiendo) tanto el numerador como el denominador por la misma expresión. 
> - **El papel del MCM:** El Mínimo Común Múltiplo sirve para que diferentes fracciones puedan "hablar el mismo idioma". Al encontrar un denominador común, podemos unificarlas para realizar operaciones como la suma o la resta.
> - **La verificación de oro:** Si quieres estar seguro de tu simplificación, puedes realizar el proceso inverso (amplificar) y deberías volver a obtener la expresión original.

## TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula |
| :--- | :--- |
| **MCM Algebraico** | Para encontrarlo: 1. Halla el MCM de los coeficientes numéricos. 2. Elige las variables (letras) con el **máximo exponente**. |
| **Factor Común** | Se extrae el número o letra que se repite en todos los términos, utilizando siempre el **menor exponente**. |
| **Diferencia de Cuadrados** | Se identifica cuando dos términos con raíz cuadrada exacta se están restando: $a^2 - b^2 = (a+b)(a-b)$. |
| **Trinomio $x^2 + bx + c$** | Se buscan dos números que multiplicados den $c$ y sumados/restados den $b$. **Chequeo mental:** Verifica que los signos elegidos den el resultado correcto en la suma/resta. |
| **Trinomio Cuadrado Perfecto** | Se reconoce porque el primer y tercer término tienen raíces exactas y el término central es el doble producto de dichas raíces: $(a \pm b)^2$. |
| **Suma o Diferencia de Cubos** | Se extraen las raíces cúbicas y se aplica: $(a \pm b)(a^2 \mp ab + b^2)$. Los signos del segundo paréntesis se intercalan si el primero es positivo. |

## SECCIÓN DE EJEMPLOS RESUELTOS ADICIONALES

```ad-example
title: Ejemplo A — Simplificación por factor común
**¡No te pierdas! Este es el camino paso a paso para simplificar:**

Simplificar la expresión: $\frac{4xy}{2x^2+6x}$

1. **Factorizar el denominador:** Observamos que en $2x^2+6x$ el máximo común divisor numérico es 2 y la letra que se repite es $x$. Obtenemos: $2x(x+3)$.
2. **Reescribir la expresión:** La fracción ahora se ve así: $\frac{4xy}{2x(x+3)}$.
3. **Simplificar factores comunes:** 
   - Dividimos los coeficientes: $4 / 2 = 2$.
   - Simplificamos las variables: $x / x = 1$ (la letra $x$ se cancela porque su exponente se vuelve cero).
4. **Resultado final:** $\frac{2y}{x+3}$
*Consejo de verificación: Si multiplicas $2y$ por $2x$ y $(x+3)$ por $2x$, ¡volverás a la fracción original!*
```

```ad-example
title: Ejemplo B — Aplicación en costos unitarios ($USD)
**¡Tú puedes! Apliquemos el álgebra a un caso de la vida real:**

**Enunciado:** Un comerciante compra productos por un valor total de $(x^2 - 2x - 3)$ dólares. Si compró $(x - 3)$ artículos, ¿cuál es el costo de cada uno?

**Proceso paso a paso:** 
1. **Plantear la fracción:** El costo unitario es $\frac{\text{Costo Total}}{\text{Cantidad}} = \frac{x^2 - 2x - 3}{x - 3}$.
2. **Factorizar el numerador (Trinomio):** Buscamos dos números que multiplicados den $-3$ y sumados den $-2$. **Chequeo mental:** $(-3) \times (+1) = -3$ y $(-3) + 1 = -2$. ¡Correcto!
   - La expresión queda: $\frac{(x-3)(x+1)}{x-3}$.
3. **Simplificar:** Cancelamos el factor idéntico $(x-3)$ arriba y abajo.
4. **Resultado final:** El costo de cada producto es de **$(x+1)$ dólares**.
```

## SECCIÓN DE EJERCICIOS DE REPASO

```ad-abstract
title: Ejercicios 🟢 Fácil (Simplificación básica)
1. Simplifica la expresión: $\frac{3x+3}{3}$
2. Reduce términos: $\frac{10a^2b}{5ab}$
3. Simplifica usando factor común: $\frac{x^2+x}{x}$
```

```ad-abstract
title: Ejercicios 🟡 Medio (Mínimo Común Denominador)
Encuentra el MCM de los denominadores para las siguientes parejas (recuerda la regla del máximo exponente):
1. $\frac{5}{x+1}$ y $\frac{2}{x-1}$
2. $\frac{1}{3a}$ y $\frac{5}{a^2}$
3. $\frac{1}{x+2}$ y $\frac{1}{x+3}$
```

```ad-abstract
title: Ejercicios 🔴 Avanzado (Aplicación Financiera $USD)
1. Si una ganancia de $(x^2 - 25)$ dólares se reparte equitativamente entre $(x + 5)$ socios, ¿cuánto recibe cada uno?
2. El área de un local comercial es de $(x^2 + 6x + 9)$ metros cuadrados. Si su largo es $(x + 3)$, ¿cuál es la expresión para su ancho? (Aplica Trinomio Cuadrado Perfecto).
3. Una empresa genera ingresos de $(x^2 - 1)$ dólares. Si debe pagar una deuda representada por la simplificación de $\frac{x^2-1}{x+1}$, ¿cuánto debe pagar en términos de $x$?
```

> [!tip] 💡 Consejo de estudio
> **Cuidado con el "1 Fantasma":** Cuando simplifiques y notes que **todos** los términos del numerador se cancelan, recuerda que nunca queda un cero; siempre queda un **1**. Por ejemplo: $\frac{x+1}{(x+1)(x-2)} = \frac{1}{x-2}$. 
> **Regla de oro:** ¡Factoriza antes de tachar! Nunca simplifiques términos que estén en medio de una suma o resta sin haberlos convertido en factores primero.