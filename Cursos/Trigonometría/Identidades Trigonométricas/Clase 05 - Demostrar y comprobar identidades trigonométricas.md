# Clase 05 — Demostrar y comprobar identidades trigonométricas
tags: #algebra #proveandchecktr
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 5 de 5

> [!info] 🧭 Navegación
> [[Clase 04|⬅ Clase 04]] | [[00 - Índice del curso|Índice]] | **Clase 05** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]

## 1. ¿Por qué es importante esta clase?
Las identidades trigonométricas permiten simplificar modelos complejos en física y navegación, transformando expresiones extensas en formas manejables para el cálculo de trayectorias y fuerzas.

*   💵 [Modelado de fluctuaciones de precios en mercados de divisas $USD].
*   🏗️ [Cálculo de tensiones en estructuras de ingeniería civil].
*   📊 [Análisis de ondas en telecomunicaciones para señales de radio].

## 2. Concepto clave

> [!note] **¿Qué es demostrar una identidad?**
> Es el proceso de mostrar que dos expresiones son iguales para cualquier valor del ángulo, como una **balanza que siempre está en equilibrio**. Como bien señala el Profe Alex, demostrar no es simplemente "hacer pasos por hacerlos"; requiere una intención estratégica para elegir el camino con menos resistencia algebraica.

> [!warning] **Error común: El "Efecto Ecuación"**
> El error más grave es tratar la identidad como una ecuación donde se busca el valor de "x".
> *   ❌ **Incorrecto:** Pasar términos sumando a restar o multiplicando a dividir al otro lado del igual.
> *   ✅ **Correcto:** Trabajar cada lado de forma independiente o transformar un miembro hasta que sea idéntico al otro.

> [!tip] **Regla mnemotécnica**
> "Si te pierdes o no ves el camino claro, pasa todo a Senos y Cosenos".

## 3. Procedimiento paso a paso
Para abordar cualquier demostración con rigor pedagógico, sigue este flujo de trabajo:

```text
PASO 1 → Identificar el lado más complejo o con mayores exponentes para simplificar.
PASO 2 → Aplicar factorizaciones (Diferencia de cuadrados o Factor común) si es necesario.
PASO 3 → Reemplazar funciones (Secante, Cosecante, Tangente) por sus equivalentes en Seno y Coseno.
PASO 4 → Realizar operaciones algebraicas (suma de fracciones heterogéneas, simplificación de términos o propiedad distributiva) para igualar ambos lados.
```

## 4. Ejemplos resueltos

### Ejemplo 1: Simplificación estratégica (Video 5)
**Identidad:** $\cos(\alpha) (\sin^2(\alpha) - \cos^2(\alpha)) \sec(\alpha) + \cos^2(\alpha) = \sin^2(\alpha)$

1.  **Análisis:** Aplicamos la propiedad conmutativa para agrupar $\cos(\alpha)$ con $\sec(\alpha)$.
2.  **Sustitución:** Sabemos que $\sec(\alpha) = \frac{1}{\cos(\alpha)}$.
3.  **Simplificación:** El producto $\cos(\alpha) \cdot \frac{1}{\cos(\alpha)}$ se **simplifica a 1** (funciones recíprocas).
4.  **Reducción:** La expresión queda $(\sin^2(\alpha) - \cos^2(\alpha)) + \cos^2(\alpha)$.
5.  **Resultado:** Los términos $-\cos^2(\alpha)$ y $+\cos^2(\alpha)$ se anulan, resultando en $\sin^2(\alpha) = \sin^2(\alpha)$.

### Ejemplo 2: Potenciación y Factorización (Video 6)
**Identidad:** $\sin^4(\alpha) - \cos^4(\alpha) = \sin^2(\alpha) - \cos^2(\alpha)$

1.  **Propiedad de potencia:** Antes de factorizar, entendemos que $\sin^4(\alpha) = (\sin^2(\alpha))^2$ y $\cos^4(\alpha) = (\cos^2(\alpha))^2$.
2.  **Diferencia de cuadrados:** Aplicamos la fórmula $a^2 - b^2 = (a+b)(a-b)$.
3.  **Factorización:** $( \sin^2(\alpha) + \cos^2(\alpha) ) \cdot ( \sin^2(\alpha) - \cos^2(\alpha) )$.
4.  **Identidad Pitagórica:** Reconocemos que $\sin^2(\alpha) + \cos^2(\alpha) = 1$.
5.  **Resultado:** $1 \cdot (\sin^2(\alpha) - \cos^2(\alpha)) = \sin^2(\alpha) - \cos^2(\alpha)$.

### Ejemplo 3: Transformación simultánea y "Carita Feliz" (Video 7)
**Identidad:** $\csc(A) - \sin(A) = \cot(A) \cdot \cos(A)$

1.  **Lado Izquierdo:** Sustituimos $\csc(A) = \frac{1}{\sin(A)}$. Aplicamos el **método de la carita feliz** (producto cruzado) para la resta:
    $$\frac{1}{\sin(A)} - \frac{\sin(A)}{1} = \frac{1 - \sin^2(A)}{\sin(A)}$$
2.  **Identidad Pitagórica:** Transformamos el numerador: $1 - \sin^2(A) = \cos^2(A)$. El lado izquierdo queda $\frac{\cos^2(A)}{\sin(A)}$.
3.  **Lado Derecho:** Sustituimos $\cot(A) = \frac{\cos(A)}{\sin(A)}$. Al multiplicar por el otro $\cos(A)$, obtenemos $\frac{\cos^2(A)}{\sin(A)}$.
4.  **Conclusión:** Ambos lados son idénticos: $\frac{\cos^2(A)}{\sin(A)} = \frac{\cos^2(A)}{\sin(A)}$.

