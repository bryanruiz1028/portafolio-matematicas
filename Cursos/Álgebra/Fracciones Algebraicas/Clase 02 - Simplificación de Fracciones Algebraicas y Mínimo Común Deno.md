# Clase 02 — Simplificación de Fracciones Algebraicas y Mínimo Común Denominador

#algebra #simplifyingalge

> [!info] 🧭 Navegación
> [Anterior: Clase 01 — Introducción a Fracciones Algebraicas](Clase01) | [Índice de Contenidos](Indice) | [Siguiente: Clase 03 — Suma y Resta de Fracciones Algebraicas](Clase03)

---

## RELEVANCIA Y APLICACIONES
Dominar la simplificación y el Mínimo Común Múltiplo (MCM) es como aprender las reglas de ortografía antes de escribir una novela. Sin estas herramientas, es imposible realizar sumas o restas de fracciones. Como explica el Profe Alex, para operar con fracciones como $\frac{5}{6}$ y $\frac{1}{4}$, primero debemos encontrar un número que sea múltiplo de ambos (el $12$). En el álgebra, el proceso es idéntico: buscamos que todas las expresiones "hablen el mismo idioma".

*   **💵 [Aplicación $USD]:** Al analizar costos de producción, simplificar expresiones de costos unitarios permite comparar precios de proveedores de forma directa y transparente.
*   **🏗️ [Aplicación práctica]:** En ingeniería civil, el cálculo de tensiones y resistencias requiere unificar denominadores para equilibrar las cargas sobre una estructura.
*   **📊 [Situación cotidiana]:** Ajustar presupuestos familiares o repartir recursos de manera equitativa cuando las bases son distintas requiere la lógica del denominador común.

---

## CONCEPTO CLAVE

*   **Simplificación:** Es el proceso de "limpiar" la fracción, eliminando los factores que se repiten arriba y abajo para hacerla más pequeña y manejable.
*   **Mínimo Común Denominador (MCD):** Es el MCM de todos los denominadores. Su función es crear una base igual para que podamos sumar o restar los numeradores directamente.

> [!tip] 💡 Truco para recordarlo: El MCM "Hambriento"
> El MCM es como un monstruo muy hambriento: cuando ve factores iguales con distintos exponentes, **siempre elige el que tiene el exponente más grande**. Hacemos esto para asegurar que el MCM sea divisible por todos los denominadores originales.

> [!warning] 🚫 ¡ERROR PROHIBIDO!
> **¡No canceles términos que están sumando o restando!** Solo se pueden simplificar **factores** (cosas que se están multiplicando).
> *   **MAL:** En $\frac{x+5}{x}$, no puedes tachar las $x$.
> *   **BIEN:** En $\frac{x(x+5)}{x}$, sí puedes tachar la $x$ porque está multiplicando a todo lo demás.

---

## PROCEDIMIENTO PASO A PASO

Para convertir fracciones a un común denominador, sigue este protocolo técnico:

```text
PASO 1 → Factorizar completamente todos los denominadores.
PASO 2 → Encontrar el MCM: Elegir bases comunes y no comunes con su MAYOR exponente.
PASO 3 → Determinar el factor de amplificación: Dividir el MCM entre el denominador original.
         Ejemplo visual: Si MCM = 3a² y Denominador = a, el factor es (3a² ÷ a) = 3a.
PASO 4 → Multiplicar numerador y denominador de cada fracción por su factor.
```

---

## BLOQUES DE EJEMPLOS

### Ejemplo 1: Monomios (Básico)
Convertir a común denominador: $\frac{1}{a}$, $\frac{1}{3a}$ y $\frac{2x}{a^2}$.
1.  **Hallar MCM:** Las bases son $3$ y $a$. El mayor exponente de $a$ es $2$. El **MCM es $3a^2$**.
2.  **Amplificar:**
    *   $\frac{1}{a} \cdot \frac{3a}{3a} = \frac{3a}{3a^2}$
    *   $\frac{1}{3a} \cdot \frac{a}{a} = \frac{a}{3a^2}$
    *   $\frac{2x}{a^2} \cdot \frac{3}{3} = \frac{6x}{3a^2}$

### Ejemplo 2: Trinomios (Simplificación)
Simplificar: $\frac{x^2 - 2x - 3}{x - 3}$.
1.  **Factorizar numerador:** Es un **Trinomio de la forma $x^2 + bx + c$**. Buscamos números que multiplicados den $-3$ y sumados den $-2$. Son $(-3)$ y $(+1)$.
2.  **Expresión:** $\frac{(x-3)(x+1)}{x-3}$.
3.  **Simplificar:** Cancelamos el factor común $(x-3)$.
**Resultado:** $x+1$.

