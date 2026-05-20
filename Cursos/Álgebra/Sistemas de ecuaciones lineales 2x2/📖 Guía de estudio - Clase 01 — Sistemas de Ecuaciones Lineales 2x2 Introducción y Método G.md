# 📖 Guía de estudio — Clase 01: Introducción a los Sistemas de Ecuaciones Lineales 2x2

> [!info] 📌 Conceptos clave
> - **Ecuación:** Es una igualdad entre dos expresiones matemáticas que contiene una o más variables (letras).
> - **Solución de una ecuación:** Hallar el valor numérico de la incógnita que hace que la igualdad sea verdadera.
> - **Sistema 2x2:** Un conjunto de **dos ecuaciones con dos incógnitas** (generalmente $x$ e $y$).
> - **El reto de la simultaneidad:** Resolver un sistema no es solo hallar una respuesta para una ecuación, sino encontrar el par de valores $(x, y)$ que **sirve para las dos ecuaciones** al mismo tiempo.
> - **Método Analítico inicial:** Antes de usar procesos complejos, podemos usar la inspección lógica o "tanteo" para buscar valores que satisfagan ambas igualdades.

---

### Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ecuación** | Una igualdad matemática entre dos expresiones que incluye variables. |
| **Variable (o Incógnita)** | Letra que representa un valor desconocido. Se llama variable porque su valor puede cambiar según el problema. |
| **Sistema Lineal** | Conjunto de ecuaciones donde todas las variables están elevadas a la **potencia 1** (exponente 1), lo que genera líneas rectas al graficarlas. |
| **Punto de Intersección** | Las coordenadas $(x, y)$ donde las dos rectas se cruzan; es la única solución común para ambas ecuaciones. |

---

### Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A — Comprobación de una solución
Para verificar si un punto es la solución de un sistema, debemos sustituir los valores en ambas ecuaciones y comprobar que la igualdad se mantenga.

**Sistema:**
1) $x + y = 5$
2) $x - y = 1$

**Valores a comprobar:** $x = 3, y = 2$

**Paso 1: Sustituir en la ecuación 1**
$3 + 2 = 5$
$5 = 5$ (Verdadero: La solución sirve para la primera ecuación).

**Paso 2: Sustituir en la ecuación 2**
$3 - 2 = 1$
$1 = 1$ (Verdadero: La solución también sirve para la segunda ecuación).

**Conclusión:** El punto $(3, 2)$ es la solución del sistema porque cumple ambas condiciones simultáneamente.
```

```ad-example
title: Ejemplo B — Aplicación en contexto de compras ($USD)
**Enunciado:** La suma del costo de un cuaderno ($x$) y un lápiz ($y$) es $5 USD. Se sabe que el cuaderno cuesta $1 USD más que el lápiz ($x - y = 1$).

**Planteamiento:**
1) $x + y = 5$
2) $x - y = 1$

**Vinculación con resultados:**
Si aplicamos la solución hallada anteriormente ($x = 3, y = 2$):
- **Precio del Cuaderno ($x$):** $3 USD.
- **Precio del Lápiz ($y$):** $2 USD.

**Respuesta final:** El cuaderno cuesta $3 USD y el lápiz cuesta $2 USD. El sistema nos permite traducir el lenguaje cotidiano a un lenguaje algebraico preciso.
```

---

### Ejercicios de Repaso

```ad-abstract
title: 🟢 Fácil — Verificación de Soluciones
Compruebe si los siguientes pares de valores son la solución de los sistemas propuestos:

1. ¿Es el punto $(5, 0)$ la solución del sistema formado por $x + y = 5$ y $x - y = 1$? (Demuestre sustituyendo).
2. ¿Es el punto $(1, 4)$ la solución del sistema formado por $y = 4 - x$ y $y = 2x + 2$?
3. ¿Es el punto $(3, 2)$ la solución del sistema formado por $2x + y = 8$ y $x - y = 1$?
```

```ad-abstract
title: 🟡 Medio — Construcción de Tablas de Valores
Para resolver por el método gráfico, primero debemos obtener puntos. Complete las siguientes tablas:

1. **Ecuación:** $y = 4 - x$
   - Si $x = 0 \rightarrow y = \dots$
   - Si $x = 1 \rightarrow y = \dots$
   - Si $x = 2 \rightarrow y = \dots$

2. **Ecuación:** $y = 2x - 5$
   - Si $x = 0 \rightarrow y = \dots$
   - Si $x = 1 \rightarrow y = \dots$
   - Si $x = 2 \rightarrow y = \dots$

3. **Ecuación:** $y = x + 1$
   - Si $x = 0 \rightarrow y = \dots$
   - Si $x = 1 \rightarrow y = \dots$
   - Si $x = 2 \rightarrow y = \dots$
```

```ad-abstract
title: 🔴 Avanzado — Interpretación Gráfica y Aplicación
Imagine que está analizando los precios de dos frutas en el mercado:
- El precio de una manzana está representado por la variable $x$.
- El precio de una pera está representado por la variable $y$.

Al graficar las dos ecuaciones de precios, las rectas se cruzan exactamente en el punto $(3, 2)$.
1. Determine el precio de cada fruta en dólares basándose en el punto de intersección.
2. Argumente pedagógicamente: ¿Por qué cualquier otro punto que esté sobre una de las rectas, pero que no sea el $(3, 2)$, no puede considerarse la solución del sistema?
```

---

> [!tip] 💡 Consejo de estudio: La ventaja del despeje
> Siempre que utilices el **método gráfico**, acostúmbrate a **despejar la variable $y$** antes de iniciar tu tabla de valores. Al hacerlo, transformas la ecuación en una función de la forma $y = f(x)$. Esto no solo facilita el cálculo mental de los puntos, sino que te ayuda a visualizar la relación de dependencia entre las variables y reduce drásticamente el riesgo de cometer errores con los signos negativos.