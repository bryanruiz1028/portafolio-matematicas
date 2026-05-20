# Clase 04 — Ecuaciones Exponenciales mediante Cambio de Variable

`#algebra #exponentialequa`

[[Clase 03|⬅ Clase 03]] | [[Índice del Curso|🏠 Índice]] | [[Clase 05|Clase 05 ➡]]

**Bloque 1 | Lección 4 de 8**

---

### ¿Por qué es importante esta clase?

> [!info] **La magia de la simplificación**
> El cambio de variable es una herramienta poderosa que permite transformar una ecuación exponencial aparentemente "imposible" o muy compleja en una forma familiar que ya dominas, como lo son las ecuaciones lineales o cuadráticas.
> 
> *   **💵 $USD:** Se utiliza para modelar el crecimiento de intereses compuestos en períodos donde el tiempo se presenta en múltiplos (ej. cada dos años).
> *   **🏗️ Construcción:** Permite calcular la degradación de materiales o la pérdida de resistencia en estructuras sometidas a esfuerzos constantes.
> *   **📊 Situación cotidiana:** Es fundamental para estimar la propagación de tendencias virales o el crecimiento acelerado de seguidores en redes sociales.

---

### Concepto Clave y Reglas de Oro

> [!note] **¿Qué es el Cambio de Variable?**
> Consiste en reemplazar una expresión exponencial que se repite en la ecuación (por ejemplo, $2^x, 3^x$ o $5^x$) por una letra simple (como $t, u$ o $m$). Esto "limpia" visualmente la ecuación para que podamos resolverla usando álgebra básica.

> [!warning] **¡No te detengas a mitad del camino!**
> Un error muy común es hallar el valor de la variable auxiliar (ej. encontrar que $u = 9$) y pensar que el ejercicio terminó. Recuerda que el objetivo es hallar el valor de **$x$**. Siempre debes "deshacer" el cambio de variable (ej. si $3^x = u$, entonces $3^x = 9$, por lo tanto $x = 2$).

> [!tip] **Identifica el patrón cuadrático**
> Si en una ecuación ves un término con exponente $x$ y otro con exponente $2x$ (por ejemplo $3^x$ y $3^{2x}$), es una señal clara de que terminarás resolviendo una **ecuación cuadrática**. ¡Es el momento de usar tus habilidades de factorización!

---

### Procedimiento Paso a Paso

Para resolver estas ecuaciones de forma infalible, aplica este esquema en tu cuaderno:

```text
PASO 1: Separar los términos usando propiedades de las potencias.
        (Suma en exponente -> Multiplicación; Resta en exponente -> División).
PASO 2: Realizar la sustitución de la potencia base por una letra auxiliar 
        (ej. a^x = u).
PASO 3: Resolver la ecuación resultante (puede ser lineal o cuadrática 
        por factorización).
PASO 4: Deshacer el cambio de variable para encontrar el valor real de x 
        igualando las bases.
```

---

### Ejemplos Desarrollados

> [!example] **Ejemplo 1: Caso Básico (Suma de potencias)**
> **Resolver:** $2^{x+1} + 2^x + 2^{x-1} = 28$
> 1. **Separar:** $2^x \cdot 2^1 + 2^x + \frac{2^x}{2^1} = 28$
> 2. **Cambio de variable:** Sea $t = 2^x$. La ecuación queda: $2t + t + \frac{t}{2} = 28$
> 3. **Eliminar denominador:** Multiplicamos todo por 2: $4t + 2t + t = 56 \Rightarrow 7t = 56$
> 4. **Resolver t:** $t = \frac{56}{7} = 8$
> 5. **Regresar a x:** $2^x = 8$. Como $8 = 2^3$, entonces **$x = 3$**.
> 
> **💡 El chequeo del Profe Alex:** Si $x=3$, entonces $2^4 + 2^3 + 2^2 = 16 + 8 + 4 = 28$. ¡Es correcto!

> [!example] **Ejemplo 2: Trinomio Cuadrático**
> **Resolver:** $(2^x)^2 - 5(2^x) + 4 = 0$
> 1. **Cambio de variable:** Sea $u = 2^x$. La ecuación queda: $u^2 - 5u + 4 = 0$
> 2. **Factorizar:** $(u - 4)(u - 1) = 0$
> 3. **Valores de u:** $u_1 = 4$ y $u_2 = 1$.
> 4. **Regresar a x:**
>    *   Para $u = 4 \Rightarrow 2^x = 2^2 \Rightarrow \mathbf{x = 2}$
>    *   Para $u = 1 \Rightarrow 2^x = 2^0 \Rightarrow \mathbf{x = 0}$
> 
> **💡 El chequeo del Profe Alex:** Verifiquemos $x=0$. $(2^0)^2 - 5(2^0) + 4 = (1)^2 - 5(1) + 4 = 1 - 5 + 4 = 0$. ¡Perfecto!

