# Clase 05 — Factorización de trinomios: Aspa Simple y Trinomio Cuadrado Perfecto
tags: #algebra #trinomialfactor
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 5 de 10

> [!info] 🧭 Navegación
> [[Clase 04|⬅ Clase 04]] | [[00 - Índice del curso|Índice]] | **Clase 05** | | [[Clase 06|Clase 06 ➡]]

> [!info] 🌍 Relevancia y aplicaciones
> La factorización de trinomios permite transformar expresiones complejas de segundo grado en productos simples, facilitando el análisis de sistemas en equilibrio y optimización de recursos.
> - 💵 **Aplicación en Finanzas:** Permite desglosar funciones de ingresos cuadráticos para hallar el precio unitario y la cantidad de productos en $USD.
> - 🏗️ **Aplicación Práctica:** En arquitectura, se utiliza para descomponer áreas superficiales en sus dimensiones lineales (largo y ancho) para la planificación de materiales.
> - 📊 **Situación Cotidiana:** Ayuda a simplificar el cálculo de presupuestos cuando el costo total depende de variables interconectadas, permitiendo una división exacta de los gastos.

> [!note] 📌 ¿Qué es la Factorización de trinomios?
> Factorizar un trinomio de la forma $ax^2 + bx + c$ es el proceso de "desarmar" un polinomio en dos binomios (paréntesis) que, al multiplicarse, regresan a la forma original. 
> 
> Existen dos casos fundamentales que estudiaremos hoy:
> 1. **Método de Aspa Simple:** Se usa cuando buscamos dos números que multiplicados den el extremo y cuya combinación cruzada nos dé el centro. Pedagógicamente, este método es simplemente la **operación inversa de la propiedad distributiva** (o FOIL). Al verificar el aspa, estamos comprobando que los términos internos y externos de la multiplicación sumen correctamente el término central.
> 2. **Trinomio Cuadrado Perfecto (TCP):** Es un caso especial donde el trinomio es el resultado de elevar un binomio al cuadrado. Se reconoce porque el término central es exactamente el doble producto de las raíces cuadradas de los extremos.
> 
> > [!warning] ⚠️ Error común
> > El error más grave es intentar factorizar sin **ordenar el trinomio**. Los términos deben estar en orden descendente según su exponente (ej. $x^2, x^1$, término independiente). Además, muchos estudiantes confunden el orden final: **el aspa se multiplica en diagonal para comprobar, pero los factores se agrupan de forma horizontal.**
> 
> > [!tip] 💡 Truco para recordarlo
> > Piensa en la **"X Mágica"**: Si las flechas cruzan para multiplicar, los brazos del signo igual deben ir rectos para agrupar. Si la suma de tu aspa no coincide con el signo o el número del centro, debes ajustar los signos de tus factores extremos.

### PROCEDIMIENTO PASO A PASO

#### Método de Aspa Simple
```text
PASO 1 → Ordenar el trinomio de mayor a menor exponente (ax² + bx + c).
PASO 2 → Descomponer los términos extremos (ax² y c) en dos factores cada uno.
PASO 3 → Multiplicar en diagonal (en aspa) y sumar los resultados.
PASO 4 → Verificar que la suma sea igual al término central (bx). 
         Si es correcto, agrupar los términos de forma HORIZONTAL en los paréntesis.
```

#### Método de Trinomio Cuadrado Perfecto (TCP)
```text
PASO 1 → Extraer la raíz cuadrada del primer y tercer término.
PASO 2 → Verificar el "Doble Producto": Multiplicar las dos raíces por 2.
PASO 3 → Si el resultado coincide con el término central, el factor es la suma 
         (o resta) de las raíces elevada al cuadrado: (r1 ± r2)².
```

---

### EJEMPLOS GUIADOS

> [!example] Ejemplo 1: Caso Básico ($x^2 + 7x + 10$)
> 1. **Descomponer extremos:** $x^2$ es $x \cdot x$; $10$ es $5 \cdot 2$.
> 2. **Multiplicar en aspa:** $x \cdot 2 = 2x$; $x \cdot 5 = 5x$.
> 3. **Verificar centro:** $5x + 2x = 7x$. ¡Coincide!
> 4. **Resultado (Agrupación horizontal):** $(x + 5)(x + 2)$.

> [!example] Ejemplo 2: Caso con Signos ($x^2 - 5x + 6$)
> Para que el producto sea $+6$ pero la suma sea negativa ($-5x$), ambos factores de $6$ deben ser negativos:
> 1. **Descomponer:** $x^2 = x \cdot x$; $6 = (-3) \cdot (-2)$.
> 2. **Verificar aspa:** $x \cdot (-2) = -2x$; $x \cdot (-3) = -3x$.
> 3. **Suma:** $-3x - 2x = -5x$. ¡Correcto!
> 4. **Resultado:** $(x - 3)(x - 2)$.

