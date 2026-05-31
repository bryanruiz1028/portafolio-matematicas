# 📖 Guía de estudio — Clase 12: Función inversa

¡Qué tal, amigas y amigos! Espero que estén muy bien. Hoy vamos a sumergirnos en el fascinante mundo de las funciones inversas. No te asustes, parece difícil, pero verás que es como un juego de roles donde todo lo que una función hace, la otra lo deshace. ¡Vamos a darle!

> [!info] 📌 Conceptos clave
> Basándonos en las explicaciones del Profe Alex, aquí tienes los pilares fundamentales para dominar este tema:
> 1. **La "deshacedora" de procesos:** La función inversa es aquel proceso que "deshace" o invierte lo que la función original realizó. Si una función suma, la inversa resta; si multiplica, la inversa divide.
> 2. **Condición de existencia (Inyectividad):** ¡Ojo aquí! No todas las funciones tienen inversa. Para que exista, la función debe ser **inyectiva** (uno a uno). Esto significa que para cada valor de salida existe un único valor de entrada.
> 3. **El espejo de la Identidad ($y = x$):** En un plano cartesiano, la gráfica de una función y su inversa son simétricas. El "espejo" es la función identidad, representada por la recta $y = x$.
> 4. **El intercambio de roles:** Aquí ocurre algo genial: el dominio de la original se convierte en el rango de la inversa, y el rango de la original pasa a ser el dominio de la inversa. 
>    * *Nota técnica:* En funciones como $f(x) = \sqrt{x+2}$, debemos restringir el dominio (en este caso $x \geq -2$) para asegurar que la función esté definida y sea inyectiva.
> 5. **Comprobación mágica:** Si pasas un número por la función original y ese resultado lo pasas por la inversa, ¡debes volver al número inicial! Es como si hiciéramos magia.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Función Inyectiva** | Condición: Si $f(x_1) = f(x_2)$, entonces $x_1 = x_2$. <br> Es el "peaje" obligatorio para que exista la inversa. |
| **Notación de Inversa** | Se representa como $f^{-1}(x)$ o $g^{-1}(x)$. <br> ¡Cuidado! El $-1$ no es una potencia, es solo un nombre especial. |
| **Pasos para hallar la inversa** | 1. Cambiar $f(x)$ por $y$. <br> 2. Intercambiar $x$ por $y$. <br> 3. Despejar la nueva variable $y$. |
| **Simetría Gráfica** | Las funciones inversas son simétricas respecto a la recta identidad $y = x$. |

---

¡Manos a la obra! Veamos cómo aplicar estos pasos con los ejemplos que el Profe Alex nos enseña en sus clases.

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Caso básico (Función Lineal)
Vamos a hallar la inversa de la función $f(x) = 2x + 3$.

**Paso 0: Verificación de Inyectividad**  
Igualamos $f(x_1) = f(x_2)$:  
$2x_1 + 3 = 2x_2 + 3$  
Restamos 3 en ambos lados: $2x_1 = 2x_2$  
Dividimos para 2: $x_1 = x_2$.  
¡Es inyectiva, podemos seguir!

1. **Planteamiento:** Escribimos $y = 2x + 3$.
2. **Intercambio:** Cambiamos las letras: $x = 2y + 3$.
3. **Despeje:** Dejamos a la $y$ solita:
   - $x - 3 = 2y$
   - $\frac{x - 3}{2} = y$

✅ **Resultado:** La función inversa es $f^{-1}(x) = \frac{x-3}{2}$.
```

```ad-example
title: Ejemplo B — Aplicación real con camisetas ($USD)
Imagina que cada camiseta cuesta $10 USD. La función de precio es $P(x) = 10x$.

1. **Contexto:** Si compramos 7 camisetas, pagamos $P(7) = 10 \cdot 7 = 70$ USD.
2. **Problema:** Si pagamos $70 USD, ¿cuántas compramos? Necesitamos la inversa.
3. **Proceso:**
   - Escribimos $p = 10u$.
   - Intercambiamos y despejamos $u$: $u = \frac{p}{10}$.
   - Nuestra función inversa es $U(p) = \frac{p}{10}$.

✅ **Resultado:** Calculamos $U(70) = \frac{70}{10} = 7$ camisetas. ¡La inversa nos devolvió al origen!
```

---

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
1. Hallar la inversa de la función lineal $f(x) = x + 3$.
2. Hallar la inversa de la función $g(x) = 2x$.
3. Utilizando la condición $f(x_1) = f(x_2)$, comprueba si $f(x) = x + 5$ es inyectiva.
```

```ad-abstract
title: 🟡 Medio
1. Hallar la inversa de $f(x) = \frac{3x-2}{x+3}$.  
   *Pista: Usa el producto cruzado y luego aplica **Factor Común** para poder despejar la $y$.*
2. Hallar la inversa de la función cúbica $f(x) = x^3 + 2$.  
   *Pista: Recuerda que lo opuesto a una potencia al cubo es la raíz cúbica $\sqrt[3]{\dots}$.*
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
"Una tienda aplica una fórmula para calcular el cobro de envíos: $G(x) = 5x - 3$, donde $x$ es el peso en kg. Halla la función inversa que permita al cliente saber el peso permitido si tiene un presupuesto de $USD determinado."

**Guía para tu éxito:** Después de intercambiar y despejar, tu respuesta debe ser $g^{-1}(x) = \frac{x+3}{5}$. ¡Inténtalo antes de ver la solución!
```

---

> [!tip] 💡 Consejo de estudio: ¡Haz la magia tú mismo!
> No te quedes con la duda. Para saber si tu respuesta es correcta, usa el truco del Profe Alex:
> 1. Elige un número, digamos el $2$.
> 2. Pásalo por la función original: $f(2) = 2(2) + 3 = 7$.
> 3. Toma ese $7$ y pásalo por tu inversa: $f^{-1}(7) = \frac{7-3}{2} = \frac{4}{2} = 2$.
> 
> **¡BOOM! Regresaste al número inicial.** Si esto ocurre, tu proceso es impecable. ¡Felicidades!