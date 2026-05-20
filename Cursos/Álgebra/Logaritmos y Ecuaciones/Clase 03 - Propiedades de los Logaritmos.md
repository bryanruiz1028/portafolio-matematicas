# Clase 03 — Propiedades de los Logaritmos
tags: #algebra #propertiesoflog
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 4

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | [[Clase 04|Clase 04 ➡]]

---

> [!info] 🌍 Relevancia y aplicaciones
> Las propiedades de los logaritmos permiten simplificar cálculos transformando operaciones de alta jerarquía (multiplicación, división, potencia) en operaciones más sencillas (suma, resta, multiplicación). Esta lógica es vital para manejar escalas exponenciales de forma lineal.
> - 💵 **Aplicación con $USD**: Permite despejar el exponente en fórmulas de interés compuesto para hallar el tiempo necesario para duplicar una inversión.
> - 🏗️ **Aplicación práctica**: Esencial para medir la magnitud de sismos (Escala Richter) o el nivel de acidez de una sustancia (pH).
> - 📊 **Situación cotidiana**: Facilita la comparación de tasas de crecimiento poblacional o la pérdida de poder adquisitivo por inflación.

---

> [!note] 📌 ¿Qué son las Propiedades de los Logaritmos?
> Son "atajos" o reglas mágicas que nos permiten transformar operaciones que parecen imposibles en otras mucho más fáciles. Por ejemplo, gracias a estas reglas, podemos convertir una raíz cuadrada en una simple multiplicación. 
> 
> **Regla de Oro de los Signos:** En expresiones con múltiples logaritmos, recuerda el "estilo Profe Alex": los términos con logaritmos **positivos van arriba** (numerador) y los logaritmos **negativos van abajo** (denominador) al unirlos.

> [!warning] ⚠️ ¡Pilas con esto!
> 1. **Bases Idénticas:** Solo puedes aplicar estas propiedades si las bases de los logaritmos son **exactamente iguales**. Si las bases son distintas, no se pueden unir ni separar.
> 2. **Error de Suma:** No confundas la suma de argumentos con la suma de logaritmos:
>    - ❌ Incorrecto: $\log(A + B) = \log A + \log B$
>    - ✅ Correcto: $\log(A \cdot B) = \log A + \log B$

> [!tip] 💡 Truco para recordarlo: "El Tobogán"
> Para la **Propiedad de la Potencia**, imagina que el exponente está en la cima de un tobogán. La regla le permite "deslizarse" hacia abajo hasta quedar sentado justo antes del logaritmo, multiplicando a toda la expresión.

---

### Procedimiento Paso a Paso

```text
PASO 1 → Identificar la operación principal en el argumento (producto, cociente, potencia o raíz).
PASO 2 → Decidir si se requiere "expandir" (separar) o "condensar" (unir). 
         * REGLA: Al condensar, logaritmos positivos van al numerador y negativos al denominador.
PASO 3 → Verificar que todas las bases sean idénticas antes de operar.
PASO 4 → Identificar logaritmos particulares (base igual al argumento da 1; argumento 1 da 0).
PASO 5 → Resolver la aritmética final para hallar el resultado.
```

---

### Ejemplos Prácticos

```ad-example
title: Ejemplo 1: Caso Básico (Producto y Base Diez)
Calcular: $\log_{10}(100 \cdot 10)$
1. **Expandir**: Como es un producto, separamos en suma: $\log_{10} 100 + \log_{10} 10$.
2. **Resolver**:
   - $\log_{10} 100 = 2$ (porque $10^2 = 100$).
   - $\log_{10} 10 = 1$ (porque base y argumento son iguales).
3. **Resultado**: $2 + 1 = 3$.
```

```ad-example
title: Ejemplo 2: Caso con Signos (Cociente)
Calcular: $\log_3(45/5)$
1. **Propiedad**: Aplicamos el logaritmo de un cociente. El de arriba es positivo y el de abajo negativo: $\log_3 45 - \log_3 5$.
2. **Análisis**: Por separado, $\log_3 45$ y $\log_3 5$ no tienen resultado entero exacto (3 a ninguna potencia entera da 45).
3. **Condensar**: Aplicamos la propiedad "al revés" para simplificar: $\log_3 (45/5) = \log_3 9$.
4. **Resolver**: $\log_3 9 = 2$ (ya que $3^2 = 9$). El uso de la propiedad hizo posible lo "imposible".
```

