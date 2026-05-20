# Clase 09 — Resolución de problemas con ecuaciones — parte 1

tags: #algebra #ecuaciones

> [!info] 🧭 Navegación
> [[Indice_Algebra]] | [[Bloque_Ecuaciones]]

## 1. Importancia y Aplicaciones Reales

> [!info] 🌍 Relevancia y aplicaciones en la vida real
> Aprender a plantear ecuaciones es la habilidad de "traducir" situaciones del mundo real al lenguaje matemático. Esta herramienta nos permite encontrar soluciones exactas a problemas que la intuición no siempre resuelve de inmediato.
> 
> **Caso en $USD:** Supón que quieres adquirir un fondo de inversión y una cuenta de ahorros. Si el fondo exige un capital que es el doble de lo que tienes en la cuenta y el total necesario es de **$45 USD**, plantear la ecuación $2n + n = 45$ te permite determinar con precisión que necesitas $15 en la cuenta y $30 en el fondo. El álgebra garantiza que tus proyecciones financieras sean rigurosas.

## 2. Conceptos Clave

> [!note] 📌 Resolución de Problemas Contextualizados
> Resolver un problema algebraico consiste en transformar el **lenguaje común** (enunciado verbal) en **lenguaje algebraico** (una igualdad con una incógnita). Antes de escribir, recuerda que la lógica es tu primera aliada: estima un resultado mentalmente para validar si tu ecuación tiene sentido.

> [!warning] ⚠️ El Peligro de los Paréntesis
> Un error frecuente es omitir los paréntesis en expresiones compuestas. Por ejemplo, "el doble del sucesor de un número" se escribe como $2(n + 1)$. Si escribes $2n + 1$, estarías calculando "el doble de un número aumentado en uno". Siempre usa paréntesis al multiplicar expresiones que representen sucesores, antecesores o edades futuras/pasadas para aplicar correctamente la propiedad distributiva.

> [!tip] 💡 La Técnica del Profe Alex para Fracciones
> Para simplificar una ecuación con denominadores, el **Profe Alex** recomienda multiplicar **cada término de la ecuación** por el denominador común. Esto elimina las fracciones de inmediato y te permite trabajar con números enteros, lo cual es mucho más sencillo y seguro.

## 3. Procedimiento Paso a Paso

Sigue esta metodología estructurada para evitar confusiones en el planteamiento:

```text
PASO 1: Identificar la pregunta y asignar una letra a la incógnita. 
        Nota: Aunque puedes usar cualquier letra (x, a, b), usamos '$n$' 
        preferentemente para números.
PASO 2: Realizar un análisis lógico inicial (estimar el resultado).
PASO 3: Traducir el enunciado a lenguaje algebraico y formar la ecuación.
PASO 4: Resolver la ecuación despejando la incógnita (mostrando pasos intermedios).
PASO 5: Verificar la solución. IMPORTANTE: Sustituye el valor obtenido en 
        el texto original del problema, NO en la ecuación que escribiste, 
        para asegurar que la lógica sea correcta.
```

## 4. Ejemplos Desarrollados

> [!example] Ejemplo 1 — El número y su mitad (Video 1)
> **Enunciado:** El doble de un número y su mitad suman $45$.
> - **Análisis Lógico:** Si el número fuera $20$, su doble es $40$ y su mitad $10$, sumando $50$. Como buscamos $45$, el número debe ser un poco menor que $20$.
> - **Planteamiento:** $2n + \frac{n}{2} = 45$
> - **Resolución:** Multiplicamos toda la ecuación por $2$ para eliminar el denominador:
>   $2(2n) + 2(\frac{n}{2}) = 2(45) \rightarrow 4n + n = 90 \rightarrow 5n = 90$
> - **Resultado:** $n = 18$. (Verificación: $36 + 9 = 45$).

> [!example] Ejemplo 2 — Resta y resultado (Video 2)
> **Enunciado:** Si al doble de un número le restamos $14$ se obtiene $30$.
> - **Análisis Lógico:** Buscamos un número que, al restarle algo, dé $30$, por lo que el "doble" debe ser cercano a $44$.
> - **Planteamiento:** $2n - 14 = 30$
> - **Resolución:** $2n = 30 + 14 \rightarrow 2n = 44 \rightarrow n = \frac{44}{2}$
> - **Resultado:** $n = 22$.

