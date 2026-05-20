# 📖 Guía de estudio — Clase 10: Resta de funciones

> [!info] 📌 Conceptos clave
> 1. **Definición fundamental:** La resta de funciones $(f - g)(x)$ consiste en sustraer cada uno de los términos de la segunda función (sustraendo) de los términos de la primera función (minuendo).
> 2. **Importancia del orden:** El orden es crítico y obligatorio. A diferencia de la suma, la resta no es conmutativa. Cambiar el orden de las funciones invierte los signos del resultado final; es decir, $(f - g)(x)$ y $(g - f)(x)$ son inversos aditivos (mismos valores, signos opuestos).
> 3. **Uso obligatorio de paréntesis:** Al plantear la resta, la segunda función debe escribirse siempre entre paréntesis precedida por el signo menos. Esto asegura la correcta aplicación de la propiedad distributiva.
> 4. **Simplificación:** El proceso termina agrupando los términos semejantes (aquellos con la misma variable y exponente), realizando las sumas o restas de sus coeficientes.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Notación de la resta** | $(f - g)(x) = f(x) - g(x)$. Siempre se resta la segunda función de la primera. |
| **Propiedad Distributiva** | Multiplicar el signo negativo $(-)$ por cada término interno del paréntesis del sustraendo: $-(a + b - c) = -a - b + c$. |
| **Términos Semejantes** | Componentes con la misma base y exponente (ej. $3x^2$ y $-x^2$). Solo estos se pueden reducir. |
| **Método "Carita Feliz"** | Para restar funciones con fracciones: $\frac{A}{B} - \frac{C}{D} = \frac{(A \cdot D) - (B \cdot C)}{B \cdot D}$. <br>*(Se multiplica en cruz para el numerador y de frente para el denominador).* |

> [!warning] ⚠️ ¡Cuidado con el "1 invisible"!
> Es un error común olvidar que términos como $-x^2$ o $-x$ tienen un coeficiente "1" implícito. Al agrupar, trátalos como $-1x^2$ o $-1x$. Asimismo, recuerda que el signo menos fuera de un paréntesis cambia **todos** los signos de los términos internos, no solo el del primero.

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Resta de polinomios (Caso básico)
**Enunciado:** Sean $f(x) = 2x^2 - 3x + 1$ y $g(x) = x^2 + 6x - 2$. Hallar $(f - g)(x)$.

**Procedimiento paso a paso:**
1. **Planteamiento:** Escribe la primera función: $2x^2 - 3x + 1$.
2. **Uso de paréntesis:** Resta la segunda función protegiéndola: $-(x^2 + 6x - 2)$.
3. **Distribución de signos:** Cambia los signos internos: $-x^2 - 6x + 2$.
4. **Agrupación de semejantes:**
   - Cuadráticos: $2x^2 - 1x^2 = x^2$
   - Lineales: $-3x - 6x = -9x$
   - Independientes: $1 + 2 = 3$
✅ **Resultado:** $x^2 - 9x + 3$
```

```ad-example
title: Ejemplo B — Aplicación real $USD (Ganancia neta)
**Enunciado:** La función de ingresos de una tienda es $I(x) = 3x^2 + 2x$ y la de costos es $C(x) = 2x^2 - 3$. Hallar la función de ganancia $G(x) = (I - C)(x)$.

**Procedimiento:**
1. **Planteamiento:** Se define $G(x) = I(x) - C(x)$.
2. **Aplicación del signo:** $3x^2 + 2x - (2x^2 - 3)$.
3. **Simplificación:** Al distribuir el signo, el $-3$ se convierte en $+3$.
   - Operación: $3x^2 + 2x - 2x^2 + 3$.
   - Agrupando: $(3x^2 - 2x^2) + 2x + 3 = 1x^2 + 2x + 3$.
✅ **Resultado:** $x^2 + 2x + 3$ (en $USD).
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel: Inicial
1. Si $f(x) = 3x^2 + 2x$ y $g(x) = 2x^2 - 3$, calcula $(f - g)(x)$.
2. Usando las mismas funciones, calcula $(g - f)(x)$.
   - 💡 **Pista para el estudiante:** Compara ambos resultados. Deberías notar que todos los signos son opuestos. Si en el ejercicio 1 obtuviste $x^2 + 2x + 3$, aquí deberías obtener $-x^2 - 2x - 3$.
```

```ad-abstract
title: 🟡 Nivel: Intermedio
1. Realiza la resta de una función racional y una polinómica: $(h - f)(x)$ donde $h(x) = \frac{x+2}{2x+1}$ y $f(x) = 2x^2 - 3x + 1$.
   - 💡 **Pista para el estudiante:** Coloca un denominador 1 debajo de $f(x)$. Utiliza el método de la **"Carita Feliz"** para multiplicar en cruz. ¡No olvides poner paréntesis al multiplicar los polinomios para no perder ningún signo!
```

```ad-abstract
title: 🔴 Nivel: Avanzado — Aplicación financiera $USD
1. Una empresa tiene una función de ingresos $f(x) = 3x^2 + 2x$ y una función de deuda $h(x) = \frac{x}{x+1}$. Hallar la función de capital final $K(x) = (f - h)(x)$.
   - 💡 **Pista para el estudiante:** Plantea la operación como $\frac{3x^2 + 2x}{1} - \frac{x}{x+1}$. Al realizar la multiplicación cruzada $(3x^2 + 2x)(x+1)$, asegúrate de distribuir cada término y luego restar la $x$ sobrante del numerador. Expresa el resultado final en $USD.
```

> [!tip] 💡 Consejo pedagógico del "Profe Alex"
> "Para no equivocarte, **nunca te saltes el paso de los paréntesis**". La mayoría de los estudiantes cometen errores por intentar cambiar los signos mentalmente mientras agrupan. Dedica un renglón exclusivo para eliminar los paréntesis y ver los nuevos signos claramente antes de intentar reducir la expresión. ¡La paciencia es la clave de la precisión en el álgebra!