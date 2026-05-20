# 📖 Guía de estudio — Clase 04: Conversión de la ecuación canónica a la ecuación general de la hipérbola

> [!info] 📌 Conceptos clave
> ¡Hola! En esta guía aprenderemos a transformar la ecuación canónica en su forma general siguiendo los pasos que nos enseña el Profe Alex. Para lograrlo, dominaremos estos cuatro pilares fundamentales:
> 1.  **Eliminación de denominadores:** Usamos el método de productos cruzados (cariñosamente llamado el método de la **"Carita Feliz"**) para deshacernos de las fracciones.
> 2.  **Desarrollo de binomios al cuadrado:** Expandimos los términos $(x-h)^2$ y $(y-k)^2$ aplicando la regla del trinomio cuadrado perfecto.
> 3.  **Distribución de coeficientes:** Multiplicamos los números resultantes de la operación de fracciones por cada término de nuestros binomios ya desarrollados.
> 4.  **Igualación a cero y ordenamiento:** Trasladamos todos los términos a un solo lado. Para que tu respuesta sea profesional, **siempre coloca el término cuadrático positivo primero**, siguiendo el orden: $Ax^2 + Cy^2 + Dx + Ey + F = 0$.

## 2. Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ecuación Canónica** | $\frac{(x-h)^2}{a^2} - \frac{(y-k)^2}{b^2} = 1$ |
| **Binomio al Cuadrado** | $(a \pm b)^2 = a^2 \pm 2ab + b^2$ |
| **Ecuación General** | $Ax^2 + Cy^2 + Dx + Ey + F = 0$ <br>*(Nota: $A$ y $C$ deben tener signos diferentes)* |

## 3. Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Centro en el origen
**Contexto:** Vamos a convertir una hipérbola básica con centro en $(0,0)$ para entender el movimiento de los números.
**Ecuación inicial:** $\frac{x^2}{9} - \frac{y^2}{4} = 1$

*   **Paso 1 (Multiplicación cruzada / Carita Feliz):** Multiplicamos los denominadores ($9 \times 4 = 36$) y cruzamos los términos para unificar la fracción:
    $\frac{4x^2 - 9y^2}{36} = 1$
*   **Paso 2 (Trasladar el denominador):** El $36$ que está dividiendo pasa al otro lado multiplicando al $1$:
    $4x^2 - 9y^2 = 36$
*   **Paso 3 (Resultado final):** Restamos $36$ en ambos lados para igualar a cero:
    $4x^2 - 9y^2 - 36 = 0$
```

```ad-example
title: Ejemplo B — Trayectoria de inversión ($USD)
**Contexto:** Imagina que la "curva de costos de una empresa" está definida por la siguiente trayectoria financiera. Nuestro objetivo es llevarla a su forma general para el reporte contable:
$\frac{(x+7)^2}{12} - \frac{(y-5)^2}{8} = 1$

*   **Paso 1 (Operación de fracciones):** Aplicamos el producto de denominadores ($12 \times 8 = 96$) y multiplicamos en cruz:
    $8(x+7)^2 - 12(y-5)^2 = 96$
*   **Paso 2 (Desarrollo de los binomios):** Elevamos al cuadrado con cuidado:
    $(x+7)^2 = x^2 + 14x + 49$
    $(y-5)^2 = y^2 - 10y + 25$
    Sustituimos: $8(x^2 + 14x + 49) - 12(y^2 - 10y + 25) = 96$
*   **Paso 3 (Distribución de coeficientes externos):** Multiplicamos el $8$ y el $-12$ por sus respectivos paréntesis:
    $(8x^2 + 112x + 392) - (12y^2 - 120y + 300) = 96$
*   **Paso 4 (Ordenamiento e igualación a cero):** Agrupamos los términos y resolvemos las constantes:
    $8x^2 - 12y^2 + 112x + 120y + 392 - 300 - 96 = 0$
    Simplificamos las constantes ($+392 - 396$):
    $8x^2 - 12y^2 + 112x + 120y - 4 = 0$
```

## 4. Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel Fácil
Transforma estas ecuaciones con centro en el origen $(0,0)$ a su forma general:
1. $\frac{x^2}{10} - \frac{y^2}{4} = 1$
2. $\frac{x^2}{12} - \frac{y^2}{6} = 1$
3. $\frac{y^2}{9} - \frac{x^2}{16} = 1$
```

```ad-abstract
title: 🟡 Nivel Medio
Desarrolla los binomios con centros desplazados $(h, k)$ y obtén la ecuación general:
1. $\frac{(x-4)^2}{6} - \frac{(y-0)^2}{12} = 1$
2. $\frac{(x+2)^2}{5} - \frac{(y-4)^2}{10} = 1$
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
**Reto Contable:** El flujo de caja de una inversión sigue la trayectoria de la hipérbola $\frac{(y-9)^2}{9} - \frac{(x+4)^2}{16} = 1$. 
Para procesar esto en el software contable, entrega la ecuación general. 
*Pista: Utiliza el método de denominador común $144$ (resultado de $9 \times 16$) para iniciar tu proceso.*
```

## 5. Cierre y Estrategia

> [!tip] 💡 Consejo de estudio
> ¡No caigas en la trampa! El error más común que el Profe Alex observa es olvidar el **"doble producto del primero por el segundo"** ($2ab$). Cuando veas $(y-5)^2$, no escribas simplemente $y^2 + 25$; recuerda que el término central $-10y$ es fundamental. ¡Sin ese término, tu hipérbola perdería su forma en el plano!