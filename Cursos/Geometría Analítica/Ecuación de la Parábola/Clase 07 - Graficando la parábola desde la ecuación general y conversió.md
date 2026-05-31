# Clase 07 — Graficando la parábola desde la ecuación general y conversión de formas

#algebra #graphtheparabol
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 7 de 9

> [!info] 🧭 Navegación
> [[Clase 06|⬅ Clase 06]] | [[00 - Índice del curso|Índice]] | **Clase 07** | [[Clase 08|Clase 08 ➡]]

---

> [!info] 🌍 Relevancia y aplicaciones
> La parábola es la curva maestra de la naturaleza y la ingeniería; describe desde la caída de una gota de agua hasta el diseño de la tecnología que nos conecta con el espacio. Dominar su ecuación permite predecir el punto exacto de impacto o de máxima eficiencia.
> - 💵 **Aplicación $USD:** Permite modelar ganancias y encontrar el "punto dulce" (precio óptimo) para maximizar ingresos sin perder clientes.
> - 🏗️ **Aplicación práctica:** Vital para fabricar antenas parabólicas y faros de autos, donde la luz o señal rebota hacia un solo punto.
> - 📊 **Situación cotidiana:** Describe la trayectoria exacta de un balón de fútbol en un tiro libre o el arco de una fuente de agua.

---

> [!note] 📌 ¿Qué es graficar la parábola desde su ecuación general?
> Imagina que la **Ecuación General** es como una habitación donde todos los muebles están amontonados y pegados a la pared, igualados a cero (un desorden total). Graficar es el proceso de "ordenar el desorden": pasamos esa mezcla a una **Ecuación Canónica** para poder ver claramente dónde está el vértice y hacia dónde abre la curva. Es como poner cada mueble en su sitio para entender el espacio.

> [!warning] ⚠️ Error común
> **Incorrecto:** Olvidar cambiar los signos al extraer el vértice $(h, k)$ de la ecuación canónica.
> **Correcto:** El vértice siempre usa el signo opuesto al valor que acompaña a $x$ y $y$ en el paréntesis. Si la ecuación dice $(x - 3)^2 = 8(y + 2)$, el vértice es $(3, -2)$.

> [!tip] 💡 Truco para recordarlo
> Para saber hacia dónde abre el camino de la parábola: **"La letra que NO está al cuadrado te indica el eje del camino"**.
> - Si la $x$ no tiene cuadrado, la parábola es **Horizontal** (abre a derecha o izquierda).
> - Si la $y$ no tiene cuadrado, la parábola es **Vertical** (abre hacia arriba o abajo).

---

### Procedimiento Paso a Paso: De General a Canónica

Para transformar la ecuación y poder graficar, necesitamos "Completar el Trinomio", que es como encontrar la pieza faltante de un rompecabezas para formar un cuadrado perfecto.

```text
PASO 1 → Agrupar: Deja los términos de la variable al cuadrado a la izquierda y pasa todo lo demás a la derecha (cambiando sus signos).
PASO 2 → Completar el Trinomio: Toma el número de la variable lineal, divídelo entre 2 y elévalo al cuadrado. 
          ***REGLA DE ORO: Lo que sumes a la izquierda, DEBES sumarlo también a la derecha para mantener el balance.***
PASO 3 → Factorizar: Convierte el lado izquierdo en un binomio al cuadrado y el lado derecho mediante factor común numérico.
PASO 4 → Identificar: Extrae el Vértice (h, k), calcula p (donde 4p es el factor común) y determina la dirección.
```

---

### Bloques de Ejemplos Prácticos

> [!example] Ejemplo 1: Caso Básico (Eje Vertical)
> **Problema:** Graficar $x^2 - 6x - 8y - 7 = 0$.
> 1. **Agrupamos:** $x^2 - 6x = 8y + 7$.
> 2. **Completamos:** La mitad de $6$ es $3$, y $3^2 = 9$. **Sumamos 9 en ambos lados:**
>    $x^2 - 6x + 9 = 8y + 7 + 9 \rightarrow x^2 - 6x + 9 = 8y + 16$.
> 3. **Factorizamos:** $(x - 3)^2 = 8(y + 2)$.
> 4. **Elementos:** 
>    - Vértice: $V(3, -2)$.
>    - Parámetro: $4p = 8$, entonces $p = 2$ (esta es la distancia del vértice al foco).
>    - Dirección: Como $y$ es positiva y no tiene cuadrado, abre hacia **arriba**.

> [!example] Ejemplo 2: Signos y Dirección (Eje Horizontal)
> **Problema:** Resolver $y^2 + 6y + 4x + 17 = 0$.
> 1. **Agrupamos:** $y^2 + 6y = -4x - 17$.
> 2. **Completamos:** La mitad de $6$ es $3$, y $3^2 = 9$.
>    $y^2 + 6y + 9 = -4x - 17 + 9 \rightarrow (y + 3)^2 = -4x - 8$.
> 3. **Factor común:** $(y + 3)^2 = -4(x + 2)$.
> 4. **Resultado:** El vértice es $V(-2, -3)$. Como el factor es $-4$ y la $x$ no tiene cuadrado, abre hacia la **izquierda** (lado negativo de $x$).

