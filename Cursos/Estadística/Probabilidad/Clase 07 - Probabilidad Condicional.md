# Clase 07 — Probabilidad Condicional

#algebra #probabilidadcon

Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 7 de 12

> [!info] 🧭 Navegación
> ◀ Lección anterior: [[06 - Regla de la Multiplicación]]
> 🏠 Inicio: [[00 - Índice del curso]]
> ▶ Próxima lección: [[08 - Teorema de Bayes]]

---

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> La probabilidad condicional nos permite ajustar nuestras predicciones y modelos cuando recibimos "pistas" o información nueva. En lugar de trabajar con una población total, aprendemos a segmentar y analizar un **universo reducido** basado en hechos ya conocidos.

*   **💵 Aplicación $USD:** En finanzas, se usa para calcular el **riesgo crediticio**. La probabilidad de impago de una deuda bancaria se recalcula constantemente según el historial del cliente (la condición).
*   **🏗️ Aplicación práctica:** En el **control de calidad**, permite determinar la probabilidad de que una pieza sea defectuosa dado que salió de una máquina específica que ha reportado fallas.
*   **📊 Situación cotidiana:** En **diagnósticos médicos**, es vital para entender la probabilidad de tener una enfermedad dado un resultado positivo en un test.

---

## Concepto clave

> [!note] 📌 ¿Qué es Probabilidad Condicional?
> Es la probabilidad de que ocurra un evento (A), sabiendo de antemano que ya ha ocurrido otro evento (B). Conceptualmente, la condición actúa como un **filtro** que descarta los elementos que no cumplen la pista, reduciendo el espacio muestral original.
> 
> Matemáticamente se expresa mediante la fórmula:
> $$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

> [!tip] 💡 Palabras Gatillo (Trigger Words)
> Para identificar un problema de probabilidad condicional, busca estas frases en el enunciado:
> - "Dado que..."
> - "Sabiendo que..."
> - "Si se sabe que..."
> - "Si ocurrió que..."

> [!warning] ⚠️ Error común
> El error más frecuente es no actualizar el denominador. Por ejemplo, en una urna de 10 esferas donde 6 son azules, si la condición es que "sea azul", el **espacio muestral original ($S=10$)** desaparece y es reemplazado por un **nuevo espacio muestral ($S=6$)**. Usar el total inicial en el denominador invalidará todo el cálculo.

> [!tip] 💡 Truco para recordarlo
> Utiliza la regla mnemotécnica: **"La condición siempre va abajo"**. En la expresión $P(A|B)$, el evento $B$ es lo que ya pasó y, por lo tanto, es el que divide en el denominador.

---

## Procedimiento paso a paso

> [!abstract] Procedimiento Técnico
> 1. **Identificar la condición:** Localizar el evento que ya ocurrió (el "filtro").
> 2. **Definir el nuevo espacio muestral:** Determinar el denominador contando cuántos elementos cumplen la condición.
> 3. **Identificar la intersección:** Determinar el numerador buscando cuántos elementos cumplen la condición **Y** el evento buscado simultáneamente.
> 4. **Dividir y expresar:** Realizar la división y expresar el resultado en fracción (simplificada), decimal o porcentaje.

---

## Ejemplos prácticos

````ad-example
**Ejemplo 1: Caso Básico (Esferas en una Urna)**
En una urna hay **10 esferas** numeradas del 1 al 10. Se sabe que **6 son azules** (1, 3, 4, 6, 8, 10) y **4 son rojas** (2, 5, 7, 9). Si sacamos una esfera y vemos que es **azul**, ¿cuál es la probabilidad de que sea un número **par**?

**Resolución por Lógica (Universo Reducido):**
*   **Nuevo espacio muestral:** Solo las 6 azules {1, 3, 4, 6, 8, 10}.
*   **Casos favorables (pares dentro de las azules):** {4, 6, 8, 10} = 4 casos.
*   **Cálculo:**
$$\frac{4}{6} = \frac{2}{3} \approx 66.6\%$$

**Resolución por Fórmula:**
*   $P(Azul) = 6/10$
*   $P(Par \cap Azul) = 4/10$
*   $P(Par|Azul) = \frac{4/10}{6/10} = \frac{4}{6} = \frac{2}{3}$
````

````ad-example
**Ejemplo 2: Caso con Porcentajes (Rasgos Físicos)**
El **40%** tiene cabello castaño, el **25%** tiene ojos castaños y el **15%** tiene ambos. Si elegimos a alguien con **ojos castaños**, ¿probabilidad de tener **cabello castaño**?
*   **Condición:** Ojos castaños (25% o 0.25).
*   **Intersección:** Ambos (15% o 0.15).
*   **Cálculo:** $15 / 25 = 3 / 5 = 0.60 \rightarrow$ **60%**.
````

