# Clase 07 — Solución de problemas con Sistemas de Ecuaciones Lineales 2x2
tags: #algebra #solucindeproble
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 7 de 8

> [!info] 🧭 Navegación
> **Anterior:** [[Clase 06 — Métodos de resolución]]
> **Índice:** [[00 - Índice del curso]]

---

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> El álgebra es el "puente" que nos permite transformar situaciones de la vida real en modelos matemáticos. Esta clase te enseñará a traducir el lenguaje cotidiano a sistemas de ecuaciones para resolver misterios que la lógica simple no siempre alcanza a descifrar.

* 💵 **Aplicación con $USD:** Dominar estas ecuaciones permite calcular perímetros exactos para presupuestos de materiales, como determinar el costo total de cercar un terreno sin desperdiciar dinero.
* 🏗️ **Aplicación práctica:** Es esencial en la ingeniería y arquitectura básica para diseñar estructuras como rectángulos de soporte o cerchas en triángulos isósceles.
* 📊 **Situación cotidiana:** Se utiliza para descifrar propiedades numéricas en sistemas de contabilidad o para crear algoritmos basados en el valor posicional de las cifras.

---

## Concepto clave

> [!note]
> Resolver problemas con sistemas 2x2 es el arte de encontrar dos valores desconocidos (incógnitas) que deben cumplir dos condiciones obligatorias al mismo tiempo. Piensa en el Álgebra como una **red de seguridad sistemática**: cuando un problema es demasiado complejo para resolverlo "al ojo" o por tanteo, las ecuaciones te darán la respuesta exacta siempre.

> [!warning] ⚠️ Error común
> Al usar el método de reducción, el error más grave es **no multiplicar toda la ecuación**. Si multiplicas las variables para cancelarlas, pero olvidas multiplicar el término independiente (el número después del signo igual), el sistema perderá su equilibrio y el resultado será incorrecto.

> [!tip] 💡 Truco para recordarlo
> ¡Dale identidad a tus variables! En lugar de usar siempre $x$ y $y$, utiliza la técnica de **"Letras con nombre"**. Si el problema habla de largo y ancho, usa $L$ y $A$. Si habla de decenas y unidades, usa $d$ y $u$. Esto te ayudará a no perder el hilo y a redactar tu respuesta final sin confusiones.

---

## Procedimiento Paso a Paso

Sigamos esta **hoja de ruta** pedagógica para dominar cualquier sistema planteado en un enunciado:

1. **PASO 1 → Asignar letras representativas:** Define claramente qué significa cada letra (ej. $i = \text{lados iguales}$).
2. **PASO 2 → Traducir al lenguaje algebraico:** Escribe las dos ecuaciones basándote en las condiciones del texto (ej. fórmulas de perímetro).
3. **PASO 3 → Resolver el sistema:** Aplica un método de resolución. Se sugiere el de **Reducción/Eliminación**, ya que en problemas geométricos las variables suelen estar alineadas y listas para cancelarse rápidamente.
4. **PASO 4 → Verificar y redactar:** Comprueba que los resultados funcionen en el problema original y escribe la respuesta incluyendo las unidades ($cm$, $metros$, $USD$).

---

## Ejemplos Desarrollados

> [!example] Ejemplo 1: El Rectángulo (Caso Geométrico)
> **Problema:** El perímetro de un rectángulo mide 38 cm. Si se duplica el largo y se aumenta el ancho en 6 cm, el perímetro sube a 74 cm. ¿Cuáles son las medidas?
> 
> **Planteamiento:**
> 1. $2L + 2A = 38$ (Suma de los cuatro lados originales).
> 2. $2(2L) + 2(A + 6) = 74 \rightarrow 4L + 2A + 12 = 74$ (Perímetro modificado).
> 
> **Resolución:** Al simplificar y restar las ecuaciones, obtenemos:
> * **Largo (L):** $12 \text{ cm}$
> * **Ancho (A):** $7 \text{ cm}$

> [!example] Ejemplo 2: Triángulo Isósceles
> **Problema:** Un triángulo isósceles tiene un perímetro de 21 cm. Si se triplican sus lados iguales y se duplica el lado desigual, el perímetro sube a 58 cm.
> 
> **Planteamiento:**
> 1. $2i + d = 21$ (Dos lados iguales y uno desigual).
> 2. $3(2i) + 2d = 58 \rightarrow 6i + 2d = 58$.
> 
> **Resultado:** Usando reducción, encontramos que los lados iguales (**i**) miden $8 \text{ cm}$ y el lado desigual (**d**) mide $5 \text{ cm}$.

> [!example] Ejemplo 3: El Número Misterioso (Valor Posicional)
> **Problema:** Un número de dos cifras tiene unidades que son el doble de las decenas. Si se invierten las cifras, el nuevo número excede en 27 al original.
> 
> **Lógica clave:** En nuestro sistema decimal, la posición importa. El número se representa como $(10d + u)$, porque las decenas valen 10 veces su cifra.
> 1. $u = 2d$
> 2. $(10u + d) = (10d + u) + 27$
> 
> **Resultado:** $d = 3$ y $u = 6$. El número es **36**.