> [!example] **Ejemplo 3: Caso Avanzado (Reconocimiento de 2x)**
> **Resolver:** $3^{2x} - 28(3^x) + 27 = 0$
> 1. **Transformar:** $(3^x)^2 - 28(3^x) + 27 = 0$
> 2. **Sustitución:** Sea $u = 3^x \Rightarrow u^2 - 28u + 27 = 0$
> 3. **Factorizar:** $(u - 27)(u - 1) = 0$. Por lo tanto, $u = 27$ o $u = 1$.
> 4. **Solución final:**
>    *   $3^x = 27 \Rightarrow 3^x = 3^3 \Rightarrow \mathbf{x = 3}$
>    *   $3^x = 1 \Rightarrow 3^x = 3^0 \Rightarrow \mathbf{x = 0}$
> 
> **💡 El chequeo del Profe Alex:** Con $x=3$, la ecuación es $3^6 - 28(3^3) + 27 = 729 - 756 + 27 = 0$. ¡Funciona!

> [!example] **Ejemplo 4: Aplicación en Inversiones ($USD)**
> **Problema:** Una inversión crece según la ecuación $5^{2x} - 30(5^x) + 125 = 0$, donde $x$ es el tiempo en años. ¿En qué años alcanza los puntos de equilibrio?
> 1. **Sustitución:** Sea $m = 5^x \Rightarrow m^2 - 30m + 125 = 0$.
> 2. **Factorizar:** Buscamos números que multiplicados den 125 y sumados 30: $(m - 25)(m - 5) = 0$.
> 3. **Valores:** $m = 25$ y $m = 5$.
> 4. **Deshacer:**
>    *   $5^x = 25 \Rightarrow \mathbf{x = 2 \text{ años}}$
>    *   $5^x = 5 \Rightarrow \mathbf{x = 1 \text{ año}}$

---

### Ejercicios para el Estudiante

> [!abstract] **Nivel 🟢 Fácil**
> 1. $3^{x+1} + 3^x = 36$
> 2. $2^x + 2^{x+2} = 40$
> 3. $5^x + 5^{x-1} = 30$
> 4. $4^{x+1} - 4^x = 48$

> [!abstract] **Nivel 🟡 Medio**
> 5. $2^{2x} - 6(2^x) + 8 = 0$
> 6. $3^{2x} - 10(3^x) + 9 = 0$
> 7. $2^{2x} - 12(2^x) + 32 = 0$
> 8. $4^{2x} - 5(4^x) + 4 = 0$

> [!abstract] **Nivel 🔴 Avanzado (Contextualizado $USD)**
> 9. **Crecimiento de Capital:** Una cuenta de ahorros sigue el modelo $10^{2x} - 110(10^x) + 1000 = 0$. Halla los valores de $x$.
> 10. **Proyección de Costos:** Resuelve $3^{2x+1} - 82(3^x) + 27 = 0$ (Pista: Separa el $+1$ primero).
> 11. **Depreciación de Activos:** Un equipo pierde valor según $7^{2x} - 8(7^x) + 7 = 0$. Determina los años $x$ de evaluación.
> 12. **Gastos Operativos:** Si los gastos siguen la forma $2^{x+1} + 2^x - 2^{x-1} = 20$, encuentra el valor de $x$.

> [!success] **Respuestas**
> 1) $x=2$; 2) $x=3$; 3) $x=2$; 4) $x=2$; 5) $x=2, x=1$; 6) $x=2, x=0$; 7) $x=3, x=2$; 8) $x=1, x=0$; 9) $x=2, x=1$; 10) $x=3, x=-1$; 11) $x=1, x=0$; 12) $x=3$.

---

### Mini-prueba de Autoevaluación

> [!question] **1. Conceptual**
> ¿Cuál es la forma correcta de separar $2^{x-1}$ antes de hacer el cambio de variable?
> *   a) $2^x - 2^1$
> *   b) $2^x / 2$
> *   c) $2^x \cdot 2$

> [!question] **2. Procedimental**
> Si al resolver una ecuación mediante el cambio $3^x = u$ obtienes que $u = 9$, ¿cuál es el valor de $x$?
> *   a) $x = 9$
> *   b) $x = 3$
> *   c) $x = 2$

> [!question] **3. Escenario $USD**
> En una proyección financiera, se llega a la expresión $5^x = 125$. ¿Cuál es el valor del tiempo $x$?
> *   a) 3
> *   b) 25
> *   c) 5

---

### Cierre y Próximo Tema

¡Excelente trabajo! Dominar el **cambio de variable** es un gran paso en tu formación algebraica. Como habrás notado, la clave para resolver estos ejercicios con rapidez es tener mucha agilidad en la **factorización de trinomios**. Si sientes que te costó identificar los números en los paréntesis, te recomiendo repasar ese tema, pues lo seguiremos usando.

En la siguiente clase, daremos un paso más allá y veremos cómo aplicar estos mismos conceptos cuando las bases no son tan evidentes. ¡Nos vemos en la próxima!

[[Clase 03|⬅ Clase 03]] | [[Índice del Curso|🏠 Índice]] | [[Clase 05|Clase 05 ➡]]