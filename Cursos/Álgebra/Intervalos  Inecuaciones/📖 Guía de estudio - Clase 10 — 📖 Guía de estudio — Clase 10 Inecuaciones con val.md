# 📖 Guía de estudio — Clase 10: Inecuaciones con valor absoluto

> [!info] 📌 Conceptos clave
> - **Definición de Valor Absoluto:** Se interpreta como la distancia de un número respecto al cero en la recta numérica. Matemáticamente, consiste en considerar el valor numérico sin su signo (siempre resultando en un valor no negativo).
> - **Comportamiento del símbolo:** La estrategia de resolución cambia según el símbolo. El "menor que" ($<$) busca valores cercanos al origen (dentro de un límite), mientras que el "mayor que" ($>$) busca valores alejados hacia los extremos.
> - **Condición de la constante:** Para aplicar las fórmulas de resolución, la constante $a$ debe ser positiva. Si es negativa, se aplica la lógica de distancias: una distancia nunca puede ser menor que un número negativo.
> - **Interpretación de resultados:** Las soluciones representan conjuntos de números que se expresan mediante intervalos o representaciones gráficas en la recta real.

## Fórmulas y definiciones importantes

| Concepto | Definición / Fórmula |
| :--- | :--- |
| **Valor Absoluto ($|x|$)** | Representa la distancia al origen o el valor numérico sin signo. |
| **Caso "Menor que" ($|x| < a$)** | Se resuelve con la estructura: $-a < x < a$. |
| **Caso "Mayor que" ($|x| > a$)** | Se descompone en la unión de dos desigualdades independientes: $x < -a$ o $x > a$. |
| **Caso con Negativos** | Si $|x| < -a \Rightarrow \emptyset$ (Sin solución, pues una distancia no es negativa); Si $|x| > -a \Rightarrow \mathbb{R}$. |

---

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A (Caso Básico)
**Resolver:** $|x - 3| \leq 12$

1. **Transformación:** Aplicamos la fórmula para "menor o igual que", situando la expresión central entre el valor negativo y positivo de la constante:
$$-12 \leq x - 3 \leq 12$$

2. **Despeje:** Para aislar la $x$, el $3$ que está restando pasa a sumar a ambos lados de la inecuación (método de Profe Alex):
$$-12 + 3 \leq x \leq 12 + 3$$
$$-9 \leq x \leq 15$$

3. **Resultado:** La solución comprende todos los números entre $-9$ y $15$, incluyendo los extremos.
**Intervalo:** $[-9, 15]$
```

```ad-example
title: Ejemplo B (Aplicación Real en USD)
**Escenario:** El saldo de una cuenta bancaria debe mantenerse en un rango de error de $10 \text{ USD}$ respecto a un objetivo de $50 \text{ USD}$.

1. **Planteamiento:** $|x - 50| \leq 10$

2. **Pasos de resolución:**
   - Estructura: $-10 \leq x - 50 \leq 10$
   - Despeje (sumar $50$ en todos los sectores): $50 - 10 \leq x \leq 10 + 50$
   - Simplificación: $40 \leq x \leq 60$

**✅ Resultado:** El rango de dinero permitido es **$40 \text{ USD} \leq x \leq 60 \text{ USD}$**.
```

---

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
Resuelva las siguientes inecuaciones básicas y determine su intervalo:
1. $|x| \geq 8$
2. $|x| > \frac{2}{3}$
3. $|x| < 5$
```

```ad-abstract
title: 🟡 Medio
Resuelva los siguientes ejercicios realizando los despejes algebraicos necesarios:
1. $|2x - 3| < 7$
2. $|x + 5| \leq 10$
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con USD
1. **Problema aplicado:** Una billetera digital permite un error de saldo de $|x - 100| \leq 15$. ¿Cuál es el rango de dinero en $USD$ permitido?
2. **Desafío algebraico:** Resuelva $|-2x + 4| < 10$. 
*Pista: Al despejar $-2x$, fíjate en el cambio de orientación de los signos de desigualdad al dividir por un número negativo.*
```

---

> [!tip] 💡 Consejo de estudio
> Utiliza la estrategia de **visualización gráfica**: si la inecuación usa "menor que" ($<$), los números están "atrapados" **entre** los límites. Si usa "mayor que" ($>$), los números "escapan" hacia los **extremos**. 
> 
> **Nota sobre intervalos:** No olvides que los corchetes $[ \ ]$ indican que el número se incluye (intervalo cerrado), mientras que los paréntesis $( \ )$ indican que el número no forma parte de la solución (intervalo abierto).