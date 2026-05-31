# Clase 05 — Regla de la suma | Unión de sucesos

#algebra #regladelasuma

Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 5 de 12

> [!info] 🧭 Navegación
> [[Clase 04|⬅ Clase 04]] | [[00 - Índice del curso|Índice]] | **Clase 05** | [[Clase 06|Clase 06 ➡]]

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> La unión de sucesos nos permite calcular la probabilidad de que ocurra al menos una de varias condiciones ("una cosa O la otra"). Es la herramienta clave para tomar decisiones cuando los escenarios no son excluyentes y queremos conocer nuestro alcance total.
> 
> *   **💵 [aplicación con $USD]:** Estimar la recaudación de una fiesta de 80 personas diferenciando ingresos por perfiles (ej. cobrar entrada premium de $10 USD a quienes cumplen ciertas condiciones).
> *   **🏗️ [aplicación práctica]:** Clasificar el inventario de una tienda de mascotas por especie y color para organizar los espacios de exhibición.
> *   **📊 [situación cotidiana]:** Maximizar las opciones de ganar en juegos de mesa al analizar múltiples resultados favorables en un solo lanzamiento de dados.

## Concepto clave

> [!note] 📌 ¿Qué es Regla de la suma?
> Es el cálculo de la probabilidad de que ocurra el suceso A **O** el suceso B. En matemáticas, la "O" significa **Unión**. El secreto didáctico es entender que si alguien cumple ambas condiciones al mismo tiempo, **no debemos contarlo dos veces**, ya que estaríamos "inflando" el resultado injustamente.

> [!warning] ⚠️ Error común
> El error más frecuente es sumar las probabilidades directamente y olvidar restar los elementos que se repiten en ambos grupos.
> *   ❌ **Incorrecto:** $P(A) + P(B)$
> *   ✅ **Correcto:** $P(A) + P(B) - P(A \cap B)$  *(Restar la intersección)*.

> [!tip] 💡 Truco para recordarlo
> Cuando veas la letra **"O"**, piensa en **"Unión"** y **"Suma"**. Pero aplica siempre la "Regla del Portero": suma a todos los invitados de la lista A y de la lista B, pero si un invitado está en ambas listas, ¡solo puede entrar una vez!

## Procedimiento paso a paso

La "Receta del Profe Alex" para no fallar nunca:

```text
PASO 0 → Realizar un chequeo visual (Diagrama de Venn mental) para ver si hay cruces.
PASO 1 → Identificar los dos sucesos (A y B) y el total de casos posibles.
PASO 2 → Hallar la probabilidad individual de cada suceso: P(A) y P(B).
PASO 3 → Identificar si hay elementos que cumplen ambos sucesos (Intersección A ∩ B).
PASO 4 → Aplicar la fórmula: P(A) + P(B) - P(A ∩ B) y simplificar el resultado.
```

## Ejemplos prácticos

> [!example] Ejemplo 1 — La Tienda de Mascotas
> En una tienda hay **15 animales** en total. Tenemos: 7 perros, 5 animales blancos y **3 perros que son blancos** (intersección).
> 
> **Pregunta:** ¿Cuál es la probabilidad de elegir un animal que sea Perro o Blanco?
> 1. $P(\text{Perro}) = 7/15$
> 2. $P(\text{Blanco}) = 5/15$
> 3. $P(\text{Perro} \cap \text{Blanco}) = 3/15$
> **Cálculo:** $7/15 + 5/15 - 3/15 = 9/15$.
> **Resultado final:** **3/5 (o 60%)**. Siempre busca la fracción más sencilla.

> [!example] Ejemplo 2 — Lanzamiento de Dado
> Al lanzar un dado de 6 caras, buscamos la probabilidad de obtener un número **par** o **mayor que 3**.
> - Sucesos pares: $\{2, \mathbf{4, 6}\}$ $\rightarrow 3/6$
> - Sucesos $> 3$: $\{\mathbf{4}, 5, \mathbf{6}\}$ $\rightarrow 3/6$
> - Intersección: $\{4, 6\}$ $\rightarrow 2/6$ (Son sucesos **mutuamente no excluyentes**).
> **Cálculo:** $3/6 + 3/6 - 2/6 = 4/6$.
> **Resultado final:** **2/3 (66.6%)**. Restamos el 4 y el 6 porque aparecían en ambos conteos.

> [!example] Ejemplo 3 — Características de la Población
> En una ciudad, el **60%** tiene ojos negros, el **80%** tiene cabello negro y el **50%** tiene ambas características.
> **Pregunta:** Probabilidad de que alguien tenga ojos o cabello negro.
> **Cálculo:** $60\% + 80\% - 50\% = \mathbf{90\%}$.

