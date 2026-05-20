# Clase 15 — Converting a pure repeating decimal to a fraction | Example 1

#algebra #convertingapure
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 15 de 22

> [!info] 🧭 Navegación
> **Anterior:** [[Clase 14 — Conceptos de decimales periódicos]] ← **Siguiente:** [[Clase 16 — Ejercicios avanzados de decimales]] →

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> Convertir decimales periódicos en fracciones no es solo un ejercicio escolar; es la única forma de garantizar **precisión absoluta** en el mundo real. Mientras que un decimal infinito te obliga a redondear (perdiendo información), la fracción conserva el valor exacto para siempre.

*   💵 **Mercado de divisas:** Al negociar dólares con una tasa de $1.\overline{12}$, usar el decimal truncado genera pérdidas acumuladas. La fracción $\frac{37}{33}$ asegura que cada centavo se contabilice con rigor bancario.
*   🏗️ **Ingeniería de precisión:** En la programación de tornos CNC y herramientas de corte automático, las medidas con decimales periódicos se convierten en fracciones para realizar ajustes milimétricos que el ojo humano no puede percibir.
*   📊 **Repartición de recursos:** Cuando divides un presupuesto de forma equitativa entre 3, 9 o 11 partes, las fracciones evitan que "desaparezcan" residuos de dinero que el decimal truncado no logra representar.

> [!note] 📌 ¿Qué es Converting a pure repeating decimal to a fraction?
> Es el método para transformar un número decimal periódico puro en su forma de fracción. Recuerda: un decimal es **periódico puro** cuando las cifras que se repiten (el periodo) comienzan justo después de la coma decimal.

> [!warning] ⚠️ Error común
> ¡Cuidado con los intrusos! Si ves un número "colado" entre la coma y el periodo (ej. $1.0\overline{2}$), este método no te servirá, porque ese es un decimal **periódico mixto**. El método de hoy es exclusivo para los puros (ej. $1.\overline{12}$), donde el "sombrero" empieza pegado a la coma.

> [!tip] 💡 Truco para recordarlo
> Para construir el denominador, usa esta regla mnemotécnica: **"Tantos nueves como cifras tenga el sombrero"**. Si el periodo tiene 2 cifras, pones $99$; si tiene una, pones $9$.

## PROCEDIMIENTO PASO A PASO

```text
PASO 1: Escribir el número completo (sin coma y sin barra de periodo).
PASO 2: Restar la parte entera (todo lo que esté a la izquierda de la coma).
PASO 3: Colocar en el denominador tantos nueves como cifras tenga el periodo.
PASO 4: Realizar la operación y simplificar la fracción hasta su mínima expresión.
```

## EJEMPLOS PRÁCTICOS

````ad-example
**Ejemplo 1 (Caso básico): $0.\overline{3}$**
1. Escribimos el número completo: $03$ (es decir, $3$).
2. Restamos la parte entera: $3 - 0 = 3$.
3. El periodo tiene una cifra: Denominador $9$.
4. Fracción resultante: $\frac{3}{9}$.
5. **Simplificación:** Sacamos tercera $\rightarrow \mathbf{\frac{1}{3}}$.
````

````ad-example
**Ejemplo 2 (Caso con enteros): $1.\overline{12}$**
1. Número completo: $112$.
2. Restamos la parte entera: $112 - 1 = 111$.
3. El periodo tiene dos cifras: Denominador $99$.
4. Fracción resultante: $\frac{111}{99}$.
5. **Simplificación:** Sacamos tercera ($\frac{111 \div 3}{99 \div 3}$) $\rightarrow \mathbf{\frac{37}{33}}$.
````

````ad-example
**Ejemplo 3 (Caso avanzado): $34.\overline{36}$**
1. Número completo: $3436$.
2. Restamos la parte entera: $3436 - 34 = 3402$.
3. El periodo tiene dos cifras: Denominador $99$.
4. Fracción resultante: $\frac{3402}{99}$.
5. **Proceso de simplificación:**
   - Sacamos tercera: $\frac{1134}{33}$.
   - Sacamos tercera nuevamente: $\mathbf{\frac{378}{11}}$.
