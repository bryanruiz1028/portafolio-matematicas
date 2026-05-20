# Clase 02 — Gráfica de la Hipérbola dada su ecuación ordinaria con centro en $(h,k)$

#algebra #graphofthehyper
**Curso:** Geometría Analítica Aplicada
**Nivel:** Secundaria / Bachillerato

> [!info] 🧭 Navegación
> - [[Clase 01 — Introducción y Centro en el Origen]]
> - [[Índice General del Curso]]
> - [[Clase 03 — Ecuaciones de las Asíntotas]]

---

## 1. Importancia de las Hipérbolas con Centro $(h,k)$

El estudio de hipérbolas con centro desplazado del origen $(h,k)$ es fundamental porque, en la práctica, los fenómenos físicos y económicos rara vez ocurren partiendo de un punto cero absoluto. Entender el desplazamiento nos permite ubicar modelos matemáticos con precisión en cualquier coordenada del plano cartesiano.

**Aplicaciones del modelo:**
*   **💵 Modelos Económicos:** Se utilizan para representar curvas de oferta y demanda, así como funciones de costos marginales donde el punto de equilibrio se desplaza según la inversión inicial o costos fijos.
*   **🏗️ Arquitectura:** Esencial para el diseño de estructuras hiperboloides, como torres de enfriamiento de plantas de energía, donde la base no coincide necesariamente con el origen de las coordenadas del terreno.
*   **📊 Trayectorias y Navegación:** Es la base de los sistemas LORAN para la navegación marítima y aérea, permitiendo calcular la posición exacta mediante la intersección de hipérbolas con focos en distintas estaciones terrestres.

---

## 2. Concepto Clave

**Explicación para principiantes:**
Imagina que dibujas una hipérbola perfecta centrada en el origen $(0,0)$ de tu cuaderno. Ahora, sin girarla ni cambiar su forma, "desliza" el dibujo completo hacia una nueva posición. Ese nuevo punto central es el centro $(h,k)$. La hipérbola mantiene su apertura y propiedades, pero ahora sus coordenadas están "mudadas" a un nuevo vecindario en el plano.

> [!warning] Error Común: La "Trampa" de los Signos
> Al extraer las coordenadas del centro $(h, k)$ de la ecuación ordinaria, **siempre debes cambiar el signo** de los números que ves. 
> - Si ves $(x - 5)$, la coordenada $h$ es $5$ positivo.
> - Si ves $(y + 2)$, la coordenada $k$ es $2$ negativo.
> - **El centro es $(5, -2)$.**

**💡 Truco de Orientación:**
Para saber si tu hipérbola se abre hacia los lados (horizontal) o hacia arriba y abajo (vertical), observa cuál de las dos fracciones es la **positiva** (la que no tiene el signo menos delante):
*   Si la fracción con **$x$** es positiva: La hipérbola es **horizontal** (paralela al eje $x$).
*   Si la fracción con **$y$** es positiva: La hipérbola es **vertical** (paralela al eje $y$).

---

## 3. Procedimiento Paso a Paso

Para graficar con precisión técnica, sigue estos pasos derivados de la metodología del Profe Alex:

```text
PASO 1: Identificar el centro (h, k) extrayendo los valores junto a 'x' 
        y 'y', invirtiendo sus signos.
PASO 2: Determinar la orientación (viendo qué fracción es positiva) y 
        obtener 'a' y 'b' calculando la raíz cuadrada de los denominadores.
PASO 3: Calcular 'c' (distancia focal) mediante Pitágoras c = √(a² + b²) 
        y la longitud del Lado Recto (LR = 2b² / a).
PASO 4: Construir la gráfica:
        • Ubicar el centro (h, k).
        • Trazar el "Rectángulo Auxiliar" delimitado por los puntos 
          (h ± a, k ± b).
        • Dibujar las asíntotas cruzando las esquinas de dicho rectángulo.
        • Trazar las ramas de la hipérbola pasando por los vértices y 
          guiándose por los extremos del Lado Recto.
```

---

## 4. Ejemplos Resueltos

> [!example] Ejemplo 1: Caso Básico (Horizontal)
> **Ecuación:** $\frac{(x-5)^2}{25} - \frac{(y+2)^2}{16} = 1$
> 1.  **Centro:** Cambiamos signos $\rightarrow$ $C(5, -2)$.
> 2.  **Orientación:** $x$ es positiva $\rightarrow$ Horizontal.
> 3.  **Valores:** $a^2=25 \Rightarrow a=5$; $b^2=16 \Rightarrow b=4$.
> 4.  **Cálculos:** $c = \sqrt{25+16} = \sqrt{41} \approx 6.4$.
> 5.  **Lado Recto:** $LR = \frac{2(16)}{5} = 6.4$.
> *Nota:* Se cuentan $5$ unidades a la derecha e izquierda del centro para los vértices.

> [!example] Ejemplo 2: Caso Vertical
> **Ecuación:** $\frac{(y+2)^2}{9} - \frac{(x-4)^2}{25} = 1$
> 1.  **Centro:** Ojo al orden $(x, y) \rightarrow$ $C(4, -2)$.
> 2.  **Orientación:** $y$ es positiva $\rightarrow$ Vertical.
> 3.  **Valores:** $a^2=9 \Rightarrow a=3$; $b^2=25 \Rightarrow b=5$.
> 4.  **Cálculos:** $c = \sqrt{9+25} = \sqrt{34} \approx 5.8$.
> 5.  **Lado Recto:** $LR = \frac{2(25)}{3} \approx 16.6$.
> *Técnica:* Al ser vertical, el valor de $a$ se cuenta hacia arriba y abajo del centro para hallar los vértices.

