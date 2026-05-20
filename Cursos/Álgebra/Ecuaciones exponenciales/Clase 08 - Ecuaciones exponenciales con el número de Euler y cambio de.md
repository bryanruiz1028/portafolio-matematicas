# Clase 08 — Ecuaciones exponenciales con el número de Euler y cambio de variable

tags: #algebra #exponentialequa

Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 8 de 8

```ad-info
title: 🧭 Navegación
- **Anterior**: [[Clase 07 — Ecuaciones con bases diferentes]]
- **Siguiente**: Final del Bloque 2 (Repaso General)
```

---

## ¿Por qué es importante esta clase?

```ad-info
title: 🌍 Relevancia y aplicaciones
El número de Euler ($e$) es la base de los logaritmos naturales y es fundamental para describir procesos de crecimiento continuo en la naturaleza. Su valor irracional permite modelar con precisión cambios instantáneos que ocurren sin interrupción.
- **$USD**: Cálculo del interés compuesto continuo para determinar el crecimiento de capitales financieros en el tiempo.
- **Ingeniería**: Análisis de la catenaria (la curva que forman los cables suspendidos) y estabilidad en estructuras complejas.
- **Crecimiento/Enfriamiento**: Modelado de la expansión de poblaciones biológicas y la ley de enfriamiento de Newton en termodinámica.
```

---

## Concepto clave

```ad-note
title: 📌 ¿Qué es el Número de Euler y el Logaritmo Natural?
El número de Euler ($e \approx 2,718$) es una constante matemática trascendental. La función inversa de la exponencial con base $e$ es el **Logaritmo Natural ($\ln$)**. 

Una propiedad pedagógica esencial es que, cuando la base del logaritmo y el argumento coinciden, el resultado es la unidad. Por lo tanto:
$$\ln(e) = 1$$
Es vital entender que el logaritmo y la base no se "anulan" ni "desaparecen", sino que la expresión **se simplifica a 1**, lo que facilita el despeje de la variable en el exponente.
```

```ad-warning
title: ⚠️ Error común
No utilices el logaritmo común ($\log$ base 10) cuando la ecuación tenga como base el número de Euler. Aunque llegarías al mismo resultado, el proceso es más ineficiente. Al usar $\ln$, aprovechas directamente que $\ln(e) = 1$, ahorrando pasos de conversión.
```

```ad-tip
title: 💡 Truco para recordarlo
Asocia la **"e"** de **Euler** con la **"n"** de **Natural** ($\ln$). Siempre que veas la base $e$ en una ecuación, el Logaritmo Natural será tu mejor herramienta de resolución.
```

---

## Procedimiento paso a paso

Para resolver estas ecuaciones de forma técnica y organizada, sigue este algoritmo:

```text
1. Identificar si las bases son iguales (igualación directa) o si requieren logaritmos.
2. Aplicar Logaritmo Natural (ln) en ambos lados de la igualdad si la base es e.
3. Bajar el exponente multiplicando al logaritmo mediante propiedades de potencias.
4. Despejar la incógnita x (aplicando cambio de variable si la estructura es cuadrática).
```

---

## Ejemplificación práctica

```ad-example
title: Ejemplo 1: Caso Básico (Bases Iguales)
**Resolver:** $e^{x+3} = e^5$

**Razonamiento:**
Dado que las bases son idénticas ($e = e$), aplicamos la propiedad de igualdad: si las bases son iguales, los exponentes deben ser iguales.
1. $x + 3 = 5$
2. $x = 5 - 3$
3. **$x = 2$**

*Validación:* $e^{2+3} = e^5$. La igualdad se cumple perfectamente.
```

```ad-example
title: Ejemplo 2: Caso con Logaritmos y Número de Euler
**Resolver:** $e^{2x+1} = 5$

**Solución:**
1. Aplicamos $\ln$ a ambos lados: $\ln(e^{2x+1}) = \ln(5)$.
2. El exponente baja y recordamos que $\ln(e) = 1$: $(2x + 1) \cdot 1 = \ln(5)$.
3. Despejamos la unidad: $2x = \ln(5) - 1$.
   *Nota pedagógica: Escribimos el "-1" alejado del argumento del logaritmo para evitar confundirlo con $\ln(5-1)$.*
4. Despejamos $x$: $x = \frac{\ln(5) - 1}{2}$.
5. **Resultado aproximado:** $x \approx 0,3047$.
```

