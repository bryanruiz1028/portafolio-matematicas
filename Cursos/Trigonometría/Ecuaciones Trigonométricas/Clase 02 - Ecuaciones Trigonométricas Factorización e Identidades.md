# Clase 02 — Ecuaciones Trigonométricas: Factorización e Identidades

#algebra #ecuacionestrigo
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 3

> [!info] 🧭 Navegación
> - Clase anterior: [[Clase 01 — Introducción a Ecuaciones Trigonométricas]]
> - Siguiente clase: [[Clase 03 — Identidades Trigonométricas Avanzadas]]

---

> [!info] 🌍 Relevancia y aplicaciones
> ¡Bienvenido a la segunda clase! Hoy subiremos de nivel. Resolver ecuaciones trigonométricas complejas no es solo un ejercicio académico; es la base para modelar fenómenos que se repiten cíclicamente. Dominar la factorización y el uso de identidades te permitirá simplificar problemas que parecen imposibles a simple vista.
> 
> - **💵 Aplicación con $USD:** En los mercados financieros, el precio de activos como el Bitcoin suele presentar ciclos de volatilidad que pueden modelarse con funciones trigonométricas. Identificar los "ángulos de estabilidad" ayuda a predecir retrocesos de precio.
> - **🏗️ Aplicación práctica:** Los ingenieros utilizan estas herramientas para calcular la distribución de tensiones en puentes colgantes ante la fuerza del viento.
> - **📊 Situación cotidiana:** Desde el vaivén rítmico de un columpio hasta la altura exacta de una cabina en la "London Eye" en un segundo determinado.

---

### 3. CONCEPTO CLAVE Y ERRORES COMUNES

> [!note] 📌 ¿Qué es una Ecuación Trigonométrica?
> Imagina una balanza en perfecto equilibrio. De un lado tenemos una "caja misteriosa" llamada función (como $\text{sen}$ o $\cos$) y dentro vive un ángulo $x$ que queremos descubrir. Resolver la ecuación es encontrar el valor exacto de ese ángulo (en grados o radianes) para que la balanza no se mueva. ¡Es como ser un detective de la geometría!

> [!warning] ⚠️ Error común: El límite de la realidad
> **¡Cuidado con el rango!** Nunca aceptes una solución donde el despeje final resulte en algo como $\text{sen}(x) = 2$ o $\cos(x) = -1.5$.
> - ❌ **Incorrecto:** Intentar hallar un ángulo si el valor absoluto es mayor a 1.
> - ✅ **Correcto:** Recuerda que el seno y el coseno son funciones "prisioneras" entre $-1$ y $1$. Si el valor sale de ahí, esa rama de la ecuación **no tiene solución**.

> [!tip] 💡 Truco para recordar identidades
> Usa esta mnemotecnia pedagógica: **"Ángulo doble, lío doble: cámbialo a sencillo"**. Siempre que veas un $2x$, tu misión principal es transformarlo en términos de $x$ para poder factorizar con éxito.

---

### 4. PROCEDIMIENTO MAESTRO

Para resolver ecuaciones de alto nivel, aplica este algoritmo lógico. ¡No te rindas con la factorización, es la llave maestra!

```text
PASO 1 → Unificar ángulos: Si detectas ángulos dobles (2x), usa identidades para convertirlos en ángulos sencillos (x).
PASO 2 → Unificar funciones: Usa identidades pitagóricas para que toda la ecuación use una sola función (ej. que todo sea seno o todo coseno).
PASO 3 → Igualar a cero y organizar: Ordena la ecuación (grado 2, grado 1, término independiente). Factoriza el trinomio o aplica la "Fórmula General" si la factorización no es evidente.
PASO 4 → Hallar ángulos y verificar: Encuentra los valores en el círculo trigonométrico (expresa el resultado en grados y radianes) y comprueba con tu calculadora.
```

> [!tip] ⌨️ Tip de Profe Alex: Uso de Calculadora
> Para verificar funciones al cuadrado como $\text{sen}^2(x)$, debes ingresarlo en la calculadora como: `(sen(x))^2`. Si escribes `sen(x^2)`, la calculadora solo elevará el ángulo, ¡dándote un error!

---

### 5. BLOQUE DE EJEMPLOS RESUELTOS (PASO A PASO)

