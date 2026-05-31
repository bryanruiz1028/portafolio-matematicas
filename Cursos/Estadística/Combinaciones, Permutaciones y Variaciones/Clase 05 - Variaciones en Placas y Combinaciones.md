# Clase 05 — Variaciones en Placas y Combinaciones

#algebra #variacionesplac

Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 5 de 6

> [!info] 🧭 Navegación
> Anterior: [[Clase 04 — Permutaciones]] | Índice: [[00 - Índice del curso]] | Siguiente: [[Clase 06 — Probabilidad Aplicada]]

> [!info] 🌍 Relevancia y aplicaciones
> El análisis combinatorio nos permite organizar sistemas de información y recursos de manera eficiente. Comprender la diferencia entre grupos y filas es la base de la seguridad informática, el diseño industrial y la gestión de inventarios.
> - **💵 Aplicación con $\$USD$:** El cálculo preciso de combinaciones ayuda a optimizar presupuestos al elegir agrupaciones de materiales o servicios de menor costo sin desperdiciar recursos en pruebas innecesarias.
> - **🏗️ Aplicación práctica:** Es esencial para diseñar sistemas de identidad únicos, como las matrículas de vehículos o códigos de barras, asegurando que siempre haya suficientes códigos disponibles para cada ciudadano.
> - **📊 Situación cotidiana:** La aplicamos al elegir el orden de las tareas del día o al seleccionar sabores de helado en una barquilla donde el orden de las bolas no cambia el sabor del postre.

---

> [!note] 📌 ¿Qué es Variaciones Placas de un automóvil?
> Imagina que una placa de auto es como el "DNI" o la huella digital de un vehículo. En el mundo de las matemáticas, llamamos **Variaciones** al proceso de contar cuántas placas distintas existen usando letras y números. Lo más importante aquí es la **identidad**: si cambias de lugar una sola letra (por ejemplo, de $AB$ a $BA$), la placa cambia de identidad por completo. ¡El orden es lo que define quién es quién!

> [!warning] ⚠️ Error común
> No confundas un **grupo** con una **identidad**. En una **Combinación** (como un grupo de amigos para almorzar), el orden no importa porque el grupo es el mismo. Pero en las **Variaciones** (como en las placas o códigos), el orden es fundamental: la placa $ABC-123$ es totalmente distinta a $CBA-123$. Si al cambiar el lugar algo cambia, no es combinación.

> [!tip] 💡 Truco para recordarlo
> Hazte siempre esta pregunta: *"Si cambio el orden de los elementos, ¿cambia el resultado final?"* 
> - **SÍ cambia:** Es una Variación (importa el orden).
> - **NO cambia:** Es una Combinación (es solo un grupo).
> **Regla de oro:** "Si al cambiar el lugar, cambia el resultado, el orden es lo esperado".

---

### Procedimiento Paso a Paso: El Método de las Cajitas

Para resolver cualquier problema de conteo, sigue estos $4$ pasos estructurados:

1.  **PASO 1: Determinar la naturaleza del problema.** ¿Es un grupo (Combinación) o es una fila/identidad (Variación)?
2.  **PASO 2: Identificar la repetición.** ¿Puedo usar el mismo elemento más de una vez? (Ejemplo: En una placa puedo usar la letra $A$ tres veces, pero en un equipo de fútbol no puedo usar al mismo jugador tres veces).
3.  **PASO 3: Definir las variables.**
    -   $n$: Total de elementos disponibles (Ej: $26$ letras o $10$ dígitos).
    -   $r$: Elementos que vamos a seleccionar.
4.  **PASO 4: Aplicar el cálculo.**
    -   **Para Variaciones (Orden importa):** Usamos el **Método de las Cajitas** (Multiplicación).
        `[ Opciones ] x [ Opciones ] x [ Opciones ]`
    -   **Para Combinaciones (Orden NO importa):** Usamos la fórmula $C(n,r) = \frac{n!}{r!(n-r)!}$ o $CR(n,r)$ si hay repetición.

---

### Bloque de Ejemplos Prácticos

**Ejemplo 1: Caso Básico (Combinación sin repetición)**
*Problema:* De $10$ estudiantes de un salón, se deben elegir $4$ para un almuerzo.
*Análisis:* ¿Importa el orden? No, porque todos van a hacer lo mismo (almorzar). Es un grupo.
*Cálculo ($10C4$):*
$$\frac{10!}{4! \times (10-4)!} = \frac{10 \times 9 \times 8 \times 7}{4 \times 3 \times 2 \times 1} = 210$$
*Resultado:* Existen $210$ formas diferentes de seleccionar el grupo.

**Ejemplo 2: Caso con Repetición (Helados)**
*Problema:* Una heladería ofrece $7$ sabores. ¿Cuántos helados de $3$ bolas se pueden armar si se pueden repetir sabores?
*Análisis:* ¿Importa el orden? No, el helado es el mismo sin importar qué bola se puso primero. Pero **sí** se permite repetir.
*Cálculo ($CR_{7,3}$):*
$$\frac{(7+3-1)!}{3! \times (7-1)!} = \frac{9!}{3! \times 6!} = \frac{9 \times 8 \times 7}{3 \times 2 \times 1} = 84$$
*Resultado:* Se pueden crear $84$ combinaciones de helado.
> [!observation]
> *Observación:* Nota que el número de helados es menor que si importara el orden, porque para la matemática, "Vainilla-Fresa" es lo mismo que "Fresa-Vainilla".

