# 📖 Guía de estudio — Clase 04: Razones Trigonométricas

> [!info] 📌 Conceptos clave
> Para dominar la trigonometría, es fundamental asentar las bases lógicas que propone el **Profe Alex**. Antes de calcular, asegúrate de comprender estos cuatro pilares:
> 1. **El escenario obligatorio:** Las razones trigonométricas solo son aplicables en **triángulos rectángulos** (aquellos que poseen un ángulo recto de 90°).
> 2. **Identificación relativa de los lados:** La **Hipotenusa** siempre será el lado más largo (frente al ángulo de 90°). Sin embargo, los nombres de los catetos dependen del ángulo de referencia: el **Opuesto** está frente a él y el **Adyacente** está junto a él.
> 3. **Regla de los dos datos:** Para resolver cualquier incógnita, necesitas conocer al menos dos datos del triángulo: dos lados, o un lado y un ángulo agudo.
> 4. **Configuración técnica:** La calculadora debe estar siempre en modo **Degrees (D)** para trabajar con grados sexagesimales. Una "R" (Radianes) o "G" (Gradianes) en pantalla arruinará el resultado.

## Fórmulas y definiciones importantes

Para facilitar la memorización, utilizaremos la mnemotecnia clásica **SOH CAH TOA**, que relaciona las iniciales de cada función con sus lados correspondientes.

| Término | Definición / Fórmula | Mnemotecnia (SOH CAH TOA) |
| :--- | :--- | :--- |
| **Seno ($\sin$)** | $\frac{\text{Cateto Opuesto}}{\text{Hipotenusa}}$ | **SOH**: **S**eno = **O**puesto / **H**ipotenusa |
| **Coseno ($\cos$)** | $\frac{\text{Cateto Adyacente}}{\text{Hipotenusa}}$ | **CAH**: **C**oseno = **A**dyacente / **H**ipotenusa |
| **Tangente ($\tan$)** | $\frac{\text{Cateto Opuesto}}{\text{Cateto Adyacente}}$ | **TOA**: **T**angente = **O**puesto / **A**dyacente |
| **Razones Inversas** | $\sin^{-1}, \cos^{-1}, \tan^{-1}$ | Se usan para hallar el **ángulo** cuando ya conoces los lados. |

---

## Ejemplos resueltos adicionales

> [!example] Ejemplo A — Hallar un lado (Caso Básico)
> **Escenario:** En un triángulo conocemos un ángulo $\theta = 32^\circ$ y una hipotenusa de $10\text{m}$. Queremos hallar el cateto opuesto ($x$).
> 
> **Paso a paso:**
> 1. **Análisis pedagógico:** ¿Por qué elegimos **Seno**? Porque el dato que buscamos es el Cateto Opuesto y el dato que tenemos es la Hipotenusa. La relación $O/H$ corresponde a $\sin$.
> 2. **Planteamiento:** $\sin(32^\circ) = \frac{x}{10}$
> 3. **Despeje:** El $10$ que divide pasa a multiplicar al otro lado: $10 \cdot \sin(32^\circ) = x$.
> 4. **Cálculo:** $x \approx 5,299\text{m}$.
> *Interpretación: Es lógico que sea menor a 10, ya que la hipotenusa debe ser el lado mayor.*

> [!example] Ejemplo B — Aplicación de costos y doble triángulo ($USD)
> **Enunciado:** Un técnico debe calcular el costo de una base metálica ($y$). Se conoce un ángulo de $60^\circ$ y una base inicial de $40\text{m}$ en el primer tramo.
> 
> **Paso a paso:**
> 1. **Cálculo de la altura compartida ($x$):** En el primer triángulo, $x$ es el cateto opuesto y $40\text{m}$ es el adyacente.
>    $\tan(60^\circ) = \frac{x}{40} \implies x = 40 \cdot \tan(60^\circ) = 69,28\text{m}$.
> 2. **Transición al segundo triángulo:** Esta altura $x = 69,28\text{m}$ ahora actúa como el **Cateto Opuesto** para el segundo ángulo de $55^\circ$. Buscamos su base $y$ (Cateto Adyacente).
>    $\tan(55^\circ) = \frac{69,28}{y}$
> 3. **Despeje del denominador:** Intercambiamos la $y$ con la función: $y = \frac{69,28}{\tan(55^\circ)} = 48,51\text{m}$.
> 4. **Aplicación comercial:** Si cada metro cuesta $\$15\text{ USD}$:
>    $48,51 \cdot 15 = \$727,65\text{ USD}$.
> 
> ✅ **Resultado:** El costo total es de **$727,65 USD**.

---

## Ejercicios de repaso

> [!abstract] 🟢 Fácil (Nivel Introductorio)
> 1. Hallar el cateto opuesto si el ángulo es $35^\circ$ y el adyacente mide $9\text{ cm}$.
> 2. Hallar la hipotenusa si el ángulo es $29^\circ$ y el cateto adyacente mide $24,72\text{ m}$.
> 3. **Teoría:** Si un problema te da el Cateto Opuesto y la Hipotenusa para hallar un ángulo, ¿qué función debes usar?

> [!abstract] 🟡 Medio (Despeje y Ángulos)
> 1. **Hallar un ángulo:** Calcula $\alpha$ si el cateto adyacente mide $12\text{m}$ y la hipotenusa $22\text{m}$.
>    *(Pista: Usa $\alpha = \cos^{-1}(12/22)$)*.
> 2. **El "Intercambio":** Resuelve $\cos(59^\circ) = \frac{23}{x}$.
>    *Nota pedagógica: Cuando la incógnita está abajo, multiplicamos por $x$ para subirla y luego dividimos por la función. En la práctica, esto parece un simple intercambio de posiciones entre la $x$ y el $\cos(59^\circ)$.*

> [!abstract] 🔴 Avanzado — Reto del Cable ($USD)
> **Problema:** Se instalará un cable entre dos cimas.
> 1. **Triángulo 1:** Halla la altura común ($x$) usando una hipotenusa de $10\text{m}$ y un ángulo de $30^\circ$.
> 2. **Triángulo 2:** Usa esa altura $x$ (que será el cateto opuesto) para hallar la nueva hipotenusa ($y$) con un ángulo de $40^\circ$.
> 3. **Costo:** Si el metro de cable cuesta **$12.50 USD**, ¿cuál es el presupuesto final?
> 
> **Clave de corrección:**
> *   $x = 10 \cdot \sin(30^\circ) = 5\text{m}$.
> *   $y = 5 / \sin(40^\circ) \approx 7,78\text{m}$.
> *   **Resultado final: $97,25 USD.**

---

> [!tip] 💡 Consejo de estudio
> La mejor forma de verificar tus resultados es la **"Prueba de Sentido Logístico"** del Profe Alex: dibuja el triángulo intentando respetar las proporciones. Si el ángulo es pequeño ($30^\circ$), el cateto opuesto debe verse claramente más corto que el adyacente. Y recuerda la regla de oro: **La hipotenusa siempre, sin excepción, debe ser el lado más largo**. Si tu cálculo dice lo contrario, revisa el despeje. ¡Y no olvides verificar la **"D"** en tu pantalla!