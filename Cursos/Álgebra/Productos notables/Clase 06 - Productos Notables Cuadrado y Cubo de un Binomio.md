# Clase 06 — Productos Notables: Cuadrado y Cubo de un Binomio

**Tags:** #matemáticas #álgebra #productos-notables #educación
**Curso:** [[Curso de Álgebra desde Cero]]

> [!info] 🧭 Navegación
> [[Clase 05 - Polinomios]] | [[Clase 07 - Factorización]]

> [!info] 🌍 Relevancia y aplicaciones
> Los productos notables son herramientas poderosas que nos permiten calcular áreas y volúmenes de forma inmediata, sin tener que realizar todas las multiplicaciones término a término. 
> 
> **Aplicaciones en el mundo real:**
> - 💵 **Finanzas:** Cálculo de intereses compuestos y modelos de crecimiento de capital.
> - 🏗️ **Arquitectura:** Diseño de espacios donde se requiere escalar áreas cuadradas de forma proporcional.
> - 📊 **Estadística:** Optimización de modelos que describen comportamientos de crecimiento cuadrático.

---

¡Qué tal amigos! Espero que estén muy bien. Bienvenidos a una nueva clase donde vamos a simplificar nuestra vida matemática. No te preocupes si al principio ves muchos paréntesis; como siempre te digo, vamos a ir paso a paso.

### Concepto Clave: El "Atajo" del Binomio

> [!note] 📌 ¿Qué es el Cuadrado de un Binomio?
> Para nosotros, el cuadrado de un binomio es simplemente un **atajo**. Imagina que en lugar de caminar por toda la calle haciendo una multiplicación distributiva larga, tomas un camino directo que te da el resultado de inmediato. Es elevar un paréntesis con dos términos al exponente `$2$` (cuadrado) o `$3$` (cubo).

> [!warning] ⚠️ Error común
> Muchos estudiantes cometen el error de "repartir" el exponente así: 
> **Incorrecto:** $(a + b)^2 = a^2 + b^2$ ❌
> **Correcto:** $(a + b)^2 = a^2 + 2ab + b^2$ ✅
> **¿Por qué?** Porque al elevar al cuadrado estamos multiplicando $(a+b) \cdot (a+b)$. Además, recuerda que el primer y el tercer término **siempre serán positivos**, ya que cualquier número (positivo o negativo) elevado a una potencia par resulta en un valor positivo.

> [!tip] 💡 Truco para recordarlo (y verificarlo)
> **La Regla Cantada:** *"El primero al cuadrado, dos veces el primero por el segundo, y el segundo al cuadrado"*.
> 
> **El Secreto del Profe Alex:** Para saber si tu resultado es correcto (especialmente en cubos), revisa los exponentes: el primer término debe ir **disminuyendo** su potencia ($3, 2, 1, 0$) mientras que el segundo término debe ir **aumentando** ($0, 1, 2, 3$). ¡Si esto se cumple, vas por muy buen camino!

---

### Procedimiento paso a paso

Para resolver estos ejercicios con éxito y sin confusiones, te recomiendo seguir este orden universal:

```text
1. Identificar claramente el primer término (a) y el segundo término (b).
2. Plantear la fórmula elevando el primer término a la potencia (cuadrado o cubo).
3. Calcular los productos intermedios (doble o triple producto). 
   *Ojo: Resuelve primero las potencias y LUEGO las multiplicaciones para no fallar.*
4. Elevar el segundo término a su potencia y simplificar los signos finales.
```

---

### Ejemplos de Aplicación

```ad-example
title: Ejemplo 1 (Caso Básico)
**Resolver:** $(x + 5)^2$
1. El primer término es $x$ y el segundo es $5$.
2. Aplicamos la regla: $x^2 + 2(x)(5) + 5^2$.
3. Resolvemos: $x^2 + 10x + 25$.
**Resultado:** $x^2 + 10x + 25$. 
*(Nota que el 10x es el doble de x por 5).*
```

```ad-example
title: Ejemplo 2 (Signos y Exponentes)
**Resolver:** $(3x^3 - 2y^2)^2$
1. Aplicamos la regla con el signo negativo central: $(3x^3)^2 - 2(3x^3)(2y^2) + (2y^2)^2$.
2. Resolvemos potencias (multiplicando exponentes): $9x^6 - 2(3x^3)(2y^2) + 4y^4$.
3. Multiplicamos el término central: $9x^6 - 12x^3y^2 + 4y^4$.
**Resultado:** $9x^6 - 12x^3y^2 + 4y^4$.
```

