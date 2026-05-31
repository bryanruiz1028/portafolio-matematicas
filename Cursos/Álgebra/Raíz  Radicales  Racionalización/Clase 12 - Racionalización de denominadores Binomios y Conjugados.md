# Clase 12 — Racionalización de denominadores: Binomios y Conjugados

#algebra #rationalization

> [!info] 🧭 Navegación
> - [Anterior: Clase 11 — Introducción a las Raíces](clase-11)
> - [Siguiente: Clase 13 — Operaciones Combinadas con Racionalización](clase-13)
> - [Índice General: Álgebra Básica](indice-algebra)

---

¡Qué tal, amigos! Espero que estén muy bien. Bienvenidos al curso de racionalización. Hoy vamos a aprender a "limpiar" nuestras fracciones cuando tienen raíces en el denominador, especialmente cuando nos encontramos con dos términos (binomios).

## RELEVANCIA Y APLICACIONES

La racionalización es el proceso de eliminar las raíces del denominador. Esto no cambia el valor de la fracción, sino que la escribe de una forma más elegante y estándar, lo cual es vital para:

*   💵 **[Aplicación con USD]:** Calcular tasas de interés compuestas o precios unitarios con precisión cuando el denominador es una raíz.
*   🏗️ **[Ingeniería Civil]:** Distribuir cargas en estructuras triangulares donde las longitudes suelen ser valores irracionales.
*   📊 **[Situación Cotidiana]:** Ajustar presupuestos en materiales de construcción (como láminas de vidrio o madera) con dimensiones expresadas en raíces.

---

## CONCEPTO CLAVE

> [!note] **¿Qué es racionalizar? (Para todos)**
> Imagina que racionalizar es como "ordenar" la parte de abajo de tu fracción. Si tienes una raíz ahí, multiplicamos arriba y abajo por un número especial para que la raíz desaparezca y se convierta en un número "normal" (entero).

> [!warning] **¡Pilas con este error!**
> Un error muy común es intentar racionalizar un binomio (como $\sqrt{3} + 5$) multiplicando solo por la raíz ($\sqrt{3}$). ¡Cuidado! Eso no elimina la raíz. Para binomios, siempre, siempre debemos usar el **conjugado**.

> [!tip] **El Truco del Conjugado**
> El conjugado es el "gemelo opuesto" de tu denominador:
> - Si tienes una suma $(a + b)$, su conjugado es la resta $(a - b)$.
> - Si tienes una resta $(a - b)$, su conjugado es la suma $(a + b)$.
> Al multiplicarlos, aplicamos un producto notable llamado "diferencia de cuadrados": $(a+b)(a-b) = a^2 - b^2$. ¡Esto elimina cualquier raíz cuadrada!

---

## PROCEDIMIENTO PASO A PASO

```text
PASO 1 → Identificar si el denominador es un monomio o un binomio.
PASO 2 → Determinar el factor multiplicador:
         - Para monomios (√[n]a^m): Buscar cuánto le falta al exponente 'm' para ser igual al índice 'n'.
         - Para binomios: Hallar el conjugado (cambiar el signo del centro).
PASO 3 → Multiplicar tanto el numerador como el denominador por ese factor.
PASO 4 → Simplificar. En binomios, usar (a² - b²) para eliminar las raíces y reducir términos.
```

---

## BLOQUES DE EJEMPLOS PRÁCTICOS

### Ejemplo 1: Caso Básico (Monomio)
Racionalizar: $\frac{5}{\sqrt{3}}$
1. Multiplicamos por $\frac{\sqrt{3}}{\sqrt{3}}$ (porque el índice es 2 y al exponente 1 le falta 1 para llegar a 2).
2. Numerador: $5 \cdot \sqrt{3} = 5\sqrt{3}$.
3. Denominador: $\sqrt{3} \cdot \sqrt{3} = (\sqrt{3})^2 = 3$.
**Resultado:** $\frac{5\sqrt{3}}{3}$

### Ejemplo 2: Caso con Signos (Binomio)
Racionalizar: $\frac{\sqrt{2}}{\sqrt{3} + \sqrt{5}}$
1. El conjugado es $(\sqrt{3} - \sqrt{5})$.
2. Numerador: $\sqrt{2}(\sqrt{3} - \sqrt{5}) = \sqrt{6} - \sqrt{10}$.
3. Denominador: Aplicamos $(a^2 - b^2) \rightarrow (\sqrt{3})^2 - (\sqrt{5})^2 = 3 - 5 = -2$.
**Resultado:** $\frac{\sqrt{6} - \sqrt{10}}{-2}$

### Ejemplo 3: Caso Avanzado (Variables)
Racionalizar: $\frac{\sqrt{x}}{3 - \sqrt{x}}$
1. El conjugado es $(3 + \sqrt{x})$.
2. Numerador: $\sqrt{x}(3 + \sqrt{x}) = 3\sqrt{x} + (\sqrt{x})^2 = 3\sqrt{x} + x$.
3. Denominador: $3^2 - (\sqrt{x})^2 = 9 - x$.
**Resultado:** $\frac{3\sqrt{x} + x}{9 - x}$

