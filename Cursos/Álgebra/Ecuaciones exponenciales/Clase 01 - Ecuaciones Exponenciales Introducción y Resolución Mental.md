# Clase 01 — Ecuaciones Exponenciales: Introducción y Resolución Mental

#algebra #exponentialequa

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 8

> [!info] 🧭 Navegación
> ⏪ [[Clase 00 - Introducción al Álgebra]] | 🏠 [[00 - Índice del curso]] | ⏩ [[Clase 02 - Propiedades Avanzadas de Exponentes]]

---

### 🌍 Relevancia y aplicaciones

> [!info] 🌍 Relevancia y aplicaciones
> Las ecuaciones exponenciales son herramientas matemáticas fundamentales para modelar fenómenos de crecimiento y decrecimiento acelerado. A diferencia de las ecuaciones lineales, aquí el cambio se multiplica rápidamente en función del tiempo o la frecuencia.
> - **💵 Aplicación USD:** Se utilizan para calcular el interés compuesto, permitiendo proyectar cuánto crecerá una inversión en dólares a lo largo de los años.
> - **🏗️ Aplicación práctica:** Son esenciales para medir el crecimiento de colonias bacterianas en biología o la velocidad de degradación de materiales radiactivos.
> - **📊 Situación cotidiana:** Explican la propagación "viral" de información, memes o virus biológicos en redes sociales y comunidades humanas.

---

### CONCEPTO CLAVE

> [!note] 📌 ¿Qué es una Ecuación Exponencial?
> Una ecuación exponencial es una igualdad donde la variable o incógnita (la variable $x$) se encuentra "atrapada" en el exponente. Resolverla consiste en encontrar qué valor debe tomar ese exponente para que la igualdad sea cierta. Por ejemplo, en $5^x = 25$, visualmente buscamos qué número "llena el hueco" del exponente para que la base $5$ se transforme en $25$.

> [!warning] ⚠️ Error común
> Es fundamental no confundir una potencia común con una ecuación exponencial:
> - $x^2 = 16$ **NO** es exponencial (la variable es la base).
> - $2^x = 16$ **SÍ** es exponencial (la variable está en el exponente).

> [!tip] 🧠 Tabla de Potencias para Resolución Mental
> Para resolver ecuaciones sin calculadora, es vital memorizar estas potencias recurrentes:
> 
> | Base $2$ | Base $3$ | Base $4$ | Base $5$ |
> | :--- | :--- | :--- | :--- |
> | $2^2 = 4$ | $3^2 = 9$ | $4^2 = 16$ | $5^2 = 25$ |
> | $2^3 = 8$ | $3^3 = 27$ | $4^3 = 64$ | $5^3 = 125$ |
> | $2^4 = 16$ | $3^4 = 81$ | $4^4 = 256$ | $5^4 = 625$ |
> | $2^5 = 32$ | $3^5 = 243$ | | |
> | $2^6 = 64$ | | | |

---

### PROCEDIMIENTO PASO A PASO

Para resolver estas ecuaciones de forma mental y eficiente, aplica la propiedad de las bases iguales:

```text
PASO 1: Observar las bases a ambos lados de la igualdad para verificar si son idénticas.
PASO 2: Si las bases son distintas, expresar el número mayor como una potencia de 
        la base menor (ejemplo: transformar 27 en 3³).
PASO 3: Igualar los exponentes. Si las bases son iguales y los resultados son iguales, 
        por lógica matemática los exponentes deben ser necesariamente los mismos.
PASO 4: Despejar la variable x en la ecuación resultante para hallar la solución final.
```

---

### EJEMPLOS DESARROLLADOS

```ad-example
title: Ejemplo 1: Resolución Básica
**Problema:** Resolver $2^x = 2^5$
**Resolución:** 
1. Observamos que las bases ya son iguales (ambas son $2$).
2. Igualamos directamente los exponentes.
3. **Resultado:** $x = 5$.
```

