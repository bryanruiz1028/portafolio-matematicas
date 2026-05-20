# Clase 01 — Introducción a los Números Racionales y Operaciones con Fracciones Negativas

---

### 1. Metadatos y Navegación
- tags: #algebra #introductiontor
- Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 2

> [!info] 🧭 Navegación
> - **Índice:** [[00 - Índice del curso]]
> - **Siguiente:** [[Clase 02 — Multiplicación y División de Racionales]]

---

### 2. Relevancia del Tema (¿Por qué es importante esta clase?)
Los números racionales son la herramienta matemática que nos permite expresar precisión donde los números enteros no llegan. Representan partes de un todo, proporciones y balances financieros.

- **💵 Aplicación $USD:** En el mundo del dinero, los centavos son fracciones de un dólar. Si tienes un saldo de $-0.75$, matemáticamente representas una deuda de $-\dfrac{3}{4}$ de dólar.
- **🏗️ Aplicación práctica:** En la construcción y carpintería, las medidas exactas (como "media pulgada" o "tres cuartos de metro") requieren el uso de racionales para evitar errores estructurales.
- **📊 Situación cotidiana:** Desde seguir una receta (usar $\dfrac{1}{3}$ de taza) hasta repartir una herencia o bienes de forma equitativa.

---

### 3. Concepto Clave: Los Números Racionales ($\mathbb{Q}$)
Un número racional es todo aquel que puede escribirse como una fracción $\dfrac{a}{b}$, donde $a$ y $b$ son **números enteros** y el denominador **$b \neq 0$**.

- **Inclusión de Conjuntos:** Los números naturales ($1, 2, 3...$) y los enteros ($..., -1, 0, 1...$) son también racionales. Cualquier entero puede expresarse como fracción agregando un $1$ en el denominador (ej. $-10 = \dfrac{-10}{1}$).
- **Identificación de Signos:** Como explica el Profe Alex, para saber si una fracción es positiva o negativa, basta con aplicar el **Truco de "Contar Negativos"**:
	- **Número impar de signos menos:** La fracción es **negativa** (ej. $-\dfrac{3}{4}$, $\dfrac{-3}{4}$, $\dfrac{3}{-4}$).
	- **Número par de signos menos:** La fracción es **positiva** (ej. $\dfrac{-3}{-4}$ se convierte en $\dfrac{3}{4}$ porque los signos se cancelan).

> [!warning] ⚠️ Error común
> - **Indeterminación:** El denominador **nunca** puede ser cero. La expresión $\dfrac{5}{0}$ no está definida en los racionales (es una indeterminación).
> - **Confusión visual:** No asumas que una fracción es negativa solo por ver signos menos. Evalúa la cantidad total; por ejemplo, $-\left( \dfrac{-3}{-5} \right)$ tiene tres signos negativos, por lo tanto, es **negativa**.

---

### 4. Procedimiento Paso a Paso

> [!info] 🛠️ Método de Resolución (Suma/Resta)
> **PASO 1:** **Simplificar signos.** Multiplica los signos internos y externos para que cada fracción tenga un único signo definido.
> **PASO 2:** **Asignar el signo al numerador.** El signo resultante colócalo siempre en el número de arriba para facilitar la operación.
> **PASO 3:** **Denominador común.** Multiplica los denominadores de las fracciones entre sí.
> **PASO 4:** **Multiplicación en cruz.** Multiplica el numerador de la primera por el denominador de la segunda, y viceversa, respetando los signos.
> **PASO 5:** **Operar y simplificar.** Suma o resta los resultados obtenidos y, obligatoriamente, simplifica la fracción final a su mínima expresión.

---

### 5. Ejemplos Prácticos

```ad-example
title: Ejemplo 1 (Básico): $-\dfrac{5}{4} - \dfrac{2}{3}$
1. **Signos al numerador:** Tenemos $\dfrac{-5}{4}$ y $\dfrac{-2}{3}$.
2. **Denominador común:** $4 \times 3 = 12$.
3. **Multiplicación en cruz:** 
   - $(-5) \times 3 = -15$
   - $4 \times (-2) = -8$
4. **Operación:** $\dfrac{-15 - 8}{12} = \mathbf{-\dfrac{23}{12}}$
*(Lógica: "Debo 15 y debo 8, en total debo 23")*
```

```ad-example
title: Ejemplo 2 (Con simplificación de signos): $\dfrac{-3}{-4} - \dfrac{1}{2}$
1. **Simplificar:** $\dfrac{-3}{-4}$ tiene dos negativos, es positiva: $\dfrac{3}{4}$.
2. **Operación:** $\dfrac{3}{4} - \dfrac{1}{2}$ (asignamos el menos al 1).
3. **Denominador común:** $4 \times 2 = 8$.
4. **Cruz:** $(3 \times 2) + (4 \times -1) \rightarrow 6 - 4 = 2$.
5. **Resultado:** $\dfrac{2}{8}$. Simplificado (mitad): $\mathbf{\dfrac{1}{4}}$.
```

```ad-example
title: Ejemplo 3 (Avanzado): $\dfrac{2}{3} - \left( -\left( -\left( \dfrac{-5}{-6} \right) \right) \right)$
1. **Contar negativos:** Hay 1 (afuera) + 2 (dentro de paréntesis) + 2 (en la fracción) = 5 signos.
2. **Simplificar:** Como 5 es impar, el término es negativo: $\dfrac{2}{3} - \dfrac{5}{6}$.
3. **Denominador:** $3 \times 6 = 18$.
4. **Cruz:** $(2 \times 6) - (5 \times 3) \rightarrow 12 - 15 = -3$.
5. **Resultado:** $\dfrac{-3}{18}$. Simplificado (tercera): $\mathbf{-\dfrac{1}{6}}$.
```

