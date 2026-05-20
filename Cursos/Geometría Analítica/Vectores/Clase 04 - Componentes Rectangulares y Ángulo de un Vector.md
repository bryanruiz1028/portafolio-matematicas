# Clase 04 — Componentes Rectangulares y Ángulo de un Vector

#algebra #componentesrect

Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 4 de 6

[!info] 🧭 Navegación
Anterior: [[Clase 03 — Representación de Vectores]] | Índice: [[00 - Índice del curso]] | Siguiente: [[Clase 05 — Suma de Vectores por Componentes]]

---

[!info] 🌍 Relevancia y aplicaciones
La **descomposición vectorial** es la herramienta fundamental que permite simplificar movimientos diagonales o fuerzas complejas en dos direcciones perpendiculares independientes. Es el pilar del análisis estructural en ingeniería y de la optimización de trayectorias.

*   **💵 [Aplicación con $USD]:** Podemos representar un portafolio de inversión como un vector. La magnitud es el capital total, mientras que sus componentes revelan la estructura del riesgo: la componente horizontal ($V_x$) representa el capital protegido (inversión fija) y la componente vertical ($V_y$) el rendimiento variable (riesgo).
*   **🏗️ [Aplicación práctica]:** En arquitectura, permite calcular con precisión cuánta carga soporta verticalmente una columna y cuánto empuje lateral recibe un muro debido al viento.
*   **📊 [Situación cotidiana]:** Al caminar por una ciudad con diseño de damero (cuadrícula), cualquier desplazamiento "en diagonal" es en realidad la combinación de caminar un número de calles hacia el Este y otro hacia el Norte.

---

[!note] 📌 ¿Qué es la Descomposición Vectorial?
Descomponer un vector es hallar sus **componentes rectangulares**, que son las "proyecciones" o sombras del vector sobre los ejes X (horizontal) e Y (vertical). 

Desde la didáctica matemática, entendemos que el vector original actúa como la **hipotenusa** de un triángulo rectángulo, donde las componentes $V_x$ y $V_y$ son los **catetos** (adyacente y opuesto, respectivamente). Esta relación geométrica es la que nos permite utilizar razones trigonométricas para navegar entre la magnitud escalar y sus partes rectangulares.

[!warning] ⚠️ ¡Atención al Ángulo y a la Calculadora!
1. **El origen del ángulo:** Las fórmulas estándar funcionan solo si el ángulo "toca" el eje horizontal (Este u Oeste). Si el problema te da un ángulo que nace del Norte o Sur, debes calcular su **complementario** restándolo de 90° antes de operar.
2. **Modo DEG:** Antes de cualquier cálculo, verifica que tu calculadora esté en modo **DEGREES (DEG)**. Si aparece "RAD" o "GRAD", tus resultados serán incorrectos.

[!tip] 💡 Regla mnemotécnica de experto
Si el ángulo toca el eje **X**, recuerda esta asociación:
*   **X** se calcula con **C**oseno (**C-X**).
*   **Y** se calcula con **S**eno (**S-Y**).

---

[!important] 📋 Procedimiento paso a paso
Para realizar una descomposición vectorial precisa, siga este protocolo:

```text
PASO 1 → Identificar la magnitud (V) y el ángulo de dirección (θ).
PASO 2 → Ajuste de ángulo: Si el ángulo nace del eje vertical (N/S), 
         calcula: θ_ajustado = 90° - θ_dado.
PASO 3 → Análisis de Signos por Cuadrante:
         - Hacia el Este/Norte: Signo (+)
         - Hacia el Oeste/Sur: Signo (-)
PASO 4 → Aplicar funciones trigonométricas:
         Vx = ± V · cos(θ)
         Vy = ± V · sen(θ)
```

---

### 📝 Ejemplos Desarrollados

**Ejemplo 1: Análisis Básico (Primer Cuadrante)**
*Vector A: 6.00 cm, 30° Norte del Este.*
1.  **Datos:** Magnitud = 6.00 cm. El ángulo (30°) toca el Este (eje X), se usa directo.
2.  **Signos:** Norte (+) y Este (+). Ambos son positivos.
3.  **Componente X (Cateto adyacente):** $A_x = 6.00 \cdot \cos(30^\circ) = 5.20$ cm.
4.  **Componente Y (Cateto opuesto):** $A_y = 6.00 \cdot \sin(30^\circ) = 3.00$ cm.

