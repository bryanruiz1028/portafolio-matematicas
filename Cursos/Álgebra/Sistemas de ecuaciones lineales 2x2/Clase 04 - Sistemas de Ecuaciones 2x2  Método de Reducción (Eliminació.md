# Clase 04 — Sistemas de Ecuaciones 2x2 | Método de Reducción (Eliminación)

#Álgebra #Sistemas2x2 #Matemáticas #MétodoReducción

> [!info] 🧭 Navegación
> ⬅️ [[Clase 03]] | 🏠 [[00 - Índice del curso]] | ➡️ [[Clase 05]]

---

### 1. Relevancia y Aplicaciones

El método de **reducción** (también llamado de eliminación) es, para muchos, el más eficiente y elegante del álgebra. Su poder reside en la capacidad de "anular" una incógnita mediante operaciones aritméticas básicas, transformando un problema complejo en una ecuación de primer grado que ya sabes resolver.

> [!info] 🌍 Relevancia y aplicaciones
> Este método es fundamental porque permite modelar situaciones de equilibrio donde dos fuerzas o valores interactúan:
> * 💵 **$USD:** Calcular el precio unitario de artículos cuando solo conoces el costo de paquetes combinados (combos).
> * 🏗️ **Práctica:** En ingeniería, se usa para determinar el equilibrio de fuerzas en estructuras simples.
> * 📊 **Cotidiana:** Distribuir recursos o tareas de forma equitativa entre dos grupos con diferentes capacidades.

---

### 2. Concepto Clave y Errores Comunes

> [!note] 📌 ¿Qué es el Método de Reducción?
> Consiste en preparar las ecuaciones para que una de las variables ($x$ o $y$) tenga el mismo coeficiente pero con **signo opuesto** en ambas líneas. Al sumar las ecuaciones verticalmente, esa variable se elimina (suma cero), dejándonos una sola ecuación con una sola incógnita.

> [!warning] ⚠️ Error común
> El error más crítico es **no multiplicar todos los términos de la ecuación**. Muchos estudiantes multiplican los términos de la izquierda pero olvidan multiplicar el número tras el signo igual ($=$). ¡Recuerda que una ecuación es una balanza; si solo alteras un lado, pierdes el equilibrio!

> [!tip] 💡 Truco para recordarlo
> Busca "el opuesto". Si en la primera ecuación tienes $+5y$, tu meta es que en la segunda aparezca $-5y$. El éxito del método depende de crear estos "rivales" matemáticos que se anulen entre sí.

---

### 3. Procedimiento Paso a Paso

Sigue esta secuencia lógica para no perderte en el proceso:

```text
1. ORDENAR: Alinear las variables en ambas ecuaciones (x, y = número).
2. MULTIPLICAR: Ajustar una o ambas ecuaciones para obtener coeficientes opuestos.
   (Usa el MCM para evitar números excesivamente grandes).
3. SUMAR: Sumar verticalmente para eliminar la variable elegida.
4. RESOLVER Y REEMPLAZAR: Hallar la primera variable. 
   Pila: Si la división no es exacta, simplifica la fracción (Regla del Profe Alex).
5. SUSTITUIR: Usar ese valor en una ecuación original para hallar la segunda variable.
```

---

### 4. Bloques de Ejemplos (Casos de Estudio)

````ad-example
**Ejemplo 1: El camino de menor resistencia (Video 1)**
Sistema:
(1) $2x + y = 8$
(2) $x - 4y = -5$

*   **Estrategia:** Observamos que $y$ ya tiene signos opuestos ($+$ y $-$). Es más fácil multiplicar la ecuación (1) por $4$ para obtener $+4y$.
*   **Paso 1 (Multiplicar):**
    $4 \cdot (2x + y = 8) \Rightarrow 8x + 4y = 32$
*   **Paso 2 (Sumar verticalmente):**
    $\begin{aligned} 8x + 4y &= 32 \\ x - 4y &= -5 \end{aligned}$
    $\overline{\quad 9x + 0 \quad = 27 \quad}$
*   **Paso 3 (Resolver):** $x = \frac{27}{9} \Rightarrow \mathbf{x = 3}$.
*   **Paso 4 (Sustituir):** En la ec. (1): $2(3) + y = 8 \Rightarrow 6 + y = 8 \Rightarrow \mathbf{y = 2}$.
*   **Resultado:** El punto de intersección es $(3, 2)$.
````

````ad-example
**Ejemplo 2: Uso del MCM y el truco del $-1$ (Video 2)**
Sistema:
(1) $6x - 5y = -9$
(2) $4x + 3y = 13$

*   **Estrategia:** Eliminaremos $x$. El **Mínimo Común Múltiplo (MCM)** de $6$ y $4$ es **$12$**. Esto es mejor que usar $24$ porque trabajamos con números más pequeños.
*   **Paso 1 (Multiplicar):** Multiplicamos (1) por $2$ ($\rightarrow 12x$) y (2) por $-3$ ($\rightarrow -12x$).
    (1) $12x - 10y = -18$
    (2) $-12x - 9y = -39$
*   **Paso 2 (Sumar):**
    $\begin{aligned} 12x - 10y &= -18 \\ -12x - 9y &= -39 \end{aligned}$
    $\overline{\quad 0 - 19y \quad = -57 \quad}$
*   **Paso 3 (Resolver):** Como tenemos $-19y = -57$, el **Profe Alex recomienda** multiplicar por $-1$ para evitar errores con signos al dividir:
    $19y = 57 \Rightarrow y = \frac{57}{19} \Rightarrow \mathbf{y = 3}$.
*   **Paso 4 (Sustituir):** En ec. (2): $4x + 3(3) = 13 \Rightarrow 4x + 9 = 13 \Rightarrow 4x = 4 \Rightarrow \mathbf{x = 1}$.
*   **Resultado:** $(1, 3)$.
````

````ad-example
**Ejemplo 3: Ordenamiento y Estrategia de Primos (Video 3)**
Sistema:
(1) $3x - 4y + 23 = 0$
(2) $6y + 11x = 19$

*   **Paso 1 (Ordenar):** Pasamos términos independientes al lado derecho y alineamos $x$ e $y$.
    (1) $3x - 4y = -23$
    (2) $11x + 6y = 19$
*   **Estrategia:** El Profe Alex sugiere eliminar la variable cuyos coeficientes no sean ambos números primos para evitar cálculos gigantes. Aquí eliminaremos $y$ (MCM de $4$ y $6$ es $12$).
*   **Paso 2 (Multiplicar):** (1) por $3$ y (2) por $2$.
    (1) $9x - 12y = -69$
    (2) $22x + 12y = 38$
*   **Paso 3 (Sumar):**
    $\begin{aligned} 9x - 12y &= -69 \\ 22x + 12y &= 38 \end{aligned}$
    $\overline{\quad 31x + 0 \quad = -31 \quad}$
*   **Paso 4 (Resolver):** $x = \frac{-31}{31} \Rightarrow \mathbf{x = -1}$.
*   **Paso 5 (Sustituir):** En ec. (2): $6y + 11(-1) = 19 \Rightarrow 6y - 11 = 19 \Rightarrow 6y = 30 \Rightarrow \mathbf{y = 5}$.
*   **Resultado:** $(-1, 5)$.
````

````ad-example
**Ejemplo 4: Aplicación Económica ($USD)**
En una cafetería, $2$ hamburguesas ($h$) y $1$ soda ($s$) cuestan $\$13$. Si compras $1$ hamburguesa y $2$ sodas, pagas $\$11$. ¿Precio de cada uno?

*   **Sistema:**
    (1) $2h + s = 13$
    (2) $h + 2s = 11$
*   **Reducción:** Multiplicamos (2) por $-2$ para eliminar $h$.
    (1) $2h + s = 13$
    (2) $-2h - 4s = -22$
*   **Suma:**
    $\begin{aligned} 2h + s &= 13 \\ -2h - 4s &= -22 \end{aligned}$
    $\overline{\quad 0 - 3s \quad = -9 \quad}$
*   **Resultado:** $-3s = -9 \Rightarrow s = 3$ (Soda: $\$3$). Reemplazando: $2h + 3 = 13 \Rightarrow \mathbf{h = 5}$ (Hamburguesa: $\$5$).
````

---

### 5. Ejercicios para el Estudiante

````ad-abstract
**🟢 Nivel Fácil**
Resuelve los siguientes sistemas (Recuerda: si no es exacta, simplifica la fracción):
1) $x + y = 5$
   $x - y = 1$
