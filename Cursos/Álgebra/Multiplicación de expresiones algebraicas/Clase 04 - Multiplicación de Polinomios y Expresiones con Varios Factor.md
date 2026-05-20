# Clase 04 — Multiplicación de Polinomios y Expresiones con Varios Factores (Método Vertical)

#algebra #multiplyingamon

[[00 - Índice del curso]] | Bloque 1 | Lección 4 de 4

---

## ¿Por qué es importante esta clase?

Dominar la multiplicación de múltiples factores algebraicos es esencial para modelar sistemas complejos. Esta habilidad permite a ingenieros y economistas calcular áreas de superficies compuestas y predecir el comportamiento de proyecciones financieras donde intervienen múltiples variables de crecimiento.

*   **💵 [aplicación con $USD]:** Se utiliza para calcular el costo final en situaciones de descuentos sucesivos o intereses compuestos, donde el precio base se multiplica por varios factores de ajuste (binomios).
*   **🏗️ [aplicación práctica]:** En arquitectura, es fundamental para determinar volúmenes de estructuras tridimensionales donde el largo, ancho y alto dependen de una misma variable constructiva.
*   **📊 [situación cotidiana]:** Permite modelar el ahorro acumulado cuando tanto el número de ahorradores como el monto que aporta cada uno crecen proporcionalmente cada mes.

---

## Concepto clave

**Definición:** La multiplicación mediante el **Método Vertical (Método 2)** organiza los polinomios uno sobre otro, de manera idéntica a la multiplicación aritmética de toda la vida. Este método es ideal para mantener el orden visual cuando trabajamos con expresiones largas. Cuando tenemos tres o más factores, aplicamos la **Propiedad Asociativa**: multiplicamos los dos primeros y el resultado obtenido se multiplica por el siguiente factor.

> [!TIP] **Pro-tip: Multiplicación de Fracciones**
> Si encuentras coeficientes fraccionarios, recuerda la regla simple: **Numerador por Numerador** y **Denominador por Denominador**. 
> Ejemplo: $\frac{1}{2}x \cdot \frac{3}{4}x = \frac{1 \cdot 3}{2 \cdot 4}x^2 = \frac{3}{8}x^2$.

**Error común:** 
1.  **Suma de exponentes en la suma final:** Muchos estudiantes suman los exponentes al realizar la reducción de columnas. Recuerda: los exponentes solo se suman durante la *multiplicación* (fase S-C-L), no en la suma final de términos semejantes.
2.  **Desalineación:** No dejar el espacio correspondiente o no alinear términos con la misma parte literal, lo que produce sumas de "peras con manzanas".

**Truco: La regla "S-C-L"**
Antes de escribir cualquier término en tu procedimiento, verifica mentalmente este orden:
1.  **S (Signo):** Multiplica los signos (Ley de signos: iguales dan $+$, diferentes dan $-$).
2.  **C (Coeficiente):** Multiplica los números (o fracciones).
3.  **L (Letras):** Escribe las letras y **suma** los exponentes de las bases iguales.

---

## Procedimiento paso a paso

**Nota de dirección:** A diferencia de la aritmética tradicional (donde multiplicamos de derecha a izquierda), en álgebra es más cómodo y común multiplicar los términos del factor inferior de **izquierda a derecha**.

1.  **PASO 1 (Orden vertical):** Escribe el polinomio con más términos arriba y el más corto abajo.
2.  **PASO 2 (Fase S-C-L):** Multiplica el primer término del polinomio inferior por cada uno de los términos del superior.
3.  **PASO 3 (Escalonamiento):** Al pasar al segundo término del factor inferior, escribe los resultados en una nueva fila, desplazándolos para que cada término quede exactamente debajo de su **término semejante** (misma letra y exponente).
4.  **PASO 4 (Reducción):** Traza una línea y suma las columnas. En este paso, la parte literal se mantiene intacta; solo operamos los coeficientes.

---

## Ejemplos de clase

::: ad-example
**Ejemplo 1: Monomio por Binomio (Caso básico)**
Operación: $5x \cdot (3x + 2)$

**Resolución vertical:**
```text
      3x + 2
    x 5x
    ---------
     15x² + 10x
```
*   **S-C-L 1:** $(+)(+) \rightarrow +$; $(5)(3) \rightarrow 15$; $(x^1)(x^1) \rightarrow x^2$.
*   **S-C-L 2:** $(+)(+) \rightarrow +$; $(5)(2) \rightarrow 10$; $(x)$ se conserva.
:::

::: ad-example
**Ejemplo 2: Signos y múltiples variables**
Operación: $-4x^2y^3 \cdot (3x^3 - xy^2 - 2)$

**Resolución vertical:**
```text
          3x³ - xy² - 2
        x     -4x²y³
        ---------------------
        -12x⁵y³ + 4x³y⁵ + 8x²y³
```
*   **Análisis:** Al multiplicar por un negativo, todos los signos del polinomio superior cambian en el resultado final. Sumamos exponentes de $x$ con $x$, y de $y$ con $y$.
:::

::: ad-example
**Ejemplo 3: Tres factores (Asociativa y Escalonamiento)**
Operación: $(2x) \cdot (x + 3) \cdot (x + 2)$

