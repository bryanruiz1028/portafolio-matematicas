# Clase 03 — División de polinomios: Guía completa y cocientes mixtos

#algebra #divisindepolino

[[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | [[Clase 04|Clase 04 ➡]]

---

## 1. Relevancia y aplicaciones: El arte de distribuir
La división de polinomios no es solo un proceso mecánico; es la base para entender cómo se reparten recursos dinámicos. En matemáticas avanzadas, nos permite descomponer funciones complejas en partes más simples.

*   **$USD (Presupuestos):** Imagina que el presupuesto total de una obra es un polinomio $C(x)$. Al dividirlo por el costo de los materiales $M(x)$, el **cociente** representa la cantidad de obra que puedes realizar y el **residuo** es el excedente de dinero que no alcanza para otra unidad completa (surplus).
*   **🏗️ Práctica (Ingeniería):** Fundamental para hallar dimensiones. Si conoces el volumen de un sólido (polinomio de grado 3) y el área de su base (grado 2), la división te entregará la altura.
*   **📊 Cotidiana (Recursos):** Se aplica en la logística de distribución de suministros donde la demanda y el tiempo varían según funciones polinómicas.

---

> [!IMPORTANT] ¿Qué es la división de polinomios?
> Es un algoritmo que busca cuántas veces un polinomio **divisor** está contenido en un **dividendo**. 
> 
> **La analogía aritmética (El secreto de Alex):**
> Al igual que en la división simple $9 \div 2$, el resultado es $4$ y sobra $1$. Podemos escribirlo como:
> $$\frac{9}{2} = 4 + \frac{1}{2}$$
> En álgebra, seguimos exactamente la misma lógica para obtener un **Cociente Mixto**:
> $$\frac{Dividendo}{Divisor} = Cociente + \frac{Residuo}{Divisor}$$
> 
> **Error común:** Olvidar cambiar los signos en la resta. **Truco:** Aplica siempre la regla de los 4 pasos: **"Busca, Multiplica, Resta, Baja"**.

---

## 2. El Algoritmo Maestro: Procedimiento Paso a Paso

Para no perderte en el proceso, visualiza la división como un ciclo de cuatro estaciones:

1.  **ORDENAR:** Organiza ambos polinomios de forma descendente (del exponente mayor al menor). 
    *   *¡Vital!* Si falta un grado (ej. de $x^3$ pasas a $x^1$), deja un **hueco** o escribe $0x^2$. Esto mantiene la alineación vertical.
2.  **BUSCAR:** Divide el primer término del dividendo entre el primero del divisor. Este es tu primer término del cociente.
3.  **MULTIPLICAR Y RESTAR:** Multiplica tu nuevo término por todo el divisor. Al colocar el resultado debajo del dividendo, **cambia todos los signos** para realizar la resta.
4.  **BAJAR:** Baja el siguiente término del dividendo y repite el ciclo hasta que el grado del residuo sea menor al del divisor.

---

## 3. Ejemplos Prácticos con Metodología Visual

### Ejemplo 1: Caso Básico (Exacto)
Dividir $6x^2 + 7x + 2$ entre $2x + 1$.

*   **BUSCA:** $6x^2 \div 2x = 3x$.
*   **MULTIPLICA/RESTA:** $3x(2x+1) = 6x^2 + 3x$. Al restar ponemos: $-6x^2 - 3x$.
*   **RESULTADO:** Nos queda $4x$.
*   **BAJA:** El $+2$. 
*   **REPITE:** $4x \div 2x = +2$. Multiplicamos $2(2x+1) = 4x+2$. Al restar: $-4x-2$.
*   **COCIENTE:** $3x + 2$ (Residuo $0$).

### Ejemplo 2: Variables múltiples ($x, y$)
Dividir $(28x^2 - 11xy - 30y^2) \div (4x - 5y)$.

> [!TIP] Consejo del Especialista
> Cuando tengas dos variables, elige una para ordenar (ej. la $x$). La otra variable ($y$) se ordenará automáticamente de forma ascendente. Mantén siempre las columnas de términos semejantes alineadas (columna de $x^2$, columna de $xy$, columna de $y^2$).

1.  **Busca:** $28x^2 \div 4x = 7x$.
2.  **Multiplica y Resta:** $7x(4x - 5y) = 28x^2 - 35xy$. Pasamos con signos cambiados: $-28x^2 + 35xy$.
3.  **Suma:** $-11xy + 35xy = 24xy$. Baja el $-30y^2$.
4.  **Repite:** $24xy \div 4x = 6y$. Multiplica $6y(4x - 5y) = 24xy - 30y^2$. Pasamos como: $-24xy + 30y^2$.
*   **Resultado Final:** $7x + 6y$.

### Ejemplo 3: El desafío de los "Huecos" (Espacialidad)
Dividir $(x^3 + y^3) \div (x + 2y)$. Observa cómo los huecos permiten que aparezcan términos nuevos sin desordenar la cuadrícula:

```text
               x^2  - 2xy  + 4y^2       <-- Cociente
           _________________________
x + 2y |  x^3  +  (0x^2y) + (0xy^2) + y^3
         -x^3  -   2x^2y                <-- Resta (Cambio de signo)
         -------------------------
               -   2x^2y  + 0xy^2
               +   2x^2y  + 4xy^2       <-- Resta (Cambio de signo)
               -------------------
                            4xy^2 + y^3
                           -4xy^2 - 8y^3
                           -------------
                                  - 7y^3 <-- Residuo
```
**Resultado en formato mixto:** $(x^2 - 2xy + 4y^2) + \frac{-7y^3}{x + 2y}$

### Ejemplo 4: Aplicación Real en Finanzas ($USD)
Una empresa estima su costo total como $C(x) = 4x^2 + 8x + 5$ dólares para $x$ lotes de producción. Se desea saber el costo unitario si se divide entre el personal por lote $P(x) = 2x + 1$.

**Fórmula de aplicación:**
$$\text{Costo Total} = (\text{Costo Unitario} \times \text{Cantidad}) + \text{Residuo no asignado}$$

Al realizar la división:
1.  **Cociente:** $2x + 3$ (Costo unitario en USD).
2.  **Residuo:** $2$ (Dólares excedentes).
3.  **Expresión Mixta:** $(2x + 3) + \frac{2}{2x + 1}$.

---

## 4. Ejercicios para el Estudiante

> [!ABSTRACT] Práctica dirigida
> Resuelve los siguientes ejercicios en tu cuaderno, respetando las columnas y los huecos.

**Nivel Fácil: Divisiones Exactas**
1.  $(x^2 + 5x + 6) \div (x + 2)$
2.  $(6x^2 - 7x + 2) \div (3x - 2)$
3.  $(a^2 - 4) \div (a + 2)$
4.  $(2x^2 + 7x + 3) \div (x + 3)$

**Nivel Medio: Dos variables y ordenamiento**
5.  $(15x^2 - 22xy - 8y^2) \div (3x - 2y)$
6.  $(a^3 + 5a^2b + ab^2 - b^3) \div (a + b)$ (Ordena por la $a$).
7.  $(x^2 + y^2 - 2xy) \div (x - y)$ (Reordena primero).
8.  $(6m^2 - 11mn + 4n^2) \div (2m - n)$

**Nivel Avanzado: Cocientes Mixtos y $USD**
9.  Reparto de $x^2 - 5x + 7$ USD entre $(x - 4)$ beneficiarios.
10. Presupuesto de $6m^4 + 7m^3 - 2m^2 + 8m - 3$ USD entre $(2m^2 + 3m - 1)$ áreas. *Pista: Cuidado con los signos al multiplicar por $-m$.*
11. Hallar la tasa de distribución de $(x^3 + y^3)$ entre $(x + 2y)$.
12. Aplicar la lógica $9/2$ al polinomio: $(x - 1) \div (x - 4)$.

---

## 5. Respuestas para el Docente

> [!SUCCESS] Solucionario oficial
> 1.  $x + 3$
> 2.  $2x - 1$
> 3.  $a - 2$
> 4.  $2x + 1$
> 5.  $5x - 4y$
> 6.  $(a^2 + 4ab - 3b^2) + \frac{2b^3}{a+b}$
> 7.  $x - y$
> 8.  $3m - 4n$
> 9.  $(x - 1) + \frac{3}{x - 4}$ (*Nota: El residuo $3$ indica un sobrante de 3 USD.*)
> 10. $(3m^2 - m + 2) + \frac{m - 1}{2m^2 + 3m - 1}$
> 11. $(x^2 - 2xy + 4y^2) + \frac{-7y^3}{x + 2y}$
> 12. $1 + \frac{3}{x - 4}$ (*Nota: Similar a $9/2$, aquí el cociente es 1 y el residuo es 3.*)

---

## 6. Mini-prueba de Autoevaluación

> [!QUESTION] Evalúa tu aprendizaje
> 1.  **¿Por qué es vital dejar "huecos" al ordenar un polinomio?**
>     *Respuesta:* Para asegurar que los términos de grados intermedios que surgen durante la multiplicación tengan una columna asignada, evitando sumar peras con manzanas (ej. sumar $x^2$ con $x^3$).
> 2.  **¿Qué diferencia hay entre la notación mixta aritmética ($4 \frac{1}{2}$) y la algebraica?**
>     *Respuesta:* En álgebra **siempre** debemos escribir el signo $+$ entre el cociente y la fracción del residuo: $Cociente + \frac{Residuo}{Divisor}$, para evitar que parezca una multiplicación.
> 3.  **Si una división de costos tiene un residuo negativo (ej. $-5$), ¿qué significa en el contexto USD?**
>     *Respuesta:* Significa un déficit; falta esa cantidad para poder completar la distribución exacta según el modelo polinómico.

---

## Notas para el próximo tema
¿Sabías que hay un "atajo" para no hacer todo este cuadro? En la **Clase 04** veremos la **Regla de Ruffini** (División Sintética), que permite dividir polinomios en segundos, siempre que el divisor sea de la forma $(x \pm a)$.

[[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | [[Clase 04|Clase 04 ➡]]