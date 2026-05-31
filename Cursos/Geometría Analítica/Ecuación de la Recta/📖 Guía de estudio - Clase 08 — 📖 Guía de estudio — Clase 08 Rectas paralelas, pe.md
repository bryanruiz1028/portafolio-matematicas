# 📖 Guía de estudio — Clase 08: Rectas paralelas, perpendiculares y la ecuación de la recta

> [!info] 📌 Conceptos clave
> ¡Bienvenido! Para dominar la geometría analítica, primero debemos entender cómo se relacionan las rectas en el plano. Aquí tienes los conceptos fundamentales:
> - **La Pendiente ($m$):** Es la medida de inclinación de una recta. Se define como la razón de cambio entre el eje vertical y el eje horizontal ($\frac{\text{cambio en } y}{\text{cambio en } x}$).
> - **Rectas Paralelas:** Son aquellas que mantienen la misma inclinación y nunca se cruzan. Matemáticamente, esto ocurre cuando sus pendientes son iguales: $m_1 = m_2$.
> - **Rectas Perpendiculares:** Son rectas que se cortan formando un ángulo de $90^\circ$. Sus pendientes son **opuestas y recíprocas**, lo que significa que $m_1 \cdot m_2 = -1$.
> - **Rectas Secantes:** Rectas que se cortan en un solo punto porque tienen pendientes diferentes ($m_1 \neq m_2$).
> - **Rectas Coincidentes:** Son, en esencia, la misma recta. Sus ecuaciones son equivalentes o proporcionales.
> - **Identificación:** En la forma explícita ($y = mx + b$), la pendiente $m$ es el coeficiente que acompaña a la $x$.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Pendiente ($m$)** | $m = \frac{\Delta y}{\Delta x} = \frac{\text{Cambio en } y}{\text{Cambio en } x}$ |
| **Ecuación Punto-Pendiente** | $y - y_1 = m(x - x_1)$ |
| **Forma Explícita** | $y = mx + b$ (donde $m$ es la pendiente) |
| **Forma General** | $Ax + By + C = 0$ |
| **Condición Paralela** | $m_1 = m_2$ |
| **Condición Perpendicular** | $m_2 = -\frac{1}{m_1}$ |

## Ejemplos resueltos adicionales

¡Observa cómo aplicamos el álgebra paso a paso para resolver estos desafíos!

````ad-example title: Ejemplo A — Hallar una recta paralela
**Problema:** Hallar la ecuación de la recta que pasa por el punto $(2, -1)$ y es paralela a la recta $y = 2x - 3$.

*   **Paso 1 (Identificar la pendiente):** Al ser paralela a $y = 2x - 3$, la nueva recta debe tener la misma pendiente. Por lo tanto, **$m = 2$**.
*   **Paso 2 (Sustituir en la fórmula punto-pendiente):** Usamos el punto dado $(2, -1)$, donde $x_1 = 2$ y $y_1 = -1$.
    $y - (-1) = 2(x - 2)$
    $y + 1 = 2x - 4$
*   **Paso 3 (Despejar para la forma explícita):**
    $y = 2x - 4 - 1$
*   **Resultado final:** **$y = 2x - 5$**
````

````ad-example title: Ejemplo B — Aplicación de costos paralelos ($USD)
**Problema:** Un servicio "A" cobra un cargo variable de $\$3$ por unidad ($y = 3x + 5$). Halla la ecuación de un servicio "B" que tiene el mismo crecimiento (paralelo) pero pasa por el punto $(1, 4)$.

*   **Paso 1 (Análisis de pendiente):** "Mismo crecimiento" significa que son paralelas. Identificamos la pendiente del servicio A: **$m = 3$**.
*   **Paso 2 (Aplicación de fórmula):** Usamos el punto $(1, 4)$ en nuestra fórmula maestra:
    $y - 4 = 3(x - 1)$
    $y - 4 = 3x - 3$
*   **Paso 3 (Resolución):**
    $y = 3x - 3 + 4$
*   **Resultado final:** **$y = 3x + 1$**
````

## Ejercicios de repaso

¡Es hora de poner a prueba lo aprendido! Resuelve estos desafíos siguiendo los procedimientos anteriores.

````ad-abstract title: 🟢 Nivel Verde — Identificación rápida
Determina si los siguientes pares de rectas son **paralelas**, **perpendiculares** o **secantes**:
1. $y = 5x + 2$  y  $y = 5x - 8$
2. $y = 3x + 1$  y  $y = -\frac{1}{3}x + 4$
3. $y = 2x + 5$  y  $y = 4x + 5$
*Ayuda: Compara las pendientes $m_1$ y $m_2$ de cada par.*
````

````ad-abstract title: 🟡 Nivel Medio — Construcción de la recta
Halla la ecuación de la recta que cumple con lo siguiente:
*   Pasa por el punto $(-3, 4)$.
*   Es **paralela** a la recta $y = -3x + 1$.
*Deja tu respuesta en forma explícita ($y = mx + b$).*
````

````ad-abstract title: 🔴 Nivel Rojo — Desafío de Perpendicularidad ($USD)
**Problema de aplicación:** Si la trayectoria de un cobro de inversión es **perpendicular** a otra que sigue la ecuación $y = 3x$, y debe pasar por el punto $(-1, 2)$, ¿cuál es su ecuación final?
*Pista: Recuerda que para la perpendicular debes "voltear" la pendiente y cambiar su signo.*
````

> [!tip] 💡 Consejo de estudio
> Para hallar la pendiente de una recta perpendicular rápidamente, aplica la técnica de **"voltear y cambiar"**: toma la pendiente original en forma de fracción, inviértela (recíproca) y cámbiale el signo (opuesta). 
> 
> **Importante:** Siempre te resultará más fácil identificar la pendiente si primero **despejas la variable $y$** para llevar la ecuación a su forma explícita. ¡No olvides cuidar los signos al hacer los traslados algebraicos!