**Ejemplo 3: Caso Avanzado (Placas Estándar)**
*Problema:* Calcular el total de placas de $3$ letras y $3$ dígitos.
*Cálculo (Método de cajas):*
- Letras: `[ 26 ] x [ 26 ] x [ 26 ]` = $26^3 = 17,576$
- Dígitos: `[ 10 ] x [ 10 ] x [ 10 ]` = $10^3 = 1,000$
- Total: $17,576 \times 1,000 = 17,576,000$.
*Resultado:* Existen $17,576,000$ placas posibles.

**Ejemplo 4: Aplicación Real con $\$USD$**
*Problema:* Una empresa fabrica placas personalizadas. Cada diseño único tiene un costo de registro de $\$15$ USD. ¿Cuál es el costo total de registrar todos los diseños posibles para un modelo de $1$ letra y $2$ números?
*Cálculo:*
- Variaciones: `[ 26 ] x [ 10 ] x [ 10 ]` = $2,600$ diseños únicos.
- Costo: $2,600 \times \$15$ USD.
*Resultado:* El costo total de registro es de $\$39,000$ USD.

---

### Ejercicios para el Estudiante

> [!tip] 💡 Pro-Tip de Pedagogía
> Antes de calcular, dibuja tus "cajitas" o identifica si estás formando un "Grupo" (Combinación) o una "Identidad" (Variación).

> [!abstract] 🟢 Nivel Fácil
> 1. Tienes $5$ amigos y solo puedes invitar a $2$ al cine. ¿Cuántos grupos distintos puedes formar?
> 2. Una tienda tiene $8$ tipos de dulces. Debes elegir $3$ para un paquete. ¿Cuántas opciones tienes?
> 3. En un salón de $15$ personas, se eligen $2$ para limpieza. ¿De cuántas formas se puede hacer?
> 4. Tienes $4$ colores de pintura y quieres elegir $2$ para una mezcla. ¿Cuántas combinaciones hay?

> [!abstract] 🟡 Nivel Medio
> 1. ¿Cuántas placas de $2$ letras y $2$ números existen si la primera letra debe ser siempre la '$Z$'?
> 2. Calcula cuántas placas de $3$ letras existen si no se pueden usar números.
> 3. ¿Cuántas placas de $4$ dígitos existen si el primer dígito no puede ser $0$?
> 4. Si una placa debe empezar con las letras '$AB$' seguidas de $3$ números, ¿cuántas opciones hay?

> [!abstract] 🔴 Nivel Avanzado
> 1. Un coleccionista quiere todas las placas posibles de $1$ letra y $1$ número. Si cada placa cuesta $\$12.50$ USD, ¿cuánto dinero necesita?
> 2. Un sistema de códigos usa $2$ letras. Si reducir el sistema a solo $1$ letra ahorra $\$500$ USD en mantenimiento por cada combinación eliminada, ¿cuánto es el ahorro total?
> 3. Se ofrecen $6$ sabores de gaseosa. Debes elegir $3$. Compara el número de opciones si se permiten repeticiones frente a si los sabores deben ser diferentes.
> 4. Una placa tiene $2$ letras y $2$ números. Si fabricar cada letra de la placa cuesta $\$2$ USD y cada número $\$1$ USD, ¿cuál es el costo total de producir una unidad de cada placa posible? (Calcula el costo por placa y multiplícalo por el total de variaciones).

> [!success] ✅ Respuestas para el Docente (Uso exclusivo)
> **Nivel Fácil:** 
> 1) $10$ | 2) $56$ | 3) $105$ | 4) $6$
> 
> **Nivel Medio:** 
> 1) $2,600$ (Cajas: `[1]x[26]x[10]x[10]`) | 2) $17,576$ ($26^3$) | 3) $9,000$ (`[9]x[10]x[10]x[10]`) | 4) $1,000$ ($10^3$)
> 
> **Nivel Avanzado:** 
> 1) $\$3,250$ USD ($26 \times 10 = 260$ placas $\times \$12.50$).
> 2) $\$325,000$ USD ($26^2 = 676$; $676 - 26 = 650$ eliminadas $\times \$500$).
> 3) Con repetición: $56$ ($CR_{6,3}$); Sin repetición: $20$ ($C_{6,3}$).
> 4) **$\$405,600$ USD**. (Costo por placa: $(\$2 \times 2) + (\$1 \times 2) = \$6$. Variaciones totales: $26 \times 26 \times 10 \times 10 = 67,600$. Costo final: $67,600 \times \$6$).

---

### Mini-Prueba de Autoevaluación

> [!question] 🧪 Pregunta 1
> Si diseño una placa de auto y decido cambiar el orden de las letras de "$XY-12$" a "$YX-12$", ¿estoy creando una placa nueva o es la misma? ¿Por qué?

> [!question] 🧪 Pregunta 2
> Una máquina de gaseosas tiene $6$ sabores. Si un cliente quiere llenar un vaso con $3$ porciones y se permite repetir sabores (no importa el orden), ¿cuántas opciones tiene?

> [!question] 🧪 Pregunta 3
> Si cada combinación única de un menú cuesta $\$5.50$ USD y existen exactamente $20$ combinaciones posibles, ¿cuánto dinero se recaudaría si se vende exactamente una de cada una?

---

> [!tip] 💡 En la próxima clase
> Ahora que dominas cómo contar grupos (combinaciones) y secuencias (variaciones), en la **Clase 06** utilizaremos estos totales para calcular la **Probabilidad**, es decir, qué tan posible es que una de estas opciones ocurra al azar.

> [!info] 🧭 Navegación
> Anterior: [[Clase 04 — Permutaciones]] | Índice: [[00 - Índice del curso]] | Siguiente: [[Clase 06 — Probabilidad Aplicada]]