> [!example] Ejemplo 4: Aplicación Real con Presupuesto ($USD)
> **Problema:** Se requiere cercar un terreno donde la base mide 13 cm más que la altura y el perímetro es de 142 cm. El costo es de $1 USD por cada cm de cerca.
> 
> **Planteamiento:**
> 1. $B = A + 13$
> 2. $2B + 2A = 142$
> 
> **Cálculo de Costo:**
> * Resolvemos: $B = 42 \text{ cm}$, $A = 29 \text{ cm}$.
> * Perímetro total = $142 \text{ cm}$.
> * Costo total = $142 \text{ cm} \times 1 \text{ USD/cm} = \mathbf{142 \text{ USD}}$.

---

## Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Verde (Fácil)
> 1. Halla las dimensiones de un rectángulo de perímetro $20 \text{ cm}$ si el largo es el doble que el ancho.
> 2. Un rectángulo tiene un perímetro de $38 \text{ cm}$ y la suma de un largo y un ancho es $19 \text{ cm}$. Calcula sus lados sabiendo que el largo es $5 \text{ cm}$ mayor que el ancho.
> 3. Encuentra la base y altura de un rectángulo cuyo perímetro es $30 \text{ cm}$ y su base mide $5 \text{ cm}$ más que su altura.
> 4. Si el perímetro de un cuadrado es $40 \text{ cm}$, plantea el sistema para encontrar sus lados (considerando $L_1 = L_2$).

> [!abstract] 🟡 Nivel Amarillo (Medio)
> 1. En un triángulo isósceles de perímetro $21 \text{ cm}$, los lados iguales miden $3 \text{ cm}$ más que el desigual. Halla los lados.
> 2. Un triángulo isósceles tiene perímetro $36 \text{ cm}$. Si el lado desigual es la mitad de uno de los iguales, ¿cuánto miden?
> 3. Halla los lados de un triángulo isósceles si al duplicar el desigual el perímetro es $26 \text{ cm}$ y el original era $21 \text{ cm}$.
> 4. El perímetro de un triángulo isósceles es $25 \text{ cm}$. Si el lado desigual aumenta $5 \text{ cm}$, el triángulo se vuelve equilátero. Halla las medidas originales.

> [!abstract] 🔴 Nivel Rojo (Avanzado)
> 1. Un número de dos cifras suma 9. Si se invierten, el número aumenta en 9. Halla el número.
> 2. Las unidades de un número son el triple de las decenas. Si se invierten, el número aumenta en 54. Halla el número.
> 3. La suma de las cifras de un número es 13. Si se resta 45 al número, las cifras se invierten. Halla el número.
> 4. **Reto USD:** Toma el número del ejercicio anterior (94). Si cada **unidad** de valor de las cifras representara un billete de $1 USD (ej. cifra 9 = 9 billetes), ¿cuántos dólares tendrías en total sumando ambos dígitos?

> [!success] Bloque de Éxito: Respuestas para el Docente
> **Nivel Verde:** 1. (L:6.6, A:3.3), 2. (L:12, A:7), 3. (B:10, A:5), 4. (L:10).
> **Nivel Amarillo:** 1. (i:8, d:5), 2. (i:14.4, d:7.2), 3. (i:8, d:5), 4. (i:10, d:5).
> **Nivel Rojo:** 1. (45), 2. (39), 3. (94), 4. ($13 USD).

---

## Autoevaluación

> [!question] Pregunta 1 (Conceptual)
> En un número de dos cifras, ¿por qué usamos la expresión $10d + u$ en lugar de simplemente $d + u$?
> *Respuesta: Porque el dígito en la posición de las decenas representa grupos de diez unidades según el sistema decimal.*

> [!question] Pregunta 2 (Procedimental)
> Si en un sistema de suma de cifras $u + d = 13$ sabemos que $d = 9$, ¿cuánto vale $u$?
> *Respuesta: $u = 4$.*

> [!question] Pregunta 3 (Aplicación $USD)
> Si un marco rectangular de $42 \text{ cm} \times 29 \text{ cm}$ tiene un costo de fabricación de $0.50 USD por cada centímetro de perímetro, ¿cuál es el costo total?
> *Respuesta: $71 USD ($142 \text{ cm} \times 0.50$).*

---

> [!tip] 💡 En la próxima clase
> ¡Felicidades! Has terminado el bloque de resolución de problemas. En la siguiente sesión veremos el último tema antes del gran examen de bloque: **Sistemas de Ecuaciones 3x3**.

> [!info] 🧭 Navegación
> **Anterior:** [[Clase 06 — Métodos de resolución]]
> **Índice:** [[00 - Índice del curso]]