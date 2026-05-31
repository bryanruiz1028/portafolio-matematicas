# Clase 03 — Volumen de un Prisma Recto

#algebra #volumeofarightp
[[Clase 02]] | [[Índice]] | [[Clase 04]]

> [!info] 🧭 Navegación
> **Anterior:** [[Clase 02]]
> **Inicio:** [[Índice]]
> **Siguiente:** [[Clase 04]]

---

### 1. ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> El cálculo del volumen nos permite determinar la capacidad de almacenamiento de cualquier objeto tridimensional. Es fundamental para entender cuánto espacio ocupa un cuerpo o cuánta materia puede contener.
> - **Logística y Finanzas:** Calcular el volumen de una caja para determinar el costo de envío internacional en $\$ \text{USD}$ basado en el espacio cúbico ocupado.
> - **Arquitectura:** Diseñar edificios y estructuras utilizando prismas para optimizar el espacio habitable y la eficiencia térmica.
> - **Vida Cotidiana:** Saber exactamente cuántos litros de agua necesitas para llenar una pecera o cuánta arena cabe en un contenedor de juegos.

---

### 2. Definición y Conceptos Fundamentales

> [!note] 📌 ¿Qué es el Volumen de un Prisma Recto?
> El volumen es la medida del espacio tridimensional que ocupa un prisma. Para encontrarlo, debemos calcular el área de su base ($A_b$) y multiplicarla por la altura del prisma ($h$). En términos sencillos, el volumen es el resultado de "apilar" la superficie de la base tantas veces como indique su altura.

> [!warning] ⚠️ Error común: La lógica de los exponentes
> Un error frecuente es sumar las dimensiones en lugar de multiplicarlas. Recuerda que al multiplicar unidades, sumamos sus exponentes: 
> $\text{cm}^2 \times \text{cm}^1 = \text{cm}^{(2+1)} = \text{cm}^3$. 
> El volumen **siempre** se expresa en unidades cúbicas ($u^3$).

> [!tip] 💡 Truco para recordarlo
> Imagina una **"pila de hojas de papel"**. Cada hoja representa el **Área de la base** ($A_b$). Si pones una hoja sobre otra hasta alcanzar una **Altura** ($h$), el total de papel acumulado representa el **Volumen** ($V$).

---

### 3. Procedimiento Universal

Para calcular el volumen de cualquier prisma recto, sigue este proceso lógico de 4 pasos:

```text
1. Identificar la forma de la base (rectángulo, hexágono, triángulo, etc.).
2. Calcular el área de dicha base (Ab) usando la fórmula correcta para esa figura.
3. Identificar la altura del prisma (h) (la distancia entre las dos bases).
4. Multiplicar Ab × h y asignar el resultado en unidades cúbicas (u³).
```

---

### 4. Ejemplos Prácticos

> [!example] Ejemplo 1: Base Rectangular (Cálculo Básico)
> **Datos:** Base de $7 \, \text{cm} \times 3 \, \text{cm}$, altura del prisma ($h$) de $9 \, \text{cm}$.
> 1. **Área de la base ($A_b$):** Al ser un rectángulo, multiplicamos sus dimensiones: $\text{Largo} \times \text{Ancho} \rightarrow 7 \, \text{cm} \times 3 \, \text{cm} = 21 \, \text{cm}^2$.
> 2. **Altura del prisma ($h$):** $9 \, \text{cm}$.
> 3. **Volumen ($V$):** $A_b \times h = 21 \, \text{cm}^2 \times 9 \, \text{cm} = 189 \, \text{cm}^3$.

> [!example] Ejemplo 2: Base Polígono Regular (Hexágono)
> **Datos:** Lado $L = 12 \, \text{cm}$, apotema $ap = 10.4 \, \text{cm}$, altura del prisma $h = 19 \, \text{cm}$.
> 1. **Perímetro de la base ($P$):** $6 \, \text{lados} \times 12 \, \text{cm} = 72 \, \text{cm}$.
> 2. **Área de la base ($A_b$):** $\frac{P \times ap}{2} = \frac{72 \, \text{cm} \times 10.4 \, \text{cm}}{2} = 374.4 \, \text{cm}^2$.
> 3. **Volumen ($V$):** $374.4 \, \text{cm}^2 \times 19 \, \text{cm} = 7113.6 \, \text{cm}^3$.

