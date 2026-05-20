# Clase 04 — Ecuaciones de primer grado con fracciones

---
**Navegación:** [Anterior: Clase 03](URL) | [Siguiente: Clase 05](URL)  
**Tags:** #Matemáticas #Álgebra #EcuacionesFraccionarias #MCM #PedagogíaDigital

---

## 1. ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia
> En la práctica, las finanzas y la ingeniería no se limitan a números enteros. Imagine que debe gestionar un presupuesto donde las obligaciones son fraccionarias: por ejemplo, destinar $\frac{1}{4}$ de los fondos a marketing y $\frac{1}{2}$ a mantenimiento. Si tras restar cargos fijos de $USD 10$, la suma de estas partes equivale a una inversión específica, resolver la ecuación fraccionaria es la única forma de calcular el capital total exacto. Dominar este método transforma problemas financieros complejos en aritmética manejable.

## 2. Concepto clave

El éxito en este tema depende de un cambio de mentalidad: no operamos con fracciones, las **eliminamos**.

> [!note] 📌 Definición
> El objetivo principal es transformar una ecuación fraccionaria en una **ecuación de números enteros**. Esto se logra multiplicando cada término por el **Mínimo Común Múltiplo (MCM)** de todos los denominadores.

> [!warning] ⚠️ Error común
> 1.  **Olvidar los términos enteros:** Es vital multiplicar los términos que NO tienen fracción (números "sueltos") por el $MCM$.
> 2.  **Peligro en los signos:** Al trabajar con binomios en el numerador precedidos por un signo menos (ej. $-\frac{x+2}{3}$), el signo negativo afectará a **todos** los términos del binomio al eliminar la fracción.

> [!tip] 💡 Truco: Método de la División Directa
> Para evitar cálculos con números gigantes, aplique esta regla: **Divida el $MCM$ entre el denominador y multiplique el resultado por el numerador.** Esto simplifica la expresión en un solo paso mental.

## 3. Procedimiento paso a paso

```markdown
PASO 1: Calcular el **MCM** de todos los denominadores.
PASO 2: Aplicar la **División Directa**: 
        (MCM ÷ Denominador) × Numerador.
PASO 3: Usar **Paréntesis de Seguridad** para proteger los numeradores 
        que sean binomios (esto evita errores de signo).
PASO 4: Resolver la **Ecuación Entera** resultante:
        - Distribuir y agrupar términos con $x$.
        - Aplicar la **Regla del -1** si la incógnita queda negativa.
        - Despejar y simplificar el resultado.
```

## 4. Ejemplos Desarrollados

````ad-example
**Ejemplo 1 (Básico):** Resuelva $\frac{3}{4}x + \frac{5}{2} = \frac{5}{2}x - \frac{11}{4}$
1.  **MCM:** El $MCM$ de $4$ y $2$ es $4$.
2.  **División Directa:**
    *   $4 \div 4 = 1 \rightarrow 1(3x)$
    *   $4 \div 2 = 2 \rightarrow 2(5)$
    *   $4 \div 2 = 2 \rightarrow 2(5x)$
    *   $4 \div 4 = 1 \rightarrow 1(11)$
3.  **Ecuación Entera:** $3x + 10 = 10x - 11$
4.  **Resolución:**
    $3x - 10x = -11 - 10$
    $-7x = -21$
    $x = \frac{-21}{-7} = 3$
**Resultado:** $x = 3$
````

````ad-example
**Ejemplo 2 (Con enteros y x negativa):** Resuelva $\frac{3x}{4} - \frac{1}{5} + 2x = \frac{5}{4} - \frac{3x}{20}$
1.  **MCM:** El $MCM$ de $4, 5$ y $20$ es $20$.
2.  **División Directa:**
    *   $20 \div 4 = 5 \rightarrow 5(3x)$
    *   $20 \div 5 = 4 \rightarrow 4(1)$
    *   $20 \times 2x = 40x$ (Término entero: se multiplica directo)
    *   $20 \div 4 = 5 \rightarrow 5(5)$
    *   $20 \div 20 = 1 \rightarrow 1(3x)$
