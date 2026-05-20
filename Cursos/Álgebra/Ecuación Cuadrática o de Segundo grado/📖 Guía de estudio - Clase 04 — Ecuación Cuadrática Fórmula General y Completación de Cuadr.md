# 📖 Guía de estudio — Clase 04: Ecuación Cuadrática por Fórmula General

> [!info] 📌 Conceptos clave
> *   **Igualación a cero:** ¡Es el paso de oro! Antes de tocar la fórmula, asegúrate de que tu ecuación termine en $= 0$. Si hay términos a la derecha, pásalos al lado izquierdo cambiando su signo.
> *   **Identificación de coeficientes:** Debes extraer los valores de $a$, $b$ y $c$ respetando siempre el signo que los acompaña. ¡Un signo olvidado cambia todo el camino!
> *   **Naturaleza de las soluciones:** No te asustes si la raíz no es exacta; en la vida real y en finanzas, los resultados suelen ser decimales. En esta guía, aproximaremos siempre a **tres cifras decimales**.
> *   **Reducción previa:** Si ves paréntesis o términos semejantes, primero "limpia" la ecuación resolviendo las operaciones hasta llegar a la forma estándar.

---

## 1. FÓRMULAS Y DEFINICIONES IMPORTANTES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Forma Estándar** | $ax^2 + bx + c = 0$ |
| **Fórmula General** | $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ |
| **Coeficientes** | **$a$**: número junto a $x^2$.<br>**$b$**: número junto a $x$.<br>**$c$**: término independiente (el número solo).<br>**Nota: ¡Debes incluirlos siempre con su signo!** |

---

## 2. EJEMPLOS RESUELTOS ADICIONALES

```ad-example
title: Ejemplo A — Caso con raíz no exacta
**Ecuación:** $3x^2 + 5x + 1 = 0$

**Paso 1: Identificar coeficientes**
$a = 3$, $b = 5$, $c = 1$.

**Paso 2: Sustitución en la fórmula**
$x = \frac{-(5) \pm \sqrt{(5)^2 - 4(3)(1)}}{2(3)}$

**Paso 3: Operación aritmética**
$x = \frac{-5 \pm \sqrt{25 - 12}}{6} \rightarrow x = \frac{-5 \pm \sqrt{13}}{6}$

¡No te preocupes! Como la $\sqrt{13}$ no es exacta ($\approx 3.606$ si redondeamos, pero usaremos los valores finales del Profe Alex), separamos las soluciones:

*   **Sub-paso para $x_1$:** $x_1 = \frac{-5 + 3.6055...}{6} \approx -0.232$
*   **Sub-paso para $x_2$:** $x_2 = \frac{-5 - 3.6055...}{6} \approx -1.434$

**Resultado:** Las soluciones son $x_1 \approx -0.232$ y $x_2 \approx -1.434$.
```

```ad-example
title: Ejemplo B — Aplicación en finanzas cotidianas $USD
**Contexto:** Un estudiante emprendedor quiere saber cuántas unidades ($x$) de un producto debe vender para que su pérdida sea cero. Su balance financiero se modela con: $x^2 - 5x - 8 = 0$.

**Planteamiento:**
Identificamos: $a = 1, b = -5, c = -8$.

**Resolución:**
$x = \frac{-(-5) \pm \sqrt{(-5)^2 - 4(1)(-8)}}{2(1)}$
$x = \frac{5 \pm \sqrt{25 + 32}}{2} \rightarrow x = \frac{5 \pm \sqrt{57}}{2}$

Calculamos la raíz con precisión: $\sqrt{57} \approx 7.550$ (redondeado de 7.5498).
*   $x_1 = \frac{5 + 7.550}{2} = \frac{12.550}{2} = 6.275$
*   $x_2 = \frac{5 - 7.550}{2} = \frac{-2.550}{2} = -1.275$

**Resultado final:**
¡Tú puedes analizar el contexto! Como no puedes vender "unidades negativas", descartamos el valor negativo. El estudiante debe vender aproximadamente **6.275 unidades** para que su balance sea cero. ✅
```

---

## 3. EJERCICIOS DE REPASO

```ad-abstract
title: 🟢 Fácil
Identifica $a, b, c$ y aplica la fórmula directamente:
1. $x^2 + 4x - 3 = 0$
2. $x^2 + 3x - 5 = 0$
3. $2x^2 - x - 5 = 0$
```

```ad-abstract
title: 🟡 Medio
¡Atención! Primero expande los paréntesis e iguala a cero antes de usar la fórmula:
1. $(x+2)(x-5) = 10$ (Multiplica primero y traslada el 10).
2. $(2x+4)(2x-3) = x(x-1) - 4$
3. $x^2 + 3x = 4$
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
Usa el truco del MCM para eliminar denominadores. ¡No dejes que las fracciones te detengan!
1. **Balance Escolar:** $\frac{1}{15}x^2 - \frac{1}{5}x - \frac{2}{3} = 0$. ¿En qué punto el balance es cero? *(Pista: El MCM es 15).*
2. **Equilibrio Financiero:** $\frac{1}{5}x^2 - \frac{1}{2}x - \frac{3}{10} = 0$. Calcula el valor de $x$. *(Pista: El MCM es 10).*
3. **Ganancia Neta:** $8x^2 + 26x - 2 = 0$. Si $x$ es el tiempo en meses, ¿cuándo la ganancia es nula?
```

---

> [!tip] 💡 Consejo de estudio
> Para dominar la fórmula general como un experto, aplica la estrategia del **Profe Alex**:
> 1. **Escribe la fórmula en cada ejercicio:** No intentes ahorrar tiempo saltándote este paso. Escribirla y **recitarla en voz alta** mientras lo haces grabará el proceso en tu memoria a largo plazo.
> 2. **Verifica tus resultados:** ¡No te quedes con la duda! Sustituye el valor de $x$ que obtuviste en la ecuación original. Si el resultado es cero (o muy cercano a cero por los decimales), ¡celebra porque lo lograste!