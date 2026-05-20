# 📖 Guía de estudio — Clase 03: Conversión de la ecuación canónica a la ecuación general de la hipérbola

> [!info] 📌 Conceptos clave
> Para transformar una ecuación de su forma canónica (u ordinaria) a la general, es fundamental dominar estos puntos:
> * **Forma General:** La ecuación debe quedar igualada a cero y seguir el orden: $Ax^2 + By^2 + Cx + Dy + E = 0$.
> * **Signos de los coeficientes:** En una hipérbola, los coeficientes de $x^2$ ($A$) y $y^2$ ($B$) deben tener obligatoriamente **signos diferentes**.
> * **Regla de las 3 partes:** Si el centro de la hipérbola está en $(0,0)$, la ecuación general solo tendrá tres términos: $x^2$, $y^2$ y el término independiente (no aparecerán $Cx$ ni $Dy$).
> * **Método de la "Carita Feliz":** Técnica de multiplicación cruzada para resolver la resta de fracciones: se multiplican los denominadores entre sí y luego se multiplica en cruz para obtener el nuevo numerador.
> * **Eliminación de denominadores:** El denominador común resultante se pasa al otro lado de la igualdad multiplicando al número 1 para simplificar la expresión.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ecuación General de la Hipérbola** | $Ax^2 + By^2 + Cx + Dy + E = 0$ |
| **Método de la Carita Feliz** | Proceso para restar $\frac{a}{b} - \frac{c}{d}$ haciendo $\frac{(a \cdot d) - (b \cdot c)}{b \cdot d}$ |
| **Cuadrado de un binomio (Suma)** | $(a + b)^2 = a^2 + 2ab + b^2$ |
| **Cuadrado de un binomio (Resta)** | $(a - b)^2 = a^2 - 2ab + b^2$ |

## Ejemplos resueltos adicionales

> [!example] Ejemplo A — Centro en (0,0)
> **Problema:** Convertir $\frac{x^2}{4} - \frac{y^2}{9} = 1$ a su forma general.
> 
> **Proceso paso a paso:**
> 1. **Resta de fracciones:** Aplicamos el método de la carita feliz. Multiplicamos denominadores ($4 \cdot 9 = 36$) y cruzamos:
>    $$\frac{9x^2 - 4y^2}{36} = 1$$
> 2. **Eliminación del denominador:** Pasamos el $36$ que está dividiendo a multiplicar al otro lado:
>    $$9x^2 - 4y^2 = 1 \cdot 36 \implies 9x^2 - 4y^2 = 36$$
> 3. **Trasposición de términos:** Igualamos a cero pasando el $36$ con signo negativo:
>    $$9x^2 - 4y^2 - 36 = 0$$
> 
> **Resultado:** $9x^2 - 4y^2 - 36 = 0$

> [!example] Ejemplo B — Centro en (h,k)
> **Problema:** Convertir $\frac{(x-2)^2}{5} - \frac{(y+4)^2}{10} = 1$ a su forma general.
> 
> **Proceso paso a paso:**
> 1. **Resta de fracciones:** Multiplicamos denominadores ($5 \cdot 10 = 50$) y aplicamos productos cruzados:
>    $$\frac{10(x-2)^2 - 5(y+4)^2}{50} = 1$$
> 2. **Simplificación y expansión:** Pasamos el $50$ a multiplicar y expandimos los binomios al cuadrado:
>    $$10(x^2 - 4x + 4) - 5(y^2 + 8y + 16) = 50$$
> 3. **Distribución de coeficientes:** Multiplicamos cada término cuidando especialmente el signo del segundo bloque:
>    $$(10x^2 - 40x + 40) - (5y^2 + 40y + 80) = 50$$
>    $$10x^2 - 40x + 40 - 5y^2 - 40y - 80 = 50$$
> 4. **Ordenamiento e igualación a cero:** Agrupamos los términos según la estructura general y trasladamos el 50:
>    $$10x^2 - 5y^2 - 40x - 40y + (40 - 80 - 50) = 0$$
> 
> **Resultado:**
> $$10x^2 - 5y^2 - 40x - 40y - 90 = 0$$

## Ejercicios de repaso

> [!abstract] 🟢 Fácil
> **Título:** `title: 🟢 Fácil`
> Convierte la siguiente ecuación a su forma general:
> $$\frac{y^2}{10} - x^2 = 1$$
> *(Pista: Coloca un 1 como denominador debajo de $x^2$ para facilitar la resta de fracciones).*

> [!abstract] 🟡 Medio
> **Título:** `title: 🟡 Medio`
> Convierte la siguiente ecuación a su forma general:
> $$\frac{y^2}{10} - \frac{x^2}{12} = 1$$

> [!abstract] 🔴 Avanzado — Aplicación con $USD
> **Título:** `title: 🔴 Avanzado — Aplicación con $USD`
> Una empresa de logística utiliza una trayectoria hiperbólica para modelar sus costos de producción en una gráfica financiera, definida por la ecuación:
> $$\frac{(y+3)^2}{4} - \frac{(x-1)^2}{7} = 1$$
> Para ingresar estos datos en un sistema contable que solo acepta formatos generales ($Ax^2 + By^2 + Cx + Dy + E = 0$), transforma la trayectoria a su forma general.

> [!tip] 💡 Consejo de estudio
> Al organizar tu respuesta final, asegúrate de que el término $x^2$ preceda al término $y^2$. Presta **atención extrema al signo negativo** central: este afecta a **todo** el numerador de la segunda fracción tras la expansión. 
> 
> **Pro-tip del Profe Alex:** Si tras igualar a cero el primer término ($Ax^2$) resulta ser negativo, es una práctica común y elegante multiplicar toda la ecuación por $-1$ para que el coeficiente de $x^2$ sea positivo. ¡Ambas formas son correctas, pero esta última es la preferida en los exámenes!