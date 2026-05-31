# 📖 Guía de estudio — Clase 03: Volumen de un Prisma Recto

> [!info] 📌 Conceptos clave
> *   **Definición de Volumen:** Para cualquier prisma recto, el volumen se calcula multiplicando el **Área de la base ($A_b$)** por la **altura ($h$)** del prisma.
> *   **Identificación de la base:** El primer paso siempre es reconocer la forma geométrica de la base (triángulo, rectángulo, pentágono, etc.), ya que esto determina qué fórmula usar para hallar el $A_b$.
> *   **Unidades Cúbicas ($cm^3, m^3$):** El volumen se expresa en unidades cúbicas porque estamos multiplicando tres dimensiones (largo $\times$ ancho $\times$ alto). Matemáticamente, multiplicamos unidades cuadradas del área ($cm^2$) por una unidad lineal de altura ($cm$), resultando en $cm^3$.
> *   **Perímetro ($P$) vs. Semiperímetro ($s$):** El perímetro es la suma de todos los lados de la base. El semiperímetro ($s$) es la mitad de esa suma ($P/2$). El valor de $s$ es un requisito indispensable para aplicar la **Fórmula de Herón** en triángulos donde no conocemos la altura de la base.

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Volumen del prisma** | $V = A_b \times h$ |
| **Área de polígono regular** | $A_b = \frac{P \times Ap}{2}$ |
| **Área de triángulo (Herón)** | $A_b = \sqrt{s(s-a)(s-b)(s-c)}$ |
| **Área de triángulo equilátero** | $A_b = \frac{\sqrt{3} \times L^2}{4}$ |
| **Semiperímetro ($s$)** | $s = \frac{a+b+c}{2}$ |

**Leyenda de variables:**
*   $A_b$: Área de la base.
*   $P$: Perímetro de la base.
*   $Ap$: Apotema (distancia del centro al medio de un lado).
*   $L$: Medida del lado en polígonos regulares.
*   $a, b, c$: Medidas de los lados de un triángulo.
*   $s$: Semiperímetro.

## Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A: Caso Básico (Prisma Rectangular)
Calcula el volumen de un prisma cuya base es un rectángulo de $7 \, cm$ de largo y $3 \, cm$ de ancho, con una altura total de $9 \, cm$.

*   **Paso 1: Calcular el área de la base ($A_b$):**
    Como la base es un rectángulo, multiplicamos sus dos dimensiones:
    $A_b = 7 \, cm \times 3 \, cm = 21 \, cm^2$.
*   **Paso 2: Calcular el volumen total ($V$):**
    Multiplicamos el área obtenida por la altura del prisma ($h$):
    $V = 21 \, cm^2 \times 9 \, cm = 189 \, cm^3$.
```

```ad-example
title: Ejemplo B: Aplicación Real (Contenedor Hexagonal)
Un contenedor industrial tiene forma de prisma hexagonal regular. El lado de la base mide $12 \, cm$, su apotema es de $10.4 \, cm$ y la altura del contenedor es de $19 \, cm$. Si el costo de llenado es de **$0.50 USD por cada $100 \, cm^3$**, ¿cuál es el costo total?

*   **Paso 1: Área de la base ($A_b$):**
    Primero hallamos el perímetro ($P$): $12 \, cm \times 6 = 72 \, cm$.
    Luego aplicamos la fórmula: $A_b = \frac{72 \, cm \times 10.4 \, cm}{2} = 374.4 \, cm^2$.
*   **Paso 2: Volumen total ($V$):**
    $V = 374.4 \, cm^2 \times 19 \, cm = 7113.6 \, cm^3$.
*   **Paso 3: Cálculo de costo:**
    1. Dividimos el volumen total por $100$ para saber cuántos grupos de $100 \, cm^3$ hay: $7113.6 / 100 = 71.136$.
    2. Multiplicamos esos grupos por el costo unitario: $71.136 \times 0.50 = 35.568$.
    **Resultado:** El costo total de llenado es de **$35.57 USD**.
```

## Ejercicios de Repaso

```ad-abstract
title: 🟢 Fácil: Prisma Rectangular
Determina el volumen de un prisma rectangular con las siguientes dimensiones:
*   Base: $6 \, m$
*   Ancho: $3 \, m$
*   Altura del prisma ($h$): $16 \, m$

**Paso 1:** Halla el área de la base ($A_b$).
**Paso 2:** Halla el volumen total ($V$).

*(Respuesta esperada: $A_b = 18 \, m^2$; $V = 288 \, m^3$)*
```

```ad-abstract
title: 🟡 Medio: Prisma Pentagonal
Halla el área de la base y el volumen de un prisma pentagonal (5 lados) con estos datos:
*   Lado de la base ($L$): $10 \, cm$
*   Apotema ($Ap$): $6.9 \, cm$
*   Altura del prisma ($h$): $15 \, cm$

*(Respuesta esperada: $A_b = 172.5 \, cm^2$; $V = 2587.5 \, cm^3$)*
```

```ad-abstract
title: 🔴 Avanzado: Aplicación con USD
Un envase de perfume tiene forma de prisma triangular con lados de base de $9 \, cm$, $8 \, cm$ y $11 \, cm$. La altura del envase es de $15 \, cm$. 
1. Calcula el área de la base usando la fórmula de Herón ($s = 14 \, cm$).
2. Calcula el volumen total.
3. Determina el costo de llenado si el líquido cuesta **$0.05 USD por cada $cm^3$**.

*(Respuesta esperada: $A_b \approx 35.5 \, cm^2$; $V = 532.5 \, cm^3$; Costo = $26.63 USD)*
```

> [!tip] 💡 Consejo de estudio
> El error más común es confundir la altura de la base (en triángulos) o la apotema (en polígonos) con la altura del prisma ($h$). **Estrategia pedagógica:** Dibuja la base por separado, calcula su área y, solo cuando tengas ese resultado, multiplícalo por la altura del prisma. ¡No olvides verificar que todas tus medidas estén en la misma unidad antes de empezar!