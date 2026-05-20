# 📖 Guía de estudio — Clase 02: Sistemas de Ecuaciones Lineales 2x2

> [!info] 📌 Conceptos clave
> Un sistema de ecuaciones $2 \times 2$ tiene como objetivo hallar los valores de las incógnitas ($x$ y $y$) que hacen que ambas igualdades sean ciertas al mismo tiempo. Para resolverlos con éxito, el **"Profe Alex"** resalta que el **Paso $1$** siempre debe ser **organizar las ecuaciones**: los términos con las letras deben estar alineados ($x$ bajo $x$, $y$ bajo $y$) y los números independientes al otro lado del signo igual ($=$). Aunque existen tres métodos principales —**Reducción**, **Sustitución** e **Igualación**—, recuerda que todos son caminos distintos para llegar exactamente al mismo resultado.

## Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Sistema de Ecuaciones 2x2** | Conjunto de dos ecuaciones lineales con dos incógnitas comunes. |
| **Método de Reducción** | Técnica para igualar coeficientes con signos opuestos y sumar las ecuaciones para eliminar una variable. |
| **Método de Sustitución** | Técnica de despejar una incógnita en una ecuación y reemplazar su expresión en la otra. |
| **Método de Igualación** | Técnica de despejar la misma incógnita en ambas ecuaciones para igualar sus resultados. |

---

## Ejemplos Resueltos Adicionales

````ad-example
**Ejemplo A — Método de Reducción**
**Problema:** Resolver el sistema:
$1)$ $x - 2y = -4$
$2)$ $3x + y = 9$

**Pasos:**
1. **Igualar coeficientes:** Queremos eliminar la $y$. En $(1)$ tenemos $-2y$. Multiplicamos la ecuación $(2)$ por $2$ para obtener $+2y$.
   - Ecuación $2$ modificada: $2(3x + y = 9) \rightarrow 6x + 2y = 18$.
2. **Sumar para eliminar:** Sumamos la ecuación $(1)$ con la nueva ecuación $(2)$:
   $(x - 2y) + (6x + 2y) = -4 + 18$
   $7x = 14$
3. **Resolver:** $x = 14 / 7 \rightarrow$ **$x = 2$**.
4. **Sustituir:** Reemplazamos $x = 2$ en la ecuación original $(2)$:
   $3(2) + y = 9 \rightarrow 6 + y = 9 \rightarrow y = 9 - 6 \rightarrow$ **$y = 3$**.

**Resultado:** $x = 2, y = 3$ ✅

> [!tip] ✅ Tip de Verificación
> Siempre comprueba tu resultado sustituyendo ambos valores en las ecuaciones originales. 
> Para $(1)$: $2 - 2(3) = 2 - 6 = -4$ (¡Correcto!). 
> Para $(2)$: $3(2) + 3 = 6 + 3 = 9$ (¡Correcto!).
````

````ad-example
**Ejemplo B — Aplicación con Costos**
**Problema:** En una cafetería, el costo de $2$ jugos ($x$) y $5$ empanadas ($y$) es de **$12$ USD**. Si se compran $3$ jugos y $2$ empanadas, el costo es de **$7$ USD**. ¿Cuál es el precio de cada artículo?

**Pasos (Sustitución):**
$1)$ $2x + 5y = 12$
$2)$ $3x + 2y = 7$

1. **Despejar:** Despejamos $x$ en la ecuación $(1)$:
   $2x = 12 - 5y \rightarrow x = \frac{12 - 5y}{2}$
2. **Sustituir:** Reemplazamos $x$ en la ecuación $(2)$:
   $3(\frac{12 - 5y}{2}) + 2y = 7$
3. **Eliminar denominador:** Para facilitar el cálculo, multiplicamos **toda** la ecuación por $2$ (el denominador que queremos eliminar):
   $3(12 - 5y) + 2(2y) = 2(7)$
   $36 - 15y + 4y = 14$
4. **Resolver para $y$:**
   $-11y = 14 - 36 \rightarrow -11y = -22 \rightarrow y = \frac{-22}{-11} \rightarrow$ **$y = 2$**.
5. **Hallar $x$:** Usamos el despeje del paso $1$:
   $x = \frac{12 - 5(2)}{2} = \frac{12 - 10}{2} = \frac{2}{2} \rightarrow$ **$x = 1$**.

**Resultado:** Jugo = $1 USD, Empanada = $2 USD ✅
````

---

## Ejercicios de Repaso

````ad-abstract
**🟢 Fácil**
Resuelve los siguientes sistemas (se recomienda Reducción). **Recordatorio:** Verifica que estén ordenados ($x, y, =$).
1.  $x + y = 10$
    $x - y = 2$
2.  $2x + 3y = 7$
    $5x - 3y = 7$
3.  $4x + y = 14$
    $x - y = 1$
````

````ad-abstract
**🟡 Medio**
Resuelve aplicando Sustitución o Igualación:
1.  $x + 5y = 7$
    $3x + 2y = 8$
2.  $3x + 2y = 14$
    $2x + y = 8$
3.  $x + 2y = 7$
    $2x + 3y = 12$
````

````ad-abstract
**🔴 Avanzado — Aplicación con $USD**
**Problema:** Un comerciante compra suministros. Plantea y resuelve el siguiente sistema utilizando la táctica del **Mínimo Común Múltiplo (MCM)** para los coeficientes:
*   La compra de $9$ paquetes de galletas ($x$) y $11$ botellas de agua ($y$) suma **$67$ USD**.
*   La compra de $6$ paquetes de galletas ($x$) y $5$ botellas de agua ($y$) suma **$33$ USD**.

**Táctica del Profesor:** Para eliminar $x$, busca el **MCM de $9$ y $6$**, que es **$18$**. Multiplica la primera ecuación por $2$ y la segunda por $-3$ para obtener coeficientes opuestos ($18$ y $-18$).
````

---

> [!tip] 💡 Consejo de estudio
> Al usar los métodos de sustitución o igualación, observa detenidamente las ecuaciones. Prioriza siempre despejar las incógnitas que tengan **coeficiente $1$** (que estén "solas") y que sean **positivas**. Esto te permitirá evitar trabajar con fracciones complejas desde el inicio y reducirá drásticamente tus errores con los signos. ¡El orden es tu mejor aliado en el álgebra!