```ad-example
title: Ejemplo 3 (Caso Avanzado - Cubo)
**Resolver:** $(3x + 2y)^3$
*Te invito a pausar el ejercicio y tratar de plantearlo tú mismo.*
1. Planteamos la fórmula: $(3x)^3 + 3(3x)^2(2y) + 3(3x)(2y)^2 + (2y)^3$.
2. **Paso crucial:** Resolvemos primero las potencias.
   $27x^3 + 3(9x^2)(2y) + 3(3x)(4y^2) + 8y^3$.
3. Ahora multiplicamos los números:
   $27x^3 + 54x^2y + 36xy^2 + 8y^3$.
**Resultado:** $27x^3 + 54x^2y + 36xy^2 + 8y^3$.
```

```ad-example
title: Ejemplo 4 (Aplicación Real $USD)
**Problema:** Una plaza de mercado cuadrada tiene un lado que mide $(x + 4)$ metros. Si el costo de pavimentación por metro cuadrado es de $10$ $USD$, ¿cuál es el costo total?
1. El área de un cuadrado es $lado^2$, entonces: $(x + 4)^2$.
2. Desarrollamos el producto notable: $x^2 + 8x + 16$ $m^2$.
3. Multiplicamos toda la expresión por el costo de $10$ $USD$: $10(x^2 + 8x + 16)$.
**Resultado:** El costo total es $10x^2 + 80x + 160$ $USD$.
```

---

### Ejercicios para el estudiante

```ad-abstract
title: 🟢 Nivel Fácil (Cuadrados simples)
1. $(m + 3)^2$
2. $(a - 2)^2$
3. $(x + 1)^2$
4. $(y - 5)^2$
```

```ad-abstract
title: 🟡 Nivel Medio (Coeficientes y Exponentes)
1. $(5m - 2)^2$
2. $(3x^2 + 1)^2$
3. $(2a + 3b)^2$
4. $(6a + 10b)^3$
```

```ad-abstract
title: 🔴 Nivel Avanzado (Problemas Aplicados)
1. Calcula el área de un terreno cuadrado cuyo lado mide $(2x + 5)$ metros.
2. Determina el volumen de un depósito cúbico de lado $(x + 2)$ metros.
3. Un muro cuadrado tiene un lado de $(a - 3)$ metros. Calcule el costo total de pintura si el metro cuadrado vale $20$ $USD$.
4. Resuelve $(2x^2 - 3y^3)^3$ aplicando la regla de signos intercalados.
```

---

### Respuestas (Para el docente)

```ad-success
**Fácil:** 1) $m^2 + 6m + 9$ | 2) $a^2 - 4a + 4$ | 3) $x^2 + 2x + 1$ | 4) $y^2 - 10y + 25$
**Medio:** 1) $25m^2 - 20m + 4$ | 2) $9x^4 + 6x^2 + 1$ | 3) $4a^2 + 12ab + 9b^2$ | 4) $216a^3 + 1080a^2b + 1800ab^2 + 1000b^3$
**Avanzado:** 1) $4x^2 + 20x + 25$ $m^2$ | 2) $x^3 + 6x^2 + 12x + 8$ $m^3$ | 3) $20a^2 - 120a + 180$ $USD$ | 4) $8x^6 - 36x^4y^3 + 54x^2y^6 - 27y^9$
```

---

### Mini-prueba de autoevaluación

```ad-question
title: Pregunta 1
¿Cuántos términos resultan siempre de desarrollar un binomio al cuadrado como $(a + b)^2$?
a) Dos términos ($a^2 + b^2$).
b) Tres términos ($a^2 + 2ab + b^2$).
c) Cuatro términos ($a^3 + 3a^2b + 3ab^2 + b^3$).
```

```ad-question
title: Pregunta 2
¿Cuál es el error en este desarrollo: $(x - 3)^2 = x^2 - 6x - 9$?
a) El término central debería ser positivo.
b) El primer término debería ser negativo.
c) El último término siempre debe ser positivo ($+9$) porque un número negativo al cuadrado da positivo.
```

```ad-question
title: Pregunta 3
Si un cuadrado tiene un lado de $(x + 1)$ metros, ¿cuál es su costo de construcción si el metro cuadrado vale $5$ $USD$?
a) $5x^2 + 10x + 5$ $USD$.
b) $5x^2 + 5$ $USD$.
c) $x^2 + 2x + 1$ $USD$.
```

---

### Cierre y Navegación Final

> [!tip] 💡 En la próxima clase
> ¡Excelente trabajo hoy! Ahora que dominas cómo expandir estos binomios, en la siguiente clase aprenderemos el camino de regreso: la **Factorización**. Veremos cómo tomar un trinomio y convertirlo de nuevo en su binomio original. ¡No te lo pierdas!

> [!info] 🧭 Navegación
> [[Clase 05 - Polinomios]] | [[Clase 07 - Factorización]]