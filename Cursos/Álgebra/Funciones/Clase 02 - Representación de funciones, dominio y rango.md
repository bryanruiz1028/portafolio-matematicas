# Clase 02 — Representación de funciones, dominio y rango

tags: #algebra #representationo
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 12

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | [[Clase 03|Clase 03 ➡]]

---

> [!info] 🌍 Relevancia y aplicaciones
> ¡Bienvenido! Hoy aprenderás el lenguaje secreto que usan los programadores, ingenieros y científicos para predecir el futuro. Dominar las funciones te da el "superpoder" de entender cómo una acción provoca un resultado exacto en el mundo real.
> - 💵 **Finanzas:** Calcular el costo total de un servicio en $USD (por ejemplo, una tarifa fija más un costo por cada hora de soporte técnico).
> - 🏗️ **Ingeniería:** Diseñar la curvatura de un puente o medir la resistencia de un material según la presión que recibe.
> - 📊 **Vida cotidiana:** Predecir a qué hora llegarás a tu destino basándote en la velocidad de tu bicicleta y el tiempo de pedaleo.

---

### 3. Concepto Clave: Representación de funciones

> [!note] 📌 ¿Qué es Representación de funciones?
> Representar una función es mostrar cómo se conectan dos mundos: el de los datos que entran ($x$) y el de los resultados que salen ($y$). 
> **Dato vital:** En matemáticas, escribir $y$ es exactamente lo mismo que escribir $f(x)$. ¡No te confundas, son gemelos!
>
> Una función se puede mostrar de 4 formas:
> 1. **Expresión analítica:** La "fórmula" mágica (ej. $f(x) = x^2$).
> 2. **Tabla de valores:** Una lista organizada de entradas y salidas.
> 3. **Parejas ordenadas:** Coordenadas del tipo $(entrada, resultado)$.
> 4. **Gráfica:** El dibujo de la relación en el plano cartesiano.
>
> **Término clave: La Imagen.** El valor específico que sale de la función tras procesar una $x$ se llama **Imagen**. El conjunto de todas las imágenes que realmente "existen" se llama **Rango**.

> [!warning] ⚠️ Error común
> 1. **¿Una o varias flechas?** Para que sea función, de cada número de entrada debe salir **una y solo una** flecha. Si un número tiene dos resultados distintos, ¡no es función!
> 2. **¡Cuidado con los signos!** Al elevar un número negativo al cuadrado, el resultado SIEMPRE es positivo. Ejemplo: $(-3)^2 = 9$. Muchos estudiantes olvidan el paréntesis y escriben $-9$, lo cual es un error que "rompe" tu gráfica.

> [!tip] 💡 Truco para recordarlo
> Imagina que la función es una **"maquinita"**. Tú metes un número (esto es el **Dominio**), la máquina hace un proceso y te entrega un resultado (la **Imagen**). Si intentas meter un número que la máquina no puede procesar (como un negativo en una raíz cuadrada), la máquina **se traba o se daña**. Esos números que "traban" la máquina no pertenecen al Dominio.

---

### 4. Procedimiento paso a paso

Para graficar una función lineal como un experto, sigue estos 4 pasos:

```text
PASO 1 → Despejar la variable 'y' para dejarla sola (ej. y = 2x + 1).
PASO 2 → Construir la tabla de valores (elige 3 valores fáciles para 'x', como 0, 1 y 2).
PASO 3 → Ubicar los puntos resultantes (las parejas ordenadas) en el plano cartesiano.
PASO 4 → Unir los puntos con una regla para trazar la línea recta.
```

---

### 5. Ejemplos Prácticos

```ad-example
title: **Ejemplo 1: Caso básico ($y = 3x - 2$)**
Evaluamos la función eligiendo valores sencillos para $x$:
- Si $x = 0$: $y = 3(0) - 2 = -2 \rightarrow$ Punto $(0, -2)$
- Si $x = 1$: $y = 3(1) - 2 = 1 \rightarrow$ Punto $(1, 1)$
- Si $x = 2$: $y = 3(2) - 2 = 4 \rightarrow$ Punto $(2, 4)$
**Resultado:** Al unir estos puntos en el plano, verás una línea recta que sube hacia la derecha.
```

```ad-example
title: **Ejemplo 2: Dominio y Rango ($f(x) = \sqrt{x}$)**
Aquí la "maquinita" se traba con negativos, porque no hay raíces cuadradas de números negativos en los reales.
- **Dominio:** $[0, \infty)$ (Desde el cero inclusive hasta el infinito).
- **Rango:** $[0, \infty)$ (Los resultados siempre serán positivos o cero).
**Gráfica:** Usamos un **punto cerrado** $\bullet$ y corchetes $[ ]$ cuando incluimos el número, y un **punto abierto** $\circ$ con paréntesis $( )$ cuando el número no forma parte del conjunto.
```

