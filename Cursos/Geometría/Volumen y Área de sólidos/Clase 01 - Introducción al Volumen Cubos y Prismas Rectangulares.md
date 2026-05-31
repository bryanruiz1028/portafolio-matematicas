# Clase 01 — Introducción al Volumen: Cubos y Prismas Rectangulares
tags: #matematicas #volumen #geometria
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 4

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]

## 1. Importancia y Relevancia
El volumen es la magnitud que nos permite cuantificar cuánto espacio ocupa un objeto en nuestro mundo tridimensional. Comprender esta medida es fundamental porque casi todo lo que nos rodea —desde una caja de cereal hasta un edificio— tiene tres dimensiones.

*   **$USD Logística:** En el transporte internacional, las empresas cobran según el volumen del paquete (el espacio que ocupa en el avión o barco), no solo por su peso.
*   **🏗️ Construcción:** Para construir una columna, un ingeniero debe calcular el volumen exacto de la cavidad para saber cuántos metros cúbicos de concreto debe comprar.
*   **📊 Situaciones Cotidianas:** Saber el volumen nos ayuda a determinar si una nevera nueva cabrá en el hueco de la cocina o cuántas cajas podemos guardar en un depósito.

## 2. Concepto Clave y Unidades

> [!note] Definición de Volumen y Ortoedro
> El **volumen** es la cantidad de espacio que ocupa un cuerpo. Para medirlo, imaginamos cuántos "cubitos" de una unidad determinada caben dentro de la figura.
> 
> En esta clase trabajaremos con el **Ortoedro** (o prisma rectangular), que es un cuerpo con base rectangular y caras laterales que también son rectángulos.

> [!warning] Volumen vs. Capacidad y el Error Común
> 1. **Diferencia:** El volumen es el espacio que ocupa el cuerpo; la capacidad es lo que cabe dentro (conceptos similares, pero distintos).
> 2. **La Trampa de la Unidad:** Muchos estudiantes creen que un cubo de arista $2\text{ m}$ tiene un volumen de $2\text{ m}^3$. ¡Cuidado! Como veremos, un cubo de arista $2$ tiene un volumen de $8\text{ m}^3$ ($2 \times 2 \times 2$). Solo en el caso del número $1$ la arista coincide con el volumen ($1 \times 1 \times 1 = 1$).

> [!tip] Regla de las Dimensiones
> El volumen siempre se expresa en **unidades cúbicas** ($m^3$, $cm^3$, $mm^3$) porque tiene **3 dimensiones**: largo, ancho y altura. Por eso usamos el exponente "$3$".

## 3. Procedimiento General (La Analogía del Edificio)
Para calcular el volumen, utilizaremos la lógica del "Profe Alex": imaginamos que el prisma es un edificio por pisos.

```text
PASO 1: Identificar las dimensiones: largo, ancho y altura (h). 
        En cubos, todas las aristas son iguales.
PASO 2: Unificar unidades. Todas las medidas deben estar en la misma unidad.
PASO 3: Calcular el Área de la Base ($A_b$). Esto nos dice cuántos cubitos 
        hay en el "primer piso".
PASO 4: Multiplicar $A_b$ por la altura ($h$). Esto es como "apilar" los 
        pisos del edificio. Fórmula: $V = A_b \times h$
PASO 5: Expresar el resultado final en unidades cúbicas ($u^3$).
```

## 4. Ejemplos de Aplicación

*   **Ejemplo 1 (Cubo):**
    Calcula el volumen de un cubo de $3\text{ m}$ de arista.
    Como todas sus aristas miden lo mismo:
    $V = 3\text{ m} \times 3\text{ m} \times 3\text{ m} = (3\text{ m})^3 = 27\text{ m}^3$
    *Dentro de este cubo caben exactamente 27 cubitos de 1 metro por lado.*

*   **Ejemplo 2 (Ortoedro con decimales):**
    Calcula el volumen de un prisma con base de $2.5\text{ m}$ de largo, $2\text{ m}$ de ancho y $1\text{ m}$ de altura.
    $A_b = 2.5\text{ m} \times 2\text{ m} = 5\text{ m}^2$ (Hay 5 cubitos en la base).
    $V = 5\text{ m}^2 \times 1\text{ m} = 5\text{ m}^3$

*   **Ejemplo 3 (Prisma Cuadrangular):**
    Un prisma de base cuadrada ($4\text{ cm} \times 4\text{ cm}$) tiene una altura de $7.5\text{ cm}$.
    $A_b = 4\text{ cm} \times 4\text{ cm} = 16\text{ cm}^2$
    $V = 16\text{ cm}^2 \times 7.5\text{ cm} = 120\text{ cm}^3$

