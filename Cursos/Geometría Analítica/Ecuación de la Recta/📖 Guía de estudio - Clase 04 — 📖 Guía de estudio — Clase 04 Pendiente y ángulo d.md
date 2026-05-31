# 📖 Guía de estudio — Clase 04: Pendiente y ángulo de inclinación de la recta a partir de dos puntos

> [!info] 📌 Conceptos clave
> - **La Pendiente ($m$):** Es la medida de la inclinación de la recta. Nos dice qué tan "empinada" está una línea.
> - **El Signo importa:** Si la pendiente es **positiva**, la recta sube (hacia la derecha). Si es **negativa**, la recta baja.
> - **Relación Trigonométrica:** Existe una conexión directa entre el álgebra y la trigonometría: $m = \tan(\theta)$.
> - **Interpretación del Ángulo:** Un ángulo positivo se mide hacia arriba desde el eje X; un ángulo negativo indica que la inclinación se mide hacia abajo (sentido de las manecillas del reloj).

### Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Pendiente ($m$)** | $m = \frac{y_2 - y_1}{x_2 - x_1}$ |
| **Ángulo ($\theta$)** | $\theta = \tan^{-1}(m)$ (se obtiene con el botón "Shift" + "tan") |
| **Signo ($+$)** | Indica que la recta es creciente o sube. |
| **Signo ($-$)** | Indica que la recta es decreciente o baja. |

---

### Ejemplos resueltos adicionales

````ad-example title: Ejemplo A — Cálculo de pendiente y ángulo 
**Problema:** Hallar la pendiente ($m$) y el ángulo de inclinación ($\theta$) de la recta que pasa por los puntos $A(-4, 5)$ y $B(2, -1)$.

**Paso 1: Etiquetar y sustituir**
Primero, identificamos nuestras coordenadas para no confundirnos:
$(x_1, y_1) = (-4, 5)$
$(x_2, y_2) = (2, -1)$

Ahora sustituimos en la fórmula. **¡Cuidado aquí!** Siempre usa paréntesis cuando tengas números negativos para evitar el "atrapamiento" de signos:
$m = \frac{-1 - 5}{2 - (-4)}$

**Paso 2: Resolver la aritmética**
En el denominador, recuerda que "menos por menos da más":
$m = \frac{-6}{2 + 4} = \frac{-6}{6} = -1$

**Paso 3: Calcular el ángulo**
Usamos la calculadora presionando **Shift + tan**:
$\theta = \tan^{-1}(-1)$
**Resultado final:** $m = -1$ (la recta baja) y $\theta = -45^\circ$.
````

````ad-example title: Ejemplo B — Depreciación de un equipo en dólares
**Problema:** Un equipo industrial cuesta $5000 al año 0 (nuevo) y su valor baja a $2000 al año 5. ¿Cuál es su ritmo de pérdida de valor?

**Paso 1: Identificar los puntos**
- Punto 1: $(0, 5000)$
- Punto 2: $(5, 2000)$

**Paso 2: Calcular la pendiente ($m$)**
$m = \frac{2000 - 5000}{5 - 0} = \frac{-3000}{5} = -600$

**Paso 3: Calcular el ángulo ($\theta$)**
$\theta = \tan^{-1}(-600) \approx -89.9^\circ$

**💡 Nota del Profesor:** ¿Viste que el ángulo es casi $-90^\circ$? Esto sucede porque el valor de la pendiente ($-600$) es muy grande. Entre mayor sea el número de la pendiente, más vertical será la línea. Aquí, el resultado $m = -600$ significa que el equipo pierde **600 USD por año**.
````

---

### Ejercicios de repaso

````ad-abstract title: 🟢 Fácil
Calcula la pendiente ($m$) para los siguientes pares de puntos (recuerda etiquetar $x_1, y_1, x_2, y_2$ antes de empezar):
1. $(1, 2)$ y $(3, 4)$
2. $(-1, -2)$ y $(4, 3)$
````

````ad-abstract title: 🟡 Medio
Calcula el ángulo de inclinación ($\theta$) para los siguientes casos:
1. Si la pendiente es $m = 1$.
2. Si la pendiente es $m = \sqrt{3}$ (Usa tu calculadora para obtener el valor decimal $1.73$ antes de aplicar la función $\tan^{-1}$).
3. Halla el ángulo si los puntos son $(0, 0)$ y $(1, 1)$.
````

````ad-abstract title: 🔴 Avanzado — Aplicación con $USD
El precio de una suscripción de software sube de $10 USD a $15 USD en un lapso de 2 años.
1. Halla la pendiente y explica qué significa el resultado en **USD/año**.
2. Calcula el ángulo de inclinación de la gráfica de costos (en grados).
````

---

> [!tip] 💡 Consejo de estudio
> **¡Revisa tu calculadora!** Para que tus ángulos sean correctos, asegúrate de que en la parte superior de la pantalla aparezca la letra **"D"** (de *Degrees* o grados). Si ves una "R" o una "G", los resultados serán erróneos.
> Para activar la función $\tan^{-1}$, recuerda siempre presionar primero la tecla **SHIFT** y luego la tecla **TAN**.