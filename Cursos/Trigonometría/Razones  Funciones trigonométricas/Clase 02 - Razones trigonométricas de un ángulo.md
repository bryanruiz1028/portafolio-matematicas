# Clase 02 — Razones trigonométricas de un ángulo

#algebra #trigonometria
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 12

> [!info] 🧭 Navegación
> ◀ [[Clase 01 — Introducción a la trigonometría]] | [[00 - Índice del curso|Índice]] | [[Clase 03 — Cálculo de ángulos desconocidos]] ▶

---

> [!info] 🌍 Relevancia y aplicaciones
> Las razones trigonométricas son herramientas matemáticas que permiten establecer relaciones numéricas constantes entre los lados de un triángulo rectángulo y sus ángulos. Son la base para comprender cómo interactúan las medidas espaciales en cualquier estructura triangular.
> 
> - **💵 Aplicación $USD:** El cálculo preciso de la hipotenusa permite optimizar la compra de materiales; por ejemplo, determinar la longitud exacta de cables de acero para soporte evita el desperdicio de metros sobrantes de alto costo.
> - **🏗️ Aplicación práctica:** En ingeniería, se utilizan para medir alturas de edificios o montañas que son imposibles de medir con una cinta métrica directa.
> - **📊 Situación cotidiana:** Permiten calcular la pendiente ideal de una rampa de acceso o la estabilidad de una escalera de mano apoyada contra una pared.

---

> [!note] 📌 ¿Qué es una razón trigonométrica?
> Una **razón trigonométrica** es el resultado de comparar, mediante una división (cociente), las longitudes de dos de los lados de un triángulo rectángulo respecto a uno de sus ángulos agudos. Esencialmente, nos dice cuántas veces cabe un lado en el otro o qué proporción guardan entre sí.

> [!warning] ⚠️ Error común
> ❌ **Incorrecto:** Confundir el cateto opuesto con el adyacente por no mirar la posición del ángulo.
> ✅ **Correcto:** Identificar siempre el cateto opuesto como el lado que está "lejos" o enfrente del ángulo de referencia. El adyacente es el que está "pegado" al ángulo.

> [!tip] 💡 Truco: SOH CAH TOA
> Para recordar las fórmulas principales, usa esta regla mnemotécnica y visualízala como fracciones:
> - **SOH**: $\text{Seno} = \frac{\text{Opuesto}}{\text{Hipotenusa}}$
> - **CAH**: $\text{Coseno} = \frac{\text{Adyacente}}{\text{Hipotenusa}}$
> - **TOA**: $\text{Tangente} = \frac{\text{Opuesto}}{\text{Adyacente}}$

---

### 📋 Procedimiento paso a paso

```text
PASO 1 → Identificar la Hipotenusa: Localizar el lado más largo, que siempre 
         está frente al ángulo recto (90°).
PASO 2 → Identificar catetos: Determinar cuál es el opuesto (lejos) y cuál el 
         adyacente (pegado) en relación al ángulo de referencia dado.
PASO 3 → Calcular el lado faltante: Si el triángulo no tiene todas sus medidas, 
         usar el Teorema de Pitágoras (h = √(a² + b²)).
PASO 4 → Aplicar la fórmula: Sustituir los valores en la razón deseada 
         (Seno, Coseno o Tangente) y simplificar las unidades de medida.
```

---

### 📝 Bloques de Ejemplos

```ad-example
title: Ejemplo 1: Caso Básico
**Datos:** Triángulo con lados de 3m, 4m y 5m. Ángulo de referencia: $\theta$.
1. **Identificación:** Hipotenusa = 5m, Cateto Opuesto = 3m.
2. **Cálculo del Seno:**
   $$\sin \theta = \frac{3 \text{ m}}{5 \text{ m}}$$
3. **Resultado:** Al dividir, las unidades (m) se eliminan, lo que significa que la razón es adimensional. El resultado es $\frac{3}{5}$ o **0.6**.
```

```ad-example
title: Ejemplo 2: Uso del Teorema de Pitágoras
**Datos:** Cateto adyacente = 3cm, Cateto opuesto = 4cm. Hipotenusa desconocida ($h$).
1. **Hallar Hipotenusa:**
   $$h = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5 \text{ cm}$$
2. **Cálculo del Coseno ($\alpha$):**
   $$\cos \alpha = \frac{\text{Cateto Adyacente}}{\text{Hipotenusa}} = \frac{3}{5}$$
3. **Resultado:** **0.6**.
```

