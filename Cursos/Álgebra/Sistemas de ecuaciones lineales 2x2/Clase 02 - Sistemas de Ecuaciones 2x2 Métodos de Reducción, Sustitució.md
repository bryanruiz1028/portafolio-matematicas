# Clase 02 — Sistemas de Ecuaciones 2x2: Métodos de Reducción, Sustitución e Igualación

#algebra #systemsofxlinea

---
« [[Clase 01]] | [[Índice]] | [[Clase 03]] »

---

> [!info] 🌍 Relevancia y aplicaciones
> Un sistema de ecuaciones 2x2 es un conjunto de dos condiciones que deben cumplirse al mismo tiempo. Resolverlo nos permite encontrar el valor exacto de dos incógnitas de forma simultánea.
> 
> *   💵 **Cálculo de precios:** Determinar el costo individual de productos en compras combinadas (USD).
> *   🏗️ **Ingeniería:** Calcular el equilibrio de materiales o fuerzas en una construcción.
> *   📊 **Comparativa de planes:** Evaluar qué tarifa de ahorro o telefonía es más barata según el uso.

> [!note] Concepto para jóvenes detectives
> Imagina que tienes dos pistas sobre dos números secretos ($x$ e $y$). Resolver un sistema 2x2 es como ser un detective: usamos las dos pistas juntas para encontrar el único par de números que hace que ambos acertijos sean ciertos al mismo tiempo. ¡Es el punto donde dos historias se cruzan!

> [!warning] ¡Cuidado con los signos!
> El error más común es olvidar que, al multiplicar una ecuación por un número negativo, **todos** los términos cambian de signo, incluyendo el resultado después del igual. ¡No dejes a ningún término atrás!

> [!tip] Regla de oro para el Método de Reducción
> Para decidir si sumar o restar las ecuaciones, observa los signos de la letra que quieres eliminar:
> *   **Signos iguales:** Se restan las ecuaciones (o multiplicas una por $-1$ y sumas).
> *   **Signos distintos:** Se suman las ecuaciones directamente.

---

### Estrategias de Resolución

> [!important] Paso Cero: La Organización
> Antes de aplicar cualquier método, asegúrate de que las ecuaciones estén **ordenadas**. Las $x$ deben estar bajo las $x$, las $y$ bajo las $y$, y los números independientes después del signo igual.
> 
> **Correcto:**
> $2x + 3y = 7$
> $5x - 4y = 12$

#### 1. Método de Reducción (Eliminación)
```text
PASO 1: Organizar las ecuaciones (x, y, = número).
PASO 2: Multiplicar una o ambas ecuaciones para que una letra tenga el mismo coeficiente.
        *TIP PRO: Si los números son difíciles, usa el Mínimo Común Múltiplo (MCM).
PASO 3: Sumar o restar para eliminar esa letra.
PASO 4: Resolver la ecuación resultante y sustituir el valor para hallar la otra incógnita.
```

#### 2. Método de Sustitución
```text
PASO 1: Despejar una letra en una ecuación. Busca la que sea "positiva y esté sola" (coeficiente 1).
PASO 2: Reemplazar esa expresión en la OTRA ecuación usando paréntesis obligatoriamente.
PASO 3: Resolver la ecuación de una sola variable.
PASO 4: Usar ese valor en el despeje del Paso 1 para hallar la segunda variable.
```

#### 3. Método de Igualación
```text
PASO 1: Despejar la MISMA letra en las dos ecuaciones.
PASO 2: Igualar las dos expresiones obtenidas.
PASO 3: Resolver la ecuación (si hay fracciones, usa el "producto cruzado").
PASO 4: Sustituir el valor hallado en cualquiera de los despejes para encontrar la otra letra.
```

---

### Ejemplos Prácticos Paso a Paso

```ad-example
title: Ejemplo 1: Método de Reducción (Completo)
**Sistema:**
1) $2x + 3y = 7$
2) $5x - 3y = 12$

**Solución:**
1. **Eliminar y:** Como ya tenemos $+3y$ y $-3y$ (mismo número, signos opuestos), sumamos las ecuaciones directamente:
   $(2x + 5x) + (3y - 3y) = 7 + 12$
   $7x = 19 \rightarrow x = \frac{19}{7}$

2. **Hallar y:** Sustituimos $x$ en la ecuación (1):
   $2(\frac{19}{7}) + 3y = 7 \rightarrow \frac{38}{7} + 3y = 7$
   $3y = 7 - \frac{38}{7} \rightarrow 3y = \frac{49-38}{7} \rightarrow 3y = \frac{11}{7}$
   $y = \frac{11}{21}$
```

