# 📖 Guía de estudio — Clase 01: Medidas de Tendencia Central

¡Hola! Qué alegría saludarte. En esta guía vamos a explorar cómo encontrar el "corazón" de un conjunto de datos. No te preocupes si al principio parece un reto; con orden y práctica, te convertirás en un experto analizando información. ¡Vamos a darle con todo!

> [!info] 📌 Conceptos clave
> *   **El Centro de los Datos:** El objetivo es encontrar el valor típico o central que representa a todo un grupo.
> *   **Media ($\bar{x}$):** Es el promedio. Sumamos todos los valores y dividimos para el total de datos ($n$).
> *   **Mediana ($Me$):** ¡El orden es la clave! Es el valor justo en medio de los datos ordenados.
> *   **Moda ($Mo$):** Es el valor más popular, el que tiene mayor frecuencia (el que más se repite).

---

## 2. TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Media ($\bar{x}$)** | Promedio aritmético. Se obtiene con $\bar{x} = \frac{\sum x}{n}$. En tablas de frecuencia usamos: $\bar{x} = \frac{\sum (x \cdot f)}{n}$. El resultado siempre lleva la misma unidad que los datos (años, goles, etc.). |
| **Mediana ($Me$)** | Valor de la posición central. Divide al conjunto en dos partes iguales (50% arriba y 50% abajo). |
| **Moda ($Mo$)** | Es el dato (variable) que tiene la mayor frecuencia absoluta ($f$). |
| **Frecuencia ($f$)** | Número de veces que aparece un dato específico. |
| **Total de datos ($n$)** | Es la suma de todas las frecuencias absolutas ($\sum f$). |

---

## 3. EJEMPLOS RESUELTOS ADICIONALES

```ad-example
title: Ejemplo A: Goles por partido (Caso Básico - Impar)
**Enunciado:** Un equipo anotó estos goles en 15 partidos: 1, 0, 2, 5, 2, 1, 0, 2, 1, 3, 0, 4, 5, 4, 3.

**Paso a paso:**
1. **Ordenar los datos:** 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5.
2. **Calcular la Media ($\bar{x}$):** 
   - Suma total: $29$ goles.
   - $\bar{x} = 29 / 15 = 1,93$ goles.
3. **Identificar la Mediana ($Me$):** 
   - Como $n=15$ (impar), la posición es $(15+1)/2 = 8$. 
   - El dato en la **Posición 8** es el **2**. Así que, $Me = 2$ goles.
4. **Identificar la Moda ($Mo$):** 
   - El dato con mayor frecuencia es el **1** (se repite 4 veces). $Mo = 1$ gol.
```

```ad-example
title: Ejemplo B: Precios de productos escolares (Caso Par $)
**Enunciado:** Precios de 10 productos (en USD): $2, $5, $3, $10, $5, $12, $15, $7, $8, $15.

**Paso a paso:**
1. **Ordenar datos:** 2, 3, 5, 5, 7, 8, 10, 12, 15, 15.
2. **Calcular la Media ($\bar{x}$):**
   - Suma: $82$.
   - $\bar{x} = 82 / 10 = 8,2$ USD.
3. **Calcular la Mediana ($Me$):**
   - Como $n=10$ (par), no hay un solo centro. Buscamos las posiciones $n/2$ y el siguiente.
   - **Posición 5:** 7 USD.
   - **Posición 6:** 8 USD.
   - **¿Por qué dividimos?** Para encontrar el punto medio exacto entre los dos centros: $Me = (7 + 8) / 2 = 7,5$ USD.
4. **Identificar la Moda ($Mo$):**
   - El 5 y el 15 se repiten 2 veces. Es un caso **bimodal**. $Mo = 5$ y $15$ USD.
```

---

## 4. EJERCICIOS DE REPASO POR NIVELES

¡Ya casi lo tienes! Sigue practicando con estos ejercicios diseñados para fortalecer tu mente.

```ad-abstract
title: 🟢 Nivel: Fácil (Conceptos iniciales)
1. Calcula la media de las estaturas de 5 niños: 1.25m, 1.30m, 1.20m, 1.50m, 1.30m.
2. Halla la moda del siguiente conjunto de edades: {12, 15, 12, 13, 16, 12, 14}.
3. Un estudiante tiene las notas: 8, 9, 10, 7, 9. ¿Cuál es su promedio ($\bar{x}$)?
```

```ad-abstract
title: 🟡 Nivel: Medio (Tablas de Frecuencia)
Utiliza los datos exactos del "profe Alex" sobre el número de hermanos de 50 personas para completar la tabla y resolver:

| Hermanos ($x$) | Frecuencia ($f$) | Frecuencia Acumulada ($F$) |
| :---: | :---: | :---: |
| 0 | 5 | 5 |
| 1 | 12 | 17 |
| 2 | 10 | 27 |
| 3 | 8 | 35 |
| 4 | 10 | 45 |
| 5 | 5 | 50 |

*   **Ejercicio 1:** Encuentra la posición $n/2$ y determina la mediana ($Me$) buscando en la frecuencia acumulada ($F$).
*   **Ejercicio 2:** Identifica la moda ($Mo$) observando la frecuencia absoluta más alta.
```

```ad-abstract
title: 🔴 Nivel: Avanzado (Análisis y Rigor $)
Los ingresos diarios de un negocio durante una semana fueron: $50, $60, $55, $300, $65, $70, $55.

1. Calcula la **Media** y la **Mediana**.
2. **Pregunta de análisis:** Si el dueño quiere saber cuánto gana "normalmente" en un día común, ¿cuál medida representa mejor la realidad: la media o la mediana? Justifica considerando el dato de $300.
```

> [!check] Solucionario (Haz clic para ver)
> **Nivel Fácil:** 1) 1.31m. 2) 12 años. 3) 8.6.
> 
> **Nivel Medio:** 1) Posición $50/2 = 25$. En la frecuencia acumulada, el 25 está contenido en el 27. La **Mediana es 2 hermanos**. 2) La frecuencia más alta es 12, por tanto, la **Moda es 1 hermano**.
> 
> **Nivel Avanzado:** 1) Media $\approx$ $93.57; Mediana = $60. 2) La **Mediana** representa mejor la realidad. El valor de $300 es un **dato atípico** (outlier) que infla el promedio (media), haciendo parecer que se gana más de lo normal. La mediana no se deja afectar por valores extremos.

---

## 5. CONSEJO DE ESTUDIO

> [!tip] 💡 ¡El orden es tu mejor aliado!
> Como dice el **profe Alex**, nunca intentes calcular la mediana sin **ordenar los datos de menor a mayor** primero. Un truco infalible para no fallar en exámenes: al terminar de organizar tus datos o hacer tu tabla, cuenta cuántos números tienes. Si la suma de tus frecuencias ($f$) no coincide con el total de datos original ($n$), ¡revisa de nuevo! No queremos que ningún dato se quede fuera de la fiesta. ¡Tú puedes lograrlo!