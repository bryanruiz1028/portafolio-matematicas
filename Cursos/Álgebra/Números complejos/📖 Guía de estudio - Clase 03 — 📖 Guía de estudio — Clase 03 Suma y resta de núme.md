# 📖 Guía de estudio — Clase 03: Suma y resta de números complejos

> [!info] 📌 Conceptos clave
> Para dominar los números complejos, debemos verlos como un equipo de dos componentes que nunca se mezclan entre sí. Aquí los pilares fundamentales:
> 1. **Estructura Binómica:** Todo número complejo tiene una **parte real** (un número puro) y una **parte imaginaria** (acompañada de la unidad $i$).
> 2. **La Regla de Oro:** Al operar, solo sumamos "peras con peras" y "manzanas con manzanas". Es decir, partes reales con reales e imaginarias con imaginarias.
> 3. **El concepto de "Opuesto":** En la resta, el signo menos fuera del paréntesis actúa como un interruptor: cambia el signo de **toda** la parte real y de **toda** la parte imaginaria que tiene delante.
> 4. **Precisión de Signos:** La mayoría de los errores ocurren por descuidos en los signos. ¡Mantén la concentración al agrupar!

---

## 2. FÓRMULAS Y DEFINICIONES IMPORTANTES

| Término | Definición / Fórmula | Nota Pedagógica |
| :--- | :--- | :--- |
| **Suma de complejos** | $(a + bi) + (c + di) = (a + c) + (bi + di)$ | Agrupamos términos semejantes antes de resolver. |
| **Resta (El Opuesto)** | $-(a + bi) = -a - bi$ | El negativo se distribuye: multiplica a ambos términos del paréntesis. |
| **Parte Real vs. Imaginaria** | En $3 + 4i$: Real = $3$, Imaginaria = $4i$ | La parte real es independiente; la imaginaria siempre lleva la $i$. |
| **Suma de Fracciones** | $\frac{a}{b} + \frac{c}{d} = \frac{(a \cdot d) + (b \cdot c)}{b \cdot d}$ | Usa el método de la "carita feliz" o busca un denominador común (amplificación). |

---

## 3. EJEMPLOS RESUELTOS ADICIONALES

```ad-example
title: Ejemplo A — Suma básica
**Problema:** Realizar la suma de $Z_1 = 3 + 4i$ y $Z_2 = 7 - 4i$.

**Procedimiento paso a paso:**
1. **Plantear la operación:** $(3 + 4i) + (7 - 4i)$.
2. **Quitar paréntesis:** En la suma, los signos internos no cambian: $3 + 4i + 7 - 4i$.
3. **Agrupar según la Regla de Oro:** $(3 + 7) + (4i - 4i)$.
4. **Resolver:** 
   * Parte Real: $3 + 7 = 10$.
   * Parte Imaginaria: $4i - 4i = 0i$.
5. **Resultado final:** $10$. 
*(Nota: Cuando la parte imaginaria es cero, el resultado es un número real puro).*
```

```ad-example
title: Ejemplo B — Saldo contable en $USD
**Contexto:** Imagina tu cuenta bancaria. La **parte real** es tu dinero en efectivo ($USD) y la **parte imaginaria ($i$)** es una inversión en criptomonedas.
Si tienes un estado de cuenta de $Z_1 = 3 + 4i$ y debes **restar** un gasto representado por $Z_2 = 7 - 4i$:

**Procedimiento:**
1. **Operación:** $(3 + 4i) - (7 - 4i)$.
2. **Aplicar el opuesto:** El signo menos cambia a los dos términos de $Z_2$: 
   $3 + 4i - 7 + 4i$.
3. **Agrupar para el balance:**
   * **Saldo real ($USD):** $(3 - 7) = -4$ (Tienes una deuda de 4 dólares).
   * **Inversión variable ($i$):** $(4i + 4i) = 8i$ (Tu inversión creció).
4. **Resultado:** Tu estado financiero final es $-4 + 8i$.
```

---

## 4. EJERCICIOS DE REPASO

```ad-abstract
title: 🟢 Nivel Fácil: Suma Directa
Aplica la Regla de Oro para resolver estas sumas:
1. $(8 - 6i) + (3 + 6i)$
2. $(-3 + 4i) + (8 - 6i)$
3. $(7 + 4i) + (-6 - 8i)$
```

```ad-abstract
title: 🟡 Nivel Medio: Resta y el Opuesto
Recuerda cambiar los signos del segundo paréntesis antes de agrupar:
1. $(10 - 2i) - (5 + 3i)$
2. $(7 - 4i) - (-2 - 5i)$
3. $(-6 + 8i) - (4 - 8i)$
```

```ad-abstract
title: 🔴 Nivel Avanzado: Transacciones en $USD
Calcula el balance final de esta operación combinada de tres movimientos financieros:
**Operación:** $Z_1 - Z_2 + Z_3$
Donde:
*   $Z_1 = 3 + 4i$ (Saldo inicial)
*   $Z_2 = 7 - 4i$ (Gasto a restar)
*   $Z_3 = \frac{1}{5} - \frac{3}{2}i$ (Ajuste de inversión con fracciones)

**Pista:** Para las fracciones, busca el común denominador (10) o usa el método de la carita feliz para operarlas con los números enteros.
```

---

## 5. CONSEJO DE ESTUDIO

> [!tip] 💡 Consejo de estudio: ¡Usa colores!
> Como recomienda el **profe Alex**, la clave del éxito es el orden visual. Antes de operar, utiliza dos colores diferentes para identificar a cada equipo:
> *   Subraya con **ROJO** todas las partes reales (los números que están solos).
> *   Subraya con **AZUL** todas las partes imaginarias (los que tienen la $i$).
> Esto evitará que cometas el error común de sumar un número real con uno imaginario por accidente. ¡Primero visualiza, luego opera!