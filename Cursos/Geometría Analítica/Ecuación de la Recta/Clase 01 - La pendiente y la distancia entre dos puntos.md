# Clase 01 — La pendiente y la distancia entre dos puntos

`#algebra` `#pendientederecta`

[Ir a la Introducción del Curso] | [Siguiente Clase: Ecuación de la Recta]

---

¡Qué tal, amigos! Espero que estén muy bien. Bienvenidos al inicio de este curso sobre la línea recta. Hoy vamos a transformar esos dibujos que vemos en el plano cartesiano en números y datos precisos aprendiendo a medir la inclinación (pendiente) y la longitud (distancia) entre cualquier pareja de puntos.

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> La pendiente y la distancia son las herramientas básicas para cuantificar el espacio. Sin ellas, no podríamos diseñar caminos seguros ni entender cómo cambian las variables en el tiempo.
> 
> - 💵 **Aplicación financiera:** La pendiente representa la "razón de cambio". Si graficamos una inversión, la pendiente nos dice exactamente cuántos dólares ($USD$) ganamos por cada día que pasa.
> - 🏗️ **Aplicación práctica:** En arquitectura, la pendiente define la inclinación de rampas para sillas de ruedas o la caída de un techo para que el agua de lluvia no se estanque.
> - 📊 **Situación cotidiana:** Imagina a un ciclista; la pendiente determina su esfuerzo. Si es positiva, le toca pedalear fuerte (subida); si es cero, va relajado (plano).

---

## Concepto clave

> [!note] 📌 ¿Qué es la pendiente de una recta?
> La pendiente (representada con la letra $m$) es la **razón de cambio** o la proporción entre el desplazamiento vertical (Eje $y$) y el desplazamiento horizontal (Eje $x$). 
> 
> Matemáticamente, si tenemos dos puntos $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$, la fórmula que utilizaremos es:
> $$m = \frac{y_2 - y_1}{x_2 - x_1}$$

> [!warning] ⚠️ Error común
> Muchos estudiantes se confunden y colocan el desplazamiento de $x$ en la parte de arriba. 
> **✅ Correcto:** El cambio en $y$ (vertical) siempre es el numerador. $m = \text{Desplazamiento en } y / \text{Desplazamiento en } x$.

> [!tip] 💡 Truco para recordarlo
> Para no olvidar el orden, recuerda: **"Primero tienes que subir o bajar del elevador ($y$) antes de poder caminar por el pasillo ($x$)"**. El movimiento vertical siempre manda arriba.

### Tipos de Rectas según su pendiente
1. **Horizontal:** Es totalmente plana, paralela al eje $x$. Como no hay subida ni bajada, el desplazamiento en $y$ es cero, por lo tanto, su pendiente es cero ($m = 0$). ¡Es como caminar en una habitación nivelada!
2. **Vertical:** Es paralela al eje $y$. Aquí el avance en $x$ es cero, y como no se puede dividir entre cero, decimos que su **pendiente es indefinida**.
3. **Inclinada:** Corta ambos ejes. Si al verla de izquierda a derecha "sube", la pendiente es **positiva** ($m > 0$). Si "baja", la pendiente es **negativa** ($m < 0$).

---

## Procedimiento paso a paso: Distancia entre puntos

Para hallar la distancia ($d$) entre dos puntos, el Profe Alex nos recuerda que estamos aplicando, en esencia, el **Teorema de Pitágoras** en el plano.

1. **Identificar coordenadas:** Nombra tus puntos como $(x_1, y_1)$ y $(x_2, y_2)$.
2. **Calcular los "catetos":** Encuentra la diferencia entre las coordenadas. El cateto horizontal es $(x_2 - x_1)$ y el vertical es $(y_2 - y_1)$.
3. **Elevar al cuadrado y sumar:** Eleva ambos resultados al cuadrado (esto hace que cualquier signo negativo se vuelva positivo) y súmalos.
4. **Raíz cuadrada:** Aplica la raíz cuadrada al resultado final para obtener la distancia.
   $$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

---

## Ejemplos de clase

> [!example] Ejemplo 1: Cálculo Básico
> **Hallar la distancia entre $A(1, 7)$ y $B(4, 3)$.**
> - Diferencia en $x$: $4 - 1 = 3$
> - Diferencia en $y$: $3 - 7 = -4$
> - Pitágoras: $3^2 + (-4)^2 = 9 + 16 = 25$
> - Resultado: $d = \sqrt{25} = 5$ unidades.

> [!example] Ejemplo 2: Manejo de Signos
> **Calcular la distancia entre $P(-5, 2)$ y $Q(0, -4)$.**
> - Diferencia en $x$: $0 - (-5) = 5$ (¡Cuidado con el doble menos!)
> - Diferencia en $y$: $-4 - 2 = -6$
> - Pitágoras: $5^2 + (-6)^2 = 25 + 36 = 61$
> - Resultado: $d = \sqrt{61} \approx 7.81$ unidades.

