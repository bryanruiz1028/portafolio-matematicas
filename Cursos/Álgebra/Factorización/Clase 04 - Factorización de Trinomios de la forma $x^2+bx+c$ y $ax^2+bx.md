# Clase 04 — Factorización de Trinomios de la forma $x^2+bx+c$ y $ax^2+bx+c$

#algebra #factorizacintri
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 4 de 10

> [!info] 🧭 Navegación
> - ⬅️ **Anterior:** [[Clase 03 - Factor Común y Agrupación]]
> - 🏠 **Índice:** [[00 - Índice del curso]]
> - ➡️ **Siguiente:** [[Clase 05 - Trinomio Cuadrado Perfecto]]

---

## I. IMPORTANCIA Y RELEVANCIA

> [!info] 🌍 Relevancia y aplicaciones
> La factorización de trinomios permite transformar expresiones cuadráticas complejas en productos de binomios lineales, facilitando la resolución de ecuaciones y la optimización de funciones. En términos de arquitectura de información, este proceso reduce la carga cognitiva al descomponer un sistema cuadrático en sus componentes base.
> - 💵 **Aplicación en $USD para modelos de costos:** Permite desglosar funciones de ingresos para identificar el Precio y la Cantidad de equilibrio.
> - 🏗️ **Estructuras arquitectónicas:** Fundamental para calcular los puntos de apoyo y resistencia en diseños basados en arcos parabólicos.
> - 📊 **Análisis de tendencias:** Utilizado para modelar y predecir el comportamiento de variables interdependientes en análisis de datos financieros.

---

## II. DEFINICIÓN Y CONCEPTOS FUNDAMENTALES

```ad-abstract
### Concepto Clave: Trinomio de la forma $x^2+bx+c$
Es un polinomio de tres términos que cumple con una jerarquía estructural específica:
1.  **Coeficiente unitario:** El término de mayor grado siempre tiene un coeficiente de 1.
2.  **Relación de exponentes:** El exponente del primer término es exactamente el **doble** del exponente del segundo término. 
    *   *Ejemplo:* Si el primero es $x^6$, el segundo debe ser $x^3$.
3.  **Término independiente:** El tercer término es una constante numérica ($c$) sin variable.
```

### Errores y Trucos de Arquitectura de Signos
> [!warning] **Error común: Asignación de signos**
> No se deben copiar los signos del trinomio directamente a los paréntesis. 
> - El signo del **primer paréntesis** es el del segundo término ($b$). 
> - El signo del **segundo paréntesis** es el resultado de la **multiplicación** de los signos del segundo y tercer término ($b \cdot c$).

> [!tip] **Mnemotecnia: "Primero el Mayor"**
> Al buscar los dos números que multiplicados resultan en $c$ y sumados/restados en $b$, coloca siempre el **valor absoluto mayor** en el primer paréntesis. Esto asegura la coherencia lógica de los signos sin necesidad de comprobaciones adicionales.

---

## III. PROCEDIMIENTO TÉCNICO

Para factorizar la forma avanzada $ax^2+bx+c$, donde el coeficiente principal es distinto de 1, aplicamos el método de **multiplicación y división por $a$**:

```text
PASO 1: Multiplicar y dividir todo el trinomio por el coeficiente "a".
PASO 2: Dejar indicada la multiplicación en el primer y segundo término 
        para formar el bloque funcional (ax).
PASO 3: Factorizar el numerador como un trinomio de la forma x² + bx + c.
PASO 4: Simplificar el denominador extrayendo factor común de los paréntesis; 
        el divisor "a" debe eliminarse totalmente mediante esta simplificación.
```

---

## IV. EJEMPLOS PRÁCTICOS DESARROLLADOS

```ad-example
**Ejemplo 1: Caso Básico ($x^2+bx+c$)**
**Factorizar:** $x^2 + 5x + 6$
1.  **Raíz:** Extraemos $\sqrt{x^2} = x$. Preparamos: $(x + \quad)(x + \quad)$.
2.  **Signos:** El primero es $(+)$. El segundo es $(+) \cdot (+) = (+)$.
3.  **Números:** Buscamos números que multiplicados den $6$ y sumados den $5$.
    *   Probamos: $3$ y $2$. (Cumplen: $3 \cdot 2 = 6$ y $3 + 2 = 5$).
4.  **Resultado:** $(x + 3)(x + 2)$.
```

```ad-example
**Ejemplo 2: Caso con Signo Inicial Negativo**
**Factorizar:** $-x^2 + 6x - 8$
1.  **Factorización del signo:** Extraemos $(-1)$ para normalizar el trinomio: $-(x^2 - 6x + 8)$.
2.  **Factorizar interno:** Buscamos números que multiplicados den $8$ y sumados den $6$: $4$ y $2$.
    *   Signos: $(x - 4)(x - 2)$.
3.  **Refinamiento Estético:** Para evitar el negativo externo, podemos multiplicarlo por el primer paréntesis:
    *   **Resultado:** $(4 - x)(x - 2)$.
```