**Paso A (Monomio por primer Binomio):**
$2x(x + 3) = 2x^2 + 6x$

**Paso B (Resultado A por el último factor):**
```text
          2x² + 6x
        x  x  + 2
        ------------
          2x³ + 6x²       <-- Multiplicando por 'x'
              + 4x² + 12x   <-- Multiplicando por '+2' (Alineado x²)
        ------------
          2x³ + 10x² + 12x
```
:::

::: ad-example
**Ejemplo 4: Aplicación real $USD (Precio con Cargo)**
El costo de un producto es $(2x + 10)$ USD. Si se compran $(x + 5)$ unidades, ¿cuál es el gasto total?

**Resolución vertical:**
```text
          2x + 10
        x  x + 5
        ------------
          2x² + 10x
              + 10x + 50
        ------------
          2x² + 20x + 50 USD
```
:::

---

## Ejercicios para el estudiante

**🟢 Nivel Fácil (Monomio por Polinomio)**
1.  Multiplica verticalmente: $4a \cdot (2a - 5)$
2.  Multiplica verticalmente: $-3x^2 \cdot (x^2 + 4x)$
3.  Multiplica verticalmente: $2b \cdot (3b^2 - b + 6)$
4.  Multiplica verticalmente: $-5y \cdot (-2y + 7)$

**🟡 Nivel Medio (Fracciones y Varios Factores)**
5.  Realiza la operación: $(\frac{1}{3}x) \cdot (\frac{6}{5}x + 9)$
6.  Multiplica los tres factores: $(2) \cdot (x + 4) \cdot (x + 1)$
7.  Calcula: $(\frac{3}{2}a^2) \cdot (\frac{4}{3}a - 6)$
8.  Multiplica: $(xy) \cdot (x + 2) \cdot (3)$

**🔴 Nivel Avanzado (Contexto Real $USD)**
9.  **Arquitectura:** Una caja tiene una base de $(x+3)$ cm de largo, un ancho de $(x+1)$ cm y una altura de $(2x)$ cm. Halla el polinomio que representa su volumen.
10. **Terrenos:** Un terreno rectangular mide $(x+10)$ metros de largo por $(x-2)$ metros de ancho. Si el precio por metro cuadrado es de $5$ USD, ¿cuál es el costo total del terreno?
11. **Finanzas:** Un producto cuesta $x$ USD. Se le aplica un primer factor de aumento $(x+2)$ y luego un factor de descuento $(x-1)$. Multiplica los tres factores para hallar la expresión final.
12. **Ahorro:** $(3x)$ personas ahorran $(x^2 + 2x)$ dólares cada una durante $(x + 4)$ meses. Halla el polinomio del ahorro total.

::: ad-success
**Respuestas y Autocorrección:**
1. $8a^2 - 20a$ (**S-C-L del primer término:** Signo $(+)$, Coeficiente $4 \cdot 2=8$, Letra $a^1 \cdot a^1=a^2$).
2. $-3x^4 - 12x^3$
3. $6b^3 - 2b^2 + 12b$
4. $10y^2 - 35y$
5. $\frac{2}{5}x^2 + 3x$ (Recuerda: $\frac{1}{3} \cdot \frac{6}{5} = \frac{6}{15} = \frac{2}{5}$).
6. $2x^2 + 10x + 8$
7. $2a^3 - 9a^2$
8. $3x^2y + 6xy$
9. $2x^3 + 8x^2 + 6x$ cm³
10. $5x^2 + 40x - 100$ USD
11. $x^3 + x^2 - 2x$
12. $3x^4 + 18x^3 + 24x^2$
:::

---

## Mini-prueba de autoevaluación

1.  **¿Qué regla aplicamos a los exponentes cuando multiplicamos letras iguales (ej. $a^4 \cdot a^2$)?**
    *   *Respuesta:* Se deben **sumar** los exponentes, resultando en $a^6$. Esto se debe a que estamos multiplicando la misma base seis veces en total.
2.  **Si al multiplicar verticalmente un binomio por otro binomio obtengo dos filas de resultados, ¿cómo debo alinearlas?**
    *   *Respuesta:* Deben alinearse de modo que los **términos semejantes** (mismas letras y exponentes) queden en la misma columna para poder sumarlos correctamente en el paso final.
3.  **Un terreno tiene un área de $(x^2 + 5x)$ m². Si el costo es de $3x$ dólares por metro cuadrado, ¿cuál es la expresión del costo total?**
    *   *Respuesta:* $3x^3 + 15x^2$. Aplicamos la distribución vertical: $(3x \cdot x^2) + (3x \cdot 5x)$.

---

## Notas para el próximo tema

¡Excelente trabajo! Has dominado la técnica para construir expresiones algebraicas complejas mediante la multiplicación. Entender este orden vertical y la estructura de los productos es el "superpoder" que necesitarás para el Bloque 2: **División Algebraica y Factorización**. Allí aprenderemos el proceso inverso: cómo tomar un polinomio y "desarmarlo" para encontrar los factores originales que lo crearon.

[[00 - Índice del curso]] | Bloque 1 | Lección 4 de 4