### Ejemplo 4: Aplicación USD
**Problema:** Un material cuesta $30$ USD y su área es $(\sqrt{3} + 1)$ metros. ¿Cuál es el precio por metro cuadrado?
1. Planteamos: $\frac{30}{\sqrt{3} + 1}$.
2. Conjugado: $(\sqrt{3} - 1)$.
3. Operación: $\frac{30(\sqrt{3} - 1)}{(\sqrt{3})^2 - 1^2} = \frac{30(\sqrt{3} - 1)}{3 - 1} = \frac{30(\sqrt{3} - 1)}{2}$.
**Resultado:** $15(\sqrt{3} - 1)$ USD por $m^2$.

---

## EJERCICIOS PARA EL ESTUDIANTE

### 🟢 Nivel Fácil (Monomios)
1. $\frac{2}{\sqrt{3}}$
2. $\frac{5}{\sqrt[3]{x}}$
3. $\frac{6}{\sqrt[3]{2^2}}$
4. $\frac{10}{\sqrt[5]{x^2}}$

### 🟡 Nivel Medio (Binomios)
1. $\frac{3\sqrt{2}}{3\sqrt{2} - 4}$
2. $\frac{5}{\sqrt{x} - 2}$
3. $\frac{\sqrt{3}}{\sqrt{3} + \sqrt{2}}$
4. $\frac{1}{\sqrt{2} - 1}$

### 🔴 Nivel Avanzado (Situaciones USD)
1. Dividir un bono de $100$ USD entre $(\sqrt{5} - \sqrt{2})$ empleados.
2. Calcular el costo de una cerca con un presupuesto de $50$ USD para un largo de $(\sqrt{3} + 2)$ metros.
3. Repartir un premio de $200$ USD proporcional a una inversión de $(4 - \sqrt{6})$ unidades.
4. Ajustar una factura de $120$ USD entre un grupo de $(\sqrt{7} + \sqrt{3})$ socios.

---

## RESPUESTAS PARA EL DOCENTE

> [!success] **Solucionario Detallado**
> **Fácil:**
> 1. $\frac{2\sqrt{3}}{3}$
> 2. $\frac{5\sqrt[3]{x^2}}{x}$ (Multiplicado por $\sqrt[3]{x^2}$)
> 3. $3\sqrt[3]{2}$ (Proceso: $\frac{6\sqrt[3]{2}}{2} = 3\sqrt[3]{2}$)
> 4. $\frac{10\sqrt[5]{x^3}}{x}$
>
> **Medio:**
> 1. $9 + 6\sqrt{2}$ (Denominador: $18 - 16 = 2$; Numerador simplificado con el 2)
> 2. $\frac{5(\sqrt{x} + 2)}{x - 4}$
> 3. $3 - \sqrt{6}$ (Denominador: $3 - 2 = 1$)
> 4. $\sqrt{2} + 1$
>
> **Avanzado:**
> 1. $\frac{100(\sqrt{5} + \sqrt{2})}{3}$ USD/empleado.
> 2. $50(2 - \sqrt{3})$ USD/metro. (Denominador: $4 - 3 = 1$)
> 3. $20(4 + \sqrt{6})$ USD. (Denominador: $16 - 6 = 10 \rightarrow 200/10 = 20$)
> 4. $30(\sqrt{7} - \sqrt{3})$ USD/socio. (Denominador: $7 - 3 = 4 \rightarrow 120/4 = 30$)

---

## AUTOEVALUACIÓN Y CIERRE

1.  **Pregunta 1:** ¿Cuál es el conjugado de $(a - b)$?
    *   *Respuesta:* Es $(a + b)$.
2.  **Pregunta 2:** ¿Qué resulta de elevar $(\sqrt{3})^2$?
    *   *Respuesta:* Resulta $3$, porque el exponente anula la raíz cuadrada.
3.  **Pregunta 3:** En finanzas, ¿qué ventaja tiene racionalizar el precio?
    *   *Respuesta:* Obtenemos una expresión equivalente pero mucho más sencilla de operar, sumar o comparar con otros valores monetarios.

> [!tip] **Notas Finales**
> ¡Excelente trabajo! Dominar el uso del conjugado es la llave maestra para el álgebra superior. No olviden que racionalizar es solo escribir lo mismo de una forma más útil. En la **Clase 13**, usaremos esto para resolver operaciones combinadas mucho más grandes. ¡Pilas y nos vemos en la próxima!

> [!info] 🧭 Navegación
> - [Anterior: Clase 11 — Introducción a las Raíces](clase-11)
> - [Siguiente: Clase 13 — Operaciones Combinadas con Racionalización](clase-13)
> - [Índice General: Álgebra Básica](indice-algebra)