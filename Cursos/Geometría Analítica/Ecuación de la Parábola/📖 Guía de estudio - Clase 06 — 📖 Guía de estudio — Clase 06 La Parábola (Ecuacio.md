# 📖 Guía de estudio — Clase 06: La Parábola (Ecuaciones General y Canónica)

> [!info] 📌 Conceptos clave
> La transición entre las formas de la ecuación de una parábola es fundamental para su análisis geométrico. Pasar de la **ecuación general** a la **canónica** (u ordinaria) permite identificar rápidamente elementos críticos como el vértice y el foco, facilitando su representación gráfica.
> * **El Proceso:** El paso central es **"completar el trinomio cuadrado perfecto"**, técnica que transforma una expresión cuadrática en un binomio al cuadrado.
> * **Estructura Visual:** Una ecuación general se reconoce porque todos sus términos están agrupados a un lado de la igualdad, resultando en $0$ al otro lado.
> * **Orientación y Apertura:** La dirección de la parábola depende de qué variable esté al cuadrado:
>     * Si $x^2$ está presente: La parábola abre **verticalmente** (hacia arriba o abajo).
>     * Si $y^2$ está presente: La parábola abre **horizontalmente** (hacia la izquierda o derecha).

## Sección: Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ecuación General** | Formato donde todos los términos se encuentran a un lado de la igualdad: $x^2 + Dx + Ey + F = 0$ o $y^2 + Dx + Ey + F = 0$. |
| **Ecuación Canónica** | Revela el vértice $(h, k)$. Estructuras: $(x-h)^2 = 4p(y-k)$ o $(y-k)^2 = 4p(x-h)$. |
| **Completar el Trinomio** | Técnica para hallar el tercer término: $(\frac{b}{2})^2$, donde $b$ es el coeficiente de la variable lineal (la que no está al cuadrado). |
| **Factorización final** | Uso del factor común en el lado derecho para dejar la variable lineal sola. El factor extraído representa la longitud del lado recto ($4p$). |

---

## Sección: Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A — De General a Canónica ($x^2$)
**Enunciado:** Convertir la ecuación general $x^2 - 6x - 8y - 7 = 0$ a su forma canónica.

**Paso 1: Agrupar términos.** Dejamos las $x$ a la izquierda y movemos los términos sin $x$ a la derecha (cambiando sus signos):
$x^2 - 6x = 8y + 7$

**Paso 2: Completar el trinomio.** Tomamos el coeficiente de $x$ ($6$), lo dividimos entre $2$ ($3$) y lo elevamos al cuadrado ($9$). Sumamos $9$ en **ambos** lados:
$x^2 - 6x + 9 = 8y + 7 + 9$
$x^2 - 6x + 9 = 8y + 16$

**Paso 3: Factorizar.** Convertimos el trinomio en binomio al cuadrado y extraemos el factor común ($4p$) al lado derecho:
$(x - 3)^2 = 8(y + 2)$

✅ **Resultado final:** $(x - 3)^2 = 8(y + 2)$
```

```ad-example
title: Ejemplo B — Modelado de costos en $USD
**Enunciado:** La trayectoria de un costo de producción sigue la ecuación $x^2 - 6x - 8y - 7 = 0$. Determine el **punto de costo mínimo** (vértice) expresando la ecuación en su forma canónica.

**Resolución:**
Utilizando el procedimiento algebraico del Ejemplo A, transformamos la ecuación general:
1.  **Separación y balance:** $x^2 - 6x + 9 = 8y + 16$
2.  **Forma canónica:** $(x - 3)^2 = 8(y + 2)$

Al comparar con $(x-h)^2 = 4p(y-k)$, extraemos el vértice $(h, k)$ invirtiendo los signos de los valores dentro de los paréntesis.

✅ **Resultado:** El punto de costo mínimo (vértice) se encuentra en $(3, -2)$. En una gráfica de costos, este punto representa el nivel de producción óptimo para minimizar gastos.
```

---

## Sección: Ejercicios de Repaso

```ad-abstract
title: 🟢 Nivel Fácil
Convierta las siguientes ecuaciones generales a su forma canónica:
1. $x^2 + 10x - 10y + 5 = 0$
2. $y^2 - 16y - 15x + 79 = 0$
3. $x^2 - 4x - 8y - 12 = 0$
```

```ad-abstract
title: 🟡 Nivel Medio
Retos de conversión con coeficientes y expansión:
1. **División inicial:** Convierta $3x^2 - 12x - 30y + 162 = 0$ (Sugerencia: Divida toda la ecuación entre 3 antes de comenzar).
2. **De canónica a general:** Expanda el binomio y agrupe términos para la ecuación $(x+2)^2 = 10(y-5)$.
3. **De canónica a general:** Transforme $(y-3)^2 = 4(x+1)$ a su forma general igualada a cero.
```

```ad-abstract
title: 🔴 Nivel Avanzado — Aplicación con $USD
**Problema de aplicación:**
Un informe financiero modela una inversión mediante la ecuación $(y - \frac{3}{2})^2 = \frac{1}{2}(x + \frac{1}{4})$. Para el archivo contable, conviértala a su **forma general**.

**Hitos de resolución (Milestones):**
*   **Paso 1:** Desarrolle el binomio al cuadrado $(y - \frac{3}{2})^2$.
*   **Paso 2:** Distribuya la fracción $\frac{1}{2}$ en el lado derecho.
*   **Paso 3:** Agrupe todos los términos a la izquierda e iguale a cero.
*   **Paso 4 (Opcional pero recomendado):** Elimine denominadores multiplicando toda la ecuación por el mínimo común múltiplo.

**💡 Hint:** Use el denominador común **8** para obtener una ecuación con números enteros: $8y^2 - 24y - 4x + 17 = 0$.
```

---

## Cierre: Consejo de Estudio

> [!tip] 💡 Consejo de estudio
> Para dominar la parábola, aplica siempre los **3 pasos invariables** del Profe Alex:
> 1. **Separar:** Deja la variable al cuadrado y su compañera lineal en un lado; traslada lo demás al otro.
> 2. **Completar:** Suma $(\frac{b}{2})^2$ en **ambos** lados para no alterar la balanza de la ecuación.
> 3. **Factorizar:** Reduce a binomio al cuadrado y extrae el factor común.
> 
> **⚠️ Regla de Oro del Signo:** Si el término al cuadrado ($x^2$ o $y^2$) es negativo al inicio, **multiplica toda la ecuación por $-1$** antes de comenzar. ¡Y no olvides verificar el cambio de signo al mover términos de un lado al otro!