```ad-example
title: Ejemplo 4 (Aplicación $USD)
Tienes una deuda de $-\dfrac{3}{4}$ USD y realizas otra compra de $-\dfrac{1}{2}$ USD. ¿Cuál es el estado de tu cuenta?
- **Operación:** $\dfrac{-3}{4} + \dfrac{-1}{2}$.
- **Cálculo:** Denominador 8. Cruz: $(-3 \cdot 2) + (4 \cdot -1) = -6 - 4 = -10$.
- **Resultado:** $\dfrac{-10}{8} = \mathbf{-\dfrac{5}{4}}$ **USD**. (Equivale a deber $1.25$ dólares).
```

---

### 6. Ubicación en la Recta Numérica
Ubicar fracciones negativas requiere contar hacia la izquierda del cero.

1. **El Denominador:** Indica en cuántas partes iguales dividimos cada unidad (el espacio entre 0 y -1, entre -1 y -2, etc.).
2. **El Numerador:** Indica cuántos saltos damos desde el cero hacia la izquierda.

**Ejemplo textual: Ubicar $-\dfrac{3}{4}$**
- Dividimos la unidad entre $0$ y $-1$ en **4 partes iguales**.
- Desde el **0**, saltamos **3 partes hacia la izquierda**. El punto se sitúa justo antes de llegar al $-1$.

---

### 7. Ejercicios para el Estudiante

```ad-abstract
title: 🟢 Nivel Fácil
1. Determina si la siguiente fracción es positiva o negativa: $\dfrac{-(-(-2))}{5}$.
2. Expresa el número entero $-15$ como un número racional.
3. Si ubicas $-\dfrac{1}{5}$ en la recta numérica, ¿entre qué dos números enteros se encuentra?
4. Escribe una fracción equivalente a $\dfrac{1}{2}$ que use dos signos negativos.
```

```ad-abstract
title: 🟡 Nivel Medio
1. Resuelve: $-\dfrac{1}{2} - \dfrac{1}{3}$
2. Resuelve: $\dfrac{5}{4} + \left( \dfrac{1}{-2} \right)$
3. Calcula: $-\dfrac{2}{5} - \left( -\dfrac{1}{4} \right)$
4. Simplifica y resuelve: $\dfrac{-3}{-3} - \dfrac{1}{2}$
```

```ad-abstract
title: 🔴 Nivel Avanzado
1. Resuelve simplificando signos primero: $-\dfrac{-2}{-3} - \left( -\left( \dfrac{-1}{-2} \right) \right)$
2. Balance financiero: Un carpintero debe $-\dfrac{7}{8}$ de un cargamento de madera. Si paga $\dfrac{1}{4}$ de la deuda, ¿cuál es su balance actual?
3. Resuelve: $\dfrac{2}{3} - \dfrac{5}{6} + \dfrac{-1}{2}$
4. Ubica en una recta numérica mental y ordena de menor a mayor: $-\dfrac{3}{2}, -\dfrac{1}{4}, 0, -\dfrac{5}{4}$.
```

---

### 8. Respuestas y Autoevaluación

```ad-success
title: Soluciones
- **Fácil:** 1. Negativa (3 signos); 2. $\dfrac{-15}{1}$; 3. Entre $0$ y $-1$; 4. $\dfrac{-1}{-2}$.
- **Medio:** 1. $-\dfrac{5}{6}$; 2. $\dfrac{3}{4}$; 3. $-\dfrac{3}{20}$; 4. $\dfrac{1}{2}$.
- **Avanzado:** 1. $-\dfrac{1}{6}$; 2. $-\dfrac{5}{8}$; 3. $-\dfrac{2}{3}$; 4. $-\dfrac{3}{2} < -\dfrac{5}{4} < -\dfrac{1}{4} < 0$.
```

```ad-question
title: Autoevaluación
1. **¿Qué sucede si el denominador de una fracción es cero?**
   a) El resultado es 0.
   b) No es un número racional definido (indeterminación).
   c) La fracción se vuelve automáticamente negativa.
2. **¿Cuál es el resultado simplificado de $-\dfrac{1}{4} + \dfrac{1}{2}$?**
   a) $\dfrac{1}{4}$
   b) $-\dfrac{1}{8}$
   c) $\dfrac{2}{4}$
3. **Si una deuda de $-\dfrac{1}{2}$ USD se suma a otra deuda de $-\dfrac{1}{2}$ USD, el saldo es:**
   a) $0$ USD
   b) $-1$ USD
   c) $-\dfrac{1}{4}$ USD
```

---

### 9. Cierre y Conexión
Dominar la suma y resta de racionales negativos es el paso más difícil del álgebra básica. Con estos fundamentos de manejo de signos y denominadores, estás listo para operaciones más directas. En la siguiente clase, exploraremos la **multiplicación y división de racionales**, donde las reglas de signos se vuelven aún más protagonistas.

> [!info] 🧭 Navegación
> - **Índice:** [[00 - Índice del curso]]
> - **Siguiente:** [[Clase 02 — Multiplicación y División de Racionales]]