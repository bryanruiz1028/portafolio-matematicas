# Clase 03 — What is pi? + Perimeter of the circle + Área del Círculo + Area and Perimeter of a Regular Polygon

#algebra #whatispi
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 7

```ad-info
title: 🧭 Navegación
*   Anterior: [[Clase 02]]
*   Índice: [[00 - Índice del curso]]
*   Siguiente: [[Clase 04]]
```

---

```ad-info
title: 🌍 Relevancia y aplicaciones
Entender la relación de $\pi$ y las propiedades de los polígonos nos permite calcular con precisión dimensiones y costos de materiales en objetos circulares y poligonales de nuestra vida diaria.

*   **💵 Aplicación con USD:** Imagina que quieres instalar un piso de cerámica en un patio hexagonal. Calcular el área exacta te permite comprar solo el material necesario, ahorrando dinero si el metro cuadrado cuesta $\$25.00$ USD.
*   **🏗️ Aplicación práctica:** Los ingenieros utilizan estos cálculos para diseñar la rotación de engranajes en motores, la resistencia de columnas arquitectónicas y el aerodinamismo de las ruedas.
*   **📊 Situación cotidiana:** ¿Alguna vez te has preguntado si conviene más una pizza grande o dos medianas? Al calcular el área (la superficie de comida) y compararla con el precio, puedes tomar la mejor decisión económica.
```

---

## Análisis Temático: Conceptos Clave

```ad-note
title: 📌 ¿Qué es Pi ($\pi$)?
El número $\pi$ (pi) es una **relación constante**. Representa cuántas veces cabe el diámetro de un círculo dentro de su propia circunferencia (el borde). No importa el tamaño del círculo, si divides la longitud de la circunferencia ($C$) entre su diámetro ($d$), siempre obtendrás el mismo valor: $\pi \approx 3.1416$.
```

```ad-warning
title: ⚠️ Error común
1. **Confundir Perímetro y Área:** Recuerda que la **circunferencia** es el borde (una línea de longitud) y se mide en unidades simples ($\text{cm}$, $\text{m}$). El **círculo** es la superficie interna (área) y se mide en unidades cuadradas ($\text{cm}^2$, $\text{m}^2$). ¡No olvides poner el exponente $2$ en tus respuestas de área!
2. **Orden de operaciones:** En la fórmula $A = \pi \cdot r^2$, **primero** debes elevar el radio al cuadrado ($r \cdot r$) y **después** multiplicar por $3.1416$.
```

```ad-tip
title: 💡 Truco para recordarlo
Para visualizar $\pi$, imagina que el diámetro es una cuerda recta. Si intentas rodear el círculo con ella, notarás que necesitas **3 cuerdas completas y un pedacito más** (ese pedacito es el $.1416$) para dar la vuelta entera.
```

---

## Procedimiento Paso a Paso

```text
Sigue estos 4 pasos para resolver cualquier problema de geometría circular o poligonal:

1. IDENTIFICAR DATOS: Determina si tienes el Radio (r) o el Diámetro (d). 
   ¡Ojo!: Si te dan el diámetro para un área, divídelo entre 2 para obtener el radio.
2. SELECCIONAR FÓRMULA:
   • Círculo (Perímetro/Circunferencia): C = 2 · π · r  (o C = π · d)
   • Círculo (Área): A = π · r²
   • Polígono Regular: Perímetro (P) = n · L | Área = (P · a) / 2
3. SUSTITUIR VALORES: Cambia las letras por números usando π ≈ 3.1416.
4. OPERAR Y ETIQUETAR: Resuelve las operaciones (potencias primero) y asigna
   las unidades correctas (lineales para perímetro, cuadradas para área).
```

---

## Ejemplos Prácticos de Aplicación

```ad-example
title: Ejemplo 1: Círculo Básico (Perímetro)
**Problema:** Hallar el perímetro de una circunferencia con un radio ($r$) de $10 \text{ cm}$.
*   **Fórmula:** $C = 2 \cdot \pi \cdot r$
*   **Sustitución:** $C = 2 \cdot 3.1416 \cdot 10$
*   **Resultado:** $62.832 \text{ cm}$
```

```ad-example
title: Ejemplo 2: Círculo con Diámetro (Área)
**Problema:** Hallar el área de un círculo cuyo diámetro ($d$) es de $32 \text{ m}$.
*   **Paso clave (Lógica):** Como el diámetro es $32$, el radio es la mitad: $r = 16 \text{ m}$.
*   **Fórmula:** $A = \pi \cdot r^2$
*   **Sustitución:** $A = 3.1416 \cdot (16)^2 \rightarrow A = 3.1416 \cdot 256$
*   **Resultado:** $804.2496 \text{ m}^2$
*   **Nota:** Si usas el $32$ directamente, estarías calculando el área de un círculo mucho más grande. Siempre usa el radio.
```

```ad-example
title: Ejemplo 3: Polígono Regular (Hexágono)
**Problema:** Hallar el perímetro y el área de un hexágono regular con lado $L = 15 \text{ cm}$ y apotema $a = 13 \text{ cm}$.
*   **Perímetro:** $P = 6 \text{ lados} \cdot 15 \text{ cm} = 90 \text{ cm}$.
*   **Área:** $A = (P \cdot a) / 2 \rightarrow A = (90 \cdot 13) / 2 = 1170 / 2$.
*   **Resultado:** $585 \text{ cm}^2$
```

