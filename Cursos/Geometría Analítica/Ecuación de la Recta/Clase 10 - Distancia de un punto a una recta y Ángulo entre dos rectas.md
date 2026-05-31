# Clase 10 — Distancia de un punto a una recta y Ángulo entre dos rectas

[[Clase 09]] | [[Clase 11]]

#geometria-analitica #matematicas #distancia #angulos #educacion

---

## Relevancia y Aplicaciones

En geometría analítica, la **distancia mínima** y la **inclinación** son fundamentales para entender la relación espacial entre objetos. No se trata solo de trazar líneas, sino de optimizar rutas y medir desviaciones de manera precisa.

*   **💵 Aplicación con $USD:** En el análisis de mercados, la distancia de un punto de precio actual a una línea de tendencia (soporte o resistencia) permite medir la **volatilidad**. Una distancia mayor indica un riesgo de mercado más alto o una desviación del valor esperado en dólares.
*   **🏗️ Aplicación práctica:** Es esencial en la arquitectura para garantizar la perpendicularidad de muros y el cálculo exacto de la inclinación en rampas de acceso, asegurando que cumplan con los estándares de seguridad.
*   **📊 Situación cotidiana:** La distancia de un punto a una recta representa el "camino más corto". Si necesitas llegar a una avenida recta desde un campo abierto, la trayectoria más rápida será siempre la línea perpendicular a dicha avenida.

---

## Conceptos Clave

> [!note] **Definición: Distancia de un punto a una recta**
> Es la longitud del segmento más corto que une un punto con una recta. Esta distancia siempre es **perpendicular** a la recta, lo que significa que el encuentro entre ambas debe formar un ángulo de 90° (recto).

> [!warning] **Error común: La forma general y las potencias**
> 1. **La Ecuación:** Nunca apliques la fórmula si la ecuación está como $y = mx + b$. Primero debes igualarla a cero para obtener la **forma general**: $Ax + By + C = 0$.
> 2. **El Signo de la Potencia:** Recuerda que en la fórmula, $B^2$ siempre será positivo.
>    *   **Correcto:** $(-4)^2 = (-4) \cdot (-4) = 16$.
>    *   **Incorrecto:** $-4^2 = -16$ (aquí el signo no está elevado, solo el número).

> [!tip] **Pro-Tip: Eliminación de fracciones**
> Si tu ecuación tiene fracciones como $y = \frac{2}{3}x + 2$, no trabajes con decimales. Multiplica toda la ecuación por el denominador común (en este caso, 3) para obtener coeficientes enteros:
> $$3(y) = 3\left(\frac{2}{3}x + 2\right) \implies 3y = 2x + 6 \implies 2x - 3y + 6 = 0$$

---

## Procedimiento Paso a Paso

Para evitar confusiones al sustituir, utiliza el **truco de alineación vertical** de Profe Alex:

```text
PASO 1 → Convertir la ecuación a la forma general: Ax + By + C = 0.
PASO 2 → Identificar valores. Escríbelos alineados para facilitar la multiplicación:
         A   B   C  (de la recta)
         ↓   ↓
         x1  y1     (del punto)
PASO 3 → Sustituir en la fórmula de distancia:
         $$d = \frac{|A(x_1) + B(y_1) + C|}{\sqrt{A^2 + B^2}}$$
PASO 4 → Resolver: el valor absoluto arriba (siempre positivo) y la raíz abajo.
```

---

## Bloques de Ejemplos

> [!ad-example] **Ejemplo 1: Caso básico (Video 1)**
> **Datos:** Recta $3x - 4y + 1 = 0$ y Punto $(3, -2)$.
> *   **Alineación:** $A=3, B=-4, C=1$ y $x_1=3, y_1=-2$.
> *   **Sustitución:**
> $$d = \frac{|3(3) + (-4)(-2) + 1|}{\sqrt{3^2 + (-4)^2}}$$
> *   **Cálculo:** $d = \frac{|9 + 8 + 1|}{\sqrt{9 + 16}} = \frac{18}{5}$
> *   **Resultado:** $3.6$ unidades.

> [!ad-example] **Ejemplo 2: Manejo de signos negativos (Video 2)**
> **Datos:** Recta $3x - 4y - 3 = 0$ y Punto $(-3, 2)$.
> *   **Sustitución:**
> $$d = \frac{|3(-3) + (-4)(2) - 3|}{\sqrt{3^2 + (-4)^2}}$$
> *   **Cálculo:** $d = \frac{|-9 - 8 - 3|}{5} = \frac{|-20|}{5} = \frac{20}{5}$
> *   **Resultado:** $4$ unidades.

