# Clase 01 — Introducción a los Vectores, Magnitud y Componentes

#física #matemáticas #vectores #introducción #educación
**Curso:** Fundamentos de Física y Matemáticas

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [Inicio del Curso] | ➡️ **Siguiente:** [Suma de Vectores]

---

## ¿Por qué es importante esta clase?

Los vectores son herramientas fundamentales para representar cómo actúan las fuerzas y cómo ocurren los movimientos en nuestro espacio tridimensional. Sin ellos, sería imposible calcular con precisión hacia dónde se dirige un objeto o cuánta potencia se necesita para mover una estructura, ya que en el mundo físico no solo importa "cuánto", sino también "hacia dónde".

*   **💵 [Aplicación $USD]:** El flujo de dinero se puede entender mediante vectores; los ingresos son vectores hacia arriba (positivos) y los egresos son vectores en dirección opuesta (negativos), determinando el saldo neto.
*   **🏗️ [Aplicación práctica]:** En la ingeniería civil, se utilizan para calcular la resistencia de las vigas en un edificio, analizando cómo el peso y el viento presionan en distintas direcciones.
*   **📊 [Situación cotidiana]:** Cuando usas un GPS para caminar "3 km al Norte", estás usando un vector. Si solo caminaras "3 km" sin dirección, podrías terminar en cualquier lugar.

---

## Concepto clave

Un **vector** es una magnitud que se representa mediante una flecha. Para entenderlo fácilmente, piensa en él como una instrucción que indica **cuánto** (su tamaño) y **hacia dónde** (su dirección y sentido). Mientras que una magnitud **escalar** se define solo con un número y su unidad (como 12 kg de masa o 5 horas de tiempo), la magnitud **vectorial** necesita orientación. 

Para visualizar las componentes, usemos la **metáfora de la sombra**: Imagina que el vector es un palo inclinado. Si pones una linterna justo encima, la "sombra" que proyecta en el suelo es la **componente X**. Si pones la linterna a un lado, la "sombra" que proyecta en la pared es la **componente Y**. Además, recuerda que un vector no cambia si lo mueves de lugar, siempre que mantengas su medida y su inclinación.

> [!warning] ⚠️ Error común
> Confundir la **rapidez** con la **velocidad**. La rapidez es escalar (ej. 5 km/h), pero la velocidad es un vector porque indica hacia dónde te mueves (ej. 5 km/h hacia el Norte).

> [!tip] 💡 Truco para recordarlo
> Para que algo sea un vector, debe cumplir con la regla **M-D-S**:
> 1. **M**agnitud: ¿Cuánto mide la flecha? (También llamado módulo o norma).
> 2. **D**irección: El ángulo o inclinación respecto al eje X.
> 3. **S**entido: Hacia dónde apunta la punta de la flecha (la cabeza del vector).

---

## Procedimiento paso a paso

Para hallar las componentes rectangulares de un vector, sigue este procedimiento técnico. Es vital que las unidades de las componentes sean las mismas que las del vector original (si el vector está en metros, sus componentes también).

```text
PASO 1: Identificar la magnitud y el ángulo (θ) del vector.
        ¡IMPORTANTE!: Asegúrate de que tu calculadora esté en modo "DEG" (Grados).
PASO 2: Determinar los signos (+/-) según el cuadrante:
        - Derecha (Este) es +X  |  Izquierda (Oeste) es -X
        - Arriba (Norte) es +Y  |  Abajo (Sur) es -Y
PASO 3: Calcular la componente X (la sombra horizontal):
        Vx = magnitud * cos(θ)
PASO 4: Calcular la componente Y (la sombra vertical):
        Vy = magnitud * sen(θ)
```

---

## Ejemplos prácticos

> [!abstract] Ejemplo 1: Cálculo de magnitud básico
> Si tenemos un vector con componentes (3, 4), para hallar su magnitud aplicamos el Teorema de Pitágoras:
> $$\text{Magnitud} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5 \text{ unidades}$$

> [!abstract] Ejemplo 2: Uso de signos por dirección (Video Ejemplo 2)
> Un vector de **10 m** con dirección **Oeste 20° Norte**:
> - Al ser **Oeste**, $V_x$ es negativo: $V_x = -10 \cdot \cos(20^\circ) \approx -9.39 \text{ m}$.
> - Al ser **Norte**, $V_y$ es positivo: $V_y = 10 \cdot \sin(20^\circ) \approx 3.42 \text{ m}$.
> *Nota: La sombra horizontal es mucho más larga que la vertical.*

