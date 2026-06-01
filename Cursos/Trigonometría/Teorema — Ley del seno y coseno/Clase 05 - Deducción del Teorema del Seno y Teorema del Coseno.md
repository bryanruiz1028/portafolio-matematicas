# Clase 05 — Deducción del Teorema del Seno y Teorema del Coseno
tags: #algebra #deducciondelteoremadelseno #trigonometria #teoremacosento
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 5 de 9

> [!info] 🧭 Navegación
> [[Clase 04|⬅ Clase 04]] | [[00 - Índice del curso|Índice]] | **Clase 05** | | [[Clase 06|Clase 06 ➡]]

> [!info] 🌍 Relevancia y aplicaciones
> El estudio de los triángulos oblicuángulos (aquellos que no poseen un ángulo recto) es fundamental porque la mayoría de las estructuras y distancias en el mundo real no forman ángulos perfectos de $90^\circ$. El Teorema del Seno y el Teorema del Coseno son las herramientas matemáticas que permiten resolver situaciones donde el Teorema de Pitágoras no tiene alcance.
> 
> *   💵 **Cálculo de costos ($USD):** Permite determinar con precisión la longitud de materiales necesarios (como vigas de acero o cercas perimetrales) para terrenos triangulares irregulares, facilitando presupuestos exactos basados en el precio por metro lineal.
> *   🏗️ **Ingeniería y Arquitectura:** Esencial para calcular tensiones en cables de puentes, ángulos de inclinación en techos y longitudes de soportes en estructuras no rectangulares.
> *   📊 **Situaciones cotidianas:** Se utiliza en la navegación marítima y aérea para calcular distancias entre puertos o aeropuertos cuando se conoce la posición de puntos de referencia intermedios.

---

### 2. CONCEPTO CLAVE: DEDUCCIÓN DEL TEOREMA DEL SENO

> [!note] 📌 ¿Qué es la deducción del teorema del seno?
> Imagina que quieres descubrir por qué las fórmulas que usamos funcionan siempre. La **deducción** es el proceso de demostración. Para un estudiante de 12 años, esto es como "partir" un triángulo cualquiera a la mitad trazando una línea recta hacia abajo (llamada altura $X$). Esta altura $X$ funciona como un **puente o vínculo común** que conecta los dos lados del triángulo. Al aplicar las reglas básicas del seno en ambos lados y despejar esa altura común, descubrimos que los lados y sus ángulos opuestos siempre guardan la misma proporción.

> [!warning] ⚠️ Error común
> Un error crítico es intentar usar el Teorema del Seno sin tener una "pareja completa". Para que este teorema funcione, necesitas conocer un ángulo y su lado opuesto. Si solo tienes los tres lados, o dos lados y el ángulo que ellos forman, no tienes una "pareja" y debes iniciar obligatoriamente con el Teorema del Coseno.

> [!tip] 💡 Truco para recordarlo
> La correspondencia es siempre **Mayúscula/Minúscula**. Los ángulos se nombran con letras mayúsculas ($A, B, C$) y sus lados opuestos llevan la misma letra en minúscula ($a, b, c$). Siempre que pienses en el ángulo $A$, visualiza una flecha que apunta directamente al lado $a$.

---

### 3. PROCEDIMIENTO PASO A PASO

Para aplicar correctamente el Teorema del Coseno siguiendo la metodología académica del "Profe Alex", siga estos cuatro pasos fundamentales. **Nota crítica:** Asegúrese de que su calculadora esté siempre en modo **Degrees (D)**; de lo contrario, los resultados angulares serán erróneos.

```text
1. NOMBRAR: Asigne letras mayúsculas (A, B, C) a los ángulos y minúsculas (a, b, c) a los lados opuestos.
2. IDENTIFICAR: Determine si el caso es SSS (Lado-Lado-Lado) o SAS (Lado-Ángulo-Lado, es decir, dos lados y el ángulo entre ellos).
3. ELEGIR FÓRMULA: Seleccione la variante del teorema que despeje su incógnita. 
   - Para un lado: a² = b² + c² - 2bc · cos(A)
   - Para un ángulo: A = arccos((a² - b² - c²) / (-2bc))
4. CALCULAR: Sustituya los valores y opere con precisión decimal.
```

