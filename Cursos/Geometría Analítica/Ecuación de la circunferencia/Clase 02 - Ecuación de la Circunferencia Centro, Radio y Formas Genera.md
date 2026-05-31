# Clase 02 — Ecuación de la Circunferencia: Centro, Radio y Formas General/Canónica

tags: #algebra #centroyradiodel #geometriaanalitica
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 2

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]

---

## ¿Por qué es importante esta clase?

Dominar la transición entre la ecuación general y la canónica es como poseer una llave maestra: nos permite convertir un conjunto abstracto de coordenadas y potencias en un mapa físico real. Esta habilidad es la que permite a un software de navegación o a un ingeniero transformar ecuaciones complejas en puntos exactos (el centro) y dimensiones tangibles (el radio) que se pueden dibujar con un compás o construir en el terreno.

**Aplicaciones prácticas:**
*   💵 **$USD:** En telecomunicaciones, determinar el costo de cobertura de una antena. Si la ecuación define un radio de alcance, podemos calcular el área de servicio y determinar el costo de licitación por kilómetro cuadrado o el gasto en cableado perimetral.
*   🏗️ **Práctica:** El diseño de infraestructuras circulares, desde la construcción de glorietas viales eficientes hasta la cúpula de una catedral, depende de identificar correctamente el centro para la estabilidad estructural.
*   📊 **Cotidiana:** La optimización de recursos en agricultura. Calcular el alcance de un aspersor de riego permite cubrir el área necesaria sin desperdiciar agua ni dinero en zonas fuera del límite.

---

## Conceptos clave

### Definición para mentes jóvenes (12 años)
Imagina que quieres darle instrucciones a alguien para dibujar un círculo perfecto. La **ecuación general** es como una frase muy larga y desordenada que nadie entiende a simple vista. Al simplificarla, encontramos el **centro $(h, k)$**, que es el punto exacto donde debes clavar la punta metálica del compás, y el **radio $(r)$**, que es cuánto debes abrir el compás antes de girarlo.

> [!warning] **¡Cuidado con los signos!**
> El error más común ocurre al extraer las coordenadas del centro. En la fórmula $(x - h)^2 + (y - k)^2 = r^2$, los signos negativos son parte de la estructura. 
> *   **Visualización:** Si ves $(x - 5)^2$, el centro es $+5$. Si ves $(x + 3)^2$, el centro es $-3$. **¡Siempre invierte el signo que ves!**

**Truco mnemotécnico para la forma general ($x^2 + y^2 + Dx + Ey + F = 0$):**
*   **D** acompaña a la **X**: Piensa en **D**esplazamiento horizontal (Eje X).
*   **E** acompaña a la **Y**: Piensa en **E**levación vertical (Eje Y).

---

## Procedimiento paso a paso

### Método 1: Uso de Fórmulas (Camino Directo)
Si ya tienes identificados los coeficientes $D, E$ y $F$:
1.  **Centro $(h, k)$:** $h = -D/2$, $k = -E/2$.
2.  **Radio $(r)$:** $r = \frac{1}{2}\sqrt{D^2 + E^2 - 4F}$.

### Método 2: Completar cuadrados (Camino Algebraico)
Este método es fundamental para entender la geometría detrás del álgebra. El secreto es mantener el **balance**: lo que sumas de un lado de la igualdad para formar un trinomio cuadrado perfecto, debes sumarlo obligatoriamente al otro lado.
1.  Agrupa términos de $x$ con $x$ y términos de $y$ con $y$.
2.  Mueve el término independiente $F$ al lado derecho del igual.
3.  Suma la mitad del coeficiente lineal elevado al cuadrado en ambos lados.
4.  Factoriza los trinomios en binomios al cuadrado.

```text
ESQUEMA DE TRABAJO:
1. Identificar coeficientes D, E y F (Asegurar que x² e y² no tengan coeficientes).
2. Agrupar y completar cuadrados (Mantener el balance de la ecuación).
3. Factorizar a la forma canónica: (x - h)² + (y - k)² = r².
4. Extraer el centro (h, k) y la raíz cuadrada del término derecho para hallar el radio.
```

---

## Ejemplos de la Clase

### Ejemplo 1: De General a Centro/Radio (Básico)
Ecuación: $x^2 + y^2 - 8x - 10y + 40 = 0$
*   $D = -8, E = -10, F = 40$.
*   $h = -(-8)/2 = 4$ ; $k = -(-10)/2 = 5 \rightarrow$ **Centro (4, 5)**.
*   $r = \frac{1}{2}\sqrt{(-8)^2 + (-10)^2 - 4(40)} = \frac{1}{2}\sqrt{64 + 100 - 160} = \frac{1}{2}\sqrt{4} = 1$.
*   **Resultado:** Centro $(4, 5)$, Radio $1$.

### Ejemplo 2: Término faltante y Radicales
Ecuación: $x^2 + y^2 + 2y - 7 = 0$
*   No hay término con $x$, por lo que $D = 0$.
*   $h = -0/2 = 0$ ; $k = -2/2 = -1 \rightarrow$ **Centro (0, -1)**.
*   $r^2 = (h^2 + k^2 - F) \rightarrow r = \sqrt{0^2 + (-1)^2 - (-7)} = \sqrt{1 + 7} = \sqrt{8}$.
*   **Nota Didáctica:** El radio tiene dos formas de presentarse. La **Forma Exacta** es $\sqrt{8}$ (o $2\sqrt{2}$), y la **Forma Aproximada** (útil para graficar o aplicaciones reales) es $\approx 2.82$.

