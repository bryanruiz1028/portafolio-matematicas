# 📋 Planificación Didáctica — What is the Standard Deviation? y Variance and Standard Deviation

## 1. Tema
What is the Standard Deviation? y Variance and Standard Deviation

---

## 2. Metodología
Se implementará el **Aprendizaje colaborativo formal**, organizando a los estudiantes en grupos heterogéneos para resolver desafíos de cálculo e interpretación. Se prioriza la resolución de problemas reales (edades y profundidades) mediante la construcción de tablas de frecuencia, fomentando la discusión grupal para transitar del cálculo mecánico a la comprensión conceptual de la dispersión.

---

## 3. Secuencia Didáctica

### 🔵 ANTICIPACIÓN — 20 min

> [!abstract] Actividad de inicio: El Reto del Lago Atípico
> Se presenta la situación basada en la "Analogía del Lago" del contexto: 
> "Un lago tiene una profundidad **media ($\bar{x}$)** de 1.5 metros y una **desviación estándar ($\sigma$)** de 1 metro". 
> 
> **Desafío:** Si mides 1.70 m y no sabes nadar, ¿es seguro entrar? 
> **Profundización:** Discutir que una $\sigma = 1$ sugiere zonas de 0.5 m y 2.5 m. Sin embargo, se debe advertir sobre los **datos atípicos**: el promedio y la desviación podrían no detectar un "agujero" de 4 metros de profundidad. 
> *Objetivo:* Comprender que la dispersión mide la variabilidad "normal", pero los riesgos existen en los extremos.

> [!note] Enfoque DUA
> - **Representación:** Presentar la situación de forma verbal y visual (dibujo de la recta de profundidad en la pizarra).
> - **Compromiso:** Vincular el concepto de "riesgo" con la medida estadística para dar relevancia al aprendizaje.
> - **Soporte:** Permitir que los estudiantes compartan experiencias previas con promedios engañosos.

---

### 🟡 CONSTRUCCIÓN — 40 min

> [!example] Actividad Central: El Taller de las Edades
> Los grupos deben calcular las medidas de dispersión para el siguiente conjunto de datos (Edades de estudiantes):
> 
> | Edad ($x$) | Frecuencia ($f$) |
> | :--- | :--- |
> | 13 | 3 |
> | 14 | 15 |
> | 15 | 23 |
> | 16 | 10 |
> | 17 | 5 |
> | 18 | 4 |
> | **Total ($n$)** | **60** |
> 
> **Pasos Procedimentales:**
> 1. **Media Aritmética ($\bar{x}$):** Calcular $\sum (x \cdot f) / n$. (Resultado esperado: 15.18 años).
> 2. **Varianza:** 
>    - Calcular la "distancia al promedio" ($x - \bar{x}$).
>    - Elevar al cuadrado para evitar que los valores negativos se anulen: $(x - \bar{x})^2$.
>    - Multiplicar por la frecuencia: $(x - \bar{x})^2 \cdot f$.
>    - **Diferenciación Crítica:** 
>        - Si es **Población**: Dividir por $n$. ($\sigma^2$)
>        - Si es **Muestra**: Dividir por $n-1$. ($s^2$)
> 3. **Desviación Estándar:** Aplicar la raíz cuadrada a la varianza. 
>    - *Explicación Pedagógica:* Se aplica la raíz para regresar de "años al cuadrado" a la unidad original: **años**.

> [!note] Enfoque DUA
> - **Acción y Expresión:** Los estudiantes pueden elegir entre realizar cálculos manuales, usar calculadora científica o una hoja de cálculo.
> - **Soporte a la Memoria de Trabajo:** Entregar fichas con fórmulas en dos formatos:
>     - *Algebraico:* $\sigma = \sqrt{\frac{\sum (x - \bar{x})^2 \cdot f}{n}}$
>     - *Descriptivo:* "La desviación es la raíz del promedio de las distancias al cuadrado".
> - **Inclusión (Discalculia):** Proveer tablas que ya incluyan la columna de $(x-\bar{x})^2$ calculada, permitiendo que el estudiante se concentre en la interpretación y la suma final.

---

### 🟢 CONSOLIDACIÓN — 20 min

> [!success] Actividad de Cierre: Análisis de Homogeneidad
> **1. Cálculo del Coeficiente de Variación (CV):**
> Utilizando los resultados previos, aplicar: $CV = \left( \frac{\sigma}{\bar{x}} \right) \cdot 100$.
> 
> **2. Criterio de Interpretación:**
> - Si **CV > 25%**: El grupo es **Heterogéneo** (datos muy dispersos).
> - Si **CV < 25%**: El grupo es **Homogéneo** (datos agrupados).
> 
> **3. Desafío In Vivo (Uso de Cinta Métrica):**
> Un representante de cada grupo medirá la estatura de sus integrantes. Deberán calcular rápidamente la media y determinar "a ojo" quién se desvía más del promedio antes de aplicar la fórmula de desviación estándar para confirmar su hipótesis.

> [!note] Enfoque DUA
> - **Comprensión:** Transformar el dato numérico (CV) en una etiqueta cualitativa (Homogéneo/Heterogéneo).
> - **Interacción Física:** El uso de la cinta métrica proporciona un estímulo táctil y cinestésico para fijar el concepto de "distancia al centro".

---

## 4. Recursos

| Recurso | Tipo | Uso en la clase |
| :--- | :--- | :--- |
| Pizarra | Físico | Modelado de la tabla de frecuencias y de la recta numérica para visualizar la dispersión de las edades. |
| Marcadores | Físico | Uso de colores (Rojo para la media, Azul para las desviaciones) para facilitar la discriminación visual. |
| Fichas Impresas | Material | Guías con la tabla de edades 13-18 y las fórmulas de población ($n$) vs muestra ($n-1$). |
| Cinta Métrica | Físico | Herramienta para la recolección de datos reales (estaturas) en la fase de consolidación. |
| Calculadoras | Digital | Facilitar el cálculo de potencias y raíces cuadradas, permitiendo el enfoque en la interpretación. |