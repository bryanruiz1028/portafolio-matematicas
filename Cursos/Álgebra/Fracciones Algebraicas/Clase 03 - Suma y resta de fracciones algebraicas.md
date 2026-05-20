# Clase 03 — Suma y resta de fracciones algebraicas
#algebra #sumayrestadefra

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 4

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | [[Clase 04|Clase 04 ➡]]

---

> [!info] 🌍 Relevancia y aplicaciones
> Dominar la suma y resta de fracciones algebraicas es vital para simplificar modelos matemáticos, resolver ecuaciones de física y entender cómo cambian los sistemas complejos.
> - 💵 **Aplicación con $USD:** Modelado de presupuestos dinámicos donde los costos variables dependen de una incógnita $x$ (como el precio de la gasolina o materia prima).
> - 🏗️ **Aplicación práctica:** Cálculo de la resistencia total en circuitos eléctricos o determinación de tiempos exactos en el llenado de tanques de agua.
> - 📊 **Situación cotidiana:** Reparto proporcional de recursos o herencias cuando las cantidades base son desconocidas.

---

> [!note] 📌 ¿Qué es Suma y resta de fracciones algebraicas?
> Imagina que es como sumar fracciones normales (como $1/2 + 1/4$), pero ahora los números están jugando a las escondidas detrás de letras. El objetivo es el mismo: encontrar un "terreno común" para poder juntarlas.

> [!warning] ⚠️ Error común
> ❌ **Incorrecto:** Intentar simplificar o "tachar" términos individuales cuando hay sumas o restas pendientes en el numerador.
> ✅ **Correcto:** Primero debes realizar toda la operación de suma/resta y solo simplificar factores comunes al final, cuando todo sea una multiplicación.

> [!tip] 💡 Truco para recordarlo: El "Escudo Protector"
> Los paréntesis son tus **"escudos protectores"**. Siempre que veas un signo menos $(-)$ antes de una fracción, coloca el numerador que sigue entre paréntesis; ese signo cambiará el "humor" (el signo) de todo lo que esté protegido por el escudo.

---

### Procedimiento Estándar (MCM)

Para sumar o restar fracciones con distinto denominador, el secreto es convertirlas en **fracciones homogéneas** (que tengan el mismo denominador) siguiendo estos pasos:

```text
PASO 1 → Hallar el mínimo común múltiplo (MCM) de los denominadores.
PASO 2 → Amplificar las fracciones para que todas compartan ese MCM (Fracciones Homogéneas).
PASO 3 → Sumar o restar los numeradores resultantes (usando escudos protectores).
PASO 4 → Simplificar la fracción final (factorizar el resultado si es necesario).
```

---

### Desarrollo de Ejemplos

> [!example] Ejemplo 1: Básico (Monomios y Homogéneas)
> **Enunciado:** $\frac{x+1}{2x} + \frac{3x-2}{2x}$
> 
> Como los denominadores ya son iguales, operamos directamente:
> 1.  **Mantener denominador:** $2x$.
> 2.  **Operar numeradores:** $(x + 1) + (3x - 2)$.
> 3.  **Agrupar términos semejantes:** $x + 3x = 4x$ y $1 - 2 = -1$.
> 
> **Resultado final:** $\frac{4x-1}{2x}$

> [!example] Ejemplo 2: Signos y Polinomios (Uso del Escudo)
> **Enunciado:** $\frac{m+2}{m-2} - \frac{m+3}{m-3}$
> 
> 1.  **Hallar MCM:** Al no ser factorizables, el MCM es $(m-2)(m-3)$.
> 2.  **Amplificar (Paso Intermedio):**
>     $\frac{(m+2)(m-3)}{(m-2)(m-3)} - \frac{(m+3)(m-2)}{(m-2)(m-3)}$
> 3.  **Aplicar Escudo Protector:**
>     $(m+2)(m-3) - \mathbf{[(m+3)(m-2)]}$
> 4.  **Desarrollo Distributivo:**
>     - Primero: $(m^2 - 3m + 2m - 6) = m^2 - m - 6$
>     - Segundo: $(m^2 - 2m + 3m - 6) = m^2 + m - 6$
> 5.  **Operación final:** $(m^2 - m - 6) - (m^2 + m - 6) = m^2 - m - 6 - m^2 - m + 6 = -2m$
> 
> **Resultado final:** $\frac{-2m}{(m-2)(m-3)}$
> *Nota: No simplifiques la $m$ de arriba con las de abajo; las de abajo están "atrapadas" en restas.*

