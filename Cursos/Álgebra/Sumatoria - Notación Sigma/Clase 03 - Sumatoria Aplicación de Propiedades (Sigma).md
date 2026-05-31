# Clase 03 — Sumatoria: Aplicación de Propiedades (Sigma)

#algebra #summationsigman
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 3 de 5

> [!info] 🧭 Navegación
> « [[Clase 02]] | [[00 - Índice del curso|Índice]] | [[Clase 04]] »

---

## 🌍 Relevancia y aplicaciones

> [!info] 🌍 Relevancia y aplicaciones
> La aplicación de las propiedades de sumatoria permite simplificar cálculos masivos que, de hacerse manualmente, tomarían horas de trabajo propenso a errores humanos. Al dominar estas reglas, transformamos expresiones complejas en operaciones aritméticas básicas, optimizando el tiempo en situaciones donde la precisión es vital. El Profe Alex destaca que estas fórmulas son herramientas esenciales para manejar sucesiones con cientos o miles de términos de forma inmediata.
> 
> *   **Económica ($USD):** Proyección de utilidades acumuladas y flujos de caja en planes de inversión a largo plazo.
> *   **Arquitectónica:** Cálculo preciso de materiales (ladrillos, vigas) en estructuras con patrones geométricos crecientes.
> *   **Estadística cotidiana:** Procesamiento de grandes conjuntos de datos para hallar promedios y varianzas en censos poblacionales.

> [!note] 📌 ¿Qué es la Notación Sigma?
> Es una "receta" abreviada para sumar muchos números. El símbolo $\Sigma$ nos da las instrucciones: el número de abajo ($i=1$) es nuestro **punto de partida**, el número superior es nuestra **meta** (donde nos detenemos), y la expresión al lado es la **regla** que debemos seguir para generar cada número de la lista antes de sumarlos todos.

> [!warning] ⚠️ Error común
> Nunca apliques las fórmulas de potencias directamente sobre una expresión compuesta. El error más grave es olvidar **separar cada término** en su propia sumatoria o dejar la **constante** (el número que multiplica) dentro del símbolo, lo que arruina el cálculo por completo.

> [!tip] 💡 Truco para recordarlo
> Para la fórmula de los cuadrados, usa la regla: **"El número ($n$), por el que le sigue ($n+1$), por la suma de esos dos ($2n+1$)"**. Todo eso siempre dividido entre 6.

---

## Procedimiento Estándar

Sigue estos 4 pasos para resolver sumatorias de forma profesional:

```text
1. Separar términos: Σ(a + b) = Σa + Σb.
2. Extraer constantes: El número sale del símbolo (c · Σi).
3. Identificar fórmulas: 
   - Lineal (i): [n(n+1)] / 2
   - Cuadrática (i²): [n(n+1)(2n+1)] / 6
   - Cúbica (i³): [[n(n+1)] / 2]²
4. Resolver y simplificar: Eliminar denominadores mediante divisiones exactas.
```

---

## Ejemplos Guiados

### Ejemplo 1: Nivel Básico (Lineal)
**Ejercicio:** $\sum_{i=1}^{50} (2i - 5)$
1. **Separación y Constantes:** $2 \sum_{i=1}^{50} i - \sum_{i=1}^{50} 5$.
2. **Aplicación:** 
   - Para $i$: $\frac{50 \times 51}{2} = 1275$. Multiplicamos por la constante 2: $2(1275) = 2550$.
   - Para la constante 5: $50 \times 5 = 250$.
3. **Resultado:** $2550 - 250 =$ **2300**.

### Ejemplo 2: Signos y Cuadrados (Simplificación Detallada)
**Ejercicio:** $\sum_{i=1}^{70} (3i^2 - 2i + 3)$
*   **Desarrollo:** $3 \sum i^2 - 2 \sum i + \sum 3$.
*   **Simplificación Clave:** Para el primer término $3 [\frac{70 \times 71 \times 141}{6}]$:
    - Mitad de 6 es **3**; mitad de 70 es **35**.
    - Tercera de **3** (denominador) es **1**; tercera del coeficiente **3** (afuera) es **1**.
    - Operación limpia: $35 \times 71 \times 141 = 350,385$.
*   **Seguimiento:** $-2 [\frac{70 \times 71}{2}] + (70 \times 3) = -4,970 + 210$.
*   **Resultado:** $350,385 - 4,970 + 210 =$ **345,625**.

### Ejemplo 3: Avanzado (Cubos)
**Ejercicio:** $\sum_{i=1}^{40} (2i^3 - 3i^2 - 5i - 10)$
*   **Fórmula de Cubos:** Es el cuadrado de la suma de naturales: $[\frac{40(41)}{2}]^2 = 820^2 = 672,400$.
*   **Cálculo por pasos:**
    - Cubos: $2 \times 672,400 = 1,344,800$.
    - Cuadrados: $3 [\frac{40 \times 41 \times 81}{6}] = 66,420$.
    - Lineal: $5 [\frac{40 \times 41}{2}] = 4,100$.
    - Constante: $40 \times 10 = 400$.
*   **Operación final:** $1,344,800 - 66,420 - 4,100 - 400$.
*   **Resultado (Source Truth):** **1,273,800**.

### Ejemplo 4: Aplicación en Negocios ($USD)
**Problema:** Un quiosco proyecta su ganancia diaria según $2i - 5$ (donde $i$ es el día). ¿Cuál es la ganancia acumulada tras 50 días?
*   **Planteamiento:** $\sum_{i=1}^{50} (2i - 5)$.
*   **Resolución:** Siguiendo el procedimiento del Ejemplo 1, obtenemos 2300.
*   **Resultado:** La ganancia total es de **$2,300 USD**.

---

## Ejercicios Prácticos

🟢 **Fácil:**
Halla el valor de: $\sum_{i=1}^{100} (5i + 2)$

🟡 **Medio:**
Halla el valor de: $\sum_{i=1}^{200} (3i^2 - 5i)$

🔴 **Avanzado ($USD):**
Una inversión crece mensualmente según $i^3 - 2i^2 + 3i$. Calcula el total acumulado en 20 meses:
$\sum_{i=1}^{20} (i^3 - 2i^2 + 3i)$

> [!success] ✅ Respuestas (para el docente)
> 1.  **Fácil:** 25,450
> 2.  **Medio:** 2,593,500
> 3.  **Avanzado:** 38,990 USD

---

## Autoevaluación y Cierre

> [!question] 1. ¿Qué permite la propiedad de linealidad?
> <details> <summary>Ver respuesta</summary> Permite descomponer una sumatoria compleja en partes más simples (sumatorias individuales) y extraer los factores constantes para aplicar las fórmulas directas. </details>

> [!question] 2. Calcula rápidamente: $\sum_{i=1}^{10} 15$
> <details> <summary>Ver respuesta</summary> Es una constante: $10 \times 15 = 150$. </details>

> [!question] 3. Aplicación rápida ($USD)
> Si ahorras "$i$" dólares cada día por 10 días, ¿cuánto tienes al final?
> <details> <summary>Ver respuesta</summary> $\sum_{i=1}^{10} i = \frac{10 \times 11}{2} = 55$ USD. </details>

**Próximo tema:** 
Las fórmulas de hoy solo funcionan si empezamos en $i=1$. En la próxima clase veremos el **"Cambio de límites o índices"**, la técnica para resolver sumatorias que inician en cualquier otro número.

> [!info] 🧭 Navegación
> « [[Clase 02]] | [[00 - Índice del curso|Índice]] | [[Clase 04]] »