# 📖 Guía de estudio — Clase 14: Regla de tres compuesta

> [!info] 📌 Conceptos clave
> La **regla de tres compuesta** es un procedimiento matemático que utilizamos cuando en un problema intervienen **3 o más variables** (a diferencia de la simple, donde solo tenemos 2).
> 
> Para dominarla, debemos seguir estos fundamentos:
> *   **Método de comparación:** Identificamos la variable que contiene la incógnita ($x$) y la comparamos individualmente con cada una de las otras variables, suponiendo que las demás permanecen constantes.
> *   **Relaciones Directas e Inversas:**
>     *   **Directa:** Si una variable aumenta y la otra también (o ambas disminuyen). Ej: Más kg de comida, más días dura.
>     *   **Inversa:** Si una variable aumenta y la otra disminuye. Ej: Más obreros, menos días tardan.
> *   **Regla de inversión:** Al plantear la ecuación, las fracciones de las variables con relación **inversa** deben invertirse. **¿Por qué?** Hacemos esto para "compensar" el comportamiento opuesto de la variable y mantener la constante de proporcionalidad correcta.

## 2. Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Regla de tres compuesta** | Método para resolver problemas de proporcionalidad con 3 o más magnitudes. |
| **Relación Directa** | Comportamiento "más-más" o "menos-menos". La fracción se escribe igual en la ecuación. |
| **Relación Inversa** | Comportamiento "más-menos" o "menos-más". La fracción se debe invertir antes de operar. |
| **Producto Cruzado** | Procedimiento para despejar la $x$ cuando está en el denominador: se multiplican los términos en diagonal ($a/x = c/d \rightarrow a \cdot d = c \cdot x$). |

## 3. Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Caso de 3 variables (Alimentación)
**Enunciado:** 30 terneros consumen 2100 kg de pienso en 7 días. ¿Durante cuántos días se podrá alimentar a 15 terneros si tenemos 600 kg de pienso?

¡Vamos a resolverlo paso a paso!

**Paso 1: Identificación de variables y tabla**
| Terneros | Kilogramos (kg) | Días ($x$) |
| :--- | :--- | :--- |
| 30 | 2100 | 7 |
| 15 | 600 | $x$ |

**Paso 2: Determinación de relaciones (Comparando con Días)**
*   **Terneros vs. Días:** Si hay **más** terneros, la comida dura **menos** días. $\rightarrow$ **Inversa.**
*   **Kilogramos vs. Días:** Si hay **más** kilos de comida, dura **más** días. $\rightarrow$ **Directa.**

**Paso 3: Planteamiento de la ecuación y simplificación**
Ubicamos la fracción de la incógnita a un lado y las demás al otro, recordando invertir la que es inversa (Terneros):
$$\frac{7}{x} = \frac{15}{30} \cdot \frac{2100}{600}$$

**Simplificación manual (¡Sigue el truco del Profe Alex!):**
1. En $\frac{2100}{600}$, eliminamos los ceros: $\frac{21}{6}$. Sacamos tercera: $\frac{21}{6} \rightarrow \frac{7}{2}$.
2. En $\frac{15}{30}$, sacamos quinceava (o quinta y luego tercera): $\frac{15}{30} \rightarrow \frac{1}{2}$.
3. Ecuación limpia: $\frac{7}{x} = \frac{1}{2} \cdot \frac{7}{2} \rightarrow \frac{7}{x} = \frac{7}{4}$.

**Despeje con producto cruzado:**
$7 \cdot 4 = 7 \cdot x \rightarrow 28 = 7x \rightarrow x = \frac{28}{7} = 4$.

✅ **Resultado final:** Se podrá alimentar a los terneros durante **4 días**.
```

```ad-example
title: Ejemplo B — Caso de 4 variables (Construcción)
**Enunciado:** 15 obreros trabajando 7 horas diarias construyen una casa en 40 días. ¿Cuántos obreros serán necesarios para construir 8 casas iguales en 60 días trabajando 8 horas diarias?

Este parece difícil por tener más datos, ¡pero con la tabla verás que es muy sencillo!

