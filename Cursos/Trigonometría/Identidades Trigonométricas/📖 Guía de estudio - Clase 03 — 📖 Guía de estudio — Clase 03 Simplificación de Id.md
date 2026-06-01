# 📖 Guía de estudio — Clase 03: Simplificación de Identidades Trigonométricas

> [!info] 📌 Conceptos clave
> 1. **Verificación vs. Simplificación:** Verificar una identidad consiste en demostrar, mediante procesos lógicos, que un lado de la igualdad es equivalente al otro. Simplificar es el proceso de reducir una expresión compleja a su forma más básica, generalmente expresándola en términos de Seno y Coseno.
> 2. **Los dos pilares de la resolución:** Para resolver cualquier identidad, solo existen dos caminos: realizar **cambios/transformaciones** (sustituir por fórmulas) y ejecutar **operaciones** (sumas, productos notables, simplificación de fracciones). **Regla estratégica:** Siempre que sea posible realizar una operación algebraica antes de transformar, se debe priorizar la operación para reducir la complejidad desde el inicio.
> 3. **Criterio de selección:** El camino más eficiente es elegir el lado de la igualdad que presente mayor complejidad (más términos, paréntesis o exponentes) para transformarlo hasta alcanzar la expresión del lado más sencillo.
> 4. **La Regla de Oro de los exponentes:** Las identidades recíprocas y de cociente son válidas para cualquier exponente ($Sen^n, Tan^n$, etc.), ya que, por propiedades de las igualdades, si $a = b$, entonces $a^n = b^n$. Por el contrario, las identidades pitagóricas son exclusivas para el exponente 2 ($Sen^2 + Cos^2 = 1$) y no pueden alterarse sin romper la igualdad fundamental.

## 2. TABLA DE FÓRMULAS Y DEFINICIONES

| **Término** | Definición / Fórmula |
| :--- | :--- |
| **Tangente** (en función de $Sen$ y $Cos$) | $Tan(A) = \frac{Sen(A)}{Cos(A)}$ |
| **Cotangente** (en función de $Sen$ y $Cos$) | $Cot(A) = \frac{Cos(A)}{Sen(A)}$ |
| **Identidad Pitagórica fundamental** | $Sen^2(A) + Cos^2(A) = 1$ |
| **Despeje de Coseno al cuadrado** | $Cos^2(A) = 1 - Sen^2(A)$ |
| **Despeje de Seno al cuadrado** | $Sen^2(A) = 1 - Cos^2(A)$ |
| **Identidad Recíproca (Seno)** | $Sen(A) = \frac{1}{Csc(A)}$ |
| **Identidad Recíproca (Cosecante)** | $Csc(A) = \frac{1}{Sen(A)}$ |

---

## 3. EJEMPLOS RESUELTOS ADICIONALES

````ad-example
title: Ejemplo A — Identidad de Coseno Doble 
**Problema:** Comprobar la siguiente identidad: $Cos^2(A) - Sen^2(A) = 2Cos^2(A) - 1$.

**Estrategia de resolución:** 
Al observar el objetivo (lado derecho), notamos que solo existe la función $Cos^2(A)$. Esto convierte al término $Sen^2(A)$ del lado izquierdo en un **"intruso"** que debe ser transformado para que toda la expresión hable el mismo "idioma" matemático.

**Paso a paso:**
1. **Transformar el intruso:** Sustituimos $Sen^2(A)$ usando su despeje pitagórico: $1 - Cos^2(A)$.
   $$Cos^2(A) - (1 - Cos^2(A))$$
2. **Operar para eliminar paréntesis:** El signo negativo afecta a ambos términos internos.
   $$Cos^2(A) - 1 + Cos^2(A)$$
3. **Simplificación final:** Agrupamos términos semejantes ($1 Cos^2 + 1 Cos^2$).
   $$2Cos^2(A) - 1$$
**Conclusión:** La identidad queda verificada al demostrar que ambos lados son iguales.
````

````ad-example
title: Ejemplo B — Optimización de Costos de Señal
**Problema:** En un proyecto de ingeniería, el costo de mantenimiento mensual ($USD) de un sensor está definido por la expresión $\frac{Sen(A)}{Tan(A)}$. Simplifique la expresión para analizar el comportamiento del costo según el ángulo de fase $A$.

**Paso a paso:**
1. **Sustitución técnica:** Cambiamos $Tan(A)$ por su identidad de cociente.
   $$\frac{Sen(A)}{\frac{Sen(A)}{Cos(A)}}$$
2. **Operación de fracciones (Extremos y Medios):** Asumimos un denominador $1$ para el $Sen(A)$ superior.
   $$\frac{\frac{Sen(A)}{1}}{\frac{Sen(A)}{Cos(A)}} = \frac{Sen(A) \cdot Cos(A)}{Sen(A)}$$
3. **Simplificación de factores:** Eliminamos el factor común $Sen(A)$ en el numerador y denominador.
   $$Cos(A)$$
**Análisis del Especialista:** El costo simplificado es $Cos(A)$ $USD. Esto implica que a medida que el ángulo $A$ se acerca a $90^\circ$, el costo tiende a cero ($Cos(90^\circ) = 0$), optimizando el presupuesto del proyecto.
````

---

## 4. EJERCICIOS DE REPASO

````ad-abstract
title: Nivel Verde (Fácil)
1. Utilizando las identidades pitagóricas, reduzca a una sola función: $1 - Cos^2(\theta)$.
2. Simplifique el producto $Tan(A) \cdot Cos(A)$ aplicando la identidad de cociente de la tangente.
````

````ad-abstract
title: Nivel Amarillo (Medio)
Demuestre la siguiente identidad partiendo del lado más complejo. Recuerde identificar al "intruso" basándose en el resultado esperado:
$$Sen^2(\theta) - Cos^2(\theta) = 1 - 2Cos^2(\theta)$$
*Nota: Asegúrese de mantener la consistencia del ángulo $\theta$ en todo su desarrollo.*
````

````ad-abstract
title: Nivel Rojo (Avanzado)
El presupuesto de una infraestructura en millones de $USD se calcula mediante la simplificación de la expresión:
$$P = \frac{Tan(A) - Cot(A)}{Tan(A) + Cot(A)}$$
a) Reduzca la expresión a términos de $Sen(A)$ y $Cos(A)$ realizando las operaciones de fracciones heterogéneas.
b) Calcule el presupuesto final si el ángulo de diseño es $A = 45^\circ$.
*(Dato: $Sen(45^\circ) = \frac{\sqrt{2}}{2}, Cos(45^\circ) = \frac{\sqrt{2}}{2}$)*.
````

---

## 5. CONSEJO DE ESTUDIO

> [!tip] 💡 Consejo de estudio
> **La visión antes que la acción:** Nunca comience a transformar términos al azar. Antes de escribir el primer paso, fije su mirada en el objetivo (el otro lado de la igualdad). Si su meta es llegar a "Cosenos", sus transformaciones deben estar dirigidas a eliminar "Senos". La trigonometría es un juego de estrategia: se gana sabiendo a dónde se quiere llegar.