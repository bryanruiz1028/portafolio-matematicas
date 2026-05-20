# Clase 03 — Sistemas de Ecuaciones 2x2 | Método de Sustitución y Determinantes

`#algebra` `#systemsofxlinea`

> [!info] Navegación
> ← [Clase 02 — Sistemas de Ecuaciones: Introducción](link_clase_02) | [Índice General](link_indice) | [Clase 04 — Métodos de Igualación y Gráfico](link_clase_04) →

---

## 🌍 Relevancia y aplicaciones

> [!info] 🌍 Relevancia y aplicaciones
> Resolver un sistema de ecuaciones consiste en encontrar los valores de variables desconocidas (generalmente $x$ e $y$) que satisfacen múltiples condiciones simultáneamente.
> * 💵 **Transacciones comerciales:** Calcular precios unitarios cuando solo conocemos el total de compras combinadas.
> * 🏗️ **Ingeniería:** Determinar el equilibrio de fuerzas o la cantidad exacta de materiales necesarios en una obra.
> * 📊 **Comparativa de servicios:** Evaluar planes de suscripción para hallar el punto donde un servicio se vuelve más económico que otro.

---

## 💡 Concepto Clave y Errores Comunes

> [!note] ¿Qué es un sistema 2x2?
> Imagina que tienes dos acertijos matemáticos conectados. Tu misión es encontrar un valor para $x$ y un valor para $y$ que hagan que ambos acertijos sean ciertos al mismo tiempo. Un sistema 2x2 son dos ecuaciones que comparten la misma solución.

> [!warning] El error del desorden
> Antes de aplicar el método de Cramer, las ecuaciones **deben estar ordenadas**. Si no lo están, los resultados serán incorrectos.
> * **Orden correcto:** Las letras $x$ e $y$ deben estar a la izquierda del igual y el número solo (término independiente) a la derecha.
> * **Formato:** $Ax + By = C$

> [!tip] La regla de oro de Cramer
> El **Determinante del Sistema ($\Delta$)** es el valor más importante: es el número que siempre irá en el denominador (abajo) al calcular los valores finales de $x$ e $y$. ¡Es uno de los métodos más sencillos y mecánicos que existen!

---

## ⚙️ Procedimientos Paso a Paso

### Bloque 1: Método de Sustitución (El truco del paréntesis)
```text
1. DESPEJAR: Elige una letra (x o y) en una de las ecuaciones y déjala sola.
   (Consejo: Elige la que sea positiva o no tenga número al lado).
2. REEMPLAZAR: Aquí aplicamos el "Truco del Profe Alex": 
   Copia la otra ecuación exactamente igual, pero en lugar de la letra 
   que despejaste, abre un paréntesis grande ( ) y mete allí lo que despejaste.
3. RESOLVER: Realiza las operaciones para hallar el valor de la única letra que queda.
4. HALLAR LA SEGUNDA LETRA: Usa ese resultado para encontrar el valor de la letra faltante.
```

### Bloque 2: Método de Determinantes (Cramer)
```text
1. ORDENAR: Asegúrate de tener el formato Ax + By = C.
2. DETERMINANTE DEL SISTEMA (Δ): Usa los coeficientes de x y y.
   REGLA: (Diagonal principal) - (Diagonal secundaria).
3. DETERMINANTES DE VARIABLES:
   - "Determinante cambiando la x" (Δx): Cambia los números de x por los independientes.
   - "Determinante cambiando la y" (Δy): Cambia los números de y por los independientes.
4. DIVIDIR: 
   - x = Δx / Δ
   - y = Δy / Δ
```

---

## 📝 Ejemplos Desarrollados

> [!ad-example] Ejemplo 1: Cramer Básico (Paso a Paso)
> **Sistema:**
> $7x + 4y = 13$
> $5x - 2y = 19$
>
> 1. **Hallar $\Delta$ (Sistema):**
>    $\begin{vmatrix} 7 & 4 \\ 5 & -2 \end{vmatrix} = (7 \cdot -2) - (4 \cdot 5) = -14 - 20 = -34$
> 2. **Hallar $\Delta x$ (Cambiando $x$ por los independientes $13$ y $19$):**
>    $\begin{vmatrix} 13 & 4 \\ 19 & -2 \end{vmatrix} = (13 \cdot -2) - (4 \cdot 19) = -26 - 76 = -102$
> 3. **Hallar $\Delta y$ (Cambiando $y$ por los independientes $13$ y $19$):**
>    $\begin{vmatrix} 7 & 13 \\ 5 & 19 \end{vmatrix} = (7 \cdot 19) - (13 \cdot 5) = 133 - 65 = 68$
> 
> **Resultados:**
> $x = -102 / -34 = 3$
> $y = 68 / -34 = -2$

