# 📖 Guía de estudio — Clase 08: Resolución de Triángulos Rectángulos con Razones Trigonométricas

> [!info] 📌 Conceptos clave
> "Resolver un triángulo" significa descubrir el valor de todos sus componentes: sus 3 lados y sus 3 ángulos. Para lograrlo con la maestría del "profe Alex", recuerda estos pilares fundamentales:
> * **Consistencia:** Una vez que elijas tu ángulo de referencia para trabajar, ¡no lo cambies! Si cambias de ángulo a mitad del ejercicio, los nombres de los catetos (opuesto y adyacente) se invertirán y podrías confundirte.
> * **Suma de ángulos:** En todo triángulo rectángulo, el ángulo recto mide 90° y los otros dos (agudos) deben sumar los **90°** restantes para completar el total de **180°** de cualquier triángulo. Esto te permite hallar un ángulo faltante con una simple resta.
> * **Totalidad:** No te detengas hasta que tengas los 6 datos (3 lados y 3 ángulos).

---

## 1. Sección de Referencia: Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Hipotenusa ($H$)** | El lado más largo, siempre ubicado frente al ángulo recto (90°). |
| **Cateto Opuesto ($CO$)** | El lado que está justo enfrente del ángulo de referencia seleccionado. |
| **Cateto Adyacente ($CA$)** | El lado que forma parte del ángulo de referencia (está "pegado" a él). |
| **Seno ($\text{sen}$)** | $\text{sen}(\theta) = \frac{CO}{H}$ |
| **Coseno ($\cos$)** | $\cos(\theta) = \frac{CA}{H}$ |
| **Tangente ($\tan$)** | $\tan(\theta) = \frac{CO}{CA}$ |
| **Funciones Inversas** | Se usan para hallar el ángulo cuando ya conoces los lados. En la calculadora verás los botones $\text{sen}^{-1}$, $\cos^{-1}$ y $\tan^{-1}$ (se activan con la tecla **Shift** o **2ndF**). La $\tan^{-1}$ se lee como **arcotangente**. |

---

## 2. Ejemplos Resueltos Paso a Paso

> [!example] Ejemplo A: Cálculo de Cateto (Caso Básico)
> **Enunciado:** Dado un triángulo con un ángulo de 32° y una hipotenusa de 15 m, halla la medida del cateto opuesto.
> 
> 1. **Paso 1 (Identificar lados):** Tenemos el ángulo $\theta = 32^\circ$ y la hipotenusa $= 15 \text{ m}$. Buscamos el Cateto Opuesto ($CO$).
> 2. **Paso 2 (Seleccionar la razón):** La fórmula que une el $CO$ con la hipotenusa es el **Seno**.
>    $$\text{sen}(32^\circ) = \frac{CO}{15 \text{ m}}$$
> 3. **Paso 3 (Despeje matemático):** Como la incógnita está arriba, el 15 que divide pasa a multiplicar al otro lado:
>    $$15 \text{ m} \cdot \text{sen}(32^\circ) = CO$$
>    $$15 \cdot 0.5299 \approx 7.948 \text{ m}$$
> 
> **Resultado:** El cateto opuesto mide **7.948 m**.

> [!example] Ejemplo B: Aplicación Real (Presupuesto de Cable)
> **Enunciado:** Necesitamos un cable para una antena. El cable es la **hipotenusa**. El ángulo de elevación es 34° y la distancia horizontal a la base (**cateto adyacente**) es 15 m. Si el metro de cable cuesta **$12.50 USD**, ¿cuál es el costo total?
> 
> 1. **Paso 1 (Identificar):** Tenemos $\theta = 34^\circ$ y $CA = 15 \text{ m}$. Buscamos la Hipotenusa ($H$). Usaremos **Coseno**.
>    $$\cos(34^\circ) = \frac{15 \text{ m}}{H}$$
> 2. **Paso 2 (El "Doble Despeje"):** ¡Atención! Aquí la incógnita está en el denominador.
>    *   **Subpaso 2.1:** Pasamos la $H$ a multiplicar: $H \cdot \cos(34^\circ) = 15$.
>    *   **Subpaso 2.2:** Pasamos el $\cos(34^\circ)$ a dividir: $H = \frac{15}{\cos(34^\circ)}$.
> 3. **Paso 3 (Cálculo):**
>    $$H = \frac{15}{0.8290} \approx 18.094 \text{ m}$$
> 4. **Paso 4 (Costo):** Multiplicamos la longitud por el precio: $18.094 \text{ m} \cdot 12.50 \text{ USD} = 226.175$.
> 
> **Resultado:** El cable mide **18.094 m** y el presupuesto final es **$226.18 USD**.

---

## 3. Ejercicios de Repaso

> [!abstract] 🟢 Nivel Fácil: ¡Tú puedes!
> *En estos ejercicios la incógnita siempre queda arriba. ¡Solo despeja y listo!*
> 1. Si un triángulo tiene un ángulo de 40°, **¿cuánto mide el otro ángulo agudo?**
> 2. **Halla el cateto opuesto** si el ángulo es de 30° y la hipotenusa mide 10 cm.
> 3. **Calcula el cateto adyacente** si la hipotenusa mide 20 m y el ángulo de referencia es 60°.

> [!abstract] 🟡 Nivel Medio: ¡Domina el despeje!
> *Aquí la incógnita queda abajo ($H$ o $CA$). Recuerda aplicar el "doble despeje" que vimos en el Ejemplo B.*
> 1. **Encuentra la hipotenusa** si el cateto adyacente mide 15 m y el ángulo es de 34°.
> 2. **Calcula la hipotenusa** sabiendo que el cateto opuesto mide 12 cm y el ángulo es de 45°.
> 3. **Halla la hipotenusa** de un triángulo con un cateto adyacente de 32 m y un ángulo de 63°.

> [!abstract] 🔴 Nivel Avanzado: Desafío de Expertos
> *¡Paso a paso llegarás a la meta! Para este ejercicio, te recomendamos **dibujar el triángulo** primero.*
> 
> **El terreno diagonal:** Un terreno tiene forma de triángulo rectángulo. Solo conoces sus dos **catetos**: la base mide 18 cm y la altura 13 cm.
> 1. **Halla el valor del ángulo agudo** que está frente al lado de 13 cm usando la función inversa ($\tan^{-1}$).
> 2. **Calcula la longitud de la diagonal** (hipotenusa) usando el seno del ángulo que acabas de encontrar.
> 3. **Presupuesto:** Si se debe proteger la diagonal con una cinta que cuesta **$25 USD por cm**, ¿cuál es el costo total del material?

---

## 4. Estrategia Final: Consejo de Estudio

> [!tip] 💡 Consejo de estudio
> Antes de presionar cualquier tecla, mira la pantalla de tu calculadora: debe aparecer una **pequeña letra "D"** o la palabra **"DEG"** (de *Degrees*). Si ves una "R" o "G", los resultados serán erróneos. 
> 
> Finalmente, aplica la **prueba de lógica**: En cualquier triángulo rectángulo, la hipotenusa **siempre** debe ser el lado más largo. Si al terminar el ejercicio un cateto es más grande que la hipotenusa, ¡revisa tus despejes!