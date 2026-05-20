# Clase 01 — Trazado y elementos de la elipse: Ecuación canónica y ordinaria

> [!info] 🧭 Navegación
> [[Índice]] | [[Clase 02]]

---

> [!info] 🌍 Relevancia y aplicaciones
> La elipse es mucho más que un círculo "alargado". Es la curva que describe el baile de los planetas alrededor del Sol y la clave detrás de fenómenos acústicos sorprendentes.
> 
> - **💵 Aplicación con $USD:** Imagine que un paisajista debe presupuestar el césped para un jardín elíptico. Conociendo las dimensiones de sus semiejes, puede calcular el área y el perímetro aproximado. Un error en el cálculo de estos elementos podría significar una pérdida de cientos de **USD** en materiales mal cortados o sobrantes.
> - **🏗️ Aplicación práctica:** En ingeniería civil, los arcos elípticos en puentes permiten una distribución de fuerzas muy eficiente, además de ofrecer una estética elegante en comparación con los arcos circulares tradicionales.
> - **📊 Situación cotidiana:** ¿Has oído hablar de las "galerías de susurros"? Gracias a la forma elíptica de ciertas salas, si te paras en un punto específico (foco) y susurras, alguien en el otro extremo (segundo foco) te escuchará con total claridad, ya que las ondas sonoras rebotan y convergen precisamente allí.

---

> [!note] 📌 ¿Qué es Trazado y elementos de la elipse?
> Imagina que fijas dos puntillas en una tabla; estos puntos son los **focos**. Si atas una cuerda a ambas puntillas (dejando algo de holgura) y usas un lápiz para tensarla, al deslizarlo alrededor habrás dibujado una elipse. 
> 
> Técnicamente, la elipse es el lugar geométrico de todos los puntos donde la suma de las distancias a los dos focos es constante. Estas distancias desde cualquier punto de la curva a cada uno de los focos se denominan **radios vectores**.
> 
> > [!warning] ⚠️ Error común
> > Es vital no confundir el papel de $a$ y $b$. En la elipse, **$a$ siempre representa el número mayor**. Si ves un 49 y un 25 en los denominadores, $a^2$ será obligatoriamente 49.
> 
> > [!tip] 💡 Truco para recordarlo
> > "El denominador más grande manda en la **orientación del eje focal**". Si el número mayor está debajo de la $x$, la elipse se extiende horizontalmente. Si está debajo de la $y$, se extiende verticalmente.

---

### Procedimiento paso a paso para graficar

```text
PASO 1: Identificar el centro (h, k) extrayendo los valores de la ecuación 
        (cambiando sus signos). Definir 'a' como el semieje mayor (raíz del 
        denominador grande) y 'b' como el semieje menor (raíz del pequeño).
PASO 2: Determinar la orientación. Si a² está bajo 'x', el eje focal es 
        horizontal. Si a² está bajo 'y', el eje focal es vertical.
PASO 3: Calcular la distancia focal 'c' partiendo de la relación pitagórica: 
        a² = b² + c²  =>  c = √(a² - b²). 
        Calcular el Lado Recto (LR) con la fórmula: LR = (2b²) / a.
PASO 4: Ubicar el centro en el plano. Marcar los vértices y focos usando 'a' y 'c'. 
        Desde cada foco, contar LR/2 hacia cada lado para situar los extremos 
        del Lado Recto y trazar la curva con precisión.
```

---

### Ejemplos Prácticos

> [!example] Ejemplo 1: Caso Básico (Centro en el origen)
> **Ecuación:** $\frac{x^2}{25} + \frac{y^2}{16} = 1$
> - **Centro:** $(0, 0)$.
> - **Semiejes:** $a^2 = 25 \implies a = 5$ (semieje mayor); $b^2 = 16 \implies b = 4$ (semieje menor).
> - **Orientación:** Como el 25 está bajo $x$, la elipse es **horizontal**.
> - **Gráfico:** Desde el centro, contamos 5 unidades a los lados (eje $x$) y 4 unidades arriba y abajo (eje $y$).

> [!example] Ejemplo 2: Centro $(h, k)$
> **Ecuación:** $\frac{(x-5)^2}{25} + \frac{(y+4)^2}{4} = 1$
> - **Centro:** Respetando la forma $(x-h)^2$, cambiamos signos: $h = 5$, $k = -4$. Centro en $(5, -4)$.
> - **Semiejes:** $a = 5$ (bajo $x$), $b = 2$ (bajo $y$).
> - **Orientación:** **Horizontal** ($a$ domina en $x$).
> - **Nota:** Los vértices principales se ubican sumando y restando $a=5$ a la coordenada $x$ del centro.

