# Clase 05 — Solución de la ecuación cuadrática completando cuadrados

#algebra #solucion-ecuaciones

[<< Clase 04 | **Clase 05** | Clase 06 >>]
*Bloque 2: Ecuaciones de Segundo Grado — Lección 5 de 8*

---

## 1. Relevancia y Aplicaciones
Completar el cuadrado es una herramienta matemática poderosa porque nos permite resolver ecuaciones que no pueden factorizarse de forma simple. Es el método "maestro" que nos da el control total sobre cualquier estructura cuadrática.

*   💵 **Finanzas:** Permite calcular puntos de equilibrio exactos en modelos de ingresos donde los precios se ajustan en $\text{USD}$, asegurando que la rentabilidad sea máxima.
*   🏗️ **Arquitectura:** Es esencial para diseñar arcos parabólicos con precisión milimétrica, permitiendo hallar el vértice exacto para la estabilidad de la obra.
*   📊 **Ciencia:** Se usa para predecir trayectorias de objetos en caída libre, determinando el segundo exacto en que un objeto alcanzará una posición determinada.

---

## 2. Concepto Clave y Definición
El método de **Completar el Cuadrado** es un "truco" algebraico para convertir un trinomio que no es perfecto en un **Trinomio Cuadrado Perfecto (TCP)**. Imagina que estás completando un rompecabezas: si te falta una pieza para formar un cuadrado perfecto, este método te enseña cómo fabricar esa pieza y dónde colocarla.

> [!warning] **¡Cuidado con la Balanza!**
> El error más común es olvidar sumar el valor calculado en **ambos** lados de la ecuación. Recuerda que una ecuación es como una balanza: lo que agregas a la izquierda, debes agregarlo a la derecha para que se mantenga el equilibrio.

> [!tip] **Regla Mnemotécnica**
> Para que nunca se te olvide el proceso, repite: **"La mitad, al cuadrado y a los dos lados"**. Esto significa que tomas la mitad del coeficiente de $x$, la elevas al cuadrado y la sumas en ambos miembros de la igualdad.

---

## 3. Procedimiento Paso a Paso
¡No te preocupes! Aunque parezca complejo, si sigues estos pasos con calma, verás que es lógico y ordenado:

```text
PASO 1: Primero, asegúrate de que el término $x^2$ esté solo. 
        Si tiene un coeficiente (a ≠ 1), divide toda la ecuación por ese número.
PASO 2: Luego, pasa el término independiente (el número sin x) al lado derecho.
PASO 3: Ahora, calcula $(b/2)^2$ —es decir, la mitad del número que acompaña 
        a la x elevado al cuadrado— y suma ese resultado en ambos lados.
PASO 4: Finalmente, factoriza como un binomio al cuadrado. Al sacar raíz 
        cuadrada, recuerda usar el símbolo ± (esto nace del concepto de 
        valor absoluto) y despeja la x.
```

---

## 4. Ejemplos Desarrollados

```ad-example
title: **Ejemplo 1 (Caso Básico)**
**Resolver: $x^2 + 6x - 16 = 0$**
1. Pasamos el $-16$ al lado derecho: $x^2 + 6x = 16$.
2. Completamos el cuadrado: La mitad de $6$ es $3$, y $3^2 = 9$. Sumamos $9$ en ambos lados:
   $x^2 + 6x + 9 = 16 + 9$
   $x^2 + 6x + 9 = 25$
3. Factorizamos el lado izquierdo: $(x + 3)^2 = 25$.
4. Aplicamos raíz cuadrada: Al extraer la raíz, surge el valor absoluto, por lo que usamos el $\pm$:
   $x + 3 = \pm \sqrt{25} \rightarrow x + 3 = \pm 5$
5. Despejamos:
   - $x_1 = 5 - 3 = 2$
   - $x_2 = -5 - 3 = -8$
**Resultados: $x_1 = 2, x_2 = -8$**
```

```ad-example
title: **Ejemplo 2 (Caso con Fracciones)**
**Resolver: $x^2 + 5x + 4 = 0$**
1. Pasamos el $4$ al derecho: $x^2 + 5x = -4$.
2. Completamos: La mitad de $5$ es $5/2$. Al elevar al cuadrado tenemos $25/4$.
   $x^2 + 5x + \frac{25}{4} = -4 + \frac{25}{4}$
3. Operamos la fracción con cuidado: Para sumar, convertimos el $-4$ a cuartos:
   $-4 = -\frac{16}{4} \rightarrow -\frac{16}{4} + \frac{25}{4} = \frac{9}{4}$
4. Factorizamos: $(x + \frac{5}{2})^2 = \frac{9}{4}$.
5. Raíz cuadrada: $x + \frac{5}{2} = \pm \frac{3}{2}$.
6. Despejamos:
   - $x_1 = \frac{3}{2} - \frac{5}{2} = -\frac{2}{2} = -1$
   - $x_2 = -\frac{3}{2} - \frac{5}{2} = -\frac{8}{2} = -4$
**Resultados: $x_1 = -1, x_2 = -4$**
```

