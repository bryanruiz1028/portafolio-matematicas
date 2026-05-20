# Clase 04 — Propiedades de la potenciación combinadas
tags: #algebra #propiedadesdela
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 4 de 4

> [!info] 🧭 Navegación
> [[Clase 03|⬅ Clase 03]] | [[00 - Índice del curso|Índice]] | **Clase 04** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]

## 1. ¿Por qué es importante esta clase?

Dominar las propiedades combinadas es el paso final para simplificar expresiones algebraicas complejas. Al reducir "expresiones gigantes" a resultados ordenados, no solo evitamos errores en cálculos posteriores, sino que optimizamos procesos en áreas técnicas y científicas.

- 💵 **Finanzas:** Cálculo de proyecciones de inversión y depreciación de activos en $USD$, donde las tasas de interés se aplican de forma exponencial sobre varios periodos.
- 🏗️ **Ingeniería:** Simplificación de fórmulas de resistencia y diseño estructural donde las variables de carga y distancia aparecen con múltiples exponentes.
- 📊 **Big Data:** Gestión de almacenamiento masivo. Los sistemas procesan datos en potencias de base $2$ o $10$, y simplificar los exponentes permite calcular la capacidad de servidores de forma instantánea.

## 2. Concepto clave

> [!note] 📌 ¿Qué son las Propiedades Combinadas?
> Es el arte de usar todas las reglas de los exponentes al mismo tiempo para que una expresión gigante se vea pequeña y ordenada. Un ejercicio se considera **terminado** solo si cumple estas reglas:
> 1. Cada base (letra o número) aparece **una sola vez**.
> 2. No existen **paréntesis** ni signos de agrupación.
> 3. No hay **exponentes negativos** (se deben transformar en positivos).
> 4. Los números reales con exponentes pequeños se **resuelven** (ej. $4^3 = 64$).

> [!warning] ⚠️ Error común: El muro invisible
> No es lo mismo una potencia de potencia con paréntesis que sin ellos. El paréntesis actúa como un "muro" que obliga a multiplicar.
> - **Sin paréntesis (Torre):** $n^{2^4} = n^{16}$ (Se resuelve primero el exponente de arriba: $2 \times 2 \times 2 \times 2 = 16$).
> - **Con paréntesis:** $(n^2)^4 = n^8$ (Se multiplican los exponentes debido al "muro": $2 \times 4 = 8$).

> [!tip] 💡 Truco para recordarlo
> - **Paso 1:** Rompo el muro (elimino paréntesis).
> - **Paso 2 y 3:** Limpio la casa (uno las bases iguales).
> - **Paso 4:** Saco la basura (muevo los exponentes negativos y resuelvo números).

## 3. Procedimiento paso a paso

Para resolver como un experto, sigue este orden lógico recomendado por el **Profe Alex**:

```text
PASO 1 → ROMPER EL MURO: Multiplica exponentes internos por externos para eliminar paréntesis.
PASO 2 → LIMPIAR LA CASA (A): Une bases que se multiplican sumando sus exponentes.
PASO 3 → LIMPIAR LA CASA (B): Une bases que se dividen restando sus exponentes.
PASO 4 → SACAR LA BASURA: Mueve los exponentes negativos (al denominador o numerador) y resuelve potencias numéricas finales.
```

## 4. Ejemplos de resolución

```ad-example
title: Ejemplo 1 — Caso básico (Unión de letras)
Simplificar $m^2 \cdot m^3 \cdot (m^4)^2$
1. **Quitar paréntesis:** $m^2 \cdot m^3 \cdot m^8$ (multiplicamos $4 \times 2$).
2. **Unir bases iguales:** $m^{2+3+8} = m^{13}$.
✅ **Resultado:** $m^{13}$
```

```ad-example
title: Ejemplo 2 — Caso con fracciones (Simplificación vertical)
$\frac{(x^2 \cdot y^3 \cdot x^3)^3}{x \cdot y^5}$
1. **Distribuir exponente externo:** $\frac{x^6 \cdot y^9 \cdot x^9}{x \cdot y^5}$ (multiplicando cada exponente interno por $3$).
2. **Unir bases arriba:** $\frac{x^{15} \cdot y^9}{x \cdot y^5}$ (sumamos $6 + 9$ para las $x$).
3. **Simplificación vertical:** Restamos exponentes donde haya más cantidad.
   - Para $x$: $15 - 1 = 14$ (quedan arriba).
   - Para $y$: $9 - 5 = 4$ (quedan arriba).
✅ **Resultado:** $x^{14} y^4$
```

