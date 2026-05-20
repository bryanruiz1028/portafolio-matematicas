# Clase 02 — Eliminación de signos de agrupación y operaciones combinadas

#algebra #eliminarsignosd

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 4

> [!info] 🧭 Navegación
> ◀ [[Clase 01]] | ▲ [[00 - Índice del curso|Índice]] | ▶ [[Clase 03]]

---

> [!info] 🌍 Relevancia y aplicaciones
> El orden de las operaciones y los signos de agrupación permiten organizar cálculos complejos de forma lógica y jerárquica. Al agrupar términos, establecemos prioridades que evitan errores y garantizan que todos lleguemos al mismo resultado matemático.
> 
> - 💵 **Aplicación con $USD**: Se utilizan corchetes para separar el cálculo de "Precio Unitario × Cantidad" del "Presupuesto Inicial", permitiendo calcular el cambio exacto tras aplicar descuentos.
> - 🏗️ **Aplicación práctica**: Es vital en fórmulas de ingeniería para calcular áreas y perímetros de estructuras con formas compuestas.
> - 📊 **Situación cotidiana**: Organización de presupuestos familiares, agrupando ahorros y gastos para conocer el saldo real disponible.

---

### Conceptos Clave y Reglas Fundamentales

> [!note] 📌 ¿Qué es Eliminar signos de agrupación?
> Imagina que los signos de agrupación (paréntesis, corchetes y llaves) son como **"cápsulas"** que protegen las operaciones que están dentro. Para resolver un problema, debemos abrir estas cápsulas desde la más pequeña hasta la más grande, resolviendo lo que hay dentro antes de eliminarlas.
> 
> **Regla de Oro**: Si no hay un signo entre un número y un paréntesis (ejemplo: $3(2)$), esto indica una **multiplicación**.

> [!warning] ⚠️ Error común
> Un error frecuente es quitar los paréntesis sin aplicar la ley de signos al valor que está dentro. 
> - ❌ **Incorrecto**: $-(+5) = 5$ (Quitar el paréntesis ignorando el signo exterior).
> - ✅ **Correcto**: $-(+5) = -5$ (Signos diferentes resultan en negativo).

> [!tip] 💡 Truco para recordarlo
> Para la interacción de signos, usa siempre esta regla:
> **"Signos iguales dan MÁS (+), signos diferentes dan MENOS (-)"**.

---

### Procedimiento Paso a Paso

Para resolver operaciones con signos de agrupación, sigue esta estructura extraída de los expertos:

```text
PASO 1 → Identificar y resolver la operación dentro del signo más interno (paréntesis).
PASO 2 → Asegurar que haya un solo número dentro del signo antes de eliminarlo.
PASO 3 → Multiplicar el número o signo exterior por el contenido interior (ley de signos).
PASO 4 → Repetir el proceso hacia afuera con corchetes y llaves siguiendo la jerarquía.
```

---

### Ejemplos Prácticos

> [!example] Ejemplo 1: Operación Básica (Niveles de agrupación)
> Resolver: $10 + \{ 5 - [ 4 + (7 - 5) ] \}$
> 1. Resolvemos el paréntesis: $(7 - 5) = 2$.
> 2. Eliminamos paréntesis: $+ (+2) = +2$. Queda: $10 + \{ 5 - [ 4 + 2 ] \}$.
> 3. Resolvemos corchete: $[ 4 + 2 ] = 6$.
> 4. Eliminamos corchete: $- (+6) = -6$. Queda: $10 + \{ 5 - 6 \}$.
> 5. Resolvemos llave: $\{ 5 - 6 \} = -1$.
> 6. Resultado final: $10 - 1$.
> $$ Resultado = 9 $$

> [!example] Ejemplo 2: Interacción de Signos Negativos (Precisión de Fuente)
> Resolver: $- 7 - \{ 3 + [ -9 - (5 - 2) ] + 3 \}$
> 1. Paréntesis: $(5 - 2) = 3$. Queda: $-(3)$.
> 2. Eliminamos paréntesis: El signo negativo exterior cambia el interior: $-3$.
> 3. Operación en corchete: $[-9 - 3 + 3] = -9$.
> 4. Eliminamos corchete: El signo $+$ exterior mantiene el signo interior: $+ (-9) = -9$.
> 5. Operación en llave: $\{ 3 - 9 \} = -6$.
> 6. Eliminación de llave: El signo $-$ exterior choca con el $-6$: $- (-6) = +6$.
> 7. Resultado: $-7 + 6$.
> $$ Resultado = -1 $$

