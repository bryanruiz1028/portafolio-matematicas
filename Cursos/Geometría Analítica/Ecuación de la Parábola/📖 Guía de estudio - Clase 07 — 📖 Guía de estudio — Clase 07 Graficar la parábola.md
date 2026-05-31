# 📖 Guía de estudio — Clase 07: Graficar la parábola a partir de la ecuación general

> [!info] **Resumen de la sesión**
> En esta clase aprenderás a transformar la ecuación general de una parábola para descubrir sus elementos ocultos. Los conceptos fundamentales que dominaremos son:
> * **Estructura de las ecuaciones:** La diferencia entre la forma general (igualada a cero) y la canónica (que nos muestra el vértice y el parámetro).
> * **Completar el Trinomio Cuadrado Perfecto (TCP):** La técnica algebraica clave para agrupar términos y simplificar la expresión.
> * **Identificación de elementos:** Cómo extraer el vértice $(h, k)$ y calcular la distancia focal $p$.
> * **Determinación de la apertura:** Analizar hacia dónde se abre la parábola (arriba, abajo, izquierda o derecha) observando los signos y las variables.

## 2. Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ecuación General** | Se presenta igualada a cero: $x^2 + Dx + Ey + F = 0$ (vertical) o $y^2 + Dx + Ey + F = 0$ (horizontal). |
| **Ecuación Canónica (Template)** | **$(x - h)^2 = 4p(y - k)$** o **$(y - k)^2 = 4p(x - h)$**. Es la forma que nos permite "leer" el vértice y la distancia $p$. |
| **Vértice $(h, k)$** | Es el punto más alto, bajo o extremo de la curva. Al extraerlo de la canónica, **siempre debemos cambiar el signo** de los números que acompañan a $x$ y $y$. |
| **Parámetro $p$** | Es la distancia entre el vértice y el foco. Se halla tomando el coeficiente del lado derecho (el número fuera del paréntesis) e igualándolo a $4p$. |

---

## 3. Ejemplos resueltos adicionales

> [!example] **Ejemplo A: Caso Básico (Variable $x^2$)**
> **Problema:** Dada la ecuación $x^2 - 6x - 8y - 7 = 0$, halla su forma canónica y el vértice.
> 
> **Paso 1: Agrupar términos.** Dejamos los términos con $x$ a la izquierda y pasamos el resto al lado derecho con signo contrario:
> $x^2 - 6x = 8y + 7$
> 
> **Paso 2: Completar el trinomio y balancear.** Tomamos el coeficiente de $x$ (6), lo dividimos para 2 y lo elevamos al cuadrado: $(6/2)^2 = 9$.
> **¡Importante!:** Para mantener la igualdad (balance), sumamos 9 en **ambos** lados:
> $x^2 - 6x + 9 = 8y + 7 + 9$
> $x^2 - 6x + 9 = 8y + 16$
> 
> **Paso 3: Factorizar.** El lado izquierdo es un binomio al cuadrado y en el derecho sacamos factor común del número que acompaña a la $y$:
> $(x - 3)^2 = 8(y + 2)$
> 
> **Resultado:**
> * **Vértice:** $(3, -2)$.
> * **Apertura:** Hacia **arriba**, porque la variable sola es $y$ y el coeficiente (8) es positivo.

> [!example] **Ejemplo B: Diseño de un Reflector Parabólico**
> **Problema:** Un ingeniero diseña un reflector cuya curva sigue la ecuación $y^2 - 10y - 12x + 13 = 0$. Se debe instalar un receptor en el foco. Si el costo de instalación es de **$25 USD** por cada unidad de distancia $p$ desde el vértice, ¿cuál es el costo total?
> 
> **Paso 1: Agrupar y mover.** 
> $y^2 - 10y = 12x - 13$
> 
> **Paso 2: Completar el trinomio.** La mitad de 10 es 5, y $5^2 = 25$. Sumamos 25 a **ambos lados** para no alterar la ecuación:
> $y^2 - 10y + 25 = 12x - 13 + 25$
> $y^2 - 10y + 25 = 12x + 12$
> 
> **Paso 3: Factorizar.** 
> $(y - 5)^2 = 12(x + 1)$
> 
> **Análisis y Costo:**
> * El vértice está en $(-1, 5)$.
> * El coeficiente $12$ es igual a $4p$. Por lo tanto, $p = 12/4 = 3$.
> * La parábola abre hacia la **derecha** ($x$ positivo).
> * **Cálculo de costo:** $3 \text{ unidades} \times \$25 \text{ USD} = \mathbf{\$75 \text{ USD}}$.

---

## 4. Ejercicios de repaso

> [!abstract] **Pon a prueba tus conocimientos**
> 
> **🟢 Nivel Fácil**
> Indica el eje (vertical/horizontal) y la dirección (arriba/abajo/izq/der) de apertura:
> 1. $(x + 5)^2 = -12(y - 2)$
> 2. $(y - 1)^2 = 8(x + 4)$
> 
> **🟡 Nivel Medio**
> Transforma la ecuación $y^2 + 6y + 4x + 17 = 0$ a su forma canónica e indica su vértice. (Pista: el resultado tendrá un coeficiente negativo en el lado derecho).
> 
> **🔴 Nivel Avanzado (Cálculo de mantenimiento)**
> Una antena parabólica sigue la ecuación $x^2 + 8x - 8y + 24 = 0$. 
> 1. Encuentra la ubicación de la directriz (recuerda que la distancia del vértice a la directriz es $p$).
> 2. Si el mantenimiento cuesta **$50 USD** por cada unidad de distancia que separa al vértice de la directriz, ¿cuál es el costo total?
> 
> *¡No te rindas! Cada paso que das te acerca más a dominar el álgebra. Tú puedes con este reto.*

---

> [!tip] **Consejo de estudio: El Principio del Espejo**
> Al completar el trinomio, imagina que el signo igual (=) es un espejo. Si agregas un peso (un número) de un lado, debes agregar exactamente el mismo peso del otro lado para que la balanza no se incline. Además, recuerda que al graficar, **$p$ siempre se trata como una distancia positiva**; el signo en la ecuación solo sirve para indicarte si vas hacia la izquierda/abajo (negativo) o derecha/arriba (positivo).