> [!abstract] Ejemplo 3: Magnitud con componentes negativas
> Hallar la magnitud del vector $\vec{B} = (-5, 2)$.
> $$\text{Magnitud} = \sqrt{(-5)^2 + 2^2} = \sqrt{25 + 4} = \sqrt{29} \approx 5.38 \text{ unidades}$$
> *Nota: Al elevar al cuadrado, el negativo desaparece porque $(-5) \cdot (-5) = 25$.*

> [!abstract] Ejemplo 4: Aplicación financiera ($USD)
> Consideremos un balance financiero: una ganancia de $100 USD (vector hacia arriba) y una pérdida de $40 USD (vector hacia abajo).
> El **vector resultante** es la suma algebraica: $100 \text{ USD} + (-40 \text{ USD}) = +60 \text{ USD}$.

---

## Ejercicios para el estudiante

### Nivel Verde (Básico)
1. Un vector tiene magnitud de 20 cm y un ángulo de 30° en el primer cuadrante. Calcule sus componentes $X$ e $Y$.
2. Clasifique las siguientes medidas: una masa de 50 kg y una fuerza de 10 N aplicada hacia el Sur. ¿Cuál es escalar y cuál es vectorial?

### Nivel Amarillo (Intermedio)
3. Calcule la magnitud de un vector cuyas componentes son $C_x = 2$ y $C_y = -4$.
4. Si un vector de 4.5 m apunta al Sur-Oeste (exactamente a 45°), ¿por qué sus componentes son idénticas en valor numérico? Explica pedagógicamente.

### Nivel Rojo (Avanzado - $USD)
5. Un inversor registra un crecimiento de 15 unidades y una caída de 8 unidades en un mismo eje. Calcule la magnitud de su posición final respecto al origen.
6. Calcule las componentes rectangulares del vector $\vec{A} = 15 \text{ cm}$ con dirección **Este 45° Sur**.

> [!success] ✅ Respuestas
> 1. $V_x = 17.32 \text{ cm}$, $V_y = 10 \text{ cm}$.
> 2. Masa = Escalar; Fuerza = Vectorial.
> 3. Magnitud $\approx 4.47 \text{ unidades}$.
> 4. Porque el ángulo de 45° divide el cuadrante de 90° exactamente por la mitad, haciendo que las "sombras" (catetos) sean iguales. $V_x = -3.18 \text{ m}$, $V_y = -3.18 \text{ m}$.
> 5. 7 unidades de magnitud.
> 6. $A_x = 10.61 \text{ cm}$, $A_y = -10.61 \text{ cm}$.

---

## Autoevaluación y Cierre

**1. ¿Qué tres elementos necesita una magnitud vectorial para estar completa?**
   a) Número, unidad y color.
   b) Magnitud, dirección y sentido.
   c) Solo magnitud y ángulo.
   *Respuesta: **b**. Sin dirección y sentido, no sabemos hacia dónde actúa el vector.*

**2. Si un vector apunta hacia el Oeste, ¿qué signo tendrá su componente horizontal ($V_x$)?**
   a) Positivo (+).
   b) Negativo (-).
   c) Cero.
   *Respuesta: **b**. En el plano cartesiano y geográfico, el Oeste representa el lado negativo de las X.*

**3. En un gráfico de $USD, si el vector de "Pérdida" es más largo que el de "Ganancia", ¿qué indica su magnitud?**
   a) Que el valor absoluto de la deuda es mayor que el ingreso.
   b) Que el dinero se mueve hacia el Este.
   c) Que el ángulo es de 45°.
   *Respuesta: **a**. La magnitud representa el "cuánto", es decir, el tamaño del movimiento financiero.*

---

## Notas para el próximo tema
En la siguiente sesión aprenderemos la **Suma de Vectores**. Utilizaremos las componentes que calculamos hoy para encontrar un único vector resultante que represente la combinación de varias fuerzas.

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [Inicio del Curso] | ➡️ **Siguiente:** [Suma de Vectores]