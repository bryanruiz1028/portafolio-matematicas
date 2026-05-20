# Clase 01 — Introducción a los Intervalos y su Representación Gráfica
tags: #algebra #intervalosintro
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 9

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]

## 1. ¿Por qué es importante esta clase?
Los intervalos nos permiten agrupar conjuntos infinitos de números reales que son imposibles de listar uno por uno. Gracias al "efecto zoom", entendemos que entre el número 1 y el 2 no hay un vacío, sino una cantidad infinita de valores (1.1, 1.01, 1.001...) que requieren una notación especial para ser definidos.

*   💵 **Aplicación con $USD:** Permite definir rangos financieros, como "saldos mayores a $10.00 USD". En matemáticas, modelamos el dinero como números reales para incluir hasta la fracción más pequeña de un centavo.
*   🏗️ **Aplicación práctica:** Vital en el cálculo de tolerancias industriales; por ejemplo, si el diámetro de un perno debe medir entre $10mm$ y $10.05mm$ para ser seguro.
*   📊 **Situación cotidiana:** Representación de límites legales y físicos, como límites de velocidad o rangos de edad permitidos.

## 2. Concepto clave
Un **intervalo** es un subconjunto de números reales que representa un segmento de la recta numérica delimitado por valores llamados **extremos**.

> [!note] Definición para jóvenes
> Imagina que usas una lupa potente (zoom) sobre la recta numérica. Entre el 1 y el 2 verás el 1.1, pero si acercas más la lupa, verás el 1.01, y luego el 1.001. Como nunca terminarías de nombrar el "siguiente" número, usamos intervalos para "empaquetar" todos esos infinitos decimales entre dos extremos.

> [!warning] ¡Cuidado con el error común!
> Un intervalo **no** es una lista de números enteros. Si decimos "números entre 2 y 5", no nos referimos solo al 3 y al 4. Incluimos cada fracción y decimal posible. Además, el **infinito ($\infty$) siempre es abierto** (usa paréntesis), porque al no ser un número real concreto, nunca podemos "llegar" a él para cerrarlo.

> [!tip] Regla mnemotécnica
> - El **corchete `[`** tiene líneas rectas que funcionan como manos: **"agarra"** al número (lo incluye).
> - El **paréntesis `(`** tiene forma curva: **"suelta"** al número (no lo incluye).

## 3. Procedimiento paso a paso
Para graficar y convertir a notación de intervalo, sigue este método basado en las lecciones del Profe Alex:

```text
PASO 0. ORDENAR: Si la variable x está a la derecha (ej. 10 > x), 
        aplica la regla mecánica: "Si volteas la x y el número, 
        DEBES voltear también el signo". (10 > x se convierte en x < 10).

PASO 1. IDENTIFICAR: Determina si x es mayor (hacia +∞) o menor (hacia -∞).

PASO 2. UBICAR EL EXTREMO: Marca el número límite en la recta numérica.

PASO 3. ELEGIR EL SÍMBOLO:
        - Punto cerrado (●) o corchete [ : Si incluye el número (≥, ≤).
        - Punto abierto/hueco (○) o paréntesis ( : Si NO incluye el número (>, <).

PASO 4. DIBUJAR: Traza la línea hacia la dirección correspondiente.
```

## 4. Ejemplos de Aplicación

*   **Ejemplo 1 (Básico): $x \geq 10$**
    "Los números mayores o iguales a 10". Incluimos el 10 con un punto cerrado y trazamos la flecha a la derecha.
    *Notación:* $[10, \infty)$

*   **Ejemplo 2 (Signos/Negativos): $x < -6$**
    "Los números menores que -6". Usamos un círculo abierto en -6 y nos movemos hacia la izquierda.
    *Notación:* $(-\infty, -6)$

*   **Ejemplo 3 (Avanzado/Doble): $-3 \leq x < 2$**
    "Los números entre -3 y 2". Este es un **intervalo semiabierto**: incluye el extremo izquierdo (-3) pero deja abierto el derecho (2).
    *Notación:* $[-3, 2)$

*   **Ejemplo 4 ($USD): $x > 7$**
    Representa "saldos mayores a $7.00 USD". Aunque físicamente usamos centavos, el modelo matemático indica que cualquier valor, por mínimo que sea el decimal superior a 7, forma parte del conjunto.
    *Notación:* $(7, \infty)$

## 5. Ejercicios para el estudiante

> [!success] 🟢 Fácil
> Representar en la recta y escribir como intervalo:
> 1. $x \leq 0$
> 2. Los números entre 5 y 15 (sin incluir los extremos).

> [!warning] 🟡 Medio
> Representar en la recta y escribir como intervalo:
> 1. $12 > x$ (Aplica la regla de voltear la variable primero).
> 2. $x \geq \frac{7}{3}$ (Divide $7 \div 3$ para ubicar el punto aproximadamente en $2.33$).

> [!danger] 🔴 Avanzado ($USD)
> Representar el siguiente rango de presupuesto:
> 1. "Gastos entre $5 y $20 USD, incluyendo ambos valores".

> [!check] Respuestas correctas
> 1. **Fácil:** $(-\infty, 0]$ y $(5, 15)$.
> 2. **Medio:** $(-\infty, 12)$ (al voltear $12 > x$ obtenemos $x < 12$) y $[\frac{7}{3}, \infty)$.
> 3. **Avanzado:** $[5, 20]$. *Explicación: Se usan corchetes en ambos extremos porque la instrucción dice "incluyendo ambos".*

## 6. Mini-prueba de autoevaluación
1. **¿Cuál es la diferencia visual en la gráfica entre un extremo incluido y uno excluido?**
   - a) El incluido es un círculo hueco; el excluido es un punto negro.
   - b) El incluido es un punto negro o corchete; el excluido es un círculo hueco o paréntesis.
   - c) No hay diferencia visual, solo en la notación escrita.

2. **Si el ejercicio plantea $15 \leq x$, ¿hacia dónde apunta la flecha y cuál es el intervalo correcto?**
   - a) Izquierda, $(-\infty, 15]$.
   - b) Derecha, $[15, \infty)$.
   - c) Derecha, $(15, \infty)$.

3. **¿Por qué el infinito siempre lleva paréntesis y no corchete?**
   - a) Por convención estética de los libros.
   - b) Porque el infinito es un número muy grande pero exacto.
   - c) Porque el infinito no es un número real alcanzable; el intervalo nunca "cierra" ahí.

## 7. Notas para el próximo tema

> [!tip] Lo que viene...
> En la Clase 02 aplicaremos estos conceptos para resolver **desigualdades lineales**. Verás que el intervalo no es solo un dibujo, sino la forma profesional de expresar la solución final de una operación algebraica compleja.

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]