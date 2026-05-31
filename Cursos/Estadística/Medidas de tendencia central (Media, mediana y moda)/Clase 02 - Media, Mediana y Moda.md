# Clase 02 — Media, Mediana y Moda
tags: #algebra #mediamedianaymo

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 3

> [!info] 🧭 Navegación
> - ⬅️ Anterior: [[Clase 01 — Introducción a la Estadística]]
> - ➡️ Siguiente: [[Clase 03 — Medidas de Dispersión]]

---

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> Las medidas de tendencia central nos permiten resumir grandes conjuntos de datos en un solo valor representativo.
> 1. **Análisis de salarios:** Determinar el ingreso promedio en `$USD` de una población para medir su bienestar económico.
> 2. **Control de calidad en construcción:** Calcular la resistencia media de los materiales para garantizar la seguridad de una obra.
> 3. **Estudios demográficos:** Identificar la edad más frecuente (`$M_o$`) en una ciudad para decidir si construir más escuelas o centros de salud.

---

## Definiciones y Conceptos Clave

> [!note] 📌 ¿Qué es Media, Mediana y Moda?
> - **Media (Promedio):** Se representa como `$\bar{x}$`. Es el valor obtenido al sumar todos los datos y dividir el resultado entre el número total de datos (`$n$`).
> - **Mediana:** Se representa como `$M_e$`. Es el valor que se encuentra exactamente a la mitad de todos los datos cuando estos están ordenados.
> 	- Si `$n$` es **impar**: Es el dato central.
> 	- Si `$n$` es **par**: Es el promedio de los dos datos centrales.
> - **Moda:** Se representa como `$M_o$`. Es el valor o valores que más veces se repiten (el de mayor frecuencia).

> [!warning] ⚠️ Error común
> Un error frecuente es intentar hallar la `$M_e$` sin haber ordenado los datos. **Procedimiento correcto:** Siempre ordena de menor a mayor. Si los datos no están ordenados, la posición central no tendrá significado estadístico.

> [!tip] 💡 Truco para recordarlo
> Para no confundirlas, usa esta regla mnemotécnica: **"La moda es lo que más se acomoda"** (es decir, lo que más se ve o se repite).

---

## Síntesis de Procedimiento Paso a Paso

Para calcular estas medidas en **datos agrupados**, utilizaremos la técnica de la "casilla extra" para la sumatoria (`$\sum$`).

```markdown
PASO 1: Calcular la marca de clase ($x_i$) promediando los límites del intervalo.
PASO 2: Crear la columna de frecuencia acumulada ($F_i$) sumando progresivamente las $f_i$.
PASO 3: Crear la columna de producto ($x_i \cdot f_i$) y sumar todos sus valores ($\sum x_i \cdot f_i$).
PASO 4: Hallar la posición de la mediana ($n/2$) y buscarla en la frecuencia acumulada ($F_i$).
PASO 5: Identificar el intervalo modal (donde la frecuencia absoluta $f_i$ sea mayor).
PASO 6: Sustituir en las fórmulas de interpolación para hallar los valores exactos.
```

---

## Ejemplos Prácticos

### Ejemplo 1: Caso Básico (Datos sin agrupar)
**Datos:** Edades de 5 compañeros: 15, 16, 14, 17, 15.
1. **Media:** `$\bar{x} = \frac{15+16+14+17+15}{5} = \frac{77}{5} = 15.4$` años.
2. **Mediana:** Ordenamos: 14, 15, **15**, 16, 17. Como `$n=5$` (impar), el centro es `$15$`.
3. **Moda:** El valor `$15$` se repite dos veces. `$M_o = 15$`.

### Ejemplo 2: Caso con Datos Agrupados (Media)
**Contexto:** Edades de 20 personas (`$n=20$`).
- Intervalo [13-15): `$x_1=14, f_1=4 \rightarrow x_i \cdot f_i = 56$`
- Intervalo [15-17): `$x_2=16, f_2=9 \rightarrow x_i \cdot f_i = 144$`
- Intervalo [17-19): `$x_3=18, f_3=3 \rightarrow x_i \cdot f_i = 54$`
- Intervalo [19-21): `$x_4=20, f_4=3 \rightarrow x_i \cdot f_i = 60$`
- Intervalo [21-23): `$x_5=22, f_5=1 \rightarrow x_i \cdot f_i = 22$`
- **Sumatoria total (`$\sum x_i \cdot f_i$`):** `$336$`
- **Media:** `$\bar{x} = \frac{336}{20} = 16.8$` años.

