# Clase 03 — Suma, Resta y Multiplicación de Números Complejos

#algebra #additionandsubt

Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 3 de 5

> [!info] 🧭 Navegación
> - ⬅️ Anterior: [[Clase 02 — Representación en el Plano Complejo]]
> - 🏠 Inicio: [[00 - Índice del curso]]
> - ➡️ Siguiente: [[Clase 04 — División de Números Complejos]]

---

> [!info] 🌍 Relevancia y aplicaciones
> Operar con números complejos es fundamental para entender el comportamiento de ondas, procesar señales digitales y analizar circuitos eléctricos de corriente alterna. 
> 
> - 💵 **Finanzas ($USD):** Permite modelar flujos de capital donde la **parte real** es la inversión base y la *parte imaginaria* representa el factor de riesgo o volatilidad.
> - 🏗️ **Ingeniería:** Esencial para el diseño de estructuras oscilatorias y puentes, donde se calculan fuerzas que no actúan en una sola dirección.
> - 📊 **Audio y Sonido:** Se utiliza para calcular la impedancia en altavoces, asegurando que el sonido sea nítido y potente.

---

> [!note] 📌 ¿Qué es la Suma y Resta de números complejos?
> ¡Es supremamente fácil! Sumar o restar complejos es simplemente agrupar términos semejantes. Como dice el **Profe Alex**, solo debemos combinar las **partes reales con las reales** y las *partes imaginarias con las imaginarias*. 
> 
> En el caso de la resta, lo más sencillo es verla como **sumar el opuesto**. Es decir, le cambiamos el signo a la parte real e imaginaria del segundo número y luego sumamos normalmente.

> [!warning] ⚠️ Error común
> ❌ **Incorrecto:** Intentar fusionar la parte real con la imaginaria (ej: $3 + 4i = 7i$). ¡Esto es un pecado matemático!
> ✅ **Correcto:** Deben mantenerse separadas. El resultado de $3 + 4i$ no se puede simplificar más, se queda así: **3** + *4i*.

> [!tip] 💡 Truco para recordarlo
> Aplica la regla de las frutas: suma **"las manzanas con las manzanas"** (partes reales) y **"las peras con las peras"** (partes imaginarias que tienen la $i$). ¡No las mezcles en la licuadora!

---

### 🧮 Procedimiento: La Multiplicación "Paso a Paso"

Para multiplicar complejos, los tratamos como binomios algebraicos siguiendo este orden didáctico:

1. **Propiedad Distributiva:** Multiplicamos cada término del primer complejo por cada término del segundo.
2. **El pivote de $i^2$:** Al multiplicar las partes imaginarias, obtendrás un término con $i^2$. **¡Ojo aquí!** Por definición $i^2 = -1$. 
   * *Regla de oro:* Siempre que veas $i^2$, **bórralo y cambia el signo** del número que lo acompaña (ej: $+12i^2$ se convierte en $-12$; $-5i^2$ se convierte en $+5$).
3. **Agrupación Visual:** Reunimos las nuevas **partes reales** por un lado y las *partes imaginarias* por otro.
4. **Simplificación Final:** Operamos las sumas/restas para llegar a la forma $a + bi$.

---

### 📝 Ejemplos Prácticos

> [!example] Ejemplo 1: Suma básica
> Dados **$Z_1 = 3 + 4i$** y **$Z_2 = 7 - 4i$**:
> $({\mathbf{3}} + 4i) + ({\mathbf{7}} - 4i)$
> - Partes Reales: $3 + 7 = \mathbf{10}$
> - Partes Imaginarias: $4i - 4i = 0i$
> **Resultado:** $10$

> [!example] Ejemplo 2: Resta con el "Opuesto"
> Operación: $Z_2 - Z_3$ donde $Z_2 = \mathbf{7} - 4i$ y $Z_3 = \mathbf{-6} - 8i$.
> 1. Escribimos el primero igual: $7 - 4i$
> 2. Sumamos el **opuesto** del segundo: $+ (6 + 8i)$
> 3. Agrupamos: $({\mathbf{7 + 6}}) + (-4i + 8i)$
> **Resultado:** $13 + 4i$

> [!example] Ejemplo 3: Multiplicación de binomios (Método Profe Alex)
> Operación: $(2 + 3i)(-5 + 4i)$
> 1. **Distributiva:** $(2 \cdot -5) + (2 \cdot 4i) + (3i \cdot -5) + (3i \cdot 4i)$
> 2. **Desarrollo:** $-10 + 8i - 15i + (3 \cdot 4)(i \cdot i)$
> 3. **El paso clave:** $-10 - 7i + 12i^2$
> 4. **Transformación de $i^2$:** Como $i^2$ cambia el signo, $+12i^2$ se convierte en $-12$.
> 5. **Final:** $({\mathbf{-10 - 12}}) - 7i = -22 - 7i$
> **Resultado:** $-22 - 7i$

