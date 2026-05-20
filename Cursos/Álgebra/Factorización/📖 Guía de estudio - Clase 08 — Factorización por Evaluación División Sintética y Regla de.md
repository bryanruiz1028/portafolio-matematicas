# 📖 Guía de estudio — Clase 08: Factorización por Evaluación (División Sintética y Regla de Ruffini)

> [!info] 📌 Conceptos clave
> ¡Hola! Bienvenido a una de las herramientas más poderosas del álgebra. Aquí aprenderemos a "desarmar" polinomios grandes siguiendo estos puntos esenciales:
> - **Para qué sirve:** Es el método ideal para factorizar polinomios de grado 3 o superior ($x^3, x^4, x^5...$), donde otros métodos ya no son suficientes.
> - **Candidatos a raíces:** No adivinamos al azar; probamos con los **divisores del término independiente** (tanto positivos como negativos).
> - **El residuo mágico:** Si al final de la "cajita" de Ruffini obtienes un **0**, ¡felicidades! Has encontrado una **raíz** o "cero" del polinomio.
> - **Teorema del Residuo:** Que el residuo sea cero significa que el polinomio evaluado en ese número es $P(a) = 0$, lo que nos permite extraer un factor exacto y reducir el grado de la expresión.

---

## 📐 Fórmulas y Definiciones Importantes

Dominar estos términos te ayudará a no perderte en el proceso. ¡Tú puedes con esto!

| Término | Definición / Fórmula |
| :--- | :--- |
| **Término Independiente** | Es el número "solitario" al final de la expresión, el que no tiene letra (variable). |
| **Divisores** | Números que dividen exactamente al término independiente. **¡Recuerda!** Siempre considera la pareja positiva y negativa (ej: $\pm 1, \pm 2, \pm 3$). |
| **Factor** | Es la forma de expresar la raíz dentro de un paréntesis. **¡Atención al signo!**: Si tu raíz es $x = a$, el factor se escribe con el signo opuesto: $(x - a)$. |
| **Coeficiente** | El número que acompaña a cada letra. Si la letra está sola (ej: $x^3$), su coeficiente es $1$. Si falta un término (ej: no hay $x^2$), su coeficiente es $0$. |

---

## 📝 El Proceso Paso a Paso

Sigue esta receta lógica para no fallar. ¡Organización es la clave del éxito!

1.  **Organizar:** Ordena el polinomio de mayor a menor exponente.
2.  **Extraer coeficientes:** Escribe solo los números. **¡Mucho ojo aquí!** Si falta alguna potencia, pon un $0$ o el resultado será incorrecto.
3.  **Probar divisores:** Elige un divisor del término independiente. Colócalo a la izquierda de tu "cajita".
4.  **Operar (Multiplica y Suma):** Baja el primer coeficiente, multiplícalo por la raíz, coloca el resultado debajo del siguiente número y suma/resta según los signos.
5.  **Repetir o "Rematar":** Si el residuo es cero, ya tienes un factor. Puedes seguir con Ruffini o, si ya llegaste a una expresión de grado 2 ($x^2$), usar los métodos de trinomios para terminar más rápido.

---

## 💡 Ejemplos Resueltos

> [!example] Ejemplo A: Caso Básico (Grado 3)
> **Polinomio:** $x^3 - 4x^2 + x + 6$
> 1. **Divisores de 6:** $\pm 1, \pm 2, \pm 3, \pm 6$.
> 2. **Prueba fallida:** Si probamos con $1$, el residuo es $4$. ¡No te rindas! Intentemos con otro.
> 3. **Prueba exitosa con $x = -1$:**
>    - Bajamos el $1$.
>    - $1 \times (-1) = -1 \rightarrow$ Sumamos: $-4 - 1 = -5$.
>    - $-5 \times (-1) = 5 \rightarrow$ Sumamos: $1 + 5 = 6$.
>    - $6 \times (-1) = -6 \rightarrow$ Sumamos: $6 - 6 = 0$. **¡Bingo!**
> 4. **Factores:** La raíz $x = -1$ se convierte en $(x + 1)$. Lo que queda es el trinomio $x^2 - 5x + 6$.
> 5. **Finalización:** Factorizamos el trinomio buscando números que multiplicados den $6$ y sumados den $-5$. ¡Son $-2$ y $-3$!
> **Resultado final:** $(x + 1)(x - 2)(x - 3)$

