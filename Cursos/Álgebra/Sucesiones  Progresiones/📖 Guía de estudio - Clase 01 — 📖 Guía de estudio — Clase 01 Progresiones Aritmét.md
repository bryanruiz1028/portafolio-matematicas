# 📖 Guía de estudio — Clase 01: Progresiones Aritméticas

# 1. Fundamentos Iniciales

> [!info] 📌 Conceptos clave
> 
> *   **Definición:** Una progresión aritmética es una sucesión de números donde la diferencia entre dos términos consecutivos es siempre constante. Cada término se obtiene sumando esa constante al anterior.
> *   **Naturaleza de la diferencia ($d$):** Este valor puede ser positivo (la sucesión es creciente/aumenta) o negativo (la sucesión es decreciente/disminuye).
> *   **Nomenclatura básica:** Identificamos el primer término como $a_1$, la posición de un término como $n$, y el valor en dicha posición como el término n-ésimo ($a_n$).
> *   **Utilidad del término general:** Es una herramienta matemática que nos permite calcular directamente cualquier término de la progresión sin necesidad de escribir toda la secuencia manualmente.

# 2. Sección de Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Progresión Aritmética** | Sucesión donde cada valor nuevo resulta de sumar una constante (diferencia) al término anterior. |
| **Diferencia ($d$)** | El salto constante entre términos. Se halla restando un término menos el anterior: $d = a_n - a_{n-1}$. |
| **Primer término ($a_1$)** | Es el valor numérico que da inicio a la secuencia. |
| **Término n-ésimo ($a_n$)** | Representa el valor numérico ubicado específicamente en la posición $n$. |
| **Fórmula Fundamental** | $a_n = a_1 + (n - 1)d$ |
| **Fórmula (Término $k$)** | $a_n = a_k + (n - k)d$ |

> [!abstract] 💡 Nota Didáctica
> En las fórmulas anteriores, utilizamos $(n-1)$ o $(n-k)$ porque estamos contando los **intervalos** o saltos de crecimiento entre términos. El primer término ($a_1$) no tiene la diferencia sumada aún, por ello se resta 1 a la posición total.

# 3. Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A — Hallar un término específico
**Problema:** Dada la sucesión 5, 8, 11, 14..., calcula el noveno término ($a_9$).

**Paso a paso:**
1. **Identificar datos:**
   - Primer término ($a_1$) = 5.
   - Diferencia ($d$) = $8 - 5 = 3$.
   - Posición buscada ($n$) = 9.
2. **Aplicar fórmula:** $a_n = a_1 + (n - 1)d$
3. **Sustituir y operar:**
   - $a_9 = 5 + (9 - 1) \cdot 3$
   - $a_9 = 5 + (8) \cdot 3$
   - $a_9 = 5 + 24$
   **Resultado:** $a_9 = 29$.
```

```ad-example
title: Ejemplo B — Ahorro constante
**Problema:** Un estudiante comienza un plan de ahorro. La primera semana guarda $15 USD ($a_1$) y cada semana siguiente guarda $5 USD adicionales ($d$). ¿Cuánto dinero ahorrará **específicamente en la semana 10** ($a_{10}$)?

**Paso a paso:**
1. **Identificar datos:**
   - Primer ahorro ($a_1$) = 15.
   - Incremento semanal ($d$) = 5.
   - Semana objetivo ($n$) = 10.
2. **Aplicar fórmula:** $a_{10} = a_1 + (n - 1)d$
3. **Sustituir y operar:**
   - $a_{10} = 15 + (10 - 1) \cdot 5$
   - $a_{10} = 15 + (9) \cdot 5$
   - $a_{10} = 15 + 45$
   **Resultado:** El estudiante ahorrará $60 USD durante la semana 10.
```

# 4. Ejercicios de Repaso

```ad-abstract
title: 🟢 Fácil
1. Identifica la diferencia ($d$) en la siguiente serie: 2, 5, 8, 11...
2. Identifica el primer término ($a_1$) en la serie: 15, 9, 3...
3. Si una serie disminuye de 6 en 6 constantemente, ¿la diferencia ($d$) es un número positivo o negativo?
```

```ad-abstract
title: 🟡 Medio
1. Hallar el término $a_{20}$ si se sabe que $a_1 = 7$ y la diferencia es $d = 5$.
2. En la sucesión 15, 9, 3..., calcula el valor del término número 12 ($a_{12}$) considerando que $d = -6$.
3. Si en una progresión aritmética el término $a_7 = 13$ y el término siguiente $a_8 = 17$, ¿cuál es la diferencia ($d$)?
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
1. Un producto cuesta $100 USD y su valor aumenta $2 USD cada mes de forma constante. ¿Cuánto costará en el mes 24?
2. Una deuda de $500 USD disminuye $40 USD cada mes. ¿Cuál será el saldo de la deuda en el mes 5?
3. Aplicando la fórmula de término conocido ($a_k$): Si en el mes 10 ($a_{10}$) tienes un saldo de $20 USD y la diferencia mensual es de $5 USD, ¿cuánto dinero tenías en el mes 4 ($a_4$)?
```

# 5. Cierre y Estrategia de Estudio

> [!tip] 💡 Consejo de estudio
> Para evitar errores comunes identificados por el "profe Alex", sigue estas reglas de oro:
> 1. **Verificación de la diferencia:** No te confíes. Verifica la diferencia restando siempre de derecha a izquierda: un término menos el que está inmediatamente atrás ($a_2 - a_1$).
> 2. **Jerarquía de operaciones:** En la fórmula $a_1 + (n-1)d$, la multiplicación de la diferencia por el paréntesis se realiza **antes** de sumar el primer término.
> 3. **Sentido común:** Si la progresión disminuye, asegúrate de que tu diferencia sea negativa en la fórmula; de lo contrario, el resultado será incorrecto.

# 6. Clave de Respuestas

A continuación, encontrarás los resultados para verificar tu progreso:

**Nivel Fácil:**
1. $d = 3$
2. $a_1 = 15$
3. Negativa ($-6$)

**Nivel Medio:**
1. $a_{20} = 102$
2. $a_{12} = -51$
3. $d = 4$

**Nivel Avanzado:**
1. $146 USD
2. $340 USD
3. $a_4 = -10 USD (Nota: Indica que en ese punto la progresión pasaba por un valor negativo o deuda antes de subir).