# 📖 Guía de estudio — Clase 08: Gráfica de una Función a Trozos y Paridad

> [!info] 📌 Conceptos clave
> ¡Hola! En esta sesión aprenderemos a trabajar con funciones que cambian sus reglas según el valor de $x$ y a identificar simetrías especiales. 
> 1. **Función a trozos:** Imagínala como una **"carrera de relevos"**. Un corredor (una función) lleva el testimonio hasta cierto punto del eje $x$, y justo ahí se lo pasa al siguiente corredor (otra función) que sigue el camino bajo sus propias reglas. Son múltiples gráficas conviviendo en un solo plano.
> 2. **Intervalos (Dominios):** Son las "zonas" del eje $x$ donde cada trozo tiene permiso de existir. Por ejemplo, $x \leq 2$ nos dice que esa regla solo vale de la mitad hacia la izquierda.
> 3. **Punto Relleno vs. Hueco:** Es la clave para no perderse en las fronteras. Un círculo relleno ($\bullet$) indica que la función **toca** ese valor ($\leq, \geq$). Un círculo vacío o "hueco" ($\circ$) indica un **límite**: la función se acerca muchísimo, pero no llega a tocar ese punto exacto ($<, >$).
> 4. **Paridad:** Es una propiedad visual. Las funciones **Pares** actúan como un espejo respecto al eje $Y$, mientras que las **Impares** tienen un doble reflejo respecto al origen.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula | Referencia Visual |
| :--- | :--- | :---: |
| **Función a Trozos** | Combinación de dos o más funciones, cada una definida para un intervalo específico del dominio. | $\begin{cases} f(x) \\ g(x) \end{cases}$ |
| **Función Par** | Cumple que $f(-x) = f(x)$. Es simétrica respecto al eje $Y$ (efecto espejo). | $(\leftrightarrow)$ |
| **Función Impar** | Cumple que $f(-x) = -f(x)$. Simétrica respecto al origen (reflejo en $Y$ y luego en $X$). | $(\swarrow \nearrow)$ |
| **Punto Relleno** | Se usa cuando el intervalo incluye el valor crítico ($\leq$ o $\geq$). | $\bullet$ |
| **Punto Hueco** | Se usa cuando el intervalo **no** incluye el valor, pero marca su frontera ($<$ o $>$). | $\circ$ |

## Ejemplos resueltos paso a paso

```ad-example
title: Ejemplo A — Graficando paso a paso (Lineal y Cuadrática)
Grafiquemos la siguiente función: 
$f(x) = \begin{cases} x + 2 & \text{si } x \leq 2 \\ x^2 - 4x & \text{si } x > 2 \end{cases}$

**Paso 1: Primer tramo ($x \leq 2$)**
Tomamos valores menores o iguales a 2. 
- Si $x=0 \rightarrow f(0)=2$. Punto: $(0, 2)$
- Si $x=1 \rightarrow f(1)=3$. Punto: $(1, 3)$
- Si $x=2 \rightarrow f(2)=4$. Punto: $(2, 4)$ $\leftarrow$ **¡Punto sólido!** (porque es $\leq$).

**Paso 2: Segundo tramo ($x > 2$)**
¡Atención! Aunque $x$ no puede ser 2, calculamos el valor en 2 para hallar el "límite" o frontera.
- Si $x=2 \rightarrow f(2) = (2)^2 - 4(2) = 4 - 8 = -4$. Punto: $(2, -4)$ $\leftarrow$ **¡Hueco!** ($\circ$)
- Si $x=3 \rightarrow f(3) = (3)^2 - 4(3) = 9 - 12 = -3$. Punto: $(3, -3)$
- Si $x=4 \rightarrow f(4) = (4)^2 - 4(4) = 16 - 16 = 0$. Punto: $(4, 0)$

**Resultado:** Verás una línea recta que sube hasta el $(2, 4)$ con un punto firme, y una curva (parábola) que "salta" e inicia con un hueco en $(2, -4)$ para luego subir.
```

