# Clase 04 — Pendiente, ángulo de inclinación y formas de la ecuación de la recta

**Navegación:**
[[Clase 03 — Ecuación de la recta]] | [[Clase 05 — Graficación de funciones lineales]]

---

### 🌍 Relevancia y aplicaciones
> [!info] **¿Por qué es importante esta clase?**
> La pendiente y el ángulo de inclinación nos dicen exactamente hacia dónde se dirige una línea y con qué fuerza lo hace. Estos conceptos son la clave para entender si un precio sube de forma explosiva o si una construcción es segura y funcional.
> - **Dólares ($USD):** El análisis de la tendencia permite predecir si el valor de una moneda subirá o bajará en las próximas horas.
> - **Construcción:** Se utiliza para calcular la inclinación exacta de un techo (pendiente) para asegurar que el drenaje de lluvia sea eficiente.
> - **Vida cotidiana:** Determina la inclinación de una carretera al subir una montaña, ayudando a diseñar caminos que los vehículos puedan transitar.

---

### CONCEPTO CLAVE

> [!note] **Definición para todos**
> La **pendiente ($m$)** es simplemente qué tan "empinada" está una línea (su inclinación). El **ángulo ($\alpha$)** es cuánto se separa la línea del suelo (eje horizontal). La conexión mágica entre ambos es: 
> $$m = \tan(\alpha)$$

> [!warning] **¡Cuidado con los signos!**
> El error más común es no cambiar los signos al mover términos de un lado al otro del igual. Si un término está sumando ($+$), pasa al otro lado restando ($-$). Un signo mal puesto cambiará la dirección de tu recta por completo.

> [!tip] **Regla mnemotécnica**
> Para recordar la fórmula de la pendiente, piensa en un elevador: **"La $y$ arriba (movimiento vertical) y la $x$ abajo (movimiento horizontal)"**.
> $$m = \frac{y_2 - y_1}{x_2 - x_1}$$

---

### PROCEDIMIENTOS PASO A PASO

#### 1. De General a Ordinaria (Explícita o Pendiente-Ordenada)
Este formato es el más útil para conocer la pendiente ($m$) y dónde corta la recta al eje $y$ ($b$).
```text
PASO 1 → Despejar la variable "y".
PASO 2 → Pasar los términos de "x" y el independiente al lado derecho (cambiando signos).
PASO 3 → Si la "y" tiene un coeficiente, dividir cada término de la derecha entre ese número.
PASO 4 → Identificar: el número con la "x" es la pendiente (m) y el número solo es el corte (b).
```

#### 2. De General a Simétrica (Segmentaria)
Ideal para graficar rápido, ya que nos da los puntos de corte en ambos ejes ($x$ y $y$).
```text
PASO 1 → Pasar el término independiente (C) al lado derecho del igual.
PASO 2 → Dividir todos los términos de la ecuación entre ese valor para obtener un "1" a la derecha.
PASO 3 → Simplificar las fracciones para que la "x" y la "y" queden con coeficiente 1.
PASO 4 → Si queda un número multiplicando a la variable, bajarlo como denominador del denominador.
```

---

### EJEMPLOS DESARROLLADOS

> [!example] **Ejemplo 1: De General a Ordinaria (Explícita)**
> **Ejercicio:** Convertir $3x + y - 5 = 0$
> 1. Despejamos la $y$: $y = -3x + 5$.
> 2. **Resultado:** La pendiente ($m$) es $-3$ y el punto de corte con el eje $y$ ($b$) es $5$.

> [!example] **Ejemplo 2: De General a Simétrica (Segmentaria)**
> **Ejercicio:** Convertir $5x + 2y - 10 = 0$
> 1. Pasamos el $-10$: $5x + 2y = 10$.
> 2. Dividimos todo entre 10: $\frac{5x}{10} + \frac{2y}{10} = \frac{10}{10}$.
> 3. Simplificamos: $\frac{x}{2} + \frac{y}{5} = 1$.
> 4. **Interpretación:** La recta corta al eje $x$ en $2$ y al eje $y$ en $5$.

