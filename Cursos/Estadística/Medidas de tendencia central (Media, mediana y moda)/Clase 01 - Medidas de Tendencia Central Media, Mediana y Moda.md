# Clase 01 — Medidas de Tendencia Central: Media, Mediana y Moda
tags: #algebra #medidasdetenden
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 3

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]

## 1. ¿Por qué es importante esta clase?
¡Qué tal, amigos! Espero que estén muy bien. Hoy vamos a entender por qué necesitamos encontrar el "centro" de los datos. En estadística, las medidas de tendencia central sirven para resumir un conjunto de valores en un solo dato representativo, permitiéndonos entender dónde se concentra la información.

Esto lo verás en todos lados:
* **Presupuestos:** Para calcular el promedio de tus gastos mensuales y saber cuánto dinero necesitas ahorrar.
* **Construcción:** Para determinar estaturas promedio o medidas estándar al diseñar espacios (como el ejemplo del niño "mediano").
* **Deportes:** Para analizar el rendimiento de un equipo, como el promedio de goles marcados en una temporada.

## 2. Concepto clave

> [!note] Definición
> Las **Medidas de Tendencia Central** son parámetros estadísticos que nos indican el centro de un conjunto de datos. Son herramientas para identificar el valor más representativo de una lista de números.

> [!warning] ¡Pilas con esto!
> Un error muy común es confundir la frecuencia ($f$) con el valor del dato ($x$). Al dar la respuesta de la moda o la mediana, **el resultado siempre es el valor del dato ($x$)**, no su frecuencia ni su posición.

> [!tip] Regla mnemotécnica para el examen:
> * **Media:** Es el "Promedio" (sumas todo y divides).
> * **Mediana:** Es el "Mediano" (como un niño llamado Alex que, al ordenar a todos por estatura, queda justo en el centro).
> * **Moda:** Es "lo más visto" (el dato que más veces se repite, el que está "de moda").

## 3. Procedimiento paso a paso
Para resolver ejercicios de datos agrupados puntualmente en tablas, sigue esta receta:

```text
1. Organizar datos: Crea columnas para x (dato) y f (frecuencia absoluta).
2. Columna x · f: Multiplica cada dato por su frecuencia para hallar la 
   suma total de los valores (necesario para la Media).
3. Ubicar la Mediana: 
   - Calcula la frecuencia acumulada (F).
   - Encuentra la posición con la fórmula: Posición = n / 2.
   - Busca la posición en la columna F. Si el número no está, 
     mira el siguiente valor hacia arriba.
4. Identificar la Moda: Busca el valor de f más alto; el dato x 
   correspondiente es la Moda.
```

## 4. Ejemplos Desarrollados

> [ad-example] Ejemplo 1: Cálculo básico de Media (Edades)
> Tenemos las edades de 10 estudiantes: 18, 16, 18, 15, 18, 20, 19, 17, 16, 19.
> 1. Sumamos todo: $18+16+18+15+18+20+19+17+16+19 = 176$.
> 2. Dividimos entre el total ($n=10$): $176 / 10 = 17,6$.
> **Resultado:** La media es 17,6 años.

> [ad-example] Ejemplo 2: El orden y la Mediana
> **Caso Impar (7 niños):** Si los ordenas por estatura, el niño en la posición 4 es la mediana porque deja 3 a cada lado.
> **Caso Par (10 estudiantes):** Usando las edades del Ejemplo 1, primero ordenamos: 15, 16, 16, 17, **18, 18**, 18, 19, 19, 20.
> Como hay dos centros (posiciones 5 y 6), promediamos: $(18 + 18) / 2 = 18$.
> **Resultado:** Mediana = 18 años.

