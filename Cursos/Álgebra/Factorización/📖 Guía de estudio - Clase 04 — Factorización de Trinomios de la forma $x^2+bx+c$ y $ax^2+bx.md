# 📖 Guía de estudio — Clase 04: Factorización de Trinomios de la forma $x^2 + bx + c$

> [!info] 📌 Conceptos clave
> ¡Hola, amigos! Antes de empezar a factorizar, debemos asegurarnos de que nuestro trinomio cumpla con estas condiciones fundamentales:
> - **Identificación:** La expresión debe tener exactamente $3$ términos. ¡Recuerda que no todos los trinomios se pueden factorizar por este método!
> - **Ordenamiento:** Los términos deben estar organizados de forma descendente: primero el término con el exponente mayor, luego el de la mitad y al final el término independiente.
> - **Coeficiente principal:** El primer término (el de mayor exponente) debe tener un coeficiente de $1$. Si el término es negativo (ej. $-x^2$), primero debemos factorizar el signo $-1$ para dejarlo positivo.
> - **Validación de exponentes:** El exponente del primer término debe ser exactamente el **doble** del exponente del segundo término (por ejemplo: $x^2$ y $x^1$, o $x^6$ y $x^3$).

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Trinomio ordenado** | Secuencia de términos siguiendo el orden: $x^{2n}$, $x^n$ y el término independiente ($x^0$ o número sin letra). |
| **Raíz del primer término** | Se calcula la raíz cuadrada del primer término (ej. $\sqrt{x^2} = x$ o $\sqrt{x^6} = x^3$) y se distribuye como el primer elemento en ambos paréntesis. |
| **Ley de signos** | El signo del primer paréntesis es el signo del **segundo término**. El signo del segundo paréntesis es el **producto** de los signos del segundo y tercer término. |
| **Validación de factores** | Se buscan dos números que multiplicados den el término independiente ($c$) y que sumados o restados (según los signos de los paréntesis) den el coeficiente central ($b$). |

> [!example] Ejemplo A — Caso básico
> **Problema:** Factorizar el trinomio $x^2 + 5x + 6$
> 
> **Paso a paso:**
> 1. **Preparación:** Abrimos dos paréntesis $( \quad )( \quad )$.
> 2. **Raíz cuadrada:** Calculamos $\sqrt{x^2} = x$. Lo colocamos al inicio de cada paréntesis: $(x \quad )(x \quad )$.
> 3. **Signos:** 
>    - En el primer paréntesis va el signo del segundo término: $(+)$.
>    - En el segundo paréntesis va el producto de los signos ($+ \cdot + = +$): $(x + \quad )(x + \quad )$.
> 4. **Búsqueda de números:** Necesitamos dos números que multiplicados den $6$ y que, al tener signos iguales, **sumados** den $5$.
>    - Los números son $3$ y $2$ ($3 \cdot 2 = 6$ y $3 + 2 = 5$).
> 
> **Resultado:** $(x + 3)(x + 2)$

> [!example] Ejemplo B — Aplicación de área y presupuesto
> **Enunciado:** El área de un terreno rectangular es $x^2 - 2x - 15$ metros cuadrados. Determina sus dimensiones y el costo de cercarlo si cada metro lineal de malla cuesta $\$10$ USD.
> 
> **Resolución:**
> 1. **Factorización:** 
>    - Raíz de $x^2$ es $x$.
>    - Signos: primero $(-)$, segundo $(- \cdot - = +)$. Tenemos $(x - \quad )(x + \quad )$.
>    - Buscamos números que multiplicados den $15$ y **restados** (signos diferentes) den $2$. Los números son $5$ y $3$.
>    - **Dimensiones:** El largo es $(x + 3)$ y el ancho es $(x - 5)$.
> 2. **Cálculo de costo ($USD):**
>    - El perímetro es la suma de sus lados: $P = 2((x + 3) + (x - 5)) = 2(2x - 2) = 4x - 4$ metros.
>    - Si el costo es de $\$10$ USD por metro, el presupuesto total es: $10 \cdot (4x - 4) = 40x - 40$ USD.
> 
> **Resultado final:** Las dimensiones son $(x - 5)$ y $(x + 3)$. El costo total está dado por la expresión $40x - 40$ USD.

> [!abstract] 🟢 Fácil
> Factoriza estos trinomios simples (¡ánimo, tú puedes!):
> 1. $x^2 + 7x + 10$
> 2. $x^2 + 3x + 2$
> 3. $x^2 + 8x + 15$

> [!abstract] 🟡 Medio
> Aplica la lógica de exponentes mayores y ordenamiento:
> 1. $m^4 - 3m^2 - 10$
> 2. $x^6 + 7x^3 - 8$
> 3. $y^2 - 14y - 120$ *(Pista: usa descomposición en factores primos para el $120$)*.

> [!abstract] 🔴 Avanzado — Aplicación con $USD
> **Problema:** Un analista financiero descubre que la utilidad de una empresa está representada por $-a^2 - 14a + 120$. 
> 1. Factoriza la expresión (recuerda extraer primero el signo negativo: $-1(a^2 + 14a - 120)$).
> 2. Si uno de los factores resultantes representa el costo por unidad en USD y el otro la cantidad de unidades, ¿cuáles son esos factores? 
> 3. Si $a = 5$, ¿cuál es el valor monetario de cada factor?

> [!tip] 💡 Consejo de estudio
> Siguiendo el método del **Profe Alex**, coloca siempre el **número mayor en el primer paréntesis**. Al hacer esto, te aseguras de que el signo del término central se mantenga correctamente de forma automática, evitando confusiones cuando los signos de los paréntesis son diferentes. ¡Es un truco infalible para no fallar!