### Ejemplo 4: Aplicación en Inversiones ($USD)
Demuestra que el modelo de tasa $\sec(\theta) - \cos(\theta)$ equivale a $\sin(\theta) \cdot \tan(\theta)$.

1.  **Sustitución:** $\frac{1}{\cos(\theta)} - \cos(\theta)$.
2.  **Operación:** $\frac{1 - \cos^2(\theta)}{\cos(\theta)}$.
3.  **Identidad:** El numerador es $\sin^2(\theta)$.
4.  **Descomposición:** $\frac{\sin(\theta) \cdot \sin(\theta)}{\cos(\theta)} = \sin(\theta) \cdot \frac{\sin(\theta)}{\cos(\theta)}$.
5.  **Resultado:** $\sin(\theta) \cdot \tan(\theta)$.

## 5. Ejercicios para el estudiante

```ad-abstract
title: 🟢 Nivel Fácil: Reemplazo directo
1. $\tan(x) \cdot \cos(x) = \sin(x)$
2. $\cot(x) \cdot \sin(x) = \cos(x)$
3. $\sin(x) \cdot \csc(x) = 1$
4. $\cos(x) \cdot \sec(x) = 1$
```

```ad-abstract
title: 🟡 Nivel Medio: Factorización y Fracciones
1. $\cos(x) \cdot (\sec(x) - \sin(x) \cdot \tan(x)) = \cos^2(x)$
2. $\tan(b) \cdot \sec^2(b) - \tan(b) = \tan^3(b)$ (Pista: Factor común)
3. $\frac{1 - \sin^2(x)}{\cos(x)} = \cos(x)$
4. $\sin^2(x) \cdot \cot^2(x) + \sin^2(x) = 1$
```

```ad-abstract
title: 🔴 Nivel Avanzado: Aplicaciones Financieras ($USD)
1. Demuestra que si el costo marginal es $\sec^2(x) - \tan^2(x)$, el costo es constante a 1 $USD.
2. Comprueba si un flujo de caja $\frac{\sin(x)}{\tan(x)}$ equivale a un ingreso de $\cos(x) \text{ USD}$.
3. Verifica si la volatilidad $\csc^2(x) - \cot^2(x)$ siempre arroja un valor de 1 $USD.
4. Demuestra que el beneficio $(\sin(x) + \cos(x))^2 - 2\sin(x)\cos(x)$ es igual a 1 $USD.
```

```ad-success
title: Guía de soluciones para el docente
- **Fácil:** Se resuelven sustituyendo funciones por sus razones fundamentales ($\frac{s}{c}$, $\frac{c}{s}$, etc.).
- **Medio:** En (2) se extrae factor común $\tan(b)$, quedando $\tan(b)(\sec^2(b) - 1)$, donde el paréntesis es $\tan^2(b)$.
- **Avanzado:** 
  1. Identidad pitagórica derivada: $1 + \tan^2 = \sec^2 \Rightarrow \sec^2 - \tan^2 = 1$.
  2. $\frac{\sin(x)}{\frac{\sin(x)}{\cos(x)}} = \cos(x)$ tras simplificar.
  3. Identidad pitagórica derivada: $1 + \cot^2 = \csc^2 \Rightarrow \csc^2 - \cot^2 = 1$.
  4. Al expandir el binomio queda $\sin^2 + 2\sin\cos + \cos^2 - 2\sin\cos = \sin^2 + \cos^2 = 1$.
```

## 6. Mini-prueba de autoevaluación

1.  **¿Qué identidad pitagórica es clave para simplificar $\sin^2(\theta) + \cos^2(\theta)$?**
    *   a) $\tan^2(\theta) + 1$
    *   b) $1$
    *   c) $\sec^2(\theta)$
    *   *Respuesta: **b**. Es la identidad fundamental: la suma de los cuadrados de seno y coseno es la unidad.*

2.  **Al simplificar $\sin^4(\alpha) - \cos^4(\alpha)$, ¿cuál es el paso previo a la factorización?**
    *   a) Pasar a senos y cosenos.
    *   b) Aplicar la propiedad de potencia de una potencia $(\sin^2)^2$.
    *   c) Restar los exponentes.
    *   *Respuesta: **b**. Para aplicar diferencia de cuadrados, debemos ver los términos como cuadrados perfectos.*

3.  **¿Cuál es el resultado de simplificar el flujo de caja $\frac{\sin(x)}{\tan(x)}$?**
    *   a) $1 \text{ USD}$
    *   b) $\cos(x) \text{ USD}$
    *   c) $\tan(x) \text{ USD}$
    *   *Respuesta: **b**. Al sustituir $\tan(x) = \frac{\sin(x)}{\cos(x)}$, los senos se simplifican a 1 y el coseno sube al numerador.*

## 7. Cierre y Navegación
Felicidades por concluir el Bloque 2. Recuerda que demostrar identidades no es solo un ejercicio de memoria, sino de agilidad mental. Esta capacidad de simplificar expresiones complejas será tu herramienta más valiosa al enfrentar integrales por sustitución trigonométrica en tus futuros cursos de Cálculo Integral.

> [!info] 🧭 Navegación
> [[Clase 04|⬅ Clase 04]] | [[00 - Índice del curso|Índice]] | **Clase 05** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]