> [!example] Ejemplo 3: Conversión Canónica a General
> **Problema:** Transformar $(y + 2)^2 = 4(x - 3)$ a forma general.
> 1. **Expandir binomio:** $y^2 + 4y + 4$.
> 2. **Distribuir derecha:** $4x - 12$.
> 3. **Igualar a cero:** $y^2 + 4y + 4 - 4x + 12 = 0$.
> 4. **Orden final:** $y^2 - 4x + 4y + 16 = 0$.

> [!example] Ejemplo 4: Aplicación $USD (Máxima Ganancia)
> **Problema:** Una empresa modela su ganancia semanal con $x^2 - 100x + 20y - 2000 = 0$, donde $x$ es el precio en $USD$. Halla el precio de máxima ganancia.
> 1. **Procedimiento:** $x^2 - 100x = -20y + 2000$.
> 2. **Completar:** $(100/2)^2 = 2500$. Sumamos 2500 a ambos lados.
>    $(x - 50)^2 = -20y + 4500 \rightarrow (x - 50)^2 = -20(y - 225)$.
> 3. **Análisis:** El vértice es $V(50, 225)$. 
> 4. **Lógica de mercado:** Como el signo de $4p$ es negativo ($-20$), la parábola es una **"U" invertida**. Esto significa que el vértice es el punto más alto (el pico).
> **Conclusión:** El precio óptimo es **$50 USD**, logrando una ganancia máxima de $225 USD.

---

### Ejercicios de Práctica

**🟢 Nivel Fácil: Identificar dirección**
1. $x^2 - 4x - 4y = 0$
2. $y^2 + 8y + 2x + 4 = 0$
3. $x^2 + 2x + 6y + 10 = 0$
4. $y^2 - 10y - 12x + 1 = 0$

**🟡 Nivel Medio: Convertir a Canónica y hallar Vértice**
5. $x^2 - 10x - 12y + 1 = 0$
6. $y^2 - 4y + 8x + 28 = 0$
7. $x^2 + 6x + 4y + 5 = 0$
8. $y^2 + 10y - 4x + 9 = 0$

**🔴 Nivel Avanzado: Problemas razonados ($USD)**
9. Una antena tiene forma $(x - 20)^2 = -10(y - 50)$. Pásala a forma general.
10. Un modelo de costos es $(x - 10)^2 = 12(y - 5)$. Pásalo a forma general.
11. Maximizar ingresos: $x^2 - 60x + 15y - 900 = 0$. Halla el vértice.
12. Convertir a general: $(y + 5)^2 = -8(x - 2)$.

> [!success] Respuestas para el docente
> 1. Vertical (Arriba) | 2. Horizontal (Izquierda) | 3. Vertical (Abajo) | 4. Horizontal (Derecha)
> 5. $(x-5)^2 = 12(y+2), V(5,-2)$ | 6. $(y-2)^2 = -8(x+3), V(-3,2)$ | 7. $(x+3)^2 = -4(y-1), V(-3,1)$ | 8. $(y+5)^2 = 4(x+4), V(-4,-5)$
> 9. $x^2 - 40x + 10y + 900 = 0$ | 10. $x^2 - 20x - 12y + 160 = 0$ | 11. $V(30, 120)$ | 12. $y^2 + 8x + 10y + 9 = 0$

---

### Autoevaluación

> [!question] 🧪 Pregunta 1
> En la ecuación $y^2 - 8x + 16 = 0$, ¿hacia dónde abre la curva?
> **Respuesta:** Abre hacia la derecha.
> **Explicación:** La variable lineal (sin cuadrado) es $x$. Al despejar, queda $8x$ (positivo), indicando el eje $x$ derecho.

> [!question] 🧪 Pregunta 2
> ¿Qué número completa el trinomio en $x^2 + 14x$?
> **Respuesta:** 49.
> **Explicación:** Se toma la mitad de 14 (7) y se eleva al cuadrado ($7^2 = 49$). Este es el "puzzle piece" faltante.

> [!question] 🧪 Pregunta 3
> Si una ecuación de ganancias es $(x - 25)^2 = -5(y - 800)$, ¿cuál es el precio de mayor éxito?
> **Respuesta:** $25 USD$.
> **Explicación:** El vértice $(25, 800)$ marca el punto máximo porque la parábola abre hacia abajo (signo negativo).

---

> [!tip] 💡 En la próxima clase
> Ya sabes transformar y graficar desde el desorden de la ecuación general. En la Clase 08, aprenderás a construir la ecuación desde cero usando solo dos pistas: el **Foco** y la **Directriz**.

> [!info] 🧭 Navegación
> [[Clase 06|⬅ Clase 06]] | [[00 - Índice del curso|Índice]] | **Clase 07** | [[Clase 08|Clase 08 ➡]]