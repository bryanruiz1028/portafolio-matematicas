# 📖 Guía de estudio — Clase 02: Centro y radio de la circunferencia a partir de la ecuación general

> [!info] 📌 Conceptos clave
> Para dominar la transición de la ecuación general a los elementos de la circunferencia, recuerda estos 4 puntos esenciales:
> * **Identificación visual:** Una ecuación general siempre debe estar igualada a cero ($= 0$). Además, los términos $x^2$ e $y^2$ deben tener coeficiente $1$ (es decir, deben estar "solitos").
> * **Presencia de términos:** La estructura es $x^2 + y^2 + Dx + Ey + F = 0$. ¡Ojo! Si en tu ejercicio no aparece el término con $x$ o con $y$, significa que su coeficiente ($D$ o $E$) es automáticamente $0$.
> * **Importancia de los signos:** Al identificar $D$, $E$ y $F$, debes respetar el signo que tienen en la ecuación. Si la fórmula dice $-D/2$ y tu $D$ es negativo, terminarás con un valor positivo.
> * **Existencia real y el discriminante:** El valor dentro de la raíz del radio ($D^2 + E^2 - 4F$) determina qué estás dibujando:
>     1. Si es **positivo**: Es una circunferencia real.
>     2. Si es **cero**: La circunferencia se reduce a un **único punto** (el centro).
>     3. Si es **negativo**: No existe una circunferencia real, pues no hay raíces cuadradas de números negativos.

---

## 2. Tabla de Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ecuación General** | $x^2 + y^2 + Dx + Ey + F = 0$ |
| **Centro ($C$)** | Punto central de coordenadas $(h, k)$ donde: <br> $h = -\frac{D}{2}$ <br> $k = -\frac{E}{2}$ |
| **Radio ($r$)** | Distancia constante del centro a la orilla: <br> $r = \frac{1}{2}\sqrt{D^2 + E^2 - 4F}$ |
| **Ecuación Canónica** | $(x - h)^2 + (y - k)^2 = r^2$ <br> (Útil como método alternativo completando cuadrados). |

---

## 3. Ejemplos Resueltos

> [!example] Ejemplo A: Caso Básico
> **Problema:** Hallar el centro y el radio de la circunferencia: $x^2 + y^2 - 8x - 10y + 40 = 0$.
> 
> **Paso 1: Identificar coeficientes ($D, E, F$)**  
> * $D = -8$  
> * $E = -10$  
> * $F = 40$  
> 
> **Paso 2: Calcular el Centro ($h, k$)**  
> * $h = -\frac{-8}{2} = \frac{8}{2} = 4$  
> * $k = -\frac{-10}{2} = \frac{10}{2} = 5$  
> **Resultado:** Centro $C(4, 5)$.
> 
> **Paso 3: Calcular el Radio ($r$)**  
> * $r = \frac{1}{2}\sqrt{(-8)^2 + (-10)^2 - 4(40)}$  
> * $r = \frac{1}{2}\sqrt{64 + 100 - 160}$  
> * $r = \frac{1}{2}\sqrt{4} = \frac{1}{2}(2) = 1$  
> **Resultado:** Radio $r = 1$.

> [!example] Ejemplo B: Aplicación Práctica (Señal de Seguridad)
> **Contexto:** Un emisor de señal cubre un área circular definida por $x^2 + y^2 + 2y - 7 = 0$. Determina la ubicación del emisor y el alcance. El costo de instalación por **metro lineal de radio** es de $1 USD.
> 
> **Procedimiento:**
> 1. **Identificar valores:** $D = 0$ (porque no hay término con $x$), $E = 2$, $F = -7$.
> 2. **Ubicación (Centro):** 
>    * $h = -\frac{0}{2} = 0$
>    * $k = -\frac{2}{2} = -1$
>    * El emisor se ubica en **$C(0, -1)$**.
> 3. **Alcance (Radio):**
>    * $r = \frac{1}{2}\sqrt{0^2 + 2^2 - 4(-7)}$
>    * $r = \frac{1}{2}\sqrt{4 + 28} = \frac{1}{2}\sqrt{32}$
>    * $r \approx \frac{1}{2}(5.656) \approx 2.82$ metros.
> 
> **Resultado Presupuestario:** El radio de alcance es de **2.82 metros**. Como cada metro de radio cuesta $1 USD, el costo total basado en el alcance es de **$2.82 USD**.

---

## 4. Ejercicios de Repaso

> [!abstract] 🟢 Nivel Fácil
> **Enunciado:** Encuentra el centro y el radio de la circunferencia: $x^2 + y^2 - 8x - 10y + 40 = 0$.  
> *(Pista: Identifica $D$ y $E$, cámbiales el signo y divídelos entre dos para hallar el centro rápidamente).*

> [!abstract] 🟡 Nivel Medio
> **Enunciado:** Calcula el centro y el radio de la ecuación: $x^2 + y^2 + x - 6 = 0$.  
> *(¡Atención!: Nota que no hay término en $y$ ($E=0$) y que $D$ es impar, por lo que trabajarás con fracciones o decimales).*

> [!abstract] 🔴 Nivel Avanzado — Aplicación con Presupuesto
> **Enunciado:** Se desea cercar una zona de juegos cuya ecuación es $x^2 + y^2 - 4x + 6y = -9$.
> 1. **Ordena:** Pasa la ecuación a su forma general igualada a cero.
> 2. **Calcula:** Encuentra el radio de la zona.
> 3. **Presupuesto:** Si el costo de materiales depende del tamaño del radio y cada unidad de radio cuesta **$10 USD**, ¿cuál es el costo total de la obra?

---

> [!tip] 💡 Consejo de estudio
> Para encontrar el centro $(h, k)$ sin memorizar fórmulas largas, usa el truco del Profe Alex: **"Toma los números que acompañan a la $x$ y a la $y$, cámbiales el signo y divídelos entre dos"**. ¡Es la forma más rápida y segura de no equivocarte en un examen!