# Clase 02 — Reducción de términos semejantes y signos de agrupación

`#algebra` `#reduccindetrmin`

---
**Navegación:**
[Anterior: Clase 01] | [Siguiente: Clase 03]
---

## 1. ¿Por qué es importante esta clase?

Para sumar cualquier cosa en la vida, y especialmente en el álgebra, los elementos deben ser de la misma naturaleza. Imagina que en una concesionaria tienes 5 carros y llegan 3 carros más; tienes 8 carros. Pero si tienes 5 carros y llegan 5 motocicletas, no tienes "10 carromotos"; simplemente tienes 5 carros y 5 motocicletas por separado.

*   **Relevancia:** En matemáticas, "reducir" es el proceso de agrupar elementos que son de la misma especie para que la expresión sea más corta y sencilla. Si no son de la misma especie, no se pueden mezclar.
*   **Aplicación $USD:** Piensa en billetes y monedas. Si $x$ representa el valor de un billete y $y$ el de una moneda, puedes agrupar tus billetes por un lado y tus monedas por otro. Nunca podrías decir que tienes un solo grupo total "xy" porque su valor y naturaleza son distintos.
*   **Aplicación práctica:** El inventario de una tienda se organiza así: no mezclas camisas con pantalones en la misma cuenta, sino que sumas "unidades de camisas" y "unidades de pantalones".

## 2. Concepto clave

```ad-note
title: 📌 ¿Qué es un Término Semejante?
Dos o más términos son semejantes cuando tienen la **misma parte literal**. Esto significa que deben tener las mismas letras y que cada letra debe tener exactamente el mismo exponente. En términos sencillos: "Son hermanos gemelos de letras".
```

```ad-warning
title: ⚠️ Error común
Muchos estudiantes intentan sumar $x$ con $x^2$, pero **no son semejantes**. Imagina que $x$ es un carro normal y $x^2$ es un carro con remolque; aunque ambos son vehículos, son de categorías (dimensiones) distintas y no se pueden contar como si fueran lo mismo. Del mismo modo, $x^2y^3$ no es semejante a $x^3y^2$ porque los exponentes están en letras diferentes. ¡Deben ser idénticos!
```

```ad-tip
title: 💡 Truco de las "Etiquetas"
Imagina que las letras y los exponentes son una "etiqueta" fluorescente pegada al número. Para poder sumar o restar dos términos, sus etiquetas deben ser **idénticas** (ej. $mn^2$ es igual a $mn^2$). Si a una etiqueta le falta un numerito o tiene una letra distinta, la regla es clara: "Manzanas con manzanas y peras con peras".
```

## 3. Procedimiento paso a paso

Para reducir términos como un experto, aplicaremos la lógica del **"Tengo y Debo"** del Profe Alex. Sigue estos pasos en tu cuaderno:

```text
1. Identificar: Busca los términos que tengan la "etiqueta" (parte literal) exactamente igual.
2. Aplicar "Tengo o Debo": Mira el signo del coeficiente.
   - Si es positivo (+), es dinero que "Tengo".
   - Si es negativo (-), es una deuda que "Debo".
3. Operar Coeficientes: Realiza la suma o resta mental de cuánto te queda o cuánto debes.
   - 💡 Pro-Tip: Si una letra no tiene número adelante (ej. "x"), recuerda que ahí hay un "1" escondido.
4. Mantener la Base: Escribe la etiqueta (letras y exponentes) igualita al lado del resultado. ¡Las letras no cambian al sumar o restar!
```

## 4. Ejemplos Desarrollados

```ad-example
title: Ejemplo 1: Básico (Suma de positivos)
**Problema:** Reducir $2m^2n^3 + 5m^2n^3$
1. La etiqueta es $m^2n^3$ en ambos.
2. Operamos: Tengo 2 y tengo 5. En total tengo 7.
3. Resultado: **$7m^2n^3$**.
```

```ad-example
title: Ejemplo 2: La lógica del "Tengo/Debo"
**Problema:** Reducir $3mn - 5mn$
1. Son semejantes (ambos son $mn$).
2. Operamos: Tengo 3 y debo 5. Como la deuda es más grande, pago los 3 y quedo debiendo 2.
3. Resultado: **$-2mn$**.
```

```ad-example
title: Ejemplo 3: Exponentes variables (Avanzado)
**Problema:** $(x^{n+1} + 4x^{n+1}) + (-13x^{n+2} + 9x^{n+2})$
1. Agrupamos los de la familia $x^{n+1}$: Tengo 1 (el uno oculto) y tengo 4 = **$5x^{n+1}$**.
2. Agrupamos los de la familia $x^{n+2}$: Debo 13 y tengo 9 = **$-4x^{n+2}$**.
3. Resultado final: **$5x^{n+1} - 4x^{n+2}$**. 
*Nota: Se quedan así porque $x^{n+1}$ y $x^{n+2}$ son de familias diferentes (diferente exponente) y no se pueden mezclar.*
```