#### Ejemplo 1: Caso básico de factorización
**Resolver:** $\cos^2(x) - \cos(x) - 2 = 0$
1. Factorizamos como un trinomio de la forma $x^2 + bx + c$: $(\cos(x) - 2)(\cos(x) + 1) = 0$.
2. Igualamos cada factor a cero:
   - $\cos(x) = 2$ → **Sin solución** (fuera de rango $[-1, 1]$).
   - $\cos(x) = -1$ → Ocurre en **$x = 180^\circ$**.
3. **Resultado:** $180^\circ$ ($\pi$ rad).

#### Ejemplo 2: Caso con Identidades Pitagóricas
**Resolver:** $\cos^2(x) + 4\text{sen}(x) + 4 = 0$
1. Sustituimos $\cos^2(x)$ por $(1 - \text{sen}^2(x))$ para unificar funciones.
2. $(1 - \text{sen}^2(x)) + 4\text{sen}(x) + 4 = 0 \implies -\text{sen}^2(x) + 4\text{sen}(x) + 5 = 0$.
3. Multiplicamos por $-1$ para facilitar: $\text{sen}^2(x) - 4\text{sen}(x) - 5 = 0$.
4. Factorizamos: $(\text{sen}(x) - 5)(\text{sen}(x) + 1) = 0$.
5. Soluciones: $\text{sen}(x) = 5$ (No existe) y $\text{sen}(x) = -1$.
6. **Resultado:** $270^\circ$ ($3\pi/2$ rad).

#### Ejemplo 3: Caso de Ángulo Doble
**Resolver:** $\text{sen}(2x) + \cos(x) = 0$
1. Usamos la identidad: $2\text{sen}(x)\cos(x) + \cos(x) = 0$.
2. Factor común $\cos(x)$: $\cos(x)(2\text{sen}(x) + 1) = 0$.
3. Igualamos factores:
   - $\cos(x) = 0 \implies x = 90^\circ, 270^\circ$.
   - $2\text{sen}(x) + 1 = 0 \implies \text{sen}(x) = -1/2 \implies x = 210^\circ, 330^\circ$.
4. **Resultado:** $90^\circ, 210^\circ, 270^\circ, 330^\circ$ ($\pi/2, 7\pi/6, 3\pi/2, 11\pi/6$ rad).

#### Ejemplo 4: Aplicación real con $USD (Fórmula General)
**Contexto:** El precio $P$ en $USD$ de un activo financiero sigue la estabilidad dada por: $\cos(2x) = 4\text{sen}^2(x) - \text{sen}(x)$.
1. Transformamos $\cos(2x)$ a $(1 - 2\text{sen}^2(x))$.
2. Igualamos a cero: $6\text{sen}^2(x) - \text{sen}(x) - 1 = 0$.
3. Usamos la **Fórmula General** ($a=6, b=-1, c=-1$):
   - $\text{sen}(x) = \frac{1 \pm \sqrt{1 - 4(6)(-1)}}{12} = \frac{1 \pm 5}{12}$.
   - $\text{sen}(x) = 1/2 \implies x = 30^\circ, 150^\circ$.
   - $\text{sen}(x) = -1/3 \implies x \approx 340.53^\circ$ y $199.47^\circ$ (usando `arcsen`).
4. **Resultado:** $30^\circ (\pi/6 \text{ rad}), 150^\circ (5\pi/6 \text{ rad})$ y valores aproximados.

---

### 6. EJERCICIOS PARA EL ESTUDIANTE

**🟢 Nivel Fácil (Factorización Directa)**
1. $\text{sen}^2(x) - \text{sen}(x) = 0$
2. $\cos^2(x) + 2\cos(x) + 1 = 0$
3. $2\text{sen}^2(x) - \text{sen}(x) = 0$
4. $\tan^2(x) - \tan(x) = 0$

---

**🟡 Nivel Medio (Identidades Pitagóricas)**
5. $2\cos^2(x) + 3\text{sen}(x) - 3 = 0$
6. $\text{sen}^2(x) - 2\cos(x) + 2 = 0$
7. $4\cos^2(x) + 4\text{sen}(x) - 1 = 0$
8. $2\text{sen}^2(x) - \cos(x) - 1 = 0$

---