> [!example] Ejemplo 3: Base Triangular (Fórmula de Herón)
> **Datos:** Lados del triángulo $a = 4 \, \text{cm}$, $b = 5 \, \text{cm}$, $c = 7 \, \text{cm}$; altura $h = 9 \, \text{cm}$.
> 1. **Semiperímetro ($s$):** $\frac{4 + 5 + 7}{2} = \frac{16}{2} = 8 \, \text{cm}$.
> 2. **Área de la base ($A_b$):** $\sqrt{s(s-a)(s-b)(s-c)} = \sqrt{8(8-4)(8-5)(8-7)} = \sqrt{8 \cdot 4 \cdot 3 \cdot 1} = \sqrt{96}$.
>    - Usando **valores aproximados**: $\sqrt{96} \approx 9.8 \, \text{cm}^2$.
> 3. **Volumen ($V$):** $9.8 \, \text{cm}^2 \times 9 \, \text{cm} = 88.2 \, \text{cm}^3$.

> [!example] Ejemplo 4: Aplicación Real y Costo en $\$ \text{USD}$
> **Contexto:** Se desea llenar un prisma triangular equilátero cuyo material de relleno cuesta $\$0.50 \, \text{USD}$ por $\text{cm}^3$.
> **Datos:** Lado de la base $L = 7 \, \text{cm}$, altura del prisma $h = 10 \, \text{cm}$.
> 1. **Área de la base ($A_b$):** $\frac{\sqrt{3} \times L^2}{4} = \frac{\sqrt{3} \times 7^2}{4} \approx 21.2 \, \text{cm}^2$.
> 2. **Volumen ($V$):** $21.2 \, \text{cm}^2 \times 10 \, \text{cm} = 212 \, \text{cm}^3$.
> 3. **Costo total:** $212 \, \text{cm}^3 \times \$0.50 \, \text{USD} = \$106.00 \, \text{USD}$.

---

### 5. Práctica Independiente

> [!abstract] 🟢 Nivel Verde (Fácil)
> 1. Prisma rectangular: Base $5 \, \text{cm} \times 4 \, \text{cm}$, Altura $10 \, \text{cm}$.
> 2. Prisma rectangular: Base $8 \, \text{m} \times 2 \, \text{m}$, Altura $5 \, \text{m}$.
> 3. Prisma rectangular: Base $10 \, \text{cm} \times 3 \, \text{cm}$, Altura $12 \, \text{cm}$.
> 4. Prisma con Área de base $A_b = 18.5 \, \text{m}^2$ y Altura $16 \, \text{m}$.

> [!abstract] 🟡 Nivel Amarillo (Medio)
> 1. Prisma triangular (Herón): Lados base $9, 8, 11 \, \text{cm}$; Altura $15 \, \text{cm}$.
> 2. Prisma pentagonal regular: Lado $10 \, \text{cm}$, Apotema $6.88 \, \text{cm}$, Altura $15 \, \text{cm}$.
> 3. Prisma triangular equilátero: Lado $6 \, \text{cm}$, Altura $8 \, \text{cm}$.
> 4. Prisma hexagonal regular: Lado $5 \, \text{cm}$, Apotema $4.33 \, \text{cm}$, Altura $10 \, \text{cm}$.

