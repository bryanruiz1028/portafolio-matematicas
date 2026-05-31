# 📖 Guía de estudio — Clase 03: Áreas Sombreadas

> [!info] 📌 Conceptos clave
> - **Definición:** El área sombreada es la región resultante de la combinación, superposición o sustracción de figuras geométricas conocidas.
> - **Método de suma:** Se utiliza cuando la figura total se compone de varias piezas que se agregan (por ejemplo, un rectángulo unido a un semicírculo).
> - **Método de resta:** Se aplica cuando a una figura principal de mayor tamaño se le "quita" o extrae otra figura menor (como un círculo grande con perforaciones circulares).
> - **Técnica de transposición (mover áreas):** Consiste en reorganizar o rotar partes de las áreas sombreadas para completar figuras más simples. Es fundamental entender la **conservación del área**: mover una pieza no cambia el área total, solo facilita su visualización y cálculo.

## 📐 Fórmulas y definiciones principales

| Término | Definición / Fórmula |
| :--- | :--- |
| **Área del Rectángulo** | $b \times h$ (Base por altura) |
| **Área del Cuadrado** | $L^2$ (Lado al cuadrado) |
| **Área del Círculo** | $\pi \times r^2$ |
| **Área del Semicírculo** | $(\pi \times r^2) / 2$ |
| **Número Pi ($\pi$)** | Aproximación estándar en esta clase: $3.1416$ |
| **Radio ($r$)** | Distancia del centro al borde. **Recuerda:** es siempre la mitad del diámetro ($d/2$). |

---

## 📝 Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Suma de Rectángulo y Semicírculo
**Problema:** Calcular el área de una figura compuesta por un rectángulo de $14 \text{ cm}$ de base y $6 \text{ cm}$ de altura, con un semicírculo de $7 \text{ cm}$ de radio acoplado a su base.

**Resolución:**
1. **Paso 1 (Área del rectángulo):** Multiplicamos base por altura.
   $14 \text{ cm} \times 6 \text{ cm} = 84 \text{ cm}^2$
2. **Paso 2 (Área del semicírculo):** Calculamos el área del círculo completo y dividimos entre dos.
   $A = \frac{3.1416 \times (7 \text{ cm})^2}{2} = \frac{3.1416 \times 49 \text{ cm}^2}{2} = 76.9692 \text{ cm}^2$
3. **Resultado final:** Sumamos ambas áreas y redondeamos.
   $84 \text{ cm}^2 + 76.9692 \text{ cm}^2 = 160.9692 \text{ cm}^2 \approx 160.97 \text{ cm}^2$
```

```ad-example
title: Ejemplo B — Costo de Material para Placa Metálica
**Problema:** Se requiere fabricar una placa metálica que consiste en un círculo grande al que se le han perforado dos círculos pequeños idénticos (radio de $4 \text{ cm}$ cada uno). El radio del círculo grande se deduce observando que su diámetro coincide con la suma de los diámetros de los pequeños, resultando en un radio de $8 \text{ cm}$. Si el material cuesta $\$2 \text{ USD}$ por $\text{cm}^2$, ¿cuál es el presupuesto?

**Cálculos:**
1. **Área Sombreada:** Aplicamos resta (Área Grande - 2 veces Área Pequeña).
   $A = (64\pi) - 2(16\pi) = 32\pi \text{ cm}^2$
   $32 \times 3.1416 = 100.5312 \text{ cm}^2 \approx 100.53 \text{ cm}^2$
2. **Costo de fabricación:** Multiplicamos el área por el valor unitario.
   $100.53 \text{ cm}^2 \times \$2 \text{ USD} = \$201.06 \text{ USD}$

**Resultado:** El costo total del material es de **$201.06 USD**.
```

---

## ✍️ Ejercicios de repaso
*Realiza todos los cálculos utilizando la aproximación $\pi \approx 3.1416$ y expresa tus resultados en $\text{cm}^2$.*

```ad-abstract
title: 🟢 Nivel: Fácil
1. Un cuadrado mide $10 \text{ cm}$ de lado. En su centro hay un círculo blanco (no sombreado) de radio $5 \text{ cm}$. Calcula el área sombreada restante.
2. Calcula el área total de una figura formada por la unión de dos rectángulos: uno de $10 \text{ cm} \times 5 \text{ cm}$ y otro de $5 \text{ cm} \times 5 \text{ cm}$.
3. Encuentra el área de una región formada por la suma de un rectángulo de $20 \text{ cm} \times 10 \text{ cm}$ y un semicírculo cuyo radio es de $10 \text{ cm}$.
```

```ad-abstract
title: 🟡 Nivel: Medio (Técnica de Transposición)
*Para estos ejercicios, te sugerimos realizar trazos auxiliares como los del minuto 2:30 del Ejemplo 5.*

1. Imagina un cuadrado de $10 \text{ cm}$ de lado dividido en 4 cuadrantes. En dos cuadrantes opuestos hay cuartos de círculo sombreados. Mueve uno de ellos para completar un rectángulo de $10 \text{ cm} \times 5 \text{ cm}$ y calcula su área.
2. En un cuadrado de $8 \text{ cm}$ de lado, hay semicírculos sombreados que "sobresalen" y huecos idénticos dentro. Identifica cómo mover las piezas para completar el área exacta del cuadrado original.
3. Se presenta un rectángulo de $12 \text{ cm} \times 6 \text{ cm}$ con un semicírculo que sale de un extremo y un hueco semicircular en el otro. Realiza la transposición para simplificar la figura a un rectángulo simple y calcula el área.
```

```ad-abstract
title: 🔴 Nivel: Avanzado — Aplicación con $USD
**Reto Final (Basado en Ejemplo 6):** Una pieza industrial tiene forma de corona circular. El círculo exterior tiene un radio de $4 \text{ cm}$ y el círculo interior (el hueco) tiene un radio de $2 \text{ cm}$.

1. Calcula el área sombreada (Área exterior - Área interior).
2. Si el acabado de la pieza cuesta $\$5 \text{ USD}$ por $\text{cm}^2$, ¿cuál es el costo total de fabricación?
```

---

> [!tip] 💡 Consejo de estudio
> Antes de aplicar fórmulas, ¡analiza la figura! Realizar **trazos auxiliares** (líneas verticales u horizontales que dividan la figura en partes iguales) te permitirá visualizar movimientos de piezas. A veces, una figura que parece imposible se resuelve simplemente moviendo un área sombreada a un espacio vacío. ¡Confía en tu capacidad de observación y verás cómo la geometría se vuelve mucho más sencilla!