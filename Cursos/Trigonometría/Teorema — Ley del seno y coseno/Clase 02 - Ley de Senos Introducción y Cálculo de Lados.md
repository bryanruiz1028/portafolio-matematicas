tags: #algebra #lawofsines
Curso: [[00 - Índice del curso]]
Bloque 1: Trigonometría de Triángulos Oblicuángulos
Lección 2 de 9

# Clase 02 — Ley de Senos: Introducción y Cálculo de Lados

> [!info] 🧭 Navegación
> **Anterior:** [[Clase 01 - Introducción a la Trigonometría]]
> **Índice:** [[00 - Índice del curso]]
> **Siguiente:** [[Clase 03 - Ley de Senos: Cálculo de Ángulos]]

---

### 1. Relevancia y Aplicaciones Reales

> [!info] 🌍 Relevancia y aplicaciones
> La Ley de Senos es la herramienta definitiva para resolver triángulos donde no existe un ángulo recto. Permite medir distancias inaccesibles mediante la relación entre ángulos y longitudes, siendo el pilar de la topografía y la navegación moderna.
> 
> **Fila 💵 - Gestión de Costos:** Permite calcular con precisión la longitud de materiales costosos (como cables de alta tensión o vigas reforzadas) antes de la obra, evitando desperdicios de presupuesto ($USD).
> 
> **Fila 🏗️ - Arquitectura:** Es esencial para diseñar soportes y techos con inclinaciones no rectangulares, asegurando que cada ángulo de apoyo sea calculado para resistir el peso de la estructura.
> 
> **Fila 📊 - Triangulación:** Se utiliza para localizar señales de radio, barcos en alta mar o incluso para el funcionamiento de tu GPS mediante la intersección de distancias y ángulos conocidos.

---

### 2. Fundamentos Teóricos: ¿Qué es Law of Sines?

> [!note] 📌 ¿Qué es Law of Sines?
> La Ley de Senos es una relación de proporcionalidad entre las longitudes de los lados de cualquier triángulo y los senos de sus ángulos opuestos. Es especialmente útil en **triángulos oblicuángulos** (aquellos que no tienen ángulos de $90^\circ$).
> 
> **Fórmula General:**
> $$\frac{a}{\sin(A)} = \frac{b}{\sin(B)} = \frac{c}{\sin(C)}$$
> 
> > [!warning] ⚠️ Error común
> > No apliques el seno al valor del lado. El seno se aplica estrictamente al **ángulo opuesto** ($\sin(A)$). Es incorrecto escribir $\sin(a)$.
> 
> > [!tip] 💡 Truco para recordarlo: "Parejas Completas"
> > Para usar esta ley, necesitas conocer al menos una "pareja completa": un lado y su ángulo opuesto (ej. lado $a$ y ángulo $A$). Si tienes una pareja completa y cualquier otro dato, ¡puedes resolver el triángulo!

---

### 3. Procedimiento Universal para Hallar un Lado

Sigue este protocolo de cuatro pasos para garantizar resultados precisos:

```text
PASO 1: Identificar y nombrar ángulos (mayúsculas A, B, C) y sus lados opuestos (minúsculas a, b, c).
PASO 2: Localizar la "Pareja Completa" (ángulo y lado cuyos valores son conocidos).
PASO 3: Plantear la ecuación igualando la fracción de la pareja completa con la de la incógnita.
PASO 4: Despejar pasando el seno que divide a multiplicar. 
        IMPORTANTE: Verifica que tu calculadora esté en modo "Deg" o "D". 
        (Si obtienes resultados negativos o incoherentes, es probable que esté en 'Rad').
```

---

### 4. Sección de Ejemplos Guiados

```ad-example
title: Ejemplo 1 (Caso Básico)
Dado un triángulo con ángulo $A = 48^\circ$, ángulo $C = 60^\circ$ y lado $c = 15\text{ m}$. Hallar el lado $x$ (lado $a$).
1. **Pareja completa:** $c$ y $C \rightarrow \frac{15}{\sin(60^\circ)}$.
2. **Planteamiento:** $\frac{x}{\sin(48^\circ)} = \frac{15}{\sin(60^\circ)}$.
3. **Despeje:** $x = \frac{15 \cdot \sin(48^\circ)}{\sin(60^\circ)}$.
**Resultado:** $12.87\text{ m}$.
```

```ad-example
title: Ejemplo 2 (Sin dibujo)
Datos: Ángulo $A = 53^\circ$, Lado $a = 30\text{ cm}$, Ángulo $B = 42^\circ$. Hallar lado $b$.
1. **Pareja completa:** $a$ y $A \rightarrow \frac{30}{\sin(53^\circ)}$.
2. **Planteamiento:** $\frac{b}{\sin(42^\circ)} = \frac{30}{\sin(53^\circ)}$.
3. **Despeje:** $b = \frac{30 \cdot \sin(42^\circ)}{\sin(53^\circ)}$.
**Resultado:** $25.13\text{ cm}$.
```

