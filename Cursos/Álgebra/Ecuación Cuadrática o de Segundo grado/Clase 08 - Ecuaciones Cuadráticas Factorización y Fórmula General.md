# Clase 08 — Ecuaciones Cuadráticas: Factorización y Fórmula General

#algebra #quadraticequations
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 8 de 8

> [!info] 🧭 Navegación
> [[Clase 07|⬅ Clase 07]] | [[00 - Índice del curso|Índice]] | **Clase 08** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]

---

> [!info] 🌍 Relevancia y aplicaciones
> Resolver ecuaciones de segundo grado permite encontrar valores críticos en fenómenos no lineales, siendo una herramienta vital para modelar la realidad física y económica.
> - 💵 **Finanzas:** Determinación de puntos de equilibrio, utilidades y precios óptimos en $USD.
> - 🏗️ **Construcción:** Cálculo preciso de dimensiones de superficies y diseño de arcos estructurales.
> - 📊 **Economía:** Análisis de modelos complejos de oferta y demanda para predecir comportamientos del mercado.

---

### Conceptos Fundamentales

> [!note] 📌 ¿Qué es una Ecuación Cuadrática?
> Es una igualdad donde el exponente más alto de la variable $x$ es 2. Su forma estándar es $ax^2 + bx + c = 0$. Debido a su grado, estas ecuaciones suelen presentar **dos posibles soluciones** (denotadas como $x_1$ y $x_2$).

> [!warning] ⚠️ Error común: La falta de igualación
> El error más grave es intentar aplicar métodos de resolución sin haber igualado la ecuación a cero. Los términos deben estar organizados de forma descendente en un solo lado de la igualdad.
> - ❌ **Incorrecto:** $x^2 - 2x = 15$
> - ✅ **Correcto:** $x^2 - 2x - 15 = 0$

> [!tip] 💡 Regla de los signos para factorización
> Al abrir los dos paréntesis $( \quad )( \quad )$, define los signos así:
> 1. **Primer paréntesis:** Baja directamente el signo del segundo término ($b$).
> 2. **Segundo paréntesis:** Resulta de la multiplicación de los signos del segundo término ($b$) y del tercero ($c$).

---

### Guía de Resolución Paso a Paso

Para resolver cualquier ecuación cuadrática, sigue este protocolo universal:

1.  **Organización:** Ordena los términos en la forma $ax^2 + bx + c = 0$.
2.  **Identificación:** Decide si usarás **Factorización** (ideal para números enteros simples) o la **Fórmula General** (método infalible para cualquier caso).
3.  **Ejecución:**
    *   **Factorización:** Busca dos números que multiplicados den $c$ y sumados/restados den $b$.
    *   **Fórmula General:** Sustituye $a, b, c$ en la fórmula: $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.
    *   **Regla de los Paréntesis:** Siguiendo el consejo del Profe Alex, sustituye siempre los valores dentro de paréntesis: $x = \frac{-(b) \pm \sqrt{(b)^2 - 4(a)(c)}}{2(a)}$. Esto evita errores fatales con los signos negativos.
4.  **Resolución Final:** Despeja las dos ecuaciones lineales para obtener $x_1$ y $x_2$.

---

### Ejemplos Prácticos

> [!example] Ejemplo 1: Caso Básico (Trinomio $x^2 + bx + c$)
> **Ecuación:** $x^2 - 2x - 15 = 0$
> 1. Buscamos dos números que multiplicados den $-15$ y que restados (porque los signos de los paréntesis son diferentes) den $2$.
> 2. Los números son $5$ y $3$. Colocamos el mayor primero: $(x - 5)(x + 3) = 0$.
> 3. Igualamos cada factor a cero:
>    - $x - 5 = 0 \rightarrow \mathbf{x_1 = 5}$
>    - $x + 3 = 0 \rightarrow \mathbf{x_2 = -3}$

> [!example] Ejemplo 2: Método de Multiplicación y División ($ax^2 + bx + c$)
> **Ecuación:** $3x^2 - 7x - 20 = 0$
> 1. Multiplicamos y dividimos por el coeficiente $a=3$: $\frac{(3x)^2 - 7(3x) - 60}{3} = 0$.
> 2. Buscamos números que multiplicados den $60$ y restados den $7$: Estos son $12$ y $5$.
> 3. Factorizamos: $\frac{(3x - 12)(3x + 5)}{3} = 0$.
> 4. Simplificamos extrayendo tercera en el primer factor: $(x - 4)(3x + 5) = 0$.
> 5. Resultados: $\mathbf{x_1 = 4}, \mathbf{x_2 = -5/3}$.

