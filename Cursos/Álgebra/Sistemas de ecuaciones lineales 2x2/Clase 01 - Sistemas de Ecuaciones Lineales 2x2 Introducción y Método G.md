# Clase 01 — Sistemas de Ecuaciones Lineales 2x2: Introducción y Método Gráfico

#algebra #sistemasdeecuac
**Curso:** Bloque 1 | Lección 1 de 8

> [!info] 🧭 Navegación
> - **Anterior:** [[Índice General]]
> - **Siguiente:** [[Clase 02 — Métodos de Sustitución e Igualación]]

---

## 2. Relevancia y Aplicaciones
Un sistema de ecuaciones es una herramienta matemática que nos permite encontrar valores desconocidos que deben cumplir varias condiciones al mismo tiempo. En lugar de resolver una sola situación aislada, buscamos el "punto de equilibrio" donde dos realidades o restricciones distintas coinciden.

Sus aplicaciones prácticas incluyen:
- 💵 **Finanzas:** Calcular el costo unitario de productos cuando solo conocemos el total de compras combinadas en `$USD$`.
- 🏗️ **Ingeniería:** Determinar la distribución de fuerzas en una estructura para asegurar que se mantenga estable bajo múltiples cargas simultáneas.
- 📊 **Análisis de Opciones:** Comparar dos planes de servicios (como telefonía o streaming) para saber exactamente en qué punto ambos cuestan lo mismo.

---

## 3. Concepto Clave

Un sistema de ecuaciones $2 \times 2$ consiste en dos ecuaciones que comparten las mismas dos incógnitas (generalmente $x$ e $y$). Resolverlo significa encontrar un par de números que, al ser reemplazados en las letras, hagan que ambas igualdades sean ciertas al mismo tiempo.

> [!note] 📌 ¿Qué es un Sistema de Ecuaciones $2 \times 2$?
> Es un conjunto de **dos** ecuaciones con **dos** variables (incógnitas). Se busca un valor para cada variable que satisfaga ambas expresiones simultáneamente. Visualmente, se representan agrupadas por una llave $\{$.

> [!warning] ⚠️ Error común
> Encontrar una respuesta que solo funcione para una de las ecuaciones.
> - `❌ Incorrecto:` En el sistema de $x + y = 5$ y $x - y = 1$, decir que $x = 5, y = 0$ es la solución (esto solo funciona en la primera ecuación).
> - `✅ Correcto:` La solución debe ser $x = 3, y = 2$, pues $3 + 2 = 5$ **Y ADEMÁS** $3 - 2 = 1$.

> [!tip] 💡 Truco para recordarlo
> Imagina que cada ecuación es un camino recto en un mapa. El sistema de ecuaciones es como buscar el **"punto de encuentro"** o la intersección donde ambos caminos se cruzan. Si las líneas no se tocan, ¡aún no has encontrado el "código secreto" que abre ambas puertas!

---

## 4. Procedimiento Paso a Paso (Método Gráfico)

Para resolver un sistema mediante gráficas, seguimos la metodología estructurada del Profe Alex:

```text
PASO 1: Despejar la variable "y" en ambas ecuaciones.
PASO 2: Construir una tabla de valores para cada ecuación (se recomienda x = 0, 1, 2).
PASO 3: Graficar ambas rectas en el mismo plano cartesiano.
PASO 4: Identificar el punto de intersección y realizar la comprobación.
```

> [!abstract] 🧠 ¿Por qué despejamos "$y$"?
> Despejar la variable $y$ es una recomendación pedagógica clave. Al dejar la ecuación en la forma $y = mx + b$, el cálculo de la tabla de valores se vuelve directo y mecánico, facilitando la visualización de la recta en el plano.

---

## 5. Ejemplos Desarrollados

> [!example] Ejemplo 1: Caso Básico
> **Sistema:**
> 1) $y = 4 - x$
> 2) $y = 2x - 5$
> 
> **Desarrollo:**
> - **Tabla 1 ($y = 4 - x$):** Si $x=0, y=4$; si $x=1, y=3$; si $x=2, y=2$.
> - **Tabla 2 ($y = 2x - 5$):** Si $x=0, y=-5$; si $x=1, y=-3$; si $x=2, y=-1$.
> - **Gráfica:** La intersección ocurre en el punto $(3, 1)$.
> 
> **Comprobación:**
> - Ec 1: $1 = 4 - 3 \Rightarrow 1 = 1$ ✅
> - Ec 2: $1 = 2(3) - 5 \Rightarrow 1 = 6 - 5 \Rightarrow 1 = 1$ ✅
> - **Resultado:** $x = 3, y = 1$.

> [!example] Ejemplo 2: Con Signos y Despeje
> **Sistema:**
> 1) $-x + y = 1$
> 2) $-2x + 4y = -8$
> 
> **Desarrollo:**
> - **Despeje:** 
>   - Ec 1: $y = 1 + x$
>   - Ec 2: $4y = -8 + 2x \Rightarrow y = \frac{-8 + 2x}{4}$
> - **Valores (Ec 2):** Si $x=0, y=-2$; si $x=2, y=-1$.
> - **Gráfica:** Al alargar las rectas, se cruzan en $(-6, -5)$.
> 
> **Comprobación:**
> - Ec 1: $-(-6) + (-5) = 6 - 5 = 1$ ✅
> - Ec 2: $-2(-6) + 4(-5) = 12 - 20 = -8$ ✅
> - **Resultado:** $x = -6, y = -5$.