> [!example] Ejemplo 3: Raíces no exactas (Rigor Técnico)
> **Ecuación:** $\frac{x^2}{20} - \frac{(y-6)^2}{14} = 1$
> 1.  **Centro:** $x$ no tiene acompañante $\rightarrow$ $C(0, 6)$.
> 2.  **Orientación:** Horizontal ($x$ positiva).
> 3.  **Valores:** $a = \sqrt{20} \approx 4.47$; $b = \sqrt{14} \approx 3.74$.
> 4.  **Cálculos:** $c = \sqrt{20+14} = \sqrt{34} \approx 5.83$.
> 5.  **Lado Recto:** $LR = \frac{2(14)}{4.47} \approx 6.26$.

> [!example] Ejemplo 4: Aplicación Financiera ($USD)
> Una empresa modela su retorno de inversión donde $x$ es la inversión en publicidad y $y$ es el beneficio (en miles de USD) mediante: $\frac{(y-1)^2}{10} - \frac{x^2}{13} = 1$.
> *   **Lógica:** Como la hipérbola es vertical y abre hacia arriba (fracción $y$ positiva), el vértice superior representa el **umbral mínimo de retorno**.
> *   **Centro:** $(0, 1)$.
> *   **Vértice superior:** $k + a = 1 + \sqrt{10} \approx 1 + 3.16 = 4.16$.
> *   **Resultado:** El retorno mínimo esperado es de $4,160$ USD. Bajo este punto, el modelo no predice beneficios según esta trayectoria.

---

## 5. Ejercicios para el Estudiante

### Nivel Fácil
1.  Grafique $\frac{(x-3)^2}{16} - \frac{(y-1)^2}{9} = 1$. Identifique centro y valores de $a, b$.
2.  Indique la orientación y el centro de $\frac{(y-2)^2}{4} - \frac{(x+4)^2}{16} = 1$.
3.  Halle el centro de $\frac{(x+5)^2}{36} - \frac{(y+5)^2}{25} = 1$.
4.  Determine el valor exacto de $a$ para $\frac{(x-1)^2}{49} - \frac{y^2}{64} = 1$.

### Nivel Medio
5.  Dada $\frac{(y+1)^2}{16} - \frac{(x-3)^2}{9} = 1$, calcule el Lado Recto y grafique.
6.  Halle las coordenadas de los focos para $\frac{(x+2)^2}{25} - \frac{(y-4)^2}{16} = 1$.
7.  Identifique todos los elementos (centro, vértices y focos) de $\frac{y^2}{9} - \frac{(x-2)^2}{16} = 1$.
8.  Calcule el valor de $c$ y grafique $\frac{(x-4)^2}{16} - \frac{(y+2)^2}{25} = 1$.

### Nivel Avanzado
9.  Grafique la hipérbola $\frac{x^2}{20} - \frac{(y-6)^2}{14} = 1$ usando dos decimales de precisión.
10. Aproxime los elementos de $\frac{(y-3)^2}{10} - \frac{x^2}{13} = 1$ y grafique sus asíntotas.
11. Realice el análisis completo (centro, $a, b, c, LR$) de $\frac{(y+2)^2}{9} - \frac{(x-4)^2}{25} = 1$.
12. **Optimización financiera ($USD):** Un costo de producción industrial sigue la trayectoria $\frac{(x-10)^2}{100} - \frac{(y-50)^2}{64} = 1$, donde $y$ es el costo en USD y $x$ las unidades producidas. Grafique la curva y determine el "costo base" (vértice más cercano al centro) cuando la producción se aleja del punto de equilibrio.

---

## 6. Respuestas y Autoevaluación

> [!success] Clave de Respuestas
> 1. $C(3, 1), a=4, b=3$.
> 2. Vertical, $C(-4, 2)$.
> 5. $LR = 4.5$.
> 6. $c \approx 6.4$. Focos en $(-2 \pm 6.4, 4) \rightarrow F_1(-8.4, 4), F_2(4.4, 4)$.
> 12. **Análisis USD:** El centro es $(10, 50)$. Al ser una hipérbola horizontal ($x$ positiva), los vértices están en $h \pm a$. Como $a=10$, los vértices están en $x=0$ y $x=20$. En estos puntos, el costo $y$ es exactamente $50$ USD. Este es el **costo base de operación** antes de que la curva de gasto hiperbólico se dispare.

### Mini-Prueba de Autoevaluación
1.  **¿Qué determina que una hipérbola sea vertical?**
    *   a) Que el denominador $a^2$ sea mayor que $b^2$.
    *   b) Que la fracción con la variable $y$ sea la positiva.
    *   c) Que el centro $(h, k)$ tenga un valor de $k$ mayor a $h$.
2.  **Si la ecuación es $\frac{(x-h)^2}{a^2} - \frac{(y-k)^2}{b^2} = 1$, ¿qué fórmula define la longitud de la "ventana" por donde pasan las ramas (Lado Recto)?**
    *   a) $2c$
    *   b) $\sqrt{a^2 + b^2}$
    *   c) $2b^2 / a$
3.  **En un modelo de costos vertical con centro $(0, 100)$ y $a=20$, ¿cuál es el costo mínimo representado por el vértice superior?**
    *   a) $80$ USD
    *   b) $120$ USD
    *   c) $100$ USD

---

> [!tip] Notas para el próximo tema
> En la **Clase 03** profundizaremos en las **ecuaciones de las asíntotas**. Aunque hoy las trazamos de forma visual usando el rectángulo auxiliar, aprenderemos la fórmula matemática para definirlas como funciones lineales exactas $y - k = \pm \frac{b}{a}(x - h)$.

> [!info] 🧭 Navegación
> - [[Clase 01 — Introducción y Centro en el Origen]]
> - [[Índice General del Curso]]
> - [[Clase 03 — Ecuaciones de las Asíntotas]]