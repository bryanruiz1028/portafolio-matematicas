# Clase 06 — Gráfica de la Hipérbola desde su Ecuación General
tags: #algebra #grficadelahiprb
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 6 de 7

---

### 1. Cabecera de Navegación y Metadatos
← [[Clase 05 — Elementos de la Hipérbola]] | [[00 - Índice del curso]] | [[Clase 07 — Ecuaciones de las Asíntotas]] →

---

### 2. Importancia y Aplicaciones Reales

> [!info] 🌍 Relevancia y aplicaciones
> La hipérbola modela el comportamiento de objetos celestes que no regresan al sistema solar y es la base del sistema LORAN, un método de navegación que mide la diferencia de tiempo entre señales para ubicar barcos y aviones con total precisión.
> 
> - **💵 $USD:** Se utiliza para modelar curvas de costos y beneficios en mercados de alta competencia para hallar el punto exacto donde la producción es eficiente.
> - **🏗️ Práctica:** Las torres de enfriamiento de las plantas nucleares tienen forma de hiperboloide porque esta geometría permite usar menos material y soportar vientos extremos.
> - **📊 Cotidiana:** Si acercas una lámpara de noche a una pared, la luz que escapa por arriba y abajo dibuja dos curvas perfectas: las ramas de una hipérbola.

---

### 3. Concepto Clave y Pedagogía

> [!note] 📌 ¿Qué es Gráfica de la Hipérbola dada su ecuación general?
> Imagina que tienes una habitación llena de juguetes desordenados (Ecuación General: $Ax^2 + Cy^2 + Dx + Ey + F = 0$). Para jugar, primero debes ordenarlos en cajas (Forma Canónica). Al transformar la ecuación, "limpiamos" el desorden matemático para ver dónde está el centro $(h, k)$ y cuánto miden sus "brazos" ($a$ y $b$), permitiéndonos dibujar la hipérbola sin errores.

> [!warning] ⚠️ Error común
> **❌ Incorrecto:** Sumar al lado derecho únicamente el número que escribiste para completar el trinomio.
> **✅ Correcto:** Debes multiplicar ese número por el factor que sacaste fuera del paréntesis antes de sumarlo al otro lado. Por ejemplo, si pusiste un $+1$ dentro de un paréntesis que tiene un $-9$ afuera, lo que realmente estás agregando es $-9$.

> [!tip] 💡 Truco para recordarlo
> "La variable positiva manda el abrazo":
> - Si después de ordenar todo, la $x^2$ es positiva, la hipérbola abraza al eje X (abre a los lados).
> - Si la $y^2$ es positiva, la hipérbola abraza al eje Y (abre arriba y abajo).

---

### 4. Procedimiento Técnico Paso a Paso

```text
PASO 1 → Agrupar los términos con "x" y los términos con "y". El número que no tiene letra se pasa al otro lado de la igualdad con signo contrario.
PASO 2 → Sacar como factor común el número que acompaña a la x² y a la y². Luego, completar el trinomio cuadrado perfecto dividiendo el número junto a la x (o la y) entre 2 y elevando el resultado al cuadrado.
PASO 3 → Dividir toda la ecuación por el número resultante a la derecha para igualar a 1. ¡OJO!: Si el número a la derecha es negativo, al dividir, los signos de las fracciones se invertirán, cambiando la orientación de la hipérbola.
PASO 4 → Identificar los valores de "a", "b" y el centro (h,k). Dibujar el rectángulo guía y las asíntotas para trazar las ramas.
```

---

### 5. Desarrollo de Ejemplos (Casos de Estudio)

> [!example] Ejemplo 1: Caso Básico (Video 4)
> **Ecuación:** $x^2 + 6x - 4y^2 + 8y + 1 = 0$
> 1. **Agrupar:** $(x^2 + 6x) - 4(y^2 - 2y) = -1$
> 2. **Completar:** $(x^2 + 6x + 9) - 4(y^2 - 2y + 1) = -1 + 9 - 4$
> 3. **Simplificar:** $(x+3)^2 - 4(y-1)^2 = 4$
> 4. **Dividir entre 4:** **$\frac{(x+3)^2}{4} - \frac{(y-1)^2}{1} = 1$**

> [!example] Ejemplo 2: Manejo de Signos (Video 3)
> **Ecuación:** $12x^2 - 9y^2 - 18y - 117 = 0$
> 1. **Agrupar:** $12x^2 - 9(y^2 + 2y) = 117$
> 2. **Factorizar y completar:** $12x^2 - 9(y^2 + 2y + 1) = 117 - 9$ (notar que $-9 \cdot 1 = -9$)
> 3. **Dividir entre 108:** $\frac{12x^2}{108} - \frac{9(y+1)^2}{108} = 1$
> 4. **Resultado:** **$\frac{x^2}{9} - \frac{(y+1)^2}{12} = 1$**

