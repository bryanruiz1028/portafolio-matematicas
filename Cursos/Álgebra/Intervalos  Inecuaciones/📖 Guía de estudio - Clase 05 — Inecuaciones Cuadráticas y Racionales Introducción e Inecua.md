# 📖 Guía de estudio — Clase 05: Inecuaciones Cuadráticas y Racionales

> [!info] 📌 Conceptos clave
> 1. **Identificación:** Una inecuación es cuadrática (o de segundo grado) si el exponente máximo de la variable es $x^2$ o si la expresión resulta de multiplicar dos factores lineales con $x$.
> 2. **Ordenamiento:** El primer paso esencial es trasladar todos los términos a un solo lado de la desigualdad (generalmente el izquierdo), dejando un **cero** al otro lado para poder comparar.
> 3. **Análisis de Signos:** Resolver una inecuación significa determinar en qué intervalos la expresión es **positiva** ($> 0$) o **negativa** ($< 0$).
> 4. **Puntos Críticos:** Son los valores que hacen que la expresión sea igual a cero. Estos puntos actúan como "fronteras" que dividen la recta numérica en distintos sectores.
> 5. **Inecuaciones Racionales:** Se resuelven de forma muy similar a las cuadráticas mediante el análisis de signos de sus factores, con una regla de oro: **el denominador nunca puede ser cero**, por lo que sus puntos críticos siempre serán abiertos (paréntesis).

---

### Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Inecuación Cuadrática** | Expresión de la forma $ax^2 + bx + c > 0$ (o $<, \leq, \geq$), donde el exponente mayor de $x$ es 2. |
| **Puntos Críticos** | Valores de $x$ obtenidos al igualar cada factor a cero (ej. si $x-a=0$, entonces $x=a$ es un punto crítico). |
| **Intervalo Abierto vs. Cerrado** | Se usa paréntesis `( )` para signos $<$ o $>$ (punto abierto/hueco). Se usa corchetes `[ ]` para $\leq$ o $\geq$ (punto cerrado/relleno). |
| **Inecuación Racional** | Inecuación que presenta la variable $x$ en el denominador de una fracción. |

---

### Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A (Caso Básico)
**Enunciado:** Resolver $x^2 - 3x - 10 > 0$.

1. **Paso 1 (Factorización):** Buscamos dos números que multiplicados den $-10$ y restados den $-3$. La expresión queda: $(x - 5)(x + 2) > 0$.
2. **Paso 2 (Puntos críticos):** Igualamos cada factor a cero. 
   - $x - 5 = 0 \Rightarrow x = 5$
   - $x + 2 = 0 \Rightarrow x = -2$
   *Nota: Como el signo es $>$, los puntos son **abiertos**.*
3. **Paso 3 (Recta numérica y signos):** Analizamos los signos multiplicando los factores en cada sector:
   `Sector 1 (< -2): (-)(-)= + | Sector 2 (-2 a 5): (-)(+)= - | Sector 3 (> 5): (+)(+)= +`
   `(+) ------- (-2) ------- (-) ------- (5) ------- (+)`
4. **Resultado:** Buscamos los valores mayores a cero (positivos).
   **Solución:** $(-\infty, -2) \cup (5, \infty)$
```

```ad-example
title: Ejemplo B (Aplicación Real $USD)
**Enunciado:** Una empresa determina que su pérdida operativa está dada por la expresión $x^2 - 2x - 24$. ¿En qué rango de unidades producidas ($x$) la empresa se mantiene en niveles de pérdida o equilibrio (valores $\leq 0$)?

1. **Paso 1 (Factorización):** $(x - 6)(x + 4) \leq 0$.
2. **Paso 2 (Puntos críticos):**
   - $x - 6 = 0 \Rightarrow x = 6$
   - $x + 4 = 0 \Rightarrow x = -4$
   *Nota: Como el signo es $\leq$, los puntos son **cerrados** (incluyen el cero).*
3. **Paso 3 (Análisis de signos):**
   `Sector 1 (< -4): (-)(-)= + | Sector 2 (-4 a 6): (-)(+)= - | Sector 3 (> 6): (+)(+)= +`
   `(+) ------- [-4] ------- (-) ------- [6] ------- (+)`
4. **Paso 4 (Interpretación Crítica):** Matemáticamente, la solución es $[-4, 6]$. Sin embargo, en el mundo real, una empresa no puede producir unidades negativas ($x \geq 0$). 
5. **Resultado:** El rango lógico de producción para mantenerse en pérdida o equilibrio es:
   **Solución:** $[0, 6]$ unidades.
```

---

### Ejercicios de Repaso

```ad-abstract
title: 🟢 Fácil
1. Resuelve la inecuación: $x^2 + x - 6 \geq 0$.
2. Determina los puntos críticos y el conjunto solución de: $(x + 3)(x - 2) \leq 0$.
```

```ad-abstract
title: 🟡 Medio
1. ¡Ordena primero! Resuelve la siguiente expresión pasando todos los términos a la izquierda: $2x^2 - 5x > 2$.
2. Encuentra el intervalo de solución para: $x^2 - 11x + 24 < 0$. *Pista: Al ser menor que cero, busca el sector donde el resultado sea negativo.*
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
**Reto del Analista de Datos:** ¡Ponte a prueba! Una tienda de tecnología modela la utilidad de sus ventas mediante la expresión $x^2 - 2x - 63$. Como experto, encuentra el rango de precios ($x$) para los cuales la utilidad es positiva o nula (es decir, $\geq 0$). Recuerda que en el contexto financiero, los precios no pueden ser negativos.
```

---

> [!tip] 💡 Consejo de estudio
> ¡Qué tal, amigas y amigos! Recuerden que para no hacerse líos con la multiplicación de signos, el **cero** es su mejor aliado. Si un sector de la recta numérica contiene al cero, elijan ese número para probar la expresión; es mucho más fácil calcular $(0-5)(0+2)$ que andar haciendo operaciones con números grandes. ¡Hagan la prueba y verán que no fallan!