**🔴 Nivel Avanzado (Ángulo Doble y Contexto Financiero $USD)**
9. $\text{sen}(2x) - \text{sen}(x) = 0$
10. $\cos(2x) + \cos(x) = 0$
11. **Análisis de Mercado:** Si el precio de un bono en $USD$ se equilibra cuando $\cos(2x) = \text{sen}(x)$, halla los puntos de equilibrio para $x \in [0, 360^\circ]$.
12. **Algoritmo de Trading:** Una IA de inversión detecta una señal de compra cuando la función de tendencia $\text{sen}(2x) + 2\cos(x) = 0$ se cumple. Halla los valores de $x$ para la señal.

> [!success] ✅ Respuestas (Verificadas)
> 1. $0^\circ, 180^\circ, 90^\circ$ ($0, \pi, \pi/2$ rad)
> 2. $180^\circ$ ($\pi$ rad)
> 3. $0^\circ, 180^\circ, 30^\circ, 150^\circ$ ($0, \pi, \pi/6, 5\pi/6$ rad)
> 4. $0^\circ, 180^\circ, 45^\circ, 225^\circ$ ($0, \pi, \pi/4, 5\pi/4$ rad)
> 5. $30^\circ, 150^\circ, 90^\circ$ ($\pi/6, 5\pi/6, \pi/2$ rad)
> 6. $0^\circ, 360^\circ$ ($0, 2\pi$ rad)
> 7. $210^\circ, 330^\circ$ ($7\pi/6, 11\pi/6$ rad) -- *¡Sí tiene solución!*
> 8. $60^\circ, 300^\circ, 180^\circ$ ($\pi/3, 5\pi/3, \pi$ rad)
> 9. $0^\circ, 180^\circ, 60^\circ, 300^\circ$ ($0, \pi, \pi/3, 5\pi/3$ rad)
> 10. $60^\circ, 180^\circ, 300^\circ$ ($\pi/3, \pi, 5\pi/3$ rad)
> 11. $30^\circ, 150^\circ, 270^\circ$ ($\pi/6, 5\pi/6, 3\pi/2$ rad)
> 12. $90^\circ, 270^\circ$ ($\pi/2, 3\pi/2$ rad)

---

### 7. AUTOEVALUACIÓN (MINI-PRUEBA)

**Pregunta 1:** Si al resolver una ecuación para un activo en $USD$ obtienes $\cos(x) = -1.5$, ¿cuál es el análisis correcto?
a) Usar `arccos` para hallar el ángulo exacto.
b) Indicar que esa rama no tiene solución pues el precio no puede modelarse ahí.
c) Multiplicar por $-1$ para que el valor sea positivo.
d) Sumar $1$ para entrar en el rango permitido.
*Respuesta: **b**. El coseno solo existe entre -1 y 1.*

**Pregunta 2:** En la ecuación $\text{sen}(2x) + \text{sen}(x) = 0$, ¿qué identidad es la llave para abrir el problema?
a) $\text{sen}^2(x) + \cos^2(x) = 1$
b) $\tan(x) = \text{sen}(x)/\cos(x)$
c) $\text{sen}(2x) = 2\text{sen}(x)\cos(x)$
d) $\cos(2x) = \cos^2(x) - \text{sen}^2(x)$
*Respuesta: **c**. Permite que todos los ángulos sean "x" y así poder aplicar factor común.*

**Pregunta 3:** Un modelo de criptomonedas da como resultado $\text{sen}(x) = 1/2$ en el primer cuadrante. ¿A qué ángulo en radianes corresponde?
a) $\pi/3$ rad
b) $\pi/4$ rad
c) $\pi/6$ rad
d) $\pi/2$ rad
*Respuesta: **c**. El seno de $30^\circ$ es $0.5$, y $30^\circ$ equivale a $\pi/6$ radianes.*

---

> [!tip] 💡 En la próxima clase
> ¡Excelente trabajo hoy! Has dominado la factorización y las identidades fundamentales. En la **Clase 03 — Identidades Trigonométricas Avanzadas**, aprenderemos a demostrar igualdades complejas y a manejar ecuaciones con múltiples funciones simultáneas. ¡Prepárate!

> [!info] 🧭 Navegación
> - Clase anterior: [[Clase 01 — Introducción a Ecuaciones Trigonométricas]]
> - Siguiente clase: [[Clase 03 — Identidades Trigonométricas Avanzadas]]