```ad-example
title: Ejemplo 3: Caso Avanzado (Raíz y Potencia)
Calcular: $\log_2(\sqrt[3]{16})$
1. **Transformar**: Pasamos la raíz a exponente fraccionario: $\log_2(16^{1/3})$.
2. **El Tobogán**: Bajamos el $1/3$ a multiplicar: $\frac{1}{3} \cdot \log_2 16$.
3. **Resolver**: Como $\log_2 16 = 4$, la operación final es $\frac{1}{3} \cdot 4$.
4. **Resultado**: $4/3$.
```

```ad-example
title: Ejemplo 4: Aplicación $USD
Si el crecimiento de un fondo se mide con $\log_{1.1}(X)$, ¿cuánto vale el logaritmo si el saldo final $X$ es $1.1$ USD?
1. **Propiedad**: Identificamos que la base ($1.1$) y el argumento ($1.1$) son idénticos.
2. **Regla Particular**: $\log_b b = 1$.
3. **Resultado**: 1. (Significa que el capital es igual a la base elevada a la 1).
```

---

### Ejercicios para el Estudiante

```ad-abstract
title: 🟢 Nivel Fácil: Logaritmos Particulares
Resuelve aplicando las reglas de base y argumento:
1. $\log_5 1$
2. $\log_7 7$
3. $\log_{10} 10$
4. $\ln e$ (Pista: La base del logaritmo natural es $e$)
```

```ad-abstract
title: 🟡 Nivel Medio: Producto y Cociente
Aplica las propiedades para condensar o expandir según convenga:
1. $\log_2(8 \cdot 4)$
2. $\log_3(81 / 9)$
3. $\log_{10}(1000 / 10)$
4. $\log_6 12 + \log_6 3$ (Une los logaritmos en uno solo primero)
```

```ad-abstract
title: 🔴 Nivel Avanzado: Potencias y Raíces ($USD)
Resuelve los siguientes casos de crecimiento e interés:
1. $\log_2(16^5)$ (Crecimiento de capital tras 5 periodos).
2. $\log_3(\sqrt{81})$ (Cálculo de tasa media simplificada).
3. $\log_5(x \cdot 5)$ (Expresa la expansión para una variable de dinero $x$).
4. $\log_2(32^{1/2})$ (Raíz cuadrada aplicada a un fondo de ahorro).
```

```ad-success
title: Respuestas y Explicaciones (Para el Docente)
**Fácil**: 1) 0 | 2) 1 | 3) 1 | 4) 1.
**Medio**: 1) 5 (porque $3+2$) | 2) 2 (porque $4-2$) | 3) 2 | 4) 2 (porque $\log_6 36$).
**Avanzado**: 
1) 20 (Bajamos el 5: $5 \cdot \log_2 16 = 5 \cdot 4$). 
2) 2 (Bajamos el 1/2: $\frac{1}{2} \cdot \log_3 81 = \frac{1}{2} \cdot 4$). 
3) $\log_5 x + 1$ (Se usa la **Propiedad del Producto** para separar $\log_5 x + \log_5 5$, y luego la **Propiedad Particular** pues $\log_5 5 = 1$). 
4) 2.5 o 5/2 (Bajamos el 1/2: $\frac{1}{2} \cdot 5$).
```

---

### Autoevaluación

```ad-question
title: Pregunta 1
¿Cuál es el resultado de $\log_{100} 1$?
**Respuesta**: 0. Por propiedad, siempre que el argumento sea 1, el resultado es 0 porque cualquier base (excepto las no permitidas) elevada a la 0 da 1.
```

```ad-question
title: Pregunta 2
¿Cómo se expresa $\log_b(\sqrt[n]{A})$ usando la propiedad de la potencia?
**Respuesta**: $\frac{1}{n} \cdot \log_b A$. Primero transformamos la raíz en exponente fraccionario ($A^{1/n}$) y luego aplicamos "el tobogán" para bajar el exponente a multiplicar.
```

```ad-question
title: Pregunta 3
Si una pérdida financiera se expresa como $\log_2(8) - \log_2(4)$, ¿qué propiedad aplicas para resolverlo rápido?
**Respuesta**: La propiedad del cociente (resta de logaritmos). Al tener la misma base, unimos los argumentos dividiendo: $\log_2(8/4) = \log_2 2 = 1$.
```

---

> [!tip] 💡 En la próxima clase
> Estas reglas de "unir y desarmar" son las herramientas que usaremos para despejar la incógnita en las **Ecuaciones Logarítmicas**. ¡No olvides el truco del tobogán!

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | [[Clase 04|Clase 04 ➡]]