> [!example] Ejemplo 4: Multiplicación por Escalar ($USD)
> Un capital de inversión $C = \mathbf{100} + 50i$ USD se triplica ($3 \times C$).
> $3 \cdot (\mathbf{100} + 50i) = (3 \cdot \mathbf{100}) + (3 \cdot 50i)$
> **Resultado:** $300 + 150i$ USD

---

### ✍️ Ejercicios de Práctica

> [!abstract] 🟢 Nivel Fácil
> 1. $(5 + 2i) + (3 + 8i)$
> 2. $(10 - 4i) + (2 + i)$
> 3. $(7 + 6i) - (3 + 2i)$
> 4. $(-1 + i) - (1 - i)$

> [!abstract] 🟡 Nivel Medio
> 1. $2(3 - 4i)$
> 2. $(1 + i)(1 - i)$
> 3. $-3(2 + 5i)$
> 4. $(2 + i)(3 + i)$

> [!abstract] 🔴 Nivel Avanzado ($USD)
> *Nota: Al multiplicar por un factor (escalar), este afecta equitativamente tanto a la inversión real como al riesgo imaginario.*
> 1. Una deuda es $D = -500 - 200i$ USD. Si se aplica un factor de riesgo de $1.5$, ¿cuál es el nuevo valor?
> 2. Multiplica el flujo de caja $C_1 = 10 + 2i$ por $C_2 = 5 - 3i$.
> 3. Calcula el triple de la suma de $Z_a = 20 + 10i$ y $Z_b = 5 + 5i$.
> 4. Resta $Z_x = 100 - 20i$ de $Z_y = 50 + 10i$ y luego multiplica el resultado por $2$.

> [!success] ✅ Respuestas para el Docente
> **Fácil:** 1) $8 + 10i$ | 2) $12 - 3i$ | 3) $4 + 4i$ | 4) $-2 + 2i$
> **Medio:** 1) $6 - 8i$ | 2) $2$ (porque $1 - i^2 = 1 + 1$) | 3) $-6 - 15i$ | 4) $5 + 5i$
> **Avanzado:** 
> 1) $-750 - 300i$ USD
> 2) $56 - 20i$ USD *(Paso clave: $50 - 30i + 10i - 6i^2 \to 50 - 20i + 6$)*
> 3) $75 + 45i$ USD
> 4) $-100 + 60i$ USD

---

### 🧐 Autoevaluación

> [!question] Pregunta 1: Conceptual
> ¿Qué sucede con el término que contiene $i^2$ al finalizar una multiplicación?
> - a) Se elimina por ser un error.
> - b) Se convierte en $1$ y se suma.
> - c) Se sustituye por $-1$, lo que cambia el signo de su coeficiente y lo vuelve real.
> - d) Se mantiene para indicar que es un número complejo de segundo grado.
> > **Respuesta correcta: c.** Es el paso más importante: $i^2$ "muta" el término de imaginario a real con signo opuesto.

> [!question] Pregunta 2: Procedimental
> ¿Cuál es el resultado de la resta $(5 - 2i) - (-3 + 4i)$?
> - a) $2 + 2i$
> - b) $8 - 6i$
> - c) $8 + 2i$
> - d) $2 - 6i$
> > **Respuesta correcta: b.** Al sumar el opuesto tenemos $(\mathbf{5 + 3}) + (-2i - 4i) = 8 - 6i$.

> [!question] Pregunta 3: Aplicación $USD
> Si una cartera $A = 200 + 100i$ USD se multiplica por un escalar de $0.5$ (se reduce a la mitad), ¿cuál es el nuevo valor?
> - a) $100 + 50i$ USD
> - b) $400 + 200i$ USD
> - c) $100 + 100i$ USD
> - d) $200 + 50i$ USD
> > **Respuesta correcta: a.** El escalar $0.5$ se distribuye: $0.5(200) = 100$ y $0.5(100i) = 50i$.

---

> [!tip] 💡 En la próxima clase
> Ya dominas las operaciones básicas. En la siguiente sesión cerraremos el bloque con la **División de números complejos**, donde conoceremos a un aliado fundamental: "el conjugado".

> [!info] 🧭 Navegación
> - ⬅️ Anterior: [[Clase 02 — Representación en el Plano Complejo]]
> - 🏠 Inicio: [[00 - Índice del curso]]
> - ➡️ Siguiente: [[Clase 04 — División de Números Complejos]]