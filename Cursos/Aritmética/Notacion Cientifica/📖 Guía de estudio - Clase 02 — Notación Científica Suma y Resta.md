# 📖 Guía de estudio — Clase 02: Suma y Resta en Notación Científica

> [!info] 📌 Conceptos clave para dominar el tema
> 1.  **Términos Semejantes:** ¡Es como el álgebra! Para sumar $3a + 5a = 8a$, las letras deben ser iguales. En notación científica, las potencias de 10 deben tener el **mismo exponente** ($10^k$) para poder operarse.
> 2.  **El "Truco" del Exponente Mayor:** Si los exponentes son distintos, convertimos el número con el exponente menor para que iguale al mayor. **¿Por qué?** Porque así el resultado final ya queda en notación científica y te ahorras un paso extra. ¡Es el secreto del Profe Alex para trabajar menos y mejor!
> 3.  **Ley de Compensación:** Para que el valor no cambie, debemos mantener el equilibrio. Si el exponente **sube** (se hace más grande), la coma se mueve a la **izquierda** (el número se achica). Si el exponente **baja**, la coma corre a la **derecha**.
> 4.  **Rigor en la Resta:** ¡Ojo aquí! En las restas es vital **completar con ceros** los espacios vacíos de los decimales. No te limites a "bajar" el número; alinea las comas y resta con cuidado.
> 5.  **Calculadora Científica:** No uses la tecla de potencia (`^`) para el $10$. Usa la tecla `EXP` o `x10ˣ`, que ya incluye la base 10. ¡Es más rápido y evita errores de sintaxis!

---

## Fórmulas y definiciones importantes

| Término | Lógica de la Regla |
| :--- | :--- |
| **Términos Semejantes** | Misma base y mismo exponente (ej. $10^4$ y $10^4$). |
| **Regla de la Coma ($\leftarrow$)** | Si sumas al exponente ($+$), el número se compensa achicándose (coma a la izquierda). |
| **Regla de la Coma ($\rightarrow$)** | Si restas al exponente ($-$), el número se compensa agrandándose (coma a la derecha). |
| **Notación Estándar ($10^0$)** | Un número sin potencia visible (como $3200$) tiene un exponente invisible: $10^0$. |

---

## Ejemplos resueltos con el método del Profe Alex

```ad-example
title: Ejemplo A — Caso básico (Exponentes iguales)
**Problema:** Sumar $3,2 \times 10^2 + 1,5 \times 10^2$

**Paso 1:** Los exponentes son iguales ($10^2$). Operamos directamente las mantisas.
**Paso 2:** Alineamos las comas verticalmente:
$$
\begin{matrix}
 & 3,2 \\
+ & 1,5 \\
\hline
 & 4,7
\end{matrix}
$$
**Paso 3:** Mantenemos la potencia de 10.
✅ **Resultado:** $4,7 \times 10^2$
```

```ad-example
title: Ejemplo B — Exponentes diferentes (Conversión y relleno de ceros)
**Problema:** Sumar $5,3 \times 10^5$ con $3200$ (que es $3200 \times 10^0$).

**Paso 1:** Identificar el exponente mayor. Es $5$.
**Paso 2:** Convertir $3200 \times 10^0$ a $10^5$. Como sumamos $5$ al exponente, movemos la coma $5$ veces a la izquierda: $0,032 \times 10^5$.
**Paso 3:** Sumar verticalmente **completando con ceros** para no perder la precisión:
$$
\begin{matrix}
 & 5,300 \\
+ & 0,032 \\
\hline
 & 5,332
\end{matrix}
$$
✅ **Resultado:** $5,332 \times 10^5$
```

```ad-example
title: Ejemplo C — Resta con resultado negativo
**Problema:** Calcular $0,172 \times 10^6 - 5,2 \times 10^6$

**Paso 1:** Los exponentes ya son iguales.
**Paso 2:** Determinar el signo. Como el número que resta ($5,2$) tiene mayor valor absoluto y es negativo, el resultado será **negativo**.
**Paso 3:** Restar el menor del mayor verticalmente, pidiendo prestado y rellenando ceros:
$$
\begin{matrix}
 & 5,200 \\
- & 0,172 \\
\hline
 & 5,028
\end{matrix}
$$
**Paso 4:** Aplicar el signo y la potencia.
✅ **Resultado:** $-5,028 \times 10^6$
```

---

## ⌨️ Tips para tu calculadora científica

*   **Uso de `EXP`:** Para escribir $5,3 \times 10^5$, presiona `5` `.` `3` `EXP` `5`. **No** presiones la tecla `x` (por) después del `EXP`.
*   **La tecla `ENG`:** Si tu resultado no está en la potencia que quieres, presiona `ENG`. Esta tecla cambia el exponente en múltiplos de 3 (notación de ingeniería). Para retroceder, usa `SHIFT` + `ENG`.
*   **Signo Negativo:** Usa la tecla `(-)` para exponentes o números negativos, y la tecla `-` solo para la operación de resta. ¡Tu calculadora te lo agradecerá!

---

## Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel Fácil (Operación directa)
1. $4,5 \times 10^3 + 2,1 \times 10^3$
2. $8,9 \times 10^5 - 3,4 \times 10^5$
3. $1,2 \times 10^{-2} + 4,5 \times 10^{-2}$
```

```ad-abstract
title: 🟡 Nivel Medio (Requiere igualar exponentes)
1. $5,3 \times 10^5 + 3,2 \times 10^2$ (Pista: el mayor es $5$, mueve la coma 3 veces en el segundo término).
2. $3,5 \times 10^{-2} - 2 \times 10^{-4}$ (Pista: $-2$ es mayor que $-4$. ¡Ojo con la recta numérica!).
3. $4,52 \times 10^4 + 3200$ (Convierte el número entero a potencia $10^4$ primero).
```

```ad-abstract
title: 🔴 Nivel Avanzado (Análisis y Aplicación)
1. **Finanzas:** Una empresa debe $5,2 \times 10^6$ USD y abona $1200000$ USD. Expresa el saldo restante en notación científica.
2. **Presupuestos:** Suma $0,5 \times 10^4$, $0,032 \times 10^4$ y $8,2 \times 10^4$.
3. **Lógica de Magnitud:** Resta $1,253 \times 10^3$ de una inversión de $0,02 \times 10^2$. ¿Quién es mayor? (Pista: Mira primero la potencia; si son distintas, iguálas para comparar las mantisas).
```

---

> [!tip] 💡 El Plan B: Método de Notación Estándar
> Si te sientes confundido con la coma en exponentes difíciles, usa el **Método 2**: convierte todo a números "largos" (decimales normales), suma o resta como siempre lo has hecho, y al final convierte el total a notación científica. 
> 
> *Recomendación:* Úsalo solo cuando los exponentes sean pequeños (entre $-10$ y $10$), ¡o terminarás escribiendo demasiados ceros! ¡Tú puedes, futuro genio de las mates!