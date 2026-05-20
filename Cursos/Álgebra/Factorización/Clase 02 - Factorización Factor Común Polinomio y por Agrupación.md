# Clase 02 — Factorización: Factor Común Polinomio y por Agrupación

#algebra #factorizacinpor

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 10

> [!info] 🧭 Navegación
> [[Clase 01 — Factor Común Monomio|← Clase 01]] | **Clase 02** | [[00 - Índice del curso|Índice]]

---

### 🌍 Relevancia y aplicaciones

> [!info] ¿Por qué es importante esta clase?
> Factorizar es el arte de simplificar lo complejo. En esta lección, aprenderás a manejar "bloques" de información, una habilidad esencial para:
>
> *   💵 **Ahorro en compras masivas:** Imagina comprar diferentes productos que comparten el mismo impuesto o precio base. Agrupar las cantidades antes de multiplicar te permite calcular el total en $USD de forma más rápida y sin errores.
> *   🏗️ **Cálculo de áreas compuestas:** En arquitectura y construcción, las estructuras suelen dividirse en secciones. Factorizar permite sumar áreas de materiales distintos que comparten una dimensión común, optimizando el diseño.
> *   📊 **Simplificación en hojas de cálculo:** Al programar fórmulas financieras, agrupar términos reduce la longitud de las ecuaciones, haciendo que tus modelos sean más claros y eficientes.

---

### 📌 Conceptos Clave

> [!note] **¿Qué es Factorización por factor común?**
> Factorizar es transformar una suma o resta en una **multiplicación**. Imagina que estás "extrayendo" o "repartiendo" lo que se repite. En el **Factor Común Polinomio**, lo que se repite no es solo una letra o un número, sino un paréntesis completo (un "bloque" o "gemelo").

> [!warning] ⚠️ Error común: El término "1" (marcador de posición)
> Cuando divides un término entre sí mismo durante la factorización (por ejemplo, $x^2 / x^2$), el resultado **siempre es 1**. Nunca desaparece ni se convierte en cero. Ese "1" actúa como un marcador de posición que mantiene la estructura original de la expresión.

> [!tip] 💡 Truco para recordarlo: "Identifica al gemelo"
> Busca el paréntesis que sea exactamente igual en todos los términos. Si encuentras "gemelos", ese es tu factor común. Si los signos están al revés (por ejemplo, uno es $a-b$ y el otro es $-a+b$), ¡puedes igualarlos factorizando el signo negativo!

---

### 🚀 Procedimiento Paso a Paso (Método por Agrupación)

Para resolver ejercicios donde no hay un factor común para todos los términos, utilizamos la agrupación (común en expresiones de 4 o 6 términos). Sigue estos pasos críticos:

```text
PASO 1 → Revisión y conteo: Verifica si hay un factor común global para TODO el ejercicio. 
         Luego, identifica si hay 4 o 6 términos para agrupar.
PASO 2 → Agrupar: Forma parejas (o tríos) que tengan letras o números en común.
PASO 3 → Extraer Factor Común: Realiza la división mental de cada pareja. 
         "Quita" lo que se repite y deja el resto dentro de un paréntesis.
PASO 4 → Factor Común Polinomio: Extrae el paréntesis "gemelo" que quedó repetido.
```

---

### 📝 Ejemplos Prácticos

#### Ejemplo 1: Caso básico (Polinomio)
**Expresión:** $m(a-b) + n(a-b)$
1. **Identificar:** El paréntesis $(a-b)$ es el factor común ("el gemelo").
2. **Dividir mentalmente:** Al "quitar" $(a-b)$ del primer término queda $m$. Al quitarlo del segundo queda $n$.
3. **Resultado:** $(a-b)(m+n)$

#### Ejemplo 2: Caso con signos (Técnica del negativo)
**Expresión:** $-m-n + x(m+n)$
1. **Observar:** Los primeros términos $-m-n$ tienen signos opuestos al paréntesis $(m+n)$.
2. **Factorizar el signo:** Extraemos el menos: $-(m+n) + x(m+n)$. (Recuerda que delante del primer paréntesis queda un $-1$ invisible).
3. **Extraer factor:** El gemelo es $(m+n)$.
4. **Resultado:** $(m+n)(-1+x)$ o convenientemente $(m+n)(x-1)$.

