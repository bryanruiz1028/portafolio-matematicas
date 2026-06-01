# 📖 Guía de estudio — Clase 02: Simplificación de Identidades Trigonométricas

> [!info] 📌 Conceptos clave
> - **Objetivo principal:** La simplificación consiste en transformar expresiones complejas para dejarlas expresadas únicamente en función de **seno ($\sin$)** y **coseno ($\cos$)**. Esto facilita la resolución de identidades más avanzadas.
> - **Uso de la ficha técnica:** Como recomienda el "Profe Alex", no intentes memorizar todo al principio. Mantén a mano una hoja con las identidades fundamentales para consultarlas rápidamente.
> - **Operaciones algebraicas esenciales:**
> 	- **Multiplicación de fracciones:** Se realiza de forma lineal (numerador por numerador, denominador por denominador).
> 	- **Ley de extremos y medios:** Para dividir fracciones, multiplicamos los términos externos para obtener el nuevo numerador y los medios para el denominador.
> 	- **El "Truco del 1":** Si tienes un término entero (como $\sin \alpha$), conviértelo en fracción escribiéndolo como $\frac{\sin \alpha}{1}$ para facilitar las operaciones.
> 	- **Suma/Resta Heterogénea (Método de la "Carita Feliz"):** 1. Multiplicamos los denominadores entre sí. 2. Multiplicamos en cruz los numeradores y denominadores para obtener los términos de la parte superior.
> - **Identidad Pitagórica Fundamental:** La suma de los cuadrados del seno y el coseno de un mismo ángulo siempre es igual a uno: $\sin^2 \alpha + \cos^2 \alpha = 1$.

> [!danger] ⚠️ ¡Cuidado con el error más común!
> Basado en las lecciones del **Source 3**, recuerda que **SOLO** puedes cancelar términos iguales arriba y abajo si se están **multiplicando**. Si existe una suma ($+$) o resta ($-$) en el numerador o denominador, la cancelación está estrictamente prohibida.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| Tangente ($\tan \alpha$) | $\tan \alpha = \frac{\sin \alpha}{\cos \alpha}$ |
| Cotangente ($\cot \alpha$) | $\cot \alpha = \frac{\cos \alpha}{\sin \alpha}$ |
| Cosecante ($\csc \alpha$) | $\csc \alpha = \frac{1}{\sin \alpha}$ |
| Identidad Pitagórica | $\sin^2 \alpha + \cos^2 \alpha = 1$ |

---

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Simplificación de un producto
**Problema:** Simplificar la expresión $\tan \alpha \cdot \csc \alpha$.

1. **Paso 1 (Sustitución):** Cambiamos $\tan \alpha$ por $\frac{\sin \alpha}{\cos \alpha}$ y $\csc \alpha$ por $\frac{1}{\sin \alpha}$.
2. **Paso 2 (Operación):** Multiplicamos las fracciones: $\frac{\sin \alpha \cdot 1}{\cos \alpha \cdot \sin \alpha}$.
3. **Paso 3 (Cancelación):** Como es una multiplicación, podemos eliminar el término común $\sin \alpha$: 
   $$\frac{\cancel{\sin \alpha}}{\cos \alpha} \cdot \frac{1}{\cancel{\sin \alpha}} = \frac{1}{\cos \alpha}$$

✅ **Resultado:** $\frac{1}{\cos \alpha}$
```

```ad-example
title: Ejemplo B — Aplicación de costos en trigonometría $USD
**Problema:** El costo de diseño de una estructura está representado por $\frac{\tan \alpha}{\cot \alpha}$ en dólares. Simplifica la expresión.

1. **Paso 1 (Sustitución):** $\frac{\frac{\sin \alpha}{\cos \alpha}}{\frac{\cos \alpha}{\sin \alpha}}$
2. **Paso 2 (Extremos y Medios):** Multiplicamos extremos ($\sin \alpha \cdot \sin \alpha$) y medios ($\cos \alpha \cdot \cos \alpha$).
3. **Paso 3 (Resultado):** Obtenemos $\frac{\sin^2 \alpha}{\cos^2 \alpha}$.
*(Nota pedagógica: Aunque el objetivo es dejarlo en sin/cos, nota que esto equivale a $\tan^2 \alpha$ para una simplificación total).*

✅ **Resultado:** El costo simplificado es $\frac{\sin^2 \alpha}{\cos^2 \alpha}$ USD.
```

---

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
1. Simplifica: $\cos \alpha \cdot \tan \alpha$. (Guía: Convierte la tangente. Como es una multiplicación, el $\cos \alpha$ arriba cancela al de abajo).
2. Simplifica: $\cot \alpha \cdot \sin \alpha$.
3. Expresa en términos de seno y coseno: $\csc \alpha \cdot \tan \alpha$.
```

```ad-abstract
title: 🟡 Medio
1. Resuelve la división: $\frac{\tan \alpha}{\sin \alpha}$. (Aplica extremos y medios colocando un 1 debajo del seno: $\frac{\sin \alpha}{1}$).
2. Simplifica la suma homogénea: $\frac{1}{\sin \alpha} + \frac{\cos \alpha}{\sin \alpha}$. (Mantén el mismo denominador).
3. Realiza la resta heterogénea: $\tan \alpha - \cot \alpha$ usando el método de "carita feliz".
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
1. **Presupuesto de Obra:** Simplifica $(\tan \alpha \cdot \csc \alpha) + \tan \alpha$. Realiza primero la multiplicación (cancelando términos permitidos) y luego suma las fracciones homogéneas resultantes.
2. **Costo Estructural:** Determina el valor simplificado de $\frac{\sin^2 \alpha + \cos^2 \alpha}{\cos \alpha \cdot \sin \alpha}$ USD. (Aplica la identidad pitagórica en el numerador antes de operar).
```

---

> [!tip] 💡 Consejo de estudio
> Como tutor, te sugiero que no te agobies intentando memorizar cada identidad hoy mismo. Crea una **ficha técnica** (una tabla limpia en una hoja aparte) y consúltala en cada ejercicio. Con la práctica repetida, tu cerebro asimilará las fórmulas de manera natural. Recuerda siempre verificar si tienes una multiplicación antes de intentar cancelar cualquier término; de lo contrario, tu resultado será incorrecto. ¡Ánimo, la constancia es la clave!