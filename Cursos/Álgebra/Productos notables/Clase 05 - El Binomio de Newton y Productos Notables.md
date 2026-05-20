# Clase 05 — El Binomio de Newton y Productos Notables
tags: #algebra #newtonsbinomial
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 5 de 6

> [!info] 🧭 Navegación
> [[Clase 04|⬅ Clase 04]] | [[00 - Índice del curso|Índice]] | **Clase 05** | [[Clase 06|Clase 06 ➡]]

---

## ¿Por qué es importante esta clase?
¿Alguna vez has intentado multiplicar un paréntesis por sí mismo cinco o seis veces? Es un proceso tedioso, lento y donde es sumamente fácil cometer un pequeño error que arruine todo el cálculo. ¡Hoy vamos a cambiar eso! Como experto, te enseñaré a "leer" el resultado directamente usando patrones numéricos. El Binomio de Newton y los productos notables no son solo fórmulas para memorizar, sino herramientas de eficiencia profesional:

- 💵 **Finanzas:** Para proyectar el crecimiento de un capital bajo interés compuesto usando la expansión de $(1 + r)^t$.
- 🏗️ **Ingeniería:** Para calcular la resistencia de materiales donde las variables crecen de forma polinomial.
- 📊 **Probabilidad:** Para hallar combinaciones posibles en eventos estadísticos mediante sus coeficientes.

---

## Conceptos clave

### 1. El Triángulo de Pascal
Antes de aplicar Newton, debemos entender su "mapa": el Triángulo de Pascal. Este triángulo nos da los **coeficientes** (los números que acompañan a las letras). 
**¿Cómo se construye?** Es un proceso de "suma de vecinos":
1. Empieza con un 1 en la cima.
2. Cada número de la fila inferior es la suma de los dos números que tiene justo encima.
3. Imagina que en los extremos hay ceros invisibles: $0 + 1 = 1$. Por eso, todas las filas empiezan y terminan con 1.
*Ejemplo:* Para la fila 2 tenemos (1, 2, 1). La fila 3 se obtiene sumando: $1, (1+2=3), (2+1=3), 1$.

### 2. El Binomio de Newton
Es la fórmula maestra para elevar cualquier binomio $(a \pm b)$ a una potencia entera positiva $n$. 

> [!warning] ⚠️ Error común de principiante
> ❌ **Incorrecto:** $(a + b)^2 = a^2 + b^2$ (¡Faltan los términos del medio!).
> ✅ **Correcto:** $(a + b)^2 = a^2 + 2ab + b^2$. 
> Recuerda: Al elevar potencias de potencias, los exponentes se multiplican: $(x^n)^m = x^{n \cdot m}$.

> [!tip] 💡 Truco del Profesor: "Sube y Baja"
> Para no perderte con las letras, observa este patrón:
> - El exponente del **primer término** empieza en el máximo ($n$) y **baja** hasta cero.
> - El exponente del **segundo término** empieza en cero y **sube** hasta el máximo ($n$).

---

## Procedimiento paso a paso
Sigue este orden riguroso para no fallar:

1. **PASO 1:** Identifica el exponente $n$ y busca la fila $n$ en el Triángulo de Pascal para obtener tus coeficientes.
2. **PASO 2:** Escribe los coeficientes dejando espacio. Si es suma, todos son $(+)$; si es resta, intercala los signos $(+, -, +, -, \dots)$.
3. **PASO 3:** Distribuye el primer término de forma descendente y el segundo de forma ascendente.
4. **PASO 4:** Resuelve primero las potencias y luego multiplica esos resultados por los coeficientes iniciales.

---

## Ejemplos de clase

> [!example] Ejemplo 1 — Caso básico (Binomio de Newton)
> **Desarrollar:** $(3m + 2n)^4$
> 1. **Coeficientes (Fila 4):** 1, 4, 6, 4, 1
> 2. **Desglose inicial:** $1(3m)^4 + 4(3m)^3(2n)^1 + 6(3m)^2(2n)^2 + 4(3m)^1(2n)^3 + 1(2n)^4$
> 3. **Resolución de potencias:** $1(81m^4) + 4(27m^3)(2n) + 6(9m^2)(4n^2) + 4(3m)(8n^3) + 1(16n^4)$
> 4. **Resultado final:** $81m^4 + 216m^3n + 216m^2n^2 + 96mn^3 + 16n^4$

> [!example] Ejemplo 2 — Caso con signos intercalados
> **Desarrollar:** $(4x - y)^5$
> 1. **Coeficientes (Fila 5):** 1, 5, 10, 10, 5, 1 (Signos: $+ , - , + , - , + , -$)
> 2. **Desglose inicial:** $1(4x)^5 - 5(4x)^4(y) + 10(4x)^3(y)^2 - 10(4x)^2(y)^3 + 5(4x)(y)^4 - 1(y)^5$
> 3. **Resolución de potencias:** $1(1024x^5) - 5(256x^4)(y) + 10(64x^3)(y^2) - 10(16x^2)(y^3) + 20xy^4 - y^5$
> 4. **Resultado final:** $1024x^5 - 1280x^4y + 640x^3y^2 - 160x^2y^3 + 20xy^4 - y^5$

> [!example] Ejemplo 3 — Binomio Conjugado (Producto Notable)
> **Resolver:** $(5x + 3)(5x - 3)$
> **Regla de oro:** El primero al cuadrado menos el segundo al cuadrado.
> - **Proceso:** $(5x)^2 - (3)^2$
> - **Resultado final:** $25x^2 - 9$
> > [!info] Nota del Profesor
> > ¿Por qué desaparece el término medio? Porque al multiplicar de forma larga, obtendrías $-15x$ y $+15x$. Al ser términos semejantes con signos opuestos, se cancelan exactamente ($15x - 15x = 0$).

