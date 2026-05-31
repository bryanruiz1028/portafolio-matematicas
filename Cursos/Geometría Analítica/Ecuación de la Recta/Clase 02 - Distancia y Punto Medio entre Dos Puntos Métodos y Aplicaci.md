# Clase 02 — Distancia y Punto Medio entre Dos Puntos: Métodos y Aplicaciones

#algebra #distancebetween

[⬅️ Clase 01](Clase01) | [🏠 Índice](Indice) | [Clase 03 ➡️](Clase03)

> [!info] 🌍 Relevancia y aplicaciones
> Calcular la distancia exacta y el punto central entre dos coordenadas es fundamental para la navegación y el diseño. Estos conceptos nos permiten determinar trayectorias óptimas y puntos de equilibrio en estructuras físicas y modelos económicos.
> - **Finanzas:** Determinar el valor promedio exacto entre dos activos financieros cotizados en **$USD**.
> - **Arquitectura/Construcción:** Localizar el "punto de equilibrio" o centro de gravedad en una viga para colocar columnas de soporte que garanticen la estabilidad de la estructura.
> - **Mapas y Navegación:** Calcular la distancia "en línea recta" (geodésica) entre dos puntos GPS para optimizar la logística de entregas.

---

### 📌 ¿Qué es la Distancia y el Punto Medio?

> [!note] Conceptos Básicos y Fórmulas
> - **Distancia ($d$):** Es la longitud del segmento que une dos puntos. En el plano cartesiano, se visualiza como la **hipotenusa** de un triángulo rectángulo. 
>   $$\text{Fórmula: } d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
> - **Punto Medio ($M$):** Es el punto que se encuentra a la misma distancia de los extremos. Antes de verlo en 2D, recuerda que en una recta numérica (1D) es simplemente el promedio de dos números. En el plano, es el promedio de las coordenadas por separado.
>   $$\text{Fórmula: } M = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} \right)$$

> [!warning] ⚠️ Error común: El choque de signos
> Según el método del **Profe Alex**, el error más frecuente ocurre al sustituir números negativos en la fórmula de distancia. El signo "menos" de la fórmula y el signo "menos" del número se encuentran:
> $$x - (-y) \implies x + y$$
> Aplica siempre el **"salto de paso"**: si ves dos negativos seguidos, conviértelos inmediatamente en una suma ($- \times - = +$).

> [!tip] 💡 Truco para recordarlo
> Para el **Punto Medio**, piensa en el "promedio de notas". Si en un examen sacas 5 y en otro 1, tu nota media es $(5+1) \div 2 = 3$. En el plano cartesiano, haces exactamente lo mismo: sumas las $X$ y divides entre 2; luego sumas las $Y$ y divides entre 2.

---

### 🚀 Procedimiento Paso a Paso

```text
1. IDENTIFICAR: Asignar (x1, y1) al punto A y (x2, y2) al punto B.
2. SUSTITUIR: Colocar los valores en la fórmula correspondiente.
3. OPERAR SIGNOS: Resolver paréntesis aplicando la ley de signos (salto de paso).
4. CÁLCULO FINAL: Resolver potencias y extraer la raíz (distancia) o dividir (punto medio).
```

---

### 📝 Bloque de Ejemplos

> [!abstract] Ejemplo 1: Método Gráfico (Pitágoras)
> **Puntos:** A(1, 1) y B(5, 4).
> 1. Al graficar, se observa que para ir de A a B avanzamos **4** unidades en el eje X y subimos **3** unidades en el eje Y.
> 2. Estos valores son los catetos de un triángulo rectángulo.
> 3. Aplicamos Pitágoras: $d = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25}$.
> 4. Resultado: la distancia es **5** unidades.

> [!abstract] Ejemplo 2: Manejo de Signos Negativos
> **Puntos:** A(-2, -5) y B(4, -2).
> 1. Sustituimos: $d = \sqrt{(4 - (-2))^2 + (-2 - (-5))^2}$.
> 2. Aplicamos el salto de paso: $d = \sqrt{(4 + 2)^2 + (-2 + 5)^2}$.
> 3. Resolvemos: $d = \sqrt{6^2 + 3^2} = \sqrt{36 + 9} = \sqrt{45}$.
> 4. Resultado: $d \approx \mathbf{6.7}$ (según el procedimiento de Profe Alex).

