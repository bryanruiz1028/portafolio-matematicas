# Clase 01 — Medidas de Posición: Cuartiles, Deciles y Percentiles

#algebra #quartilesintrod #estadistica #medidasposicion

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 2

> [!info] 🧭 Navegación
> - ⬅️ **Anterior**: [Introducción a la Estadística]
> - ➡️ **Siguiente**: [Interpretación de Percentiles y Diagramas de Caja]

---

## Relevancia y Aplicaciones

Las medidas de posición son herramientas fundamentales en estadística que permiten dividir un conjunto de datos ordenados en intervalos de igual tamaño. Su propósito es identificar qué ubicación ocupa un valor específico en la distribución, facilitando la comprensión de qué porcentaje de los datos es **igual o menor** a dicho valor.

- **💵 [USD]**: Se aplica para analizar la escala salarial en una empresa; por ejemplo, para determinar qué sueldo en dólares marca el límite del 25% de los empleados con menores ingresos.
- **🏗️ [Práctica]**: En el control de calidad industrial, permite establecer si el peso o resistencia de un material se encuentra dentro de los estándares aceptables del 90% de la producción.
- **📊 [Cotidiana]**: Se utiliza para interpretar resultados educativos o demográficos, como entender si la edad de un estudiante se sitúa en el tramo del 10% más joven de su clase.

---

## Concepto Clave

> [!note] 📌 ¿Qué son las Medidas de Posición?
> Son valores que dividen un conjunto de datos ordenados en partes porcentuales iguales. Imagina que cortas una cuerda en pedazos exactos:
> - **Cuartiles (Q)**: Dividen los datos en 4 partes (cada una es el 25%).
> - **Deciles (D)**: Dividen los datos en 10 partes (cada una es el 10%).
> - **Percentiles (P)**: Dividen los datos en 100 partes (cada una es el 1%).
> 
> **Equivalencia vital**: El Cuartil 2 ($Q_2$), el Decil 5 ($D_5$) y el Percentil 50 ($P_{50}$) representan exactamente el centro de la distribución, por lo que equivalen a la **mediana**.

> [!warning] ⚠️ Error común
> El error más grave es intentar calcular la posición sin haber **ordenado los datos de menor a mayor**. Sin orden, la posición hallada no representa ningún porcentaje real de la distribución.

> [!tip] 💡 Truco para recordarlo
> Asocia el nombre con la fracción del total: 
> - **Cuartil** = Cuarta parte ($\frac{1}{4}$ del total).
> - **Decil** = Décima parte ($\frac{1}{10}$ del total).
> - **Percentil** = Centésima parte ($\frac{1}{100}$ del total).

---

## Procedimiento Paso a Paso

```text
PASO 1: Ordenar los datos de menor a mayor.
PASO 2: Identificar el número total de datos (n).
PASO 3: Calcular la posición (Pos) según el tipo de medida:
        - Cuartiles:   Pos = (k * n) / 4   [o k*(n+1)/4 si n es impar]
        - Deciles:     Pos = (k * n) / 10
        - Percentiles:   Pos = (k * n) / 100
        (Donde 'k' es el número del cuartil, decil o percentil buscado).
PASO 4: Ubicar el valor. Si la posición es decimal (ej. 4.5), se promedian los 
        valores de las posiciones adyacentes (en este caso, posición 4 y 5).
```

---

## Ejemplos Prácticos

> [!example] Ejemplo 1: Caso Básico (Datos Impares)
> **Problema**: Hallar los cuartiles de las edades de 11 personas: 14, 15, 15, 15, 15, 16, 16, 16, 17, 17, 18.
> **Solución**:
> 1. $n = 11$. Usamos $Pos = k(n+1)/4$.
> 2. **Q1**: $Pos = 1(12)/4 = 3$. El dato en posición 3 es **15**.
> 3. **Q2**: $Pos = 2(12)/4 = 6$. El dato en posición 6 es **16**.
> 4. **Q3**: $Pos = 3(12)/4 = 9$. El dato en posición 9 es **17**.
> *Interpretación*: El 75% de las personas tienen una edad **igual o menor** a 17 años.

> [!example] Ejemplo 2: Caso Par (Promedio central)
> **Problema**: Hallar el $Q_2$ (mediana) de 10 edades: 14, 15, 15, 16, 17, 18, 18, 19, 19, 20.
> **Solución**:
> 1. $n=10$. La posición central se encuentra entre el dato 5 y el dato 6.
> 2. El dato en la posición 5 es **17** y en la posición 6 es **18**.
> 3. **Q2**: $(17 + 18) / 2 = \mathbf{17.5}$.

