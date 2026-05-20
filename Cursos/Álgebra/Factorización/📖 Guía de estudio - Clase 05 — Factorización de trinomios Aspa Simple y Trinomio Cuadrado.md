# 📖 Guía de estudio — Clase 05: Factorización de trinomios de la forma $ax^2+bx+c$

> [!info] 📌 Conceptos clave
> Para dominar la factorización por el método de aspa simple, es fundamental entender los siguientes pilares pedagógicos:
> - **Organización descendente:** Antes de comenzar, el trinomio debe estar ordenado según el exponente de la variable, de mayor a menor (ej. $x^2, x^1$ y el término independiente).
> - **Lógica del Aspa Simple:** El objetivo es descomponer los términos de los extremos (el primero y el tercero) en dos factores cada uno, de modo que su interacción genere el término central.
> - **Condición de los exponentes:** Este método es aplicable si el exponente del primer término es el doble del exponente del término central (ej. en $x^4 + bx^2 + c$, funciona porque 2 es la mitad de 4).
> - **Verificación vs. Resultado:** La prueba de validez se realiza mediante una **multiplicación en cruz** (en aspa). Sin embargo, una vez verificado el término central, los factores finales se deben escribir **siempre de forma horizontal**.

| Término | Definición / Fórmula |
| :--- | :--- |
| **Trinomio organizado** | Expresión de tres términos dispuesta en orden: término cuadrático ($x^2$), término lineal ($x^1$) y término independiente (número sin variable). |
| **Aspa Simple** | Método que busca factores para los extremos cuya multiplicación cruzada y posterior suma algebraica verifican el término medio. |
| **Factorización** | Proceso inverso a la multiplicación que descompone una expresión en factores más simples (binomios). |
| **Raíz de una letra** | Operación que consiste en dividir el exponente de la variable por 2 (aplicable cuando el exponente es par; ej. la raíz de $x^6$ es $x^3$). |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Caso Básico
**Ejercicio:** Factorizar $x^2 + 7x + 10$

- **Paso 1: Descomponer los extremos.**
  - Para $x^2$: Los factores son $x \cdot x$.
  - Para $10$: Los factores son $(+5) \cdot (+2)$.
- **Paso 2: Multiplicación en cruz (Verificación).**
  - $(x \cdot +5) = +5x$
  - $(x \cdot +2) = +2x$
  - Suma algebraica: $5x + 2x = 7x$. ¡Coincide con el término central!
- **Resultado final:** Agrupamos los términos horizontalmente:
  **$(x + 5)(x + 2)$**
```

```ad-example
title: Ejemplo B — Caso con aplicación real $USD
**Enunciado:** El área de un terreno rectangular está representada por la expresión $6x^2 + 7x + 2$ dólares. Determine las expresiones que representan sus dimensiones (largo y ancho).

- **Paso 1: Descomponer los términos extremos con sus signos.**
  - Factores de $6x^2$: $3x$ y $2x$ (ya que $3x \cdot 2x = 6x^2$).
  - Factores de $+2$: $+2$ y $+1$ (ya que $(+2) \cdot (+1) = +2$).
- **Paso 2: Verificación en aspa.**
  - $(3x \cdot +1) = +3x$
  - $(2x \cdot +2) = +4x$
  - Suma de resultados: $3x + 4x = 7x$. El término central es correcto.
- **Resultado:** Las dimensiones del terreno, expresadas como el producto de sus lados, son:
  **$(3x + 2)(2x + 1)$**
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Dificultad: Fácil (a = 1)
Factoriza los siguientes trinomios donde el coeficiente principal es 1:
1. $x^2 - 5x + 6$
2. $a^2 + 7a + 6$
3. $x^2 - x - 6$
```

```ad-abstract
title: 🟡 Dificultad: Media (a > 1)
color: 255, 200, 0
Factoriza buscando los factores adecuados para el coeficiente $a$:
1. $2x^2 - 3x - 2$
2. $3x^2 - 3x - 6$
3. $12x^2 - x - 6$
```

```ad-abstract
title: 🔴 Dificultad: Avanzada — Aplicación con $USD
color: 255, 0, 0
**Problema de Costo Total:** El presupuesto para una producción textil se define por el trinomio $15m^2 - 23m + 4$ dólares. 
1. Halla los dos factores resultantes de la factorización.
2. Si el **Costo Total = (Precio Unitario) × (Cantidad)**, ¿qué binomios representan estas dos variables comerciales?
*Pista: Utiliza el método de aspa simple para descomponer $15m^2$ y $+4$ buscando que la suma cruzada resulte en $-23m$.*
```

> [!tip] 💡 Consejo de estudio
> **La estrategia de los signos:** Si el término independiente es negativo, los signos de tus factores numéricos **deben ser diferentes**. Si al realizar la prueba del aspa obtienes el número correcto pero con el **signo opuesto** (ej. obtienes $+3x$ pero necesitas $-3x$), no borres todo: simplemente intercambia los signos de los factores que elegiste y vuelve a verificar. ¡Es la forma más rápida de corregir!