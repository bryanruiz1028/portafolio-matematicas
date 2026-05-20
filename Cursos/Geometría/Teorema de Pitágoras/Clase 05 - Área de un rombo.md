# Clase 05 — Área de un rombo | Conociendo su lado y 1 diagonal | Aplicación del Teorema de Pitágoras

[[Clase 04]] | [[00 - Índice del curso]]

#Geometría #TeoremaDePitágoras #ÁreaRombo #MatemáticasSecundaria

---

> [!info] 🌍 Relevancia y aplicaciones
> Dominar la triangulación en el rombo es la base para resolver geometrías complejas descomponiéndolas en figuras simples y manejables. Este método es esencial en ingeniería estructural y navegación GPS para determinar distancias y superficies mediante puntos de referencia clave. Aplicar Pitágoras aquí nos permite diseñar desde estructuras arquitectónicas precisas hasta objetos cotidianos con total exactitud matemática.
> 
> *   **💵 [USD]:** Calcular el presupuesto de lona para un estandarte romboidal conociendo solo el marco exterior y un soporte transversal.
> *   **🏗️ [Práctica]:** Diseño de cerchas en forma de rombo para puentes o techos, donde se debe calcular el material según la carga soportada.
> *   **📊 [Cotidiana]:** Cálculo exacto de papel o tela para fabricar cometas (papalotes) simétricos a partir de la longitud de las varillas.

---

### 3. Fundamentos Teóricos (Concepto Clave)

> [!note] 📌 ¿Qué es Área de un rombo?
> El área de un rombo se calcula tradicionalmente multiplicando sus dos diagonales y dividiendo el resultado entre dos ($A = \frac{D \cdot d}{2}$). Cuando solo conocemos una diagonal, nuestra estrategia didáctica consiste en transformar un "problema de rombos" en un "problema de triángulos". Debido a que las diagonales de un rombo son perpendiculares y **se cortan exactamente en su punto medio**, la figura queda dividida en 4 triángulos rectángulos iguales. Esto nos permite usar el Teorema de Pitágoras para encontrar la mitad de la diagonal que nos falta.

> [!warning] ⚠️ Error común
> ❌ **Incorrecto:** Usar el valor del cateto encontrado mediante Pitágoras directamente en la fórmula del área.
> ✅ **Correcto:** El resultado del Teorema de Pitágoras es solo la **mitad** de la diagonal. Debes multiplicar ese valor por 2 para obtener la diagonal completa ($D$ o $d$) antes de proceder al cálculo final.

> [!tip] 💡 Truco para recordarlo
> Memoriza esta rima técnica: *"Pitágoras me da la mitad, el doble me da la diagonal"*.

---

### 4. Algoritmo de Resolución (Procedimiento)

```text
PASO 1: Identificar el triángulo rectángulo interno (Hipotenusa = lado del rombo; Cateto 1 = diagonal conocida / 2).
PASO 2: Aplicar el Teorema de Pitágoras (a² + b² = c²) para hallar el cateto faltante (x).
PASO 3: Multiplicar x por 2 para obtener la longitud de la diagonal faltante (D o d).
PASO 4: Aplicar la fórmula final: Área = (D · d) / 2.
```

---

### 5. Modelado de Problemas (Ejemplos)

```ad-example
title: Ejemplo 1: Básico (Trios Pitagóricos)
**Problema:** Hallar el área de un rombo cuyo lado mide 5 cm y una de sus diagonales mide 8 cm.
**Resolución:**
1. **Extraer triángulo:** Hipotenusa = 5 cm; Cateto conocido = 4 cm (8 / 2).
2. **Pitágoras:** $x^2 + 4^2 = 5^2 \implies x^2 + 16 = 25 \implies x^2 = 9 \implies x = 3$ cm.
3. **Diagonal faltante:** $3$ cm $\cdot 2 = 6$ cm.
4. **Área:** $\frac{8 \text{ cm} \cdot 6 \text{ cm}}{2} = \mathbf{24 \text{ cm}^2}$.
```

```ad-example
title: Ejemplo 2: Con unidades de medida (Metros)
**Problema:** Hallar el área de un rombo de lado 13 m y una diagonal de 10 m.
**Resolución:**
1. **Triángulo:** Hipotenusa = 13 m; Cateto conocido = 5 m (10 / 2).
2. **Pitágoras:** $13^2 = 5^2 + x^2 \implies 169 = 25 + x^2 \implies 144 = x^2 \implies x = 12$ m.
3. **Diagonal faltante:** $12$ m $\cdot 2 = 24$ m.
4. **Área:** $\frac{24 \text{ m} \cdot 10 \text{ m}}{2} = \mathbf{120 \text{ m}^2}$.
*Nota: Siempre expresa el área en unidades al cuadrado ($m^2$).*
```

