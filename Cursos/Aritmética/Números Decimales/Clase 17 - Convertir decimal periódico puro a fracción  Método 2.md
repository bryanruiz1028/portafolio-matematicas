# Clase 17 — Convertir decimal periódico puro a fracción | Método 2

#algebra #convertirdecimal
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 17 de 22

> [!info] 🧭 Navegación
> - Anterior: [[Clase 16 — Convertir decimal exacto a fracción]]
> - Siguiente: [[Clase 18 — Convertir decimal periódico mixto a fracción]]

---

> [!info] 🌍 Relevancia y aplicaciones
> La conversión de decimales infinitos en fracciones no es solo un ejercicio teórico; es la única forma de garantizar la **precisión absoluta** en el cálculo. El redondeo prematuro es el enemigo de la exactitud.
> 
> - **Reparto de divisas ($USD):** Si intentas repartir $1$ USD entre tres personas usando decimales exactos ($0.33$ por persona), siempre perderás un centavo en el camino ($0.99$). Usar la fracción $1/3$ garantiza que el valor total se mantenga íntegro.
> - **Ingeniería de alta precisión:** En la fabricación de piezas, usar $0.33$ m en lugar de $1/3$ de metro genera un error de $3.3$ mm. En un motor o una estructura de soporte, este desfase puede causar fallos catastróficos.
> - **Proporciones en construcción:** Al mezclar materiales en proporciones exactas (como $1/9$ de aditivo), convertir el decimal periódico a fracción permite medir volúmenes reales sin dejar residuos acumulativos en grandes obras.

---

### Concepto clave

> [!note] 📌 ¿Qué es convertir decimal periódico puro a fracción?
> Un decimal periódico puro es aquel donde el **periodo** (la cifra o grupo de cifras que se repiten infinitamente) comienza inmediatamente después de la coma decimal. En matemáticas, representamos esta repetición con una barra o vínculo sobre las cifras: $0.\bar{3}$ o $1.\overline{36}$. El objetivo es encontrar la fracción irreducible $\frac{a}{b}$ que genera exactamente ese número infinito.

> [!warning] ⚠️ Error común
> Un error muy frecuente entre estudiantes es tratar un decimal periódico como si fuera exacto. Por ejemplo, afirmar que $0.\bar{3} = \frac{3}{10}$. 
> **Recuerda:** $\frac{3}{10}$ es exactamente $0.3$. Para representar el infinito $0.333...$ necesitamos el denominador $9$, es decir, $\frac{3}{9} = \frac{1}{3}$.

> [!tip] 💡 Truco para recordarlo
> La clave está en los **"Nueves"**: El denominador de tu fracción tendrá tantos nueves como cifras tenga el periodo. 
> - Si el periodo es de 1 cifra (ej. $0.\bar{5}$), el denominador es $9$.
> - Si el periodo es de 2 cifras (ej. $0.\overline{45}$), el denominador es $99$.

---

### Procedimiento paso a paso (Método Algebraico)

Este método se basa en crear una igualdad para "neutralizar" la parte infinita mediante una resta.

```text
PASO 1: Definir la ecuación igualando el decimal a "x" (x = 0.333...).
PASO 2: Multiplicar toda la ecuación por una potencia de 10 (10, 100, 1000...) 
        según la cantidad de cifras del periodo para desplazar la coma.
PASO 3: Restar la primera ecuación a la segunda. El "Eureka" ocurre aquí: 
        al estar alineadas, las partes infinitas se restan y dan cero.
PASO 4: Despejar "x" y simplificar la fracción resultante.
```

---

### Ejemplos Prácticos

> [!example] Ejemplo 1: Caso Básico ($0.\bar{3}$)
> 1. **Igualar:** $x = 0.333...$
> 2. **Multiplicar:** El periodo tiene 1 cifra, multiplicamos por $10^1 = 10$.
>    $$10x = 3.333...$$
> 3. **Restar (Alineación):** 
>    $$\begin{aligned} 10x &= 3.333... \\ -x &= 0.333... \\ \hline 9x &= 3.0 \end{aligned}$$
>    *(Note cómo la parte periódica desaparece por completo).*
> 4. **Despejar:** $x = \frac{3}{9}$. Simplificando entre 3: **$\frac{1}{3}$**.

> [!example] Ejemplo 2: Manejo de Signos ($-0.\bar{6}$)
> **¡Atención!** El signo no desaparece, se reserva para el final. Trabajamos con el valor absoluto:
> 1. Proceso para $0.\bar{6}$:
>    $10x = 6.666...$
>    $10x - x = 6 \rightarrow 9x = 6$
> 2. **Simplificar:** $x = \frac{6}{9} = \frac{2}{3}$.
> 3. **Resultado:** Aplicamos el signo original: **$-\frac{2}{3}$**.

