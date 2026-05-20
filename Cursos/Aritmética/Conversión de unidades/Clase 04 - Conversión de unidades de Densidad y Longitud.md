# Clase 04 — Conversión de unidades de Densidad y Longitud

tags: #algebra #conversindeunid
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 4 de 6

> [!info] 🧭 Navegación
> [Anterior: Clase 03 — Conversión de Longitud]([[Clase 03 - Conversión de Longitud]]) | [Índice del curso]([[00 - Índice del curso]])

> [!info] 🌍 Relevancia y aplicaciones
> Entender la densidad nos permite comprender qué tan "apretadas" están las partículas de un material en un espacio determinado, mientras que dominar las unidades inglesas (pulgadas, pies, yardas) es esencial para el comercio y la ingeniería global.
> - **💵 [Aplicación USD]:** Calcular con precisión los costos de importación de materias primas cuyo precio varía según su peso (masa) y el volumen que ocupan en el transporte.
> - **🏗️ [Aplicación práctica]:** Interpretación correcta de planos arquitectónicos y manuales de maquinaria fabricada en EE. UU. o Reino Unido, donde los pies y pulgadas son la norma.
> - **📊 [Situación cotidiana]:** Saber si un objeto flotará o se hundirá en el agua al comparar su densidad, o calcular cuánta pintura comprar para una superficie medida en yardas.

> [!note] 📌 ¿Qué es Conversión de unidades de Densidad?
> ¡Hola! Imagina que la densidad es como un autobús escolar: si hay muchos niños en poco espacio, la densidad es alta; si hay pocos niños en el mismo autobús, es baja. Matemáticamente, es la relación entre la **masa** y el **volumen** ($\text{Densidad} = \frac{\text{masa}}{\text{volumen}}$). 
> 
> Lo emocionante de convertir unidades de densidad es que debemos transformar **dos unidades al mismo tiempo**: una unidad de masa (como gramos a kilogramos) y una de volumen (como centímetros cúbicos a metros cúbicos). Para lograrlo, utilizaremos "cadenas" de factores de conversión.

> [!warning] ⚠️ Error común
> El tropiezo más frecuente es olvidar que las unidades de volumen son cúbicas. Muchos estudiantes creen que como $1\text{ m} = 100\text{ cm}$, entonces $1\text{ m}^3$ también son $100\text{ cm}^3$. ¡Cuidado!
> Al elevar al cubo la longitud, también elevamos el número: 
> $(100\text{ cm})^3 = 100 \times 100 \times 100 = 1,000,000\text{ cm}^3$. 
> Por lo tanto: **$1\text{ m}^3 = 1,000,000\text{ cm}^3$** (o $10^6$).

> [!tip] 💡 Truco para recordarlo
> ¿No tienes una cinta métrica a la mano? Recuerda que un **pie** ($1\text{ ft}$) mide exactamente **30.48 cm**, que es casi lo mismo que una **regla escolar grande** de plástico. ¡Visualiza esa regla y nunca olvidarás el tamaño de un pie!

### Procedimiento paso a paso

```text
PASO 1: Identificar las equivalencias necesarias (ej. 1 kg = 1000 g, 1 in = 2.54 cm).
PASO 2: Plantear el factor de conversión (fracciones) o la Regla de Tres simple.
PASO 3: Multiplicar los valores de arriba y dividir por el producto de los de abajo.
PASO 4: Cancelar las unidades repetidas y verificar que el resultado tenga sentido.
```

### Ejemplos guiados

> [!example] Ejemplo 1: Básico - Densidad
> **Problema:** Convertir $5000 \frac{g}{cm^3}$ a $\frac{kg}{cm^3}$.
> Como queremos cambiar gramos a kilogramos pero mantener los $\text{cm}^3$, usamos un solo factor:
> 1. Factor: $\frac{5000\text{ g}}{1\text{ cm}^3} \cdot \left( \frac{1\text{ kg}}{1000\text{ g}} \right)$
> 2. Operación: $\frac{5000 \cdot 1}{1000}$
> **Resultado:** **$5 \frac{kg}{cm^3}$**

> [!example] Ejemplo 2: Longitudes (Regla de Tres)
> **Problema:** Convertir 52 pies a centímetros.
> 1. Equivalencia: $1\text{ pie} = 30.48\text{ cm}$.
> 2. Planteamiento: 
>    $1\text{ pie} \rightarrow 30.48\text{ cm}$
>    $52\text{ pies} \rightarrow x$
> 3. Cálculo: $x = \frac{52 \cdot 30.48}{1}$
> **Resultado:** **1584.96 cm**

