# 📖 Guía de estudio — Clase 07: Resolución de ecuaciones cuadráticas (Método Po-Shen Loh)

> [!info] 📌 Conceptos clave
> - **Condición de inicio ($a=1$):** Para aplicar este método, el coeficiente de $x^2$ debe ser **1**. Si la ecuación comienza con un número distinto (como $2x^2$ o $5x^2$), debemos dividir toda la ecuación por ese número antes de continuar.
> - **El Centro ($t$):** Es el punto medio exacto o promedio entre las dos soluciones de la ecuación. Se calcula como $t = -b/2$. **¡Cuidado con los signos!** Si $b$ es negativo, la fórmula se convierte en positivo (ej. si $b = -6$, entonces $t = -(-6)/2 = 3$).
> - **La Distancia ($u$):** Representa la **distancia horizontal** desde el centro hasta cada una de las raíces. Se obtiene resolviendo la relación entre el centro al cuadrado y el término independiente ($c$).
> - **Lógica del método:** En lugar de memorizar una fórmula mecánica, aprovechamos la simetría de la parábola. Buscamos dos números cuya suma sea $-b$ y cuyo producto sea $c$, usando el centro como punto de partida.

## TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ecuación estándar** | $x^2 + bx + c = 0$ (El coeficiente $a$ debe ser 1). |
| **Centro ($t$)** | El promedio de las raíces: $t = -\frac{b}{2}$ |
| **Distancia al cuadrado ($u^2$)** | Ecuación de Po-Shen Loh: $t^2 - u^2 = c$ |
| **Soluciones finales** | Valores de $x$ que resuelven la ecuación: $x = t \pm u$ |

---

## SECCIÓN DE EJEMPLOS RESUELTOS ADICIONALES

```ad-example
title: Ejemplo A — Solución con números enteros
**Enunciado:** Resolver $x^2 + 2x - 3 = 0$.

**Paso 1: Hallar el centro ($t$)**
Identificamos $b = 2$.
$t = -\frac{2}{2} = -1$

**Paso 2: Hallar la distancia ($u$)**
Usamos la fórmula $t^2 - u^2 = c$, con $c = -3$.
$(-1)^2 - u^2 = -3$
$1 - u^2 = -3$
$1 + 3 = u^2$
$4 = u^2 \Rightarrow u = \sqrt{4} = 2$

**Resultado final:**
$x_1 = t + u = -1 + 2 = 1$
$x_2 = t - u = -1 - 2 = -3$
```

```ad-example
title: Ejemplo B — Aplicación: Cálculo de ingresos
**Enunciado:** Una tienda de artículos escolares modela su ganancia con la ecuación $x^2 - 6x + 8 = 0$. ¿Cuántas unidades "x" deben venderse para alcanzar el punto de equilibrio (ganancia igual a cero)?

**Pasos lógicos:**
1. **Identificar valores:** $b = -6$, $c = 8$.
2. **Calcular centro ($t$):** Aplicamos el cambio de signo: $t = -\frac{(-6)}{2} = 3$.
3. **Calcular distancia ($u$):**
   $3^2 - u^2 = 8$
   $9 - u^2 = 8 \Rightarrow 9 - 8 = u^2 \Rightarrow u^2 = 1 \Rightarrow u = 1$.
4. **Soluciones finales:**
   $x_1 = 3 + 1 = 4$
   $x_2 = 3 - 1 = 2$

**Resultado:** Se deben vender 2 o 4 unidades para que la ganancia sea cero. ✅
```

---

## EJERCICIOS DE REPASO

```ad-abstract
title: 🟢 Fácil
color: 0, 200, 0
Resuelva las siguientes ecuaciones donde $u$ es un número entero:
1. $x^2 - 4x + 3 = 0$
2. $x^2 + 4x + 4 = 0$ *(Nota: Si $u=0$, existe una única solución real).*
3. $x^2 - 6x + 5 = 0$
```

```ad-abstract
title: 🟡 Medio
color: 255, 255, 0
Resuelva aplicando simplificación previa o trabajando con raíces no exactas:
1. $x^2 - 8x + 13 = 0$ (Deje el resultado expresado con raíz).
2. $2x^2 - 2x - 12 = 0$ (Divida primero toda la ecuación entre 2).
3. $x^2 - 6x - 4 = 0$ (Obtenga el valor de $u$ como una raíz cuadrada).
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
color: 200, 0, 0
**Problema:** Una startup tecnológica modela el balance de sus costos de operación mediante la ecuación $x^2 - 6x - 4 = 0$, donde "x" representa miles de dólares. Para fines de auditoría, la empresa necesita hallar los valores de "x" donde el balance es cero (puntos críticos).

**Instrucción:** Calcule las soluciones $x_1$ y $x_2$ utilizando formato decimal.
*(Dato: aproxime $\sqrt{13} \approx 3.61$)*.
```

---

> [!tip] 💡 Consejo de estudio
> No intentes memorizar cada paso como una regla rígida. Lo más importante es entender que el centro $t = -b/2$ es el promedio de las soluciones. Al comprender que estamos buscando dos puntos situados simétricamente a una distancia $u$ de ese centro, estarás razonando matemáticamente en lugar de solo aplicar una fórmula mecánica que podrías olvidar después del examen.