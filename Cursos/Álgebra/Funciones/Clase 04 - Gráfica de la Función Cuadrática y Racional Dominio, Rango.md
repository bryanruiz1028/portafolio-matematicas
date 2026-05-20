# Clase 04 — Gráfica de la Función Cuadrática y Racional: Dominio, Rango y Asíntotas

tags: #algebra #graphofthequadr
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 4 de 12

> [!info] 🧭 Navegación
> - Anterior: [[Clase 03 - Tipos de Funciones]]
> - Índice: [[00 - Índice del curso]]
> - Siguiente: [[Clase 05 - Análisis de Parábolas y Asíntotas Oblicuas]]

---

### 🌍 Relevancia y aplicaciones

¿Qué tal amigos? Espero que estén muy bien. Hoy vamos a ver cómo las funciones cuadráticas y racionales modelan el mundo. Las parábolas describen trayectorias perfectas, mientras que las racionales nos enseñan que en la naturaleza existen límites que no siempre se pueden cruzar.

*   **💵 Aplicación $USD:** Las empresas utilizan la cima de la parábola (vértice) para encontrar el precio exacto que maximiza sus ingresos en dólares o el punto donde los costos de producción son mínimos.
*   **🏗️ Aplicación práctica:** Desde el diseño de cables en puentes colgantes hasta el cálculo de dónde caerá un proyectil; la física depende de la precisión de estas curvas.
*   **📊 Situación cotidiana:** Observa el chorro de agua de una fuente o cómo la señal de satélite rebota en el fondo de una antena parabólica; ahí hay matemáticas en acción.

---

### 📌 ¿Qué es la Función Cuadrática y la Asíntota?

> [!note] 📌 Conceptos clave
> - **Función Cuadrática:** Es una función de segundo grado ($ax^2 + bx + c$) cuya gráfica siempre es una **parábola**. Su dominio siempre son todos los números Reales ($\mathbb{R}$) porque la curva se abre infinitamente hacia la izquierda y la derecha.
> - **Asíntota:** Es una línea recta guía a la que la función se acerca cada vez más y más cuando tiende al infinito. Piensen en ella como una "pared" o "carril" que orienta el camino de la gráfica.

> [!warning] ⚠️ Error común: El mito de la asíntota
> Muchos estudiantes (y algunos profes) creen que la función **nunca** puede tocar la asíntota. ¡Cuidado! La función puede cruzar la asíntota horizontal en el "centro" de la gráfica. Lo que define a la asíntota es que la función se acerca a ella sin tocarla únicamente en los extremos (cuando $x$ es un número gigante o muy pequeño).

> [!tip] 💡 Truco para el Vértice
> Para no olvidar nunca cómo hallar el centro de tu parábola, apréndete esta rima:
> *"El opuesto de $b$, sobre el doble de $a$, el centro de tu gráfica te dará."*
> **Fórmula:** $x = \frac{-b}{2a}$

---

### 📋 Procedimiento paso a paso (El Método del Paréntesis)

Para graficar sin errores, sigue mi recomendación estrella:

```text
1. Identifica los coeficientes a, b, y c (con sus signos).
2. Calcula x del vértice usando x = -b / (2a).
3. Halla la y del vértice usando el "Método del Paréntesis": 
   Copia la función original, pero en lugar de la 'x', pon paréntesis vacíos ( ). 
   Luego, mete el valor de x dentro de esos paréntesis y resuelve.
4. Construye tu tabla de valores con el vértice en la fila central.
5. Elige dos valores menores y dos mayores a x. ¡Verás el "efecto espejo"!
```

---

### 📝 Ejemplos Prácticos

> [!example] Ejemplo 1: Caso Básico
> **Función:** $y = x^2 - 6x + 5$
> 1. $a=1, b=-6, c=5$.
> 2. Vértice $x$: $x = -(-6) / 2(1) = 3$.
> 3. Vértice $y$: $y = ( )^2 - 6( ) + 5 \rightarrow (3)^2 - 6(3) + 5 = 9 - 18 + 5 = -4$.
> 
> **Tabla con efecto espejo:**
> | x | y | Observación |
> |---|---|---|
> | 1 | 0 | Extremo izquierdo |
> | 2 | -3 | Un paso del centro |
> | **3** | **-4** | **Vértice (Centro)** |
> | 4 | -3 | ¡Efecto espejo! |
> | 5 | 0 | ¡Efecto espejo! |

