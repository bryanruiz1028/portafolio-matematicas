# Clase 01 — Sistemas de ecuaciones de 3x3 | Introducción

#algebra #sistemasdeecuac

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 4

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]

---

> [!info] 🌍 Relevancia y aplicaciones
> Resolver estos sistemas permite encontrar un punto único en el espacio donde se intersectan tres dimensiones o planos. Es el paso fundamental para entender el mundo tridimensional.
> - 💵 **Costos:** Calcular el precio exacto de tres productos distintos (ej. una manzana, una pera y una sandía) tras realizar varias compras combinadas.
> - 🏗️ **Ingeniería:** Determinar el punto de equilibrio donde se unen tres fuerzas o soportes en una estructura 3D.
> - 📊 **Situación cotidiana:** Distribuir cantidades exactas de tres ingredientes en una receta para cumplir con un peso total específico.

---

### 3. Concepto Clave: ¿Qué es un Sistema 3x3?

> [!note] 📌 ¿Qué es Sistemas de ecuaciones de 3x3?
> Es un conjunto de 3 ecuaciones lineales con 3 incógnitas (normalmente $x, y, z$). Buscamos los valores que, al ser reemplazados, hacen que las tres igualdades sean verdaderas al mismo tiempo.
> 
> **La lógica de la notación:**
> Según explica el Profe Alex, cuando ves un número pegado a una letra (ej. $3x$), esto indica una **multiplicación**. Por ejemplo, si $3x = 15$, la solución es $x = 5$ porque $3 \cdot 5 = 15$.
> 
> **Representación geométrica:**
> - Una ecuación con 1 variable representa un **punto**.
> - Una ecuación con 2 variables representa una **línea** en un plano 2D.
> - Una ecuación con 3 variables representa un **plano** (como una hoja de papel) en un espacio 3D.

> [!warning] ⚠️ Error común
> Un error frecuente es creer que si encuentras valores que funcionan para la primera ecuación, ya terminaste. ¡Cuidado! Eso es un paso incompleto. Para que sea una solución del *sistema*, debe ser la "llave" que abre las tres puertas (ecuaciones) al mismo tiempo.

> [!tip] 💡 Truco para recordarlo
> Usa la analogía de la **hoja de papel**: Imagina cada ecuación como una hoja de papel infinita flotando en el espacio. La solución del sistema es el único punto exacto donde las tres hojas se cruzan. A este punto se le llama **ordenada triple** y se escribe como $(x, y, z)$.

---

### 4. Procedimiento Paso a Paso (Verificación)

Una vez que entendemos qué es un sistema, el primer paso didáctico es aprender a **verificar** si una propuesta de solución es correcta. Para confirmar si un punto $(x, y, z)$ funciona, sigue este proceso:

1. **PASO 1 →** Identificar los valores numéricos asignados a cada variable: $x, y, z$.
2. **PASO 2 →** Reemplazar las variables en la **primera ecuación** y realizar las operaciones.
3. **PASO 3 →** Repetir el reemplazo en la **segunda y tercera ecuación** de forma independiente.
4. **PASO 4 →** Confirmar si se cumple la igualdad en los tres casos para asegurar que es una **verdad matemática**.

---

### 5. Bloques de Ejemplos

> [!example] Ejemplo 1: Verificación básica
> Dada la ecuación $x + y + z = 10$, probemos el punto $(1, 2, 7)$:
> $$1 + 2 + 7 = 10 \implies 10 = 10$$
> Se cumple la igualdad.

> [!example] Ejemplo 2: El efecto de los signos
> En la misma ecuación $x + y + z = 10$, probemos el punto $(5, 20, -15)$:
> $$5 + 20 + (-15) = 10 \implies 25 - 15 = 10 \implies 10 = 10$$
> **Nota:** Recuerda que, según la ley de signos, sumar un número negativo es equivalente a restar.

> [!example] Ejemplo 3: ¿Por qué debe cumplir las TRES?
> Supongamos un sistema donde las dos primeras ecuaciones dan una verdad, pero la tercera es $x + y + z = 5$.
> Si probamos el punto $(1, 2, 7)$:
> 1. $1 + 2 + 7 = 10$ (Verdad ✅)
> 2. $1 + 2 + 7 = 10$ (Verdad ✅)
> 3. $1 + 2 + 7 = 10$ (¡Falso! ❌ Debería ser $5$)
> **Conclusión:** $(1, 2, 7)$ **no** es solución del sistema.

