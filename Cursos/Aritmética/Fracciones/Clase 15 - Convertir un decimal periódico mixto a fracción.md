[[Clase 14|⬅ Clase 14]] | [[00 - Índice del curso|Índice]] | [[Clase 16|Clase 16 ➡]]

# Clase 15 — Convertir un decimal periódico mixto a fracción

¡Hola! Soy tu guía en este fascinante camino por la aritmética. Hoy daremos un paso maestro: aprenderemos a transformar decimales periódicos mixtos en fracciones exactas. Esta habilidad es como tener una "llave maestra" que nos permite pasar de la imprecisión del infinito a la seguridad de los números enteros. ¡Comencemos!

---

## 1. ¿Por qué es importante esta clase?

En matemáticas, la precisión lo es todo. Trabajar con decimales que nunca terminan puede causar errores acumulados en cálculos complejos. Las fracciones, en cambio, capturan el valor real sin perder un solo decimal.

*   **Finanzas (USD):** Al manejar tasas de interés o balances bancarios, un decimal periódico mal redondeado puede significar la pérdida de dinero. Expresar $\$8,75\bar{9}$ como una fracción exacta garantiza un informe contable impecable.
*   **Carpintería e Ingeniería:** Si una medida es de $0,41\bar{6}$ pulgadas, convertirla a la fracción $\frac{5}{12}$ permite que un ingeniero ajuste sus herramientas con total fidelidad al plano original.
*   **Cotidiana:** ¿Alguna vez has intentado dividir una cuenta de $\$100$ entre 6 personas? El resultado es $16,666...$. Entender la fracción $\frac{100}{6}$ (o $\frac{50}{3}$) nos permite repartir el presupuesto de forma equitativa sin dejar "centavos en el aire".

---

## 2. Conceptos Clave

> [!info] **¿Qué es un Decimal Periódico Mixto?**
> Es aquel que, después de la coma, tiene una combinación de dos mundos:
> 1. **Anteperiodo:** Cifras que no se repiten (se quedan fijas).
> 2. **Periodo:** Cifras que se repiten infinitamente.
> *Ejemplo:* En $1,1\bar{6}$, el **1** es el anteperiodo y el **6** es el periodo.

> [!abstract] **¿Qué es un Número Mixto?**
> Es la unión de un número entero y una fracción propia. Es muy útil para visualizar cantidades que superan la unidad (como una pizza entera y un trozo de otra).
> *Ejemplo:* $1 \frac{2}{3}$ (Se lee: un entero y dos tercios).

> [!warning] **¡Cuidado con el Denominador!**
> Un error muy común es tratar a los decimales mixtos como si fueran puros. Recuerda: el denominador debe reflejar tanto la parte que se repite como la que no. Si olvidas los ceros del anteperiodo, tu resultado estará equivocado.

> [!tip] **Truco: La Regla de las Flechas (Sin cruces)**
> Para construir el denominador en el método directo, usa esta lógica visual:
> 1. Mira el **periodo**: Pon un **9** por cada cifra que se repita.
> 2. Mira el **anteperiodo**: Pon un **0** por cada cifra decimal que no se repita.
> 
> **Visualización:**
> Decimal: $0, 4 1 \bar{6}$
> $\quad \quad \quad \quad \quad \downarrow$
> Periodo (6): $\quad \quad 1 \text{ cifra} \rightarrow 9$
> Anteperiodo (41): $2 \text{ cifras} \rightarrow 00$
> **Denominador resultante: 900**

---

## 3. Procedimiento paso a paso (Método Algebraico)

El **Método Algebraico** (o Método de las Ecuaciones) es el más sólido porque nos enseña la lógica detrás de la eliminación del infinito.

1.  **Igualar:** Llamamos $x$ a nuestro decimal (Ej. $x = 1,1\bar{6}$).
2.  **Preparar (Hacia Periódico Puro):** Multiplicamos por una potencia de 10 para mover la coma justo hasta donde empieza el periodo.
3.  **Desplazar (Cubrir el Periodo):** Multiplicamos nuevamente para que la coma salte el periodo completo.
4.  **Restar y Resolver:** Restamos las ecuaciones resultantes para "borrar" la parte infinita y despejamos $x$.

---

## 4. Ejemplos Resueltos

### Ejemplo 1: Convertir $1,1\bar{6}$ (Método Algebraico)
*   **Paso 1:** $x = 1,1666...$
*   **Paso 2:** Multiplicamos por 10 (1 cifra de anteperiodo): $10x = 11,666...$
*   **Paso 3:** Multiplicamos el original por 100 (para saltar el 1 y el 6): $100x = 116,666...$
*   **Paso 4 (Resta Vertical):**
$$
\begin{array}{r@{\quad=\quad}l}
100x & 116,666... \\
- 10x & 11,666... \\
\hline
90x & 105
\end{array}
$$
*   **Resolución:** $x = \frac{105}{90}$. Simplificamos dividiendo entre 15: **$x = \frac{7}{6}$**.

### Ejemplo 2: Convertir $0,41\bar{6}$ (Manejo de ceros)
*   $x = 0,41666...$
*   Multiplicamos por 100 para llegar al periodo: $100x = 41,666...$
*   Multiplicamos por 1000 para pasar el periodo: $1000x = 416,666...$
*   **Resta Vertical:**
$$
\begin{array}{r@{\quad=\quad}l}
1000x & 416,666... \\
- 100x & 41,666... \\
\hline
900x & 375
\end{array}
$$
*   **Simplificación paso a paso:**
    $\frac{375}{900} \xrightarrow{\div 5} \frac{75}{180} \xrightarrow{\div 5} \frac{15}{36} \xrightarrow{\div 3} \mathbf{\frac{5}{12}}$.

