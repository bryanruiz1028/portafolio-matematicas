# Clase 02 — Operaciones Avanzadas con Números Binarios: Resta, Multiplicación y División

#algebra #subtractingbina

🧭 **Navegación**
> [!multi-column]
> > [⬅️ Clase Anterior](Clase01)
>
> > [🏠 Índice del Curso](Indice)

---

### 2. Relevancia y Aplicaciones

> [!info] 🌍 Relevancia y aplicaciones
> Las operaciones binarias avanzadas son el motor del procesamiento de datos moderno, permitiendo que los circuitos lógicos ejecuten tareas complejas con solo dos estados.
> - 💵 **Aplicación USD:** Los cajeros automáticos procesan restas binarias para deducir retiros en dólares de tu saldo bancario y calcular el cambio exacto.
> - 🏗️ **Aplicación práctica:** La multiplicación binaria es vital en el escalado de imágenes; al redimensionar una foto, el procesador multiplica valores de píxeles mediante "desplazamientos" de bits.
> - 📊 **Situación cotidiana:** La gestión de permisos de archivos en Linux o Windows se basa en divisiones y restos binarios para determinar quién puede leer o escribir un documento.

---

### 3. Conceptos Clave y Definiciones

> [!note] 📌 ¿Qué es la Resta, Multiplicación y División Binaria?
> Estas operaciones son un "juego de ceros y unos" con reglas similares al sistema decimal, pero mucho más simplificadas. De hecho, como dice el Profe Alex, ¡la división binaria es **10,000 veces más fácil** que la decimal! Esto se debe a que en el cociente solo puedes poner $0$ (no cabe) o $1$ (sí cabe).

> [!warning] ⚠️ Error común
> En la resta, cuando te encuentras con $0 - 1$, no puedes operar directamente. Debes "pedir prestado" (borrow) a la columna de la izquierda. El error es pensar que el préstamo vale diez; en realidad, el $1$ que pides prestado convierte al $0$ en un **2 decimal**, que en binario se escribe como **$10_2$**. ¡No lo confundas con el número diez!

> [!tip] 💡 Truco para recordarlo
> Regla mnemotécnica: "En binario, prestar un 1 te da un 2".

---

### 4. Procedimientos Paso a Paso

```text
PASOS PARA OPERACIONES BINARIAS

Paso 1: Alineación
Alinear las cifras hacia la derecha en columnas (minuendo/sustraendo o factores).

Paso 2: Reglas Básicas
- Resta: 1-0=1, 1-1=0, 0-0=0.
- Multiplicación: 1x1=1, 1x0=0, 0x1=0, 0x0=0.
- División: Decidir si el divisor "cabe" (1) o "no cabe" (0).

Paso 3: Gestión de Acarreos y Préstamos
- Multiplicación: Al sumar resultados parciales, si da 2 pones 0 y llevas 1. 
  *Truco: Multiplicar por 10 es solo agregar un 0 al final (desplazamiento a la izquierda).*
- Resta: Si es 0-1, pides prestado y el 0 se convierte en un 2 decimal (10 en binario).

Paso 4: Casita de División
Nota: La posición del divisor (la "casita") puede variar según tu país (estilo Colombia vs México), 
pero la lógica de comparar si el divisor cabe en el dividendo parcial es universal.
```

---

### 5. Ejemplos Prácticos Detallados

> [!example] Ejemplo 1: Resta Básica ($10 - 5$ en decimal)
> **Operación:** $1010_2 - 101_2$
> 1. Alineamos: $1010$ sobre $0101$.
> 2. Columna derecha ($0 - 1$): Pedimos prestado. El $0$ se convierte en **$10_2$** (que es 2).
> 3. Operamos: $2 - 1 = 1$.
> 4. La columna de la izquierda, que era $1$, prestó y quedó en $0$. Entonces: $0 - 0 = 0$.
> 5. Siguiente columna ($0 - 1$): Pedimos prestado al último $1$. El $0$ se vuelve $2$: $2 - 1 = 1$.
> **Resultado:** $101_2$ (que equivale a $5$ en decimal).

> [!example] Ejemplo 2: Multiplicación con Desplazamiento ($22 \times 2$ en decimal)
> **Operación:** $10110_2 \times 10_2$
> 1. Como multiplicamos por $10_2$, aplicamos la lógica de "shift": desplazamos el número original una posición a la izquierda y agregamos un cero.
> 2. Proceso manual: Multiplicar por $0$ da $00000$. Multiplicar por $1$ da $10110$ (desplazado).
> 3. Al sumar los niveles, simplemente añadimos el cero del primer paso.
> **Resultado:** $101100_2$ (que equivale a $44$ en decimal).

