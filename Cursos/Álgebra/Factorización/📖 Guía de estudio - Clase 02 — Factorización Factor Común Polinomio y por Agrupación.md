# 📖 Guía de estudio — Clase 02: Factorización por Factor Común

> [!info] 📌 Conceptos clave
> 
> ¡Hola! Hoy vamos a dominar el arte de simplificar expresiones. Para ser un experto en factorización por factor común, solo necesitas tener claros estos cuatro pilares:
> 1. **Factor Común (Letras):** Es la letra (o letras) que aparece en **todos** los términos. El secreto es elegir siempre la que tenga el **menor exponente**.
> 2. **Factor Común (Números):** Se obtiene mediante el **Máximo Común Divisor (MCD)**. Buscamos el número más grande que sea capaz de dividir a todos los coeficientes al mismo tiempo.
> 3. **La Regla del "1":** ¡Mucho ojo aquí! Si al dividir un término por el factor común el resultado es idéntico, nunca lo dejes vacío. Recuerda que cualquier cantidad dividida por sí misma es igual a $1$ (como decir $5 \div 5 = 1$). Ese $1$ es el "guardián" de la posición en el paréntesis.
> 4. **¿Cuándo agrupar?:** Si ves que no hay una letra que se repita en toda la expresión, pero tienes un polinomio de **4 o 6 términos**, es la señal para usar **Factor Común por Agrupación**. Agrupamos en parejas o tríos para encontrar factores comunes parciales.

---

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Factor Común Monomio** | Es la variable o coeficiente que se repite en cada término. Se extrae la letra con el exponente más pequeño: $x^n$ donde $n$ es el mínimo. |
| **Máximo Común Divisor (MCD)** | Es el mayor número que divide exactamente a todos los coeficientes. Se halla mediante la descomposición simultánea. |
| **Factor Común Polinomio** | Es cuando el factor repetido es un paréntesis completo, como $(a + b)$. Lo tratamos como si fuera una sola letra para extraerlo. |

---

## Ejemplos Resueltos Adicionales

### Ejemplo A — Caso de Factor Común Monomio y Numérico

```ad-example
title: Ejemplo A — Caso Básico
**Expresión a factorizar:** $16x^3y^2 - 8x^2y - 24x^4y^2 - 40x^2y^3$

**Paso 1: Hallar el MCD de los coeficientes (16, 8, 24, 40)**
Realizamos la descomposición simultánea (buscando divisores que funcionen para todos):
- 16, 8, 24, 40 | **2** (mitad)
- 8, 4, 12, 20  | **2** (mitad)
- 4, 2, 6, 10   | **2** (mitad)
- 2, 1, 3, 5    | *(Aquí paramos, ya no hay divisor común para todos)*
**MCD:** $2 \times 2 \times 2 = \mathbf{8}$.

**Paso 2: Identificar letras con menor exponente**
- Para $x$: los exponentes son 3, 2, 4, 2. El menor es **$x^2$**.
- Para $y$: los exponentes son 2, 1, 2, 3. El menor es **$y$** (exponente 1).
- **Factor Común Final:** $8x^2y$.

**Paso 3: Dividir cada término (restando exponentes)**
1. $16x^3y^2 \div 8x^2y = 2xy$
2. $8x^2y \div 8x^2y = 1$ (¡La regla del 1! No la olvides).
3. $24x^4y^2 \div 8x^2y = 3x^2y$
4. $40x^2y^3 \div 8x^2y = 5y^2$

**Resultado:** $8x^2y(2xy - 1 - 3x^2y - 5y^2)$
```

### Ejemplo B — Aplicación en Finanzas (Agrupación)

```ad-example
title: Ejemplo B — Aplicación en Finanzas
**Escenario:** En un modelo financiero, la expresión $4a^3 - 1 - a^2 + 4a$ representa el **Ingreso Total**. Factorizarla nos permite separar el **Precio Unitario** de la **Cantidad Vendida**. ¡Vamos a descifrarlo!

**Paso 1: Agrupar términos estratégicamente**
Agrupamos el primero con el cuarto (tienen el 4) y el segundo con el tercero:
$(4a^3 + 4a) + (-a^2 - 1)$

**Paso 2: Factorizar cada grupo (¡Cuidado con los signos!)**
- En el primer grupo, el factor común es $4a$: $4a(a^2 + 1)$.
- En el segundo grupo, ambos son negativos. Para que el paréntesis coincida con el anterior, **factorizamos el signo menos (o $-1$)**. 
- *Nota del experto:* Al sacar el $-1$, aplicamos la propiedad distributiva a la inversa; esto "voltea" los signos internos: $-(a^2 + 1)$. ¡Ahora los paréntesis son idénticos!

**Paso 3: Extraer el Factor Común Polinomio**
El paréntesis $(a^2 + 1)$ es ahora nuestro factor común. Lo extraemos y escribimos en otro paréntesis lo que quedó "afuera":
**Resultado final:** $(a^2 + 1)(4a - 1)$

*Interpretación:* El ingreso se compone de un factor de crecimiento $(a^2 + 1)$ y una base comercial $(4a - 1)$.
```

---

## Ejercicios de Repaso

```ad-abstract
title: Nivel 🟢 Fácil
Ideal para calentar motores. Factoriza estos monomios:
1. $x^5y^2 - x^2$
2. $3a + 3b$
3. $5x^3 - 10x^2$
```

```ad-abstract
title: Nivel 🟡 Medio
Aquí el factor es un bloque completo. ¡No te dejes confundir!
1. $m(a - b) + n(a - b)$
2. $x(a + 1) - (a + 1)$
3. $a + b + x(a + b)$ *(Pista: Imagina un paréntesis invisible en $(a + b)$ y recuerda la regla del 1)*.
```

```ad-abstract
title: Nivel 🔴 Avanzado (Aplicación USD)
**Reto de Logística:**
Una empresa calcula su costo operativo mediante la expresión:
$ax + bx + ay + by$
Donde $x$ e $y$ son costos de transporte y $a$ y $b$ son cantidades de insumos. 
**Tarea:** Factoriza la expresión por agrupación. ¿Cómo ayuda esto a un gerente a ver el costo total como una relación entre insumos y rutas?
```

---

> [!tip] 💡 Consejo de estudio
> **La Prueba de Fuego (Verificación):** ¿No estás seguro de tu resultado? ¡No te preocupes! Aplica la **propiedad distributiva** y multiplica tus factores. Si después de multiplicar regresas exactamente a la expresión original del ejercicio, significa que tu proceso es impecable. ¡La matemática no miente!