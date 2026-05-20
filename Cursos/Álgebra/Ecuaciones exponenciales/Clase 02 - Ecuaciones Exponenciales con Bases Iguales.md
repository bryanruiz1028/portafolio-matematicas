# Clase 02 — Ecuaciones Exponenciales con Bases Iguales

tags: #algebra #exponentialequa
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 8

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | | [[Clase 03|Clase 03 ➡]]

---

## 1. Importancia y Aplicaciones Reales

> [!info] 🌍 Relevancia y aplicaciones
> Entender cómo igualar bases es como encontrar una llave maestra: una vez que los "números de abajo" son idénticos, el misterio del exponente se resuelve solo. Esto es fundamental para entender procesos que se disparan rápidamente.
>
> - 💵 **Aplicación con $USD:** Calcular cuántos meses deben pasar para que tus ahorros se dupliquen con un interés compuesto.
> - 🏗️ **Aplicación práctica:** Predecir el crecimiento de una población de bacterias o el aumento de habitantes en una ciudad.
> - 📊 **Situación cotidiana:** Analizar la velocidad con la que un meme se vuelve viral cuando cada persona lo comparte con un número constante de amigos.

---

## 2. Concepto Clave y Reglas de Oro

> [!note] 📌 ¿Qué es una Ecuación Exponencial con Bases Iguales?
> Imagina una balanza perfecta. Si en ambos lados tienes la misma base (el número grande de abajo), para que la igualdad sea cierta, los exponentes (los números pequeños de arriba) **tienen que ser iguales**.
>
> **Propiedad fundamental:** Si $a^x = a^y$, entonces $x = y$.

> [!warning] ⚠️ Error común
> No puedes igualar exponentes si hay números "estorbando" fuera de la base.
> - **Ejemplo:** En $2 \cdot 3^x = 9$, no puedes decir que la base es 6. ¡Error! Primero debes pasar el 2 dividiendo al otro lado ($3^x = 4.5$).
> - Tampoco funciona si hay sumas o restas separando términos sin antes factorizar.

> [!tip] 💡 Truco para recordarlo
> Usa la regla: **"Bases iguales, exponentes gemelos"**. Si logras que los de abajo sean espejos, los de arriba deben ser idénticos.

---

## 3. Procedimiento General (Algoritmo de Resolución)

```text
PASO 1: Asegurar que haya un solo término a cada lado de la igualdad. 
       (Nota: Si hay sumas o restas de potencias, debemos usar factorización 
       antes de poder igualar).
PASO 2: Convertir las bases para que sean idénticas (expresarlas como potencias 
       de un mismo número primo, como 2, 3 o 5).
PASO 3: Igualar los exponentes (eliminar las bases).
PASO 4: Resolver la ecuación resultante y VERIFICAR siempre el resultado.
```

---

## 4. Ejemplos Prácticos Detallados

> [!example] Ejemplo 1: Caso Básico
> **Resolver:** $5^{x+2} = 5^7$
> 1. Las bases ya son iguales (base 5).
> 2. Igualamos exponentes: $x + 2 = 7$.
> 3. Despejamos: $x = 7 - 2 \implies \mathbf{x = 5}$.

> [!example] Ejemplo 2: Bases por Convertir
> **Resolver:** $2^x = 64$
> 1. Buscamos el 64 en las potencias de 2: $2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 = 64$, es decir, $2^6$.
> 2. Reescribimos: $2^x = 2^6$.
> 3. Igualamos: $\mathbf{x = 6}$. ¡No olvides verificar que la base sea la misma!

> [!example] Ejemplo 3: Caso Cuadrático y Verificación Crucial
> **Resolver:** $4^{x^2 - 3x - 16} = 16$
> 1. Convertimos el 16: $16 = 4^2$.
> 2. Igualamos exponentes: $x^2 - 3x - 16 = 2$.
> 3. Llevamos a cero: $x^2 - 3x - 18 = 0$.
> 4. Factorizamos: $(x - 6)(x + 3) = 0$. Obtenemos $x_1 = 6$ y $x_2 = -3$.
> 5. **Verificación del valor negativo ($x = -3$):**
>    Sustituimos en el exponente original: $(-3)^2 - 3(-3) - 16 = 9 + 9 - 16 = 2$.
>    Nos queda $4^2 = 16$. ¡Correcto! El resultado negativo es totalmente válido.

