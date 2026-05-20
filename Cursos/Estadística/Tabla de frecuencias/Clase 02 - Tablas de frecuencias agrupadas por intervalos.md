# Clase 02 — Tablas de frecuencias agrupadas por intervalos
tags: #algebra #frequencytableg
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 3

> [!info] 🧭 Navegación
> [[Clase 01 — Tablas de frecuencias simples]] | [[00 - Índice del curso]] | [[Clase 03 — Histogramas y Polígonos de Frecuencia]]

¡Qué tal amigas y amigos! Espero que estén muy bien. En esta clase vamos a aprender a organizar datos cuando tenemos muchísima información o valores muy diferentes entre sí. Aprender a agrupar es clave para que nuestras tablas no midan tres metros de largo y para que nuestros gráficos se entiendan a la primera.

> [!info] 🌍 Relevancia y aplicaciones
> Agrupar datos en intervalos es la estrategia fundamental para organizar grandes volúmenes de información que presentan muchos valores diferentes. Sin esta técnica, los gráficos serían ilegibles y el análisis de datos resultaría caótico y poco práctico.
> - 💵 **Aplicación $USD:** Análisis de precios de miles de productos en un supermercado para clasificarlos en rangos de costo (ej. productos de bajo costo vs. artículos de lujo).
> - 🏗️ **Aplicación Práctica:** Control de pesos en logística industrial, donde se agrupan las cargas en intervalos para optimizar la distribución en camiones o contenedores.
> - 📊 **Situación Cotidiana:** Organización de las edades de los asistentes a un concierto masivo para crear estrategias de marketing dirigidas a grupos específicos.

> [!note] 📌 Tablas de frecuencia agrupadas por intervalos
> Imagina que tienes muchísimos datos diferentes, como si tuvieras cientos de canicas de distintos tamaños regadas por el suelo. Si intentas contar cada tamaño por separado, nunca terminarías. Hacer una tabla por intervalos es como **"poner los datos en cajas o cajones"**. En lugar de anotar cada valor por separado, creas grupos (ej. "canicas de 1 a 3 cm") para que todo sea mucho más fácil de entender y manejar.

> [!warning] ⚠️ Error común
> El error más típico es contar un dato en dos cajas al mismo tiempo. Por ejemplo, si tienes un intervalo de 10 a 15 y otro de 15 a 20, ¿dónde pones el número 15? Usamos la regla del **intervalo semiabierto $[a, b)$**: el primer número (a la izquierda) **SÍ** se incluye en ese grupo (cerrado), pero el segundo (a la derecha) **NO** se incluye (abierto), sino que se cuenta en la fila de abajo. ¡El 15 siempre va a la caja donde él sea el número inicial!

> [!tip] 💡 Truco para recordarlo
> Para no olvidar el orden de los pasos iniciales, recuerda la palabra **"RAKI-A"**:
> 1. **RA**ngo (¿Qué tanto espacio ocupan mis datos?).
> 2. **K** (¿Cuántas filas o "cajones" voy a construir?).
> 3. **A**mplitud (¿Qué tan ancho es cada cajón?).

### Procedimiento Paso a Paso

```text
PASO 1 → Calcular el Rango (R = Dato_max - Dato_min).
PASO 2 → Determinar el número de intervalos (k) usando la Regla de Sturges: 
         k = 1 + 3.322 log(n). 
         REGLA: Redondear siempre al número IMPAR más cercano para mejor equilibrio.
PASO 3 → Calcular la Amplitud (A = R / k). 
         REGLA: Redondear siempre HACIA ARRIBA al entero siguiente para que no falte espacio.
PASO 4 → Definir los límites y la Marca de Clase (xi), que es el punto medio: (L_inferior + L_superior) / 2.
```

### Ejemplos Prácticos

> [!example] Ejemplo 1: Pesos de estudiantes (Caso Básico)
> Se analizan los pesos de 40 estudiantes ($n=40$):
> - **Cálculos:** $R = 53 - 33 = 20$. Por Sturges, $k = 1 + 3.322 \log(40) = 6.32$. Redondeamos al impar más cercano: **$k=7$**.
> - **Amplitud:** $A = 20 / 7 = 2.85$. Redondeamos hacia arriba: **$A=3$**.
> - **Resultado (Primera Fila):** 
>   Intervalo: $[33, 36)$ | Marca de Clase ($x_i$): $34.5$ | Frecuencia absoluta ($f_i$): $1$.
>   *(Nota: Como el rango total cubierto será $7 \times 3 = 21$, y nuestro rango real es 20, el último dato (53) quedará perfectamente guardado).*