### Ejemplo 3: Convertir $3,2\overline{45}$ (Método Directo)
Aquí usamos la fórmula rápida para mayor agilidad:
*   **Numerador:** Todo el número sin coma ($3245$) menos la parte no periódica ($32$).
    $3245 - 32 = 3213$
*   **Denominador:** Dos "9" (por el 45) y un "0" (por el 2).
    $990$
*   **Resultado:** $\frac{3213}{990} \xrightarrow{\text{simplificado por 9}} \mathbf{\frac{357}{110}}$.

### Ejemplo 4: El Caso Especial USD ($8,75\bar{9}$)
En contabilidad, a veces aparece un $9$ periódico al final. 
*   **Cálculo:** $\frac{8759 - 875}{900} = \frac{7884}{900}$.
*   Simplificando sucesivamente llegamos a $\mathbf{\frac{219}{25}}$.
> [!note] **Observación Pedagógica:** Si divides $219 \div 25$, obtendrás **$8,76$**. ¿Por qué? Porque un $9$ periódico tiene el efecto de "redondear" hacia arriba la cifra anterior. Por eso, en un libro contable, $\frac{219}{25}$ es la forma perfecta de cerrar un ciclo infinito.

---

## 5. Ejercicios para el Estudiante

> [!question] **¡Pon a prueba tu lógica!**
> Resuelve y simplifica a la mínima expresión:
> 1. **Nivel Fácil:** Convierte $0,4\bar{6}$ a fracción.
> 2. **Nivel Medio:** Convierte $1,0\overline{12}$ a fracción.
> 3. **Nivel Avanzado (USD):** Una tasa de presupuesto es de $0,1\overline{81}$. Exprésala como fracción para evitar errores de redondeo.

> [!success] **Resultados Sugeridos**
> 1. $\frac{7}{15}$
> 2. $\frac{167}{165}$ (proviene de $\frac{1002}{990}$)
> 3. $\frac{2}{11}$ (proviene de $\frac{180}{990}$)

---

## 6. Mini-prueba de autoevaluación

1.  **¿Cuál es el anteperiodo en el número $23,7\overline{32}$?**
    *   a) 32
    *   b) 7
    *   c) 23
2.  **Al convertir $0,1\bar{2}$ por el método directo, ¿por qué el denominador es 90?**
    *   a) Porque hay un 9 por el periodo (2) y un 0 por el anteperiodo (1).
    *   b) Porque tiene dos decimales.
    *   c) Es una regla fija para todos los decimales.
3.  **Si un producto cuesta $\$0,8\bar{3}$ por gramo, ¿cuál es su valor en fracción?**
    *   a) $\frac{5}{6}$
    *   b) $\frac{83}{100}$
    *   c) $\frac{1}{3}$

*Respuestas: 1-b, 2-a, 3-a ($\frac{75}{90}$ simplificado).*

---

## 7. Notas para el próximo tema

¡Excelente trabajo! Has dominado la conversión más difícil. En la **Clase 16**, utilizaremos estas fracciones para resolver **operaciones combinadas**. Prepárate para sumar, restar y multiplicar decimales y fracciones en un mismo ejercicio.

[[Clase 14|⬅ Clase 14]] | [[00 - Índice del curso|Índice]] | [[Clase 16|Clase 16 ➡]]

---
`SEPARADOR_GUIA_ESTUDIO`

# Guía de Estudio: Decimales y Números Mixtos

### Resumen Comparativo de Conversión
| Tipo de Decimal | Ejemplo | Característica | Denominador (Método Directo) |
| :--- | :--- | :--- | :--- |
| **Exacto** | $0,5$ | No tiene periodo | Potencia de 10 (Ej. $10$) |
| **Periódico Puro** | $0,\bar{3}$ | Periodo inicia tras la coma | Solo nueves (Ej. $9$) |
| **Periódico Mixto** | $1,1\bar{6}$ | Tiene anteperiodo y periodo | Nueves y ceros (Ej. $90$) |

### Fórmula Maestra (Método Directo)
$$\text{Fracción} = \frac{\text{Número Completo (sin coma)} - \text{Parte No Periódica (sin coma)}}{\text{Tantos 9 como cifras periódicas y tantos 0 como anteperiódicas}}$$

### Explicación Gráfica de Números Mixtos
Imagina que los números son comida para visualizar mejor las fracciones:

*   **De Mixto a Fracción ($1 \frac{2}{3}$):** Imagina que tienes **un pastel entero** y **2/3 de otro**. Para saber cuánto tienes en total, corta el pastel entero en 3 trozos iguales. Ahora tienes 3 trozos (del primero) + 2 trozos (del segundo) = **5 trozos de un tercio ($\frac{5}{3}$)**.
*   **De Fracción a Mixto ($\frac{9}{2}$):** Tienes 9 mitades de pan. Si juntas cada par de mitades para hacer panes completos, formarás **4 panes enteros** y te sobrará **una mitad**. Se escribe: **$4 \frac{1}{2}$**.

### Ejercicios de Repaso Final

1.  **Conversión:** $2 \frac{1}{3}$ a fracción. (Respuesta: $\frac{7}{3}$)
2.  **Conversión:** $\frac{11}{4}$ a número mixto. (Respuesta: $2 \frac{3}{4}$)
3.  **Decimal Mixto:** $7,0\bar{5}$ a fracción. (Respuesta: $\frac{127}{18}$ después de simplificar $\frac{635}{90}$)
4.  **Avanzado:** $23,7\overline{32}$ a fracción. (Respuesta: $\frac{23495}{990} \rightarrow \mathbf{\frac{4699}{198}}$)