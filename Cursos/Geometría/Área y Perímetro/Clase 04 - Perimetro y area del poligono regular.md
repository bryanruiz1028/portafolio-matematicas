# Clase 04 — Perimeter and area of ​​a regular polygon when we know its apothem + Perímetro y área del polígono regular cuando conocemos su Lado + Radius and diameter knowing the perimeter of the circumference + Radius and diameter of the circumference knowing the area

#algebra #perimeterandarea

> [!info] 🧭 Navegación
> [[Clase 03|⬅ Clase 03]] | [[00 - Índice del curso|Índice]] | **Clase 04** | [[Clase 05|Clase 05 ➡]]

---

## RELEVANCIA

Dominar el cálculo de perímetros y áreas es fundamental para interpretar y transformar el espacio físico de manera eficiente. Esta competencia matemática nos permite cuantificar superficies y bordes, facilitando la toma de decisiones en diversos campos profesionales. A continuación, exploraremos cómo estas herramientas impactan directamente en la economía y la ingeniería.

* 💵 **Gestión de Costos:** Determinar la longitud de un cerramiento (perímetro) o la extensión de una superficie (área) es vital para presupuestar materiales. Por ejemplo, calcular el costo total en $USD para alfombrar una oficina o cercar un terreno.
* 🏗️ **Construcción y Arquitectura:** El diseño de estructuras como plazas hexagonales o columnas circulares requiere precisión geométrica para garantizar la estabilidad y la correcta distribución de recursos.
* 📊 **Vida Cotidiana:** Desde calcular el tamaño exacto de un mantel para una mesa circular hasta determinar el material necesario para el marco de una ventana regular, estas fórmulas optimizan nuestras actividades diarias.

---

## CONCEPTO CLAVE

> [!note] 📌 Definición para principiantes
> El **perímetro** es la medida del borde de una figura (la orilla), mientras que el **área** representa la superficie interior (lo de adentro). Un polígono regular de $n$ lados puede entenderse como una unión de $n$ triángulos isósceles iguales. El **apotema** es la distancia desde el centro del polígono hasta el punto medio de cualquiera de sus lados, actuando como la altura de esos triángulos internos. En el círculo, esta función la cumple el **radio**, que conecta el centro con cualquier punto de la circunferencia.

> [!warning] ⚠️ Error común
> Es vital no confundir el **apotema** con el **radio del polígono**. Geométricamente, si observamos el triángulo rectángulo interno, el radio del polígono es la **hipotenusa** (va hacia el vértice), mientras que el apotema es el **cateto adyacente** al ángulo central (va hacia el punto medio del lado). Usar la hipotenusa en lugar del cateto arruinará tus cálculos de área.

> [!tip] 💡 Truco para recordarlo
> Asocia siempre la **A** de **A**potema con la **A**ltura de los triángulos internos. Si conoces la altura (apotema) y la base (lado), puedes hallar el área de un triángulo; al multiplicarlo por el número de lados, obtienes el área total. Por eso la fórmula es $P \times ap / 2$.

---

## PROCEDIMIENTO PASO A PASO

### Bloque 1: Polígono Regular (Cálculos de Lado y Apotema)

Para resolver polígonos, dividimos el ángulo central en dos ($2n$) porque trabajamos con la mitad de cada triángulo interno para formar un triángulo rectángulo. Usaremos $\pi = 3.1416$.

```text
Paso 1: Hallar el ángulo de trabajo (θ)
        θ = 360 / (2 * n)

Paso 2: Relación Lado-Apotema (Trigonometría)
        Opción A: Si conocemos el Lado (L)
            ap = (L / 2) / tan(θ)
        Opción B: Si conocemos el Apotema (ap)
            x = ap * tan(θ)
            L = 2 * x

Paso 3: Calcular el Perímetro (P)
        P = n * L

Paso 4: Calcular el Área (A)
        A = (P * ap) / 2
```

### Bloque 2: Círculo y Circunferencia

```text
Paso 1: Hallar el Radio (r)
        Desde Perímetro: r = P / (2 * π)
        Desde Área:      r = √(A / π)

Paso 2: Calcular el Diámetro (d)
        d = 2 * r
```

*Nota: Redondear siempre a dos decimales para mayor precisión académica.*

---

## EJEMPLOS PRÁCTICOS

````ad-example
**Ejemplo 1 (Caso Básico): Pentágono regular con lado de 16 cm**
1. **Ángulo:** $\theta = 360 / (2 \times 5) = 36^\circ$.
2. **Apotema:** $ap = (16 / 2) / \tan(36^\circ) = 8 / 0.7265 = 11.01 \text{ cm}$.
3. **Perímetro:** $P = 5 \times 16 = 80.00 \text{ cm}$.
4. **Área:** $A = (80.00 \times 11.01) / 2 = 440.40 \text{ cm}^2$.
````

````ad-example
**Ejemplo 2 (Caso con Diámetro): Círculo con perímetro de 10 cm**
1. **Radio:** $r = 10 / (2 \times 3.1416) = 10 / 6.2832 = 1.59 \text{ cm}$.
2. **Diámetro:** $d = 2 \times 1.59 = 3.18 \text{ cm}$.
````

