# 📖 Guía de estudio — Clase 02: Probabilidad de un evento simple

> [!info] 📌 Conceptos clave
> La **probabilidad** es la herramienta matemática que nos permite medir qué tan posible es que ocurra un evento al azar. Se basa en los siguientes pilares:
> * **Medida de posibilidad:** Es un valor numérico que indica la frecuencia con la que puede ocurrir un resultado bajo condiciones de azar.
> * **Regla de Laplace:** Es la fórmula principal para calcular probabilidades en eventos simples.
> * **Representación múltiple:** El resultado puede expresarse como **fracción** (simplificada), **decimal** (resultado de la división) y **porcentaje**.
> * **Límites de probabilidad:** Un evento **imposible** tiene probabilidad $0$ ($0\%$), mientras que un evento **seguro** tiene probabilidad $1$ ($100\%$).

---

## 2. Tabla de Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Regla de Laplace** | $P(A) = \frac{\text{Casos favorables}}{\text{Casos posibles}}$ |
| **Regla de la Suma ("O")** | En probabilidad, la letra "o" indica suma. Si los eventos son mutuamente excluyentes: $P(A \text{ o } B) = P(A) + P(B)$. |
| **Espacio Muestral** | Es el conjunto de todos los resultados posibles de un experimento (ej. los números del $1$ al $6$ en un dado). En la fórmula, representa el denominador. |
| **Evento Simple** | Un acontecimiento con un único resultado posible dentro de un experimento (ej. que salga "cara" en una moneda). |
| **Probabilidad en Porcentaje** | Se obtiene multiplicando el decimal por $100$, lo que equivale a **correr la coma dos lugares hacia la derecha**. |

---

## 3. Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A: Lanzamiento de un dado (Números Primos)
**Escenario:** Se lanza un dado de seis caras ($1, 2, 3, 4, 5, 6$). ¿Cuál es la probabilidad de obtener un número primo?

**Paso a paso:**
1. **Identificar casos totales:** Un dado tiene $6$ caras, por lo tanto, el espacio muestral es $6$.
2. **Identificar casos favorables:** Los números primos en un dado son $2, 3$ y $5$. Son $3$ casos favorables.
3. **Aplicar la fórmula:** $P(\text{primo}) = \frac{3}{6}$.
4. **Simplificar:** Dividiendo ambos por $3$, obtenemos $P = \frac{1}{2}$.
5. **Convertir a porcentaje:** $\frac{1}{2} = 0.5$. Corremos la coma dos lugares: $0.5 \times 100 = 50\%$.

**Resultado:** Tienes un $50\%$ de probabilidad de obtener un número primo.
```

```ad-example
title: Ejemplo B: Aplicación Real (Rifa Escolar $)
**Escenario:** Una rifa escolar tiene $50$ boletos en una caja. Solo $5$ boletos tienen un premio de $\$20$ USD. ¿Cuál es la probabilidad de sacar un boleto premiado?

**Paso a paso:**
1. **Identificar casos totales:** Hay $50$ boletos en total (denominador).
2. **Identificar casos favorables:** Hay $5$ boletos con premio (numerador).
3. **Aplicar la fórmula:** $P(\text{premio}) = \frac{5}{50}$.
4. **Simplificar:** Dividiendo entre $5$, obtenemos $P = \frac{1}{10}$.
5. **Convertir a porcentaje:** $1 \div 10 = 0.1$. Multiplicamos por $100$: $0.1 \times 100 = 10\%$.

**Resultado:** La probabilidad de ganar los $\$20$ USD es del $10\%$.
```

---

## 4. Ejercicios de Repaso

```ad-abstract
title: 🟢 Bloque Fácil (Iniciación)
1. **Dados:** Si lanzas un dado de $6$ caras, ¿cuál es la probabilidad de sacar un número menor a $3$?
2. **Baraja:** De una baraja inglesa de $52$ cartas, ¿cuál es la probabilidad de extraer un As? (Hay $4$ ases en total).
3. **Evento Seguro:** Si lanzas un dado de $6$ caras, ¿cuál es la probabilidad de obtener un número menor a $7$? Exprésalo en porcentaje.
```

```ad-abstract
title: 🟡 Bloque Medio (Suma de Probabilidades)
*Recordatorio: La "o" significa sumar los casos favorables.*
1. **Urna de colores:** En una urna hay $4$ bolas rojas, $2$ azules y $1$ amarilla (Total: $7$). ¿Cuál es la probabilidad de sacar una bola **roja o azul**?
2. **Cartas:** En una baraja de $52$ cartas, ¿cuál es la probabilidad de sacar una carta de **corazones o de picas**? (Cada palo tiene $13$ cartas).
3. **Dados:** Al lanzar un dado, ¿cuál es la probabilidad de que salga un **1 o un 6**?
```

```ad-abstract
title: 🔴 Bloque Avanzado (Aplicación Técnica y $)
1. **La Tómbola:** Una tómbola tiene $20$ canicas: $2$ doradas (premio $\$50$), $8$ plateadas (premio $\$10$) y $10$ blancas (sin premio).
   * a) ¿Cuál es la probabilidad en porcentaje de ganar los $\$50$?
   * b) ¿Cuál es la probabilidad en porcentaje de ganar los $\$10$?
2. **Cartas con Letras:** De una baraja de $52$ cartas, ¿cuál es la probabilidad de extraer una carta que tenga una **letra** ($A, J, Q, K$)? Recuerda que hay $4$ de cada una. Expresa el resultado en fracción simplificada y porcentaje.
3. **Caja de Canicas:** Una caja tiene $10$ canicas. Si sacas una verde ganas $\$5$ USD. Hay $4$ canicas verdes. Expresa la probabilidad en fracción simplificada, decimal y porcentaje.
```

---

## 5. Consejo de Estudio

> [!tip] 💡 Verificación del "Profe Alex"
> Para asegurar que tu cálculo es correcto, sigue estos pasos antes de entregar:
> 1. **La Regla del Denominador:** El número de abajo siempre debe ser mayor o igual al de arriba. Si el numerador es más grande, ¡revisa tu conteo!
> 2. **El Rango Decimal:** El resultado de la división siempre debe estar entre $0$ y $1$. Si obtienes algo como $1.5$, el ejercicio está mal planteado.
> 3. **Simplificación:** Antes de dividir, verifica si ambos números se pueden dividir por $2, 3$ o $5$. Una fracción pequeña como $\frac{1}{2}$ es mucho más fácil de convertir a $0.5$ que $\frac{26}{52}$.