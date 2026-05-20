# 📖 Guía de estudio — Clase 03: Factor común por agrupación de términos (Ejemplo 2)

> [!info] 📌 Conceptos clave
> 1.  **Cantidad de términos:** Este método se aplica cuando la expresión tiene un número par de términos (normalmente 4 o 6), lo que nos permite formar grupos de igual tamaño (2+2 o 3+3).
> 2.  **Descarte inicial:** Antes de agrupar, siempre verifica que NO exista un factor común global; es decir, algo que se repita en absolutamente todos los términos.
> 3.  **El objetivo final:** La meta es que, tras factorizar cada grupo por separado, obtengamos un "paréntesis idéntico" en ambos lados.
> 4.  **¡Cuidado con los signos!:** Si notas que los términos de tus paréntesis son iguales pero tienen signos opuestos, debes factorizar el $-1$ para "voltear" los signos y que todo coincida.

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Término** | Cada parte de una expresión separada por $+$ o $-$. |
| **Factor Común** | Es el número, letra o paréntesis que se repite. Ejemplo: $ab + ac = a(b+c)$. |
| **Agrupación** | Organizar términos en grupos que compartan un factor propio. Sin factor común interno, la agrupación no sirve. |

---

## Ejemplos Resueltos Adicionales

````ad-example | title: Ejemplo A — Factorización de 6 términos con ajuste de signo
**Ejercicio:** $2am - 2an + 2a - m + n - 1$

1.  **Agrupación:** Formamos dos grupos de tres términos porque notamos que el número $2$ y la letra $a$ se repiten al inicio:
    $(2am - 2an + 2a) + (-m + n - 1)$
2.  **Factorización del primer grupo:** Extraemos el factor común $2a$. 
    *Nota de Profe Alex:* ¿Por qué queda un $1$? Porque al dividir $2a \div 2a$, el resultado es **1**. ¡Nunca lo olvides!
    $2a(m - n + 1)$
3.  **¡Cuidado con los signos!:** El segundo grupo es $(-m + n - 1)$. Si comparas, tiene los mismos términos que nuestro paréntesis anterior pero con signos opuestos. Por eso, factorizamos el $-1$:
    $-1(m - n + 1)$
4.  **Resultado final:** Como los paréntesis son ahora idénticos, los extraemos como factor común:
    **(m - n + 1)(2a - 1)**
````

````ad-example | title: Ejemplo B — Agrupación por coeficientes y variables múltiples
**Ejercicio:** $3ax - 6a + 3ay - 2by - 2bx + 4b$

1.  **Organización:** Buscamos grupos con lógica numérica. Usamos la **descomposición en factores primos** para ver que los números $3, 6, 3$ tienen como Máximo Común Divisor (MCD) al $3$, mientras que $2, 2, 4$ tienen al $2$.
    $(3ax - 6a + 3ay) + (-2by - 2bx + 4b)$
2.  **Factorización local:**
    *   En el primer grupo, extraemos $3a$: $3a(x - 2 + y)$.
    *   En el segundo grupo, extraemos $-2b$ para que los signos internos cambien y coincidan con el primero: $-2b(y + x - 2)$.
3.  **Verificación:** Nota que $(x - 2 + y)$ es lo mismo que $(y + x - 2)$ porque el orden de los sumandos no altera el resultado (propiedad conmutativa). 
4.  **Resultado final:** Unificamos el paréntesis común y lo que quedó fuera:
    **(x + y - 2)(3a - 2b)**
````

---

## Ejercicios de Repaso

````ad-abstract | title: 🟢 Nivel: Fácil (Agrupación simple)
1. $am + an + bm + bn$
2. $3x + 3y + ax + ay$
3. $2a + 2b + ma + mb$
````

````ad-abstract | title: 🟡 Nivel: Medio (Cambio de signo necesario)
1. $4ax - 4ay - x + y$ *(Pista: Factoriza el $-1$ en el segundo grupo).*
2. $5m - 5n - am + an$
3. $x^2 - x - ax + a$
````

````ad-abstract | title: 🔴 Nivel: Avanzado (Aplicación con $USD)
*Instrucción: Los coeficientes representan valores en dólares. Agrupa los gastos e ingresos según su variable.*
1. $\$3ax - \$6a + $\$3ay - \$2by - \$2bx + \$4b$
2. $\$2am - \$2an + \$2a - \$1m + \$1n - \$1$
3. $\$10xa - \$5xb + \$6ya - \$3yb$
````

---

> [!tip] 💡 Consejo de estudio
> La clave para saber si tu agrupación es correcta es observar los paréntesis. Si son idénticos, vas por buen camino **porque** eso te permite hacer el último paso. Si no son iguales ni factorizando el signo menos, intenta agrupar los términos de una forma distinta.

> [!info] 🚀 ¿Qué sigue?
> Si alguna vez te encuentras con solo **dos términos** que se están restando y ambos tienen raíz cuadrada exacta, ¡estarás frente a una **Diferencia de Cuadrados**! Prepárate, porque ese es nuestro próximo tema.