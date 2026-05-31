# Clase 02 — Gráficos Estadísticos: Circulares, Cajas y Bigotes, y Tallos y Hojas

#algebra #cmohacerungrfic

> [!info] 🧭 Navegación
> ◀ **Anterior:** [Clase 01 — Tablas de Frecuencia](link_placeholder)
> 🟢 **Actual:** Clase 02 — Gráficos Estadísticos
> ▶ **Siguiente:** [Clase 03 — Medidas de Tendencia Central](link_placeholder)

---

> [!info] 🌍 Relevancia y aplicaciones
> ¡Qué tal, amigas y amigos! Estos gráficos son herramientas poderosas para "hacer hablar" a los números. Nos permiten ver de un solo vistazo cómo se distribuyen los datos y comparar grupos de forma ultrarrápida sin leer largas tablas.
> 
> *   **💵 Aplicación USD:** Analiza tus presupuestos familiares; verás qué "rebanada" de tus ingresos se va en renta o comida.
> *   **🏗️ Aplicación práctica:** En construcción, un diagrama de cajas revela si la resistencia de los materiales es constante o si hay lotes defectuosos.
> *   **📊 Situación cotidiana:** Es el estándar para presentar resultados de encuestas de opinión y preferencias del consumidor.

---

> [!abstract] 📌 Conceptos Clave para el Éxito
> *   **Gráfico Circular:** Imagínalo como una **pizza**. Cada porción representa una parte del total. Es ideal para mostrar porcentajes.
> *   **Diagrama de Cajas (Boxplot):** Es un resumen visual de 5 números que nos dice dónde se "amontona" la gente y qué tan dispersos están los datos.
> *   **Tallos y Hojas:** Es una forma de organizar una lista que acaba pareciendo un gráfico de barras, ¡pero sin perder ni un solo dato original!
> 
> **⚠️ Error común:** ¡Cuidado! Muchos estudiantes intentan graficar el porcentaje directamente como si fueran grados. Recuerda: el transportador mide grados, no porcentajes. Debes hacer la conversión a 360°.
> 
> **💡 El Truco del Reloj:** Piensa en la circunferencia como un **reloj de 360 grados**. Para pasar de porcentaje a grados, usa la **Regla de Tres**: si el 100% son 360°, entonces tu porcentaje "X" es igual a $(X \times 360) / 100$.
> 
> **🧐 Nota de Experto sobre Atípicos:** Un dato es **atípico leve** si supera $1.5 \times RIC$. Pero si el dato es realmente exagerado (supera $3 \times RIC$), se le llama **atípico extremo**. ¡Márcalos siempre con un asterisco fuera de los bigotes!

---

> [!tip] 🛠️ Procedimientos Paso a Paso
> 
> **1. Gráfico Circular (El método del transportador)**
> 1. Organiza tus datos y obtén el porcentaje ($h_i \%$).
> 2. Aplica la fórmula del ángulo: $\alpha = \frac{\% \times 360}{100}$.
> 3. Dibuja un círculo y traza un **radio inicial** (una línea del centro al borde).
> 4. **Consejo de oro:** Pon el centro del transportador en el centro del círculo y el 0° sobre tu radio. Marca el ángulo, traza la línea y ¡listo! Para el siguiente, **rota tu transportador** usando la nueva línea como tu nuevo "cero".
> 
> **2. Boxplot (Datos No Agrupados)**
> 1. Ordena de menor a mayor.
> 2. Identifica los "5 magníficos": Mínimo, Q1, Q2 (Mediana), Q3 y Máximo.
> 3. **Lógica de Cuartiles:** La Mediana (Q2) parte los datos en dos. El Q1 es la mediana de la primera mitad y el Q3 es la mediana de la segunda mitad.
> 
> **3. Boxplot (Datos Agrupados)**
> 1. Calcula la posición: $Pos = \frac{k \times n}{4}$.
> 2. Busca esa posición en la frecuencia acumulada ($F_i$).
> 3. **Tip del Profe Alex:** Si no encuentras el número exacto en $F_i$, toma el **inmediato superior**. Si lo encuentras exacto, promedia ese dato con el siguiente.
> 
> **4. Tallos y Hojas (El orden perfecto)**
> 1. Define la **hoja** como la última cifra del número. El resto es el **tallo**.
> 2. **Para decimales:** Si tienes $1.5$ y $1.75$, completa el primero como $1.50$. Así, el tallo es $1.5$ y la hoja es $0$. ¡Todos deben tener la misma cantidad de cifras!
> 3. Escribe los tallos en una columna y las hojas a la derecha, siempre en orden.

---

