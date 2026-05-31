# Clase 01 — ¿Qué son los números imaginarios? + Potencias de $i$ + Suma y Resta

tags: #algebra #numerosimaginarios
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 5

> [!info] 🧭 Navegación
> *   **Índice:** [[00 - Índice del curso]]
> *   **Siguiente Lección:** [[Clase 02 — Introducción a los números complejos]]

---

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> Los números imaginarios permiten resolver ecuaciones que no tienen solución en el conjunto de los números reales, como aquellas que resultan en raíces de números negativos. Históricamente, fueron nombrados por René Descartes y formalizados por Leonhard Euler para expandir los horizontes de la matemática.

*   💵 **Aplicación con $USD:** En modelos de predicción financiera, las deudas cuadráticas o flujos de caja teóricos a veces requieren raíces negativas para equilibrar balances en escenarios de riesgo hipotético, tratando estos valores como una dimensión de análisis separada.
*   🏗️ **Aplicación práctica:** Son fundamentales en ingeniería para describir ondas y corrientes alternas. La unidad imaginaria representa una rotación de $90^\circ$ en el plano, permitiendo modelar fenómenos cíclicos.
*   📊 **Situación cotidiana:** Resolución de acertijos matemáticos avanzados que involucran áreas "imposibles" o dimensiones teóricas donde los números reales son insuficientes.

---

## Concepto clave

> [!note] 📌 ¿Qué son los números imaginarios?
> La unidad imaginaria, representada por la letra $i$, se define como la raíz cuadrada de $-1$ ($i = \sqrt{-1}$). Por lo tanto, por definición, $i^2 = -1$.
> 
> Un número imaginario es el producto de cualquier número real $b$ por la unidad imaginaria $i$ (ejemplo: $3i$, $-5i$, $\sqrt{2}i$).

> [!warning] ⚠️ Error común
> Elevar un número negativo al cuadrado no es lo mismo que la unidad imaginaria. Recuerda que, por definición: $\sqrt{-1} \cdot \sqrt{-1} = -1$. El resultado es un número real negativo, no positivo ($1$).

> [!tip] 💡 Truco para recordarlo: El ciclo de $i$
> Los resultados de las potencias de $i$ se repiten cada cuatro valores. Puedes usar el resto de la división del exponente entre $4$ para saber el resultado:
> - Resto $0 \rightarrow i^0 = 1$
> - Resto $1 \rightarrow i^1 = i$
> - Resto $2 \rightarrow i^2 = -1$
> - Resto $3 \rightarrow i^3 = -i$

---

## Procedimiento paso a paso

Para simplificar raíces negativas, calcular potencias grandes y operar, sigue esta metodología técnica:

```text
PASO 1 → Identificar la raíz negativa y separarla: $\sqrt{-n} = \sqrt{-1} \cdot \sqrt{n}$.
PASO 2 → Sustituir la $\sqrt{-1}$ por la unidad imaginaria $i$.
PASO 3 → Simplificar la raíz del número real (calculando su raíz exacta o usando factores primos).
PASO 4 → Agrupar términos semejantes (sumar/restar coeficientes de términos con la misma raíz e $i$).
PASO 5 → Para potencias grandes ($i^n$), dividir el exponente $n$ entre 4. El resto de la división (0, 1, 2 o 3) será el nuevo exponente simplificado según el ciclo básico.
```

---

## Ejemplos prácticos

```ad-example
title: Ejemplo 1 (Básico): Simplificación de $\sqrt{-36} + \sqrt{-9}$
1. Separamos las raíces: $(\sqrt{-1} \cdot \sqrt{36}) + (\sqrt{-1} \cdot \sqrt{9})$
2. Sustituimos por $i$: $(i \cdot 6) + (i \cdot 3)$
3. Ordenamos: $6i + 3i$
4. Sumamos términos semejantes: **$9i$**
```

```ad-example
title: Ejemplo 2 (Con signos): Operación de $4i - 2\sqrt{-16}$
1. Resolvemos la raíz negativa: $\sqrt{-16} = \sqrt{-1} \cdot \sqrt{16} = 4i$
2. Sustituimos en la expresión: $4i - 2(4i)$
3. Multiplicamos los coeficientes reales: $4i - 8i$
4. Resultado final: **$-4i$**
```

