# 📖 Guía de estudio — Clase 07: Teorema de la Probabilidad Total

¡Qué tal, amigas y amigos! Espero que estén muy bien. En esta guía vamos a dominar el **Teorema de la Probabilidad Total**. A veces este nombre suena un poco intimidante, pero ya verán que si seguimos la lógica de los "caminos" y usamos bien nuestros diagramas, ¡es pan comido! Como siempre dice el Profe Alex: el secreto no está en memorizar fórmulas complejas, sino en entender qué está pasando en nuestro dibujo.

> [!info] 📌 Conceptos clave
> El Teorema de la Probabilidad Total nos permite calcular la probabilidad de un evento que puede ocurrir por distintas vías o escenarios. Es, básicamente, la **suma de todas las probabilidades de los caminos** que nos llevan al mismo resultado.
> 
> *   **¿Cuándo usar este teorema?** ¡Esta es la clave! Lo usamos cuando el ejercicio nos pide la probabilidad de un suceso pero **no nos especifica un orden exacto**. Por ejemplo: si nos piden "sacar una bola azul y una verde", sin decirnos cuál sale primero.
> *   **El Diagrama de Árbol:** Es nuestra mejor herramienta visual. Nos permite ver todas las opciones y calcular probabilidades multiplicando a través de las ramas.
> *   **Independencia vs. Dependencia:** 
>     *   **Con reemplazo:** Los eventos son independientes. La probabilidad no cambia porque devolvemos el objeto (el denominador se mantiene igual).
>     *   **Sin reemplazo:** Los eventos son dependientes. ¡Cuidado aquí! El total de elementos disminuye, por lo que el denominador cambia (de $\frac{x}{8}$ a $\frac{y}{7}$, por ejemplo).

---

## 2. Fórmulas y Definiciones Importantes

| **Término** | **Definición / Fórmula** |
| :--- | :--- |
| **Teorema de la Probabilidad Total** | Es la suma de las probabilidades de todas las rutas válidas. Matemáticamente, sumamos los resultados de multiplicar las ramas que nos sirven. |
| **Regla de la Multiplicación** | Se usa para hallar la probabilidad de una ruta específica ("esto **y** luego esto"): $P(A \text{ y } B) = P(A) \times P(B|A)$. |
| **Diagrama de Árbol** | Representación gráfica de todos los resultados posibles. **Multiplicamos** al avanzar por una rama y **sumamos** al combinar diferentes rutas finales. |
| **Eventos Sin Reemplazo** | Condición donde la probabilidad del segundo evento se ve afectada por el primero, ya que el espacio muestral se reduce. |

---

## 3. Ejemplos Resueltos

> [!example] Ejemplo A — Extracción de esferas con reemplazo
> **Contexto:** En una urna hay $8$ esferas: $5$ azules, $2$ rojas y $1$ verde. Si sacamos dos esferas consecutivas **con reemplazo**, ¿cuál es la probabilidad de sacar una azul y una verde?
> 
> **Paso a paso:**
> 1.  **Identificar las rutas:** Como no nos piden un orden, nos sirven dos escenarios:
>     *   Ruta 1: (Azul **y** Verde) $\rightarrow P(A_1 \cap V_2)$
>     *   Ruta 2: (Verde **y** Azul) $\rightarrow P(V_1 \cap A_2)$
> 2.  **Calcular probabilidades:** Al ser con reemplazo, el total siempre es $8$.
>     *   Ruta 1: $\frac{5}{8} \times \frac{1}{8} = \frac{5}{64}$
>     *   Ruta 2: $\frac{1}{8} \times \frac{5}{8} = \frac{5}{64}$
> 3.  **Sumar los resultados (Probabilidad Total):**
>     *   $P(\text{Total}) = \frac{5}{64} + \frac{5}{64} = \frac{10}{64}$
> 4.  **Resultado final:** Simplificamos a $\frac{5}{32}$. En decimal es $0.1562$, lo que equivale al **$15.62\%$**.