````ad-example
**Ejemplo 3: Caso Avanzado (Deportes y "Únicamente")**
El 40% practica fútbol y el 15% practica ambos. El **50% practica únicamente baloncesto**. Si seleccionamos a alguien que practica **baloncesto**, ¿probabilidad de que practique **fútbol**?
*   **Denominador (Total Baloncesto):** Sumamos los que practican "únicamente baloncesto" (50%) + los que practican "ambos" (15%) = **65%**.
*   **Intersección:** Practica ambos (15%).
*   **Cálculo:** $15 / 65 = 3 / 13 \approx 23\%$.
````

````ad-example
**Ejemplo 4: Aplicación Real $USD (E-commerce)**
El **30%** de los productos son de **Electrónica**. El **10%** del total general son Electrónica con **descuento**. Si compramos algo de **Electrónica**, ¿probabilidad de que tenga descuento?
*   **Condición:** Electrónica (30%).
*   **Intersección:** Electrónica + Descuento (10%).
*   **Cálculo:** $10 / 30 = 1 / 3 \approx 33.3\%$.
````

---

## Ejercicios para el estudiante

### Bloque Verde (Fácil - Urna de esferas)
1. En la urna de 10 esferas (6 azules, 4 rojas), ¿probabilidad de que sea **roja** dado que es **par**?
2. Probabilidad de que sea **impar** dado que es **azul**.
3. Probabilidad de que sea **mayor a 7** dado que es **roja**.
4. Probabilidad de que sea **azul** dado que es **menor a 4**.

### Bloque Amarillo (Medio - Porcentajes)
1. El 30% habla inglés, el 20% francés y el 10% ambos. Si alguien habla **inglés**, ¿probabilidad de que hable **francés**?
2. Si habla **francés**, ¿probabilidad de que hable **inglés**?
3. El 60% aprobó Matemáticas, el 40% Física y el 20% ambas. Si aprobó **Física**, ¿probabilidad de aprobar **Matemáticas**?
4. Según los datos del ejercicio anterior, ¿qué porcentaje de la población **no aprobó ninguna**?

### Bloque Rojo (Avanzado - $USD)
1. El 60% de artículos cuestan >**$100 USD**. El 20% del total son artículos de >**$100 USD** con **garantía**. Probabilidad de garantía dado que cuesta >**$100 USD**.
2. Un banco reporta que el 15% de clientes tiene **hipoteca** y **tarjeta**. Si el 40% tiene tarjeta, ¿probabilidad de que alguien con tarjeta tenga hipoteca?
3. El 25% de productos son **importados**. El 80% de los importados cuesta >**$50 USD**. ¿Probabilidad de que un producto al azar sea importado Y cueste >**$50 USD**?
4. El 10% de los productos totales son **nacionales** y cuestan >**$50 USD**. Si el resto de productos nacionales cuestan menos, ¿probabilidad de que un producto cueste >**$50 USD** dado que es **nacional**?

````ad-success
**Soluciones para el docente**
*   **Verde:** 1) 1/5 (20%), 2) 2/6 (33.3%), 3) 1/4 (25%), 4) 2/3 (66.6%).
*   **Amarillo:** 1) 10/30 (33.3%), 2) 10/20 (50%), 3) 20/40 (50%), 4) 20%.
*   **Rojo:** 
    *   1) 20/60 (33.3%).
    *   2) 15/40 (37.5%).
    *   3) 20% (Cálculo: $0.25 \times 0.80$).
    *   4) **13.3%**. Desglose: Población Nacional = 100% - 25% (importados) = **75**. Intersección (Nacional y >$50) = **10**. Cálculo: $10 / 75 = 0.1333$.
````

---

## Mini-prueba de autoevaluación

````ad-question
**1. Conceptual: ¿Qué representa el denominador en una probabilidad condicional?**
1. El espacio muestral original de toda la población.
2. La probabilidad de la intersección entre ambos eventos.
3. El nuevo espacio muestral limitado por la condición.

**Respuesta:** 3. La condición actúa como un filtro que reduce el universo de estudio.
````

````ad-question
**2. Procedimental: En la expresión $P(X|Y)$, ¿cuál es el evento que ya ocurrió?**
1. El evento X.
2. El evento Y.
3. Ambos ocurren al mismo tiempo.

**Respuesta:** 2. Por convención y mnemotecnia, la condición es el segundo término y va "abajo".
````

````ad-question
**3. Aplicación $USD: Un activo tiene 20% de probabilidad de subir. El mercado es alcista el 50% de las veces. Si la probabilidad de que ambos ocurran es 15%, ¿probabilidad de que el activo suba dado que el mercado es alcista?**
1. 30%
2. 7.5%
3. 15%

**Respuesta:** 1. Cálculo: $15\% / 50\% = 0.30$ (30%).
````

---

## Notas para el próximo tema

> [!tip] 💡 En la próxima clase
> Conectaremos la probabilidad condicional con el **Teorema de Bayes**. Aprenderemos cómo "invertir" la condición: si sabemos la probabilidad de A dado B, ¿cómo calculamos la de B dado A?

---
> [!info] 🧭 Navegación
> ◀ Lección anterior: [[06 - Regla de la Multiplicación]]
> 🏠 Inicio: [[00 - Índice del curso]]
> ▶ Próxima lección: [[08 - Teorema de Bayes]]