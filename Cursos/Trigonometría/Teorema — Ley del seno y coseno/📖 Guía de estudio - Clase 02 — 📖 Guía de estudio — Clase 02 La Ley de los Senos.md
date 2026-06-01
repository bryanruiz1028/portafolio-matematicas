# 📖 Guía de estudio — Clase 02: La Ley de los Senos

> [!info] 📌 Conceptos clave
> 1. **Universalidad:** La Ley de los Senos es aplicable a cualquier tipo de triángulo. Aunque es la herramienta principal para resolver triángulos oblicuángulos (aquellos que no tienen ángulos rectos), funciona en todos los casos.
> 2. **Notación y Oposición:** Existe una relación obligatoria de oposición. Los ángulos se designan con letras mayúsculas ($A, B, C$) y sus lados opuestos con la misma letra en minúscula ($a, b, c$).
> 3. **Requisito de la Pareja Completa:** Para aplicar la fórmula, es indispensable conocer al menos una "pareja completa": un ángulo y la medida de su lado opuesto.
> 4. **Flexibilidad Algebraica:** La fórmula se puede invertir según la necesidad del despeje. Se pueden colocar los lados en el numerador o los senos de los ángulos en el numerador.

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ley de los Senos (Flexibilidad)** | **Lados arriba:** $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$ <br> **Senos arriba:** $\frac{\sin A}{a} = \frac{\sin B}{b} = \frac{\sin C}{c}$ |
| **Notación Obligatoria** | El lado $a$ debe estar siempre frente al ángulo $A$, el lado $b$ frente al ángulo $B$, y así sucesivamente. |
| **Pareja Completa** | Es el dato esencial para resolver la ecuación. Consiste en un ángulo conocido y su lado opuesto también conocido. |
| **Configuración de Calculadora** | Para cálculos trigonométricos con grados sexagesimales, la calculadora debe estar en modo **"Grados"** (busque la letra **D** o la abreviatura **DEG**). |

## Ejemplos Resueltos

````ad-example
**Ejemplo A (Caso Básico): Hallar el lado $x$**

**Problema:** Dado un triángulo con $\angle C = 60^\circ$, lado $c = 15m$ y $\angle A = 48^\circ$, calcula el valor del lado $x$ (lado $a$).

*   **Paso 1: Identificar la pareja completa.** Tenemos el ángulo $C$ ($60^\circ$) y su lado opuesto $c$ ($15m$).
*   **Paso 2: Plantear la ecuación con la incógnita.** Relacionamos la pareja conocida con los datos de la incógnita $a$:
    $$\frac{x}{\sin 48^\circ} = \frac{15m}{\sin 60^\circ}$$
*   **Paso 3: Despejar y calcular.** El $\sin 48^\circ$ pasa a multiplicar al otro lado:
    $$x = \frac{15m \cdot \sin 48^\circ}{\sin 60^\circ}$$
*   **Resultado:** $x \approx 12,87m$.
````

````ad-example
**Ejemplo B (Aplicación Real): Costo de cableado ($USD)**

**Problema:** Se requiere comprar un cable de refuerzo para una antena cuya longitud corresponde al lado $b$. Los datos son: $\angle A = 53^\circ$, lado $a = 30cm$ y $\angle B = 42^\circ$. Si cada centímetro de cable cuesta $0,50 USD, ¿cuál es el costo total?

*   **Paso 1: Identificar la pareja completa.** Conocemos $A = 53^\circ$ y $a = 30cm$.
*   **Paso 2: Plantear la ecuación para hallar $b$.**
    $$\frac{b}{\sin 42^\circ} = \frac{30cm}{\sin 53^\circ}$$
*   **Paso 3: Despejar y calcular la longitud.**
    $$b = \frac{30cm \cdot \sin 42^\circ}{\sin 53^\circ} \approx 25,13 cm$$
*   **Paso 4: Calcular el costo final.** Multiplicamos la longitud por el precio unitario:
    $$25,13 cm \cdot 0,50 USD = 12,565 USD$$
*   **Resultado:** El costo total será de aproximadamente **$12,57 USD**.
````

## Ejercicios de Repaso

> [!abstract] 🟢 Nivel Fácil
> En un triángulo se conocen los siguientes datos: ángulo $B = 70^\circ$, lado $b = 14$ y ángulo $A = 36^\circ$. Calcula la medida del lado $a$.
> **Resultado esperado:** $8,75$.

> [!abstract] 🟡 Nivel Medio
> En un triángulo con vértices $M, N$ y $O$, se sabe que el ángulo en el vértice $M$ es de $100^\circ$ y su lado opuesto $m$ mide $22cm$. Si el ángulo en el vértice $N$ es de $40^\circ$:
> 1. Identifica la pareja completa usando las letras asignadas.
> 2. Plantea la ecuación para hallar la medida del lado $n$ (opuesto al ángulo $N$).
> 3. Realiza el cálculo final.

> [!abstract] 🔴 Nivel Avanzado (Aplicación USD)
> Un terreno triangular debe ser cercado en uno de sus costados. Los datos medidos son: ángulo $A = 53^\circ$ y su lado opuesto $a = 60m$. Si otro de sus ángulos mide $B = 42^\circ$, calcula cuánto costará cercar el lado $b$ si el metro de valla tiene un precio de **$20,00 USD**. 
> *(Nota: Primero debes hallar la longitud del lado $b$ usando la Ley de los Senos y luego calcular el costo total).*

> [!tip] 💡 Consejo de estudio
> Una estrategia efectiva para no confundirse con la fórmula extendida es "tapar" físicamente (con un dedo o un papel) la fracción que no contiene ni datos conocidos ni la incógnita que buscas. Así, tu mente se enfocará solo en la proporción de dos fracciones que necesitas resolver.