````

````ad-example
**Ejemplo 4 (Aplicación real USD)**
Un producto financiero tiene un costo de $3.\overline{6}$ dólares. ¿Cuál es su monto exacto en fracción?
1. Operación: $\frac{36 - 3}{9} = \frac{33}{9}$.
2. Simplificación: Sacamos tercera $\rightarrow \mathbf{\frac{11}{3}}$.
**Resultado:** El cobro exacto en el banco debe ser de $\frac{11}{3}$ de dólar.
````

## EJERCICIOS PARA EL ESTUDIANTE

````ad-abstract
**🟢 Fácil (Una cifra periódica)**
1. $0.\overline{5}$
2. $0.\overline{7}$
3. $0.\overline{2}$
4. $0.\overline{4}$
````

````ad-abstract
**🟡 Medio (Parte entera y dos cifras periódicas)**
1. $2.\overline{15}$
2. $1.\overline{05}$
3. $3.\overline{21}$
4. $4.\overline{45}$
````

````ad-abstract
**🔴 Avanzado (Problemas aplicados $USD)**
1. Una acción bursátil subió $1.\overline{21}$ dólares. Exprésalo como fracción para el reporte contable.
2. Un rendimiento genera $0.\overline{18}$ dólares de interés. Convierte a fracción simplificada.
3. El costo de una comisión es de $5.\overline{18}$ dólares. ¿Cuál es su equivalente fraccionario exacto?
4. Se debe repartir un bono de $3.\overline{6}$ dólares entre empleados. Convierte a fracción.
````

````ad-success
**Respuestas correctas (Simplificadas)**
*   **Fácil:** 1) $\frac{5}{9}$ | 2) $\frac{7}{9}$ | 3) $\frac{2}{9}$ | 4) $\frac{4}{9}$
*   **Medio:** 1) $\frac{213}{99} = \frac{71}{33}$ | 2) $\frac{104}{99}$ | 3) $\frac{318}{99} = \frac{106}{33}$ | 4) $\frac{441}{99} = \frac{49}{11}$
*   **Avanzado:** 
    1) $\frac{120}{99} = \frac{40}{33}$ 
    2) $\frac{18}{99} = \frac{2}{11}$
    3) $\mathbf{\frac{57}{11}}$ (Ejercicio de práctica del video)
    4) $\mathbf{\frac{11}{3}}$ (Ejercicio de práctica del video)
````

## AUTOEVALUACIÓN

````ad-question
**Pregunta 1 (Conceptual):** ¿Qué condición debe cumplirse para que un decimal sea "periódico puro"?
*   **Respuesta:** El periodo (las cifras que se repiten) debe comenzar inmediatamente después de la coma decimal, sin ningún número fijo en medio.
````

````ad-question
**Pregunta 2 (Procedimental):** Si tienes el número $0.\overline{456}$, ¿qué denominador debe tener la fracción?
*   **Respuesta:** $999$. Porque el periodo tiene 3 cifras y la regla dice que se pone un nueve por cada cifra periódica.
````

````ad-question
**Pregunta 3 (Aplicación $USD):** Un software de trading indica una ganancia de $1.\overline{1}$ dólares. ¿Cuál es la fracción simplificada que representa este valor?
a) $\frac{11}{9}$
b) $\frac{10}{9}$
c) $\frac{1}{9}$
d) $\frac{11}{10}$
*   **Respuesta:** **b) $\frac{10}{9}$**. (Proceso: $11 - 1 = 10$ como numerador y $9$ como denominador). El distractor (a) es común si olvidas restar la parte entera.
````

> [!tip] 💡 En la próxima clase
> Prepárate para manejar números mucho más grandes y resolveremos un misterio matemático: **¿Por qué $0.\overline{9}$ es igual a $1$?** Analizaremos respuestas raras que desafían tu lógica pero que son 100% correctas.

> [!info] 🧭 Navegación
> **Anterior:** [[Clase 14 — Conceptos de decimales periódicos]] ← **Siguiente:** [[Clase 16 — Ejercicios avanzados de decimales]] →