> [!example] Ejemplo 3: Caso Avanzado $ax^2$ ($2x^2 - 3x - 2$)
> 1. **Descomponer:** $2x^2 = 2x \cdot x$; $-2 = 1 \cdot (-2)$.
> 2. **Multiplicar en aspa:** $2x \cdot (-2) = -4x$; $x \cdot 1 = 1x$.
> 3. **Verificar centro:** $-4x + 1x = -3x$.
> 4. **Resultado (Horizontal):** $(2x + 1)(x - 2)$.

> [!example] Ejemplo 4: Aplicación Real en $USD$
> El ingreso total de una empresa está modelado por el área $3x^2 - 14x - 5$. Si sabemos que el largo representa la cantidad de productos vendidos y el ancho representa el precio unitario en $USD$:
> 1. **Factorizar:** Descomponemos $3x^2$ en $(3x)(x)$ y $-5$ en $(1)(-5)$.
> 2. **Verificar aspa:** $(3x \cdot -5) + (x \cdot 1) = -15x + 1x = -14x$.
> 3. **Interpretación:** Los factores son $(3x + 1)$ y $(x - 5)$.
> 4. **Conclusión:** Si la cantidad de productos es $(3x + 1)$, entonces el **Precio Unitario es $(x - 5)$ USD**.

---

### EJERCICIOS PARA EL ESTUDIANTE

> [!abstract] 🟢 Nivel Fácil (Coeficiente $a=1$)
> 1. $x^2 + 3x + 2$
> 2. $x^2 + 5x + 6$
> 3. $x^2 + 8x + 12$
> 4. $x^2 + 4x + 4$ (Pista: Intenta identificar si es TCP)

> [!abstract] 🟡 Nivel Medio (Mezcla de signos y $a > 1$)
> 1. $6x^2 + 7x + 2$
> 2. $x^2 - x - 6$
> 3. $8a^2 - 14a - 15$ (Resuelve usando el método de aspa).
> 4. $9m^2 - 6mn + n^2$ (Realiza la prueba del doble producto).

> [!abstract] 🔴 Nivel Avanzado (Aplicaciones $USD)
> 1. El ingreso de una tienda es $2a^2 + 7a + 3$ $USD$. Si se vendieron $(a + 3)$ unidades, ¿cuál es el precio unitario?
> 2. Factoriza $12x^2 - x - 6$ para hallar las dimensiones de una bodega.
> 3. Un terreno tiene un área de $15m^2 - 23m - 4$. Halla sus factores lineales.
> 4. Determina mediante la prueba del doble producto si $m^2 + 5m + 25$ es un Trinomio Cuadrado Perfecto.

> [!success] ✅ Respuestas
> **Fácil:** 1. $(x+2)(x+1)$ | 2. $(x+3)(x+2)$ | 3. $(x+6)(x+2)$ | 4. $(x+2)^2$ (Es TCP).
> **Medio:** 1. $(3x+2)(2x+1)$ | 2. $(x-3)(x+2)$ | 3. $(2a-5)(4a+3)$ | 4. $(3m-n)^2$ (Es TCP).
> **Avanzado:** 1. $(2a+1)$ $USD$ | 2. $(4x-3)(3x+2)$ | 3. $(3m-4)(5m+1)$ | 4. No es TCP (el doble producto debería ser $10m$, no $5m$).

---

### MINI-PRUEBA DE AUTOEVALUACIÓN

> [!question] Pregunta 1 (Conceptual)
> Para que un trinomio sea un **Cuadrado Perfecto**, ¿qué relación debe existir entre sus términos una vez extraídas las raíces de los extremos?
> - **Respuesta:** El término central debe ser exactamente el doble del producto de ambas raíces ($2 \cdot r_1 \cdot r_2$).

> [!question] Pregunta 2 (Procedimental)
> Al factorizar $x^2 - x - 6$, ¿por qué se eligen los números $-3$ y $+2$?
> - **Respuesta:** Porque su producto es $-6$ y su suma es $-1$, lo cual coincide con los coeficientes del trinomio. Al agrupar horizontalmente, obtenemos $(x - 3)(x + 2)$.

> [!question] Pregunta 3 (Aplicación $USD)
> Si el costo total de una producción es $3x^2 - 5x - 2$ $USD$ y un factor es $(x - 2)$, ¿cuál es el costo unitario?
> - **Respuesta:** $(3x + 1)$ $USD$. Se obtiene al descomponer $3x^2$ en $(3x)(x)$ y $-2$ en $(1)(-2)$, verificando que el aspa dé $-5x$.

---

> [!tip] 💡 En la próxima clase
> Hemos dominado los trinomios de segundo grado. En la **Clase 06**, subiremos la potencia para explorar la **Factorización de cubos y la Diferencia de cuadrados**.

> [!info] 🧭 Navegación
> [[Clase 04|⬅ Clase 04]] | [[00 - Índice del curso|Índice]] | **Clase 05** | | [[Clase 06|Clase 06 ➡]]