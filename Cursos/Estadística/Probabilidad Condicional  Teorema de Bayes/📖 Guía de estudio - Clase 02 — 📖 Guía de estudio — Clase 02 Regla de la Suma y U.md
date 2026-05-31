# 📖 Guía de estudio — Clase 02: Regla de la Suma y Unión de Sucesos

¡Qué tal, amigas y amigos! Espero que estén muy bien. En esta guía vamos a profundizar en un tema que a veces parece confuso, pero que con dibujos y orden se vuelve muy sencillo: la **Unión de Sucesos**. Aprenderemos a calcular la probabilidad de que ocurra una cosa **o** la otra. ¡Vamos a darle!

> [!info] 📌 Conceptos clave
> 1.  **La clave está en la "o":** Siempre que en un ejercicio leas que buscamos la probabilidad de que ocurra "esto **o** aquello", estamos hablando de una **unión**. Visualmente, es como juntar dos grupos en uno solo.
> 2.  **¡Cuidado con la doble cuenta!:** Este es el error más común. Si algunos elementos cumplen las dos condiciones al mismo tiempo (intersección), al sumar los grupos los estarás contando dos veces. ¡Por eso siempre debemos restar esa intersección!
> 3.  **Sucesos Mutuamente Excluyentes:** Si dos eventos no tienen nada en común (como que un animal sea perro y gato a la vez), se dice que son mutuamente excluyentes. En este caso, la intersección es cero.
> 4.  **Organización con herramientas:** Para no perdernos, usamos **Diagramas de Venn** (círculos) para ver el solapamiento, o **Tablas de Contingencia**, donde los totales de cada grupo se ubican siempre al final de las filas y columnas.

---

## Fórmulas y Definiciones Importantes

| Término | Símbolo / Fórmula | Definición simple |
| :--- | :--- | :--- |
| **Unión de sucesos** | $P(A \cup B)$ | Probabilidad de que ocurra el suceso A, el suceso B o ambos. |
| **Intersección** | $P(A \cap B)$ | Elementos que pertenecen a ambos conjuntos a la vez (lo que se repite). |
| **Regla de la suma** | $P(A) + P(B) - P(A \cap B)$ | Fórmula general. Si los sucesos son **mutuamente excluyentes**, la intersección es $0$. |
| **Espacio muestral** | $S$ o Total de casos | El universo completo de todos los resultados posibles. |

---

## Ejemplos Resueltos Adicionales

> [!example] Ejemplo A: Lanzamiento de un dado (Caso con intersección)
> **Problema:** Si lanzas un dado de 6 caras, ¿cuál es la probabilidad de obtener un número que sea **par o mayor a 3**?
> 
> **Paso 1: Identificar casos favorables por separado.**
> *   Números pares (A): {2, 4, 6} → $P(A) = 3/6$
> *   Números mayores a 3 (B): {4, 5, 6} → $P(B) = 3/6$
> 
> **Paso 2: Identificar la intersección.**
> *   ¿Qué números son pares **y** mayores a 3? Son el {4, 6}.
> *   Intersección ($A \cap B$) = 2 casos → $P(A \cap B) = 2/6$
> 
> **Paso 3: Aplicar la fórmula.**
> *   $P(A \cup B) = \frac{3}{6} + \frac{3}{6} - \frac{2}{6} = \frac{4}{6}$
> 
> **Resultado Final:** 
> *   Simplificando: **2/3**
> *   En porcentaje: **66.6%**

> [!example] Ejemplo B: Tienda de Electrónica (Uso de datos reales)
> **Problema:** En una tienda hay 80 productos. La mitad cuestan más de $20 USD. Hay 10 productos importados, y de esos importados, 8 cuestan más de $20 USD. ¿Cuál es la probabilidad de elegir un producto **Importado o que cueste más de $20 USD**?
> 
> **Desglose paso a paso:**
> 1.  $P(\text{Importado}) = 10/80$
> 2.  $P(>20\text{ USD}) = 40/80$ (la mitad de 80).
> 3.  $P(\text{Importado} \cap >20\text{ USD}) = 8/80$ (estos productos están en ambas categorías).
> 
> **Cálculo:**
> $P = \frac{10}{80} + \frac{40}{80} - \frac{8}{80} = \frac{42}{80}$
> 
> **Simplificación para mis amigas y amigos:**
> *   Dividimos ambos números por 2: $42 \div 2 = 21$ y $80 \div 2 = 40$.
> *   Resultado en fracción: **21/40**
> *   Resultado en porcentaje: **52.5%**

---

## Ejercicios de Repaso

> [!abstract] 📝 ¡Pon a prueba tu conocimiento!
> 
> ### 🟢 Nivel Verde (Fácil - Dados)
> 1.  Calcula la probabilidad de obtener un número **primo o mayor a 2**.
> 2.  Calcula la probabilidad de obtener un **1 o un número mayor a 2**.
> 3.  Calcula la probabilidad de obtener un número **par o impar**.
> 
> ### 🟡 Nivel Amarillo (Medio - Tienda de Mascotas)
> *Datos: Total 15 animales (7 perros, 6 gatos, 2 conejos). Hay 5 animales blancos en total, y de ellos, 3 son perros blancos.*
> 1.  ¿Cuál es la probabilidad de elegir un **perro o un animal blanco**?
> 2.  ¿Cuál es la probabilidad de elegir un **perro o un gato**? (Recuerda: no hay perros-gatos).
> 3.  ¿Cuál es la probabilidad de elegir un **conejo o un gato**?
> 
> ### 🔴 Nivel Rojo (Avanzado - Venta de Garaje)
> *Contexto: Hay 60 artículos en total. 32 son de mujer y 28 de hombre. Se pagaron 36 artículos en efectivo ($USD) y los demás con tarjeta. Sabemos que 20 artículos de mujer se pagaron en efectivo.*
> 1.  Si eliges un artículo al azar, ¿cuál es la probabilidad de que sea **de Mujer o haya sido pagado en Efectivo**?

> [!success] ✅ Clave de respuestas (Verifica tu lógica)
> *   **Nivel Verde:** 1) 5/6 (83.3%), 2) 5/6 (83.3%), 3) 6/6 (100%).
> *   **Nivel Amarillo:** 1) 9/15 = 3/5 (60%), 2) 13/15 (86.6%), 3) 8/15 (53.3%).
> *   **Nivel Rojo:** 1) 48/60 = 4/5 (80%).
>     *   *Lógica:* $32/60 (\text{Mujer}) + 36/60 (\text{Efectivo}) - 20/60 (\text{Ambos}) = 48/60$.

---

> [!tip] 💡 Consejo de estudio: ¡Dibuja primero!
> Como siempre les digo, **no intenten resolver de memoria**. Dibujen los círculos (Venn). La clave maestra es: **empiecen siempre por el centro**. Coloquen primero el número de la intersección (los que cumplen ambas cosas). Luego, completen los lados restando ese centro al total de cada grupo. Esto les asegura que nunca contarán a la misma persona o cosa dos veces. ¡Hacer el dibujo es entender el problema!