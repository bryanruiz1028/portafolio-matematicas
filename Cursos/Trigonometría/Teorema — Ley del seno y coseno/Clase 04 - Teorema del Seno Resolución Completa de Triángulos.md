# Clase 04 — Teorema del Seno: Resolución Completa de Triángulos

tags: #algebra #sinetheoremsolv
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 4 de 9

> [!info] 🧭 Navegación
> [[Clase 03|⬅ Clase 03]] | [[00 - Índice del curso|Índice]] | **Clase 04** | | [[Clase 05|Clase 05 ➡]]

## 1. ¿Por qué es importante esta clase?
> [!info] 🌍 Relevancia y aplicaciones
> "Resolver" un triángulo es un proceso integral que consiste en hallar la medida de sus tres lados y sus tres ángulos. El Teorema del Seno es la llave maestra para este rompecabezas cuando disponemos de una "parejita" (un lado y su ángulo opuesto). Su aplicación trasciende el aula, siendo vital en la navegación para establecer rumbos y en la ingeniería para el cálculo de estructuras complejas.

- 💵 **Finanzas:** Permite determinar con precisión el perímetro de terrenos irregulares para calcular presupuestos de cercado basados en precios por metro lineal en $USD.
- 🏗️ **Construcción:** Fundamental para medir distancias inaccesibles entre dos puntos en un plano urbano mediante triangulación.
- 📊 **Situación cotidiana:** Ajuste técnico de antenas de telecomunicaciones para garantizar que el lóbulo de radiación cubra áreas con pendientes geográficas específicas.

## 2. Concepto clave
> [!note] 📌 ¿Qué es resolver el triángulo con el Teorema del Seno?
> Imagina que el triángulo es un conjunto de datos que deben encajar. Resolverlo significa encontrar todos los valores faltantes. El Teorema del Seno establece que la relación entre un lado y el seno de su ángulo opuesto es constante para todo el triángulo:
> $$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$$

> [!warning] ⚠️ Error común
> ❌ **Incorrecto:** Intentar resolver el triángulo si no tienes una "pareja" completa (un lado y su ángulo de enfrente) o si tu calculadora está en modo **Radianes (R)**.
> ✅ **Correcto:** Antes de empezar, identifica tu "pareja de oro" y verifica que la calculadora muestre **"D"** o **"DEG"** (Degrees/Grados).

> [!tip] 💡 Truco para recordarlo
> "Lado sobre su ángulo de enfrente, siempre es equivalente".

## 3. Procedimiento paso a paso
Para resolver el triángulo de forma metódica (estilo "Profe Alex"), sigue este orden:

1.  **Identificación:** Etiqueta los ángulos con mayúsculas ($A, B, C$) y sus lados opuestos con minúsculas ($a, b, c$).
2.  **Suma de Ángulos:** Si conoces dos ángulos, halla el tercero restando su suma de $180^\circ$.
3.  **Selección de la Pareja:** Ubica la "parejita" conocida para establecer la constante de proporcionalidad.
4.  **Despeje y Cálculo:** 
    *   Si buscas un **lado**, pon los lados arriba: $\frac{a}{\sin A} = \dots$
    *   Si buscas un **ángulo**, pon los senos arriba: $\frac{\sin A}{a} = \dots$ y usa la función inversa ($\arcsin$ o $\sin^{-1}$).

## 4. Ejemplos de Resolución

```ad-example
title: Ejemplo 1 — Caso básico (Lado-Ángulo-Ángulo)
**Datos:** $B=30^\circ, C=108^\circ$ y lado $c=39\text{ cm}$.
- **Paso 1:** Hallar el ángulo $A \implies 180^\circ - 108^\circ - 30^\circ = 42^\circ$.
- **Paso 2:** Hallar lado '$a$' usando la pareja '$c$':
$$\frac{a}{\sin 42^\circ} = \frac{39}{\sin 108^\circ} \implies a = \frac{39 \cdot \sin 42^\circ}{\sin 108^\circ}$$
✅ **Resultado:** $a \approx 27.439\text{ cm}$.
```

```ad-example
title: Ejemplo 2 — Caso con ajuste de tercer ángulo
**Datos:** $A=80^\circ, C=70^\circ$ y lado $b=21\text{ cm}$.
Aquí no hay pareja inicial (tenemos lado $b$ pero no ángulo $B$). 
- **Paso 1:** Hallar $B$ primero: $B = 180^\circ - (80^\circ + 70^\circ) = 30^\circ$.
- **Paso 2:** Con la pareja '$b$' ($B=30^\circ, b=21$), calculamos los lados '$a$' y '$c$'.
✅ **Resultado:** $a \approx 41.362\text{ cm}$, $c \approx 39.467\text{ cm}$.
⚠️ **Nota:** No olvides cerrar los paréntesis en la calculadora: `sin(80)`.
```

```ad-example
title: Ejemplo 3 — Caso avanzado (Hallar Ángulo Agudo)
**Datos:** $A=35^\circ, a=11\text{ m}, c=16\text{ m}$.
- **Paso 1:** Hallar ángulo $C$ usando arcoseno:
$$\frac{\sin C}{16} = \frac{\sin 35^\circ}{11} \implies C = \arcsin\left(\frac{16 \cdot \sin 35^\circ}{11}\right)$$
- **Paso 2:** Con $C \approx 56.542^\circ$, hallamos $B = 180^\circ - 35^\circ - 56.542^\circ = 88.458^\circ$.
- **Paso 3:** Hallar lado '$b$'.
✅ **Resultado:** $C \approx 56.542^\circ, B \approx 88.458^\circ, b \approx 19.17\text{ m}$.
```