> [!example] Ejemplo 4: Aplicación real ($USD)
> Si 1 manzana ($x$), 1 pera ($y$) y 1 sandía ($z$) cuestan $\$10$ USD:
> Ecuación: $x + y + z = 10$.
> Si el mercado dice que los precios son $(\$2, \$3, \$5)$:
> Verificación: $2 + 3 + 5 = 10$. Los precios son una solución válida para el sistema.

---

### 6. Ejercicios para el Estudiante

> [!abstract] Actividades de Práctica
> **🟢 Nivel Fácil: Encuentra la variable faltante**
> 1. $x + y + z = 15$ | Si $x = 5, y = 5$, ¿cuánto vale $z$?
> 2. $x + y + z = 20$ | Si $x = 10, z = 2$, ¿cuánto vale $y$?
> 3. $x + y + z = 8$ | Si $x = 4, y = 6$, ¿cuánto vale $z$?
> 4. $x + y + z = 12$ | Si $x = 15, y = 2$, ¿cuánto vale $z$?
>
> **🟡 Nivel Medio: Coeficientes y multiplicaciones**
> 1. $2x + y + z = 10$ | Verifica si $(2, 3, 3)$ es solución.
> 2. $x + 3y + z = 15$ | Verifica si $(2, 4, 1)$ es solución.
> 3. $2x + 2y + 2z = 24$ | Verifica si $(6, 4, 2)$ es solución.
> 4. $3x - y + z = 8$ | Verifica si $(3, 2, 1)$ es solución.
>
> **🔴 Nivel Avanzado: Planteamiento $USD**
> 1. Una entrada ($x$), palomitas ($y$) y refresco ($z$) cuestan $\$20$ USD. Si $x = 11$ y $y = 5$, halla $z$.
> 2. Tres amigos compran un regalo de $\$30$ USD. El amigo $x$ pone $\$12$, el amigo $y$ pone $\$10$. ¿Cuánto pone $z$?
> 3. Un kit de herramientas cuesta $\$60$ USD. La herramienta $x$ cuesta $\$15$, la herramienta $y$ cuesta el doble que $x$. ¿Cuánto cuesta $z$?
> 4. Tres libros idénticos cuestan $\$45$ USD. ¿Cuál es el valor de $x, y, z$?

> [!success] ✅ Respuestas para el docente
> **Fácil:** 1) $z = 5$ | 2) $y = 8$ | 3) $z = -2$ | 4) $z = -5$
> **Medio:** 
> 1) Sí: $2(2) + 3 + 3 = 10 \rightarrow 4 + 3 + 3 = 10$ 
> 2) Sí: $2 + 3(4) + 1 = 15 \rightarrow 2 + 12 + 1 = 15$
> 3) Sí: $2(6) + 2(4) + 2(2) = 24 \rightarrow 12 + 8 + 4 = 24$
> 4) Sí: $3(3) - 2 + 1 = 8 \rightarrow 9 - 2 + 1 = 8$
> **Avanzado:** 
> 1) $z = 4$ | 2) $z = 8$ | 3) $y = 30 \rightarrow 15 + 30 + z = 60 \rightarrow z = 15$ | 4) $x = 15, y = 15, z = 15$

---

### 7. Mini-prueba de Autoevaluación

> [!question] Comprueba lo aprendido
> 1. **¿Qué representa geométricamente una sola ecuación con tres incógnitas?**
>    *(Respuesta: Un plano, comparable a una hoja de papel que se extiende al infinito).*
> 2. **¿Qué significa encontrar la solución de un sistema de 3x3?**
>    *(Respuesta: Hallar los valores de las variables que transforman las tres ecuaciones en una verdad matemática al mismo tiempo).*
> 3. **Si $x + y + z = 25$ USD y sabemos que $x = 10$ y $y = 5$, ¿cuánto vale $z$?**
>    *(Respuesta: $z = 10$).*

---

### 8. Cierre y Próximo Tema

> [!tip] 💡 En la próxima clase
> Ahora que dominas la verificación, aprenderemos los métodos para resolver estos sistemas desde cero. Exploraremos: **Reducción (Eliminación), Sustitución, Regla de Cramer (Determinantes), Método de Gauss y Método de Gauss-Jordan.**

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]