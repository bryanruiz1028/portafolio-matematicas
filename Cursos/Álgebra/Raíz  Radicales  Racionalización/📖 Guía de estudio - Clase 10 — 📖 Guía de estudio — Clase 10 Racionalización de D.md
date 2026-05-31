# 📖 Guía de estudio — Clase 10: Racionalización de Denominadores

> [!info] 📌 Conceptos clave
> ¡Hola, amigas y amigos! Antes de empezar, aseguremos estas ideas base para que el camino sea súper sencillo:
> 1. **El Objetivo**: Racionalizar es simplemente "limpiar" el denominador. Queremos eliminar cualquier raíz de la parte de abajo de nuestra fracción para que operar sea más fácil.
> 2. **El Binomio Conjugado**: Si tenemos una suma o resta como $a + b$, su conjugado es $a - b$. Al multiplicarlos, usamos la propiedad $(a+b)(a-b) = a^2 - b^2$, lo que eleva cada término al cuadrado y elimina las raíces cuadradas.
> 3. **Igualar para Cancelar**: Cuando hay sumas dentro de una raíz (como $\sqrt[n]{suma}$), la clave es que el exponente de toda la suma sea igual al índice de la raíz. ¡Si son iguales, la raíz se va!
> 4. **Simplificación**: ¡No te detengas al eliminar la raíz! Siempre observa si los números que quedaron fuera de la raíz (arriba y abajo) se pueden simplificar.

## Tabla de Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Racionalización** | Proceso matemático para transformar denominadores con raíces en números sin ellas, manteniendo el valor de la fracción. |
| **Binomio Conjugado** | Consiste en escribir los mismos términos pero cambiando el signo central. Ejemplo: de $3 - \sqrt{2}$ pasamos a $3 + \sqrt{2}$. |
| **Propiedad de Cancelación** | $\sqrt[n]{a^n} = a$. La raíz se elimina solo cuando el **índice** y el **exponente** de la cantidad total son idénticos. |

## Ejemplos Resueltos Adicionales

> [!example] Ejemplo A — Racionalización con Conjugado
> **Ejercicio**: Racionalizar la expresión $\frac{5}{3 - \sqrt{2}}$
> 
> **¡Paso a paso!**
> 1. **Identificar el conjugado**: Como abajo tenemos $3 - \sqrt{2}$, multiplicamos arriba y abajo por su pareja: $3 + \sqrt{2}$.
>    $$\frac{5}{3 - \sqrt{2}} \cdot \frac{3 + \sqrt{2}}{3 + \sqrt{2}}$$
> 2. **Aplicar diferencia de cuadrados**: En el denominador, elevamos cada término al cuadrado y siempre restamos:
>    $$3^2 - (\sqrt{2})^2 = 9 - 2 = 7$$
> 3. **Operar el numerador**: Aquí tienes dos opciones válidas. Puedes dejarlo expresado o multiplicar el 5 por lo de adentro:
>    $$5(3 + \sqrt{2}) \quad \text{o} \quad 15 + 5\sqrt{2}$$
> 
> **Resultado final**: $\frac{5(3 + \sqrt{2})}{7}$ (O también $\frac{15 + 5\sqrt{2}}{7}$). ¡Ambas formas son correctas!

> [!example] Ejemplo B — Aplicación en Finanzas
> **Problema**: Un fondo de inversión de $5\text{ USD}$ debe dividirse entre la raíz cuadrada de un proyecto que cuesta $x + 2$. ¿Cómo queda la expresión racionalizada?
> 
> **¡Paso a paso!**
> 1. **Plantear la fracción**: Tenemos $\frac{5}{\sqrt{x+2}}$. Para eliminar la raíz, multiplicamos por otra raíz idéntica: $\sqrt{x+2}$.
> 2. **Unir y elevar**: Al multiplicar raíces iguales, el radicando queda elevado al cuadrado:
>    $$\frac{5 \cdot \sqrt{x+2}}{\sqrt{(x+2)^2}}$$
> 3. **Cancelar y finalizar**: El cuadrado cancela la raíz cuadrada en el denominador.
>    
> **Resultado final**: $\frac{5\sqrt{x+2}}{x+2} \text{ USD}$

## Ejercicios de Repaso

> [!abstract] 🟢 Fácil
> ¡Comencemos con calma! Racionaliza estas expresiones de un solo término:
> 1. $\frac{2}{\sqrt{5}}$
> 2. $\frac{3}{\sqrt{7}}$
> 3. $\frac{1}{\sqrt{3}}$

> [!abstract] 🟡 Medio
> ¡Atención aquí! Usa el binomio conjugado y **no olvides simplificar** si es posible:
> 1. $\frac{2}{5-\sqrt{5}}$ *(Pista: Al final verás un 2 arriba y un 20 abajo. ¡Saca mitad!)*
> 2. $\frac{5}{\sqrt{3}-4}$ *(¡Cuidado! El denominador será $3 - 16 = -13$. Mantén ese signo negativo).*

> [!abstract] 🔴 Avanzado — Aplicación con $USD
> **Desafío**: Racionaliza el presupuesto de un contrato dado por la fórmula:
> $$\frac{2x^3+1}{\sqrt[3]{2x^3+1}} \text{ USD}$$
> 
> **Guía del Profe**:
> *   Como es una **raíz cúbica** (índice 3) y lo de adentro está elevado a la 1, debes multiplicar por el radicando **elevado al cuadrado** ($\sqrt[3]{(2x^3+1)^2}$) para que $1 + 2 = 3$.
> *   **¡Ojo!** Recuerda que debes elevar *toda la suma* al cuadrado, no los términos por separado.
> *   Al final, notarás que el factor de arriba y el nuevo denominador son iguales. ¡Simplifícalos!

> [!tip] 💡 Consejo de estudio
> ¡Atención, exploradores! Antes de lanzarse a multiplicar, recuerden la regla de oro: **$(x+2)^2$ no es lo mismo que $x^2 + 2^2$**. Siempre traten a la suma o resta dentro de la raíz como un solo bloque protegido por paréntesis. 
> 
> Además, si después de racionalizar tienen un factor fuera de la raíz arriba y un número abajo, como $\frac{2(5+\sqrt{5})}{20}$, simplifiquen dividiendo ambos por el mismo número: $\frac{1(5+\sqrt{5})}{10}$. ¡Se ve mucho más profesional!