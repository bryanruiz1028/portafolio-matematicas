# Clase 18 — Convert a mixed recurring decimal to a fraction | Example 1 + Convert a mixed recurring decimal to a fraction | Example 2

> [!info] 🧭 Navegación
> ⬅️ [Clase 17](link_clase_17) | 📋 [Índice](link_indice) | ➡️ [Clase 19](link_clase_19)

---

## RELEVANCIA Y APLICACIONES

La conversión de decimales periódicos mixtos a fracciones es esencial para obtener una precisión absoluta en disciplinas donde el error por redondeo puede comprometer la seguridad o la rentabilidad, permitiendo trabajar con valores exactos en lugar de aproximaciones decimales infinitas.

*   **💵 Aplicación con $USD**: Calcular con exactitud el pago de intereses o tarifas recurrentes, como un cobro de $3,5\overline{8}$ USD, evitando la pérdida de centavos que ocurre al truncar decimales en transacciones bancarias masivas.
*   **🏗️ Aplicación práctica**: Traducir medidas de planos arquitectónicos (ej. $7,0\overline{5}$ metros) a fracciones exactas para asegurar que el corte de materiales en obra sea perfecto.
*   **📊 Situación cotidiana**: Garantizar la repartición equitativa de recursos (combustible, alimentos o herencias) que resultan en cifras decimales infinitas, asegurando que no sobre ni falte nada.

---

## CONCEPTO CLAVE

Un **decimal periódico mixto** es aquel que, en su parte decimal, presenta una combinación de dos elementos: primero, una cifra o grupo de cifras que no se repiten (denominado **anteperiodo**) y, posteriormente, una cifra o grupo de cifras que se repiten infinitamente (denominado **periodo**).

> [!warning] Error Común
> El error más frecuente en los estudiantes es olvidar restar la parte no periódica en el numerador. No basta con escribir las cifras del número; es obligatorio restar todas las cifras que se encuentran antes del periodo (incluyendo la parte entera) para que la igualdad matemática se mantenga.

> [!tip] El Truco de las "Flechas que no se cruzan"
> Para recordar el orden correcto del denominador sin confundirse:
> 1. Mira las cifras bajo la raya del **periodo**: cada una baja y se convierte en un $9$.
> 2. Mira las cifras del **anteperiodo**: cada una baja y se convierte en un $0$.
> Al visualizar que las flechas bajan en orden directo hacia el denominador, recordarás que los $9$ siempre se escriben a la izquierda de los $0$.

---

## PROCEDIMIENTO PASO A PASO

```text
PASO 1: Escribir el número completo en el numerador (sin coma y sin raya de periodo).
PASO 2: Restar al número anterior la parte que NO tiene periodo (la unión del 
        entero y el anteperiodo, sin la coma).
PASO 3: En el denominador, colocar tantos "9" como cifras tenga el periodo y 
        tantos "0" como cifras tenga el anteperiodo (decimales no periódicos).
PASO 4: Realizar la resta en el numerador y simplificar la fracción resultante 
        hasta su mínima expresión.
PASO 5: Verificación. Dividir el numerador entre el denominador obtenido; el 
        resultado debe coincidir con el decimal original.
```

---

## EJEMPLOS GUIADOS

> [!example] Ejemplo 1: Convertir $7,0\overline{5}$
> 1.  **Numerador**: Escribimos el número completo ($705$) y restamos la parte que no se repite ($70$). Operación: $705 - 70 = 635$.
> 2.  **Denominador**: El periodo tiene una cifra ($5$), ponemos un $9$. El anteperiodo tiene una cifra ($0$), ponemos un $0$. Obtenemos $90$.
> 3.  **Fracción**: $\frac{635}{90}$.
> 4.  **Simplificación**: Como terminan en $5$ y $0$, dividimos entre $5$: $635 \div 5 = 127$ y $90 \div 5 = 18$.
> 5.  **Verificación**: Al dividir $127 \div 18$, obtenemos exactamente $7,0555...$
> **Resultado final**: $\frac{127}{18}$

> [!example] Ejemplo 2: Convertir $3,2\overline{45}$
> 1.  **Numerador**: $3245 - 32 = 3213$.
> 2.  **Denominador**: El periodo tiene dos cifras ($45$), ponemos dos $9$. El anteperiodo tiene una cifra ($2$), ponemos un $0$. Obtenemos $990$.
> 3.  **Fracción**: $\frac{3213}{990}$.
> 4.  **Simplificación**: Dividimos entre $3$ (ya que la suma de sus cifras es múltiplo de 3): $3213 \div 3 = 1071$ y $990 \div 3 = 330$. Dividimos nuevamente entre $3$: $1071 \div 3 = 357$ y $330 \div 3 = 110$. El número $357$ no es divisible por $2$ ni por $5$, y $110$ no es divisible por $3$, por lo que la fracción es irreducible.
> **Resultado final**: $\frac{357}{110}$

