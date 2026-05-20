# Clase 01 — Fracciones Algebraicas: Equivalencia, Simplificación y los 6 Métodos de Factorización
tags: #algebra #privatevideo
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 4

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]

---

## 1. Relevancia y Aplicaciones
> [!info] 🌍 Relevancia y aplicaciones
> El álgebra técnica permite reducir la complejidad de sistemas masivos a expresiones mínimas operables. La simplificación no es un paso estético, es un proceso de **optimización de recursos** que impacta directamente en la eficiencia de cálculo.
> 
> - **💵 Aplicación $USD:** Crucial para modelar tasas de interés compuesto o determinar el valor de cuotas fijas en préstamos donde el capital y el tiempo están representados por variables polinómicas.
> - **🏗️ Aplicación práctica:** En ingeniería estructural, se utiliza para simplificar las razones de carga y resistencia, permitiendo diseñar estructuras con el menor gasto de material posible.
> - **📊 Situación cotidiana:** Permite comparar el costo unitario real entre productos de distintas marcas, volúmenes y precios, eliminando el "ruido" publicitario para encontrar la oferta óptima.

---

## 2. Conceptos Clave

### 2.1 Definiciones Fundamentales
> [!note] 📌 ¿Qué es una Fracción Algebraica?
> Es la división indicada entre dos polinomios.
> - **Equivalencia:** Dos fracciones son equivalentes si representan el mismo valor numérico. Se verifica mediante el **producto cruzado**: $\frac{A}{B} = \frac{C}{D} \iff A \cdot D = B \cdot C$.
> - **Simplificación:** Proceso de dividir numerador y denominador por un factor común. Para simplificar expresiones complejas, es obligatorio **factorizar** primero.

### 2.2 Guía de Decisión: Los 6 Métodos de Factorización
Para simplificar con éxito, el "Arquitecto de Información" debe clasificar la expresión según su número de términos:

| Categoría | Método de Factorización | Condición Clave |
| :--- | :--- | :--- |
| **Universal** | 1. **Factor Común** | Se extrae lo que se repite en **todos** los términos. |
| **2 Términos** | 2. **Diferencia de Cuadrados** | Dos términos restando con raíz cuadrada exacta ($a^2 - b^2$). |
| | 3. **Suma/Resta de Cubos** | Dos términos con raíz cúbica exacta ($a^3 \pm b^3$). |
| **3 Términos** | 4. **Trinomio Cuadrado Perfecto** | Extremos positivos con raíz exacta; el medio es $2 \cdot \text{raiz1} \cdot \text{raiz2}$. |
| | 5. **Trinomio** $x^2 + bx + c$ | El término principal no tiene coeficiente visible (es 1). |
| | 6. **Trinomio** $ax^2 + bx + c$ | El término principal tiene un coeficiente $a \neq 1$. |

### 2.3 Errores y Reglas de Oro
> [!warning] ⚠️ Error crítico de "Cancelación"
> **PROHIBIDO:** Cancelar términos que están sumando o restando.
> *   *Incorrecto:* $\frac{x+5}{x} \neq 5$ (No se puede cancelar la $x$ porque arriba está sumando).
> *   *Correcto:* $\frac{x(5)}{x} = 5$ (Se cancela porque la $x$ es un **factor** que multiplica).

> [!tip] 💡 Regla del "Exponente Dominante"
> Para simplificar potencias, pregúntate: **"¿Dónde hay más?"**. 
> Resta los exponentes y deja la variable en la posición donde el exponente original era mayor. Si el numerador queda vacío, **coloca un 1**.

---

## 3. Procedimiento paso a paso (Algoritmo de Simplificación)

