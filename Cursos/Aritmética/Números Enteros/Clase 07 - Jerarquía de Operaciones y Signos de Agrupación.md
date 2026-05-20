# Clase 07 — Jerarquía de Operaciones y Signos de Agrupación

**tags:** #algebra #hierarchyofoper
**Curso:** [[00 - Índice del curso]] | Bloque 2 | Lección 7 de 8

> [!info] 🧭 Navegación
> [[Clase 06|⬅ Clase 06]] | [[00 - Índice del curso|Índice]] | **Clase 07** | [[Clase 08|Clase 08 ➡]]

## 1. ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> La jerarquía de operaciones es el "semáforo" de las matemáticas. Sin reglas claras sobre qué operación va primero, cada persona obtendría un resultado distinto. Este orden garantiza precisión y uniformidad en todo el mundo.
> 
> - 💵 **Finanzas:** Imagina que tienes $100 USD y compras 3 artículos de $12 USD, pero el cajero te aplica un descuento de $5 USD al final. La jerarquía permite calcular tu saldo real: $100 - (3 \times 12 - 5) = 69$.
> - 🏗️ **Construcción:** Para calcular el material de una pared con una ventana, necesitas restar el área de la ventana antes de multiplicar por el costo del cemento.
> - 📊 **Situación cotidiana:** Organizar tu presupuesto diario requiere sumar tus gastos en grupos y luego restarlos de tus ingresos; si te saltas el orden, podrías pensar que tienes más dinero del que realmente queda.

## 2. Concepto clave

> [!note] 📌 ¿Qué es la Jerarquía de Operaciones?
> Es el orden obligatorio en el que se deben resolver las operaciones en un ejercicio combinado. Para no fallar, sigue siempre esta prioridad:
> 1. **Signos de agrupación:** Primero lo que está dentro de `()`, `[]` y `{}`.
> 2. **Potencias y raíces:** $(\dots)^n$ y $\sqrt{\dots}$.
> 3. **Multiplicación y división:** De izquierda a derecha.
> 4. **Sumas y restas:** Siempre al final.

> [!warning] ⚠️ Error común
> Muchos estudiantes resuelven de izquierda a derecha sin pensar. 
> En el caso: **3 + 5 * 2**
> - ❌ **Error:** Sumar 3 + 5 y luego multiplicar por 2 ($8 \times 2 = 16$).
> - ✅ **Correcto:** Primero multiplicar 5 * 2 y luego sumar el 3 ($3 + 10 = 13$).

> [!tip] 💡 La clave: Separar en términos
> Antes de empezar, divide el ejercicio usando los signos **más (+)** y **menos (-)** que estén **fuera** de los paréntesis. Esto crea "bloques" independientes que puedes resolver por separado antes de realizar la suma o resta final.

## 3. Procedimiento paso a paso

Para eliminar signos de agrupación y resolver operaciones combinadas, sigue este método estructurado:

```text
PASO 1 → Identificar lo que está "más adentro" (generalmente paréntesis).
PASO 2 → Resolver potencias y raíces dentro de ese nivel.
PASO 3 → Realizar multiplicaciones y divisiones.
PASO 4 → Resolver sumas y restas para dejar UN SOLO NÚMERO dentro del signo.
PASO 5 → ELIMINAR EL SIGNO (Regla de Oro):
         - Si hay un NÚMERO a la izquierda (pegado): Multiplica el número de afuera por el de adentro.
         - Si hay un SIGNO a la izquierda: Multiplica el signo de afuera por el de adentro (Ley de Signos).
```

## 4. Ejemplos Desarrollados

```ad-example
title: Ejemplo 1 — Jerarquía Básica con Potencias
**Ejercicio:** $3^2 - 2 \times 3$

1. **Separar en términos:** Los bloques son **[ $3^2$ ]** y **[ $2 \times 3$ ]**.
2. **Resolver Bloque 1:** $3^2 = 9$.
3. **Resolver Bloque 2:** $2 \times 3 = 6$.
4. **Finalizar:** $9 - 6 = 3$.
✅ Resultado: 3
```

```ad-example
title: Ejemplo 2 — Caso con Corchetes y Paréntesis
**Ejercicio:** $[ (18-16) \div 2 + 36 \div (12-6) + 6 ]^2$

1. **Resolver paréntesis internos:** $(18-16) = 2$ y $(12-6) = 6$.
2. **Separar en términos dentro del corchete:** 
   $[ \mathbf{(2 \div 2)} + \mathbf{(36 \div 6)} + \mathbf{6} ]^2$
3. **Resolver divisiones:** $[ 1 + 6 + 6 ]^2$.
4. **Simplificar corchete:** $[ 13 ]^2$.
5. **Potencia final:** $13 \times 13 = 169$.
✅ Resultado: 169
```

