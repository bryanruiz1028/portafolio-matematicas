# Clase 04 — Pythagorean Theorem | Area of ​​an equilateral triangle given its height + Perimeter and area of ​​an equilateral triangle | Application of the Pythagorean Theorem

#algebra #pythagoreantheo

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [Clase 03 — Aplicaciones Básicas del Teorema de Pitágoras]
> ⬆️ **Índice:** [Curso de Geometría y Álgebra]
> ➡️ **Siguiente:** [Clase 05 — Áreas en Polígonos Regulares y Apotema]

---

## 1. ¿Por qué es importante esta clase?
Dominar el cálculo de dimensiones en triángulos equiláteros nos permite revelar medidas "ocultas", como la altura $h$, partiendo únicamente de un lado $L$ conocido. Esta habilidad es fundamental para resolver problemas donde no podemos medir directamente el centro de una figura, pero necesitamos conocer su superficie total para aplicaciones técnicas y financieras.

*   **💵 Aplicación con $USD$:** Imagina que debes fabricar una placa conmemorativa de acero en forma de triángulo equilátero. Si el material cuesta $\$50 \text{ USD}$ por metro cuadrado, calcular el área exacta mediante Pitágoras evitará que compres material de más o de menos.
*   **🏗️ Aplicación práctica:** En arquitectura, el diseño de estructuras de soporte y techos de dos aguas utiliza triángulos equiláteros para distribuir cargas; conocer la altura $h$ exacta es vital para determinar la longitud de las vigas de soporte.
*   **📊 Situación cotidiana:** Al delimitar zonas de juego o diseñar jardines, conocer el área total a partir de un solo lado te permite presupuestar con precisión recursos como rollos de césped artificial o galones de pintura.

---

## 2. Concepto clave

> [!note] 📌 ¿Qué es Pythagorean Theorem?
> Es una herramienta matemática que establece que en cualquier triángulo rectángulo, la suma de los cuadrados de los catetos es igual al cuadrado de la hipotenusa ($a^2 + b^2 = c^2$). 
> 
> En un **triángulo equilátero**, todos los lados son iguales. Cuando trazamos la altura, esta actúa como una línea simétrica que divide el triángulo en dos triángulos rectángulos perfectos. La propiedad fundamental es que **la altura divide la base exactamente en dos partes iguales**.

> [!warning] ⚠️ ¡Cuidado con la trampa!
> Un error muy común es intentar aplicar el teorema usando el lado completo del triángulo equilátero como la base del triángulo rectángulo. ¡No lo hagas! Para que el cálculo sea correcto, debes usar solo **la mitad de la base** ($L/2$), ya que es ahí donde se forma el ángulo de $90^\circ$.

> [!tip] 💡 Tu superpoder matemático
> Para no confundirte nunca, recuerda: **La hipotenusa siempre es la reina**. En este escenario, el lado original del triángulo equilátero ($L$) siempre será el lado más largo del triángulo rectángulo, es decir, la hipotenusa ($c$). La altura ($h$) y la mitad de la base ($L/2$) siempre serán los catetos ($a$ y $b$).

---

## 3. Procedimiento paso a paso

```text
1. Identificar datos: Determinar si el problema entrega el lado L (hipotenusa) o la altura h (cateto).
2. Dividir la base: Calcular la mitad del lado (L/2) para obtener la base del triángulo rectángulo.
3. Asignar roles y aplicar Pitágoras: 
   - Definir c = L, a = h, y b = L/2. 
   - Sustituir en a² + b² = c² para despejar la variable desconocida.
4. Cálculos finales: 
   - Perímetro (P) = 3 * L
   - Área (A) = (Base Total * Altura) / 2
```

---

## 4. Ejemplos de aplicación

