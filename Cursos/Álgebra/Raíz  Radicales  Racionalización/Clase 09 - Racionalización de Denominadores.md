# Clase 09 — Racionalización de Denominadores
tags: #algebra #racionalizacin
Curso: [[00 - Índice del curso]] | Bloque 3 | Lección 9 de 14

> [!info] 🧭 Navegación
> [[Clase 08|⬅ Clase 08]] | [[00 - Índice del curso|Índice]] | **Clase 09** | | [[Clase 10|Clase 10 ➡]]

## 1. ¿Por qué es importante esta clase?
> [!info] 🌍 Relevancia y aplicaciones
> La racionalización es el proceso matemático que nos permite transformar expresiones con raíces en el denominador en fracciones equivalentes mucho más sencillas. Al eliminar los radicales de la parte inferior, obtenemos una estructura numérica limpia que facilita enormemente las operaciones de suma, resta y división en álgebra superior.

- 💵 **Aplicación financiera:** Permite simplificar el cálculo de costos unitarios y presupuestos que involucran raíces, haciendo que las operaciones manuales sean viables al trabajar con divisores enteros.
- 🏗️ **Ingeniería:** Es una técnica fundamental para normalizar denominadores en **fórmulas de resistencia** de materiales, asegurando que los valores de carga sean interpretables y estandarizados.
- 📊 **Cálculo cotidiano:** Ofrece la ventaja de trabajar con denominadores enteros, lo que permite repartir o dividir cantidades de forma más intuitiva que si tuviéramos un divisor irracional.

## 2. Concepto clave
> [!note] 📌 ¿Qué es Racionalización?
> Según la metodología del profe Alex, racionalizar una fracción consiste en encontrar una fracción equivalente que **no tenga radicales en el denominador**. Es como "limpiar" la parte de abajo de la fracción para que solo queden números enteros.

> [!warning] ⚠️ Error común
> ❌ **Incorrecto:** Intentar simplificar un número que está "afuera" de la raíz con uno que está "adentro". Por ejemplo, en $\frac{\sqrt{2}}{10}$, no puedes simplificar el 2 con el 10.
> ✅ **Correcto:** Solo puedes simplificar factores que estén **ambos fuera** o **ambos dentro** de la raíz. Piensa en el símbolo de la raíz como un "escudo" que protege al número.

> [!tip] 💡 Truco para recordarlo: La lógica del "Complemento"
> Para raíces de índice superior (cúbicas, quintas, etc.), debes multiplicar por lo que le falta al exponente para alcanzar al índice. 
> **Fórmula:** $n - m$ (donde $n$ es el índice y $m$ es el exponente original).
> *Ejemplo:* Si tienes $\sqrt[5]{3^2}$, restas $5 - 2 = 3$. Entonces multiplicas por $\sqrt[5]{3^3}$.

## 3. Procedimiento paso a paso
Para racionalizar un **binomio** (denominador con dos términos sumando o restando), aplicamos el siguiente protocolo técnico:

```
PASO 1 → Identificar el binomio en el denominador.
PASO 2 → Multiplicar numerador y denominador por el "conjugado" (mismos términos, signo opuesto).
PASO 3 → Aplicar el producto notable (diferencia de cuadrados): (a-b)(a+b) = a² - b².
PASO 4 → Simplificar la fracción final eliminando factores comunes fuera de las raíces.
```

## 4. Ejemplos resueltos

```ad-example
title: Ejemplo 1 — Denominador Monomio (Raíz Cuadrada)
Racionalizar $\frac{5}{\sqrt{3}}$. Multiplicamos por $\frac{\sqrt{3}}{\sqrt{3}}$:
$$\frac{5}{\sqrt{3}} \cdot \frac{\sqrt{3}}{\sqrt{3}} = \frac{5\sqrt{3}}{\sqrt{3}^2} = \frac{5\sqrt{3}}{3}$$
**Resultado:** $\frac{5\sqrt{3}}{3}$
```

```ad-example
title: Ejemplo 2 — Denominador Monomio (Índice Superior)
Racionalizar $\frac{2}{\sqrt[3]{5}}$. El índice es 3 y el exponente del 5 es 1. Aplicamos el complemento ($3-1=2$):
$$\frac{2}{\sqrt[3]{5^1}} \cdot \frac{\sqrt[3]{5^2}}{\sqrt[3]{5^2}} = \frac{2\sqrt[3]{25}}{\sqrt[3]{5^3}}$$
Al anular la raíz cúbica con el exponente 3 obtenemos:
**Resultado:** $\frac{2\sqrt[3]{25}}{5}$
```

```ad-example
title: Ejemplo 3 — Denominador Binomio (Raíces compuestas)
Racionalizar $\frac{5}{\sqrt{7}-\sqrt{2}}$. Usamos el conjugado $(\sqrt{7}+\sqrt{2})$:
$$\frac{5(\sqrt{7}+\sqrt{2})}{(\sqrt{7}-\sqrt{2})(\sqrt{7}+\sqrt{2})} = \frac{5(\sqrt{7}+\sqrt{2})}{\sqrt{7}^2 - \sqrt{2}^2}$$
Paso intermedio visual: $\frac{5(\sqrt{7}+\sqrt{2})}{7 - 2} = \frac{5(\sqrt{7}+\sqrt{2})}{5}$
**Resultado:** $\sqrt{7}+\sqrt{2}$ (tras simplificar los 5).
```

