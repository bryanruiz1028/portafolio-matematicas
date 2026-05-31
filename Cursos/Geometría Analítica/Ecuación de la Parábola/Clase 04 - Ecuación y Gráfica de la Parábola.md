# Clase 04 — Ecuación y Gráfica de la Parábola

`#algebra` `#geometriaanalitica`

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 4 de 9

> [!info] 🧭 Navegación
> [[Clase 03]] | **Índice** | **Clase 04** | [[Clase 05]]

> [!info] 🌍 Relevancia y aplicaciones
> La parábola es una de las curvas más poderosas en la ingeniería y la física debido a su propiedad reflexiva: todo lo que choca contra ella en paralelo se dirige hacia un único punto llamado **foco**.
> 
> *   💵 **$USD Aplicación:** El análisis de costos en la fabricación de antenas y reflectores depende de la precisión de la curvatura para optimizar el uso de materiales costosos.
> *   🏗️ **Práctica:** Los puentes colgantes utilizan cables en forma de parábola para distribuir el peso de la plataforma de manera uniforme.
> *   📊 **Vida Diaria:** Se encuentra en los faros de los autos, antenas de televisión satelital y en la trayectoria de un balón de fútbol.

---

> [!note] 📌 ¿Qué es la parábola y sus elementos?
> Para entenderla fácilmente, imagina que la parábola es una curva en forma de "U". Tiene un punto central llamado **Vértice** (donde la curva da la vuelta). Lo más increíble es que cualquier punto de esa "U" está a la misma distancia de un punto interno (el **Foco**) y de una línea recta que está "detrás" de la curva (la **Directriz**).

> [!warning] ⚠️ Error común: El cambio de signos
> Al extraer el vértice $(h, k)$ de la ecuación ordinaria, **siempre** debes cambiar el signo de los números que ves en la fórmula. 
> *   Si ves $(x - 3)$, el valor de $h$ es $3$.
> *   Si ves $(y + 2)$, el valor de $k$ es $-2$.
> 
> **Ejemplo:**
> ❌ **Incorrecto:** En $(x - 3)^2 = 8(y + 2)$, decir que el vértice es $V(-3, 2)$.
> ✅ **Correcto:** El vértice es $V(3, -2)$.

> [!tip] 💡 Truco para recordarlo
> Para saber hacia dónde abre la parábola sin confundirte, recuerda: **"La letra sola (la que no tiene el cuadrado) manda la dirección"**.
> 
> *   **Si la "y" está sola:**
> 	*   $+y \implies$ Abre hacia **Arriba** ($\uparrow$)
> 	*   $-y \implies$ Abre hacia **Abajo** ($\downarrow$)
> *   **Si la "x" está sola:**
> 	*   $+x \implies$ Abre hacia la **Derecha** ($\rightarrow$)
> 	*   $-x \implies$ Abre hacia la **Izquierda** ($\leftarrow$)

---

### PROCEDIMIENTO PASO A PASO

#### A. Para graficar desde la ecuación ordinaria
```text
1. Identificar el Vértice (h, k): Extrae los valores de los paréntesis cambiando sus signos.
2. Determinar la Dirección: Identifica la variable no al cuadrado y su signo.
3. Calcular 'p': Toma el número exterior y divídelo entre 4 (4p = Coeficiente).
4. Ubicar Foco y Directriz: Camina la distancia 'p' desde el vértice hacia "adentro" para el foco y hacia "afuera" para la directriz.
5. Dibujar el Lado Recto (LR): Desde el foco, mide una distancia de 2p hacia ambos lados (perpendicular al eje) para determinar qué tan ancha es la "U". El ancho total es 4p.
```

#### B. Para convertir de Ecuación Ordinaria a General
```text
1. Desarrollar el binomio al cuadrado: Usa (a ± b)² = a² ± 2ab + b².
2. Distribuir el coeficiente: Multiplica el valor de 4p por los términos del segundo paréntesis.
3. Igualar a cero: Mueve todos los términos al lado izquierdo de la ecuación.
4. Ordenar la ecuación: Término cuadrático, términos lineales (x, y) y término independiente = 0.
```

---

### EJEMPLOS RESUELTOS

```ad-example
title: Ejemplo 1: Identificación básica
**Problema:** Hallar $V$, $p$ y dirección de $(x - 3)^2 = 8(y + 2)$.
1. **Vértice:** Cambiamos signos $\implies V(3, -2)$.
2. **Dirección:** La letra sola es $y$ positiva $\implies$ Abre hacia **Arriba**.
3. **Parámetro p:** $4p = 8 \implies p = 8/4 = 2$.
**Resultado:** $V(3, -2)$, $p = 2$, Abre hacia arriba.
```

```ad-example
title: Ejemplo 2: Manejo de signos y orientación
**Problema:** Analizar $(y + 2)^2 = -4(x + 5)$.
1. **Vértice:** La $x$ tiene $+5$ y la $y$ tiene $+2$. Cambiamos signos $\implies V(-5, -2)$.
2. **Dirección:** La letra sola es $x$ negativa $\implies$ Abre a la **Izquierda**.
3. **Parámetro p:** $4p = 4 \implies p = 1$.
**Resultado:** $V(-5, -2)$, $p = 1$, Abre a la izquierda.
```

