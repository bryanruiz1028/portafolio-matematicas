# Clase 05 — División de números complejos y potencias de "i"

`tags: #matemáticas #álgebra-lineal #números-complejos #educación`

[[Clase 04|⬅ Clase 04]] | [[Índice|🏠 Inicio]] | [[Clase 06|Clase 06 ➡]]

---

### 1. Introducción: Relevancia y Aplicaciones

> [!info] 🌍 Relevancia y aplicaciones
> Durante siglos, los matemáticos evitaron el "monstruo" de las raíces cuadradas de números negativos, considerándolas imposibles o "anfibios entre el ser y la nada". En 1777, **Leonhard Euler** estandarizó el uso de la letra $i$ para $\sqrt{-1}$, permitiendo que la ciencia avanzara en terrenos donde los números reales no tenían respuesta.
> 
> **¿Dónde aplicamos esto hoy?**
> *   **Ingeniería de Circuitos:** La división de complejos es fundamental para calcular la impedancia en circuitos de corriente alterna (relación entre voltaje y corriente).
> *   **Balance Financiero Proyectado:** En modelos de riesgo, se utilizan para representar flujos de efectivo bajo variables complejas, permitiendo ajustes precisos en carteras de inversión de **$USD**.
> *   **Procesamiento Digital:** El filtrado de audio y la compresión de imágenes dependen de operar con estas frecuencias imaginarias para eliminar ruido.

---

### 2. Conceptos Clave: La Unidad Imaginaria y el Conjugado

> [!note] 📌 ¿Qué es la División de números complejos?
> Dividir números complejos no es una partición común; es un proceso de **eliminación de la unidad imaginaria ($i$) del denominador**. El objetivo es transformar el denominador en un número real multiplicándolo por su **conjugado**.

#### El Ciclo de Potencias de $i$
Según el estándar de Euler, la unidad imaginaria $i$ se comporta de forma cíclica cada cuatro potencias:
*   $i^0 = 1$ (Todo número elevado a la cero es la unidad).
*   $i^1 = i$ (Cualquier base a la potencia 1 es la misma base).
*   $i^2 = -1$ (Definición fundamental: al elevar $\sqrt{-1}$ al cuadrado, la raíz se elimina).
*   $i^3 = -i$ (Resultado de multiplicar $i^2 \cdot i = -1 \cdot i$).

#### El Conjugado de un número complejo ($\bar{Z}$)
Si tenemos un número $Z = a + bi$, su conjugado (denotado como $\bar{Z}$) es simplemente el mismo número pero con el signo de la parte imaginaria invertido: $\bar{Z} = a - bi$.

> [!warning] ⚠️ Error común
> Al obtener el conjugado, **solo se cambia el signo del centro** (la parte imaginaria). La parte real permanece idéntica. 
> *   Ejemplo: Si $Z = -5 + 3i$, entonces $\bar{Z} = -5 - 3i$.

> [!tip] 💡 Truco para recordarlo
> El ciclo de $i$ siempre se repite: **1, i, -1, -i**. Para cualquier potencia mayor, divide el exponente entre 4; el residuo (0, 1, 2 o 3) te dirá a cuál de los valores básicos equivale.

---

### 3. Procedimiento Paso a Paso

Para resolver una división $\frac{Z_1}{Z_2}$, sigue esta secuencia técnica:

```text
1. Identificar el conjugado del denominador (Z2) -> Z̄2.
2. Multiplicar numerador y denominador por dicho conjugado (Z̄2).
3. Realizar los cálculos:
   a. Numerador: Aplicar propiedad distributiva término a término.
   b. Denominador: Usar el producto notable (a + bi)(a - bi) = a² + b².
4. Sustituir i² por -1, simplificar términos y separar en parte real e imaginaria.
```

---

### 4. Sección de Ejemplos Desarrollados

```ad-example
**Ejemplo 1: Operación Básica**
Dividir $Z_1 = -4 + 5i$ entre $Z_2 = 8 - 2i$:
1. **Conjugado del denominador ($\bar{Z}_2$):** $8 + 2i$.
2. **Planteamiento:** $\frac{-4 + 5i}{8 - 2i} \cdot \frac{8 + 2i}{8 + 2i}$
3. **Desarrollo del Numerador:**
   $\begin{aligned} &(-4 \cdot 8) + (-4 \cdot 2i) + (5i \cdot 8) + (5i \cdot 2i) \\ &= -32 - 8i + 40i + 10i^2 \\ &= -32 + 32i + 10(-1) = -42 + 32i \end{aligned}$
4. **Desarrollo del Denominador:** $8^2 + 2^2 = 64 + 4 = 68$.
5. **Resultado Final:** $\frac{-42}{68} + \frac{32}{68}i = -\frac{21}{34} + \frac{8}{17}i$
```

