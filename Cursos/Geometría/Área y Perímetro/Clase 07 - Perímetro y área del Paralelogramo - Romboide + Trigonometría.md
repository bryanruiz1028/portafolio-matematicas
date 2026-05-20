# Clase 07 — Perímetro y área del Paralelogramo - Romboide + Trigonometría

**Tags:** #matemáticas #geometría #trigonometría #área #perímetro
**Curso:** Geometría y Razonamiento Matemático
**Navegación:** [[Clase 06 — Áreas de Cuadrados y Rectángulos]] | [[Clase 08 — Área del Triángulo]]

---

## ¿POR QUÉ ES IMPORTANTE ESTA CLASE?

Dominar el cálculo de superficies no es solo una necesidad escolar; es una habilidad crítica para la gestión de recursos y la valoración de bienes. En la práctica, muchas de las superficies que medimos no son rectángulos perfectos, y saber interpretar un **romboide** es la clave para la precisión profesional:

*   💵 **Valoración de Terrenos:** En el sector inmobiliario, el precio de un lote de tierra se calcula por su área total. Un error en la medición puede significar miles de dólares de diferencia al determinar el valor en $USD de una propiedad.
*   🏗️ **Arquitectura y Estructuras:** Muchos diseños modernos y techos industriales utilizan formas de paralelogramos. Calcular el material necesario depende de entender la relación entre sus ángulos y su superficie.
*   📊 **Planificación de Espacios:** Desde la medición de un jardín con diseño paisajístico hasta la instalación de paneles en una pared inclinada, el área nos indica cuánto material (césped, pintura, azulejos) requerimos.

---

## CONCEPTO CLAVE

El **Área** se define fundamentalmente como el **número de cuadrados unitarios** que caben dentro de una superficie plana. Un **Paralelogramo** (específicamente el **Romboide**) es un cuadrilátero con lados opuestos paralelos y ángulos opuestos iguales.

Es vital distinguir las unidades de medida:
1.  **Área:** Se expresa siempre en **unidades cuadradas** ($cm^2, m^2$), pues contamos cuadrados.
2.  **Perímetro:** Se expresa en **unidades lineales** ($cm, m$), pues sumamos longitudes.

> [!warning] **Error Crítico: Lado vs. Altura**
> El lado inclinado **NUNCA** es la altura del romboide. La altura ($h$) es la línea perpendicular (a $90^\circ$) que une la base con la parte superior. A veces, para medirla, es necesario trazarla fuera de la figura sobre la **prolongación de la base**.

> [!tip] **El Truco del Rectángulo (Visualización)**
> Imagina que el romboide tiene un triángulo "sobrante" en un extremo. Si cortas ese triángulo verticalmente y lo deslizas hacia el extremo opuesto, encajará perfectamente, transformando el romboide en un rectángulo con la misma base y altura. Por eso, su fórmula es idéntica: **$A = b \cdot h$**.

---

## PROCEDIMIENTO PASO A PASO

Cuando conocemos los lados y el ángulo interno, pero no la altura, aplicamos este flujo lógico para resolver el problema:

```text
OBJETIVO: Hallar Área (A) y Perímetro (P)
-----------------------------------------------------------
PASO 1: Identificar datos conocidos:
        Base (b), Lado inclinado (a) y Ángulo (θ).

PASO 2: Calcular la Altura (h) usando Trigonometría:
        Como buscamos el Cateto Opuesto (h) y tenemos la 
        Hipotenusa (a), usamos la razón SENO:
        sin(θ) = h / a  ==>  h = a · sin(θ)

PASO 3: Calcular el Área (A):
        A = b · h  (Resultado en unidades²)

PASO 4: Calcular el Perímetro (P):
        P = 2b + 2a (Suma de los cuatro lados exteriores)
-----------------------------------------------------------
```

---

## EJEMPLOS

> [!example] **Ejemplo 1: Caso Directo (Profe Alex)**
> Un paralelogramo tiene una base $b = 5 \text{ cm}$ y una altura $h = 3 \text{ cm}$.
> *   **Área:** $5 \text{ cm} \cdot 3 \text{ cm} = 15 \text{ cm}^2$.
> *   **Nota:** Fíjate que el resultado es en $cm^2$ porque estamos contando cuadritos.

> [!example] **Ejemplo 2: Uso de Trigonometría**
> Romboide con base $b = 10 \text{ m}$, lado $a = 7 \text{ m}$ y ángulo $\theta = 60^\circ$.
> 1.  **Hallar altura ($h$):** $h = 7 \cdot \sin(60^\circ) \approx 6.06 \text{ m}$.
> 2.  **Calcular Área:** $A = 10 \text{ m} \cdot 6.06 \text{ m} \approx 60.60 \text{ m}^2$.
> 3.  **Calcular Perímetro:** $P = 10 + 10 + 7 + 7 = 34 \text{ m}$.

