# Clase 04 — Líneas y Puntos Notables del Triángulo

**Metadatos:**
- **Tags:** #geometría #matemáticas #triángulos #puntos-notables #educación
- **Curso:** [[Índice de Geometría Aplicada]]
- **Navegación:** [[Clase 03 — Clasificación de Triángulos]] | [[Clase 05 — Teorema de Pitágoras]]

---

> [!info] 🧭 Navegación
> En esta sesión exploraremos las cuatro líneas maestras del triángulo: **medianas, mediatrices, bisectrices y alturas**. Aprenderemos a trazar sus puntos de encuentro (**baricentro, circuncentro, incentro y ortocentro**) y a entender por qué son vitales en la ingeniería y la economía.

> [!info] 🌍 Relevancia y aplicaciones
> La geometría de los puntos notables permite optimizar recursos y asegurar la estabilidad de las estructuras.
> - 🏗️ **[Práctica]:** El **baricentro** es el centro de masa. Si necesitas colgar un cartel triangular y que no se incline, el agujero debe ir exactamente en este punto.
> - 💵 **[USD]:** Al planificar rutas de entrega, hallar el **circuncentro** permite ubicar un centro de distribución a la misma distancia de tres tiendas, minimizando el gasto de combustible de forma equitativa.
> - 📊 **[Cotidiana]:** El trazado de **alturas** es la base para calcular el área de cualquier superficie triangular (Base × Altura / 2).

---

## 3. Conceptos Clave

> [!note] Las 4 Líneas y sus Puntos
> 1. **Mediana:** Une un vértice con el punto medio del lado opuesto. Su punto es el **Baricentro** (Centro de gravedad, siempre interno).
> 2. **Mediatriz:** Línea perpendicular que pasa por el punto medio de un lado. Su punto es el **Circuncentro** (Equidistante de los vértices).
> 3. **Bisectriz:** Semirrecta que divide un ángulo en dos partes iguales. Su punto es el **Incentro** (Equidistante de los **lados** y centro del círculo inscrito).
> 4. **Altura:** Segmento perpendicular que va desde un vértice al lado opuesto. Su punto es el **Ortocentro**.

> [!warning] Ubicación de Puntos según el Triángulo
> ¡Cuidado! No todos los puntos están siempre dentro del triángulo:
> - **Ortocentro y Circuncentro:** Se encuentran **dentro** en triángulos acutángulos, **fuera** en obtusángulos, y en los **límites** (vértice o hipotenusa) en triángulos rectángulos.
> - **Baricentro e Incentro:** Siempre son **internos**, sin importar el tipo de triángulo.

> [!tip] Regla Mnemotécnica: "Circun" de Circundar
> El **Circuncentro** es el centro de la circunferencia que **circunscribe** (rodea) al triángulo. Imagina que el triángulo está "encerrado" en un círculo que toca todas sus esquinas.

---

## 4. Procedimientos Paso a Paso

### Trazado de **Medianas** y **Baricentro**
```text
Paso 1: Mide con una regla cada lado del triángulo y marca el punto medio exacto.
Paso 2: Traza una línea recta (Mediana) desde cada vértice hasta el punto medio del lado opuesto.
Paso 3: Identifica la intersección de las tres líneas como el Baricentro.
Paso 4: Verifica la relación 2:1 (la distancia vértice-baricentro es el doble que baricentro-lado).
```

### Trazado de **Mediatrices** y **Circuncentro** (Método del Compás)
```text
Paso 1: Abre el compás con una medida que sea visiblemente mayor a la mitad del lado.
Paso 2: Haz centro en un vértice y traza un arco; repite desde el otro vértice del mismo lado.
Paso 3: Une los dos puntos donde se cruzan los arcos con una línea recta (Mediatriz).
Paso 4: Repite en los otros lados. El cruce de las tres mediatrices es el Circuncentro.
```

### Trazado de **Bisectrices** e **Incentro**
```text
Paso 1: Haz centro con el compás en el vértice y traza un arco pequeño que corte ambos lados.
Paso 2: Desde esos nuevos cortes, traza dos arcos hacia el centro del ángulo (sin cerrar el compás).
Paso 3: Une el vértice con el punto donde se cruzaron esos arcos finales (Bisectriz).
Paso 4: El punto donde las tres bisectrices se encuentran es el Incentro.
```

### Trazado de **Alturas** y **Ortocentro** (Método del "Carrito")
```text
Paso 1: Apoya un lado del ángulo recto de la escuadra sobre la base (el lado) del triángulo.
Paso 2: Desliza la escuadra como un "carrito" hasta que el otro lado alcance el vértice opuesto.
Paso 3: Si el triángulo es obtusángulo, prolonga el lado (línea punteada) para que el carrito alcance el vértice.
Paso 4: Traza la línea perpendicular. El cruce de las tres alturas es el Ortocentro.
```

---

## 5. Ejemplos Resueltos

> [!example] Ejemplo 1: El Baricentro y la Medida Real
> **Enunciado:** Hallar el **Baricentro** de un triángulo con lados de 19.4 cm, 26 cm y 28.5 cm.
> **Pasos:**
> 1. Marcar puntos medios a los 9.7 cm, 13 cm y 14.25 cm.
> 2. Unir cada punto medio con su vértice opuesto.
> 3. Al medir la **Mediana** de 21 cm, observamos que del vértice al **Baricentro** hay 14 cm y del **Baricentro** al lado hay 7 cm.
> **Resultado:** Se confirma la relación **2:1** (14 es el doble de 7).

