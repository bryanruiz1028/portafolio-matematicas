# Clase 04 — Regla de la Suma | Unión de Sucesos

> [!info] 🧭 Navegación
> - **Anterior:** [[Clase 03 — Sucesos Mutuamente Excluyentes]]
> - **Siguiente:** [[Clase 05 — Probabilidad Condicional]]

---

### 1. Relevancia y Aplicaciones
Dominar la **unión de sucesos** es vital para entender la realidad sin errores de bulto. En estadística, la precisión depende de no duplicar información: si contamos dos veces a la misma persona por cumplir dos condiciones, nuestros datos dejarán de ser fiables.

*   💵 **Aplicación $USD:** Las aseguradoras de salud calculan la probabilidad de que un cliente necesite servicios médicos, medicamentos o ambos. Si la probabilidad de un gasto doble es alta, el costo de la prima (póliza) en dólares se ajusta para cubrir ese riesgo financiero.
*   🏗️ **Logística:** En el mantenimiento de una flota, se calcula la probabilidad de que un vehículo necesite reparación de motor **o** de frenos para optimizar el presupuesto mensual y el inventario de repuestos.
*   📊 **Situación cotidiana:** Al elegir un plan de transporte, evaluamos qué tan probable es que necesitemos usar el metro, un taxi o ambos en un mismo mes para decidir si el costo fijo de una tarjeta ilimitada vale la pena.

---

### 2. Definición del Concepto Clave

> [!note] 📌 ¿Qué es la Regla de la Suma?
> Es la regla que usamos para calcular la probabilidad de que ocurra el evento A, el evento B, o ambos a la vez. En matemáticas, esto se conoce como la **Unión de Sucesos** ($A \cup B$) y se identifica fácilmente por el uso de la letra "**o**".

> [!warning] ⚠️ Error común: "El Doble Conteo"
> Imagina una tienda de mascotas con gatos blancos. Si sumas todos los gatos por un lado y todos los animales blancos por otro, habrás contado a los **gatos blancos** dos veces. Esto es un error grave: ¡podrías terminar con una probabilidad mayor al 100% (lo cual es matemáticamente imposible)! Siempre debemos restar esa "doble cuenta" (la intersección).

> [!tip] 💡 Truco para recordarlo
> Visualiza siempre el **Diagrama de Venn**: dos círculos que se cruzan. La regla de la suma es simplemente el área total de ambos círculos. Para no repetir el centro (donde se cruzan), lo sumamos una vez y restamos el exceso.

---

### 3. Procedimiento Paso a Paso

Para resolver problemas de unión de sucesos, sigue este flujo lógico:

```text
PASO 1 → Identificar los eventos (A, B) y el total de casos posibles.
PASO 2 → Determinar si hay intersección (¿pueden ocurrir ambos a la vez?).
PASO 3 → Dibujar un diagrama de Venn: identifica la intersección primero.
         Aplica la fórmula: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
PASO 4 → Realizar el cálculo y expresar el resultado final (Fracción, Decimal o %).
```

---

### 4. Bloques de Ejemplos Prácticos

#### Ejemplo 1: Lanzamiento de dado (Mutuamente Excluyentes)
*¿Cuál es la probabilidad de que al lanzar un dado caiga un número **Par** o **Impar**?*
*   **Evento A (Par):** {2, 4, 6} → $3/6$.
*   **Evento B (Impar):** {1, 3, 5} → $3/6$.
*   **Intersección:** Un número no puede ser ambos a la vez ($0$).
*   **Cálculo:** $3/6 + 3/6 = 6/6 = 1$.
*   **Resultado:** $100\%$ (Suceso seguro).

#### Ejemplo 2: Lanzamiento de dado (Sucesos No Excluyentes)
*¿Cuál es la probabilidad de obtener un número **Par** o **Mayor que 3**?*
*   **Evento A (Par):** {2, 4, 6} → $3/6$.
*   **Evento B (>3):** {4, 5, 6} → $3/6$.
*   **Intersección (A ∩ B):** {4, 6} → Son 2 números que cumplen ambos requisitos.
*   **Cálculo:** $3/6 + 3/6 - 2/6 = 4/6 = 2/3$.
*   **Resultado:** $0.6667$ o $66.67\%$.

#### Ejemplo 3: El Consultorio Médico
*En una sala de espera, el 60% toma café (C), el 50% lee revistas (R) y el 20% hace ambas cosas.*
*   **Visualización (Venn):**
    *   Solo Café: $60\% - 20\% = 40\%$
    *   Solo Revistas: $50\% - 20\% = 30\%$
    *   Intersección (Ambos): $20\%$
