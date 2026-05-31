# Clase 04 — Suma de naturales, cuadrados, cubos y constante

#algebra #sumatorias

> [!info] 🧭 Navegación
> [Anterior: Clase 03](Clase03) | [Índice General](Indice) | [Siguiente: Clase 05](Clase05)

---

> [!info] 🌍 Relevancia y aplicaciones
> Las sumatorias notables funcionan como potentes "atajos" matemáticos que nos permiten calcular acumulados de miles de datos de forma instantánea sin tener que sumar uno por uno. Gracias a estas estructuras lógicas, podemos resolver problemas complejos con una sola operación.
> - **Finanzas ($USD):** Cálculo de ahorros acumulados, intereses o proyecciones de inversión en el tiempo.
> - **Ingeniería y Construcción:** Determinación de la cantidad de materiales necesarios para estructuras piramidales o apilamientos de vigas y bloques.
> - **Análisis de Datos:** Procesamiento rápido de tendencias masivas en registros de consumo diario o estadísticas de crecimiento.

---

> [!note] 📌 ¿Qué son estas sumatorias?
> En matemáticas, existen sucesiones de números que aparecen con mucha frecuencia. Para no perder tiempo sumando término a término (lo cual sería eterno si tuviéramos que sumar hasta el 1,000), utilizamos fórmulas que nos dan el resultado directo. Estas fórmulas son herramientas esenciales para manejar números naturales, sus potencias o valores que no cambian.
> 
> ### Fórmulas Principales
> 1. **Suma de Naturales ($i$):** $\frac{n(n+1)}{2}$. Esta es conocida mundialmente como la **Fórmula de Gauss**, en honor al genio que la descubrió de niño.
> 2. **Suma de Cuadrados ($i^2$):** $\frac{n(n+1)(2n+1)}{6}$
> 3. **Suma de Cubos ($i^3$):** $\left[\frac{n(n+1)}{2}\right]^2$. ¡Fíjate bien! Es el resultado de la suma de naturales elevado al cuadrado.
> 4. **Suma de una Constante ($c$):** $n \times c$. 
> 
> > [!important] Nota sobre las variables
> > Recuerda que la letra del índice ($i, j, k$) no cambia el resultado. Además, si dentro de la sumatoria ves una letra que **no** es la del índice (por ejemplo, $\sum_{i=1}^{10} x$), esa letra se trata como una **constante**, exactamente igual que si fuera un número.

> [!warning] ⚠️ El "Atrapamoscas" (Error común)
> Estas fórmulas **solo** funcionan si la sumatoria comienza estrictamente en **1**. Si ves algo como $\sum_{i=5}^{20} i^2$, ¡cuidado! Es una "trampa"; no puedes aplicar la fórmula directamente porque no empieza desde el primer término.

> [!tip] 💡 Truco para recordarlo
> - **Para los cuadrados (Regla del Profe Alex):** No te memorices la fórmula difícil. Solo multiplica el límite superior ($n$), por el número que le sigue ($n+1$), y luego por la **suma de esos dos** ($2n+1$). Al final, divide todo entre 6.
> - **Para los cubos:** Es simplemente "el cuadrado de la suma de los naturales". Si te sabes la de Gauss, ya te sabes la de los cubos.

---

### 🛠 Procedimiento Paso a Paso

```text
PASO 1: Identificar el límite superior (n). Es el número que indica hasta dónde llega la suma.
PASO 2: Verificar que el límite inferior sea 1. Si ves i=2 o i=5, detente (necesitas otras propiedades).
PASO 3: Seleccionar la fórmula según el exponente de la variable (i, i² o i³).
PASO 4: Sustituir 'n' y SIMPLIFICAR SIEMPRE antes de multiplicar. 
        • Si divides entre 6, busca un número con mitad y otro con tercera. 
        • Esto evita trabajar con números gigantes y errores de cálculo.
```

---

### 📝 Ejemplos Prácticos

```ad-example
title: **Ejemplo 1: Suma de Naturales (Fórmula de Gauss)**
Calcula la suma de los primeros 50 números naturales: $\sum_{i=1}^{50} i$
1. **$n = 50$**
2. **Aplicamos:** $\frac{50 \times 51}{2}$
3. **Simplificamos:** Sacamos mitad al 50 ($25$) y al 2 ($1$).
4. **Operación:** $25 \times 51$
**Resultado:** $1,275$
```

