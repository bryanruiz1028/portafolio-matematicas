# 📖 Guía de estudio — Clase 01: Introducción a los Intervalos y su Representación

> [!info] Conceptos fundamentales
> 
> - **¿Qué es un intervalo?**: Es la representación de un subconjunto o una parte específica de los números reales.
> - **La densidad de los números reales (El efecto "Zoom")**: A diferencia de los números enteros, entre dos números reales (como el 1 y el 2) existe una **infinidad de valores** (1.1, 1.01, 1.001...). Como no existe un número "siguiente" al 1 que podamos definir con exactitud, necesitamos los intervalos para agrupar todos esos valores infinitos.
> - **Inclusión vs. Exclusión**: Usamos corchetes `[]` para indicar que el extremo **sí** está incluido (se grafica con punto relleno). Usamos paréntesis `()` o corchetes invertidos `][` para indicar que el extremo **no** está incluido (se grafica con punto hueco).
> - **La naturaleza del infinito**: El símbolo $\infty$ (ya sea positivo o negativo) representa valores que no tienen fin. Por convención, siempre se acompaña de un **paréntesis abierto**, ya que al no ser un número concreto, el intervalo nunca puede "cerrarse" en él.
> - **Tipos de intervalos**: Pueden ser abiertos, cerrados o semiabiertos (ya sea a la izquierda o a la derecha).

## Fórmulas y definiciones importantes

| Término | Definición / Notación | Significado Visual |
| :--- | :--- | :--- |
| **Intervalo** | Un grupo o porción de la recta real. | Un segmento sombreado que conecta dos puntos. |
| **Intervalo Cerrado** | `[a, b]` | Incluye ambos extremos; se usan **puntos rellenos** en los límites. |
| **Intervalo Abierto** | `(a, b)` o `]a, b[` | No incluye los extremos; se usan **puntos huecos** (bolitas sin rellenar). |
| **Semiabierto a la izquierda** | `(a, b]` o `]a, b]` | No incluye el extremo izquierdo, pero sí el derecho (punto hueco y punto relleno). |
| **Semiabierto a la derecha** | `[a, b)` o `[a, b[` | Incluye el extremo izquierdo, pero no el derecho (punto relleno y punto hueco). |
| **Infinito** | `∞` | Representa continuidad sin fin; la gráfica termina en una **flecha**. |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Representación de un intervalo semiabierto
**Enunciado:** Representar el intervalo de números mayores o iguales a -3 y menores que 2.

1. **Identificar extremos:** Los límites son -3 y 2.
2. **Determinar símbolos:** "Mayor o igual" significa que el -3 está incluido (corchete `[`). "Menor que" significa que el 2 no está incluido (paréntesis `)`).
3. **Notación de conjunto:** $\{x \mid -3 \leq x < 2\}$
4. **Notación de intervalo:** `[-3, 2)` o `[-3, 2[`
5. **Resultado visual:** En la recta numérica, dibujamos un **punto relleno** sobre el -3 y un **punto hueco** sobre el 2, conectándolos con un **segmento sombreado**.
```

```ad-example
title: Ejemplo B — Aplicación Real $USD
**Enunciado:** Un videojuego cuesta más de $10 USD pero no más de $50 USD. Expresa el rango de precios como intervalo.

*   **Paso 1:** Traducimos "más de 10" como una condición de exclusión: $x > 10$. El precio no puede ser exactamente 10.
*   **Paso 2:** Traducimos "no más de 50" como una condición de inclusión: $x \leq 50$. El precio puede ser 50 pero no superarlo.
*   **Resultado:** El intervalo de presupuesto es **`(10, 50]`** o **`]10, 50]`**.
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
1. Clasifica el intervalo `(5, 8)`: ¿Es abierto, cerrado o semiabierto?
2. Si un intervalo es `(2, 10]`, ¿el número 10 forma parte del conjunto? ¿Por qué?
3. Escribe la notación de intervalo para: "Todos los números reales entre 1 y 4, incluyendo a ambos".
```

```ad-abstract
title: 🟡 Medio
1. Convierte la desigualdad $x > -5$ a notación de intervalo (recuerda usar el infinito).
2. Describe la gráfica de `[-2, 3)`: ¿Qué tipo de punto lleva cada extremo y hacia dónde va el segmento?
3. Si tienes la expresión $15 > x$, ordénala para que la $x$ quede a la izquierda y escribe su intervalo.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
**Enunciado:** Una cuenta de ahorros cobra comisión si el saldo es **estrictamente menor** a $100 USD ($s < 100$). Una persona tiene un saldo $s$ que se encuentra en el rango donde **no paga comisión**, y su contrato establece un saldo máximo permitido de $5000 USD. 

*   **Reto:** Expresa el rango del saldo $s$ (que no paga comisión) utilizando tanto la notación de intervalo como la de desigualdad.
```

> [!tip] Consejo de estudio
> 
> ¡No dejes que los signos te confundan! Recuerda el truco de la **"boca"** de la desigualdad: la abertura siempre "se come" al número más grande. Para leer los intervalos correctamente, acostúmbrate a poner siempre la variable $x$ a la izquierda. Si tienes $10 > x$, simplemente dale la vuelta a todo (incluyendo el signo) para leerlo como $x < 10$ ("los números menores que 10"). ¡Es mucho más intuitivo para graficar!