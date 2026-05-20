# Clase 06 — Dominio, rango y gráfica de funciones racionales y con raíz cuadrada

tags: #algebra #domainrangeandg
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 6 de 12

> [!info] 🧭 Navegación
> [[Clase 05|⬅ Clase 05]] | [[00 - Índice del curso|Índice]] | **Clase 06** | [[Clase 07|Clase 07 ➡]]

## 1. ¿Por qué es importante esta clase?
El análisis de funciones permite predecir comportamientos límites y entender las restricciones naturales de un fenómeno matemático o financiero. Dominar las asíntotas y raíces es fundamental para:
- Calcular la estabilización de **costos unitarios ($USD)** cuando la producción tiende al infinito.
- Determinar los límites de **resistencia de materiales** antes de alcanzar un punto de ruptura crítico.
- Modelar **trayectorias** asintóticas en fenómenos físicos y biológicos.

## 2. Concepto clave
Una **función racional** es aquella donde la variable independiente se encuentra en el denominador, mientras que una **función con raíz cuadrada** contiene la variable bajo un radical de índice par.

> [!note] Dominio y Rango
> - **Dominio:** Valores permitidos de $x$ que no generan indeterminaciones.
> - **Rango:** Valores resultantes en $y$ tras la evaluación.

> [!warning] Restricción: División por cero
> En funciones racionales, el denominador **nunca** puede ser cero. Esto genera discontinuidades en la gráfica: asíntotas verticales o "huecos".

> [!warning] Restricción: Raíces negativas
> En funciones de raíz cuadrada, el contenido del radical debe ser $\geq 0$. Si el resultado es negativo, la calculadora arrojará "Error" pues no existe solución en el campo de los números reales, resultando en un dominio truncado.

> [!tip] Regla mnemotécnica para asíntotas verticales
> Para recordar cómo identificar las "paredes" invisibles de la gráfica:
> *“¡Denominador a cero, pared a la vista!”*

## 3. Procedimiento paso a paso
Para graficar funciones racionales complejas, aplica este algoritmo técnico:

```text
1. FACTORIZAR: Simplifica numerador y denominador por completo.
2. IDENTIFICAR HUECOS VS. ASÍNTOTAS: 
   - Si un factor variable se simplifica -> Hay un HUECO.
   - Si un factor permanece solo en el denominador -> Hay una ASÍNTOTA.
3. ASÍNTOTAS HORIZONTALES/OBLICUAS:
   - Grados iguales: y = cociente de coeficientes principales.
   - Grado num = grado den + 1: Realizar división polinómica.
4. PUNTOS CRÍTICOS: Hallar interceptos (ceros) y puntos de control adicionales.
```

## 4. Ejemplos de aplicación

> [!ad-example] Ejemplo 1: Grados Iguales y Simplificación de Constantes
> **Función:** $$f(x) = \frac{2x^2+4}{2x^2-8}$$
> 1. **Factorización:** $$\frac{2(x^2+2)}{2(x+2)(x-2)}$$
> 2. **Análisis técnico:** El coeficiente constante `2` se simplifica. **Nota importante:** Simplificar una constante NO crea un hueco; solo los factores que contienen a $x$ lo hacen.
> 3. **Asíntotas Verticales:** El denominador es cero en $x=2$ y $x=-2$.
> 4. **Asíntota Horizontal:** Como los grados son iguales ($x^2$), dividimos coeficientes: $2/2 = 1$. Asíntota en $y=1$.

> [!ad-example] Ejemplo 2: El caso de los "Huecos" (Discontinuidad Puntual)
> **Función:** $$f(x) = \frac{x^3-x^2-2x}{x^3-4x}$$
> 1. **Factorización:** $$\frac{x(x-2)(x+1)}{x(x+2)(x-2)}$$
> 2. **Simplificación:** Los factores variables $x$ y $(x-2)$ se eliminan. Esto genera huecos en lugar de asíntotas.
> 3. **Coordenadas de los huecos:** Evaluamos la función simplificada $g(x) = \frac{x+1}{x+2}$ en los valores eliminados:
>    - Para $x=0$: $g(0) = 1/2 \implies$ **Hole 1: (0, 0.5)**
>    - Para $x=2$: $g(2) = 3/4 \implies$ **Hole 2: (2, 0.75)**
> 4. **Asíntota Vertical:** El único factor que quedó en el denominador es $(x+2)$, por lo tanto, hay una asíntota en $x = -2$.