```ad-example
title: Ejemplo 4: Aplicación de moneda ($USD)
**Problema:** Tienes 10 billetes de valor $x$ y 5 monedas de valor $y$. Te dan 3 billetes $x$ y pierdes 2 monedas $y$.
1. Expresión: $10x + 5y + 3x - 2y$.
2. Reducimos billetes ($x$): Tengo 10 y tengo 3 = $13x$.
3. Reducimos monedas ($y$): Tengo 5 y debo 2 = $3y$.
4. Resultado: **$13x + 3y$**. No se puede simplificar más porque billetes y monedas tienen valores (variables) distintos.
```

## 5. Casos con Signos de Agrupación

Cuando veas paréntesis `()`, corchetes `[]` o llaves `{}`, recuerda que **el signo que está afuera es una ORDEN**:

1.  **Si el signo es positivo (+):** La orden es "Deja todo igual". Quitas el paréntesis y los términos de adentro mantienen su propio signo.
2.  **Si el signo es negativo (-):** La orden es "¡Cambia todo!". Quitas el paréntesis y todos los términos de adentro cambian al signo opuesto ($+$ pasa a $-$ y viceversa).
3.  **Orden de ataque:** Siempre se resuelve **"de adentro hacia afuera"**: primero paréntesis, luego corchetes y al final las llaves.

**Ejemplo paso a paso:** $2x - [5x - (3y + 2x)]$
*   **Paso 1 (Quitar paréntesis):** El signo $-$ antes del paréntesis es una orden de cambiar signos. El $3y$ (que era $+$) pasa a $-$ y el $2x$ (que era $+$) pasa a $-$.
    *   $2x - [5x - 3y - 2x]$
*   **Paso 2 (Quitar corchete):** Otra vez hay un signo $-$ afuera. Es una orden de cambiar todo lo que quedó dentro del corchete.
    *   $2x - 5x + 3y + 2x$
*   **Paso 3 (Reducir):** Agrupamos las $x$. Tengo 2, debo 5, tengo 2. En total: $2 - 5 + 2 = -1$.
    *   Resultado: **$-x + 3y$**.

## 6. Ejercicios para el estudiante

```ad-abstract
title: 🟢 Nivel Fácil: Reducción Directa
1. $7a + 12a$
2. $15x^2 - 9x^2$
3. $5mn + 3mn + 2mn$
4. $-10b - 4b$
```

```ad-abstract
title: 🟡 Nivel Medio: Mezcla de Términos
1. $8m - 3n + 5m - 2n$
2. $10a^2 + 4b - 15a^2 + 6b$
3. $x + y - 5x + 3y$
4. $15ab - 6ab + 2c$
```

```ad-abstract
title: 🔴 Nivel Avanzado: Agrupación y Exponentes
1. $3x - [2x + (5x - 3x)]$
2. $5a^{n+1} - 3a^{n+1} + 2a^{n+2}$
3. $-(2x - 3y) + (5x - 2y)$
4. $10m^2 - [3m^2 - (5n + 2m^2)]$ *(Pista: ¡Ojo con el doble signo negativo al final!)*
```

```ad-success
title: ✅ Respuestas para el docente (Haz clic para expandir)
collapse: true
**Fácil:** 
1. $19a$ 
2. $6x^2$ 
3. $10mn$ 
4. $-14b$

**Medio:** 
1. $13m - 5n$ 
2. $-5a^2 + 10b$ 
3. $-4x + 4y$ 
4. $9ab + 2c$

**Avanzado:** 
1. $-x$ 
2. $2a^{n+1} + 2a^{n+2}$ 
3. $3x + y$ 
4. $9m^2 + 5n$
```

## 7. Mini-prueba de autoevaluación

```ad-question
title: Pregunta 1
¿Cuál de los siguientes grupos contiene solo términos semejantes?
A) $3x, 3y, 3z$
B) $2ab^2, 5a^2b, 7ab$
C) $4m^2n^3, -m^2n^3, \frac{1}{2}m^2n^3$
**Respuesta correcta: C** (Tienen letras y exponentes idénticos).
```

```ad-question
title: Pregunta 2
¿Cuál es el resultado de reducir $-8m^2 - 3m^2$?
A) $-5m^2$
B) $-11m^2$
C) $11m^4$
**Respuesta correcta: B** (Debo 8 y debo 3, en total debo 11).
```

```ad-question
title: Pregunta 3
En una compra, tienes 5 artículos tipo "$a$". Devuelves 2 tipo "$a$" y luego compras 3 artículos diferentes tipo "$b$". ¿Cómo queda tu balance?
A) $3a + 3b$
B) $6ab$
C) $7a - 3b$
**Respuesta correcta: A** ($5a - 2a = 3a$; los $3b$ no se pueden mezclar).
```

## 8. Cierre y Navegación

**Notas para el próximo tema:**
Dominar la reducción es como aprender a organizar tu mochila antes de un viaje largo. En la siguiente clase utilizaremos esta base para la **multiplicación de polinomios**, donde descubrirás que, a diferencia de la suma, en la multiplicación las letras *sí* pueden cambiar sus exponentes. ¡Prepárate!

---
**Navegación:**
[Anterior: Clase 01] | [Siguiente: Clase 03]
---