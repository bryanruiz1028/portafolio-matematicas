# 📖 Guía de estudio — Clase 03: Operaciones Combinadas

> [!info] 📌 Conceptos clave
> Para resolver correctamente ejercicios con múltiples operaciones, debemos seguir un orden estricto llamado **jerarquía de operaciones**. Saltarse este orden es el error más común en matemáticas.
> 
> 1.  **Operaciones dentro de paréntesis:** Es el primer punto de ataque.
>     *   **⭐ Sub-regla de Oro:** Si dentro de un paréntesis hay varias operaciones, debemos aplicar la misma jerarquía interna (primero potencias, luego multiplicaciones, etc.).
> 2.  **Potencias y raíces:** Se resuelven una vez despejados los paréntesis.
> 3.  **Multiplicaciones y divisiones:** Tienen la misma prioridad entre ellas, pero se resuelven siempre antes que cualquier suma o resta.
> 4.  **Sumas y restas:** Es el paso final. Aquí es donde determinamos el resultado definitivo.

---

## 2. Fórmulas y Definiciones Importantes

| Término | Definición / Regla |
| :--- | :--- |
| **Jerarquía de operaciones** | El camino obligatorio para resolver ejercicios con diversos signos. Sin este orden, el resultado será incorrecto. |
| **Símbolo de división ($\div$)** | Representa la división. Aunque en algunos países se usa el símbolo $:$, en otros como España es muy común ver el óbelo ($\div$). |
| **Multiplicación implícita** | Ocurre cuando un número está pegado a un paréntesis o raíz sin un signo visible (ej. $3(2)$ o $2\sqrt{16}$). **¡Cuidado!** Muchos estudiantes olvidan que aquí hay un "por" invisible y fallan al no escribirlo en el siguiente paso. |
| **Ley de signos** | Regla aplicada **exclusivamente** en multiplicación y división (ej. menos por más da menos). **NUNCA** la uses para sumar o restar. |
| **Suma/Resta (Debo vs. Tengo)** | La lógica para el paso final: los números negativos son lo que "debo" y los positivos lo que "tengo". Esta técnica evita confusiones con la ley de signos. |

---

## 3. Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A — Jerarquía Básica (Paréntesis y División)
**Ejercicio:** $14 \div (3 + 4) + 9 - 10 \div 2$

1. **Prioridad 1: Eliminando Paréntesis**
   Resolvemos la operación interna: $(3 + 4) = 7$.
   El ejercicio queda: $14 \div (7) + 9 - 10 \div 2$
   *Nota didáctica:* Al quedar un solo número, el paréntesis ya no indica una operación interna, por lo que $14 \div (7)$ es exactamente lo mismo que $14 \div 7$.

2. **Prioridad 2: Multiplicaciones y Divisiones**
   ¡Cuidado aquí! No sumes el 7 con el 9. Primero resolvemos las divisiones:
   - $14 \div 7 = 2$
   - $10 \div 2 = 5$
   Ahora tenemos: $2 + 9 - 5$

3. **Prioridad 3: Sumas y Restas (Tengo vs. Debo)**
   - Tengo $2$ y tengo $9$, en total **tengo $11$**.
   - Como debo $5$, pago con mis $11$ y me quedan $6$.
   $11 - 5 = 6$

**Resultado final: 6**
```

```ad-example
title: Ejemplo B — Aplicación en Compras ($USD)
**Contexto:** Un comerciante compra 3 artículos de $8 cada uno. Luego, recibe un premio de una bonificación de $63 que se reparte entre 9 personas. Después, paga una deuda de $8 que comparte con un socio (dividida entre 2) y, finalmente, encuentra $7 en su abrigo.

**Planteamiento:** $3 \times 8 + 63 \div 9 - 8 \div 2 + 7$

**Paso 1: Aplicamos la técnica del subrayado**
Como recomienda el Profe Alex, subrayamos primero multiplicaciones y divisiones para no tocarlas con las sumas antes de tiempo:
$\underline{3 \times 8} + \underline{63 \div 9} - \underline{8 \div 2} + 7$

**Paso 2: Resolvemos lo subrayado**
- Compra: $24$
- Premio: $7$
- Deuda: $4$
Queda la expresión: $24 + 7 - 4 + 7$

**Paso 3: Saldo Final (Sumas y restas)**
- $24 + 7 = 31$
- $31 - 4 = 27$
- $27 + 7 = 34$

**Resultado final: $34 USD**
```

---

## 4. Ejercicios de Repaso

```ad-abstract
title: 🟢 Fácil
**Nivel: Iniciación**
Resuelve el siguiente ejercicio de práctica del Video 1:
$4 + (3 + 7) \times 4 - 20 \div 5 + 7$
*Recuerda: El paréntesis es tu primera prioridad. Luego, ataca la multiplicación y la división antes de sumar.*
```

```ad-abstract
title: 🟡 Medio
**Nivel: Intermedio**
Resuelve integrando potencias y raíces:
$5^2 - 2\sqrt{16} + 36 \div 3 - 2 \times 3 \times 5$
*Pista del Especialista: Identifica la multiplicación implícita en $2\sqrt{16}$. Primero halla la raíz y luego multiplícala por 2.*
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
**Nivel: Desafío Profe Alex**
Una empresa calcula su saldo de cierre con la siguiente operación compleja:
$10 \times \sqrt{4} \times \sqrt[3]{8} - (25 - 7) + (20 \div 2^2)$

**Pista para el éxito:** Dentro del último paréntesis, tienes una división y una potencia ($2^2$). Siguiendo la jerarquía, ¡debes resolver la potencia antes de poder dividir!
```

---

## 5. Consejo de Estudio

> [!tip] 💡 La estrategia del color
> Para no caer en la "trampa de la suma temprana", haz lo que hace el Profe Alex: antes de empezar a calcular, toma un **lápiz de color o un resaltador** y subraya únicamente las multiplicaciones y divisiones. Esto visualmente te recordará que esos bloques están "unidos" y no puedes sumarlos a los números vecinos hasta que hayas resuelto esa operación. ¡Es el método más seguro para no fallar!