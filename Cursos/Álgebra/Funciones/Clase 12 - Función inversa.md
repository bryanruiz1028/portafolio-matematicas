# Clase 12 — Función inversa

#algebra #funcininversa

> [!info] 🧭 Navegación
> [[Clase 11 — Composición de funciones]] | [[Clase 13 — Funciones Logarítmicas]]

---

¿Qué tal amigas y amigos? Espero que estén muy bien. En esta clase vamos a aprender a encontrar la función inversa de una función. Este es un tema fascinante porque nos permite "deshacer" procesos matemáticos, algo que es extremadamente útil tanto en la vida diaria como en la ingeniería.

### ¿Por qué es importante esta clase?

Imagina que tienes una empresa de camisetas y cada una cuesta $10 USD. Tu función de ingresos sería $f(x) = 10x$, donde $x$ es el número de camisetas. Pero, ¿qué pasa si al final del día revisas la caja y tienes $70 USD? Para saber cuántas camisetas vendiste, necesitas un proceso que haga el camino de regreso.

La **función inversa** es esa herramienta que permite revertir un proceso para recuperar el valor inicial.

**Aplicaciones específicas:**
* 💵 **$USD:** Determinar cuántas unidades se vendieron conociendo el ingreso total (Precio vs. Cantidad).
* 🏗️ **Ingeniería:** Revertir procesos de cálculo de resistencia para ajustar el diseño original.
* 📊 **Ciencia:** Convertir resultados finales (como una temperatura registrada) de vuelta a su variable de origen (como la energía aplicada).

---

### Concepto clave

Para un estudiante de secundaria, la función inversa es como una **"máquina que hace el camino de regreso"**. Si la función $f$ toma a $x$ y lo convierte en $y$, la función inversa $f^{-1}$ toma a $y$ y lo devuelve exactamente a $x$.

*   **El truco del espejo:** Si graficamos una función y su inversa, verás que son simétricas respecto a la recta $y = x$. Es como si esa diagonal fuera un espejo.
*   **¡Cuidado! Error común:** No todas las funciones tienen inversa. Para que exista, la función debe ser **inyectiva** (uno a uno). Además, recuerda que $f^{-1}(x)$ es solo una notación, **no** significa que debas elevar a la potencia $-1$ o calcular el recíproco $\frac{1}{f(x)}$.

---

### Procedimiento paso a paso

Para hallar la inversa, te recomiendo seguir siempre este algoritmo de 4 pasos que nunca falla:

```text
1. Verificar inyectividad: Comprobar que f(x₁) = f(x₂) implica que x₁ = x₂.
2. Intercambiar variables: Cambiar cada "y" por "x", y cada "x" por "y".
3. Despejar la nueva variable "y": Realizar las operaciones para dejar la "y" sola.
4. Renombrar el resultado: Llamar a la nueva expresión f⁻¹(x).
```

---

### Ejemplos Prácticos

> [!example] Ejemplo 1: Función Lineal (Básico)
> Vamos a encontrar la función inversa de $f(x) = 2x + 3$. Verás que es la más sencilla.
> 
> **Paso 1: Verificar inyectividad**
> $2x_1 + 3 = 2x_2 + 3$
> $2x_1 = 2x_2$
> $x_1 = x_2$ (¡Es inyectiva!)
> 
> **Paso 2: Intercambiar variables**
> Escribimos la función como $y = 2x + 3$ y cambiamos: $x = 2y + 3$
> 
> **Paso 3: Despejar $y$**
> $x - 3 = 2y$
> $\frac{x - 3}{2} = y$
> 
> **Paso 4: Renombrar**
> $f^{-1}(x) = \frac{x - 3}{2}$
> 
> **✨ El truco del Profe Alex (Verificación):**
> Probemos con un número. Si en la función original $f(x)$ usamos $x = 5$:
> $f(5) = 2(5) + 3 = 13$
> Ahora, si metemos ese $13$ en nuestra inversa $f^{-1}(x)$:
> $f^{-1}(13) = \frac{13 - 3}{2} = \frac{10}{2} = 5$
> ¡Magia! Volvimos al número original.

> [!example] Ejemplo 2: Función Racional (Con productos cruzados)
> Hallar la inversa de $f(x) = \frac{3x - 2}{x + 3}$. Aquí debemos tener cuidado con el álgebra.
> 
> **Paso 1: Verificar inyectividad**
> $\frac{3x_1 - 2}{x_1 + 3} = \frac{3x_2 - 2}{x_2 + 3}$
> Aplicamos productos cruzados: $(3x_1 - 2)(x_2 + 3) = (3x_2 - 2)(x_1 + 3)$
> $3x_1x_2 + 9x_1 - 2x_2 - 6 = 3x_1x_2 + 9x_2 - 2x_1 - 6$
> Eliminamos términos iguales: $9x_1 - 2x_2 = 9x_2 - 2x_1$
> Agrupamos: $11x_1 = 11x_2 \implies x_1 = x_2$. (Es inyectiva).
> 
> **Paso 2: Intercambio**
> $x = \frac{3y - 2}{y + 3}$
> 
> **Paso 3: Despejar $y$**
> $x(y + 3) = 3y - 2$
> $xy + 3x = 3y - 2$
> Pasamos todo lo que tiene $y$ a un lado: $xy - 3y = -3x - 2$
> **Factor común:** Sacamos la $y$ para que quede una sola: $y(x - 3) = -3x - 2$
> $y = \frac{-3x - 2}{x - 3}$
> 
> **Paso 4: Resultado**
> $f^{-1}(x) = \frac{-3x - 2}{x - 3}$