```ad-example
title: **Ejemplo 3: Caso avanzado ($3y - 2x = 4$)**
Primero, debemos despejar la $y$ para que sea fácil trabajar:
1. $3y = 4 + 2x$
2. $y = \frac{4 + 2x}{3}$
Si $x = 1$: $y = \frac{4 + 2(1)}{3} = \frac{6}{3} = 2 \rightarrow$ Punto $(1, 2)$.
**Manejo de fracciones:** Si el resultado fuera $4/3$, dividimos la unidad del eje $Y$ en 3 partes iguales y contamos 4 desde el cero.
```

```ad-example
title: **Ejemplo 4: Aplicación en $USD**
Una suscripción de juegos cuesta $5 USD de base más $2 USD por cada nivel premium desbloqueado ($x$).
**Fórmula:** $y = 2x + 5$
- Con 0 niveles: $y = 2(0) + 5 = 5$ USD.
- Con 3 niveles: $y = 2(3) + 5 = 11$ USD.
Aquí el **Dominio** son los niveles (0, 1, 2...) y el **Rango** es el dinero total en $USD que pagarás.
```

---

### 6. Ejercicios para el Estudiante

```ad-abstract
title: 🟢 Nivel Fácil: Identificación
1. En una tabla, si $x=5$ tiene como resultados $y=10$ y $y=12$ al mismo tiempo, ¿es una función?
2. Indica el dominio de este conjunto: $\{(0, 2), (1, 4), (2, 6)\}$.
3. Si la función es $f(x) = x^2$, ¿cuál es la **imagen** del número $-4$? (¡Recuerda el signo!).
4. En una gráfica que va desde $x = -5$ hasta $x = 10$, ¿cuál es su dominio?
```

```ad-abstract
title: 🟡 Nivel Medio: Gráficas simples
Grafica las siguientes funciones creando una tabla con $x = \{0, 1, 2\}$:
1. $y = 2x + 1$
2. $y = x - 3$
3. $f(x) = 3x$
4. $y = -x + 2$
```

```ad-abstract
title: 🔴 Nivel Avanzado: Aplicaciones $USD
Resuelve y representa:
1. Un envío cuesta $4 USD fijos más $2 USD por cada kg de peso. Escribe la función y calcula el costo de enviar 10 kg.
2. Un técnico cobra $15 USD por la visita y $20 USD por cada hora de reparación. ¿Cuánto cuesta un arreglo de 2 horas?
3. Tienes $50 USD en tu billetera y gastas $5 USD cada día en almuerzo. Escribe la función del dinero que te queda tras $x$ días.
4. Un artista vende cuadros a $100 USD cada uno, pero gasta $20 USD en materiales por cada cuadro. Escribe la función de su ganancia neta.
```

```ad-check
title: ✅ Respuestas para el docente
- **Fácil:** 1. No (una entrada no puede tener dos salidas). 2. $D = \{0, 1, 2\}$. 3. 16. 4. $[-5, 10]$.
- **Medio:** 1. Puntos $(0,1), (1,3), (2,5)$. 2. Puntos $(0,-3), (1,-2), (2,-1)$. 3. Puntos $(0,0), (1,3), (2,6)$. 4. Puntos $(0,2), (1,1), (2,0)$.
- **Avanzado:** 1. $y = 2x + 4$; $24 USD. 2. $y = 20x + 15$; $55 USD. 3. $y = -5x + 50$. 4. $y = 80x$ (Ganancia menos gasto).
```

---

### 7. Autoevaluación

> [!question] ¿Cómo se le llama al conjunto de todos los resultados (valores de $y$) que salen de la función?
> A) Dominio.
> B) Rango o conjunto de imágenes.
> C) Expresión analítica.
> *Respuesta correcta: B*

> [!question] Si evaluamos $f(x) = x^2 + 1$ con $x = -2$, el resultado es:
> A) -3
> B) 3
> C) 5
> *Respuesta correcta: C (porque $(-2)^2 = 4$, y $4 + 1 = 5$)*

> [!question] En un plan de celular que cuesta $10 USD fijos y $0.5 USD por cada GB extra ($x$), ¿qué representa la $x$?
> A) El costo total de la factura.
> B) Los GB adicionales consumidos (Dominio).
> C) El cargo fijo mensual.
> *Respuesta correcta: B*

---

> [!tip] 💡 En la próxima clase
> Ya dominas cómo se ven las funciones en el papel. En la siguiente clase, aprenderemos a clasificar las funciones por su "personalidad": ¡conoceremos las **Funciones Lineales, Cuadráticas y constantes**!

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | [[Clase 03|Clase 03 ➡]]