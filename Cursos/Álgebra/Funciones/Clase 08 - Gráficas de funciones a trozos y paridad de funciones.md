# Clase 08 — Gráficas de funciones a trozos y paridad de funciones

`#algebra` `#graphofpiecewise`

[[Clase 07 — Introducción a Funciones]] | [[Clase 09 — Dominio y Rango]]

---

## 1. Relevancia y Aplicaciones

> [!info] 🌍 Relevancia y aplicaciones
> Las funciones a trozos modelan situaciones reales donde las reglas del juego cambian según la cantidad o el tiempo, permitiendo que una sola función tenga comportamientos distintos en diferentes intervalos.
> - **Tarifas y Finanzas:** Esencial para calcular impuestos o servicios en dólares ($USD$), donde el costo por unidad varía drásticamente al superar ciertos umbrales de consumo.
> - **Diseño y Arquitectura:** Permite modelar rampas y estructuras donde la pendiente debe cambiar en puntos específicos para cumplir con normas de seguridad.
> - **Planes de Datos:** Reflejan el consumo diario de internet, con un cargo fijo por una cantidad base de GB y una tarifa variable para el excedente.

---

## 2. Conceptos Fundamentales: Funciones a Trozos y Paridad

> [!note] 📌 ¿Qué es una Función a Trozos?
> Imagina que tienes un **"rompecabezas de gráficas"**. En lugar de una sola línea infinita, dibujamos varios pedazos de gráficos en un mismo plano. Como dice el Profe Alex, es "dibujar varios gráficos en uno", pero con una condición: cada pieza solo puede existir en su propio territorio asignado en el eje $x$.

> [!warning] ⚠️ Error común
> El fallo más habitual es graficar la función en todo el plano. ¡Cuidado! Solo debes realizar el trazo dentro de los límites de $x$ que indica la regla. Si la instrucción dice $x < 2$, tu gráfica para ese trozo debe detenerse exactamente antes de llegar al $2$.

> [!tip] 💡 Truco para recordarlo
> Piensa en los intervalos como **"fronteras territoriales"**. Para no perderte, te recomiendo trazar **líneas punteadas verticales** en los valores de $x$ donde cambia la función. Estas líneas son muros que te indican dónde termina una regla y comienza la otra.

### Paridad de Funciones: Simetría Visual
La paridad nos dice cómo se comporta la gráfica respecto al centro o los ejes:
- **Función Par (Simetría respecto al eje $Y$):** Imagina que el eje $Y$ es un espejo. Si pudieras realizar un **doblez de papel** justo por la mitad vertical, ambos lados de la gráfica coincidirían perfectamente. Matemáticamente: $f(-x) = f(x)$.
- **Función Impar (Simetría respecto al origen):** No basta con un reflejo. Aquí la gráfica es idéntica si decides **girar el tablero 180°** respecto al punto central $(0,0)$. Es un "doble reflejo" (primero sobre el eje $Y$ y luego sobre el eje $X$). Matemáticamente: $f(-x) = -f(x)$.

---

## 3. Procedimiento para Graficar y Determinar Paridad

### Para Funciones a Trozos
¡Vamos a analizar este reto paso a paso para no perdernos!
1. **PASO 1:** Identificar los intervalos de $x$ y qué función le toca a cada uno.
2. **PASO 2:** Crear una tabla de valores para cada intervalo. **Tip del Profe:** Incluye siempre el número del límite (frontera) en tu tabla, aunque el intervalo sea "abierto" ($<$ o $>$), para saber exactamente dónde poner el hueco.
   *Formato sugerido:*
   | $x$ (Entrada) | $f(x)$ (Cálculo) | Punto $(x, y)$ |
   | :--- | :--- | :--- |
   | Valor límite | Sustitución | $(x, y)$ |
3. **PASO 3:** Ubicar los puntos. Diferencia entre un **punto relleno** (•) para intervalos cerrados ($\le, \ge$) y un **punto hueco** (○) para intervalos abiertos ($<, >$).
4. **PASO 4:** Unir los puntos según la función (recta para lineales, curva para parábolas).

