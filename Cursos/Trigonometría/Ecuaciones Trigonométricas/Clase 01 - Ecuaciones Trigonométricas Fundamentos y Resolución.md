# Clase 01 — Ecuaciones Trigonométricas: Fundamentos y Resolución
tags: #algebra #ecuacionestrigo
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 3

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]

## 1. Importancia y Aplicaciones

Las ecuaciones trigonométricas permiten modelar fenómenos que se repiten en intervalos regulares, conocidos como fenómenos cíclicos. Su estudio es vital para determinar los instantes precisos en que una variable alcanza un valor determinado dentro de su periodo de oscilación.

*   💵 **Aplicación con $USD:** En el análisis técnico de mercados, la tasa de cambio de una divisa puede presentar comportamientos estacionales. Al modelar la fluctuación del precio del $USD mediante funciones seno o coseno, resolvemos la ecuación para identificar los **puntos de equilibrio**; es decir, los momentos exactos del ciclo financiero donde la tasa no genera pérdidas ni ganancias adicionales.
*   🏗️ **Aplicación práctica:** En ingeniería civil y arquitectura, estas ecuaciones se utilizan para calcular los ángulos de inclinación en cerchas y estructuras, garantizando que la distribución de fuerzas vectoriales cumpla con los estándares de seguridad.
*   📊 **Situación cotidiana:** El sistema de posicionamiento global (GPS) utiliza la resolución de razones trigonométricas para triangular la ubicación exacta de un dispositivo, calculando ángulos de incidencia entre satélites y receptores.

## 2. Conceptos Fundamentales

Una **Ecuación Trigonométrica** es una igualdad que involucra funciones trigonométricas (seno, coseno, etc.) donde la incógnita es el ángulo. A diferencia de una identidad (que es válida para cualquier ángulo), la ecuación solo se cumple para valores específicos.

> [!note] 📌 ¿Qué es una Ecuación Trigonométrica? (Explicación para jóvenes)
> Imagina una balanza en equilibrio. En un plato hay un número conocido y en el otro una función con un "ángulo escondido" dentro. Resolver la ecuación es como ser un detective: debemos descubrir qué ángulo específico logra que la balanza se mantenga nivelada.

> [!warning] ⚠️ Error común: La solución única
> El error más frecuente es dar una sola respuesta (ej. $x = 30^\circ$). Debido a la periodicidad de las funciones y a la naturaleza del círculo trigonométrico, las funciones repiten sus valores en distintos cuadrantes. Por ello, debemos buscar todas las soluciones en el primer ciclo ($0^\circ$ a $360^\circ$) o añadir $+ 2k\pi$ para la **solución general**.

> [!tip] 💡 Regla de los signos y ejes
> Para localizar soluciones, recuerda que el **Seno corresponde al eje Y** y el **Coseno al eje X**. Una regla mnemotécnica útil es **"SENTICOS"**:
> *   **I Cuadrante:** **T**odas son positivas.
> *   **II Cuadrante:** Solo el **S**eno es positivo (Eje Y positivo).
> *   **III Cuadrante:** Solo la **T**angente es positiva (Seno y Coseno negativos).
> *   **IV Cuadrante:** Solo el **C**oseno es positivo (Eje X positivo).

## 3. Procedimiento General de Resolución

Para resolver con rigor didáctico cualquier ecuación trigonométrica, siga estos pasos:

```text
1. Identifique: Observe si existen ángulos dobles (2x) o funciones al cuadrado que requieran identidades previas.
2. Aísle: Realice despejes algebraicos para dejar la función trigonométrica principal sola en un lado de la igualdad.
3. Determine el ángulo de referencia: Localice el valor del ángulo base buscando el resultado positivo en la tabla de ángulos notables o usando la función inversa en la calculadora (cos⁻¹, sin⁻¹).
4. Expanda: Ubique las soluciones finales en los cuadrantes correspondientes según el signo resultante (positivo o negativo) usando el círculo trigonométrico.
5. Verifique: Sustituya los ángulos en la ecuación original para confirmar que la igualdad se cumple.
```

## 4. Ejemplos Prácticos Desarrollados

> [!example] Ejemplo 1: Caso Básico
> **Ecuación:** $\sin(x) = 1/2$
> 1. En la tabla de ángulos notables, el seno es $1/2$ a los $30^\circ$. Este es nuestro ángulo base.
> 2. Como el valor es positivo, el seno también es positivo en el **II Cuadrante**.
> 3. Calculamos la segunda solución: $180^\circ - 30^\circ = 150^\circ$.
> **Soluciones:** $30^\circ$ y $150^\circ$.

> [!example] Ejemplo 2: Uso de Calculadora (Arco coseno)
> **Ecuación:** $4 \cos(x) - 3 = 0$
> 1. Despejamos: $\cos(x) = 3/4$.
> 2. Como $3/4$ no es un valor notable, aplicamos la función inversa: $x = \arccos(3/4)$.
> 3. La calculadora indica $\approx 41.4^\circ$.
> 4. El coseno es positivo también en el **IV Cuadrante**: $360^\circ - 41.4^\circ = 318.6^\circ$.
> **Soluciones:** $41.4^\circ$ y $318.6^\circ$.

