# Clase 01 — Introducción e Identidades Trigonométricas (Recíprocas y Pitagóricas)

#algebra #trigonometricid

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 5

> [!info] 🧭 Navegación
> - ⬅️ **Anterior**: [[00 - Índice del curso]]
> - ➡️ **Siguiente**: [[Clase 02 — Demostración de Identidades]]

---

## 1. ¿Por qué es importante esta clase?

¡Bienvenido al inicio de este camino! Dominar las identidades trigonométricas es como adquirir un **"superpoder" matemático**: te permitirá transformar expresiones que parecen imposibles en fórmulas simples y elegantes. Estas igualdades son el lenguaje secreto que conecta todas las funciones del triángulo.

> [!info] 🌍 Relevancia y aplicaciones
> Las identidades nos permiten simplificar cálculos técnicos y encontrar valores para funciones que no suelen estar en las calculadoras (como la secante o la cosecante), asegurando precisión en ingeniería y arquitectura.
> 
> - **💵 [Aplicación con USD]:** Si el costo de un cable de acero depende de su longitud, y esta se define por la inclinación de una antena, las identidades permiten presupuestar costos exactos usando solo ángulos.
> - **🏗️ [Aplicación práctica]:** En la construcción, el uso del **círculo unitario** permite diseñar estructuras circulares y soportes donde la estabilidad depende de la relación perfecta entre los catetos y la hipotenusa.
> - **📊 [Situación cotidiana]:** Permiten calcular distancias inaccesibles (como la altura de una montaña o un edificio) simplemente midiendo sombras y ángulos de elevación.

---

## 2. Conceptos clave

> [!note] **¿Qué es una Identidad Trigonométrica?**
> Es una igualdad entre dos expresiones trigonométricas que es válida para **todos** los valores del ángulo (variable). A diferencia de una **ecuación común** (que solo es cierta para algunos valores específicos), la identidad es una verdad universal en el universo del ángulo.

> [!warning] **Errores comunes a evitar**
> 1. **Confundir identidad con ecuación:** En $x + 3 = 5$, solo $x=2$ funciona. En una identidad como $\text{sen}^2(\theta) + \cos^2(\theta) = 1$, ¡cualquier ángulo funciona!
> 2. **Olvido de exponentes:** En las identidades pitagóricas, las funciones **deben** estar elevadas al cuadrado. No es lo mismo $\text{sen}(\theta) + \cos(\theta)$ que $\text{sen}^2(\theta) + \cos^2(\theta)$.

### A. Identidades Recíprocas (Inversas)
Para aprenderlas, utiliza esta **regla mnemotécnica**. Escribe las funciones en orden y conecta los extremos (el primero con el último, el segundo con el penúltimo...):

1. $\text{sen}(\alpha)$ $\longleftrightarrow$ $\csc(\alpha)$ $\implies \text{sen}(\alpha) = \frac{1}{\csc(\alpha)}$
2. $\cos(\alpha)$ $\longleftrightarrow$ $\sec(\alpha)$ $\implies \cos(\alpha) = \frac{1}{\sec(\alpha)}$
3. $\tan(\alpha)$ $\longleftrightarrow$ $\cot(\alpha)$ $\implies \tan(\alpha) = \frac{1}{\cot(\alpha)}$

### B. Identidades de Cociente
Antes de operar, recuerda que la tangente y cotangente nacen de la relación entre el seno y el coseno:
- $\tan(\alpha) = \frac{\text{sen}(\alpha)}{\cos(\alpha)}$
- $\cot(\alpha) = \frac{\cos(\alpha)}{\text{sen}(\alpha)}$

### C. Identidades Pitagóricas
Estas identidades nacen del **Círculo Unitario** (un círculo con radio $r = 1$). Al aplicar el Teorema de Pitágoras ($a^2 + b^2 = c^2$) en este círculo, donde los catetos son el seno y el coseno, obtenemos nuestra identidad fundamental:

$$\text{sen}^2(\theta) + \cos^2(\theta) = 1$$

De esta "fórmula madre" podemos deducir otras dividiendo toda la igualdad:
- Si dividimos por $\text{sen}^2(\theta)$, obtenemos: $1 + \cot^2(\theta) = \csc^2(\theta)$.
- Si dividimos por $\cos^2(\theta)$, obtenemos: $\tan^2(\theta) + 1 = \sec^2(\theta)$.

---

## 3. Procedimiento paso a paso: Verificación

Si quieres comprobar si una expresión es una identidad usando tu tecnología, sigue estos pasos:

> [!warning] **Aviso Técnico Crucial**
> Antes de empezar, asegúrate de que tu calculadora esté configurada en modo **Grados (D o DEG)**. Si está en Radianes (R), los resultados de los ángulos en grados no coincidirán.

> [!abstract] **Pasos para verificar con calculadora**
> 1. **Elegir un ángulo:** Selecciona un valor cualquiera (ej. $30^\circ$ o $45^\circ$).
> 2. **Evaluar el lado izquierdo:** Calcula el valor numérico de la primera expresión.
> 3. **Evaluar el lado derecho:** Calcula el valor numérico de la segunda expresión.
> 4. **Comparar:** Si ambos resultados son idénticos, has verificado la identidad para ese valor.

---

## 4. Ejemplos de Aplicación

> [!example] **Ejemplo 1: Identidad Recíproca con Ángulo Fijo**
> Demostrar que $\tan(\alpha) = \frac{1}{\cot(\alpha)}$ con $\alpha = 30^\circ$.
> 1. Usando identidad de cociente: $\cot(30^\circ) = \frac{\cos(30^\circ)}{\text{sen}(30^\circ)} \approx 1.732$.
> 2. En la calculadora: $\tan(30^\circ) \approx 0.577$.
> 3. Verificamos la división: $\frac{1}{1.732} = 0.577$.
> **Conclusión:** $0.577 = 0.577$. ¡Se cumple!

