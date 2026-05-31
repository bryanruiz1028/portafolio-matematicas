# Clase 02 — Volumen del Prisma Triangular Equilátero y Prisma Recto

#algebra #volumendeunpris

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [Clase 01 — Introducción a los Prismas](link_clase_01) | ➡️ **Siguiente:** [Clase 03 — Prismas con otras bases](link_clase_03)

---

### ¿Por qué es importante esta clase?
Los prismas rectos nos rodean: desde la caja de cereal en tu cocina hasta los grandes rascacielos de una ciudad. Saber calcular su volumen no es solo un ejercicio matemático, sino una herramienta para entender cuánto espacio ocupan los objetos y cuánto material necesitamos para construirlos o llenarlos.

**Aplicaciones en el mundo real:**
*   **💵 [USD]:** Determinar el costo exacto de llenar un tanque prismático con un combustible que cuesta, por ejemplo, $5.50 USD por $m^3$.
*   **🏗️ [Práctica]:** Calcular la cantidad de concreto necesaria para fabricar columnas arquitectónicas de soporte.
*   **📊 [Cotidiana]:** Diseñar el empaque perfecto para un chocolate (como el famoso "Toblerone") asegurando que quepa en su caja de transporte.

---

### Concepto Clave

> [!note] Definiciones del Profe Alex
> *   **Prisma Recto:** Es un cuerpo geométrico con dos caras paralelas e iguales llamadas **bases**. Su característica distintiva es que todas sus **caras laterales son rectángulos**.
> *   **Prisma Triangular Equilátero:** Es un prisma cuya base es un triángulo con sus tres lados de la misma medida ($L$).

> [!warning] Error Común de Unidades
> No confundas superficie con espacio. El área se mide en unidades cuadradas ($m^2$), pero el volumen representa un espacio tridimensional y **siempre** debe escribirse en **unidades cúbicas** ($m^3$, $cm^3$, etc.).

> [!tip] La Regla de Oro
> El volumen de cualquier prisma recto se calcula siempre con la misma lógica:
> **Volumen ($V$) = Área de la base ($A_b$) $\times$ Altura del prisma ($h$)**
> Lo único que cambia de un prisma a otro es la fórmula que usamos para encontrar el área de su base.

---

### Procedimiento Paso a Paso

Para un prisma triangular equilátero, normalmente necesitaríamos la altura del triángulo para calcular su área. Para facilitarnos la vida y evitar el Teorema de Pitágoras, usaremos una **fórmula directa** (o "atajo") que solo requiere conocer la medida del lado.

```text
1. IDENTIFICAR: Anota la medida del lado de la base (L) y la altura del prisma (h).
2. ÁREA DE LA BASE (Ab): Usa la fórmula especial para triángulos equiláteros: 
   Ab = (L² * √3) / 4   (Donde L² es Lado multiplicado por Lado).
3. VOLUMEN (V): Multiplica el área obtenida (Ab) por la altura total del prisma (h).
4. UNIDADES: Escribe el resultado con sus unidades elevadas al cubo (³).
```

---

### Ejemplos de Aplicación

```ad-example
title: Ejemplo 1: Caso Base (Lado 6m, Altura 9m)
1. **Área de la base:** Usamos $L = 6$.
   $A_b = \frac{6^2 \cdot \sqrt{3}}{4} = \frac{36 \cdot \sqrt{3}}{4} = 9\sqrt{3} \approx 15.588 \, m^2$
2. **Volumen:** Multiplicamos por la altura $h = 9$.
   $V = 15.588 \, m^2 \cdot 9 \, m = 140.292 \, m^3$
**Resultado:** El volumen es aproximadamente **$140.292 \, m^3$**.
```

```ad-example
title: Ejemplo 2: El Prisma "Azul" (Decimales)
Datos: Lado ($L$) = 3m, Altura ($h$) = 1m.
1. **Área de la base:** $A_b = \frac{3^2 \cdot \sqrt{3}}{4} = \frac{9 \cdot \sqrt{3}}{4} \approx 3.897 \, m^2$
2. **Volumen:** $V = 3.897 \, m^2 \cdot 1 \, m \approx 3.89 \, m^3$
**Resultado:** El volumen es **$3.89 \, m^3$**.
```