---

### 4. EJEMPLOS PRÁCTICOS

```ad-example
title: Ejemplo 1: Demostración Formal del Teorema del Seno
**Objetivo:** Demostrar que $\frac{b}{\sin(B)} = \frac{c}{\sin(C)}$ usando la altura $X$ como vínculo.

**Paso 1:** En un triángulo oblicuángulo, trazamos la altura $X$ desde el vértice $A$ hacia el lado $a$, dividiéndolo en dos triángulos rectángulos.
**Paso 2:** En el triángulo rectángulo de la izquierda:
$\sin(C) = \frac{X}{b} \implies X = b \cdot \sin(C)$
**Paso 3:** En el triángulo rectángulo de la derecha:
$\sin(B) = \frac{X}{c} \implies X = c \cdot \sin(B)$
**Paso 4 (Conclusión):** Como $X$ es el **vínculo común** en ambas ecuaciones, igualamos:
$b \cdot \sin(C) = c \cdot \sin(B)$
Al reordenar los términos, obtenemos la proporción fundamental:
$\frac{b}{\sin(B)} = \frac{c}{\sin(C)}$
```

```ad-example
title: Ejemplo 2: Cálculo de un Ángulo (Caso SSS)
**Datos:** Lados $a = 13\text{ m}$, $b = 15\text{ m}$ y $c = 6\text{ m}$. Hallar el ángulo $A$.

1. **Fórmula:** $A = \arccos\left(\frac{a^2 - b^2 - c^2}{-2bc}\right)$
2. **Sustitución:** $A = \arccos\left(\frac{13^2 - 15^2 - 6^2}{-2 \cdot 15 \cdot 6}\right)$
3. **Operación:** $A = \arccos\left(\frac{169 - 225 - 36}{-180}\right) = \arccos\left(\frac{-92}{-180}\right)$
4. **Resultado:** $A = 59,262^\circ$
```

```ad-example
title: Ejemplo 3: Resolución Completa (Caso SAS)
**Datos:** Lado $b = 8\text{ cm}$, Lado $c = 11\text{ cm}$, Ángulo $A = 105^\circ$.

1. **Hallar lado $a$:**
   $a = \sqrt{8^2 + 11^2 - 2(8)(11)\cos(105^\circ)}$
   $a = \sqrt{64 + 121 - 176(-0,2588)}$
   $a = 15,184\text{ cm}$
2. **Hallar ángulo $B$:**
   $B = \arccos\left(\frac{8^2 - 15,184^2 - 11^2}{-2 \cdot 15,184 \cdot 11}\right)$
   $B = 30,592^\circ$
3. **Hallar ángulo $C$:**
   $C = 180^\circ - 105^\circ - 30,592^\circ = 44,408^\circ$
```

```ad-example
title: Ejemplo 4: Aplicación Presupuestaria ($USD)
Se desea cercar el terreno del Ejemplo 2 (lados de $13\text{ m}, 15\text{ m}$ y $6\text{ m}$). Si el costo del metro lineal de cerca es de $50\text{ USD}$, ¿cuál es el presupuesto total?

1. **Perímetro:** $13\text{ m} + 15\text{ m} + 6\text{ m} = 34\text{ m}$.
2. **Presupuesto:** $34\text{ m} \cdot 50\text{ USD/m} = 1.700\text{ USD}$.
```

---

### 5. EJERCICIOS DE PRÁCTICA

