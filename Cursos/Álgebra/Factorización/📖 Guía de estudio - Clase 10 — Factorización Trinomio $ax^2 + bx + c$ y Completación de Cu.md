# 📖 Guía de estudio — Clase 10: Los 6 Métodos de Factorización más utilizados

> [!info] 📌 Conceptos clave
> Como especialistas, nuestra prioridad es que desarrolles un "ojo clínico" para las matemáticas. Antes de operar, analiza la estructura de la expresión siguiendo estos pilares:
> - **Prioridad de análisis (El filtro del Factor Común):** Este es siempre el primer paso. No importa si tienes 2, 3 o más términos; siempre verifica si hay algo que se repita. Extraer el factor común simplifica la expresión y, a menudo, revela qué segundo método debes aplicar.
> - **Jerarquía por número de términos:** 
> 	- **2 términos (Binomios):** Busca una Diferencia de Cuadrados o una Suma/Diferencia de Cubos.
> 	- **3 términos (Trinomios):** Evalúa si es un Trinomio Cuadrado Perfecto (TCP), o de las formas $x^2 + bx + c$ o $ax^2 + bx + c$.
> - **Reconocimiento visual de potencias:** Para ganar velocidad, identifica raíces al instante. 
>   - **Raíz Cuadrada:** Divide el exponente entre 2 (Ej: $\sqrt{x^{10}} = x^5$).
>   - **Raíz Cúbica:** Divide el exponente entre 3 (Ej: $\sqrt[3]{x^{12}} = x^4$).
> - **El orden es ley:** Organiza siempre los términos de mayor a menor exponente respecto a una variable. Un trinomio desordenado es la causa principal de errores en los signos.

## Fórmulas y definiciones importantes

| Método | Definición / Lógica Didáctica | Regla de Signos / Estructura |
| :--- | :--- | :--- |
| **Factor Común** | Se extrae el Máximo Común Divisor (MCD) de los números y la letra con el **menor exponente** presente en todos los términos. | $a(b + c) = ab + ac$ |
| **Diferencia de Cuadrados** | Dos términos con raíces cuadradas exactas restándose. | $(a - b)(a + b)$ |
| **Suma o Diferencia de Cubos** | Dos términos con raíces cúbicas exactas. El segundo paréntesis es un trinomio. | Suma: $(a + b)(a^2 - ab + b^2)$ <br> Resta: $(a - b)(a^2 + ab + b^2)$ |
| **Trinomio Cuadrado Perfecto** | El término central debe ser el **doble producto** de las raíces del primer y tercer término ($2 \times r_1 \times r_2$). | $(a \pm b)^2$ |
| **Trinomio $x^2 + bx + c$** | Buscamos dos números que multiplicados den '$c$' y sumados/restados den '$b$'. | **1er signo:** el del 2do término. <br> **2do signo:** producto del 2do por el 3ero. |
| **Trinomio $ax^2 + bx + c$** | *(Método de multiplicar y dividir por 'a')*. Se busca transformar la expresión para que el término $(ax)$ actúe como una sola variable. | Se multiplica y divide todo por '$a$', dejando la multiplicación **indicada** en el término central. |

## Ejemplos resueltos paso a paso

> [!example] Ejemplo A — Trinomio de la forma $x^2 + bx + c$
> **Ejercicio:** Factorizar $x^2 + 3x - 10$
> 1. **Preparación:** Abrimos dos paréntesis y repartimos la raíz del primer término: $(x \quad )(x \quad )$.
> 2. **Determinación de signos:** 
>    - El primer paréntesis lleva el signo del segundo término: $(+)$.
>    - El segundo paréntesis lleva el producto de los signos ($+ \times - = -$): $(-)$.
> 3. **Criterio numérico:** Como los signos son opuestos ($+$ y $-$), buscamos números que **restados** den 3 y **multiplicados** den 10.
> 4. **Selección:** Los números son 5 y 2. Siempre colocamos el mayor primero.
> 
> ✅ **Resultado:** $(x + 5)(x - 2)$

> [!example] Ejemplo B — Aplicación financiera (Diferencia de Cuadrados)
> **Enunciado:** El área de un terreno para un proyecto de $USD está representada por $25x^4 - 49y^2$. Factoriza para hallar sus dimensiones.
> 1. **Extracción de raíces:** 
>    - $\sqrt{25x^4} = 5x^2$ (dividimos exponente $4 \div 2$).
>    - $\sqrt{49y^2} = 7y$ (dividimos exponente $2 \div 2$).
> 2. **Construcción:** Aplicamos la estructura de binomios conjugados $(a-b)(a+b)$.
> 
> ✅ **Resultado:** $(5x^2 - 7y)(5x^2 + 7y)$

## Ejercicios de repaso

> [!abstract] 🟢 Nivel Inicial
> 1. **Factor común:** $9x^2y^3 - 12x^3y^2$  *(Ayuda: El MCD de 9 y 12 es 3)*.
> 2. **Diferencia de cuadrados:** $x^2 - y^2$
> 3. **Diferencia de cuadrados:** $16m^4 - 1$

> [!abstract] 🟡 Nivel Medio (Análisis de signos)
> 1. $n^2 - 8n + 12$
> 2. $y^2 - 9y + 20$
> 3. $x^2 - 7x - 30$

> [!abstract] 🔴 Nivel Avanzado — Aplicación en Costos $USD
> **Desafío:** Un contratista define su costo total como $12m^4 - 13m^2 - 35$. Factoriza para hallar los costos unitarios.
> 
> **Paso 1: Multiplicar y dividir por 12.** Transformamos para que aparezca el término $(12m^2)$:
> $\frac{(12m^2)^2 - 13(12m^2) - 420}{12}$
> 
> **Paso 2: Hallar los números críticos.** Necesitamos números que multiplicados den $420$ y restados den $13$. 
> *Técnica didáctica (Descomposición):* $420 = 2 \times 2 \times 3 \times 5 \times 7$. Combinando factores, hallamos **28** ($2 \times 2 \times 7$) y **15** ($3 \times 5$).
> 
> **Paso 3: Factorizar y simplificar.** 
> $\frac{(12m^2 - 28)(12m^2 + 15)}{12}$
> Para eliminar el denominador, buscamos factores en los paréntesis que multipliquen 12 ($4 \times 3$):
> - Sacamos cuarta al primer paréntesis: $(3m^2 - 7)$.
> - Sacamos tercera al segundo paréntesis: $(4m^2 + 5)$.
> 
> ✅ **Resultado final:** $(3m^2 - 7)(4m^2 + 5)$

> [!tip] 💡 Estrategia de Maestría
> 1. **La Prueba de Fuego:** Nunca des un ejercicio por terminado sin verificar. Aplica la **Propiedad Distributiva** (multiplicar los factores); si no regresas a la expresión original, revisa tus signos.
> 2. **Agilidad Mental:** Memoriza los cuadrados (1, 4, 9... hasta 100) y cubos (1, 8, 27, 64, 125). Identificar estos números te dirá qué método usar en menos de un segundo.
> 3. **La Regla del 1%:** Solo el 1% de los estudiantes alcanzan la excelencia. Ese 1% es el que no se rinde, el que practica un ejercicio extra y el que entiende que la factorización no es memoria, sino reconocimiento de patrones. ¡Tú perteneces a ese grupo!