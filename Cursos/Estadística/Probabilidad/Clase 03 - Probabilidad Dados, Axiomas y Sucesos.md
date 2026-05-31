# Clase 03 — Probabilidad: Dados, Axiomas y Sucesos

#algebra #probabilityofas

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 12

> [!info] 🧭 Navegación
> ◀ [[Clase 02 — Regla de Laplace]] | [[00 - Índice del curso]] | [[Clase 04 — Probabilidad Compuesta]] ▶

---

> [!info] 🌍 Relevancia y aplicaciones
> La probabilidad es la herramienta matemática que permite transformar la incertidumbre en predicciones calculadas, fundamentales para la toma de decisiones financieras y el diseño de sistemas lógicos.
> 
> - 💵 **Aplicación con $USD:** Evaluar el riesgo en una apuesta de casino detectando un dado "cargado" que altera el valor esperado de la ganancia.
> - 🏗️ **Aplicación práctica:** Uso de los axiomas fundamentales en el desarrollo de algoritmos de aleatoriedad para videojuegos y simulaciones de tráfico.
> - 📊 **Situación cotidiana:** Decidir la participación en un sorteo basándose en si los sucesos de ganar diferentes premios son mutuamente excluyentes.

---

> [!note] 📌 Conceptos Fundamentales: Axiomas y Dados
> Para dominar la probabilidad, debemos comprender que esta se rige por reglas inamovibles y estructuras espaciales específicas:
> 
> ### 1. Los 3 Axiomas de Kolmogorov (según Profe Alex)
> Un **axioma** es una verdad evidente que no requiere demostración. En probabilidad, estos son:
> 1. **No negatividad:** $P(A) \geq 0$. La probabilidad nunca puede ser negativa.
> 2. **Certidumbre:** $P(S) = 1$. La probabilidad del **Espacio Muestral** (todo lo que puede pasar) es siempre 1 (100%).
> 3. **Adición:** Para sucesos mutuamente excluyentes, $P(A \cup B) = P(A) + P(B)$.
> 
> ### 2. El Espacio Muestral de dos dados
> Al lanzar dos dados, no sumamos sus caras para hallar el total de resultados; aplicamos el principio multiplicativo: $6 \text{ (dado 1)} \times 6 \text{ (dado 2)} = \mathbf{36}$ **combinaciones únicas**.
> 
> ### 3. Dados Cargados (Ruptura de Equiprobabilidad)
> Un **dado cargado** es aquel donde se ha modificado la física para que un evento sea más probable. Esto rompe la "equiprobabilidad" (donde todas las caras valen lo mismo) y nos obliga a trabajar con un sistema de **pesos**.
> 
> > [!important] 🔄 Terminología: ¿Excluyentes o Incompatibles?
> > Según el contexto matemático y pedagógico, los términos **Sucesos Mutuamente Excluyentes** y **Sucesos Incompatibles** son **sinónimos**. Se refieren a eventos que no pueden ocurrir al mismo tiempo (su intersección es vacía), como obtener un número "par" e "impar" en un solo lanzamiento.

> [!warning] ⚠️ Error común
> **Incorrecto:** Pensar que al lanzar dos dados hay solo 12 resultados posibles (sumar los valores máximos).
> **Correcto:** Entender que existen 36 combinaciones. El suceso (1,2) es un caso distinto al (2,1), aunque ambos sumen 3.

> [!tip] 💡 Truco para recordarlo
> Utiliza la **"Regla del Cuadrado"**: Dibuja o visualiza una cuadrícula de $6 \times 6$. Las filas representan el dado A y las columnas el dado B. Esto te permitirá contar casos favorables sin omitir ninguna combinación.

---

### Procedimiento Paso a Paso (Regla de Laplace Extendida)

```text
PASO 1 → Identificar el Espacio Muestral (n): 
         - Dados normales: 36 casos.
         - Dado cargado: Sumar los "pesos" asignados. 
           (Ej: Si Par=2 e Impar=1, Total = 2+2+2 + 1+1+1 = 9).
PASO 2 → Identificar Casos Favorables (f): 
         - Contar combinaciones o sumar pesos de los eventos deseados.
PASO 3 → Aplicar la Fórmula: 
         - P(A) = f / n.
PASO 4 → Simplificar y Convertir: 
         - Reducir la fracción y expresar en decimal o porcentaje (%).
```

---

### Ejemplos Prácticos

> [!example] Ejemplo 1: Probabilidad de Suma 4 (Dos Dados)
> **Problema:** Hallar la probabilidad de que la suma sea exactamente 4.
> - **Casos posibles:** 36.
> - **Casos favorables:** $(1,3), (2,2), (3,1) \implies 3$ casos.
> - **Cálculo:** $P = \frac{3}{36} = \frac{1}{12}$
> - **Resultado:** $0.083 \approx 8.3\%$

> [!example] Ejemplo 2: Obtener un "Par" o Identidad
> **Problema:** Probabilidad de que ambos dados muestren el mismo número.
> - **Casos favorables:** $(1,1), (2,2), (3,3), (4,4), (5,5), (6,6) \implies 6$ casos.
> - **Cálculo:** $P = \frac{6}{36} = \frac{1}{6}$
> - **Resultado:** $0.166 \approx 16.6\%$