> [!example] Ejemplo 3: Avanzado (Factorización)
> **Enunciado:** $\frac{x}{x^2-1} - \frac{x+1}{(x-1)^2}$
> 
> 1.  **Factorizar:** $x^2-1 = (x+1)(x-1)$. El otro es $(x-1)^2$.
> 2.  **MCM:** $(x+1)(x-1)^2$ (tomamos el mayor exponente).
> 3.  **Amplificar (Paso Intermedio):**
>     $\frac{x(x-1)}{(x+1)(x-1)^2} - \frac{(x+1)(x+1)}{(x+1)(x-1)^2}$
> 4.  **Operar Numeradores:** $(x^2 - x) - \mathbf{(x^2 + 2x + 1)}$
> 5.  **Simplificar:** $x^2 - x - x^2 - 2x - 1 = -3x - 1$.
> 
> **Resultado final:** $\frac{-3x-1}{(x+1)(x-1)^2}$

> [!example] Ejemplo 4: Aplicación Real en $USD (Costos Variables)
> **Problema:** Una empresa calcula que su costo de transporte es $\frac{5}{x^2+x-20}$ y su costo de materiales es $\frac{x}{x^2-4x-5}$. Hallar el costo total.
> 
> 1.  **Factorizar denominadores:**
>     - Transporte: $x^2+x-20 = (x+5)(x-4)$
>     - Materiales: $x^2-4x-5 = (x-5)(x+1)$
> 2.  **Hallar MCM:** $(x+5)(x-4)(x-5)(x+1)$
> 3.  **Amplificar y Unificar:**
>     $\frac{5(x-5)(x+1) + x(x+5)(x-4)}{(x+5)(x-4)(x-5)(x+1)}$
> 4.  **Resolver Numerador:**
>     - $5(x^2 - 4x - 5) + x(x^2 + x - 20)$
>     - $5x^2 - 20x - 25 + x^3 + x^2 - 20x$
>     - **Sumar semejantes:** $x^3 + 6x^2 - 40x - 25$
> 
> **Resultado final:** $\frac{x^3 + 6x^2 - 40x - 25}{(x+5)(x-4)(x-5)(x+1)}$ dólares.

---

### Ejercicios Prácticos

> [!abstract] 🟢 Nivel Fácil
> 1. $\frac{5}{x} + \frac{2}{x}$
> 2. $\frac{a+2}{3a} - \frac{1}{3a}$
> 3. $\frac{7x}{2y} + \frac{3x}{2y}$
> 4. $\frac{4a}{5b} + \frac{a}{5b}$

> [!abstract] 🟡 Nivel Medio
> 1. $\frac{2}{x-3} + \frac{x}{x+2}$
> 2. $\frac{a+b}{3a+b} - \frac{a-b}{3a+b}$
> 3. $\frac{5}{x+1} - \frac{3}{x-1}$
> 4. $\frac{x+2}{x} + \frac{x}{x+2}$

> [!abstract] 🔴 Nivel Avanzado
> 1. El precio de un insumo es $\frac{x+1}{x^2-x-20}$ USD y sube un valor de $\frac{-(x-7)}{x^2-4x-5}$ USD. ¿Cuál es el precio final?
> 2. $\frac{x}{x^2-1} - \frac{x+1}{(x-1)^2}$
> 3. $\frac{3}{x^2-5x+6} + \frac{2}{x^2-4}$
> 4. $\frac{x-1}{x^2-4x+4} - \frac{x+2}{x^2-4}$

> [!success] ✅ Respuestas para el docente
> **Fácil:** 1) $7/x$ | 2) $(a+1)/3a$ | 3) $5x/y$ | 4) $a/b$
> **Medio:** 1) $\frac{x^2-x+4}{(x-3)(x+2)}$ | 2) $\frac{2b}{3a+b}$ | 3) $\frac{2x-8}{(x+1)(x-1)}$ | 4) $\frac{2x^2+4x+4}{x(x+2)}$
> **Avanzado:** 
> 1) $\frac{5x+29}{(x-5)(x+4)(x+1)}$
> 2) $\frac{-3x-1}{(x+1)(x-1)^2}$
> 3) $\frac{5x}{(x-3)(x-2)(x+2)}$
> 4) $\frac{1}{(x-2)^2}$

---

### Autoevaluación

> [!question] ¿Cuál es el objetivo de hallar el MCM en fracciones algebraicas?
> **Respuesta:** Convertir fracciones heterogéneas en fracciones homogéneas (con igual denominador) para poder sumar o restar sus numeradores.

> [!question] Resuelve mentalmente: $\frac{10x}{3a} - \frac{4x}{3a}$
> a) $\frac{14x}{3a}$ | b) $\frac{6x}{3a}$ | c) $\frac{2x}{a}$ | d) $\frac{6x}{0}$
> **Respuesta:** c) $\frac{2x}{a}$. Al restar queda $6x/3a$, y al simplificar entre 3 obtenemos $2x/a$.

> [!question] Si un costo es $\frac{10}{x}$ dólares y otro es $\frac{5}{x}$ dólares, ¿cuál es el total?
> **Respuesta:** $\frac{15}{x}$ dólares.

---

> [!tip] 💡 En la próxima clase
> Utilizaremos estas herramientas para resolver **Ecuaciones Algebraicas**, donde el objetivo será despejar el valor de $x$ tras unificar todas las fracciones.

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | [[Clase 04|Clase 04 ➡]]