```ad-example
title: Ejemplo 4: Aplicación en USD (Cerca de Jardín)
**Problema:** Se desea cercar un jardín circular con un radio de $4 \text{ m}$. Si el metro de cerca cuesta $\$15.50 \text{ USD}$, ¿cuánto cuesta el proyecto?
*   **Circunferencia:** $C = 2 \cdot 3.1416 \cdot 4 = 25.1328 \text{ m}$.
*   **Costo total:** $25.1328 \text{ m} \cdot 15.50 \text{ USD/m} = \$389.5584 \text{ USD}$.
```

---

## Bloque de Ejercicios

```ad-abstract
title: 🟢 Nivel Fácil: Círculos Directos
1. Calcula la circunferencia de un círculo con $r = 5 \text{ cm}$.
2. Calcula el área de un círculo con $r = 14 \text{ m}$.
3. Halla el perímetro de un círculo si su diámetro es $10 \text{ cm}$.
4. Halla el área de un círculo si su diámetro es $20 \text{ m}$.
```

```ad-abstract
title: 🟡 Nivel Medio: Polígonos Regulares
1. Un pentágono regular tiene un lado de $16 \text{ m}$ y una apotema de $11 \text{ m}$. Calcula su área.
2. Calcula el perímetro de un octágono regular si cada lado mide $10 \text{ cm}$.
3. Halla el área de un hexágono regular con lado de $20 \text{ cm}$ y apotema de $17.32 \text{ cm}$.
4. Un pentágono tiene un perímetro de $80 \text{ m}$. ¿Cuánto mide cada lado?
```

```ad-abstract
title: 🔴 Nivel Avanzado: Aplicaciones USD
1. **Lona de piscina:** Se debe cubrir una piscina circular de $6 \text{ m}$ de diámetro. Si la lona cuesta $\$20 \text{ USD}$ por $\text{m}^2$, ¿cuál es el costo total?
2. **Borde de lujo:** Un reloj circular tiene un radio de $15 \text{ cm}$. El borde de oro cuesta $\$5 \text{ USD}$ por cada centímetro. ¿Cuál es el costo del borde?
3. **Piso hexagonal:** Un salón hexagonal tiene lados de $10 \text{ m}$ y apotema de $8.66 \text{ m}$. Si pintar el piso cuesta $\$12 \text{ USD}$ por $\text{m}^2$, ¿cuánto se gastará?
4. **Valla metálica:** Un parque circular tiene un diámetro de $20 \text{ m}$. Si la valla cuesta $\$18.75 \text{ USD}$ por metro lineal, ¿cuál es el presupuesto?
```

```ad-success
title: Soluciones (Usando π = 3.1416)
**Fácil:** 
1) $31.416 \text{ cm}$ | 2) $615.7536 \text{ m}^2$ | 3) $31.416 \text{ cm}$ | 4) $314.16 \text{ m}^2$
**Medio:** 
1) $440 \text{ m}^2$ | 2) $80 \text{ cm}$ | 3) $1039.2 \text{ cm}^2$ | 4) $16 \text{ m}$
**Avanzado:** 
1) Área: $28.2744 \text{ m}^2$ | Costo: $\$565.488 \text{ USD}$
2) Perímetro: $94.248 \text{ cm}$ | Costo: $\$471.24 \text{ USD}$
3) Área: $259.8 \text{ m}^2$ | Costo: $\$3117.60 \text{ USD}$
4) Perímetro: $62.832 \text{ m}$ | Costo: $\$1178.10 \text{ USD}$
```

---

## Autoevaluación y Cierre

```ad-question
title: Pregunta 1
¿Cuál es la definición matemática de $\pi$?
a) El radio elevado al cuadrado.
b) La relación (división) entre la circunferencia y el diámetro.
c) El área de un polígono dividido entre su apotema.
d) La suma del radio y el diámetro.
```

```ad-question
title: Pregunta 2
Según la jerarquía de operaciones, ¿qué debes hacer primero para calcular el área de un círculo?
a) Multiplicar $\pi$ por el radio.
b) Dividir el radio entre dos.
c) Elevar el radio al cuadrado.
d) Multiplicar el diámetro por $3.1416$.
```

```ad-question
title: Pregunta 3
Tienes un terreno circular con un **diámetro** de $10 \text{ m}$. Si el césped sintético cuesta $\$2 \text{ USD}$ por metro cuadrado ($\text{m}^2$), ¿cuál es el costo para cubrirlo?
a) $\$314.16 \text{ USD}$
b) $\$62.83 \text{ USD}$
c) $\$157.08 \text{ USD}$
d) $\$20.00 \text{ USD}$
```

### Notas para el próximo tema
¡Felicidades! Has dominado las figuras planas. En la próxima clase, daremos el salto a la tercera dimensión. Utilizaremos estas bases de área para aprender a calcular el **volumen** de cilindros, donde verás que el círculo vuelve a ser el protagonista.

```ad-info
title: 🧭 Navegación
*   Anterior: [[Clase 02]]
*   Índice: [[00 - Índice del curso]]
*   Siguiente: [[Clase 04]]
```