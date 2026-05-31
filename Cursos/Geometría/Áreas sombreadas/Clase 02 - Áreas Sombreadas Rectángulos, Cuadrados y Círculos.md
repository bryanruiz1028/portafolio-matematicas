# Clase 02 — Áreas Sombreadas: Rectángulos, Cuadrados y Círculos

#algebra #shadedareas  
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 3

> [!info] 🧭 Navegación
> - Anterior: [[Clase 01 — Conceptos Básicos de Áreas]]
> - Índice: [[00 - Índice del curso]]
> - Siguiente: [[Clase 03 — Áreas en Figuras Compuestas Complejas]]

---

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> El cálculo de áreas sombreadas permite determinar la cantidad de material necesario en diseños complejos eliminando el material sobrante. Es la base para optimizar recursos en cualquier proceso de manufactura o construcción.

- **💵 [aplicación con $USD]:** Calcular el costo de desperdicio de material (metal o madera) al recortar piezas circulares de láminas rectangulares.
- **🏗️ [aplicación práctica]:** Diseño arquitectónico de ventanas o tragaluces con formas geométricas combinadas (rectángulos con arcos de medio punto).
- **📊 [situación cotidiana]:** Calcular la cantidad de césped necesaria para un jardín que tiene una fuente circular en el centro.

---

## Concepto clave

> [!note] 📌 ¿Qué es Shaded Areas?
> El área sombreada es el espacio que queda cuando a una figura principal (como un cuadrado o rectángulo) se le "resta" o quita otra figura interna (como un círculo o medio círculo). Es, esencialmente, una resta de superficies.

> [!warning] ⚠️ Error común
> El error más frecuente es olvidar elevar el radio al cuadrado ($r^2$) en la fórmula del círculo o no dividir el área del círculo cuando solo se tiene una parte (como medio círculo o un cuarto).

> [!tip] 💡 Truco para recordarlo
> "El área sombreada es la resta de la figura mayor menos la figura menor". 
> *Nota: Para estos ejercicios usaremos $\pi \approx 3.1416$ para obtener resultados precisos.*

---

## Procedimiento paso a paso

```text
PASO 1 → Identificar las figuras conocidas (cuadrado, rectángulo, círculo o fracciones). 
         NOTA: Identifica el radio (r). Si el círculo toca los bordes, el radio es la mitad del lado.
PASO 2 → Identificar si las áreas se suman o se restan (normalmente es Figura Exterior - Hueco Interior).
PASO 3 → Calcular el área de cada figura por separado usando las fórmulas:
         - Cuadrado: L × L
         - Rectángulo: b × h
         - Círculo: π × r²
PASO 4 → Realizar la operación final y expresar el resultado en unidades cuadradas (cm²).
```

---

## Ejemplos Prácticos

> [!example] Ejemplo 1: Cuadrado con círculo inscrito
> **Problema:** Hallar el área sombreada de un cuadrado de lado $6\text{ cm}$ con un círculo dentro.
> 1. **Área del Cuadrado:** $6\text{ cm} \times 6\text{ cm} = 36\text{ cm}^2$.
> 2. **Área del Círculo:** Como el círculo toca los lados, el diámetro es $6\text{ cm}$, por lo tanto, el radio es $r=3\text{ cm}$.
>    $A = 3.1416 \times (3)^2 = 3.1416 \times 9 = 28.27\text{ cm}^2$.
> 3. **Resta Final:** $36 - 28.27 = 7.73\text{ cm}^2$.
> **Resultado:** $7.73\text{ cm}^2$.

> [!example] Ejemplo 2: Rectángulo con hueco de medio círculo
> **Problema:** Rectángulo de $12\times6\text{ cm}$ con una sustracción de medio círculo.
> 1. **Área del Rectángulo:** $12 \times 6 = 72\text{ cm}^2$.
> 2. **Área de Medio Círculo:** El radio es la mitad de la altura ($r=3\text{ cm}$).
>    Área círculo completo $= 3.1416 \times 3^2 = 28.27\text{ cm}^2$.
>    Área medio círculo $= 28.27 / 2 = 14.13\text{ cm}^2$.
> 3. **Resta Final:** $72 - 14.13 = 57.87\text{ cm}^2$ (redondeado).
> **Resultado:** $57.86\text{ cm}^2$ (según ajuste decimal estándar).

