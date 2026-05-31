# Clase 14 — Introducción de factores en un radical y reducción de radicales a mínimo común índice

#algebra #introducingfact

Curso: [[00 - Índice del curso]] | Bloque 3 | Lección 14 de 14

> [!info] 🧭 Navegación
> [[Clase 13|⬅ Clase 13]] | [[00 - Índice del curso|Índice]] | **Clase 14** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]

---

> [!info] 🌍 Relevancia y aplicaciones
> Lograr que varios radicales compartan el mismo índice es el "puente" técnico necesario para realizar operaciones de multiplicación y división entre ellos. Sin esta homogeneización, no es posible aplicar las propiedades distributivas de la radicación.
> 
> - **💵 [Finanzas]**: Cálculo de tasas de interés compuesto que involucran diferentes periodos de tiempo (mensual vs. trimestral) expresados como radicales de distinto índice.
> - **🏗️ [Arquitectura]**: Ajuste de escalas en planos donde las dimensiones críticas se calculan con raíces para mantener proporciones exactas en estructuras no lineales.
> - **📊 [Crecimiento]**: Comparación de modelos de crecimiento exponencial en poblaciones o ahorros que requieren igualar los índices temporales para su análisis.

---

## 3. Conceptos Clave

> [!note] 📌 ¿Qué es introducir factores y reducir índice?
> - **Introducción de factores**: Proceso de trasladar un multiplicador externo al interior de la raíz. Para mantener la igualdad, el factor debe elevarse a una potencia igual al índice del radical.
> - **Reducción a común índice**: Proceso de transformar radicales distintos en otros equivalentes con igual índice. 
>   - **El "Porqué" Pedagógico**: Basándonos en las potencias fraccionarias, reducir a común índice es como **amplificar una fracción**. Si tenemos $\sqrt[3]{m^1} = m^{1/3}$ y queremos llevarla a índice 12, amplificamos la fracción por 4: $m^{4/12} = \sqrt[12]{m^4}$. El valor no cambia, solo su presentación.

> [!warning] ⚠️ Error común
> Solo se pueden introducir **factores** (elementos que multiplican al radical). Nunca se deben introducir sumandos o términos de una resta.
> - ❌ $2 + \sqrt{5} \neq \sqrt{5 \cdot 2^2}$ (El 2 es un sumando)
> - ✅ $2\sqrt{5} = \sqrt{5 \cdot 2^2}$ (El 2 es un factor)

> [!tip] 💡 Truco para recordarlo
> Piensa en el índice de la raíz como el **"peaje"** o impuesto que el factor debe pagar para entrar en la "casa" del radical. Si la casa es de grado $n$, el factor debe pagar elevándose a la potencia $n$.

---

## 4. Procedimientos Paso a Paso

```text
PROCEDIMIENTO: INTRODUCCIÓN DE FACTORES
PASO 1 → Identificar el índice de la raíz.
PASO 2 → Elevar el factor externo a una potencia igual al índice. 
         *Nota: Si el factor ya tiene un exponente, aplica la "Potencia de otra Potencia" 
         (multiplica el exponente del factor por el índice de la raíz).*
PASO 3 → Multiplicar el resultado por el contenido original del radical.
PASO 4 → Simplificar la operación numérica si es posible.
```

```text
PROCEDIMIENTO: REDUCCIÓN A COMÚN ÍNDICE
PASO 1 → Hallar el Mínimo Común Múltiplo (MCM) de todos los índices involucrados. 
         Este será nuestro "Nuevo Índice".
PASO 2 → Dividir el MCM por el índice original de cada raíz para hallar el 
         "Factor de Amplificación".
PASO 3 → Multiplicar tanto el índice como TODOS los exponentes internos por dicho factor.
         *RECUERDA: Si un término no tiene exponente visible, su exponente es 1.*
```

---

## 5. Ejemplos Prácticos

> [!example] Casos de estudio guiados
> 
> **Ejemplo 1 (Básico):** Introducir $2$ en $\sqrt[3]{5}$
> 1. El índice es 3. Elevamos el factor: $2^3 = 8$.
> 2. Operamos dentro: $\sqrt[3]{5 \cdot 8} = \sqrt[3]{40}$.
> 
> **Ejemplo 2 (Signos):** Introducir $-5$ en $\sqrt{3}$
> - **Lógica:** Al ser un índice par, si introducimos el signo menos $(-5)^2$ se volvería $+25$, cambiando el signo original de la expresión (de negativo a positivo). 
> - **Regla:** El negativo se deja **fuera**.
> - **Resultado:** $- \sqrt{3 \cdot 5^2} = - \sqrt{3 \cdot 25} = -\sqrt{75}$.
> 
> **Ejemplo 3 (Avanzado):** Reducir $\sqrt[3]{m}$ y $\sqrt[4]{m}$ a común índice.
> 1. $\text{MCM}(3, 4) = 12$.
> 2. Raíz 1: $12 \div 3 = 4$. Elevamos $m^1 \to m^{1 \cdot 4} = \sqrt[12]{m^4}$.
> 3. Raíz 2: $12 \div 4 = 3$. Elevamos $m^1 \to m^{1 \cdot 3} = \sqrt[12]{m^3}$.
> 
> **Ejemplo 4 ($USD):** Una inversión crece a una tasa de $2\sqrt[2]{10}$ USD. Introducir el factor para facilitar comparaciones.
> - Paso: $\sqrt{10 \cdot 2^2} = \sqrt{10 \cdot 4}$.
> - **Resultado:** $\sqrt{40}$ USD.