> [!example] Ejemplo 3: División — ¿Cabe o no cabe? ($15 \div 3$ en decimal)
> **Operación:** $1111_2 \div 11_2$
> 1. Tomamos las primeras dos cifras del dividendo: $11$. ¿Cabe el divisor $11$? **Sí (1)**.
> 2. Restamos: $11 - 11 = 00$.
> 3. Bajamos la siguiente cifra: $1$. ¿Cabe el $11$ en el $01$? **No (0)**. Ponemos $0$ en el cociente.
> 4. Bajamos la última cifra: $1$. Ahora tenemos $11$. ¿Cabe el $11$? **Sí (1)**.
> 5. Restamos: $11 - 11 = 0$.
> **Resultado:** $101_2$ (que equivale a $5$ en decimal).

> [!example] Ejemplo 4: Aplicación Real Bancaria (USD)
> **Problema:** Restar un cargo de $\$13$ ($1101_2$) a un saldo de $\$25$ ($11001_2$).
> 1. Columna 1: $1 - 1 = 0$.
> 2. Columna 2: $0 - 0 = 0$.
> 3. Columna 3 ($0 - 1$): Pide prestado. Se vuelve $2$. $2 - 1 = 1$.
> 4. Columna 4 ($0 - 1$): El $1$ de la izquierda prestó y quedó en $0$. Pide prestado al final. Se vuelve $2$. $2 - 1 = 1$.
> **Resultado:** $1100_2$ (que equivale a $\$12$ en decimal).

---

### 6. Ejercicios de Práctica

> [!abstract] 🟢 Nivel Fácil
> 1. $111_2 - 101_2$
> 2. $101_2 - 10_2$
> 3. $11_2 \times 10_2$
> 4. $110_2 \times 1_2$

> [!abstract] 🟡 Nivel Medio
> 1. $1000_2 - 1_2$ (Préstamos sucesivos)
> 2. $1111_2 - 1001_2$
> 3. $110_2 \div 11_2$
> 4. $1010_2 \div 10_2$

> [!abstract] 🔴 Nivel Avanzado
> 1. Multiplica un precio de $\$6$ ($110_2$) por 3 unidades ($11_2$) y resta un descuento de $\$2$ ($10_2$).
> 2. $11011_2 \div 11_2$
> 3. $101010_2 \div 110_2$ (Referencia del video: $42 \div 6$).
> 4. Realiza el cálculo: $(111_2 \times 11_2) - 1010_2$.

> [!success] Soluciones para el Docente
> - **Fácil:** 1) $10$, 2) $11$, 3) $110$, 4) $110$.
> - **Medio:** 1) $111$ ($8-1=7$), 2) $110$, 3) $10$, 4) $101$.
> - **Avanzado:** 
>    1) $10000_2$ ($18-2 = 16_{10}$).
>    2) $1001$.
>    3) $111$ ($7_{10}$).
>    4) $1011$. *Comprobación: $(7 \times 3) - 10 = 21 - 10 = 11_{10}$*.

---

### 7. Autoevaluación

> [!question] Pregunta 1
> ¿Qué valor decimal representa el "préstamo" que una columna le da a un cero en la resta binaria?
> **Respuesta:** Representa un **2 decimal**. Se escribe como $10$ en binario, permitiendo que la operación sea $2 - 1 = 1$.

> [!question] Pregunta 2
> En el video del Profe Alex, ¿cuál es el resultado de la división $101010_2 \div 110_2$?
> **Respuesta:** El resultado es $111_2$. En decimal, esto equivale a $42 \div 6 = 7$.

> [!question] Pregunta 3
> Si ejecutas una multiplicación de un número binario por $10_2$ y luego le restas el mismo número original, ¿qué obtienes?
> **Respuesta:** Obtienes el mismo número original. Multiplicar por $10_2$ es duplicar el valor ($x \times 2$), y al restar el original ($2x - x$), queda $x$.

---

### 8. Cierre y Transición

> [!tip] 💡 En la próxima clase
> Has dominado las operaciones de la "calculadora humana" binaria. En la próxima sesión, cerraremos este bloque aprendiendo cómo convertir estos resultados a otros sistemas como el Octal y el Hexadecimal.

🧭 **Navegación**
> [!multi-column]
> > [⬅️ Clase Anterior](Clase01)
>
> > [🏠 Índice del Curso](Indice)