> [!example] Ejemplo 2: Ortocentro en Triángulo Rectángulo
> **Enunciado:** Localizar el **Ortocentro** de un triángulo con un ángulo de 90°.
> **Pasos:**
> 1. Identificar que los catetos (piso y pared) ya son perpendiculares entre sí.
> 2. Notar que la **Altura** desde un vértice ya coincide con el cateto.
> 3. Trazar la **Altura** de la hipotenusa hacia el vértice recto.
> **Resultado:** El **Ortocentro** se ubica exactamente en el vértice del ángulo recto.

> [!example] Ejemplo 3: Ubicación del Circuncentro
> **Enunciado:** Determinar el centro de un círculo que pase por los tres vértices.
> **Pasos:**
> 1. Trazar las **Mediatrices** de al menos dos lados usando el método de los arcos.
> 2. El punto de cruce es el **Circuncentro**.
> 3. Colocar la punta del compás ahí y abrir hasta cualquier vértice.
> **Resultado:** El círculo toca los tres vértices con precisión milimétrica.

> [!example] Ejemplo 4: Análisis de Costos (USD)
> **Enunciado:** Una empresa debe conectar tres sedes (A, B, C) a una base de datos central. Si se ubica en un vértice, la distancia a las otras sedes es de 200m y 220m ($4,200 total). Si se ubica en el **Circuncentro**, la distancia a cada sede es de 120m. El costo por metro es de $10 USD. ¿Cuánto se ahorra?
> **Pasos:**
> 1. Costo en Vértice: (200 + 220) × 10 = $4,200 USD.
> 2. Costo en **Circuncentro**: (120 × 3) × 10 = $3,600 USD.
> **Resultado:** Ahorro total de **$600 USD** al usar geometría aplicada.

---

## 6. Ejercicios para el Estudiante

> [!abstract] Nivel Verde (Fácil)
> 1. Dibuja un triángulo equilátero de 10 cm por lado y traza sus tres **medianas**.
> 2. Si el lado de un triángulo mide 18.6 cm, ¿a qué medida exacta se debe trazar la **mediatriz**?
> 3. ¿Cómo se llama el punto notable que funciona como centro de equilibrio?
> 4. Dibuja una **bisectriz** usando el método del compás en un ángulo de 60°.

> [!abstract] Nivel Amarillo (Medio)
> 5. Dibuja un triángulo obtusángulo y traza sus **alturas** usando prolongaciones. ¿El **ortocentro** quedó dentro o fuera?
> 6. En una **mediana** de 15 cm, calcula cuánto mide el segmento que va desde el **baricentro** hasta el vértice.
> 7. Ubica el **circuncentro** en un triángulo rectángulo. ¿Es cierto que quedó en la mitad de la hipotenusa?
> 8. Traza el círculo inscrito de un triángulo (dentro) hallando primero el **incentro**.

> [!abstract] Nivel Rojo (Avanzado/USD)
> 9. **Ingeniería:** Se diseña una pieza triangular metálica que debe girar sobre un eje sin vibrar. ¿En qué punto notable se debe perforar?
> 10. **Logística:** Tienes 3 bodegas. El costo de conexión desde el **circuncentro** es de $3,600 USD (120m a cada vértice a $10/m). Si decides mudarte a un vértice para ahorrar renta, y las distancias ahora son de 190m y 210m, ¿cuánto dinero extra gastarás en cableado?
> 11. **Demostración:** Dibuja un triángulo isósceles y comprueba si el **ortocentro**, **baricentro** y **circuncentro** están alineados.
> 12. **Áreas:** Si una **mediana** divide un triángulo de $1,200 m^2$ en dos, ¿cuál es el área de cada triángulo resultante?

> [!success] Soluciones para el Docente
> 1. Trazos internos. 2. 9.3 cm. 3. **Baricentro**. 4. Dos ángulos de 30°. 5. Fuera. 6. 10 cm (Relación 2/3 de 15). 7. Sí. 9. **Baricentro**. 10. $400 USD extra (Costo nuevo $4,000 - $3,600). 12. $600 m^2$ cada uno.

---

## 7. Mini-Prueba de Autoevaluación

> [!question] Selecciona la respuesta correcta:
> **1. ¿En qué tipo de triángulo el Ortocentro coincide con un vértice?**
> a) Acutángulo.
> b) Obtusángulo.
> c) Rectángulo.
> d) Equilátero.
>
> **2. Si el segmento de una mediana que va del Baricentro al lado mide 4.5 cm, ¿cuánto mide el segmento que va del Baricentro al vértice opuesto?**
> a) 4.5 cm.
> b) 9 cm.
> c) 13.5 cm.
> d) 2.25 cm.
>
> **3. Un desarrollador de software quiere ubicar un servidor que esté a la misma distancia de tres terminales. ¿Qué punto debe calcular?**
> a) El **Incentro**.
> b) El **Ortocentro**.
> c) El **Baricentro**.
> d) El **Circuncentro**.

---
**Siguiente tema:** [[Clase 05 — Aplicaciones del Teorema de Pitágoras]]
[[Clase 03]] | [[Índice del Curso]] | [[Clase 05]]

---