# Clase 03 — Ecuaciones de Segundo Grado por Fórmula General
#algebra #quadraticequati

[[Clase 02 — Métodos de Factorización | ← Clase Anterior]] | [[Índice de Álgebra | Inicio]] | [[Clase 04 — Raíces no exactas y Simplificación | Próxima Clase →]]

---

## Relevancia y Aplicaciones

¡Bienvenidos! Hoy aprenderemos a usar la "llave maestra" del álgebra: la **Fórmula General**. A diferencia de la factorización, este método funciona para *todas* las ecuaciones cuadráticas, sin importar qué tan complicados sean los números.

*   **Aplicación $USD:** En el mundo de los negocios, se usa para encontrar el "punto de equilibrio". Si "x" representa las unidades vendidas, resolver la ecuación nos dice exactamente cuántas ventas necesitamos para que los ingresos cubran los costos de producción y la ganancia no sea negativa.
*   **Aplicación práctica:** Los ingenieros la utilizan para calcular trayectorias parabólicas. Desde el lanzamiento de un balón hasta el diseño de la curvatura de un puente colgante, la fórmula general nos da las coordenadas exactas.
*   **Situación cotidiana:** Imagina que quieres poner piso nuevo en una habitación y sabes que el largo mide 2 metros más que el ancho. Si tienes el área total, usarás una ecuación cuadrática para conocer las medidas exactas y no desperdiciar material.

---

## Concepto Clave

### Definición
Una ecuación de segundo grado tiene la forma $ax^2 + bx + c = 0$. Para hallar el valor de $x$, utilizamos la siguiente expresión:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

*   **$a$**: El número junto a la $x^2$.
*   **$b$**: El número junto a la $x$.
*   **$c$**: El término independiente (el número solo).
*   **El Discriminante ($D$):** Es la parte dentro de la raíz ($b^2 - 4ac$). Este valor es "el soplón" de la ecuación: nos dice si habrá dos soluciones, una sola, o ninguna (en los números reales).

> [!warning] Error de Novato: El signo de $b$
> La fórmula dice **$-b$**, lo que significa: **"Cambia el signo de b"**. Como dice el Profe Alex, si en tu ecuación $b$ es $-5$, en la fórmula debes escribir $+5$. ¡No lo olvides!

> [!tip] Profe Tip: Cuando $a=1$
> Si no ves ningún número acompañando a la $x^2$, recuerda que $a = 1$. En estos casos, el denominador siempre será **2** (porque $2 \times 1 = 2$). ¡Esto te ahorrará mucho tiempo!

### Regla Mnemotécnica
Para no olvidar el orden del discriminante ($b^2 - 4ac$), recuerda esto:
*"El **B**ebé al cuadrado tiene **4** **A**migos en la **C**asa"*.

---

## Procedimiento Paso a Paso

Un "truco de experto" es calcular las partes por separado para no llenar la hoja de números tachados:

```text
1. IGUALAR A CERO: Mueve todo a la izquierda (o derecha) para que la ecuación termine en "= 0".
2. IDENTIFICAR: Escribe cuánto valen a, b y c con sus signos.
3. CALCULAR EL DISCRIMINANTE (D): Calcula primero D = b² - 4ac.
4. SUSTITUIR Y RESOLVER: Pon los valores en la fórmula, aplica la raíz y obtén x1 (con +) y x2 (con -).
```

---

## Ejemplos Desarrollados

> [!example] Ejemplo 1: Caso Básico con Simplificación
> **Ecuación:** $3x^2 + 2x - 8 = 0$
> 1. **Identificar:** $a = 3, b = 2, c = -8$.
> 2. **Discriminante:** $D = (2)^2 - 4(3)(-8) = 4 + 96 = 100$.
> 3. **Fórmula:** $x = \frac{-2 \pm \sqrt{100}}{6} = \frac{-2 \pm 10}{6}$
> 4. **Resultados:**
>    *   $x_1 = \frac{-2 + 10}{6} = \frac{8}{6} \rightarrow$ **Simplificado:** $\mathbf{4/3}$
>    *   $x_2 = \frac{-2 - 10}{6} = \frac{-12}{6} \rightarrow$ **Resultado:** $\mathbf{-2}$

> [!example] Ejemplo 2: Transposición y Dinero ($USD$)
> **Ecuación:** $2x^2 + 13x + 6 = 5x^2 + 16x + 3$
> El Profe Alex recomienda mover todo al lado donde la $x^2$ quede **positiva**.
> $0 = (5x^2 - 2x^2) + (16x - 13x) + (3 - 6) \rightarrow \mathbf{3x^2 + 3x - 3 = 0}$
> *   **$a=3, b=3, c=-3$**. El discriminante es $D = 3^2 - 4(3)(-3) = 9 + 36 = 45$.
> *   $x = \frac{-3 \pm \sqrt{45}}{6}$. Al usar calculadora para raíces no exactas:
> *   $x_1 \approx 0.618$. En dólares, esto sería **$0.62 USD**.
> *   $x_2 \approx -1.618$.

