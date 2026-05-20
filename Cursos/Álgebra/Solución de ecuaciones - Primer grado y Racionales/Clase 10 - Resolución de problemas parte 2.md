# Clase 10 — Resolución de problemas con ecuaciones — parte 2

#algebra #ecuaciones
Curso: [[00 - Índice del curso]] | Bloque IV | Lección 10 de 11

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [[Clase 09 — Resolución de problemas con ecuaciones — parte 1]]
> ➡️ **Siguiente:** [[Clase 11 — Resolución de problemas con ecuaciones — parte 3]]

---

## ¿Por qué es importante esta clase?

Dominar el modelado de situaciones reales mediante ecuaciones es la habilidad definitiva del pensamiento algebraico. No se trata simplemente de encontrar un valor numérico, sino de estructurar la realidad para resolver conflictos financieros, geométricos y logísticos con precisión absoluta.

**Ejemplo práctico de aplicación:**
Imagina que los presupuestos de dos departamentos están en una **razón de 7:9**. Si se inyecta un capital extra de **4 $USD** a cada uno, la proporción cambia a **4:5**. El álgebra nos permite determinar con exactitud los montos iniciales sin depender del tanteo infinito.

---

## Concepto clave

> [!abstract] Definición: Traducción y Estructura de Razones
> Resolver problemas implica traducir el **lenguaje cotidiano** al **lenguaje algebraico**. 
> - **Antecedente:** Es el término superior de una razón (numerador).
> - **Consecuente:** Es el término inferior de una razón (denominador).
> En problemas de razones (ej. 7:9), representamos los números como $7n$ y $9n$, donde $n$ es la constante de proporcionalidad que buscamos.

> [!warning] La Regla de la Cantidad Menor
> Para simplificar el despeje y evitar fracciones o valores negativos innecesarios, siempre **asigna la variable a la cantidad menor**. Esto permite expresar el resto de las condiciones mediante sumas o multiplicaciones directas.

> [!tip] Truco: Comprobación por lógica (Rango de respuesta)
> Antes de aplicar el álgebra, haz una prueba mental rápida. Si el total es 281 y hay más niñas que niños, sabes que los niños deben ser menos de 140. Si tu resultado algebraico es 200, sabrás inmediatamente que hubo un error de planteamiento.

---

## Procedimiento paso a paso

```text
PASO 1: Identificar y nombrar las incógnitas.
       Asignar letras representativas (n, a, c) a la cantidad MENOR 
       para facilitar el planteamiento.

PASO 2: Escribir la ecuación.
       Traducir las condiciones del enunciado. Si hay razones, plantear 
       como fracción; si hay tiempo pasado, restar a ambos lados.

PASO 3: Resolver la ecuación.
       Aplicar operaciones inversas y producto cruzado si existen 
       denominadores, hasta despejar la variable.

PASO 4: Verificar en el contexto original.
       Sustituir el valor en el problema real, no solo en la ecuación, 
       para asegurar que la lógica se cumple.
```

---

## Desarrollo de ejemplos

### Ejemplo 1: Geometría (Rectángulos)
**Problema:** La base de un rectángulo es el triple de su altura y el perímetro es 32.
*   **Paso 1:** Altura (menor) = $a$; Base = $3a$.
*   **Paso 2:** Perímetro $\implies a + 3a + a + 3a = 32$.
*   **Paso 3:** $8a = 32 \implies a = 4$.
*   **Paso 4:** Si la altura es 4, la base es $3(4) = 12$. 
    *   *Lógica:* $4 + 12 + 4 + 12 = 32$. **Correcto.**

### Ejemplo 2: Números pares consecutivos
**Problema:** La suma de dos números pares consecutivos es 174.
*   **Paso 1:** Menor = $2n$; Siguiente = $2n + 2$. (Usamos $2n$ para garantizar paridad).
*   **Paso 2:** $2n + (2n + 2) = 174$.
*   **Paso 3:** $4n + 2 = 174 \implies 4n = 172 \implies n = 43$.
*   **Paso 4:** 
    *   Primer número: $2(43) = 86$.
    *   Segundo número: $86 + 2 = 88$.
    *   *Verificación:* $86 + 88 = 174$. **Correcto.**

