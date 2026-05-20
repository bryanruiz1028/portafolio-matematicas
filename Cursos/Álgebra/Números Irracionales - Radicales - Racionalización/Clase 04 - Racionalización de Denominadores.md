# Clase 04 — Racionalización de Denominadores
tags: #algebra #racionalizacin
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 4 de 6

> [!info] 🧭 Navegación
> [[Clase 03|⬅ Clase 03]] | [[00 - Índice del curso|Índice]] | **Clase 04** | | [[Clase 05|Clase 05 ➡]]

---

### 1. RELEVANCIA Y APLICACIONES

> [!info] 🌍 Relevancia y aplicaciones
> Racionalizar es un proceso fundamental para eliminar raíces del denominador, transformando expresiones complejas en otras fáciles de operar. Esto agiliza la suma de fracciones con radicales y permite realizar divisiones de forma mucho más intuitiva, exacta y profesional.
> 
> - 💵 **Cálculo de costos unitarios ($USD):** Permite distribuir presupuestos que involucran raíces (como áreas o hipotenusas) en montos manejables.
> - 🏗️ **Ingeniería civil:** Fundamental para determinar medidas de soporte y tensiones donde las fórmulas incluyen raíces cuadradas en sus bases.
> - 📊 **Estandarización financiera:** Facilita la creación de reportes rápidos al trabajar con valores decimales aproximados más limpios.

---

### 2. CONCEPTO CLAVE Y ERRORES COMUNES

> [!note] 📌 ¿Qué es Racionalización?
> Racionalizar una fracción consiste en encontrar una **fracción equivalente** que no tenga raíces (radicales) en el denominador. Es como "limpiar" la parte de abajo de la fracción para que solo queden números enteros, facilitando así cualquier cálculo posterior.

> [!warning] ⚠️ Error común
> Jamás intentes simplificar un número que está fuera de una raíz con uno que está dentro. Según el Profe Alex, "lo de afuera va con lo de afuera".
> **Incorrecto:** $\frac{\sqrt{10}}{10} = \sqrt{1} = 1$
> **Correcto:** No se pueden simplificar. $\frac{\sqrt{10}}{10}$ es una expresión irreducible a menos que racionalices el numerador (lo cual no es nuestro objetivo aquí).

> [!tip] 💡 Truco para recordarlo
> Para los binomios, recuerda esta regla: **"El conjugado es el gemelo con humor opuesto"**. Es decir, usas los mismos números, pero si el original está "positivo" (+), su gemelo debe estar "negativo" (-).

---

### 3. PROCEDIMIENTO PASO A PASO

Para racionalizar denominadores binomios (dos términos), seguimos este proceso técnico:

```text
PASO 1 → Identificar el binomio del denominador (ej. √a - √b).
PASO 2 → Multiplicar numerador y denominador por el conjugado (cambiar el signo central).
PASO 3 → Aplicar diferencia de cuadrados en el denominador: (a - b)(a + b) = a² - b².
PASO 4 → Simplificar factores si es posible. IMPORTANTE: Solo simplifica factores que estén 
         FUERA de las raíces. Si el denominador resulta negativo, mueve el signo al numerador.
```

---

### 4. SECCIÓN DE EJEMPLOS PRÁCTICOS

```ad-example
title: Ejemplo 1 (Monomio Básico)
**Problema:** Racionalizar $\frac{5}{\sqrt{3}}$
1. Multiplicamos numerador y denominador por la misma raíz: $\frac{5}{\sqrt{3}} \cdot \frac{\sqrt{3}}{\sqrt{3}}$
2. En el numerador obtenemos: $5\sqrt{3}$
3. En el denominador: $\sqrt{3} \cdot \sqrt{3} = 3$
**Resultado:** $\frac{5\sqrt{3}}{3}$
```

```ad-example
title: Ejemplo 2 (Monomio Índice n)
**Problema:** Racionalizar $\frac{2}{\sqrt[5]{3^2}}$
1. Para eliminar la raíz, el exponente debe igualar al índice (5). Si tenemos $3^2$, nos falta $3^3$.
2. Multiplicamos por $\frac{\sqrt[5]{3^3}}{\sqrt[5]{3^3}}$.
3. Denominador: $\sqrt[5]{3^2 \cdot 3^3} = \sqrt[5]{3^5} = 3$.
4. Numerador: $2\sqrt[5]{27}$.
**Resultado:** $\frac{2\sqrt[5]{27}}{3}$
```

```ad-example
title: Ejemplo 3 (Binomio Conjugado)
**Problema:** Racionalizar $\frac{5}{\sqrt{7} - \sqrt{2}}$
1. Multiplicamos por el conjugado: $(\sqrt{7} + \sqrt{2})$.
2. Numerador: $5(\sqrt{7} + \sqrt{2})$.
3. Denominador: $(\sqrt{7})^2 - $(\sqrt{2})^2 = 7 - 2 = 5$.
4. Simplificación: El 5 de afuera del numerador se cancela con el 5 del denominador.
**Resultado:** $\sqrt{7} + \sqrt{2}$
```

