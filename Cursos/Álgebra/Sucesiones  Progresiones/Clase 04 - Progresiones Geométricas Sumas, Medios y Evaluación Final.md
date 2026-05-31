# Clase 04 — Progresiones Geométricas: Sumas, Medios y Evaluación Final
#algebra #geometricprogre

> [!info] 🧭 Navegación
> - [Clase 01 — Introducción a las Progresiones](clase-01)
> - [Clase 02 — Término Enésimo](clase-02)
> - [Clase 03 — La Razón en Progresiones Geométricas](clase-03)
> - **Clase 04 — Sumas, Medios y Evaluación Final**

---

> [!info] 🌍 Relevancia y aplicaciones
> Las progresiones geométricas son el lenguaje del crecimiento acelerado. A diferencia de las progresiones aritméticas (que avanzan a pasos constantes), estas "saltan" mediante multiplicaciones, permitiéndonos modelar fenómenos dinámicos:
> - **Finanzas ($USD):** Es la base del interés compuesto, donde tu dinero no solo crece, sino que crece cada vez más rápido sobre los intereses acumulados.
> - **Construcción y Diseño:** Se utiliza en la arquitectura fractal y en el cálculo de estructuras que deben soportar cargas proporcionales decrecientes o crecientes.
> - **Situaciones Cotidianas:** Explica la viralidad en redes sociales; si una persona comparte un video con 3 amigos y estos repiten el proceso, el crecimiento sigue una secuencia geométrica imparable.

---

> [!note] 📌 ¿Qué son los Medios Geométricos y la Suma?
> **Interpolar medios geométricos** es como **construir un puente**. Imagina que el primer término ($a_1$) y el último ($a_n$) son los pilares sólidos en las orillas de un río. Los "medios" son las vigas intermedias que debemos colocar. Para que el puente sea estable y perfecto, estas vigas deben estar separadas por una proporción exacta llamada razón ($r$).
> 
> Por otro lado, la **Suma de términos ($S_n$)** es nuestra herramienta de eficiencia. En lugar de sumar uno a uno todos los términos de una secuencia larga, usamos una fórmula que nos da el total acumulado de forma instantánea.

> [!warning] ⚠️ Error común
> Al buscar la razón para interpolar, es vital recordar que el índice de la raíz es $n - 1$. Si te piden interpolar 4 medios, no uses raíz cuarta; el total de términos es 6, por lo que debes usar raíz quinta ($\sqrt[5]{\dots}$).

> [!tip] 💡 Truco para recordarlo
> Para determinar $n$ en cualquier problema de interpolación, aplica siempre: 
> $$n = \text{medios a interpolar} + 2$$
> (Los "2" representan los dos extremos que ya conoces).

---

### Procedimiento Paso a Paso (Algoritmos)

#### Algoritmo para Interpolar Medios Geométricos
```text
1. Identificar a1, an y la cantidad de medios solicitados.
2. Definir n como (medios + 2).
3. Calcular la razón r con la fórmula: r = [(an / a1)^(1/(n-1))].
4. Generar la secuencia multiplicando a1 por r sucesivamente hasta llegar a an.
```

#### Algoritmo para Calcular la Suma ($S_n$)
```text
1. Identificar a1, r y n.
2. Verificar r: 
   - Si r = 1: La suma es simplemente Sn = n * a1.
   - Si r ≠ 1: Aplicar Sn = [a1 * (r^n - 1)] / (r - 1).
3. Resolver siguiendo la jerarquía: Potencia -> Resta -> Multiplicación -> División.
```

---

### Ejemplos Prácticos

**Ejemplo 1: Interpolar 4 medios geométricos entre 96 y 3**
- **Datos:** $a_1 = 96$, $a_n = 3$, Medios = 4 $\Rightarrow n = 6$.
- **Razón:** $r = \sqrt[6-1]{\frac{3}{96}} = \sqrt[5]{\frac{1}{32}} = \frac{1}{2}$.
- **Secuencia:** $96, \mathbf{48, 24, 12, 6}, 3$.
- *Resultado:* Los medios son $48, 24, 12$ y $6$.

**Ejemplo 2: Interpolar 3 medios entre 3 y 48 (Caso de raíz par)**
- **Datos:** $a_1 = 3$, $a_n = 48$, Medios = 3 $\Rightarrow n = 5$.
- **Razón:** $r = \sqrt[5-1]{\frac{48}{3}} = \sqrt[4]{16} = \pm 2$.
- **Análisis:** Al ser una raíz de índice par, existen dos configuraciones posibles para nuestro "puente":
	1. **Con $r = 2$:** $3, \mathbf{6, 12, 24}, 48$.
	2. **Con $r = -2$:** $3, \mathbf{-6, 12, -24}, 48$ (secuencia oscilante).