**Ejemplo 1 (Caso Básico - Lado conocido):**
Dado un triángulo equilátero con un lado $L = 10 \text{ cm}$:
1.  La base del triángulo rectángulo es $5 \text{ cm}$ (la mitad de $10$).
2.  Planteamos Pitágoras ($a^2 + b^2 = c^2$): $h^2 + 5^2 = 10^2$.
3.  Calculamos: $h^2 + 25 = 100 \Rightarrow h^2 = 75$.
4.  Altura: $h = \sqrt{75} \approx 8.66 \text{ cm}$.
5.  Área: $(10 \text{ cm} \cdot 8.66 \text{ cm}) / 2 = 43.30 \text{ cm}^2$.

**Ejemplo 2 (Configuración Algebraica):**
Si solo conocemos la altura, usamos un truco algebraico: llamamos a la mitad de la base $x$. Como el triángulo es equilátero, el lado completo (la hipotenusa) mide $2x$. ¡Así, la hipotenusa será siempre el doble de la base del triángulo rectángulo, simplificando el despeje!

**Ejemplo 3 (Caso Avanzado - Altura conocida):**
Si la altura $h$ es de $5 \text{ m}$:
1.  Planteamos usando el truco del ejemplo anterior: $x^2 + 5^2 = (2x)^2$.
2.  Resolvemos potencias: $x^2 + 25 = 4x^2$.
3.  Despejamos $x$: $25 = 3x^2 \Rightarrow x^2 = 25/3 \Rightarrow x = \sqrt{8.33} \approx 2.88 \text{ m}$.
4.  La base completa es $L = 2x = 5.76 \text{ m}$.
5.  Área final: $(5.76 \text{ m} \cdot 5 \text{ m}) / 2 = 14.40 \text{ m}^2$.

**Ejemplo 4 (Aplicación real $USD$):**
Se debe imprimir un banner triangular equilátero de lado $L = 4 \text{ m}$. El costo es de $\$15 \text{ USD}$ por $m^2$.
1.  Hallamos altura: $2^2 + h^2 = 4^2 \Rightarrow 4 + h^2 = 16 \Rightarrow h = \sqrt{12} \approx 3.46 \text{ m}$.
2.  Área: $(4 \cdot 3.46) / 2 = 6.92 \text{ m}^2$.
3.  Costo total: $6.92 \cdot 15 = \$103.80 \text{ USD}$.

> [!info] 📚 Curiosidad Matemática
> ¿Sabías que existe una fórmula directa para el área de un triángulo equilátero que no requiere hallar la altura primero? Es $Area = \frac{\sqrt{3}}{4} \cdot L^2$. También puedes usar la **Fórmula de Herón** si conoces todos los lados. ¡Exploralas para verificar tus resultados!

---

## 5. Ejercicios para el estudiante

### 🟢 Fácil (Lados enteros)
1.  Calcula $P$ y $A$ de un triángulo equilátero de lado $6 \text{ cm}$.
2.  Calcula $P$ y $A$ de un triángulo equilátero de lado $12 \text{ cm}$.
3.  Calcula $P$ y $A$ de un triángulo equilátero de lado $8 \text{ cm}$.
4.  Calcula $P$ y $A$ de un triángulo equilátero de lado $20 \text{ cm}$.

### 🟡 Medio (Dada la altura)
*En estos ejercicios, encuentra primero el lado $L$ y luego el área $A$.*
5.  Halla $L$ y $A$ si la altura $h = 10 \text{ cm}$.
6.  Halla $L$ y $A$ si la altura $h = 15 \text{ cm}$.
7.  Halla $L$ y $A$ si la altura $h = 3 \text{ m}$.
8.  Halla $L$ y $A$ si la altura $h = 7.5 \text{ cm}$.

