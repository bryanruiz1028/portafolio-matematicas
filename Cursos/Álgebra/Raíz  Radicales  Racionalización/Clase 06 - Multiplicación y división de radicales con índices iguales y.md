# Clase 06 — Multiplicación y división de radicales con índices iguales y diferentes

tags: #algebra #multiplicacion #division #radicales
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 6 de 14

### 1. Bloque de Navegación Superior
> [!info] 🧭 Navegación
> [[Clase 05 — Suma y resta de radicales]] | [[00 - Índice del curso]] | **[[Clase 06 — Multiplicación y división de radicales]]** | [[Clase 07 — Racionalización de denominadores]]

---

### 2. Importancia y Aplicaciones
> [!info] ¿Por qué es importante esta clase?
> En el álgebra y en la vida real, no siempre operamos con las mismas escalas. Aprender a manejar radicales con índices diferentes nos permite unificar medidas y comparar magnitudes que, a simple vista, parecen incompatibles.
> 
> - 💵 **Aplicación USD:** Se utiliza en finanzas para calcular el costo unitario de activos o tasas de depreciación cuando los periodos de tiempo se expresan en diferentes raíces temporales.
> - 🏗️ **Aplicación práctica:** Es vital en el diseño estructural y arquitectura para calcular áreas y resistencia de materiales donde las dimensiones escalan de forma no lineal.
> - 📊 **Situación cotidiana:** Permite comparar escalas de crecimiento poblacional o biológico que operan bajo ritmos de progresión distintos.

---

### 3. Marco Conceptual

**Concepto clave:**
Operar con radicales de diferentes índices es como intentar sumar monedas de distintos países; primero debemos convertirlas a una "moneda común". Para multiplicar o dividir raíces, es obligatorio que el **índice** (el número pequeño sobre la raíz) sea igual. Si son diferentes, usamos el Mínimo Común Múltiplo (MCM) para homogenizarlos.

> [!warning] Error común
> **Jamás** multipliques o dividas los números de adentro (radicandos) si los índices son distintos. 
> ❌ $\sqrt[3]{10} / \sqrt{2} \neq \sqrt[3]{5}$
> ✅ Primero debes igualar los índices mediante el MCM y luego realizar la operación.

> [!tip] La Metáfora de la Cárcel
> Imagina que la raíz es una **cárcel**. El índice representa los **años de condena** (sentencia del juez) que debe cumplir un número para poder salir a la libertad. Si el índice es 3, cualquier número o letra adentro necesita un exponente de 3 para ser liberado. Si tiene más (ej. exponente 5), cumple sus 3 años, sale una unidad a la calle, y el resto (2 años) se queda adentro cumpliendo el resto de su estancia.

---

### 4. Procedimiento Universal (Paso a Paso)

```text
PASO 1: Factorización de coeficientes.
        Convierte los números grandes en potencias de números primos 
        (ejemplo: 25 -> 5²; 81 -> 3⁴).
PASO 2: Obtención del Mínimo Común Múltiplo (MCM).
        Calcula el MCM de todos los índices de las raíces involucradas.
PASO 3: Amplificación de la raíz.
        Multiplica el índice y TODOS los exponentes internos por el factor 
        necesario para alcanzar el MCM.
PASO 4: Operación y simplificación.
        Suma exponentes (multiplicación) o réstalos (división). 
        Para "salir de la cárcel", divide tus años (exponente) entre 
        la condena (índice); el cociente sale y el residuo se queda.
```

---

### 5. Sección de Ejemplos Guiados

> [!example] Ejemplo 1: División mismo índice (Básico)
> **Problema:** Dividir $\frac{\sqrt[3]{81x^7}}{\sqrt[3]{3x^2}}$
> 1. **Unificar:** Como los índices son iguales (3), ponemos todo en una sola "cárcel": $\sqrt[3]{\frac{81x^7}{3x^2}}$.
> 2. **Dividir:** $81 \div 3 = 27$. Restamos exponentes de las letras: $x^{7-2} = x^5$. Obtenemos $\sqrt[3]{27x^5}$.
> 3. **Factorizar:** $27 = 3^3$. Así que tenemos $\sqrt[3]{3^3 x^5}$.
> 4. **Extraer:** El $3^3$ cumple sus 3 años exactos y sale. La $x^5$ tiene años de sobra: cumple 3 (sale una $x$) y le sobran 2 que se quedan adentro.
> **Resultado:** $3x \sqrt[3]{x^2}$

> [!example] Ejemplo 2: Coeficientes fuera de la raíz
> **Problema:** $\frac{\sqrt{75x^2y^3}}{5\sqrt{3xy^2}}$
> 1. **Organizar:** El $1/5$ se queda afuera. Metemos lo demás en la raíz cuadrada: $\frac{1}{5} \sqrt{\frac{75x^2y^3}{3xy^2}}$.
> 2. **Operar:** $75 \div 3 = 25$. Restamos exponentes: $x^{2-1} = x^1$, $y^{3-2} = y^1$.
> 3. **Simplificar:** $25 = 5^2$. La raíz queda $\frac{1}{5} \sqrt{5^2xy}$.
> 4. **Eliminar:** El $5^2$ sale de la cárcel como $5$. Al multiplicarse por el $1/5$ que esperaba afuera, se cancelan ($5/5 = 1$).
> **Resultado:** $\sqrt{xy}$