```ad-example
title: Ejemplo 2: Signos y Operaciones
**Problema:** Resolver $3^{x+2} = 3^6$
**Resolución:**
1. Las bases son iguales ($3$).
2. Igualamos los exponentes: $x + 2 = 6$.
3. Despejamos la variable $x$ restando $2$ en ambos lados: $x = 6 - 2$.
4. **Resultado:** $x = 4$.
```

```ad-example
title: Ejemplo 3: Transformación de Bases
**Problema:** Resolver $3^{2x-1} = 27$
**Resolución:**
1. Las bases son distintas ($3$ y $27$), pero sabemos que $27 = 3^3$.
2. Reescribimos la ecuación: $3^{2x-1} = 3^3$.
3. Igualamos exponentes: $2x - 1 = 3$.
4. Resolvemos la ecuación lineal: $2x = 4 \rightarrow x = \frac{4}{2}$.
5. **Resultado:** $x = 2$.
```

```ad-example
title: Ejemplo 4: Inversión en USD
**Problema:** Si una inversión de $1$ USD se duplica cada año, ¿en cuántos años tendremos $8$ USD?
**Resolución:**
1. El crecimiento se representa como $2^x = 8$ (donde $x$ es el tiempo en años).
2. Transformamos el $8$ a base $2$: $2^x = 2^3$.
3. Al tener bases iguales, igualamos los exponentes.
4. **Resultado:** $x = 3$. Se necesitan $3$ años para alcanzar los $8$ USD.
```

---

### EJERCICIOS PARA EL ESTUDIANTE

```ad-abstract
title: 🟢 Nivel Fácil: Igualación Directa
1. $5^x = 5^{10}$
2. $2^x = 16$
3. $7^x = 49$
4. $10^x = 1000$
```

```ad-abstract
title: 🟡 Nivel Medio: Transformación Lineal
1. $3^{x+1} = 81$
2. $2^{x-3} = 32$
3. $5^{2x} = 125$
4. $4^{x+2} = 64$
```

```ad-abstract
title: 🔴 Nivel Avanzado: Aplicación USD
1. Una cuenta de ahorros en USD triplica su valor siguiendo la fórmula $3^{x-1} = 27$. Hallar $x$.
2. El precio de una acción sube según $2^{x+2} = 128$. Hallar $x$.
3. Una deuda en dólares crece bajo la ecuación $5^{x-5} = 25$. ¿En qué valor de $x$ alcanza los $25$ USD?
4. Si un fondo de inversión rinde según $3^{2x-4} = 9$. Hallar el valor de $x$.
```

```ad-success
title: ✅ Soluciones para el Docente
**Fácil:** 1) $x=10$; 2) $x=4$; 3) $x=2$; 4) $x=3$.
**Medio:** 1) $x=3$; 2) $x=8$; 3) $x=1.5$; 4) $x=1$.
**Avanzado:** 1) $x=4$; 2) $x=5$; 3) $x=7$; 4) $x=3$.
```

---

### MINI-PRUEBA DE AUTOEVALUACIÓN

```ad-question
title: Pregunta 1
¿Cuál de las siguientes es una ecuación exponencial?
A) $x^3 = 27$
B) $4^x = 64$
C) $2x + 5 = 10$
D) $\sqrt{x} = 4$
```

```ad-question
title: Pregunta 2
Resuelve mentalmente: $2^{x+1} = 32$
```

```ad-question
title: Pregunta 3
Si el precio de una suscripción digital sube anualmente según la ecuación $2^x = 64$ dólares, ¿cuál es el valor de $x$?
```

---

> [!tip] 💡 En la próxima clase
> En la lección siguiente profundizaremos en el uso de las **Propiedades de los Exponentes** para resolver casos más complejos donde las bases no son tan obvias o requieren simplificación previa mediante multiplicación y división de potencias.

> [!info] 🧭 Navegación
> ⏪ [[Clase 00 - Introducción al Álgebra]] | 🏠 [[00 - Índice del curso]] | ⏩ [[Clase 02 - Propiedades Avanzadas de Exponentes]]