# Clase 10 — Teorema de la Probabilidad Total
tags: #algebra #teoremadelaprob
Curso: [[00 - Índice del curso]] | Bloque 3 | Lección 10 de 12

> [!info] 🧭 Navegación
> [[Clase 09|⬅ Clase 09]] | [[00 - Índice del curso|Índice]] | **Clase 10** | | [[Clase 11|Clase 11 ➡]]

## 1. ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> El Teorema de la Probabilidad Total es la herramienta que nos permite unificar diferentes escenarios de incertidumbre en un único valor ejecutable. Es fundamental cuando un evento final depende de varias causas o "caminos" previos.
> 
> *   **💵 Aplicación USD:** Imagine una planta donde la Máquina C fabrica el 60% de la producción con un 4% de defectos. Si cada error le cuesta a la empresa **$100 USD** en reparaciones, este teorema permite calcular el impacto económico real sobre la producción total.
> *   **🏗️ Aplicación práctica:** En el control de calidad industrial, es vital para evaluar el desempeño global de una fábrica que opera con múltiples líneas de producción, cada una con su propia tasa de efectividad.
> *   **📊 Situación cotidiana:** Permite modelar el éxito profesional. Por ejemplo, la probabilidad de que el "Señor Gómez" sea nombrado gerente no es un evento aislado, sino que depende de variables previas como la expansión física de su empresa.

## 2. Concepto clave

> [!note] 📌 ¿Qué es el Teorema de la Probabilidad Total?
> Es la suma de las probabilidades de todas las rutas o condiciones iniciales que conducen a un mismo evento. Para aplicarlo, las causas (eventos iniciales) deben ser **mutuamente excluyentes** (no pueden ocurrir al mismo tiempo) y su suma debe cubrir la totalidad del espacio muestral.

*   **Matemáticamente se expresa así:**
    $$P(A) = \sum P(A|B_i)P(B_i) = P(A|B_1)P(B_1) + P(A|B_2)P(B_2) + \dots$$

*   **⚠️ Error común:** No confundir con la simple "Regla de la Multiplicación". Usamos la multiplicación cuando el orden es estricto (ej. "primero azul Y luego roja"). Usamos **Probabilidad Total** cuando el evento puede ocurrir por diversas rutas y el orden no está definido o existen múltiples causas (ej. "obtener una azul y una verde en cualquier orden").
*   **💡 Truco para recordarlo (Diagrama de Árbol):** Como enseña el Profe Alex, visualiza las ramas del árbol. La regla de oro es: *"Si avanzas por la misma rama, multiplicas; si saltas a una rama paralela (cambias de camino), sumas"*.

## 3. Procedimiento paso a paso

```text
PASO 1: Identificar las probabilidades a priori. 
        Son las probabilidades de las causas iniciales (ej. P de Máquina A, B o C).

PASO 2: Determinar las probabilidades condicionales. 
        Identificar qué ocurre dentro de cada subgrupo (ej. P de defecto dado que es Máquina A).

PASO 3: Multiplicar las probabilidades de cada rama. 
        Calcular la probabilidad específica de cada camino (Causa × Efecto).

PASO 4: Sumar los resultados de todos los caminos. 
        Se suman todos los trayectos que llevan al evento deseado para obtener el total.
```

## 4. Ejemplos Desarrollados

> [!example] Ejemplo 1: Urna con esferas (Caso Básico)
> Una urna tiene 5 esferas azules (A), 2 rojas (R) y 1 verde (V). Se extraen dos con reemplazo. ¿Cuál es la probabilidad de sacar una azul y una verde en cualquier orden?
> *   **Ruta 1 (Azul y luego Verde):** $(5/8) \times (1/8) = 5/64$
> *   **Ruta 2 (Verde y luego Azul):** $(1/8) \times (5/8) = 5/64$
> *   **Probabilidad Total:** $5/64 + 5/64 = 10/64 = 5/32 \approx 15.62\%$

> [!example] Ejemplo 2: El nombramiento del Sr. Gómez (Diagrama de Árbol)
> La empresa tiene un 60% ($3/5$) de probabilidad de abrir sucursal. Si la abre, la probabilidad de que Gómez sea gerente es 70% ($7/10$). Si no la abre ($2/5$), la probabilidad cae al 10% ($1/10$).
> *   **Camino A (Abre y es gerente):** $(3/5) \times (7/10) = 21/50$
> *   **Camino B (No abre y es gerente):** $(2/5) \times (1/10) = 2/50$
> *   **Probabilidad Total:** $21/50 + 2/50 = 23/50 = 0.46$ o **46%**.