> [!example] Ejemplo 2: Edades en centro comercial (Ajuste de Rango)
> Con 60 personas ($n=60$), el rango original es $R = 71 - 5 = 66$.
> - **Cálculos:** $k \approx 7$ y $A \approx 9.42$ (redondeado a **10**).
> - **El "Sobreado":** Al multiplicar $k \times A$ ($7 \times 10$), el "Nuevo Rango" ($R'$) es **70**. Como $70 - 66 = 4$, nos sobran 4 unidades.
> - **Ajuste:** Para que la tabla quede centrada y profesional, repartimos ese sobrante: restamos 2 al inicio y sumamos 2 al final.
> - **Inicio real:** Empezamos en **3** (en lugar de 5). Así, el último intervalo terminará en **73** (cubriendo el 71).
> - **⚠️ Nota vital:** Si no ajustas el rango o redondeas la amplitud hacia abajo, los datos más altos se quedarán "sin cajón" al final de la tabla.

> [!example] Ejemplo 3: ¿Cuándo usar intervalos? (Caso Avanzado)
> En el video vimos que si hay **más de 12 valores diferentes** (como en las velocidades de conductores), se DEBE usar intervalos. Si usas una tabla simple con 20 filas, el gráfico tendrá columnas flacas e ilegibles. Los intervalos sacrifican la precisión exacta de cada número (usando el promedio o Marca de Clase) para darnos una "foto" clara de la situación general.

> [!example] Ejemplo 4: Precios de suscripciones ($USD)
> Basado en las "Horas de lectura" ($n=50$) del video (datos de 0 a 25):
> - **Cálculos:** $R=25, k=7, A=4$.
> - **Intervalos y Frecuencias Absolutas ($f_i$):**
>   1. $[0, 4):$ **21**
>   2. $[4, 8):$ **17**
>   3. $[8, 12):$ **5**
>   4. $[12, 16):$ **3**
>   5. $[16, 20):$ **2**
>   6. $[20, 24):$ **1**
>   7. $[24, 28):$ **1**
> - **Análisis:** Gracias a la agrupación, vemos de un vistazo que la gran mayoría de clientes prefiere suscripciones de bajo costo (menos de $8 USD).

### Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Fácil: Teoría y Selección
> 1. Calcula el rango si el dato máximo es 100 y el mínimo es 15.
> 2. Tienes 18 valores diferentes en una encuesta. ¿Usas tabla simple o por intervalos?
> 3. ¿Qué sucede si redondeas la amplitud ($A$) hacia abajo?
> 4. Según la regla de los 12 valores, ¿es recomendable agrupar si solo tienes 5 valores distintos?

> [!abstract] 🟡 Nivel Medio: Cálculos Iniciales
> Tienes 15 edades: `10, 12, 15, 18, 20, 25, 30, 32, 35, 40, 42, 45, 48, 50, 22`.
> - Calcula el Rango ($R$).
> - Determina el número de intervalos ($k$) usando Sturges (redondea al impar más cercano).
> - Halla la Amplitud ($A$) necesaria.

> [!abstract] 🔴 Nivel Avanzado: Construcción $USD
> Precios de 20 acciones ($n=20$): `110, 150, 180, 200, 250, 300, 310, 350, 380, 400, 410, 450, 480, 495, 120, 220, 280, 330, 370, 440`.
> - Construye la tabla calculando $R, k$ y $A$.
> - Calcula para cada intervalo: Marca de Clase ($x_i$), Frecuencia Absoluta ($f_i$), Frecuencia Relativa ($h_i$) y Porcentaje.

> [!abstract] ✅ Respuestas
> **Fácil:** 1) $R=85$. 2) Intervalos. 3) Los datos mayores quedarían fuera. 4) No, se usa tabla simple.
> **Medio:** $R=40$. $k \approx 4.9 \rightarrow 5$. $A=8$.
> **Avanzado ($n=20$):** $R=385, k=5, A=77$.
> - $[110, 187): x_i=148.5, f_i=4, h_i=0.20, \%=20\%$
> - $[187, 264): x_i=225.5, f_i=3, h_i=0.15, \%=15\%$
> - $[264, 341): x_i=302.5, f_i=4, h_i=0.20, \%=20\%$
> - $[341, 418): x_i=379.5, f_i=5, h_i=0.25, \%=25\%$
> - $[418, 495]: x_i=456.5, f_i=4, h_i=0.20, \%=20\%$
>
> **Mini-prueba:** 1) b. 2) 7. 3) 20% ($10/50 = 0.20$).

### Mini-prueba de autoevaluación

> [!question] Pregunta 1
> ¿Cuál es el propósito principal de la variable $k$ en la Regla de Sturges?
> - a) Medir el promedio de los datos.
> - b) Definir el número de filas (intervalos) de la tabla.
> - c) Calcular la distancia entre el dato mayor y el menor.

> [!question] Pregunta 2
> Si tienes un Rango de 44 y necesitas 7 intervalos, ¿cuál es la amplitud exacta redondeada para tu tabla?
> *Cálculo:* $44 / 7 = 6.28$. La respuesta es: ________.

> [!question] Pregunta 3
> En un estudio de precios ($USD) con 50 datos, un intervalo tiene una frecuencia absoluta de 10. ¿Qué porcentaje del total representa?

---

> [!tip] 💡 En la próxima clase
> Ahora que sabemos organizar datos en "cajones", aprenderemos a darles vida visualmente. En la Clase 03 utilizaremos estas tablas para construir **Histogramas y Polígonos de Frecuencia**. ¡No se lo pierdan!

> [!info] 🧭 Navegación
> [[Clase 01 — Tablas de frecuencias simples]] | [[00 - Índice del curso]] | [[Clase 03 — Histogramas y Polígonos de Frecuencia]]