> [!example] Ejemplo 3: Rectángulo con dos cuartos de círculo
> **Problema:** Rectángulo de $11\times5\text{ cm}$ con dos cuartos de círculo en las esquinas ($r=5$).
> 1. **Análisis:** Dos cuartos de círculo equivalen a medio círculo completo.
> 2. **Área del Rectángulo:** $11 \times 5 = 55\text{ cm}^2$.
> 3. **Área de Medio Círculo:** Con $r=5$, el círculo total es $78.5\text{ cm}^2$ (usando $\pi \approx 3.14$). La mitad es $39.25\text{ cm}^2$.
> 4. **Resta Final:** $55 - 39.25 = 15.75\text{ cm}^2$.
> **Resultado:** $15.75\text{ cm}^2$.

> [!example] Ejemplo 4: Aplicación Real (Costo de material)
> **Problema:** Una lámina de metal de $14\times8\text{ cm}$ cuesta $\$2$ USD por $\text{cm}^2$. Si se extrae un círculo de radio $4\text{ cm}$, ¿cuál es el valor del material sombreado?
> 1. **Área Rectángulo:** $14 \times 8 = 112\text{ cm}^2$.
> 2. **Área Círculo:** Con $r=4$, $A = 3.1416 \times 4^2 = 50.27\text{ cm}^2$.
> 3. **Área Sombreada:** $112 - 50.27 = 61.73\text{ cm}^2$.
> 4. **Conclusión Pedagógica (Costo):** Multiplicamos el área útil por el precio.
>    $61.73 \times \$2 = \$123.46$.
> **Valor de la parte sombreada:** $\$123.46$ USD.

---

## Ejercicios para el estudiante

> [!abstract] 🟢 Ejercicio Fácil
> Calcula el área sombreada de un rectángulo de $14\times8\text{ cm}$ al que se le quita un círculo completo de radio $r=4\text{ cm}$.

> [!abstract] 🟡 Ejercicio Medio
> Calcula el área sombreada de un cuadrado de lado $8\text{ cm}$ al que se le sustrae medio círculo ($r=4\text{ cm}$).

> [!abstract] 🔴 Ejercicio Avanzado ($USD$)
> Un rectángulo de $8\times4\text{ cm}$ tiene 4 huecos de cuartos de círculo en sus esquinas ($r=2\text{ cm}$).
> 1. Calcula el área sombreada (Pista: 4 cuartos = 1 círculo completo).
> 2. Si cada $\text{cm}^2$ de material sombreado se vende a $\$5$ USD, ¿cuál es el precio de la pieza?

> [!success] Respuestas
> - 🟢 **Fácil:** $61.73\text{ cm}^2$.
> - 🟡 **Medio:** $38.74\text{ cm}^2$.
> - 🔴 **Avanzado:** $19.44\text{ cm}^2$ (usando $\pi \approx 3.14$). **Precio final:** $\$97.2$ USD.

---

## Autoevaluación y Cierre

> [!question] Pregunta 1
> Si una figura tiene un ancho de $10\text{ cm}$ y un círculo inscrito toca ambos lados, ¿cuál es el radio del círculo?
> - A) $10\text{ cm}$
> - B) $5\text{ cm}$
> - C) $25\text{ cm}$
> *Tip: El diámetro es el ancho total; el radio es siempre la mitad.*

> [!question] Pregunta 2
> ¿Cuál es la fórmula correcta para el área de un círculo?
> - A) $\pi \times r$
> - B) $2 \times \pi \times r$
> - C) $\pi \times r^2$

> [!question] Pregunta 3
> Para hallar el área sombreada donde un círculo está dentro de un cuadrado, la operación es:
> - A) Área Círculo - Área Cuadrado
> - B) Área Cuadrado - Área Círculo
> - C) Área Cuadrado + Área Círculo

> [!tip] 💡 En la próxima clase
> Ahora que dominas la resta de figuras básicas, en la siguiente lección aprenderemos a trabajar con **figuras compuestas más complejas**, donde múltiples formas se suman y restan simultáneamente.

---
> [!info] 🧭 Navegación
> - Anterior: [[Clase 01 — Conceptos Básicos de Áreas]]
> - Índice: [[00 - Índice del curso]]
> - Siguiente: [[Clase 03 — Áreas en Figuras Compuestas Complejas]]