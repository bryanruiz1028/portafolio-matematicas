# Clase 02 — Cuartiles, Deciles y Percentiles en Datos Agrupados

#algebra #cuartilesdecile

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 2

> [!info] 🧭 Navegación
> - **Anterior:** [[Clase 01 — Introducción a las Medidas de Posición]]
> - **Siguiente:** [[Clase 03 — Interpretación y Gráficos Boxplots]]

---

> [!info] 🌍 Relevancia y aplicaciones
> Dividir un conjunto de datos en grupos con la misma cantidad de elementos es vital para entender grandes poblaciones. ¡Es más fácil de lo que parece! Nos permite ubicar con precisión dónde se encuentra un individuo respecto al grupo total.
> 
> - **Finanzas:** Identificar qué salario en `$USD` separa al 25% de los empleados con menores ingresos del resto para ajustar políticas salariales.
> - **Ingeniería y Construcción:** Analizar la distribución de medidas de resistencia en materiales; por ejemplo, asegurar que el Decil 9 (el 90%) cumpla con los estándares.
> - **Vida Diaria:** Determinar si una nota escolar sitúa a un estudiante en el 10% superior de su clase o analizar la distribución de pesos en una población.

---

> [!note] 📌 ¿Qué es Cuartiles, Deciles y Percentiles?
> Imagina que tienes una fila de personas ordenadas de la más pequeña a la más alta y quieres repartir dulces en grupos iguales:
> - Los **Cuartiles** dividen la fila en **4 partes** (25% cada una).
> - Los **Deciles** la dividen en **10 partes** (10% cada una).
> - Los **Percentiles** la dividen en **100 partes** (1% cada una).

> [!warning] ⚠️ Error común
> ¡Mucho ojo! El resultado que obtienes al calcular la **posición** ($k \cdot n / 4, 10, 100$) **no es el valor de la medida**. Es simplemente el "número de asiento" o ubicación que debes buscar en la columna de **Frecuencia Absoluta Acumulada** ($F_i$) para saber en qué intervalo se encuentra el dato.

> [!tip] 💡 Truco para recordarlo
> - **D**ecil empieza con **D** de **Diez**.
> - **P**ercentil empieza con **P** de **Porcentaje** (y los porcentajes siempre se calculan sobre **Cien**).

---

## Procedimiento Técnico (Cálculo)

Para hallar cualquier medida de posición, ¡no te asustes por la fórmula! Solo sigue estos 4 pasos de forma estructurada:

```text
PASO 1: Calcular la POSICIÓN usando (k * n / divisor). 
        (Divisor: 4 para Cuartiles, 10 para Deciles, 100 para Percentiles).
PASO 2: Ubicar ese número en la columna de Frecuencia Absoluta Acumulada (Fi).
PASO 3: Identificar los datos del intervalo: Límite inferior (Li), Amplitud (A), 
        Frecuencia anterior (Fi-1) y Frecuencia absoluta acumulada (Fi).
PASO 4: Aplicar la fórmula de INTERPOLACIÓN: 
        Medida = Li + A * [(Posición - Fi-1) / (Fi - Fi-1)]
```

> [!abstract] Nota Didáctica
> En el denominador de la fórmula, la resta $(F_i - F_{i-1})$ es exactamente igual a la **frecuencia absoluta** del intervalo ($f_i$). ¡Usa la que te resulte más cómoda!

---

## Ejemplos Prácticos

> [!example] Ejemplo 1: Cuartil 1 ($Q_1$) - Edades ($n=60$)
> Basado en el estudio de edades de 60 personas:
> 1. **Posición:** $1 \cdot 60 / 4 = 15$.
> 2. Buscamos 15 en **Frecuencia Acumulada**. Está entre 10 y 22.
> 3. **Datos:** $L_i = 40$, $A = 5$, $F_{i-1} = 10$, $F_i = 22$.
> 4. **Cálculo:** $40 + 5 \cdot [(15 - 10) / (22 - 10)] = 40 + 5 \cdot (5 / 12) = 40 + 2.08$.
> **Resultado:** **42.08 años**. ¡Ya lo tienes!

> [!example] Ejemplo 2: Decil 2 ($D_2$) - Respuestas de Examen ($n=100$)
> En un examen con 100 alumnos:
> 1. **Posición:** $2 \cdot 100 / 10 = 20$.
> 2. Buscamos 20 en $F_i$. Se encuentra en el intervalo donde $F_{i-1} = 14$ y $F_i = 39$.
> 3. **Datos:** $L_i = 20$, $A = 10$.
> 4. **Cálculo:** $20 + 10 \cdot [(20 - 14) / (39 - 14)] = 20 + 10 \cdot (6 / 25) = 20 + 2.4$.
> **Resultado:** **22.4 respuestas correctas**.