> [!example] Ejemplo 4: Aplicación $USD
> **Problema:** Una inversión de $1 USD se duplica cada año ($2^x$). ¿Cuándo llegará a $32 USD?
> 1. Ecuación: $2^x = 32$.
> 2. Convertimos: $2^x = 2^5$.
> 3. Resultado: **5 años**.

---

## 5. Práctica Dirigida para el Estudiante

> [!abstract] 🟢 Nivel Fácil (Directas)
> 1. $3^{x-1} = 3^5$
> 2. $2^{x+4} = 2^{10}$
> 3. $7^{2x} = 7^8$
> 4. $5^{x+2} = 5^{2x-1}$

> [!abstract] 🟡 Nivel Medio (Conversión y Despeje)
> 1. $9^x = 27$ *(Pista: usa base 3)*
> 2. $2^x - 5 = 59$ *(Pista: pasa el 5 sumando primero)*
> 3. $4^{x+1} = 64$
> 4. $25^x = 125$ *(Pista: usa base 5)*

> [!abstract] 🔴 Nivel Avanzado (Factorización y Aplicaciones)
> 1. $2^{x+1} + 2^{x+2} = 48$ *(Pista: Separa como $2 \cdot 2^x + 4 \cdot 2^x = 48$)*
> 2. $5^x + 5^{x+1} = 150$ *(Pista: Míralo como $1 \cdot 5^x + 5 \cdot 5^x = 150$)*
> 3. $2^{x^2-6x+12} = 16$ *(Resuelve la cuadrática igualando a base 2)*
> 4. **Problema $USD:** Si un artículo cuesta **$100 USD** y su valor se triplica cada década ($3^x$), ¿cuántas décadas deben pasar para que el artículo valga **$2,700 USD**? *(Ecuación: $100 \cdot 3^x = 2700$)*

---

## 6. Solucionario para el Docente

> [!success] Respuestas Confirmadas
> **Fácil:** 1) $x=6$ | 2) $x=6$ | 3) $x=4$ | 4) $x=3$
> **Medio:** 1) $x=1.5$ | 2) $x=6$ | 3) $x=2$ | 4) $x=1.5$
> **Avanzado:** 1) $x=3$ | 2) $x=2$ | 3) $x_1=2, x_2=4$ | 4) $x=3$ décadas.
>
> **¡Recuerda verificar siempre!** — Como dice el Profe Álex, la verificación te da la seguridad de que tu proceso fue perfecto.

---

## 7. Autoevaluación Rápida

> [!question] Pregunta 1
> ¿Qué condición debe cumplirse para poder igualar directamente los exponentes de dos potencias?
> *Respuesta: Que ambas potencias tengan la misma base y estén solas a cada lado del igual.*

> [!question] Pregunta 2
> ¿Cuál es la forma correcta de expresar 27 para resolver $3^x = 27$?
> a) $9 \cdot 3$
> b) $27^1$
> c) $3^3$
> *Respuesta: c) $3^3$.*

> [!question] Pregunta 3 (Reto $USD)
> Una criptomoneda duplica su valor cada mes ($2^x$). Si hoy vale **$1 USD**, ¿en cuántos meses valdrá **$128 USD**?
> a) 6 meses
> b) 7 meses
> c) 8 meses
> *Respuesta: b) 7 meses ($2^7 = 128$).*

---

## 8. Cierre y Conexión

> [!tip] 💡 En la próxima clase
> ¿Qué sucede si las bases son rebeldes y no se pueden igualar (como $2^x = 7$)? En la **Clase 03** descubriremos el poder de los logaritmos y el cambio de variable para dominar cualquier ecuación.

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | | [[Clase 03|Clase 03 ➡]]