> [!example] Ejemplo 3: Selección de estudiantes (Eventos Dependientes)
> En una clase de 9 niñas y 6 niños (15 en total), se eligen 3 estudiantes sin reemplazo. Probabilidad de que las 3 sean niñas:
> *   **Paso 1:** $9/15$ (primera niña).
> *   **Paso 2:** $8/14$ (segunda niña, queda una menos en el total).
> *   **Paso 3:** $7/13$ (tercera niña).
> *   **Cálculo:** $(9/15) \times (8/14) \times (7/13) = 12/65 \approx 18.46\%$.
> *   *Nota técnica: Al no haber reemplazo, los denominadores y numeradores disminuyen en cada paso.*

> [!example] Ejemplo 4: Control de costos (Aplicación USD)
> Una fábrica tiene tres máquinas con las siguientes cuotas de producción y tasas de defecto:
> - **Máquina A:** 10% producción (0.1) con 1% defectos (0.01) → $0.1 \times 0.01 = 0.001$
> - **Máquina B:** 30% producción (0.3) con 2% defectos (0.02) → $0.3 \times 0.02 = 0.006$
> - **Máquina C:** 60% producción (0.6) con 4% defectos (0.04) → $0.6 \times 0.04 = 0.024$
> 
> **Probabilidad Total de Defecto:** $0.001 + 0.006 + 0.024 = 0.031$ (3.1%).
> **Impacto Económico:** Si cada pieza defectuosa de la Máquina C cuesta **$100 USD** reparar, la probabilidad de incurrir en ese costo específico al tomar una pieza al azar es del **2.4%**.

## 5. Ejercicios para el estudiante

*   **🟢 Fácil:** Una urna contiene 10 esferas azules y 5 rojas. Si se extraen dos esferas con reemplazo, calcule la probabilidad de obtener una de cada color en cualquier orden.
*   **🟡 Medio:** Una fábrica produce balones de fútbol (60%) y baloncesto (40%). La probabilidad de defecto en fútbol es 0.05 y en baloncesto es 0.03. Calcule la probabilidad total de que un balón elegido al azar sea defectuoso.
*   **🔴 Avanzado (Aplicación USD):** El Sr. Gómez (del Ejemplo 2) tiene una probabilidad total del 46% de ser nombrado gerente. Si lo logra, recibirá un bono de **$5,000 USD**. Calcule el "valor esperado" del bono (Probabilidad total × Monto del bono).

## 6. Respuestas y Autoevaluación

> [!success] Respuestas de los ejercicios
> *   **Fácil:** $P = (10/15 \times 5/15) + (5/15 \times 10/15) = 50/225 + 50/225 = 100/225 \approx 44.4\%$.
> *   **Medio:** $P = (0.6 \times 0.05) + (0.4 \times 0.03) = 0.03 + 0.012 = 0.042$ (4.2%).
> *   **Avanzado:** Valor esperado = $0.46 \times 5000 = \mathbf{\$2,300 USD}$.

> [!question] Mini-prueba de comprensión
> 1. **¿Qué operación matemática realizamos al "saltar" de una ruta paralela a otra (ramas diferentes) para consolidar un resultado?**
>    a) Multiplicación.
>    b) División.
>    c) Suma.
> 2. **Si el evento A tiene una probabilidad de 0.8 y el evento B (dado que ocurrió A) tiene 0.9, ¿cuál es la probabilidad de que ocurra esa ruta específica A-B?**
>    a) 1.7
>    b) 0.72
>    c) 0.1
> 3. **Si una fábrica tiene una probabilidad de defecto total de 0.031 y produce 1,000 piezas, ¿cuántas se esperan defectuosas estadísticamente?**
>    a) 3.1 piezas.
>    b) 31 piezas.
>    c) 310 piezas.

## 7. Notas finales

> [!tip] 💡 En la próxima clase
> Una vez que dominamos cómo sumar todas las causas para llegar a un efecto (Probabilidad Total), aprenderemos el proceso inverso: si ya sabemos que ocurrió el efecto (ej. una pieza salió defectuosa), ¿cuál es la probabilidad de que la causa haya sido la Máquina A? A esto lo llamamos el **Teorema de Bayes**.

> [!info] 🧭 Navegación
> [[Clase 09|⬅ Clase 09]] | [[00 - Índice del curso|Índice]] | **Clase 10** | | [[Clase 11|Clase 11 ➡]]