```ad-example
title: Ejemplo 3: Área y Perímetro
**Problema:** Un rombo tiene un lado de 10 cm y una diagonal de 16 cm. Hallar su perímetro y área.
**Resolución:**
1. **Perímetro:** Al tener 4 lados iguales, $P = 10 \text{ cm} \cdot 4 = \mathbf{40 \text{ cm}}$.
2. **Área:**
   - Mitad de diagonal = 8 cm.
   - Pitágoras: $10^2 = 8^2 + x^2 \implies 100 = 64 + x^2 \implies 36 = x^2 \implies x = 6$ cm.
   - Diagonal faltante = $6 \text{ cm} \cdot 2 = 12$ cm.
   - Área = $\frac{16 \cdot 12}{2} = \mathbf{96 \text{ cm}^2}$.
```

```ad-example
title: Ejemplo 4: Aplicación 💵 [USD]
**Problema:** Se diseña un vitral romboidal con un lado de 25 cm y una diagonal de 40 cm. Calcular el costo total si el vidrio cuesta $0.05 USD por $cm^2$.
**Resolución:**
1. **Pitágoras:** Hipotenusa 25, Cateto 20. $25^2 - 20^2 = 625 - 400 = 225 \implies \sqrt{225} = 15$ cm.
2. **Diagonal total:** $15 \text{ cm} \cdot 2 = 30$ cm.
3. **Área:** $\frac{40 \cdot 30}{2} = 600 \text{ cm}^2$.
4. **Costo Final:** $600 \text{ cm}^2 \cdot 0.05 \text{ USD} = \mathbf{30 \text{ USD}}$.
```

---

### 6. Práctica Independiente (Ejercicios)

```ad-abstract
title: Nivel Fácil (Cálculos enteros)
1. Lado 5 cm, Diagonal 6 cm. Hallar Área.
2. Lado 10 m, Diagonal 12 m. Hallar Área.
3. Lado 5 mm, Diagonal 8 mm. Hallar Área.
4. Lado 13 cm, Diagonal 10 cm. Hallar Área.
```

```ad-abstract
title: Nivel Medio (Raíces exactas mayores)
1. Lado 17 cm, Diagonal 16 cm. Hallar Área.
2. Lado 25 m, Diagonal 14 m. Hallar Área.
3. Lado 20 cm, Diagonal 32 cm. Hallar Área.
4. Lado 15 m, Diagonal 18 m. Hallar Área.
```

```ad-abstract
title: Nivel Avanzado (Contexto Real y 💵 [USD])
1. Una baldosa romboidal de lado 25 cm tiene una diagonal de 30 cm. ¿Cuál es su área?
2. Un dije de joyería tiene un lado de 13 mm y una diagonal de 24 mm. Hallar su área.
3. Se construye una piscina romboidal (lado 10 m, diagonal 16 m). El revestimiento cuesta $12 USD por $m^2$. ¿Cuánto cuesta revestirla?
4. Un estandarte de lado 17 cm tiene una diagonal de 30 cm. Hallar su área y el costo de tela si cuesta $0.02 USD el $cm^2$.
```

```ad-success
title: Respuestas (Clave para el docente)
**Fácil:** 1) 24 cm², 2) 96 m², 3) 24 mm², 4) 120 cm².
**Medio:** 1) 240 cm², 2) 336 m², 3) 384 cm², 4) 216 m².
**Avanzado:** 1) 600 cm², 2) 120 mm², 3) 1,152 USD (Área: 96 m²), 4) 240 cm² / 4.8 USD.
```

---

### 7. Validación de Aprendizaje (Mini-prueba)

```ad-question
title: Pregunta 1
¿Qué propiedad geométrica de las diagonales del rombo nos garantiza que podemos formar triángulos rectángulos para aplicar Pitágoras?
```

```ad-question
title: Pregunta 2
Si al aplicar el Teorema de Pitágoras en el triángulo interno de un rombo obtienes un cateto de 9 cm, ¿cuál es el valor de la diagonal completa que debes usar en la fórmula del área?
```

```ad-question
title: Pregunta 3
Un rombo decorativo tiene un lado de 5 m y una diagonal de 6 m. Si el barniz especial cuesta $2 USD por $m^2$, ¿cuál es el presupuesto total para barnizarlo?
```

---

### 8. Cierre y Proyección

> [!tip] 💡 En la próxima clase
> Integrando lo aprendido hoy sobre el uso de Pitágoras en rombos, daremos el siguiente paso: el cálculo de **áreas de figuras compuestas** y la resolución de **polígonos regulares** mediante la apotema.

[[Clase 04]] | [[00 - Índice del curso]]