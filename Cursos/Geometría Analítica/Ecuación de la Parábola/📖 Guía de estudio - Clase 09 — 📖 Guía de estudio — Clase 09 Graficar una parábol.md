# 📖 Guía de estudio — Clase 09: Graficar una parábola a partir de su ecuación general

> [!info] 📌 Conceptos clave
> *   **La Ecuación General:** Se reconoce porque solo una de las variables ($x$ o $y$) está elevada al cuadrado. Su estructura suele ser $Ax^2 + Dx + Ey + F = 0$ o $Cy^2 + Dx + Ey + F = 0$.
> *   **Necesidad de Transformación:** Para graficar con precisión, debemos pasar la ecuación general a su **forma ordinaria o canónica**. Esto nos permite visualizar "el ADN" de la parábola: su vértice y su apertura.
> *   **Completar el Trinomio:** Es la técnica algebraica fundamental que consiste en sumar un valor específico en ambos lados de la igualdad para crear un binomio al cuadrado.
> *   **Elementos de Navegación:** Una vez en forma ordinaria, identificamos el **Vértice** $(h, k)$, el **Foco** (punto interno), el **Parámetro** ($p$) y la **Directriz** (recta externa).

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ecuación General** | $Ax^2 + Dx + Ey + F = 0$ (Vertical) o $Cy^2 + Dx + Ey + F = 0$ (Horizontal). |
| **Ecuación Ordinaria** | $(x-h)^2 = 4p(y-k)$ (Abre en eje $y$) o $(y-k)^2 = 4p(x-h)$ (Abre en eje $x$). |
| **Vértice $(h, k)$** | Punto de origen. **Importante:** Al extraer los valores de la ecuación, ¡cambia sus signos! |
| **Parámetro ($p$)** | Distancia del vértice al foco. Se obtiene despejando $4p$ del coeficiente del término lineal. |
| **Lado Recto ($LR$)** | Ancho total de la parábola a la altura del foco. $LR = |4p|$. |
| **Foco ($F$)** | Se ubica a una distancia $p$ del vértice, siempre hacia "adentro" de la curva. |
| **Directriz ($D$)** | Recta situada a una distancia $p$ del vértice, en sentido opuesto al foco. |

---

## Ejemplos Resueltos Adicionales

```ad-example
**Título: Ejemplo A — Caso con $x$ al cuadrado (Análisis Completo)**
**Ecuación inicial:** $x^2 + 10x - 12y + 1 = 0$

**Paso 1: Separar términos.** Dejamos las variables cuadráticas a la izquierda y lo demás a la derecha.
$x^2 + 10x = 12y - 1$

**Paso 2: Completar el Trinomio Cuadrado Perfecto.** Tomamos el coeficiente de $x$ ($10$), lo dividimos entre $2$ y lo elevamos al cuadrado: $(\frac{10}{2})^2 = 5^2 = 25$. Sumamos $25$ en ambos lados para mantener el equilibrio:
$x^2 + 10x + 25 = 12y - 1 + 25$
$x^2 + 10x + 25 = 12y + 24$

**Paso 3: Factorizar para obtener la forma ordinaria.**
$(x + 5)^2 = 12(y + 2)$

**Paso 4: Identificar elementos y graficar mentalmente.**
*   **Vértice ($V$):** $(-5, -2)$ (Recuerda cambiar los signos).
*   **Abertura:** Como $x$ está al cuadrado y el coeficiente $12$ es positivo, abre hacia **arriba**.
*   **Parámetro ($p$):** $4p = 12 \implies p = \frac{12}{4} = 3$.
*   **Foco ($F$):** Como abre hacia arriba, sumamos $p$ a la coordenada $k$ del vértice: $F = (-5, -2 + 3) = (-5, 1)$.
*   **Directriz ($D$):** Restamos $p$ a la coordenada $k$ del vértice: $y = -2 - 3 \implies y = -5$.
```

```ad-example
**Título: Ejemplo B — Aplicación en construcción y presupuesto ($USD)**
**Contexto:** Un arquitecto diseña un arco parabólico para una entrada cuya ecuación es $y^2 + 6y - 4x + 17 = 0$. Se requiere instalar un cable de soporte de lujo a lo largo del **Lado Recto**. El costo del cable es de $15.50 USD por metro.

**Paso 1: Transformar a la forma ordinaria.**
$y^2 + 6y = 4x - 17$
Completamos el cuadrado con la mitad de $6$ al cuadrado: $(\frac{6}{2})^2 = 3^2 = 9$.
$y^2 + 6y + 9 = 4x - 17 + 9$
$(y + 3)^2 = 4x - 8$
**Forma ordinaria:** $(y + 3)^2 = 4(x - 2)$

**Paso 2: Extraer datos técnicos.**
*   **Vértice ($V$):** $(2, -3)$.
*   **Dirección:** Abre hacia la **derecha** ($y$ al cuadrado, parámetro positivo).
*   **Parámetro ($p$):** $4p = 4 \implies p = 1$.
*   **Foco ($F$):** Sumamos $p$ a la coordenada $h$: $F = (2 + 1, -3) = (3, -3)$.
*   **Directriz ($D$):** $x = 2 - 1 \implies x = 1$.
*   **Lado Recto ($LR$):** $|4p| = 4$ metros.

**Paso 3: Cálculo de presupuesto.**
$Costo = Longitud (LR) \times Precio$
$Costo = 4 \, \text{m} \times 15.50 \, \text{USD/m} = 62.00 \, \text{USD}$.
```

---

## Ejercicios de Repaso

```ad-abstract
**🟢 Nivel Verde (Fácil): Identificación directa**
Determina el vértice $(h, k)$, el valor de $p$ y la dirección de apertura:
1. $(x - 2)^2 = 8(y + 5)$
2. $(y + 1)^2 = -12(x - 3)$
3. $x^2 = 4(y - 1)$
```

```ad-abstract
**🟡 Nivel Amarillo (Medio): Conversión de General a Ordinaria**
Transforma las siguientes ecuaciones completando el cuadrado y halla el vértice:
4. $x^2 - 8x - 8y + 32 = 0$
5. $y^2 + 2y - 12x + 37 = 0$
6. $x^2 + 4x + 12y - 20 = 0$
```

```ad-abstract
**🔴 Nivel Rojo (Avanzado): Análisis Completo**
Resuelve aplicando todo lo aprendido:
7. Para la ecuación $y^2 + 4y - 16x + 20 = 0$, calcula las coordenadas exactas del **Foco** y la ecuación de la **Directriz**.
8. **Cálculo Económico:** El diseño de una antena sigue la ecuación $x^2 - 6x - 10y + 19 = 0$. Si el lado recto debe reforzarse con una aleación que cuesta $22.00 USD el metro, ¿cuál es el costo total del refuerzo?
9. Realiza el esquema mental de $x^2 = -16(y + 2)$. Explica razonadamente si el foco se encuentra por encima o por debajo del vértice y cuál es su coordenada $y$.
```

---

> [!tip] 💡 Consejo de estudio
> **La técnica del dibujo auxiliar:** No confíes solo en tu memoria para las fórmulas del foco y la directriz. Antes de calcular coordenadas, haz un **bosquejo rápido**. Si ves que la parábola abre hacia la izquierda, dibuja una "C" invertida y marca el vértice. Visualmente verás que el foco está a la izquierda (restas $p$ a $x$) y la directriz a la derecha (sumas $p$ a $x$). ¡Tu cerebro procesa mejor las imágenes que las fórmulas abstractas! Confía en tu dibujo.