> [!example] Ejemplo 3 — Números consecutivos (Video 3)
> **Enunciado:** La suma de dos números consecutivos es $451$.
> - **Análisis Lógico:** Si los números son casi iguales y suman $451$, cada uno debe estar cerca de la mitad de $450$, es decir, alrededor de $225$.
> - **Planteamiento:** $n + (n + 1) = 451$
> - **Resolución:** $2n + 1 = 451 \rightarrow 2n = 450 \rightarrow n = 225$
> - **Resultado:** El primer número es $225$ y su consecutor $(n+1)$ es $226$.

> [!example] Ejemplo 4 — El triple y el sucesor (Video 4)
> **Enunciado:** Al sumar el triple de un número con el doble de su sucesor se obtiene $42$.
> - **Análisis Lógico:** Probamos con $n=10$: $3(10) + 2(11) = 52$. Es muy alto, probemos con $n=8$: $3(8) + 2(9) = 24 + 18 = 42$.
> - **Planteamiento:** $3n + 2(n + 1) = 42$
> - **Resolución (Propiedad Distributiva):**
>   $3n + 2n + 2 = 42 \rightarrow 5n + 2 = 42 \rightarrow 5n = 40$
> - **Resultado:** $n = 8$. (Aquí aplicamos el paréntesis para no olvidar multiplicar el $+1$).

> [!example] Ejemplo 5 — Problema de edades y proyecciones (Video 5)
> **Enunciado:** Un padre tiene $37$ años y su hijo $9$. ¿En cuántos años la edad del padre será el triple que la del hijo?
> - **Análisis Lógico:** El tiempo pasa para ambos. Si pasan $a$ años, ambos envejecen la misma cantidad.
> - **Planteamiento:** $37 + a = 3(9 + a)$
> - **Resolución:** $37 + a = 27 + 3a \rightarrow 37 - 27 = 3a - a \rightarrow 10 = 2a$
> - **Resultado:** $a = 5$. Dentro de $5$ años, el padre tendrá $42$ y el hijo $14$ ($14 \times 3 = 42$).
> 
> > [!tip] Aplicación Financiera $USD
> > Este cálculo es idéntico a las proyecciones de ahorro. Si tienes un capital inicial y una meta de ahorro, y ambos reciben un depósito mensual idéntico ($a$), puedes calcular en qué mes tu capital acumulado llegará a ser el triple de tu aporte mensual.

## 5. Ejercicios para el Estudiante

🟢 **Nivel Fácil:**
El triple de un número disminuido en $8$ equivale al número aumentado en $24$. Hallar el número $n$.
*(Pista: "Equivale" significa $=$ y "disminuido" significa resta).*

🟡 **Nivel Medio:**
La suma de tres números consecutivos es $81$. Hallar los tres números.
*(Pista: Define los números como $n$, $n+1$ y $n+2$).*

🔴 **Nivel Avanzado (Contexto $USD):**
La diferencia entre el quíntuple del antecesor de un precio en **$USD** y el triple de su sucesor es $24$. ¿Cuál es el precio base $n$?
*(Recordatorio: Antecesor es $n-1$, sucesor es $n+1$, y diferencia es una resta).*

## 6. Respuestas y Autoevaluación

> [!success] ✅ Soluciones a los ejercicios
> 1. **Resultado:** $n = 16$.
> 2. **Resultado:** Los números son $\{26, 27, 28\}$. (Planteamiento: $n + n+1 + n+2 = 81 \rightarrow 3n + 3 = 81$).
> 3. **Resultado:** $n = 16$. (Planteamiento: $5(n-1) - 3(n+1) = 24$).

> [!question] ¿Qué operación representa la palabra "diferencia" en matemáticas?
> a) Una suma de términos.
> b) El resultado de una multiplicación.
> c) El resultado de una resta. **(Correcta)**

> [!question] ¿Cómo se representa algebraicamente el sucesor de un número $n$?
> a) $n - 1$
> b) $n + 1$ **(Correcta)**
> c) $2n$

> [!question] ¿Cuál es la ventaja de multiplicar toda la ecuación por el denominador?
> a) Cambia el resultado final para que sea más fácil.
> b) Elimina las fracciones para trabajar con números enteros. **(Correcta)**
> c) Permite ignorar la incógnita temporalmente.

## 7. Cierre y Navegación Final

> [!tip] 💡 En la próxima clase...
> Profundizaremos en problemas que involucran múltiples fracciones simultáneas y situaciones con más de una variable (Parte 2). ¡Sigue practicando tu traducción al lenguaje algebraico!

> [!info] 🧭 Navegación
> [[Indice_Algebra]] | [[Bloque_Ecuaciones]]