# Clase 14 — Convert an exact decimal to a fraction

#algebra #convertanexactd

Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 14 de 22

> [!info] 🧭 Navegación
> [[Clase 13|⬅ Clase 13]] | [[00 - Índice del curso|Índice]] | **Clase 14** | [[Clase 15|Clase 15 ➡]]

---

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> Convertir decimales exactos (aquellos con una cantidad finita de cifras) a fracciones es fundamental para trabajar con valores exactos en lugar de aproximaciones. Al **amplificar** un decimal, creamos una **fracción equivalente** que mantiene el valor original pero facilita cálculos más complejos.
> 
> - 💵 **Finanzas:** Calcular el valor exacto de una moneda (ej. $0,75 USD es exactamente $\frac{3}{4}$ de dólar).
> - 🏗️ **Construcción:** Interpretar planos donde las medidas exactas como **1,25 metros** se representan como $\frac{5}{4}$ de metro para cortes de precisión.
> - 📊 **Estadística:** Expresar resultados de datos finitos de forma clara y profesional.

---

## Concepto clave

> [!note] 📌 ¿Qué es Convert an exact decimal to a fraction?
> Un **decimal exacto** es un número que tiene una parte decimal **finita** (un número limitado de cifras después de la coma). A diferencia de los decimales periódicos, estos no se repiten infinitamente.

> [!warning] ⚠️ Error común
> El error más frecuente es no **simplificar** la fracción final. Por ejemplo, dejar el resultado como $\frac{125}{100}$ es técnicamente correcto en valor, pero matemáticamente incompleto. La respuesta final siempre debe ser la fracción irreducible, en este caso: $\frac{5}{4}$.

> [!tip] 💡 Truco para recordarlo
> El número de **ceros** en la potencia de 10 es igual al número de cifras que hay después de la coma. 
> - 1 cifra decimal $\rightarrow$ usa $10^1 = 10$
> - 2 cifras decimales $\rightarrow$ usa $10^2 = 100$
> - 3 cifras decimales $\rightarrow$ usa $10^3 = 1000$

---

## Procedimiento paso a paso

Para transformar un decimal exacto, seguimos este proceso lógico:

```text
PASO 1: Escribir el decimal como el numerador de una fracción con denominador 1.
PASO 2: Identificar el número de cifras decimales (después de la coma).
PASO 3: Amplificar la fracción multiplicando numerador y denominador por la 
        potencia de 10 correspondiente (10, 100, 1000, etc.).
PASO 4: Simplificar la fracción resultante hasta su mínima expresión.
```

---

## Ejemplos Prácticos Detallados

````ad-example
**Ejemplo 1: Conversión básica (12,3)**
1. Escribimos el decimal sobre la unidad: $\frac{12,3}{1}$.
2. Como hay **1 cifra decimal**, amplificamos por $10^1 = 10$:
   $$\frac{12,3 \times 10}{1 \times 10} = \frac{123}{10}$$
3. Verificamos simplificación: 123 no es divisible por 2 ni por 5.
**Resultado:** $\mathbf{\frac{123}{10}}$
````

````ad-example
**Ejemplo 2: Con simplificación (1,25)**
1. Escribimos sobre la unidad: $\frac{1,25}{1}$.
2. Hay **2 cifras decimales**, amplificamos por $10^2 = 100$:
   $$\frac{1,25 \times 100}{1 \times 100} = \frac{125}{100}$$
3. Simplificamos dividiendo entre 5 de forma sucesiva:
   $$\frac{125 \div 5}{100 \div 5} = \frac{25}{20}$$
   $$\frac{25 \div 5}{20 \div 5} = \frac{5}{4}$$
**Resultado:** $\mathbf{\frac{5}{4}}$
````

````ad-example
**Ejemplo 3: Caso avanzado (52,324)**
1. Amplificamos por $10^3 = 1000$ (3 cifras decimales):
   $$\frac{52,324 \times 1000}{1 \times 1000} = \frac{52324}{1000}$$