```ad-example
title: Ejemplo 3: El Prisma "Rojo" (Centímetros)
Datos: Lado ($L$) = 5cm, Altura ($h$) = 8cm.
1. **Área de la base:** $A_b = \frac{5^2 \cdot \sqrt{3}}{4} = \frac{25 \cdot \sqrt{3}}{4} \approx 10.825 \, cm^2$
2. **Volumen:** $V = 10.825 \, cm^2 \cdot 8 \, cm = 86.6 \, cm^3$
**Resultado:** El volumen es **$86.6 \, cm^3$**.
```

```ad-example
title: Ejemplo 4: Aplicación Económica [USD]
Si el contenedor del **Ejemplo 1** ($140.292 \, m^3$) se llena con un material que cuesta **$2.00 USD** por metro cúbico:
*   **Cálculo:** $140.292 \times 2.00 = 280.584$
**Resultado:** El costo total es de **$280.58 USD** (redondeado a dos decimales según el estándar financiero).
```

---

### Ejercicios para el Estudiante

```ad-abstract
title: 🟢 Nivel Verde (Fácil - Sustitución directa)
1. Lado base: 2m | Altura prisma: 5m
2. Lado base: 4m | Altura prisma: 10m
3. Lado base: 10cm | Altura prisma: 20cm
4. Lado base: 1m | Altura prisma: 6m
```

```ad-abstract
title: 🟡 Nivel Amarillo (Medio - Uso de decimales)
1. Lado base: 3.5m | Altura prisma: 7m
2. Lado base: 6cm | Altura prisma: 12.5cm
3. Lado base: 8m | Altura prisma: 4.2m
4. Lado base: 2.5cm | Altura prisma: 10cm
```

```ad-abstract
title: 🔴 Nivel Rojo (Avanzado - Aplicación USD)
1. Un tanque triangular ($L = 6m, h = 9m$) se llena con un líquido que cuesta $5.00 USD el $m^3$. ¿Cuál es el costo total?
2. Una columna ($L = 12cm, h = 100cm$) se rellena de resina a $0.50 USD el $cm^3$. Calcula el costo.
3. Se fabrica un chocolate ($L = 4cm, h = 15cm$). Si el $cm^3$ cuesta $0.10 USD, ¿cuánto cuesta producirlo?
4. Un contenedor ($L = 10m, h = 3m$) cobra $1.50 USD por $m^3$ de espacio. ¿Cuál es la renta mensual?
```

```ad-success
title: Solucionario para el Docente
*   **Verde:** 1) $8.66 \, m^3$, 2) $69.28 \, m^3$, 3) $866.02 \, cm^3$, 4) $2.59 \, m^3$.
*   **Amarillo:** 1) $37.13 \, m^3$, 2) $194.85 \, cm^3$, 3) $116.39 \, m^3$, 4) $27.06 \, cm^3$.
*   **Rojo:** 1) $701.46 USD, 2) $3,117.69 USD, 3) $10.39 USD, 4) $194.85 USD.
```

---

### Mini-prueba de Autoevaluación

```ad-question
title: Pregunta 1
¿Cuál es la característica obligatoria de las caras laterales de cualquier prisma recto?
a) Son siempre cuadrados perfectos.
b) Son siempre rectángulos.
c) Deben ser triángulos equiláteros.
d) Tienen forma de rombo.
```

```ad-question
title: Pregunta 2
¿Para qué utilizamos la fórmula $A = \frac{L^2 \cdot \sqrt{3}}{4}$ en esta clase?
a) Para hallar el volumen total de un solo golpe.
b) Para hallar el área de la base sin necesitar la altura del triángulo.
c) Para calcular el costo en dólares.
d) Para medir la altura total del prisma.
```

```ad-question
title: Pregunta 3
Si un prisma tiene un volumen de $10 \, m^3$ y el costo de almacenamiento es de $3.00 USD por cada unidad cúbica, ¿cuál es el costo total?
a) $3.33 USD
b) $30.00 USD
c) $13.00 USD
d) $30.00 \, m^3$
```

---

### Notas Finales y Navegación
¡Excelente trabajo! Hoy aprendiste que el volumen no es más que "capas" de área acumuladas una sobre otra hasta alcanzar una altura. Dominar el prisma triangular es el paso más difícil; una vez que entiendes que solo cambia la fórmula de la base ($A_b$), podrás calcular el volumen de cualquier figura. En la próxima clase, aplicaremos esta misma "Regla de Oro" a prismas con bases de muchos más lados.

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [Clase 01 — Introducción a los Prismas](link_clase_01) | ➡️ **Siguiente:** [Clase 03 — Prismas con otras bases](link_clase_03)