### Ejemplo 3: Población estudiantil
**Problema:** En un colegio hay 281 estudiantes. Las niñas exceden en 23 al doble de los niños.
*   **Paso 1:** Niños (menor) = $n$; Niñas = $2n + 23$.
*   **Paso 2:** $n + (2n + 23) = 281$.
*   **Paso 3:** $3n = 258 \implies n = 86$.
*   **Paso 4:** Niños = 86. Niñas = $2(86) + 23 = 195$.
    *   *Verificación:* $86 + 195 = 281$. **Correcto.**

### Ejemplo 4: Edades y Tiempo Pasado
**Problema:** Andrés tiene el doble de edad que Claudia. Hace 10 años, él tenía el cuádruple.
*   **Paso 1:** Claudia (actual) = $c$; Andrés (actual) = $2c$.
*   **Paso 2:** Hace 10 años: $(2c - 10) = 4(c - 10)$.
*   **Paso 3:** $2c - 10 = 4c - 40 \implies 30 = 2c \implies c = 15$.
*   **Paso 4:** Claudia = 15 años, Andrés = 30 años.
    
> [!tip] Nota del Profe: Lógica Temporal
> Al tratar con problemas de "hace X años" o "dentro de X años", la operación debe aplicarse a **ambas personas**, ya que el tiempo transcurre de igual forma para todos. Por eso restamos 10 tanto a $2c$ como a $c$.

### Ejemplo 5: Razones y Proporciones ($USD)
**Problema:** Dos precios están en razón 7:9. Si ambos suben 4 $USD, la nueva razón es 4:5.
*   **Paso 1:** Precio A (antecedente) = $7n$; Precio B (consecuente) = $9n$.
*   **Paso 2:** $\frac{7n + 4}{9n + 4} = \frac{4}{5}$
*   **Paso 3:** $5(7n + 4) = 4(9n + 4) \implies 35n + 20 = 36n + 16 \implies n = 4$.
*   **Paso 4:** Precio A = $7(4) = 28$ $USD; Precio B = $9(4) = 36$ $USD.

> [!tip] Nota del Profe: Producto Cruzado
> Aplicamos el producto cruzado para eliminar los denominadores. El denominador del segundo miembro pasa multiplicando al numerador del primero y viceversa. Esto transforma una proporción compleja en una ecuación lineal simple.

---

## Ejercicios para el estudiante

> [!ad-example] 🟢 Fácil (Verde)
> La suma de tres números pares consecutivos es igual a 162. Encuentra los tres números.

> [!ad-example] 🟡 Medio (Amarillo)
> Un lote rectangular tiene un perímetro de 94 m. El largo mide 5 m más que el doble del ancho. Halla las dimensiones.

> [!ad-example] 🔴 Avanzado (Rojo)
> Dos inversiones están en razón 4:5. Si el **antecedente** aumenta 6 $USD y el **consecuente** disminuye 5 $USD, la razón pasa a ser 6:5. ¿De cuánto eran las inversiones iniciales?

> [!ad-success] Respuestas
> 🟢 52, 54 y 56.
> 🟡 Ancho: 14 m, Largo: 33 m.
> 🔴 Inversiones de 24 $USD y 30 $USD.

---

## Mini-prueba de autoevaluación

> [!question] Selecciona la opción correcta:
> 
> **1. ¿Cuál es la traducción correcta para "el quíntuple de un número excedido en 2"?**
> A) $5(x + 2)$
> B) $5x + 2$
> C) $x/5 + 2$
> 
> **2. Si planteamos una edad de hace 5 años, ¿qué debemos hacer?**
> A) Restar 5 solo a la variable de la persona menor.
> B) Restar 5 a todas las variables que representan edades en ese momento.
> C) Multiplicar la edad actual por 5.
> 
> **3. En un problema de razones (ej. 4:5), ¿por qué usamos la misma variable $n$ para ambos términos?**
> A) Porque ambos números son iguales.
> B) Porque $n$ representa la constante de proporcionalidad que fue simplificada.
> C) Por convención estética del álgebra.

---

> [!tip] Cierre de la lección
> ¡Excelente progreso! Has aprendido a manejar razones y cambios temporales. Estos son los cimientos de la ingeniería y las finanzas. En la **Clase 11**, daremos el paso final enfrentando los desafíos más complejos del bloque. ¡Sigue adelante!

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [[Clase 09 — Resolución de problemas con ecuaciones — parte 1]]
> ➡️ **Siguiente:** [[Clase 11 — Resolución de problemas con ecuaciones — parte 3]]