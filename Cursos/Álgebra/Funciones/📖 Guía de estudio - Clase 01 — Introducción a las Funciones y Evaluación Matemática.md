# 📖 Guía de estudio — Clase 01: ¿Qué es una Función?

¡Qué tal, amigas y amigos! Espero que estén muy bien. En esta guía vamos a descubrir qué es realmente una función. Olvida por un momento las fórmulas complicadas; vamos a entenderlo paso a paso, como si estuviéramos frente a una máquina mágica.

> [!info] 📌 Conceptos clave
> 1.  **La Metáfora de la Máquina:** Imagina una máquina a la que le ingresas un objeto (entrada) y ella realiza un proceso para entregarte algo transformado (salida). Por ejemplo, una máquina que recibe un auto blanco y lo "pinta de azul". En matemáticas, las funciones son máquinas que reciben números ($x$), les aplican una regla y devuelven un resultado único ($y$).
> 2.  **Definición de Función:** Es una asociación entre dos conjuntos ($A$ y $B$) donde a cada elemento del primer conjunto le corresponde un **único** elemento del segundo. ¡Piénsalo así!: de cada número de entrada solo puede salir una "flecha" hacia un resultado.
> 3.  **Variables:**
>     *   **Variable Independiente ($x$):** Es el valor que nosotros elegimos ingresar a la máquina. ¡No depende de nadie!
>     *   **Variable Dependiente ($y$ o $f(x)$):** Es el resultado que sale de la máquina. Se llama así porque su valor "depende" de qué número hayamos metido al principio.
> 4.  **Dominio y Rango:** El **Dominio** son todos los valores que *pueden* entrar a la máquina (valores de $x$). El **Rango o Imagen** son todos los valores que *efectivamente salen* de ella (valores de $y$).
> 5.  **Regla de Correspondencia:** Es la "instrucción" interna de la máquina. Puede ser "duplicar el número", "elevarlo al cuadrado" o cualquier operación matemática.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Función $f(x)$** | Asociación que asigna a cada entrada un **único** resultado mediante una regla. |
| **Dominio** | Conjunto de todos los posibles valores de entrada ($x$) que la función puede procesar. |
| **Rango / Imagen** | Conjunto de todos los valores resultantes o de salida ($y$). |
| **Inyectiva** | Función "uno a uno": a cada valor de salida le corresponde máximo uno de entrada. |
| **Sobreyectiva** | Función donde "no sobra nada": todo el conjunto de llegada es imagen de algo. |
| **Biyectiva** | Cuando la función es Inyectiva y Sobreyectiva al mismo tiempo. |
| **Binomio al Cuadrado** | $(a + b)^2 = a^2 + 2ab + b^2$ (necesario para evaluar expresiones compuestas). |

---

## Ejemplos resueltos con el "Profe"

```ad-example
title: Ejemplo A — Evaluación con números negativos
Dada la función $f(x) = 3x - 2$, vamos a hallar $f(-3)$.
1. **Sustituir:** Cambiamos la $x$ por el número, usando paréntesis para proteger el signo: $f(-3) = 3(-3) - 2$.
2. **Multiplicar:** Resolvemos la multiplicación primero. Más por menos da menos: $3 \times -3 = -9$.
3. **Operar:** Ahora resolvemos la resta final con cuidado: $-9 - 2 = -11$.
✅ **Resultado:** $f(-3) = -11$. Esto significa que en el plano cartesiano, la función pasa por el punto $(-3, -11)$.
```

```ad-example
title: Ejemplo B — Aplicación con Binomio al Cuadrado
Si tenemos $f(x) = x^2 - 3x - 12$, evaluemos la expresión compleja $f(2x + 1)$.
1. **Preparar la máquina:** Ponemos paréntesis donde antes estaba la $x$: $f(2x+1) = (\dots)^2 - 3(\dots) - 12$.
2. **Ingresar la expresión:** Colocamos $(2x + 1)$ dentro de cada paréntesis.
3. **Desarrollar el binomio:** Usamos la fórmula $(a+b)^2$:
   $(2x + 1)^2 = (2x)^2 + 2(2x)(1) + 1^2 = 4x^2 + 4x + 1$.
4. **Distributiva y simplificación:**
   $-3(2x + 1) = -6x - 3$.
5. **Unir todo:** $4x^2 + 4x + 1 - 6x - 3 - 12$.
✅ **Resultado simplificado:** $f(2x+1) = 4x^2 - 2x - 14$.
```

```ad-example
title: Ejemplo C — Aplicación real: Costo de Estacionamiento $USD
Un estacionamiento cobra $0.50 USD por cada minuto. La función es $P(t) = 0.50t$.
Si un auto se queda 20 minutos ($t=20$):
1. **Sustituir:** $P(20) = 0.50 \times 20$.
2. **Operar:** Multiplicamos y obtenemos 10.
✅ **Resultado:** El costo total es $10.00 USD. Aquí el costo **depende** del tiempo transcurrido.
```

---

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
1. Dada la función $f(x) = 2x - 5$, encuentra el valor de $f(0)$.
2. Si la regla de la máquina es "elevar al cuadrado" ($g(x) = x^2$), ¿qué sale si ingresas el número $3$?
3. En una función donde la regla es "duplicar", si el conjunto de entrada es $\{1, 2\}$, ¿cuál es el Rango?
```

```ad-abstract
title: 🟡 Medio
1. **¡Cuidado con la trampa!:** Dada la función $g(x) = 5x + 4$, halla el valor de $f(-2)$. 
   *(Piénsalo un poquito: ¿Conocemos la función $f$ o solo la $g$? Si la función se llama $G$, no podemos resolver $F$ sin conocer su regla).*
2. Evalúa la función $f(x) = 3x - 5$ para la expresión $(x + 1)$. Recuerda aplicar la propiedad distributiva.
3. Si $h(x) = x^2 - 1$, calcula $h(-2)$ recordando proteger el negativo con paréntesis.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
Un servicio de entrega cobra una tarifa fija de $5.00 USD más $2.00 USD por cada kilómetro ($k$) recorrido.
1. Escribe la función $C(k)$ que representa el costo total.
2. Calcula el costo si la entrega es a 12 km de distancia.
3. Si el cliente pagó $35.00 USD, ¿cuántos kilómetros recorrió el repartidor? 
   *(Aquí el costo final es el dato conocido, así que debemos despejar la variable independiente $k$ porque la distancia es lo que queremos descubrir).*
```

> [!tip] 💡 Consejo del Profe
> Para no cometer errores de signos, siempre que reemplaces una variable $x$ por un número (especialmente si es negativo), **escríbelo siempre dentro de un paréntesis**. Esto te ayudará a ver claramente si tienes que aplicar la ley de signos o elevar una potencia negativa. ¡El paréntesis es el escudo de tu operación!