> [!example] Ejemplo 2: Edades de Amigos de Andrés (Boxplot)
> **Datos (n=14):** 10, 11, 11, 12, 14, 14, 14, 15, 16, 16, 16, 17, 17, 18.
> *   **Mínimo:** 10 | **Máximo:** 18.
> *   **Q2 (Mediana):** Al ser 14 datos, promediamos los centrales (posiciones 7 y 8): $(14 + 15) / 2 = \mathbf{14.5}$.
> *   **Q1:** Es la mediana de los primeros 7 datos (10, 11, 11, **12**, 14, 14, 14). El dato central es 12. *Nota: Si usas el método exacto de promediar extremos en la mitad, obtenemos 11.5*. Usaremos **11.5** para mayor precisión didáctica.
> *   **Q3:** Es la mediana de los últimos 7 datos (15, 16, 16, **16**, 17, 17, 18). El dato central es **16**.

> [!example] Ejemplo 4: Gastos en Dólares (Tallos y Hojas)
> **Precios:** $1.20, $1.75, $1.50, $1.25.
> *   **Paso 1:** Identificamos que el tallo será la parte entera y la primera décima (1.2, 1.5, 1.7).
> *   **Paso 2:** Las hojas serán las centésimas.
> 
> | Tallo | Hojas |
> | :--- | :--- |
> | 1.2 | 0 5 |
> | 1.5 | 0 |
> | 1.7 | 5 |
> *(Nota: El 1.5 se escribe como 1.50 para que la hoja sea 0)*.

---

> [!note] 🎯 Reto: ¡Pon a prueba tu conocimiento!
> 
> **🟢 Nivel Fácil**
> Una encuesta sobre mascotas da: Perros 50%, Gatos 20%, Aves 10%, Otros 20%. Calcula los grados para cada sector.
> 
> **🟡 Nivel Medio**
> Calcula los 5 valores del Boxplot para estas edades: 11, 12, 14, 14, 15, 16, 17, 18, 19, 20, 22.
> 
> **🔴 Nivel Avanzado ($USD)**
> Analiza los precios de estos **40 productos** de una tienda:
> 
> | Precio ($) | Frecuencia ($f_i$) | Frecuencia Acum. ($F_i$) |
> | :--- | :--- | :--- |
> | 6 | 5 | 5 |
> | 7 | 8 | 13 |
> | 8 | 10 | 23 |
> | 9 | 7 | 30 |
> | 10 | 5 | 35 |
> | 11 | 3 | 38 |
> | 12 | 1 | 39 |
> | 25 | 1 | 40 |
> 
> 1. Halla Q1 y Q3 usando las posiciones $(k \times 40) / 4$.
> 2. Calcula el Rango Intercuartílico ($RIC$).
> 3. Identifica si el precio de $25 es un dato atípico leve.

> [!success] Solucionario
> *   **Fácil:** Perros (180°), Gatos (72°), Aves (36°), Otros (72°). ¡Suma 360°!
> *   **Medio:** Min=11, Q1=14, Q2=16, Q3=19, Max=22.
> *   **Avanzado:**
>     1. **Q1:** Posición 10 $\rightarrow$ Está en el precio **$7**. **Q3:** Posición 30 $\rightarrow$ Está en el precio **$9**.
>     2. **RIC:** $9 - 7 = \mathbf{2}$.
>     3. **Límite:** $Q3 + (1.5 \times RIC) = 9 + (1.5 \times 2) = \mathbf{12}$. Como $25 > 12$, **¡Sí! El precio de $25 es un dato atípico.**

---

> [!question] Autoevaluación
> 1.  **Conceptual:** Si al sumar los ángulos de tu gráfico circular te da 359.8°, ¿está mal? *(R: No, es normal perder decimales, lo importante es estar muy cerca de 360°).*
> 2.  **Procedimental:** En una lista de 20 datos (par), ¿cómo hallas la mediana? *(R: Promediando los datos en las posiciones 10 y 11).*
> 3.  **Aplicación USD:** Si el $RIC$ de tus gastos es muy grande, ¿qué significa? *(R: Significa que tus gastos varían mucho mes a mes, no son estables).*

**Notas finales:** ¡Excelente trabajo! Dominar estos gráficos te permitirá analizar datos como un profesional. En la próxima clase, daremos el salto a las **Medidas de Tendencia Central**. ¡Te espero!

> [!info] 🧭 Navegación
> ◀ **Anterior:** [Clase 01 — Tablas de Frecuencia](link_placeholder)
> 🟢 **Actual:** Clase 02 — Gráficos Estadísticos
> ▶ **Siguiente:** [Clase 03 — Medidas de Tendencia Central](link_placeholder)