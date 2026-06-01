# 📖 Guía de estudio — Clase 05: Demostración y Comprobación de Identidades Trigonométricas

> [!info] 📌 Conceptos clave
> *   **Preparación de recursos:** Es fundamental contar con una hoja de fórmulas a la mano para identificar rápidamente qué sustituciones realizar. La memorización facilita la agilidad mental.
> *   **Estrategia de selección:** Comienza siempre trabajando con el lado de la igualdad que presente mayor complejidad o exponentes más altos (como potencias a la cuarta).
> *   **Conversión universal:** Una técnica altamente efectiva consiste en transformar todas las funciones (secante, cosecante, tangente) a términos de **seno y coseno**.
> *   **Transformación simultánea:** En identidades donde ambos lados son complejos, es válido transformar ambos miembros de la igualdad al mismo tiempo hasta llegar a una expresión idéntica en ambos lados.
> *   **Intencionalidad pedagógica:** No realices cambios al azar. Cada transformación debe tener un "porqué" (por ejemplo, para cancelar un denominador o reducir un exponente mediante factorización).

---

## Sección de Referencia: Fórmulas y definiciones importantes

Para resolver los ejercicios de esta clase, utilizaremos las siguientes identidades extraídas de los casos de estudio de Profe Alex:

| Categoría | Término | Fórmula / Identidad |
| :--- | :--- | :--- |
| **Pitagóricas** | Identidad Fundamental | $sen^2(\alpha) + cos^2(\alpha) = 1$ |
| | Despeje (Coseno) | $cos^2(\alpha) = 1 - sen^2(\alpha)$ |
| | Despeje (Seno) | $sen^2(\alpha) = 1 - cos^2(\alpha)$ |
| **Recíprocas** | Secante | $sec(\alpha) = \frac{1}{cos(\alpha)}$ |
| | Cosecante | $csc(\alpha) = \frac{1}{sen(\alpha)}$ |
| **Cociente** | Tangente | $tan(\alpha) = \frac{sen(\alpha)}{cos(\alpha)}$ |
| | Cotangente | $cot(\alpha) = \frac{cos(\alpha)}{sen(\alpha)}$ |
| **Producto** | Recíprocos | $sec(\alpha) \cdot cos(\alpha) = 1$ / $csc(\alpha) \cdot sen(\alpha) = 1$ |

---

## Sección de Aplicación: Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Factorización por diferencia de cuadrados
**Enunciado:** Demostrar que $sen^4(\alpha) - cos^4(\alpha) = sen^2(\alpha) - cos^2(\alpha)$.

**Paso a paso e intencionalidad:**
1. **Identificar la herramienta:** Al observar exponentes de grado 4, la **intención** es reducirlos. Usaremos la diferencia de cuadrados: $a^2 - b^2 = (a+b)(a-b)$.
2. **Reescribir:** Expresamos como potencia de una potencia para visualizar los términos:
   $(sen^2(\alpha))^2 - (cos^2(\alpha))^2$
3. **Aplicar la factorización:** Aquí $a = sen^2(\alpha)$ y $b = cos^2(\alpha)$:
   $(sen^2(\alpha) + cos^2(\alpha)) \cdot (sen^2(\alpha) - cos^2(\alpha))$
4. **Sustituir por la unidad:** El primer paréntesis es la Identidad Pitagórica. La **intención** de este paso es simplificar la multiplicación al máximo:
   $1 \cdot (sen^2(\alpha) - cos^2(\alpha))$
5. **Conclusión:** Cualquier expresión multiplicada por 1 es sí misma.
   $sen^2(\alpha) - cos^2(\alpha) = sen^2(\alpha) - cos^2(\alpha)$