> [!example] Ejemplo 3: Convertir $0,4\overline{6}$
> 1.  **Numerador**: $46 - 4 = 42$. *Nota: Al retirar la coma para formar un entero, los ceros a la izquierda pierden su valor posicional, por lo que $046$ se escribe simplemente como $46$.*
> 2.  **Denominador**: Una cifra periódica ($6$) = un $9$. Una cifra en el anteperiodo ($4$) = un $0$. Obtenemos $90$.
> 3.  **Fracción**: $\frac{42}{90}$.
> 4.  **Simplificación**: Sacamos mitad: $\frac{21}{45}$. Luego sacamos tercera: $\frac{7}{15}$.
> **Resultado final**: $\frac{7}{15}$

> [!example] Caso Especial de Aplicación Financiera: $8,75\overline{9}$ USD
> Al aplicar el procedimiento en este precio:
> Numerador: $8759 - 875 = 7884$.
> Denominador: Un $9$ (por el periodo $9$) y dos $0$ (por el anteperiodo $75$).
> Fracción: $\frac{7884}{900} = \frac{219}{25}$ (tras simplificar por $4$ y luego por $9$).
> **Consecuencia económica**: Si divides $219 \div 25$, el resultado es exactamente $8,76$. Esto ocurre porque un periodo de $9$ tiende a redondear la cifra inmediatamente anterior. En un banco, una deuda recurrente de $8,75\overline{9}$ se cobraría exactamente como $8,76$ USD.

---

## EJERCICIOS PARA EL ESTUDIANTE

*   **🟢 Verde (Fácil)**:
    1.  Convertir $1,7\overline{8}$
    2.  Convertir $0,4\overline{6}$
*   **🟡 Amarillo (Medio)**:
    1.  Convertir $5,2\overline{18}$
    2.  Convertir $0,8\overline{12}$
*   **🔴 Rojo (Avanzado)**:
    1.  El costo de un servicio es de $3,5\overline{8}$ USD. Representa este valor como una fracción simplificada para un reporte contable de alta precisión.

> [!success] Bloque de Respuestas
> *   **Verde**: 
>     1. $\frac{161}{90}$ 
>     2. $\frac{7}{15}$
>
> *   **Amarillo**: 
>     1. $\frac{5166}{990} \rightarrow \frac{287}{55}$ 
>     2. $\frac{804}{990} \rightarrow \frac{134}{165}$
>
> *   **Rojo**: 
>     $(358 - 35) / 90 = \frac{323}{90}$ USD.

---

## MINI-PRUEBA DE AUTOEVALUACIÓN

1.  **¿Qué determina la cantidad de ceros en el denominador de la fracción?**
    *   a) La cantidad de cifras de la parte entera.
    *   b) La cantidad de cifras bajo la raya del periodo.
    *   c) La cantidad de cifras del anteperiodo (decimales no periódicos).
    *   d) El valor del primer decimal.

2.  **En la conversión del número $0,2\overline{5}$, ¿cuál es el numerador antes de realizar la resta?**
    *   *Respuesta*: Es **25**. El procedimiento dicta escribir el número sin coma ni raya; luego se le restaría el anteperiodo ($2$), quedando $\frac{25 - 2}{90} = \frac{23}{90}$.

3.  **Si un producto cuesta $1,3\overline{3}$ USD, ¿cuál es su fracción simplificada?**
    *   *Respuesta*: $\frac{13 - 1}{9} = \frac{12}{9} = \frac{4}{3}$ USD. Aunque este caso es periódico puro, el método de resta sigue siendo consistente.

**Respuestas Autoevaluación:**
1. **c)** Los ceros siempre representan a la parte decimal que no se repite.
2. **25**. Recuerda siempre restar la parte no periódica después de identificar este número.
3. **$\frac{4}{3}$**. Al verificar $4 \div 3$, obtendrás el $1,333...$ original.

---

## CIERRE Y NAVEGACIÓN FINAL

En la próxima clase, profundizaremos en ejercicios de mayor complejidad técnica y analizaremos casos donde el resultado decimal de la fracción parece alejarse visualmente de la cifra inicial, explorando los límites de los números racionales.

> [!info] 🧭 Navegación
> ⬅️ [Clase 17](link_clase_17) | 📋 [Índice](link_indice) | ➡️ [Clase 19](link_clase_19)