> [!example] Ejemplo 3: Pendiente a partir de desplazamientos
> **Una recta avanza 6 unidades en $x$ y baja 2 unidades en $y$. Hallar $m$.**
> - Cambio en $y = -2$ (porque baja).
> - Cambio en $x = 6$.
> - $m = -2 / 6$.
> - Resultado: $m = -1/3$.

> [!example] Ejemplo 4: Aplicación Financiera ($USD$)
> **Un activo financiero vale $\$1$ el día 1 y $\$7$ el día 4. ¿Cuál es la magnitud del cambio (distancia) en el gráfico?**
> - Puntos: $(1, 1)$ y $(4, 7)$. Aquí el eje $x$ es el tiempo y el eje $y$ es el dinero.
> - Cateto temporal ($x$): $4 - 1 = 3$ días.
> - Cateto monetario ($y$): $7 - 1 = 6$ dólares.
> - Magnitud: $d = \sqrt{3^2 + 6^2} = \sqrt{45} \approx 6.71$. 
> *Nota: Esta distancia es una abstracción visual que representa la longitud del segmento que une ambos estados financieros.*

---

## Ejercicios para el estudiante

> [!abstract] 🟢 Nivel Verde (Fácil)
> 1. Hallar la distancia entre $(2, 1)$ y $(5, 1)$.
> 2. Hallar la distancia entre $(3, 2)$ y $(3, 6)$.
> 3. Hallar la distancia entre $(10, 5)$ y $(13, 9)$.
> 4. Si una recta es horizontal y pasa por $y = 4$, ¿cuál es su pendiente $m$?

> [!abstract] 🟡 Nivel Amarillo (Medio)
> 1. Calcular la distancia entre $(-2, 3)$ y $(4, -1)$.
> 2. Hallar la pendiente de la recta que pasa por $(1, 1)$ y $(3, 5)$.
> 3. Calcular la distancia entre $(-1, -1)$ y $(2, 3)$.
> 4. Hallar $m$ si avanzamos 10 unidades en $x$ y bajamos 5 unidades en $y$.

> [!abstract] 🔴 Nivel Rojo (Avanzado)
> 1. Una deuda financiera pasa de $\$100$ a $\$40$ en 3 meses. Si el mes es el eje $x$ y el dinero el eje $y$, calcula la pendiente de la deuda.
> 2. Determina la distancia exacta entre $A(-5, -2)$ y $B(0, 10)$.
> 3. Un precio sube de $\$10$ a $\$20$ en 2 días. Calcula la pendiente y la longitud (distancia) del segmento en el gráfico.
> 4. Si la pendiente es $m = 2$ y el desplazamiento en $x$ es 3, ¿cuánto fue el desplazamiento en $y$?

> [!success] ✅ Respuestas para el docente
> **Verde:** 1) 3 | 2) 4 | 3) 5 | 4) $m = 0$.
> **Amarillo:** 1) $\sqrt{52} \approx 7.21$ | 2) $m = 2$ | 3) 5 | 4) $m = -1/2$.
> **Rojo:** 
> 1) $m = -20$ $USD$/mes. (Razonamiento: $\frac{40 - 100}{3} = \frac{-60}{3} = -20$. Significa que la deuda baja 20 dólares cada mes).
> 2) $d = 13$ unidades.
> 3) $m = 5$, $d = \sqrt{104} \approx 10.19$.
> 4) $\Delta y = 6$.

---

## Mini-prueba de autoevaluación

> [!question] 1. Conceptual
> Si una recta es perfectamente horizontal, ¿por qué su pendiente es cero?
> *Respuesta: Porque el desplazamiento vertical ($y_2 - y_1$) es cero. Al dividir cero entre cualquier avance en $x$, el resultado es siempre cero.*

> [!question] 2. Procedimental
> ¿Por qué elevamos al cuadrado las diferencias de las coordenadas al buscar la distancia?
> *Respuesta: Porque buscamos aplicar el Teorema de Pitágoras ($a^2 + b^2 = c^2$) y para asegurar que todas las distancias sean positivas, ya que no existen longitudes negativas.*

> [!question] 3. Aplicación Financiera
> En un gráfico de ahorros, si calculas una pendiente de $m = -2$, ¿tu dinero está aumentando o disminuyendo?
> *Respuesta: Está disminuyendo. Una pendiente negativa en un contexto financiero indica una pérdida o descenso de valor por cada unidad de tiempo.*

---

## Notas para el próximo tema

> [!tip] 💡 En la próxima clase
> ¡Excelente trabajo hoy! Ahora que ya saben medir qué tan inclinada está una recta y cuánto mide un segmento, estamos listos para el siguiente nivel: aprender a escribir la **Ecuación de la Recta** en su forma punto-pendiente. Esto nos permitirá describir cualquier camino lineal con una simple fórmula.

Espero que les haya gustado la clase. Si fue así, los invito a que sigan practicando con los ejercicios. ¡Nos vemos en el próximo video! **Bye, bye.**

---
[Ir a la Introducción del Curso] | [Siguiente Clase: Ecuación de la Recta]