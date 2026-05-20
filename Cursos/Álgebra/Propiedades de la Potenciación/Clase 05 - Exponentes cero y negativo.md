# Clase 05 — Power with exponent 0 equals 1 | Explanation + Power of negative numbers + Potencia con exponente negativo | Explicación + Potencias con exponentes negativos | Potencia de Fracciones Explicación

#algebra #powerwithexpone

Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 5 de 7

> [!info] 🧭 Navegación
> [[Clase 04|⬅ Clase 04]] | [[00 - Índice del curso|Índice]] | **Clase 05** | [[Clase 06|Clase 06 ➡]]

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> ¡Bienvenidos! Hoy descubriremos que los exponentes no solo sirven para agrandar números, sino también para representar la unidad y las partes más pequeñas de un todo. Dominar estas propiedades te permitirá simplificar cálculos en finanzas y ciencias de forma asombrosa.
> 
> - **💵 Aplicación $USD:** En escalas financieras, $10^0$ representa nuestra unidad base ($1 USD). Entender esto es la base para comprender cómo crece o decrece el dinero.
> - **🏗️ Aplicación práctica:** En ingeniería, las potencias negativas permiten trabajar con medidas microscópicas o frecuencias de radio sin escribir infinitos ceros.
> - **📊 Situación cotidiana:** Usamos exponentes negativos para expresar deudas o reducciones proporcionales (como cuando algo se deprecia a la décima parte de su valor).

## Concepto clave

> [!note] 📌 ¿Qué es Power with exponent 0 equals 1?
> Cualquier número (excepto el 0) elevado al exponente 0 es igual a 1. ¿Por qué? Imagina una división de potencias iguales: $a^n / a^n$. Por leyes de exponentes, restamos: $n - n = 0$. Pero sabemos que cualquier cantidad dividida por sí misma es 1. Por lo tanto, $a^0 = 1$.
> 
> **¿Y qué pasa con $0^0$?** El Profe Alex nos explica que esto **no está definido**. Para que una potencia dé 1, debemos poder "simplificar" (sacar mitad, quinta, etc.). Si intentamos simplificar $0/0$, no obtenemos 1; el cero dividido por cualquier número sigue siendo cero. Como no podemos dividir entre cero, $0^0$ no existe en los reales.

> [!warning] ⚠️ Error común: ¡Cuidado con los paréntesis!
> No es lo mismo $(-3)^2$ que $-3^2$. 
> - En **$(-3)^2$**, la base es $-3$. El exponente par convierte el resultado en positivo: $(-3) \cdot (-3) = 9$.
> - En **$-3^2$**, el negativo está "afuera". Solo elevas el 3: $-(3 \cdot 3) = -9$. ¡Fíjate siempre si el signo está dentro de la "protección" del paréntesis!

> [!tip] 💡 Truco: La "Orden de Mudanza" (Reciprocidad)
> Un exponente negativo es una **instrucción de reciprocidad**. Míralo como una **"orden de mudanza"**: si el número tiene un exponente negativo arriba, mándalo abajo (al denominador) y ¡listo!, el exponente se vuelve positivo. Si es una fracción, simplemente "le das la vuelta" (la inviertes).

## Procedimiento paso a paso

```text
PASO 1: Observar la base. ¿Tiene paréntesis? Esto es vital para decidir qué pasará con el signo al final.
PASO 2: Evaluar el exponente. Si es 0, el resultado es 1 (siempre que la base no sea 0).
PASO 3: Si el exponente es negativo, aplica la "orden de mudanza": invierte la base o pásala al denominador para que el exponente sea positivo.
PASO 4: Resolver la potencia final y aplicar signos: 
        - Exponente PAR: Resultado siempre POSITIVO (si hay paréntesis).
        - Exponente IMPAR: El resultado MANTIENE EL SIGNO DE LA BASE.
```

## Ejemplos Desarrollados

```ad-example
title: Ejemplo 1 (Básico): Exponente Cero
**Problema:** Resolver $5^0$.
**Explicación:** El 0 nace de una resta de iguales, como $3 - 3$.
$5^0 = 5^{3-3} = \frac{5^3}{5^3} = \frac{125}{125} = 1$.
**Resultado:** 1
```