```ad-example
title: **Ejemplo 3 (Caso Avanzado $a \neq 1$)**
**Resolver: $2x^2 + 8x - 24 = 0$**
1. Como el $x^2$ no está solo, dividimos toda la ecuación entre $2$:
   $\frac{2x^2}{2} + \frac{8x}{2} - \frac{24}{2} = \frac{0}{2} \rightarrow x^2 + 4x - 12 = 0$
2. Pasamos el $-12$: $x^2 + 4x = 12$.
3. Completamos: La mitad de $4$ es $2$, y $2^2 = 4$.
   $x^2 + 4x + 4 = 12 + 4 \rightarrow (x + 2)^2 = 16$
4. Raíz cuadrada: $x + 2 = \pm 4$.
5. Despejamos:
   - $x_1 = 4 - 2 = 2$
   - $x_2 = -4 - 2 = -6$
**Resultados: $x_1 = 2, x_2 = -6$**
```

```ad-example
title: **Ejemplo 4 (Aplicación $\text{USD}$)**
**Problema:** Un ajuste de precio $x$ en un producto sigue la relación $x^2 - 10x = 25$. Halla el ajuste en $\text{USD}$.
1. Completamos el cuadrado: La mitad de $-10$ es $-5$, y $(-5)^2 = 25$.
   $x^2 - 10x + 25 = 25 + 25 \rightarrow (x - 5)^2 = 50$
2. Raíz cuadrada: $x - 5 = \pm \sqrt{50}$ (aprox. $\pm 7.07$).
3. Despejamos: $x = 5 \pm 7.07$.
   - $x_1 \approx 12.07 \text{ USD}$
   - $x_2 \approx -2.07 \text{ USD}$
**Nota pedagógica:** En finanzas, un resultado negativo como $x_2$ suele interpretarse como un descuento o una reducción en el precio base.
```

---

## 5. Práctica para el Estudiante

```ad-abstract
title: **Nivel Verde (Fácil)**
Resuelve completando el cuadrado:
1. $x^2 - 8x + 12 = 0$
2. $x^2 + 4x - 5 = 0$
3. $x^2 - 10x + 9 = 0$
4. $x^2 + 2x - 8 = 0$
```

```ad-abstract
title: **Nivel Amarillo (Medio)**
Cuidado con las fracciones:
1. $x^2 - 3x - 8 = 0$
2. $x^2 + 5x + 6 = 0$
3. $x^2 + x - 6 = 0$
4. $x^2 - 7x + 10 = 0$
```

```ad-abstract
title: **Nivel Rojo (Avanzado: Aplicaciones $\text{USD}$ con $a > 1$)**
1. Una empresa de tecnología calcula su pérdida mensual mediante $2x^2 - 12x = 32$. Halla el valor positivo de $x$ en $\text{USD}$.
2. El costo de producción de un componente es $3x^2 - 18x = 21$. ¿Qué ajuste $x$ en $\text{USD}$ cumple la ecuación?
3. Un modelo de ingresos para una app es $5x^2 + 20x = 105$. Encuentra el valor positivo de $x$ en $\text{USD}$.
4. El ajuste de presupuesto para un proyecto arquitectónico es $2x^2 - 8x = 24$. Halla los valores de $x$ en $\text{USD}$.
```

---

## 6. Respuestas para el Docente

```ad-success
title: **Solucionario**
**Verde:** 1) $x = 6, 2$ | 2) $x = 1, -5$ | 3) $x = 9, 1$ | 4) $x = 2, -4$.
**Amarillo:** 1) $x \approx 4.77, -1.77$ | 2) $x = -2, -3$ | 3) $x = 2, -3$ | 4) $x = 5, 2$.
**Rojo:**
1) $x = 8 \text{ USD}$ (se descarta $-2$).
2) $x = 7 \text{ USD}$ (se descarta $-1$).
3) $x = 3 \text{ USD}$ (se descarta $-7$).
4) $x = 6, -2 \text{ USD}$.
```

---

## 7. Autoevaluación

```ad-question
title: **1. Pregunta Conceptual**
¿Qué número se debe sumar en ambos lados para completar el cuadrado en la expresión $x^2 + 12x$?
A) $6$
B) $12$
C) $36$
D) $144$
```

```ad-question
title: **2. Pregunta Procedimental**
Si tienes la ecuación $3x^2 + 6x = 9$, ¿cuál es el primer paso correcto según el método de completar el cuadrado?
A) Sumar $9$ en ambos lados.
B) Dividir toda la ecuación entre $3$.
C) Sacar la raíz cuadrada de $3$.
D) Restar $6x$ en ambos lados.
```

```ad-question
title: **3. Pregunta de Aplicación**
Un pequeño negocio usa $x^2 - 4x = 12$ para calcular su pérdida en $\text{USD}$. ¿Cuál es el valor positivo de $x$?
A) $x = 2 \text{ USD}$
B) $x = 6 \text{ USD}$
C) $x = 4 \text{ USD}$
D) $x = 12 \text{ USD}$
```

---

## 8. Cierre y Navegación Final

> [!tip] **Notas para el próximo tema**
> Dominar este "truco" de completar el cuadrado es vital, ya que es el procedimiento exacto que se utiliza para demostrar la **Fórmula General Cuadrática** que estudiaremos en la Clase 06. ¡Si entiendes esto, la fórmula será pan comido!

[<< Clase 04 | **Clase 05** | Clase 06 >>]
*Bloque 2: Ecuaciones de Segundo Grado — Lección 5 de 8*