> [!example] Ejemplo 3: El Dado Cargado (Pesos 2:1)
> **Problema:** En un dado donde los pares valen el doble que los impares, ¿cuál es la probabilidad de obtener un número $> 4$?
> 1. **Total de pesos:** Impares $(1, 3, 5) = 1+1+1=3$; Pares $(2, 4, 6) = 2+2+2=6$. Total $= 9$.
> 2. **Favorables ($>4$):** Cara 5 (peso 1) y Cara 6 (peso 2). Suma $= 3$.
> 3. **Cálculo:** $P = \frac{3}{9} = \frac{1}{3}$
> - **Resultado:** $0.333 \approx 33.3\%$

> [!example] Ejemplo 4: Aplicación Real $USD y Axioma del Complemento
> **Problema:** Un jugador gana **$50 USD** si la suma de dos dados es 7. Calcule su probabilidad de éxito y de fracaso.
> - **Éxito (Suma 7):** $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1) \implies \frac{6}{36} = \frac{1}{6}$ ($16.6\%$).
> - **Fracaso (Complemento):** Aplicando el axioma $P(A^c) = 1 - P(A)$.
> - **Cálculo:** $1 - \frac{1}{6} = \frac{5}{6}$
> - **Resultado:** $0.833 \approx 83.3\%$ de probabilidad de perder los **$50 USD**.

---

### Ejercicios para el Estudiante

#### 🟢 Nivel Fácil (Conceptos Básicos)
1. Calcula la probabilidad de que la suma de dos dados sea exactamente 2.
2. Calcula la probabilidad de que la suma sea exactamente 12.
3. Utilizando el axioma de suceso seguro, ¿cuál es la probabilidad de que la suma de dos dados sea menor a 15?
4. Explica por qué "sacar un 2" y "sacar un 5" en un dado son sucesos incompatibles.

#### 🟡 Nivel Medio (Dados Cargados y Complementos)
1. En un dado cargado (Pares peso 2, Impares peso 1), ¿cuál es la probabilidad de obtener un número par? (Muestra la fracción).
2. Usando el mismo dado cargado, halla la probabilidad de obtener un 1 o un 3.
3. Si la probabilidad de que un evento $A$ ocurra es $\frac{2}{7}$, calcula $P(A^c)$ usando la fórmula del complemento.
4. Calcula la probabilidad de que la suma de dos dados sea exactamente 7.

#### 🔴 Nivel Avanzado (Axiomas y Retos)
1. Si la probabilidad de ganar un premio de **$100 USD** es $0.3$, ¿cuál es la probabilidad de perder según los axiomas?
2. En el dado cargado (Pares=2, Impares=1), calcula la probabilidad de obtener un número primo mayor que 2.
3. **Reto:** Se lanzan dos dados. ¿Son los sucesos "Suma es par" y "Suma es mayor que 10" mutuamente excluyentes? Demuéstralo listando el caso que rompe la regla.
4. Calcula la probabilidad de que al lanzar dos dados, la suma sea un número primo (2, 3, 5, 7, 11).

#### ✅ Respuestas
- **Fácil:** 1) $\frac{1}{36}$ (2.7%); 2) $\frac{1}{36}$ (2.7%); 3) $1$ (100%); 4) Porque no pueden ocurrir simultáneamente en un solo lanzamiento.
- **Medio:** 1) $\frac{6}{9} = \frac{2}{3}$ (66.6%); 2) $\frac{2}{9}$ (22.2%); 3) $1 - \frac{2}{7} = \frac{5}{7}$ (71.4%); 4) $\frac{6}{36} = \frac{1}{6}$ (16.6%).
- **Avanzado:** 1) $1 - 0.3 = 0.7$ (70%); 2) Caras {3, 5} con pesos $1+1=2$. Resultado: $\frac{2}{9}$ (22.2%); 3) No, porque el caso $(6,6)$ cumple ambos (suma 12 es par y > 10); 4) $\frac{15}{36} = \frac{5}{12}$ (41.6%).

---

### Mini-Prueba de Autoevaluación

1. **Definición técnica:** ¿Por qué un valor de probabilidad de $-0.5$ es imposible?
   - Según el **Axioma de No Negatividad**, cualquier $P(A) \geq 0$.
2. **Comparación de probabilidades:** Al lanzar dos dados, ¿qué suma tiene más probabilidades: 7 o 10?
   - La suma 7 ($\frac{6}{36}$) es más probable que la suma 10 ($\frac{3}{36}$).
3. **Cálculo de pérdida:** Si un algoritmo de casino tiene una probabilidad de victoria de $0.05$ ($5\%$), ¿cuál es la probabilidad de pérdida basada en el axioma del espacio muestral?
   - $P(\text{pérdida}) = 1 - 0.05 = 0.95$ ($95\%$).

---

> [!tip] 💡 En la próxima clase
> Aplicaremos estos axiomas para entender qué sucede cuando realizamos múltiples experimentos consecutivos en la **Clase 04 — Probabilidad Compuesta**.

> [!info] 🧭 Navegación
> ◀ [[Clase 02 — Regla de Laplace]] | [[00 - Índice del curso]] | [[Clase 04 — Probabilidad Compuesta]] ▶