# 📖 Guía de estudio — Clase 06: Resolución de la Ecuación Cuadrática

> [!info] 📌 Conceptos clave
> Una ecuación de segundo grado es aquella donde el exponente máximo de la incógnita ($x$) es **2**. Dominar su resolución es fundamental para entender parábolas y resolver problemas financieros complejos.
> - **Estructura estándar:** Se representa siempre como $ax^2 + bx + c = 0$.
> - **Condición indispensable:** El coeficiente $a$ **nunca** puede ser cero ($a \neq 0$); de lo contrario, la ecuación dejaría de ser cuadrática.
> - **Fórmula General:** Es la herramienta universal. Si el valor dentro de la raíz ($b^2 - 4ac$) es negativo, la ecuación **no tiene solución en los números reales**.
> - **Interpretación Gráfica:** Las soluciones o "raíces" son los puntos exactos donde la parábola corta el eje $x$.

## 📋 Tabla de fórmulas y definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ecuación Cuadrática** | Forma estándar: $ax^2 + bx + c = 0$ |
| **Fórmula General** | Conocida también como "Báskara" o "La Chicharronera": $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ |
| **Coeficientes ($a, b, c$)** | Deben tomarse **siempre con su signo**. $a$: acompaña a $x^2$; $b$: acompaña a $x$; $c$: término independiente. |
| **Centro (Po-Shen Loh)** | Punto medio entre las soluciones: $C = \frac{-b}{2}$. **Nota:** Si $a \neq 1$, primero divide toda la ecuación entre el valor de $a$. |

---

## 💡 Ejemplos resueltos

::: ad-example
### Ejemplo A — Aplicación de la Fórmula General
**Enunciado:** Resolver la ecuación $x^2 + 8x + 12 = 0$. ¡Recuerda ir paso a paso!

1.  **Identificar coeficientes:** Aquí $a=1, b=8, c=12$.
2.  **Sustituir en la fórmula:** Como $b=8$, en la fórmula usamos $-b$, es decir, **$-8$**.
    $x = \frac{-(8) \pm \sqrt{(8)^2 - 4(1)(12)}}{2(1)}$
3.  **Operar la raíz:**
    $x = \frac{-8 \pm \sqrt{64 - 48}}{2} \Rightarrow x = \frac{-8 \pm \sqrt{16}}{2} \Rightarrow x = \frac{-8 \pm 4}{2}$
4.  **Obtener soluciones:**
    -   $x_1 = \frac{-8 + 4}{2} = \frac{-4}{2} = -2$
    -   $x_2 = \frac{-8 - 4}{2} = \frac{-12}{2} = -6$
    **Resultado:** Las soluciones son $x = -2$ y $x = -6$.
:::

::: ad-example
### Ejemplo B — Análisis de costos de producción
**Enunciado:** Un emprendimiento determina que su costo de producción mensual sigue la ecuación $x^2 - 10x + 21 = 0$. ¿En qué cantidad de unidades ($x$) el costo es balanceado?

**Resolución mediante Método Po-Shen Loh (Centro y Distancia):**
1.  **Hallar el Centro ($C$):** Cambiamos el signo a $b$ (de $-10$ a $10$) y dividimos entre 2.
    $C = \frac{10}{2} = 5$.
2.  **Establecer la distancia ($u$):** Sea $u$ la distancia desconocida desde el centro $C$ hacia las raíces. Aplicamos $(C - u)(C + u) = c$:
    $(5 - u)(5 + u) = 21 \Rightarrow 25 - u^2 = 21$
3.  **Despejar $u$:**
    $25 - 21 = u^2 \Rightarrow 4 = u^2 \Rightarrow u = 2$.
4.  **Calcular soluciones:**
    -   $x_1 = 5 - 2 = 3$ unidades.
    -   $x_2 = 5 + 2 = 7$ unidades.
    **Conclusión:** El costo se balancea al producir **3** o **7** unidades.
:::

---

## ✍️ Ejercicios de repaso

::: ad-abstract
### 🟢 Bloque: Nivel Fácil
Identifica los coeficientes $a, b, c$ (¡con su signo!) y resuelve las siguientes ecuaciones:
1. $x^2 + 4x + 3 = 0$
2. $x^2 - 6x + 8 = 0$
3. $x^2 + 2x - 15 = 0$
:::

::: ad-abstract
### 🟡 Bloque: Nivel Medio
Organiza la ecuación en su forma estándar ($ax^2 + bx + c = 0$) antes de resolver. ¡Cuidado con los decimales!
1. $x^2 + 5x = -6$
2. $x^2 - 1.5x - 1 = 0$
3. $2x^2 + 8x + 6 = 0$ (Sugerencia: Divide todo entre 2 para que $a=1$ y sea más fácil).
:::

::: ad-abstract
### 🔴 Bloque: Nivel Avanzado (Aplicación Financiera)
¡Recuerda que esto es un reto para ti! Una empresa tecnológica busca su punto de equilibrio financiero mediante la ecuación:
$$2x^2 - 16x + 24 = 0$$
- **Paso 1:** Simplifica la ecuación dividiendo todos los términos entre 2.
- **Paso 2:** Halla los valores de $x$ que satisfacen la ecuación simplificada.
- **Paso 3:** Si cada unidad de $x$ representa un presupuesto de **$1,000 USD**, ¿cuáles son los dos presupuestos exactos en USD donde la empresa no tiene pérdidas ni ganancias?
:::

---

> [!tip] 💡 Consejo de estudio
> ¡No dejes que los signos te confundan, ve con calma! El error más común es olvidar el **cambio de signo de $b$** al calcular el centro o sustituir en la fórmula. Escribe siempre tus coeficientes a un lado. Al finalizar, haz una verificación mental: suma tus dos soluciones y divide entre 2; ese resultado **debe ser igual** a $-b/2$. ¡Si coincide, vas por buen camino!