```ad-example
title: Ejemplo 3 — Caso avanzado (Corchetes y negativos)
$[(a^2 \cdot b \cdot c^{-2})^{-2}]$
1. **Multiplicar exponentes:** $a^{-4} \cdot b^{-2} \cdot c^4$ (recuerda: $-2 \times -2 = +4$).
2. **Saca la basura (Negativos):** $c^4$ se queda arriba. Las bases $a$ y $b$ bajan al denominador con exponente positivo.
✅ **Resultado:** $\frac{c^4}{a^4 \cdot b^2}$
```

```ad-example
title: Ejemplo 4 — Aplicación real con $USD
Un fondo de inversión crece a razón de $(10^2)^3$ USD por cada $10^3$ inversionistas. ¿Cuánto aporta cada uno?
1. **Simplificar numerador:** $(10^2)^3 = 10^6$.
2. **Dividir entre base igual:** $\frac{10^6}{10^3} = 10^{6-3} = 10^3$.
3. **Resolver número:** $10 \times 10 \times 10 = 1,000$.
✅ **Resultado:** $1,000$ USD
```

## 5. Ejercicios para el estudiante

```ad-abstract
title: 🟢 Fácil — Simplificación de una sola base
1. $(x^3)^4$
2. $m^2 \cdot m^5 \cdot m$
3. $\frac{a^{10}}{a^7}$
4. $(b^0)^5$
```

```ad-abstract
title: 🟡 Medio — Combinación de dos propiedades
1. $(x^2 \cdot y^3)^2$
2. $\frac{m^5 \cdot n^2}{m^2 \cdot n^4}$
3. $(a^{-2} \cdot b^3)^{-1}$
4. $\frac{(x \cdot y)^3}{x^2}$
```

```ad-abstract
title: 🔴 Avanzado — Aplicaciones Técnicas y Big Data
1. **Finanzas:** Una criptomoneda vale $2^5$ USD. Si su valor cambia por un factor de $(2^2)^{-1}$, calcula el valor final simplificado.
2. **Presupuesto:** Simplifica la expresión de costos: $\frac{(10^2 \cdot 5^3)^{-2}}{10^{-5}}$ USD.
3. **Infraestructura:** Un servidor cuesta $(x^2 \cdot y^3)^3$ USD y el gasto se reparte entre $x^5$ departamentos. ¿Cuánto paga cada uno?
4. **Big Data:** Un sistema procesa $(2^3)^2$ Petabytes cada $2^4$ meses. Calcula el procesamiento total simplificado.
```

```ad-success
title: ✅ Respuestas (para el docente)
**Fácil:** 1. $x^{12}$ | 2. $m^8$ | 3. $a^3$ | 4. $1$
**Medio:** 1. $x^4 y^6$ | 2. $\frac{m^3}{n^2}$ | 3. $\frac{a^2}{b^3}$ | 4. $x y^3$
**Avanzado:** 
1. $2^3 = 8$ USD.
2. $\frac{10}{5^6}$ USD (Nota: $10^{-4 - (-5)} = 10^1$).
3. $x y^9$ USD.
4. $2^{10} = 1,024$ Petabytes.
```

## 6. Mini-prueba de autoevaluación

```ad-question
title: 🧪 Pregunta 1
¿Qué sucede con los exponentes cuando aplicamos la propiedad de "potencia de una potencia" (con paréntesis)?
a) Se suman | b) Se restan | c) Se multiplican | d) Se vuelven cero
**Respuesta:** c) Se multiplican. El paréntesis indica que el exponente externo afecta a todo el bloque interno.
```

```ad-question
title: 🧪 Pregunta 2
¿Cuál es la forma correcta de expresar $x^{-3}$ para que el ejercicio esté terminado?
a) $-x^3$ | b) $\frac{1}{x^3}$ | c) $x^3$ | d) $0$
**Respuesta:** b) $\frac{1}{x^3}$. Un exponente negativo nos indica que la base debe invertirse al denominador para ser positiva.
```

```ad-question
title: 🧪 Pregunta 3
Si un servidor cuesta $(5^2)^2$ USD y recibe un subsidio que divide el costo por $5^3$, ¿cuál es el precio final?
a) $5$ USD | b) $25$ USD | c) $125$ USD | d) $1$ USD
**Respuesta:** a) $5$ USD. $(5^2)^2 = 5^4$. Al dividir por $5^3$, restamos exponentes: $4 - 3 = 1$. El resultado es $5^1 = 5$.
```

## 7. Notas para el próximo tema

> [!tip] 💡 En la próxima clase
> Ya dominas los exponentes enteros. Ahora daremos el salto a los **Exponentes Fraccionarios**. Aprenderás que una fracción en el exponente (como $x^{1/2}$) no es más que una **raíz** disfrazada. ¡Prepárate para fusionar la potenciación con la radicación!

> [!info] 🧭 Navegación
> [[Clase 03|⬅ Clase 03]] | [[00 - Índice del curso|Índice]] | **Clase 04** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]