> [!example] Ejemplo B: Variación de Ganancias ($USD)
> **Contexto:** Imagina que el polinomio $x^4 + x^3 - 6x^2 - 4x + 8$ representa la variación de ganancias de una tienda en un periodo de $x$ meses. Factorizarlo nos ayuda a encontrar los "puntos de equilibrio" donde la ganancia fue cero.
> 1. **Primer paso:** Al probar con $x = 1$, el residuo es $0$. Esto significa que en el **mes 1**, la tienda no ganó ni perdió. Factor: $(x - 1)$.
> 2. **Segundo paso:** Con los coeficientes restantes ($1, 2, -4, -8$), probamos con $x = 2$. ¡También da residuo $0$! Significa que en el **mes 2** hubo otro punto de equilibrio. Factor: $(x - 2)$.
> 3. **Tercer paso:** Nos queda el trinomio $x^2 + 4x + 4$. Este es un **Trinomio Cuadrado Perfecto**.
>    - Se factoriza como $(x + 2)(x + 2)$ o $(x + 2)^2$.
> **Interpretación Financiera:** El resultado $(x - 1)(x - 2)(x + 2)^2$ nos dice que los momentos críticos de la tienda ocurrieron en los meses 1 y 2.
> **Resultado final:** $(x - 1)(x - 2)(x + 2)^2$

---

## ✍️ Ejercicios de Repaso

> [!abstract] 🟢 Nivel Fácil
> Factoriza el siguiente polinomio de grado 3:
> $x^3 - 2x^2 - x + 2$
> *Pista: ¡Prueba con el 1 positivo! Si la suma de coeficientes es cero, ya tienes el camino libre.*

> [!abstract] 🟡 Nivel Medio
> Factoriza el siguiente polinomio de grado 4. Necesitarás aplicar Ruffini dos veces antes de poder usar el método de trinomios:
> $n^4 + n^3 - 27n^2 - n + 120$
> *Pista: Los factores incluyen raíces como $2$ y $-3$. ¡No olvides cambiarles el signo al escribir el paréntesis!*

> [!abstract] 🔴 Nivel Avanzado (Aplicación $USD)
> Un modelo de flujos financieros de una empresa está representado por:
> $2x^5 - x^4 - 20x^3 - 5x^2 + 48x + 36$
> **Tu reto:** Encuentra los 5 factores. Si llegas a un trinomio de la forma $ax^2 + bx + c$, utiliza el método de multiplicación y división por el coeficiente principal para "rematar" el ejercicio.
>
> **Clave de respuestas (¡No la mires hasta terminar!):**
> Los factores son: $(x + 1)(x - 2)(x + 2)(x - 3)(2x + 3)$.
> *Nota: El factor $(2x+3)$ representa un flujo proyectado donde el tiempo o la tasa tienen una proporción de 2 a 3.*

---

> [!tip] 💡 Consejo de estudio
> Utiliza el **"Ojo Clínico"** del Profe Alex para ahorrar tiempo valioso:
> 1. **La prueba del 1:** Suma todos los coeficientes del polinomio. Si el resultado es **exactamente 0**, ¡no busques más! La primera raíz es $x = 1$.
> 2. **Sé un estratega:** No es obligatorio hacer Ruffini hasta el final. En cuanto reduzcas el polinomio a grado 2 ($x^2$), utiliza la factorización de trinomios de la forma $x^2 + bx + c$ o $ax^2 + bx + c$. ¡Es mucho más rápido y te hará ver como un experto!