> [!example] Ejemplo 3: Caso Avanzado (Datos Agrupados en Intervalos)
> **Problema**: Hallar el Decil 2 ($D_2$) en una tabla de 60 personas (edades de 30 a 60 años).
> **Glosario técnico**: 
> - $L_i$: Límite inferior del intervalo.
> - $A$: Amplitud del intervalo (tamaño).
> - $F_{i-1}$: Frecuencia acumulada anterior.
> - $F_i$: Frecuencia acumulada del intervalo actual.
> 
> **Solución**:
> 1. **Posición**: $k \cdot n / 10 \rightarrow 2 \cdot 60 / 10 = 12$.
> 2. Buscamos el 12 en la frecuencia acumulada ($F_i$). Se encuentra en el intervalo $[40-45)$ porque allí la frecuencia sube de 10 a 22.
> 3. Datos: $L_i = 40$; $A = 5$; $F_{i-1} = 10$; $F_i = 22$.
> 4. **Fórmula**: $L_i + A \cdot \left[ \frac{\text{Pos} - F_{i-1}}{F_i - F_{i-1}} \right]$
> 5. **D2**: $40 + 5 \cdot \left[ \frac{12 - 10}{22 - 10} \right] = 40 + 5 \cdot (2/12) = \mathbf{40.83}$.

> [!example] Ejemplo 4: Aplicación USD
> **Problema**: Precios de 12 productos: $55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66. Hallar Q1, Q2 y Q3.
> **Solución ($n=12$)**:
> 1. **Q1**: Promedio entre posiciones 3 y 4: $(57+58)/2 = \mathbf{57.5}$ USD.
> 2. **Q2**: Promedio entre posiciones 6 y 7: $(60+61)/2 = \mathbf{60.5}$ USD.
> 3. **Q3**: Promedio entre posiciones 9 y 10: $(63+64)/2 = \mathbf{63.5}$ USD.

---

## Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Fácil
> 1. Hallar $Q_1$ en la serie: 10, 12, 13, 14, 15.
> 2. Hallar $Q_2$ en la serie: 20, 21, 24, 25, 28, 30.
> 3. Hallar $Q_3$ en la serie: 5, 7, 8, 9, 10, 11, 12.
> 4. Identificar el $Q_2$ en: 1, 2, 3, 4, 5, 6, 7.

> [!abstract] 🟡 Nivel Medio
> Usando la tabla de 60 estudiantes (edades 13 a 19):
> 1. Hallar el Decil 6 ($D_6$).
> 2. Hallar el Percentil 5 ($P_5$).
> 3. Hallar el Decil 7 ($D_7$).
> 4. Hallar el Percentil 52 ($P_{52}$).

> [!abstract] 🔴 Nivel Avanzado (USD)
> Con la tabla de 60 presupuestos agrupados (intervalos 30-60 USD, $A=5$):
> 1. Calcular el Cuartil 1 ($Q_1$).
> 2. Calcular el Percentil 55 ($P_{55}$).
> 3. Determinar el Decil 4 ($D_4$) para un análisis de costos.
> 4. Calcular el límite del 75% de los gastos ($Q_3$).

> [!success] ✅ Respuestas
> **Fácil**: 1. 12 | 2. 24.5 | 3. 11 | 4. 4.
> **Medio**: 1. 15 | 2. 13 | 3. 16 | 4. 15.
> **Avanzado**: 1. 42.08 USD | 2. 47.39 USD | 3. 45.43 USD | 4. 50 USD.

---

## Mini-Prueba de Autoevaluación

> [!question] Pregunta 1
> ¿A qué medida de tendencia central equivale exactamente el Cuartil 2 ($Q_2$)?
> **Respuesta**: Equivale a la Mediana.

> [!question] Pregunta 2
> Si en una serie sin agrupar el cálculo de posición resulta en un decimal como 2.5, ¿qué debemos hacer?
> **Respuesta**: Se debe buscar el valor intermedio (promedio) entre el dato en la posición 2 y el dato en la posición 3.

> [!question] Pregunta 3
> ¿Qué significa que un artículo de lujo esté en el Decil 9 ($D_9$) de precios en dólares?
> **Respuesta**: Significa que el 90% de los artículos similares tienen un precio **igual o menor** que ese valor.

---

> [!tip] 💡 En la próxima clase
> Analizaremos la interpretación profunda de los percentiles en grandes bases de datos y aprenderemos a visualizar estas medidas mediante los Diagramas de Caja (Boxplots).

> [!info] 🧭 Navegación
> - ⬅️ **Anterior**: [Introducción a la Estadística]
> - ➡️ **Siguiente**: [Interpretación de Percentiles y Diagramas de Caja]