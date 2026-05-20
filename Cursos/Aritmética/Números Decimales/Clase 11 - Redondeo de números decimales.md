# Clase 11 — Rounding decimal numbers

#algebra #roundingdecimal

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 11 de 22

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [[Lección 10 — Decimal place value]]
> 📋 **Índice:** [[00 - Índice del curso]]
> ➡️ **Siguiente:** [[Lección 12 — Operations with decimals]]

---

## 🌍 Relevancia y aplicaciones

Redondear no es simplemente "quitar números"; es una herramienta poderosa para simplificar nuestra vida matemática. Nos permite obtener valores similares a los originales pero mucho más amigables para realizar cálculos rápidos.

*   **💵 [USD]:** Si un televisor cuesta **$999**, nuestra mente lo redondea automáticamente a **$1.000**. Gracias a esto, podemos calcular al instante que comprar cinco televisores nos costaría unos **$5.000**, en lugar de perder tiempo multiplicando el valor exacto.
*   **🏗️ [Práctica]:** En ingeniería y construcción, redondear permite manejar medidas extensas sin que la precisión necesaria para la seguridad se vea comprometida.
*   **📊 [Cotidiana]:** Es vital para estimar presupuestos en el supermercado o calcular el tiempo de llegada en un viaje sin necesidad de una calculadora.

---

## 📍 Fundamento: El Mapa de Posiciones

Antes de redondear, es fundamental identificar correctamente dónde vamos a "cortar" el número. Como menciona el Profe Alex, no podemos redondear si no sabemos ubicar la posición solicitada.

```text
      5 3 , 4   6   3   8   5
      ^ ^   ^   ^   ^   ^   ^
      | |   |   |   |   |   |
Decenas | Décimas | Milésimas |
     Unidades  Centésimas  Diezmilésimas
```

> [!tip] 💡 Nota regional
> En esta clase utilizamos la **coma (,)** para separar los decimales. Si en tu país se utiliza el **punto (.)**, ¡no te preocupes! La lógica y el procedimiento son exactamente los mismos.

---

## 📌 ¿Qué es Rounding decimal numbers?

> [!note] **Definición**
> Redondear es el proceso de convertir un número en otro valor cercano que sea más sencillo de usar en operaciones matemáticas, manteniendo una aproximación fiel al valor original.

> [!warning] ⚠️ **Error común**
> Muchos estudiantes olvidan que el **5** ya es un número "grande". Al redondear 53,46 a la décima, el error es dejarlo en 53,4. Lo correcto es subir a **53,5** porque la cifra siguiente (6) es mayor o igual a 5.

> [!tip] 💡 **Truco para recordarlo**
> Aplica la regla del **"Vecino de la derecha"**:
> 1. Ubica tu cifra objetivo.
> 2. Mira a su vecino inmediato a la derecha.
> 3. Si el vecino es **pequeño (0, 1, 2, 3, 4)**, tu cifra se queda igual.
> 4. Si el vecino es **grande (5, 6, 7, 8, 9)**, a tu cifra le sumas 1.

---

## 🚀 Procedimiento paso a paso

> [!todo] **Guía para redondear con éxito**
> 1. **Identificar:** Localiza la posición (unidades, décimas, centésimas, etc.) a la que deseas redondear.
> 2. **Observar:** Mira exclusivamente la cifra situada a la derecha de esa posición.
> 3. **Decidir:**
>    * Si es **0-4**: La cifra objetivo no cambia.
>    * Si es **5-9**: Suma **1** a la cifra objetivo.
>    * **Regla de Acarreo (Profe Alex):** Si la cifra objetivo es un **9** y debes sumar 1, mira la cifra a su izquierda y trátalas como un bloque (ej. si tienes `...49` y el 9 debe subir, el bloque se convierte en `50`).
> 4. **Limpiar:** Elimina todas las cifras a la derecha. Si el resultado termina en **0** después de la coma, omítelo para simplificar el número.

---

## 📖 Ejemplos prácticos

