# Clase 03 — Pendiente e inclinación de la recta

#algebra #pendientedelare

**Curso:** Ecuación de la Recta
**Lección:** 03 de 11

> [!info] 🧭 Navegación
> [[Clase02|⬅️ Clase 02: Representación en el plano cartesiano]] | [[Indice|🏠 Índice]] | [[Clase04|Clase 04: Ecuación Punto-Pendiente ➡️]]

---

> [!info] 🌍 Relevancia y aplicaciones
> La pendiente es una medida numérica que nos indica qué tan inclinada está una recta y cuál es su ritmo de cambio. Es la "velocidad" a la que algo sube o baja.
> 
> - 💵 **Aplicación USD:** Permite calcular la tasa de cambio; por ejemplo, cuántos pesos aumenta el precio del dólar por cada día que pasa.
> - 🏗️ **Aplicación práctica:** Esencial en la construcción para determinar la inclinación segura de rampas de acceso o la caída de los techos para que drene el agua.
> - 📊 **Situación cotidiana:** Representa el esfuerzo físico al subir una colina en bicicleta; a mayor pendiente, mayor inclinación y dificultad.

---

> [!note] 📌 ¿Qué es Pendiente de la recta o inclinación de la recta?
> La pendiente (denotada con la letra **$m$**) es el "grado de inclinación" de una recta. Imagina que quieres ir de una **"Casa Morada"** a una **"Casa Verde"** en un mapa:
> 
> 1. Primero usas el **ascensor** (movimiento vertical en el eje **Y**): ¿cuánto subiste o bajaste?
> 2. Luego caminas por la **calle** (movimiento horizontal en el eje **X**): ¿cuánto avanzaste?
> 
> La pendiente es simplemente dividir ese movimiento del ascensor entre el movimiento de la calle:
> $$m = \frac{\text{Incremento en Y}}{\text{Incremento en X}} = \frac{y_2 - y_1}{x_2 - x_1}$$
> 
> - Si la recta sube (de izquierda a derecha), la pendiente es **positiva**.
> - Si la recta baja, la pendiente es **negativa**.
> - Si es totalmente horizontal (piso plano), la pendiente es **cero**.

> [!warning] ⚠️ Error común
> ❌ **Incorrecto:** Restar las coordenadas en desorden (mezclar el punto 1 con el punto 2 de forma cruzada) o poner las $X$ arriba.
> ✅ **Correcto:** Mantener la consistencia. Si eliges empezar con el punto $B$ arriba, debes empezar con el punto $B$ abajo: $\frac{y_2 - y_1}{x_2 - x_1}$.

> [!tip] 💡 Truco para recordarlo
> Para no olvidar la posición en la fórmula, recuerda: **"Lo que sube o baja (Y) va arriba; lo que avanza (X) va abajo"**.

---

### 📝 Procedimiento paso a paso

Sigue este protocolo lógico para no cometer errores en tus cálculos:

```text
1. IDENTIFICAR y etiquetar las coordenadas de los dos puntos como (x1, y1) y (x2, y2).
2. ESCRIBIR la fórmula fundamental: m = (y2 - y1) / (x2 - x1).
3. SUSTITUIR los valores. ¡OJO! Si un número es negativo, usa paréntesis. 
4. OPERAR las restas y simplificar la fracción resultante hasta su mínima expresión.
```

---

### Ejemplos Prácticos

> [!example] Ejemplo 1: Caso Básico
> **Puntos:** $A(2, 1)$ y $B(4, 5)$
> 1. **Etiquetamos:** $x_1=2, y_1=1$ | $x_2=4, y_2=5$.
> 2. **Sustituimos:** $m = \frac{5 - 1}{4 - 2}$
> 3. **Operamos:** $m = \frac{4}{2}$
> 4. **Resultado:** **$m = 2$** (La recta sube 2 unidades por cada 1 que avanza).

> [!example] Ejemplo 2: Caso con Signos Negativos
> **Puntos:** $C(-1, 4)$ y $D(6, -3)$
> 1. **Etiquetamos:** $x_1=-1, y_1=4$ | $x_2=6, y_2=-3$.
> 2. **Sustituimos:** $m = \frac{-3 - 4}{6 - (-1)}$
> 3. **Lógica de signos:** Fíjate en el denominador: $6 - (-1)$. Recuerda que el primer **menos** es de la fórmula y el segundo es del número; por eso, "menos por menos es más" y se vuelven una suma: $6 + 1 = 7$.
> 4. **Operamos:** $m = \frac{-7}{7}$
> 5. **Resultado:** **$m = -1$** (La pendiente es negativa, la recta va bajando).

