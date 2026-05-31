# Clase 07 — Potencia de radicales

tags: #algebra #powerofradicals
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 7 de 14

ad-info
title: 🧭 Navegación
◀️ [[Clase 06 - Multiplicación de radicales]] | 🏠 [[00 - Índice del curso|Índice]] | [[Clase 08 - Raíz de una raíz]] ▶️

---

ad-info
title: 🌍 Relevancia y aplicaciones
La potencia de radicales permite escalar dimensiones en geometría y física, facilitando el cálculo de crecimientos exponenciales en medidas que originalmente están bajo una raíz. Su dominio es clave para simplificar expresiones complejas antes de realizar cálculos numéricos finales.

*   **💵 Aplicación USD:** En el sector financiero, se utiliza para proyectar el crecimiento de inversiones mediante fórmulas de interés compuesto donde las tasas implican raíces que se elevan a potencias según el tiempo.
*   **🏗️ Aplicación práctica:** Es fundamental en arquitectura para determinar el cambio exacto en el volumen de una estructura cuando sus aristas crecen de forma proporcional a un radical.
*   **📊 Situación cotidiana:** Los ajustes de brillo y sonido en dispositivos digitales suelen seguir leyes de potencias y radicales para que el cambio sea fluido al ojo y oído humano.

---

ad-note
title: Concepto Clave: La Analogía de la Cárcel
Elevar una raíz a una potencia es equivalente a aplicar ese exponente a cada factor que se encuentra dentro y fuera del radical.

Como dice el **Profe Alex**, imagina que la raíz es una **"cárcel"**. El exponente externo representa los **"años de condena"** que les otorgamos a los números de adentro para que intenten alcanzar la libertad (el índice de la raíz). Si los años de condena igualan o superan al índice, ¡el número puede salir!

**Fórmula General:**
$$(a \sqrt[n]{b})^m = a^m \sqrt[n]{b^m}$$

ad-warning
title: Error Común
¡No olvides el coeficiente! El exponente externo afecta **tanto al número de afuera como al de adentro**.
*   ❌ **Incorrecto:** $2\sqrt{3}^2 = 2 \cdot 3 = 6$
*   ✅ **Correcto:** $2\sqrt{3}^2 = 2^2 \cdot 3 = 4 \cdot 3 = 12$

ad-tip
title: El Truco de los "Invisibles"
Recuerda que en matemáticas hay elementos que están ahí aunque no se vean:
1. El índice de una raíz cuadrada es un **2 invisible** ($\sqrt{x} = \sqrt[2]{x}$).
2. El exponente de un número sin potencia es un **1 invisible** ($x = x^1$).
**Regla de oro:** Si el exponente y el índice se pueden dividir exactamente, hazlo. Si son iguales, se eliminan por completo.

---

ad-abstract
title: Procedimiento Paso a Paso
```text
PASO 1 → Descomponer números grandes en sus factores primos (ej. 18 = 2 · 3²).
PASO 2 → Distribuir el exponente externo a cada factor (coeficientes y raíces).
PASO 3 → Multiplicar exponentes internos por el externo (Potencia de otra potencia).
PASO 4 → Extraer factores de la raíz dividiendo el nuevo exponente entre el índice o simplificando el índice y el exponente por su máximo común divisor.
```

---

ad-example
title: Ejemplo 1: Básico
Calcular: $\sqrt[5]{3}^{10}$
1. Aplicamos la propiedad: $\sqrt[5]{3^{10}}$.
2. Dividimos el exponente por el índice: $10 / 5 = 2$.
3. Resultado: $3^2 = 9$.

ad-example
title: Ejemplo 2: Con factores primos
Calcular: $\sqrt[6]{18}^3$
1. **Factorizamos 18:** $\sqrt[6]{2 \cdot 3^2}^3$.
2. **Distribuimos el exponente:** $\sqrt[6]{2^3 \cdot 3^{(2 \cdot 3)}} = \sqrt[6]{2^3 \cdot 3^6}$.
3. **Extracción:** El $3^6$ cumplió los 6 años de condena, sale de la cárcel: $3\sqrt[6]{2^3}$.
4. **Simplificación final:** Simplificamos el índice $6$ y el exponente $3$ dividiendo ambos por $3$ (su máximo común divisor).
5. **Resultado:** $3\sqrt[2]{2^1} \rightarrow 3\sqrt{2}$.

ad-example
title: Ejemplo 3: Avanzado con variables
Calcular: $(x \sqrt[3]{x^2})^2$
1. **Distribuimos:** $x^2 \sqrt[3]{(x^2)^2}$.
2. **Potencia de potencia:** $x^2 \sqrt[3]{x^4}$.
3. **Separamos para extraer:** $x^2 \sqrt[3]{x^3 \cdot x}$.
4. **Liberación:** El $x^3$ sale como $x$: $x^2 \cdot x \sqrt[3]{x}$.
5. **Resultado:** $x^3 \sqrt[3]{x}$.

ad-example
title: Ejemplo 4: Aplicación USD
Una inversión de $100$ USD crece según la fórmula $V = 100(\sqrt[3]{2})^6$. Calcule el valor final.
1. Elevamos el radicando: $100 \sqrt[3]{2^6}$.
2. Dividimos exponente entre índice: $6 / 3 = 2$.
3. Operamos: $100 \cdot 2^2 = 100 \cdot 4$.
4. **Resultado:** $400$ USD.

---

ad-success
title: Ejercicios para el Estudiante

**🟢 Nivel Fácil**
1. $(\sqrt[4]{m})^4$
2. $\sqrt[2]{3^6}$

**🟡 Nivel Medio**
3. $(2\sqrt[3]{m^2})^3$
4. $(\sqrt[6]{x^2y^3})^3$

**🔴 Nivel Avanzado**
5. Si el lado de un cuadrado mide $5\sqrt{x^3}$ metros, calcule el costo total del terreno si el valor por metro cuadrado es de $1$ USD.

**Respuestas:**
1. $m$
2. $27$ (porque $3^3 = 27$)
3. $8m^2$
4. $xy\sqrt{y}$ (Proceso: $\sqrt[6]{x^6y^9} = x \cdot y^{9/6} = x \cdot y^{3/2} = xy\sqrt{y}$)
5. $25x^3$ USD

---

ad-question
title: Autoevaluación
1. ¿Qué sucede con el símbolo de la raíz cuando el exponente es exactamente igual al índice?
2. En el procedimiento, ¿qué operación matemática se realiza al aplicar un exponente externo a un exponente interno (Potencia de otra potencia)?
3. Si un objeto tiene un área de $(\sqrt{10})^4$ metros cuadrados, ¿cuál es su valor numérico simplificado?

ad-tip
title: Próximo tema
En la **Clase 08** veremos la **Raíz de una raíz**. Aprenderás que cuando una cárcel está dentro de otra cárcel, los guardias (índices) simplemente se multiplican.

---
ad-info
title: 🧭 Navegación
◀️ [[Clase 06 - Multiplicación de radicales]] | 🏠 [[00 - Índice del curso|Índice]] | [[Clase 08 - Raíz de una raíz]] ▶️