> [ad-example] Ejemplo 3: Datos Agrupados (60 Estudiantes)
> Buscamos las medidas para las edades de 60 estudiantes:
> 
> | Edad ($x$) | Frecuencia ($f$) | $x \cdot f$ | Frecuencia Acumulada ($F$) |
> | :--- | :--- | :--- | :--- |
> | 13 | 3 | 39 | 3 |
> | 14 | 14 | 196 | 17 |
> | 15 | 23 | 345 | 40 |
> | 16 | 10 | 160 | 50 |
> | 17 | 5 | 85 | 55 |
> | 18 | 4 | 72 | 59 |
> | 19 | 1 | 19 | 60 |
> | **Total** | **60** | **916** | |
> 
> * **Media:** $\bar{x} = 916 / 60 = 15,26$ años.
> * **Mediana:** Posición $60 / 2 = 30$. Como 30 no está en la columna $F$, buscamos el que sigue: el 40. El valor de $x$ ahí es **15 años**.
> * **Moda:** La frecuencia más alta es 23. El valor de $x$ es **15 años**.

> [ad-example] Ejemplo 4: Aplicación en Precios ($USD)
> Compras tres artículos de \$10, \$15 y \$20 USD.
> 1. Suma: $10 + 15 + 20 = 45$.
> 2. Promedio: $45 / 3 = 15$.
> **Resultado:** El precio promedio es \$15 USD.

## 5. Ejercicios para el estudiante

*   🟢 **Verde (Fácil):** Un equipo marcó estos goles en 15 partidos: `1, 2, 0, 2, 5, 1, 0, 2, 4, 3, 1, 4, 3, 0, 1`. Calcula media, mediana y moda.
*   🟡 **Amarillo (Medio):** Compara la moda de estos dos colegios:
    *   **Colegio A:** `24, 26, 30, 23, 22, 24, 24, 25, 26, 20, 22, 30`
    *   **Colegio B:** `24, 24, 24, 25, 25, 25, 22, 21, 20, 23, 26, 30`
*   🔴 **Rojo (Avanzado):** Completa la tabla y halla las medidas para el número de hermanos de 50 personas:
    *   $x$ (Hermanos): 0, 1, 2, 3, 4
    *   $f$ (Personas): 5, 12, 10, 8, 15

## 6. Respuestas (para el docente)

> [ad-success] Resultados exactos
> *   **Goles:** Media: 1,93; Mediana: 2; Moda: 1.
> *   **Estudiantes:** Colegio A: Moda 24. Colegio B: Bimodal (24 y 25).
> *   **Hermanos:** Media: 2,64 (basado en suma 132); Mediana: 2 (Posición 25); Moda: 4 (frecuencia 15). *Nota: Los cálculos siguen los resultados finales del video del Profe Alex.*

## 7. Mini-prueba de autoevaluación

> [ad-question] Pregunta 1
> Si el número de datos es par (ej. $n=10$), ¿cómo se calcula la mediana?
> *   A) Se elige el número más grande.
> *   B) Se promedian los dos datos centrales.
> *   C) Es igual a la moda.
> **Respuesta: B.** Al no haber un único centro, se toman los dos valores del medio y se dividen entre 2.

> [ad-question] Pregunta 2
> En una tabla, si la posición $n/2$ es 25 y en la columna $F$ tienes los valores 17 y 27, ¿cuál eliges?
> *   A) El 17, por ser el más cercano.
> *   B) El 27, por ser el siguiente hacia arriba.
> *   C) Ninguno, hay que repetir el conteo.
> **Respuesta: B.** Según la lógica del Profe Alex, si el número exacto no está, se busca el valor que lo contiene (el que sigue).

> [ad-question] Pregunta 3
> Calcula el promedio de estos precios: \$2, \$5 y \$8 USD.
> *   A) \$4 USD.
> *   B) \$15 USD.
> *   C) \$5 USD.
> **Respuesta: C.** $(2+5+8) = 15$; $15 / 3 = 5$.

## 8. Notas para el próximo tema

> [!tip] 💡 En la próxima clase
> ¡No te lo pierdas! Vamos a ver **Datos agrupados por intervalos**. Usaremos la misma lógica de hoy, pero aprenderás a usar la **marca de clase** para representar a los grupos. ¡Allá nos vemos!

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]