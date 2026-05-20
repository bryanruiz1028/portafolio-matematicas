# 📖 Guía de estudio — Clase 06: Dominio, rango y gráfica de una función racional

> [!info] 📌 Conceptos clave
> Una función racional es aquella que se expresa como el cociente de dos polinomios, donde la variable independiente ($x$) aparece necesariamente en el denominador. Para facilitar el álgebra, un "pro-tip" pedagógico es reemplazar siempre $f(x)$ por $y$. El análisis completo se resume en estos 4 pilares:
> 1. **Factorización:** Es el primer paso para simplificar la función y descubrir "tesoros ocultos" como los huecos.
> 2. **Identificación de asíntotas:** Determinar las "barreras invisibles" verticales (donde el denominador es cero) y horizontales (el comportamiento en el infinito).
> 3. **Determinación de ceros:** Hallar los puntos donde la función toca los ejes coordenados.
> 4. **Importancia de la gráfica:** Graficar permite validar visualmente el dominio y el rango, detectando saltos que el análisis numérico podría ignorar.

## Tabla de Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Dominio** | Conjunto de todos los números reales (simbolizado como $\mathbb{R}$) excepto los valores que anulan el denominador (causantes de asíntotas verticales o huecos). |
| **Asíntota Vertical** | Recta a la que la función se acerca infinitamente pero nunca toca. Se obtiene igualando el denominador a cero ($D(x) = 0$). |
| **Asíntota Horizontal** | Indica el valor de $y$ al que se estabiliza la función cuando $x$ es muy grande. Si los grados del numerador y denominador son iguales, se calcula como el cociente de los **Coeficientes Principales** (los números que acompañan a la $x$ de mayor grado). |
| **Huecos (Puntos de discontinuidad)** | Se presentan cuando un factor idéntico se simplifica arriba y abajo. Representan un "punto vacío" en la gráfica. |
| **Rango** | Conjunto de valores de salida ($y$). Se determina analizando la gráfica o despejando la variable $x$ para identificar qué valores de $y$ generan una indeterminación. |

---

## Ejemplos Resueltos Adicionales

::: ad-example
### Ejemplo A: Análisis de asíntotas y ceros
**Problema:** Analizar detalladamente la función $f(x) = \frac{2x^2+4}{2x^2-8}$

**1. Sustitución, factorización y simplificación:**
Cambiamos $f(x)$ por $y$ y extraemos el factor común $2$:
$y = \frac{2(x^2+2)}{2(x^2-4)}$
Simplificamos los coeficientes: $y = \frac{x^2+2}{x^2-4}$
*Nota:* El numerador ($x^2+2$) no se puede factorizar más por ser una suma de cuadrados, pero el denominador es una diferencia de cuadrados: $y = \frac{x^2+2}{(x+2)(x-2)}$.

**2. Cálculo de asíntotas verticales:**
Igualamos cada factor del denominador a cero:
$x + 2 = 0 \Rightarrow x = -2$
$x - 2 = 0 \Rightarrow x = 2$
Hay dos asíntotas verticales en $x = -2$ y $x = 2$.

**3. Asíntota horizontal:**
Dividimos los coeficientes principales. Observa que el resultado es el mismo en la función original y en la simplificada:
Original: $y = \frac{2}{2} = 1$ | Simplificada: $y = \frac{1}{1} = 1$
La asíntota horizontal está en $y = 1$.

**4. Cálculo de ceros:**
Igualamos el numerador a cero: $x^2 + 2 = 0 \Rightarrow x^2 = -2$. Como no existe raíz cuadrada de un número negativo en los reales, la función **no tiene ceros** (no cruza el eje $x$).
:::

::: ad-example
### Ejemplo B: Aplicación de costo promedio ($ USD)
**Enunciado:** El costo promedio en USD para producir $x$ cientos de artículos está dado por $C(x) = \frac{x+1}{x+2}$. ¿Cuál es el costo cuando la producción es extremadamente alta?

**1. Análisis de tendencia:**
Una producción "muy alta" significa que $x$ tiende al infinito. Esto se resuelve hallando la asíntota horizontal.

**2. Cálculo:**
Los grados son iguales ($1$). Los coeficientes principales son $1$ en el numerador y $1$ en el denominador:
$y = \frac{1}{1} \Rightarrow y = 1$

**3. Conclusión:**
Cuando la producción aumenta indefinidamente, el costo promedio por cada cien artículos tiende a estabilizarse en **1 USD**.
:::

---

## Ejercicios de Repaso

::: ad-abstract
### 🟢 Nivel Fácil
Dada la función $f(x) = \frac{3x^2}{x^2-1}$:
1. Determina el dominio expresándolo como todos los reales menos las restricciones.
2. Encuentra las asíntotas verticales igualando el denominador a cero.
:::

::: ad-abstract
### 🟡 Nivel Medio
Dada la función $f(x) = \frac{x^3-x^2-2x}{x^3-4x}$:
1. Factoriza completamente ambos términos.
2. Identifica los "tesoros ocultos": ¿En qué valores de $x$ existen huecos? (Pista: busca factores que se simplifiquen, especialmente en $x=0$ y $x=2$).
3. Halla la asíntota horizontal de la función resultante.
:::

::: ad-abstract
### 🔴 Nivel Avanzado (Aplicación de Rango)
En el problema de costos donde $y = \frac{x+1}{x+2}$:
1. **Despeje de variable:** Sigue el método del Profe Alex para despejar $x$ en términos de $y$. (Pista: $(x+2) \cdot y = x+1$).
2. **Análisis de indeterminación:** Una vez despejada la $x$, observa el nuevo denominador. ¿Qué valor de $y$ lo anularía?
3. **Resultado:** Define el rango de la función de costo y explica por qué $y \neq 1$.
:::

---

> [!tip] 💡 Consejo de estudio
> Siguiendo la recomendación del Profe Alex, **siempre realiza el gráfico**, aunque el ejercicio no lo pida. Visualizar la curva es la única forma segura de detectar "huecos" y "saltos" (asíntotas), lo que te permitirá escribir el dominio y el rango con total precisión sin depender únicamente de las fórmulas.