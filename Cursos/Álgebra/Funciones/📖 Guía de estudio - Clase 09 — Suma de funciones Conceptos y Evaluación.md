# 📖 Guía de estudio — Clase 09: Suma de funciones

> [!info] 📌 Conceptos clave
> - **Definición fundamental:** La suma de dos funciones se define como $(f + g)(x) = f(x) + g(x)$. En términos prácticos, consiste en sumar las expresiones algebraicas de ambas funciones.
> - **Regla de simplificación:** Tras agrupar términos semejantes, el resultado debe expresarse en **Forma Estándar**, organizando los términos de mayor a menor exponente.
> - **Regla del dominio ($D_f \cap D_g$):** El dominio de la suma es la **intersección** de los dominios de las funciones originales.
>   - *¿Por qué?* Desde un enfoque pedagógico, la función suma solo puede existir en los valores de $x$ donde **ambas** funciones originales tienen "permiso" de existir simultáneamente.
> - **Evaluación en un punto:** Para hallar $(f + g)(c)$, es metodológicamente más sencillo y seguro calcular $f(c)$ y $g(c)$ por separado y luego sumar los valores numéricos obtenidos.

## 2. TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula | Nota Adicional |
| :--- | :--- | :--- |
| **Suma de funciones** | $(f + g)(x) = f(x) + g(x)$ | Siempre utiliza **paréntesis** al sustituir funciones para proteger los signos. |
| **Dominio de la intersección** | $D_{f+g} = D_f \cap D_g$ | **Importante:** El dominio se determina intersectando las funciones originales *antes* de cualquier simplificación algebraica. |
| **Función Racional** | $\frac{P(x)}{Q(x)}; Q(x) \neq 0$ | El valor que hace que el denominador sea cero debe excluirse del dominio. |
| **Función Raíz** | $\sqrt{f(x)}; f(x) \geq 0$ | El argumento bajo una raíz cuadrada debe ser mayor o igual a cero (no se permiten negativos en $\mathbb{R}$). |

## 3. EJEMPLOS RESUELTOS - CASO BÁSICO

````ad-example
title: Ejemplo A — Suma de polinomios
Dadas las funciones:  
$f(x) = 3x + 2$  
$g(x) = 2x^2 + 5x - 6$

**Paso 1: Agrupar términos**  
Escribimos la suma protegiendo cada función:  
$(f + g)(x) = (3x + 2) + (2x^2 + 5x - 6)$

**Paso 2: Sumar términos semejantes (Forma estándar)**  
Ordenamos por el exponente mayor ($x^2$):  
1. Término cuadrático: $2x^2$  
2. Términos lineales: $3x + 5x = 8x$  
3. Términos independientes: $2 - 6 = -4$

**Resultado final:**  
$(f + g)(x) = 2x^2 + 8x - 4$ ✅
````

## 4. EJEMPLOS RESUELTOS - APLICACIÓN COTIDIANA ($USD)

````ad-example
title: Ejemplo B — Ingresos totales en una tienda
Un comerciante vende dos tipos de productos. La ganancia por el producto A sigue la función $f(x) = 10x + 50$, mientras que la del producto B sigue $g(x) = 15x - 20$, donde $x$ es el tiempo en horas. ¿Cuál es la ganancia total tras 4 horas?

**Método: Evaluación por separado (Más eficiente)**

1. **Evaluar $f(4)$:**  
   $f(4) = 10(4) + 50 = 40 + 50 = 90$ USD

2. **Evaluar $g(4)$:**  
   $g(4) = 15(4) - 20 = 60 - 20 = 40$ USD

3. **Suma de resultados:**  
   $(f + g)(4) = f(4) + g(4) = 90 + 40 = 130$

**Respuesta:** La ganancia total tras 4 horas de operación es de **130 USD**. ✅
````

## 5. EJERCICIOS DE REPASO

````ad-abstract
title: 🟢 Nivel Fácil: Suma directa
1. Si $f(x) = x + 2$ y $g(x) = 3x + 1$, halla $(f + g)(x)$.
2. Dadas $h(x) = 5x - 4$ y $j(x) = 2x + 8$, halla $(h + j)(x)$.
3. Si $f(x) = 4x$ y $g(x) = -2x + 5$, halla $(f + g)(x)$.
````

````ad-abstract
title: 🟡 Nivel Medio: Evaluación en un punto
*Instrucción: Utiliza paréntesis obligatoriamente al sustituir valores negativos.*
1. Hallar $(f + g)(-2)$ dadas las funciones racionales:
   $f(x) = \frac{3x + 8}{x^2 + 3x - 4}$ y $g(x) = \frac{x + 4}{x^2 + 5x - 2}$
2. Hallar $(f + g)(3)$ para $f(x) = 3x + 2$ y $g(x) = 2x^2 + 5x - 6$.
````

````ad-abstract
title: 🔴 Nivel Avanzado: Aplicación y Dominio
Una empresa define su gasto total $G(x)$ como la suma del costo de operación $C(x) = \frac{3}{x - 2}$ y el mantenimiento $M(x) = \sqrt{x + 2}$.
1. Expresa la función $G(x) = (C + M)(x)$.
2. Determina el dominio de $G(x)$ analizando la intersección en una recta numérica.

**Clave de solución:** 
- Restricción $C(x)$: $x \neq 2$.
- Restricción $M(x)$: $x \geq -2$.
- **Dominio final:** $[-2, 2) \cup (2, \infty)$. El valor $2$ se excluye con paréntesis por la restricción del denominador.
````

## 6. CONSEJO DE ESTUDIO

> [!tip] 💡 Estrategia de la "Carita Feliz" y Signos
> Para sumar fracciones algebraicas, visualiza la operación de la siguiente manera:
> $$\frac{a}{b} + \frac{c}{d} = \frac{(a \cdot d) + (b \cdot c)}{b \cdot d}$$
> 
> **Recomendaciones del experto:**
> 1. **Uso de Paréntesis:** Al multiplicar binomios (como $2x+3$ por $3x+1$), siempre colócalos entre paréntesis antes de aplicar la propiedad distributiva.
> 2. **Cuidado de Signos:** Si sustituyes un valor negativo, por ejemplo $x = -2$, escríbelo como $(-2)$. Esto evitará errores comunes en potencias como $(-2)^2 = 4$.