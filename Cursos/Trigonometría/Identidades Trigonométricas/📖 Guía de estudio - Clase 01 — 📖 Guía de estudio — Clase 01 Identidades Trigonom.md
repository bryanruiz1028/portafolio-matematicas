# 📖 Guía de estudio — Clase 01: Identidades Trigonométricas

1. **📌 Conceptos clave**

> [!info] **Fundamentos de las Identidades**
> * **Ecuación vs. Identidad:** Según el Profe Alex, **resolver una ecuación** es "encontrar el valor de la variable para que esta igualdad sea verdadera". Una ecuación solo se cumple para algunos valores (ej. $x + 3 = 5$ solo si $x = 2$). En cambio, una **identidad** es una igualdad que es válida para **TODOS** los valores que se le asignen a la variable.
> * **La Regla del "Mismo Ángulo":** Para que una identidad sea válida, los ángulos deben ser idénticos en toda la expresión. Como dice el autor: "si aquí dice alfa, aquí tiene que decir alfa". No podemos aplicar estas reglas si los ángulos son diferentes (ej. $\sin^2(30^\circ) + \cos^2(40^\circ)$ no es igual a 1).
> * **Circunferencia Unitaria:** Es una circunferencia de radio = 1. Al trazar un triángulo dentro de ella, la **hipotenusa mide exactamente 1**. Aquí, el seno es la medida de la línea vertical y el coseno es la medida de la línea horizontal.
> * **Orden sugerido:** Para dominar el tema, memoriza las funciones en este orden: **1. Seno, 2. Coseno, 3. Tangente, 4. Cotangente, 5. Secante y 6. Cosecante**.

2. **Fórmulas y definiciones importantes**

En esta guía utilizaremos el símbolo $\theta$ (theta) para representar el ángulo, pero recuerda que puede usarse cualquier letra ($\alpha, \beta, A, x$); lo importante es que sea la misma en toda la fórmula.

| Término | Definición / Fórmula |
| :--- | :--- |
| **Identidades Recíprocas** | $\sin(\theta) = 1 / \csc(\theta)$ <br> $\cos(\theta) = 1 / \sec(\theta)$ <br> $\tan(\theta) = 1 / \cot(\theta)$ <br> $\cot(\theta) = 1 / \tan(\theta)$ <br> $\sec(\theta) = 1 / \cos(\theta)$ <br> $\csc(\theta) = 1 / \sin(\theta)$ |
| **Identidades de Cociente** | $\tan(\theta) = \sin(\theta) / \cos(\theta)$ <br> $\cot(\theta) = \cos(\theta) / \sin(\theta)$ <br> *(Útiles para calcular funciones que no están en la calculadora)* |
| **Identidad Pitagórica Fundamental** | $\sin^2(\theta) + \cos^2(\theta) = 1$  <br> *(También se puede escribir como $1 = \sin^2(\theta) + \cos^2(\theta)$)* |
| **Sub-identidades (Despejes)** | $\sin^2(\theta) = 1 - \cos^2(\theta)$ <br> $\cos^2(\theta) = 1 - \sin^2(\theta)$ |
| **Identidades Secundarias** | $\csc^2(\theta) = 1 + \cot^2(\theta)$ <br> $\sec^2(\theta) = \tan^2(\theta) + 1$ <br> *(Se obtienen dividiendo la fundamental por $\sin^2$ o $\cos^2$)* |

3. **Ejemplos resueltos adicionales**

````ad-example
**Ejemplo A: Demostración de la Tangente**
¿Por qué $\tan(\theta) = \sin(\theta) / \cos(\theta)$? Usando las definiciones de razones trigonométricas:
1. Sustituimos: $\sin(\theta) = \frac{CO}{H}$ y $\cos(\theta) = \frac{CA}{H}$ (donde CO es Cateto Opuesto, CA es Cateto Adyacente y H es Hipotenusa).
2. Formamos la fracción: $\frac{\frac{CO}{H}}{\frac{CA}{H}}$.
3. Aplicamos la ley de **extremos y medios** (multiplicar los de afuera y los de adentro): $\frac{CO \cdot H}{CA \cdot H}$.
4. Al simplificar la Hipotenusa ($H$), nos queda $\frac{CO}{CA}$.
5. Por definición, $\frac{CO}{CA}$ es la Tangente. ¡Queda demostrado!
````

````ad-example
**Ejemplo B: Cálculo de Cotangente con calculadora**
Como la calculadora no tiene tecla de cotangente, para hallar la **Cotangente de 40°**:
1. **Paso vital:** Revisa que tu calculadora esté en modo grados (busca la letra **"D"** o **"Deg"** en la pantalla).
2. Usa la identidad de cociente: $\cot(40^\circ) = \frac{\cos(40^\circ)}{\sin(40^\circ)}$.
3. Al realizar la división: $\frac{0.766}{0.642} \approx 1.19$.
Resultado: $\cot(40^\circ) = 1.19$.
````

4. **Ejercicios de repaso**

````ad-abstract
**🟢 Nivel Fácil**
Escribe la expresión recíproca para las siguientes funciones (asumiendo el ángulo $\theta$):
1. $\cos(\theta) = $
2. $\tan(\theta) = $
3. $\csc(\theta) = $
````

````ad-abstract
**🟡 Nivel Medio**
Verifica la Identidad Pitagórica Fundamental usando un ángulo de $30^\circ$:
*   **Paso 1:** Asegúrate de que tu calculadora muestre la **"D"** (Deg).
*   **Paso 2:** Calcula $(\sin 30^\circ)^2$ y $(\cos 30^\circ)^2$.
*   **Paso 3:** Suma ambos resultados. ¿Obtuviste exactamente **1**?
*   *Nota:* Recuerda que en la circunferencia unitaria esto viene de aplicar el Teorema de Pitágoras: $cateto^2 + cateto^2 = hipotenusa^2$, donde $1^2 = 1$.
````

````ad-abstract
**🔴 Nivel Avanzado**
Demuestra analíticamente que $\cot(\theta) = \cos(\theta) / \sin(\theta)$.
Para resolverlo, sustituye $\cos(\theta)$ por $\frac{CA}{H}$ y $\sin(\theta)$ por $\frac{CO}{H}$. Utiliza el método de **Extremos y Medios** para simplificar la expresión y llegar a la razón de la cotangente ($\frac{CA}{CO}$).
````

5. **💡 Consejo de estudio**

> [!tip] **Parejas Recíprocas por Extremos**
> Si escribes las funciones en orden vertical (Seno, Coseno, Tangente, Cotangente, Secante, Cosecante), las recíprocas se encuentran uniendo los extremos:
> *   La 1ª con la 6ª (**Seno** y **Cosecante**).
> *   La 2ª con la 5ª (**Coseno** y **Secante**).
> *   La 3ª con la 4ª (**Tangente** y **Cotangente**).