# Clase 01 — Introducción a las Áreas Sombreadas

> [!nav] Navegación
> **Curso:** Geometría Aplicada | **Clase Actual:** 01 | **Siguiente:** Clase 02 — Figuras Compuestas

### ¿Por qué es importante esta clase?

El estudio de las áreas sombreadas es una de las herramientas más poderosas del diseño y la ingeniería. Nos permite entender cómo se estructuran las formas complejas a partir de figuras básicas. En la práctica, esta habilidad es la que permite calcular con precisión cuánta materia prima se necesita para fabricar un objeto, evitando desperdicios y optimizando costos.

**Aplicaciones prácticas:**
*   **Finanzas (USD):** Determinar el presupuesto exacto para la compra de vinilo o pintura en un diseño publicitario que combina formas curvas y rectas.
*   **Arquitectura e Industria:** Calcular el área neta de láminas de metal necesarias para piezas industriales que tienen perforaciones o cortes geométricos.
*   **Vida Cotidiana:** Diseñar un jardín calculando cuánto césped comprar para parterres que contienen fuentes circulares o senderos triangulares dentro de un terreno rectangular.

---

### Concepto Clave

Las **Áreas Sombreadas** son superficies que resultan de la combinación de figuras geométricas conocidas. Básicamente, es el espacio que queda cuando **unimos (sumamos)** dos o más figuras, o cuando **quitamos (restamos)** una figura del interior de otra.

En este curso, además de las figuras totales, utilizaremos frecuentemente partes del círculo:
*   **Semicírculo:** Exactamente la mitad de un círculo ($1/2$).
*   **Cuadrante:** La cuarta parte de un círculo ($1/4$).

> [!warning] Error Común
> El error más frecuente es confundir el **Diámetro** con el **Radio**. Recuerda que para las fórmulas de área siempre necesitamos el **Radio** (la mitad del diámetro). Otro error típico es calcular el área de la figura exterior y olvidar restar el hueco interno.

**Truco del Experto:** Visualiza las figuras como **piezas de un rompecabezas**. Algunas piezas se agregan para completar la superficie (suma) y otras actúan como moldes de galletas que recortan y retiran una parte del material (resta).

---

### Formulario de Referencia

Antes de comenzar, asegúrate de tener estas fórmulas a mano. Son tus herramientas de trabajo:

*   **Cuadrado:** $A = L^2$ (Lado por lado)
*   **Círculo:** $A = \pi \times r^2$ (Donde $\pi \approx 3.14$)
*   **Rectángulo:** $A = b \times h$ (Base por altura)
*   **Triángulo:** $A = \frac{b \times h}{2}$
*   **Polígono Regular:** $A = \frac{\text{perímetro} \times \text{apotema}}{2}$
*   **Trapecio:** $A = \frac{(B + b)}{2} \times h$ (Suma de bases entre dos, por altura)

---

### Procedimiento paso a paso

Para resolver problemas de áreas sombreadas como un profesional, sigue este orden lógico:

1.  **Identificar las figuras:** Observa el gráfico y detecta qué figuras básicas lo componen (¿hay cuadrados?, ¿hay partes de círculos?).
2.  **Determinar la operación:** Decide si la zona sombreada nace de una unión (sumar áreas) o de una sustracción (restar la figura interna de la externa).
3.  **Calcular áreas individuales:** Aplica la fórmula correspondiente a cada pieza por separado.
4.  **Realizar la operación final:** Suma o resta los resultados para obtener el área sombreada total.

---

### Ejemplos

> [!example] Ejemplo 1: Resta básica (Círculo en Cuadrado)
> **Problema:** Un cuadrado de 10 cm de lado tiene un círculo inscrito. Calcula el área de las esquinas (área sombreada).
> 1. **Figuras:** Cuadrado ($L=10$) y Círculo ($r=5$).
> 2. **Operación:** Área del Cuadrado - Área del Círculo.
> 3. **Cálculos:**
>    *   Cuadrado: $10^2 = 100 \text{ cm}^2$
>    *   Círculo: $3.14 \times 5^2 = 78.5 \text{ cm}^2$
> 4. **Resultado:** $100 - 78.5 = 21.5 \text{ cm}^2$.

> [!example] Ejemplo 2: Suma de figuras (Composición)
> **Problema:** Un rectángulo de $10 \text{ m} \times 5 \text{ m}$ tiene un semicírculo unido a uno de sus lados de 5 m.
> 1. **Figuras:** Rectángulo y Semicírculo ($r=2.5$).
> 2. **Operación:** Área Rectángulo + Área Semicírculo.
> 3. **Cálculos:**
>    *   Rectángulo: $10 \times 5 = 50 \text{ m}^2$
>    *   Semicírculo: $(3.14 \times 2.5^2) / 2 \approx 9.81 \text{ m}^2$
> 4. **Resultado:** $50 + 9.81 = 59.81 \text{ m}^2$.

