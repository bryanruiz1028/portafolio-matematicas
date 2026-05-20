# 📖 Guía de estudio — Clase 05: Solución de la ecuación cuadrática completando cuadrados

> [!info] 📌 Conceptos clave
> - **Objetivo del método:** ¡Hola! El objetivo principal es transformar una ecuación con términos $x^2$ y $x$ en una expresión con una sola $x$. Esto nos permite "despejar" la incógnita de forma directa.
> - **La regla del coeficiente 1:** Para que este truco funcione, el coeficiente que acompaña a $x^2$ (llamado $a$) debe ser 1. Si no lo es, dividimos toda la ecuación por $a$. ¿Por qué? Porque esto simplifica la estructura y nos asegura que el binomio al cuadrado que formaremos sea exacto.
> - **El término mágico:** El número que completa el trinomio se calcula como $(\frac{b}{2})^2$.
> - **Propiedad del valor absoluto:** Recuerda que al aplicar raíz cuadrada a un término al cuadrado, obtenemos un valor absoluto: $\sqrt{(algo)^2} = |algo|$. Esto es lo que explica por qué aparecen dos soluciones ($\pm$).

## Tabla de Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ecuación Cuadrática Estándar** | $ax^2 + bx + c = 0$ |
| **Tercer término (Completación)** | $(\frac{b}{2})^2$ (Se obtiene dividiendo el coeficiente de $x$ entre $2$ y elevándolo al cuadrado). |
| **Factorización del Trinomio** | $(x + \frac{b}{2})^2$ (El signo es el mismo que el del término lineal $bx$). |

---

## Ejemplos Resueltos Detallados

```ad-example
title: Ejemplo A — Caso con raíces exactas
**¡Vamos a resolverlo paso a paso!**
**Ecuación:** $x^2 + 6x - 16 = 0$

**Sigue este camino:**
1. **Mover el término independiente:** Llevamos el $-16$ al otro lado con signo opuesto.
   $x^2 + 6x = 16$
2. **Completar el cuadrado:** Calculamos el tercer término: $(\frac{6}{2})^2 = 3^2 = 9$. Sumamos $9$ en ambos lados para mantener el equilibrio:
   $x^2 + 6x + 9 = 16 + 9$
   $x^2 + 6x + 9 = 25$
3. **Factorizar y aplicar valor absoluto:** Factorizamos el trinomio como $(x + 3)^2$ y aplicamos raíz cuadrada:
   $\sqrt{(x + 3)^2} = \sqrt{25}$
   $|x + 3| = 5$ 
   *(¡Aquí está el secreto! El valor absoluto genera las dos opciones: $+5$ y $-5$)*.
   $x + 3 = \pm 5$
4. **Obtener soluciones:**
   $x_1 = 5 - 3 = 2$
   $x_2 = -5 - 3 = -8$

**Resultado final ✅:** $x_1 = 2, x_2 = -8$
```

```ad-example
title: Ejemplo B — Aplicación de costos en $USD
**Contexto:** El costo de producción de un artículo sigue la ecuación estándar $x^2 - 10x - 3 = 0$. Encuentra el valor de $x$ (unidades) que satisface este gasto.

**¡Tú puedes, sigue estos pasos!**
1. **Preparar la ecuación:** Pasamos el $-3$ al lado derecho.
   $x^2 - 10x = 3$
2. **Completar el cuadrado:** Calculamos $(\frac{-10}{2})^2 = (-5)^2 = 25$. Sumamos $25$ en ambos lados:
   $x^2 - 10x + 25 = 3 + 25$
   $(x - 5)^2 = 28$
3. **Aplicar raíz cuadrada:** Como $\sqrt{28}$ no es exacta, usamos una aproximación decimal.
   $|x - 5| = \sqrt{28}$
   $x - 5 \approx \pm 5.29$
4. **Despejar $x$:**
   $x \approx 5 \pm 5.29$
   $x_1 \approx 5 + 5.29 = 10.29$
   $x_2 \approx 5 - 5.29 = -0.29$

**Análisis pedagógico:** En el mundo real (unidades producidas), no podemos tener $-0.29$ artículos. Por lo tanto, tomamos la solución lógica positiva.
**Resultado final ✅:** $x \approx 10.29$ unidades.
```

---

## Ejercicios de Repaso Categorizados

```ad-abstract
title: 🟢 Fácil
Resuelve estas ecuaciones aplicando el método de completación:
1. $x^2 - 8x + 12 = 0$
2. $x^2 + 12x + 5 = 0$ (Nota: puedes dejar la raíz expresada si no es exacta).
3. $x^2 + 6x - 16 = 0$
```

```ad-abstract
title: 🟡 Medio
¡Cuidado aquí! Primero divide toda la ecuación por el coeficiente de $x^2$ para que $a = 1$:
1. $2x^2 + 8x - 24 = 0$
2. $4x^2 + 2x - 5 = 0$
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
**Problema de análisis:** Una empresa calcula que el tiempo necesario para equilibrar su presupuesto mensual sigue la ecuación $2x^2 + 5x - 7 = 0$, donde $x$ representa el tiempo en meses. 
1. Transforma la ecuación dividiendo por $a$.
2. Completa los cuadrados para hallar $x_1$ y $x_2$.
3. **Pregunta de reflexión:** Si obtienes una solución negativa, ¿tiene sentido para medir el tiempo en meses? Indica cuál es la respuesta correcta para el negocio.
```

---

> [!tip] 💡 Consejo de estudio
> Al terminar, adquiere el hábito de **verificar tus resultados**. Reemplaza los valores de $x$ obtenidos en la ecuación original. Si al operar todo el resultado es $0$, ¡felicidades, eres un experto! Como dice el "profe Alex", la comprobación es tu mejor aliada para estar seguro de tu éxito.