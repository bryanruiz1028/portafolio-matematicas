# Clase 01 — Conceptos básicos de estadística | Población, muestra, dato, individuo

#algebra #conceptosbsicos

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 2

> [!info] 🧭 Navegación
> - Anterior: [[00 - Índice del curso]]
> - Siguiente: [[Clase 02 — Medidas de Dispersión y Tablas de Frecuencia]]

---

> [!info] 🌍 Relevancia y aplicaciones
> La estadística es una herramienta de las matemáticas que nos sirve para recopilar, organizar y analizar información para entender fenómenos y tomar decisiones basadas en la realidad.
> - 💵 Aplicación financiera ($USD): Se utiliza para analizar la evolución de los precios de productos y entender variaciones en el costo de vida.
> - 🏗️ Control de calidad: En la industria se emplea para medir piezas, como tornillos, asegurando que cumplan con los estándares requeridos.
> - 📊 Situaciones cotidianas: Permite organizar los resultados de encuestas sobre preferencias, como elegir el refrigerio favorito en un grupo escolar.

---

> [!note] 📌 ¿Qué es Conceptos básicos de estadística?
> La estadística es la ciencia que recolecta y estudia datos. Para trabajar en ella, es fundamental distinguir los siguientes términos:
> - Población: Es el conjunto de todos los individuos o elementos sobre los que se quiere realizar el estudio.
> - Individuo o unidad estadística: Es cada uno de los elementos que componen la población de forma independiente.
> - Muestra: Es un subgrupo pequeño y representativo seleccionado de la población, generalmente a quienes se les realiza la consulta directa.
> - Dato: Es cada uno de los valores o respuestas obtenidas en el estudio (una edad, una medida, una preferencia).
> - Moda: Es el valor o los valores que más veces se repiten dentro del conjunto de datos.
> 
> Tipos de Variables
> Las variables son las características que medimos y se clasifican en:
> 1. Cualitativas (Cualidades): Se expresan mediante palabras.
>    - Nominal: No admiten un orden específico (ej. color favorito, estado civil).
>    - Ordinal: Siguen un orden lógico o jerárquico (ej. medallas deportivas, primer apellido por orden alfabético, niveles de desempeño).
> 2. Cuantitativas (Cantidades): Se expresan mediante números.
>    - Discreta: Valores que se pueden contar con números enteros (ej. número de hermanos, cantidad de pantalones).
>    - Continua: Valores que pueden tomar infinitas posibilidades o requieren gran precisión (ej. el peso exacto de un balón, el tiempo de una carrera).

> [!warning] ⚠️ Error común
> Es importante no confundir la población con la muestra. La población representa a la totalidad de los sujetos posibles de estudio, mientras que la muestra se refiere únicamente a los sujetos que fueron seleccionados para obtener la información.

> [!tip] 💡 Truco para recordarlo
> Cuando intentes identificar una variable cuantitativa, asóciala con la pregunta ¿cuánto?. Si la respuesta es un número, la variable es cuantitativa.

---

### Procedimiento paso a paso

```text
1. Identificar elementos del estudio:
   - Definir la población (el grupo total de interés).
   - Definir la muestra (el grupo específico consultado).
   - Definir el dato (la naturaleza de la respuesta obtenida).

2. Calcular la Media (Promedio):
   - Sumar todos los valores de los datos.
   - Dividir el total de la suma entre el número total de datos (n).

3. Hallar la Mediana:
   - Ordenar todos los datos de menor a mayor.
   - Si n es impar: Seleccionar el valor que ocupa la posición central.
   - Si n es par: Localizar los dos valores centrales, sumarlos y dividirlos entre 2.

4. Encontrar Deciles:
   - Ordenar los datos de forma ascendente.
   - Aplicar la fórmula de posición: Posición = (K * n) / 10.
     * K es el decil buscado (1 al 9).
     * n es el número total de datos.
   - Si el resultado de la posición es decimal, se debe sumar los valores de las dos posiciones enteras más cercanas y dividir el resultado por 2.
```

---

### Bloque de ejemplos prácticos

> [!example] Ejemplo 1: Identificación básica
> En un estudio en Bogotá se consultó a 20 empresas sobre su número de empleados afiliados a seguridad social.
> - Población: Todas las empresas de la ciudad de Bogotá.
> - Muestra: Las 20 empresas que fueron seleccionadas para la encuesta.
> - Individuo: Una empresa de Bogotá.
> - Dato: El número de trabajadores reportado (ej. 7, 8, 10).

> [!example] Ejemplo 2: Cálculo de la Mediana (n par)
> Notas obtenidas por 6 estudiantes: 13, 14, 14, 15, 15, 16.
> 1. Los datos se encuentran ordenados.
> 2. Al ser 6 datos, los valores centrales están en la posición 3 y 4: (14 y 15).
> 3. Cálculo: (14 + 15) / 2 = 14.5.
> - Resultado: La mediana de las notas es 14.5.