### Para Paridad Numérica
Utilizaremos la regla de las potencias: $(-x)^n$ es positivo si $n$ es par, y negativo si $n$ es impar.
1. **PASO 1:** Sustituir cada $x$ por $(-x)$ usando **siempre paréntesis**. Ejemplo: $5x^2 \to 5(-x)^2$.
2. **PASO 2:** Simplificar signos. Si el exponente es par, el negativo desaparece; si es impar, el negativo sale del paréntesis.
3. **PASO 3:** Comparar. Si el resultado es igual a la original, es **Par**. Si todos los signos se invirtieron, es **Impar**.

---

## 4. Ejemplos Prácticos Detallados

```ad-example
title: Ejemplo 1: Gráfica Básica con Cambio de Regla
**Función:** $f(x) = \begin{cases} x + 2 & \text{si } x \le 2 \\ x^2 - 4x & \text{si } x > 2 \end{cases}$
**Análisis:** 
1. Para $x \le 2$ (Intervalo cerrado): Evaluamos en $x=2 \to 2+2=4$. Dibujamos un **punto cerrado** en $(2, 4)$ y trazamos la recta hacia la izquierda.
2. Para $x > 2$ (Intervalo abierto): Evaluamos en $x=2 \to 2^2 - 4(2) = -4$. Dibujamos un **punto hueco** en $(2, -4)$ y trazamos la curva de la parábola hacia la derecha.
```

```ad-example
title: Ejemplo 2: Solapamiento (Continuidad visual)
**Función:** $f(x) = x^2 + 2$ ($x < 0$); $f(x) = 2 - x$ ($0 \le x < 2$); $f(x) = x^2 - 4x + 3$ ($x \ge 2$).
**Explicación:** En $x=0$, la primera función deja un hueco en $(0, 2)$, pero la segunda función (que incluye al cero) coloca un punto cerrado exactamente en $(0, 2)$. El punto cerrado "tapa" el hueco, haciendo que la gráfica se vea unida.
```

```ad-example
title: Ejemplo 3: Demostración de Paridad
**Problema:** Determinar si $f(x) = 2x^2 - 3$ es par o impar.
**Proceso:**
1. $f(-x) = 2(-x)^2 - 3$.
2. Como el exponente $2$ es par, $(-x)^2 = x^2$.
3. Resultado: $f(-x) = 2x^2 - 3$.
**Resultado:** Como $f(-x)$ es idéntica a $f(x)$, la función es **Par**.
```

```ad-example
title: Ejemplo 4: Aplicación de Tarifas ($USD$)
**Problema:** Una empresa cobra $\$10\ USD$ fijos por hasta $5\ GB$. Después, cobra $\$2\ USD$ adicionales por cada $GB$ extra.
**Función:** $f(x) = \begin{cases} 10 & \text{si } 0 \le x \le 5 \\ 10 + 2(x-5) & \text{si } x > 5 \end{cases}$
**Por qué $(x-5)$:** Este término representa únicamente los $GB$ que **exceden** el límite inicial. Si consumes $7\ GB$, solo pagas el extra por $2\ GB$ ($7-5=2$).
```

---

## 5. Ejercicios de Aplicación

```ad-abstract
title: 🟢 Nivel Verde (Fácil)
1. Si una gráfica coincide perfectamente al doblar el papel por el eje $Y$, ¿es par o impar?
2. Una función es idéntica tras girarla $180^\circ$ respecto al origen. Identifica su paridad.
3. Para graficar $x > 4$, ¿el punto en el número $4$ debe ser abierto o cerrado?
4. Determina visualmente si $f(x) = x^2$ tiene simetría de espejo.
```

