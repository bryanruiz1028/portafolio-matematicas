# 📖 Guía de estudio — Clase 04: Gráfica y ecuación de la parábola conociendo el vértice y la directriz

¡Hola! En esta sesión vamos a dominar la construcción de parábolas paso a paso. No te preocupes si al principio ves muchas letras; verás que, siguiendo la lógica del "Profe Alex", todo se resume a ubicar puntos en el plano y contar distancias. ¡Vamos a ello!

> [!info] 📌 Conceptos clave
> Para entender la parábola, imagina que es una curva "equilibrada". Estos son sus pilares:
> 1. **Vértice $(h, k)$:** Es el punto más importante, el "corazón" de la parábola donde nace la curva.
> 2. **Directriz:** Es una recta fija. Imaginala como una pared: la parábola siempre le da la espalda y se abre hacia el lado contrario.
> 3. **El Parámetro $p$:** Es la distancia mágica. Es la separación exacta entre el vértice y la directriz. **¡Dato importante!** El vértice es el punto medio entre el foco y la directriz; por eso, la distancia del vértice al foco también es $p$.
> 4. **El "Truco de la Letra":** Para saber hacia dónde abre la parábola, mira la ecuación. **La letra que NO está al cuadrado indica el eje.** Si la **$x$** no está al cuadrado, es horizontal (abre a izquierda o derecha). Si la **$y$** no está al cuadrado, es vertical (abre arriba o abajo).
> 5. **Lado Recto ($4p$):** Es una línea que pasa por el foco y nos dice qué tan "ancha" o "abierta" es nuestra parábola.

---

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Vértice** | Punto de origen $(h, k)$. |
| **Parámetro ($p$)** | Distancia desde el Vértice ($V$) hasta la directriz (o hasta el Foco $F$). |
| **Ecuación Horizontal** | $(y - k)^2 = 4p(x - h)$ *(La $x$ no está al cuadrado)* |
| **Ecuación Vertical** | $(x - h)^2 = 4p(y - k)$ *(La $y$ no está al cuadrado)* |
| **Lado Recto (LR)** | $|4p|$ (Es el ancho total de la curva en el foco). |

---

> [!example] 📝 Ejemplos resueltos
>
> ### Ejemplo A: Caso Básico
> **Problema:** Hallar la ecuación de la parábola con vértice $V(-2, 4)$ y directriz en la recta $x = -3$.
> 
> **Paso 1: Determinar el parámetro $p$.**
> ¡Fíjate bien! La coordenada $x$ del vértice es $-2$ y la directriz está en $x = -3$. Si cuentas la distancia en el plano, hay solo **1 unidad** de diferencia. Entonces, $p = 1$.
> 
> **Paso 2: Identificar la orientación.**
> Como la directriz es vertical ($x = -3$) y el vértice está a su derecha, la parábola debe abrirse hacia la **derecha** (eje X positivo). ¡Recuerda que nunca debe cruzar la directriz!
> 
> **Paso 3: Sustituir en la fórmula.**
> Usamos la fórmula horizontal porque abre hacia el eje X: $(y - k)^2 = 4p(x - h)$.
> Aquí ocurre el "choque de signos" que explica el Profe Alex:
> $(y - 4)^2 = 4(1)(x - (-2))$
> **Resultado final:** $(y - 4)^2 = 4(x + 2)$
>
> ---
>
> ### Ejemplo B: Aplicación Real (Soporte de Antena)
> **Problema:** Diseñamos un soporte parabólico con vértice en $(3, 1)$ y directriz en $y = -1$. Si la instalación cuesta 50 USD por cada unidad del Lado Recto, ¿cuál es la ecuación y el costo?
>
> **Paso 1: Hallar $p$ y la orientación.**
> Del vértice ($y = 1$) a la directriz ($y = -1$) hay una distancia de **2 unidades**, así que $p = 2$. Como el vértice está arriba de la directriz, la parábola abre hacia **arriba** (eje Y positivo).
> 
> **Paso 2: Construir la ecuación.**
> ¡No te saltes pasos! Usamos la vertical: $(x - h)^2 = 4p(y - k)$.
> $(x - 3)^2 = 4(2)(y - 1)$
> **Resultado de la ecuación:** $(x - 3)^2 = 8(y - 1)$
> 
> **Paso 3: Calcular el costo.**
> El Lado Recto es $4p$, es decir, $4 \times 2 = 8$ unidades.
> Costo: $8 \text{ unidades} \times 50 \text{ USD} = 400 \text{ USD}$.
> **Resultado:** La inversión necesaria es de **400 USD**.

---

> [!abstract] ✍️ Ejercicios de repaso
>
> ### 🟢 Nivel: Fácil (Identificación)
> 1. Una parábola tiene $V(0,0)$ y directriz $y = -2$. ¿Cuánto vale $p$ y hacia dónde abre?
> 2. Si el vértice está en $(4, 5)$ y la directriz es $x = 6$, calcula el valor de $p$.
> 3. Identifica el vértice y el parámetro $p$ si la directriz es $y = 10$ y el vértice es $(0, 5)$.
>
> ### 🟡 Nivel: Medio (Construcción de Ecuación)
> 1. Encuentra la ecuación canónica con $V(2, 2)$ y directriz $x = 0$.
> 2. Halla la ecuación si el vértice es el origen $V(0, 0)$ y la directriz es $y = 3$.
> 3. Escribe la ecuación para $V(-1, 4)$ con directriz $x = -5$.
>
> ### 🔴 Nivel: Avanzado (Aplicación $USD)
> 1. Una empresa cobra 100 USD por cada metro de cable para marcar la directriz. Si una parábola tiene $V(1, -5)$, abre hacia la izquierda con $p=3$, halla su ecuación y el costo total si la directriz cruza todo el eje vertical visible (asumiendo que el eje visible mide 10 unidades).
> 2. Se fabrica un reflector con $V(0, 2)$ y directriz $y = 0$. Si el material del Lado Recto cuesta 75 USD por unidad de longitud, ¿cuál es la ecuación canónica y el presupuesto total para el Lado Recto?

---

> [!tip] 💡 Consejo de estudio: ¡Cuidado con los signos!
> El error más común es olvidar que la fórmula tiene un "menos" de fábrica: $(x - h)$ y $(y - k)$. 
> 
> ¡Fíjate en este detalle! Cuando pasas las coordenadas del vértice a la ecuación, **los signos siempre parecen invertirse**:
> - Si el vértice es **positivo** como $(3, 2)$, en el paréntesis verás $(x - 3)$ y $(y - 2)$.
> - Si el vértice es **negativo** como $(-3, -2)$, la resta de la fórmula choca con el negativo del número y se vuelve positivo: $(x + 3)$ y $(y + 2)$.
> 
> **Regla de oro:** ¡Al escribir la ecuación, cámbiale el signo a las coordenadas del vértice!