```ad-example
title: Ejemplo 2 (Signos): El poder del paréntesis
**Problema:** Comparar $(-2)^4$ y $-2^4$.
**Explicación:** 
1. $(-2)^4$: Base negativa con exponente par $\rightarrow$ POSITIVO. $(-2)(-2)(-2)(-2) = 16$.
2. $-2^4$: El negativo espera afuera. $-(2 \cdot 2 \cdot 2 \cdot 2) = -16$.
**Resultado:** 16 y -16.
```

```ad-example
title: Ejemplo 3 (Avanzado): Fracción e inversión
**Problema:** Resolver $(\frac{2}{3})^{-2}$.
**Explicación:** ¡No te asustes por la fracción! Aplicamos la orden de mudanza invirtiendo los términos:
$(\frac{2}{3})^{-2} = (\frac{3}{2})^2$.
Ahora elevamos ambos: $\frac{3^2}{2^2} = \frac{9}{4}$.
**Resultado:** 9/4
```

```ad-example
title: Ejemplo 4 (Aplicación $USD): Centavos y potencias
**Problema:** Si una inversión de $1 USD se reduce por un factor de $10^{-1}$, ¿cuánto dinero queda?
**Explicación:** $10^{-1}$ significa mover el 10 al denominador:
$10^{-1} = \frac{1}{10^1} = 0.1$.
**Resultado:** 0.1 USD (equivalente a 10 centavos de dólar).
```

## Ejercicios y Autoevaluación

```ad-abstract
title: Nivel 1: Fácil (Verde)
1. $25^0$
2. $3^{-1}$
3. $(-7)^0$
4. $y^0$ (donde $y \neq 0$)
```

```ad-abstract
title: Nivel 2: Medio (Amarillo)
1. $(-4)^2$ vs $-4^2$
2. $(\frac{1}{3})^{-2}$
3. $(\frac{2}{5})^{-1}$
4. $(-2)^{-3}$
```

```ad-abstract
title: Nivel 3: Avanzado ($USD) (Rojo)
1. Resolver: $(a + b)^0$ asumiendo que $(a + b) \neq 0$.
2. Si una deuda se expresa como $10^{-2}$ USD, ¿cuál es su valor en formato decimal?
3. Calcular: $(\frac{1}{2})^{-3} + 10^0$.
4. Determinar el signo y valor de: $(-1)^{100} + (-1)^{99}$.
```

```ad-success
title: Respuestas para el Docente
**Fácil:** 1. (1) | 2. (1/3) | 3. (1) | 4. (1).
**Medio:** 1. (16 y -16) | 2. (9) | 3. (5/2 o 2.5) | 4. (-1/8 o -0.125).
**Avanzado:** 
1. (1): Toda base compuesta elevada a cero es la unidad.
2. (0.01 USD): Es un centavo, ya que $1/10^2 = 1/100$.
3. (9): Porque $2^3 + 1 = 8 + 1$.
4. (0): Porque $1 + (-1) = 0$. (Par da positivo, impar mantiene el negativo).
```

```ad-question
title: Mini-prueba de teoría
1. ¿Por qué $0^0$ no es 1? (Pista: Piensa en la simplificación).
2. ¿Qué acción física realizas sobre una fracción cuando tiene exponente negativo?
3. Si tienes $-x^4$ (sin paréntesis), ¿por qué el resultado siempre será negativo sin importar el valor de $x$?
```

## Cierre y Navegación Final

> [!tip] 💡 En la próxima clase
> ¡Gran trabajo hoy! En la Clase 06 uniremos todo: usaremos estas reglas de exponentes 0 y negativos dentro de **operaciones combinadas**. ¡Prepárate para el reto final!

> [!info] 🧭 Navegación
> [[Clase 04|⬅ Clase 04]] | [[00 - Índice del curso|Índice]] | **Clase 05** | [[Clase 06|Clase 06 ➡]]

---