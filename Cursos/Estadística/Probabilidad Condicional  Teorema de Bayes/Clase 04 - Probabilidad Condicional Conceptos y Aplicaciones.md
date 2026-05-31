# Clase 04 — Probabilidad Condicional: Conceptos y Aplicaciones

#algebra #probabilidadcon

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 4 de 9

> [!info] 🧭 Navegación
> ⬅️ [[Clase 03 - Regla de la Multiplicación]] | 🏠 [[00 - Índice del curso]] | [[Clase 05 - Teorema de Probabilidad Total]] ➡️

---

### ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> La probabilidad condicional es nuestra herramienta para actualizar lo que sabemos. En la vida real, raramente tomamos decisiones "a ciegas"; casi siempre tenemos una pista extra que cambia nuestras expectativas.
> 
> - **💵 [aplicación con $USD]:** Probabilidad de que una inversión supere los $100 USD de ganancia si sabemos que el mercado cerró al alza (la pista del mercado reduce la incertidumbre).
> - **🏗️ [aplicación práctica]:** En una fábrica, la probabilidad de que una pieza sea defectuosa dado que fue fabricada por la "Máquina B" (que es más antigua que la A).
> - **📊 [situación cotidiana]:** Diagnósticos médicos: la probabilidad de tener una enfermedad dado que el test resultó positivo.

---

### Concepto Clave

> [!note] 📌 ¿Qué es Probabilidad Condicional?
> ¡Hola, amigas y amigos! Imaginen que estamos jugando a las adivinanzas. La probabilidad condicional no es más que calcular la posibilidad de que algo ocurra, pero utilizando una **pista o información extra** que ya conocemos.
> 
> Esta pista hace que nuestro "universo" de posibilidades se haga más pequeño. Técnicamente, a esto lo llamamos trabajar con un **Espacio Muestral Reducido**. Seguimos aplicando la **Regla de Laplace**, pero con un ajuste lógico:
> 
> $$\text{Probabilidad} = \frac{\text{Casos Favorables (dentro de la pista)}}{\text{Espacio Muestral Reducido (el grupo de la pista)}}$$

> [!warning] ⚠️ Error común
> **❌ Incorrecto:** Seguir usando el total de toda la población cuando ya nos dieron un dato que descarta a una parte.
> **✅ Correcto:** "Olvidar" a todos los que no cumplen con la condición. Tu nuevo "total" es solo el grupo que cumple la pista.

> [!tip] 💡 Truco para recordarlo: La Regla de la "Pista"
> Si en un problema lees frases como *"se sabe que..."*, *"si es que..."* o *"dado que..."*, ¡detente! Esa es tu pista. Olvida el resto del mundo y concéntrate únicamente en ese grupo. Lo que esté fuera de la pista ya no existe para tu cálculo.

---

### Procedimiento Paso a Paso

Sigue esta secuencia lógica para no perderte nunca en la fórmula:

```text
PASO 1 → Identificar la condición o "pista" (lo que ya sabemos que ocurrió).
PASO 2 → Definir el Espacio Muestral Reducido (el nuevo denominador es solo el grupo de la condición).
PASO 3 → Contar cuántos elementos de ese nuevo grupo cumplen con lo que queremos hallar (numerador).
PASO 4 → Dividir y expresar en fracción, decimal o porcentaje.
```

---

### Bloques de Ejemplos

> [!example] Ejemplo 1: El caso de la urna (Prueba Visual)
> **Problema:** En una urna hay 10 esferas: 6 azules y 4 rojas. Las azules tienen los números $\{1, 3, 4, 6, 8, 10\}$. Si sacamos una esfera y vemos que es **azul**, ¿cuál es la probabilidad de que sea un número **par**?
> 
> **Lógica del Profe Alex:**
> 1. **Condición:** "Es azul". Ignoramos las 4 rojas. 
> 2. **Denominador:** Nuestro universo ahora son solo las 6 esferas azules.
> 3. **Prueba visual (Numerador):** De las azules $\{1, 3, 4, 6, 8, 10\}$, ¿cuántas son pares? Contamos: el 4, el 6, el 8 y el 10. Son **4 esferas**.
> 4. **Resultado:** $\frac{4}{6} = \frac{2}{3} \approx 66.6\%$.

> [!example] Ejemplo 2: Rasgos físicos (Uso de Porcentajes)
> **Problema:** El 40% de una población tiene cabello castaño, el 25% tiene ojos castaños y el 15% tiene ambos. Si elegimos a alguien que tiene **ojos castaños**, ¿cuál es la probabilidad de que tenga cabello castaño?
> 
> **Lógica:**
> - **Pista:** Tiene ojos castaños ($25\%$). Este es nuestro denominador.
> - **Favorable:** Los que tienen ojos castaños Y además cabello castaño ($15\%$).
> - **Cálculo:** $\frac{15\%}{25\%}$. Simplificamos el símbolo $\%$ y dividimos: $\frac{15}{25} = \frac{3}{5} = 0.6 = 60\%$.

