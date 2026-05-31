# 📖 Guía de estudio — Clase 11: Racionalización de denominadores

> [!info] 📌 Conceptos clave
> *   **El objetivo primordial:** Racionalizar no es "desaparecer" la raíz, sino transformarla. Buscamos que el denominador sea un número racional (sin raíces) multiplicando por un "1 conveniente" que no altere el valor de la fracción.
> *   **La regla de oro del exponente:** Para eliminar una raíz de índice $n$, necesitamos que el exponente de cada factor dentro de la raíz sea exactamente igual a $n$. ¡Pilas! Si te falta algo para llegar al índice, eso es lo que debes completar.
> *   **El poder del conjugado:** En binomios, usamos la diferencia de cuadrados $(a + b)(a - b) = a^2 - b^2$. Esto garantiza que ambos términos se eleven al cuadrado y las raíces se eliminen.
> *   **Estrategia de agrupación:** Cuando enfrentamos trinomios, "engañamos" al ejercicio agrupando dos términos en un paréntesis para tratarlo como si fuera un binomio común. ¡Ojo! Esto suele requerir racionalizar dos veces.

## TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Racionalización de Monomios** | Se multiplica por una raíz del mismo índice donde los exponentes internos sumen exactamente el valor del índice. |
| **Producto de Conjugados** | Técnica clave para binomios: $(a + b)(a - b) = a^2 - b^2$. El signo central cambia para crear la diferencia. |
| **Cuadrado de un Binomio** | Fórmula esencial para expandir términos agrupados: $(a \pm b)^2 = a^2 \pm 2ab + b^2$. ¡No olvides el término central! |
| **Factores Primos** | Antes de empezar, descompón siempre los números grandes. Por ejemplo, $9$ debe escribirse como $3^2$ y $8$ como $2^3$. |

## EJEMPLOS RESUELTOS ADICIONALES

```ad-example
title: Ejemplo A — Racionalización de un monomio
**Ejercicio:** Racionalizar la expresión $\frac{2a}{\sqrt{2ax}}$

1. **Identificar los faltantes:** Dentro de la raíz (índice 2), tenemos $2^1, a^1, x^1$. Para llegar al exponente 2, a cada uno le falta 1.
2. **Multiplicar por el factor complementario:** Multiplicamos numerador y denominador por $\sqrt{2ax}$ (el "1 conveniente").
$$\frac{2a \cdot \sqrt{2ax}}{\sqrt{2ax} \cdot \sqrt{2ax}}$$
3. **Operar el denominador:** Al unir las raíces, sumamos exponentes: $\sqrt{2^2 a^2 x^2}$. Esto permite eliminar la raíz:
$$\frac{2a\sqrt{2ax}}{2ax}$$
4. **Simplificación final:** Como el $2$ y la $a$ están multiplicando tanto arriba como abajo (fuera de la raíz), los podemos simplificar.
**Resultado:** $\frac{\sqrt{2ax}}{x}$
```

```ad-example
title: Ejemplo B — Distribución de presupuesto
**Problema:** Se debe distribuir un presupuesto de $6 USD entre un grupo de trabajo representado por $(\sqrt{2} + \sqrt{3} + \sqrt{5})$. Racionalizar este valor es fundamental para obtener una cifra manejable en contabilidad.

1. **Agrupar para simplificar:** Tratamos los primeros dos términos como uno solo: $[(\sqrt{2} + \sqrt{3}) + \sqrt{5}]$.
2. **Multiplicar por el conjugado:** Usamos el signo opuesto $(-)$.
$$\frac{6 \cdot [(\sqrt{2} + \sqrt{3}) - \sqrt{5}]}{[(\sqrt{2} + \sqrt{3}) + \sqrt{5}] \cdot [(\sqrt{2} + \sqrt{3}) - \sqrt{5}]}$$
3. **Diferencia de cuadrados:** El denominador se vuelve $(\sqrt{2} + \sqrt{3})^2 - (\sqrt{5})^2$.
4. **Desarrollar el binomio:** En el denominador obtenemos $(2 + 2\sqrt{6} + 3) - 5$. Al sumar $2+3-5=0$, el denominador se reduce a $2\sqrt{6}$.
5. **Segunda racionalización:** Tenemos $\frac{6(\sqrt{2} + \sqrt{3} - \sqrt{5})}{2\sqrt{6}}$. Simplificamos $6/2 = 3$ y multiplicamos por $\sqrt{6}/\sqrt{6}$:
$$\frac{3(\sqrt{2} + \sqrt{3} - \sqrt{5}) \cdot \sqrt{6}}{\sqrt{6} \cdot \sqrt{6}} = \frac{3(\sqrt{12} + \sqrt{18} - \sqrt{30})}{6}$$
6. **Resultado final:** Simplificamos $3/6$ a $1/2$ y descomponemos las raíces ($\sqrt{12} = 2\sqrt{3}$ y $\sqrt{18} = 3\sqrt{2}$):
**Resultado:** $\frac{2\sqrt{3} + 3\sqrt{2} - \sqrt{30}}{2}$
```

## EJERCICIOS DE REPASO

```ad-abstract
title: 🟢 Fácil
1. Racionalizar: $\frac{3}{\sqrt[3]{x}}$
2. Racionalizar: $\frac{5}{\sqrt{2a}}$
3. Racionalizar: $\frac{6}{\sqrt[3]{3x}}$. ¡Pilas! El 3 tiene exponente 1, así que debes multiplicar por $\sqrt[3]{3^2 x^2}$ para completar el cubo.
```

```ad-abstract
title: 🟡 Medio
1. Racionalizar: $\frac{2}{\sqrt{5} - \sqrt{3}}$
2. Racionalizar: $\frac{\sqrt{3}}{\sqrt{2} + \sqrt{3}}$
3. Racionalizar: $\frac{3}{2 - \sqrt{3}}$ (Usa el conjugado $2 + \sqrt{3}$ y recuerda que $2^2 = 4$).
```

```ad-abstract
title: 🔴 Avanzado (Aplicación con $USD)
**Problema:** Repartir una donación de $3 USD entre un grupo cuya carga es $(\sqrt{2} - \sqrt{3} - \sqrt{5})$. 
**Pista:** Agrupa como $(\sqrt{2} - \sqrt{3}) - \sqrt{5}$. Tras la primera racionalización, el denominador será $-2\sqrt{6}$. Vuelve a racionalizar por $\sqrt{6}$.
**Resultado esperado:** $\frac{3\sqrt{2} - 2\sqrt{3} - \sqrt{30}}{4}$
```

> [!tip] 💡 Consejo de estudio
> ¡Mucho cuidado con la simplificación! Como advierte el Profe Alex, solo puedes sacar mitad o tercera si **todos** los términos de la expresión lo permiten. Si tienes $\frac{12 - 6\sqrt{3} + 3\sqrt{5}}{22}$, no puedes sacar mitad porque el $3\sqrt{5}$ no tiene mitad exacta. Para simplificar, el factor debe estar fuera de la raíz y ser común en todo el numerador y denominador. Si uno solo falla, ¡no se toca!