```ad-example
title: Ejemplo 4 — Aplicación real (Caso Ángulo Obtuso)
**Situación:** Terreno triangular con $B=31^\circ$, $b=20\text{ m}$, $c=38\text{ m}$. Cerca cuesta $\$15\text{ USD}/m$.
- **Anomalía:** La calculadora da $C \approx 78.118^\circ$, pero el plano muestra un ángulo obtuso.
- **Ajuste Técnico:** Las calculadoras siempre devuelven el ángulo agudo ($0-90^\circ$). Matemáticamente, $\sin(x) = \sin(180-x)$. Debemos restar de $180^\circ$ para hallar el suplemento obtuso: $180^\circ - 78.118^\circ = 101.882^\circ$.
- **Cálculo Final:** $A = 180^\circ - 31^\circ - 101.882^\circ = 47.118^\circ$. El lado $a \approx 28.45\text{ m}$.
✅ **Resultado:** Perímetro $= 20 + 38 + 28.45 = 86.45\text{ m}$. 
**Costo total:** $86.45 \times 15 = \$1,296.75\text{ USD}$.
```

## 5. Ejercicios para el estudiante

```ad-abstract
title: 🟢 Fácil — Hallar el lado faltante
1. $B=62^\circ, b=10\text{ m}, C=46^\circ$. Hallar $c$.
2. $A=45^\circ, a=15\text{ cm}, B=30^\circ$. Hallar $b$.
3. $C=100^\circ, c=25\text{ m}, A=20^\circ$. Hallar $a$.
4. $B=55^\circ, b=12\text{ cm}, C=70^\circ$. Hallar $c$.
```

```ad-abstract
title: 🟡 Medio — Resolución completa
Halle el ángulo restante y los dos lados faltantes:
1. $B=110^\circ, a=30\text{ cm}, C=29^\circ$.
2. $A=80^\circ, b=15\text{ m}, C=40^\circ$.
3. $C=105^\circ, B=35^\circ, a=10\text{ cm}$.
4. $A=50^\circ, B=60^\circ, c=22\text{ m}$.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
Resuelva los terrenos (considerando el ángulo obtuso indicado). Cercado: $\$20\text{ USD}/m$.
1. $A=21^\circ, a=14\text{ m}, c=26\text{ m}$. ($C$ es obtuso).
2. $B=25^\circ, b=10\text{ m}, a=18\text{ m}$. ($A$ es obtuso).
3. $C=30^\circ, c=15\text{ m}, b=25\text{ m}$. ($B$ es obtuso).
4. $A=15^\circ, a=8\text{ m}, c=20\text{ m}$. ($C$ es obtuso).
```

```ad-success
title: ✅ Respuestas (para el docente)
**Bloque Fácil:**
1. $c \approx 8.15\text{ m}$ | 2. $b \approx 10.61\text{ cm}$ | 3. $a \approx 8.68\text{ m}$ | 4. $c \approx 13.76\text{ cm}$

**Bloque Medio:**
1. $A=41^\circ, b \approx 42.97\text{ cm}, c \approx 22.18\text{ cm}$
2. $B=60^\circ, a \approx 17.06\text{ m}, c \approx 11.13\text{ m}$
3. $A=40^\circ, b \approx 8.92\text{ cm}, c \approx 15.03\text{ cm}$
4. $C=70^\circ, a \approx 17.94\text{ m}, b \approx 20.28\text{ m}$

**Bloque Avanzado:**
1. $C \approx 138.28^\circ, B \approx 20.72^\circ, b \approx 13.82\text{ m}$. Costo: $\$1,076.40$
2. $A \approx 130.48^\circ, C \approx 24.52^\circ, c \approx 9.82\text{ m}$. Costo: $\$756.40$
3. $B \approx 123.56^\circ, A \approx 26.44^\circ, a \approx 13.36\text{ m}$. Costo: $\$1,067.20$
4. $C \approx 139.68^\circ, B \approx 25.32^\circ, b \approx 13.21\text{ m}$. Costo: $\$824.20$
```

## 6. Mini-prueba de autoevaluación
```ad-question
title: 🧪 Pregunta 1
Si en un triángulo $A=100^\circ$ y $B=40^\circ$, ¿cuánto mide $C$?
- a) $180^\circ$ | **b) $40^\circ$** (Explicación: $180 - 100 - 40 = 40$).
```
```ad-question
title: 🧪 Pregunta 2
¿Cuál es el despeje correcto de $x$ en $\frac{x}{\sin 50^\circ} = \frac{10}{\sin 30^\circ}$?
- a) $x = 10 \cdot \sin 50^\circ \cdot \sin 30^\circ$ | **b) $x = \frac{10 \cdot \sin 50^\circ}{\sin 30^\circ}$**
```
```ad-question
title: 🧪 Pregunta 3
Si un lado mide $10\text{ m}$ y su ángulo opuesto es $30^\circ$, ¿cuál es la proporción constante (lado/seno)?
- a) $5$ | **b) $20$** (Cálculo: $10 / \sin 30^\circ = 10 / 0.5 = 20$).
```

## 7. Notas para el próximo tema
> [!tip] 💡 En la próxima clase
> Ahora que dominas el Teorema del Seno con su "pareja de oro", ¿qué pasa si los datos conocidos no son opuestos entre sí (por ejemplo, dos lados y el ángulo que forman)? Para esos casos usaremos el **Teorema del Coseno**.

> [!info] 🧭 Navegación
> [[Clase 03|⬅ Clase 03]] | [[00 - Índice del curso|Índice]] | **Clase 04** | | [[Clase 05|Clase 05 ➡]]