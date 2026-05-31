# Clase 05 — Parábola: Gráfica, Foco, Vértice y Directriz desde la Ecuación y Viceversa

#algebra #parbolagraficar

Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 5 de 9

> [!info] 🧭 Navegación
> - ⬅️ Clase anterior: [[Clase 04 — Elementos de la Parábola]]
> - ➡️ Próxima clase: [[Clase 06 — Ecuación General de la Parábola]]

---

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> La parábola describe matemáticamente cómo se mueven los objetos bajo la influencia de la gravedad y cómo las señales de onda se concentran en un solo punto.
> - **💵 Aplicación $USD:** En optimización económica, el [[Vértice]] de una función parabólica representa el punto crítico donde una empresa alcanza su **ganancia máxima** o minimiza sus costos de producción.
> - **🏗️ Aplicación práctica:** El diseño de antenas satelitales y faros de autos depende del [[Foco]], el punto donde se reflejan todas las señales entrantes o salientes.
> - **📊 Situación cotidiana:** La trayectoria de un balón de fútbol o un proyectil (balística) sigue una curva que solo podemos predecir conociendo estos elementos.

---

## Concepto clave

> [!note] 📌 ¿Qué es Parábola Graficar y encontrar foco, vértice y directriz conociendo su ecuación ordinaria?
> Es el proceso técnico de extraer las coordenadas del [[Vértice]] $(h, k)$ y el parámetro focal $p$ directamente de la estructura de la ecuación. Con estos datos, podemos ubicar la parábola espacialmente sin necesidad de tabular múltiples puntos, usando una construcción geométrica precisa.

> [!warning] ⚠️ Error común
> 1. **Signos opuestos:** Al extraer $h$ y $k$ de la ecuación, siempre debes invertir su signo. Si lees $(x + 1)$, entonces $h = -1$.
> 2. **Dirección de apertura:** Muchos estudiantes abren la parábola hacia la directriz. Recuerda la analogía del Profe Alex: **"La parábola le tiene miedo a la directriz"**, por lo que siempre se aleja de ella y "envuelve" al foco.

> [!tip] 💡 Truco para recordarlo
> Utiliza la regla del **"Orden F-V-D"**: Los tres elementos principales siempre están alineados. El [[Vértice]] es el punto medio; el [[Foco]] está a una distancia $p$ "dentro" de la curva y la [[Directriz]] está a una distancia $p$ por "fuera".

---

## Procedimiento paso a paso

```text
PASO 1: Identificar el Vértice V(h, k) cambiando los signos. 
        Determinar orientación: 
        - Si el término al cuadrado es (x - h)², la parábola es vertical (arriba/abajo). 
        - Si es (y - k)², es horizontal (derecha/izquierda). 
        El signo del coeficiente lineal indica el sentido exacto.

PASO 2: Calcular "p". Iguala el coeficiente de la ecuación a 4p (4p = valor). 
        Despeja dividiendo entre 4.

PASO 3: Ubicar Foco y Directriz. Siguiendo la línea del eje de simetría y el orden F-V-D, 
        mide la distancia p desde el vértice. El Foco está en la zona donde abre 
        la curva; la Directriz es la recta perpendicular al eje en el lado opuesto.

PASO 4: Trazar el Lado Recto (LR). Su longitud total es 4p. Pasa por el foco y se 
        distribuye 2p hacia cada lado. Estos puntos definen el "ancho" o apertura real.
```

---

## Ejemplos

### Ejemplo 1: De elementos a gráfica y ecuación (Básico)
**Datos:** Foco $F(2, 0)$ y Directriz $y = 2$.
1. **Vértice:** El vértice es el punto medio entre el foco y la directriz. Como la directriz es horizontal ($y=2$) y el foco está en $y=0$, el punto medio en $y$ es $y_v = \frac{0 + 2}{2} = 1$. Coordenadas: $V(2, 1)$.
2. **Parámetro $p$:** La distancia entre $V(2, 1)$ y $F(2, 0)$ es $1$ unidad ($p = 1$).
3. **Apertura:** Como la curva "le tiene miedo" a la directriz ($y=2$) y busca al foco ($y=0$), abre hacia **abajo**.
4. **Ecuación:** Al ser vertical hacia abajo, usamos $(x - h)^2 = -4p(y - k)$.
   $(x - 2)^2 = -4(1)(y - 1) \implies (x - 2)^2 = -4(y - 1)$.

### Ejemplo 2: De ecuación a elementos (Con cambios de signo)
**Ecuación:** $(x + 1)^2 = -12(y - 2)$
1. **Vértice:** Cambiamos signos de la ecuación: $h = -1, k = 2$. $V(-1, 2)$.
2. **Parámetro $p$:** $4p = 12 \implies p = 3$.
3. **Apertura:** Es $x^2$ (vertical) con signo negativo: abre hacia **abajo** (eje $y$ negativo).
4. **Elementos:** Bajamos $3$ unidades desde el vértice para el foco: $F(-1, -1)$. Subimos $3$ unidades para la directriz: $y = 2 + 3 = 5$.

