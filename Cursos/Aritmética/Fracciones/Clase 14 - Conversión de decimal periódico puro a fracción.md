# Clase 14 — Conversión de decimal periódico puro a fracción

[[Clase 13]] | [[00 - Índice del curso]]

---

> [!info] 🌍 Relevancia y aplicaciones
> Convertir decimales periódicos a fracciones es una habilidad esencial para garantizar la precisión matemática absoluta. A diferencia de los decimales infinitos, que obligan a realizar redondeos, las fracciones permiten operar con el valor real y exacto de un número.
> 
> * 💵 **Finanzas:** Comprender por qué un valor de $5.\overline{9}$ es una **equivalencia exacta** a $6$ permite cierres contables sin fugas de centavos.
> * 🏗️ **Ingeniería:** En el diseño estructural, el uso de fracciones evita errores acumulativos en medidas repetitivas que, de otro modo, comprometerían la seguridad de la obra.
> * 📊 **Estadística:** Permite representar proporciones que no cierran en decimales simples (como $1/3$ de una muestra poblacional) sin perder datos en el análisis.

---

> [!note] 📌 ¿Qué es un decimal periódico puro?
> Es aquel número decimal donde el **periodo** (la cifra o grupo de cifras que se repiten infinitamente) comienza **inmediatamente después** de la coma decimal.
> 
> * **Ejemplo:** En $1.\overline{36}$, el periodo "36" inicia justo tras la coma.

> [!warning] ⚠️ Error común
> Un error frecuente es tratar un decimal periódico como si fuera exacto. Por ejemplo, afirmar que $0.333... = \frac{3}{10}$. La realidad es que $0.\overline{3} = \frac{3}{9}$, lo cual simplificado resulta en $\frac{1}{3}$.

> [!tip] 💡 Truco para recordarlo
> "Tantos nueves en el denominador como cifras tenga el sombrero (periodo)". Si el periodo tiene una cifra, usa un $9$; si tiene dos, usa $99$.

---

### Procedimiento paso a paso (Método de sustracción rápida)

Para convertir un decimal periódico puro a fracción de forma eficiente, aplicamos el siguiente algoritmo:

```text
PASO 1 → Escribir el número completo (sin coma ni marca de periodo).
PASO 2 → Restar la parte entera (todo lo que está a la izquierda de la coma).
PASO 3 → Colocar como denominador tantos "9" como cifras tenga el periodo.
PASO 4 → Simplificar la fracción resultante hasta su mínima expresión.
```

---

### Ejemplos resueltos

> [ad-example] **Ejemplo 1: Caso básico ($1.\overline{12}$)**
> 1. **Numerador:** Escribimos el número sin coma ($112$) y restamos la parte entera ($1$): $112 - 1 = 111$.
> 2. **Denominador:** El periodo ($12$) tiene dos cifras, por lo tanto usamos $99$.
> 3. **Fracción resultante:** $\frac{111}{99}$.
> 4. **Simplificación:** Dividimos entre 3 (ya que $1+1+1=3$, múltiplo de 3):
>    $$\frac{111 \div 3}{99 \div 3} = \frac{37}{33}$$

> [ad-example] **Ejemplo 2: Parte entera cero ($0.\overline{3}$)**
> 1. **Numerador:** $3 - 0 = 3$.
> 2. **Denominador:** Una cifra en el periodo, usamos un $9$.
> 3. **Fracción:** $\frac{3}{9}$.
> 4. **Simplificación:** Sacamos tercera parte.
> **Resultado:** $\frac{1}{3}$

> [ad-example] **Ejemplo 3: Caso avanzado ($34.\overline{36}$)**
> 1. **Numerador:** $3436 - 34 = 3402$.
> 2. **Denominador:** Dos cifras en el periodo ($36$), usamos $99$.
> 3. **Simplificación Paso a Paso:** 
>    *Aplicamos la **Regla del 3**: Sumamos los dígitos de 3402 ($3+4+0+2=9$). Como 9 es múltiplo de 3, simplificamos:*
>    $$\frac{3402 \div 3}{99 \div 3} = \frac{1134 \div 3}{33 \div 3} = \frac{378}{11}$$
> **Resultado:** $\frac{378}{11}$

