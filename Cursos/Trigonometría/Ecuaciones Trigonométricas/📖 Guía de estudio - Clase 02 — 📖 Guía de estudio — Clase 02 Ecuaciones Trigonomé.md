# 📖 Guía de estudio — Clase 02: Ecuaciones Trigonométricas (Factorización e Identidades)

> [!info] 📌 Conceptos clave
> 1. **Unificación y Síntesis:** Antes de proceder con cualquier despeje, es imperativo unificar la función trigonométrica. Si la ecuación presenta funciones mixtas (seno y coseno), aplique identidades pitagóricas para consolidar la expresión en una sola variable. La unificación es el requisito técnico previo para la factorización.
> 2. **Reconocimiento de Estructuras Algebraicas:** Identifique patrones de trinomios ($ax^2 + bx + c$) o factor común. El objetivo es reducir la complejidad trigonométrica a una estructura conocida donde la "variable" sea, por ejemplo, el $\cos(x)$.
> 3. **Restricción Geométrica del Dominio:** El rango de las funciones seno y coseno está estrictamente limitado al intervalo $[-1, 1]$. Geométricamente, esto se debe a que en el círculo unitario el radio es $1$, o bien, que la hipotenusa siempre es mayor o igual que los catetos. Cualquier valor fuera de este rango (ej. $\cos(x) = 2$) carece de solución real.
> 4. **Conversión de Argumentos (Ángulo Doble):** Es obligatorio convertir ángulos dobles ($2x$) a ángulos sencillos ($x$) mediante identidades de expansión para que todos los términos de la ecuación posean el mismo argumento y sean operables entre sí.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Identidad Pitagórica (Seno)** | Para sustituir términos cuadráticos: $\text{sen}^2(x) = 1 - \cos^2(x)$. |
| **Identidad Pitagórica (Coseno)** | Para sustituir términos cuadráticos: $\cos^2(x) = 1 - \text{sen}^2(x)$. |
| **Ángulo Doble del Seno** | Conversión obligatoria: $\text{sen}(2x) = 2\text{sen}(x)\cos(x)$. |
| **Ángulo Doble del Coseno** | **Variantes de Unificación (Cruciales):** <br> 1. $\cos^2(x) - \text{sen}^2(x)$ <br> 2. $1 - 2\text{sen}^2(x)$ (para unificar a seno) <br> 3. $2\cos^2(x) - 1$ (para unificar a coseno). |
| **Fórmula General Cuadrática** | Resuelve $ax^2 + bx + c = 0$ cuando la factorización directa no es evidente. La variable resolutiva es $\text{sen}(x)$ o $\cos(x)$: $\text{var}(x) = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$. |

---

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Factorización de Trinomio Básico
**Problema:** Resolver $\cos^2(x) - \cos(x) - 2 = 0$.

*   **Paso 1: Visualización y Reducción:** Sustituimos mentalmente $\cos(x) = u$ para transformar la complejidad trigonométrica en la forma algebraica conocida $u^2 - u - 2 = 0$.
*   **Paso 2: Factorización por trinomio:** Buscamos dos números que multiplicados resulten en $-2$ y sumados en $-1$ (los valores son $-2$ y $1$).
    $(\cos(x) - 2)(\cos(x) + 1) = 0$
*   **Paso 3: Igualación a cero de cada factor:**
    1.  $\cos(x) - 2 = 0 \Rightarrow \cos(x) = 2$.
    2.  $\cos(x) + 1 = 0 \Rightarrow \cos(x) = -1$.

✅ **Resultado y Validación:**
- Para $\cos(x) = 2$: **Sin solución**. Excede el radio unitario ($|2| > 1$).
- Para $\cos(x) = -1$: La solución es **180° ($\pi$ rad)**.
*Sugerencia pedagógica: Verifique en su calculadora digitando $\cos(180)^2 - \cos(180) - 2$; el resultado debe ser exactamente 0.*
```

```ad-example
title: Ejemplo B — Aplicación en Análisis de Mercado $USD
**Problema:** En un modelo de fluctuación financiera, la función de costos es $C(x) = 2\text{sen}^2(x) + 3\cos(x)$. Determine en qué meses ($x$) el costo iguala una ganancia proyectada de $3 USD. Considere $x \in [0, 12]$ meses, donde $360^\circ$ representa el ciclo anual completo.