> [!example] Ejemplo 3: Caso Avanzado (Fracciones)
> **Sistema:**
> 1) $5x - 3y = 9$
> 2) $x + y = 5$
> 
> **Desarrollo:**
> - **Despeje Ec 1:** $y = \frac{5x - 9}{3}$.
> - **Tabla de valores (Ec 1):** 
>   - Si $x=0, y=-3$. 
>   - Si $x=1, y=\frac{5(1)-9}{3} = -4/3$. 
> - **Técnica de Graficado:** Para ubicar $-4/3$, dividimos la unidad en el eje $y$ en **tres partes iguales** (tercios) y contamos 4 partes hacia abajo desde el origen.
> - **Gráfica:** La intersección se encuentra en $(3, 2)$.
> 
> **Comprobación:**
> - Ec 1: $5(3) - 3(2) = 15 - 6 = 9$ ✅
> - Ec 2: $3 + 2 = 5$ ✅

> [!example] Ejemplo 4: Aplicación en $USD$
> **Problema:** Un helado ($x$) y un dulce ($y$) cuestan juntos $5$ $USD$. Si la diferencia de precio entre el helado y el dulce es de $1$ $USD$, ¿cuánto cuesta cada uno?
> **Ecuaciones:**
> 1) $x + y = 5$
> 2) $x - y = 1$
> 
> **Comprobación Visual:** Al graficar, la intersección está en $(3, 2)$.
> - $3 + 2 = 5$ $USD$ (Suma total)
> - $3 - 2 = 1$ $USD$ (Diferencia)
> - **Conclusión:** El helado cuesta $3$ $USD$ y el dulce $2$ $USD$.

---

## 6. Ejercicios para el Estudiante

> [!abstract] Actividades de Práctica
>
> **Nivel Verde (Fácil - Ya despejadas):**
> 1. $y = x + 1$ ; $y = -x + 3$
> 2. $y = 2x$ ; $y = x + 2$
> 3. $y = 4 - x$ ; $y = x$
> 4. $y = 3$ ; $y = x + 1$
>
> **Nivel Amarillo (Medio - Requiere despeje simple):**
> 1. $x + y = 4$ ; $x - y = 2$
> 2. $2x + y = 5$ ; $x + y = 3$
> 3. $-x + y = 0$ ; $x + y = 2$
> 4. $x + 2y = 6$ ; $x - y = 0$
>
> **Nivel Rojo (Avanzado - Problemas en $USD$):**
> 1. La suma de dos productos es $20$ $USD$ y su diferencia es $4$ $USD$. Encuentra sus precios $(x, y)$.
> 2. El doble del precio de $X$ más el precio de $Y$ es $12$ $USD$. Si el precio de $X$ y $Y$ es el mismo, halla los valores.
> 3. Compré dos artículos por $15$ $USD$. El primero ($x$) costó el doble que el segundo ($y$).
> 4. $x + y = 10$ $USD$. El precio de $y$ es igual al de $x$ más $2$ $USD$.

> [!success] Clave de Respuestas
> **Verde:** 1) $(1, 2)$ | 2) $(2, 4)$ | 3) $(2, 2)$ | 4) $(2, 3)$
> **Amarillo:** 1) $(3, 1)$ | 2) $(2, 1)$ | 3) $(1, 1)$ | 4) $(2, 2)$
> **Rojo:** 1) $(12, 8)$ | 2) $(4, 4)$ | 3) $(10, 5)$ | 4) $(4, 6)$

---

## 7. Autoevaluación y Cierre

> [!question] Pregunta 1
> ¿Qué requisitos debe cumplir un par ordenado $(x, y)$ para ser considerado la solución legítima de un sistema?
> *Respuesta: Debe hacer que ambas ecuaciones del sistema sean verdaderas simultáneamente tras la sustitución.*

> [!question] Pregunta 2
> En el método gráfico, ¿qué representa físicamente el punto donde se cortan las dos rectas?
> *Respuesta: Representa la solución única, el único par de valores que satisface ambas condiciones al mismo tiempo.*

> [!question] Pregunta 3
> Si un dulce ($x$) y un chocolate ($y$) cuestan $10$ $USD$ en total, y el chocolate cuesta el triple que el dulce ($y = 3x$), ¿cuál es el precio del dulce?
> A) $2$ $USD$
> B) $2.5$ $USD$
> C) $5$ $USD$
> *Respuesta correcta: B ($2.5$ $USD$, ya que $2.5 + 3(2.5) = 10$).*

> [!tip] 💡 En la próxima clase
> Ahora que sabes visualizar las soluciones, aprenderemos a encontrarlas de forma exacta mediante el rigor del álgebra, sin depender de la precisión de nuestro trazo, usando los **Métodos de Sustitución e Igualación**.

---
> [!info] 🧭 Navegación
> - **Anterior:** [[Índice General]]
> - **Siguiente:** [[Clase 02 — Métodos de Sustitución e Igualación]]