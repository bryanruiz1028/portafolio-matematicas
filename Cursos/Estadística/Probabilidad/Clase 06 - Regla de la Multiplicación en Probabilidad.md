# Clase 06 — Regla de la Multiplicación en Probabilidad

tags: #algebra #regladelamultip
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 6 de 12

> [!info] 🧭 Navegación
> [[Clase 05|⬅ Clase 05]] | [[00 - Índice del curso|Índice]] | [[Clase 07|Clase 07 ➡]]

> [!info] 🌍 Relevancia y aplicaciones
> La regla de la multiplicación nos permite calcular la probabilidad de que dos o más eventos ocurran de manera simultánea o consecutiva (intersecciones). Es la herramienta esencial para entender cómo el resultado de un primer suceso puede alterar el escenario del segundo.
> 
> *   💵 **Finanzas y seguros:** Estimación de riesgos donde deben fallar múltiples sistemas para que ocurra un siniestro.
> *   🏗️ **Control de calidad industrial:** Cálculo de la probabilidad de que una pieza supere varios filtros de inspección en cadena.
> *   📊 **Vida diaria:** Predicción de eventos secuenciales, como la probabilidad de que hoy llueva **y** además se me olvide el paraguas.

> [!note] 📌 ¿Qué es la Regla de la Multiplicación?
> Imagina que quieres que ocurran dos cosas: por ejemplo, sacar una carta roja **y** luego otra roja. En probabilidad, la palabra clave es **"y"** (intersección). Esta regla nos indica que para hallar la probabilidad de que ambos eventos sucedan, debemos multiplicar sus probabilidades individuales.
> 
> **Fórmulas fundamentales:**
> 
> $$P(A \cap B) = P(A) \cdot P(B)$$
> *(Para eventos **independientes**: el primer resultado no afecta al segundo).*
> 
> $$P(A \cap B) = P(A) \cdot P(B|A)$$
> *(Para eventos **dependientes**: el primer resultado cambia las opciones del segundo).*
> 
> > [!important] **Nota del Experto: Probabilidad vs. Conteo**
> > No confundas esta regla con la "Regla de la Multiplicación" de las permutaciones. Aquí calculamos la **posibilidad de ocurrencia** (un valor entre 0 y 1 o 0% y 100%), no el número total de formas de organizar objetos.

> [!warning] ⚠️ Error común
> El error más grave es **sumar** las probabilidades. Recuerda: la suma se usa para la opción "O" (disyunción). Si buscas que pase el evento A **Y** el evento B, la operación correcta es la **multiplicación**.

> [!tip] 💡 Truco para recordarlo
> Siempre que veas la letra **"y"** en el enunciado de un problema (ejemplo: "azul **y** verde"), visualízala como un signo de multiplicación **(×)**. Es tu señal de acción.

### Procedimiento paso a paso

Para resolver problemas de probabilidad compuesta como un experto, sigue este algoritmo:

**PASO 1** → Identificar la naturaleza del evento: ¿Es **con reemplazo** (independiente) o **sin reemplazo** (dependiente)? Si no se devuelve el objeto, el espacio muestral se reduce.

**PASO 2** → Calcular la probabilidad del primer evento $P(A)$ aplicando la **Regla de Laplace**:
$$\frac{\text{Casos Favorables}}{\text{Casos Totales}}$$

**PASO 3** → Calcular la probabilidad del segundo evento $P(B)$. Si es **sin reemplazo**, ajusta las cifras:
*   El **denominador** (total) siempre disminuye en 1.
*   El **numerador** (favorables) disminuye en 1 **solo si** el segundo evento busca la misma característica que el primero (ej. sacar dos rojas seguidas).

**PASO 4** → Multiplicar las fracciones resultantes, simplificar al máximo y, si se requiere, convertir a porcentaje.

---

### Ejemplos Detallados

> [!abstract] Ejemplo 1: Urnas y esferas (Básico)
> En una urna hay 5 esferas azules, 2 rojas y 1 verde (Total = 8). Se sacan dos esferas **sin reemplazo**. ¿Probabilidad de 1ra azul y 2da verde?
> *   **1ra Azul:** $P(A) = 5/8$
> *   **2da Verde:** El total baja a 7. Como la primera fue azul, aún queda 1 verde. $P(V|A) = 1/7$
> *   **Cálculo:** 
> $$\frac{5}{8} \cdot \frac{1}{7} = \frac{5}{56} \approx 8.9\%$$

> [!abstract] Ejemplo 2: Selección en el aula
> En una clase hay 10 niños y 8 niñas (Total = 18). Se eligen 3 alumnos al azar. ¿Probabilidad de que los tres sean niños?
> *   **1er niño:** $10/18$
> *   **2do niño:** $9/17$ (un niño menos, una persona menos).
> *   **3er niño:** $8/16$
> *   **Cálculo simplificado:** 
> $$\frac{10}{18} \cdot \frac{9}{17} \cdot \frac{8}{16} \rightarrow \frac{5}{9} \cdot \frac{9}{17} \cdot \frac{1}{2} = \frac{5}{34} \approx 14.7\%$$

