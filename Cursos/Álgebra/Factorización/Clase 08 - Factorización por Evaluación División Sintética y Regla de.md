# Clase 08 — Factorización por Evaluación: División Sintética y Regla de Ruffini

`#algebra` `#factoringbyeval`

> [!info] 🧭 Navegación
> - **Anterior:** [[Clase 07 — Factorización de Trinomios]]
> - **Índice:** [[Índice de Álgebra]]
> - **Siguiente:** [[Clase 09 — Fracciones Algebraicas y Simplificación]]

---

### 🌍 Relevancia y aplicaciones

> [!info] **¿Por qué aprender esto?**
> La factorización de polinomios de grado superior permite descomponer funciones matemáticas complejas en factores lineales simples para analizar su comportamiento gráfico. Es la herramienta clave para identificar los puntos exactos donde una curva interseca el eje horizontal, permitiendo modelar fenómenos físicos y financieros con precisión técnica. Dominar este método facilita la resolución de ecuaciones que, a simple vista, parecen imposibles de simplificar.

*   💵 **Finanzas:** Se utiliza para encontrar los **puntos de equilibrio** en funciones de costos o ganancias expresadas en $USD; es decir, los valores donde la utilidad es exactamente cero.
*   🏗️ **Ingeniería:** Análisis de la estabilidad de estructuras mediante el cálculo de las raíces de polinomios de grado 3 o 4 que representan tensiones internas.
*   📊 **Crecimiento:** Predicción de tendencias en fenómenos biológicos o económicos donde los datos no son lineales y requieren curvas polinomiales para su ajuste.

---

### 📌 ¿Qué es la Factorización por Evaluación (División Sintética/Ruffini)?

> [!note] **Definición para principiantes**
> Imagina que tienes un polinomio muy grande (como un juguete complejo armado con muchas piezas). Este método es un "truco" para desarmarlo en piezas pequeñas llamadas factores. Lo logramos probando con los números que dividen exactamente al **término independiente** (el número que no tiene letra al final) hasta que el residuo de nuestra cuenta sea **cero**.

> [!warning] ⚠️ **Error común: El término faltante**
> Si el polinomio salta de un exponente a otro (por ejemplo, de $x^3$ directamente a $x$, sin tener $x^2$), **debes colocar un 0** como coeficiente en ese lugar dentro de la tabla. Si omites este paso, el procedimiento fallará completamente.

> [!tip] 💡 **Truco para recordarlo**
> Usa la técnica de **"Baja, multiplica y suma"**: El primer número de la izquierda siempre "cae" directo al fondo de la tabla. Luego, ese número se multiplica por la raíz que estás probando, el resultado se coloca en la siguiente columna y se suma verticalmente para repetir el ciclo.

---

### Procedimiento Paso a Paso

1.  **Organizar y Extraer:** Ordena el polinomio de mayor a menor exponente y extrae los coeficientes. Si falta un grado, coloca un cero.
2.  **Identificar Divisores:** Busca todos los divisores (positivos y negativos) del término independiente. Estas son tus "raíces candidatas".
3.  **Ejecutar Ruffini:** Prueba los divisores en la tabla usando el ciclo de "multiplicar y sumar" hasta que el último número (residuo) sea **0**.
4.  **Escribir Factores y Reducir:** Si el número $x = c$ funciona, el factor es **$(x - c)$** (¡cuidado con el cambio de signo!). El resultado de la tabla es un polinomio de un grado menor. Repite el proceso hasta llegar a un trinomio de segundo grado que puedas factorizar por métodos tradicionales.

---

### Ejemplos Prácticos

#### Ejemplo 1: Caso Básico ($x^3 - 4x^2 + x + 6$)
Buscamos los divisores de **6**: $\pm1, \pm2, \pm3, \pm6$. Probamos con $x = -1$:

| Raíz | 1 | -4 | 1 | 6 |
| :---: | :---: | :---: | :---: | :---: |
| **-1** | | -1 | 5 | -6 |
| | **1** | **-5** | **6** | **0** |

Como el residuo es **0**, el primer factor es $(x + 1)$. Los coeficientes restantes ($1, -5, 6$) forman el trinomio $x^2 - 5x + 6$, que se factoriza como $(x-2)(x-3)$.
**Resultado final:** **$(x+1)(x-2)(x-3)$**.

#### Ejemplo 2: Manejo de Signos ($a^3 - 2a^2 - 5a + 6$)
Probamos con la raíz $x = 1$:

| Raíz | 1 | -2 | -5 | 6 |
| :---: | :---: | :---: | :---: | :---: |
| **1** | | 1 | -1 | -6 |
| | **1** | **-1** | **-6** | **0** |

El primer factor es $(a-1)$. El residuo es $a^2 - a - 6$, que factorizado resulta en $(a-3)(a+2)$.
**Resultado final:** **$(a-1)(a-3)(a+2)$**.

#### Ejemplo 3: Doble División Sintética ($x^4 + x^3 - 6x^2 - 4x + 8$)
Al ser grado 4, reducimos el grado dos veces:
1.  **Primera división ($x = 1$):** Produce el factor $(x-1)$ y deja los coeficientes $1, 2, -4, -8$.
2.  **Segunda división ($x = 2$):** Usamos los nuevos coeficientes. Produce el factor $(x-2)$ y deja $1, 4, 4$.
3.  **Trinomio final:** $x^2 + 4x + 4$, que es un Trinomio Cuadrado Perfecto: $(x+2)^2$.

**Resultado final:** **$(x-1)(x-2)(x+2)^2$**.

#### Ejemplo 4: Aplicación Real en $USD ($2x^5 - x^4 - 20x^3 - 5x^2 + 48x + 36$)
Esta función representa el ingreso de una empresa. Los factores representan los **puntos de equilibrio** (donde el ingreso es cero).
- Probamos raíces: $x = -1$, $x = 2$, $x = -2$.
- Esto nos deja con el trinomio $2x^2 - 3x - 9$.
- Para factorizar $2x^2 - 3x - 9$, multiplicamos y dividimos por el coeficiente principal (2):
  $\frac{(2x)^2 - 3(2x) - 18}{2} = \frac{(2x-6)(2x+3)}{2} = (x-3)(2x+3)$.

**Puntos de equilibrio (Factores):** **$(x+1)(x-2)(x+2)(x-3)(2x+3)$**.

---

### Ejercicios para el Estudiante

> [!abstract] **Nivel Verde: Inicial**
> 1. $x^3 - 6x^2 + 11x - 6$
> 2. $x^3 + 2x^2 - x - 2$
> 3. $x^3 - 3x^2 - 4x + 12$
> 4. $x^3 + 4x^2 + x - 6$

> [!abstract] **Nivel Amarillo: Intermedio**
> 1. $x^4 - 5x^2 + 4$ (Recuerda usar el coeficiente 0 para $x^3$ y $x$)
> 2. $x^4 + 2x^3 - 13x^2 - 14x + 24$
> 3. $x^4 - 10x^2 + 9$
> 4. $n^4 - 27n^2 - 46n + 120$

> [!abstract] **Nivel Rojo: Desafío Aplicado**
> 1. Halla los factores del costo total $C(x) = x^3 - 7x + 6$ en $USD.
> 2. Factoriza $2x^3 - 3x^2 - 8x - 3$ (Atención al coeficiente 2).
> 3. $8a^4 - 18a^3 - 75a^2 + 46a + 120$
> 4. $x^5 - 5x^4 - 7x^3 + 41x^2 + 30x - 72$

---