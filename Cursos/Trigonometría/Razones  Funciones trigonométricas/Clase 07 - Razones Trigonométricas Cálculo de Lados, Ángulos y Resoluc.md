# Clase 07 — Razones Trigonométricas: Cálculo de Lados, Ángulos y Resolución de Problemas Complejos

---
**Tags:** #matemáticas #trigonometría #geometría #resolución-problemas #diseño-técnico
**Curso:** Matemáticas de Secundaria / Bachillerato Técnico
**Bloque:** Trigonometría y Aplicaciones Métricas

---

> [!info] 🧭 Navegación
> - **Clase Anterior:** [[Conceptos Básicos de Triángulos Rectángulos]]
> - **Tema Actual:** Razones Trigonométricas (Seno, Coseno, Tangente)
> - **Siguiente Clase:** [[Resolución de Triángulos Oblicuángulos: Ley de Seno y Coseno]]

---

## 🏗️ Relevancia y Aplicaciones

La trigonometría no es solo un ejercicio académico; es el lenguaje que permite a ingenieros y arquitectos transformar ángulos en distancias reales y presupuestos precisos.

*   **$USD Económico:** Un ingeniero civil debe calcular la longitud necesaria de un cable de soporte (hipotenusa) para una torre de telecomunicaciones antes de comprar el material. Si el cálculo determina una longitud de 10 metros y el cable certificado cuesta **$15.50 por metro**, el presupuesto total se establece en **$155.00**. La precisión evita el desperdicio de capital.
*   **🏗️ Construcción y Topografía:** Permite determinar alturas que no se pueden medir manualmente, como la cima de una colina, la altitud de vuelo de una aeronave o la elevación de un faro sobre un risco.
*   **📊 Situación Cotidiana:** Es vital en la navegación marítima y aérea para calcular distancias horizontales seguras entre embarcaciones u obstáculos mediante ángulos de depresión o elevación.

---

```ad-note
title: Concepto Clave: El Triángulo como Relación
Para un estudiante de 12 años, las razones trigonométricas son "comparadores" de lados. Imagina que el ángulo de referencia es un **ojo que mira**:
1. El lado que tiene justo enfrente es el **Cateto Opuesto**.
2. El lado que le sirve de base (y no es el más largo) es el **Cateto Adyacente**.
3. El lado más largo y diagonal, siempre frente al ángulo recto, es la **Hipotenusa**.
Las razones (Seno, Coseno, Tangente) solo nos dicen cuántas veces cabe un lado en el otro según la apertura de ese "ojo".
```

```ad-warning
title: Configuración Crítica de la Calculadora
Un error de configuración puede arruinar un diseño técnico. Asegúrese de que su calculadora esté en modo **"DEG"** o muestre una **"D"** en pantalla (Grados sexagesimales).
* **DEG (Degrees):** Es el modo correcto para geometría y construcción.
* **RAD (Radians):** Se reserva para Cálculo Avanzado y Matemáticas Superiores.
* **Prueba rápida:** Calcule `sin(90)`. Si el resultado es **1**, está en el modo correcto. Si obtiene **0.89**, está en Radianes y debe cambiarlo.
```

```ad-tip
title: Regla Mnemotécnica: SOH CAH TOA
Esta palabra "mágica" le ayudará a seleccionar la fórmula correcta instantáneamente:
* **SOH:** **S**eno = **O**puesto / **H**ipotenusa.
* **CAH:** **C**oseno = **A**dyacente / **H**ipotenusa.
* **TOA:** **T**angente = **O**puesto / **A**dyacente.
```

---

## 🛠️ Procedimiento Paso a Paso

Para resolver problemas con el rigor del Profe Alex, siga siempre estos cuatro pasos:

```text
PASO 1: Identificar los lados. Nombre el Cateto Opuesto (CO), Cateto Adyacente (CA) 
         e Hipotenusa (H) según la posición del ángulo de referencia.

PASO 2: Listar datos y objetivo. Escriba los valores conocidos y la incógnita (x).

PASO 3: Seleccionar la herramienta. Elija la razón (Seno, Coseno o Tangente) que 
         conecte los dos lados que aparecen en su lista de datos.

PASO 4: Ejecutar el despeje. 
         - Para hallar un lado: Despeje la variable 'x' mediante multiplicación o división.
         - Para hallar un ángulo: Use la función inversa (arcsin, arccos o arctan).
```

---

## 📝 Ejemplos Prácticos

```ad-example
title: Ejemplo 1: Cálculo de un Lado (Video 1)
**Problema:** En un triángulo rectángulo con un ángulo de 32° y una hipotenusa de 10m, ¿cuál es la medida del cateto opuesto?
1. **Datos:** Ángulo = 32°; Hipotenusa = 10m; CO = $x$.
2. **Fórmula (SOH):** $\text{sen}(32^{\circ}) = \frac{x}{10}$.
3. **Despeje:** $10 \cdot \text{sen}(32^{\circ}) = x$.
4. **Resultado:** $x \approx 5.3 \text{ metros}$.
```

```ad-example
title: Ejemplo 2: Cálculo de un Ángulo (Video 2)
**Problema:** Un triángulo tiene un CO de 6m y una Hipotenusa de 8m. Halle el ángulo $\theta$.
1. **Datos:** CO = 6; H = 8; Ángulo = $\theta$.
2. **Fórmula (SOH):** $\text{sen}(\theta) = \frac{6}{8}$.
3. **Despeje:** $\theta = \text{arcsen}(0.75)$.
4. **Resultado:** $\theta \approx 48.59^{\circ}$.
```

