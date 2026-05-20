# Clase 02 — Área del triángulo cuando conocemos la Base y la Altura + Área y Perímetro del triangulo cuando conocemos sus 3 lados | Fórmula de Herón + Area of ​​an equilateral triangle knowing its side + Perimeter and area of ​​an equilateral triangle | Application of the Pythagorean Theorem

[Clase 01](#) | [Índice](#) | **Clase 02** | [Clase 03](#)

***

> [!info] 🧭 Relevancia y aplicaciones
> El cálculo del área de un triángulo no es solo un ejercicio matemático; es una herramienta esencial para transformar el mundo físico en números y presupuestos. Gran parte de las estructuras que nos rodean, desde el diseño de un puente hasta el plano de una casa, utilizan la geometría triangular por su estabilidad y versatilidad.
> - 💵 **Presupuestos y Finanzas:** Calcular el área exacta es el primer paso para determinar costos en $USD al comprar materiales, como metros cuadrados de césped, alfombras o baldosas.
> - 🏗️ **Construcción y Diseño:** Los ingenieros utilizan estas fórmulas para diseñar cerchas de techos y paneles solares, asegurando que el material sea suficiente para cubrir la superficie.
> - 📊 **Situaciones Cotidianas:** Si quieres remodelar un jardín de forma triangular o pintar un mural decorativo, saber el área te permite comprar la cantidad exacta de insumos sin desperdiciar dinero.

> [!note] Concepto de Área
> El área es la medida de la superficie total que ocupa una figura plana. Imagina que quieres cubrir un triángulo con cuadraditos de $1 \text{ cm} \times 1 \text{ cm}$. La fórmula estándar es $Área = \frac{Base \times Altura}{2}$. 
> **¿Por qué dividimos entre 2?** Porque cualquier triángulo es exactamente la mitad de un rectángulo que comparte su misma base y altura. ¡Es como cortar un sándwich rectangular por la mitad!

> [!warning] ¡Cuidado con estos errores comunes!
> - **❌ Olvidar las unidades:** El área siempre debe expresarse en unidades cuadradas ($cm^2, m^2, km^2$). Escribir solo "20" es incorrecto.
> - **❌ Confundir los lados:** En la fórmula básica, la altura ($h$) **no** es el lado inclinado del triángulo. La altura siempre debe medirse en un ángulo recto (90°) respecto a la base.

> [!tip] La Fórmula de Herón y el "Atajo" Equilátero
> Si no conoces la altura, pero tienes los tres lados ($a, b, c$), usa la **Fórmula de Herón**. La clave es el **Semiperímetro ($s$)**, que es simplemente la mitad del perímetro total ($s = \frac{a+b+c}{2}$).
> 
> *Dato extra:* Para triángulos equiláteros, existe una fórmula directa: $Área = \frac{L^2 \times \sqrt{3}}{4}$. Sin embargo, aprender a usar Pitágoras (como veremos abajo) te da el "superpoder" de resolver cualquier triángulo sin memorizar fórmulas complejas.

***

### 4. Procedimiento Paso a Paso

#### Método 1: Fórmula de Herón (Conociendo los 3 lados)
```text
PASO 1: Calcular el Perímetro (P) sumando los tres lados: P = a + b + c.
PASO 2: Hallar el Semiperímetro (s) dividiendo el resultado anterior: s = P / 2.
PASO 3: Calcular las diferencias de Herón: (s - a), (s - b) y (s - c).
PASO 4: Aplicar la fórmula final: Área = √[s × (s - a) × (s - b) × (s - c)].
```

#### Método 2: Triángulo Equilátero mediante Teorema de Pitágoras
```text
PASO 1: Trazar la altura (h) desde el vértice superior, dividiendo la base en dos partes iguales.
PASO 2: Identificar el triángulo rectángulo interno (Hipotenusa = Lado; Base = Lado / 2).
PASO 3: Aplicar Pitágoras para despejar la altura: (Lado)² = h² + (Lado / 2)².
PASO 4: Con el valor de "h", usar la fórmula general: Área = (Base × Altura) / 2.
*Nota: Este método es el favorito del "Profe Alex" porque fomenta el razonamiento lógico sobre la memoria.
```

***

### 5. Ejemplos Desarrollados

> [!example] Ejemplo 1 (Básico: Base y Altura)
> **Problema:** Calcula el área de un triángulo cuya base mide $8 \text{ cm}$ y su altura mide $4 \text{ cm}$.
> **Solución:** 
> $Área = \frac{Base \times Altura}{2}$
> $Área = \frac{8 \text{ cm} \times 4 \text{ cm}}{2} = \frac{32}{2} = 16 \text{ cm}^2$.

> [!example] Ejemplo 2 (Fórmula de Herón)
> **Problema:** Hallar el área de un triángulo con lados de $7 \text{ cm}, 5 \text{ cm}$ y $6 \text{ cm}$.
> **Solución:**
> 1. $P = 7 + 5 + 6 = 18 \text{ cm}$.
> 2. $s = \frac{18}{2} = 9 \text{ cm}$.
> 3. Aplicando Herón: $\sqrt{9 \times (9-7) \times (9-5) \times (9-6)} = \sqrt{9 \times 2 \times 4 \times 3} = \sqrt{216}$.
> **Resultado:** $14.69 \text{ cm}^2$. *(Cuidado: No uses el perímetro 18 en la raíz, usa siempre s = 9).*

> [!example] Ejemplo 3 (Avanzado: Triángulo Equilátero)
> **Problema:** Calcular el área de un triángulo equilátero de lado $10 \text{ cm}$ usando el Teorema de Pitágoras.
> **Solución:**
> 1. Al trazar la altura, formamos un triángulo rectángulo con base $5 \text{ cm}$ e hipotenusa $10 \text{ cm}$.
> 2. Hallamos $h$: $10^2 = h^2 + 5^2 \Rightarrow 100 = h^2 + 25 \Rightarrow h = \sqrt{75} \approx 8.66 \text{ cm}$.
> 3. $Área = \frac{10 \text{ cm} \times 8.66 \text{ cm}}{2}$.
> **Resultado:** $43.3 \text{ cm}^2$.

> [!example] Ejemplo 4 (Aplicación en USD)
> **Problema:** Un panel de vidrio triangular tiene una base de $2 \text{ m}$ y una altura de $1.5 \text{ m}$. Si el metro cuadrado de vidrio cuesta $25 \text{ USD}$, ¿cuánto cuesta el panel?
> **Solución:**
> 1. Área: $\frac{2 \text{ m} \times 1.5 \text{ m}}{2} = 1.5 \text{ m}^2$.
> 2. Costo: $1.5 \text{ m}^2 \times 25 \text{ USD} = 37.5 \text{ USD}$.
> **Resultado:** El costo total es $37.5 \text{ USD}$.

***

### 6. Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Fácil (Base/Altura)
> 1. Base = $10 \text{ cm}$, Altura = $5 \text{ cm}$.
> 2. Base = $6 \text{ cm}$, Altura = $4 \text{ cm}$.
> 3. Base = $14 \text{ m}$, Altura = $8 \text{ m}$.
> 4. Base = $15 \text{ cm}$, Altura = $4 \text{ cm}$.

> [!abstract] 🟡 Nivel Medio (Herón/Equilátero)
> 1. Hallar el área de un triángulo equilátero cuyo lado mide $6 \text{ cm}$ (usa Pitágoras).
> 2. Hallar el área usando Herón para un triángulo de lados $10, 6$ y $9$.
> 3. Calcular el área de un triángulo equilátero de lado $3.5 \text{ m}$.
> 4. Triángulo de lados $12 \text{ cm}, 15 \text{ cm}$ y $9 \text{ cm}$ (Usa Herón).

> [!abstract] 🔴 Nivel Avanzado (Aplicación $USD)
> 1. Se desea pintar una pared triangular de base $12 \text{ m}$ y altura $8 \text{ m}$. El costo de la pintura por $m^2$ es de $12 \text{ USD}$. ¿Cuánto cuesta pintar la pared?
> 2. Un terreno triangular tiene lados de $20 \text{ m}, 25 \text{ m}$ y $30 \text{ m}$. El impuesto es de $2 \text{ USD}$ por cada $m^2$. Calcula el impuesto total usando la fórmula de Herón.
> 3. Una pieza de metal triangular (equilátera) de lado $4 \text{ m}$ cuesta $100 \text{ USD}$ el $m^2$. Halla el costo total.
> 4. Se compra un jardín triangular (base $5 \text{ m}$, altura $6 \text{ m}$) por un valor total de $1500 \text{ USD}$. ¿Cuál es el costo por metro cuadrado?

> [!success] Resultados para el Docente
> **Fácil:** 1) $25 \text{ cm}^2$; 2) $12 \text{ cm}^2$; 3) $56 \text{ m}^2$; 4) $30 \text{ cm}^2$.
> **Medio:** 1) $\approx 15.59 \text{ cm}^2$; 2) $s=12.5, Área \approx 26.66 \text{ cm}^2$; 3) $\approx 5.3 \text{ m}^2$; 4) $s=18, Área = 54 \text{ cm}^2$.
> **Avanzado:** 1) $576 \text{ USD}$; 2) $s=37.5, Área \approx 248.03 \text{ m}^2, Costo \approx 496.06 \text{ USD}$; 3) $h \approx 3.46 \text{ m}, Área \approx 6.92 \text{ m}^2, Costo \approx 692 \text{ USD}$; 4) $100 \text{ USD}/m^2$.

