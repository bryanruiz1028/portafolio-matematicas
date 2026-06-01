# 📖 Guía de estudio — Clase 04: Demostración y Comprobación de Identidades Trigonométricas

> [!info] 📌 Conceptos clave
> Para dominar la demostración de identidades, es fundamental aplicar estas estrategias procedimentales recomendadas por expertos:
> * **Priorizar el lado complejo:** Inicia siempre transformando el lado de la igualdad que presente más términos o mayor dificultad (paréntesis, fracciones o potencias) para simplificarlo hasta alcanzar el lado más sencillo.
> * **Conversión a Seno y Coseno:** Una técnica estándar y efectiva es transformar funciones como tangentes y secantes a términos de $\sin \theta$ y $\cos \theta$, lo que facilita la cancelación de términos.
> * **Simplificación de Binomios a Monomios:** Antes de operar, busca identidades que permitan convertir dos términos (como $1 + \tan^2 \theta$) en uno solo ($\sec^2 \theta$). Reducir el tamaño de la expresión es la clave del éxito.
> * **Identificación de Productos Notables:** Al observar expresiones con paréntesis elevados al cuadrado, aplica el desarrollo de binomios para liberar los términos y poder aplicar la identidad fundamental.

### TABLA DE FÓRMULAS Y DEFINICIONES

Utiliza esta tabla como referencia rápida para tus sustituciones. Mantener la consistencia en el ángulo ($\theta$) te ayudará a identificar patrones más rápido.

| Término | Definición / Fórmula |
| :--- | :--- |
| **Identidad Pitagórica Fundamental** | $\sin^2 \theta + \cos^2 \theta = 1$ |
| **Identidad de la Tangente** | $\tan \theta = \frac{\sin \theta}{\cos \theta}$ |
| **Identidad Recíproca (Secante)** | $\sec \theta = \frac{1}{\cos \theta}$ |
| **Identidad Pitagórica Secundaria** | $\tan^2 \theta + 1 = \sec^2 \theta$ |
| **Binomio al Cuadrado (Suma)** | $(a + b)^2 = a^2 + 2ab + b^2$ |
| **Binomio al Cuadrado (Resta)** | $(a - b)^2 = a^2 - 2ab + b^2$ |

---

### EJEMPLO RESUELTO A: CASO BÁSICO

````ad-example
**Ejemplo A — Simplificación de Tangentes**

**Problema:** Demostrar la identidad $\frac{1}{1 + \tan^2 \theta} = \cos^2 \theta$.

**Procedimiento:**
1. **Paso 1 (Reducción del denominador):** Observamos que $1 + \tan^2 \theta$ es una identidad pitagórica secundaria. La sustituimos por un solo término para simplificar: $\frac{1}{\sec^2 \theta}$.
2. **Paso 2 (Uso de recíprocas):** Sabemos que la secante es la recíproca del coseno. Sustituimos $\sec^2 \theta$ por su equivalencia: $\frac{1}{\frac{1}{\cos^2 \theta}}$.
3. **Paso 3 (Extremos y medios):** Para resolver la división, colocamos un 1 debajo del numerador para completar la fracción: $\frac{\frac{1}{1}}{\frac{1}{\cos^2 \theta}}$.
4. **Paso 4 (Operación final):** Multiplicamos los extremos ($1 \cdot \cos^2 \theta$) y los medios ($1 \cdot 1$).

**Resultado:** ✅ $\cos^2 \theta$
````

---

### EJEMPLO RESUELTO B: APLICACIÓN COTIDIANA ($USD)

````ad-example
**Ejemplo B — Modelado de Variación de Costos ($USD)**

**Enunciado:** Un analista financiero utiliza la expresión $(\sin A + \cos A)^2$ para representar la combinación de dos variables de mercado. Se requiere simplificar esta expresión para obtener una fórmula de costos operativos más eficiente.

**Procedimiento:**
1. **Paso 1 (Expansión del binomio):** Aplicamos la fórmula del cuadrado de un binomio $(a+b)^2 = a^2 + 2ab + b^2$.
   * $(\sin A + \cos A)^2 = \sin^2 A + 2\sin A \cos A + \cos^2 A$.
2. **Paso 2 (Reorganización lógica):** Agrupamos los términos cuadráticos para aplicar la identidad fundamental:
   * $(\sin^2 A + \cos^2 A) + 2\sin A \cos A$.
3. **Paso 3 (Sustitución pitagórica):** Dado que $\sin^2 A + \cos^2 A = 1$, reemplazamos esos términos por la unidad.
4. **Paso 4 (Resultado final):** La expresión simplificada es $1 + 2\sin A \cos A$.

**Fórmula simplificada de costos en $USD:** $1 + 2 \sin A \cos A$ ✅
````

---

### EJERCICIOS DE REPASO GRADUADOS

````ad-abstract
**Nivel 🟢 Fácil: Sustitución Directa (Un solo paso)**
1. Exprese $\tan^2 \theta$ únicamente en términos de seno y coseno.
2. Exprese la función $\sec \theta$ en términos de $\cos \theta$.
3. Utilizando una identidad pitagórica, convierta el binomio $\sec^2 \theta - 1$ en un solo término.
````

````ad-abstract
**Nivel 🟡 Medio: Comprobación de Identidades**
1. Verifique que $\cos^2 \theta (\sec^2 \theta - 1) = \sin^2 \theta$. (Pista: simplifique el paréntesis primero).
2. Demuestre que $\frac{\sin^2 \theta}{\cos^2 \theta} + 1 = \sec^2 \theta$ realizando la suma de fracciones.
3. Compruebe si $(\sin A - \cos A)^2 = 1 - 2\sin A \cos A$ usando el binomio al cuadrado negativo.
````

````ad-abstract
**Nivel 🔴 Avanzado — Aplicación $USD**
**Reto del Analista:** Un sistema financiero reporta un valor de mercado basado en la expresión $(1 - \sin^2 A)(\tan^2 A + 1)$. Demuestre, paso a paso, que al simplificar esta expresión el resultado es una unidad de valor constante (**1 USD**), utilizando la conversión a coseno y secante.
````

---

### CONSEJO DE ESTUDIO FINAL

> [!tip] 💡 La mentalidad del experto
> Recuerda que el objetivo no es simplemente resolver el ejercicio que tienes enfrente, sino **dominar las herramientas y trucos** que te servirán para cualquier identidad futura. Cuando te enfrentes a sumas de fracciones, usa el método de la **"carita feliz"** (multiplicación cruzada y de denominadores). Ten siempre tus fórmulas escritas a mano; la memoria falla, pero la lógica procedimental, con la práctica constante, se vuelve instintiva.