**Ejemplo 3: Suma de los primeros 10 términos de $5, 10, 20 \dots$**
- **Datos:** $a_1 = 5, r = 2, n = 10$.
- **Fórmula:** $S_{10} = \frac{5(2^{10} - 1)}{2 - 1}$
- **Cálculo:** $S_{10} = \frac{5(1024 - 1)}{1} = 5(1023) = 5115$.

**Ejemplo 4: Aplicación $USD (Inversión)**
Una inversión de $100 USD se duplica cada año. ¿Cuál es el valor acumulado (suma de los valores anuales) al cabo de 5 años?
- **Datos:** $a_1 = 100, r = 2, n = 5$.
- **Cálculo:** $S_5 = \frac{100(2^5 - 1)}{2 - 1} = 100(31) = 3100$.
- *Resultado:* El valor acumulado es $\$3,100 \text{ USD}$.

---

### Ejercicios para el Estudiante

**🟢 Fácil (Conceptos básicos)**
1. Dada la secuencia $4, 12, 36 \dots$, halla la razón $r$.
2. Calcula el término $a_9$ de la progresión $4, 12, 36 \dots$
3. En la progresión $96, 48, 24 \dots$, halla $r$.
4. Halla $a_9$ para la progresión $96, 48, 24 \dots$

**🟡 Medio (Interpolación y Fracciones)**
1. Interpolar 3 medios geométricos entre $9$ y $16/9$.
2. Calcular la suma de los primeros 7 términos si $a_1 = 2/27$ y $r = 3$.
3. Hallar la suma de los primeros 7 términos de la progresión $1, 2, 4, 8 \dots$
4. Interpolar 6 medios geométricos entre $5/8$ y $80$.

**🔴 Avanzado (Desafíos de Evaluación)**
1. Hallar $a_1$ si se sabe que $a_7 = 1/64$ y la razón $r = 1/2$.
2. Hallar la razón $r$ si el tercer término $a_3 = 3$ y el sexto término $a_6 = 24$.
3. Hallar $a_1$ para la progresión donde $a_3 = 10$ y $r = 5$.
4. Si $a_1 = 6$ y $a_3 = 54$, calcula el décimo término ($a_{10}$).

#### ✅ Respuestas
| Nivel | Ejercicio 1 | Ejercicio 2 | Ejercicio 3 | Ejercicio 4 |
| :--- | :--- | :--- | :--- | :--- |
| **Fácil** | $r=3$ | $a_9=26,244$ | $r=1/2$ | $a_9=3/8$ |
| **Medio** | $r = \pm 2/3$ | $S_7 = 2186/27$ | $S_7 = 127$ | $r=2$ |
| **Avanzado** | $a_1 = 1$ | $r = 2$ | $a_1 = 2/5$ | $a_{10} = 118,098$ |

---

### Autoevaluación (Mini-prueba)

1. **Pregunta Conceptual:** Si la razón es $r = 1$, ¿por qué falla la fórmula $S_n = \frac{a_1(r^n - 1)}{r - 1}$?
   *Respuesta:* Porque al sustituir $r=1$ en el denominador, obtenemos $1 - 1 = 0$. La división por cero es una indeterminación matemática. En este caso, la progresión es constante y la suma es simplemente $n \cdot a_1$.

2. **Pregunta Procedimental:** Interpolar un medio geométrico entre $3$ y $12$.
   *Respuesta:* $n = 3$, $r = \sqrt{12/3} = 2$. El medio es $3 \cdot 2 = 6$.

3. **Pregunta de Aplicación:** Ahorras $\$10$ el primer mes y duplicas la cantidad cada mes. ¿Cuánto has ahorrado **en total** al finalizar el cuarto mes?
   *Respuesta:* $a_1 = 10, r = 2, n = 4$. $S_4 = \frac{10(2^4 - 1)}{2 - 1} = 10(15) = \$150$.

---

### Cierre y Próximo Tema

> [!tip] 💡 En la próxima clase
> Con esto cerramos el estudio de las sucesiones. En el próximo bloque, daremos el salto a las **Matemáticas Financieras**, donde aplicaremos estas fórmulas para entender créditos, amortizaciones y cómo crece el dinero en el tiempo real.

> [!info] 🧭 Navegación
> - [Clase 01 — Introducción a las Progresiones](clase-01)
> - [Clase 02 — Término Enésimo](clase-02)
> - [Clase 03 — La Razón en Progresiones Geométricas](clase-03)
> - **Clase 04 — Sumas, Medios y Evaluación Final**