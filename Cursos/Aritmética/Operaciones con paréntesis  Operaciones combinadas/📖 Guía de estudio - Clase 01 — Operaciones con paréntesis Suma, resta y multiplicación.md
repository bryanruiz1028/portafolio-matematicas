# 📖 Guía de estudio — Clase 01: Operaciones con Paréntesis

> [!info] 📌 Conceptos clave
> *   **El signo como "orden":** El signo a la izquierda del paréntesis da una instrucción. Un **signo positivo (+)** ordena mantener el número interno igual; un **signo negativo (-)** ordena cambiar el signo de lo que está adentro.
> *   **Regla de signos seguidos:** Cuando dos signos quedan juntos al eliminar el paréntesis: signos iguales se transforman en **positivo (+)** y signos diferentes en **negativo (-)**.
> *   **Multiplicación implícita:** Si hay un número pegado al paréntesis sin un signo (+ o -) de por medio, indica una **multiplicación**.
> *   **Jerarquía de operaciones:** Antes de eliminar paréntesis, siempre se deben resolver las operaciones que estén dentro de ellos.
> *   **Orden de resolución:** Primero se resuelven los paréntesis (lo interno), luego las multiplicaciones y, finalmente, las sumas y restas.

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Signo positivo antes** | $+(a) = a$ / $+(-a) = -a$. El contenido no cambia. |
| **Signo negativo antes** | $-(a) = -a$ / $-(-a) = a$. El contenido cambia de signo. |
| **Multiplicación implícita** | $n(a)$ significa $n \times a$. **Importante:** Se multiplica el número incluyendo su propio signo. |
| **Regla de signos** | Signos iguales: $(+)(+)$ o $(-)(-)$ dan **+**. <br> Signos diferentes: $(+)(-)$ o $(-)(+)$ dan **-**. |

## Ejemplos Resueltos Adicionales

```ad-example
**Ejemplo A: Caso Básico (Eliminación con signo negativo)**
**Problema:** Resolver la operación $-5 - (-3)$

*   **Paso 1:** Identificamos el signo a la izquierda del paréntesis. Es un negativo ($-$). Esta es la "orden" para cambiar lo de adentro.
*   **Paso 2:** Quitamos el paréntesis y transformamos el $-3$ en **$+3$**.
*   **Paso 3:** Aplicamos la lógica de "debo/tengo". Si debo 5 y ahora tengo 3, pago mi deuda y quedo debiendo 2.
**Resultado:** $-2$
```

```ad-example
**Ejemplo B: Aplicación Real ($USD)**
**Contexto:** Tienes una deuda de $7 ($-7$) y decides sumar otra deuda de $2 ($+(-2)$). ¿Cuál es tu saldo final?
**Operación:** $-7 + (-2)$

*   **Paso 1:** El signo positivo ($+$) afuera indica que el valor interno mantiene su signo.
*   **Paso 2:** Al eliminar el paréntesis, la operación queda: $-7$ **$- 2$**.
*   **Paso 3:** Interpretamos el dinero: "Debo $7 y debo otros $2". Esto resulta en una deuda total de **$9 USD**.
**Resultado:** $-\$9$
```

## Ejercicios de Repaso

```ad-abstract
**🟢 Nivel Fácil: Eliminación Simple**
1. $+( -8 )$
2. $- ( +10 )$
3. $- ( -15 )$
```

```ad-abstract
**🟡 Nivel Medio: Operación Interna Primero**
1. $+( -5 + 8 )$
2. $-( 10 - 12 )$
3. $- ( -7 - 2 )$
```

```ad-abstract
**🔴 Nivel Avanzado: Aplicación con $USD**
1. Tienes 3 deudas de $7 cada una. Exprésalo como $3( -7 )$ y calcula el total.
2. Tienes un ingreso de $50 y debes restar 2 gastos (compras) de $15 cada uno: $50 + 2( -15 )$.
3. Un banco te anula 4 cobros pendientes de $5 cada uno ($-4 \times -5$), pero luego realizas 2 compras de $3 cada una ($+2 \times -3$). ¿Cuál es tu saldo final? 
*(Pista: $-4(-5) + 2(-3)$)*
```

> [!tip] 💡 Consejo de estudio
> Para mantener la claridad y evitar errores visuales, **resuelve siempre hacia abajo**, alineando los signos iguales uno debajo del otro. Antes de operar, detente un segundo e identifica qué hay exactamente a la izquierda del paréntesis: si es solo un signo, aplicas la regla de cambio; si es un número, recuerda que debes multiplicar ese número (con todo y su signo) por lo que está adentro.