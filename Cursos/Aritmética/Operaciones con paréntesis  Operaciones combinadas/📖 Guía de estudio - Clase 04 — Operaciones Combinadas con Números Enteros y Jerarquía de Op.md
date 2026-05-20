# 📖 Guía de estudio — Clase 04: Operaciones combinadas con números enteros

> [!info] 📌 Conceptos clave
> Para resolver correctamente ejercicios con múltiples operaciones, es fundamental seguir la **jerarquía de operaciones**. Este orden no es opcional; es la regla que garantiza que todos lleguemos al mismo resultado:
> 1.  **Paréntesis**: Se resuelven primero todas las operaciones dentro de los signos de agrupación.
> 2.  **Potencias y Raíces**: Se calculan una vez que el interior sea un solo número.
> 3.  **Multiplicación y División**: Tienen la misma prioridad y se realizan antes que las sumas.
> 4.  **Sumas y Restas**: Es el último nivel de la jerarquía.

---

## Tabla de Fórmulas y Definiciones

| Término | Definición / Regla |
| :--- | :--- |
| **Jerarquía de Operaciones** | El orden obligatorio que dicta qué cálculos deben realizarse antes que otros. |
| **Signos de Agrupación** | Uso de **paréntesis** para priorizar operaciones. Deben resolverse hasta que quede un solo número para poder eliminarlos. |
| **Potencias y Raíces** | Se aplican sobre un **solo número**. Si hay operaciones dentro, trátalas como si estuvieran en un "paréntesis oculto" antes de aplicar la raíz o potencia. |
| **Multiplicación Implícita** | Si no hay un signo (como $\times$ o $\cdot$) entre un número y un paréntesis, se asume que es una **multiplicación**. |
| **Bases Negativas** | **¡Cuidado!** $-3^2$ significa $-(3 \times 3) = -9$ (el menos está fuera). En cambio, $(-3)^2$ significa $(-3) \times (-3) = 9$. |

---

## Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A: Caso Básico y la Trampa de la Izquierda
**Operación:** $17 - 5 \times 2 + 3$

1. **Identificar Prioridad:** Tenemos resta, multiplicación y suma. Según la jerarquía, la multiplicación "le gana" a las demás.
2. **Multiplicación:** Resolvemos $5 \times 2 = 10$. La expresión queda: $17 - 10 + 3$.
3. **Sumas y Restas:** Ahora resolvemos en orden: $17 - 10 = 7$, y $7 + 3 = 10$.

**Pedagogía del error:** Muchos fallan al hacer $17 - 5 = 12$ y luego $12 \times 2 = 24$. Esto es incorrecto porque la resta nunca debe hacerse antes que una multiplicación.
**Resultado final:** $10$
```

```ad-example
title: Ejemplo B: Aplicación Real ($USD)
**Contexto:** Un comerciante inicia con dinero y registra sus ventas del día.
**Operación:** $10 + 10 \times 3 + 20 \times 1 + 5 \times 0 + 3$

**Interpretación monetaria:**
*   **$10$**: Dinero inicial.
*   **$10 \times 3$**: 10 productos vendidos a $3 USD cada uno.
*   **$20 \times 1$**: 20 productos vendidos a $1 USD cada uno.
*   **$5 \times 0$**: 5 productos regalados (precio $0 USD).
*   **$3$**: Una moneda extra encontrada.

**Resolución Técnica:**
1. **Multiplicaciones primero:** Debemos saber cuánto dinero entró por cada grupo de ventas *antes* de sumarlo al total. 
   $10 \times 3 = 30$; $20 \times 1 = 20$; $5 \times 0 = 0$.
2. **El efecto del cero:** Nota que $5 \times 0$ es $0$. Esto no afecta al resto de la suma, solo significa que esas 5 ventas no aportaron dinero.
3. **Suma final:** $10 + 30 + 20 + 0 + 3 = 63$.

**Resultado final:** $63$ USD
```

---

## Ejercicios de Repaso

```ad-abstract
title: 🟢 Nivel: Fácil
1. $2 + 3 + 4 \times 0$  *(R: 5)*
2. $5 + 2 \times 3$  *(R: 11)*
3. $10 - 2 \times 4$  *(R: 2)*
```

```ad-abstract
title: 🟡 Nivel: Medio
1. $\sqrt{15 - 3 \times 2} + 5$  *(R: 8)*
2. $3^2 - 4 + 1$  *(R: 6)*
3. $2 \times \sqrt{9} + (-2)^2$  *(R: 10)*
```

```ad-abstract
title: 🔴 Nivel: Avanzado — Modelado con $USD
*Para estos ejercicios, plantea la expresión matemática completa usando paréntesis donde sea necesario antes de resolver.*

1. Tienes $50 USD. Compras 2 camisetas de $15 USD cada una. ¿Cuánto te queda? 
   *(Expresión: $50 - (2 \times 15)$ | R: $20)*
2. Un cliente paga con $100 USD por 3 libros de $20 USD y 2 lapiceros de $5 USD. ¿Cuál es su cambio?
   *(Expresión: $100 - (3 \times 20 + 2 \times 5)$ | R: $30)*
3. En una caja hay 5 billetes de $10 USD y 4 billetes de $5 USD. Si retiras $12 USD, ¿cuánto queda?
   *(Expresión: $(5 \times 10 + 4 \times 5) - 12$ | R: $58)*
```

---

> [!tip] 💡 Consejo de estudio
> ¡No caigas en la trampa de la linealidad! El error más común, incluso en adultos, es resolver de izquierda a derecha como si estuvieras leyendo una oración. En matemáticas, la **multiplicación y división siempre tienen prioridad sobre la suma y resta**. Si ves una operación mixta, detente un segundo, marca las multiplicaciones y resuélvelas primero. ¡Es la clave para no fallar en las "preguntas sencillas"!