> [!example] Ejemplo 3: Análisis Avanzado (Video 3)
> **Ecuación:** $-12x^2 + 8y^2 - 32y - 64 = 0$
> 1. **Proceso detallado:** 
>    - Agrupamos: $-12x^2 + 8(y^2 - 4y) = 64$
>    - Completamos trinomio en $y$: $-12x^2 + 8(y^2 - 4y + 4) = 64 + 32$ (porque $8 \cdot 4 = 32$)
>    - Obtenemos: $-12x^2 + 8(y-2)^2 = 96$
>    - Dividimos entre 96: $\frac{8(y-2)^2}{96} - \frac{12x^2}{96} = \frac{96}{96}$
>    - Simplificamos fracciones: **$\frac{(y-2)^2}{12} - \frac{x^2}{8} = 1$**
> 2. **Elementos:** Centro $(0, 2)$; $a = \sqrt{12} \approx 3.4$ (Vertical); $b = \sqrt{8} \approx 2.8$ (Horizontal).
> 3. **Gráfica:** $c = \sqrt{20} \approx 4.4$ y el Lado Recto $\approx 4.7$.

> [!example] Ejemplo 4: Aplicación Costos de Producción $USD (Video 4)
> **Problema:** Los costos de una empresa siguen la ecuación $-5x^2 - 10x + y^2 + 6y + 9 = 0$.
> 1. **Transformación:** Al completar cuadrados llegamos a $-5(x+1)^2 + (y+3)^2 = -5$.
> 2. **El "Giro":** Al dividir todo entre $-5$, los signos cambian:
>    $\frac{-5(x+1)^2}{-5} + \frac{(y+3)^2}{-5} = \frac{-5}{-5}$  $\rightarrow$ **$\frac{(x+1)^2}{1} - \frac{(y+3)^2}{5} = 1$**
> 3. **Puntos de interés:** Centro $(-1, -3)$. Al ser positiva la $x$, los vértices (límites de costo) están en **$V_1(-2, -3)$** y **$V_2(0, -3)$**.

---

### 6. Práctica Independiente

> [!abstract] Nivel Verde (Fácil)
> Dada la ecuación $\frac{(x+1)^2}{1} - \frac{(y+3)^2}{5} = 1$:
> 1. Identifica las coordenadas del centro $(h, k)$.
> 2. Determina los valores de $a^2$ y $b^2$.

> [!abstract] Nivel Amarillo (Medio)
> Convierte la siguiente ecuación general a su forma canónica:
> $x^2 + 6x - 4y^2 + 8y + 1 = 0$

> [!abstract] Nivel Rojo (Avanzado)
> En un modelo económico ($USD$), la curva de pérdida está definida por $12x^2 - 9y^2 - 18y - 117 = 0$. 
> 1. Encuentra la distancia focal ($c$). 
> 2. Determina las coordenadas de los vértices (puntos de equilibrio) para identificar los límites de producción en dólares.

> [!success] Respuestas exactas
> - **Verde:** Centro $(-1, -3)$; $a^2 = 1, b^2 = 5$.
> - **Amarillo:** $\frac{(x+3)^2}{4} - \frac{(y-1)^2}{1} = 1$.
> - **Rojo:** $c = \sqrt{21} \approx 4.58$. Vértices en $V_1(-3, -1)$ y $V_2(3, -1)$. La hipérbola es horizontal.

---

### 7. Evaluación y Cierre

> [!question] Pregunta 1
> En el ejemplo 3, ¿cuál es la distancia exacta desde el centro hasta uno de los focos? (Usa el valor de $c$ obtenido).

> [!question] Pregunta 2
> En el Ejemplo 4, ¿por qué la hipérbola terminó siendo horizontal si originalmente el término $y^2$ era positivo en la ecuación general?

> [!question] Pregunta 3
> Si un modelo de costos en $USD$ tiene un centro en $X = -1$ y se desplaza 3 unidades hacia la derecha para encontrar un foco, ¿en qué coordenada de $X$ se encuentra ese foco?

> [!tip] 💡 En la próxima clase
> Ya sabemos ubicar los puntos clave, pero para que la gráfica sea perfecta necesitamos las "paredes" invisibles que la hipérbola nunca toca: **Ecuaciones de las Asíntotas**.

---
← [[Clase 05 — Elementos de la Hipérbola]] | [[00 - Índice del curso]] | [[Clase 07 — Ecuaciones de las Asíntotas]] →