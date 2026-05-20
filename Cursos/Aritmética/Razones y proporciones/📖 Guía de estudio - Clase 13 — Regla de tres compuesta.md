# 📖 Guía de estudio — Clase 13: Regla de Tres Compuesta

¡Qué tal, amigos! Espero que estén muy bien. En esta guía vamos a desglosar paso a paso cómo dominar la regla de tres compuesta. No se asusten por el nombre; al igual que con la regla simple, la clave está en ser organizados y aprender a "conversar" con las variables para saber cómo se relacionan entre sí. ¡Vamos a darle!

> [!info] 📌 Conceptos clave
> - **Más de dos variables:** A diferencia de la regla de tres simple, la compuesta entra en juego cuando tenemos 3, 4 o más magnitudes comparándose al mismo tiempo.
> - **¿Cómo encontrar las variables?:** ¡Es un truco súper fácil! Solo tienes que buscar las palabras o sustantivos que aparecen justo después de cada número (por ejemplo: 8 **horas**, 2000 **ruedas**, 5 **días**).
> - **Relación entre variables:** Comparamos siempre las variables con la que tiene la incógnita (X). Pueden ser **Directas** (si una aumenta, la otra también: "a más, más") o **Inversas** (si una aumenta, la otra disminuye: "a más, menos").
> - **El papel de "X":** Es nuestro tesoro escondido. La variable donde está la X siempre se escribe como una fracción a un lado del igual para poder despejarla.

---

## FÓRMULAS Y DEFINICIONES IMPORTANTES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Regla de Tres Compuesta** | Procedimiento matemático para resolver problemas de proporcionalidad donde intervienen tres o más magnitudes. |
| **Relación Directa** | Cuando ambas variables se mueven en el mismo sentido. Ejemplo: A más **grifos** abiertos, más **litros** de agua consumidos. |
| **Relación Inversa** | Cuando las variables se mueven en sentidos opuestos. Ejemplo: A más **obreros** trabajando, menos **días** tardarán en terminar la obra. |

---

## EJEMPLOS RESUELTOS PASO A PASO

::: ad-example
### Ejemplo A — Producción de Ruedas
**Problema:** En una fábrica, trabajando 8 **horas** diarias, han fabricado 2000 **ruedas** en 5 **días**. ¿Cuántos **días** tardarán en fabricar 3000 **ruedas** si trabajan 10 **horas** diarias?

**¡Paso 1: Organicemos nuestros datos!**
- **Horas**: 8 | 10
- **Ruedas**: 2000 | 3000
- **Días**: 5 | **X**

**¡Paso 2: Identifiquemos las relaciones!** (Siempre comparamos contra la columna de la "X", que es **Días**):
- **Horas vs. Días:** Si trabajan más horas al día, ¿tardarán más o menos días? ¡Menos días! Como es "a más, menos", es una relación **Inversa**.
- **Ruedas vs. Días:** Si queremos fabricar más ruedas, ¿necesitamos más o menos días? ¡Más días! Como es "a más, más", es una relación **Directa**.

**¡Paso 3: Configuremos la ecuación!**
Escribimos la fracción de la incógnita a un lado y las demás al otro. **Ojo aquí:** Como la relación de **Horas** es Inversa, debemos invertir su fracción (escribimos $10/8$ en lugar de $8/10$).
$$\frac{5}{X} = \frac{10}{8} \cdot \frac{2000}{3000}$$

**¡Paso 4: El "Superpoder" de la simplificación!**
Para no trabajar con números gigantes, simplificamos *antes* de multiplicar:
1. Tachamos los tres ceros de las ruedas: $\frac{2000}{3000} \rightarrow \frac{2}{3}$.
2. Sacamos mitad a la fracción de horas: $\frac{10}{8} \rightarrow \frac{5}{4}$.
3. Ahora tenemos: $\frac{5}{X} = \frac{5}{4} \cdot \frac{2}{3}$. Podemos simplificar el 2 (arriba) con el 4 (abajo) sacando mitad: $\frac{5}{2} \cdot \frac{1}{3}$.
4. Multiplicamos lo que quedó: $\frac{5}{X} = \frac{5}{6}$.
5. Aplicamos **producto cruzado** (cruzamos los valores para liberar a la X): $5 \cdot 6 = 5 \cdot X \implies 30 = 5X \implies X = 6$.

**Resultado:** Tardarán **6 días**.
:::

::: ad-example
### Ejemplo B — Consumo en Grifos
**Problema:** 9 **grifos** abiertos durante 40 **horas** han consumido 200 **litros** de agua. ¿Cuántos **litros** consumen 15 **grifos** durante 9 **horas**?

**¡Paso 1: Planteamiento!**
- **Grifos**: 9 | 15
- **Horas**: 40 | 9
- **Litros**: 200 | **X**

**¡Paso 2: Relaciones!** (Comparamos contra **Litros**):
- **Grifos vs. Litros:** A más grifos, más litros consumidos. Es **Directa**.
- **Horas vs. Litros:** A más horas abiertos, más litros. Es **Directa**.

**¡Paso 3: Ecuación y Simplificación!**
$$\frac{200}{X} = \frac{9}{15} \cdot \frac{40}{9}$$
- ¡Mira qué fácil! Eliminamos el 9 de arriba con el 9 de abajo (novena de 9 es 1).
- Nos queda $\frac{40}{15}$. Simplificamos sacando quinta: $\frac{8}{3}$.
- Ahora, aplicamos producto cruzado para despejar: $200 \cdot 3 = 8 \cdot X \implies 600 = 8X$.
- Dividimos $600 / 8 = 75$.

**Resultado:** Consumirán **75 litros**.
:::

---

## EJERCICIOS DE REPASO

::: ad-abstract
### 🟢 Nivel Fácil
**Consumo de agua:** Si 9 **grifos** abiertos durante 40 **horas** consumen 200 **litros**, ¿cuántos **litros** consumirán 12 **grifos** en 6 **horas**?
*(Resultado esperado: 40 litros).*
:::

::: ad-abstract
### 🟡 Nivel Medio
**Construcción de muro:** 4 **obreros** trabajando 7 **horas** diarias construyen un muro en 3 **días**. ¿Cuántos **días** tardarán 3 **obreros** trabajando 8 **horas** diarias?
*(Resultado esperado: 3.5 días. Recuerda que 3.5 significa **3 días y medio**; ¡usa la lógica para interpretar tus resultados!).*
:::

::: ad-abstract
### 🔴 Nivel Avanzado — Aplicación Compleja
**Fábrica de ruedas:** En una fábrica, trabajando 8 **horas** diarias, se fabrican 2000 **ruedas** en 5 **días**. ¿Cuántas **horas** diarias deben trabajar para fabricar 1400 **ruedas** en 4 **días**?
*(Resultado esperado: 7 horas).*
:::

---

> [!tip] 💡 Consejo de estudio del Profe Alex
> ¡No te compliques con números grandes, amigos! Simplificar no es solo un truco, es un **superpoder** para evitar errores y no depender de la calculadora. Acuérdate de tachar ceros arriba y abajo, y de sacar mitades o terceras siempre que puedas *antes* de hacer la multiplicación final. ¡Confía en tu proceso y verás que las matemáticas son pan comido! ¡Bye, bye!