*   **Paso 1: Unificación de la función:** Sustituimos $\text{sen}^2(x)$ para que toda la ecuación dependa del coseno.
    $2(1 - \cos^2(x)) + 3\cos(x) = 3$
*   **Paso 2: Simplificación algebraica:**
    $2 - 2\cos^2(x) + 3\cos(x) - 3 = 0 \Rightarrow -2\cos^2(x) + 3\cos(x) - 1 = 0$
    Multiplicamos por $-1$ para normalizar el término cuadrático: $2\cos^2(x) - 3\cos(x) + 1 = 0$.
*   **Paso 3: Factorización (Método de Aspa):**
    $(2\cos(x) - 1)(\cos(x) - 1) = 0$
    1. $2\cos(x) - 1 = 0 \Rightarrow \cos(x) = 1/2 \Rightarrow x = 60^\circ, 300^\circ$
    2. $\cos(x) - 1 = 0 \Rightarrow \cos(x) = 1 \Rightarrow x = 0^\circ, 360^\circ$

✅ **Resultado:** El costo iguala la ganancia en los meses **0, 2, 10 y 12** (calculado como $\frac{\text{ángulo}}{360} \times 12$).
En radianes: $0, \frac{\pi}{3}, \frac{5\pi}{3}, 2\pi$ rad.
```

---

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
1. **Factor Común:** Resuelva $\cos^2(x) + \cos(x) = 0$. Exprese sus soluciones en grados y radianes.
2. **Ubicación Geométrica:** Determine todos los valores de $x$ para los cuales $\text{sen}(x) = -1$ dentro del intervalo $[0, 2\pi]$.
3. **Análisis Crítico:** ¿Por qué la expresión $\cos(x) = 2$ es una inconsistencia matemática en el conjunto de los números reales? Sustente basándose en la hipotenusa del triángulo rectángulo.
```

```ad-abstract
title: 🟡 Medio
1. **Unificación Pitagórica:** Halle la solución de $\text{sen}^2(x) - \cos(x) + 1 = 0$ transformando el término cuadrático a coseno.
2. **Identidad de Argumento:** Resuelva $\text{sen}(2x) + \cos(x) = 0$ expandiendo el ángulo doble para extraer un factor común.
3. **Método de Aspa (Tijeras):** Factorice y resuelva $2\text{sen}^2(x) + 3\text{sen}(x) + 1 = 0$. 
*(Pista: Busque factores para $2\text{sen}^2(x)$ y $1$ que, multiplicados en cruz, sumen el término central $3\text{sen}(x)$).*
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
1. **Proyección de Ingresos:** Los ingresos de una consultora en miles de $USD siguen la función $I(x) = \cos(2x) + \text{sen}(x)$, donde $x$ representa el tiempo en meses transcurridos ($360^\circ = 12$ meses). Calcule en qué momentos del año el ingreso es exactamente $0.5$ ($500 USD).
*Instrucción técnica:* Utilice la identidad de ángulo doble para unificar a seno, aplique la **fórmula general cuadrática** y utilice la función **Arcoseno** para obtener los ángulos decimales. Valide sus resultados con la tecla **Ans** de su calculadora.
```

---

> [!tip] 💡 Consejo de estudio del experto
> Evite la memorización mecánica de tablas de ángulos. Utilice siempre el **círculo trigonométrico** para visualizar los cuadrantes, especialmente cuando trabaje con valores negativos (ej. el seno es negativo en el III y IV cuadrante). 
> 
> **Estrategia de validación:** Al obtener un resultado decimal complejo en su calculadora, no borre la pantalla. Utilice la tecla **Ans** (Answer) para sustituir el valor exacto en la ecuación original. Si la igualdad se cumple (ej. $0 = 0$ o un valor cercano como $1 \times 10^{-10}$), su procedimiento es correcto. No ignore la importancia de entregar sus respuestas finales en **radianes** para cumplir con los estándares técnicos internacionales.