### Ejemplo 3: Términos "solos" y fracciones
**Ecuación:** $y^2 = 6(x - 2)$
1. **Vértice:** Como $y$ no está en un paréntesis con otro número, $k = 0$. $h = 2$. $V(2, 0)$.
2. **Parámetro $p$:** $4p = 6 \implies p = \frac{6}{4} = \frac{3}{2} = 1.5$.
3. **Apertura:** Es $y^2$ positivo: abre hacia la **derecha** (eje $x$ positivo).
4. **Instrucción para graficar fracciones:** Para ubicar $p = 1.5$ ($3/2$), observa el denominador $(2)$: divide cada unidad del plano cartesiano en dos partes iguales. Luego, cuenta $(3)$ mitades desde el vértice hacia la derecha para el foco: $F(3.5, 0)$ o $F(\frac{7}{2}, 0)$.

### Ejemplo 4: Aplicación económica ($USD)
**Problema:** La utilidad mensual de una fábrica de calzado sigue la ecuación $(x - 100)^2 = -20(y - 500)$, donde $x$ representa las unidades vendidas y $y$ la ganancia en $USD.
1. **Interpretación:** Al abrir hacia abajo, el vértice representa el valor máximo.
2. **Coordenadas:** $h = 100$ y $k = 500$.
3. **Conclusión:** El valor $k = 500$ representa la **ganancia máxima de 500 USD**, mientras que $h = 100$ representa la **cantidad óptima de 100 unidades** a vender para alcanzar dicho beneficio.

---

## Ejercicios para el estudiante

### Bloque 🟢 Fácil (Identificación)
Halla el vértice $V(h, k)$ y el valor de $p$ para:
1. $(x - 3)^2 = 8(y + 1)$
2. $(y - 5)^2 = 16(x - 2)$
3. $x^2 = 4(y - 7)$
4. $(y + 4)^2 = -20x$

### Bloque 🟡 Medio (Construcción)
Halla la ecuación ordinaria con los siguientes datos:
1. Foco $F(0, 3)$, Directriz $y = -1$
2. Foco $F(2, 1)$, Directriz $x = 6$
3. Vértice $V(0, 0)$, Foco $F(0, -2)$
4. Vértice $V(1, 1)$, $p = 3$, abre hacia la derecha.

### Bloque 🔴 Avanzado ($USD)
1. Un reflector parabólico tiene un costo de producción. Si su forma sigue la ecuación $y^2 = 12x$, ¿en qué coordenada $x$ se ubica el foco para colocar la bombilla?
2. La eficiencia de un panel solar se modela con $(x - 50)^2 = -40(y - 100)$. Si $y$ es el porcentaje de eficiencia, ¿cuál es la eficiencia máxima?
3. Un túnel tiene forma de parábola con ecuación $x^2 = -16(y - 4)$. Halla las coordenadas del foco (punto de mayor resistencia estructural).
4. Una antena de $150$ USD tiene su foco en $F(0, 2)$ y vértice en $V(0, 0)$. Determina su ecuación ordinaria.

### Bloque ✅ Respuestas
**🟢 Fácil:**
1. $V(3, -1), p = 2$
2. $V(2, 5), p = 4$
3. $V(0, 7), p = 1$
4. $V(0, -4), p = 5$

**🟡 Medio:**
1. $(x - 0)^2 = 8(y - 1)$
2. $(y - 1)^2 = -8(x - 4)$
3. $x^2 = -8y$
4. $(y - 1)^2 = 12(x - 1)$

**🔴 Avanzado:**
1. $F(3, 0)$
2. Máximo $y = 100$
3. $F(0, 0)$
4. $x^2 = 8y$

---

## Mini-prueba de autoevaluación
1. **¿Cuál es la distancia total entre el foco y la directriz?** (Respuesta: $2p$).
2. **Si una ecuación tiene la forma $(y - k)^2 = -4p(x - h)$, ¿en qué dirección se aleja de la directriz?** (Respuesta: Hacia la izquierda / eje $x$ negativo).
3. **En un modelo de costos parabólico, ¿qué coordenada del vértice ($h$ o $k$) suele representar el costo mínimo en USD?** (Respuesta: La coordenada $k$).

---

## Notas para el próximo tema

> [!tip] 💡 En la próxima clase
> Analizaremos la **Ecuación General de la Parábola** ($Ax^2 + Dx + Ey + F = 0$). Aprenderás la técnica de completar el trinomio cuadrado perfecto para regresar a la forma ordinaria que dominaste hoy.

> [!info] 🧭 Navegación
> - ⬅️ Clase anterior: [[Clase 04 — Elementos de la Parábola]]
> - ➡️ Próxima clase: [[Clase 06 — Ecuación General de la Parábola]]