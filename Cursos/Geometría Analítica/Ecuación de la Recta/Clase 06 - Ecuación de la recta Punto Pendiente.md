# Clase 06 — Ecuación de la recta Punto Pendiente

#algebra #ecuacindelarect
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 6 de 11

> [!info] 🧭 Navegación
> ◀ Lección anterior: [[05 - Pendiente de una recta]]
> 🔼 Índice: [[00 - Índice del curso]]
> ▶ Próxima lección: [[07 - Gráfica de la recta]]

---

### 🌍 Relevancia y aplicaciones
> [!info] 🌍 Relevancia y aplicaciones
> Conocer un punto de paso y la inclinación de una recta es la herramienta definitiva para predecir trayectorias. Nos permite determinar el comportamiento futuro de cualquier variable partiendo de su estado actual y su ritmo de cambio constante.
> 
> *   💵 **Proyección financiera:** Estimar el crecimiento de una inversión a partir de un saldo actual (punto) y una tasa de interés fija (pendiente).
> *   🏗️ **Construcción:** Calcular la inclinación exacta de una rampa o techo partiendo de un solo punto de apoyo estructural.
> *   📊 **Vida cotidiana:** Predecir el tiempo de llegada en un viaje si conoces tu ubicación actual en el GPS y la velocidad constante a la que te desplazas.

---

### 📌 ¿Qué es la Ecuación Punto-Pendiente?
> [!note] 📌 ¿Qué es Ecuación de la recta Punto Pendiente?
> Es una fórmula que nos permite encontrar la ecuación completa de una recta conociendo solo dos datos: un punto de paso $(x_1, y_1)$ y su pendiente ($m$).

> [!warning] ⚠️ Error común
> Ten mucho cuidado con los signos al sustituir valores negativos. Si el punto es $(-5, -2)$, la fórmula genera un "choque" de signos: $y - (-2)$ y $x - (-5)$. **Debes transformarlos en positivos ($y + 2$ y $x + 5$)** antes de operar, tal como lo explica el Profe Alex para evitar errores en el despeje.

> [!tip] 💡 Truco para recordarlo
> El nombre de la ecuación te dice qué buscar: para que funcione, solo necesitas "pescar" del problema un **Punto** y una **Pendiente**. ¡Si los tienes, ya tienes la recta!

---

### 📋 Procedimiento Paso a Paso

```text
PASO 1 → Identificar y etiquetar los datos: el punto (x₁, y₁) y la pendiente m.
PASO 2 → Sustituir los valores en la fórmula fundamental: y - y₁ = m(x - x₁).
PASO 3 → Aplicar la propiedad distributiva para multiplicar la pendiente por los términos del paréntesis.
PASO 4 → Despejar la variable "y" para obtener la forma "pendiente-ordenada al origen" (y = mx + b). 
         A esta versión el Profe Alex la llama la "forma más bonita", técnicamente conocida como forma simplificada o explícita.
```

---

### 📝 Ejemplos Desarrollados

#### Ejemplo 1: Caso Básico
**Problema:** Hallar la ecuación de la recta que pasa por $A(3, 5)$ con una pendiente $m = 2$.
1.  **Sustitución:** $y - 5 = 2(x - 3)$
2.  **Distributiva:** $y - 5 = 2x - 6$
3.  **Despeje:** $y = 2x - 6 + 5$
4.  **Resultado:** $y = 2x - 1$

#### Ejemplo 2: El reto de los Signos Negativos
**Problema:** Hallar la ecuación de la recta que pasa por $A(-2, 5)$ con $m = 4$.
1.  **Sustitución:** $y - 5 = 4(x - (-2))$
2.  **Simplificación:** $y - 5 = 4(x + 2)$ (Aquí aplicamos la ley de signos).
3.  **Distributiva:** $y - 5 = 4x + 8$
4.  **Resultado final:** $y = 4x + 13$