***

### 7. Mini-prueba de Autoevaluación

> [!question] Pregunta 1: Conceptual
> ¿Por qué dividimos entre 2 en la fórmula estándar del área del triángulo?
> a) Porque el triángulo tiene 3 lados.
> b) Porque un triángulo representa la mitad de un rectángulo con su misma base y altura.
> c) Porque es una regla de la raíz cuadrada.
> d) Porque así lo indica la fórmula de Herón.
> > [!check] **Respuesta correcta: b**. Al duplicar un triángulo y unirlo por su lado inclinado, siempre obtenemos un paralelogramo o rectángulo.

> [!question] Pregunta 2: Procedimental
> Si el perímetro de un triángulo es $24 \text{ cm}$, ¿cuál es el valor de "$s$" para aplicar la fórmula de Herón?
> a) $24 \text{ cm}$
> b) $48 \text{ cm}$
> c) $12 \text{ cm}$
> d) $8 \text{ cm}$
> > [!check] **Respuesta correcta: c**. El semiperímetro ($s$) es la mitad del perímetro: $\frac{24}{2} = 12 \text{ cm}$.

> [!question] Pregunta 3: Aplicación $USD
> Un panel triangular tiene un área de $10 \text{ m}^2$. Si el costo del vidrio es de $5 \text{ USD}$ por metro cuadrado, ¿cuál es el costo total?
> a) $15 \text{ USD}$
> b) $50 \text{ USD}$
> c) $2 \text{ USD}$
> d) $25 \text{ USD}$
> > [!check] **Respuesta correcta: b**. Multiplicamos el área total por el costo unitario: $10 \text{ m}^2 \times 5 \text{ USD} = 50 \text{ USD}$.

***

> [!tip] 💡 En la próxima clase
> Ahora que eres un experto en áreas triangulares, aprenderemos a calcular el área de figuras compuestas. Verás cómo cualquier polígono complejo puede "romperse" en pequeños triángulos para facilitar su medición.

[Clase 01](#) | [Índice](#) | **Clase 02** | [Clase 03](#)