# Clase 02 — Polígonos regulares: Ángulos, propiedades y cálculo de apotema

#geometria #angulosinteriores

> [!info] 🧭 Navegación
> - **Anterior:** [[Clase 01 — Introducción a los Polígonos]]
> - **Índice:** [[Curso de Geometría Plana]]

---

### 1. Relevancia y aplicaciones

> [!info] 🌍 Relevancia y aplicaciones
> Comprender los polígonos regulares y sus ángulos es fundamental para transformar figuras planas en estructuras tridimensionales. En el diseño y la arquitectura, el cálculo preciso de los ángulos asegura que las piezas encajen perfectamente.
> 
> - **💵 Aplicación USD:** El cálculo del apotema permite determinar la cantidad exacta de material necesario para refuerzos internos; por ejemplo, el costo de un marco de soporte basado en el precio por metro lineal de apotema en estructuras monumentales.
> - **🏗️ Aplicación práctica:** La estabilidad de los domos geodésicos depende de la división perfecta de ángulos para distribuir las cargas de peso de forma equitativa.
> - **📊 Situación cotidiana:** Se utiliza en el diseño gráfico para la creación de logotipos simétricos y en la ingeniería vial para la fabricación de señales de tránsito estandarizadas.

---

### 2. Conceptos Clave

> [!note] 📌 ¿Qué es un polígono regular?
> Un polígono regular es una figura geométrica que tiene **todos sus lados y todos sus ángulos internos iguales**. 
> 
> **Definiciones rápidas del Profe Alex:**
> - **Centro ($C$):** Punto interior que está a la misma distancia de todos los vértices.
> - **Vértice:** Punto de unión de dos lados.
> - **Radio ($r$):** Segmento que une el centro con cualquier vértice.
> - **Apotema ($a$):** Segmento que une el centro con el punto medio de un lado.

> [!warning] ⚠️ Error común
> No confundas el **radio** con el **apotema**. El radio llega al **vértice**, mientras que el apotema llega al **punto medio del lado**, formando un ángulo de $90^\circ$ (ángulo recto). Piensa en el apotema como la **altura** de los triángulos internos que forman el polígono.

> [!tip] 💡 Truco para recordarlo: Triangulación
> Para saber cuánto suman los ángulos internos, imagina que divides el polígono en triángulos desde un solo vértice. Cada lado extra añade un triángulo de $180^\circ$ a la suma total:
> - **Triángulo:** $180^\circ$
> - **Cuadrilátero:** $180^\circ + 180^\circ = 360^\circ$
> - **Pentágono:** $180^\circ + 180^\circ + 180^\circ = 540^\circ$
> - **Fórmula general:** $(n - 2) \cdot 180^\circ$ (donde $n$ es el número de lados).

---

### 3. Procedimiento para hallar el Apotema

¡No te asustes por la fórmula! Si sigues estos 4 pasos, resolverás cualquier polígono como un profesional. Para calcular el apotema ($a$) conociendo su lado ($L$):

```text
PASO 1: Identificar el número de lados (n) y la medida del lado (L).
PASO 2: Calcular el ángulo θ (teta) usando la fórmula: θ = 360 / (2 * n).
        *Nota: El "2n" representa los 2 triángulos rectángulos que se
        forman dentro de cada sección del polígono.
PASO 3: Aplicar la fórmula del apotema: a = L / (2 * tan(θ)).
PASO 4: Resolver en la calculadora (en modo DEG) y aproximar decimales.
```

---

### 4. Ejemplos de Aplicación

````ad-example
title: Ejemplo 1: Ángulos en un Romboide
Si tenemos un romboide con un ángulo conocido de $65^\circ$, ¿cuánto miden los demás?
1. Por propiedad de paralelogramos, los ángulos opuestos son iguales: el opuesto mide $65^\circ$.
2. Sumamos los conocidos: $65^\circ + 65^\circ = 130^\circ$.
3. Restamos del total de un cuadrilátero: $360^\circ - 130^\circ = 230^\circ$.
4. Dividimos entre los dos ángulos restantes (que también son iguales): $230^\circ / 2 = 115^\circ$.
**Resultado:** Los ángulos son $65^\circ$, $115^\circ$, $65^\circ$ y $115^\circ$.
````

````ad-example
title: Ejemplo 2: Suma de ángulos de un Hexágono
Calcula la suma de los ángulos internos de un hexágono regular ($n = 6$).
Utilizamos la fórmula: $(n - 2) \cdot 180^\circ$.
1. $6 - 2 = 4$ (esto significa que el hexágono contiene 4 triángulos internos).
2. $4 \cdot 180^\circ = 720^\circ$.
**Resultado:** La suma de los ángulos internos es $720^\circ$.
````

````ad-example
title: Ejemplo 3: Apotema de un Hexágono
Halla el apotema de un hexágono regular cuyo lado mide $15 \text{ cm}$.
1. $n = 6$, $L = 15 \text{ cm}$.
2. Ángulo $\theta = 360 / (2 \cdot 6) = 360 / 12 = 30^\circ$.
3. Aplicamos: $a = 15 / (2 \cdot \tan(30^\circ))$.
4. En calculadora: $15 / (2 \cdot 0.5773) \approx 12.99 \text{ cm}$.
**Resultado:** El apotema es $12.99 \text{ cm}$.
````

