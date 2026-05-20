# Clase 02 — Medidas de Dispersión y Posición: Varianza, Desviación Estándar, Desviación Media y Cuartiles
tags: #algebra #varianceandstan #estadistica
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 2

> [!info] 🧭 Navegación
> [[Clase 01 — Medidas de Tendencia Central]] | [[00 - Índice del curso]]

> [!info] 🌍 Relevancia y aplicaciones
> Estas medidas nos permiten entender qué tan agrupados o "desparramados" están los datos respecto al promedio central. No basta con saber el promedio; necesitamos saber si los datos son constantes o muy variables.
> 
> *   💵 **$USD**: Permiten comparar si los precios de un producto son estables en diferentes tiendas o si cambian drásticamente.
> *   🏗️ **Práctica**: En la industria, se usan para el control de calidad, asegurando que las piezas no varíen más de lo permitido.
> *   📊 **Cotidiana**: Ayudan a ver si las notas de un examen fueron similares para todos o si hubo extremos muy marcados (notas muy altas y muy bajas).

> [!note] 📌 ¿Qué son la Varianza y la Desviación Estándar?
> Imagina que el promedio es el "centro de una habitación". La **varianza** y la **desviación estándar** nos indican qué tan lejos se han movido los números de ese centro. Si los valores son pequeños, los datos están cerca del promedio; si son grandes, están muy dispersos.
> 
> Por otro lado, los **cuartiles** son los tres puntos de corte que dividen un conjunto de datos ordenados en cuatro grupos iguales. Cada uno marca un límite acumulado: el **Q1** representa el 25% de los datos, el **Q2** el 50% (la mediana) y el **Q3** el 75%.

> [!warning] ⚠️ Error común
> Un error muy frecuente es calcular la varianza y olvidar elevar las restas al cuadrado, o bien, obtener la varianza y olvidar sacar la raíz cuadrada para hallar la desviación estándar. Recuerda: la varianza se expresa en unidades al cuadrado (ej. $kg^2$), mientras que la desviación estándar regresa a la unidad original (ej. $kg$).

> [!tip] 💡 Truco para recordarlo
> **"Cuartiles = Cortes de una pizza"**: Para dividir una pizza en 4 pedazos iguales (cuartos), solo necesitas hacer 3 cortes. Por eso existen 3 cuartiles (Q1, Q2, Q3) para generar 4 grupos de información.

---

### Procedimiento paso a paso

```text
PASO 1 → Ordenar los datos de menor a mayor (indispensable para cuartiles).
PASO 2 → Calcular la Media Aritmética (promedio).
PASO 3 → Calcular desviaciones: Restar cada dato menos la media (x - promedio).
PASO 4 → Aplicar la fórmula correspondiente:
         • Desviación Media: Promediar los VALORES ABSOLUTOS de las restas.
         • Varianza (Población): Dividir la suma de cuadrados entre 'N'.
         • Varianza (Muestra): Dividir la suma de cuadrados entre 'n - 1'.
PASO 5 → Desviación Estándar: Calcular la raíz cuadrada de la varianza.
```

---

### Ejemplos Prácticos

> [!example] Ejemplo 1: Caso Básico - Cuartiles
> **Datos (Edades de 11 personas):** 14, 15, 15, 15, 15, 16, 16, 16, 17, 17, 18.
> 1. **Q2 (Mediana):** Como hay 11 datos (impar), la posición central es la 6. El valor es $16$.
> 2. **Q1:** Observamos los 5 datos a la izquierda de la mediana (14, 15, 15, 15, 15). El centro es $15$.
> 3. **Q3:** Observamos los 5 datos a la derecha de la mediana (16, 16, 17, 17, 18). El centro es $17$.
> *Interpretación: El 25% de las personas tiene 15 años o menos; el 50% tiene 16 años o menos; el 75% tiene 17 años o menos.*

> [!example] Ejemplo 2: Caso con Signos - Desviación Media
> **Datos (5 edades):** 12, 13, 12, 14, 15.
> 1. **Promedio:** $\bar{x} = \frac{12+13+12+14+15}{5} = \frac{66}{5} = 13.2$.
> 2. **Desviaciones Absolutas:**
>    - $|12 - 13.2| = 1.2$
>    - $|13 - 13.2| = 0.2$
>    - $|12 - 13.2| = 1.2$
>    - $|14 - 13.2| = 0.8$
>    - $|15 - 13.2| = 1.8$
> 3. **Cálculo:** Suma de desviaciones $= 1.2 + 0.2 + 1.2 + 0.8 + 1.8 = 5.2$.
> 4. **Resultado:** $D_m = \frac{5.2}{5} = \mathbf{1.04}$.

