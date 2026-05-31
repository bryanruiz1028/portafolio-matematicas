# 📖 Guía de estudio — Clase 05: Probabilidad Condicional

¿Qué tal, amigas y amigos? Espero que estén muy bien. En esta guía vamos a dominar la probabilidad condicional, un tema que parece difícil pero que, si lo miramos con lógica, ¡es pan comido! Como siempre dice el profe Alex: "¡Pilas con esto!", porque entender la condición es la clave de todo.

> [!info] 📌 Conceptos clave
> La probabilidad condicional ocurre cuando tenemos una **"restricción"** o una **"pista"** adicional. Ya no calculamos sobre el total de los datos, sino sobre un grupo reducido que cumple con algo que "ya ocurrió".
> 
> - **Espacio Muestral Restringido:** La condición reduce nuestro universo de búsqueda. 
> - **La Condición:** Es fundamental identificar qué evento ya es un hecho (el denominador).
> - **Lógica vs. Fórmula:** Podemos usar la fórmula matemática o la lógica de **tablas de contingencia**, que suelen ser mucho más visuales y directas.
> - **Resultados:** Siempre puedes expresar tus respuestas como fracción ($24/25$), decimal ($0.96$) o porcentaje ($96\%$).

---

## 2. Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Probabilidad Condicional $P(A \mid B)$** | Probabilidad de que ocurra $A$ dado que $B$ ya sucedió. <br> Fórmula: $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ |
| **Intersección ($A \cap B$)** | Elementos que cumplen ambas condiciones simultáneamente (ej. aprueba Matemáticas **e** Inglés). |
| **Regla de la Multiplicación** | Se usa para hallar la intersección si conocemos la condicional: <br> $P(A \cap B) = P(B) \cdot P(A \mid B)$ |
| **Complemento o Suceso Contrario** | Probabilidad de que algo "no ocurra". Se calcula como la diferencia para llegar al total: $1 - P(A)$. |

---

## 3. Ejemplos Resueltos Adicionales

> [!example] Ejemplo A — Estudiantes de Matemáticas e Inglés
> En un curso, el $80\%$ aprueba Matemáticas ($P(M) = 0.80$), el $75\%$ aprueba Inglés ($P(I) = 0.75$) y, de los que aprobaron Matemáticas, el $90\%$ aprueba Inglés ($P(I \mid M) = 0.90$).
> 
> **Pregunta:** ¿Cuál es la probabilidad de aprobar Matemáticas si ya se sabe que se aprobó Inglés? ($P(M \mid I)$)
> 
> **Paso a paso:**
> 1. **Hallar la intersección ($M \cap I$):** Multiplicamos los datos conocidos.
>    $P(M \cap I) = P(M) \cdot P(I \mid M) = 0.80 \cdot 0.90 = 0.72$ (o $72\%$).
> 
> 2. **Aplicar la fórmula condicional:**
>    $P(M \mid I) = \frac{P(M \cap I)}{P(I)} = \frac{0.72}{0.75}$
> 
> 3. **Intuición matemática:** ¡Pilas! Aquí el $0.75$ es nuestro **nuevo total**. Ya no nos importa el curso entero, sino solo el grupo que aprobó Inglés.
> 
> 4. **Resultado:**
>    $P(M \mid I) = 0.96$
>    **Respuesta final:** Existe un **$96\%$** de probabilidad de haber aprobado Matemáticas.

> [!example] Ejemplo B — Clientes y Descuentos en Ventas ($USD)
> - El $60\%$ de los clientes usa tarjeta de crédito ($P(T) = 0.60$).
> - El $30\%$ de las compras son superiores a $\$100$ USD ($P(C) = 0.30$).
> - De los que usan tarjeta, el $25\%$ hace compras superiores a $\$100$ USD ($P(C \mid T) = 0.25$).
> 
> **Pregunta:** Si un cliente hizo una compra superior a $\$100$ USD, ¿cuál es la probabilidad de que haya usado tarjeta? ($P(T \mid C)$)
> 
> **Paso a paso:**
> 1. **Intersección (Tarjeta y Compra > $\$100$):**
>    $P(T \cap C) = P(T) \cdot P(C \mid T) = 0.60 \cdot 0.25 = 0.15$ ($15\%$).
> 
> 2. **Cálculo de la probabilidad condicional:**
>    $P(T \mid C) = \frac{P(T \cap C)}{P(C)} = \frac{0.15}{0.30}$
> 
> 3. **La prueba de fuego:** 
>    $P(T \mid C) = 0.5$
>    **Respuesta final:** La probabilidad es del **$50\%$**.

---

## 4. Ejercicios de Repaso

> [!abstract] 🟢 Fácil
> Basado en una carrera atlética con $200$ participantes: $123$ hombres ($M$) y $77$ mujeres ($F$). Hay $20$ niñas en la categoría "Niños" y $60$ personas en la categoría "Senior" ($41$ hombres y $19$ mujeres).
> 1. Calcule la probabilidad simple de que un corredor elegido al azar sea mujer.
> 2. Calcule la probabilidad de que un corredor sea una niña (Femenino en categoría Niños).
> 3. Si se selecciona a alguien de la categoría **Senior**, ¿cuál es la probabilidad de que sea hombre?

> [!abstract] 🟡 Medio
> Definamos $A = \text{Aprobar}$ y $E = \text{Entregar trabajos}$. Resuelva usando la lógica del suceso contrario:
> 1. Si la probabilidad de aprobar dado que NO se entregó el trabajo es del $30\%$ ($P(A \mid \text{No E}) = 0.30$), ¿cuál es la probabilidad de perder la materia (No A) en esa misma condición?
> 2. Si el $80\%$ de los estudiantes entrega trabajos ($P(E) = 0.80$), ¿cuál es la probabilidad de elegir a alguien que NO entregó?
> 3. Si $P(A \mid E) = 0.875$, calcule la probabilidad de no aprobar habiendo entregado los trabajos.

> [!abstract] 🔴 Avanzado — Aplicación con $USD
> **Reto de Tabla de Contingencia:** Complete la siguiente tabla de una tienda con $200$ clientes y responda.
> 
> | Categoría | Gasto < \$50 | Gasto \$50-\$100 | Gasto > \$100 | Total |
> | :--- | :---: | :---: | :---: | :---: |
> | **Compra con Descuento** | $20$ | $30$ | $50$ | **$100$** |
> | **Compra Precio Regular**| $40$ | $10$ | $50$ | **$100$** |
> | **Total** | **$60$** | **$40$** | **[ ? ]** | **$200$** |
> 
> **Pregunta:** Primero, halle el valor faltante en el total de "Gasto > \$100". Luego, si seleccionamos un cliente que gastó más de $\$100$ USD, ¿cuál es la probabilidad de que haya pagado el **Precio Regular**?

---

> [!tip] 💡 Consejo de estudio
> Cuando los datos te confundan, **dibuja la Tabla de Contingencia**. Es la mejor forma de visualizar el "nuevo total". Recuerda siempre realizar la "prueba de fuego": las sumas de tus filas y columnas deben coincidir con el Gran Total en la esquina inferior derecha. Si la tabla cuadra, ¡tu resultado será correcto!