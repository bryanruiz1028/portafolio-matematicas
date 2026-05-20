# 📖 Guía de estudio — Clase 02: Simplificación de expresiones con radicales

```ad-info
title: 📌 Conceptos clave
- **Índice par vs. impar**: Si el radicando es negativo, la cancelación directa solo es válida si el índice es **impar** (ej. $\sqrt[3]{-a^3} = -a$). Si el índice es **par**, el resultado es siempre positivo.
- **Valor Absoluto**: Al simplificar raíces de índice par con variables ($\sqrt{x^2}$) o números negativos, es obligatorio usar el **valor absoluto** ($|a|$) para obtener la raíz principal.
- **Mínimo Común Índice (MCI)**: Técnica para igualar índices calculando el **MCM** de los mismos. Permite preparar raíces para operaciones como la multiplicación.
- **Descomposición en factores primos**: Consiste en desglosar el radicando para agrupar sus factores en potencias que coincidan con el índice, facilitando su extracción.
```

---

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Índice Impar (Negativo)** | Se cancela directamente: $\sqrt[n]{-a^n} = -a$ (Si $n$ es impar). Ej: $\sqrt[3]{-8} = \sqrt[3]{-2^3} = -2$. |
| **Índice Par (Negativo/Variable)** | Se aplica valor absoluto: $\sqrt[n]{a^n} = \vert a \vert$. Ej: $\sqrt{(-7)^2} = \vert -7 \vert = 7$ o $\sqrt{x^2} = \vert x \vert$. |
| **Mínimo Común Índice** | Se multiplica índice y exponente por un factor $k$ ($k = \text{MCM} \div \text{índice}$): $\sqrt[n]{a^m} = \sqrt[n \cdot k]{a^{m \cdot k}}$. |
| **Extracción de Factores** | Un factor sale de la raíz si su exponente es igual o múltiplo del índice. Se divide: $\text{Exponente} \div \text{Índice}$. |
| **Simplificación de Fracciones** | **Regla de oro:** Antes de extraer factores, simplifica la fracción *dentro* del radical si es posible. |

---

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Simplificación de raíz con factores primos
**Problema:** Simplificar $\sqrt[3]{250}$

**Paso a paso:**
1. **Árbol de descomposición:**
   - $250 \div 2 = 125$
   - $125 \div 5 = 25$
   - $25 \div 5 = 5$
   - $5 \div 5 = 1$
   Factores: $2 \cdot 5 \cdot 5 \cdot 5 = 2 \cdot 5^3$.
2. **Organización por índice:** Como el índice es **3**, buscamos "tríos". Tenemos un trío de cincos: $5^3$.
3. **Sustitución y separación:** $\sqrt[3]{2 \cdot 5^3} = \sqrt[3]{5^3} \cdot \sqrt[3]{2}$.
4. **Extracción final:** El exponente $3$ se cancela con el índice $3$.
**Resultado:** $5\sqrt[3]{2}$
```

```ad-example
title: Ejemplo B — Cálculo de presupuesto con áreas cuadradas ($USD)
**Problema:** Un jardín cuadrado tiene un área de $12 \text{ m}^2$. Se desea cercar un lado con una malla que cuesta $10 \text{ USD}$ por metro. ¿Cuál es el costo total simplificado?

**Paso a paso:**
1. **Hallar el lado ($L$):** El lado de un cuadrado es la raíz del área: $L = \sqrt{12}$.
2. **Simplificar el radical:**
   - $12 = 2^2 \cdot 3$.
   - $\sqrt{2^2 \cdot 3} = 2\sqrt{3} \text{ metros}$.
3. **Calcular costo:** Multiplicamos la longitud simplificada por el precio unitario:
   $\text{Costo} = (2\sqrt{3} \text{ m}) \cdot (10 \text{ USD/m}) = 20\sqrt{3} \text{ USD}$.
**Resultado:** $20\sqrt{3} \text{ USD}$
```

---

## Ejercicios de repaso

```ad-abstract
### Bloque 🟢 Fácil: Cancelación y Valor Absoluto
1. Simplifica aplicando la regla de índice impar: $\sqrt[5]{(-6)^5}$
2. Simplifica aplicando la regla de índice par: $\sqrt{(-10)^2}$
3. Simplifica la variable con índice par (¡Cuidado con la regla!): $\sqrt{x^2}$
4. Simplifica la variable con índice impar: $\sqrt[3]{x^3}$

### Bloque 🟡 Medio: Índices y Fracciones
1. Reduce a mínimo común índice para poder multiplicarlos: $\sqrt{m}$ y $\sqrt[3]{n}$.
2. Simplifica simplificando la fracción interna primero: $\sqrt{\frac{54}{8}}$
3. Extrae factores de la fracción: $\sqrt[3]{\frac{125}{16}}$

### Bloque 🔴 Avanzado — Aplicación con $USD
1. **El Contenedor:** El volumen de un contenedor cúbico es $\sqrt[3]{1080} \text{ m}^3$. Simplifica esta expresión para hallar la medida de su arista (lado).
2. **El Presupuesto:** Si el material para cubrir la **base** del contenedor cuesta $15 \text{ USD}$ por metro cuadrado, ¿cuál es el costo total?
   *(Pista: Primero eleva la arista simplificada al cuadrado para obtener el área de la base y luego multiplica por el costo).*
```

---

```ad-tip
title: 💡 Consejo de estudio
¡Todo depende del índice! Antes de empezar a escribir, mira siempre el "numerito pequeño" de la raíz. Él es tu guía: te dice si debes formar **parejas** (índice 2), **tríos** (índice 3) o **cuartetos** (índice 4). Si organizas tus factores primos en esos grupos desde el principio, la extracción será automática y sin errores.
```