### 🔴 Avanzado (Aplicación $USD$)
9.  Un jardín equilátero tiene un lado de $10 \text{ m}$. El metro de cerca cuesta $\$12 \text{ USD}$ y el césped $\$8 \text{ USD}$ por $m^2$. Calcula el costo total (cerca + césped).
10. Una señal de tránsito equilátera tiene $h = 60 \text{ cm}$. Si el metal cuesta $\$0.05 \text{ USD}$ por $cm^2$, ¿cuánto cuesta el material?
11. Se fabrica una carpa equilátera de lado $L = 3 \text{ m}$. La lona del piso cuesta $\$22 \text{ USD}$ por $m^2$. Calcula el costo total del piso.
12. Un logo equilátero tiene $h = 12 \text{ cm}$. El grabado láser cuesta $\$2 \text{ USD}$ por $cm^2$. Calcula el presupuesto total.

> [!success] Soluciones para el docente (Cálculos con 2 decimales)
> 1. $P=18\text{ cm}, A=15.58\text{ cm}^2$ | 2. $P=36\text{ cm}, A=62.35\text{ cm}^2$
> 3. $P=24\text{ cm}, A=27.71\text{ cm}^2$ | 4. $P=60\text{ cm}, A=173.20\text{ cm}^2$
> 5. $L=11.54\text{ cm}, A=57.70\text{ cm}^2$ | 6. $L=17.32\text{ cm}, A=129.90\text{ cm}^2$
> 7. $L=3.46\text{ m}, A=5.19\text{ m}^2$ | 8. $L=8.66\text{ cm}, A=32.47\text{ cm}^2$
> 9. Cerca: $\$360$, Césped: $\$346.40$, Total: $\$706.40 \text{ USD}$
> 10. $L=69.28\text{ cm}, A=2078.40\text{ cm}^2$, Costo: $\$103.92 \text{ USD}$
> 11. $h=2.60\text{ m}, A=3.90\text{ m}^2$, Costo: $\$85.80 \text{ USD}$
> 12. $L=13.86\text{ cm}, A=83.16\text{ cm}^2$, Costo: $\$166.32 \text{ USD}$

---

## 6. Mini-prueba de autoevaluación

> [!question] Pregunta 1: Conceptual
> En un triángulo equilátero de lado $L$, ¿por qué no podemos usar $L$ como base en la fórmula de Pitágoras?
> **Respuesta:** Porque el Teorema de Pitágoras solo funciona en triángulos rectángulos. Al trazar la altura, el triángulo se divide, y la base del nuevo triángulo rectángulo es exactamente la mitad, es decir, $L/2$.

> [!question] Pregunta 2: Procedimental
> Si un triángulo equilátero tiene lado $L = 2 \text{ m}$, ¿cuál es su altura exacta?
> **Respuesta:** $\sqrt{3} \text{ m}$ (aprox. $1.73 \text{ m}$). Cálculo: $1^2 + h^2 = 2^2 \Rightarrow 1 + h^2 = 4 \Rightarrow h = \sqrt{3}$.

> [!question] Pregunta 3: Aplicación $USD$
> Una placa triangular equilátera de lado $L = 2 \text{ m}$ cuesta $\$100 \text{ USD}$ por $m^2$. ¿Cuál es el presupuesto total?
> **Respuesta:** $\$173.00 \text{ USD}$. Como la altura es $1.73 \text{ m}$, el área es $(2 \cdot 1.73)/2 = 1.73 \text{ m}^2$. Al multiplicar por $\$100$, obtenemos el costo.

---

## 7. Notas para el próximo tema y navegación final

> [!tip] Conexión con el siguiente nivel
> Comprender la altura de un triángulo equilátero es el primer paso para dominar los **polígonos regulares**. En la próxima clase, veremos cómo esta altura se convierte en la **apotema**, la pieza clave para calcular el área de hexágonos y otras figuras complejas. ¡No te lo pierdas!

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [Clase 03 — Aplicaciones Básicas del Teorema de Pitágoras]
> ⬆️ **Índice:** [Curso de Geometría y Álgebra]
> ➡️ **Siguiente:** [Clase 05 — Áreas en Polígonos Regulares y Apotema]