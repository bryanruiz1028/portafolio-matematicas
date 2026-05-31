# 📋 Planificación Didáctica — Introducción a los Cuartiles y Deciles en datos agrupados y no agrupados

**Nivel:** Básica Superior (12–15 años) | **Duración:** 80 minutos
**Tags:** #planificacion #dua #estadistica #cuartiles #deciles

---

## 1. Tema
Introducción a los Cuartiles y Deciles en datos agrupados y no agrupados.

---

## 2. Metodología
Se implementará el enfoque de **Aprendizaje Colaborativo Formal**. El aula se organizará en grupos heterogéneos de cuatro estudiantes, donde cada integrante asumirá un rol específico: **líder** (coordina el flujo de trabajo), **secretario** (registra procesos y resultados), **calculador** (ejecuta las operaciones aritméticas) y **vocero** (comunica los hallazgos al plenario) para resolver retos de posición estadística.

---

## 3. Secuencia Didáctica

### 🔵 ANTICIPACIÓN — 20 min

> [!abstract] Actividad de inicio: "¿Dónde está la mitad?"
> Se inicia con un reto de ordenamiento físico. Utilizando el ejemplo de las "edades" o "pantalones" (Source Context), se solicita a un grupo de voluntarios que se ordenen de menor a mayor frente a la clase. Los estudiantes deben identificar visualmente el punto central o **mediana** (Q2). Se explica que, así como la mediana divide al grupo en dos partes iguales (50%), hoy aprenderemos a segmentar los datos en cuatro partes (cuartiles) y diez partes (deciles) para un análisis de posición más preciso.

> [!note] Enfoque DUA
> - **Qué:** Activación de conocimientos previos sobre la mediana y la importancia crítica del orden ascendente de los datos.
> - **Cómo:** De manera grupal y kinestésica, manipulando "fichas de datos" o la posición de los propios compañeros para visualizar físicamente la ubicación de las medidas de posición.

---

### 🟡 CONSTRUCCIÓN — 40 min

> [!example] Actividades centrales: Modelado y Técnica
> Como experto pedagogo, presento la transición de la lógica visual al rigor algorítmico en dos bloques:
>
> **1. Datos no agrupados (Lógica vs. Fórmula):**
> *   **Método Lógico (Mediana de las Mitades):** Explico que el Cuartil 2 (Q2) es la mediana de todo el conjunto. El Q1 es la mediana de la mitad inferior y el Q3 es la mediana de la mitad superior.
> *   **Uso de Fórmulas de Posición:**
>     *   Si el número de datos ($n$) es **impar**: $\text{Posición} = \frac{k(n+1)}{4}$.
>     *   Si es **par**: $\text{Posición} = \frac{k \cdot n}{4}$.
>     *   Para **Deciles**, la posición se halla con: $\text{Posición} = \frac{k \cdot n}{10}$.
> *   **Ejemplo Práctico con el Dataset de 11 Edades:** $\{14, 15, 15, 15, 15, 16, 16, 16, 17, 17, 18\}$. Se modela que Q2 (Posición 6) es 16; Q1 (Posición 3) es 15; y Q3 (Posición 9) es 17.
>
> **2. Datos agrupados en intervalos (Interpolación y Atajo):**
> Presento la fórmula para hallar el valor exacto cuando los datos están en tablas:
> $$Q_k, D_k = L_i + A \cdot \left( \frac{\text{Posición} - F_{i-1}}{F_i - F_{i-1}} \right)$$
> *   **Definición de Términos:** $\text{Posición}$ (es $k \cdot n / 4$ para cuartiles o $k \cdot n / 10$ para deciles), $L_i$ (Límite inferior), $A$ (Amplitud), $F_{i-1}$ (Frecuencia acumulada anterior) y $F_i$ (Frecuencia acumulada del intervalo).
> *   **Atajo Pedagógico (Exact Match):** Si al calcular la "Posición", el número resultante se encuentra **exactamente** en la columna de la frecuencia acumulada ($F_i$), no es necesario aplicar la fórmula larga: el cuartil o decil es simplemente el **límite superior** de ese intervalo.
>
> **3. Interpretación Conceptual:**
> Insisto en que el resultado estadístico carece de valor sin interpretación. El estudiante debe dominar que un Decil 4 ($D4$) representa que el 40% de la muestra tiene un valor **menor o igual a** dicho resultado.

> [!note] Enfoque DUA
> - **Qué:** Construcción del concepto de "medidas de posición" mediante modelado dual (lógico y algorítmico).
> - **Cómo:** Modelado docente en pizarra diferenciando variables con colores, seguido de resolución guiada en parejas.
> - **Por qué:** Proporcionar múltiples medios de representación para reducir la carga cognitiva (atajo del límite superior) y fortalecer la percepción visual.

---

### 🟢 CONSOLIDACIÓN — 20 min

> [!success] Actividad de cierre: "Ticket de Salida"
> Los estudiantes deben resolver un reto final: calcular el Decil 5 (D5) de un conjunto pequeño y argumentar por qué este coincide matemáticamente con el Cuartil 2 (Q2) y la Mediana.
>
> **Requisito de Maestría:** La respuesta solo se considerará correcta si la conclusión utiliza la frase técnica: **"El 50% de los datos es menor o igual a [resultado]"**. El vocero de cada grupo socializará la interpretación para validar el aprendizaje colectivo.

> [!note] Enfoque DUA
> - **Qué:** Demostración de aprendizaje sobre la equivalencia funcional entre Mediana, Q2 y D5.
> - **Cómo:** Expresión de resultados mediante lenguaje verbal y escrito para consolidar la interpretación porcentual.

---

## 4. Recursos

| Recurso | Tipo | Uso en la clase |
| :--- | :--- | :--- |
| **Pizarra** | Físico | Modelado de las fórmulas de posición y representación gráfica de las divisiones de datos (25%, 50%, 75%). |
| **Marcadores** | Físico | Uso de colores diferenciados para identificar visualmente $F_{i-1}$ (anterior) y $F_i$ (posterior) en la fórmula. |
| **Fichas de Datos** | Impreso | Set de datos desordenados (ej. edades, notas) que los grupos deben organizar para aplicar el método lógico. |
| **Guía de Ejercicios** | Impreso | Tablas de frecuencias preparadas para la práctica de interpolación en datos agrupados. |
| **Cinta Métrica** | Físico | **Sugerencia Pedagógica:** Recolectar datos reales de estatura de los estudiantes para construir una tabla de frecuencias en tiempo real y calcular deciles basados en su propia realidad. |