### Ejemplo 3: Caso Avanzado (Mediana y Moda Agrupadas)
**Contexto:** `$n=130$` trabajadores (Horas trabajadas).
- **Posición Mediana:** `$n/2 = 65$`. Buscamos en `$F_i$` y seleccionamos el intervalo con `$L_i = 70, A = 5, F_{i-1} = 43, f_i = 50$`.
- **Fórmula de Mediana:** `$M_e = L_i + A \cdot \left( \frac{\frac{n}{2} - F_{i-1}}{f_i} \right)$`
- **Cálculo:** `$M_e = 70 + 5 \cdot \left( \frac{65 - 43}{50} \right) = 70 + 2.2 = 72.2$` horas.
- **Fórmula de Moda:** `$M_o = L_i + A \cdot \left( \frac{f_i - f_{i-1}}{(f_i - f_{i-1}) + (f_i - f_{i+1})} \right)$`
- **Cálculo:** `$M_o = 70 + 5 \cdot \left( \frac{50 - 20}{(50 - 20) + (50 - 17)} \right) = 72.38$` horas.

### Ejemplo 4: Aplicación Real ($USD)
Convertimos los pesos de 13 alumnos en precios de productos en una tienda:
`$40, $42, $45, $45, $45, $46, $47, $48, $48, $49, $49, $53, $56`.
- **Media:** `$\bar{x} = \frac{\sum \text{precios}}{13} = \frac{607}{13} = 46.69$` USD.
- **Moda:** El precio `$45` USD es el que más se repite (3 veces). `$M_o = 45$` USD.

---

## Ejercicios para el Estudiante

```ad-abstract
title: 🟢 Nivel Fácil (Datos sin agrupar)
1. Hallar la media de hermanos: 3, 1, 1, 0, 2, 2, 1, 0, 3.
2. Calcular la mediana del conjunto anterior (debes ordenar los 9 datos).
3. Determinar la moda del conjunto de hermanos.
4. Si un nuevo dato indica que un alumno tiene 10 hermanos, ¿qué medida se verá más afectada?
```

```ad-abstract
title: 🟡 Nivel Medio (Tablas de frecuencia)
1. Calcula la marca de clase ($x_i$) para un intervalo de precios entre $[50 - 60) USD$.
2. Si las frecuencias absolutas son $4, 10$ y $2$, ¿cuál es el valor de $n$?
3. Hallar la marca de clase para el intervalo $[80 - 85)$.
4. Si $x_i = 55$ y $f_i = 10$, ¿cuál es el valor de la casilla $x_i \cdot f_i$?
```

```ad-abstract
title: 🔴 Nivel Avanzado (Aplicación Financiera $USD)
1. Con $n=160$, posición $80$, $L_i=100$, $A=20$, $F_{i-1}=70$ y $f_i=20$, calcule la $M_e$ en $USD$.
2. En un intervalo con $L_i=50$, $f_i=10$, $f_{i-1}=4$, $f_{i+1}=2$ y $A=10$, calcule la $M_o$ en $USD$.
3. Si la $\sum x_i \cdot f_i = 8600 USD$ y $n=200$, ¿cuál es el precio promedio?
4. Determine la mediana si la posición $n/2$ coincide exactamente con un valor de $F_i$.
```

```ad-success
title: ✅ Resultados Numéricos
- **Fácil:** 1. `$\bar{x} = 1.44$`. 2. `$M_e = 1$`. 3. `$M_o = 1$`. 4. La media (sube a 2.3).
- **Medio:** 1. $55$. 2. $n = 16$. 3. $82.5$. 4. $550$.
- **Avanzado:** 1. `$110$` USD. 2. `$54.28$` USD. 3. `$43$` USD. 4. Es igual al límite superior del intervalo (porque ese valor acumula exactamente el 50% de los datos).
```

---

## Autoevaluación (Mini-prueba)

```ad-question
title: Pregunta 1
¿Cómo se denomina a una distribución que presenta dos valores diferentes con la misma frecuencia máxima?
**Respuesta:** Distribución **bimodal**. Si son más de dos, se llama multimodal.
```

```ad-question
title: Pregunta 2
¿Cómo se calcula técnicamente la amplitud ($A$) de un intervalo en una tabla?
**Respuesta:** Restando el límite inferior al límite superior ($L_s - L_i$). Por ejemplo, en $[15-17)$, $A = 17 - 15 = 2$.
```

```ad-question
title: Pregunta 3
Si un conjunto de 10 facturas suma 150 USD, ¿cuál es el promedio y qué símbolo lo representa?
**Respuesta:** El promedio es $15$ USD y se representa con el símbolo `$\bar{x}$`.
```

---

> [!tip] 💡 En la próxima clase
> Veremos las **Medidas de Dispersión**. Aprenderemos que el promedio no lo es todo; necesitamos saber qué tan "separados" están los datos de ese centro.

> [!info] 🧭 Navegación
> - ⬅️ Anterior: [[Clase 01 — Introducción a la Estadística]]
> - ➡️ Siguiente: [[Clase 03 — Medidas de Dispersión]]