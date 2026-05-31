# 📖 Guía de estudio — Clase 02: Sumatoria y Notación Sigma

> [!info] 📌 Conceptos clave
> 1. **Definición:** La sumatoria es una herramienta matemática que nos permite escribir de forma abreviada y compacta la suma de muchos términos de una sucesión.
> 2. **Variables contadoras:** Se utilizan letras como $i$, $j$, $k$ o $n$. Estas funcionan como "contadores" que van cambiando su valor de uno en uno, reemplazándose en la fórmula principal.
> 3. **Límites de la sumatoria:** El número debajo del símbolo $\sum$ es el **límite inferior** (dónde empezamos) y el número de arriba es el **límite superior** (dónde terminamos). 
> 4. **El proceso de resolución:** Para no equivocarnos, primero reemplazamos la variable, luego resolvemos las operaciones internas (potencias y multiplicaciones) y, finalmente, sumamos todos los resultados obtenidos.

## Fórmulas y definiciones importantes

| Término | Definición / Función |
| :--- | :--- |
| **Notación Sigma ($\sum$)** | Símbolo griego que representa la instrucción de sumar una serie de términos. |
| **Límite Inferior** | Define el valor inicial de la variable (ej. $i=1$). **¡Cuidado!** No siempre empieza en 1; puede iniciar en cualquier entero. |
| **Límite Superior** | Indica el valor final donde se detiene la suma. Es el tope del reemplazo. |
| **Orden de Operación** | Para cada término, el orden estricto es: **1.** Potencias, **2.** Multiplicaciones/Divisiones, **3.** Sumas/Restas. |

## Ejemplos resueltos paso a paso

Como recomienda el **Profe Alex**, para evitar que el ejercicio se convierta en un "monstruo" lleno de números, realizaremos los cálculos de cada término "aparte".

```ad-example
title: Ejemplo A — Suma de potencias cuadráticas
**Problema:** Calcular el valor de $\sum_{i=1}^{4} i^2$.

**Paso 1: Cálculos independientes (Aparte)**
- Para $i=1$: $(1)^2 = 1$
- Para $i=2$: $(2)^2 = 4$
- Para $i=3$: $(3)^2 = 9$
- Para $i=4$: $(4)^2 = 16$

**Paso 2: Suma final**
$1 + 4 + 9 + 16 = 30$

**✅ Resultado:** $30$
```

```ad-example
title: Ejemplo B — Aplicación de ahorro diario en $USD
**Problema:** Un estudiante ahorra dinero durante 3 días según la fórmula $\sum_{k=1}^{3} (3k + 2)$. ¿Cuál es el ahorro total?

**Paso 1: Cálculo por día (Reemplazo de $k$)**
- **Día 1 ($k=1$):** $3(1) + 2 = 3 + 2 = 5$ USD
- **Día 2 ($k=2$):** $3(2) + 2 = 6 + 2 = 8$ USD
- **Día 3 ($k=3$):** $3(3) + 2 = 9 + 2 = 11$ USD

**Paso 2: Suma de resultados**
$5 + 8 + 11 = 24$

**✅ Ahorro Total:** $24$ USD
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel: Fácil
1. Calcule el valor de $\sum_{i=1}^{4} 3i$. (Sugerencia: Reemplace $i$ por 1, 2, 3 y 4).
2. Determine el resultado de $\sum_{k=1}^{5} (k + 2)$.
3. Resuelva la sumatoria $\sum_{j=1}^{3} (3j - 1)$.
```

```ad-abstract
title: 🟡 Nivel: Medio
1. Calcule la suma de cuadrados para $\sum_{n=1}^{3} n^2$.
2. **¡Cuidado con el inicio!** Encuentre el valor de $\sum_{i=2}^{4} (3i^2 - 5)$. 
3. Resuelva la sumatoria con fracciones: $\sum_{k=1}^{3} \frac{k+1}{2k}$.
```

```ad-abstract
title: 🔴 Nivel: Avanzado — Aplicación de costos en $USD
**Problema:** El costo de producción de 4 artículos sigue la fórmula $\sum_{i=1}^{4} \frac{i^2 + 6}{i}$ en dólares.

**Pista de resolución:** Realice los cálculos de cada término por separado. Simplifique las fracciones que den resultados enteros antes de sumar.
- **Término 1 ($i=1$):** $\frac{1^2+6}{1} = 7$
- **Término 2 ($i=2$):** $\frac{2^2+6}{2} = \frac{10}{2} = 5$
- **Término 3 ($i=3$):** $\frac{3^2+6}{3} = \frac{15}{3} = 5$
- **Término 4 ($i=4$):** $\frac{4^2+6}{4} = \frac{22}{4} = 5.5$ (o $\frac{11}{2}$)

*Para la suma final, puede convertir todo a decimales o utilizar el método del Mínimo Común Múltiplo (MCM) para trabajar con fracciones homogéneas.*
```

> [!tip] 💡 Consejo de estudio del Profe Alex
> ¡No intentes hacerlo todo en una sola línea! Haz como yo: realiza las operaciones de cada término **en un espacio aparte** de tu hoja. Si te quedan fracciones como en el ejercicio avanzado, busca el **MCM** de los denominadores para convertirlas en fracciones homogéneas; esto hace que la suma final sea mucho más sencilla y evita errores comunes.