> [!ad-example] Ejemplo 2: El peligro de los signos
> **Sistema:**
> $3x - y = 1$
> $2x + 3y = 8$
> 
> * **Atención:** Como la $y$ no tiene número visible, su coeficiente es $-1$.
> * **Cálculo de $\Delta$:** Multiplicamos diagonal principal ($3 \cdot 3 = 9$) y restamos la secundaria ($-1 \cdot 2 = -2$).
> * **Visualización:** $9 - (-2)$. El doble negativo se convierte en suma: $9 + 2 = 11$.
> * **Cálculo de $\Delta x$:** $3 - (-8) = 3 + 8 = 11$.
> 
> **Resultados:** $x = 11/11 = 1$, $y = 22/11 = 2$.

> [!ad-example] Ejemplo 3: Sustitución con Fracciones
> **Sistema:**
> $10x + 18y = -11$
> $16x - 9y = -5$
> 
> 1. Despejamos $x$ en la ec. 1: $x = \frac{-11 - 18y}{10}$.
> 2. Reemplazamos en la ec. 2 usando el **paréntesis grande**: $16(\frac{-11 - 18y}{10}) - 9y = -5$.
> 3. **Eliminar denominador:** Multiplicamos cada término por $10$.
> 4. Al resolver la ecuación lineal resultante: $y = -1/3$.
> 5. Sustituimos para hallar $x$: $x = -1/2$.

> [!ad-example] Ejemplo 4: Aplicación en un Sistema de Puntos
> En un videojuego, ganar un nivel ($x$) otorga puntos y cometer un error ($y$) los resta.
> Si superas **7 niveles** y cometes **4 errores**, terminas con **13 puntos**. Si superas **5 niveles** y cometes **2 errores** (restándolos de nuevo), terminas con **19 puntos**.
> $7x + 4y = 13$
> $5x - 2y = 19$
> Usando los cálculos del Ejemplo 1, vemos que cada nivel superado otorga **3 puntos** ($x=3$) y cada error cometido quita **2 puntos** ($y=-2$).

---

## ✏️ Ejercicios para el Estudiante

> [!ad-abstract] Práctica por niveles
> **Nivel Fácil:**
> $2x + 8y = -2$
> $x - 2y = 5$
> 
> **Nivel Medio:**
> $4x + 5y = 5$
> $-4x - 10y = -7$
> 
> **Nivel Avanzado (¡Cuidado! Requiere ordenar):**
> $4x + 5y = 5$
> $-10y - 4x = -7$
> *Pista: Ordena la segunda ecuación para que la $x$ quede debajo de la $x$.*

> [!ad-success] Soluciones y Simplificación
> * **Fácil:** $x = 2$, $y = -1/2$.
> * **Medio/Avanzado:**
>   - $x = \frac{-15}{-20} \xrightarrow{\text{sacando quinta}} \frac{3}{4}$
>   - $y = \frac{-8}{-20} \xrightarrow{\text{sacando cuarta}} \frac{2}{5}$
> *(Nota: En el avanzado, al ordenar queda $-4x - 10y = -7$, resultando en el mismo sistema del nivel medio).*

---

## ❓ Autoevaluación y Cierre

> [!ad-question] Preguntas de repaso
> **1. En el método de sustitución, ¿qué se recomienda colocar al reemplazar una variable?**
> A) Un signo de división.
> B) Un paréntesis grande para proteger la expresión.
> C) El número 0.
>
> **2. ¿Qué sucede si aplicas Cramer sin haber ordenado las ecuaciones primero?**
> A) Los resultados para $x$ e $y$ estarán intercambiados o serán erróneos.
> B) No sucede nada, el método funciona igual.
> C) La ecuación se resuelve automáticamente.
>
> **3. ¿Cuál es la regla para resolver un determinante de 2x2?**
> A) Sumar todos los números del cuadro.
> B) Multiplicar la diagonal principal y sumarle la secundaria.
> C) Multiplicar la diagonal principal y RESTAR el resultado de la secundaria.

> [!tip] Próximo paso
> Ya sabes resolver sistemas de forma analítica. En la **Clase 04**, aprenderemos a visualizar estas soluciones mediante el **Método Gráfico** y exploraremos el **Método de Igualación**.

---
> [!info] Navegación
> ← [Clase 02 — Sistemas de Ecuaciones: Introducción](link_clase_02) | [Índice General](link_indice) | [Clase 04 — Métodos de Igualación y Gráfico](link_clase_04) →