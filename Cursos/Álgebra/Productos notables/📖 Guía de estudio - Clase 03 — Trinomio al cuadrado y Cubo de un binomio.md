# 📖 Guía de estudio — Clase 03: Trinomio al cuadrado

> [!info] 📌 Conceptos clave
> El **trinomio al cuadrado** es un **producto notable** que nos permite obtener el resultado de multiplicar un trinomio por sí mismo sin necesidad de realizar la multiplicación larga término a término.
> 1. **Definición:** Elevar $(a + b + c)^2$ es equivalente a $(a + b + c) \cdot (a + b + c)$.
> 2. **La regla de los 6 términos:** El desarrollo de un trinomio al cuadrado siempre consta de **6 términos** antes de cualquier simplificación.
> 3. **Procedimiento:** Se eleva cada término al cuadrado (siempre resultan positivos) y se suma el doble producto de todas las combinaciones de parejas posibles.
> 4. **Orden Alfabético:** Para un resultado profesional y organizado, el Profe Alex recomienda siempre escribir las variables de cada término en orden alfabético (ej. $xy$ en lugar de $yx$).
> 5. **Ley de Signos:** Mientras que los cuadrados son siempre positivos, el signo de los dobles productos dependerá de la multiplicación de los términos originales (ej. $+ \cdot - = -$ o $- \cdot - = +$).

## Fórmulas y definiciones importantes

| Componente | Fórmula / Definición | Tip del Profe Alex |
| :--- | :--- | :--- |
| **Fórmula General** | $(a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2ac + 2bc$ | Memoriza la estructura: "Tres cuadrados y tres dobles". |
| **Cuadrados** | $a^2, b^2, c^2$ | No importa el signo original, el cuadrado **siempre es positivo**. |
| **Dobles productos** | $2(ab), 2(ac), 2(bc)$ | Multiplica la pareja, luego duplica el resultado. ¡Cuidado con los signos! |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Caso básico con coeficientes simples
**Desarrollo de:** $(x + y + 3)^2$

- **Paso 1: Elevar cada término al cuadrado**
  - $(x)^2 = x^2$
  - $(y)^2 = y^2$
  - $(3)^2 = 9$

- **Paso 2: Obtener los dobles productos de las parejas**
  - Doble del 1ro por el 2do: $2 \cdot (x \cdot y) = 2xy$
  - Doble del 1ro por el 3ro: $2 \cdot (x \cdot 3) = 6x$
  - Doble del 2do por el 3ro: $2 \cdot (y \cdot 3) = 6y$

- ✅ **Resultado final:** $x^2 + y^2 + 9 + 2xy + 6x + 6y$
```

```ad-example
title: Ejemplo B — Aplicación con contexto financiero $USD
**Problema:** Un analista define el costo total ($C$) de un proyecto como la suma de tres rubros: $2m$, $3n$ y $5$ USD. Si el factor de riesgo se calcula como el costo al cuadrado ($C^2$), ¿cuál es la expresión resultante?

- **Paso 1: Cuadrado de los términos (siempre positivos)**
  - $(2m)^2 = 4m^2$
  - $(3n)^2 = 9n^2$
  - $(5)^2 = 25$

- **Paso 2: Dobles productos (aplicando duplicación)**
  - $2 \cdot (2m \cdot 3n) = 2 \cdot (6mn) = 12mn$
  - $2 \cdot (2m \cdot 5) = 2 \cdot (10m) = 20m$
  - $2 \cdot (3n \cdot 5) = 2 \cdot (15n) = 30n$

- ✅ **Resultado:** La expresión del riesgo es $4m^2 + 9n^2 + 25 + 12mn + 20m + 30n$ USD.
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil — Términos positivos
Desarrolla aplicando la metodología de parejas y el conteo de 6 términos:
1. $(x + n + 4)^2$
2. $(a + b + 2)^2$
3. $(y + z + 1)^2$
```

```ad-abstract
title: 🟡 Medio — Manejo de signos negativos
Atención: Recuerda que $(- \times - = +)$ en los dobles productos.
1. $(3x - 2y - 5)^2$ (Signos: $+ , - , -$)
2. $(m - n + 3)^2$ (Signos: $+ , - , +$)
3. $(-a - b - c)^2$ (Signos: $- , - , -$)
```

```ad-abstract
title: 🔴 Avanzado — Aplicación compleja $USD
**Contexto:** Calcula el cuadrado de la siguiente función de costos variables: $(5a^2 + 3b^3 - ab)^2$.

**Guía de resolución:**
1. **Cuadrados:** Aplicar potencia de una potencia (multiplicar exponentes).
   - $(5a^2)^2 = 25a^4$
   - $(3b^3)^2 = 9b^6$
   - $(-ab)^2 = a^2b^2$
2. **Dobles Productos:** Sumar exponentes al multiplicar variables iguales (ej. $b^3 \cdot b = b^4$).
   - $2(5a^2)(3b^3) = 30a^2b^3$
   - $2(5a^2)(-ab) = -10a^3b$
   - $2(3b^3)(-ab) = -6ab^4$

- ✅ **Resultado esperado:** $25a^4 + 9b^6 + a^2b^2 + 30a^2b^3 - 10a^3b - 6ab^4$
```

> [!tip] 💡 Consejo de estudio del Profe Alex
> Para saber si tu ejercicio está bien, realiza siempre estas tres verificaciones:
> 1. **¿Hay 6 términos?** Si te faltan o sobran, revisa las parejas.
> 2. **¿Los tres cuadrados son positivos?** Si pusiste un signo menos en $a^2, b^2$ o $c^2$, está incorrecto.
> 3. **¿Está en orden alfabético?** Asegúrate de escribir $ab, ac, bc$ para mantener la claridad matemática. Al multiplicar $b^3 \cdot b$, recuerda que los exponentes se suman: $3 + 1 = 4$.