> [!ad-example] Ejemplo 3: Asíntota Oblicua mediante División
> **Función:** $$f(x) = \frac{x^2-4x-5}{x-2}$$
> 1. **Análisis de Grado:** El numerador (grado 2) es una unidad mayor que el denominador (grado 1). Existe una asíntota oblicua.
> 2. **División polinómica:**
>    $$x^2 - 4x - 5 = (x - 2)(x - 2) - 9$$
>    Al dividir, obtenemos: $$f(x) = (x - 2) + \frac{-9}{x - 2}$$
> 3. **Interpretación:** Cuando $x$ tiende a infinito, el término $\frac{-9}{x-2}$ se aproxima a cero. Por lo tanto, la función se comporta como la recta: **$y = x - 2$**.

> [!ad-example] Ejemplo 4: Aplicación Financiera ($USD)
> **Escenario:** Un modelo de costo de producción está definido por $$C(x) = \sqrt{x-6}$$ donde $x$ son unidades producidas.
> 1. **Restricción Real:** Para que el costo sea un valor financiero válido en $USD$, el radical no puede ser negativo.
> 2. **Dominio:** $x - 6 \geq 0 \implies x \geq 6$. 
> 3. **Conclusión:** Si la producción es menor a 6 unidades, el resultado no es un número real, lo que significa que el costo no puede calcularse en el mercado financiero real. El dominio inicia en 6 y el rango en 0 $USD.

## 5. Ejercicios para el estudiante

> [!ad-abstract] Nivel Verde (Fácil)
> Determine el dominio de las siguientes funciones:
> 1. $f(x) = \frac{10}{x-5}$
> 2. $g(x) = \sqrt{x+4}$

> [!ad-abstract] Nivel Amarillo (Medio)
> Dada la función $f(x) = \frac{x^2-9}{x-3}$, identifique si existe una asíntota vertical o un hueco en $x=3$. Justifique factorizando el numerador.

> [!ad-abstract] Nivel Rojo (Avanzado)
> Una empresa de logística modela su costo de operación como $f(x) = \sqrt{4x-20}$. Calcule el rango de la función en $USD$ considerando únicamente valores que pertenezcan al dominio de números reales.

> [!ad-success] Soluciones para el docente
> - **Verde:** 1) Dom: $\mathbb{R} - \{5\}$; 2) Dom: $x \geq -4$.
> - **Amarillo:** Hueco en $x=3$. Al factorizar $\frac{(x-3)(x+3)}{x-3}$, el factor variable se simplifica, eliminando la asíntota.
> - **Rojo:** Dominio $x \geq 5$; Rango $[0, \infty)$ $USD$.

## 6. Mini-prueba de autoevaluación

> [!ad-question] Pregunta 1
> ¿Cuál es la diferencia gráfica entre simplificar un factor constante (número) y un factor variable (que contiene $x$)?
> - **Respuesta:** Simplificar una constante solo ajusta la escala de la función; simplificar un factor variable elimina una indeterminación y crea un **hueco** en la gráfica.

> [!ad-question] Pregunta 2
> ¿Cómo se determina el inicio del rango en una función de raíz cuadrada simple como $f(x) = \sqrt{x+k}$?
> - **Respuesta:** Dado que la raíz cuadrada principal siempre devuelve valores no negativos, el rango comienza en $0$ y se extiende hacia el infinito ($[0, \infty)$).

> [!ad-question] Pregunta 3
> Si una función de utilidad tiene una asíntota oblicua $y = x - 2$, ¿cuál es la tendencia de la ganancia ($USD$) a largo plazo?
> - **Respuesta:** Indica una tendencia lineal ascendente. Por cada unidad adicional producida ($x$), la ganancia ($y$) aumentará aproximadamente en 1 unidad $USD$ de forma constante a medida que los valores crecen.

## 7. Notas para el próximo tema

> [!tip] Conexión curricular
> Las asíntotas que hemos estudiado hoy son la representación visual de un concepto más profundo: el comportamiento de una función cuando se acerca a un límite. En la **Clase 07**, formalizaremos esto mediante el estudio de **Límites en el infinito**.

> [!info] 🧭 Navegación
> [[Clase 05|⬅ Clase 05]] | [[00 - Índice del curso|Índice]] | **Clase 06** | [[Clase 07|Clase 07 ➡]]