> [!example] Ejemplo 3: Resultados Negativos
> **Ecuación:** $2 \sin(x) + \sqrt{3} = 0$
> 1. Despejamos: $\sin(x) = -\sqrt{3}/2$.
> 2. **Paso intermedio mental:** Buscamos el valor positivo $\sqrt{3}/2$ en la tabla; corresponde a $60^\circ$. *Nota: $60^\circ$ no es solución, solo es nuestro ángulo de referencia.*
> 3. Como el seno es **negativo**, trasladamos esos $60^\circ$ a los cuadrantes **III** y **IV**.
> 4. Cuadrante III: $180^\circ + 60^\circ = 240^\circ$.
> 5. Cuadrante IV: $360^\circ - 60^\circ = 300^\circ$.
> **Soluciones:** $240^\circ$ y $300^\circ$.

> [!example] Ejemplo 4: Factorización y Ciclos de Inversión ($USD)
> **Situación:** La tasa de retorno de una inversión en $USD se modela como $R(x) = 2 \sin(x)\cos(x) - \cos(x)$. Los ángulos de equilibrio (donde $R(x) = 0$) indican los días del ciclo financiero donde no hay pérdidas ni ganancias.
> 1. Factorizamos por factor común: $\cos(x) \cdot (2 \sin(x) - 1) = 0$.
> 2. Igualamos cada factor a cero:
>    *   **Caso A:** $\cos(x) = 0 \implies x = 90^\circ$ y $x = 270^\circ$.
>    *   **Caso B:** $2 \sin(x) - 1 = 0 \implies \sin(x) = 1/2 \implies x = 30^\circ$ y $x = 150^\circ$.
> **Soluciones:** El equilibrio se alcanza a los $30^\circ, 90^\circ, 150^\circ$ y $270^\circ$.

## 5. Práctica Independiente

> [!abstract] 🟢 Nivel Fácil (Despeje simple)
> Resuelve para $x$ en el intervalo $[0^\circ, 360^\circ]$:
> 1. $\cos(x) = 1/2$
> 2. $\tan(x) = \sqrt{3}/3$

> [!abstract] 🟡 Nivel Medio (Signos y calculadora)
> Resuelve para $x$ en el intervalo $[0^\circ, 360^\circ]$:
> 1. $2 \sin(x) + 1 = 0$
> 2. $5 \cos(x) - 2 = 0$ (Usa calculadora)

> [!abstract] 🔴 Nivel Avanzado (Aplicación $USD)
> Una fluctuación en el precio del $USD está determinada por la ecuación: $2 \sin(x)\cos(x) - \sqrt{3}\cos(x) = 0$. Factorice la expresión y halle todos los ángulos de equilibrio en el primer círculo trigonométrico.

> [!success] Respuestas para validación
> *   **Fácil:** 1) $60^\circ, 300^\circ$; 2) $30^\circ, 210^\circ$.
> *   **Medio:** 1) $210^\circ, 330^\circ$ (Ref: $30^\circ$); 2) $66.42^\circ, 293.58^\circ$.
> *   **Avanzado:** $\cos(x)(2 \sin(x) - \sqrt{3}) = 0$. Soluciones: $90^\circ, 270^\circ$ y $60^\circ, 120^\circ$.

## 6. Autoevaluación

> [!question] 1. Conceptual
> ¿Cuál es la diferencia fundamental entre una identidad y una ecuación trigonométrica?
> A) La identidad tiene soluciones infinitas y la ecuación no.
> B) La ecuación solo es válida para ciertos valores del ángulo, la identidad para todos.
> C) La ecuación no usa funciones trigonométricas.

> [!question] 2. Procedimental
> Si al despejar obtenemos $\cos(x) = -0.5$, ¿en qué cuadrantes debemos ubicar las soluciones finales?
> A) I y IV (donde X es positivo).
> B) II y III (donde X es negativo).
> C) II y IV.

> [!question] 3. Aplicada
> En un modelo de inversión donde el retorno es $\sin(x) = -1$, ¿en qué ángulo se encuentra el punto de equilibrio mínimo?
> A) $90^\circ$
> B) $180^\circ$
> C) $270^\circ$

## 7. Cierre de Clase

Hemos consolidado la técnica de resolución mediante el aislamiento de funciones y el uso estratégico del círculo trigonométrico para hallar múltiples soluciones.

> [!tip] 💡 En la próxima clase
> Elevaremos el nivel de complejidad abordando ecuaciones que incluyen **funciones al cuadrado** e **identidades pitagóricas**, herramientas indispensables cuando la ecuación presenta diferentes funciones mezcladas (ej. senos y cosenos al mismo tiempo).

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]