```ad-example
title: Ejemplo 3: Relación Recíproca (Caso Avanzado)
**Datos:** Lados 10, 6 y 11.6 (hipotenusa aproximada).
**Ángulo de referencia:** $\alpha$ (donde el lado 10 es el cateto opuesto).
1. **Tangente:** $\tan \alpha = \frac{10}{6} = 1.66...$
2. **Cotangente:** Es la razón **recíproca** de la tangente. $\cot \alpha = \frac{6}{10} = 0.6$.
**Nota:** Observa cómo los valores se invierten; la cotangente es simplemente la fracción de la tangente "al revés".
```

```ad-example
title: Ejemplo 4: Aplicación Estructural $USD
**Problema:** Se desea asegurar un poste publicitario. El poste mide 4m de alto (cateto opuesto) y su base está a 3m del anclaje (cateto adyacente). Si el cable de soporte (hipotenusa) cuesta $15.50 USD por metro:
1. **Cálculo de cable:** Aplicando $h = \sqrt{4^2 + 3^2}$, la hipotenusa es 5m.
2. **Costo total:** $5 \text{ metros} \times \$15.50 = \mathbf{\$77.50 \text{ USD}}$.
```

---

### ✏️ Ejercicios para el Estudiante

```ad-abstract
title: Actividades de Práctica
**🟢 Nivel Fácil: Identificación directa**
Dados los lados de un triángulo (6, 8, 10) y tomando como referencia el **ángulo opuesto al lado 6**:
1. Calcule el Seno.
2. Calcule el Coseno.
3. Calcule la Tangente.
4. Calcule la Cosecante (recíproca del seno).

**🟡 Nivel Medio: Cálculo de lado faltante**
En un triángulo con catetos de 5 y 12:
1. Calcule la Hipotenusa usando Pitágoras.
2. Halle el Seno del ángulo menor (opuesto al lado 5).
3. Halle el Coseno del mismo ángulo.
4. Halle la Tangente del mismo ángulo.

**🔴 Nivel Avanzado ($USD): Problemas aplicados**
1. Una escalera se apoya a 6m de altura en una pared y su base está a 8m. Si el metro de escalera cuesta $25 USD, ¿cuánto cuesta la escalera total?
2. La sombra de un edificio de 10m de altura es de 6m. Se instalará un toldo desde la azotea hasta el final de la sombra. Si el material cuesta $12 USD el metro lineal, calcule el presupuesto (use la hipotenusa exacta $\sqrt{136} \approx 11.66m$).
3. Un cable de 11.6m une un poste de 10m con el suelo. Si el costo de instalación es de $5.50 USD por metro de cable, calcule el costo total.
4. Se requiere una rampa con una base de 4m y una altura de 3m. El recubrimiento cuesta $20 USD por metro de longitud de rampa. ¿Cuál es el costo?
```

```ad-success
title: ✅ Respuestas para el Docente
- **Fácil:** 1) 0.6 | 2) 0.8 | 3) 0.75 | 4) 1.66
- **Medio:** 1) 13 | 2) 5/13 (≈0.38) | 3) 12/13 (≈0.92) | 4) 5/12 (≈0.41)
- **Avanzado:** 1) $250 USD | 2) $139.92 USD (usando 11.66m) | 3) $63.80 USD | 4) $100 USD
```

---

### 🧠 Mini-Prueba de Autoevaluación

```ad-question
title: Autoevaluación rápida
1. **¿Cuál es el nombre del lado que siempre se encuentra frente al ángulo recto?**
2. **Si un triángulo tiene catetos de 3 y 4, ¿cuál es el valor de la tangente para el ángulo opuesto al lado de 3?**
3. **Si necesitas comprar un cable para una hipotenusa de 10 metros y cada metro cuesta $15.50 USD, ¿cuál es el presupuesto total?**
```

---

> [!tip] 💡 En la próxima clase
> Ahora que sabes identificar y calcular las razones como fracciones y decimales, aprenderemos a realizar la operación para encontrar el valor exacto de los ángulos desconocidos en grados.

> [!info] 🧭 Navegación
> ◀ [[Clase 01 — Introducción a la trigonometría]] | [[00 - Índice del curso|Índice]] | [[Clase 03 — Cálculo de ángulos desconocidos]] ▶