### Ejemplo 3: De Centro/Radio a General
Centro $(2, 5)$, Radio $3$.
1.  Sustituir: $(x - 2)^2 + (y - 5)^2 = 3^2$.
2.  Desarrollar: $(x^2 - 4x + 4) + (y^2 - 10y + 25) = 9$.
3.  Simplificar: $x^2 + y^2 - 4x - 10y + 20 = 0$.

### Ejemplo 4: Ecuación a partir de 3 puntos
Puntos: $A(-4, 1), B(3, -2), C(6, 5)$.
Sustituimos cada punto en $x^2 + y^2 + Dx + Ey + F = 0$ para crear un sistema $3 \times 3$:
1.  $-4D + E + F = -17$
2.  $3D - 2E + F = -13$
3.  $6D + 5E + F = -61$
> [!tip] **Consejo Didáctico**
> En estos sistemas, siempre es más fácil eliminar primero la variable $F$, ya que su coeficiente siempre es $1$ en todas las ecuaciones.
*   **Resultados:** $D = -2, E = -6, F = -19$.

---

## Ejercicios para el estudiante

### 🟢 Nivel Fácil: Identificación
Indica los valores de $D, E$ y $F$:
1.  $x^2 + y^2 - 6x + 8y - 10 = 0$
2.  $x^2 + y^2 + 4x - 12 = 0$
3.  $x^2 + y^2 - 2x - 2y + 1 = 0$
4.  $x^2 + y^2 + 10y = 0$

### 🟡 Nivel Medio: Conversión y Geometría
Determina el Centro y Radio completando cuadrados:
1.  $x^2 + y^2 - 4x - 6y + 9 = 0$
2.  $x^2 + y^2 + 8x + 2y + 8 = 0$
3.  $x^2 + y^2 - 10x + 16 = 0$
4.  $x^2 + y^2 + 12x - 4y + 31 = 0$

### 🔴 Nivel Avanzado: Aplicaciones Reales ($USD)
1.  Un radar detecta objetos en un área definida por $x^2 + y^2 - 4x + 6y - 12 = 0$. Si cada km² de monitoreo cuesta $50 USD, ¿cuál es el costo total de operación?
2.  Un jardín circular tiene la ecuación $x^2 + y^2 = 49$. Se desea cubrir con césped artificial de $12 USD el m². Calcula el presupuesto total.
3.  Una glorieta urbana está delimitada por $x^2 + y^2 - 20x = 0$. El costo de pavimentación es de $25 USD por m². ¿Cuánto cuesta la obra?
4.  Se diseña una fuente con centro $(3, -2)$ que debe tocar el punto $(3, 1)$. Si el borde de piedra cuesta $20 USD por metro lineal, ¿cuál es el costo?

---

### Sección de respuestas (Para el docente)

| Ejercicio | Resultado |
| :--- | :--- |
| **Fácil 1** | $D=-6, E=8, F=-10$ |
| **Fácil 2** | $D=4, E=0, F=-12$ |
| **Fácil 3** | $D=-2, E=-2, F=1$ |
| **Fácil 4** | $D=0, E=10, F=0$ |
| **Medio 1** | $C(2, 3), r=2$ |
| **Medio 2** | $C(-4, -1), r=3$ |
| **Medio 3** | $C(5, 0), r=3$ |
| **Medio 4** | $C(-6, 2), r=3$ |
| **Avanzado 1** | $C(2, -3), r=5$, Área $\approx 78.54$ km², Costo: $3,927$ USD |
| **Avanzado 2** | $r=7$, Área $\approx 153.94$ m², Costo: $1,847.28$ USD |
| **Avanzado 3** | $C(10, 0), r=10$, Área $\approx 314.16$ m², Costo: $7,854$ USD |
| **Avanzado 4** | $r=3$, Perímetro $\approx 18.85$ m, Costo: $377$ USD |

---

## Mini-prueba de autoevaluación

1.  **Conceptual:** Si al calcular el radio, el valor bajo la raíz es negativo, ¿qué significa? 
    *   *Respuesta:* Significa que la ecuación no representa una circunferencia real (es un lugar geométrico imaginario).
2.  **Procedimental:** Halla el centro de $x^2 + y^2 + 10x - 6y + 9 = 0$.
    *   *Respuesta:* $C(-5, 3)$.
3.  **Aplicación:** Una moneda tiene el borde $x^2 + y^2 = 4$. ¿Cuál es su diámetro y su valor si cada unidad de área vale $2 USD?
    *   *Respuesta:* Diámetro $= 4$. Área $\approx 12.56$. Valor $\approx 25.13$ USD.

---

## Notas para el próximo tema
En la siguiente clase estudiaremos la **Elipse**. Veremos que, a diferencia de la circunferencia donde el radio es constante, la elipse se "estira", lo que nos obligará a trabajar con dos distancias distintas desde el centro. ¡Prepárate para expandir tu visión del plano!

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]