**Ejemplo 2: Cambio de Eje y Signos (Tercer Cuadrante)**
*Vector M: 8.00 cm, Sur 34° Oeste.*
1.  **Ajuste de Ángulo:** El ángulo toca el Sur (eje Y). Calculamos el complementario: $90^\circ - 34^\circ = 56^\circ$. Ahora el ángulo toca el Oeste.
2.  **Signos:** Sur (-) y Oeste (-).
3.  **Componente X:** $M_x = -8.00 \cdot \cos(56^\circ) = -4.47$ cm.
4.  **Componente Y:** $M_y = -8.00 \cdot \sin(56^\circ) = -6.63$ cm.

**Ejemplo 3: Proceso Inverso (Hallar el Ángulo)**
*¿Cuál es el ángulo de un vector con componentes $V_x = 5$ y $V_y = 3$?*
1.  **Fórmula:** $\theta = \tan^{-1} \left( \frac{|V_y|}{|V_x|} \right)$.
2.  **Cálculo:** $\theta = \tan^{-1} (3 / 5) = \tan^{-1} (0.6)$.
3.  **Resultado:** $\theta = 30.96^\circ$.
*Tip de experto: Siempre usa valores absolutos (positivos) en la división para obtener el ángulo agudo con respecto al eje X.*

**Ejemplo 4: Aplicación Financiera ($USD)**
*Un capital de $12,000 USD se invierte con un "ángulo de agresividad" de 25°.*
1.  **Inversión Fija (Componente X):** $12,000 \cdot \cos(25^\circ) = 10,875.70$ USD.
2.  **Riesgo Variable (Componente Y):** $12,000 \cdot \sin(25^\circ) = 5,071.43$ USD.

---

### ✍️ Ejercicios para el Estudiante

[!abstract] 🟢 Nivel Verde (Cálculo Directo)
Determine las componentes $V_x$ e $V_y$ para los siguientes vectores en el primer cuadrante (Norte-Este):
1.  10.00 m a 20°.
2.  5.00 m a 45°.
3.  15.00 m a 10°.
4.  20.00 m a 60°.

[!abstract] 🟡 Nivel Amarillo (Análisis de Ángulos y Signos)
Calcule las componentes cuidando el ángulo complementario y la dirección:
1.  12.00 cm, Norte 80° Oeste.
2.  8.00 cm, Sur 20° Este.
3.  Halle el ángulo si $V_x = 6.00$ y $V_y = 7.00$.
4.  Halle el ángulo si $V_x = -4.00$ y $V_y = -2.00$.

[!abstract] 🔴 Nivel Rojo (Modelado Financiero $USD)
1.  Un fondo de $500.00 USD tiene un ángulo de riesgo de 30°. Calcule sus componentes de estabilidad (x) y variabilidad (y).
2.  Un capital de $1,000.00 USD se desvía 15° hacia pérdidas (Sur del Este). Calcule $V_x$ y $V_y$.
3.  Si la variabilidad es de $200.00 USD ($V_y$) y la base fija es de $800.00 USD ($V_x$), ¿cuál es el ángulo de riesgo?
4.  Un portafolio de $2,500.00 USD con ángulo de 40° Sur del Este. Calcule sus componentes.

[!success] ✅ Respuestas Sugeridas
*   **Verde:** 1) $x=9.40, y=3.42$ | 2) $x=3.54, y=3.54$ | 3) $x=14.77, y=2.60$ | 4) $x=10.00, y=17.32$.
*   **Amarillo:** 1) (Usa 10°) $x=-11.82, y=2.08$ | 2) (Usa 70°) $x=2.74, y=-7.52$ | 3) $49.40^\circ$ | 4) $26.57^\circ$.
*   **Rojo:** 1) $x=433.01, y=250.00$ | 2) $x=965.93, y=-258.82$ | 3) $14.04^\circ$ | 4) $x=1915.11, y=-1606.97$.

---

### 🏁 Autoevaluación y Cierre

[!question] ❓ Comprueba tu aprendizaje
1.  **¿Qué sucede si utilizas el ángulo que toca el eje Norte sin restarlo de 90°?**
    *   Tus componentes quedarán invertidas ($V_x$ será $V_y$ y viceversa).
2.  **Si un vector tiene componentes $V_x = -3.00$ y $V_y = 4.00$, ¿en qué cuadrante se encuentra?**
    *   En el segundo cuadrante (Norte del Oeste).
3.  **En el modelado financiero de esta clase, ¿qué representa físicamente el cateto adyacente?**
    *   La componente de inversión fija o capital base.

[!tip] 💡 En la próxima clase
Dominar la descomposición es el 90% del éxito en física de vectores. En la siguiente sesión, utilizaremos estas "piezas" para sumar múltiples vectores y hallar una única **Fuerza Resultante**.

---
[!info] 🧭 Navegación
Anterior: [[Clase 03 — Representación de Vectores]] | Índice: [[00 - Índice del curso]] | Siguiente: [[Clase 05 — Suma de Vectores por Componentes]]