```ad-example
title: Ejemplo 3: Caso Avanzado (Cambio de Variable)
**Resolver:** $5^{2x} + 20 = 9(5^x)$

**Solución:**
Este problema presenta una estructura de ecuación cuadrática oculta.
1. Reescribimos: $(5^x)^2 - 9(5^x) + 20 = 0$.
2. Sustituimos $m = 5^x$, obteniendo: $m^2 - 9m + 20 = 0$.
3. Factorizamos el trinomio: $(m - 5)(m - 4) = 0$.
4. Obtenemos dos valores para $m$: $m_1 = 5$ y $m_2 = 4$.
5. Volvemos a la variable original:
   - Para $m_1$: $5^x = 5 \implies \mathbf{x = 1}$.
   - Para $m_2$: $5^x = 4 \implies x = \log_5 4$.
6. **Resultados:** $x = 1$ y $x \approx 0,8613$.
```

```ad-example
title: Ejemplo 4: Aplicación Real ($USD)
Si una inversión inicial de $1000$ crece continuamente a una tasa anual $r$, el monto final tras $t$ años es $A = 1000e^{rt}$. Para hallar el tiempo en que la inversión se duplica ($2000$), resolvemos:
$1000e^{rt} = 2000 \implies e^{rt} = 2$
Aplicando $\ln$: $rt = \ln(2) \implies t = \frac{\ln(2)}{r}$.

**Conclusión técnica:** Si la tasa $r$ fuera del $5\%$ ($0,05$), el tiempo necesario sería $t = \frac{0,6931}{0,05} \approx \mathbf{13,86}$ **años**.
```

---

## Ejercicios para el estudiante

```ad-abstract
title: 🟢 Nivel Verde (Fácil)
1. $e^x = e^2$
2. $e^{x-5} = e^1$
3. $e^{2x} = e^4$
4. $e^{x+1} = e^3$
```

```ad-abstract
title: 🟡 Nivel Amarillo (Medio)
1. $e^x = 5$
2. $e^{3x-2} = 10$
3. $e^{2x-2} = e^{x-1}$
4. $e^{x+3} = 2^{2x-1}$
```

```ad-abstract
title: 🔴 Nivel Rojo (Avanzado - Cambio de Variable)
1. $3^{2x} - 11(3^x) + 18 = 0$
2. $e^{2x} - 5e^x + 6 = 0$
3. $5^{2x} - 6(5^x) + 5 = 0$
4. $2^{2x} - 3(2^x) + 2 = 0$
```

```ad-success
title: Respuestas exactas y aproximadas
- **Verde:** 1) $x=2$; 2) $x=6$; 3) $x=2$; 4) $x=2$.
- **Amarillo:** 1) $x \approx 1,6094$; 2) $x = \frac{\ln(10)+2}{3} \approx 1,4341$; 3) $x=1$; 4) $x \approx -9,56$.
- **Rojo:** 
  1) $x=2$ y $x = \log_3 2 \approx 0,6309$.
  2) $x = \ln 3 \approx 1,0986$ y $x = \ln 2 \approx 0,6931$.
  3) $x=1$ y $x=0$.
  4) $x=1$ y $x=0$.
```

---

## Mini-prueba de autoevaluación

```ad-question
title: Pregunta 1: ¿Cuál es el valor exacto de $\ln(e)$?
- a) 0
- b) $2,718$
- c) **1**
- d) No está definido

**Explicación:** Dado que la base del logaritmo natural es $e$, el logaritmo de la base siempre simplifica a 1.
```

```ad-question
title: Pregunta 2: ¿Cuál es el procedimiento inicial óptimo para $e^x = 7$?
- a) Dividir ambos lados por $e$.
- b) **Aplicar Logaritmo Natural ($\ln$) a ambos lados.**
- c) Aplicar logaritmo común ($\log$) a ambos lados.
- d) Elevar ambos lados a la potencia $e$.

**Explicación:** El $\ln$ permite bajar el exponente $x$ y simplificar la base $e$ de forma inmediata.
```

```ad-question
title: Pregunta 3: En la ecuación $e^{2x} = e^4$, ¿cuál es el valor de $x$?
- a) $x = 4$
- b) $x = 8$
- c) **$x = 2$**
- d) $x = \ln(2)$

**Explicación:** Al tener bases iguales, igualamos los exponentes: $2x = 4$, por lo tanto $x = 2$.
```

---

## Notas para el próximo tema

```ad-tip
title: 💡 En la próxima clase
¡Has finalizado el estudio de las ecuaciones exponenciales! Hemos cubierto desde bases iguales hasta el número de Euler y cambios de variable complejos. En la siguiente sesión, realizaremos un **Repaso General del Bloque 2** para prepararte para la evaluación final del módulo.
```

```ad-info
title: 🧭 Navegación
- **Anterior**: [[Clase 07 — Ecuaciones con bases diferentes]]
- **Siguiente**: Final del Bloque 2 (Repaso General)
```