---

## 6. Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Verde (Fácil)
> 1. Introducir el factor: $3\sqrt{2}$
> 2. Introducir el factor: $2\sqrt[3]{3}$
> 3. Introducir el factor: $5\sqrt{x}$
> 4. Introducir el factor: $4\sqrt[3]{2}$

> [!abstract] 🟡 Nivel Amarillo (Medio)
> Reducir a mínimo común índice los siguientes pares:
> 1. $\sqrt{a}$ y $\sqrt[3]{a}$
> 2. $\sqrt[3]{2}$ y $\sqrt[4]{3}$
> 3. $\sqrt{5x}$ y $\sqrt[3]{2x}$
> 4. $\sqrt[4]{m^2}$ y $\sqrt[6]{m^3}$

> [!abstract] 🔴 Nivel Rojo (Avanzado $USD)
> 1. **Contabilidad:** Un software solo acepta "radicales puros". Si el costo es $3x\sqrt{2x}$ USD, ¿cómo debe ingresarse el valor tras introducir el factor $3x$?
> 2. Reducir a índice común las expresiones: $\sqrt{3}$, $\sqrt[3]{2}$ y $\sqrt[4]{5}$.
> 3. **Comparación:** ¿Cuál es el mayor precio? Expresa $\sqrt[5]{2}$ USD y $\sqrt[2]{3}$ USD con un mismo índice (MCM 10) para decidir.
> 4. Introducir factores y simplificar aplicando potencia de otra potencia: $2a^2b\sqrt[3]{3ab^2}$

> [!success] ✅ Soluciones para el Docente
> **Verde:** 1) $\sqrt{18}$ | 2) $\sqrt[3]{24}$ | 3) $\sqrt{25x}$ | 4) $\sqrt[3]{128}$
> **Amarillo:** 1) $\sqrt[6]{a^3}, \sqrt[6]{a^2}$ | 2) $\sqrt[12]{2^4}, \sqrt[12]{3^3}$ | 3) $\sqrt[6]{125x^3}, \sqrt[6]{4x^2}$ | 4) $\sqrt[12]{m^6}, \sqrt[12]{m^6}$ (Ambas resultan iguales al simplificar/amplificar).
> **Rojo:** 
> 1) $\sqrt{18x^3}$ USD (Cálculo: $(3x)^2 \cdot 2x = 9x^2 \cdot 2x = 18x^3$).
> 2) $\sqrt[12]{3^6}, \sqrt[12]{2^4}, \sqrt[12]{5^3}$ (Índices: 729, 16, 125).
> 3) $\sqrt[10]{4}$ USD y $\sqrt[10]{243}$ USD. (Claramente $\sqrt[10]{243}$ es mayor).
> 4) $\sqrt[3]{24a^7b^5}$ (Cálculo: $2^3(a^2)^3 b^3 \cdot 3ab^2 = 8a^6b^3 \cdot 3ab^2 = 24a^7b^5$).

---

## 7. Autoevaluación

> [!question] Pregunta 1
> ¿Qué exponente debe adquirir un factor externo para poder ingresar legalmente a una raíz de índice $n$?
> - a) $1$
> - b) $n$
> - c) $n-1$
> - d) No necesita exponente.
> 
> **Respuesta: b.** Explicación: Se debe elevar al índice para contrarrestar la operación de raíz y mantener el valor original.

> [!question] Pregunta 2
> Al reducir $\sqrt[3]{a}$ y $\sqrt[4]{b}$ a común índice, ¿por cuánto debemos multiplicar los exponentes internos de la primera raíz ($\sqrt[3]{a}$)?
> - a) 3
> - b) 12
> - c) 4
> - d) 1
> 
> **Respuesta: c.** Explicación: El MCM es 12. Como el índice original era 3, el factor de amplificación es $12 \div 3 = 4$.

> [!question] Pregunta 3
> Si un descuento financiero se representa como $-3\sqrt{2}$ USD, ¿cuál es la forma correcta de introducir el factor numérico?
> - a) $\sqrt{-18}$
> - b) $\sqrt{18}$
> - c) $-\sqrt{18}$
> - d) $-\sqrt{6}$
> 
> **Respuesta: c.** Explicación: El signo se mantiene fuera porque el índice es par. Introducimos el 3 como $3^2 = 9$, y $9 \cdot 2 = 18$.

---

> [!tip] 💡 En la próxima clase
> Con el dominio de la reducción a común índice, estamos listos para el último paso del bloque: **Multiplicación y división de radicales de distinto índice**. ¡Aquí es donde toda la teoría se une!

> [!info] 🧭 Navegación
> [[Clase 13|⬅ Clase 13]] | [[00 - Índice del curso|Índice]] | **Clase 14** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]