```

```ad-example
title: Ejemplo B — Optimización de presupuestos en ingeniería ($USD)
**Enunciado:** El costo de materiales para un soporte estructural depende de la simplificación de la expresión: $E = [cos(\alpha) \cdot (sen^2(\alpha) - cos^2(\alpha)) \cdot sec(\alpha)] + cos^2(\alpha)$. Si cada unidad simplificada equivale a $1,000 USD, determine el costo final.

**Paso a paso e intencionalidad:**
1. **Agrupación estratégica:** Usamos la propiedad conmutativa para juntar el coseno con su recíproco (la secante). La **intención** es anular términos rápidamente:
   $E = [cos(\alpha) \cdot sec(\alpha)] \cdot (sen^2(\alpha) - cos^2(\alpha)) + cos^2(\alpha)$
2. **Sustitución recíproca:** Sabemos que $cos(\alpha) \cdot sec(\alpha) = 1$:
   $E = 1 \cdot (sen^2(\alpha) - cos^2(\alpha)) + cos^2(\alpha)$
3. **Simplificación algebraica:** Al eliminar el paréntesis, observamos términos opuestos:
   $E = sen^2(\alpha) - cos^2(\alpha) + cos^2(\alpha)$
4. **Resultado final:** Los términos $cos^2$ se anulan entre sí, dejando la expresión mínima:
   $E = sen^2(\alpha)$
5. **Cálculo monetario:** El costo final es de **$sen^2(\alpha) \times 1,000$ USD**.
```

---

## Sección de Práctica: Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel: Fácil (Sustitución Directa)
color: 0, 255, 0
1. Demuestre que $csc(\alpha) \cdot sen(\alpha) = 1$ usando la identidad recíproca de la cosecante.
2. Compruebe que $sec(\alpha) \cdot cos(\alpha) = 1$ sustituyendo la secante por su definición en cociente.
3. Verifique la igualdad $tan(\alpha) \cdot cos(\alpha) = sen(\alpha)$ transformando la tangente a senos y cosenos.
```

```ad-abstract
title: 🟡 Nivel: Medio (Operaciones y Factorización)
color: 255, 255, 0
1. Demuestre que $tan(\beta) \cdot (sec^2(\beta) - 1) = tan^3(\beta)$. (Pista: use la identidad de la tangente al cuadrado para sustituir el paréntesis).
2. Verifique mediante la suma de fracciones la siguiente identidad: $\frac{1}{cos(\alpha)} + tan(\alpha) = \frac{1 + sen(\alpha)}{cos(\alpha)}$.
3. Demuestre la siguiente igualdad: $tan(x) \cdot sec^2(x) - tan(x) = tan^3(x)$. (Pista fundamental: Identifique primero el **Factor Común** en el lado izquierdo).
```

```ad-abstract
title: 🔴 Nivel: Avanzado (Aplicación y Validación Dual)
color: 255, 0, 0
**Reto de Ingeniería Financiera:** Una constructora validará un ahorro de **$500 USD** si se comprueba la siguiente identidad mediante la transformación simultánea de ambos lados:
$$csc(\alpha) - sen(\alpha) = cot(\alpha) \cdot cos(\alpha)$$
*   **Tarea:** Transforme el lado izquierdo (realizando la resta de fracciones) y el lado derecho (sustituyendo la cotangente) de forma paralela hasta demostrar que ambos miembros son iguales a $\frac{cos^2(\alpha)}{sen(\alpha)}$. Si se logra, el ahorro es válido.
```

---

> [!tip] 💡 Consejo de estudio
> Para dominar la trigonometría, adopta la mentalidad del "Profe Alex": **no escribas pasos por inercia**. Antes de realizar cualquier cambio, haz una pausa y pregúntate: *"¿Qué busco con esta transformación?"*. Si logras visualizar mentalmente que un coseno se cancelará o que una suma se convertirá en la unidad antes de anotarlo, habrás pasado de memorizar fórmulas a entender la lógica del lenguaje matemático. No dejes que los exponentes te asusten; son solo pistas para saber qué técnica de factorización usar.