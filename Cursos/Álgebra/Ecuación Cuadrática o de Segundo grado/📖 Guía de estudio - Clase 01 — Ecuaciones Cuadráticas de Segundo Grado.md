# 📖 Guía de estudio — Clase 01: Ecuaciones Cuadráticas (Segundo Grado)

> [!info] 📌 Conceptos clave
> ¡Bienvenido al estudio de las ecuaciones cuadráticas! Para dominar este tema, es fundamental tener claros estos cuatro pilares:
> 1. **La forma estándar:** Una ecuación de segundo grado completa siempre se organiza como $ax^2 + bx + c = 0$.
> 2. **¿Por qué de "segundo grado"?:** Se llaman así porque el mayor exponente de la incógnita (la $x$) es **2**. Esto nos indica que, generalmente, encontraremos dos soluciones.
> 3. **La condición esencial ($a \neq 0$):** El coeficiente $a$ nunca puede ser cero. Si lo fuera, el término $x^2$ desaparecería y la ecuación pasaría a ser de primer grado.
> 4. **¿Qué significa "resolver"?:** Resolver es encontrar los valores de $x$ que, al ser sustituidos, hacen que la igualdad sea verdadera (normalmente, que todo el lado izquierdo sea igual a cero).

## Fórmulas y definiciones importantes

| Término | Definición / Estructura |
| :--- | :--- |
| **Ecuación Completa** | Posee los tres términos: cuadrático ($ax^2$), lineal ($bx$) e independiente ($c$), igualados a cero. |
| **Coeficientes ($a, b, c$)** | Números reales que acompañan a las letras. **$a$** está con $x^2$, **$b$** con $x$, y **$c$** es el número solo. |
| **Trinomio Cuadrado Perfecto (TCP)** | Se identifica si: $\text{Término central} = 2 \cdot (\sqrt{ax^2}) \cdot (\sqrt{c})$. Este caso especial produce una **única solución**. |
| **Incompletas Mixtas ($ax^2 + bx = 0$)** | Se resuelven por **Factor Común $x$**. ¡Un truco! En estas ecuaciones, una de las soluciones siempre será $x = 0$. |
| **Incompletas Puras ($ax^2 + c = 0$)** | Se resuelven mediante **Despeje** directo. Al final, se aplica una raíz cuadrada ($\pm \sqrt{}$) para obtener los dos valores. |

> [!important] ⚡ Reglas de oro antes de empezar
> Para que no falles en tus ejercicios, sigue siempre estos pasos de preparación:
> *   **Iguala a cero:** Si hay términos del lado derecho, pásalos al izquierdo cambiando su signo.
> *   **Ordena con cuidado:** Asegúrate de que el orden sea $x^2 \rightarrow x \rightarrow \text{número}$.
> *   **Coeficiente positivo:** Si el término $x^2$ es negativo, ¡multiplica toda la ecuación por $-1$! Es mucho más fácil factorizar cuando $ax^2$ es positivo.

## Ejemplos resueltos paso a paso

```ad-example
title: Ejemplo A — Factorización de trinomio simple ($x^2 + bx + c$)
**Ejercicio:** $x^2 + 5x + 6 = 0$

**Procedimiento pedagógico:**
1. **Abrir paréntesis:** Preparamos el esquema $(x \quad)(x \quad) = 0$.
2. **Regla de signos (Método Profe Alex):** El primer signo se baja igual ($+$). El segundo es el resultado de multiplicar ambos signos de la ecuación: $(+) \cdot (+) = (+)$.
3. **Buscar números:** Buscamos dos números que multiplicados den **6** y, como los signos son iguales, sumados den **5**. Los números son **3** y **2**. (Siempre coloca el mayor primero).
4. **Igualar factores a cero:**
   - $x + 3 = 0 \implies x_1 = -3$
   - $x + 2 = 0 \implies x_2 = -2$

**Resultado final:** ✅ $x_1 = -3, x_2 = -2$.
```

```ad-example
title: Ejemplo B — Aplicación de costos y equilibrio ($USD)
**Situación:** El punto de equilibrio de una microempresa se modela con la ecuación $x^2 - 12x + 36 = 0$. ¿A qué valor de producción $x$ (en cientos de USD) se alcanza el equilibrio único?

**Procedimiento pedagógico:**
1. **Verificar si es TCP:** 
   - Raíz de $x^2 = x$; Raíz de $36 = 6$.
   - Verificación: $2 \cdot (x) \cdot (6) = 12x$. ¡Es un Trinomio Cuadrado Perfecto!
2. **Factorizar:** Escribimos el binomio al cuadrado con el signo central: $(x - 6)^2 = 0$.
3. **Solución única:** Para que el resultado sea cero, la base debe ser cero:
   - $x - 6 = 0 \implies x = 6$.

**Resultado final:** ✅ El equilibrio se alcanza a los **600 USD**.
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel: Fácil
*Instrucción: Factoriza estos trinomios simples directamente.*
1. $x^2 + 2x - 35 = 0$
2. $x^2 + 10x + 24 = 0$
3. $x^2 + 12x + 32 = 0$
```

```ad-abstract
title: 🟡 Nivel: Medio
*Instrucción: ¡Aplica las Reglas de Oro! Ordena e iguala a cero antes de resolver.*
1. $x^2 = 6x + 16$
2. $4x^2 + 25 = 20x$
3. $2x^2 - 6x - 10 = x^2 - 24$
```

```ad-abstract
title: 🔴 Nivel: Avanzado (Contexto Financiero)
*Instrucción: Resuelve las siguientes situaciones aplicando despeje o factor común.*
1. **Punto de equilibrio:** Una empresa de software estima que sus pérdidas se anulan cuando $3x^2 - 12 = 0$. Halla el valor positivo de $x$ (en miles de USD) para no tener pérdidas.
2. **Optimización de recursos:** Si el costo de marketing está definido por $5x^2 - 10x = 0$, identifica los dos valores de inversión $x$ que mantienen el presupuesto en balance.
```

> [!tip] 💡 Consejo para el éxito: La Verificación
> ¡No entregues tu examen con dudas! Para estar 100% seguro, toma tu respuesta (por ejemplo, $x = -3$) y sustitúyela en la ecuación original. Si al final obtienes una identidad como $0 = 0$ o $65 = 65$, significa que tu cálculo es correcto.

¡Sigue practicando! La clave de las matemáticas es la constancia. Si tienes dudas, repasa la tabla de definiciones y asegúrate de haber seguido el orden de los signos correctamente.