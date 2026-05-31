# Clase 04 — Volumen del Cilindro y la Esfera

#algebra #volumencilindro #volumenesfera

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 4 de 4

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [[Clase 03 — Volumen del Prisma y la Pirámide]]
> 🏠 **Inicio:** [[00 - Índice del curso]]
> ➡️ **Siguiente:** Final del Bloque 1

---

> [!info] 🌍 Relevancia y aplicaciones
> El cálculo de volúmenes es fundamental para cuantificar el espacio tridimensional y la capacidad de almacenamiento, permitiendo transformar medidas teóricas en datos logísticos y económicos reales.
> - **💵 Aplicación USD:** Determinar con precisión el costo de llenar depósitos industriales de combustible según su volumen en $m^3$.
> - **🏗️ Aplicación práctica:** Diseño y optimización de infraestructuras como silos de almacenamiento de granos o tanques hidroneumáticos.
> - **📊 Situación cotidiana:** Desde calcular la cantidad de gas en un balón deportivo hasta el volumen exacto de líquido en una lata de refresco.

---

### 3. Conceptos Clave

> [!note] 📌 ¿Qué es el Volumen del Cilindro y la Esfera?
> 
> - **Cilindro:** Es un sólido geométrico con dos bases circulares paralelas y congruentes. Su volumen se define como el producto del área de la base ($A_b$) por la altura ($h$). Dado que la base siempre es un círculo, sustituimos $A_b$ por $\pi \cdot r^2$:
>   $$V = A_b \cdot h \implies V = \pi \cdot r^2 \cdot h$$
> 
> - **Esfera:** Es un sólido perfectamente redondeado donde todos los puntos de su superficie equidistan del centro. El volumen depende únicamente de la medida del radio ($r$):
>   $$V = \frac{4}{3} \cdot \pi \cdot r^3$$
> 
> **Nota técnica sobre $\pi$:** Para cálculos escolares usamos $\pi \approx 3.1416$. Si utilizas la tecla $\pi$ de una calculadora científica, los decimales finales pueden variar ligeramente debido a la mayor precisión del dispositivo.

> [!warning] ⚠️ Error común
> 1. **Diámetro vs. Radio:** Es frecuente olvidar dividir el diámetro entre 2 antes de aplicar las fórmulas. Siempre opera con el radio ($r$).
> 2. **Potencias:** En la esfera, el radio debe elevarse **al cubo** ($r^3$). Un error típico es multiplicarlo por 3 o elevarlo solo al cuadrado.
>    - Correcto: $5^3 = 5 \cdot 5 \cdot 5 = 125$.
>    - Incorrecto: $5 \cdot 3 = 15$.

> [!tip] 💡 Truco
> Para no dudar en el examen: el volumen siempre mide el "espacio ocupado". Por ello, el resultado debe expresarse obligatoriamente en **unidades cúbicas** ($cm^3, m^3, mm^3$). Si multiplicas tres dimensiones (o una unidad al cuadrado por una lineal), obtienes un cubo.

---

### 4. Procedimientos Paso a Paso

#### Para el Cilindro
```text
PASO 1 → Identificar si se cuenta con el área de la base (Ab) o el radio (r).
PASO 2 → Si se tiene el radio, calcular el área del círculo: π · r².
PASO 3 → Multiplicar el área de la base por la altura (h).
```

#### Para la Esfera
```text
PASO 1 → Identificar el radio. Si el dato es el diámetro, dividir entre 2.
PASO 2 → Elevar el radio al cubo (r · r · r).
PASO 3 → Multiplicar el resultado por 4, multiplicar por π (3.1416) y dividir entre 3.
```

---

### 5. Ejemplos Desarrollados

> [!example] **Ejemplo 1: Cilindro con Área de Base conocida**
> **Datos:** $A_b = 20 \text{ cm}^2$ | $h = 15 \text{ cm}$
> $$V = 20 \text{ cm}^2 \cdot 15 \text{ cm}$$
> **Resultado:** $300 \text{ cm}^3$

> [!example] **Ejemplo 2: Esfera con Radio**
> **Datos:** $r = 5 \text{ cm}$
> 1. Elevar al cubo: $5^3 = 125$
> 2. Aplicar fórmula: $V = \frac{4 \cdot 3.1416 \cdot 125}{3}$
> 3. Operación: $V = \frac{1570.8}{3}$
> **Resultado:** $523.6 \text{ cm}^3$