> [!example] Ejemplo 3: Multiplicación por número externo
> Resolver: $5 + 3(4 - 1)$
> 1. Resolvemos el interior: $(4 - 1) = 3$.
> 2. **Pro-Tip**: Al no haber signo entre el 3 y el paréntesis, el número se **distribuye** multiplicando al contenido: $3 \times 3 = 9$.
> 3. Sumamos al valor inicial: $5 + 9$.
> $$ Resultado = 14 $$

> [!example] Ejemplo 4: Aplicación en dólares ($USD)
> Un comerciante tiene un presupuesto de $1000 USD y realiza una compra de 12 artículos de $49 USD cada uno.
> **Planteamiento**: $1000 - (12 \times 49)$
> 1. Resolvemos la multiplicación interna: $12 \times 49 = 588$.
> 2. Restamos del presupuesto inicial: $1000 - 588$.
> $$ Saldo = 412 USD $$

---

### Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Fácil: Eliminación simple
> 1. **Ejercicio 1**: $15 + (8 - 3) =$
> 2. **Ejercicio 2**: $20 - (10 + 5) =$
> 3. **Ejercicio 3**: $-( -7 + 4) + 2 =$
> 4. **Ejercicio 4**: $5 + [ 3 - (2 - 1) ] =$

> [!abstract] 🟡 Nivel Medio: Corchetes y multiplicaciones
> 1. **Ejercicio 1**: $2 \times (5 + 3) - 10 =$
> 2. **Ejercicio 2**: $-3 \times [ 4 - (6 - 2) ] =$
> 3. **Ejercicio 3**: $12 + 4 \times (10 - 8) =$
> 4. **Ejercicio 4**: $5 \times [ -2 + (3 \times 4) ] =$

> [!abstract] 🔴 Nivel Avanzado: Aplicación $USD (Anidada)
> 1. **Ejercicio 1**: Tienes $500 USD. Pagas 3 facturas de $45 USD y recibes $100 USD. Plantea: $\{ 500 - (3 \times 45) \} + 100 =$
> 2. **Ejercicio 2**: Una empresa paga 5 bonos de $120 USD, pero descuenta $20 de impuestos y $5 de seguro a cada uno: $5 \times [ 120 - (20 + 5) ] =$
> 3. **Ejercicio 3**: Saldo $1500 USD. Compras 2 equipos de $300 y pagas una deuda de $200: $\{ 1500 - [ (2 \times 300) + 200 ] \} =$
> 4. **Ejercicio 4**: Un fondo de $2000 USD se divide en 2 partes. A una parte se le restan $150 de gastos y $50 de comisión bancaria: $\{ (2000 / 2) - [ 150 + 50 ] \} =$

> [!success] ✅ Respuestas
> **Fácil**: 1) 20 | 2) 5 | 3) 5 | 4) 7
> **Medio**: 1) 6 | 2) 0 | 3) 20 | 4) 50
> **Avanzado**: 1) $465 USD | 2) $475 USD | 3) $700 USD | 4) $800 USD

---

### Autoevaluación

> [!question] Pregunta 1 (Conceptual)
> ¿Cuál es el orden jerárquico estándar para eliminar signos de agrupación cuando están anidados?
> *Respuesta: 1° Paréntesis `()`, 2° Corchetes `[]`, 3° Llaves `{}`.*

> [!question] Pregunta 2 (Procedimental)
> Resuelve mentalmente: $10 - (-5 + 2)$. ¿Cuál es el resultado correcto?
> a) 7
> b) 13
> c) 3
> *Respuesta correcta: **b) 13** (Porque $-5 + 2 = -3$, y $10 - (-3) = 10 + 3$).*

> [!question] Pregunta 3 (Aplicación $USD)
> Si debes $50 USD y te prestan otros $30 USD (ambos negativos para ti), pero recibes $100 USD de regalo, ¿cuál es tu saldo?
> *Planteamiento: $- (50 + 30) + 100$*
> *Respuesta: $20 USD.*

---

> [!tip] 💡 En la próxima clase
> Ahora que dominas los signos de agrupación en aritmética, estamos listos para entrar al lenguaje del álgebra puro: **Variables y Términos Semejantes**, donde los números se combinan con letras.

> [!info] 🧭 Navegación
> ◀ [[Clase 01]] | ▲ [[00 - Índice del curso|Índice]] | ▶ [[Clase 03]]