# 📖 Guía de estudio — Clase 02: Resta de Números Binarios

¡Hola, futuros genios de la informática! Bienvenidos a una nueva clase. Hoy vamos a dominar la resta binaria. Aunque al principio parezca un reto, verán que es incluso más sencilla que la resta decimal que aprendieron en la escuela. ¡No se rindan, el préstamo binario es un truco que dominarán en un abrir y cerrar de ojos!

> [!info] 📌 Conceptos clave
> 1. **Simplicidad ante todo:** Como solo usamos ceros (0) y unos (1), las combinaciones posibles son muy pocas. ¡Es matemáticas en su forma más pura!
> 2. **¿Quién es el más grande?:** Antes de restar, identifica el número mayor (Minuendo). Primero, cuenta las cifras: el que tenga más, es el mayor. Si tienen las mismas, compara de izquierda a derecha hasta encontrar el primer dígito diferente.
> 3. **La regla del "préstamo" (Borrow):** Al igual que en el sistema decimal, si no nos alcanza para restar (como en $0 - 1$), le pedimos a la columna de la izquierda.
> 4. **El valor del préstamo:** ¡Aquí está el secreto! En binario, cuando pides prestado, recibes **2** (en decimal pedías 10). Así que simplemente haces $2 - 1 = 1$. ¡Facilísimo!

---

## 2. Fórmulas y Definiciones Importantes

Asegúrate de tener esta tabla a la mano. Es tu "mapa del tesoro" para resolver cualquier ejercicio.

| Término | Definición / Fórmula |
| :--- | :--- |
| **Regla básica 1** | $1 - 0 = 1$ |
| **Regla básica 2** | $1 - 1 = 0$ |
| **Regla básica 3** | $0 - 0 = 0$ |
| **Regla básica 4** | $0 - 1 = 1$ (y pide prestado $1$ a la izquierda) |
| **Préstamo Binario** | Cuando una columna pide prestado, el $1$ de la izquierda se convierte en $0$ y la columna actual recibe un valor de $2_2$. |
| **Comprobación** | Es la estrategia para estar 100% seguros: convierte tus números binarios a decimal, resta y verifica que el resultado coincida. |

---

## 3. Ejemplos Resueltos Adicionales

¡Vamos a ver la teoría en acción! Presta mucha atención a cómo se mueven los préstamos.

> [!example] Ejemplo A: Caso Básico con Préstamo
> **Problema:** Restar $1010_2 - 0101_2$
> 
> Analicemos columna por columna de derecha a izquierda:
> ```text
>        (0) (2) (0) (2)  <-- Valores tras préstamos
>         1   0   1   0_2 (Minuendo: 10)
>      -  0   1   0   1_2 (Sustraendo: 5)
>      ------------------
>         0   1   0   1_2 (Resultado: 5)
> ```
> **Paso a paso:**
> 1. **Columna 1:** $0 - 1$. No alcanza. Pedimos al de al lado. El $1$ de la izquierda se vuelve $0$ y nosotros recibimos $2$. Ahora: $2 - 1 = \mathbf{1}$.
> 2. **Columna 2:** Teníamos un $1$, pero como prestó, ahora es $0$. Entonces: $0 - 0 = \mathbf{0}$.
> 3. **Columna 3:** $0 - 1$. ¡Otra vez pedimos prestado! El $1$ de la izquierda se vuelve $0$ y recibimos $2$. Ahora: $2 - 1 = \mathbf{1}$.
> 4. **Columna 4:** Como prestó su único $1$, quedó en $0$. Entonces: $0 - 0 = \mathbf{0}$.

> [!example] Ejemplo B: Aplicación Real $USD
> **Escenario:** Imagina que tienes un presupuesto de **$1101_2$** dólares (13 USD) y gastas **$0101_2$** dólares (5 USD) en un videojuego. ¿Cuál es tu saldo?
> 
> ```text
>         1 1 0 1_2  (Tienes 13)
>      -  0 1 0 1_2  (Gastas 5)
>      ------------
>         1 0 0 0_2  (Te quedan 8)
> ```
> **Proceso:**
> *   **Col. 1:** $1 - 1 = 0$
> *   **Col. 2:** $0 - 0 = 0$
> *   **Col. 3:** $1 - 1 = 0$
> *   **Col. 4:** $1 - 0 = 1$
> **Resultado:** Tu saldo final es de **$1000_2$** dólares. ¡Excelente administración!

---

## 4. Ejercicios de Repaso

¡Llegó tu turno! Toma papel y lápiz. Recuerda: la práctica hace al maestro.

> [!todo] 🟢 Nivel: Fácil (Sin préstamos complejos)
> Resuelve estas restas directas para calentar motores:
> 1. $111_2 - 101_2$
> 2. $110_2 - 010_2$
> 3. $101_2 - 001_2$

> [!todo] 🟡 Nivel: Medio (Con préstamos simples)
> Pon a prueba tu habilidad de pedir prestado:
> 1. $1010_2 - 0011_2$
> 2. $1100_2 - 0101_2$
> 3. $1011_2 - 0111_2$

> [!todo] 🔴 Nivel: Avanzado (Aplicación USD y préstamos sucesivos)
> Resuelve estos retos de razonamiento matemático:
> 1. Un cliente paga con un billete de **$1000_2$** dólares por una gorra que cuesta **$0111_2$** dólares. ¿Cuánto cambio recibe?
> 2. Tienes **$10000_2$** dólares y compras herramientas por **$1001_2$** dólares. ¿Cuánto te sobra?
> 
> > [!tip] 💡 Pista para el Nivel Avanzado
> > Cuando restas algo como $1000_2$, el préstamo debe viajar por varios ceros. El primer $1$ se vuelve $0$, los ceros del medio se convierten en **$1$** y el último cero (donde necesitas restar) recibe el **$2$**. ¡Es igual que el ejemplo de $1000 - 735$ que vimos en clase decimal!

---

## 5. Consejo de Estudio

> [!tip] 💡 La Estrategia del "Profe Alex"
> Para irte a dormir sin dudas, aplica siempre la **Conversión y Comparación**:
> 1. Al terminar tu resta binaria, convierte el minuendo y el sustraendo a decimal.
> 2. Haz la resta en decimal (la que ya conoces de memoria).
> 3. Convierte tu resultado binario a decimal.
> **¡Si los números coinciden, celebralo porque tu ejercicio está perfecto!** 🚀