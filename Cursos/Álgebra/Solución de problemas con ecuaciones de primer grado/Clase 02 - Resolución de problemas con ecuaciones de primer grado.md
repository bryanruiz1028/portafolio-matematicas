# Clase 02 — Resolución de problemas con ecuaciones de primer grado
tags: #algebra #solucindeproble
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 4

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | | [[Clase 03|Clase 03 ➡]]

## ¿Por qué es importante esta clase?
> [!info] 🌍 Relevancia y aplicaciones
> Resolver problemas con ecuaciones no es solo hacer cálculos; es desarrollar la capacidad de convertir el lenguaje cotidiano en lenguaje matemático. Esta habilidad te permite encontrar respuestas exactas a incógnitas sobre cantidades desconocidas, lo que te ayuda a tomar decisiones basadas en datos reales y lógica, ¡evitando las suposiciones!

- 💵 **Finanzas personales:** Calcular presupuestos cuando los precios de productos dependen de otros valores.
- 🏗️ **Planificación técnica:** Determinar dimensiones o cantidades exactas en proyectos de construcción o logística.
- 📊 **Situaciones cotidianas:** Resolver acertijos sobre edades y repartir recursos de manera equitativa.

## Concepto clave
> [!note] 📌 ¿Qué es la solución de problemas con ecuaciones?
> ¡Imagina que eres un **detective numérico**! Resolver un problema de este tipo consiste en traducir una historia o un acertijo del lenguaje común a una "oración matemática" (la ecuación). Tu objetivo es descubrir el valor de una letra "escondida" (la incógnita) que hace que la historia tenga sentido.
> 
> [!warning] ⚠️ Error común
> ❌ **Incorrecto:** Encontrar el valor de la incógnita (ej. $n = 43$) y darlo como respuesta final sin leer la pregunta original. 
> ✅ **Correcto:** Verificar si el resultado satisface las condiciones del problema y responder específicamente lo que se pregunta (ej. "El número mayor es 88").
> 
> [!tip] 💡 Truco para recordarlo: La regla de las 3 "L"
> Para que nunca te pierdas, aplica siempre:
> 1. **L**eer el problema (entender la historia).
> 2. **L**enguaje algebraico (traducir a símbolos).
> 3. **L**ógica de verificación (comprobar si la respuesta es coherente).

## Procedimiento paso a paso
¡No te asustes por el texto largo! Vamos a desglosarlo como un profesional. Antes de empezar, recuerda que la parte más difícil es la traducción; una vez que tienes la ecuación, ¡ya tienes medio camino ganado!

> [!tip] 💡 Paso 0: Estimación Lógica
> Antes de escribir cualquier ecuación, intenta "adivinar" el número mentalmente. ¿Es más de 10? ¿Menos de 100? Esto te dará una "brújula" para saber si tu resultado final tiene sentido.

```text
PASO 1 → Asignar una letra a la incógnita principal (lo que nos preguntan).
PASO 2 → Traducir el enunciado del lenguaje formal al algebraico (formar la ecuación).
PASO 3 → Resolver la ecuación despejando la letra (letras a un lado, números al otro).
PASO 4 → Verificar el resultado en el enunciado original para asegurar que cumple las condiciones.
```

---

## Ejemplo 1 — Caso básico: El doble de un número
*Si al doble de un número le restamos 14, se obtiene 30. ¿Cuál es el número?*

```ad-example
title: Resolución Paso a Paso
→ **Paso 1:** Definimos $n$ como el número desconocido.
→ **Paso 2 (Ecuación):** $2n - 14 = 30$.
→ **Paso 3 (Resolución):** 
$2n = 30 + 14$
$2n = 44$
$n = \frac{44}{2} \implies n = 22$.

✅ **Resultado:** El número es 22.
🔍 **Verificación:** El doble de 22 es $2(22) = 44$. Si le restamos 14: $44 - 14 = 30$. ¡Correcto!
```

## Ejemplo 2 — Caso con signos: Números pares consecutivos
*La suma de dos números pares consecutivos es 174. ¿Cuál es el número mayor?*

> [!tip] 🔑 El "Código Secreto" de la Paridad
> Para un pedagogo, es vital que sepas esto: $2n$ es el "código secreto" que garantiza que un número sea **par**, porque cualquier número multiplicado por 2 siempre es par. El siguiente par siempre será $2n + 2$.

```ad-example
title: Resolución Paso a Paso
→ **Paso 1:** Menor = $2n$; Mayor = $2n + 2$.
→ **Paso 2 (Ecuación):** $(2n) + (2n + 2) = 174$.
→ **Paso 3 (Resolución):**
$4n + 2 = 174$
$4n = 172$
$n = \frac{172}{4} \implies n = 43$.
*Ahora sustituimos para hallar el mayor:* $2(43) + 2 = 86 + 2 = 88$.

✅ **Resultado:** El número mayor es 88.
🔍 **Verificación:** Si el mayor es 88, el anterior par es 86. Sumamos: $86 + 88 = 174$. ¡Exacto!
```