> [!example] Ejemplo 4 — Aplicación real con USD
> **Problema:** Un terreno cuadrado mide $(x + 4)$ metros por lado. Si el costo del m² es de $10 USD, ¿cuál es el valor total del terreno?
> 1. **Área (Binomio al cuadrado):** $(x + 4)^2 = x^2 + 8x + 16$.
> 2. **Valor monetario:** $10(x^2 + 8x + 16) = 10x^2 + 80x + 160$.
> - **Resultado:** $10x^2 + 80x + 160$ USD.

---

## Ejercicios para el estudiante

> [!abstract] 🟢 Fácil — Conceptos y Pascal
> 1. Construye las primeras 6 filas del Triángulo de Pascal.
> 2. Desarrolla $(a + b)^3$ usando los coeficientes del triángulo.
> 3. Resuelve mentalmente: $(x + 2)(x - 2)$.
> 4. ¿Cuántos términos tiene el desarrollo de $(m + n)^4$?

> [!abstract] 🟡 Medio — Aplicación de potencias
> 1. Desarrolle $(2x + 3y)^4$.
> 2. Resuelva el binomio conjugado $(3m^2 + 2n)(3m^2 - 2n)$.
> 3. Desarrolle $(x^2 - 5)^3$.
> 4. Simplifique la expresión: $(x + 1)^2 - (x - 1)^2$.

> [!abstract] 🔴 Avanzado — Retos de aplicación
> 1. Un capital de 1000 USD crece a una tasa $r=0.05$ durante $t=3$ años según $(1+r)^t$. Desarrolla el binomio y calcula el valor final.
> 2. El costo de un chip es $(x^2 + 10)^2$ USD. Si $x=2$, ¿cuál es el costo?
> 3. Resuelve el binomio complejo del video: $(4m^2n^3 - 2p)^5$.
> 4. Diferencia de precio entre dos parcelas cuadradas de lados $(x+5)$ y $(x-5)$ si el m² vale $50 USD.

---

> [!success] ✅ Respuestas (Clave Docente)
> **Nivel Fácil:**
> 1. Filas: (1), (1,1), (1,2,1), (1,3,3,1), (1,4,6,4,1), (1,5,10,10,5,1).
> 2. $a^3 + 3a^2b + 3ab^2 + b^3$.
> 3. $x^2 - 4$.
> 4. 5 términos (Regla: $n+1$).
>
> **Nivel Medio:**
> 1. $16x^4 + 96x^3y + 216x^2y^2 + 216xy^3 + 81y^4$.
> 2. $9m^4 - 4n^2$.
> 3. $x^6 - 15x^4 + 75x^2 - 125$.
> 4. **4x**. Desarrollo: $(x^2+2x+1) - (x^2-2x+1) = 2x - (-2x) = 4x$.
>
> **Nivel Avanzado:**
> 1. **1157.625 USD**. Desarrollo: $1000[1^3 + 3(1)^2(0.05) + 3(1)(0.05)^2 + (0.05)^3]$. Esto es $1000(1 + 0.15 + 0.0075 + 0.000125)$.
> 2. **196 USD**. $(2^2 + 10)^2 = (4+10)^2 = 14^2 = 196$.
> 3. $1024m^{10}n^{15} - 2560m^8n^{12}p + 2560m^6n^9p^2 - 1280m^4n^6p^3 + 320m^2n^3p^4 - 32p^5$.
> 4. **1000x USD**. Resta de áreas: $(x^2+10x+25) - (x^2-10x+25) = 20x$. Multiplicado por 50 USD/m² da $1000x$.

---

## Mini-prueba de autoevaluación

> [!question] 🧪 Pregunta 1
> ¿Cuál es el desarrollo correcto de $(x - y)^2$?
> a) $x^2 + y^2$
> b) $x^2 - y^2$
> c) $x^2 - 2xy + y^2$
> d) $x^2 + 2xy + y^2$
> **Respuesta correcta: c)** En un binomio al cuadrado con resta, el término central siempre es negativo.

> [!question] 🧪 Pregunta 2
> Si elevamos un binomio a la potencia $n=6$, ¿cuántos términos obtendremos?
> a) 5
> b) 6
> c) 7
> d) 12
> **Respuesta correcta: c)** El número de términos es siempre $n+1$.

> [!question] 🧪 Pregunta 3
> Si el área de un local es $(x+10)(x-10)$ m² y el m² cuesta $2 USD, ¿cuál es el precio total?
> a) $2x^2 - 200$ USD
> b) $x^2 - 100$ USD
> c) $2x^2 - 100$ USD
> d) $2x - 20$ USD
> **Respuesta correcta: a)** El producto notable es $(x^2 - 100)$, que multiplicado por 2 resulta en $2x^2 - 200$.

---

## Notas para el próximo tema
> [!tip] 💡 En la próxima clase
> ¡Felicidades! Has dominado el arte de "expandir" expresiones. En la siguiente clase haremos el camino de regreso: la **Factorización**. Aprenderemos a tomar estos resultados y encontrar los paréntesis originales.

> [!info] 🧭 Navegación
> [[Clase 04|⬅ Clase 04]] | [[00 - Índice del curso|Índice]] | **Clase 05** | [[Clase 06|Clase 06 ➡]]