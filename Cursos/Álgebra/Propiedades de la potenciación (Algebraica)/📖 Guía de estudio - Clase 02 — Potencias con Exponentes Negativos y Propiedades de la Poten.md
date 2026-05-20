# 📖 Guía de estudio — Clase 02: Potencias con exponente negativo

## 1. Resumen inicial

> [!info] 📌 Conceptos clave
> - **Imposibilidad operativa:** No podemos multiplicar una base por sí misma una cantidad negativa de veces. El exponente negativo es, en realidad, un "indicador de ubicación" que nos avisa que la potencia pertenece al lado opuesto de la fracción.
> - **Origen lógico:** Un exponente negativo surge de un cociente donde el exponente del denominador es mayor que el del numerador (ej. $a^2 / a^5 = a^{2-5} = a^{-3}$).
> - **Regla de inversión:** Para convertir un exponente negativo en positivo, movemos la potencia: si está arriba, pasa al denominador; si está abajo, sube al numerador. En fracciones: $\left( \frac{a}{b} \right)^{-n} = \left( \frac{b}{a} \right)^n$.
> - **Restricción crítica ($a \neq 0$):** La base nunca puede ser cero ($0$) si el exponente es negativo, ya que esto implicaría una división por cero, la cual no está definida.

---

## 2. Tabla de fórmulas y definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Potencia con exponente negativo** | Indica que la base es un divisor: $a^{-n} = \frac{1}{a^n}$. También aplica a la inversa: $\frac{1}{a^{-n}} = a^n$. |
| **Inversión de fracción** | Para eliminar el negativo, se intercambian los términos: $\left( \frac{a}{b} \right)^{-n} = \left( \frac{b}{a} \right)^n$. |
| **Exponente cero (El "Porqué")** | Es el paso intermedio de la demostración: $a^{-n} = a^{0-n} = \frac{a^0}{a^n} = \frac{1}{a^n}$. Recordando que $a^0 = 1$. |
| **Potencia de una potencia** | Los exponentes se multiplican: $\left( a^m \right)^n = a^{m \cdot n}$. Es vital respetar la ley de signos (ej. negativo por negativo es positivo). |

---

## 3. Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A: Conversión de base entera y su lógica
**Problema:** Expresar $x^{-4}$ con exponente positivo y resolver $5^{-3}$.

**Paso a paso:**
1. **Lógica de origen:** Imagina que $5^{-3}$ proviene de la resta $5^{0-3}$. Esto equivale a $\frac{5^0}{5^3}$.
2. **Aplicación de la regla:** Como $5^0 = 1$, la expresión se convierte en $\frac{1}{5^3}$.
3. **Resolución de $x^{-4}$:** Siguiendo el mismo principio, movemos la base al denominador: $x^{-4} = \frac{1}{x^4}$.
4. **Cálculo final de $5^{-3}$:** 
   - $\frac{1}{5 \cdot 5 \cdot 5} = \frac{1}{125}$
   - **Resultado:** $x^{-4} = \frac{1}{x^4}$ y $5^{-3} = \frac{1}{125}$.
```

```ad-example
title: Ejemplo B: Aplicación en escalas monetarias ($USD)
**Escenario:** En economía, a veces dividimos potencias de base 10 para expresar cantidades pequeñas. Si dividimos $10^2$ USD entre $10^5$ unidades de medida, ¿cuál es el valor resultante?

**Paso a paso:**
1. **Resta de exponentes:** $10^2 / 10^5 = 10^{2-5} = 10^{-3}$.
2. **Conversión a positivo:** $10^{-3} = \frac{1}{10^3} = \frac{1}{1000}$.
3. **Interpretación visual:** $\frac{1}{1000}$ de un dólar es igual a $0.001$ USD. 
4. **Resultado:** Este valor se conoce como "una milésima de dólar" (equivalente a un décimo de centavo o una mili-unidad).
```

---

## 4. Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel Fácil: Conversión Directa
Escribe las siguientes expresiones utilizando únicamente exponentes positivos:
1. $3^{-2}$
2. $y^{-7}$
3. $\frac{1}{x^{-5}}$ (Pista: ¡Súbelo al numerador!)
```

```ad-abstract
title: 🟡 Nivel Medio: Fracciones y Signos Combinados
Simplifica y elimina los exponentes negativos de los resultados:
1. $\left( \frac{5}{2} \right)^{-3}$
2. $\left( x^{-2} \right)^{-4}$
3. $\left( \frac{a^{-2}}{b} \right)$ (Solo mueve la variable con exponente negativo)
```

```ad-abstract
title: 🔴 Nivel Avanzado: Aplicación de Múltiples Reglas
Resuelve y simplifica totalmente las siguientes expresiones:
1. Simplifica aplicando potencia de una potencia y producto: $\left( y^{-2} \right)^{-5} \cdot y^{-3}$
2. Resuelve la siguiente fracción compleja: $\left( \frac{x^{-2} \cdot y^3}{z^2} \right)^{-2}$
```

---

## 5. Consejo de estudio

> [!tip] 💡 La técnica de la mudanza y el guardián
> Para no confundirte con los signos, piensa que el exponente negativo es una "orden de mudanza". 
> - Si el número está en el **techo** (numerador) con un negativo, "se muda" al **piso de abajo** (denominador) para estar feliz (positivo). 
> - Si se muda y arriba no queda nadie, el número **1** siempre se queda como **guardián** para mantener la estructura de la fracción. 
> - ¡Ojo! Si el número ya es positivo, **no lo muevas**, él ya está en su lugar correcto.