### Ejemplo 3: Polinomios (Avanzado)
Llevar a común denominador: $\frac{5}{x+1}$ y $\frac{2}{x-1}$.
1.  **MCM:** Como no se pueden factorizar más, el MCM es el producto de ambos: $(x+1)(x-1)$.
2.  **Amplificación:**
    *   Fracción 1: $\frac{5(x-1)}{(x+1)(x-1)}$
    *   Fracción 2: $\frac{2(x+1)}{(x-1)(x+1)}$

### Ejemplo 4: Aplicación $USD
Costo A: $\frac{3}{x}$ USD. Costo B: $\frac{2}{x+2}$ USD.
1.  **MCM:** $x(x+2) = x^2 + 2x$.
2.  **Amplificar A:** $\frac{3(x+2)}{x(x+2)} = \frac{3x+6}{x^2+2x}$.
3.  **Amplificar B:** $\frac{2(x)}{x(x+2)} = \frac{2x}{x^2+2x}$.
**Costo unificado:** $\frac{(3x+6) + 2x}{x^2+2x} = \frac{5x+6}{x^2+2x}$ USD.

---

## EJERCICIOS PARA EL ESTUDIANTE

> [!abstract] 📝 Práctica de Clase
>
> **🟢 Fácil (Monomios):**
> 1. Hallar MCM de: $2x, 4x^2, 6x^3$.
> 2. Hallar MCM de: $a^2b, ab^2$.
> 3. Hallar MCM de: $3x, 5y, 2xy$.
> 4. Convertir $\frac{1}{x}$ para que tenga denominador $x^2$.
>
> **🟡 Medio (Factorización):**
> 5. Simplificar usando Diferencia de Cuadrados: $\frac{x^2-1}{x+1}$.
> 6. Simplificar usando Factor Común: $\frac{3a+3b}{3}$.
> 7. Simplificar: $\frac{a^2-b^2}{a-b}$.
> 8. Simplificar: $\frac{x^2-4}{x+2}$.
>
> **🔴 Avanzado (Aplicación y Polinomios):**
> 9. Hallar el común denominador de $\frac{3}{x^2-1}$ y $\frac{x}{x+1}$.
> 10. Convertir a denominador común los costos $\frac{10}{x-5}$ y $\frac{5}{x+5}$.
> 11. Simplificar la expresión de costo: $\frac{x^2-7x+12}{x-3}$.
> 12. Hallar MCM de: $(x+1), (x+1)^2, (x-1)$.

> [!success] ✅ Respuestas
> 1. $12x^3$ | 2. $a^2b^2$ | 3. $30xy$ | 4. $\frac{x}{x^2}$
> 5. $x-1$ | 6. $a+b$ | 7. $a+b$ | 8. $x-2$
> 9. $(x-1)(x+1)$ | 10. $\frac{10(x+5)}{(x-5)(x+5)}$ y $\frac{5(x-5)}{(x+5)(x-5)}$ | 11. $x-4$ | 12. $(x+1)^2(x-1)$

---

## MINI-PRUEBA DE AUTOEVALUACIÓN

> [!question] 📝 Autoevaluación
>
> **1. En el MCM, ¿por qué elegimos el mayor exponente?**
> *Respuesta:* Para garantizar que el MCM sea divisible por todos los denominadores originales.
>
> **2. ¿Puedo simplificar la $y$ en $\frac{x+y}{y}$?**
> *Respuesta:* No, porque la $y$ del numerador es un término (está sumando), no un factor.
>
> **3. Si amplificamos $\frac{1}{x-1}$ para que su denominador sea $(x-1)(x+1)$, ¿cuál es el nuevo numerador?**
> *Respuesta:* El nuevo numerador es $(x+1)$. Dividimos el MCM entre el denominador original $(x-1)$ y multiplicamos el resultado por el numerador original ($1$).

---

## NOTAS FINALES Y NAVEGACIÓN

> [!tip] 💡 En la próxima clase
> Ya dominas el "motor" de las fracciones. En la **Clase 03: Suma y Resta**, usaremos el MCM para unir piezas separadas en una sola expresión poderosa. ¡No faltes!

> [!info] 🧭 Navegación
> [Anterior: Clase 01 — Introducción a Fracciones Algebraicas](Clase01) | [Índice de Contenidos](Indice) | [Siguiente: Clase 03 — Suma y Resta de Fracciones Algebraicas](Clase03)