> [!example] Ejemplo 3: Cálculo de Deciles
> En una lista de 20 notas ordenadas, calculamos la posición para el Decil 4 (D4) y el Decil 7 (D7).
> - Posición D4: (4 * 20) / 10 = 8. El valor en la octava posición es el D4.
> - Posición D7: (7 * 20) / 10 = 14. El valor en la posición catorce es el D7.

> [!example] Ejemplo 4: Media de precios ($USD)
> Precios registrados de 5 artículos: $15, $10, $16, $14, $17 USD.
> 1. Suma total: 15 + 10 + 16 + 14 + 17 = 72.
> 2. Promedio: 72 / 5 = 14.4.
> - Resultado: El precio medio es de $14.4 USD.

---

### Ejercicios para el estudiante

> [!abstract] 🟢 Nivel Fácil: Identificación de variables
> Determina el tipo de variable (Cualitativa Nominal, Cualitativa Ordinal, Cuantitativa Discreta o Cuantitativa Continua):
> 1. El color preferido de los alumnos de un curso.
> 2. El número de pantalones que tienen tus amigos en casa.
> 3. Las medallas entregadas en una competencia (Oro, Plata, Bronce).
> 4. El primer apellido de los compañeros de clase.

> [!abstract] 🟡 Nivel Medio: Media y Moda
> Calcula la media aritmética y la moda para los siguientes conjuntos:
> 1. Edades de amigos: 12, 15, 12, 13, 12, 14, 13.
> 2. Cantidad de hermanos: 1, 0, 2, 1, 1, 3.
> 3. Calificaciones: 4, 3, 5, 4, 2.
> 4. Faltas de asistencia: 0, 2, 1, 0, 0, 3, 0.

> [!abstract] 🔴 Nivel Avanzado: Medidas de posición ($USD)
> Resuelve los problemas de posición utilizando las fórmulas correspondientes:
> 1. Salarios mensuales en USD: $400, $450, $500, $550, $600, $700. Calcula la mediana.
> 2. Gastos de envío en USD: $10, $12, $15, $18, $20, $22, $25, $30, $35, $40. Halla el Decil 2 (D2).
> 3. Costos de suscripción en USD: $5, $5, $8, $10, $12, $15. Calcula la mediana.
> 4. Ahorros de 10 personas (datos ordenados de $50 a $200). Identifica el Decil 5 (D5).

> [!success] Respuestas para el docente
> Fácil:
> 1. Cualitativa Nominal.
> 2. Cuantitativa Discreta.
> 3. Cualitativa Ordinal.
> 4. Cualitativa Ordinal (debido al orden alfabético).
> 
> Medio:
> 1. Media: 13 | Moda: 12.
> 2. Media: 1.33 | Moda: 1.
> 3. Media: 3.6 | Moda: 4.
> 4. Media: 0.85 | Moda: 0.
> 
> Avanzado:
> 1. Mediana: $525 USD.
> 2. Posición 2: $12 USD.
> 3. Mediana: $9 USD.
> 4. El D5 corresponde a la mediana del conjunto.

---

### Mini-prueba de autoevaluación

> [!question] Pregunta 1
> Si una fábrica produce todos los balones de un lote pero solo se mide el peso de 500 de ellos, ¿cuál es la muestra?
> a) Todos los balones fabricados.
> b) Los 500 balones seleccionados.
> c) El peso de cada balón individual.
> d) El encargado de la medición.
> Respuesta correcta: b. La muestra es el grupo representativo que se toma para obtener los datos.

> [!question] Pregunta 2
> En el conjunto de datos par (10, 12, 14, 16), ¿cuál es el procedimiento para hallar la mediana?
> a) Elegir el número 14 por estar a la derecha.
> b) Promediar los valores centrales 12 y 14.
> c) Sumar todos los valores del conjunto.
> d) Buscar el valor que más se repite.
> Respuesta correcta: b. En conjuntos pares se debe promediar los dos datos que quedan en el centro.

> [!question] Pregunta 3
> Un estudiante organiza su presupuesto y gasta en almuerzos durante 4 días las siguientes cantidades: $5, $7, $5, $3 USD. ¿Cuál es el promedio de su gasto diario?
> a) $5 USD.
> b) $6 USD.
> c) $4 USD.
> d) $20 USD.
> Respuesta correcta: a. La suma de los gastos (20) dividida entre el número de días (4) da como resultado 5.

---

> [!tip] 💡 En la próxima clase
> Una vez comprendidos los conceptos básicos y las medidas de posición, avanzaremos hacia el estudio de las medidas de dispersión y la elaboración de tablas de frecuencia para analizar qué tan concentrados o alejados se encuentran los datos respecto al promedio.

> [!info] 🧭 Navegación
> - Anterior: [[00 - Índice del curso]]
> - Siguiente: [[Clase 02 — Medidas de Dispersión y Tablas de Frecuencia]]