```ad-example
**Ejemplo 3: Caso Avanzado ($ax^2+bx+c$)**
**Factorizar:** $8a^6 - 14a^3 - 15$
1.  **Transformación:** Multiplicamos y dividimos por $8$: $\frac{(8a^3)^2 - 14(8a^3) - 120}{8}$
2.  **Búsqueda de Factores (Análisis de 120):** Descomponemos 120 en factores primos:
    *   $120 = 2 \cdot 2 \cdot 2 \cdot 3 \cdot 5$
    *   Buscamos parejas que restadas den 14:
        *   $(5 \cdot 3) \text{ y } (2 \cdot 2 \cdot 2) \rightarrow 15 - 8 = 7$ (No)
        *   $(5 \cdot 2 \cdot 2) \text{ y } (3 \cdot 2) \rightarrow \mathbf{20 - 6 = 14}$ (**Sí**)
3.  **Factorizar Numerador:** $\frac{(8a^3 - 20)(8a^3 + 6)}{8}$
4.  **Simplificación:** Dividimos el 8 entre los dos paréntesis (usando $4 \cdot 2 = 8$):
    *   Sacamos cuarta al primero: $(8a^3 - 20)/4 = (2a^3 - 5)$
    *   Sacamos mitad al segundo: $(8a^3 + 6)/2 = (4a^3 + 3)$
5.  **Resultado:** $(2a^3 - 5)(4a^3 + 3)$.
```

```ad-example
**Ejemplo 4: Aplicación Económica**
**Problema:** Una función de ingresos en $USD es $I = 2x^2 + 7x + 3$. Encuentre los binomios que representan el (Precio) y la (Cantidad).
1.  **Procedimiento:** $\frac{(2x)^2 + 7(2x) + 6}{2}$
2.  **Factores:** Multiplicados 6 y sumados 7: **6 y 1**.
    *   $\frac{(2x + 6)(2x + 1)}{2}$
3.  **Simplificación:** Sacamos mitad al primer paréntesis para eliminar el denominador:
    *   **Resultado:** $(x + 3)(2x + 1)$
4.  **Conclusión:** El Precio es $(x + 3)$ $USD y la Cantidad es $(2x + 1)$ unidades.
```

---

## V. SECCIÓN DE PRÁCTICA

### Ejercicios por Niveles

**Nivel Verde (Fácil)**
1. $x^2 + 7x + 10$
2. $a^2 + 8a + 12$
3. $x^2 + 5x + 4$
4. $m^2 + 9m + 20$

**Nivel Amarillo (Medio - Exponentes y Signos)**
5. $x^4 - 5x^2 - 14$
6. $m^6 + 7m^3 - 8$
7. $x^2 - 2x - 15$
8. $a^2 - 10a + 21$

**Nivel Rojo (Avanzado - Contexto $USD)**
9. Un terreno tiene un área de $6x^2 + 7x + 2$ $USD. Halle sus dimensiones.
10. Determine la base y altura de una placa con área $3x^2 - 5x - 2$ $USD.
11. Factorice la función de costo de producción $2x^2 + 3x - 2$ $USD.
12. Descomponga la utilidad proyectada $5x^2 + 13x - 6$ $USD en factores lineales.

```ad-success
### Clave de Respuestas
1. $(x+5)(x+2)$
2. $(a+6)(a+2)$
3. $(x+4)(x+1)$
4. $(m+5)(m+4)$
5. $(x^2-7)(x^2+2)$
6. $(m^3+8)(m^3-1)$
7. $(x-5)(x+3)$
8. $(a-7)(a-3)$
9. $(3x+2)(2x+1)$
10. $(3x+1)(x-2)$
11. $(2x-1)(x+2)$
12. $(5x-2)(x+3)$
```

---

## VI. AUTOEVALUACIÓN Y CIERRE

```ad-question
**Responde rápidamente:**
1. Si el primer término es $x^{10}$, ¿cuál debe ser el exponente del segundo término para aplicar estos métodos?
2. En la expresión $x^2 - 2x - 15$, ¿qué signos tendrán los paréntesis y por qué?
3. Factorice mentalmente la expresión de costo $x^2 - x - 6$ $USD.
```

**Notas de Conexión:**
La técnica de multiplicar y dividir por $a$ para normalizar el trinomio es fundamental para entender la completación de cuadrados. En la próxima clase, estudiaremos el **Trinomio Cuadrado Perfecto**, donde los factores resultantes son idénticos.

---
> [!info] 🧭 Navegación
> - ⬅️ **Anterior:** [[Clase 03 - Factor Común y Agrupación]]
> - 🏠 **Índice:** [[00 - Índice del curso]]
> - ➡️ **Siguiente:** [[Clase 05 - Trinomio Cuadrado Perfecto]]