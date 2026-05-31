# 📖 Guía de estudio — Clase 12: Racionalización de denominadores

> [!info] 📌 Conceptos clave
> *   **Objetivo de la racionalización:** Es el proceso pedagógico y técnico que permite eliminar las raíces de los denominadores en una fracción para facilitar operaciones posteriores.
> *   **Regla fundamental de cancelación:** Para suprimir una raíz de forma efectiva, el índice de la misma y el exponente de la cantidad subradical deben ser exactamente iguales ($\sqrt[n]{a^n} = a$).
> *   **Estrategia de compensación:** Cuando el exponente es menor que el índice, debemos multiplicar por una expresión que complete "lo que le falta" al exponente para alcanzar el valor del índice.
> *   **Simplificación avanzada:** Como técnica de optimización, si el índice y el exponente de una raíz tienen un divisor común, se pueden simplificar antes o después del proceso (ej. $\sqrt[4]{3^2}$ puede simplificarse a $\sqrt{3}$).

## 2. TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Racionalización** | Procedimiento para quitar la raíz del denominador, permitiendo una expresión más limpia para el cálculo numérico. |
| **Índice y Exponente** | Relación matemática indispensable para liberar una cantidad de la raíz: deben igualarse mediante la multiplicación. |
| **Expresión Conjugada** | Binomio con el signo central opuesto. Si partimos de $(a + b)$, su conjugada es $(a - b)$. |
| **Producto de Conjugados** | $(a + b)(a - b) = a^2 - b^2$. Se utiliza específicamente para generar **términos al cuadrado**, lo cual es el único método para cancelar raíces cuadradas en binomios. |

---

## 3. EJEMPLOS RESUELTOS ADICIONALES

> [!example] Ejemplo A — Monomio con raíz cuadrada
> **Ejercicio:** Racionalizar la expresión $\frac{5}{\sqrt{3}}$.
> 
> **Paso 1: Identificar el factor multiplicador.** 
> Como el denominador es $\sqrt{3}$ (índice 2, exponente 1), multiplicamos numerador y denominador por $\sqrt{3}$ para que el exponente sume 2.
> $$\frac{5}{\sqrt{3}} \cdot \frac{\sqrt{3}}{\sqrt{3}}$$
> 
> **Paso 2: Simplificar el denominador.**
> Multiplicamos directamente: en el numerador queda $5\sqrt{3}$. En el denominador, $\sqrt{3} \cdot \sqrt{3} = \sqrt{3^2}$. Al igualarse el índice y el exponente, la raíz se cancela.
> $$\frac{5\sqrt{3}}{3}$$
> 
> **Resultado final:** $\frac{5\sqrt{3}}{3}$

> [!example] Ejemplo B — Costo unitario con raíces ($ USD)
> **Escenario:** El precio de un material de construcción es de $6$ USD por cada $\sqrt[3]{4}$ metros. Determine el costo racionalizado por metro lineal.
> 
> **Paso 1: Plantear la operación.**
> Expresamos el 4 como potencia: $\frac{6}{\sqrt[3]{2^2}}$. El índice es 3 y el exponente es 2.
> 
> **Paso 2: Racionalizar.**
> Para que el exponente llegue a 3, falta 1 ($3 - 2 = 1$). Multiplicamos por $\sqrt[3]{2^1}$:
> $$\frac{6}{\sqrt[3]{2^2}} \cdot \frac{\sqrt[3]{2}}{\sqrt[3]{2}} = \frac{6\sqrt[3]{2}}{\sqrt[3]{2^3}}$$
> 
> **Paso 3: Simplificación y división final.**
> La raíz del denominador se cancela, quedando el número $2$. Procedemos a realizar la división de los números enteros ($6 \div 2$):
> $$\frac{6\sqrt[3]{2}}{2} = 3\sqrt[3]{2}$$
> 
> **Resultado final:** El costo es de **$3\sqrt[3]{2}$ USD** por metro.

---

## 4. EJERCICIOS DE REPASO

> [!abstract] 🟢 Fácil (Monomios simples)
> 1. Racionalizar: $\frac{2}{\sqrt{x}}$
> 2. Racionalizar: $\frac{3}{\sqrt{5}}$
> 3. Racionalizar: $\frac{1}{\sqrt{y}}$

> [!abstract] 🟡 Medio (Índices mayores y binomios)
> 1. Racionalizar: $\frac{7}{\sqrt[5]{x^2}}$
> 2. Racionalizar y simplificar: $\frac{3}{\sqrt[4]{3^2}}$ *(Nota: Recuerde simplificar el índice y el exponente si es posible).*
> 3. Racionalizar el binomio: $\frac{3}{3-\sqrt{x}}$

> [!abstract] 🔴 Avanzado — Aplicación con $ USD
> **Problema de presupuesto:**
> Un ingeniero civil define el presupuesto de una pieza estructural mediante la siguiente expresión:
> $$\text{Costo} = \frac{3\sqrt{3}}{2\sqrt{3}-\sqrt{6}} \text{ USD}$$
> 
> **Instrucciones:** 
> 1. Racionalice utilizando la expresión conjugada.
> 2. Realice la multiplicación de monomio por binomio en el numerador.
> 3. Simplifique los términos finales para obtener el valor exacto.
> 
> **Resultado esperado:** $3 + \frac{3\sqrt{2}}{2}$ USD.

---

## 5. CONSEJO DE ESTUDIO

> [!tip] 💡 Estrategia de "Lo que falta"
> Para dominar la racionalización de monomios con índices altos, simplemente realiza una resta mental: **Índice - Exponente**. El resultado es el exponente que debe tener tu factor multiplicador. Por ejemplo, si tienes $\sqrt[5]{x^2}$, la operación es $5 - 2 = 3$; por lo tanto, multiplicas por $\sqrt[5]{x^3}$. ¡Esta técnica elimina cualquier duda sobre qué raíz utilizar!