```ad-example
title: Ejemplo 1 — [Caso básico]
**Problema:** Redondear **53,46385** a las **unidades**.
1. La cifra de las unidades es el **3**.
2. El vecino a la derecha es **4**.
3. Como 4 es pequeño, el 3 se mantiene.
**Resultado:** 53
```

```ad-example
title: Ejemplo 2 — [Casos de acarreo]
**Problema:** Redondear **1,496** a las **centésimas**.
1. La cifra de las centésimas es el **9**.
2. El vecino es **6** (grande, sumamos 1).
3. Aplicamos la regla de acarreo: el bloque **49** sube a **50**.
**Resultado:** 1,50 → **1,5** *(Se elimina el cero final porque no altera el valor y simplifica el número).*
```

```ad-example
title: Ejemplo 3 — [Avanzado]
**Problema:** Redondear **756,9195** a las **milésimas**.
1. La cifra de las milésimas es el **9**.
2. El vecino es **5** (grande, sumamos 1).
3. El bloque **19** se convierte en **20**.
**Resultado:** 756,920 → **756,92** *(Omitimos el cero final siguiendo la recomendación del Profe Alex).*
```

```ad-example
title: Ejemplo 4 — [Aplicación $USD]
**Problema:** Un artículo cuesta **$53,468**. Redondear a la **décima** más cercana.
1. La décima es el **4**. El vecino es **6** (grande).
2. El 4 sube a **5**.
**Resultado:** $53,5
```

---

## ✍️ Ejercicios para el estudiante

Utiliza el número **15,9642** para practicar:

```ad-abstract
title: 🟢 Fácil (Posiciones básicas)
1. Redondea **15,9642** a las **unidades**.
2. Redondea **15,9642** a las **milésimas**.
```

```ad-abstract
title: 🟡 Medio (Regla del 5 y acarreo)
1. Redondea **15,9642** a las **décimas**.
2. Redondea **15,9642** a las **centésimas**.
*(Pista: Observa qué sucede con el **15,9** al redondear a la unidad: el bloque 15 sube a 16 debido al 9 en las décimas).*
```

```ad-abstract
title: 🔴 Avanzado (Aplicación $USD)
Si compras 3 artículos que cuestan **$15,96** cada uno y decides redondear el precio a la **unidad** antes de sumarlos para una estimación rápida, ¿cuál sería el presupuesto total estimado?
```

```ad-abstract
title: ✅ Respuestas
- **Fácil:** 1. (16) | 2. (15,964)
- **Medio:** 1. (16,0 → 16) | 2. (15,96)
- **Avanzado:** Cada artículo ($15,96) se redondea a $16. Total: 16 x 3 = **$48**.
```

---

## 📝 Autoevaluación

```ad-question
title: 1. Concepto
¿Qué sucede si la cifra a la derecha de la posición que quieres redondear es un **5**?
a) La cifra objetivo se mantiene igual.
b) Se le resta 1 a la cifra objetivo.
c) Se le suma 1 a la cifra objetivo.
d) Se eliminan todos los decimales automáticamente.
```

```ad-question
title: 2. Procedimiento
¿Cuál es el redondeo de **53,46385** a las décimas?
a) 53,4
b) 53,5
c) 53,46
d) 53,47
```

```ad-question
title: 3. Aplicación
Si un producto tiene un precio de **$999,99**, ¿cuál es su redondeo a la unidad más cercana?
a) $999,9
b) $999
c) $1.000
d) $1.000,99
```

¡Excelente trabajo! Recuerda que el redondeo es tu mejor aliado para hacer que las matemáticas sean más **amigables** y rápidas en tu día a día.

> [!tip] 💡 **En la próxima clase**
> Ahora que dominas el redondeo, estamos listos para realizar operaciones más complejas. En la siguiente lección aplicaremos esto en sumas, restas y multiplicaciones con decimales.

---

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [[Lección 10 — Decimal place value]]
> 📋 **Índice:** [[00 - Índice del curso]]
> ➡️ **Siguiente:** [[Lección 12 — Operations with decimals]]