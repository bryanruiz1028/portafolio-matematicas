# 📖 Guía de estudio — Clase 02: Cuadrado de un binomio

> [!info] 📌 Conceptos clave
> 1.  **El Trinomio Cuadrado Perfecto (TCP):** Al elevar un binomio al cuadrado, el resultado siempre es un trinomio compuesto por: el cuadrado del primer término, más o menos el doble producto del primero por el segundo, más el cuadrado del segundo término.
> 2.  **Fracciones al cuadrado:** Al elevar una fracción a una potencia, la regla dicta que el exponente afecta tanto al numerador como al denominador de forma independiente (ej. $(\frac{a}{b})^2 = \frac{a^2}{b^2}$).
> 3.  **Potencia de una potencia:** Si un término con exponente se eleva al cuadrado, se aplica la ley de exponentes mediante la multiplicación de los mismos (ej. $(x^n)^2 = x^{n \cdot 2}$).
> 4.  **Binomios con doble signo negativo:** En casos como $(-a - b)^2$, el resultado será completamente positivo. Esto ocurre porque el cuadrado de cualquier cantidad negativa es positivo, y el "doble producto" de dos números negativos también resulta en un valor positivo por la ley de signos, comportándose igual que $(a + b)^2$.

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Primer término al cuadrado** | $a^2$ |
| **Doble producto** | $\pm 2ab$ (El signo depende del operador central del binomio original). |
| **Segundo término al cuadrado** | $b^2$ (Siempre resulta en un valor positivo). |

---

## Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A — Caso con fracciones y potencias
**Desarrollo del binomio:** $(\frac{3}{4}x^3 + \frac{2}{3}y^2)^2$

*   **Paso 1: Elevar el primer término al cuadrado.**
    $(\frac{3}{4}x^3)^2 = \frac{9}{16}x^6$
    *(Elevamos $3^2$ y $4^2$, y multiplicamos los exponentes de la $x$: $3 \times 2 = 6$)*.

*   **Paso 2: Doble producto del primero por el segundo.**
    $2 \cdot (\frac{3}{4}x^3) \cdot (\frac{2}{3}y^2)$
    Operando coeficientes: $\frac{2}{1} \cdot \frac{3}{4} \cdot \frac{2}{3} = \frac{12}{12} = 1$.
    En álgebra, el coeficiente $1$ suele omitirse por elegancia, dejando el término como: $x^3y^2$.

*   **Paso 3: Elevar el segundo término al cuadrado.**
    $(\frac{2}{3}y^2)^2 = \frac{4}{9}y^4$
    *(Elevamos $2^2$ y $3^2$, y multiplicamos los exponentes de la $y$: $2 \times 2 = 4$)*.

**Resultado (TCP):** $\frac{9}{16}x^6 + x^3y^2 + \frac{4}{9}y^4$
```

```ad-example
title: Ejemplo B — Aplicación de área y costos ($USD)
**Enunciado:** Determine el costo total de un terreno cuadrado cuyo lado mide $(x + 5)$ metros, considerando que el precio por metro cuadrado es de $1 USD.

**Solución:**
Primero, obtenemos el área del terreno (lado al cuadrado):
$(x + 5)^2 = x^2 + 2(x)(5) + 5^2 = x^2 + 10x + 25$

Multiplicando el área por el valor unitario ($1 USD), obtenemos la expresión monetaria:
**Costo total:** $(x^2 + 10x + 25)$ USD
```

---

## Ejercicios de Repaso

Recuerda que, conforme ganes confianza, el objetivo es **saltarse los pasos intermedios** para escribir el resultado de forma directa.

```ad-abstract
title: Bloque 🟢 Fácil
1. $(x + 2)^2$
2. $(2m + n)^2$
3. $(a + 3b)^2$
```

```ad-abstract
title: Bloque 🟡 Medio
1. $(\frac{1}{3} - \frac{5}{2}m^2n^3)^2$
2. $(\frac{x}{2} + \frac{3}{4}y^2)^2$
3. $(\frac{2}{5}a^2 - \frac{1}{2}b)^2$
```

```ad-abstract
title: Bloque 🔴 Avanzado
1. $(-6x - 7yz)^2$
2. Calcule el costo total en USD de una superficie cuadrada de lado $(2x + 10)$ metros, con un valor de $1 USD por metro cuadrado. 
   *(Resultado esperado: $(4x^2 + 40x + 100)$ USD)*.
```

---

## Cierre y Consejo

> [!tip] 💡 Consejo de estudio
> Para simplificar el cálculo del **término central** cuando trabajes con fracciones, aplica la estrategia del "Profe Alex": simplifica antes de multiplicar. En el producto $2 \cdot \frac{3}{2} \cdot \frac{5}{4}$, puedes cancelar el $2$ del numerador con el $2$ del denominador inmediatamente. Esto evita trabajar con números innecesariamente grandes y reduce drásticamente la posibilidad de cometer errores aritméticos. ¡La maestría está en la simplificación!