> [ad-example] **Ejemplo 4: El caso del periodo 9 ($5.\overline{9}$)**
> Este caso es especial porque demuestra una **equivalencia exacta**.
> 1. **Operación:** $\frac{59 - 5}{9} = \frac{54}{9}$.
> 2. **Resultado:** $54 \div 9 = 6$.
> **Análisis pedagógico:** Matemáticamente, $5.\overline{9}$ no solo "se parece" al 6, sino que **es igual a 6**. Es como un televisor de $\$999.\overline{99}$ dólares; su valor real y contable es exactamente $\$1000$.

---

### Ejercicios para el estudiante

> [ad-abstract] **Practica lo aprendido**
> **Nivel Verde (Fácil):**
> 1. Convierte $0.\overline{6}$ a fracción.
> 
> **Nivel Amarillo (Medio):**
> 2. Convierte $3.\overline{6}$ a fracción.
> 3. Convierte $5.\overline{18}$ a fracción (Simplifica hasta llegar a onceavos).
> 
> **Nivel Rojo (Avanzado):**
> 4. Demuestra mediante el método de la fracción por qué $12.\overline{9}$ equivale exactamente a $13$.

> [ad-success] **Soluciones (Clave de respuestas)**
> 1. $0.\overline{6} = \frac{6}{9} = \frac{2}{3}$
> 2. $3.\overline{6} = \frac{36-3}{9} = \frac{33}{9} = \frac{11}{3}$
> 3. $5.\overline{18} = \frac{518-5}{99} = \frac{513}{99} = \frac{513 \div 9}{99 \div 9} = \frac{57}{11}$
> 4. $12.\overline{9} = \frac{129-12}{9} = \frac{117}{9} = 13$

---

### Mini-prueba de autoevaluación

> [ad-question] **Evalúa tu conocimiento**
> **1. ¿Cuál es la característica principal de un decimal periódico puro?**
> a) El periodo tiene solo cifras pares.
> b) El periodo comienza inmediatamente después de la coma.
> c) Siempre tiene un cero como parte entera.
> 
> **2. ¿Cuál es la fracción simplificada de $0.333...?$**
> a) $\frac{3}{10}$
> b) $\frac{1}{3}$
> c) $\frac{3}{99}$
> 
> **3. ¿A qué número entero equivale exactamente $5.\overline{9}$?**
> a) $5.9$
> b) $5.99$
> c) $6$
> 
> **Respuestas:** 1-b, 2-b, 3-c.

---

> [!tip] 💡 En la próxima clase
> Analizaremos los **Decimales Periódicos Mixtos**, donde existen cifras (anteperiodo) entre la coma y el inicio del periodo.

[[Clase 13]] | [[00 - Índice del curso]]

---
---

# Guía de Estudio: Conversión de Decimales Periódicos Puros

### 1. Conceptos Fundamentales
*   **Parte Entera:** Los dígitos situados a la izquierda de la coma decimal.
*   **Periodo:** La cifra o grupo de cifras que se repiten infinitamente.
*   **Regla de Divisibilidad del 3:** Útil para simplificar. Si la suma de los dígitos de un número es múltiplo de 3, el número es divisible por 3.

### 2. El Método Algebraico (Por qué funciona)
Este método explica la lógica detrás de la regla de los "nueves". El objetivo es **eliminar la parte infinita** mediante una resta. Usaremos $1.\overline{36}$:

1.  **Igualar a $x$:** $x = 1.363636...$
2.  **Multiplicar por potencia de 10:** Como hay 2 cifras periódicas, multiplicamos por $100$.
    *   $100x = 136.363636...$ (La coma se desplaza dos lugares).
3.  **Restar ecuaciones:**
    *   $100x - x = 99x$
    *   $136.3636... - 1.3636... = 135$
    *   *Nota:* Al restar, los decimales infinitos se cancelan perfectamente ($0.3636... - 0.3636... = 0$).
4.  **Despejar:** $x = \frac{135}{99}$. Tras simplificar por 3 dos veces, obtenemos $\frac{15}{11}$.

### 3. Fórmula General
$$\text{Fracción} = \frac{\text{Número sin coma} - \text{Parte Entera}}{\text{Tantos 9 como cifras tenga el periodo}}$$

### 4. Ejercicios de Repaso Adicionales
1.  **Convertir $1.\overline{2}$:**
    $$\frac{12 - 1}{9} = \frac{11}{9}$$
2.  **Convertir $421.\overline{36}$:**
    $$\frac{42136 - 421}{99} = \frac{41715}{99} = \frac{13905}{33} = \frac{4635}{11}$$
3.  **Convertir $0.\overline{15}$:**
    $$\frac{15 - 0}{99} = \frac{15}{99} = \frac{5}{33}$$