```ad-example
**Ejemplo 2: Simplificación de Fracciones**
Dividir $1$ entre $Z = -9 - 12i$:
1. **Multiplicación por conjugado:** $\frac{1(-9 + 12i)}{(-9)^2 + (12)^2}$
2. **Cálculo:** $\frac{-9 + 12i}{81 + 144} = \frac{-9 + 12i}{225}$
3. **Separación:** $-\frac{9}{225} + \frac{12}{225}i$
4. **Simplificación Máxima:** $-\frac{1}{25} + \frac{4}{75}i$
```

```ad-example
**Ejemplo 3: Uso de Potencias de $i$**
Resolver $\frac{i^6}{2 + i^7}$:
1. **Reducción:** $i^6 = i^2 = -1$. Además, $i^7 = i^3 = -i$.
2. **Expresión:** $\frac{-1}{2 - i}$.
3. **Conjugado:** $\bar{Z} = 2 + i$.
4. **Operación:** $\frac{-1(2 + i)}{2^2 + 1^2} = \frac{-2 - i}{4 + 1} = -\frac{2}{5} - \frac{1}{5}i$
```

```ad-example
**Ejemplo 4: Aplicación Financiera ($USD$)**
Una deuda de $(-100 + 50i) USD$ se reparte entre $(10 + 5i)$ socios. ¿Cuál es la "responsabilidad compleja" de cada socio?
1. **Multiplicación:** $\frac{-100 + 50i}{10 + 5i} \cdot \frac{10 - 5i}{10 - 5i}$
2. **Numerador:** $-1000 + 500i + 500i - 250i^2 = -1000 + 1000i + 250 = -750 + 1000i$.
3. **Denominador:** $10^2 + 5^2 = 125$.
4. **Resultado:** $(-6 + 8i) USD$ por socio.
```

---

### 5. Práctica Independiente

```ad-abstract
**🟢 Nivel Fácil**
1. Hallar el conjugado de $Z = 12 - 5i$.
2. Hallar el conjugado de $Z = -3 + i$.
3. Simplificar $i^{40}$.
4. Simplificar $i^{23}$.
```

```ad-abstract
**🟡 Nivel Medio**
1. Resolver: $\frac{3 + 2i}{1 + i}$
2. Resolver: $\frac{5 - i}{2 - 3i}$
3. Resolver: $\frac{-2 + 4i}{3 + i}$
4. Hallar el conjugado de la suma: $\overline{(2 + 3i) + (1 - 5i)}$.
```

```ad-abstract
**🔴 Nivel Avanzado (Contexto $USD$)**
1. Dividir una inversión de $(20 + 10i) USD$ entre un factor de riesgo de $(1 - i)$.
2. Calcular $\frac{Z_1}{Z_2}$ si $Z_1 = (10i + i^2) USD$ y $Z_2 = (3 + i) USD$.
3. Simplificar y dividir: $\frac{i^5 + i^6}{i^0 + i^1}$.
4. Un activo de $(15 + 30i) USD$ se divide en $(3 - 3i)$ cuotas. ¿Cuál es el valor de cada una?
```

```ad-success
**Solucionario para el Docente**
*   **Fácil:** 1) $12+5i$, 2) $-3-i$, 3) $1$, 4) $-i$.
*   **Medio:** 1) $2.5 - 0.5i$, 2) $1+i$, 3) $-0.2 + 1.4i$, 4) $3+2i$.
*   **Avanzado:** 1) $(5+15i) USD$, 2) $(0.7 + 3.1i) USD$, 3) $i$, 4) $(-2.5 + 7.5i) USD$.
```

---

### 6. Evaluación y Cierre

```ad-question
**Pregunta 1: Teoría**
¿En qué año Leonhard Euler introdujo el símbolo $i$ para estandarizar los números imaginarios?
```

```ad-question
**Pregunta 2: Procedimiento**
Para dividir $\frac{Z_1}{2 + 3i}$, multiplicamos el numerador por $(2 - 3i)$. ¿Qué operación se realiza en el denominador para obtener un número real de forma rápida?
```

```ad-question
**Pregunta 3: Aplicación**
Si una pérdida financiera es $(-20 + 10i) USD$ y se divide exactamente por $2i$, ¿cuál es el componente real del resultado?
```

**Notas para el próximo tema:** En la Clase 06 aprenderemos a llevar estos resultados al **Plano de Argand**, visualizando la posición de los números complejos de forma geométrica.

[[Clase 04|⬅ Clase 04]] | [[Índice|🏠 Inicio]] | [[Clase 06|Clase 06 ➡]]