```ad-example
title: Ejemplo 3 (Avanzado): Suma de raíces no exactas $\sqrt{-5} + \sqrt{-45}$
1. Expresamos en términos de $i$: $\sqrt{5}i + \sqrt{45}i$
2. Descomponemos $45$ en factores primos: $45 = 9 \cdot 5$
3. Simplificamos la raíz: $\sqrt{45} = \sqrt{9 \cdot 5} = 3\sqrt{5}$
4. Expresión resultante: $1\sqrt{5}i + 3\sqrt{5}i$
5. Sumamos coeficientes: **$4\sqrt{5}i$**
```

```ad-example
title: Ejemplo 4 (Aplicación $USD): Balance de activos imaginarios
En un modelo predictivo, sumamos dos "pérdidas teóricas" representadas por $\sqrt{-100}$ USD y $\sqrt{-400}$ USD. Al ser valores imaginarios, operan en un vector distinto al capital real.
1. Simplificamos: $\sqrt{-100} = 10i$ y $\sqrt{-400} = 20i$.
2. Sumamos las magnitudes del vector imaginario: $10i + 20i = 30i$.
3. Resultado: La deuda técnica total es de **$30i$ USD**.
```

---

## Ejercicios para el estudiante

```ad-abstract
title: 🟢 Dificultad: Fácil (Potencias y raíces exactas)
1. Calcula $i^{85}$ (Pista: $85 \div 4$ deja resto $1$).
2. Calcula $i^{12}$.
3. Simplifica $\sqrt{-49} + \sqrt{-1}$.
4. Simplifica $\sqrt{-100} - \sqrt{-64}$.
```

```ad-abstract
title: 🟡 Dificultad: Medio (Simplificación y suma)
1. Calcula el resultado de $i^{52} + i^{54}$.
2. Simplifica $\sqrt{-20} + \sqrt{-80}$ (Usa factores primos).
3. Resuelve la expresión $5\sqrt{-9} + 2i$.
4. Resuelve $\sqrt{-18} - \sqrt{-2}$.
```

```ad-abstract
title: 🔴 Dificultad: Avanzado ($USD y operaciones combinadas)
1. Un balance financiero teórico presenta tres activos imaginarios: $\sqrt{-25}$, $\sqrt{-144}$ e $i^{201}$. ¿Cuál es el valor total del conjunto?
2. En un modelo de riesgo, tienes una pérdida de $\sqrt{-121}$ USD y le restas un flujo de $\sqrt{-16}$ USD. ¿Cuál es el remanente imaginario?
3. Resuelve la resta de potencias: $i^{79} - i^{197}$.
4. Simplifica al máximo: $2\sqrt{-50} + 3\sqrt{-8}$.
```

```ad-success
title: ✅ Respuestas para el docente
**Fácil:** 1) $i$, 2) $1$, 3) $8i$, 4) $2i$.
**Medio:** 1) $0$ (ya que $1 + (-1) = 0$), 2) $6\sqrt{5}i$, 3) $17i$, 4) $2\sqrt{2}i$.
**Avanzado:** 1) $18i$ (Explicación: $5i + 12i + i^1 = 18i$), 2) $7i$ USD, 3) $-2i$ (Explicación: $-i - i = -2i$), 4) $16\sqrt{2}i$.
```

---

## Mini-prueba de autoevaluación

```ad-question
title: Pregunta 1: Conceptual
¿Qué matemático estandarizó el uso del símbolo $i$ para representar la unidad imaginaria?
A) René Descartes
B) Leonhard Euler
C) Isaac Newton
*Respuesta: B. Euler lo introdujo para formalizar el concepto que Descartes había nombrado.*
```

```ad-question
title: Pregunta 2: Procedimental
¿Cuál es el resultado de simplificar la operación $i^{52} + i^{54}$?
A) $2$
B) $i$
C) $0$
*Respuesta: C. Como $i^{52} = 1$ e $i^{54} = -1$, la suma es $0$.*
```

```ad-question
title: Pregunta 3: Aplicación $USD
Si sumas dos activos representados por $\sqrt{-16}$ USD y $\sqrt{-81}$ USD, el resultado en el modelo es:
A) $13i$ USD
B) $11i$ USD
C) $97i$ USD
*Respuesta: A ($4i + 9i = 13i$).*
```

---

> [!tip] 💡 En la próxima clase
> Ahora que dominas los números imaginarios puros y sus potencias, aprenderemos a combinarlos con la recta real para formar **Números Complejos** en su forma binómica ($a + bi$).

> [!info] 🧭 Navegación
> *   **Índice:** [[00 - Índice del curso]]
> *   **Siguiente Lección:** [[Clase 02 — Introducción a los números complejos]]