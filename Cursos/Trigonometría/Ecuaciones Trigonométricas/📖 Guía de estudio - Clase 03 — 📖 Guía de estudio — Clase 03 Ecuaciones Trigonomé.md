# 📖 Guía de estudio — Clase 03: Ecuaciones Trigonométricas

## 1. RESUMEN DE CONCEPTOS CLAVE

> [!info] 📌 Conceptos clave
> - **Definición de resolución:** Resolver una ecuación trigonométrica consiste en hallar el valor del ángulo $x$ (la variable) que hace que la igualdad sea matemáticamente verdadera.
> - **Aislamiento de la función:** El primer paso fundamental es realizar el despeje de la función trigonométrica (dejar el $\sin(x)$, $\cos(x)$, etc., solo en un lado de la igualdad) tratándola como una incógnita algebraica común.
> - **Herramientas de apoyo:** Se debe utilizar la **tabla de ángulos notables** para identificar el ángulo de referencia inicial y el **círculo trigonométrico** para visualizar su posición en los distintos cuadrantes.
> - **Rango de soluciones:** Debido a la naturaleza cíclica de las funciones, suelen existir múltiples soluciones. Generalmente se buscan los valores comprendidos en una vuelta completa, es decir, entre $0^\circ$ y $360^\circ$ ($0$ y $2\pi$ radianes).

## 2. TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ecuación Trigonométrica** | Expresión donde se debe encontrar el valor de la variable (ángulo) dentro de una función dada. |
| **Seno de $30^\circ$ / $\pi/6$** | Valor numérico de $\frac{1}{2}$ o $0.5$. |
| **Coseno de $45^\circ$ / $\pi/4$** | Valor numérico de $\frac{\sqrt{2}}{2}$. |
| **Solución en el II Cuadrante** | Se aplica $180^\circ - \text{ángulo de referencia}$ (usar cuando la función $\sin$ es positiva en dicho cuadrante). |
| **Solución en el IV Cuadrante** | Se aplica $360^\circ - \text{ángulo de referencia}$ (usar cuando la función $\cos$ es positiva en dicho cuadrante). |

---

## 3. EJEMPLOS RESUELTOS ADICIONALES

````ad-example
title: Ejemplo A — Despeje de Seno
**Ejercicio:** Resolver la ecuación $2\sin(x) + 3 = 4$

**Análisis pedagógico:**
1. **Despeje algebraico:** Primero restamos $3$ en ambos lados y luego dividimos por $2$.
   $2\sin(x) = 4 - 3 \implies 2\sin(x) = 1$
   $\sin(x) = \frac{1}{2}$
2. **Identificación del ángulo de referencia:** Consultamos la tabla de ángulos notables. El ángulo cuyo seno es $\frac{1}{2}$ es $x = 30^\circ$ (o $\frac{\pi}{6}$ radianes). Esta es nuestra primera solución ($x_1$).
3. **Lógica de cuadrantes:** El resultado del seno es positivo ($+1/2$). El seno es positivo en el I y II cuadrante. 
4. **Cálculo de la segunda solución ($x_2$):** En el II cuadrante, medimos $30^\circ$ desde el **eje X** hacia arriba:
   $x_2 = 180^\circ - 30^\circ = 150^\circ$ (equivalente a $\frac{5\pi}{6}$ radianes).

**Soluciones finales:** $x_1 = 30^\circ$ ($\frac{\pi}{6}$ rad) y $x_2 = 150^\circ$ ($\frac{5\pi}{6}$ rad).
````

````ad-example
title: Ejemplo B — Variación de inversión en $USD
**Escenario:** Un analista financiero modela el ciclo de una inversión donde el valor fluctúa. Se desea hallar la fase $x$ (momento del ciclo) en la que el valor alcanza exactamente $\sqrt{2}$ USD, siguiendo la ecuación: $2\cos(x) = \sqrt{2}$.

**Procedimiento:**
1. **Aislar la fase:** Despejamos la función coseno pasando el $2$ a dividir:
   $\cos(x) = \frac{\sqrt{2}}{2}$
2. **Ángulo de referencia:** Por tabla de ángulos notables, sabemos que el $\cos(45^\circ) = \frac{\sqrt{2}}{2}$. Por tanto, la fase inicial es $x = 45^\circ$ ($\frac{\pi}{4}$ rad).
3. **Ubicación en el círculo:** El coseno es positivo en el I y IV cuadrante. 
   - En el I cuadrante: $45^\circ$.
   - En el IV cuadrante: Medimos $45^\circ$ desde el **eje X** hacia abajo: $360^\circ - 45^\circ = 315^\circ$ (equivalente a $\frac{7\pi}{4}$ radianes).

**Resultado:** Los momentos de fase donde la inversión alcanza el valor meta son $45^\circ$ y $315^\circ$.
````

---

## 4. EJERCICIOS DE REPASO

````ad-abstract
title: 🟢 Fácil
Determine el valor de $x$ para la ecuación $\sin(x) = \frac{1}{2}$. Proporcione únicamente la primera solución positiva expresada tanto en grados como en su equivalente en radianes.
````

````ad-abstract
title: 🟡 Medio
Resuelva la ecuación $4\sin(\theta) + 5 = 7$. 
*Pista:* Al despejar, la ecuación se simplifica a $\sin(\theta) = \frac{1}{2}$. Encuentre todas las soluciones posibles para $\theta$ en el rango de $0^\circ \leq \theta \leq 360^\circ$.
````

````ad-abstract
title: 🔴 Avanzado (Aplicación $USD)
Para verificar una proyección de ganancias, un estudiante debe comprobar si los ángulos $45^\circ$ y $315^\circ$ satisfacen la condición $2\cos(x) = \sqrt{2}$. 
**Reto:** Utilice su calculadora para realizar la comprobación: introduzca la operación $2 \times \cos(\text{ángulo})$ y verifique si el resultado es aproximadamente $1.41$ (el valor decimal de $\sqrt{2}$). Justifique por qué ambos ángulos arrojan el mismo resultado positivo basándose en la posición del eje X.
````

---

## 5. CONSEJO DE ESTUDIO

> [!tip] 💡 Consejo de estudio
> No intentes memorizar mecánicamente si debes sumar o restar $180^\circ$. La clave del éxito es la **visualización mental del círculo trigonométrico**. Recuerda que todos los ángulos se miden partiendo desde el **eje X**. Si entiendes en qué cuadrantes cada función es positiva o negativa, podrás ubicar las soluciones de cualquier ecuación de forma lógica y sin errores de signo.