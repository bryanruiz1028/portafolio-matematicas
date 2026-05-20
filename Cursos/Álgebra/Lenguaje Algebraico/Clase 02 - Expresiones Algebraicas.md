# CLASE 02: EXPRESIONES ALGEBRAICAS — OPERACIONES Y APLICACIONES

---
**Navegación:** [[Clase 01 - Lenguaje Algebraico|← Anterior]] | [[00 - Índice del curso|Índice →]]

**Tags:**
#algebra #algebraiclanguage

---

## 1. RELEVANCIA Y APLICACIONES
En esta sesión, subiremos de nivel. El lenguaje algebraico no solo sirve para nombrar cosas, sino para **modelar procesos**: entender cómo se comportan los números que se siguen entre sí y cómo transformar oraciones completas en ecuaciones reales usando el signo "=".

*   **💵 Dinero ($USD):** Para entender el valor de un billete o un precio, usamos el sistema decimal. Por ejemplo, un precio de $25 no es solo un 2 y un 5; matemáticamente es $(10 \cdot 2) + 5$. El álgebra nos permite representar cualquier precio desconocido de dos o tres cifras.
*   **🏗️ Construcción:** Al diseñar estructuras con secciones repetitivas, los ingenieros calculan dimensiones de partes "consecutivas" (vigas o soportes que van uno tras otro) usando estas fórmulas.
*   **📊 Situación cotidiana:** Determinar quién sigue en una fila (sucesor) o quién estaba antes (antecesor) en un sistema de turnos numerado.

---

## 2. CONCEPTO CLAVE
El lenguaje algebraico es la **traducción matemática** de palabras en símbolos. En esta etapa, aprenderemos a identificar el "punto de equilibrio" en una oración: el momento en que la descripción se convierte en una igualdad ($=$).

> [!warning] ⚠️ Error común: El orden y los signos de puntuación
> La posición de las palabras y el uso de comas cambia totalmente el resultado:
> 1.  **Jerarquía de operaciones:**
>     *   *La quinta parte del cubo de un número:* Primero el cubo, luego divides. $\rightarrow \frac{x^3}{5}$
>     *   *El cubo de la quinta parte de un número:* Primero divides, luego elevas todo al cubo. $\rightarrow (\frac{x}{5})^3$
> 2.  **La Regla de la Coma:**
>     *   "Las tres quintas partes de un número**,** aumentado en 4": La coma separa la fracción del aumento. $\rightarrow \frac{3}{5}x + 4$
>     *   "Las tres quintas partes de un número aumentado en 4": Al no haber coma, el $+4$ va dentro del proceso de la fracción. $\rightarrow \frac{3}{5}(x + 4)$

> [!tip] 💡 Truco para números consecutivos
> *   **Sucesor:** Para hallar el siguiente, **suma 1** ($x + 1$).
> *   **Antecesor:** Para hallar el anterior, **resta 1** ($x - 1$).
> *   **Pares/Impares:** Como los pares van "saltando" un número (ej. 2, 4, 6), para hallar el siguiente par o impar consecutivo debemos **sumar 2** ($x + 2$).

---

## 3. PROCEDIMIENTO PASO A PASO

```text
PASO 1 → Identificar palabras clave de operación ("sucesor", "triple", "cociente") 
         y de igualdad ("es", "equivale", "resulta en", "es igual a").
PASO 2 → Asignar variables ($x, y$) a los valores desconocidos.
PASO 3 → Traducir jerarquías. Si una operación afecta a TODA una suma o resta, 
         ¡USA PARÉNTESIS! (Ej: "El triple de la suma" → $3(x+y)$).
PASO 4 → Unir las piezas colocando el signo "=" donde la oración indique igualdad.
```

---

## 4. BLOQUE DE EJEMPLOS

> [!example] Ejemplo 1: Tres números consecutivos
> Existen dos formas correctas de plantearlo según tu punto de referencia:
> *   **Opción A (Desde el menor):** $x, x+1, x+2$
> *   **Opción B (Desde el centro):** $x-1, x, x+1$ (Esta es muy útil en ecuaciones avanzadas).

> [!example] Ejemplo 2: Igualdad y equivalencia
> **Traducir:** "La suma de dos números es 51".
> *   Suma de dos números: $x + y$
> *   Palabra clave "es": $=$
> *   **Resultado:** $x + y = 51$

> [!example] Ejemplo 3: Análisis de factores (Avanzado)
> **Traducir:** "El producto entre el doble de un número y la tercera parte de su consecutivo".
> *   **Factor 1 (Doble de un número):** $2x$
> *   **Factor 2 (Tercera parte del consecutivo):** $\frac{x+1}{3}$
> *   **Operación (Producto):** Multiplicamos ambos bloques.
> *   **Resultado:** $2x \cdot (\frac{x+1}{3})$

> [!example] Ejemplo 4: El sistema decimal ($USD)
> Para representar un número de dos cifras (como el 25), recordamos que la primera cifra son **decenas** (valen 10) y la segunda **unidades** (valen 1).
> *   Si la cifra de las decenas es $x$ y la de las unidades es $y$:
> *   **Resultado:** $10x + y$ (Porque es $10 \cdot x + 1 \cdot y$).