> [!abstract] 🔴 Nivel Rojo (Avanzado - Aplicación Financiera)
> **Pista:** Primero calcula el Volumen ($V$) siguiendo los 4 pasos universales y luego multiplica el resultado por el precio unitario.
> 1. Un contenedor triangular equilátero tiene lado $15 \, \text{cm}$ y altura $14.3 \, \text{cm}$. Si el líquido cuesta $\$1.50 \, \text{USD}$ por $\text{cm}^3$, ¿cuál es el costo total?
> 2. Un prisma hexagonal tiene $A_b = 50 \, \text{cm}^2$ y $h = 20 \, \text{cm}$. El costo de envío es $\$0.05 \, \text{USD}$ por cada $\text{cm}^3$.
> 3. Calcula el costo de llenar un prisma rectangular (base $4 \times 5 \, \text{cm}$, altura $10 \, \text{cm}$) si el material cuesta $\$2.25 \, \text{USD}$ por $\text{cm}^3$.
> 4. Un prisma triangular tiene $A_b = 9.8 \, \text{cm}^2$ y $h = 9 \, \text{cm}$. El costo es de $\$10 \, \text{USD}$ por $\text{cm}^3$.

> [!success] ✅ Respuestas para el Docente
> **Verde:** 
> 1) $200 \, \text{cm}^3$ | 2) $80 \, \text{m}^3$ | 3) $360 \, \text{cm}^3$ | 4) $296 \, \text{m}^3$.
> **Amarillo (Valores aproximados):** 
> 1) $V \approx 532.5 \, \text{cm}^3$ | 2) $V = 2580 \, \text{cm}^3$ | 3) $V \approx 124.7 \, \text{cm}^3$ | 4) $V = 649.5 \, \text{cm}^3$.
> **Rojo (Cálculo de volumen $\rightarrow$ Costo final):** 
> 1) $V \approx 1392.8 \, \text{cm}^3 \rightarrow \text{Costo} = \$2,089.20 \, \text{USD}$
> 2) $V = 1000 \, \text{cm}^3 \rightarrow \text{Costo} = \$50.00 \, \text{USD}$
> 3) $V = 200 \, \text{cm}^3 \rightarrow \text{Costo} = \$450.00 \, \text{USD}$
> 4) $V = 88.2 \, \text{cm}^3 \rightarrow \text{Costo} = \$882.00 \, \text{USD}$

---

### 6. Evaluación y Cierre

> [!question] Pregunta 1: Conceptual
> ¿Qué sucede con las unidades de medida al calcular un volumen?
> a) Se quedan igual porque solo sumamos.
> b) Se vuelven cuadradas porque multiplicamos dos lados.
> c) Se vuelven cúbicas porque sumamos los exponentes ($2+1=3$).
> d) Desaparecen al final del proceso.
> **Respuesta correcta: c.** El volumen integra tres dimensiones, por lo que las unidades siempre deben ser cúbicas.

> [!question] Pregunta 2: Procedimental
> Si un prisma tiene una base rectangular de $10 \, \text{cm} \times 5 \, \text{cm}$ y una altura de $2 \, \text{cm}$, ¿cuál es su volumen?
> a) $17 \, \text{cm}^3$
> b) $50 \, \text{cm}^3$
> c) $100 \, \text{cm}^3$
> d) $70 \, \text{cm}^3$
> **Respuesta correcta: c.** $A_b = 10 \times 5 = 50 \, \text{cm}^2$. Luego, $V = 50 \times 2 = 100 \, \text{cm}^3$.

> [!question] Pregunta 3: Aplicación Económica
> Si un prisma ocupa $20 \, \text{cm}^3$ y el material cuesta $\$2.00 \, \text{USD}$ por cada $\text{cm}^3$, ¿cuál es el costo total?
> a) $\$22.00 \, \text{USD}$
> b) $\$40.00 \, \text{USD}$
> c) $\$10.00 \, \text{USD}$
> d) $\$20.00 \, \text{USD}$
> **Respuesta correcta: b.** Multiplicamos el volumen por el costo unitario ($20 \times 2 = 40$).

> [!tip] 💡 En la próxima clase
> Ya dominas cómo calcular el espacio interior de un prisma. En la **Clase 04**, aprenderemos sobre el **Área Superficial**: cuánta "piel" o material exterior cubre a estos cuerpos.

---
> [!info] 🧭 Navegación
> **Anterior:** [[Clase 02]]
> **Inicio:** [[Índice]]
> **Siguiente:** [[Clase 04]]