> [!example] Ejemplo B — Probabilidad de ascenso laboral ($USD)
> **Contexto:** El Sr. Gómez sabe que hay un $60\%$ ($0.6$) de probabilidad de que su empresa abra una sucursal. Si la abren, tiene un $70\%$ ($0.7$) de ser gerente. Si no la abren, su probabilidad baja al $10\%$ ($0.1$). Si es nombrado gerente, ganará un bono de **$1,000 USD**. ¿Qué probabilidad tiene de ganar ese dinero?
> 
> **Paso a paso:**
> 1.  **Escenarios para ser gerente:**
>     *   **Caso 1 (Abre sucursal):** $P(\text{Abre}) = 0.6$. Probabilidad de ser gerente aquí: $0.6 \times 0.7 = 0.42$.
>     *   **Caso 2 (No abre sucursal):** Primero calculamos el complemento: $1 - 0.6 = 0.4$. La probabilidad de ser gerente aquí es: $0.4 \times 0.1 = 0.04$.
> 2.  **Suma de Probabilidad Total:** $0.42 + 0.04 = 0.46$.
> 
> **Resultado:** El Sr. Gómez tiene un **$46\%$** de probabilidad de obtener el cargo y el bono de **$1,000 USD**.

---

## 4. Ejercicios de Repaso

> [!abstract] 🟢 Fácil: Teoría Fundamental
> ¿Cuál debe ser el resultado de sumar las probabilidades de todas las ramas finales de un diagrama de árbol completo? ¿Por qué?
> 
> *   **Respuesta:** Debe ser igual a $1$ (o $100\%$). Esto es porque el diagrama representa la totalidad de los eventos posibles dentro del espacio muestral; no puede sobrar ni faltar probabilidad.

> [!abstract] 🟡 Medio: El desafío de la urna
> En una urna hay $8$ esferas: $4$ azules, $3$ rojas y $1$ verde. Si extraes dos esferas **sin reemplazo**, calcula la probabilidad de sacar una azul y una roja (en cualquier orden).
> 
> *   **Pista pedagógica:** Recuerda que al sacar la primera, ¡ya solo quedan $7$ esferas para la segunda extracción!
> *   *(Resultado: $\frac{24}{56} = \frac{3}{7} \approx 42.85\%$)*

> [!abstract] 🔴 Avanzado: Aplicación Real ($USD)
> El $80\%$ ($0.8$) de los alumnos de una clase hace sus tareas. De los que las hacen, el $90\%$ ($0.9$) aprueba. De los que no las hacen, el $70\%$ ($0.7$) aprueba. Si aprobar la materia otorga automáticamente una beca de **$500 USD**, ¿cuál es la probabilidad de que un alumno elegido al azar gane la beca?
> 
> *   **Ayuda:** Multiplica (Tarea $\times$ Aprueba) + (No Tarea $\times$ Aprueba).
> *   *(Resultado: $86\%$ de probabilidad de ganar los $500 USD$)*

---

## 5. Estrategia de Estudio

> [!tip] 💡 Consejos de un Especialista
> ¡No te agobies! Sigue estos pasos y verás cómo todo encaja:
> 1.  **Dibuja siempre el árbol:** No intentes hacerlo todo de cabeza. Ver las ramas te ayuda a no olvidar ninguna combinación.
> 2.  **La regla de oro de los conectores:** 
>     *   Si dices "**Y**" (un evento tras otro en la misma rama) $\rightarrow$ **Multiplica** ($\times$).
>     *   Si dices "**O**" (un camino u otro camino diferente) $\rightarrow$ **Suma** ($+$).
> 3.  **Checklist de verificación:**
>     *   [ ] ¿Las ramas que salen de cada nodo suman exactamente $1$?
>     *   [ ] Si es "sin reemplazo", ¿resté $1$ al total en el segundo paso?
>     *   [ ] ¿Identifiqué todos los caminos que cumplen la condición del problema?

¡Ánimo! La probabilidad es solo una forma de organizar las posibilidades del mundo. ¡Tú puedes con esto!