> [!abstract] Ejemplo 3: El poder del Complemento (Avanzado)
> Una fábrica produce balones: 60% fútbol, 40% baloncesto. Los de fútbol fallan el 5% y los de baloncesto el 3%. ¿Probabilidad de un balón de baloncesto en **buen estado**?
> *   **Dato:** Si el 3% de baloncesto falla, el **97%** está bien (regla del complemento: $1 - 0.03 = 0.97$).
> *   **Cálculo:** 
> $$0.4 \cdot 0.97 = 0.388 = 38.8\%$$

> [!abstract] Ejemplo 4: Análisis de Riesgo Financiero (USD)
> Si un balón de fútbol defectuoso cuesta a la empresa una pérdida de **$15.00 USD**, ¿cuál es la probabilidad de que un balón al azar sea de fútbol y esté defectuoso?
> *   **Prob. Fútbol:** $0.6$
> *   **Prob. Defectuoso:** $0.05$
> *   **Cálculo:** 
> $$0.6 \cdot 0.05 = 0.03 = 3\%$$
> *(Esto indica que el 3% de toda la producción genera esa pérdida de $15 USD).*

---

### Ejercicios para el estudiante

#### 🟢 Fácil: Urnas y Esferas (Datos: 5 azules, 2 rojas, 1 verde)
1. Hallar la probabilidad de sacar roja y luego azul **con reemplazo**.
2. Hallar la probabilidad de sacar verde y luego roja **sin reemplazo**.
3. Hallar la probabilidad de sacar dos rojas **con reemplazo**.
4. Hallar la probabilidad de sacar azul, roja y verde (en ese orden) **sin reemplazo**.

#### 🟡 Medio: Selección de Grupos (Datos: 10 niños, 8 niñas | Lote 20 esferos, 5 dañados)
5. Del grupo de niños/niñas, probabilidad de elegir dos niñas seguidas.
6. Del mismo grupo, probabilidad de elegir niño, luego niña y luego niño.
7. Del lote de 20 esferos, probabilidad de que al elegir dos al azar, ninguno sirva.
8. Del lote de esferos, probabilidad de que el primero sí sirva y el segundo no.

#### 🔴 Avanzado: Aplicación y Costos USD
9. Basado en el lote de esferos (5/20 dañados): Si un esfero dañado representa una pérdida de **$2.50 USD**, ¿cuál es la probabilidad de que el primer esfero extraído active esa pérdida?
10. En la fábrica de balones: ¿Cuál es la probabilidad de que un balón elegido al azar sea de fútbol y **no** esté defectuoso? (Usa el complemento del 5%).
11. Si la empresa fabrica **1,000 balones**, ¿cuántos se espera que sean de fútbol-defectuosos y cuál sería la pérdida total en USD según el Ejemplo 4?
12. En el lote de 20 esferos: Si cada esfero funcional genera **$1.00 USD** de ganancia, ¿probabilidad de sacar dos esferos seguidos que generen ganancia?

> [!success] Solucionario Compacto
> 1) $5/32$ | 2) $1/28$ | 3) $1/16$ | 4) $5/168$ | 5) $7/51$ | 6) $20/153$ | 7) $1/19$ | 8) $15/76$ | 9) $25\%$ | 10) $57\%$ | 11) 30 balones y $\$450$ USD | 12) $21/38$

---

### Mini-prueba de autoevaluación
1.  **Conceptual:** En un evento "sin reemplazo", ¿por qué cambian las probabilidades del segundo suceso?
    *(Respuesta: Porque el primer evento modifica el espacio muestral total y la cantidad de casos favorables disponibles).*
2.  **Procedimental:** Si lanzas una moneda ($1/2$) y un dado ($1/6$), ¿probabilidad de obtener "Escudo" y un número mayor a 4?
    *(Cálculo: $1/2 \cdot 2/6 = 1/6 \approx 16.6\%$).*
3.  **Aplicación:** Una máquina tiene un 2% de error. Si el error cuesta **$100 USD**, ¿qué porcentaje de la producción total representa este riesgo financiero directo?
    *(Respuesta: El 2% de la producción).*

> [!tip] 💡 En la próxima clase
> Exploraremos la **Probabilidad Total**, donde aprenderemos a combinar varios caminos de multiplicación para entender resultados globales. ¡No te lo pierdas!

> [!info] 🧭 Navegación
> [[Clase 05|⬅ Clase 05]] | [[00 - Índice del curso|Índice]] | [[Clase 07|Clase 07 ➡]]