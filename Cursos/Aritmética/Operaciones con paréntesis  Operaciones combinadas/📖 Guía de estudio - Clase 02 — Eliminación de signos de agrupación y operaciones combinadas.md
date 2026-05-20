# 📖 Guía de estudio — Clase 02: Eliminación de Signos de Agrupación

¡Hola! En esta guía aprenderás a dominar el arte de simplificar expresiones complejas. Como dice el **Profe Alex**, la clave no está en la velocidad, sino en la **minuciosidad**. Al terminar este material, serás capaz de resolver cualquier operación con signos de agrupación siguiendo un proceso lógico y ordenado.

---

## 1. Introducción y Conceptos Clave

Para vencer el caos de los paréntesis, corchetes y llaves, debemos seguir tres reglas de oro que garantizan el éxito:

> [!info] 📌 Conceptos fundamentales
> 1.  **Orden Jerárquico (De adentro hacia afuera):** Primero eliminamos los paréntesis `( )`, luego los corchetes `[ ]` y finalmente las llaves `{ }`. ¡Este orden es inamovible!
> 2.  **La Regla del Número Único (Reducción):** Antes de destruir un signo de agrupación, es indispensable reducir su contenido a un **solo número**. Si hay sumas o restas dentro, resuélvelas primero.
> 3.  **La Mirada a la Izquierda (Eliminación):** Una vez que tienes un solo número, mira inmediatamente a la izquierda del signo de agrupación:
>     *   **Si hay un signo (+ o -):** Aplicamos la ley de signos (Multiplicación de signos).
>     *   **Si hay un número:** El número de afuera multiplica al resultado interno (Multiplicación de números).
> 4.  **El Truco del Separador:** A veces, el paréntesis no indica una operación, sino que solo sirve para separar dos signos seguidos (por ejemplo: `+ (-5)`).

---

## 2. Fórmulas y Definiciones Importantes

Utiliza esta tabla como tu mapa de navegación. Recuerda: **Signos iguales = Positivo (+)** y **Signos diferentes = Negativo (-)**.

| Término | Definición / Regla | Visualización (Paso a Paso) |
| :--- | :--- | :--- |
| **Paréntesis ( )** | Primer nivel de agrupación. Se resuelven primero. | `-( 10 - 3 ) = -( 7 )` |
| **Corchetes [ ]** | Segundo nivel. Envuelven a los paréntesis. | `-[ 5 + ( 2 ) ] = -[ 7 ]` |
| **Llaves { }** | Tercer nivel. Son la capa más externa del ejercicio. | `+{ 4 - [ 9 ] } = +{ -5 }` |
| **Multiplicación de Signos** | Si solo hay un signo a la izquierda, multiplica: `-(-)` es `+`. | `- ( - 4 ) = +4` |
| **Multiplicación de Números** | Si hay un número "tocando" el signo, multiplica el valor. | `-3 ( +2 ) = -6` |

---

## 3. Ejemplos Resueltos Paso a Paso

```ad-example
title: Ejemplo A — El método de la Reducción y Eliminación
**Enunciado:** `-(+5 - [ + (7 - 5) ] - 8)`

**Proceso lógico:**
1. **Reducción del paréntesis:** Resolvemos `(7 - 5)`. Nos queda `2`.
   *Expresión:* `-(+5 - [ + (2) ] - 8)`
2. **Eliminación del paréntesis:** Como hay un signo `+` a la izquierda, multiplicamos signos: `+` por `+` da `+`.
   *Expresión:* `-(+5 - [ +2 ] - 8)`
3. **Eliminación del corchete:** ¡Atención aquí! Solo hay un número dentro del corchete. Miramos a la izquierda: hay un signo `-`. Multiplicamos: `-` por `+` da `-`.
   *Expresión:* `-(+5 - 2 - 8)`
4. **Reducción de las llaves (Lógica "Debo y Tengo"):** 
   - Tengo 5 y gasto 2, me quedan 3.
   - Tengo 3, pero debo 8, entonces quedo debiendo 5 (`-5`).
   *Expresión:* `-( -5 )`
5. **Eliminación final:** El signo `-` de afuera con el `-` de adentro son iguales. El resultado se vuelve positivo.

✅ **Resultado:** **+5**
```

```ad-example
title: Ejemplo B — Aplicación de finanzas cotidianas ($USD)
**Enunciado:** `-(7 + { -5 + [ 8 - (5 - 3) ] })`

**Interpretación como presupuesto:**
1. **Gasto pequeño:** El paréntesis `(5 - 3)` es una compra de $3 con un billete de $5. Te quedan `2`.
   *Expresión:* `-(7 + { -5 + [ 8 - 2 ] })`
2. **Saldo en corchetes:** Tenías $8 y te quitan el saldo del paréntesis ($2). Te quedan `6`.
   *Expresión:* `-(7 + { -5 + 6 })`
3. **Saldo en llaves:** Debes $5 pero tienes $6. Pagas y te queda `1` a favor.
   *Expresión:* `-(7 + 1)`
4. **Cierre de cuenta:** Sumas el dinero externo: `7 + 1 = 8`. El signo negativo final afuera de todo indica que este saldo es un pago obligatorio o una salida total de dinero.

✅ **Resultado:** **-8**
```

---

## 4. Ejercicios de Repaso

¡Es tu turno! Aplica la **minuciosidad** en cada paso.

```ad-abstract
title: 🟢 Nivel: Fácil
1. `5 + (8 - 3)`
2. `10 - [ 5 + (2 - 1) ]`
3. `-( -4 + 6 )`
```

```ad-abstract
title: 🟡 Nivel: Medio
1. `-9 + { -1 + 5 - [ 8 + (5 - 3) - 2 ] + 9 }`
2. `7 - [ 3 + ( -5 + 2 ) - ( 8 - 10 ) ]`
3. `15 + { -2 - [ -3 + ( 4 - 5 ) ] }`
```

```ad-abstract
title: 🔴 Nivel: Avanzado (Desafío de Multiplicación)
1. **Contexto:** Tienes un negocio y tu deuda se ha triplicado. El sobre de cuentas dice: `-3 * { -7 + [ -4 * ( -6 ) + 15 ] }`.
2. **Instrucción:** Recuerda el truco del Profe Alex: si el número está pegado a la llave, ¡multiplica todo el resultado final!
3. **Ejercicio:** `-12 * { -7 + [ -4 * ( -6 ) + 5 + 12 ] + 15 }`
```

---

## 5. Estrategia de Estudio

> [!tip] 💡 Consejos del Profe Alex
> 1. **Copia con Minuciosidad:** La mayoría de los errores ocurren por copiar un `+` como `-`. Revisa cada línea como si fueras un detective.
> 2. **Identifica el "Lado Izquierdo":** Antes de romper un signo, pregúntate: "¿Tengo un signo o tengo un número?". Esto define si solo cambias el signo o si debes multiplicar valores.
> 3. **No saltes pasos:** Al principio, escribe la reducción (el número solo dentro del signo) antes de la eliminación. Esto evitará que te confundas con la ley de signos.
> 4. **Usa el dinero:** Si te confundes en las sumas, recuerda: **Positivo es lo que Tengo, Negativo es lo que Debo**. ¡Nunca falla!