3.  **Ecuación Entera:** $15x - 4 + 40x = 25 - 3x$
4.  **Resolución:**
    $55x - 4 = 25 - 3x \rightarrow 55x + 3x = 25 + 4$
    $58x = 29 \rightarrow x = \frac{29}{58}$
**Resultado:** $x = \frac{1}{2}$
````

````ad-example
**Ejemplo 3 (Con binomios y Regla del -1):** Resuelva $\frac{x+2}{12} - \frac{2x-3}{9} = \frac{4-3x}{18} + \frac{x}{6}$
1.  **MCM:** El $MCM$ de $12, 9, 18$ y $6$ es $36$.
2.  **Paso de Seguridad (Paréntesis):** 
    $3(x+2) - 4(2x-3) = 2(4-3x) + 6(x)$
3.  **Distribución (Cuidado con los signos):**
    $3x + 6 - 8x + 12 = 8 - 6x + 6x$
4.  **Resolución:**
    $-5x + 18 = 8$
    $-5x = 8 - 18 \rightarrow -5x = -10$
5.  **Regla del -1:** Multiplicamos toda la ecuación por $-1$:
    $5x = 10 \rightarrow x = \frac{10}{5} = 2$
**Resultado:** $x = 2$
````

````ad-example
**Ejemplo 4 (Aplicación USD):**
*Problema:* Si un tercio de una cuenta de restaurante más la mitad de la misma suma $USD 25$ tras restar $USD 10$ de cargos fijos, ¿cuál es el total?
1.  **Planteamiento:** $\frac{1}{3}x + \frac{1}{2}x - 10 = 25$
2.  **MCM:** El $MCM$ de $3$ y $2$ es $6$.
3.  **Ecuación Entera:** $2x + 3x - 60 = 150$
4.  **Resolución:** $5x = 210 \rightarrow x = \frac{210}{5}$
**Resultado:** $x = 42$. El total es $USD 42$.
````

## 5. Ejercicios para el estudiante

*Nota: Si el resultado no es un número entero, simplifique la fracción hasta su forma irreducible.*

1.  **🟢 Fácil:** Resuelva $\frac{x}{2} + \frac{x}{4} = 3$
2.  **🟡 Medio:** Resuelva $\frac{2x}{3} - 4 = \frac{x}{5}$
3.  **🔴 Avanzado ($USD):** Si $\frac{2}{3}$ de un presupuesto $x$, menos $\frac{1}{4}$ del mismo equivale a $USD 500$. ¿Cuál es el presupuesto total?

## 6. Respuestas y Autoevaluación

````ad-success
**Soluciones:**
1.  **Fácil:** $x = 4$
2.  **Medio:** $x = \frac{60}{7}$
3.  **Avanzado:** $x = 1200$ (Ecuación: $\frac{2}{3}x - \frac{1}{4}x = 500$)
````

### Mini-prueba de concepto
````ad-question
**1. ¿Cuál es el MCM correcto para la ecuación $\frac{x}{3} + \frac{x}{4} = 5$?**
a) $7$
b) **$12$**
c) $1$

**2. ¿Qué ocurre con el signo de $-3$ en $-(2x-3)$ al eliminar denominadores?**
a) Se mantiene negativo.
b) **Cambia a positivo ($+3$) por la distribución del signo menos.**
c) Se elimina.

**3. Si multiplicamos la ecuación $x + \frac{1}{2} = 3$ por el MCM ($2$), ¿cómo queda el término entero $x$?**
a) $x$
b) **$2x$**
c) $\frac{x}{2}$
````

## 7. Cierre y Navegación

Dominar la eliminación de denominadores es el puente hacia el álgebra avanzada. En la **próxima clase**, abordaremos las **ecuaciones racionales**, donde la incógnita $x$ se encuentra en el denominador, exigiendo un análisis de valores prohibidos.

---
**Navegación:** [Anterior: Clase 03](URL) | [Siguiente: Clase 05](URL)  
**Tags:** #Matemáticas #Álgebra #EcuacionesFraccionarias #MCM #PedagogíaDigital