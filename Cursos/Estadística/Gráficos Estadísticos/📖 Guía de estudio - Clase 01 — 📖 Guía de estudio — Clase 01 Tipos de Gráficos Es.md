# 📖 Guía de estudio — Clase 01: Tipos de Gráficos Estadísticos

> [!info] 📌 Conceptos clave
> ¡Qué tal, amigas y amigos! Antes de empezar a trazar líneas, es vital entender estos puntos para que sus gráficos hablen por sí solos:
> 1. **La organización es el primer paso:** Como siempre les digo, no podemos graficar si los datos no están en una tabla de frecuencias. ¡Un gráfico sin orden es un gráfico que miente!
> 2. **Datos agrupados puntualmente:** Se usan para variables cualitativas (colores, gustos) o cuantitativas discretas (pocos datos numéricos). Aquí usamos el **Gráfico de Barras** con las barras siempre separadas.
> 3. **Datos agrupados por intervalos:** Ideales para muchos datos o variables continuas (como la masa corporal). En este caso, usamos el **Histograma**, donde las barras van obligatoriamente pegadas.
> 4. **Preferencia por los límites:** Aunque en el eje horizontal del histograma puedes usar la Marca de Clase, yo les recomiendo usar los **límites inferiores y superiores**. ¡Se entiende mucho mejor para cualquier persona que vea tu trabajo!
> 5. **Claridad ante todo:** El objetivo es que alguien vea tu gráfico y lo entienda sin que tú estés ahí para explicarlo. ¡No olvides nombrar tus ejes!

---

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Gráfico de Barras** | Diagrama con barras rectangulares separadas. Se usa para datos cualitativos o discretos. |
| **Histograma** | Gráfico con barras unidas o pegadas. Representa datos agrupados en intervalos. |
| **Frecuencia Absoluta** | Es el número de veces que se repite un dato o la cantidad de elementos en un intervalo. |
| **Intervalos** | Rangos de valores con un límite inferior ($L_i$) y uno superior ($L_s$). |
| **Marca de Clase ($M_c$)** | Es el punto medio del intervalo. Se calcula así: $M_c = \frac{L_i + L_s}{2}$ |

---

## Ejemplos resueltos adicionales

> [!example] Ejemplo A — Construcción de Gráfico de Barras
> **Contexto:** Analizamos las edades de un grupo de estudiantes:
> * 13 años: 6 estudiantes
> * 14 años: 11 estudiantes
> * 15 años: 8 estudiantes
>
> **Paso 1: Dibujar ejes y nombrar variables.** Trazamos el eje horizontal para la "Edad (años)" y el vertical para el "Número de personas". ¡Ojo! Si no pones los nombres, nadie sabrá de qué hablas.
> **Paso 2: Establecer escala uniforme.** Como el máximo es 11, usaremos una escala de 2 en 2 (0, 2, 4, 6, 8, 10, 12). No escribas solo el 6, el 11 y el 8 en el eje; eso deforma el gráfico.
> **Resultado:** Dibujamos barras de igual ancho. La de 14 años llegará justo a la mitad entre el 10 y el 12. **Importante:** Las barras deben estar separadas para que sea un gráfico de barras correcto.

> [!example] Ejemplo B — Interpretación de Gastos en Viajes
> **Contexto:** Un gráfico muestra el presupuesto de una empresa en miles de dólares ($USD).
> * **Año 2019:** 470 (etiquetado en miles)
> * **Año 2020:** 84 (etiquetado en miles)
>
> **Pregunta:** ¿Cuál es la diferencia real de gasto entre ambos años?
> **Análisis:** No te dejes engañar por los números pequeños. El gráfico dice "en miles", así que 470 representa $470,000 USD y 84 representa $84,000 USD.
> **Cálculo:** $470,000 - 84,000 = 386,000$.
> **Resultado:** La diferencia es de **$386,000 USD**. En el 2020 se gastaron 386 mil dólares menos que en el 2019. ¡Siempre lee las etiquetas de los ejes!

---

## Ejercicios de repaso

> [!abstract] 🟢 Fácil
> **Responde con precisión:**
> 1. ¿Cuál es la característica física obligatoria que diferencia a un histograma de un gráfico de barras?
>    * a) El color de las barras.
>    * b) Que en el histograma las barras están pegadas y en el de barras están separadas.
>    * c) El grosor de los ejes.
> 2. Si las barras de tu gráfico están separadas, ¿qué tipo de datos estás representando?
>    * a) Datos agrupados por intervalos.
>    * b) Datos cualitativos o discretos puntuales.
> 3. En un histograma, ¿qué indica que las barras estén pegadas?
>    * a) Que los datos son continuos y siguen un orden de intervalos.
>    * b) Que se acabó el espacio en el papel.

> [!abstract] 🟡 Medio
> **Analiza la siguiente tabla de "Masa Corporal en kg" y responde:**
>
> | Intervalo (kg) | Frecuencia (Estudiantes) |
> | :--- | :--- |
> | [33 - 36) | 1 |
> | [36 - 39) | 9 |
> | [39 - 42) | 14 |
>
> 1. Calcula la **Marca de Clase ($M_c$)** del tercer intervalo: \_\_\_\_\_\_\_\_\_\_\_\_.
> 2. Si dibujas el histograma, ¿qué altura exacta debe tener la barra del segundo intervalo? \_\_\_\_\_\_\_\_\_\_\_\_.

> [!abstract] 🔴 Avanzado — Aplicación con $USD
> **Usa los siguientes datos de "Ingresos Mensuales" (en miles de $USD) para resolver:**
> * Ene: 100 | Feb: 120 | Mar: 150 | Abr: 180 | May: 180 | Jun: 120
>
> 1. **Cálculo de Trimestre:** ¿A cuánto asciende el total de ingresos del primer trimestre (Ene, Feb, Mar)? Expresa el resultado en dólares completos (sin usar la palabra "miles").
> 2. **Análisis de Metas:** Siguiendo la lógica de interpretación, ¿en cuántos meses de este semestre los ingresos fueron **estrictamente mayores** a $150,000 USD?

---

> [!tip] 💡 Consejo de estudio
> ¡Mucho cuidado con este error! Es el más común: muchos estudiantes escriben en el eje vertical solamente los números de las frecuencias que tienen en su tabla (por ejemplo, poner el 1, luego el 9 y luego el 14 pegaditos). **¡No lo hagas!**
> Para que el gráfico no sea engañoso, debes mantener una **escala uniforme**. Si decides ir de 3 en 3 (3, 6, 9, 12, 15...), respeta esa distancia siempre. Así, la diferencia de altura entre las barras mostrará la realidad de los datos. ¡Espero que este consejo les sirva mucho!