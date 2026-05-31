# Clase 08 — Rectas paralelas, perpendiculares y posiciones relativas

#algebra #parallelandperp

Curso: [[00 - Índice del curso]] | Bloque 3 | Lección 8 de 11

> [!info] 🧭 Navegación
> - [[#relevancia-y-aplicaciones|Relevancia y aplicaciones]]
> - [[#fundamentos-teóricos|Concepto clave]]
> - [[#metodología-operativa|Procedimiento paso a paso]]
> - [[#bloques-de-ejemplos-prácticos|Ejemplos prácticos]]
> - [[#entrenamiento|Ejercicios]]
> - [[#evaluación-rápida|Autoevaluación]]

---

## RELEVANCIA Y APLICACIONES

La inclinación de una recta, conocida como **pendiente** ($m$), es el factor que determina si dos trayectorias están destinadas a cruzarse o si se mantendrán siempre a la misma distancia.

*   **💵 Aplicación USD:** Imagina dos carteras de inversión. Si ambas crecen con la misma tasa de interés (misma pendiente), pero una inició con $100$ USD y la otra con $500$ USD, sus gráficas serán rectas paralelas: crecen igual, pero la segunda siempre tendrá una ventaja constante de $400$ USD.
*   **🏗️ Aplicación práctica:** En la arquitectura, las vigas que sostienen un techo deben ser perfectamente paralelas para distribuir el peso de forma equitativa y evitar que la estructura colapse.
*   **📊 Situación cotidiana:** El diseño de los carriles en una autopista o las líneas que delimitan las pistas de atletismo son ejemplos vitales donde las rectas deben mantener la misma pendiente para ser seguras.

---

## FUNDAMENTOS TEÓRICOS (Concepto clave)

### Definiciones sencillas
*   **Rectas Paralelas:** Tienen la **misma inclinación** ($m_1 = m_2$) y nunca se tocan.
*   **Rectas Perpendiculares:** Se cruzan formando una "L" perfecta (ángulo de 90°). Sus pendientes son "recíprocas y opuestas".
*   **Posiciones Relativas:** 
    *   *Coincidentes:* Es la misma recta expresada de forma distinta. Sus coeficientes son proporcionales (ej: si multiplicas $3x + 2y - 5 = 0$ por dos, obtienes $6x + 4y - 10 = 0$; ambas son la misma recta).
    *   *Secantes:* Son el estado "por defecto". Si las pendientes no son iguales, las rectas se cortarán en algún punto del infinito.

> [!warning] Error Común
> El error más frecuente ocurre al aplicar la propiedad distributiva con pendientes negativas. Por ejemplo, al calcular $-3(x + 3)$, muchos estudiantes escriben $-3x + 9$ por error. Lo correcto es multiplicar el signo también: $-3 \cdot x = -3x$ y $-3 \cdot 3 = -9$.

> [!tip] Reglas mnemotécnicas
> - **Paralelas = Pendientes Gemelas.**
> - **Perpendiculares = Voltear y Cambiar.** (Si tienes $3/4$, "volteas" la fracción a $4/3$ y "cambias" el signo a $-4/3$).

---

## METODOLOGÍA OPERATIVA (Procedimiento paso a paso)

Para hallar la ecuación de una recta paralela a otra pasando por un punto $(x_1, y_1)$, sigue este proceso:

```text
PASO 1: Identificar la pendiente (m1) de la recta conocida. 
        Si no está despejada, deja sola a la "y" para ver el número que acompaña a "x".
PASO 2: Asignar esa misma pendiente a nuestra nueva recta (m2 = m1).
PASO 3: Sustituir el punto dado (x1, y1) y la pendiente en la fórmula 
        punto-pendiente: y - y1 = m(x - x1).
PASO 4: Resolver operaciones y despejar "y" para la forma explícita 
        o igualar a cero para la forma general.
```

---

## BLOQUES DE EJEMPLOS PRÁCTICOS

> [!example] Ejemplo 1: Caso Básico
> **Problema:** Hallar la recta que pasa por $(2, -1)$ y es paralela a $y = 2x + 3$.
> 1. Pendiente conocida: $m = 2$.
> 2. Nueva recta: Usamos $m = 2$ y punto $(2, -1)$.
> 3. Sustitución: $y - (-1) = 2(x - 2) \rightarrow y + 1 = 2x - 4$.
> 4. Resultado: **$y = 2x - 5$**.

> [!example] Ejemplo 2: Caso con Signos
> **Problema:** Hallar la recta que pasa por $(-3, 4)$ y es paralela a $y = -3x + 1$.
> 1. Pendiente: $m = -3$.
> 2. Sustitución: $y - 4 = -3(x - (-3)) \rightarrow y - 4 = -3(x + 3)$.
> 3. Desarrollo: $y - 4 = -3x - 9$.
> 4. Resultado: **$y = -3x - 5$**.

> [!example] Ejemplo 3: Caso Avanzado (Forma General)
> **Problema:** Hallar la recta que pasa por $(-2, 3)$ y es paralela a $y - 2x - 3 = 0$.
> 1. Despejamos la original: $y = 2x + 3$. La pendiente es $m = 2$.
> 2. Nueva recta: $y - 3 = 2(x - (-2)) \rightarrow y - 3 = 2(x + 2)$.
> 3. Propiedad distributiva: $y - 3 = 2x + 4$.
> 4. Forma General: Pasamos todo a un lado: $-2x + y - 3 - 4 = 0$.
> 5. Resultado: **$-2x + y - 7 = 0$** (o $2x - y + 7 = 0$).

> [!example] Ejemplo 4: Aplicación USD (Suscripciones)
> **Problema:** El servicio "StreamA" tiene un **Costo Mensual (m)** de $5$ USD y un **Costo Inicial/Deuda (b)** de $-10$ USD ($y = 5x - 10$). El servicio "StreamB" tiene el mismo costo mensual pero inicia sin deuda ($y = 5x$).
> - Ambas tienen $m = 5$.
> - Al ser paralelas, la diferencia de $10$ USD se mantendrá por siempre; nunca cruzarán sus precios.

---

## ENTRENAMIENTO

### 🟢 Fácil: Identificación
Indica la pendiente de una recta paralela ($m_{par}$) y una perpendicular ($m_{per}$):
1. $y = 4x - 5$
2. $y = -2x + 1$
3. $y = \frac{2}{3}x - 8$
4. $y = x + 5$

### 🟡 Medio: Construcción
Halla la ecuación explícita ($y = mx + b$) de la recta paralela que pasa por el punto:
1. Pasa por $(1, 2)$ y es paralela a $y = 3x - 1$.
2. Pasa por $(0, -4)$ y es paralela a $y = -5x + 2$.
3. Pasa por $(-2, -1)$ y es paralela a $y = \frac{1}{2}x + 3$.
4. Pasa por $(4, 3)$ y es paralela a $y = 2x$.

### 🔴 Avanzado: Aplicación y Análisis
1. Dos barcos siguen las rutas $R_1: y = 2x + 5$ y $R_2: -4x + 2y - 10 = 0$. ¿Son rutas paralelas, secantes o coincidentes?
2. Un ahorro en USD sigue la función $y = 10x + 50$. Si otro plan de ahorro es paralelo y pasa por el punto $(0, 20)$, ¿cuál es su ecuación?
3. Determina si las rectas $y = 3x - 2$ y $y = -\frac{1}{3}x + 5$ son perpendiculares. Justifica.
4. Halla la ecuación general de la recta paralela a $2x + y - 5 = 0$ que pasa por $(1, 1)$.

### ✅ Respuestas para el docente
*   **Fácil:** 
    1. $m_{par} = 4$; $m_{per} = -1/4$ (invertir y cambiar signo).
    2. $m_{par} = -2$; $m_{per} = 1/2$.
    3. $m_{par} = 2/3$; $m_{per} = -3/2$.
    4. $m_{par} = 1$; $m_{per} = -1$.
*   **Medio:** 
    1. $y = 3x - 1$ (Es la misma recta).
    2. $y = -5x - 4$.
    3. $y = \frac{1}{2}x$.
    4. $y = 2x - 5$.
*   **Avanzado:** 
    1. **Coincidentes.** Si despejas $R_2$: $2y = 4x + 10 \rightarrow y = 2x + 5$. Son idénticas.
    2. $y = 10x + 20$.
    3. **Sí.** Al multiplicar $3 \cdot (-1/3) = -1$ (cumple la condición de perpendicularidad).
    4. $2x + y - 3 = 0$.

---

## EVALUACIÓN RÁPIDA

1.  **¿Qué condición deben cumplir dos ecuaciones en forma general para ser coincidentes?**
    *   Sus coeficientes deben ser proporcionales (multiplicados por el mismo número).
2.  **Si una recta tiene $m = \frac{3}{4}$, aplica la regla "Voltear y Cambiar" para hallar la pendiente perpendicular.**
    *   Invierto: $4/3$. Cambio signo: $-4/3$.
3.  **Dos amigos ahorran $15$ USD por semana ($m = 15$). Si uno empezó con $100$ USD y otro con $200$ USD, ¿se encontrarán sus ahorros alguna vez?**
    *   No, porque sus gráficas son **paralelas** (misma pendiente, distinto intercepto).

---

## CIERRE Y PROYECCIÓN

Hoy aprendimos que la pendiente define la relación espacial entre dos rectas. En la **Clase 09**, exploraremos qué sucede cuando las rectas son **secantes** y aprenderemos a calcular el punto exacto de su encuentro mediante **Sistemas de Ecuaciones**.

> [!info] 🧭 Navegación
> - [[#relevancia-y-aplicaciones|Relevancia y aplicaciones]]
> - [[#fundamentos-teóricos|Concepto clave]]
> - [[#metodología-operativa|Procedimiento paso a paso]]
> - [[#bloques-de-ejemplos-prácticos|Ejemplos prácticos]]
> - [[#entrenamiento|Ejercicios]]
> - [[#evaluación-rápida|Autoevaluación]]