> [!example] Ejemplo 3: El Caso de la Raíz Imposible
> **Ecuación:** $3x^2 + 2x + 5 = 0$
> 1. **Discriminante:** $D = (2)^2 - 4(3)(5) = 4 - 60 = \mathbf{-56}$.
> 2. **Conclusión:** Como el discriminante es negativo, la raíz $\sqrt{-56}$ no existe en los números reales. **Esta ecuación no tiene solución real.**

> [!example] Ejemplo 4: Ganancia Neta ($USD$)
> **Problema:** Una tienda calcula su éxito con $x^2 - 2x - 3 = 0$, donde $x$ es el precio ideal.
> *   **$a=1, b=-2, c=-3$**. El discriminante es $D = (-2)^2 - 4(1)(-3) = 4 + 12 = 16$.
> *   $x = \frac{2 \pm \sqrt{16}}{2} = \frac{2 \pm 4}{2}$.
> *   $x_1 = 6/2 = \mathbf{3}$ | $x_2 = -2/2 = -1$.
> **Respuesta:** El precio ideal es **$3 USD** (el valor negativo no se aplica a precios reales).

---

## Ejercicios para el Estudiante

### 🟢 Fácil (Raíces exactas)
1. $x^2 - x - 42 = 0$
2. $x^2 + 2x - 15 = 0$
3. $2x^2 + 6x - 20 = 0$
4. $4x^2 - 20x + 25 = 0$

### 🟡 Medio (Simplificación y Distribución)
1. $x(x + 3) = 5x + 3$
2. $2x(3x - 5) = 4x + 8$
3. $(x + 1)(3x - 4) = 2x - 2$
4. $5(2x^2 - 1) + 3 = 2(4x + 3x) - 4$

### 🔴 Avanzado (Modelado $USD$ - Redondear a 2 decimales)
1. El costo de producir $x$ artículos se modela con: $2x^2 + 13x + 6 = 5x^2 + 16x + 3$. Hallar $x$ en dólares.
2. Una inversión rinde según la ecuación: $3x^2 + 3x - 3 = 0$. Calcule el retorno $x$.
3. Ingresos: $x(2x + 1) + 6$. Gastos: $x(5x + 1) + 15x + 3$. ¿En qué punto $x$ se igualan?
4. Determine el precio $x$ que anula la pérdida: $x^2 - x - 42 = 0$.

---

## Respuestas (Para el Docente)

> [!success] Solucionario con Discriminantes ($D$)
> **Fácil:**
> 1) $D=169$; $x=\{7, -6\}$ | 2) $D=64$; $x=\{3, -5\}$ | 3) $D=196$; $x=\{2, -5\}$ | 4) $D=0$; $x=2.5$.
> 
> **Medio:**
> 1) $D=16$; $x=\{3, -1\}$ | 2) $D=388$; $x \approx \{2.81, -0.47\}$ | 3) $D=25$; $x=\{2, -1/3\}$ | 4) $D=144$; $x=\{1, -0.2\}$.
> 
> **Avanzado:**
> 1) $D=45$; $x \approx \$0.62 USD$ | 2) $D=45$; $x \approx \{0.62, -1.62\}$ | 3) $D=-11$; No tiene solución real | 4) $D=169$; $x = \$7 USD$ (se descarta negativo).

---

## Autoevaluación y Cierre

1. **¿Qué información nos da un discriminante negativo?**
   *   Indica que la parábola no toca el eje X y, por tanto, no hay solución en los números reales.
2. **Si en la fórmula ves "$-b$" y tu $b$ original es $-7$, ¿qué número escribes?**
   *   Escribes $7$ (positivo).
3. **Problema Rápido:** Un descuento se modela con $x^2 - 5x + 6 = 0$. ¿Cuáles son los valores de $x$?
   *   a) 2 y 3 
   *   b) 5 y 6
   *   c) -2 y -3
   *(Respuesta: a, con $D=1$)*

**Próxima clase:** ¿Qué hacemos si la raíz no es exacta pero no queremos usar decimales? Aprenderemos a **simplificar radicales** para obtener respuestas elegantes y profesionales.

---
[[Clase 02 — Métodos de Factorización | ← Clase Anterior]] | [[Índice de Álgebra | Inicio]] | [[Clase 04 — Raíces no exactas y Simplificación | Próxima Clase →]]