```ad-example
title: Ejemplo 3 (Práctica del video)
Halla el valor de $x$ si su ángulo opuesto es $36^\circ$ y la pareja conocida es un lado de $14$ con un ángulo de $70^\circ$.
1. **Planteamiento:** $\frac{x}{\sin(36^\circ)} = \frac{14}{\sin(70^\circ)}$.
2. **Despeje:** $x = \frac{14 \cdot \sin(36^\circ)}{\sin(70^\circ)}$.
**Resultado:** $8.75$.
```

```ad-example
title: Ejemplo 4 (Aplicación $USD)
El lado hallado en el Ejemplo 1 ($12.87\text{ m}$) es la longitud de un cable que cuesta $5\text{ USD}$ por metro.
1. **Cálculo:** $12.87\text{ m} \times 5\text{ USD/m} = 64.35\text{ USD}$.
**Costo Total:** $64.35\text{ USD}$.
```

---

### 5. Ejercicios Prácticos

```ad-abstract
title: 🟢 Nivel Verde (Fácil - Identificación directa)
1. Dado $A = 40^\circ, a = 10\text{ cm}$ y $B = 30^\circ$, halla el lado $b$.
2. Dado $C = 80^\circ, c = 20\text{ m}$ y $A = 45^\circ$, halla el lado $a$.
3. La pareja completa es $12 / \sin(50^\circ)$. Halla $x$ si su ángulo opuesto es $25^\circ$.
4. Halla el lado $c$ si $C = 60^\circ, B = 40^\circ$ y $b = 15$.
```

```ad-abstract
title: 🟡 Nivel Amarillo (Medio - Deducción de ángulos)
*Instrucción: Utiliza la suma interna de 180° para hallar el ángulo faltante antes de aplicar la Ley de Senos.*
1. Datos: $a = 10, A = 100^\circ, B = 30^\circ$. Halla el lado $c$.
2. Datos: $b = 25, B = 45^\circ, C = 35^\circ$. Halla el lado $a$.
3. Datos: $c = 40, A = 60^\circ, B = 60^\circ$. Halla el lado $a$.
4. Un triángulo tiene ángulos de $70^\circ$ y $50^\circ$. El lado opuesto al ángulo de $70^\circ$ mide $18$. Halla el tercer lado (el opuesto al ángulo restante).
```

```ad-abstract
title: 🔴 Nivel Rojo (Avanzado - Presupuesto $USD)
1. Un arquitecto requiere vigas de madera. El lado calculado es de $8.5\text{ m}$. Si el metro cuesta $12\text{ USD}$, ¿cuál es el costo total?
2. Se requiere un cable de soporte. El ángulo opuesto al cable es de $40^\circ$, el ángulo de elevación en el otro extremo es de $55^\circ$ y la base conocida (opuesta al tercer ángulo) mide $20\text{ m}$. Halla la longitud del cable y su costo a $15\text{ USD/m}$.
3. Un terreno tiene un lado de $50\text{ m}$ opuesto a un ángulo de $45^\circ$. Se debe cercar el lado opuesto al ángulo de $60^\circ$. Si el metro de cerca cuesta $20\text{ USD}$, halla el presupuesto.
4. Halla el perímetro total de un triángulo con $A=40^\circ, B=60^\circ$ y lado $c=10$. Calcula el costo de bordearlo con cinta de seguridad de $2\text{ USD/m}$.
```

---

### 6. Solucionario para el Docente

> [!success] Respuestas Rápidas (Redondeo a 2 decimales)
> **Nivel Verde:** 1) $7.78\text{ cm}$, 2) $14.36\text{ m}$, 3) $6.62$, 4) $20.21$.
> **Nivel Amarillo:** 1) $7.78$, 2) $34.82$, 3) $40.00$, 4) $16.59$.
> **Nivel Rojo:** 1) $102\text{ USD}$, 2) $12.90\text{ m} \rightarrow 193.50\text{ USD}$, 3) $61.24\text{ m} \rightarrow 1,224.80\text{ USD}$, 4) Perímetro $\approx 25.32\text{ m} \rightarrow 50.64\text{ USD}$.

---

### 7. Autoevaluación Conceptual y Procedimental

```ad-question
title: Pregunta 1
¿Qué información mínima necesitas para empezar a usar la Ley de Senos?
```

```ad-question
title: Pregunta 2
Si el resultado de $\sin(90^\circ)$ en tu calculadora es $0.8939$ en lugar de $1$, ¿qué configuración debes cambiar para que el cálculo sea correcto?
```

```ad-question
title: Pregunta 3
Si un cable mide $10\text{ m}$ y su precio es de $12\text{ USD/m}$, ¿cuál es el presupuesto total?
```

---

### 8. Cierre y Conexión

> [!tip] 💡 En la próxima clase
> Ahora que sabes calcular longitudes, aprenderemos a encontrar **ángulos desconocidos**. Veremos cómo despejar la función seno y utilizar la tecla "Shift + Sin" ($\sin^{-1}$) en la calculadora para hallar aperturas exactas.

> [!info] 🧭 Navegación
> **Anterior:** [[Clase 01 - Introducción a la Trigonometría]]
> **Índice:** [[00 - Índice del curso]]
> **Siguiente:** [[Clase 03 - Ley de Senos: Cálculo de Ángulos]]