# 📖 Guía de estudio — Clase 06: Cuadrado de un binomio

> [!info] 📌 Conceptos clave
> Esta guía sintetiza los fundamentos para resolver el cuadrado de un binomio, un producto notable esencial en el álgebra. Basándonos en las lecciones del **Profe Alex**, es vital comprender no solo el procedimiento, sino la lógica detrás de la fórmula:
> 
> 1.  **Definición de binomio:** Expresión algebraica de exactamente dos términos unidos por una suma o resta.
> 2.  **Condición del exponente:** Esta regla es exclusiva para binomios elevados a la **potencia 2**. Si el exponente es 3, se requiere la fórmula del *Cubo de un binomio*, un tema distinto que no debe confundirse con el actual.
> 3.  **La estructura del resultado (Trinomio):** El desarrollo siempre genera tres términos. **Alerta de error:** Un fallo común es aplicar una "distributiva falsa" pensando que $(a + b)^2 = a^2 + b^2$. Esto es incorrecto; el término central ($2ab$) es lo que completa el área del cuadrado.
> 4.  **Comportamiento de los signos:** El primer y tercer término siempre resultarán **positivos** (pues toda cantidad elevada al cuadrado es positiva). El signo del segundo término será idéntico al signo original del binomio.
> 5.  **Términos no semejantes:** Una vez obtenido el trinomio, no se deben sumar los términos entre sí si no son semejantes (por ejemplo, $x^2$ y $x$ representan dimensiones distintas).

## Fórmulas y definiciones importantes

| Término | Descripción | Fórmula |
| :--- | :--- | :--- |
| **Cuadrado de la suma** | El cuadrado del primer término, **más** el doble producto del primero por el segundo, **más** el cuadrado del segundo. | $(a + b)^2 = a^2 + 2ab + b^2$ |
| **Cuadrado de la diferencia** | El cuadrado del primer término, **menos** el doble producto del primero por el segundo, **más** el cuadrado del segundo. | $(a - b)^2 = a^2 - 2ab + b^2$ |
| **Potencia de potencia** | Si una base ya tiene exponente y se eleva al cuadrado, los exponentes se multiplican. Ejemplo del Profe Alex: $(x^3)^2 = x^6$. | $(x^n)^m = x^{n \cdot m}$ |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Caso con variables y números
**Problema**: Resolver $(x + 5)^2$

- **Paso 1: Identificar términos**. Primero: $x$; Segundo: $5$.
- **Paso 2: Plantear la estructura**. Aplicamos la fórmula de la suma: $(x)^2 + 2(x)(5) + (5)^2$.
- **Paso 3: Resolver operaciones**. Multiplicamos el centro ($2 \cdot 5 = 10$) y la potencia final ($5 \cdot 5 = 25$).

✅ **Resultado**: $x^2 + 10x + 25$
```

```ad-example
title: Ejemplo B — Aplicación práctica con $USD
**Enunciado**: El área de un panel solar cuadrado está definida por $(2a + 4)^2$ en dólares. Determine la expresión de su costo total.

- **Paso 1: Cuadrado del primero**. **Atención pedagógica:** Debe elevarse tanto el coeficiente como la variable: $(2a)^2 = 4a^2$.
- **Paso 2: Doble producto**. Multiplicamos el 2 constante por ambos términos: $2(2a)(4) = 16a$.
- **Paso 3: Cuadrado del segundo**. Resolvemos la potencia simple: $4^2 = 16$.

✅ **Resultado**: El costo total es $(4a^2 + 16a + 16) \text{ USD}$.
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil — Nivel Inicial
Practica la identificación de términos y la aplicación de la fórmula básica:
1. $(m + 3)^2$
2. $(y - 7)^2$
3. $(x + 10)^2$
```

```ad-abstract
title: 🟡 Medio — Coeficientes y Exponentes
Aplica la regla de potencia de potencia y eleva correctamente los coeficientes:
1. $(3x^2 + 2y)^2$
2. $(5m - 2)^2$
3. $(x^3 - 5)^2$
```

```ad-abstract
title: 🔴 Avanzado — Aplicación Técnica en $USD
Resuelve y expresa en formato monetario. **Nota técnica:** Por convención pedagógica, ordena las variables del término central alfabéticamente (ej. $m$ antes que $n$):
1. $(3x^3 - 2y^2)^2 \text{ USD}$
2. $(4b^2 + 5c^3)^2 \text{ USD}$
3. $(-5m^2 + 3n^2)^2 \text{ USD}$ (Aplica el consejo de reordenar términos antes de iniciar).
```

> [!tip] 💡 Consejo de estudio del "Profe Alex"
> Cuando enfrentes un binomio que comienza con un término negativo (como $-5m + 3n$), no te compliques con la gestión de signos negativos al inicio. La estrategia más segura es **reordenar los términos** manteniendo sus signos originales: transforma $-5m + 3n$ en $(3n - 5m)$. 
> 
> Al hacerlo, conviertes un ejercicio potencialmente confuso en un "Cuadrado de la diferencia" estándar, lo cual es psicológicamente más sencillo de procesar y reduce drásticamente los errores en el primer término del trinomio. Recordatorio final: el primero y el último término del resultado **siempre** deben ser positivos.