```ad-example
title: Ejemplo 2: Método de Sustitución
**Sistema:**
1) $x - 2y = -4$
2) $3x + y = 9$

**Solución:**
1. **Despeje ideal:** En (1), $x$ está sola y positiva: $x = -4 + 2y$.
2. **Sustitución:** En (2), reemplazamos $x$: $3(-4 + 2y) + y = 9$.
3. **Resolver:** 
   $-12 + 6y + y = 9$
   $7y = 9 + 12 \rightarrow 7y = 21 \rightarrow y = 3$.
4. **Finalizar:** $x = -4 + 2(3) \rightarrow x = 2$.
**Resultado:** $(2, 3)$
```

```ad-example
title: Ejemplo 3: Método de Igualación (Con Scaffolding)
**Sistema:**
1) $x + 6y = 27$
2) $7x - 3y = 9$

**Solución:**
1. **Despejar x en ambas:**
   (1) $x = 27 - 6y$
   (2) $7x = 9 + 3y \rightarrow x = \frac{9 + 3y}{7}$
2. **Igualar:** $27 - 6y = \frac{9 + 3y}{7}$
3. **Producto cruzado:** $7(27 - 6y) = 9 + 3y$
   $189 - 42y = 9 + 3y$
4. **Agrupar términos (Paso a paso):**
   $189 - 9 = 3y + 42y$ 
   $180 = 45y \rightarrow y = \frac{180}{45} \rightarrow y = 4$
5. **Hallar x:** $x = 27 - 6(4) = 27 - 24 = 3$.
**Resultado:** $(3, 4)$
```

```ad-example
title: Ejemplo 4: Aplicación Real (Entradas al Cine en USD)
**Problema:** Un grupo paga 35 USD por 2 entradas de adulto ($x$) y 3 de niño ($y$). Otro grupo paga 45 USD por 4 entradas de adulto y 1 de niño.

**Sistema:**
1) $2x + 3y = 35$
2) $4x + y = 45$

**Resolución (Sustitución):**
1. Despejamos $y$ en (2): $y = 45 - 4x$.
2. Sustituimos en (1): $2x + 3(45 - 4x) = 35$.
3. Resolvemos: $2x + 135 - 12x = 35 \rightarrow -10x = 35 - 135 \rightarrow -10x = -100$.
4. $x = 10$ USD (Adulto).
5. $y = 45 - 4(10) = 5$ USD (Niño).
```

---

### Ejercicios y Autoevaluación

> [!abstract] Practica lo aprendido
> **Nivel Fácil (Verde):**
> 1. $x + y = 10$
> 2. $x - y = 2$
> 
> **Nivel Medio (Amarillo):**
> 1. $3x + 2y = 14$
> 2. $x + y = 5$ 
> *(Sugerencia: Multiplica la segunda por -2 para usar Reducción).*
> 
> **Nivel Avanzado (Rojo):**
> En una tienda de tecnología, 2 teclados y 3 ratones cuestan 70 USD. Si compras 4 teclados y 1 ratón, pagas 90 USD. ¿Cuál es el precio de cada artículo?

> [!success] Solucionario
> *   **Fácil:** $x = 6, y = 4$
> *   **Medio:** $x = 4, y = 1$
> *   **Avanzado:** Teclado = 20 USD, Ratón = 10 USD.

---

### Mini-Prueba de Comprensión

```ad-question
title: Pregunta 1
Si en el método de Reducción los coeficientes son iguales pero tienen el mismo signo (ej: $5x$ y $5x$), ¿cuál es el procedimiento correcto?
1. Sumar las ecuaciones.
2. Restar las ecuaciones o multiplicar una por $-1$ y luego sumar.
3. El sistema no tiene solución.
```

```ad-question
title: Pregunta 2
¿Cuál es la recomendación de Profe Alex para elegir qué letra despejar en Sustitución?
1. La letra que tenga el número más grande al lado.
2. La letra que esté negativa al final de la ecuación.
3. La letra que esté sola (coeficiente 1) y positiva.
```

```ad-question
title: Pregunta 3
En el sistema $x + y = 10$ y $x - y = 4$, ¿puedes hallar mentalmente $x$ e $y$?
> [!success] Click para ver respuesta
> Al sumar las ecuaciones mentalmente: $2x = 14 \rightarrow x = 7$. Luego, $7 + y = 10 \rightarrow y = 3$.
```

---

> [!tip] Próximo Paso: La Prueba de Fuego
> ¡Gran trabajo! Has dominado los tres métodos principales. En la **Clase 03**, aprenderemos el proceso de **Verificación**: cómo estar 100% seguros de que nuestros resultados son correctos antes de entregar un examen. 

---
« [[Clase 01]] | [[Índice]] | [[Clase 03]] »