> [!example] **Ejemplo 2: Despeje Pitagórico**
> Si sabemos que $\cos(\theta) = 0.8$, ¿cuánto vale $\text{sen}^2(\theta)$?
> 1. Partimos de: $1 - \cos^2(\theta) = \text{sen}^2(\theta)$.
> 2. Elevamos el coseno: $(0.8)^2 = 0.64$.
> 3. Restamos de la unidad: $1 - 0.64 = 0.36$.
> **Resultado:** $\text{sen}^2(\theta) = 0.36$.

> [!example] **Ejemplo 3: Deducción de Identidades Derivadas**
> Demostrar cómo obtener la identidad de la cosecante dividiendo por el seno:
> 1. Base: $\text{sen}^2(\theta) + \cos^2(\theta) = 1$.
> 2. Dividimos cada término entre $\text{sen}^2(\theta)$:
>    $$\frac{\text{sen}^2(\theta)}{\text{sen}^2(\theta)} + \frac{\cos^2(\theta)}{\text{sen}^2(\theta)} = \frac{1}{\text{sen}^2(\theta)}$$
> 3. Aplicamos identidades de cociente y recíprocas:
>    $$1 + \cot^2(\theta) = \csc^2(\theta)$$

> [!example] **Ejemplo 4: Presupuesto de Obra (USD)**
> El costo de un tensor de acero es de $\$12$ por metro. Necesitamos un tensor cuya longitud sea igual a $\csc(30^\circ)$. ¿Cuál es el costo?
> 1. Como la calculadora no tiene tecla $\csc$, usamos la identidad: $\csc(30^\circ) = \frac{1}{\text{sen}(30^\circ)}$.
> 2. $\text{sen}(30^\circ) = 0.5$.
> 3. Longitud: $\frac{1}{0.5} = 2$ metros.
> 4. **Costo final:** $2 \text{ m} \times \$12 = \$24 \text{ USD}$.

---

## 5. Ejercicios para el estudiante

> [!abstract] **🟢 Nivel Fácil: Identificación**
> 1. ¿Cuál es la función recíproca del $\cos(x)$?
> 2. ¿A qué función equivale la expresión $1 / \text{sen}(\theta)$?
> 3. Si $\tan(A) = 0.5$, ¿cuál es el valor de $\cot(A)$?
> 4. Expresa la $\sec(x)$ en términos de su recíproca.

> [!abstract] **🟡 Nivel Medio: Pitagóricas**
> Completa las siguientes igualdades fundamentales:
> 1. $1 - \text{sen}^2(x) = \dots$
> 2. $\sec^2(\theta) - 1 = \dots$
> 3. $\cos^2(45^\circ) + \text{sen}^2(45^\circ) = \dots$
> 4. $1 + \cot^2(y) = \dots$

> [!abstract] **🔴 Nivel Avanzado: Aplicación USD**
> 1. Una viga de soporte cuesta $\$100 \times \sec(60^\circ)$. Calcula el costo total usando la recíproca del coseno.
> 2. Un presupuesto de pintura es de $\$50 \times \csc^2(45^\circ)$. Halla el valor total.
> 3. Si el costo de un conector es $\$10 \times (\tan^2(30^\circ) + 1)$, ¿cuál es su precio final? (Usa identidades pitagóricas para simplificar).
> 4. Un panel solar rinde una ganancia de $\$200 / \csc(90^\circ)$. ¿Cuál es la ganancia real?

> [!success] **Solucionario para el Docente**
> - **Fácil:** 1. $\sec(x)$ | 2. $\csc(\theta)$ | 3. $2$ | 4. $1/\cos(x)$.
> - **Medio:** 1. $\cos^2(x)$ | 2. $\tan^2(\theta)$ | 3. $1$ | 4. $\csc^2(y)$.
> - **Avanzado:** 
>   1. $\$200$ (porque $\cos 60^\circ=0.5 \implies \sec 60^\circ=2$).
>   2. $\$100$ (porque $\text{sen} 45^\circ \approx 0.707 \implies \csc^2 45^\circ=2$).
>   3. $\$13.33$ ($\tan^2+1 = \sec^2$; $\sec^2 30^\circ = 1.333$).
>   4. $\$200$ (porque $\csc 90^\circ=1$).

---

## 6. Mini-prueba de autoevaluación

> [!question] **Pregunta 1**
> Explica con tus palabras: ¿Por qué una identidad trigonométrica tiene "infinitas soluciones" a diferencia de una ecuación?

> [!question] **Pregunta 2**
> Selecciona la opción que **NO** es una identidad pitagórica válida:
> a) $\text{sen}^2(x) + \cos^2(x) = 1$
> b) $\tan^2(x) + 1 = \sec^2(x)$
> c) $\text{sen}(x) + \cos(x) = 1$

> [!question] **Pregunta 3 (USD)**
> Para una rampa, se requiere un perfil metálico cuya longitud es $5 \times \sec(0^\circ)$ metros. Si el precio por metro es $\$20$ USD, ¿cuál es el presupuesto total?

---

## 7. Notas para el próximo tema

> [!tip] **Hacia la Clase 02**
> ¡Felicidades por completar la base! En la siguiente lección usaremos estas piezas de rompecabezas para realizar **Demostraciones de Identidades**. Aprenderás a transformar expresiones complejas en otras más simples usando pura lógica algebraica.

---
> [!info] 🧭 Navegación
> - ⬅️ **Anterior**: [[00 - Índice del curso]]
> - ➡️ **Siguiente**: [[Clase 02 — Demostración de Identidades]]