```ad-example
title: **Ejemplo 2: Suma de Cuadrados (Regla de la Suma)**
Halla el valor de: $\sum_{i=1}^{20} i^2$
1. **$n = 20$**
2. **Planteamos:** $\frac{20 \times 21 \times (20+21)}{6} = \frac{20 \times 21 \times 41}{6}$
3. **Simplificación visual:** 
   - El 6 se convierte en 1.
   - Sacamos **mitad**: El 6 baja a 3 y el 20 sube a 10.
   - Sacamos **tercera**: El 3 baja a 1 y el 21 sube a 7.
4. **Operación final:** $10 \times 7 \times 41$
**Resultado:** $2,870$
```

```ad-example
title: **Ejemplo 3: Suma de Cubos**
Encuentra la suma de los primeros 10 cubos: $\sum_{k=1}^{10} k^3$
1. **$n = 10$**
2. **Suma natural:** $\frac{10 \times 11}{2} = 5 \times 11 = 55$
3. **Elevamos al cuadrado:** $55^2 = 3,025$
**Resultado:** $3,025$
```

```ad-example
title: **Ejemplo 4: Aplicación en $USD (Constante)**
Ahorras una cantidad constante de **$3.2 USD** diarios por **50 días**: $\sum_{i=1}^{50} 3.2$
1. **$n = 50$, $c = 3.2$**
2. **Aplicamos:** $50 \times 3.2 = 160$
**Resultado:** $160$ USD
```

---

### ✏️ Ejercicios para el Estudiante

```ad-abstract
title: 🟢 Nivel Fácil
1. Calcula la suma de los números naturales del 1 al 100 utilizando la fórmula de Gauss.
2. Halla el resultado de la sumatoria de la constante 15 cuando $n=40$.
```

```ad-abstract
title: 🟡 Nivel Medio
1. Calcula la suma de los cuadrados de los primeros 15 números ($n=15$). *Recuerda simplificar el 6 antes de multiplicar.*
2. Halla la suma de los cubos de los primeros 5 números ($n=5$).
```

```ad-abstract
title: 🔴 Nivel Avanzado
1. **El reto del ahorro:** Un estudiante decide ahorrar dinero siguiendo esta regla: el día 1 ahorra $1^2$, el día 2 ahorra $2^2$, y así sucesivamente hasta el día 10. ¿Cuál es el total ahorrado? *(Pista: Debes calcular $\sum_{i=1}^{10} i^2$)*.
2. Calcula la sumatoria de la constante $c=12.5$ para un periodo de $n=80$.
```

```ad-success
title: ✅ Respuestas para el Docente
- **Fácil:** 1) 5,050 | 2) 600
- **Medio:** 1) 1,240 (simplificando: $5 \times 8 \times 31$) | 2) 225
- **Avanzado:** 1) 385 USD (10x11x21 / 6) | 2) 1,000
```

---

### ❓ Autoevaluación

```ad-question
title: Pregunta 1: Conceptual
¿Qué sucede si intentas aplicar la fórmula de $n \times c$ en una sumatoria que empieza en $i=5$?
***
**Respuesta:** El resultado será incorrecto. 
**Explicación:** Las fórmulas de sumas notables están diseñadas bajo la condición de que el conteo inicie en 1. Si empieza en 5, estarías sumando menos veces de las que indica el límite superior $n$.
```

```ad-question
title: Pregunta 2: Procedimental
Calcula mentalmente la suma de los cubos para $n=3$.
***
**Respuesta:** 36.
**Explicación:** Suma natural: $(3 \times 4)/2 = 6$. Elevado al cuadrado: $6^2 = 36$. Comprobación: $1^3(1) + 2^3(8) + 3^3(27) = 36$.
```

```ad-question
title: Pregunta 3: Aplicación $USD
Si un banco cobra una comisión fija de $13 USD por cada trámite y realizas 30 trámites, ¿cuál es el costo total?
***
**Respuesta:** 390 USD.
**Explicación:** Aplicamos la suma de una constante: $n \times c = 30 \times 13 = 390$.
```

---

> [!tip] 💡 En la próxima clase
> ¿Qué pasa cuando la suma no empieza en 1? En la Clase 05 aprenderemos las propiedades para "ajustar" los límites y poder usar estas mismas fórmulas en cualquier situación.

> [!info] 🧭 Navegación
> [Anterior: Clase 03](Clase03) | [Índice General](Indice) | [Siguiente: Clase 05](Clase05)