> [!example] Ejemplo 3: Triángulo dentro de Círculo
> **Problema:** Un círculo de radio 6 cm contiene un triángulo de base 6 cm y altura 4 cm. La sombra está en el círculo pero fuera del triángulo.
> 1. **Operación:** Área Círculo - Área Triángulo.
> 2. **Cálculos:**
>    *   Círculo: $3.14 \times 6^2 = 113.04 \text{ cm}^2$
>    *   Triángulo: $(6 \times 4) / 2 = 12 \text{ cm}^2$
> 3. **Resultado:** $113.04 - 12 = 101.04 \text{ cm}^2$.

> [!example] Ejemplo 4: Análisis de Costos (USD)
> **Problema:** Un letrero cuadrado de 2 m de lado tiene un hueco circular de 1 m de radio. El material cuesta \$15 USD por $m^2$.
> 1. **Área:** Cuadrado ($4 \text{ m}^2$) - Círculo ($3.14 \times 1^2 = 3.14 \text{ m}^2$).
> 2. **Resta:** $4 - 3.14 = 0.86 \text{ m}^2$.
> 3. **Costo total:** $0.86 \text{ m}^2 \times 15 \text{ USD} = \$12.90 \text{ USD}$.

---

### Ejercicios para el estudiante

> [!abstract] Práctica de Clase
> **Nivel Fácil (Resta de figuras poligonales):**
> 1. Cuadrado de 8 m con un cuadrado interno "hueco" de 3 m de lado.
> 2. Rectángulo de $10 \times 6$ cm con un rectángulo interno de $2 \times 3$ cm.
> 3. Cuadrado de 12 cm al que se le quitan 4 cuadrados pequeños de 2 cm en cada esquina.
> 4. Rectángulo de $20 \times 10$ m con una franja central (rectángulo) de $20 \times 2$ m que se debe restar.
>
> **Nivel Medio (Semicírculos y Triángulos):**
> 5. Un triángulo de base 10 y altura 8 con un pequeño círculo de radio 1 en su centro (quitar el círculo).
> 6. Dos semicírculos de radio 4 unidos por su diámetro. ¿Cuál es el área total resultante?
> 7. Un cuadrado de lado 6 con un triángulo de base 6 y altura 6 recortado desde su base.
> 8. Un cuadrante de círculo (1/4) con un radio de 10 cm.
>
> **Nivel Avanzado (Problemas con USD):**
> 9. Una mesa circular de radio 1 m tiene un triángulo de vidrio en el centro ($b=1, h=0.5$). La madera cuesta \$50 USD por $m^2$. ¿Cuánto cuesta la madera (área sombreada)?
> 10. Una pared de $5 \times 3$ m tiene dos ventanas circulares de radio 0.5 m cada una. Pintarla cuesta \$10 USD por $m^2$. ¿Cuál es el costo?
> 11. Una pieza metálica es un trapecio ($B=10, b=6, h=4$) con un agujero cuadrado central de lado 2. El metal cuesta \$100 USD por $m^2$.
> 12. Un jardín rectangular de $50 \times 20$ m tiene una fuente circular central de radio 5 m. El césped cuesta \$5 USD por $m^2$.

> [!check]- Ver Respuestas Sugeridas
> 1. 55 $m^2$
> 2. 54 $cm^2$
> 3. 128 $cm^2$
> 4. 160 $m^2$
> 5. 36.86 (Aprox.)
> 6. 50.24 (Es un círculo completo)
> 7. 18 (Es la mitad del cuadrado)
> 8. 78.5 $cm^2$
> 9. \$144.50 USD
> 10. \$134.30 USD
> 11. \$2,800 USD (Área trapecio 32 - Área cuadrado 4 = 28)
> 12. \$4,607.50 USD

---

### Mini-prueba de autoevaluación

> [!question] Comprueba tu aprendizaje
> 1. **Concepto:** Si para obtener el área sombreada unimos un triángulo a un rectángulo, ¿estamos aplicando una suma o una resta de áreas?
> 2. **Procedimiento:** De acuerdo al formulario, para hallar el área de un Pentágono Regular, ¿qué datos necesitas además de la apotema?
> 3. **Cálculo rápido:** Un panel publicitario rectangular mide $3 \text{ m} \times 2 \text{ m}$. Si el material cuesta \$20 USD el metro cuadrado, ¿cuál es el costo total del panel?

---

### Notas Finales

Dominar la identificación de figuras y saber cuándo sumar o restar es el secreto para no fallar en geometría. En la **Clase 02**, daremos el siguiente paso: analizaremos figuras compuestas más complejas y aprenderemos a detectar sectores circulares "escondidos" dentro de polígonos.

> [!nav] Navegación
> **Curso:** Geometría Aplicada | **Clase Actual:** 01 | **Siguiente:** Clase 02 — Figuras Compuestas