```ad-example
title: Ejemplo 3 — Eliminación de Llaves y Multiplicación Compleja
**Ejercicio:** $-12 \{ -7 + [ -4(-2 \cdot 3) + 5 - (-10 - 2) ] + 15 \}$

1. **Operaciones más internas:** 
   - $(-2 \cdot 3) = -6$ 
   - $(-10 - 2) = -12$
2. **Eliminar paréntesis dentro del corchete (Regla de Oro):**
   - El -4 multiplica al -6: **+24** (número por número).
   - El signo menos multiplica al -12: **+12** (signo por signo).
   - Resultado parcial: $[ 24 + 5 + 12 ]$.
3. **Simplificar corchete:** $24 + 5 + 12 = \mathbf{41}$.
4. **Simplificar llaves (Separar en términos):**
   - Llave = $\{ \mathbf{-7} + \mathbf{41} + \mathbf{15} \}$.
   - Sumando positivos: $41 + 15 = 56$. Restando el negativo: $56 - 7 = \mathbf{49}$.
5. **Multiplicación final:** El -12 está pegado a la llave, así que multiplicamos:
   $-12 \times 49 = -588$.
✅ Resultado: -588
```

```ad-example
title: Ejemplo 4 — Aplicación real con $USD
**Problema:** Tienes $100 USD. Compras 3 libros de $12 USD cada uno y recibes un descuento de $5 USD en el total de esa compra.

1. **Lógica pedagógica:** Primero calculamos el "ticket" o cuenta total de la librería dentro de un paréntesis y luego lo restamos de nuestro dinero inicial.
2. **Planteamiento:** $100 - (3 \times 12 - 5)$.
3. **Operación interna:** $100 - (36 - 5)$.
4. **Cuenta total:** $100 - 31$.
✅ Resultado: $69 USD
```

## 5. Ejercicios para el estudiante

```ad-abstract
title: 🟢 Fácil — Operaciones Combinadas Simples
1. $5 + 2 \times 3^2$
2. $10 - (2 + 3) \times 2$
3. $\sqrt{49} + 5 \times 2$
4. $15 \div 3 + 4$
```

```ad-abstract
title: 🟡 Medio — Signos de Agrupación Múltiples
1. $2 \times [5 + (8 - 3)]$
2. $-3 \times [4^2 - (10 \div 2)]$
3. $25 - 8^2 + 8(19 - 12)$
4. $5(2^3 - 4) + \sqrt{36}$
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con Dinero
1. Un comerciante compra 12 artículos a $15 USD cada uno y paga $20 USD adicionales de envío. Escribe la operación y resuelve.
2. Tienes $200 USD, gastas $(3 \times 40)$ en ropa y $(2 \times 15)$ en comida. ¿Cuánto queda?
3. Un ahorro de $500 USD se divide en 2 partes iguales. A una de esas partes le restas un gasto de $45 USD. ¿Cuánto queda en esa parte?
4. Calcula el costo total de 4 cajas de herramientas que cuestan $80 USD cada una, si se aplica un descuento de $15 USD **a cada caja**.
```

```ad-success
title: ✅ Respuestas (para el docente)
| Nivel | 1 | 2 | 3 | 4 |
| :--- | :--- | :--- | :--- | :--- |
| **🟢 Fácil** | 23 | 0 | 17 | 9 |
| **🟡 Medio** | 20 | -33 | 17 | 26 |
| **🔴 Avanzado** | $200 | $50 | $205 | $260 |
```

## 6. Autoevaluación y Cierre

```ad-question
title: 🧪 Pregunta 1
¿Qué se resuelve primero en una operación que no tiene signos de agrupación?
a) Sumas b) Multiplicaciones c) Potencias d) Restas
**Respuesta:** c) — Según la jerarquía, las potencias y raíces van antes que multiplicaciones y sumas.
```

```ad-question
title: 🧪 Pregunta 2
Si hay un signo menos (-) justo antes de un paréntesis como $-( -5 )$, el resultado es:
a) -5 b) 0 c) 5 d) -1
**Respuesta:** c) — Al multiplicar signos iguales (negativo por negativo), el resultado es positivo.
```

```ad-question
title: 🧪 Pregunta 3
Si compras 5 productos de $10 USD y pagas con $100 USD, ¿cuál es la expresión correcta?
a) $100 - 5 + 10$ b) $(100 - 5) \times 10$ c) $100 - (5 \times 10)$ d) $5 \times 10 - 100$
**Respuesta:** c) — Primero calculas el total del gasto (multiplicación) y luego lo restas del dinero disponible.
```

## 7. Notas para el próximo tema

> [!tip] 💡 En la próxima clase
> En la **Clase 08**, llevaremos estas reglas al siguiente nivel. Usaremos la jerarquía de operaciones pero aplicada a **fracciones y números decimales**. ¡Repasa bien la ley de signos antes de la próxima sesión!

> [!info] 🧭 Navegación
> [[Clase 06|⬅ Clase 06]] | [[00 - Índice del curso|Índice]] | **Clase 07** | [[Clase 08|Clase 08 ➡]]