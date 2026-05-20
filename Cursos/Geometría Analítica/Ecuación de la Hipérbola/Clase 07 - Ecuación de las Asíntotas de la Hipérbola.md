# Clase 07 — Ecuación de las Asíntotas de la Hipérbola
#algebra #equationoftheas

Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 7 de 7

> [!info] 🧭 Navegación
> [[Clase 06 — Elementos de la Hipérbola|« Clase Anterior]] | [[00 - Índice del curso|Índice]] | Clase Siguiente »

---

## 1. ¿Por qué es importante esta clase?
Las asíntotas son las "guías" invisibles que definen la apertura de la hipérbola. Sin ellas, sería imposible trazar la curva con precisión, ya que determinan hacia dónde se extienden las ramas en el infinito.

*   **💵 Aplicación financiera:** En proyecciones de inversión, las asíntotas representan los límites críticos o "techos" de rentabilidad y los niveles de riesgo donde los beneficios tienden a estabilizarse.
*   **🏗️ Aplicación práctica:** En ingeniería y arquitectura, se utilizan para diseñar estructuras hiperboloides (como torres de enfriamiento), asegurando que las líneas de tensión sigan trayectorias lineales eficientes.
*   **📊 Situación cotidiana:** Permiten modelar fenómenos donde una variable se acerca a un valor límite sin tocarlo nunca, como la velocidad de escape orbital o la saturación de un mercado.

---

## 2. Concepto clave

> [!note] 📌 ¿Qué es la Ecuación de las Asíntotas?
> Las asíntotas son dos líneas rectas que se cruzan exactamente en el centro $(h, k)$ de la hipérbola. Para definirlas, utilizamos dos medidas fundamentales extraídas de los denominadores de la ecuación canónica:
> *   **Distancia vertical ($\Delta y$):** Es la raíz cuadrada del denominador bajo la variable $y$.
> *   **Distancia horizontal ($\Delta x$):** Es la raíz cuadrada del denominador bajo la variable $x$.
>
> La pendiente ($m$) de estas rectas siempre estará dada por la relación entre estas dos distancias.

> [!warning] ⚠️ Error común
> Un error muy frecuente es creer que la pendiente siempre se forma con el primer denominador que vemos. **¡No es así!** La pendiente siempre sigue el orden del eje vertical sobre el horizontal: $m = \frac{\Delta y}{\Delta x}$. Siempre verifica cuál es el número que está "bajo la $y$" para colocarlo en el numerador.

> [!tip] 💡 Truco para recordarlo
> Piensa en el concepto de **Rise/Run** (Subida/Avance). La pendiente de cualquier recta es cuánto sube ($y$) dividido por cuánto avanza ($x$). Por lo tanto, el valor asociado a $y$ siempre será el numerador de tu pendiente.

---

## 3. Procedimientos paso a paso

### MÉTODO 1 (Punto-Pendiente)
Este método es el más riguroso y utiliza la base conceptual de la ecuación de la recta: $y - y_1 = m(x - x_1)$.

1.  **Identificar el centro $(h, k)$:** Extrae los valores de la ecuación canónica (recordando cambiarles el signo).
2.  **Calcular $\Delta y$ y $\Delta x$:** Obtén las raíces cuadradas de los denominadores.
3.  **Aplicar la fórmula puente:** Sustituye los valores en la estructura:
    $$y - k = \pm \left( \frac{\Delta y}{\Delta x} \right)(x - h)$$
4.  **Despejar $y$:** Distribuye la fracción en el paréntesis, mueve el valor de $k$ al otro lado y simplifica para llegar a la forma $y = mx + b$.

### MÉTODO 2 (Igualar a Cero)
> [!important] 🎓 Nota didáctica
> Como bien señala el Profe Alex, este no es un principio algebraico formal de la hipérbola, sino un **algoritmo procedimental o "truco" matemático** efectivo para llegar al mismo resultado sin memorizar la fórmula de la recta.

1.  **Sustituir por Cero:** En la ecuación canónica, reemplaza el $1$ por un $0$.
2.  **Transponer la fracción:** Pasa el término que tiene el signo negativo al otro lado de la igualdad para que ambos queden positivos.
3.  **Extraer raíces:** Aplica raíz cuadrada a ambos lados para eliminar los cuadrados. **Recuerda añadir el $\pm$** en uno de los lados (preferiblemente donde está la $x$) para obtener las dos rectas.
4.  **Despejar $y$:** Realiza el despeje final para obtener ambas ecuaciones lineales.

---

## 4. Ejemplos desarrollados

````ad-example
**Ejemplo 1: Método 1 (Centro $0,0$)**
**Ecuación:** $\frac{y^2}{9} - \frac{x^2}{4} = 1$
1. Centro: $(0, 0)$.
2. $\Delta y = \sqrt{9} = 3$ | $\Delta x = \sqrt{4} = 2$.
3. Como el centro es el origen, la fórmula se simplifica a $y = \pm \left( \frac{\Delta y}{\Delta x} \right)x$.
**Resultado:** $y = \frac{3}{2}x$ y $y = -\frac{3}{2}x$.
````

