# Guía de estudio — Clase 08: Inecuaciones con Valor Absoluto

> [!info] 📌 Conceptos clave
> - **Definición de Valor Absoluto:** Es la magnitud de un número sin tomar en cuenta su signo, representada técnicamente como su **distancia respecto al origen (cero)** en la recta numérica. Al ser una distancia, el resultado siempre es positivo o cero.
> - **Condición de aplicación:** Las fórmulas estándar se aplican cuando el valor absoluto se compara con un número positivo ($a > 0$).
> - **Casos con números negativos:** 
> 	- Si tenemos $|x| < a$ y $a$ es negativo: La solución es el **conjunto vacío ($\emptyset$)**, pues un valor positivo nunca será menor que uno negativo.
> 	- Si tenemos $|x| > a$ y $a$ es negativo: La solución son **todos los números reales ($\mathbb{R}$)**, ya que cualquier valor absoluto siempre será mayor que un número negativo.
> - **Sentido de la desigualdad:** El procedimiento varía según el símbolo: "mayor que" ($>$) implica una **unión** de intervalos, mientras que "menor que" ($<$) implica un **intervalo acotado** (sándwich).

---

## 2. TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Valor Absoluto** | La magnitud de un número sin signo, representada por su distancia al origen. |
| **Caso Mayor que ($|x| > a$)** | Se descompone en la unión de dos inecuaciones separadas: $x < -a \cup x > a$. |
| **Caso Menor que ($|x| < a$)** | Se resuelve mediante la fórmula de **"sándwich"**: $-a < x < a$. |
| **Notación de Intervalos** | **Corchetes** $[ ]$ para $\leq$ o $\geq$ (cerrado/incluye extremo). **Paréntesis** $( )$ para $<$ o $>$ (abierto/excluye extremo). |

---

## 3. EJEMPLOS RESUELTOS

```ad-example
title: Ejemplo A — Caso con símbolo Mayor que
**Ejercicio:** Resolver $|x + 5| \geq 3$

**Procedimiento:**
1. **Identificar la fórmula:** Al usar $\geq$, el Profe Alex nos indica que debemos separar el problema en dos casos unidos por el símbolo de unión ($\cup$).
2. **Desglose en dos inecuaciones:**
   - **Caso 1:** $x + 5 \leq -3$ (Cambiamos el sentido y el signo).
   - **Caso 2:** $x + 5 \geq 3$ (Idéntico al original pero sin barras).
3. **Despeje de la incógnita:**
   - En el Caso 1: $x \leq -3 - 5 \Rightarrow x \leq -8$.
   - En el Caso 2: $x \geq 3 - 5 \Rightarrow x \geq -2$.
4. **Resultado en intervalos:** 
   Representamos los números menores o iguales a $-8$ unidos a los mayores o iguales a $-2$.
   **Solución:** $(-\infty, -8] \cup [-2, \infty)$
```

```ad-example
title: Ejemplo B — Variación de Costos de Construcción (Ajuste en USD)
**Contexto:** Un proyecto de infraestructura permite una variación en el costo de materiales representada por $|\frac{2x + 4}{3}| \leq 6$, donde $x$ es el ajuste presupuestario en dólares.

**Procedimiento:**
1. **Aplicar efecto "Sándwich":** Como es "menor o igual que", la expresión queda "atrapada" entre el valor negativo y el positivo del extremo:
   $-6 \leq \frac{2x + 4}{3} \leq 6$
2. **Eliminar el denominador:** Multiplicamos los tres miembros de la inecuación por 3:
   $(-6 \cdot 3) \leq 2x + 4 \leq (6 \cdot 3) \Rightarrow -18 \leq 2x + 4 \leq 18$
3. **Aislar el término con $x$:** Restamos 4 en todos los sectores:
   $-18 - 4 \leq 2x \leq 18 - 4 \Rightarrow -22 \leq 2x \leq 14$
4. **Despeje final:** Dividimos todo entre 2 (al ser positivo, no cambia el sentido):
   $-11 \leq x \leq 7$
**Solución:** El ajuste permitido fluctúa en el intervalo $[-11, 7]$ USD.
```

---

## 4. EJERCICIOS DE REPASO

```ad-abstract
title: 🟢 Nivel: Fácil
color: 0, 200, 0
1. $|x| < 12$
2. $|x| \geq 25$
3. $|x| < -5$ (Analice la propiedad de las distancias negativas).
4. $|x| > -10$ (Considere el concepto de "Todos los Reales").
```

```ad-abstract
title: 🟡 Nivel: Medio
color: 255, 200, 0
1. $|3x - 2| > 4$
2. $|\frac{x}{3} - 2| > 4$
3. $|x + 8| \leq 10$
```

```ad-abstract
title: 🔴 Nivel: Avanzado (Aplicación $USD)
color: 200, 0, 0
1. $|\frac{4x - 3}{3}| < 5$ → *Meta: Hallar el intervalo abierto entre los dos extremos simplificados.*
2. $|\frac{3x - 1}{4}| \geq 5$ → *Meta: Expresar como la unión de dos infinitos.*
3. **Problema de Balance:** Un cajero reporta un desfase de caja según $|\frac{2x - 10}{5}| \leq 4$. Determine el rango exacto de dólares ($x$) que explican este movimiento. (Resultado esperado: $[ -5, 15 ]$).
```

---

## 5. CONSEJO DE ESTUDIO

> [!tip] 💡 Estrategia para "quitar las barras"
> Para resolver estas inecuaciones con la fluidez del Profe Alex, recuerda:
> 
> 1. **Aislamiento previo:** Nunca intentes quitar las barras si hay números sumando o multiplicando fuera de ellas. Primero despeja el valor absoluto para que quede solo en un lado de la inecuación.
> 2. **Para "Mayor que" ($>$):** Una respuesta es el problema original sin barras. La otra respuesta se obtiene escribiendo la expresión interna igual, pero **invirtiendo el sentido de la desigualdad** ($>$ pasa a $<$) y **cambiando el signo** del número (positivo a negativo).
> 3. **Para "Menor que" ($<$):** Se crea un "sándwich". Escribe el número de la derecha en negativo a la izquierda, y coloca la expresión del centro sin barras. Se llama así porque la $x$ queda atrapada entre dos límites.
> 4. **¡CUIDADO!:** Si durante el despeje de la $x$ debes multiplicar o dividir por un **número negativo**, es obligatorio **voltear el sentido de todos los signos de desigualdad** en ese paso.