> [!example] Ejemplo 2: Signos y Coeficientes
> **Función:** $y = 2x^2 - 4x - 1$
> Aquí $a=2$ (abre hacia arriba), $b=-4$.
> - $x = -(-4) / 2(2) = 4 / 4 = 1$.
> - Usando paréntesis: $y = 2(1)^2 - 4(1) - 1 = 2(1) - 4 - 1 = 2 - 4 - 1 = -3$.
> - **Rango:** Como abre hacia arriba, el rango empieza en el vértice y sube: $[-3, \infty)$. Usamos corchete $[$ porque el punto -3 sí se toca.

> [!example] Ejemplo 3: Introducción a Racionales (Los 3 Casos)
> Para $y = \frac{2x - 1}{x + 3}$, analicemos las asíntotas:
> 1. **Vertical:** Igualamos denominador a cero: $x + 3 = 0 \Rightarrow \mathbf{x = -3}$.
> 2. **Horizontal:**
>    - **Caso N=D:** Si los grados son iguales (como aquí, ambos grado 1), dividimos coeficientes: $y = 2/1 = \mathbf{2}$.
>    - **Caso N<D:** Si el grado de arriba es menor, la asíntota es siempre $\mathbf{y = 0}$.
>    - **Caso N>D:** Si el de arriba es mayor por uno, no hay horizontal, hay **oblicua** (la veremos luego).

> [!example] Ejemplo 4: Aplicación de Ganancia ($USD)
> Una tienda calcula su ganancia con $G(x) = -x^2 + 10x - 16$. ¿Cuántas unidades $x$ maximizan el beneficio?
> - $x = -10 / 2(-1) = 5$ unidades.
> - Ganancia máxima: $-(5)^2 + 10(5) - 16 = -25 + 50 - 16 = \mathbf{9\ USD}$.

---

### ✍️ Ejercicios para el estudiante

> [!abstract] 🟢 Nivel: Fácil
> 1. Identifica $a, b, c$ en $y = 3x^2 - 5x + 2$.
> 2. Calcula el $x$ del vértice para $y = x^2 - 2x + 8$.
> 3. En $y = 2x^2 + 8x - 1$, ¿cuánto vale $x$ del vértice?
> 4. ¿Hacia dónde abre $y = -x^2 + 4$?

> [!abstract] 🟡 Nivel: Medio
> Hallar el rango (usa corchetes y paréntesis correctamente) de estas funciones que abren hacia abajo:
> 1. $y = -x^2 + 2x + 3$ (Vértice $y=4$)
> 2. $y = -2x^2 + 8x - 5$ (Vértice $y=3$)
> 3. $y = -x^2 - 4x + 1$ (Vértice $y=5$)
> 4. $y = -3x^2 + 6x$ (Vértice $y=3$)

> [!abstract] 🔴 Nivel: Avanzado
> 1. Halla las asíntotas (V e H) de $y = \frac{3x + 2}{x - 5}$.
> 2. Halla la asíntota horizontal de $y = \frac{x + 1}{x^2 - 4}$ (Pista: Grado N < Grado D).
> 3. Una empresa tiene un costo promedio $C(x) = \frac{4x + 100}{x}$. Halla la asíntota horizontal. ¿Qué significa ese valor para el costo si producimos millones de unidades?
> 4. Realiza la tabla de 5 valores para $y = x^2 - 4x + 3$ centrada en el vértice.

---

### ✅ Respuestas para el docente

> [!success] Solucionario
> **Fácil:** 1) $a=3, b=-5, c=2$. 2) $x=1$. 3) $x=-2$. 4) Hacia abajo.
> **Medio:** 1) $(-\infty, 4]$. 2) $(-\infty, 3]$. 3) $(-\infty, 5]$. 4) $(-\infty, 3]$.
> **Avanzado:** 1) AV: $x=5$, AH: $y=3$. 2) AH: $y=0$ (Caso N<D). 3) AH: $y=4$. Significa que el costo mínimo se estabilizará en $4 USD. 4) Vértice en (2, -1). Puntos: (0,3), (1,0), (2,-1), (3,0), (4,3).

---

### 🧠 Mini-prueba de Autoevaluación

> [!question] 1. Sobre el Dominio
> ¿Cuál es el dominio de la función $f(x) = -5x^2 + 2x - 9$?
> - a) Solo reales negativos.
> - b) Todos los números Reales ($\mathbb{R}$).
> - c) Reales excepto el cero.
> - d) No tiene dominio.
> 
> **Respuesta: b.** Explicación: Como explica el Profe Alex, las parábolas se abren infinitamente, cubriendo todo el eje X.

> [!question] 2. Asíntotas en Racionales
> Si el grado del numerador es 1 y el del denominador es 2, ¿cuál es la asíntota horizontal?
> - a) No existe.
> - b) $y = 1$.
> - c) $y = 0$.
> - d) $y = 2$.
> 
> **Respuesta: c.** Explicación: Cuando el grado de abajo es mayor, la función siempre tiende a cero en el infinito.

> [!question] 3. Aplicación $USD
> En una función de costo $C(x) = x^2 - 20x + 150$, ¿en qué punto $x$ el costo deja de bajar y empieza a subir?
> - a) $x = 20$.
> - b) $x = 10$.
> - c) $x = -10$.
> - d) $x = 5$.
> 
> **Respuesta: b.** Explicación: $x = -(-20) / 2(1) = 10$. Es el punto mínimo de la parábola.

---

> [!tip] 💡 En la próxima clase
> ¿Qué tal amigos? No se pierdan la siguiente lección, donde veremos qué pasa cuando el grado de arriba es mayor al de abajo y aparecen las misteriosas **asíntotas oblicuas**.

> [!info] 🧭 Navegación
> - Anterior: [[Clase 03 - Tipos de Funciones]]
> - Índice: [[00 - Índice del curso]]
> - Siguiente: [[Clase 05 - Análisis de Parábolas y Asíntotas Oblicuas]]