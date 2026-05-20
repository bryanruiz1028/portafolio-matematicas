# Clase 01 — Logaritmos: Introducción y Resolución de Ecuaciones
tags: #algebra #logarithms
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 4

> [!info] 🧭 Navegación
> Siguiente: [[Clase 02]]

> [!info] 🌍 Relevancia y aplicaciones
> Los logaritmos son herramientas matemáticas fundamentales que permiten despejar incógnitas cuando estas se encuentran en el exponente, resultando esenciales para medir procesos de crecimiento.
> - 💵 **Finanzas:** Cálculo de intereses compuestos y determinación del tiempo necesario para duplicar una inversión en $USD.
> - 🏗️ **Ingeniería:** Uso en escalas logarítmicas como la escala Richter (sismos) o la medición de decibelios (sonido).
> - 📊 **Ciencias:** Análisis del crecimiento poblacional y la velocidad de propagación de datos o virus.

---

> [!note] 📌 ¿Qué son los Logaritmos?
> Un logaritmo es, esencialmente, la búsqueda de un **exponente**. La pregunta clave que debemos hacernos es: "¿A qué número debo elevar la base para obtener el argumento (resultado de la potencia)?".
> 
> **Ejemplo:** $\log_2 8 = 3$ porque $2^3 = 8$.

> [!warning] ⚠️ Error común
> ❌ **Incorrecto:** Pensar que si un logaritmo no tiene base escrita, la base es 1.
> ✅ **Correcto:** Cuando no hay una base escrita, se sobreentiende por convención que la **base es 10**.

> [!tip] 💡 Truco para recordarlo: La regla del "giro"
> Para convertir un logaritmo en potencia, imagina un giro: la base "empuja" al resultado para convertirlo en su exponente, y esto se iguala al argumento.
> $$\log_{\text{base}}(\text{argumento}) = \text{resultado} \implies \text{base}^{\text{resultado}} = \text{argumento}$$

---

### 4. Procedimiento Paso a Paso
Para resolver ecuaciones logarítmicas, siga estos cuatro pasos universales basados en la metodología didáctica del curso:

```text
PASO 1 → Simplificar los logaritmos utilizando propiedades. 
         (Suma se convierte en multiplicación; resta se convierte en división).
PASO 2 → Convertir el logaritmo a su forma exponencial o, si hay logaritmos 
         de la misma base en ambos lados, igualar directamente los argumentos.
PASO 3 → Resolver la ecuación lineal resultante (agrupar términos con X en un 
         lado y números en el otro).
PASO 4 → Verificar que el resultado sea válido. Al sustituir la X obtenida, 
         el argumento resultante DEBE SER MAYOR QUE CERO (> 0).
```

---

### 5. Ejemplos Desarrollados

> [!example] Ejemplo 1: Conversión básica
> **Resolver:** $\log_3(2x - 5) = 2$
> 1. Aplicamos la definición (el giro): $3^2 = 2x - 5$.
> 2. Resolvemos la potencia: $9 = 2x - 5$.
> 3. Despejamos: $9 + 5 = 2x \implies 14 = 2x$.
> 4. **Resultado:** $x = 7$. (Verificación: $2(7)-5 = 9$, el cual es $>0$. Es válido).

> [!example] Ejemplo 2: Igualación de argumentos
> **Resolver:** $\log_5(2x - 23) = \log_5(x - 5)$
> 1. Al tener la misma base (5) en ambos lados, eliminamos los logaritmos e igualamos argumentos: $2x - 23 = x - 5$.
> 2. Agrupamos términos: $2x - x = -5 + 23$.
> 3. **Resultado:** $x = 18$. (Verificación: $18-5 = 13$, el cual es $>0$. Es válido).
> *Nota: Es vital cuidar los signos al trasponer términos.*