> [!example] Ejemplo 3: Caso Avanzado - Varianza y Desviación Estándar (Población)
> **Datos (5 niños):** 5, 6, 6, 7, 8.
> 1. **Promedio:** $\bar{x} = 6.4$.
> 2. **Varianza ($\sigma^2$):**
>    - $(5 - 6.4)^2 = 1.96$
>    - $(6 - 6.4)^2 = 0.16$
>    - $(6 - 6.4)^2 = 0.16$
>    - $(7 - 6.4)^2 = 0.36$
>    - $(8 - 6.4)^2 = 2.56$
>    - **Suma de cuadrados:** $5.2$.
>    - **Varianza:** $\sigma^2 = \frac{5.2}{5} = \mathbf{1.04}$.
> 3. **Desviación Estándar ($\sigma$):** $\sigma = \sqrt{1.04} = \mathbf{1.01}$.

> [!example] Ejemplo 4: Aplicación Real en $USD (Muestra)
> **Datos (Precios de suscripción):** $52, $55, $58.
> 1. **Promedio:** $\bar{x} = 55 \text{ USD}$.
> 2. **Varianza Muestral ($s^2$):** Al ser una muestra, dividimos por $n-1 = 2$.
>    - $\frac{(52-55)^2 + (55-55)^2 + (58-55)^2}{3-1} = \frac{9 + 0 + 9}{2} = \frac{18}{2} = \mathbf{9 \text{ USD}^2}$.
> 3. **Desviación Estándar ($s$):** $s = \sqrt{9} = \mathbf{3 \text{ USD}}$.
> *Nota: Este cálculo se realizó bajo el criterio de **Muestra** ($n-1$).*

---

### Ejercicios para el Estudiante

> [!abstract] Actividades de práctica
> 🟢 **Fácil**: Calcula Q1, Q2 y Q3 para la siguiente serie de edades: $12, 14, 15, 16, 18, 20, 22$.
> 
> 🟡 **Medio**: Se registra el número de hermanos de 6 personas: $0, 1, 1, 2, 2, 3$. Calcula la Desviación Media.
> 
> 🔴 **Avanzado**: Los precios de 4 laptops son: $400, $420, $380, $410. Calcula la Varianza y la Desviación Estándar tratándolos como una **muestra**.

> [!success] Respuestas
> *   **Fácil**: $Q1 = 14$; $Q2 = 16$; $Q3 = 20$.
> *   **Medio**: Promedio $\bar{x} = 1.5$. Suma de desviaciones absolutas: $|0-1.5| + |1-1.5| + |1-1.5| + |2-1.5| + |2-1.5| + |3-1.5| = 1.5 + 0.5 + 0.5 + 0.5 + 0.5 + 1.5 = 5.0$. Desviación Media: $D_m = \frac{5}{6} \approx \mathbf{0.83 \text{ hermanos}}$.
> *   **Avanzado**: 
>     - Promedio: $\bar{x} = 402.5 \text{ USD}$.
>     - Varianza Muestral ($s^2$): $\frac{(400-402.5)^2 + (420-402.5)^2 + (380-402.5)^2 + (410-402.5)^2}{4-1}$.
>     - $s^2 = \frac{6.25 + 306.25 + 506.25 + 56.25}{3} = \frac{875}{3} \approx \mathbf{291.67 \text{ USD}^2}$.
>     - Desviación Estándar ($s$): $\sqrt{291.67} \approx \mathbf{17.07 \text{ USD}}$.

---

### Mini-prueba de autoevaluación

> [!question] ¿Cuánto has aprendido?
> 1. **¿Qué cuartil coincide siempre con la mediana (el 50% de los datos)?**
>    - a) Q1 | b) Q2 | c) Q3 | d) Q4
> 2. **Si la varianza de un conjunto de pesos es $9 \text{ kg}^2$, ¿cuál es la desviación estándar?**
>    - a) $81 \text{ kg}$ | b) $4.5 \text{ kg}$ | c) $3 \text{ kg}$ | d) $9 \text{ kg}$
> 3. **Si los precios en dólares tienen una desviación estándar de $0$, ¿qué significa?**
>    - a) Son muy caros | b) Todos los precios son iguales | c) Hubo mucha inflación | d) Faltan datos

---

> [!tip] 💡 En la próxima clase
> Llevaremos estos conceptos al siguiente nivel: aprenderemos a aplicar estas fórmulas en **tablas de frecuencias y datos agrupados**, esenciales para manejar grandes volúmenes de información.

> [!info] 🧭 Navegación
> [[Clase 01 — Medidas de Tendencia Central]] | [[00 - Índice del curso]]