#### Ejemplo 3: Caso avanzado (Agrupación por dos vías)
**Expresión:** $a^2 + ab + ax + bx$
*   **Forma A (Agrupando 1-2 y 3-4):**
    $(a^2 + ab) + (ax + bx) \rightarrow a(a+b) + x(a+b) = \mathbf{(a+b)(a+x)}$
*   **Forma B (Agrupando 1-3 y 2-4):**
    $(a^2 + ax) + (ab + bx) \rightarrow a(a+x) + b(a+x) = \mathbf{(a+x)(a+b)}$
*   **Lección:** No importa cómo agrupes, el resultado es el mismo porque el orden de los factores no altera el producto.

#### Ejemplo 4: Aplicación real ($USD)
Compramos $x$ cajas de clavos y $1$ martillo. El precio de cada caja es $(a+b)$ y el martillo también cuesta $(a+b)$. Simplifica el costo total.
1. **Planteamiento:** $x(a+b) + 1(a+b)$
2. **Factorización:** $(a+b)(x+1)$.
3. **Uso:** Ahora solo sumas las cantidades $(x+1)$ y multiplicas por el precio una sola vez.

> [!tip] 💡 Pro-Tip: La Verificación
> Siempre puedes comprobar si tu factorización es correcta multiplicando los paréntesis resultantes (propiedad distributiva). Si al multiplicar regresas a la expresión original, ¡tu trabajo es perfecto!

---

### ✍️ Ejercicios para el Estudiante

**🟢 Nivel: Fácil (Factor Común Polinomio)**
1. $x(a+1) + y(a+1)$
2. $a(n+2) + (n+2)$
3. $2x(m-n) + (m-n)$
4. $a(x+1) - b(x+1)$

**🟡 Nivel: Medio (Agrupación de 4 términos y MCD)**
5. $12ax + 24ay + 36bx + 72by$ (Busca primero el MCD de todos los coeficientes).
6. $a^2 + ab + ac + bc$
7. $4a^3 + 4a - a^2 - 1$
8. $x^2 - x + 3x - 3$

**🔴 Nivel: Avanzado (Signos y Aplicaciones en $USD)**
9. Una factura muestra dos cobros: $12x(y+5)$ y $8w(y+5)$. Factoriza para hallar el factor común máximo.
10. $m^2 + mn - m - n$
11. $2x^2 - 4xy - x + 2y$
12. $ax - ay - x + y$

> [!success] ✅ Respuestas (para el docente)
> 1. $(a+1)(x+y)$ | 2. $(n+2)(a+1)$ | 3. $(m-n)(2x+1)$ | 4. $(x+1)(a-b)$
> 5. $12(a+3b)(x+2y)$ | 6. $(a+b)(a+c)$ | 7. $(a^2+1)(4a-1)$ | 8. $(x-1)(x+3)$
> 9. $4(y+5)(3x+2w)$ | 10. $(m+n)(m-1)$ | 11. $(x-2y)(2x-1)$ | 12. $(x-y)(a-1)$

---

### 📝 Mini-prueba de Autoevaluación

1. **¿Qué marcador de posición queda cuando un término se divide por sí mismo en la factorización?**
   - a) 0
   - b) 1
   - c) Se elimina la posición.

2. **Para factorizar $x^2 + xy + ax + ay$ por agrupación, ¿cuál es el primer factor común de la pareja $(x^2 + xy)$?**
   - a) $y$
   - b) $x$
   - c) $a$

3. **Si tienes dos servicios en $USD: $15(p+q)$ y $10(p+q)$, ¿cuál es la expresión totalmente factorizada usando el MCD numérico?**
   - a) $5(p+q)(3+2)$
   - b) $25(p+q)$
   - c) $5(p+q)$

---

> [!tip] 💡 En la próxima clase
> Ya dominas el arte de encontrar "gemelos". En la Clase 03, aprenderás la **Diferencia de Cuadrados**, donde aprenderemos a "desarmar" binomios especiales de forma instantánea.

> [!info] 🧭 Navegación
> [[Clase 01 — Factor Común Monomio|← Clase 01]] | **Clase 02** | [[00 - Índice del curso|Índice]]