> [!example] Ejemplo 3: Índices Diferentes (Avanzado)
> **Problema:** Dividir $\frac{\sqrt[4]{9m^5}}{\sqrt[3]{3m^2}}$
> 1. **Factorizar:** El 9 se convierte en $3^2$. Tenemos $\frac{\sqrt[4]{3^2m^5}}{\sqrt[3]{3m^2}}$.
> 2. **MCM:** El juez dicta una nueva condena común. El MCM de 4 y 3 es **12**.
> 3. **Amplificar:** 
>    - Arriba (x3): $\sqrt[12]{3^6m^{15}}$
>    - Abajo (x4): $\sqrt[12]{3^4m^8}$
> 4. **Operar:** $\sqrt[12]{\frac{3^6m^{15}}{3^4m^8}} = \sqrt[12]{3^{6-4}m^{15-8}} = \sqrt[12]{3^2m^7}$.
> 5. **Finalizar:** Revertimos el paso 1 ($3^2 = 9$). Como nadie tiene 12 años o más, nadie sale de esta cárcel.
> **Resultado:** $\sqrt[12]{9m^7}$

> [!example] Ejemplo 4: Aplicación Real USD
> **Problema:** El ingreso total de una importación es $\sqrt[4]{x^9}$ dólares por un lote de $\sqrt[6]{x^2}$ productos. ¿Cuál es el precio unitario?
> 1. **Planteamiento:** Se requiere una división: $\frac{\sqrt[4]{x^9}}{\sqrt[6]{x^2}}$.
> 2. **MCM:** El MCM de 4 y 6 es **12**.
> 3. **Amplificar:** 
>    - Ingreso (x3): $\sqrt[12]{x^{27}}$
>    - Cantidad (x2): $\sqrt[12]{x^4}$
> 4. **Operar:** $\sqrt[12]{x^{27-4}} = \sqrt[12]{x^{23}}$.
> 5. **Extraer de la cárcel:** La condena es de 12 años. Como la $x$ tiene 23 años, dividimos: $23 \div 12 = 1$ y sobran $11$. Sale una $x$ y se quedan $x^{11}$.
> **Resultado:** $x \sqrt[12]{x^{11}}$ dólares por unidad. *Esta simplificación permite al importador proyectar costos de forma lineal según el volumen $x$.*

---

### 6. Práctica Independiente

> [!abstract] Ejercicios de aplicación
> **Verde (Fácil - Mismo Índice):**
> 1. $\sqrt{x^5} / \sqrt{x^3}$
> 2. $\sqrt[3]{54a^8} / \sqrt[3]{2a^2}$
> 3. $\sqrt[4]{x^{10}y^5} / \sqrt[4]{x^2y}$
> 4. $\sqrt[5]{m^{12}} / \sqrt[5]{m^2}$
> 
> **Amarillo (Medio - Índices Mixtos):**
> 1. $\sqrt{x} \cdot \sqrt[3]{x}$
> 2. $\sqrt[4]{3a^3} / \sqrt[2]{3a}$
> 3. $\sqrt[3]{2} \cdot \sqrt[4]{2}$
> 4. $\sqrt[3]{x^2} / \sqrt[6]{x}$
> 
> **Rojo (Avanzado - Aplicación USD):**
> 1. Si el ingreso total por $x$ unidades vendidas es $\sqrt[3]{27x^7}$ USD, ¿cuál es el ingreso por unidad?
> 2. Determine el factor de depreciación de un activo valuado en $\sqrt[4]{16x^{13}}$ dividido por su tiempo de vida útil $\sqrt{x}$.

> [!success] Solucionario (Para el docente)
> **Verde:** 1. $x$ | 2. $3a^2$ | 3. $x^2 y$ | 4. $m^2$
> **Amarillo:** 1. $\sqrt[6]{x^5}$ | 2. $\sqrt[4]{a/3}$ | 3. $\sqrt[12]{2^7}$ | 4. $\sqrt[6]{x^3}$ o $\sqrt{x}$
> **Rojo:** 1. $3x^2$ (Se extraen todos los factores de la cárcel) | 2. $2x^2 \sqrt[4]{x}$ (Extrayendo términos con exponente $\geq 4$)

---

### 7. Evaluación y Cierre

> [!question] Mini-prueba de autoevaluación
> 1. **En la división de radicales, ¿qué operación realizamos con los exponentes de las letras iguales?**
>    - a) Se suman.
>    - b) Se restan.
>    - c) Se multiplican.
> 2. **Si tienes una raíz con índice 4 y otra con índice 6, ¿cuál es el nuevo índice común (MCM)?**
>    - a) 24
>    - b) 10
>    - c) 12
> 3. **Si un presupuesto de $\sqrt[3]{x^4}$ USD se reparte equitativamente entre $\sqrt[3]{x}$ departamentos, ¿cuánto recibe cada uno?**
>    - a) $x$
>    - b) $\sqrt[3]{x^5}$
>    - c) $x^3$

> [!tip] Siguiente Paso
> ¡Excelente trabajo! Ahora que dominas la homogenización de índices, estamos listos para la **Racionalización**. Aprenderemos a "limpiar" nuestras fracciones eliminando las raíces del denominador para que tus informes financieros luzcan impecables.

---
> [!info] 🧭 Navegación
> [[Clase 05 — Suma y resta de radicales]] | [[00 - Índice del curso]] | **[[Clase 06 — Multiplicación y división de radicales]]** | [[Clase 07 — Racionalización de denominadores]]