```ad-example
title: Ejemplo B — Verificación numérica de Paridad
Determinemos si $f(x) = 2x^2 - 3$ es una función **Par**.

1. **Sustitución:** Cambiamos todas las $x$ por $(-x)$:
   $f(-x) = 2(-x)^2 - 3$
2. **Desarrollo:** Como toda potencia par vuelve positivo al signo negativo ($(-x) \cdot (-x) = x^2$):
   $f(-x) = 2(x^2) - 3$
3. **Comparación:** ¿Es $2x^2 - 3$ igual a la original? **Sí**.
✅ **Conclusión:** La función es **Par**.

> [!tip] Nota del Experto: ¿Y si fuera Impar?
> Para que sea **Impar**, tras hallar $f(-x)$, debes calcular también $-f(x)$ (cambiarle el signo a toda la función original). Si ambos resultados son idénticos, la función es Impar. ¡Recuerda que si los signos no coinciden exactamente, la función simplemente no tiene paridad!
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel Inicial
1. Si un tramo de la función termina en la condición $x > 7$, ¿qué símbolo visual debemos dibujar en la coordenada $x=7$: un punto sólido ($\bullet$) o un hueco ($\circ$)?
2. Evalúa la función constante $f(x) = 5$ en el intervalo $0 \leq x \leq 10$. ¿Cuál es el valor de la función en $x=0$, $x=5$ y $x=10$?
3. Si al doblar tu hoja de papel por el eje $Y$, la parte derecha de la gráfica cae exactamente encima de la izquierda, ¿qué tipo de paridad tiene?
```

```ad-abstract
title: 🟡 Nivel Intermedio
1. Para la función $f(x) = \begin{cases} x + 3 & \text{si } x < 1 \\ 2x & \text{si } x \geq 1 \end{cases}$, construye una tabla de valores con $x = 0, 1, 2$. Indica en qué par ordenado debe ir un hueco.
2. Demuestra analíticamente que $f(x) = x^3 - 4x$ es una función **Impar**. (Pista: Halla $f(-x)$, luego $-f(x)$ y comprueba que son iguales).
3. Un estudiante dibujó un punto sólido en $(5, 10)$ para la función $f(x) = 2x$ definida como $x < 5$. Explica por qué esto es un error pedagógico basándote en el signo de desigualdad.
```

```ad-abstract
title: 🔴 Nivel Avanzado — Aplicación Práctica ($USD)
1. Un plan de datos cuesta $\$15$ USD mensuales si consumes entre 0 y 10GB. Si excedes los 10GB, el costo es de $\$15 + \$3$ por cada GB extra. Define las dos expresiones matemáticas de esta función a trozos.
2. En una factura de energía, el "punto de cambio de tarifa" es $x=200$ kWh. El tramo inicial termina en $\$40$ USD (punto sólido) y el segundo tramo inicia en $\$45$ USD (hueco). Si consumes exactamente 200 kWh, ¿cuánto debes pagar?
3. En economía, analiza la paridad de una función de flujo: Si una pérdida de inversión ($-x$) genera un déficit que es exactamente el opuesto al beneficio de una inversión positiva ($-f(x)$), de modo que $f(-x) = -f(x)$, ¿qué paridad describe este modelo de negocio?
```

> [!tip] 💡 El consejo del "Profe Alex"
> ¡No dejes tus gráficas incompletas! Al llenar tu tabla de valores, **incluye siempre el valor crítico (el borde)**, aunque tenga un signo de $<$ o $>$. Esto te permite saber exactamente dónde poner el **punto hueco** y desde dónde arranca la línea. Además, te recomiendo usar **colores distintos** para cada tramo; esto evita que te confundas en los puntos de unión y hace que tu trabajo sea mucho más profesional y fácil de entender. ¡A graficar!