2. Simplificamos mediante mitades sucesivas ($\div 2$):
   $$\frac{52324 \div 2}{1000 \div 2} = \frac{26162}{500}$$
   $$\frac{26162 \div 2}{500 \div 2} = \frac{13081}{250}$$
**Resultado:** $\mathbf{\frac{13081}{250}}$
````

````ad-example
**Ejemplo 4: Aplicación en $USD**
Si un dulce cuesta **$0,75**, ¿qué fracción de dólar representa?
1. Escribimos $\frac{0,75}{1}$ y amplificamos por $100$:
   $$\frac{75}{100}$$
2. Simplificamos por 5: $\frac{75 \div 5}{100 \div 5} = \frac{15}{20}$
3. Simplificamos por 5 nuevamente: $\frac{15 \div 5}{20 \div 5} = \frac{3}{4}$
**Resultado:** El dulce cuesta $\mathbf{\frac{3}{4}}$ de dólar.
````

---

## Bloques de Ejercicios

````ad-abstract
**Nivel Verde (Fácil)**
Convierte a fracción y simplifica si es necesario:
1. $0,2$
2. $0,8$
3. $1,5$
4. $4,2$
````

````ad-abstract
**Nivel Amarillo (Medio)**
Obtén la fracción irreducible:
1. $0,45$
2. $0,120$ (Pista: el cero final se puede omitir o simplificar al inicio).
3. $2,50$
4. $0,64$
````

````ad-abstract
**Nivel Rojo (Avanzado)**
Problemas de aplicación contextualizada:
1. Un tornillo de precisión mide **1,20 cm**. Exprésalo en fracción.
2. Un dulce pequeño cuesta **$0,05**. ¿Qué fracción de dólar es?
3. Un envase de laboratorio pesa **0,250 kg**. Exprésalo en fracción.
4. Una cinta de medir marca **3,125 m**. Exprésalo en fracción irreducible.
````

> [!success] ✅ Solucionario para el docente
> - **Fácil:** 1) $\frac{1}{5}$ | 2) $\frac{4}{5}$ | 3) $\frac{3}{2}$ | 4) $\frac{21}{5}$
> - **Medio:** 1) $\frac{9}{20}$ | 2) $\frac{3}{25}$ (de $\frac{120}{1000} \rightarrow \frac{12}{100}$) | 3) $\frac{5}{2}$ | 4) $\frac{16}{25}$
> - **Avanzado:** 1) $\frac{6}{5}$ cm | 2) $\frac{1}{20}$ de dólar | 3) $\frac{1}{4}$ kg | 4) $\frac{25}{8}$ m

---

## Mini-prueba de autoevaluación

````ad-question
**Pregunta 1:** ¿Qué define a un decimal para que lo llamemos "exacto"?
**Respuesta:** Que tiene un número **finito** de cifras decimales (no se repiten al infinito).
````

````ad-question
**Pregunta 2:** Para convertir el número $0,007$, ¿por qué potencia de 10 debemos amplificar?
**Respuesta:** Por **1000** ($10^3$), ya que tiene tres posiciones decimales después de la coma.
````

````ad-question
**Pregunta 3:** Si un artículo cuesta $0,50, ¿cuál es su fracción simplificada?
**Respuesta:** $\mathbf{\frac{1}{2}}$. El proceso es $\frac{50}{100} \rightarrow \frac{5}{10} \rightarrow \frac{1}{2}$.
````

---

## Notas para el próximo tema

> [!tip] 💡 En la próxima clase
> Una vez dominados los decimales exactos, pasaremos a un reto mayor: los **decimales periódicos puros**. Aprenderemos qué hacer cuando los números se repiten infinitamente (como $0,333...$) y cómo usar el número 9 en el denominador.

> [!info] 🧭 Navegación
> [[Clase 13|⬅ Clase 13]] | [[00 - Índice del curso|Índice]] | **Clase 14** | [[Clase 15|Clase 15 ➡]]