> [!example] Ejemplo 3: Avanzado - Yardas a Metros
> **Problema:** Convertir 24 yardas a metros.
> 1. Equivalencia: $1\text{ yarda} = 0.9149\text{ m}$.
> 2. Operación: $24 \cdot 0.9149 = 21.9576$.
> **Resultado:** **21.96 m** (redondeado correctamente).

> [!example] Ejemplo 4: Aplicación USD
> **Problema:** Un metal tiene una densidad de $12 \frac{g}{cm^3}$. Si el envío cuesta **0.50 USD** por cada kilogramo, ¿cuánto cuesta enviar $1000 \text{ cm}^3$?
> 1. Convertimos la densidad a $\frac{kg}{cm^3}$ usando el factor:
>    $12 \frac{g}{cm^3} \cdot \left( \frac{1\text{ kg}}{1000\text{ g}} \right) = 0.012 \frac{kg}{cm^3}$
> 2. Calculamos la masa total del envío:
>    $0.012 \frac{kg}{cm^3} \cdot 1000\text{ cm}^3 = 12\text{ kg}$
> 3. Calculamos el costo final:
>    $12\text{ kg} \cdot 0.50\text{ USD/kg} = 6.00\text{ USD}$
> **Resultado:** El costo total es **6.00 USD**.

---

### Ejercicios para el estudiante

#### 🟢 Fácil (Longitud)
1. Convierte 3 pulgadas a centímetros ($1\text{ in} = 2.54\text{ cm}$).
2. Convierte 50 centímetros a pulgadas.
3. Convierte 10 pulgadas a centímetros.
4. Convierte 25.4 pies a centímetros ($1\text{ ft} = 30.48\text{ cm}$).

#### 🟡 Medio (Densidad)
5. Convierte $5000 \frac{g}{cm^3}$ a $\frac{kg}{cm^3}$.
6. Convierte $12 \frac{g}{cm^3}$ a $\frac{kg}{m^3}$ (Recuerda: $1\text{ m}^3 = 1,000,000\text{ cm}^3$).
7. Convierte $250 \frac{kg}{m^3}$ a $\frac{g}{m^3}$.
8. Convierte $7200 \frac{kg}{m^3}$ a $\frac{g}{cm^3}$.

#### 🔴 Avanzado (Aplicación con $USD)
9. Una tela se vende a **5 USD** la yarda. ¿Cuántos dólares cuestan 15 metros de esa tela? (Usa $1\text{ yarda} = 0.9149\text{ m}$).
10. El costo de una madera es de **3 USD** por pie. ¿Cuánto cuesta una pieza que mide 350 cm?
11. Un líquido tiene una densidad de $1.2 \frac{g}{cm^3}$. Si el transporte de cada kilogramo cuesta **2 USD**, ¿cuánto cuesta transportar $5000\text{ cm}^3$?
12. Un material especial cuesta **10 USD** por metro. ¿Cuánto cuestan 5 yardas de ese material?

#### ✅ Respuestas
1. **7.62 cm**
2. **19.69 in** (redondeado de 19.685)
3. **25.4 cm**
4. **774.19 cm** (redondeado de 774.192)
5. **5 \frac{kg}{cm^3}**
6. **12,000 \frac{kg}{m^3}**
7. **250,000 \frac{g}{m^3}**
8. **7.2 \frac{g}{cm^3}**
9. **81.98 USD** (Cálculo: $15 \div 0.9149 \cdot 5 = 81.976...$)
10. **34.45 USD** (Cálculo: $350 \div 30.48 \cdot 3 = 34.448...$)
11. **12.00 USD** (Masa: $6\text{ kg}$)
12. **45.75 USD** (Cálculo: $5 \cdot 0.9149 \cdot 10 = 45.745$)

---

### Mini-prueba de autoevaluación

1. **¿Cuál es la equivalencia correcta de 1 metro cúbico en centímetros cúbicos?**
   - a) $1,000\text{ cm}^3$
   - b) $10,000\text{ cm}^3$
   - c) $1,000,000\text{ cm}^3$

2. **Si tienes una pieza de metal de 10 pulgadas de largo, ¿cuántos cm mide?**
   - Respuesta: **25.4 cm**

3. **Una viga de madera mide 8 pies. Si el precio es de 4 USD por pie, ¿cuál es el costo?**
   - a) 24 USD
   - b) 32 USD
   - c) 30.48 USD

---

> [!tip] 💡 En la próxima clase
> ¡Excelente trabajo! Ahora que ya sabes moverte entre dimensiones y densidades, en la **Clase 05** daremos el salto al tiempo: aprenderemos a convertir horas, minutos y segundos para calcular velocidades.

> [!info] 🧭 Navegación
> [Anterior: Clase 03 — Conversión de Longitud]([[Clase 03 - Conversión de Longitud]]) | [Índice del curso]([[00 - Índice del curso]])