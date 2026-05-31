# 📖 Guía de estudio — Clase 04: Suma de los primeros números naturales, cuadrados y cubos

> [!info] 📌 Conceptos clave
> *   **El punto de partida ($i=1$):** Para que nuestras fórmulas funcionen como "magia", es obligatorio que la sumatoria comience siempre desde 1. Si tu ejercicio empieza en otro número, ¡no te preocupes!, existen propiedades para ajustarlo, pero la base siempre es el inicio en la unidad.
> *   **La genialidad de Gauss:** Para sumar números naturales, usamos la lógica de los "extremos". Al emparejar el primero con el último, la suma de cada pareja siempre es igual a $n+1$. Como tenemos $n/2$ parejas, la fórmula simplemente multiplica esa suma constante por el número de pares.
> *   **El "Secreto" de los Cubos:** No necesitas memorizar una fórmula compleja para los cubos ($i^3$). Existe una relación asombrosa: el resultado es simplemente la suma de los números naturales ($i$) elevada al cuadrado. ¡Es el cuadrado del resultado simple!
> *   **¿Qué es una constante?:** En el mundo de las sumatorias, una constante es cualquier número real (como $3.2$ o $\sqrt{2}$) o cualquier letra que sea distinta al índice. Por ejemplo, si nuestro índice es $i$, la letra $k$ o $m$ se tratan como constantes.

## Tabla de Fórmulas y Definiciones

> [!important] **Nota Bene:** Todas estas fórmulas solo son válidas si el límite inferior es **$i=1$**.

| Término | Definición / Fórmula |
| :--- | :--- |
| **Suma de una constante ($c$)** | $n \cdot c$ |
| **Suma de números naturales ($i$)** | $\frac{n(n+1)}{2}$ |
| **Suma de cuadrados ($i^2$)** | $\frac{n(n+1)(2n+1)}{6}$ |
| **Suma de cubos ($i^3$)** | $\left[ \frac{n(n+1)}{2} \right]^2$ o $(\text{Suma de } i)^2$ |

---

## Ejemplos Resueltos Adicionales

````ad-example
**Ejemplo A — Suma de los primeros 20 cuadrados**

Calculemos cuánto suman los cuadrados desde el 1 hasta el 20: $\sum_{i=1}^{20} i^2$

1.  **Paso 1: Localizamos nuestro "techo" o límite superior.** Aquí, $n = 20$.
2.  **Paso 2: Aplicamos la mnemotecnia del Profe Alex.** "El número ($20$), por el siguiente ($21$), por la suma de los dos ($20+21=41$)":
    $$\frac{20 \cdot 21 \cdot 41}{6}$$
3.  **Paso 3: Simplificación estratégica.** Como $6 = 2 \cdot 3$, buscamos un múltiplo de 2 y uno de 3 en el numerador para simplificar antes de multiplicar:
    *   **Mitad de 6** es 3; **mitad de 20** es 10.
    *   **Tercera de 3** es 1; **tercera de 21** es 7.
    *   Ahora la operación es mucho más sencilla: $10 \cdot 7 \cdot 41$.
4.  **Resultado final:** $70 \cdot 41 = 2,870$.
````

````ad-example
**Ejemplo B — Ahorro constante en dólares**

Imagina que un estudiante decide ahorrar una cantidad fija de **$3.20 USD** diarios durante **50 días**. ¿Cuál será el total?

1.  **Identificar valores:** Nuestra constante es $c = 3.2$ y el tiempo o límite es $n = 50$.
2.  **Aplicar propiedad de la constante:** La teoría nos dice que solo debemos multiplicar el límite superior por el valor constante ($n \cdot c$).
    $$50 \cdot 3.2$$
3.  **Resultado final:** ✅ El ahorro total será de **$160 USD**.
````

---

## Ejercicios de Repaso por Niveles

````ad-abstract
**🟢 Nivel Fácil**
1. Utiliza la lógica de Gauss para hallar la suma de los primeros 100 números naturales.
2. Determina el valor de la sumatoria de la constante $8$ cuando $n=5$.
3. Comprobación rápida: Aplica la fórmula de naturales para $n=2$ y verifica si coincide con $1+2$.
````

````ad-abstract
**🟡 Nivel Medio**
1. Encuentra la suma de los primeros 10 cubos. *Pista: Recuerda usar la variable $k$ en tu planteamiento ($k^3$).*
2. Si el índice es $i$, calcula la sumatoria de la constante "$k$" hasta un techo de $n=20$.
3. Aplica la fórmula de cuadrados para hallar la suma de los primeros 50 cuadrados. *¡No olvides simplificar el 6 antes de multiplicar!*
````

````ad-abstract
**🔴 Nivel Avanzado — Aplicación con $USD**
1. **Fondo de Inversión:** Un activo duplica el valor de los cuadrados de cada día. Calcula el valor acumulado de los primeros 5 días: $\sum_{i=1}^{5} 2 \cdot i^2$.
2. **El Reto del Ahorro:** ¿Qué cantidad de dinero es mayor al final del periodo?
    *   Opción A: El ahorro total de los primeros 20 cubos en dólares.
    *   Opción B: El ahorro total de los primeros 50 cuadrados en dólares.
    *   *Pista: Compara $210^2$ frente a la simplificación de $50, 51, 101$ entre $6$.*
````

---

> [!tip] 💡 Consejo de estudio
> Para evitar errores manuales y ahorrar tiempo, adopta siempre el hábito de **simplificar antes de multiplicar**. En la fórmula de cuadrados, el denominador $6$ (que es $2 \times 3$) siempre encontrará "pareja" en el numerador para simplificarse totalmente. Además, recuerda que los cubos son "hijos" de los naturales: si ya calculaste la suma simple, solo elévala al cuadrado y habrás terminado. ¡Así de fácil!