> [!example] **Ejemplo 3: Esfera con Diámetro**
> **Datos:** $D = 32 \text{ m}$
> 1. Obtener radio: $r = \frac{32}{2} = 16 \text{ m}$
> 2. Elevar al cubo: $16^3 = 4096$
> 3. Operar: $V = \frac{4 \cdot 3.1416 \cdot 4096}{3}$
> **Resultado:** $17157.3 \text{ m}^3$

> [!example] **Ejemplo 4: Aplicación USD (Cilindro)**
> **Situación:** Un tanque cilíndrico de radio $25 \text{ m}$ y altura $13 \text{ m}$ contiene gas. El costo es de $0.50 \text{ USD}$ por $m^3$.
> 1. Volumen: $V = 3.1416 \cdot (25)^2 \cdot 13$
> 2. $V = 3.1416 \cdot 625 \cdot 13 = 25525.5 \text{ m}^3$
> 3. Costo total: $25525.5 \cdot 0.50$
> **Resultado:** $12762.75 \text{ USD}$

---

### 6. Ejercicios para el Estudiante

**Nivel Verde (Fácil)**
1. Cilindro: $A_b = 10 \text{ cm}^2$, $h = 5 \text{ cm}$.
2. Cilindro: $A_b = 45 \text{ m}^2$, $h = 10 \text{ m}$.
3. Esfera: $r = 3 \text{ cm}$.
4. Esfera: $r = 1 \text{ m}$.

**Nivel Amarillo (Medio)**
5. Cilindro: $r = 2 \text{ cm}$, $h = 10 \text{ cm}$.
6. Esfera: $d = 10 \text{ cm}$.
7. Cilindro: $d = 4 \text{ m}$, $h = 5 \text{ m}$.
8. Esfera: $d = 2 \text{ m}$.

**Nivel Rojo (Avanzado)**
9. Un cilindro con $r = 3 \text{ m}$ y $h = 10 \text{ m}$ se llena con un líquido de $1.20 \text{ USD}/m^3$. ¿Costo total?
10. Una esfera con $r = 2 \text{ m}$ contiene gas de $2.00 \text{ USD}/m^3$. ¿Valor del contenido?
11. Tanque cilíndrico de $d = 10 \text{ m}$ y $h = 2 \text{ m}$. Costo de llenado: $0.75 \text{ USD}/m^3$.
12. Canica esférica de $d = 6 \text{ cm}$. Material: $0.10 \text{ USD}/cm^3$.

> [!success] **Respuestas**
> 1. $50 \text{ cm}^3$ | 2. $450 \text{ m}^3$ | 3. $113.1 \text{ cm}^3$ | 4. $4.19 \text{ m}^3$
> 5. $125.66 \text{ cm}^3$ | 6. $523.6 \text{ cm}^3$ | 7. $62.83 \text{ m}^3$ | 8. $4.19 \text{ m}^3$
> 9. $339.29 \text{ USD}$ | 10. $67.02 \text{ USD}$ | 11. $117.81 \text{ USD}$ | 12. $11.31 \text{ USD}$

---

### 7. Mini-Prueba de Autoevaluación

> [!question] **Pregunta 1**
> Si el diámetro de una esfera es de $20 \text{ cm}$, ¿qué valor debes usar para $r$ en la fórmula?
> **Respuesta:** $10 \text{ cm}$. El radio es la mitad del diámetro ($20 / 2$). Es el error más común en este tema.

> [!question] **Pregunta 2**
> ¿Cuál es el primer paso para calcular el volumen de un cilindro si solo conoces el radio de la base y la altura?
> **Respuesta:** Calcular el área de la base circular mediante la fórmula $\pi \cdot r^2$.

> [!question] **Pregunta 3**
> Si una esfera tiene un volumen de $1 \text{ m}^3$ y el material cuesta $10 \text{ USD}$ por $m^3$, ¿cuál es el costo total?
> **Respuesta:** $10 \text{ USD}$. Se multiplica el volumen total ($1 \text{ m}^3$) por el precio unitario ($10 \text{ USD}/m^3$).

---

> [!tip] 💡 En la próxima clase
> ¡Felicidades! Has completado el estudio de los volúmenes principales. Con esto finalizamos el bloque de figuras tridimensionales y estamos listos para el cierre del curso.

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [[Clase 03 — Volumen del Prisma y la Pirámide]]
> 🏠 **Inicio:** [[00 - Índice del curso]]
> ➡️ **Siguiente:** Final del Bloque 1