> [!example] Ejemplo 3: Deportes y la trampa del "únicamente" (Avanzado)
> **Problema:** En un club, el 40% juega Fútbol, el 35% juega **únicamente** Baloncesto y el 15% juega ambos. Si elegimos a alguien que juega **Baloncesto**, ¿probabilidad de que juegue Fútbol?
> 
> **Lógica:**
> - **Ojo con la pista:** Para el denominador necesitamos a TODOS los de Baloncesto. El problema dice que el 35% juega *solo* baloncesto y el 15% juega *ambos*. Entonces, el total de baloncesto es $35\% + 15\% = 50\%$.
> - **Numerador:** Los que juegan fútbol dentro de ese grupo (los del "ambos"): $15\%$.
> - **Resultado:** $\frac{15}{50} = \frac{3}{10} = 30\%$.

> [!example] Ejemplo 4: Electrónica y Precios ($USD)
> **Problema:** El 60% de los productos de una tienda cuestan más de $10 USD. El 20% son electrónicos con precio mayor a $10 USD. Si compras un producto de **más de $10 USD**, ¿cuál es la probabilidad de que sea electrónico?
> 
> **Lógica:**
> - **Condición:** Precio $> 10$ USD ($60\%$).
> - **Favorable:** Electrónico y $> 10$ USD ($20\%$).
> - **Resultado:** $\frac{20}{60} = \frac{1}{3} \approx 33.3\%$.

---

### Ejercicios para el estudiante

#### 🟢 Nivel Fácil (Urnas y Esferas)
1. Urna con 10 esferas (5 verdes, 5 amarillas). De las verdes, los números son $\{2, 4, 6, 7, 9\}$. Probabilidad de par dado que es verde.
2. Urna con 12 esferas (8 azules, 4 rojas). De las azules, 6 son pares. Probabilidad de par dado que es azul.
3. Urna con 8 esferas (4 azules, 4 rojas). De las azules, las pares son $\{2, 8\}$. Probabilidad de par dado que es azul.
4. Urna con 10 esferas (6 azules, 4 rojas). De las azules, 4 son pares. Probabilidad de **impar** dado que es azul.

#### 🟡 Nivel Medio (Porcentajes y Conjuntos)
5. 30% estudia Inglés, 20% Francés y 10% ambos. Probabilidad de Inglés dado que estudia Francés.
6. 50% practica Danza, 40% Canto y 20% ambos. Probabilidad de Danza dado que practica Canto.
7. 60% prefiere Pizza, 40% Hamburguesa y 30% ambos. Probabilidad de Pizza dado que prefiere Hamburguesa.
8. 45% prefiere Tecnología, 35% Ciencias y 15% ambos. Probabilidad de Tecnología dado que prefiere Ciencias.

#### 🔴 Nivel Avanzado (Términos "únicamente" y $USD)
9. 40% juega Fútbol, 10% juega **únicamente** Baloncesto y 15% ambos. Probabilidad de Fútbol dado que juega Baloncesto.
10. 30% usa Netflix, 20% usa **únicamente** Disney+ y 10% ambos. Probabilidad de Netflix dado que usa Disney+.
11. En una tienda, el 50% gasta más de $50 USD. El 20% gasta más de $50 USD y compra libros. Probabilidad de comprar libros dado que gastó más de $50 USD.
12. El 70% de las ventas son 'Suscripción Premium' ($100 USD). El 30% del total de ventas son 'Premium' realizadas por 'Empresas'. Probabilidad de que el cliente sea 'Empresa' dado que compró 'Premium'.

#### ✅ Respuestas y Lógica
1. **3/5 (60%)** | 2. **6/8 = 3/4 (75%)** | 3. **2/4 = 1/2 (50%)** | 4. **2/6 = 1/3 (33.3%)**
5. **10/20 = 50%** | 6. **20/40 = 50%** | 7. **30/40 = 75%** | 8. **15/35 = 3/7 (42.8%)**
9. **15/25 = 60%** (Denominador: $10\% \text{ únicamente} + 15\% \text{ ambos} = 25\%$).
10. **10/30 = 33.3%** (Denominador: $20\% \text{ únicamente} + 10\% \text{ ambos} = 30\%$).
11. **20/50 = 40%** | 12. **30/70 = 3/7 (42.8%)**

---

### Mini-prueba de autoevaluación

1. **Conceptual:** Cuando aplicamos probabilidad condicional, ¿el denominador aumenta, disminuye o se mantiene igual respecto a la probabilidad simple?
2. **Procedimental:** Si $P(A \cap B) = 0.1$ y $P(B) = 0.5$, ¿cuál es la probabilidad de $A$ dado $B$? (Calcula $\frac{0.1}{0.5}$).
3. **Aplicación $USD:** Un restaurante da cupones al 20% de sus clientes. El 10% del total de clientes recibe cupón **y** gasta más de $100 USD. Si un cliente tiene un cupón, ¿cuál es la probabilidad de que haya gastado más de $100 USD?

---

> [!tip] 💡 En la próxima clase
> Ya sabemos ajustar probabilidades con una pista. En la próxima lección veremos cómo sumar varias de estas condiciones para resolver problemas más complejos usando el **Teorema de Probabilidad Total**. ¡Allí nos vemos!

> [!info] 🧭 Navegación
> ⬅️ [[Clase 03 - Regla de la Multiplicación]] | 🏠 [[00 - Índice del curso]] | [[Clase 05 - Teorema de Probabilidad Total]] ➡️