> [!example] **Ejemplo 3: Aplicación Avanzada**
> Datos: $b = 14 \text{ cm}$, $a = 9 \text{ cm}$, $\theta = 56^\circ$.
> 1.  **Altura:** $h = 9 \cdot \sin(56^\circ) \approx 7.46 \text{ cm}$.
> 2.  **Área:** $A = 14 \cdot 7.46 \approx 104.44 \text{ cm}^2$.
> 3.  **Perímetro:** $P = 2(14) + 2(9) = 46 \text{ cm}$.

> [!example] **Ejemplo 4: Valor de Mercado ($USD)**
> Un terreno (lote) tiene base $10 \text{ m}$ y altura $5 \text{ m}$. El precio por $m^2$ es de $100 \text{ USD}$.
> 1.  **Área:** $10 \text{ m} \cdot 5 \text{ m} = 50 \text{ m}^2$.
> 2.  **Valor Total:** $50 \text{ m}^2 \cdot 100 \text{ USD/m}^2 = 5,000 \text{ USD}$.

---

## EJERCICIOS PARA EL ESTUDIANTE

### 🟢 Nivel Fácil: Cálculo Directo
1.  **Base:** $8 \text{ cm}$, **Altura:** $4 \text{ cm}$. Hallar área.
2.  **Base:** $12 \text{ m}$, **Altura:** $7 \text{ m}$. Hallar área.
3.  **Base:** $15 \text{ cm}$, **Altura:** $10 \text{ cm}$. Hallar área.
4.  **Base:** $6 \text{ m}$, **Altura:** $2.5 \text{ m}$. Hallar área.

### 🟡 Nivel Medio: Con Razones Trigonométricas
*Nota: Use $\sin(30^\circ) = 0.5$ y $\sin(45^\circ) \approx 0.707$*
1.  **Base:** $10 \text{ m}$, **Lado:** $6 \text{ m}$, **Ángulo:** $30^\circ$.
2.  **Base:** $20 \text{ cm}$, **Lado:** $10 \text{ cm}$, **Ángulo:** $30^\circ$.
3.  **Base:** $15 \text{ m}$, **Lado:** $8 \text{ m}$, **Ángulo:** $45^\circ$.
4.  **Base:** $5 \text{ m}$, **Lado:** $4 \text{ m}$, **Ángulo:** $30^\circ$.

### 🔴 Nivel Avanzado: Terrenos y Finanzas
1.  Un **predio** tiene base $20 \text{ m}$ y altura $15 \text{ m}$. El costo es de $200 \text{ USD/m}^2$. Calcule el valor total.
2.  Una **parcela** tiene base $50 \text{ m}$ y altura $30 \text{ m}$. El costo es de $50 \text{ USD/m}^2$. Calcule el valor total.
3.  Un **lote** tiene base $100 \text{ m}$ y altura $40 \text{ m}$. El costo es de $150 \text{ USD/m}^2$. Calcule el valor total.
4.  Un **terreno** tiene base $25 \text{ m}$ y altura $12 \text{ m}$. El costo es de $300 \text{ USD/m}^2$. Calcule el valor total.

### ✅ Respuestas (Key)
*   **Fácil:** 1) $32 \text{ cm}^2$, 2) $84 \text{ m}^2$, 3) $150 \text{ cm}^2$, 4) $15 \text{ m}^2$.
*   **Medio:** 
    1. $h=3 \text{ m} \rightarrow A=30 \text{ m}^2$.
    2. $h=5 \text{ cm} \rightarrow A=100 \text{ cm}^2$.
    3. $h \approx 5.66 \text{ m} \rightarrow A \approx 84.90 \text{ m}^2$.
    4. $h=2 \text{ m} \rightarrow A=10 \text{ m}^2$.
*   **Avanzado:** 1) $60,000 \text{ USD}$, 2) $75,000 \text{ USD}$, 3) $600,000 \text{ USD}$, 4) $90,000 \text{ USD}$.

---

## MINI-PRUEBA DE AUTOEVALUACIÓN

1.  **Conceptual:** Si un romboide tiene un área de $12 \text{ m}^2$, ¿qué significa esto físicamente?
    *   *Significa que en su superficie interior caben exactamente 12 cuadrados de 1 metro por lado.*
2.  **Procedimental:** ¿Por qué usamos el **Seno** para hallar la altura y no el Coseno?
    *   *Porque la altura representa el cateto opuesto al ángulo dado, y el seno es la razón que relaciona dicho cateto con la hipotenusa (el lado inclinado).*
3.  **Aplicación:** Si un lote romboide tiene un área de $25 \text{ m}^2$ y se vende a $10 \text{ USD}$ el metro cuadrado, ¿cuál es el precio final?
    *   *$250 \text{ USD}$.*

---

## CIERRE Y NOTAS

Has aprendido que el romboide es, en esencia, un rectángulo transformado. En la siguiente clase, veremos cómo este mismo concepto de "base por altura" se divide a la mitad para dar origen a la fórmula del área del triángulo.

**Navegación:** [[Clase 06 — Áreas de Cuadrados y Rectángulos]] | [[Clase 08 — Área del Triángulo]]