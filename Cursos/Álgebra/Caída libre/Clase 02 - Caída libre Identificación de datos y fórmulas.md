# Clase 02 — Caída libre: Identificación de datos y fórmulas
#algebra #cadalibre

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 4

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 4

> [!info] 🧭 Navegación
> [[Clase 01 - Introducción a la Caída Libre y la Gravedad|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | | [[Clase 03 - Caída libre Gravedad lunar, lanzamientos y aplicaciones con|Clase 03 ➡]]

---

> [!info] 🌍 Relevancia y aplicaciones
> El dominio de la caída libre permite predecir comportamientos físicos sin mediciones directas. En el mundo real, esto se traduce en:
> 
> *   💵 **Finanzas:** Evaluar el riesgo de activos. Si un sensor de $1,200 USD cae, conocer la velocidad de impacto define si la garantía cubre el daño por negligencia o falla técnica.
> *   🏗️ **Ingeniería:** Calcular la altura de edificios o profundidad de pozos simplemente midiendo el tiempo de caída de un objeto.
> *   📊 **Cotidiano:** Determinar la velocidad con la que un objeto golpea el suelo para diseñar empaques de protección efectivos.

---

> [!note] 📌 ¿Qué es Caída libre?
> Es un movimiento vertical donde un objeto se desplaza únicamente bajo la influencia de la gravedad ($g$). Para resolver problemas, debemos identificar las 5 variables fundamentales y sus unidades:
> 
> | Variable | Magnitud | Unidad (SI) |
> | :--- | :--- | :--- |
> | $v_0$ | Velocidad inicial | $m/s$ |
> | $v_f$ | Velocidad final | $m/s$ |
> | $g$ | Gravedad | $m/s^2$ |
> | $t$ | Tiempo | $s$ |
> | $y$ | Altura / Distancia | $m$ |

> [!warning] ⚠️ Reglas de Oro: Signos y Estados
> 1. **Dirección:** Si el objeto **baja**, la gravedad es positiva ($9,8 m/s^2$). Si el objeto **sube**, la gravedad es negativa ($-9,8 m/s^2$) porque frena el movimiento.
> 2. **Punto Máximo:** En un lanzamiento hacia arriba, cuando el objeto alcanza su altura máxima, su **$v_f$ es siempre $0 m/s$**.
> 3. **Desde el reposo:** Si el problema dice "se deja caer" o "se suelta", la **$v_0$ es $0 m/s$**.

> [!tip] 🧠 El "Ojímetro" de la Física (Logic Check)
> La gravedad en la Tierra es aproximadamente $10 m/s^2$. Esto significa que, cada segundo que un objeto cae, su velocidad aumenta en $10 m/s$. Si cae por 3 segundos, su velocidad final debe estar cerca de los $30 m/s$. ¡Usa esto para verificar si tu resultado tiene sentido!

---

### Procedimiento para elegir fórmulas

Para seleccionar la fórmula correcta sin confundirse, aplicamos la técnica de la **Variable Ausente**:

```text
PASO 1 → Listar los 3 datos conocidos (ej. v0, g, t).
PASO 2 → Identificar la variable que se busca (la incógnita).
PASO 3 → Identificar la "variable ausente" (la que no aparece, no se conoce y no se pregunta).
PASO 4 → Seleccionar la fórmula que NO contenga esa variable ausente.
```

---

### Ejemplos Resueltos

> [!abstract] Ejemplo 1: Caída desde reposo
> **Problema:** Una piedra se deja caer y choca contra el piso 5 segundos después. Calcula la altura.
> *   **Datos:** $v_0 = 0 m/s$, $t = 5 s$, $g = 9,8 m/s^2$ (baja).
> *   **Busco:** $y$.
> *   **Variable ausente:** $v_f$.
> *   **Fórmula:** $y = v_0 \cdot t + \frac{g \cdot t^2}{2}$
> *   **Solución:** $y = 0 \cdot (5) + \frac{9,8 \cdot (5)^2}{2} = \frac{9,8 \cdot 25}{2} = 122,5 m$.

> [!abstract] Ejemplo 2: Tiempo de subida
> **Problema:** Se lanza una piedra hacia arriba con $v_0 = 12 m/s$. Calcula el tiempo para alcanzar el punto más alto.
> *   **Datos:** $v_0 = 12 m/s$, $v_f = 0 m/s$ (punto alto), $g = -9,8 m/s^2$ (sube).
> *   **Busco:** $t$.
> *   **Variable ausente:** $y$.
> *   **Fórmula:** $v_f = v_0 + g \cdot t$
> *   **Solución:** $0 = 12 + (-9,8) \cdot t \rightarrow -12 = -9,8 \cdot t \rightarrow t = 1,22 s$.

> [!abstract] Ejemplo 3: Altura máxima (Paso a paso)
> **Problema:** Un objeto lanzado hacia arriba tarda 3s en llegar al punto más alto. Calcula $v_0$ y la altura máxima ($y$).
> 1. **Para $v_0$:** (Ausente $y$) $\rightarrow v_f = v_0 + g \cdot t$
>    $0 = v_0 + (-9,8 \cdot 3) \rightarrow v_0 = 29,4 m/s$.
> 2. **Para $y$:** (Ahora conocemos 4 datos, usamos la más directa)
>    $y = v_0 \cdot t + \frac{g \cdot t^2}{2}$
>    $y = (29,4 \cdot 3) + \frac{-9,8 \cdot (3)^2}{2} = 88,2 - 44,1 = 44,1 m$.

> [!abstract] Ejemplo 4: Caso Dron ($1,200 USD$)
> **Problema:** Un dron de $1,200 USD$ se apaga a 20m de altura. Calcula la velocidad de impacto ($v_f$).
> *   **Datos:** $v_0 = 0 m/s$, $y = 20 m$, $g = 9,8 m/s^2$.
> *   **Variable ausente:** $t$.
> *   **Fórmula:** $v_f^2 = v_0^2 + 2 \cdot g \cdot y$
> *   **Solución:** $v_f^2 = 0 + 2 \cdot 9,8 \cdot 20 = 392 \rightarrow v_f = \sqrt{392} \approx 19,8 m/s$.

---

### Ejercicios de Práctica

> [!success] 🟢 Fácil: Identificación
> 1. ¿Cuál es el valor de $v_0$ si un objeto "se suelta"?
> 2. En el punto más alto de un lanzamiento, ¿cuánto vale $v_f$?
> 3. Si un dato dice $25 m/s$, ¿a qué variable se refiere?
> 4. ¿Qué signo tiene $g$ si el objeto se lanza hacia el cielo?

> [!warning] 🟡 Medio: Cálculos ($g = 9,8 m/s^2$ o $10 m/s^2$)
> 1. Se deja caer un objeto y tarda 4s en caer. ¿Altura?
> 2. ¿Velocidad final del objeto anterior al tocar el suelo?
> 3. Se lanza un objeto hacia abajo a $v_0 = 5 m/s$. Velocidad tras 2s?
> 4. Un objeto cae desde 45m. ¿Tiempo de caída? (Usa $g = 10 m/s^2$).

> [!danger] 🔴 Avanzado: Lanzamientos y Costos
> 1. Proyectil lanzado hacia arriba alcanza 100m. Calcula $v_0$ y $t$ de subida.
> 2. Un cohete gasta $50 USD$ por segundo de vuelo. Si se lanza a $49 m/s$, ¿cuánto dinero gasta hasta alcanzar su altura máxima?
> 3. Se lanza un objeto hacia arriba a $60 m/s$. ¿Velocidad a los 2s?
> 4. Un paquete de medicina cae de 80m. Si impacta a más de $40 m/s$ se pierde la carga ($2,000 USD$). ¿Se rompen las medicinas?

> [!todo] ✅ Respuestas
> *   **Fácil:** 1. $0 m/s$ | 2. $0 m/s$ | 3. Velocidad ($v_0$ o $v_f$) | 4. Negativo.
> *   **Medio:** 
> 	1. $78,4 m$ (Ausente: $v_f$)
> 	2. $39,2 m/s$ (Ausente: $y$)
> 	3. $24,6 m/s$ (Ausente: $y$)
> 	4. $3 s$ (Ausente: $v_f$)
> *   **Avanzado:** 
> 	1. $v_0 = 44,27 m/s$ (Ausente: $t$); $t = 4,51 s$ (Ausente: $v_0$ inicial)
> 	2. $t = 5 s$, Gasto = $250 USD$ (Ausente: $y$)
> 	3. $40,4 m/s$ (Ausente: $y$)
> 	4. $v_f = 39,6 m/s$. No se rompen (es menor a 40). (Ausente: $t$)

---

### Autoevaluación

> [!question] ad-question: ¿Por qué $v_f = 0$ en la altura máxima?
> Porque es el punto de inflexión: el objeto agota su energía cinética ascendente y se detiene un instante antes de empezar a descender.

> [!question] ad-question: ¿Qué fórmula usar si no tienes la altura ($y$) ni te la piden?
> Se usa $v_f = v_0 + g \cdot t$, ya que es la única que relaciona velocidades, gravedad y tiempo sin requerir la distancia.

> [!question] ad-question: Si un sensor de $800 USD$ cae de un estante, ¿cómo es el signo de $g$?
> Positivo ($+9,8 m/s^2$), porque el desplazamiento es hacia abajo, siguiendo la aceleración natural de la gravedad.

---

> [!tip] 💡 En la próxima clase
> Aplicaremos estos despejes para resolver **problemas de encuentro**, donde dos objetos se mueven al mismo tiempo (uno sube y otro baja) y debemos hallar el punto exacto de colisión.

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 4

> [!info] 🧭 Navegación
> [[Clase 01 - Introducción a la Caída Libre y la Gravedad|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | | [[Clase 03 - Caída libre Gravedad lunar, lanzamientos y aplicaciones con|Clase 03 ➡]]