> [!ad-example] **Ejemplo 3: Ángulo entre dos rectas**
> **Datos:** $y = 3x - 1$ ($m_1=3$) y $y = 2x + 5$ ($m_2=2$).
> *   **Fórmula:** $\theta = \arctan \left| \frac{m_1 - m_2}{1 + m_1 \cdot m_2} \right|$
> *   **Sustitución:** $\theta = \arctan \left| \frac{3 - 2}{1 + (3)(2)} \right| = \arctan \left| \frac{1}{7} \right|$
> *   **Resultado:** $\approx 8.13^\circ$.

> [!ad-example] **Ejemplo 4: Aplicación Original ($USD)**
> **Problema:** Una línea de soporte financiero es $2x - 3y + 5 = 0$. El precio actual en el tiempo $x=5$ es $y=10$ USD. Hallar la desviación.
> *   **Cálculo:** $d = \frac{|2(5) - 3(10) + 5|}{\sqrt{2^2 + (-3)^2}} = \frac{|10 - 30 + 5|}{\sqrt{13}}$
> *   **Resultado:** $\frac{15}{3.605} \approx 4.16$ USD de desviación.

---

> [!info] **Teoría de Intersección**
> *   **Rectas Paralelas:** Si $m_1 = m_2$, las rectas nunca se cruzan; por lo tanto, no existe un ángulo de inclinación entre ellas (es $0^\circ$).
> *   **Rectas Perpendiculares:** Si $m_1 \cdot m_2 = -1$, el ángulo entre ellas es exactamente **90°**.

---

## Ejercicios para el Estudiante

> [!ad-abstract] **Práctica Propuesta**
>
> ### **Verde (Fácil)**
> 1. Hallar $d$ del punto $P(1, 2)$ a la recta $3x + 4y + 4 = 0$.
> 2. Hallar $d$ del origen $P(0, 0)$ a la recta $5x + 12y - 26 = 0$.
> 3. Identifica $A, B$ y $C$ en la recta $x - 2y + 8 = 0$.
> 4. Calcula la distancia de $P(2, 5)$ a la recta $6x + 8y + 10 = 0$.
>
> ### **Amarillo (Medio)**
> 5. Convierte $y = 2x + 3$ a forma general y halla su distancia al origen.
> 6. Calcula el ángulo entre las rectas $y = x + 1$ y $y = -2x + 4$.
> 7. Hallar la distancia de $P(-1, -1)$ a la recta $y = \frac{3}{4}x + 2$ (Usa el pro-tip de fracciones).
> 8. Determina si las rectas con $m_1 = 5$ y $m_2 = 5$ tienen un ángulo de cruce.
>
> ### **Rojo (Avanzado)**
> 9. Un activo financiero sigue la tendencia $x - y + 2 = 0$. Si el precio es $P(10, 15)$, calcula la volatilidad en $USD$.
> 10. Halla la distancia entre $P(2, 4)$ y la recta que pasa por $(0,0)$ con $m=1$.
> 11. Determina el ángulo entre $2x - 3y + 6 = 0$ y $x + 2y - 4 = 0$.
> 12. Un dron está en $(5, 5)$. Una pared es la recta $3x + 4y - 10 = 0$. ¿Cuál es la distancia mínima antes del impacto?

> [!ad-success] **Solucionario**
> 1) $3$ | 2) $2$ | 3) $A=1, B=-2, C=8$ | 4) $6.2$ | 5) $2x-y+3=0; d \approx 1.34$ | 6) $71.56^\circ$ | 7) $3.4$ | 8) No (son paralelas) | 9) $3.53$ USD | 10) $1.41$ | 11) $60.25^\circ$ | 12) $5$ unidades.

---

## Mini-Prueba de Autoevaluación

> [!ad-question] **Evaluación Rápida**
> 1. **Conceptual:** ¿Qué orientación debe tener el segmento de distancia para ser considerado el "camino más corto"?
> 2. **Procedimental:** Si una recta está expresada como $y = 3x - 5$, ¿cuál es el primer paso antes de usar la fórmula de distancia?
> 3. **Aplicación $USD:** Si calculas la distancia de un precio a una recta y el resultado es $d = 0$, ¿qué significa esto para el inversor?

---

## Cierre y Navegación

Dominar la distancia y los ángulos nos permite cuantificar la relación exacta entre puntos y trayectorias. Estos cálculos son la base para el diseño técnico y el análisis de datos. En la próxima clase, aplicaremos estos conocimientos para realizar graficaciones detalladas de sistemas de ecuaciones lineales.

[[Clase 09]] | [[Clase 11]]