2) $2x + 3y = 7$
   $x - 3y = 2$
````

````ad-abstract
**🟡 Nivel Medio**
Ordena primero y luego aplica reducción:
3) $5x = 10 + 2y$
   $3x + 4y = 32$
4) $2x + y = 4$
   $3x - 2y = -1$
````

````ad-abstract
**🔴 Nivel Avanzado (Aplicación)**
5) En el cine, $3$ entradas de adulto y $2$ de niño cuestan $\$42$. Si $2$ de adulto y $3$ de niño cuestan $\$38$, ¿cuál es el precio de cada una?
````

---

### 6. Solucionario para el Docente

````ad-success
**Respuestas de la Práctica:**
1. $x=3, y=2$
2. $x=3, y=1/3$ (Nota pedagógica: Aquí la división no es exacta, se deja como fracción).
3. $x=4, y=5$
4. $x=1, y=2$
5. Adulto = $\$10, Niño = $\$6
````

---

### 7. Autoevaluación

> [!question] Pregunta 1
> ¿Por qué es preferible usar el MCM (Mínimo Común Múltiplo) en lugar de simplemente multiplicar los coeficientes entre sí?
> A) Porque los signos cambian automáticamente.
> B) Porque evita trabajar con números innecesariamente grandes.
> C) Porque solo así se puede eliminar la variable $x$.
> D) No es preferible, siempre es mejor multiplicar los coeficientes entre sí.

> [!question] Pregunta 2
> ¿Qué sucede si al sumar las dos ecuaciones ambas variables ($x$ e $y$) se eliminan y queda $0 = 0$?
> A) Cometiste un error de multiplicación.
> B) El sistema tiene infinitas soluciones.
> C) El sistema no tiene solución.
> D) Debes multiplicar por $-1$ y volver a empezar.

> [!question] Pregunta 3
> Si tienes el término $3x$ en la primera ecuación y $-x$ en la segunda, ¿por qué número debes multiplicar la segunda ecuación para eliminar la $x$?
> A) Por $1$
> B) Por $-3$
> C) Por $3$
> D) Por $0$

---

### 8. Cierre y Próximo Tema

¡Excelente trabajo! Has aprendido a dominar el método de reducción. Recuerda que la clave del éxito en álgebra es el orden y la constancia: **la práctica hace al maestro**. No te desanimes si un signo te juega una mala pasada al principio, ¡es parte del aprendizaje!

> [!tip] 💡 En la próxima clase
> Veremos el **Método de Sustitución**, una técnica ideal para cuando una de las variables ya está despejada o es fácil de aislar. ¡Prepárate para seguir sumando conocimientos!

> [!info] 🧭 Navegación
> ⬅️ [[Clase 03]] | 🏠 [[00 - Índice del curso]] | ➡️ [[Clase 05]]