```ad-example
title: Ejemplo 4 (Aplicación $USD)
**Problema:** Repartir $15 USD entre $\sqrt[3]{3}$ personas de forma racionalizada.
1. Expresión inicial: $\frac{15}{\sqrt[3]{3^1}}$
2. Completamos el índice: Multiplicamos por $\frac{\sqrt[3]{3^2}}{\sqrt[3]{3^2}}$.
3. Denominador: $\sqrt[3]{3^3} = 3$. Numerador: $15\sqrt[3]{9}$.
4. Simplificamos lo de afuera: $15 \div 3 = 5$.
**Resultado:** $5\sqrt[3]{9}$ USD por persona.
```

---

### 5. EJERCICIOS PARA EL ESTUDIANTE

```ad-abstract
title: Verde (Fácil)
1. $\frac{2}{\sqrt{2}}$
2. $\frac{1}{\sqrt{5}}$
3. $\frac{3}{\sqrt{3}}$
4. $\frac{7}{\sqrt{7}}$
```

```ad-abstract
title: Amarillo (Medio)
1. $\frac{1}{\sqrt{5}+\sqrt{3}}$
2. $\frac{2}{\sqrt{7}-\sqrt{5}}$
3. $\frac{5}{3-\sqrt{2}}$ (Nota: Recuerda que esta fracción puede ser irreducible).
4. $\frac{4}{\sqrt{6}+\sqrt{2}}$
```

```ad-abstract
title: Rojo (Avanzado)
1. $\frac{10 USD}{\sqrt[4]{2}}$
2. $\frac{6 USD}{\sqrt[3]{3}}$
3. $\frac{1}{\sqrt[5]{2^2}}$
4. $\frac{12}{\sqrt[4]{8}}$ (Pista: $8 = 2^3$, completa lo que falta para llegar a índice 4).
```

```ad-success
title: Respuestas Sugeridas
- **Verde:** 1) $\sqrt{2}$, 2) $\frac{\sqrt{5}}{5}$, 3) $\sqrt{3}$, 4) $\sqrt{7}$
- **Amarillo:** 1) $\frac{\sqrt{5}-\sqrt{3}}{2}$, 2) $\sqrt{7}+\sqrt{5}$, 3) $\frac{15+5\sqrt{2}}{7}$ (No se puede simplificar más porque 15 y 5 no son divisibles ambos por 7), 4) $\sqrt{6}-\sqrt{2}$
- **Rojo:** 1) $5\sqrt[4]{8}$, 2) $2\sqrt[3]{9}$, 3) $\frac{\sqrt[5]{8}}{2}$, 4) $6\sqrt[4]{2}$
```

---

### 6. MINI-PRUEBA DE AUTOEVALUACIÓN

```ad-question
title: Pregunta 1
¿Cuál es el conjugado correcto de $3 - \sqrt{2}$?
A) $-3 - \sqrt{2}$
B) $3 + \sqrt{2}$
C) $\sqrt{2} - 3$

**Respuesta:** B. Siguiendo el truco del "gemelo con humor opuesto", solo cambiamos el signo que separa a los dos términos.
```

```ad-question
title: Pregunta 2
Al racionalizar $\frac{2}{\sqrt{2}}$, el resultado es:
A) $1$
B) $\sqrt{2}$
C) $2\sqrt{2}$

**Respuesta:** B. Al multiplicar por $\sqrt{2}/\sqrt{2}$ obtenemos $2\sqrt{2}/2$. El 2 de afuera se simplifica con el 2 de abajo.
```

```ad-question
title: Pregunta 3
Si un costo de $10 USD se divide por $\sqrt{5}$, ¿cuál es el valor racionalizado?
A) $2\sqrt{5}$ USD
B) $5\sqrt{2}$ USD
C) $10\sqrt{5}$ USD

**Respuesta:** A. $\frac{10}{\sqrt{5}} \cdot \frac{\sqrt{5}}{\sqrt{5}} = \frac{10\sqrt{5}}{5}$. Dividimos lo de afuera: $10 \div 5 = 2$.
```

---

### 7. CIERRE Y NAVEGACIÓN INFERIOR

> [!tip] 💡 En la próxima clase
> Ahora que dominas la racionalización básica y de binomios, en la próxima sesión exploraremos la simplificación de radicales complejos y cómo trabajar con variables (letras) dentro de las raíces. ¡Sigue practicando!

> [!info] 🧭 Navegación
> [[Clase 03|⬅ Clase 03]] | [[00 - Índice del curso|Índice]] | **Clase 04** | | [[Clase 05|Clase 05 ➡]]