> [!example] Ejemplo 3: Avanzado con parte entera ($1.\overline{36}$)
> 1. **Igualar:** $x = 1.3636...$
> 2. **Multiplicar:** Periodo de 2 cifras ($36$), multiplicamos por $100$.
>    $$100x = 136.3636...$$
> 3. **Restar:**
>    $$\begin{aligned} 100x &= 136.3636... \\ -x &= 1.3636... \\ \hline 99x &= 135 \end{aligned}$$
> 4. **Simplificación paso a paso:**
>    $x = \frac{135}{99} \xrightarrow{\div 3} \frac{45}{33} \xrightarrow{\div 3} \mathbf{\frac{15}{11}}$

> [!example] Ejemplo 4: Aplicación Bancaria ($0.\overline{90}$ USD)
> Convertir un precio de $0.9090...$ USD a su valor exacto:
> 1. $x = 0.\overline{90} \rightarrow 100x = 90.\overline{90}$
> 2. Resta: $100x - x = 90.\overline{90} - 0.\overline{90} \rightarrow 99x = 90$
> 3. $x = \frac{90}{99}$. Dividiendo ambos entre $9$: **$\frac{10}{11}$** de dólar.

---

### Ejercicios para el estudiante

> [!abstract] Nivel Fácil (Verde)
> Convierte a fracción (periodo de una cifra):
> 1. $0.\bar{5}$
> 2. $0.\bar{2}$
> 3. $0.\bar{7}$
> 4. $0.\bar{4}$

> [!abstract] Nivel Medio (Amarillo)
> Considera la parte entera y periodos de dos cifras:
> 1. $1.\bar{2}$
> 2. $0.\overline{45}$
> 3. $2.\overline{15}$
> 4. $0.\overline{12}$

> [!abstract] Nivel Avanzado: Aplicación USD (Rojo)
> 1. Un dulce cuesta $0.\overline{33}$ USD, ¿qué fracción de dólar representa?
> 2. Un componente electrónico cuesta $0.\overline{09}$ USD, ¿cuál es su valor fraccionario?
> 3. Una criptomoneda sube $1.\bar{6}$ USD, exprésalo como fracción.
> 4. El costo de un servicio es de $0.\overline{18}$ USD, exprésalo como fracción simplificada.

> [!success] Respuestas y Procedimientos
> **Fácil:** 1) $5/9$, 2) $2/9$, 3) $7/9$, 4) $4/9$.
> **Medio:** 
> 1) $11/9$ (de $\frac{12-1}{9}$), 2) $5/11$ (de $\frac{45}{99}$), 3) $71/33$ (de $\frac{213}{99}$), 4) $4/33$ (de $\frac{12}{99}$).
> **Avanzado:** 
> 1) $1/3$ USD (de $\frac{33}{99}$), 2) $1/11$ USD (de $\frac{9}{99}$), 3) $5/3$ USD (de $\frac{15}{9}$), 4) $2/11$ USD (de $\frac{18}{99}$).

---

### Mini-prueba de autoevaluación

> [!question] Pregunta 1
> Si el periodo de un decimal tiene 3 cifras (ej. $0.\overline{123}$), ¿por qué potencia de 10 se debe multiplicar la ecuación y por qué?
> > [!success] Respuesta
> > Se multiplica por **1000**. Esto es necesario para desplazar la coma tres lugares, asegurando que la parte decimal infinita en la segunda ecuación sea idéntica a la original, permitiendo que se cancelen al restar.

> [!question] Pregunta 2
> Realiza mentalmente: ¿A qué fracción equivale $0.\bar{1}$?
> > [!success] Respuesta
> > **$1/9$**. Aplicando el método: $9x = 1$, por lo tanto $x = 1/9$.

> [!question] Pregunta 3
> Un activo financiero cotiza a $0.\overline{72}$ USD. ¿Cuál es su equivalente más simplificado?
> a) $72/100$
> b) $8/11$
> c) $72/90$
> > [!success] Respuesta
> > **b) $8/11$**. El planteamiento es $99x = 72$. La fracción $\frac{72}{99}$ se simplifica dividiendo ambos términos entre $9$, resultando en $\frac{8}{11}$.

---

> [!tip] 💡 En la próxima clase
> Ya dominas el caso donde el periodo empieza justo tras la coma. En la siguiente lección enfrentaremos los **decimales periódicos mixtos**, donde existe un "intruso" (anteperiodo) entre la coma y el periodo.

> [!info] 🧭 Navegación
> - Anterior: [[Clase 16 — Convertir decimal exacto a fracción]]
> - Siguiente: [[Clase 18 — Convertir decimal periódico mixto a fracción]]