> [!important] Ejemplo 3: Caso Especial (Coincidencia Exacta)
> ¿Qué pasa si la posición calculada aparece **exactamente** en la columna $F_i$? Por ejemplo, al calcular el **Percentil 71** ($P_{71}$), la posición es 71 y este valor ya está en la tabla.
> - **¡Buenas noticias!** Puedes saltarte la fórmula de **interpolación**.
> - El resultado es simplemente el **Límite Superior** del intervalo correspondiente.
> - Debido a que los datos se acumulan exactamente en ese borde, el resultado es **40**.

> [!example] Ejemplo 4: Aplicación en Precios ($USD$)
> Analizando los precios de 100 productos (usando la misma estructura de intervalos del examen anterior):
> 1. **Posición del $P_{40}$:** $40 \cdot 100 / 100 = 40$.
> 2. Ubicamos 40 en $F_i$. Supera al 39, por lo que entra en el siguiente rango.
> 3. **Datos:** $L_i = 30$, $A = 10$, $F_{i-1} = 39$, $F_i = 71$.
> 4. **Cálculo:** $30 + 10 \cdot [(40 - 39) / (71 - 39)] = 30 + 10 \cdot (1 / 32) = 30 + 0.31$.
> **Resultado:** **30.3 $USD$**. Esto significa que el 40% de los productos cuestan 30.3 $USD$ o menos.

---

## Rango Intercuartílico (IQR)

El **Rango Intercuartílico** es una medida de dispersión que nos indica qué tan alejados están los datos en el 50% central de la población. Se obtiene restando el Cuartil 3 y el Cuartil 1.

Usando los datos del ejemplo de edades:
- $Q_3 = 50$
- $Q_1 = 42.08$
- **$IQR = 50 - 42.08 = 7.92$**

---

## Ejercicios y Autoevaluación

> [!abstract] Nivel Fácil: Cálculo de Posiciones
> Determina únicamente la posición ($k \cdot n / \text{divisor}$) para:
> 1. $Q_2$ con $n=80$.
> 2. $D_7$ con $n=100$.
> 3. $P_{25}$ con $n=200$.

> [!abstract] Nivel Medio: Pesos ($n=50$)
> En una tabla de pesos de 50 personas, halla el valor del $Q_2$ (Mediana). La posición calculada es 25. Al revisar la tabla, observas que el valor 25 aparece exactamente en la **frecuencia acumulada** de un intervalo que va de 50 a 60 kg. ¿Cuál es el valor del cuartil?

> [!abstract] Nivel Avanzado: Contexto Financiero ($USD$)
> Una empresa analiza los ingresos de 100 empleados. Al calcular el Percentil 71 ($P_{71}$), la posición resulta ser 71. Si en la tabla de frecuencias el valor 71 coincide con el $F_i$ del intervalo $[30, 40)$, ¿cómo interpretas este resultado en dólares?

> [!success] Respuestas para el docente
> - **Fácil:** 1) 40, 2) 70, 3) 50.
> - **Medio:** $Q_2 = 60$ kg. Al haber coincidencia exacta con $F_i$, el resultado es el límite superior.
> - **Avanzado:** $P_{71} = 40$ $USD$. El 71% de los empleados gana 40 $USD$ o menos. ¡Excelente análisis!

### Mini-prueba de autoevaluación
1. **Si la posición calculada es 45 y en la columna $F_i$ aparece exactamente el 45:**
   - a) Se debe aplicar obligatoriamente la fórmula de interpolación.
   - b) El resultado es automáticamente el Límite Superior del intervalo.
   - c) El resultado es el promedio de los límites.

2. **Para calcular el Decil 5 ($D_5$), ¿qué divisor debes usar en la fórmula de posición?**
   - a) 4
   - b) 100
   - c) 10

3. **Interpretación financiera: Si el $P_{10}$ de precios de un catálogo es $15$ $USD$, significa que:**
   - a) Solo el 10% de los productos son caros (cuestan más de $15$ $USD$).
   - b) El 10% de los productos tienen un precio de $15$ $USD$ o menos.
   - c) El precio más repetido es $15$ $USD$.

*(Respuestas: 1-b, 2-c, 3-b)*

---

> [!tip] 💡 En la próxima clase
> ¡Felicidades por completar esta lección! Ahora que dominas el cálculo de estas medidas, aprenderemos a visualizarlas de forma profesional. En la siguiente clase construiremos **Boxplots (Diagramas de Caja y Bigotes)** para comparar distribuciones como todo un experto. ¡Nos vemos allí!

> [!info] 🧭 Navegación
> - **Anterior:** [[Clase 01 — Introducción a las Medidas de Posición]]
> - **Siguiente:** [[Clase 03 — Interpretación y Gráficos Boxplots]]