> [!example] Ejemplo 3: Caso con Decimales (Orientación Vertical)
> **Ecuación:** $\frac{x^2}{32} + \frac{y^2}{64} = 1$
> - **Orientación:** **Vertical** (el denominador mayor, 64, está bajo $y$).
> - **Semiejes:** $a^2 = 64 \implies a = 8$; $b^2 = 32 \implies b = \sqrt{32} \approx 5.65$.
> - **Distancia Focal ($c$):** $a^2 = b^2 + c^2 \implies c = \sqrt{64 - 32} = \sqrt{32} \approx 5.65$.
> - **Lado Recto:** $LR = \frac{2(32)}{8} = 8$. (Se grafican 4 unidades a cada lado del foco).

> [!example] Ejemplo 4: Aplicación Presupuesto USD
> Se desea cercar un terreno elíptico definido por $\frac{x^2}{100} + \frac{y^2}{64} = 1$ (metros). El costo de la cerca es de **15.00 USD** por metro.
> 1. **Identificación:** $a = 10, b = 8$.
> 2. **Perímetro aproximado:** $P \approx \pi(a + b) = 3.14 \times (10 + 8) = 56.52$ metros.
> 3. **Costo total:** $56.52 \times 15.00 \text{ USD} = 847.80 \text{ USD}$.

---

### Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Fácil: Identificación inicial
> Identifique centro, semieje mayor ($a$) y semieje menor ($b$) de:
> 1. $\frac{x^2}{100} + \frac{y^2}{36} = 1$
> 2. $\frac{x^2}{4} + \frac{y^2}{9} = 1$
> 3. $\frac{x^2}{49} + \frac{y^2}{25} = 1$
> 4. $\frac{x^2}{16} + \frac{y^2}{64} = 1$

> [!abstract] 🟡 Nivel Medio: Elementos completos
> Halle centro, vértices y focos (use aproximación decimal donde sea necesario):
> 1. $\frac{(x-3)^2}{64} + \frac{(y+7)^2}{9} = 1$
> 2. $\frac{(x+3)^2}{1} + \frac{(y-1)^2}{32} = 1$
> 3. $\frac{(x-2)^2}{16} + \frac{y^2}{25} = 1$
> 4. $\frac{x^2}{49} + \frac{(y-5)^2}{25} = 1$

> [!abstract] 🔴 Nivel Avanzado: Diseño y presupuesto
> El marco de una ventana elíptica sigue la ecuación $\frac{(x-10)^2}{25} + \frac{(y-12)^2}{16} = 1$ (en metros). Si el material del marco cuesta **45.00 USD** por metro lineal, ¿cuál es el presupuesto estimado del proyecto? (Use $P \approx \pi(a+b)$).

> [!success] Solucionario para el Docente
> **Fácil:** 1. $C(0,0), a=10, b=6$. 2. $C(0,0), a=3, b=2$. 3. $C(0,0), a=7, b=5$. 4. $C(0,0), a=8, b=4$.
> **Medio:** 
> 1. $C(3,-7), a=8, b=3, c=\sqrt{55} \approx 7.41$. 
> 2. $C(-3,1), a=\sqrt{32} \approx 5.65, b=1, c=\sqrt{31} \approx 5.56$. 
> 3. $C(2,0), a=5, b=4, c=3$. 
> 4. $C(0,5), a=7, b=5, c=\sqrt{24} \approx 4.89$.
> **Avanzado:** $a=5, b=4$. $P \approx 3.14 \times 9 = 28.26 \text{ m}$. Costo: $28.26 \times 45.00 = 1,271.70 \text{ USD}$.

---

### Autoevaluación

> [!question] 🧪 Pregunta 1
> En la definición de la elipse, ¿cómo se llaman los segmentos cuya suma de longitudes es constante para cualquier punto de la curva?
> - A) Ejes focales.
> - B) Radios vectores.
> - C) Lados rectos.

> [!question] 🧪 Pregunta 2
> Aplicando la relación pitagórica $a^2 = b^2 + c^2$, si una elipse tiene $a = 13$ y $b = 5$, ¿cuál es su distancia focal $c$?
> - A) 8
> - B) 12
> - C) 18

> [!question] 🧪 Pregunta 3
> Si una mesa elíptica tiene $a=2$ y $b=1$ (metros), y el acabado del borde cuesta **20.00 USD** el metro, ¿cuál es el costo aproximado ($\approx$)?
> - A) 188.40 USD
> - B) 125.60 USD
> - C) 62.80 USD

---

> [!tip] 💡 En la próxima clase
> Veremos cómo transformar una **Ecuación General** de la elipse (aquella igualada a cero) a su **Forma Canónica** mediante el método de completar cuadrados para poder graficarla fácilmente.

> [!info] 🧭 Navegación
> [[Índice]] | [[Clase 02]]