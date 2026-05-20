# 📖 Guía de estudio — Clase 01: Introducción a los Sistemas de Ecuaciones de 3x3

¡Hola! Qué alegría comenzar este camino juntos. Hoy vamos a descubrir que las matemáticas no solo viven en líneas planas, sino que tienen cuerpo, profundidad y volumen. Resolver sistemas de ecuaciones es como ser un detective del espacio: buscamos el lugar exacto donde tres realidades distintas se encuentran. ¡Prepárate para ver los números en $3D$!

> [!info] 📌 Conceptos clave
> * **Ecuación de primer grado con tres incógnitas:** Es una igualdad donde participan tres valores desconocidos (generalmente $x$, $y$ y $z$) elevados a la potencia $1$.
> * **Significado de "solucionar":** Imagina que resolver es como encontrar la pieza exacta que falta para que una balanza esté en perfecto equilibrio. Es hallar los valores que, al sustituirlos, convierten la ecuación en una verdad matemática (ej. $10 = 10$).
> * **Representación geométrica (Planos):** En un espacio tridimensional, cada ecuación no es una línea, sino un **plano**. Visualízalo como un "cartoncito" o una hoja de papel que se extiende infinitamente en todas direcciones.
> * **La "Triple Verdad" del sistema:** Para que un punto $(x, y, z)$ sea la solución del sistema, debe hacer que las **tres** ecuaciones sean verdaderas al mismo tiempo. Geométricamente, es el único punto de intersección donde los tres planos se cruzan.

## Tabla de Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Incógnita** | Es la variable o letra (como $x$, $y$ o $z$) cuyo valor es el "tesoro escondido" que debemos encontrar. |
| **Ecuación de primer grado** | Una igualdad donde todas las variables tienen exponente $1$ (no verás $x^{2}$ ni $y^{3}$). |
| **Plano** | Es el dibujo de una ecuación de tres incógnitas. Imagina una **hoja de papel infinita** flotando en el espacio. |
| **Punto $(x, y, z)$** | Es la coordenada única donde se tocan los tres planos; representa la solución final del sistema. |

## Sección de Ejemplos Resueltos

````ad-example
title: Ejemplo A — Verificación de una solución
**Enunciado:** Comprobar si el punto $(1, 2, 7)$ es una solución válida para la ecuación $x + y + z = 10$.

**Paso a paso:**
1. **Identificar valores:** Según el punto, tenemos que $x = 1$, $y = 2$ y $z = 7$.
2. **Sustituir en la ecuación:** Reemplazamos las letras por sus valores protegidos por paréntesis:
   $(1) + (2) + (7) = 10$
3. **Realizar la suma:** 
   $1 + 2 = 3$
   $3 + 7 = 10$
4. **Verificar la verdad:** Como obtenemos $10 = 10$, la balanza está equilibrada. El punto **es una solución**.
````

````ad-example
title: Ejemplo B — Aplicación de presupuesto $USD
**Enunciado:** Compras tres artículos ($x$, $y$, $z$) y el total es de $10$ USD. Si el objeto $x$ cuesta $5$, el objeto $y$ cuesta $20$ y el objeto $z$ es una devolución (valor negativo) de $-15$, ¿es este presupuesto correcto?

**Proceso de validación:**
1. **Plantear la ecuación:** $x + y + z = 10$.
2. **Sustituir valores:** $5 + 20 + (-15) = 10$.
3. **Calcular con cuidado:**
   $5 + 20 = 25$
   $25 - 15 = 10$
4. **Conclusión:** Debido a que $10 = 10$, esta combinación de precios es matemáticamente válida para la ecuación.
````

## Métodos de Solución

Para resolver un sistema completo de $3 \times 3$, donde buscamos el punto donde se cruzan tres planos, utilizaremos estos $5$ métodos principales:

1. **Reducción / Eliminación**
2. **Sustitución**
3. **Determinantes (Regla de Cramer)**
4. **Método de Gauss**
5. **Método de Gauss-Jordan**

*Nota: Esta guía se enfoca en que comprendas la geometría y la lógica del sistema antes de pasar a los cálculos complejos de estos métodos.*

## Ejercicios de Repaso

````ad-abstract
title: 🟢 Nivel Verde — Fácil
Verifica si los siguientes puntos son soluciones para la ecuación $x + y + z = 15$:
1. Punto $(5, 5, 5)$
2. Punto $(10, 2, 3)$
3. Punto $(1, 1, 1)$
````

````ad-abstract
title: 🟡 Nivel Amarillo — Medio
Encuentra el valor de la incógnita $z$ para que la igualdad sea verdadera en la ecuación $x + y + z = 15$:
1. Si $x = 2$ y $y = 3$, ¿cuánto debe valer $z$?
2. Si $x = 10$ y $y = 0$, ¿cuánto debe valer $z$?
3. Si $x = -5$ y $y = 20$, ¿cuánto debe valer $z$?
````

````ad-abstract
title: 🔴 Nivel Rojo — Avanzado (El Reto de la Tienda)
Tres amigos compran snacks que en total suman $25$ USD ($x + y + z = 25$). 
1. Si el primer snack ($x$) cuesta $12$ y el segundo ($y$) cuesta $8$, calcula el valor que debería tener el tercer snack ($z$) para que el presupuesto sea correcto.
2. Una vez hallado $z$, verifica tu respuesta sustituyendo los tres valores en la ecuación original. ¿Se cumple la "verdad matemática"? Explica por qué.
````

> [!tip] 💡 Consejo de estudio
> ¡No te fíes solo del primer resultado! Para estar $100\%$ seguro en un sistema de ecuaciones, siempre reemplaza tus valores en las **tres** ecuaciones originales. Si la igualdad es verdadera en todas, tu solución es impecable. La verificación es el escudo contra los errores.