> [!example] Ejemplo 3: Función Cúbica (Avanzado)
> Hallar la inversa de $f(x) = x^3 + 2$.
> 
> **Paso 1: Verificar inyectividad**
> $x_1^3 + 2 = x_2^3 + 2 \implies x_1^3 = x_2^3 \implies x_1 = x_2$.
> 
> **Paso 2: Intercambio**
> $x = y^3 + 2$
> 
> **Paso 3: Despejar $y$**
> $x - 2 = y^3$
> Aplicamos raíz cúbica a ambos lados: $\sqrt[3]{x - 2} = y$
> 
> **Paso 4: Resultado**
> $f^{-1}(x) = \sqrt[3]{x - 2}$

> [!example] Ejemplo 4: Aplicación Inversión ($USD)
> Una aplicación calcula la ganancia de una inversión con $f(x) = \sqrt{2x - 6}$, donde $x$ son dólares invertidos. Halla la función para recuperar el dato de la inversión.
> 
> **Paso 1: Verificar inyectividad**
> $\sqrt{2x_1 - 6} = \sqrt{2x_2 - 6} \implies 2x_1 - 6 = 2x_2 - 6 \implies x_1 = x_2$.
> 
> **Paso 2: Intercambio**
> $x = \sqrt{2y - 6}$
> 
> **Paso 3: Despejar $y$**
> Elevamos al cuadrado: $x^2 = 2y - 6$
> $x^2 + 6 = 2y$
> $\frac{x^2 + 6}{2} = y$
> 
> **Paso 4: Resultado**
> $f^{-1}(x) = \frac{x^2 + 6}{2}$

---

### Ejercicios para el estudiante

**🟢 Nivel Fácil (Lineales)**
1. $f(x) = 5x - 3$
2. $g(x) = 2x + 8$
3. $h(x) = \frac{x}{4} + 1$
4. $f(x) = -3x + 2$

**🟡 Nivel Medio (Racionales)**
5. $f(x) = \frac{5x}{x - 4}$
6. $g(x) = \frac{2x + 1}{x - 1}$
7. $h(x) = \frac{x + 2}{x - 2}$
8. $f(x) = \frac{3x}{2x + 5}$

**🔴 Nivel Avanzado (Raíces y Contexto $USD)**
9. $f(x) = \sqrt{x + 5}$
10. $g(x) = \sqrt{3x - 9}$
11. Un sistema define el costo en dólares como $C = \sqrt[3]{x + 1}$. Halla la función para determinar las unidades $x$ a partir del costo $C$.
12. En una tienda de calzado, la relación de ingresos es $I = \frac{4x - 1}{x + 2}$. Encuentra la función inversa para hallar las unidades $x$ vendidas.

> [!success] Soluciones para el docente
> 1. $f^{-1}(x) = \frac{x + 3}{5}$ | 2. $g^{-1}(x) = \frac{x - 8}{2}$ | 3. $h^{-1}(x) = 4x - 4$ | 4. $f^{-1}(x) = \frac{2 - x}{3}$
> 5. $f^{-1}(x) = \frac{4x}{x - 5}$ | 6. $g^{-1}(x) = \frac{x + 1}{x - 2}$ | 7. $h^{-1}(x) = \frac{2x + 2}{x - 1}$ | 8. $f^{-1}(x) = \frac{5x}{3 - 2x}$
> 9. $f^{-1}(x) = x^2 - 5$ | 10. $g^{-1}(x) = \frac{x^2 + 9}{3}$ | 11. $f^{-1}(C) = C^3 - 1$ | 12. $f^{-1}(I) = \frac{2I + 1}{4 - I}$

---

### Mini-prueba de autoevaluación

1.  **Conceptual:** ¿Por qué es obligatorio que una función sea inyectiva para tener inversa?
2.  **Procedimental:** Halla la inversa de $f(x) = \frac{x}{x + 2}$.
3.  **Aplicación:** Si el precio de las camisetas es $P(x) = 10x$, ¿cuál es su inversa? Si el ingreso fue de $70 USD, ¿cuántas camisetas se vendieron usando dicha inversa?

---

### Cierre y Notas

Amigas y amigos, recuerden que si una función no es inyectiva en todo su dominio (como la parábola $f(x) = x^2$), no todo está perdido. Podemos **restringir el dominio**. Por ejemplo, si solo tomamos los valores positivos ($x \geq 0$), la función se vuelve inyectiva y ¡listo!, ya podemos encontrar su inversa. ¡Sigan practicando y nos vemos en la próxima clase!

> [!info] 🧭 Navegación
> [[Clase 11 — Composición de funciones]] | [[Clase 13 — Funciones Logarítmicas]]