# 📖 Guía de estudio — Clase 04: Cubo de un binomio

> [!info] 📌 Conceptos clave
> Para dominar este producto notable, es fundamental comprender los siguientes puntos basados en la metodología del Profe Alex:
> 1. **Definición y condición:** El cubo de un binomio es una expresión formada por dos términos sumados o restados, elevados a la potencia 3. Para aplicar esta regla, es obligatorio que existan exactamente **dos términos** y un **exponente 3**.
> 2. **Diferencia de signos:** 
>    - En la suma $$(a+b)^3$$, todos los términos resultantes son positivos.
>    - En la resta $$(a-b)^3$$, los signos se presentan **intercalados**, comenzando siempre con positivo: $$(+, -, +, -)$$.
> 3. **Estructura del resultado:** El desarrollo siempre genera un polinomio de **cuatro términos**. Los coeficientes numéricos (1, 3, 3, 1) no son arbitrarios; provienen de la cuarta fila del **Triángulo de Pascal**.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Cubo de la Suma** | $$(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$$ |
| **Cubo de la Diferencia** | $$(a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$$ |
| **Regla de Exponentes** | El exponente del primer término disminuye $$(a^3, a^2, a^1, a^0)$$ mientras el del segundo aumenta $$(b^0, b^1, b^2, b^3)$$. |
| **Potencia de una Potencia** | Si un término ya tiene exponente, se deben multiplicar los exponentes: $$(a^n)^m = a^{n \cdot m}$$. |

> [!warning] ⚠️ ¡Cuidado con los coeficientes!
> Un error común es multiplicar el coeficiente por el exponente (ej. $$2 \cdot 3 = 6$$). Recuerda que el coeficiente también se debe elevar al cubo: $$2^3 = 2 \cdot 2 \cdot 2 = 8$$.

---

## Ejemplos resueltos

```ad-example
title: Ejemplo A — Caso básico con suma
**Ejercicio:** Resolver $$(x + 5)^3$$

- **Paso 1: Plantear la estructura.**
  $$(x)^3 + 3(x)^2(5) + 3(x)(5)^2 + (5)^3$$
- **Paso 2: Resolver potencias.** Calculamos $$5^2$$ y $$5^3$$.
  $$x^3 + 3(x^2)(5) + 3(x)(25) + 125$$
- **Paso 3: Resolver multiplicaciones finales.**
  $$x^3 + (3 \cdot 5)x^2 + (3 \cdot 25)x + 125$$
✅ **Resultado:** $$x^3 + 15x^2 + 75x + 125$$
```

```ad-example
title: Ejemplo B — Aplicación de volumen y costo $USD
**Enunciado:** Un depósito cúbico tiene una arista que mide $$(x + 2)$$ metros. Si el costo de revestimiento es de $$3 \text{ USD}$$ por metro cúbico, determine la expresión del volumen y el costo total.

- **Paso 1: Desarrollar el volumen.** Elevamos la arista al cubo:
  $$V = (x + 2)^3$$
  $$V = (x)^3 + 3(x^2)(2) + 3(x)(2^2) + (2)^3$$
- **Paso 2: Resolver potencias y productos intermedios.**
  $$V = x^3 + 3(x^2)(2) + 3(x)(4) + 8$$
  $$V = x^3 + 6x^2 + 12x + 8$$
- **Paso 3: Calcular el costo total.** Multiplicamos el polinomio resultante por $$3$$.
  $$\text{Costo} = 3 \cdot (x^3 + 6x^2 + 12x + 8)$$
✅ **Resultado:** $$3x^3 + 18x^2 + 36x + 24$$ (Expresión final en $$USD$$).
```

---

## Ejercicios de repaso

¡Ahora es tu turno! Aplica lo aprendido en los siguientes niveles de dificultad:

```ad-abstract
title: 🟢 Fácil — Aplicación directa
1. $$(m + 3)^3$$
2. $$(y - 1)^3$$
3. $$(a + 4)^3$$
```

```ad-abstract
title: 🟡 Medio — Coeficientes y variables múltiples
1. $$(2x + 3)^3$$
2. $$(2xy + 3)^3$$
3. $$(3a^2 - 2b)^3$$
```

```ad-abstract
title: 🔴 Avanzado — Razonamiento y potencias
1. Un cubo de madera tiene aristas de $$(2x^2y + 1)$$ cm. Calcule el volumen.
2. Si el precio de un activo financiero se comporta según la función $$(x - 4)^3$$, desarrolle la expresión polinómica.
3. El costo de materiales para un proyecto arquitectónico está dado por $$(3x + 2)^3$$. Desarrolle el polinomio final.
```

> [!tip] 💡 Consejo de estudio del Profe Alex
> Para verificar que tu resultado es correcto, revisa dos cosas:
> 1. **Orden de exponentes:** Los exponentes de la primera variable deben disminuir $$(3, 2, 1, 0)$$ y los de la segunda aumentar.
> 2. **Términos no semejantes:** Al finalizar, deberás tener exactamente **cuatro términos** que no se pueden sumar ni restar entre sí. Si puedes simplificar más, algo falló en el procedimiento.