**Paso 1: Identificación de variables y tabla**
| Obreros ($x$) | Horas | Casas | Días |
| :--- | :--- | :--- | :--- |
| 15 | 7 | 1 | 40 |
| $x$ | 8 | 8 | 60 |

**Paso 2: Comparación con la incógnita (Obreros)**
*   **Horas:** Entre más obreros, se necesitan **menos** horas diarias. $\rightarrow$ **Inversa.**
*   **Casas:** Entre más obreros, se pueden construir **más** casas. $\rightarrow$ **Directa.**
*   **Días:** Entre más obreros, se requieren **menos** días. $\rightarrow$ **Inversa.**

**Paso 3: Ecuación y ejecución**
Invertimos las variables marcadas como inversas:
*   Horas: era $7/8$, al ser inversa se escribe $8/7$.
*   Días: era $40/60$, al ser inversa se escribe $60/40$.

$$\frac{15}{x} = \frac{8}{7} \cdot \frac{1}{8} \cdot \frac{60}{40}$$

**Simplificación:**
*   Tachamos el $8$ que está arriba con el $8$ que está abajo (simplificación cruzada).
*   En $\frac{60}{40}$, quitamos ceros y sacamos mitad: $\frac{6}{4} \rightarrow \frac{3}{2}$.
*   Operamos: $\frac{15}{x} = \frac{1 \cdot 1 \cdot 3}{7 \cdot 1 \cdot 2} \rightarrow \frac{15}{x} = \frac{3}{14}$.

**Despeje:**
$15 \cdot 14 = 3 \cdot x \rightarrow 210 = 3x \rightarrow x = \frac{210}{3} = 70$.

✅ **Resultado final:** Se necesitan **70 obreros**.
```

## 4. Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel Fácil
**Problema:** 30 terneros consumen 2100 kg de pienso en 7 días. ¿Cuántos kilogramos de pienso se necesitan para alimentar a 12 terneros durante 8 días?
*(Pista: Compara los kilogramos con los terneros y con los días. Ambas relaciones son directas).*

**Respuesta sugerida:**
960 kg.
```

```ad-abstract
title: 🟡 Nivel Medio
**Problema:** Si 6 hombres realizan un muro de 30 metros trabajando 6 horas diarias durante 9 días, ¿cuántos hombres se necesitan para realizar 40 metros de muro trabajando 8 horas diarias durante 6 días?
*(Pista: Relaciona la variable "hombres" con las demás para saber cuáles invertir).*

**Respuesta sugerida:**
9 hombres.
```

```ad-abstract
title: 🔴 Nivel Avanzado
**Problema:** Un granjero tiene 1800 ovejas con alimento para 20 días. Si vende 800 ovejas y a las restantes decide darles el doble de ración, ¿para cuántos días alcanzará el alimento?

**Pista pedagógica:** 
1. Calcula las ovejas restantes: $1800 - 800 = 1000$ ovejas.
2. Agrega la variable "Ración": La ración inicial es $1$ y la nueva es $2$ (el doble).
3. Relaciona los Días ($x$) con las Ovejas (Inversa) y con la Ración (Inversa).

**Respuesta sugerida:**
18 días.
```

## 5. Consejo de estudio

> [!tip] 💡 La estrategia de simplificación del Profe Alex
> No te apresures a multiplicar números grandes. El secreto para resolver estos problemas sin calculadora y sin errores es **simplificar antes de operar**:
> 
> 1. **Elimina ceros:** Si un número arriba y otro abajo terminan en cero, táchalos.
> 2. **Saca partes:** Busca mitad, tercera o quinta. 
> 3. **Simplificación cruzada:** ¡Este es el mejor truco! Puedes simplificar **cualquier** numerador con **cualquier** denominador, siempre que estén en el mismo lado del signo igual. Por ejemplo, si tienes un 8 en la primera fracción y un 8 abajo en la tercera, ¡puedes eliminarlos de inmediato!
> 
> Esto reduce fracciones complejas a números pequeños y fáciles de manejar mentalmente.