*   **Ejemplo 4 (Aplicación de Costos):**
    Enviar $1\text{ m}^3$ cuesta $\$50\text{ USD}$. ¿Cuánto cuesta enviar un contenedor de $2\text{ m} \times 3\text{ m} \times 2\text{ m}$?
    $V = 2\text{ m} \times 3\text{ m} \times 2\text{ m} = 12\text{ m}^3$
    $\text{Costo} = 12\text{ m}^3 \times \$50\text{ USD}/\text{m}^3 = \$600\text{ USD}$

## 5. Ejercicios Prácticos

### 🟢 Nivel Fácil
1.  Calcula el volumen de un cubo con una arista de $4\text{ m}$.
2.  Halla el volumen de un ortoedro de $5\text{ m}$ de largo, $4\text{ m}$ de ancho y $2\text{ m}$ de altura.
3.  Calcula el volumen de un cubo de arista $2\text{ m}$.
4.  Halla el volumen de un ortoedro de $12\text{ m} \times 8\text{ m} \times 3\text{ m}$.

### 🟡 Nivel Medio
1.  Calcula el volumen de un prisma cuadrangular con arista de la base de $2.2\text{ m}$ y altura de $1.5\text{ m}$.
2.  Halla el volumen de un prisma rectangular con base de $4\text{ cm} \times 3.5\text{ cm}$ y altura de $6\text{ cm}$.
3.  Calcula el volumen de un cubo de arista $8\text{ cm}$.
4.  Halla el volumen de un ortoedro de $6\text{ cm}$ de largo, $3\text{ cm}$ de ancho y $2\text{ cm}$ de altura.

### 🔴 Nivel Avanzado
1.  Si el material de relleno cuesta $\$0.05\text{ USD}$ por cada $cm^3$, ¿cuál es el costo de rellenar un cubo de $10\text{ cm}$ de arista?
2.  Un contenedor tiene un volumen de $24\text{ m}^3$. Si el largo es de $4\text{ m}$ y el ancho de $3\text{ m}$, ¿cuál es su altura?
3.  Calcula el costo de llenar un prisma cuadrangular (base $5\text{ m}$ de arista, altura $8\text{ m}$) si el contenido cuesta $\$2\text{ USD}$ por $m^3$.
4.  Un bloque sólido tiene un volumen de $6\text{ m}^3$. Si su base mide $3\text{ m} \times 2\text{ m}$, ¿cuál es su altura?

---
### ✅ Respuestas
**Fácil:** 1) $64\text{ m}^3$ | 2) $40\text{ m}^3$ | 3) $8\text{ m}^3$ | 4) $288\text{ m}^3$
**Medio:** 1) $7.26\text{ m}^3$ | 2) $84\text{ cm}^3$ | 3) $512\text{ cm}^3$ | 4) $36\text{ cm}^3$
**Avanzado:** 1) $\$50\text{ USD}$ | 2) $2\text{ m}$ | 3) $\$400\text{ USD}$ | 4) $1\text{ m}$

## 6. Autoevaluación

**1. ¿Qué representa el área de la base ($A_b$) en la analogía de los pisos de un edificio?**
a) La altura total del edificio.
b) El número de cubos de una unidad que hay en el primer piso.
c) El espacio total que ocupa el edificio.

**2. Si un cubo tiene una arista de $10\text{ cm}$, su volumen es:**
a) $30\text{ cm}^3$
b) $100\text{ cm}^3$
c) $1000\text{ cm}^3$

**3. Un ortoedro cuesta $\$50\text{ USD}$ por cada $m^3$ de espacio ocupado. Si mide $2\text{ m} \times 1\text{ m} \times 3\text{ m}$, ¿cuál es su costo total?**
a) $\$300\text{ USD}$
b) $\$150\text{ USD}$
c) $\$600\text{ USD}$

## 7. Cierre y Próximo Tema
¡Excelente trabajo! Has aprendido que el volumen de un prisma rectangular u ortoedro se reduce a entender cuántos cubos caben en la base y cuántas veces se repiten hacia arriba. Esta lógica de **"Área de la base por la altura"** es universal. En la **Clase 02**, utilizaremos este mismo principio para calcular el volumen de prismas con bases diferentes, como triángulos o hexágonos. ¡Nos vemos allí!

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]