> [!example] Ejemplo 3: Uso de propiedades (Resta) y Validación
> **Resolver:** $\log_2(x - 3) - \log_2(5) = \log_2(2x + 1)$
> 1. La resta de logaritmos se convierte en división: $\log_2(\frac{x-3}{5}) = \log_2(2x + 1)$.
> 2. Igualamos argumentos: $\frac{x-3}{5} = 2x + 1$.
> 3. Pasamos el 5 multiplicando: $x - 3 = 5(2x + 1) \implies x - 3 = 10x + 5$.
> 4. Despejamos: $-3 - 5 = 10x - x \implies -8 = 9x \implies x = -8/9$.
> 5. **Análisis de validez:** Al sustituir $x = -8/9$ en el primer argumento $(x - 3)$, obtenemos $-8/9 - 3 = -35/9$. Como el argumento es negativo, **la ecuación no tiene solución real**.

> [!example] Ejemplo 4: Aplicación en Inversiones ($USD)
> **Problema:** Si una cuenta en $USD se duplica cada año, ¿en cuánto tiempo llegará a 30 veces su valor original?
> **Ecuación:** $2^x = 30$
> 1. Aplicamos logaritmo a ambos lados: $\log(2^x) = \log(30)$.
> 2. Bajamos el exponente: $x \cdot \log(2) = \log(30)$.
> 3. Despejamos con calculadora: $x = \frac{\log(30)}{\log(2)}$.
> 4. **Resultado:** $x \approx 4.91$ años.

---

### 6. Ejercicios para el Estudiante

**A. Fácil (Introducción al cálculo directo)**
1. $\log_3 3$
2. $\log_{25} 25$
3. $\log_2 16$
4. $\log_9 1$

**B. Medio (Ecuaciones lineales)**
1. $\log_2(6x + 70) = 6$
2. $\log_5(12x + 5) = 3$
3. $\log_7(-x + 7) = \log_7(2x - 5)$
4. $\log_2(x + 5) + \log_2(2) = \log_2(5x - 3)$

**C. Avanzado (Exponenciales aplicadas a proyecciones en $USD)**
1. Un activo financiero quintuplica su valor cada dos periodos siguiendo la ecuación $5^{2x} = 13$. ¿En cuánto tiempo llegará a valer 13 veces su valor inicial?
2. Se comparan dos proyecciones de precios de acciones en $USD mediante la ecuación $4^{2x-3} = 7^x$. Resuelva para encontrar el punto de equilibrio $x$.
3. Si el precio de una criptomoneda se duplica periódicamente siguiendo la ecuación $2^x = 64$, ¿cuántos periodos deben pasar para alcanzar ese precio?
4. Un fondo de inversión de alto riesgo escala sus ganancias en base 10. Si la proyección sigue la ecuación $10^x = 10,000$, halle el tiempo $x$.

> [!success] Respuestas a los ejercicios
> **Bloque A:** 1) 1; 2) 1; 3) 4; 4) 0.
> **Bloque B:** 1) $x = -1$; 2) $x = 10$; 3) $x = 4$; 4) $x = 13/3$.
> **Bloque C:** 1) $x \approx 0.796$; 2) $x \approx 4.50$; 3) $x = 6$; 4) $x = 4$.

---

### 7. Autoevaluación y Cierre

> [!question] Pregunta 1
> Si encuentras la expresión $\log(100)$ sin base escrita, ¿cuál es el valor implícito de dicha base?
> A) 0
> B) 1
> C) 10

> [!question] Pregunta 2
> ¿Qué condición debe cumplir el argumento de un logaritmo tras verificar la solución de una ecuación?
> A) Debe ser igual a la base.
> B) Debe ser un número mayor a cero.
> C) Debe ser un número negativo.

> [!question] Pregunta 3
> Si al resolver una ecuación exponencial obtienes $x \approx 4.91$, ¿cuál es la interpretación correcta?
> A) El resultado es exacto y no requiere más decimales.
> B) Es un valor aproximado porque no se incluyeron todas las cifras de la calculadora.
> C) El logaritmo no se pudo resolver.

> [!tip] 💡 En la próxima clase
> Exploraremos cómo resolver ecuaciones logarítmicas más complejas, específicamente aquellos casos donde aparecen números "sueltos" (términos independientes sin logaritmo) dentro de la igualdad.

> [!info] 🧭 Navegación
> Siguiente: [[Clase 02]]