---

## 5. EJERCICIOS PARA EL ESTUDIANTE

### 🟢 Nivel Fácil: Sucesiones y tipos
1.  El sucesor de un número.
2.  El antecesor de un número.
3.  Un número par (múltiplo de 2).
4.  Dos números impares consecutivos (Recuerda sumar 2).

### 🟡 Nivel Medio: Operaciones compuestas
5.  La quinta parte del cubo de un número.
6.  El cubo de la quinta parte de un número.
7.  La suma de dos números dividida por su diferencia.
8.  El cuadrado de la suma de dos números equivale al triple de su producto.

### 🔴 Nivel Avanzado: Ecuaciones y $USD
9.  La suma de dos números consecutivos es igual a 51.
10. Un número de tres cifras (centenas $x$, decenas $y$, unidades $z$).
11. Las dos terceras partes de la suma de dos números.
12. El triple de la suma de dos números resulta en su producto.

---

> [!success] ✅ Clave de Respuestas
> 1. $x + 1$ | 2. $x - 1$ | 3. $2x$ | 4. $2x+1, 2x+3$ (o simplemente $x$ e $x+2$ si aclaramos que $x$ es impar).
> 5. $\frac{x^3}{5}$ | 6. $(\frac{x}{5})^3$ | 7. $\frac{x+y}{x-y}$ | 8. $(x+y)^2 = 3xy$
> 9. $x + (x + 1) = 51$ | 10. $100x + 10y + z$ | 11. $\frac{2}{3}(x + y)$ | 12. $3(x + y) = xy$

---

## 6. MINI-PRUEBA DE AUTOEVALUACIÓN

**1. Si queremos escribir tres números pares consecutivos, ¿por qué sumamos 2 en lugar de 1?**
*Respuesta: Porque si sumamos 1 a un par, obtenemos un impar. Para "saltar" al siguiente par, debemos avanzar dos unidades ($2x, 2x+2, 2x+4$).*

**2. Traduce: "El triple de la suma de dos números equivale a su producto".**
*Respuesta: $3(x + y) = xy$. Sin el paréntesis, el triple solo afectaría a la $x$, lo cual sería un error.*

**3. ¿Cómo representarías el valor total de un fajo de billetes que tiene $x$ billetes de cien, $y$ billetes de diez y $z$ monedas de uno?**
*Respuesta: $100x + 10y + z$.*

---

## 7. NOTAS Y CIERRE
💡 **En la próxima clase:** ¡Es hora de la verdad! Utilizaremos todo este lenguaje para resolver problemas de la vida real mediante ecuaciones.

**Navegación:**
`[[Clase 01 — Algebraic Language | Part 1 + Part 2]]` | `[[Indice_Algebra]]`

---

## GUÍA DE ESTUDIO (RESUMEN)

### TÉRMINOS CLAVE
| Concepto | Expresión Algebraica | Lógica |
| :--- | :--- | :--- |
| **Sucesor** | $x + 1$ | El siguiente número entero. |
| **Antecesor** | $x - 1$ | El número anterior. |
| **Número Par** | $2x$ | Siempre divisible por 2. |
| **Número Impar** | $2x - 1$ o $2x + 1$ | Un par menos (o más) uno. |
| **Pares Consecutivos**| $2x, 2x + 2$ | Saltos de 2 en 2. |

### ESTRUCTURA DE LOS NÚMEROS (Sistema Decimal)
No olvides que la posición de una cifra determina su valor:
*   **2 cifras:** $10x + y$ (Ej: $x$ son decenas).
*   **3 cifras:** $100x + 10y + z$ (Ej: $x$ son centenas).

### ¡AHA! MOMENTS (Ejemplos Extra)
1.  **La diferencia entre un número y su antecesor:**
    *   Traducción: $x - (x - 1)$
    *   *Dato curioso:* Si resuelves esto, el resultado siempre es **1**. ¡La distancia entre cualquier número y su anterior es constante!
2.  **El cociente entre un número y su mitad:**
    *   Traducción: $\frac{x}{x/2}$
    *   *Nota:* El cociente es el resultado de una división.

### EJERCICIOS DE REPASO FINAL
1.  Traduce: "La suma de un número par y el triple del siguiente par". $\rightarrow$ *$2x + 3(2x + 2)$*
2.  Traduce: "Tres números impares consecutivos". $\rightarrow$ *$x, x+2, x+4$ (siendo $x$ impar).*
3.  Traduce: "El cociente entre el cuadrado de un número y su sucesor". $\rightarrow$ *$\frac{x^2}{x+1}$*
4.  Traduce: "La diferencia entre un número y su doble es igual a 10". $\rightarrow$ *$x - 2x = 10$*
5.  Traduce: "Las tres quintas partes de un número aumentado en 4" (Sin coma). $\rightarrow$ *$\frac{3}{5}(x+4)$*