## Ejemplo 3 — Caso avanzado: Edades y tiempo
*La edad de Andrés es el doble de la de Claudia. Hace 10 años, la edad de Andrés era el cuádruple de la de Claudia. ¿Qué edades tienen hoy?*

```ad-example
title: Resolución Paso a Paso
→ **Paso 1:** Claudia hoy = $c$; Andrés hoy = $2c$.
→ **Paso 2 (Ecuación):** Hace 10 años, ambos tenían 10 años menos:
$2c - 10 = 4(c - 10)$
→ **Paso 3 (Resolución):**
$2c - 10 = 4c - 40$
$40 - 10 = 4c - 2c$
$30 = 2c \implies c = \frac{30}{2} \implies c = 15$.

✅ **Resultado:** Claudia tiene 15 años y Andrés tiene 30.
🔍 **Verificación:** Hace 10 años, Claudia tenía 5 y Andrés tenía 20. ¿Es 20 el cuádruple de 5? $4(5) = 20$. ¡Perfecto!
```

## Ejemplo 4 — Aplicación real con $USD (Presupuesto)
*El costo de una laptop y un monitor suma $110 USD. Si el precio de la laptop excede al quíntuple del precio del monitor en $2 USD, ¿cuánto cuesta cada uno?*

```ad-example
title: Resolución Paso a Paso
→ **Paso 1:** Monitor = $n$; Laptop = $5n + 2$.
→ **Paso 2 (Ecuación):** $n + (5n + 2) = 110$.
→ **Paso 3 (Resolución):**
$6n + 2 = 110$
$6n = 108$
$n = \frac{108}{6} \implies n = 18$.
*Laptop:* $5(18) + 2 = 90 + 2 = 92$.

✅ **Resultado:** El monitor cuesta $18 USD y la laptop $92 USD.
🔍 **Verificación:** $18 + 92 = 110$. Además, $92$ es igual a $5(18) + 2$. ¡Cuentas claras!
```

---

## Ejercicios para el estudiante
Pon a prueba tus habilidades de detective con estos retos de tres niveles. ¡Recuerda aplicar las 3 L y no olvides el Paso 0!

```ad-abstract
title: 🟢 Fácil — Traduciendo enunciados sencillos
1. El triple de un número disminuido en 8 equivale al mismo número aumentado en 24. Hallar el número.
2. Si al doble de un número le sumas 10, obtienes 50. ¿Cuál es el número?
```

```ad-abstract
title: 🟡 Medio — Números consecutivos y repartición
1. Hallar tres números pares consecutivos cuya suma sea 162.
2. En un grupo de 281 personas, las mujeres exceden en 23 al doble de los hombres. ¿Cuántos hombres y mujeres hay?
```

```ad-abstract
title: 🔴 Avanzado — Edades y dinero ($USD)
1. Diana tiene el triple de la edad de Camilo. Dentro de 5 años, la edad de Diana será el doble de la de Camilo. Hallar sus edades actuales.
2. Un smartphone y un estuche cuestan $154 USD. Si el smartphone cuesta el séxtuple del estuche más $7 USD, ¿cuál es el precio de cada artículo?
```

```ad-success
title: ✅ Respuestas (para el docente)
- **Fácil:** 1. [16] | 2. [20]
- **Medio:** 1. [Los números son 52, 54 y 56] | 2. [86 hombres y 195 mujeres]
- **Avanzado:** 1. [Camilo: 5 años, Diana: 15 años] | 2. [Estuche: $21 USD, Smartphone: $133 USD]
```

---

## Mini-prueba de autoevaluación
```ad-question
title: 🧪 Pregunta 1
¿Cuál es el primer paso indispensable para resolver un problema mediante ecuaciones según lo visto en clase?
a) Resolver la suma.  
b) Asignar una letra (variable) a la incógnita.  
c) Multiplicar por dos.  
d) Escribir el resultado.  
**Respuesta:** b) — Sin definir la variable, no se puede construir la estructura lógica.
```

```ad-question
title: 🧪 Pregunta 2
Si buscamos dos números pares consecutivos, ¿cómo debemos representar el segundo número algebraicamente?
a) $n + 1$  
b) $2n$  
c) $2n + 2$  
d) $n + n$  
**Respuesta:** c) — Los números pares van de dos en dos, por lo tanto, sumamos 2 al primer par ($2n$).
```

```ad-question
title: 🧪 Pregunta 3
Si un videojuego cuesta el doble que un control y entre ambos suman $90 USD, ¿cuál es la ecuación correcta?
a) $x + 2x = 90$  
b) $x + x + 2 = 90$  
c) $2x = 90$  
d) $x - 2x = 90$  
**Respuesta:** a) — Sumamos el precio del control ($x$) más el doble de ese precio ($2x$) para igualar al total.
```

## Notas para el próximo tema
> [!tip] 💡 En la próxima clase
> Ahora que dominas los problemas con números enteros, prepárate para la **Clase 03**, donde aprenderemos a resolver ecuaciones que incluyen **fracciones**. Aplicaremos los mismos pasos de traducción, pero con nuevas herramientas para despejar. ¡Te espero!

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | | [[Clase 03|Clase 03 ➡]]