```text
PASO 1 → ANALIZAR: Identificar y extraer el Factor Común si existe.
PASO 2 → CLASIFICAR: Contar los términos del numerador y denominador.
    2.1 Si hay 2 términos: ¿Es diferencia de cuadrados o de cubos?
    2.2 Si hay 3 términos: ¿Es TCP o trinomio de la forma x^2 o ax^2?
PASO 3 → FACTORIZAR: Aplicar el método correspondiente para convertir sumas en productos.
PASO 4 → SIMPLIFICAR: Cancelar factores idénticos arriba y abajo.
    4.1 Si el numerador se simplifica totalmente, DEJAR UN 1.
    4.2 Si el denominador se simplifica totalmente, puede omitirse.
```

---

## 4. Ejemplos Prácticos Estructurados

```ad-example
title: Ejemplo 1 — Monomios y Regla de Ubicación
**Problema:** Simplificar $\frac{18x^3y^2}{6x^5}$

1. **Coeficientes:** $\frac{18}{6} = 3$ (queda arriba porque $18 > 6$).
2. **Variable X:** ¿Dónde hay más? Abajo ($5 > 3$). Restamos $5 - 3 = 2$. La $x^2$ queda **abajo**.
3. **Variable Y:** Solo hay arriba, se mantiene arriba.

**Resultado:** $\frac{3y^2}{x^2}$
```

```ad-example
title: Ejemplo 2 — Diferencia de Cuadrados (2 términos)
**Problema:** Simplificar $\frac{x^2 - 16}{x - 4}$

1. **Numerador:** 2 términos, resta, raíces exactas ($x$ y $4$). 
   *Factorización:* $(x - 4)(x + 4)$.
2. **Denominador:** Ya es una expresión mínima $(x - 4)$.
3. **Simplificación:** Cancelamos el bloque factor $(x - 4)$.

**Resultado:** $x + 4$
```

```ad-example
title: Ejemplo 3 — Trinomio Cuadrado Perfecto (3 términos)
**Problema:** Simplificar $\frac{a - 5}{a^2 - 10a + 25}$

1. **Denominador:** 3 términos. Raíces: $a$ y $5$. Prueba: $2(a)(5) = 10a$ (cumple TCP).
   *Factorización:* $(a - 5)^2$.
2. **Simplificación:** Cancelamos un $(a - 5)$ de arriba con uno de abajo.
3. **Regla del 1:** Como arriba no quedó nada, colocamos 1.

**Resultado:** $\frac{1}{a - 5}$
```

```ad-example
title: Ejemplo 4 — Aplicación $USD (Trinomio $x^2+bx+c$)
**Problema:** Una deuda de $x^2 + 7x + 12$ USD se liquida en $x + 3$ meses. Hallar el pago mensual.

1. **Planteamiento:** $\frac{x^2 + 7x + 12}{x + 3}$
2. **Factorizar:** Buscamos dos números que multiplicados den $12$ y sumados $7 \to (4, 3)$.
   *Expresión:* $\frac{(x + 4)(x + 3)}{x + 3}$
3. **Simplificación:** Cancelamos $(x + 3)$.

**Resultado:** El pago mensual es de $(x + 4)$ USD.
```

---

## 5. Ejercicios para el Estudiante

```ad-abstract
title: 🟢 Nivel Fácil — Monomios y Factor Común
1. $\frac{15x^2y^5}{5x^4y^2}$
2. $\frac{4a + 4b}{4}$
3. $\frac{10m^3}{20m^7}$
4. $\frac{3x^2 - 6x}{3x}$
```

```ad-abstract
title: 🟡 Nivel Medio — Binomios y Trinomios
1. $\frac{x^2 - 25}{x + 5}$
2. $\frac{x^2 + 6x + 9}{x + 3}$
3. $\frac{a^2 - 1}{a^2 + 2a + 1}$
4. $\frac{m^2 + 5m + 6}{m + 2}$
```

