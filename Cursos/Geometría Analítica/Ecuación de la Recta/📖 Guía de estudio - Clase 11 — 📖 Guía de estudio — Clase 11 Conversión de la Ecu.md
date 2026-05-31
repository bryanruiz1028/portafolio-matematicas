# 📖 Guía de estudio — Clase 11: Conversión de la Ecuación General a la Ordinaria de la Recta

> [!info] 📌 Conceptos clave
> - **Ecuación General o Fundamental ($Ax + By + C = 0$):** Es la forma donde todos los términos están en un solo lado de la igualdad, igualados a cero. En esta estructura, los parámetros de la recta (pendiente e intercepto) no son evidentes a simple vista.
> - **Ecuación Ordinaria, Explícita o Punto-Pendiente ($y = mx + b$):** Es la forma donde la variable $y$ se encuentra totalmente despejada. Su gran utilidad pedagógica radica en que muestra directamente la pendiente ($m$) y la ordenada al origen ($b$).
> - **El proceso de "Despeje":** Transformar la ecuación implica aislar la $y$. Primero, movemos los términos de $x$ y la constante al otro lado del igual (invirtiendo sus signos) y, finalmente, dividimos cada término por el coeficiente de $y$.
> - **El Intercepto como Punto de Partida:** El valor de $b$ no es solo un número; es el **punto de partida** o valor inicial en el eje $Y$ para graficar el movimiento de la pendiente.

## Tabla de Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ecuación General** | $Ax + By + C = 0$ |
| **Ecuación Ordinaria / Explícita** | $y = mx + b$ |
| **Pendiente ($m$) desde la general** | $m = -\frac{A}{B}$ |
| **Ordenada al origen ($b$)** | Punto $(0, b)$ donde la recta corta el eje $Y$ (valor inicial o punto de partida). |

## Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A: Conversión Paso a Paso (Caso Básico)
**Enunciado:** Convertir la ecuación general $5x + 2y - 3 = 0$ a su forma ordinaria o explícita.

1. **Mover términos:** Trasladamos los términos que no contienen la variable $y$ al lado derecho de la igualdad, cambiando sus signos:
   $2y = -5x + 3$

2. **Despejar "y":** El coeficiente $2$ que multiplica a la $y$ pasa a dividir a toda la expresión del lado derecho:
   $y = \frac{-5x + 3}{2}$

3. **Separar términos:** Para obtener la forma $y = mx + b$, distribuimos el denominador entre ambos términos:
   $y = -\frac{5}{2}x + \frac{3}{2}$

**Resultado Final:**
- **Pendiente ($m$):** $-\frac{5}{2}$
- **Intercepto / Punto de corte ($b$):** $\frac{3}{2}$ (equivalente a $1.5$ en el eje $Y$).
```

```ad-example
title: Ejemplo B: Aplicación en Contexto Financiero ($USD)
**Enunciado:** El saldo de una deuda se rige por la ecuación general $2x + y - 10 = 0$, donde $x$ representa los días transcurridos y $y$ el saldo pendiente en dólares. Encuentre la tasa de cambio y el saldo inicial.

1. **Aislar el término con "y":** Movemos los términos $2x$ y $-10$ al lado derecho:
   $y = -2x + 10$

2. **Análisis del coeficiente:** Observamos que el coeficiente de $y$ es $1$. Por lo tanto, no es necesario realizar ninguna división adicional para completar el despeje.

3. **Identificación de elementos:**
   - La **pendiente ($m$)** es $-2$. Esto indica que la deuda disminuye $2$ USD por cada día (tasa de cambio).
   - La **ordenada al origen ($b$)**, o intercepto, es $10$.

**Conclusión:** La tasa de cambio es de $-\frac{2}{1}$ y el saldo inicial o "punto de partida" de la deuda es de $10$ USD.
```

## Ejercicios de Repaso

```ad-abstract
title: 🟢 Nivel Fácil: Conversión Directa
Transforma las siguientes ecuaciones generales a su forma ordinaria ($y = mx + b$):
1. $x + y - 5 = 0$
2. $2x + y + 4 = 0$
3. $x - y + 1 = 0$
```

```ad-abstract
title: 🟡 Nivel Medio: Coeficientes y Signos
Realiza el despeje completo considerando los cambios de signo y divisiones:
1. $6x - 2y + 8 = 0$
2. $-3x + 4y - 12 = 0$
3. $5x - 5y + 10 = 0$
```

```ad-abstract
title: 🔴 Nivel Avanzado: Aplicación con Contexto
Resuelve los problemas planteados determinando $m$ y $b$ tras la conversión:
1. **Servicios básicos:** El costo de un servicio se rige por $10x - 2y + 50 = 0$, donde $x$ son unidades consumidas. Determina el costo fijo (intercepto $b$) y el costo por unidad (pendiente $m$).
2. **Ahorros:** Un plan de ahorro mensual sigue la ecuación $3x - y + 15 = 0$. Convierte a forma explícita para identificar el crecimiento mensual del ahorro.
```

> [!tip] 💡 Consejo de estudio
> ¡Cuidado con los signos! Al usar la fórmula directa $m = -\frac{A}{B}$, recuerda que el signo negativo de la fórmula es independiente al signo del coeficiente $A$. Como enseña el **Profe Alex**, si $A$ es negativo (por ejemplo, $A = -2$), se producirá un choque de signos: $m = -\frac{(-2)}{B}$, lo que resultará en una pendiente positiva. Verifica siempre tu despeje manual comparándolo con esta fórmula para evitar errores comunes.