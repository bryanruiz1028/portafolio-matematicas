# 📖 Guía de estudio — Clase 01: División de monomios

> [!info] 📌 Conceptos clave
> Para dominar la división de monomios, es fundamental seguir el orden lógico y las reglas de simplificación explicadas por el Profe Alex:
> 1. **Orden de operación:** Se debe resolver siempre en esta secuencia: **Signos** (ley de signos) $\rightarrow$ **Números** (dividir o simplificar coeficientes) $\rightarrow$ **Letras** (restar exponentes).
> 2. **Regla de los exponentes para bases iguales:** Al dividir variables iguales, se mantiene la base y se **restan** los exponentes: $\frac{x^a}{x^b} = x^{a-b}$.
> 3. **Eliminación o cancelación:** Si el numerador y el denominador tienen términos idénticos (misma base y mismo exponente), estos se "tachan". Si se eliminan todos los términos, el resultado final es $1$.
> 4. **Coeficientes fraccionarios:** Se resuelven mediante la multiplicación de **extremos y medios** (comúnmente llamada "Ley de la oreja").
> 5. **Manejo de exponentes algebraicos:** Cuando los exponentes son binomios (ej. $n+1$), la resta debe escribirse obligatoriamente entre **paréntesis** para aplicar correctamente el cambio de signos.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **División de signos** | Se aplica la ley: $(+) \div (+) = +$; $(-) \div (-) = +$; $(+) \div (-) = -$; $(-) \div (+) = -$. |
| **Cociente de potencias** | $\frac{x^a}{x^b} = x^{a-b}$. Se resta el exponente superior menos el inferior. |
| **Ley de la oreja** | Para dividir $\frac{\frac{a}{b}}{\frac{c}{d}}$, multiplicamos los extremos ($a \cdot d$) para el numerador y los medios ($b \cdot c$) para el denominador. |
| **Eliminación de términos** | Se "tachan" letras cuando $\text{base}$ y $\text{exponente}$ son iguales en ambos niveles (ej. $\frac{y^3}{y^3}$), simplificando el proceso visual. |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Caso con exponentes algebraicos
**Problema:** Resolver la división $\frac{6x^{m+2}}{3x^{m-1}}$

- **Paso 1: Dividir coeficientes.**
  $\frac{6}{3} = 2$.
- **Paso 2: Plantear la resta de los exponentes.**
  Escribimos la base $x$ y restamos el exponente de abajo al de arriba usando paréntesis: $(m+2) - (m-1)$.
- **Paso 3: Simplificar signos y términos.**
  Aplicamos la propiedad distributiva del signo menos: el $-(m-1)$ se convierte en $-m + 1$.
  Operamos: $m + 2 - m + 1$. Aquí, $m - m$ se elimina, y $2 + 1 = 3$.
- **Resultado final:** $2x^3$ ✅
```

```ad-example
title: Ejemplo B — Caso con aplicación real $USD
**Contexto:** El costo total de un lote de memorias USB es de $24x^5 y^2$ dólares. Si se compraron $4x^2 y$ unidades, ¿cuál es el precio por unidad?

- **Proceso:**
  1. **División de coeficientes (dinero):** $\frac{24}{4} = 6$.
  2. **Resta de exponentes (especificaciones):**
     - Para $x$: $5 - 2 = 3$.
     - Para $y$: $2 - 1 = 1$ (el exponente $1$ no se escribe).
- **Resultado:** $6x^3 y$ ✅ (Expresado en $/unidad).
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
1. Resuelve la siguiente división con coeficientes enteros: $\frac{8a^4 b^5}{4a^2 b^2}$.
2. Determina el resultado de $\frac{15x^3 y^4}{15x^3 y^4}$ explicando por qué el resultado es $1$ tras la eliminación total.
3. Divide los siguientes términos con signos opuestos: $\frac{12m^6}{-3m^2}$.
```

```ad-abstract
title: 🟡 Medio
1. Resuelve la división de fracciones $\frac{\frac{3}{4}x^5}{\frac{6}{5}x^2}$. Nota: Debes simplificar la fracción resultante a su mínima expresión.
2. Calcula el cociente con un exponente de variable única: $\frac{x^m}{x^2}$.
3. Resuelve $\frac{10a^3 b^2}{2a^2}$. Nota: Como la letra $b$ no tiene pareja en el denominador, se mantiene idéntica en el resultado.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
1. Desarrolla la siguiente operación compleja: $\frac{\frac{1}{2}x^{n+5}}{\frac{1}{4}x^{n+1}}$.
2. **Costo por área:** Un terreno rectangular tiene un área de $15a^2 b^3$ metros cuadrados. Si el costo total fue de $30a^5 b^7$ USD, ¿cuál es el precio en USD por cada metro cuadrado? (Divide $\frac{\text{Costo}}{\text{Área}}$).
```

> [!tip] 💡 Consejo de estudio
> Siguiendo la metodología del Profe Alex, evita usar el símbolo "$\div$". Escribir siempre la operación en **forma de fracción vertical** ayuda a visualizar qué términos se pueden tachar y facilita la resta de exponentes. Cuando trabajes con binomios en los exponentes, usa **siempre paréntesis** al restar; esto garantiza que el signo negativo afecte a todos los términos internos, evitando el error más común en álgebra.