```ad-abstract
title: 🔴 Nivel Avanzado — Aplicaciones $USD y Financieras
1. **Costo Unitario:** Un lote de $x - 1$ productos costó $x^2 - 2x + 1$ USD. Simplifica para hallar el costo por unidad.
2. **Rendimiento:** Una cuenta generó $x^2 - 9$ USD en $x - 3$ días. ¿Cuál es el interés diario?
3. **Reparto:** Distribuye $x^2 + 8x + 15$ USD entre $x + 5$ inversores.
4. **Análisis de activos:** Simplifica la razón entre la caída de valor $x^2 - 16$ y el factor de riesgo $x + 4$.
```

```ad-success
title: ✅ Solucionario Técnico (Con pasos de factorización)
**Fácil:**
1. $\frac{3y^3}{x^2}$ (Resta $4-2$ en denominador).
2. $a + b$ (Factor común $4(a+b)/4$).
3. $\frac{1}{2m^4}$ (Resta $7-3$ en denominador, dejar 1 arriba).
4. $x - 2$ (Factor común $3x(x-2)/3x$).

**Medio:**
1. $x - 5$ (Dif. Cuadrados: $(x-5)(x+5)$).
2. $x + 3$ (TCP: $(x+3)^2$).
3. $\frac{a-1}{a+1}$ (Dif. Cuadrados / TCP: $\frac{(a-1)(a+1)}{(a+1)^2}$).
4. $m + 3$ (Trinomio: $(m+3)(m+2)$).

**Avanzado:**
1. $x - 1$ USD (Factorización: $(x-1)^2 / (x-1)$).
2. $x + 3$ USD (Factorización: $(x-3)(x+3) / (x-3)$).
3. $x + 3$ USD (Factorización: $(x+5)(x+3) / (x+5)$).
4. $x - 4$ (Factorización: $(x-4)(x+4) / (x+4)$).
```

---

## 6. Autoevaluación

```ad-question
title: 🧪 Pregunta 1
¿Cuál es el primer paso lógico al simplificar la expresión $\frac{5x^2 + 10x}{5x}$?
a) Cancelar las $5x^2$.
b) Restar los exponentes de las $x$.
c) Extraer el factor común $5x$ en el numerador.
**Respuesta:** c. 
**Lógica:** Antes de simplificar, debemos convertir la suma en producto mediante el Factor Común: $5x(x + 2) / 5x$.
```

```ad-question
title: 🧪 Pregunta 2
Si simplificamos $\frac{x - 3}{x^2 - 9}$, ¿cuál es el resultado correcto?
a) $x + 3$
b) $\frac{1}{x + 3}$
c) $x - 3$
**Respuesta:** b. 
**Lógica:** El denominador es una diferencia de cuadrados $(x-3)(x+3)$. Al cancelar $(x-3)$, el numerador queda vacío, por lo que se debe colocar un $1$ sobre el factor restante.
```

```ad-question
title: 🧪 Pregunta 3
Dos productos tienen precios expresados como $P_1 = \frac{x^2 - 4}{x - 2}$ y $P_2 = x + 2$. ¿Son equivalentes?
a) No, $P_1$ es una fracción y $P_2$ un entero.
b) Sí, porque al simplificar $P_1$ obtenemos $x + 2$.
c) Solo si $x = 0$.
**Respuesta:** b. 
**Lógica:** Al factorizar $x^2 - 4$ como $(x-2)(x+2)$ y dividir por $(x-2)$, la expresión resultante es $x+2$, demostrando equivalencia algebraica.
```

---

## 7. Cierre y Próximos Pasos

> [!video] 🎥 Nota del Instructor
> El método 6 (Trinomio $ax^2 + bx + c$) es el más complejo debido a que requiere multiplicar y dividir por la constante $a$. Si tienes dudas con este método específico, revisa el video privado de apoyo antes de la próxima sesión.

> [!tip] 💡 En la próxima clase
> Aplicaremos estos 6 métodos para resolver **Multiplicación y División de Fracciones Algebraicas**, donde la clave será simplificar *antes* de operar para evitar cálculos masivos.

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]