````ad-example
**Ejemplo 3 (Caso Avanzado): Hexágono regular con apotema de 7 cm**
1. **Ángulo:** $\theta = 360 / (2 \times 6) = 30^\circ$.
2. **Medio Lado (x):** $x = 7 \times \tan(30^\circ) = 7 \times 0.5773 = 4.04 \text{ cm}$.
3. **Lado Completo:** $L = 2 \times 4.04 = 8.08 \text{ cm}$.
4. **Perímetro:** $P = 6 \times 8.08 = 48.48 \text{ cm}$.
5. **Área:** $A = (48.48 \times 7) / 2 = 169.68 \text{ cm}^2$.
*Nota: Se utiliza $cm^2$ porque la entrada fue en $cm$.*
````

````ad-example
**Ejemplo 4 (Aplicación $USD): Jardín circular de 15 m²**
*Un jardín circular tiene un área de $15.00 \text{ m}^2$. Si el costo de la cerca es de $12.50 USD por metro lineal, calcule el costo total.*
1. **Radio:** $r = \sqrt{15 / 3.1416} = \sqrt{4.7746} = 2.19 \text{ m}$.
2. **Perímetro:** $P = 2 \times 3.1416 \times 2.19 = 13.76 \text{ m}$.
3. **Costo Total:** $13.76 \times 12.50 = 172.00 \text{ USD}$.
````

---

## EJERCICIOS PARA EL ESTUDIANTE

````ad-abstract
**Nivel Verde (Fácil)**
1. Calcula el perímetro de un octágono regular cuyo lado mide 5 cm.
2. Si el diámetro de un círculo es 20 cm, ¿cuál es su radio?
3. Halla el perímetro de un cuadrado (n=4) si su lado mide 12 m.
4. Calcula el radio de un círculo si su diámetro es de 7.5 cm.
````

````ad-abstract
**Nivel Amarillo (Medio)**
1. Un hexágono regular tiene un lado de 10 cm y un apotema de 8.66 cm. Halla su área.
2. Calcula el área de un pentágono con perímetro de 50 cm y apotema de 6.88 cm.
3. Encuentra el radio de un círculo que tiene un perímetro de 15.4 cm.
4. Un polígono de 20 lados tiene un lado de 2 cm. Calcula su perímetro.
````

````ad-abstract
**Nivel Rojo (Avanzado)**
1. **Piscina:** Se desea comprar una lona para cubrir una piscina hexagonal de apotema 7.00 m. Si la lona cuesta $15.00 USD por $m^2$, ¿cuál es el costo total? (Usa el área del Ejemplo 3 ajustada a metros).
2. **Orfebrería:** Una moneda circular tiene un área de $1.00 \text{ cm}^2$. Si se le quiere poner un borde de oro que cuesta $50.00 USD por cm lineal, ¿cuánto costará el borde?
3. **Parque:** Un parque decagonal regular (n=10) tiene un lado de 20.00 m. Calcula su área total.
4. **Ingeniería:** El perímetro de una rueda es de 0.75 m. Calcula su diámetro con dos decimales.
````

````ad-success
**Respuestas Esperadas (Standard: 2 decimales)**
*   **Verde:** 1) 40.00 cm | 2) 10.00 cm | 3) 48.00 m | 4) 3.75 cm
*   **Amarillo:** 1) 259.80 cm² | 2) 172.00 cm² | 3) 2.45 cm | 4) 40.00 cm
*   **Rojo:** 1) 2,545.20 USD | 2) 176.00 USD | 3) 3,078.00 m² | 4) 0.24 m
````

---

## MINI-PRUEBA DE AUTOEVALUACIÓN

````ad-question
**Pregunta 1**
¿Cuál es la diferencia conceptual entre círculo y circunferencia?
*(Respuesta: La circunferencia es la línea curva que representa el perímetro; el círculo es la superficie contenida dentro de ella).*
````

````ad-question
**Pregunta 2**
¿Por qué se utiliza $2n$ en el denominador de la fórmula del ángulo central?
*(Respuesta: Porque para usar trigonometría debemos dividir el triángulo isósceles central en dos triángulos rectángulos).*
````

````ad-question
**Pregunta 3**
Si un círculo tiene un perímetro de $25.13 \text{ m}$, y el costo de pintura para su borde es de $2.00 USD por metro, ¿cuál es el costo total?
*(Respuesta: $50.26 USD).*
````

---

> [!tip] 💡 En la próxima clase
> Una vez dominadas las figuras en dos dimensiones, daremos el salto al espacio. Prepárate para estudiar los **Volúmenes de Cuerpos Geométricos** y cómo la geometría define el mundo tridimensional.

> [!info] 🧭 Navegación
> [[Clase 03|⬅ Clase 03]] | [[00 - Índice del curso|Índice]] | **Clase 04** | [[Clase 05|Clase 05 ➡]]