```ad-abstract
title: Ejercicios de Aplicación
**Nivel Fácil: Identificación y Conceptos**
1. Si conoces los tres lados ($SSS$), ¿qué teorema es obligatorio usar primero?
2. Escriba la fórmula del Teorema del Seno que relaciona el lado $a$ con el lado $b$.
3. En un triángulo $MNP$, ¿cuál es el nombre del lado opuesto al ángulo $M$?
4. Si un ángulo mide $90^\circ$, ¿es necesario el Teorema del Coseno o basta con Pitágoras?

**Nivel Medio: Cálculos Geométricos**
5. Calcule el lado $a$ si $b = 6, c = 10$ y $A = 82^\circ$.
6. Calcule el ángulo $B$ si $a = 20, b = 12$ y $c = 10$.
7. Si en un triángulo $A = 105^\circ$ y $B = 30,592^\circ$, ¿cuánto mide el ángulo $C$?
8. ¿Puede usarse el Teorema del Seno si solo se conocen los lados $a, b, c$? Justifique.

**Nivel Avanzado: Aplicaciones Financieras ($USD)**
9. Un jardín triangular tiene lados de $10\text{ m}, 12\text{ m}$ y $6\text{ m}$. El costo de bordearlo es $15\text{ USD}$ por metro. ¿Costo total?
10. Se requiere una viga (lado $a$) para una estructura donde $b = 8\text{ m}, c = 11\text{ m}$ y $A = 105^\circ$. El costo es $120\text{ USD/m}$. ¿Costo de la viga?
11. Un terreno tiene lados $13\text{ m}, 15\text{ m}$ y $6\text{ m}$. Se paga $20\text{ USD}$ por cada grado del ángulo más pequeño. ¿Cuánto se paga?
12. Calcule el costo de materiales para un marco que incluya el lado del Ej. 5 y el perímetro del triángulo del Ej. 6, a un costo de $45\text{ USD/m}$.
```

```ad-success
title: Respuestas del Docente
1. **Teorema del Coseno**.
2. $\frac{a}{\sin(A)} = \frac{b}{\sin(B)}$.
3. **Lado $m$**.
4. Basta con **Pitágoras** (es más eficiente).
5. $a = 10,922$.
6. $B = 32,859^\circ$.
7. $C = 44,408^\circ$.
8. **No**, porque no se tiene ninguna "pareja" (ángulo conocido con su lado opuesto).
9. $28\text{ m} \cdot 15 = 420\text{ USD}$.
10. $15,184\text{ m} \cdot 120 = 1.822,08\text{ USD}$.
11. El lado más corto es $6\text{ m}$, por lo que el ángulo opuesto es el menor ($C = 23,3^\circ$). Pago: $23,3 \cdot 20 = 466\text{ USD}$.
12. Lado Ej 5 ($10,922$) + Perímetro Ej 6 ($20+12+10 = 42$) = $52,922\text{ m}$. Costo: $52,922 \cdot 45 = 2.381,49\text{ USD}$.
```

---

### 6. AUTOEVALUACIÓN

```ad-question
title: 1. Configuración Técnica
**¿En qué modo debe estar configurada la calculadora para estos cálculos?**
A) Radianes (R)
B) Gradiantes (G)
C) Degrees (D)

*Respuesta correcta: **C**. El modo "Degrees" asegura que la calculadora interprete los valores en grados sexagesimales.*
```

```ad-question
title: 2. Propiedad de Suplementarios
**¿Cuál de las siguientes igualdades es fundamental para la deducción en triángulos obtusángulos?**
A) $\sin(180 - y) = \cos(y)$
B) $\sin(180 - y) = \sin(y)$
C) $\sin(180 - y) = -\sin(y)$

*Respuesta correcta: **B**. El seno de un ángulo es igual al seno de su suplementario, lo cual permite que el teorema sea universal para cualquier triángulo.*
```

```ad-question
title: 3. Aplicabilidad
**¿Cuál es el criterio para iniciar la resolución mediante el Teorema del Coseno?**
A) Conocer una pareja ángulo-lado opuesto.
B) Conocer los tres ángulos del triángulo.
C) Conocer los tres lados (SSS) o dos lados y el ángulo comprendido (SAS).

*Respuesta correcta: **C**.*
```

---

### 7. CIERRE Y CONEXIÓN

> [!tip] 💡 En la próxima clase
> Tras dominar la deducción y los casos básicos de aplicación de los Teoremas del Seno y Coseno, estamos listos para integrar estas leyes. En la **Clase 06**, resolveremos problemas complejos que requieren el uso combinado de ambas herramientas en un solo ejercicio.

> [!info] 🧭 Navegación
> [[Clase 04|⬅ Clase 04]] | [[00 - Índice del curso|Índice]] | **Clase 05** | | [[Clase 06|Clase 06 ➡]]