> [!abstract] Ejemplo 3: Cálculo de Punto Medio
> **Puntos:** A(5, 2) y B(1, 6).
> 1. Promedio de X: $(5 + 1) \div 2 = 6 \div 2 = \mathbf{3}$.
> 2. Promedio de Y: $(2 + 6) \div 2 = 8 \div 2 = \mathbf{4}$.
> 3. El Punto Medio es el punto **(3, 4)**.

> [!abstract] Ejemplo 4: Aplicación Financiera (**$USD**)
> **Problema:** Una acción de tecnología "A" cotiza a **$10.50 USD** y la acción "B" a **$15.50 USD**. ¿Cuál es el precio medio exacto?
> 1. Aplicamos punto medio unidimensional: $\frac{10.50 + 15.50}{2}$.
> 2. Sumamos: $26.00 \div 2$.
> 3. Resultado: El precio medio es de **$13.00 USD**.

---

### ✏️ Ejercicios para el Estudiante

> [!example] Nivel Verde (Fácil - Punto Medio)
> Hallar el punto medio de:
> 1. A(2, 4) y B(8, 10)
> 2. A(0, 0) y B(6, 4)
> 3. A(10, 2) y B(2, 8)
> 4. A(5, 5) y B(15, 15)

> [!example] Nivel Amarillo (Medio - Distancia con Signos)
> Calcular la distancia entre:
> 1. A(-3, 1) y B(3, 1)
> 2. A(-1, -1) y B(2, 3)
> 3. A(4, -2) y B(-2, 6)
> 4. A(-5, -5) y B(0, 0)

> [!example] Nivel Rojo (Avanzado - Fracciones y Aplicaciones)
> 1. Hallar el punto medio entre $A(1/2, 1)$ y $B(3/2, 5)$.
> 2. Hallar el punto medio entre $A(3/4, -3/2)$ y $B(-3/2, 1/4)$.
> 3. Una tienda A está en $(0, 0)$ y vende un producto a **$12.00 USD**. La tienda B está en $(10, 0)$ y lo vende a **$18.00 USD**. ¿En qué coordenada $(x, 0)$ se encuentra el punto equidistante en el eje X y cuál es el precio medio en **$USD**?
> 4. Calcular la distancia entre $A(1/2, 2)$ y $B(5/2, 2)$.

---

> [!success] ✅ Respuestas (para el docente)
> **Nivel Verde:** 1. (5, 7) | 2. (3, 2) | 3. (6, 5) | 4. (10, 10).
> **Nivel Amarillo:** 1. 6 | 2. 5 | 3. 10 | 4. $\sqrt{50} \approx 7.07$.
> **Nivel Rojo:** 1. (1, 3) | 2. (-3/8, -5/8) | 3. Coordenada (5, 0) y Precio **$15.00 USD** | 4. 2.

---

### 🧪 Autoevaluación (Mini-prueba)

1. **¿Qué concepto del plano cartesiano equivale a calcular la hipotenusa de un triángulo rectángulo?**
   - A) Punto Medio
   - B) Distancia
   - C) El origen
   - D) El promedio
   *Respuesta: B. La distancia entre dos puntos se calcula mediante el Teorema de Pitágoras.*

2. **Al calcular la distancia entre (2, 5) y (-3, 5), ¿cuál es el resultado correcto tras aplicar el "salto de paso" en el paréntesis de las X ($x_2 - x_1$)?**
   - A) $2 - 3 = -1$
   - B) $2 - (-3) = 2 + 3 = 5$
   - C) $5 - 5 = 0$
   - D) $-3 - 2 = -5$
   *Respuesta: B. Al restar un número negativo, la operación se transforma en una suma siguiendo la instrucción del Profe Alex.*

3. **Si el precio de un activo sube de $100 USD a $200 USD, ¿cuál es el "punto medio" financiero?**
   - A) **$150 USD**
   - B) **$125 USD**
   - C) **$175 USD**
   - D) **$300 USD**
   *Respuesta: A. El promedio simple es $(100 + 200) \div 2 = 150$.*

---

> [!tip] 💡 En la próxima clase
> Ya sabemos medir qué tan larga es una línea y dónde está su centro. Ahora aprenderemos qué tan "inclinada" está. El próximo tema es: **La Pendiente de una Recta**.

[⬅️ Clase 01](Clase01) | [🏠 Índice](Indice) | [Clase 03 ➡️](Clase03)