```ad-example
title: Ejemplo 4 — Aplicación real con $USD
Si un costo unitario está dado por $\frac{3}{\sqrt{5}-\sqrt{2}}$ USD, racionalizamos:
$$\frac{3(\sqrt{5}+\sqrt{2})}{5-2} = \frac{3(\sqrt{5}+\sqrt{2})}{3}$$
**Resultado:** $(\sqrt{5}+\sqrt{2})$ USD.
```

## 5. Ejercicios para el estudiante

```ad-abstract
title: 🟢 Fácil — Monomios Cuadrados
1. Racionalizar $\frac{2}{\sqrt{2}}$.
2. Racionalizar $\frac{1}{\sqrt{6}}$ (extraído de $\sqrt{5/6}$).
3. Racionalizar $\frac{5}{2\sqrt{5}}$.
4. Racionalizar $\frac{3}{5\sqrt{2}}$.
```

```ad-abstract
title: 🟡 Medio — Índices Superiores y Binomios
1. Racionalizar $\frac{1}{\sqrt[5]{2^2}}$.
2. Racionalizar $\frac{2}{\sqrt[4]{a}}$.
3. Racionalizar $\frac{1}{\sqrt{5}+\sqrt{3}}$.
4. Racionalizar $\frac{3}{\sqrt{5}-\sqrt{2}}$.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD (Binomios de práctica)
Determine el valor exacto en USD de los siguientes presupuestos industriales:
1. Material tipo A: $\frac{2}{5-\sqrt{5}}$ USD.
2. Material tipo B: $\frac{5}{\sqrt{3}-4}$ USD.
3. Servicio técnico: $\frac{1}{\sqrt{5}+\sqrt{3}}$ USD.
4. Mantenimiento: $\frac{3}{\sqrt{5}-\sqrt{2}}$ USD.
```

```ad-success
title: ✅ Respuestas (para el docente)
**🟢 Fácil:** 1. [$\sqrt{2}$] | 2. [$\sqrt{6}/6$] | 3. [$\sqrt{5}/2$] | 4. [$3\sqrt{2}/10$]
**🟡 Medio:** 1. [$\frac{\sqrt[5]{2^3}}{2}$] | 2. [$\frac{2\sqrt[4]{a^3}}{a}$] | 3. [$\frac{\sqrt{5}-\sqrt{3}}{2}$] | 4. [$\sqrt{5}+\sqrt{2}$]
**🔴 Avanzado:** 
1. [$\frac{5+\sqrt{5}}{10}$ USD]
2. [$\frac{5\sqrt{3}+20}{-13}$ USD]
3. [$\frac{\sqrt{5}-\sqrt{3}}{2}$ USD]
4. [$\sqrt{5}+\sqrt{2}$ USD]
```

## 6. Mini-prueba de autoevaluación
```ad-question
title: 🧪 Pregunta 1
¿Por qué se multiplica por el conjugado en un binomio?
a) Para sumar las raíces. 
b) Para crear una diferencia de cuadrados y eliminar las raíces. 
c) Para simplificar el numerador. 
d) Porque el índice es 2.
**✅ Respuesta: b** — Al multiplicar $(a-b)(a+b)$ obtenemos $a^2-b^2$, lo que cancela las raíces cuadradas.
```

```ad-question
title: 🧪 Pregunta 2
Si el denominador es $\sqrt[5]{3^2}$, ¿por qué factor se debe multiplicar para racionalizar?
a) $\sqrt[5]{3^5}$ 
b) $\sqrt[5]{3^2}$ 
c) $\sqrt[5]{3^3}$ 
d) $\sqrt[5]{3^1}$
**✅ Respuesta: c** — Aplicando la regla $n-m$: $5 - 2 = 3$. Los exponentes deben sumar el índice.
```

```ad-question
title: 🧪 Pregunta 3
Calcula el valor racionalizado de un presupuesto de $\frac{5}{\sqrt{5}}$ USD.
a) $5\sqrt{5}$ 
b) $\sqrt{5}$ 
c) 1 
d) $5$
**✅ Respuesta: b** — $\frac{5\sqrt{5}}{5} = \sqrt{5}$.
```

## 7. Notas para el próximo tema
> [!tip] 💡 En la próxima clase
> En la **Clase 10** profundizaremos en la racionalización de expresiones más complejas que incluyen **variables algebraicas** (letras como $x$ o $a$) y el manejo de binomios con raíces de índices superiores.

> [!info] 🧭 Navegación
> [[Clase 08|⬅ Clase 08]] | [[00 - Índice del curso|Índice]] | **Clase 09** | | [[Clase 10|Clase 10 ➡]]