```ad-example
title: Ejemplo 3: Sistema de Ecuaciones Complejo (Video 10 - Avión)
**Problema:** Dos observadores a 790m de distancia ven un avión con ángulos de 82° y 70°. Halle la altura ($h$).
1. **Definición de variables:** Sea $y$ la distancia del primer observador al punto bajo el avión. La distancia del segundo será $(790 - y)$.
2. **Ecuaciones de Tangente (TOA):**
   - $\tan(82^{\circ}) = \frac{h}{y} \implies h = y \cdot \tan(82^{\circ})$
   - $\tan(70^{\circ}) = \frac{h}{790 - y} \implies h = (790 - y) \cdot \tan(70^{\circ})$
3. **Igualación y Desglose Algebraico:**
   $y \cdot \tan(82^{\circ}) = (790 - y) \cdot \tan(70^{\circ})$
   $y \cdot \tan(82^{\circ}) = 790 \cdot \tan(70^{\circ}) - y \cdot \tan(70^{\circ})$
   $y \cdot \tan(82^{\circ}) + y \cdot \tan(70^{\circ}) = 790 \cdot \tan(70^{\circ})$
4. **Factorización Crítica:**
   $y \cdot (\tan 82^{\circ} + \tan 70^{\circ}) = 790 \cdot \tan 70^{\circ}$
5. **Cálculo final:** $y \approx 220.06\text{m}$. Sustituyendo en $h$:
   **Resultado:** $h = 220.06 \cdot \tan(82^{\circ}) \approx 1565.80 \text{ metros}$.
```

```ad-example
title: Ejemplo 4: Aplicación de Diseño y Costo (Video 9)
**Problema:** Tras resolver un sistema de ecuaciones para una colina con un poste de 30m, se determina que la altura de la colina es $22.83\text{m}$. Se requiere instalar una valla de seguridad cuyo costo es de **$25 USD por metro lineal de altura**.
1. **Cálculo:** $22.83 \text{ m} \cdot 25 \text{ USD/m}$.
2. **Resultado:** El costo total de inversión para la valla es de **$570.75 USD**.
```

---

## ✍️ Ejercicios para el Estudiante

```ad-abstract
title: 🟢 Nivel Fácil: Cálculo de Lados
1. Determine el Cateto Adyacente ($y$) si el ángulo de referencia es de 65° y la hipotenusa mide 13 metros. (Pista: CAH).
2. Determine el Cateto Opuesto ($x$) si el ángulo es de 35° y el Cateto Adyacente mide 7 metros. (Pista: TOA).
```

```ad-abstract
title: 🟡 Nivel Medio: Cálculo de Ángulos
1. En un triángulo rectángulo, el cateto opuesto mide 12m y el adyacente mide 19m. Calcule el ángulo $\theta$ en grados sexagesimales.
2. Un operario apoya una escalera de 9m (hipotenusa) contra una pared, quedando la base a 6m de la misma (cateto adyacente). Calcule el ángulo de inclinación $\alpha$.
```

```ad-abstract
title: 🔴 Nivel Avanzado: Aplicación Técnica y Financiera
**Problema:** Un globo aerostático es observado por dos técnicos separados por 300m con ángulos de elevación de 79° y 60°.
1. Calcule la altura exacta ($h$) alcanzada por el globo utilizando el método de igualación de tangentes.
2. Si el costo operativo del quemador de propano es de **$2.5 USD por cada metro de altura alcanzada**, ¿cuál es el costo total del ascenso? (*Nota: Use el valor de altura sin redondear para el cálculo final*).
```

---

```ad-success
title: Respuestas para el Docente (Solucionario)
* **Fácil 1:** $y = 13 \cdot \cos(65^{\circ}) \approx 5.49 \text{ m}$.
* **Fácil 2:** $x = 7 \cdot \tan(35^{\circ}) \approx 4.90 \text{ m}$.
* **Medio 1:** $\theta = \arctan(12/19) \approx 32.28^{\circ}$ ($32^{\circ} 16' 32''$).
* **Medio 2:** $\alpha = \arccos(6/9) \approx 48.19^{\circ}$ ($48^{\circ} 11' 22''$).
* **Avanzado:** 
   1. Altura ($h$): Se obtiene mediante $y \cdot (\tan 79^{\circ} + \tan 60^{\circ}) = 300 \cdot \tan 60^{\circ} \rightarrow y \approx 75.60\text{m}$. Por tanto, $h = 75.60 \cdot \tan(79^{\circ}) \approx 388.38 \text{ m}$.
   2. Costo Técnico: $388.38 \cdot 2.5 = \$970.95 \text{ USD}$.
```

---

## 🏁 Autoevaluación y Cierre

```ad-question
title: Preguntas de Verificación
1. Si un cateto forma parte del ángulo de referencia (lo toca) y no es la hipotenusa, ¿cuál es su nombre técnico?
2. Usted obtiene que el `sen(30) = -0.98`. ¿Cuál es el error técnico en su herramienta de cálculo?
3. Un ingeniero necesita una guaya de soporte que actúe como hipotenusa en un ángulo de 30° para alcanzar una altura de 5m. Si la guaya cuesta $10/m, ¿cuánto es el costo total? (Ayuda: $\text{sen}(30^{\circ}) = 0.5$).
```

**Notas para el próximo tema:**
Hemos dominado la resolución de triángulos rectángulos. Sin embargo, en la topografía real, muchos terrenos forman triángulos oblicuángulos (sin ángulos de 90°). En la siguiente clase, expandiremos nuestro arsenal con la **Ley del Seno y del Coseno**.

> [!info] 🧭 Navegación Final
> - **Tema Anterior:** [[Conceptos Básicos de Triángulos Rectángulos]]
> - **Siguiente Clase:** [[Resolución de Triángulos Oblicuángulos: Ley de Seno y Coseno]]