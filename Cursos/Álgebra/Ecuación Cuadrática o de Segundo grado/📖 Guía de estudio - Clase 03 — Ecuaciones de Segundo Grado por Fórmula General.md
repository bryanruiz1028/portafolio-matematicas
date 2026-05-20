# 📖 Guía de estudio — Clase 03: Ecuaciones de Segundo Grado por Fórmula General

> [!info] 📌 Conceptos clave
> 1. **Igualación a cero:** Para aplicar la fórmula, la ecuación debe estar en la forma $ax^2 + bx + c = 0$. Si hay términos en el lado derecho, trasládalos al izquierdo cambiando su signo para que la ecuación quede igualada a cero.
> 2. **Identificación de coeficientes:** Debes extraer con precisión los valores de $a$ (término cuadrático), $b$ (término lineal) y $c$ (término independiente), conservando siempre el signo que los precede.
> 3. **Uso de la fórmula general:** Es la herramienta universal para resolver estas ecuaciones: $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$. Sustituir correctamente es la clave del éxito.
> 4. **Interpretación de resultados:** Obtendremos generalmente dos soluciones ($x_1$ y $x_2$). Si el valor bajo la raíz es negativo, la ecuación no tiene solución en el conjunto de los números reales, pero sí en el campo de los **números complejos**.

## Sección de Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Fórmula General** | $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ |
| **Coeficiente $a$** | Número (coeficiente) que acompaña al término $x^2$. |
| **Coeficiente $b$** | Número (coeficiente) que acompaña al término $x$. |
| **Coeficiente $c$** | Término independiente (el número que no tiene variable). |
| **Cálculo del discriminante** | Es la expresión $b^2 - 4ac$. Determina la naturaleza de las raíces; si es negativo, la solución pertenece a los **números complejos**. |

## Ejemplos Resueltos Detallados

```ad-example
title: Ejemplo A — Caso con raíces exactas
**Ecuación:** $3x^2 + 2x - 8 = 0$

1. **Identificar $a, b, c$:** 
   $a = 3$, $b = 2$, $c = -8$.

2. **Sustituir en la fórmula:**
   Utilizamos paréntesis para proteger los signos, especialmente en los negativos:
   $$x = \frac{-(2) \pm \sqrt{(2)^2 - 4(3)(-8)}}{2(3)}$$

3. **Cálculo del discriminante ($b^2 - 4ac$):**
   * El término $-b$ cambia el signo de $b$: $-2$.
   * $(2)^2 = 4$.
   * $-4(3)(-8) = +96$ (menos por más da menos, por menos da más).
   * Radicando: $4 + 96 = 100$.
   * Raíz cuadrada: $\sqrt{100} = 10$.

4. **Calcular resultados:**
   * $x_1 = \frac{-2 + 10}{6} = \frac{8}{6} = \frac{4}{3}$
   * $x_2 = \frac{-2 - 10}{6} = \frac{-12}{6} = -2$
```

```ad-example
title: Ejemplo B — Aplicación real $USD
**Enunciado:** Si el costo de producción de un artículo está definido por la relación $x^2 - x - 42 = 0$, donde $x$ representa el valor unitario en dólares, determine los posibles valores de $x$.

1. **Identificar coeficientes:**
   $a = 1$, $b = -1$, $c = -42$.

2. **Sustituir y simplificar:**
   $$x = \frac{-(-1) \pm \sqrt{(-1)^2 - 4(1)(-42)}}{2(1)}$$
   * Cambio de signo en $-b$: $1$.
   * $(-1)^2 = 1$ (todo número negativo al cuadrado resulta positivo).
   * $-4(1)(-42) = +168$.
   * Raíz: $\sqrt{1 + 168} = \sqrt{169} = 13$.

3. **Resolución:**
   * $x_1 = \frac{1 + 13}{2} = \frac{14}{2} = 7$ USD.
   * $x_2 = \frac{1 - 13}{2} = \frac{-12}{2} = -6$ USD.

*Nota pedagógica:* En contextos de dinero o producción, descartamos el resultado negativo ($x = -6$) porque un precio o cantidad no puede ser menor a cero. La respuesta lógica es **7 USD**.
```

## Ejercicios de Repaso (Niveles)

```ad-abstract
title: Nivel 🟢 Fácil
Resuelve las siguientes ecuaciones que ya están organizadas. ¡Cuidado con el ejercicio 2!
1. $2x^2 + 6x - 20 = 0$
2. $3x^2 + 2x + 5 = 0$ (Observa el signo del discriminante).
3. $4x^2 - 20x + 25 = 0$
```

```ad-abstract
title: Nivel 🟡 Medio
Como explica el Profe Alex, primero organiza los términos e iguala a cero:
1. $x^2 = x + 42$
2. $x(x + 3) = 5x + 3$
3. $3x(2x - 3) = 3x - 4$
```

```ad-abstract
title: Nivel 🔴 Avanzado (USD)
**Problemas con decimales:** Usa tu calculadora para hallar los valores aproximados con tres cifras decimales.
1. **Caso Ganancia:** Una empresa halla su punto de equilibrio con $6x^2 - 14x - 8 = 0$. (Nota: Aquí surge la raíz $\sqrt{388}$).
2. **Caso Costos:** Determina los valores de $x$ para la ecuación $6x^2 - 12x + 4 = 0$. (Nota: Aquí surge la raíz $\sqrt{48}$).
```

> [!tip] 💡 Consejo de estudio
> ¡Hola, qué tal! Como siempre te digo, la práctica es lo que hace que esto parezca fácil. Dos consejos de oro: 
> 1. **Usa paréntesis siempre:** Al sustituir, escribe siempre el valor de $b$ entre paréntesis, especialmente si es negativo, como $(-14)^2$. Esto evita que te equivoques con el signo. 
> 2. **Domina las raíces:** Aprenderte de memoria las raíces exactas ($\sqrt{100}=10, \sqrt{169}=13, \sqrt{196}=14$) te dará una velocidad increíble en los exámenes. ¡A practicar!