```ad-example
title: Ejemplo 3: Conversión a Forma General
**Problema:** Convertir $(x - 5)^2 = 8(y - 3)$ a forma general ($Ax^2 + Dx + Ey + F = 0$).
1. **Expandir:** $(x - 5)^2 = x^2 - 10x + 25$.
2. **Distribuir:** $8(y - 3) = 8y - 24$.
3. **Igualar:** $x^2 - 10x + 25 = 8y - 24$.
4. **Pasar todo a la izquierda:** $x^2 - 10x - 8y + 25 + 24 = 0$.
**Resultado:** $x^2 - 10x - 8y + 49 = 0$.
```

```ad-example
title: Ejemplo 4: Aplicación en Costos ($USD)
**Problema:** Un arco parabólico decorativo sigue la ecuación $(x - 0)^2 = -20(y - 10)$. Si el costo de refuerzo estructural es de $100 USD por cada metro de altura desde el suelo hasta el vértice, ¿cuál es el costo total?
1. **Vértice:** $V(0, 10)$. La altura máxima es el valor de $k$, que es $10$ metros.
2. **Cálculo:** $10 \text{ m} \times 100 \text{ USD/m} = 1000 \text{ USD}$.
**Resultado:** El costo total es de $1,000 USD.
```

---

### PRÁCTICA PARA EL ESTUDIANTE

```ad-abstract
title: 🟢 Nivel Fácil: Identificación
Encuentra el Vértice ($V$) y el parámetro ($p$) para:
1. $(x + 2)^2 = 20(y - 5)$
2. $(y + 3)^2 = -12(x + 3)$
3. $(x - 2)^2 = 3(y - 2)$
4. $(y - 4)^2 = 16(x - 1)$
```

```ad-abstract
title: 🟡 Nivel Medio: Conversión
Convierte las siguientes ecuaciones ordinarias a su forma general:
1. $(x - 1)^2 = 12(y + 1)$
2. $(y + 2)^2 = -10(x - 4)$
3. $(x + 3)^2 = 4(y - 2)$
4. $(y - 5)^2 = 8(x + 2)$
```

```ad-abstract
title: 🔴 Nivel Avanzado: Aplicaciones y Trayectorias
1. **Inversión de Foco:** Una antena tiene la forma $(y - 0)^2 = 4(x - 0)$. Si el material del soporte del foco cuesta $50 USD por cada unidad de distancia $p$ desde el vértice, ¿cuál es el costo del soporte?
2. **Altura de Túnel:** Un túnel tiene la ecuación $(x - 0)^2 = -4(y - 5)$. Si el vértice representa la altura máxima, ¿a cuántos metros del suelo está el techo?
3. **Ecuación de Puente:** Un ingeniero necesita la ecuación de un cable que abre hacia arriba, con vértice en el origen $V(0,0)$ y una distancia $p=5$ para soportar el peso. Determina la ecuación ordinaria.
4. **Reporte Técnico de Costos:** Un cable sigue la trayectoria $(x - 6)^2 = 12(y - 3)$. 
   * a) Convierte la ecuación a su forma general. 
   * b) Si el costo de materiales se calcula multiplicando el valor del Lado Recto ($4p$) por $100 USD, ¿cuál es el presupuesto total?
```

```ad-success
title: ✅ Soluciones para el Docente
**Fácil:** 
1. $V(-2, 5), p=5$
2. $V(-3, -3), p=3$
3. $V(2, 2), p=0.75$
4. $V(1, 4), p=4$

**Medio:** 
1. $x^2 - 2x - 12y - 11 = 0$
2. $y^2 + 4y + 10x - 36 = 0$
3. $x^2 + 6x - 4y + 17 = 0$
4. $y^2 - 10y - 8x + 9 = 0$

**Avanzado:**
1. $p=1$. Costo: $1 \times 50 = 50 \text{ USD}$.
2. Altura = $k = 5$ metros.
3. $(x - 0)^2 = 20(y - 0)$ o simplemente $x^2 = 20y$.
4. a) $x^2 - 12x - 12y + 72 = 0$. b) $4p = 12$. Costo: $12 \times 100 = 1,200 \text{ USD}$.
```

---

### AUTOEVALUACIÓN (QUIZ)

```ad-question
title: Pregunta 1
Si la distancia entre el Vértice y el Foco es de 3 unidades ($p=3$), ¿cuánto mide el ancho total de la parábola en el foco (Lado Recto)?
**Respuesta:** 12 unidades (Fórmula $LR = 4p$).
```

```ad-question
title: Pregunta 2
¿Hacia dónde abre la parábola con ecuación $(y - k)^2 = 4p(x - h)$ si el valor de $4p$ es un número positivo?
**Respuesta:** Hacia la derecha (eje X positivo), porque la "x" es la letra sola y es positiva.
```

```ad-question
title: Pregunta 3
Un cable de puente tiene una distancia $p = 2$ metros. Si el metro de cable especial cuesta $150 USD, ¿cuál es el costo de un tramo de cable que tenga la longitud exacta del parámetro $p$?
**Respuesta:** $300 USD ($150 \times 2$).
```

---

> [!tip] 💡 En la próxima clase
> Ahora que dominas la parábola con vértice $(h, k)$ y su conversión a la forma general, en la **Clase 05** aprenderemos a encontrar los elementos (V, F, D) partiendo directamente desde la ecuación general. ¡Prepárate para completar el trinomio!

> [!info] 🧭 Navegación
> [[Clase 03]] | **Índice** | **Clase 04** | [[Clase 05]]