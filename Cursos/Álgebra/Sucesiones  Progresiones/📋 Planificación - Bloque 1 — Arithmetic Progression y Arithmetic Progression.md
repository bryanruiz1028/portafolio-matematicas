# 📋 Planificación Didáctica — Arithmetic Progression y Geometric Progression

**INFORMACIÓN PRELIMINAR**
*   **Nivel:** Educación Secundaria / Media (Álgebra)
*   **Duración:** 80 minutos
*   **Tags:** #Matemáticas #Progresiones #Álgebra #PlanificaciónDocente

---

## 1. TEMA
**Arithmetic Progression y Geometric Progression**

## 2. METODOLOGÍA
**Aprendizaje Colaborativo Formal**
Se organizarán grupos heterogéneos para que los estudiantes manipulen fichas numéricas y comparen patrones aditivos (aritméticos) frente a multiplicativos (geométricos). Como mentor, el docente debe guiar la transición del pensamiento concreto —la observación física de las secuencias— hacia la abstracción algebraica, fomentando que el estudiante "ejercite la lógica" antes de recurrir mecánicamente a las fórmulas.

---

## 3. SECUENCIA DIDÁCTICA

### 3.1 ANTICIPACIÓN (20 min)
**Actividad de inicio:** "El Reto del Crecimiento". Se presentan dos escenarios para ser analizados sin cálculos complejos iniciales:
1.  **Ahorro Lineal (PA):** Un estudiante ahorra $3 adicionales cada día (3, 6, 9, 12...).
2.  **Ahorro Explosivo (PG):** Un estudiante comienza con $3 y cada día triplica su ahorro (3, 9, 27, 81...).

> [!abstract] Reto de comparación y lógica
> Antes de aplicar fórmulas, invite a los estudiantes a "adivinar" razonadamente cuál secuencia superará los $500 primero. El objetivo es identificar que en la PA la diferencia ($d=3$) es constante por suma, mientras que en la PG la razón ($r=3$) es constante por multiplicación.

> [!note] Enfoque DUA
> *   **Qué:** Activación de conocimientos previos sobre patrones, suma repetida y potencias.
> *   **Cómo:** Lluvia de ideas y registro visual comparativo en la pizarra. Es vital permitir que el estudiante use su intuición numérica para predecir el comportamiento de las series.

---

### 3.2 CONSTRUCCIÓN (40 min)
La explicación se divide en dos bloques técnicos, priorizando la comprensión lógica de los elementos sobre la memorización.

**Bloque A: Progresiones Aritméticas (PA)**
*   **Diferencia ($d$):** Se halla restando un término menos el anterior ($a_n - a_{n-1}$).
*   **Término General:** $a_n = a_1 + (n-1)d$.
*   **Suma ($S_n$):** $S_n = \frac{(a_1 + a_n)n}{2}$.

**Bloque B: Progresiones Geométricas (PG)**
*   **Razón ($r$):** Se halla dividiendo un término entre su anterior ($a_n / a_{n-1}$).
*   **Término General:** $a_n = a_1 \cdot r^{n-1}$.
*   **Suma ($S_n$):** $S_n = \frac{a_1(r^n - 1)}{r - 1}$.

> [!warning] El Error muy Grave (Trap)
> Un error común en el álgebra de progresiones es realizar la multiplicación del primer término por la razón *antes* de resolver la potencia (ej: hacer $4 \cdot 3^8$ como $12^8$). Se debe enfatizar la jerarquía de operaciones: primero la potencia, luego el producto.

> [!example] Ejercicio de Interpolación (Nuance del Profe Alex)
> **Problema:** Interpolar 3 medios geométricos entre 3 y 48.
> 1.  Identificar datos: $a_1 = 3$, $a_5 = 48$, $n = 5$.
> 2.  Fórmula de la razón: $r = \sqrt[n-1]{a_n / a_1} = \sqrt[4]{48 / 3} = \sqrt[4]{16}$.
> 3.  **Análisis de experto:** Como el índice de la raíz es **par** (4), existen **dos respuestas posibles**: $r = 2$ y $r = -2$.
>     *   Si $r = 2$, la progresión es creciente: 3, **6, 12, 24**, 48.
>     *   Si $r = -2$, la progresión es alternada: 3, **-6, 12, -24**, 48.

> [!note] Enfoque DUA
> *   **Qué:** Modelado de fórmulas con apoyo manipulativo.
> *   **Cómo:** Uso de fichas para construir secuencias como (96, 48, 24, 12, 6, 3) donde se observa que $r=1/2$.
> *   **Por qué:** Para facilitar la transición del pensamiento concreto al abstracto, permitiendo que el estudiante visualice cómo los números se reducen o crecen antes de aplicar la raíz.

---

### 3.3 CONSOLIDACIÓN (20 min)
**Actividad de cierre:** "Desafío de Identificación y Cálculo". Los grupos deben resolver dos secuencias específicas del contexto:

1.  **Secuencia A:** 2, 5, 8... (Identificar tipo y hallar $a_{10}$).
2.  **Secuencia B:** 5, 10, 20... (Identificar tipo y hallar $a_{10}$).

> [!success] Solucionario para Co-evaluación
> *   **A (Aritmética):** $d = 3$. Término $a_{10} = 2 + (9 \cdot 3) = \mathbf{29}$.
> *   **B (Geométrica):** $r = 2$. Término $a_{10} = 5 \cdot 2^9 = 5 \cdot 512 = \mathbf{2560}$.
> Los estudiantes intercambian cuadernos para verificar no solo el resultado, sino el uso correcto de la jerarquía de operaciones.

---

## 4. RECURSOS

| Recurso | Tipo | Uso en la clase |
| :--- | :--- | :--- |
| **Pizarra y Marcadores** | Físico | Modelado. Usar colores distintos para $d$ (suma) y $r$ (multiplicación). |
| **Fichas Numéricas** | Manipulativo | Construcción física de las series para alumnos con estilo de aprendizaje cinestésico. |
| **Calculadora** | Técnico | Uso exclusivo para potencias elevadas (como $2^9$ o $3^8$) tras plantear la lógica. |
| **Granos de Arroz o Lentejas** | Manipulativo | **Representación de la Leyenda del Tablero de Ajedrez:** Colocar 1 grano en el primer cuadro, 2 en el segundo, 4 en el tercero... para demostrar visualmente por qué el crecimiento geométrico es "explosivo". |

**Nota Pedagógica Final:** Es vital que el estudiante comprenda que si dividimos cualquier término de una PG entre su anterior ($a_n / a_{n-1}$), siempre obtendremos la misma razón. Ejercitar esta comprobación manual previene errores en el despeje de fórmulas más complejas.