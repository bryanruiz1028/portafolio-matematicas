# 📖 Guía de estudio — Clase 02: Varianza y Desviación Estándar

> [!info] 📌 Conceptos clave
> * **Varianza:** Es el promedio de los cuadrados de las diferencias entre cada dato y su media aritmética. Se mide en unidades al cuadrado.
> * **Desviación Estándar:** Es la raíz cuadrada de la varianza. Su gran ventaja es que devuelve el resultado a la **unidad de medida original** (años, kg, USD).
> * **Población vs. Muestra:** Si analizas a todos los individuos usamos $N$ (Población). Si es solo una parte, usamos $n-1$ (Muestra) para mayor precisión estadística.
> * **Interpretación:** Ambas medidas indican qué tan "dispersos" o alejados están los datos respecto al promedio central.

### Tabla de fórmulas y definiciones

| Término | Definición | Fórmula Matemática |
| :--- | :--- | :--- |
| **Varianza Poblacional ($\sigma^2$)** | Se usa cuando tenemos los datos de todo el grupo estudiado. | $$\sigma^2 = \frac{\sum (x - \bar{x})^2}{N}$$ |
| **Varianza Muestral ($s^2$)** | Se usa cuando los datos son solo una parte representativa (muestra). | $$s^2 = \frac{\sum (x - \bar{x})^2}{n - 1}$$ |
| **Desviación Estándar** | Es la medida de dispersión en unidades originales. | $$\sigma = \sqrt{\sigma^2} \quad \text{o} \quad s = \sqrt{s^2}$$ |
| **Promedio ($\bar{x}$)** | Es el punto de equilibrio; la suma de datos dividida por el total. | $$\bar{x} = \frac{\sum x}{n}$$ |

---

### Sección de ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Edades de niños (Población)
**Contexto:** Se analizan las edades de los únicos 5 niños de un pequeño taller: 5, 6, 6, 7 y 8 años.

**Paso 1: Cálculo del promedio ($\bar{x}$)**
$\bar{x} = \frac{5 + 6 + 6 + 7 + 8}{5} = \frac{32}{5} = 6,4$ años.

**Paso 2: Diferencias al cuadrado**
* $(5 - 6,4)^2 = (-1,4)^2 = 1,96$
* $(6 - 6,4)^2 = (-0,4)^2 = 0,16$
* $(6 - 6,4)^2 = (-0,4)^2 = 0,16$
* $(7 - 6,4)^2 = (0,6)^2 = 0,36$
* $(8 - 6,4)^2 = (1,6)^2 = 2,56$

**Paso 3: Suma y división por $N$ (Población)**
$\sigma^2 = \frac{1,96 + 0,16 + 0,16 + 0,36 + 2,56}{5} = \frac{5,2}{5} = 1,04$

**Resultado:** La varianza es **1,04 años²**.
```

```ad-example
title: Ejemplo B — Gastos diarios (Muestra)
**Contexto:** Se toma una muestra de los gastos de 3 días de una persona: $52, $55 y $58 USD.

**Paso 1: Cálculo del promedio ($\bar{x}$)**
$\bar{x} = \frac{52 + 55 + 58}{3} = \frac{165}{3} = 55$ USD.

**Paso 2: Diferencias al cuadrado**
* $(52 - 55)^2 = (-3)^2 = 9$
* $(55 - 55)^2 = (0)^2 = 0$
* $(58 - 55)^2 = (3)^2 = 9$

**Paso 3: Varianza Muestral ($s^2$)**
Dividimos la suma ($18$) entre $n-1$ ($3-1=2$) porque los datos se consideran una **muestra**:
$s^2 = \frac{18}{2} = 9$ USD².

**Paso 4: Desviación Estándar ($s$)**
$s = \sqrt{9} = 3$ USD.

**Resultado:** La varianza es **9 USD²** y la desviación estándar es **3 USD**.
```

---

### Sección de ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
Calcula el promedio ($\bar{x}$) y la varianza ($\sigma^2$) tratando estos conjuntos como **población**:
1. Datos: 2, 4, 6
2. Datos: 10, 10, 10
3. Datos: 1, 3, 5
```

```ad-abstract
title: 🟡 Medio
Calcula la varianza poblacional ($\sigma^2$). Aquí el promedio es decimal, ¡usa los paréntesis con cuidado!
1. Datos: 4, 5, 8, 9  *(Pista: $\bar{x} = 6,5$)*
2. Datos: 12, 15, 16, 18, 20 *(Pista: $\bar{x} = 16,2$)*
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
Se registran los ahorros semanales de una **muestra** de 4 amigos: $20, $25, $30 y $35 USD.
1. Calcula la varianza muestral ($s^2$).
2. Calcula la desviación estándar ($s$).
3. **Análisis:** Explica qué significa el resultado de la desviación estándar en el contexto del dinero.
```

---

### ✅ Clave de Respuestas (Solucionario)

**Nivel Fácil:**
1. $\bar{x}=4, \sigma^2=2,67$ (aproximado).
2. $\bar{x}=10, \sigma^2=0$. *Nota pedagógica: Cuando los datos son iguales, no hay dispersión.*
3. $\bar{x}=3, \sigma^2=2,67$ (aproximado).

**Nivel Medio:**
1. $\bar{x}=6,5, \sigma^2=4,25$.
2. $\bar{x}=16,2, \sigma^2=7,76$.

**Nivel Avanzado:**
1. **Promedio:** $27,5$ USD.
2. **Varianza ($s^2$):** $41,67$ USD².
3. **Desviación Estándar ($s$):** $\approx 6,45$ USD.
4. **Análisis de ejemplo:** "La desviación estándar de $6,45$ USD indica que, en promedio, los ahorros de los amigos se alejan o varían aproximadamente $6,45$ dólares respecto al promedio de $27,5$ USD."

---

> [!tip] 💡 Consejo de estudio
> 1. **Paréntesis obligatorios:** En la calculadora, escribe siempre `(dato - promedio)^2`. Si no usas los paréntesis antes de elevar al cuadrado, la máquina solo elevará el segundo número y tu resultado será erróneo.
> 2. **Limpieza de memoria:** Acostúmbrate a borrar la memoria de tu calculadora (`Shift + CLR` en muchos modelos) entre ejercicios para evitar que se arrastren datos anteriores.
> 3. **El paso final:** La varianza es un paso intermedio. ¡No olvides aplicar la **raíz cuadrada** para obtener la desviación estándar!