#### Ejemplo 3: Operando con Fracciones
**Problema:** Hallar la ecuación de la recta que pasa por $A(3, -4)$ con $m = -2/5$.
1.  **Sustitución:** $y - (-4) = -2/5(x - 3) \rightarrow y + 4 = -2/5x + 6/5$
2.  **Despeje:** $y = -2/5x + 6/5 - 4$
3.  **Operación de fracciones:** Usamos el método de la **"Carita feliz" (productos cruzados)** para resolver $\frac{6}{5} - \frac{4}{1} = \frac{6 - 20}{5} = -\frac{14}{5}$.
4.  **Resultado:** $y = -2/5x - 14/5$

#### Ejemplo 4: Aplicación en Costos ($USD)
**Problema:** El costo total ($y$) de producir materiales ($x$) sigue una trayectoria recta que pasa por el punto $(2/3, -5/2)$ con una tasa de costo por unidad (pendiente) de $3/2$.
1.  **Sustitución:** $y - (-5/2) = 3/2(x - 2/3)$
2.  **Simplificación:** $y + 5/2 = 3/2x - 1$ (Nota: $\frac{3}{2} \cdot \frac{2}{3} = 1$).
3.  **Despeje:** $y = 3/2x - 1 - 5/2$
4.  **Resultado final:** $y = 3/2x - 7/2$
    *   *Interpretación:* $x$ representa las unidades producidas y $y$ el costo total en USD.

---

### ✏️ Ejercicios para el Estudiante

**🟢 Nivel Fácil (Reemplazo directo)**
1. $A(2, 4), m = 3$
2. $A(1, 7), m = 5$
3. $A(5, 2), m = 1$
4. $A(4, 10), m = 2$

**🟡 Nivel Medio (Signos negativos)**
5. $A(-3, 4), m = 2$
6. $A(2, -6), m = -3$
7. $A(-1, -1), m = 4$
8. $A(-5, 2), m = -1$

**🔴 Nivel Avanzado (Fracciones y Aplicaciones $USD)**
9. $A(1/2, 3), m = 2/3$
10. $A(-2, 1/4), m = 1/2$
11. Un activo financiero vale $y = -3/2$ en el tiempo $x = 5/2$ con una tasa $m = 3/2$.
12. $A(-3, 2), m = 3/4$

#### ✅ Respuestas
1. $y = 3x - 2$ | 2. $y = 5x + 2$ | 3. $y = x - 3$ | 4. $y = 2x + 2$
5. $y = 2x + 10$ | 6. $y = -3x$ | 7. $y = 4x + 3$ | 8. $y = -x - 3$
9. $y = 2/3x + 8/3$ | 10. $y = 1/2x + 5/4$ | 11. $y = 3/2x - 21/4$ | 12. $y = 3/4x + 17/4$

---

### 🧠 Mini-prueba de Autoevaluación

1.  **¿Qué ocurre con el signo de la coordenada $x_1$ si su valor original es negativo (ej. $-4$) al introducirlo en la fórmula?**
    *   *Respuesta:* Se convierte en positivo ($x + 4$) por el choque de signos entre el negativo de la fórmula y el del número.

2.  **Si tienes $y - 2 = 3(x - 1)$, ¿cuál es la forma "más bonita" (simplificada)?**
    *   *Respuesta:* $y = 3x - 1$.

3.  **Negocios:** Si el precio por unidad ($m$) es $5 USD y al vender 2 unidades ($x$) el saldo es $12 ($y$), ¿cuál es la ecuación?
    *   *Respuesta:* $y = 5x + 2$.
    *   *Proceso:* Sustituimos en $y - 12 = 5(x - 2) \rightarrow y - 12 = 5x - 10 \rightarrow y = 5x + 2$.

> [!important] Comprobación
> Como dice el Profe Alex: para estar 100% seguro, sustituye la $x$ original en tu resultado. Si obtienes la $y$ del punto, ¡tu ejercicio está perfecto!

---

> [!tip] 💡 En la próxima clase
> Ahora que dominas la estructura algebraica, aprenderemos a llevar estos datos al plano cartesiano en **[[07 - Gráfica de la recta]]**.

> [!info] 🧭 Navegación
> ◀ Lección anterior: [[05 - Pendiente de una recta]]
> 🔼 Índice: [[00 - Índice del curso]]
> ▶ Próxima lección: [[07 - Gráfica de la recta]]