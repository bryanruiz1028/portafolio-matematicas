# 📖 Guía de estudio — Clase 04: Probabilidad Condicional

> [!info] 📌 Conceptos clave
> 
> * **Definición fundamental:** La probabilidad condicional es la probabilidad de que ocurra un evento (A), sabiendo de antemano que ya ha ocurrido otro evento (B).
> * **Reducción del espacio muestral:** A diferencia de la probabilidad simple, aquí el "universo" de datos se reduce. El denominador ya no es el total de la población, sino únicamente el grupo que cumple la condición dada.
> * **Identificación de la condición:** Se reconoce en los enunciados mediante palabras clave como "si...", "dado que...", "sabiendo que..." o "se encontró que...".
> * **Función de la "pista":** La información adicional actúa como una pista que permite descartar los casos que no cumplen con la premisa inicial, simplificando el cálculo.

### 📋 Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Regla de Laplace** | $\frac{\text{Casos favorables}}{\text{Casos posibles}}$ (Base de toda probabilidad). |
| **Probabilidad Condicional $P(A|B)$** | $\frac{P(A \cap B)}{P(B)}$ (Probabilidad de la intersección dividida por la probabilidad de la condición). |
| **Intersección ($A \cap B$)** | Individuos que cumplen ambas condiciones simultáneamente. En la fórmula condicional, actúa como el **numerador**. |

---

### 📝 Ejemplos Resueltos Adicionales

#### Ejemplo A (Caso Básico: Urna de esferas)
En una urna hay 10 esferas numeradas. Se sabe que hay 6 esferas azules (algunas pares, otras impares). Queremos calcular la probabilidad de sacar una esfera con número **par**, sabiendo que la esfera extraída es **azul**.

*   **Paso 1 (Comparación Lógica):** En una probabilidad simple, el denominador sería 10 (todas las esferas). Sin embargo, al darnos la pista de que es **azul**, el espacio muestral se reduce. Nuestro nuevo denominador es 6.
*   **Paso 2 (Contar casos favorables):** Dentro del grupo exclusivo de las 6 esferas azules, identificamos cuáles tienen número par. Según los datos, hay 4 esferas que cumplen ambos requisitos (ser azul y ser par).
*   **Paso 3 (Resultado):** Aplicamos la reducción: $\frac{4}{6}$.
*   **Simplificación:** $\frac{2}{3} \approx 66.6\%$.

#### Ejemplo B (Aplicación Real: Gasto en Belleza)
Un estudio de mercado analiza el comportamiento de clientes que pagan sus productos en **$USD**. El 25% de los clientes gasta en la categoría "Cuidado de Ojos" y el 15% gasta en "Ambas" categorías (Ojos y Cabello). Si sabemos que un cliente ya realizó un gasto en "Cuidado de Ojos", ¿cuál es la probabilidad de que también gaste en "Cabello"?

*   **Paso 1 (Datos):** $P(\text{Ojos}) = 25\%$ (Condición) y $P(\text{Cabello} \cap \text{Ojos}) = 15\%$.
*   **Paso 2 (Fórmula):** $P(\text{Cabello} | \text{Ojos}) = \frac{P(\text{Cabello} \cap \text{Ojos})}{P(\text{Ojos})}$.
*   **Paso 3 (Cálculo):** $\frac{15\%}{25\%} = \frac{15}{25}$. Al ser una división de porcentajes, el símbolo % se simplifica.
*   **Resultado:** $\frac{3}{5} = 0.60$, lo que equivale al **60%**.

---

### ✍️ Ejercicios de Repaso

> [!abstract] 🟢 Nivel: Fácil
> Utilizando el experimento de las 10 esferas, se extrae una al azar. Si se nos informa que la esfera es **roja**, calcula por lógica la probabilidad de que esta sea **par**. 
> * **Datos:** Hay 4 esferas rojas en total y solo 1 de ellas es roja y par simultáneamente.

> [!abstract] 🟡 Nivel: Medio
> En una institución educativa, el 50% de los alumnos practica Baloncesto ($B$) y el 15% practica tanto Fútbol como Baloncesto ($F \cap B$). Si se selecciona un estudiante al azar y se confirma que practica baloncesto, ¿cuál es la probabilidad de que también practique fútbol?

> [!abstract] 🔴 Nivel: Avanzado (Aplicación $USD)
> Un club deportivo premium cobra sus membresías en **$USD**. Tras un análisis financiero, se obtuvieron los siguientes datos sobre los suscriptores:
> * El 15% de los ingresos proviene de socios que pagan por **Ambos** servicios (Gimnasio y Piscina).
> * El 50% de los ingresos proviene de socios que pagan **únicamente** el servicio de Piscina.
> 
> Si se selecciona un suscriptor al azar y se confirma que paga el servicio de Piscina, ¿cuál es la probabilidad de que también pague por "Ambos" servicios? 
> 
> **Pista pedagógica:** El denominador debe ser el total de suscriptores de Piscina ($50\% \text{ única} + 15\% \text{ ambos} = 65\%$). El numerador es el porcentaje de "Ambos" ($15\%$).

---

> [!tip] 💡 Consejo de estudio
> El **Profe Alex** recomienda que, antes de correr a aplicar la fórmula, utilices la **lógica de visualización**. Imagina que el grupo total de datos se "encoge" basándose solo en la condición dada. Al ver este nuevo grupo reducido como tu nuevo "100%", identificar el numerador se vuelve mucho más intuitivo y evitarás errores comunes al colocar los datos en la fórmula.