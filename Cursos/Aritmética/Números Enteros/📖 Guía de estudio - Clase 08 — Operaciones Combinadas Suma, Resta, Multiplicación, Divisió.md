# 📖 Guía de estudio — Clase 08: Operaciones Combinadas

> [!info] 📌 Conceptos clave
> Para resolver correctamente ejercicios con múltiples operaciones, los matemáticos utilizamos un orden de prioridad que evita confusiones. Sigue siempre estos pasos:
> 1. **Paréntesis:** Se resuelven primero todas las operaciones dentro de ellos. Si hay varios signos de agrupación, trabajamos siempre de **adentro hacia afuera**.
> 2. **Potencias y Raíces:** Una vez liberados los paréntesis, resolvemos estas operaciones antes que cualquier otra.
> 3. **Multiplicación y División:** Se ejecutan en el tercer nivel. ¡Cuidado! Si aparecen ambas en la misma línea, debemos resolverlas **de izquierda a derecha**.
> 4. **Suma y Resta:** Es el nivel final. Al igual que el anterior, si hay varias seguidas, las resolvemos **de izquierda a derecha**.

---

## FÓRMULAS Y DEFINICIONES IMPORTANTES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Paréntesis** | Representan el primer nivel de prioridad. Debemos resolver lo que está contenido en ellos para "simplificar" la expresión. |
| **Potencias y Raíces** | Segundo nivel de jerarquía. ¡No caigas en la trampa! Recuerda que `$5^2$` no es `$5 \times 2 = 10$`, sino `$5 \times 5 = 25$`. |
| **Multiplicación y División** | Tercer nivel de prioridad. Si coinciden en rango, se resuelven de izquierda a derecha. Nota: El símbolo `$\div$` es común en regiones como España para representar la división. |
| **Suma y Resta** | Nivel final de la jerarquía. Solo se realizan cuando hemos despejado todas las operaciones de los niveles superiores, siempre de izquierda a derecha. |

---

## EJEMPLOS RESUELTOS ADICIONALES

```ad-example
**Ejemplo A: Caso Básico**
**Ejercicio:** `$14 \div (3+4) + 9 - 10 \div 2$`

Vamos a resolver paso a paso para no perdernos:
- **Paso 1 (Paréntesis):** Primero resolvemos la suma interna `$(3+4) = 7$`. La expresión ahora es: `$14 \div 7 + 9 - 10 \div 2$`.
- **Paso 2 (Divisiones):** Ahora buscamos divisiones y multiplicaciones de izquierda a derecha.
    - `$14 \div 7 = 2$`
    - `$10 \div 2 = 5$`
    - La expresión se simplifica a: `$2 + 9 - 5$`.
- **Paso 3 (Sumas y Restas):** Finalmente, operamos de izquierda a derecha.
    - `$2 + 9 = 11$`
    - `$11 - 5 = 6$`
**Resultado final:** `$6$`
```

```ad-example
**Ejemplo B: Aplicación real ($USD)**
**Contexto:** Imagina que estamos gestionando tus finanzas personales del mes:
1. Compras `$3$` cajas de chocolates a `$8$` cada una (`$3 \times 8$`).
2. Recibes una bonificación de `$63$` que se reparte equitativamente en `$9$` meses (`$63 \div 9$`).
3. Pagas una de las 2 cuotas de una deuda total de `$8$` (`$- 8 \div 2$`).
4. Encuentras un billete de `$7$` en tu bolsillo (`$+ 7$`).

**Operación:** `$3 \times 8 + 63 \div 9 - 8 \div 2 + 7$`

- **Paso 1 (Multiplicación y Divisiones):** Resolvemos primero los productos y cocientes.
    - `$3 \times 8 = 24$`
    - `$63 \div 9 = 7$`
    - `$8 \div 2 = 4$`
    - La expresión queda: `$24 + 7 - 4 + 7$`.
- **Paso 2 (Sumas y Restas):** Operamos en orden de aparición.
    - `$24 + 7 = 31$`
    - `$31 - 4 = 27$`
    - `$27 + 7 = 34$`
**Resultado final:** `$34$` USD
```

---

## EJERCICIOS DE REPASO

```ad-abstract
**Nivel Verde (Fácil)**
Demuestra que dominas la prioridad básica resolviendo la siguiente operación:
**Ejercicio:** `$5 + 4 \times 2 - 3$`
*Sugerencia: Recuerda que la multiplicación "pesa más" que la suma y la resta.*

<details>
<summary><b>Ver Clave de Respuesta</b></summary>
Paso 1: $5 + 8 - 3$ <br>
Paso 2: $13 - 3$ <br>
<b>Resultado: $10$</b>
</details>
```

```ad-abstract
**Nivel Amarillo (Medio)**
Subimos un poco el nivel incluyendo paréntesis y divisiones:
**Ejercicio:** `$(3+7) \times 4 - 20 \div 5 + 1$`

<details>
<summary><b>Ver Clave de Respuesta</b></summary>
Paso 1 (Paréntesis): $10 \times 4 - 20 \div 5 + 1$ <br>
Paso 2 (Multiplicación y División): $40 - 4 + 1$ <br>
Paso 3 (Suma y Resta de izquierda a derecha): $36 + 1$ <br>
<b>Resultado: $37$</b>
</details>
```

```ad-abstract
**Nivel Rojo (Avanzado - Presupuesto en $USD)**
Calcula el saldo final de un presupuesto considerando estos movimientos:
- Tienes un ahorro inicial de `$5^2$`.
- Sumas una ganancia por consultoría de `$3 \times 3$`.
- Restas el costo de una herramienta que vale `$\sqrt{9}$`.
- Sumas un reembolso de `$3 \times 2$`.

**Operación a resolver:** `$5^2 + 3 \times 3 - \sqrt{9} + 3 \times 2$`

<details>
<summary><b>Ver Clave de Respuesta</b></summary>
Paso 1 (Potencias y Raíces): $25 + 3 \times 3 - 3 + 3 \times 2$ <br>
Paso 2 (Multiplicaciones): $25 + 9 - 3 + 6$ <br>
Paso 3 (Suma y Resta): $34 - 3 + 6 = 31 + 6$ <br>
<b>Resultado: $37$ USD</b>
</details>
```

---

> [!tip] 💡 Consejo de estudio
> Como bien dice el "profe Alex", la clave para no equivocarse nunca es **no saltarse pasos**. Aunque sientas que puedes hacerlo mentalmente, resuelve solo una operación a la vez y **copia todo lo demás exactamente igual** en el renglón de abajo. Mantener el orden visual es la mejor defensa contra los errores de signos y jerarquía.