```ad-abstract
title: 🟡 Nivel Amarillo (Medio)
1. Evalúa la paridad de $f(x) = 3x^2 - 5x$ mediante sustitución.
2. Demuestra si $f(x) = x^3 - 4x$ es impar usando el paso a paso numérico.
3. Si $f(x) = 5$ para $x < 0$ y $f(x) = x + 5$ para $x \ge 0$, ¿cuánto vale $f(0)$?
4. Calcula $f(-3)$ y $f(3)$ para $f(x) = |x| + 1$ y define si es par.
```

```ad-abstract
title: 🔴 Nivel Rojo (Avanzado)
1. Grafica el costo en $USD$: $C(x) = 15$ si $0 \le x \le 10$ y $C(x) = 15 + 3(x-10)$ si $x > 10$.
2. Construye la gráfica de $f(x) = -\frac{x^2}{2} - 2x$ para $x < -2$ y $f(x) = x+5$ para $-2 \le x < 1$. Indica los puntos de frontera.
3. Demuestra matemáticamente si la función constante $f(x) = k$ (donde $k$ es un número real) es par o impar.
4. Diseña una función a trozos que presente un "salto" (discontinuidad) en $x=3$.
```

---

## 6. Solucionario para el Docente

```ad-success
1. **Verde:** (1) Par, (2) Impar, (3) Abierto (Hueco), (4) Par.
2. **Amarillo:** (1) Sin paridad, (2) Impar ($f(-x) = -x^3 + 4x = -f(x)$), (3) $f(0)=5$, (4) Ambos valen $4$, es Par.
3. **Rojo:** 
   - (1) Recta horizontal de $(0,15)$ a $(10,15)$ (punto cerrado). Luego, recta con pendiente $3$ partiendo de $(10,15)$.
   - (2) Parábola con punto hueco en $(-2, 2)$ y recta con punto cerrado en $(-2, 3)$ y punto hueco en $(1, 6)$.
   - (3) Es Par porque $f(-x) = k$, que es igual a $f(x)$.
   - (4) Ejemplo: $f(x)=1$ si $x \le 3$ y $f(x)=5$ si $x > 3$.
```

---

## 7. Autoevaluación

```ad-question
title: Pregunta Conceptual
¿Qué acción física en el papel demuestra que una función es impar?
a) Doblarlo por el eje $X$.
b) Doblarlo por el eje $Y$.
c) Girarlo $180^\circ$ sobre el origen.
d) No se puede demostrar físicamente.

**Respuesta:** **c)**. La simetría impar es una simetría rotacional respecto al origen $(0,0)$.
```

```ad-question
title: Pregunta Procedimental
Si en una función a trozos evaluamos un límite en el intervalo $x > 2$, ¿cómo representamos ese punto?
a) Punto relleno porque el $2$ es la frontera.
b) Punto hueco porque el símbolo $>$ no incluye la igualdad.
c) No se grafica el punto en $2$.
d) Una flecha hacia la izquierda.

**Respuesta:** **b)**. El "hueco" (intervalo abierto) indica que la función se acerca infinitamente al valor, pero no lo toma.
```

```ad-question
title: Pregunta de Aplicación
Usando la función del Ejemplo 4 (Tarifa base $\$10$ hasta $5\ GB$, $\$2$ extra por cada adicional), ¿cuál es el costo de consumir $8\ GB$?
a) $\$10\ USD$
b) $\$13\ USD$
c) $\$16\ USD$
d) $\$26\ USD$

**Respuesta:** **c)**. Se calculan los $\$10$ base $+$ $(\$2 \times 3\ GB \text{ extras}) = 10 + 6 = 16\ USD$.
```

---

## 8. Cierre y Conexión

> [!tip] 💡 En la próxima clase
> Dominar estas gráficas "fragmentadas" es el primer paso para conquistar el **Dominio y el Rango**. En nuestra siguiente sesión, aprenderás a leer estos dibujos para determinar exactamente qué valores de entrada y salida permite la función. ¡Nos vemos en la frontera de los números!

[[Clase 07 — Introducción a Funciones]] | [[Clase 09 — Dominio y Rango]]