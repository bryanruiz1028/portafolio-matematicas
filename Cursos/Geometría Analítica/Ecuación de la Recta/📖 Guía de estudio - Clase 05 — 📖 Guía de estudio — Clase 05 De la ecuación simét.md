# 📖 Guía de estudio — Clase 05: De la ecuación simétrica a la forma general de la recta

> [!info] 📌 Conceptos clave
> 1. **Igualdad a la unidad:** La ecuación simétrica (también llamada segmentaria) se reconoce porque siempre debe estar igualada a **1**.
> 2. **Corte en el eje X:** El denominador debajo de la variable $x$ (denominado $a$) indica el punto exacto donde la recta cruza el eje horizontal: $(a, 0)$.
> 3. **Corte en el eje Y:** El denominador debajo de la variable $y$ (denominado $b$) indica el punto donde la recta cruza el eje vertical: $(0, b)$.
> 4. **Meta de la forma general:** Consiste en transformar la ecuación a la forma $Ax + By + C = 0$, eliminando denominadores y buscando que el primer término ($Ax$) sea preferiblemente positivo para que la expresión sea más limpia.

---

# Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ecuación Simétrica/Segmentaria** | $\frac{x}{a} + \frac{y}{b} = 1$ |
| **Ecuación General** | $Ax + By + C = 0$ |
| **Punto de corte en X ($a$)** | Coordenada donde la recta toca el eje X: $(a, 0)$. |
| **Punto de corte en Y ($b$)** | Coordenada donde la recta toca el eje Y: $(0, b)$. |

---

# Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A — Caso básico
**Problema:** Convierte la ecuación $\frac{x}{2} + \frac{y}{5} = 1$ a su forma general.

**Paso 1: Suma de fracciones (Método de la carita feliz).**
Multiplicamos los denominadores para obtener el común: $2 \times 5 = 10$.
Multiplicamos en cruz para el numerador: $(x \times 5) + (2 \times y) = 5x + 2y$.
La ecuación se transforma en: $\frac{5x + 2y}{10} = 1$.

**Paso 2: Eliminar el denominador.**
El $10$ que está dividiendo pasa al otro lado a multiplicar al $1$:
$5x + 2y = 1 \times 10 \Rightarrow 5x + 2y = 10$.

**Paso 3: Igualar a cero.**
Trasladamos el término independiente al lado izquierdo con signo contrario para dejar la ecuación "limpia":
**$5x + 2y - 10 = 0$** (Forma General).
```

```ad-example
title: Ejemplo B — Aplicación con presupuesto de materiales $USD
**Enunciado:** Un proyecto escolar tiene un presupuesto limitado. El ahorro ($x$) y el gasto ($y$) están representados por la ecuación: $\frac{x}{10} + \frac{y}{20} = 1$. Encuentra la forma general.

**Paso 1: Suma de fracciones.**
Denominador común: $10 \times 20 = 200$.
Numerador en cruz: $20x + 10y$.
Ecuación: $\frac{20x + 10y}{200} = 1$.

**Paso 2: Despeje inicial.**
Pasamos el $200$ a multiplicar: $20x + 10y = 200$.
Igualamos a cero: $20x + 10y - 200 = 0$.

**Paso 3: Simplificación obligatoria.**
Siguiendo el estándar del Profe Alex, siempre buscamos la forma más simple. Como todos los términos son divisibles entre $10$, dividimos toda la ecuación:
$(20x + 10y - 200 = 0) \div 10$
**Resultado final:** **$2x + y - 20 = 0$**.
```

---

# Ejercicios de Repaso

```ad-abstract
title: 🟢 Nivel Verde (Fácil)
Convierte las siguientes ecuaciones simétricas a su forma general:
1. $\frac{x}{3} + \frac{y}{4} = 1$
2. $\frac{x}{5} + \frac{y}{2} = 1$
3. $\frac{x}{6} + \frac{y}{3} = 1$ (No olvides simplificar el resultado final).
```

```ad-abstract
title: 🟡 Nivel Amarillo (Medio)
**Nota pedagógica:** Al multiplicar en cruz, el signo negativo se queda con el número del denominador (ej. $-3 \times y = -3y$).
4. $\frac{x}{-3} + \frac{y}{4} = 1$
5. $\frac{x}{2} + \frac{y}{-5} = 1$
6. $\frac{x}{-2} + \frac{y}{-6} = 1$
```

```ad-abstract
title: 🔴 Nivel Rojo (Avanzado)
Convierte a la forma general simplificada ($Ax + By + C = 0$) para facilitar el análisis de costos:
7. Un negocio de tecnología define su inversión mediante: $\frac{x}{50} + \frac{y}{100} = 1$.
8. La relación entre gastos de transporte ($x$) y alimentación ($y$) es: $\frac{x}{15} + \frac{y}{30} = 1$.
9. Para un evento, la relación entre costo de publicidad ($x$) y producción ($y$) es: $\frac{x}{40} + \frac{y}{80} = 1$.
```

---

> [!tip] 💡 Consejo de estudio
> Antes de empezar con el álgebra, realiza una **verificación visual**. Ubica los puntos $a$ y $b$ en el plano cartesiano usando la ecuación simétrica. Una vez que obtengas tu ecuación general, si decides graficarla usando otro método (como tabla de valores o pendiente-ordenada), la recta **debe pasar exactamente por esos mismos puntos**. Si no coinciden, ¡revisa tu despeje de signos!