> [!example] Ejemplo 4 — Aplicación real con $USD
> En una fiesta de **80 personas**:
> - 40 son mayores de 20 años.
> - 10 son extranjeros.
> - 8 son extranjeros mayores de 20 años (intersección).
> 
> **Cálculo de probabilidad (>20 o extranjero):**
> $40/80 + 10/80 - 8/80 = 42/80 = \mathbf{21/40}$.
> 
> **Estimación de Ingresos:** Si decides cobrar una entrada premium de **$10 USD** a cualquier persona que sea mayor de 20 años o extranjera, y el resto paga **$5 USD**:
> - Personas Premium: 42 $\rightarrow 42 \times \$10 = \mathbf{\$420 \text{ USD}}$.
> - Personas Estándar: 38 (80 - 42) $\rightarrow 38 \times \$5 = \mathbf{\$190 \text{ USD}}$.
> - **Ingreso Total Estimado: $610 USD.**

## Ejercicios para el estudiante

> [!abstract] 🟢 Nivel Fácil: Dados
> 1. Probabilidad de obtener un 1 o un número mayor a 2.
> 2. Probabilidad de obtener un número impar o un 2.
> 3. Probabilidad de obtener un 6 o un número menor a 3.
> 4. Probabilidad de obtener un número mayor a 4 o un número par.

> [!abstract] 🟡 Nivel Medio: Tienda de Mascotas
> *Datos: 15 animales total (7 perros, 6 gatos, 2 conejos).*
> 1. Probabilidad de elegir un perro o un gato.
> 2. Probabilidad de elegir un gato o un conejo.
> 3. Probabilidad de elegir un perro o un conejo.
> 4. ¿Por qué en estos casos la intersección es 0? Explica usando el concepto de **Sucesos mutuamente excluyentes**.

> [!abstract] 🔴 Nivel Avanzado: La Cena
> *Datos para 60 personas:*
> 
> | Género | Comió Flan ($12) | Comió Torta ($15) | Total |
> | :--- | :---: | :---: | :---: |
> | **Mujeres** | 20 | 12 | 32 |
> | **Hombres** | 16 | 12 | 28 |
> | **Total** | 36 | 24 | 60 |
> 
> 1. Probabilidad de elegir una Mujer o alguien que comió Flan.
> 2. Probabilidad de elegir un Hombre o alguien que comió Torta.
> 3. Probabilidad de elegir a alguien que comió Torta o una Mujer.
> 4. Si el grupo de "Mujeres o personas que comieron Torta" debe pagar su cuenta, ¿cuál es el gasto total en $USD de ese grupo?

> [!success] ✅ Respuestas
> **Fácil:** 1) 5/6 | 2) 2/3 | 3) 1/2 | 4) 2/3.
> **Medio:** 1) 13/15 | 2) 8/15 | 3) 3/5 | 4) Porque un animal no puede ser perro y gato al mismo tiempo; son **mutuamente excluyentes**.
> **Avanzado:** 1) 4/5 (80%) | 2) 2/3 | 3) 11/15 | 4) **$600 USD**. 
> *Desglose: (20 mujeres-flan × $12) + (12 mujeres-torta × $15) + (12 hombres-torta × $15) = $240 + $180 + $180.*

## Mini-prueba de autoevaluación

> [!question] Pregunta 1: Conceptual
> ¿Qué operación matemática representa la "O" en los problemas de probabilidad?
> **Respuesta:** La suma (unión). Representa la acumulación de posibilidades.

> [!question] Pregunta 2: Procedimental
> Si el 60% de una población tiene ojos negros, ¿cuál es la probabilidad de que NO los tenga? ¿Cómo se llama esta regla?
> **Respuesta:** 40%. Se llama **Probabilidad Complementaria** (1 - P(A)). Es un adelanto de cómo calcular lo que queda fuera de un conjunto.

> [!question] Pregunta 3: Aplicación $USD
> En el ejemplo de la fiesta (80 personas), si la probabilidad de ser "mayor de 20 o extranjero" es 42/80, ¿cuántas personas pagarán la entrada estándar de $5 USD?
> **Respuesta:** 38 personas. Se obtiene restando el grupo de la unión del total: $80 - 42 = 38$.

> [!tip] 💡 En la próxima clase
> ¿Qué pasa si el resultado de un evento cambia las reglas del siguiente? Entraremos al mundo de los **Sucesos Dependientes y Probabilidad Condicional**.

> [!info] 🧭 Navegación
> [[Clase 04|⬅ Clase 04]] | [[00 - Índice del curso|Índice]] | **Clase 05** | [[Clase 06|Clase 06 ➡]]