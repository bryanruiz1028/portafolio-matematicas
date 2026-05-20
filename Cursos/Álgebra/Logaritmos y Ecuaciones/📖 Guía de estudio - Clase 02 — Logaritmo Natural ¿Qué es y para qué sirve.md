# 📖 Guía de estudio — Clase 02: El Logaritmo Natural

> [!info] 📌 Conceptos clave
> - **El número $e$:** Es un número irracional muy famoso conocido como el **Número de Euler**. Su valor aproximado es **$2.718281...$** y tiene infinitas cifras decimales que no se repiten.
> - **¿Qué es el $ln$?:** El Logaritmo Natural (también llamado **Logaritmo Neperiano**) es simplemente un logaritmo cuya base es el número $e$. Es la forma abreviada de escribir $\log_e$.
> - **La Base "Invisible":** ¡Ojo! Cuando veas $ln(x)$, la base $e$ está ahí, pero es **invisible**. Siempre que leas $ln$, recuerda mentalmente que la base es $e$.
> - **Relación y Propiedades:** Todo logaritmo busca un exponente ($\text{Base}^{\text{exponente}} = \text{Argumento}$). Por eso, $ln(1) = 0$ (porque $e^0 = 1$) y $ln(e) = 1$ (porque $e^1 = e$).

---

### Sección: Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Número $e$** | Número de Euler; es un número irracional con valor aproximado de **$2.718281$**. |
| **Logaritmo Natural ($ln$)** | También llamado **Logaritmo Neperiano**. Equivale a escribir $\log_e$. |
| **Argumento** | Es el número al que se le aplica el logaritmo (el resultado de la potencia). |
| **Base** | Es el número que se eleva al exponente. En el logaritmo natural, la base siempre es **$e$**. |

---

### Sección: Ejemplos Resueltos

```ad-example
title: Ejemplo A — Caso básico
**Problema:** Hallar el valor de $ln(e)$.

**Paso a paso:**
1. **Traducir el símbolo:** Recordamos que $ln(e)$ es lo mismo que escribir $\log_e(e)$.
2. **Hacerse la pregunta clave:** ¿A qué exponente debo elevar la base ($e$) para que el resultado sea el argumento ($e$)?
3. **Plantear la ecuación mental:** $e^{?} = e$.
4. **Conclusión:** Como cualquier número elevado a la 1 es igual a sí mismo ($e^1 = e$), el exponente que buscamos es **1**.

**Resultado:** $ln(e) = 1$.
```

```ad-example
title: Ejemplo B — Aplicación con crecimiento $USD$
**Problema:** Imagina que una inversión de $1 USD$ crece siguiendo una fórmula que usa el número $e$. En este tipo de problemas, el **tiempo** suele ser el exponente. 

Si después de un tiempo "$x$" tu inversión alcanza un valor igual a $e$, la ecuación sería:
$e^x = e$

Para hallar el tiempo, usamos el logaritmo natural:
$x = ln(e)$

Como ya sabemos que el exponente para que $e$ se convierta en $e$ es 1, el tiempo transcurrido es **1 año** (o la unidad de tiempo que se use). El $ln$ nos sirve para "bajar" el exponente y descubrir el tiempo.
```

---

### Sección: Ejercicios de Repaso

```ad-abstract
title: 🟢 Nivel Fácil (Identificación)
1. En la expresión $ln(15)$, ¿cuál es la base invisible y cuál es el argumento?
2. Identifica la base y el argumento en la expresión $ln(100)$.
3. Si tienes el logaritmo $ln(w)$, indica qué número representa la base y qué letra es el argumento.
```

```ad-abstract
title: 🟡 Nivel Medio (Cálculo y Conversión)
1. Calcula mentalmente el valor de $ln(1)$. (Pista: ¿A qué número elevas la base para que te dé 1?).
2. Convierte la expresión larga $\log_e(50)$ a su forma abreviada de logaritmo natural.
3. Escribe el logaritmo $ln(20)$ en su "forma larga" (utilizando la palabra $\log$ y su base correspondiente).
```

```ad-abstract
title: 🔴 Nivel Avanzado (Contexto Financiero)
1. Supongamos que el crecimiento de una empresa en dólares depende del logaritmo natural:
   - Si la empresa no crece y se mantiene en su capital inicial de $1 USD$, el éxito se mide como $ln(1)$. ¿Cuál es el valor del éxito en este caso?
   - Si la empresa crece hasta alcanzar exactamente el valor de la base $e$, el éxito es $ln(e)$. ¿Qué valor toma el éxito en ese momento?
```

---

### Sección: Consejo de Estudio

> [!tip] 💡 Consejo de estudio
> Para resolver cualquier logaritmo sin confundirte, el mejor truco es **pensar en voz alta**. Cada vez que veas un ejercicio, hazte siempre la misma pregunta: **"¿A qué número debo elevar la base para que me dé el argumento?"**. Si te acostumbras a razonar así, ¡resolverás los logaritmos naturales mucho más rápido que usando una calculadora!