> [!example] Ejemplo 3: Caso con Fracciones Heterogéneas
> **Puntos:** $A(1/2, 3/4)$ y $B(-2/3, 1/2)$
> *Nota: "Heterogéneas" solo significa que tienen diferente número abajo.*
> 1. **Numerador ($y_2 - y_1$):** $\frac{1}{2} - \frac{3}{4} = \frac{(1 \cdot 4) - (3 \cdot 2)}{2 \cdot 4} = \frac{4 - 6}{8} = \frac{-2}{8} = -\frac{1}{4}$ (Usamos el método de la **"carita feliz"**).
> 2. **Denominador ($x_2 - x_1$):** $-\frac{2}{3} - \frac{1}{2} = \frac{(-2 \cdot 2) - (1 \cdot 3)}{3 \cdot 2} = \frac{-4 - 3}{6} = -\frac{7}{6}$
> 3. **Operación Final:** Usamos la **"Ley de la oreja"** (extremos y medios):
>    $$\frac{-1/4}{-7/6} = \frac{-1 \cdot 6}{4 \cdot -7} = \frac{-6}{-28}$$
> 4. **Simplificamos:** **$m = \frac{3}{14}$**

> [!example] Ejemplo 4: Aplicación Real USD
> **Contexto:** El precio del dólar el lunes (día 1) es de $\$3.800$ y el miércoles (día 3) es de $\$3.900$.
> 1. **Puntos:** $(1, 3800)$ y $(3, 3900)$.
> 2. **Cálculo:** $m = \frac{3900 - 3800}{3 - 1} = \frac{100}{2}$
> 3. **Resultado:** **$m = 50$**
> 4. **Interpretación:** La pendiente es positiva, lo que significa que el dólar sube a una tasa de **$\$50$ por día**.

---

### 🏋️ Ejercicios para el estudiante

> [!abstract] 🟢 Nivel Verde (Fácil)
> Calcula la pendiente de las rectas que pasan por:
> 1. $(1, 2)$ y $(3, 6)$
> 2. $(0, 0)$ y $(2, 8)$
> 3. $(2, 3)$ y $(4, 7)$
> 4. $(5, 10)$ y $(10, 20)$

> [!abstract] 🟡 Nivel Amarillo (Medio)
> Calcula la pendiente incluyendo signos y fracciones con igual denominador:
> 1. $(-2, 3)$ y $(4, -5)$
> 2. $(-1, -1)$ y $(2, 2)$
> 3. $(1/5, 2/5)$ y $(3/5, 4/5)$
> 4. $(2, 5)$ y $(4, 1)$

> [!abstract] 🔴 Nivel Rojo (Avanzado)
> Resuelve los siguientes problemas de aplicación:
> 1. Un ahorro comenzó en el mes 2 con $\$50$ USD y en el mes 5 llegó a $\$110$ USD. ¿Cuál es el ritmo de ahorro mensual ($m$)?
> 2. Un termómetro marcaba $10^\circ$ a las 2:00 PM y $-2^\circ$ a las 6:00 PM. Calcula la pendiente de temperatura por hora.
> 3. Una rampa inicia en el suelo $(0, 0)$ y sube hasta una altura de 3 metros en una distancia horizontal de 12 metros $(12, 3)$. Calcula su inclinación.
> 4. **Interpreta:** Si la pendiente del precio de una consola de videojuegos es $m = -100$ USD/semana, ¿el precio está subiendo o bajando? ¿Cuánto cambia exactamente cada semana?

> [!success] ✅ Solucionario (Para el docente)
> **Verde:** 1) $m=2$ | 2) $m=4$ | 3) $m=2$ | 4) $m=2$.
> **Amarillo:** 1) $m=-4/3$ | 2) $m=1$ | 3) $m=1$ | 4) $m=-2$.
> **Rojo:** 1) $m=20$ USD/mes | 2) $m=-3^\circ$/hora | 3) $m=1/4$ | 4) El precio baja; disminuye $100$ USD cada semana.

---

### 🧠 Mini-prueba de autoevaluación

> [!question] Pregunta 1
> Si al calcular la pendiente el resultado es un número positivo (ej. $m = 5$), ¿qué dirección toma la recta en la gráfica de izquierda a derecha?
> > [!success] Respuesta
> > La recta es creciente, es decir, **sube**.

> [!question] Pregunta 2
> ¿Cuál es la pendiente de una recta que pasa por el origen $(0,0)$ y por el punto $(5, 15)$?
> > [!success] Respuesta
> > $m = \frac{15 - 0}{5 - 0} = \frac{15}{5} =$ **$3$**.

> [!question] Pregunta 3
> En un plan de ahorro, en el mes 2 tienes $\$50$ USD y en el mes 5 tienes $\$110$ USD. ¿Cuál es la pendiente de tu ahorro?
> > [!success] Respuesta
> > $m = \frac{110 - 50}{5 - 2} = \frac{60}{3} =$ **$20$**. Ahorras $\$20$ USD por mes.

---

> [!tip] 💡 En la próxima clase
> Ahora que sabes medir la inclinación ($m$), aprenderemos a usar este valor junto con un punto cualquiera para construir la **Ecuación Punto-Pendiente**. Esto nos permitirá crear la "fórmula mágica" de cualquier línea recta.

> [!info] 🧭 Navegación
> [[Clase02|⬅️ Clase 02: Representación en el plano cartesiano]] | [[Indice|🏠 Índice]] | [[Clase04|Clase 04: Ecuación Punto-Pendiente ➡️]]