> [!example] Ejemplo 3: Aplicación de la Fórmula General
> **Ecuación:** $2x^2 + 9x + 10 = 0$ ($a=2, b=9, c=10$)
> 1. Aplicamos paréntesis en la sustitución: $x = \frac{-(9) \pm \sqrt{(9)^2 - 4(2)(10)}}{2(2)}$.
> 2. Calculamos el discriminante: $81 - 80 = 1$.
> 3. Operamos: $x = \frac{-9 \pm \sqrt{1}}{4} \rightarrow x = \frac{-9 \pm 1}{4}$.
> 4. Soluciones: $\mathbf{x_1 = -2}, \mathbf{x_2 = -2.5}$.

> [!example] Ejemplo 4: Aplicación en Finanzas ($USD$)
> **Problema:** El ingreso de una tienda se define por la ecuación $x^2 + x - 6 = 0$, donde $x$ representa el precio unitario en $USD.
> 1. Factorizando: $(x + 3)(x - 2) = 0$.
> 2. Resultados matemáticos: $x = -3$ y $x = 2$.
> 3. **Interpretación Pedagógica:** Aunque ambas son soluciones algebraicas válidas, en el contexto de precios descartamos el valor negativo. El precio de venta real es **$2 USD**.

---

### Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Fácil: Factorización Directa
> 1. $x^2 + x - 6 = 0$
> 2. $x^2 - 5x + 6 = 0$
> 3. $x^2 + 3x - 10 = 0$
> 4. $x^2 - x - 2 = 0$

> [!abstract] 🟡 Nivel Medio: Trinomio de la forma $ax^2 + bx + c$
> 1. $7x^2 - 10x + 3 = 0$
> 2. $2x^2 + 5x + 3 = 0$
> 3. $3x^2 - 5x + 2 = 0$
> 4. $6x^2 + 7x + 2 = 0$

> [!abstract] 🔴 Nivel Avanzado: Escenarios Financieros ($USD$)
> Resuelve usando la Fórmula General considerando $x$ como una variable de precio/inversión:
> 1. Encuentra el precio $x$ que equilibra los costos según: $5x^2 + 7x + 2 = 0$.
> 2. Determina la tasa de retorno $x$ en el modelo: $3x^2 + 8x + 4 = 0$.
> 3. Calcula el valor de mercado $x$ para la utilidad: $2x^2 - 7x + 3 = 0$.
> 4. Halla el punto de ajuste de precios según: $4x^2 + 11x + 6 = 0$.

> [!success] ✅ Respuestas exactas
> - **Fácil:** (1) $x=2, -3$; (2) $x=3, 2$; (3) $x=2, -5$; (4) $x=2, -1$.
> - **Medio:** (1) $x=1, 3/7$; (2) $x=-1, -3/2$; (3) $x=1, 2/3$; (4) $x=-1/2, -2/3$.
> - **Avanzado (Valores en $USD):** (1) $x=-0.4, -1$; (2) $x \approx -0.66, -2$; (3) $x=3, 0.5$; (4) $x=-0.75, -2$.

---

### Autoevaluación y Cierre

> [!question] ¿Es posible empezar a factorizar si la ecuación está escrita como $x^2 + 5x = -6$?
> No. Primero debes transponer el $-6$ al lado izquierdo para obtener $x^2 + 5x + 6 = 0$. Solo entonces puedes buscar los números que sumados den $5$ y multiplicados den $6$.

> [!question] Si tengo $10 + 2x^2 + 9x = 0$, ¿cuáles son los valores de $a, b$ y $c$?
> Debes ordenar la ecuación por el grado del exponente: $2x^2 + 9x + 10 = 0$. Así, $a=2, b=9$ y $c=10$.

> [!question] Si al calcular el precio de un producto obtengo $x_1 = 4$ y $x_2 = -1.5$, ¿cuál es la respuesta correcta?
> La respuesta correcta es $4$ $USD. Los resultados negativos en contextos de magnitudes físicas o económicas (como precios o distancias) carecen de sentido práctico y se descartan.

> [!tip] 💡 En la próxima clase
> ¡Enhorabuena! Has completado el bloque de Álgebra. En la siguiente etapa, utilizaremos estas herramientas para analizar Funciones y modelar gráficamente el comportamiento de estas ecuaciones.

---

> [!info] 🧭 Navegación
> [[Clase 07|⬅ Clase 07]] | [[00 - Índice del curso|Índice]] | **Clase 08** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]