> [!example] **Ejemplo 3: Simplificación "a las malas"**
> **Ejercicio:** Convertir $5x + 2y - 8 = 0$ a forma simétrica.
> 1. Movemos el término independiente: $5x + 2y = 8$.
> 2. Dividimos entre 8: $\frac{5x}{8} + \frac{2y}{8} = 1$.
> 3. **El truco:** Como queremos que la $x$ tenga coeficiente 1, dividimos arriba y abajo por 5 (o simplemente bajamos el 5): $\frac{x}{8/5} + \frac{y}{4} = 1$. Así, el corte en $x$ es la fracción $8/5$.

> [!example] **Ejemplo 4: Aplicación en el Mercado ($USD)**
> **Problema:** El precio de un activo sube de $2 USD a $5 USD en 3 días. Calcula la pendiente.
> 1. Puntos: $(0, 2)$ y $(3, 5)$.
> 2. Aplicamos la fórmula: $m = \frac{5 - 2}{3 - 0} = \frac{3}{3} = 1$.
> 3. **Resultado:** La pendiente es $1 USD/día$, lo que significa que el precio aumenta 1 dólar cada día.

---

### EJERCICIOS PARA EL ESTUDIANTE

> [!attention] **Nota técnica para el ángulo**
> Asegúrate de que tu calculadora esté en modo **"DEG" (Degrees)** antes de calcular el arco tangente ($\tan^{-1}$), de lo contrario obtendrás resultados incorrectos en radianes.

**Nivel Verde (Fácil): Conversión a Ordinaria/Explícita**
1. $2x + y - 8 = 0$
2. $5x + y + 2 = 0$
3. $x - y + 4 = 0$
4. $4x + 2y - 6 = 0$

**Nivel Amarillo (Medio): Ángulo de inclinación ($\alpha = \arctan(m)$)**
1. Hallar el ángulo si $m = 1$.
2. Hallar el ángulo si $m = 0$.
3. Hallar el ángulo si $m = -1$ (Explica qué significa el signo).
4. Hallar el ángulo si $m = 1.5$.

**Nivel Rojo (Avanzado - $USD): Interpretación y Aplicación**
1. El precio del Bitcoin baja de $60,000 USD a $54,000 USD en 2 horas. Calcula la pendiente de devaluación e interpreta el signo.
2. Un activo financiero sube de $10 USD a $25 USD en 5 días. Calcula la pendiente y el ángulo de crecimiento en el gráfico.
3. El dólar se mantiene estable en $40 USD durante 10 días. ¿Cuál es su pendiente y su ángulo de inclinación?
4. Si la pendiente de una acción es $m = 0.75$, ¿cuál es su ángulo de crecimiento?

> [!success] **Respuestas**
> **Verde:** 1) $y = -2x + 8$ | 2) $y = -5x - 2$ | 3) $y = x + 4$ | 4) $y = -2x + 3$.
> **Amarillo:** 1) $45^\circ$ | 2) $0^\circ$ | 3) $-45^\circ$ (Significa que el ángulo se mide hacia abajo del eje X) | 4) $56.31^\circ$.
> **Rojo:** 
> 1) $m = -3,000$ USD/hora (El signo negativo indica que el valor está cayendo).
> 2) $m = 3$ USD/día; $\alpha = 71.56^\circ$.
> 3) $m = 0$ USD/día; $\alpha = 0^\circ$ (Línea totalmente horizontal).
> 4) $\alpha = 36.87^\circ$.

---

### MINI-PRUEBA DE AUTOEVALUACIÓN
1. **Conceptual:** En la forma simétrica $\frac{x}{a} + \frac{y}{b} = 1$, ¿qué representa físicamente el número $a$?
2. **Procedimental:** Si una recta pasa por $(2, 3)$ y $(4, 7)$, ¿cuál es su pendiente?
3. **Interpretación:** Si una gráfica de precios tiene una pendiente de $m = 0.5$, ¿qué significa?
   a) El precio baja 0.5 unidades por día.
   b) El precio sube 0.5 unidades por cada unidad de tiempo.
   c) El precio no cambia.

---

### CIERRE Y NAVEGACIÓN
> [!tip] **Próximo paso**
> ¡Has dominado las formas de la ecuación! Ahora que sabes identificar la pendiente y los cortes con solo mirar la ecuación, en la siguiente clase aprenderás a **graficar estas rectas de forma instantánea** sin hacer tablas de valores.

**Navegación:**
[[Clase 03 — Ecuación de la recta]] | [[Clase 05 — Graficación de funciones lineales]]