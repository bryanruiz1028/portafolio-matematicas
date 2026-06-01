# 📖 Guía de estudio — Clase 01: Ecuaciones Trigonométricas

¡Hola! Soy tu profesor y hoy vamos a dominar el mundo de las ecuaciones trigonométricas. Este tema puede parecer desafiante al principio, pero si comprendes la lógica del círculo y el uso correcto de tu calculadora, verás que es un proceso muy sistemático. ¡Vamos a ello!

> [!info] 📌 Conceptos clave
> - **¿Qué es una ecuación trigonométrica?** Es una igualdad donde la incógnita ($x$) no es un número cualquiera, sino la **rotación o ángulo desconocido** dentro de una función.
> - **La naturaleza de las soluciones:** Debido a que las funciones son periódicas (se repiten), estas ecuaciones suelen tener múltiples soluciones en un giro ($0^\circ$ a $360^\circ$) e incluso infinitas si no limitamos el rango.
> - **El Círculo Trigonométrico:** ¡Es tu mejor aliado! Nos sirve para ubicar en qué cuadrantes los signos de las funciones coinciden con nuestro despeje y así encontrar todas las soluciones.
> - **Uso de Funciones Inversas:** Para liberar a la $x$, aplicamos el "arco" de la función ($\text{sen}^{-1}$ o $\cos^{-1}$). Esto le pregunta a la calculadora: "¿Qué ángulo tiene este valor?".

---

### 📊 Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ecuación Trigonométrica** | Igualdad matemática que solo se cumple para valores específicos del ángulo $x$. |
| **Identidad Pitagórica base** | $\text{sen}^2(x) + \cos^2(x) = 1$ (Fundamental para simplificar expresiones). |
| **Función Inversa (Arco)** | El proceso para despejar el ángulo. Si $\cos(x) = a$, entonces $x = \cos^{-1}(a)$. |
| **Signos por Cuadrante** | **Seno (+):** I y II (Eje $Y$ positivo). <br> **Coseno (+):** I y IV (Eje $X$ positivo). <br> **Tangente (+):** I y III (División de signos iguales). |

---

### 📝 Ejemplos Resueltos

```ad-example
title: Ejemplo A: Caso Básico con Calculadora
**Ecuación:** $4\cos(x) - 3 = 0$

1. **Despeje inicial:** Pasamos el 3 sumando y el 4 dividiendo.
   $$\cos(x) = \frac{3}{4}$$
2. **Uso de la calculadora:** Aplicamos la función inversa. ¡Ojo! Como $3/4$ no es un ángulo notable, obtendremos un valor decimal.
   $$x = \cos^{-1}(0.75) \approx 41.4^\circ$$
   *Nota: Este valor es una **aproximación**. Al verificarlo, el resultado no será cero exacto, sino un número muy pequeño.*
3. **Búsqueda de la segunda solución:** El coseno es positivo en el IV cuadrante. Para hallarlo, restamos nuestro ángulo del giro completo:
   $$x_2 = 360^\circ - 41.4^\circ = 318.6^\circ$$
**Soluciones estimadas:** $41.4^\circ$ y $318.6^\circ$.
```

```ad-example
title: Ejemplo B: Aplicación Real (Fluctuación de precios USD)
**Problema:** El precio de una divisa fluctúa según el modelo $2\text{sen}(x) + \sqrt{3} = 0$. Hallar los momentos (ángulos) de equilibrio.

1. **Despeje:**
   $$2\text{sen}(x) = -\sqrt{3} \implies \text{sen}(x) = -\frac{\sqrt{3}}{2}$$
2. **Análisis de signos:** Como el seno es negativo, buscamos soluciones en los cuadrantes III y IV (donde el eje $Y$ es negativo).
3. **Regla de oro (Ángulo de Referencia):** Para no confundirnos, **ignoramos el signo negativo** un momento y buscamos en la tabla: ¿Cuándo el $\text{sen}(x) = \sqrt{3}/2$? La respuesta es $60^\circ$. ¡Este es nuestro ángulo de referencia!
4. **Cálculo de soluciones reales:**
   - **Cuadrante III:** $180^\circ + 60^\circ = 240^\circ$
   - **Cuadrante IV:** $360^\circ - 60^\circ = 300^\circ$
**Respuesta:** El equilibrio se alcanza a los $240^\circ$ y $300^\circ$. ¡Este paso es vital para no perder soluciones!
```

---

### ✍️ Ejercicios de Repaso

```ad-abstract
title: 🟢 Nivel: Fácil
1. Halla las dos soluciones para la ecuación: $\cos(x) = \frac{\sqrt{2}}{2}$.
2. Determina el valor de $x$ para la ecuación: $\tan(x) = 1$. (Pista: Revisa el cuadrante III).
```

```ad-abstract
title: 🟡 Nivel: Medio
1. Resuelve $2\cos(x) + 1 = 0$. ¡Cuidado! El despeje resultará en un valor negativo; busca los cuadrantes donde el coseno (eje $X$) sea negativo.
2. Simplifica y resuelve: $3\text{sen}(x) + 5\text{sen}(x) + 1 = 6$. Primero suma los términos semejantes de seno para poder despejar.
```

```ad-abstract
title: 🔴 Nivel: Avanzado (Modelo de Tasas de Interés)
**Ecuación:** $2\text{sen}(x)\cos(x) - \cos(x) = 0$

**Instrucción:** ¡No te asustes! Factoriza por **factor común** $\cos(x)$. Esto dividirá tu problema en dos partes:
1. $\cos(x) = 0$
2. $2\text{sen}(x) - 1 = 0$

**Reto:** Encuentra las **4 soluciones** posibles entre $0^\circ$ y $360^\circ$. 
*Hint: Recuerda que cada factor te dará dos soluciones distintas en el círculo.*
```

---

> [!tip] 💡 Consejo de estudio: La Verificación
> ¡No te quedes con la duda! Siempre sustituye el ángulo hallado en la ecuación original. Si tu calculadora muestra un número como **$4.4 \times 10^{-4}$** (que en pantalla puede verse como `4.4E-4`), significa **$0.0004$**. Este valor es prácticamente **cero**, lo que confirma que tu aproximación es correcta. ¡La calculadora es tu herramienta de seguridad!