````ad-example
**Ejemplo 2: Método 1 (Centro $h, k$)**
**Ecuación:** $\frac{(x-5)^2}{25} - \frac{(y+2)^2}{16} = 1$
1. Centro: $(5, -2)$.
2. $\Delta y = \sqrt{16} = 4$ | $\Delta x = \sqrt{25} = 5$.
3. Sustitución en punto-pendiente: $y - (-2) = \pm \frac{4}{5}(x - 5) \implies y + 2 = \pm 0.8(x - 5)$.
4. **Asíntota positiva:** $y + 2 = 0.8x - 4 \implies y = 0.8x - 6$.
5. **Asíntota negativa:** $y + 2 = -0.8x + 4 \implies y = -0.8x + 2$.
````

````ad-example
**Ejemplo 3: Método 2 (Igualar a cero)**
**Ecuación:** $\frac{x^2}{9} - \frac{y^2}{4} = 1$
1. Igualar a cero: $\frac{x^2}{9} - \frac{y^2}{4} = 0 \implies \frac{x^2}{9} = \frac{y^2}{4}$.
2. Raíces cuadradas: $\sqrt{\frac{x^2}{9}} = \sqrt{\frac{y^2}{4}} \implies \pm \frac{x}{3} = \frac{y}{2}$.
3. Despejar $y$: $y = \pm \frac{2}{3}x$.
````

````ad-example
**Ejemplo 4: Aplicación Real ($USD)**
Un analista de riesgos modela el beneficio proyectado ($y$ en millones de $USD) frente al capital de inversión expuesto ($x$ en millones de $USD) mediante la ecuación del Ejemplo 2. ¿Cuál es el límite de tendencia del beneficio si el capital aumenta indefinidamente?
*   **Solución:** Las asíntotas representan las líneas de tendencia de este modelo. Según el cálculo anterior, el beneficio se estabilizará siguiendo las trayectorias de $y = 0.8x - 6$ y $y = -0.8x + 2$. El valor $m = 0.8$ indica que por cada millón de capital extra en riesgo, el techo de beneficio potencial crece $0.8$ millones.
````

---

## 5. Ejercicios para el estudiante

````ad-abstract
**🟢 Nivel Fácil: Conceptos básicos**
Halla las ecuaciones de las asíntotas para las siguientes hipérbolas con centro en el origen:
1. $\frac{x^2}{25} - \frac{y^2}{4} = 1$
2. $\frac{y^2}{16} - \frac{x^2}{9} = 1$
````

````ad-abstract
**🟡 Nivel Medio: Centro desplazado y raíces**
1. Determina las asíntotas de: $\frac{(x+3)^2}{16} - \frac{(y-1)^2}{9} = 1$.
2. Calcula la pendiente de las asíntotas de una hipérbola vertical donde la distancia vertical es $\Delta y = 7$ y la distancia horizontal es $\Delta x = \sqrt{30}$.
````

````ad-abstract
**🔴 Nivel Avanzado: Aplicación USD**
Una empresa de tecnología financiera modela su curva de oferta donde el precio de mercado tiende a un límite. Si la ecuación de la curva es una hipérbola con centro $(0,0)$, un denominador bajo $y$ de $49$ y un denominador bajo $x$ de $30$:
- Determina la pendiente del precio límite (asíntota) en $USD.
- Expresa la ecuación de la tendencia positiva.
````

````ad-success
**Soluciones**
*   **Fácil 1:** $y = \pm 0.4x$ (o $\pm \frac{2}{5}x$)
*   **Fácil 2:** $y = \pm 1.33x$ (o $\pm \frac{4}{3}x$)
*   **Medio 1:** $y = 0.75x + 3.25$ y $y = -0.75x - 1.25$
*   **Medio 2:** $m \approx \pm 1.29$ (Calculado como $7 / \sqrt{30}$)
*   **Avanzado:** La pendiente es $m = \frac{7}{\sqrt{30}} \approx 1.29$. La tendencia positiva es $y = 1.29x$.
````

---

## 6. Evaluación y Cierre

````ad-question
**Pregunta 1**
¿Qué punto geométrico es común a ambas asíntotas sin importar la orientación de la hipérbola?
*   *Respuesta:* El **centro $(h, k)$** de la hipérbola; es el único punto donde las dos rectas se intersecan.
````

````ad-question
**Pregunta 2**
Si conoces la pendiente de una asíntota, ¿cómo obtienes automáticamente la de la otra?
*   *Respuesta:* Simplemente **cambiando el signo**. Si una es $m$, la otra es $-m$, pues tienen inclinaciones simétricas respecto al eje.
````

````ad-question
**Pregunta 3**
En un modelo financiero, si la "Distancia en $y$" ($\Delta y$) aumenta mientras la "Distancia en $x$" ($\Delta x$) se mantiene igual, ¿qué ocurre con el límite de beneficios?
*   *Respuesta:* La pendiente de la asíntota se vuelve **más pronunciada** (mayor inclinación), lo que indica un crecimiento del límite más acelerado por cada unidad de $x$.
````

> [!tip] 💡 En la próxima clase
> ¡Felicidades! Has completado el estudio detallado de la hipérbola. Con esto, cerramos el bloque de secciones cónicas individuales. En la próxima sesión, aprenderemos a identificar cualquier cónica (círculo, elipse, parábola o hipérbola) analizando simplemente su ecuación general.

---
> [!info] 🧭 Navegación
> [[Clase 06 — Elementos de la Hipérbola|« Clase Anterior]] | [[00 - Índice del curso|Índice]] | Clase Siguiente »