````ad-example
title: Ejemplo 4: Aplicación Económica (USD)
Se desea colocar un refuerzo de bronce en el apotema de un pentágono de lado $6 \text{ cm}$. Si el cm lineal de bronce cuesta **$15.50 USD**, ¿cuál es el costo del refuerzo?
1. Hallar apotema del pentágono ($n = 5$, $L = 6 \text{ cm}$):
   - $\theta = 360 / (2 \cdot 5) = 36^\circ$.
   - $a = 6 / (2 \cdot \tan(36^\circ)) \approx 4.13 \text{ cm}$.
2. Calcular costo basado en la longitud lineal: $4.13 \text{ cm} \cdot 15.50 \text{ USD/cm} = 64.015 \text{ USD}$.
**Resultado:** El costo aproximado es de **$64.02 USD**.
````

---

### 5. Ejercicios para el Estudiante

````ad-abstract
title: 🟢 Nivel Fácil
1. ¿Cómo se llaman los polígonos regulares de $7$, $10$ y $12$ lados?
2. ¿Cuál es la suma de los ángulos internos de cualquier triángulo?
````

````ad-abstract
title: 🟡 Nivel Medio
1. En un trapecio isósceles, los ángulos de la base menor son iguales. Si un ángulo de la base mayor mide $70^\circ$, ¿cuánto miden los otros tres ángulos?
2. Calcula el ángulo $\theta$ necesario para la fórmula del apotema en un octágono regular ($n = 8$).
````

````ad-abstract
title: 🔴 Nivel Avanzado
Un arquitecto diseña una fuente con forma de decágono regular ($n = 10$) cuyo lado mide $10 \text{ metros}$. Necesita instalar un sensor a lo largo del apotema que cuesta **$120.00 USD** por cada metro lineal de longitud. ¿Cuál será el presupuesto total para el sensor?
````

---

### 6. Respuestas y Autoevaluación

> [!success] Soluciones breves
> - **Fácil:** 1. Heptágono, Decágono, Dodecágono. 2. $180^\circ$.
> - **Medio:** 1. $70^\circ, 110^\circ, 110^\circ$. (Razonamiento: La base mayor tiene ángulos iguales ($70^\circ+70^\circ=140^\circ$), restamos de $360^\circ$ y dividimos los $220^\circ$ restantes entre los dos ángulos iguales de la base menor). 2. $\theta = 22.5^\circ$ ($360/16$).
> - **Avanzado:** $\theta = 18^\circ$, $a \approx 15.39 \text{ m}$, Costo $\approx 1,846.80 \text{ USD}$. (Razonamiento: Se calcula el apotema con $n=10$ y $L=10$, luego se multiplica por el costo unitario).

````ad-question
title: Pregunta 1: Teórica
¿Qué sucede con la suma de los ángulos internos de un polígono a medida que aumentamos el número de lados?
a) Se mantiene igual ($360^\circ$).
b) Disminuye $180^\circ$ por cada lado extra.
c) Aumenta $180^\circ$ por cada lado extra.
d) Se reduce a la mitad.
**Respuesta correcta: c**. Según la regla de triangulación, cada lado adicional permite formar un triángulo más dentro de la figura, sumando $180^\circ$ adicionales.
````

````ad-question
title: Pregunta 2: Procedimental
Para un pentágono regular de lado $8 \text{ cm}$, ¿cuál es el primer paso para hallar el apotema?
a) Multiplicar $8 \cdot 5$.
b) Calcular el ángulo $\theta = 360 / (2 \cdot 5)$.
c) Dividir $180$ entre $5$.
d) Multiplicar la tangente por el radio.
**Respuesta correcta: b**. El primer paso conceptual es determinar el ángulo $\theta$ del triángulo rectángulo interno que utiliza el apotema.
````

````ad-question
title: Pregunta 3: Aplicación USD
Si el apotema de un polígono mide $10 \text{ cm}$ y el material de cobertura cuesta **$5.00 USD** el cm, pero hay un descuento del $10\%$ si el costo supera los **$40.00 USD**, ¿cuánto se paga finalmente?
a) $50.00 USD
b) $45.00 USD
c) $40.00 USD
d) $55.00 USD
**Respuesta correcta: b**. Costo inicial: $10 \text{ cm} \cdot 5 = 50 \text{ USD}$. Como supera los $40$, aplicamos el descuento: el $10\%$ de $50$ es $5$. Total: $50 - 5 = 45 \text{ USD}$.
````

---

> [!tip] 💡 En la próxima clase
> Ahora que dominas el cálculo del apotema, estamos listos para el siguiente nivel: **Cálculo de Áreas en Polígonos Regulares**, donde el apotema será la pieza clave de nuestra fórmula final.

> [!info] 🧭 Navegación
> - **Anterior:** [[Clase 01 — Introducción a los Polígonos]]
> - **Índice:** [[Curso de Geometría Plana]]