*   **Cálculo:** $P(C \cup R) = 60\% + 50\% - 20\% = 90\%$.
*   **Conclusión:** Existe un 90% de probabilidad de que un paciente esté consumiendo café o leyendo.

#### Ejemplo 4: Aplicación $USD (Logística de Transporte)
*Una empresa analiza costos: el 70% usa transporte público (costo mensual $80) y el 55% usa transporte particular (costo mensual $120). El 40% usa ambos servicios.*
*   **Análisis de Costos:** Un empleado que usa ambos servicios gasta exactamente **$200 USD** ($80 + $120).
*   **Pregunta:** ¿Cuál es la probabilidad de que un empleado genere un gasto de exactamente $200 USD?
*   **Respuesta:** Es la probabilidad de la intersección: **40%**.
*   **Probabilidad de cualquier gasto de transporte:** $70\% + 55\% - 40\% = 85\%$.

---

### 5. Ejercicios de Aplicación

🟢 **Nivel: Fácil (Dados)**
1. En el lanzamiento de un dado, calcula la probabilidad de obtener un número "Par" **o** un número "Menor que 2".

🟡 **Nivel: Medio (Tienda de Mascotas)**
En una tienda hay **13 animales** en total (7 gatos y 4 perros; los 2 restantes son de otra especie). De ellos, hay 4 animales blancos: 2 son gatos blancos y 2 son perros blancos.
2. ¿Cuál es la probabilidad de elegir al azar un animal que sea **Gato o Blanco**? (Expresa en decimal y %).
3. ¿Cuál es la probabilidad de elegir un **Gato o un Perro**?

🔴 **Nivel: Avanzado (Presupuesto $USD)**
4. Un profesional tiene un presupuesto de viáticos de **$200 USD**. Se sabe que el 70% de las veces usa transporte público (costo $80) y el 55% usa particular (costo $120). El 40% de las veces usa ambos en el mismo periodo.
   *   Calcula la probabilidad de que el profesional necesite usar transporte (cualquiera de los dos).
   *   ¿Cuál es la probabilidad exacta de que el profesional agote su presupuesto total de $200 USD usando ambos servicios?

---

### 6. Solucionario y Autoevaluación

```ad-success
title: ✅ Soluciones Comentadas
1. **Dados:** Par {2,4,6} y Menor que 2 {1}. Son excluyentes. $3/6 + 1/6 = 4/6 = 66.67\%$.
2. **Gato o Blanco:** $P(G) = 7/13$, $P(B) = 4/13$, $P(G \cap B) = 2/13$.
   Cálculo: $7/13 + 4/13 - 2/13 = 9/13 \approx 0.6923$ o **69.23%**.
3. **Gato o Perro:** $7/13 + 4/13 - 0 = 11/13 \approx 84.62\%$. (No hay intersección).
4. **Presupuesto:** 
   - Probabilidad de transporte: $70\% + 55\% - 40\% = 85\%$.
   - Probabilidad de gastar los $200 USD: Corresponde a la intersección (Público Y Particular) = **40%**.
```

```ad-question
title: 📝 Mini-prueba de teoría
1. Si $P(A) = 0.6$ y $P(B) = 0.4$, y son mutuamente excluyentes, ¿cuál es $P(A \cup B)$?
   a) 1.0 (100%)  b) 0.2  c) 0.0
2. En la regla de la suma para sucesos no excluyentes, ¿por qué restamos la intersección?
   a) Porque es un valor negativo. b) Para corregir el doble conteo de los mismos elementos.
3. Si al calcular una unión de sucesos obtienes **115%**, ¿qué ocurrió?
   a) Es un evento muy seguro. b) Olvidaste restar la intersección en el cálculo.
```

---

### 7. Cierre y Conexión

Entender la unión de sucesos nos protege de errores contables y nos permite presupuestar mejor en situaciones de incertidumbre. Pero, ¿qué pasa si el hecho de que ocurra un evento cambia la probabilidad de que ocurra el otro?

> [!tip] 💡 En la próxima clase
> Entraremos en el fascinante mundo de la **Probabilidad Condicional**. Aprenderemos a calcular probabilidades cuando ya tenemos información previa, como: "¿Cuál es la probabilidad de que un paciente tome café *sabiendo que* ya eligió una revista?".

---
> [!info] 🧭 Navegación Final
> - [[Clase 03 — Sucesos Mutuamente Excluyentes | ⬅️ Volver a Clase 03]]
> - [[Clase 05 — Probabilidad Condicional | ➡️ Ir a Clase 05]]