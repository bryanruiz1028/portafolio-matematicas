# RESPUESTAS DOCENTE: Binary Numbers y Convertir Binario a Decimal

> [!warning] ⚠️ Solo para uso del docente — No distribuir a estudiantes

Binary Numbers y Convertir Binario a Decimal

## Solucionario Detallado (Q1-Q8)

*   **Q1: Opción C.** El sistema binario es de base 2. Según el "profe Alex", esto significa que solo emplea dos símbolos (0 y 1) para representar cualquier cantidad, a diferencia del sistema decimal que usa diez.
*   **Q2: Opción D.** En binario, los valores de las casillas se duplican de derecha a izquierda: la primera vale 1, la segunda vale 2 y la tercera vale 4 ($2^2$).
*   **Q3: Opción B.** El 1 funciona como un "interruptor" o switch. Si la casilla tiene un 1, el valor de esa posición (sea 1, 2, 4, 8...) se suma al total decimal; si tiene un 0, se ignora.
*   **Q4: V.** Es verdadero. El valor de la cifra cambia según su posición (unidades, doses, cuatros, ochos, dieciséis, etc.), manteniendo la lógica de potencias de la base.
*   **Q5: V.** Es verdadero. Los números impares no tienen mitad exacta en el conjunto de los enteros; por tanto, al dividir por 2, siempre dejarán un residuo de 1 en la primera división (la de las unidades).
*   **Q6:** **Doble** (c), **Potencias** (a), **Dos** (e).
*   **Q7:** **Decimal** (d), **Divisiones** (f), **Residuos** (b).
*   **Q8:**
    1. 1010 -> **c) 10** (Justificación: 8 + 0 + 2 + 0 = 10)
    2. 1100 -> **d) 12** (Justificación: 8 + 4 + 0 + 0 = 12)
    3. 10001 -> **b) 17** (Justificación: 16 + 0 + 0 + 0 + 1 = 17)
    4. 111 -> **a) 7** (Justificación: 4 + 2 + 1 = 7)

## Resolución de Problemas (Q9-Q10)

**Q9. Conversión de 11011 a decimal:**
*   Identificación de valores por casilla (de derecha a izquierda): 1, 2, 4, 8, 16.
*   Aplicación del "interruptor" (1=sumar, 0=no sumar):
    *   (1 x 16) + (1 x 8) + (0 x 4) + (1 x 2) + (1 x 1)
*   Suma final: 16 + 8 + 0 + 2 + 1 = **27**.

**Q10. Aplicación $21 USD:**
*   **Expresión:** 16 + 4 + 1 = 21.
*   **Procedimiento:** Buscamos los valores de los billetes (potencias de 2) que sumados den 21.
    *   Billete de $16: **SÍ** (Resta 5)
    *   Billete de $8: **NO** (Se pasaría)
    *   Billete de $4: **SÍ** (Resta 1)
    *   Billete de $2: **NO** (Se pasaría)
    *   Billete de $1: **SÍ** (Resta 0)
*   Traducción a bits (Encendido/Apagado): 1 - 0 - 1 - 0 - 1.
*   **Resultado:** **10101**.

## Rúbrica de Evaluación

| Sección | Logrado (Puntaje Máximo) | En proceso | Por lograr |
| :--- | :--- | :--- | :--- |
| **Teoría (I, II, III)** | Identifica con precisión la base, los símbolos, el orden de lectura de residuos y el método de duplicación. | Confunde términos técnicos o comete errores de concordancia en el banco de palabras. | No reconoce los símbolos básicos ni el concepto de valor posicional. |
| **Relacionar (IV)** | Asocia correctamente los 4 valores binarios con sus decimales (1pt). | Relaciona 2 o 3 valores correctamente; presenta dudas en la posición de los bits (0.5pt). | No logra realizar conversiones mentales básicas o asocia al azar (0pt). |
| **Ejercicios (V, VI)** | Desarrolla procedimientos completos mostrando la suma de posiciones o divisiones; llega al resultado exacto. | El procedimiento es coherente, pero comete errores en la duplicación de valores o invierte el orden de los residuos al leer el resultado final. | No establece la relación entre el valor de la casilla y el dígito binario. |

## Escala de Desempeño y Retroalimentación

*   **10:** Excelente. Comprensión total de la lógica binaria y el pensamiento computacional.
*   **8-9:** Muy Bueno. Domina el método, aunque requiere mayor orden en el desarrollo.
*   **6-7:** Satisfactorio. Conoce el procedimiento, pero presenta errores de cálculo aritmético.
*   **4-5:** Suficiente. Presenta dificultades conceptuales en la base 2 y potencias.
*   **Menos de 4:** Necesita refuerzo. Requiere tutoría en división sucesiva y valor posicional.

**Observaciones del docente:**
*   **Error más frecuente:** ____________________________________________________
*   **Sección con menor rendimiento:** __________________________________________
*   **Fecha de aplicación:** ____/____/____