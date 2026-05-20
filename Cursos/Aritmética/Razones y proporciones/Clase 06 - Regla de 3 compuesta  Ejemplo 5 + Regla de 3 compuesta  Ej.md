# Clase 06 — Regla de 3 compuesta | Ejemplo 5 + Regla de 3 compuesta | Ejemplo 6 + Regla de 3 compuesta | Ejemplo 7
#algebra #regladecompuest #curso_profe_alex

> [!info] 🧭 Navegación
> [[Clase 05]] | [[Índice]] | [[Clase 07]]

# Sección I: Introducción y Relevancia

> [!info] 🌍 Relevancia y aplicaciones
> La **Regla de 3 Compuesta** es la evolución lógica de la proporcionalidad simple. En el diseño de proyectos complejos, rara vez interactúan solo dos variables. Esta herramienta permite al gestor o ingeniero modelar la realidad mediante el análisis simultáneo de múltiples magnitudes, facilitando la toma de decisiones basada en la optimización de recursos limitados.

**Aplicaciones Prácticas:**
*   💵 **Proyectos de Construcción:** Estimación de presupuestos y mano de obra cuando cambian los plazos y la magnitud de la obra.
*   🏗️ **Gestión de Fábricas:** Reajuste de tiempos de entrega y operatividad de maquinaria tras averías o cambios en la jornada laboral.
*   📊 **Optimización Ganadera:** Cálculo preciso de raciones y días de suministro ante variaciones en la población animal y ajustes en el consumo.

# Sección II: Fundamentos Teóricos

> [!note] 📌 ¿Qué es la Regla de 3 compuesta?
> Es un procedimiento matemático utilizado para resolver problemas de proporcionalidad donde intervienen **tres o más magnitudes**. Su esencia radica en establecer una cadena de comparaciones entre una magnitud que contiene una incógnita ($X$) y el resto de las variables conocidas.

> [!warning] ⚠️ Error común
> El fallo más habitual es aplicar la "operación en cruz" de forma mecánica sin realizar el **análisis cualitativo previo**. No todas las relaciones son iguales; operar sin determinar si una magnitud es Directa o Inversa respecto a la incógnita conducirá inevitablemente a un resultado erróneo.

> [!tip] 💡 Truco para recordarlo
> Siguiendo la metodología del **Profe Alex**, recuerda: "La variable es lo que cambia". Para analizar la relación, tapa mentalmente las variables que no estés usando y compara la columna de la incógnita con la variable activa. Pregúntate: *¿Si esta magnitud aumenta, la incógnita debería aumentar o disminuir?*

# Sección III: Metodología Resolutiva

```text
PASO 1 → Identificar las magnitudes y organizar los datos en columnas. 
         (Se recomienda ubicar la columna de la incógnita en un extremo).
PASO 2 → Análisis de Proporcionalidad: Comparar CADA magnitud con la de la incógnita. 
         Anotar si es Directa (D) o Inversa (I).
PASO 3 → Planteamiento de la Ecuación: La fracción de la incógnita (X/A) se iguala al 
         producto de las demás fracciones. 
         IMPORTANTE: Si la magnitud es Inversa, se debe INVERTIR su fracción.
PASO 4 → Simplificación y Resolución: Reducir las fracciones mediante la eliminación 
         de factores comunes para despejar X con facilidad.
```

# Sección IV: Desarrollo de Ejemplos (Casos de Estudio)

```ad-example
title: Ejemplo 5: Construcción de Casas
**Problema:** 15 obreros trabajando 7h/día construyen 1 casa en 40 días. ¿Cuántos obreros se necesitan para construir 8 casas en 60 días trabajando 8h/día?

**1. Organización y Análisis:**
*   **Obreros (X):** 15 | $x$
*   **Horas/día (Inversa):** 7 | 8 (A más horas, menos obreros necesarios).
*   **Casas (Directa):** 1 | 8 (A más casas, más obreros necesarios).
*   **Días (Inversa):** 40 | 60 (A más días, menos obreros necesarios).

**2. Ecuación:**
Isolamos la incógnita y aplicamos las inversiones necesarias:
$$\frac{x}{15} = \frac{7}{8} \cdot \frac{8}{1} \cdot \frac{40}{60}$$

**3. Resolución:**
Simplificamos el 8 con el 8 y los ceros de 40/60:
$$x = 15 \cdot \left( \frac{7}{1} \cdot \frac{1}{1} \cdot \frac{4}{6} \right) \rightarrow x = 15 \cdot \frac{28}{6} = 70$$
**Resultado:** Se necesitan **70 obreros**.
```

```ad-example
title: Ejemplo 6: Ganadería y Raciones
**Problema:** Un granjero tiene 1800 ovejas y alimento para 20 días. Si vende algunas y a las restantes les da el 80% de la ración, el alimento dura 30 días. ¿Cuántas vendió?

**1. Análisis:** Consideramos la ración inicial como el 100%. Los días pasan de 20 a 30 (10 días más).
*   **Ovejas (X):** 1800 | $x$
*   **Días (Inversa):** 20 | 30
*   **Ración (Inversa):** 100% | 80% (A menos ración por oveja, más ovejas pueden comer).

**2. Ecuación:**
$$\frac{x}{1800} = \frac{20}{30} \cdot \frac{100}{80}$$

**3. Resolución:**
$$x = 1800 \cdot \left( \frac{2}{3} \cdot \frac{10}{8} \right) = 1800 \cdot \frac{20}{24} = 1500 \text{ ovejas.}$$
**Conclusión:** Si quedan 1500 y había 1800, el granjero **vendió 300 ovejas**.
```

```ad-example
title: Ejemplo 7: Fábrica y Averías (Fase Mixta)
**Problema:** Una fábrica con 10 máquinas empaca 400,000 unidades en 5 días (8h/d). Al iniciar el 5to día se dañan 3 máquinas. El resto trabajará 10h/d. ¿En cuánto tiempo entregan el pedido total de 1,000,000 de unidades?

**Fase 1 (Días 1 a 4):**
Las máquinas trabajaron normal 4 de los 5 días previstos.
$$\text{Unidades empacadas} = 400,000 \cdot \frac{4}{5} = 320,000 \text{ unidades.}$$

**Fase 2 (Resto del pedido):**
*   **Unidades faltantes:** $1,000,000 - 320,000 = 680,000$.
*   **Máquinas restantes:** $10 - 3 = 7$.
*   **Nueva jornada:** 10 horas/día.
*   **Incógnita (Días):** $x$

**Planteamiento de la Fase 2 (Comparando con el estándar inicial):**
$$\frac{x}{5} = \underbrace{\frac{8}{10}}_{\text{Horas (I)}} \cdot \underbrace{\frac{10}{7}}_{\text{Máq (I)}} \cdot \underbrace{\frac{680,000}{400,000}}_{\text{Unid (D)}}$$

**Resolución:**
Simplificando 10 con 10 y ceros:
$$x = 5 \cdot \frac{8}{7} \cdot \frac{68}{40} = 5 \cdot \frac{8}{7} \cdot 1.7 \approx 9.71 \text{ días.}$$

**Resultado Total:** 4 días (iniciales) + 9.71 días $\approx$ **13.71 días (Aproximadamente 14 días).**
```

```ad-example
title: Aplicación de Costos: Presupuesto de Obra
**Problema:** Según los datos del Ejemplo 5, el presupuesto para construir la 1ª casa fue de $1,500 USD (considerando 15 obreros y 40 días). ¿Cuál será el costo de construcción si ahora debemos entregar 8 casas?

**Análisis de Proporcionalidad:** El costo es **Directamente Proporcional** al número de casas construidas.
*   **Casas:** 1 | 8
*   **Costo (X):** $1,500 | $x$

**Planteamiento:**
$$\frac{x}{1500} = \frac{8}{1}$$
$$x = 1500 \cdot 8 = 12,000$$

**Resultado:** El presupuesto necesario asciende a **$12,000 USD**. (Nota: En este modelo, el costo se escala por unidad de obra terminada, asumiendo que los cambios en obreros/días se ajustan para cumplir dicho volumen).
```

# Sección V: Práctica Dirigida

```ad-abstract
title: 🟢 Nivel Fácil (Verde)
Si 15 obreros construyen 1 casa en 40 días trabajando 7h/día, ¿cuántos días tardarán 5 obreros trabajando 6h/día para construir 3 casas?
```

```ad-abstract
title: 🟡 Nivel Medio (Amarillo)
Un granjero tiene 1800 ovejas y alimento para 20 días (ración simple). Si vende 800 ovejas y decide darles el doble de ración a las restantes, ¿para cuántos días alcanzará el alimento?
```

```ad-abstract
title: 🔴 Nivel Avanzado (Rojo - Fase Mixta)
30 obreros empiezan un trabajo de 100 días. Al terminar el día 20, se retiran 5 obreros y los restantes deciden trabajar 10h/día (antes trabajaban 7h/día). Si el ritmo original era de 1 casa cada 40 días con 15 obreros, ¿cuántas casas totales entregarán al final de los 100 días?
```

```ad-success
title: Solucionario
1. **Ejercicio Verde:** 420 días.
2. **Ejercicio Amarillo:** 18 días (Inversa en ovejas, Inversa en ración).
3. **Ejercicio Rojo:** 5.76 casas (1 casa en la Fase 1 + 4.76 casas en la Fase 2).
```

# Sección VI: Evaluación y Cierre

```ad-question
title: Pregunta 1
¿Por qué la relación entre "Obreros" y "Días" es inversa?
**Respuesta:** Porque a mayor cantidad de trabajadores (aumenta magnitud A), el tiempo necesario para terminar la obra disminuye (disminuye magnitud B).
```

```ad-question
title: Pregunta 2
En el Ejemplo 6, ¿qué significa que la ración sea del 80%?
**Respuesta:** Significa que cada animal recibe menos alimento que antes. Al ser una relación inversa, esto permite que el alimento dure más días o alcance para más animales.
```

```ad-question
title: Pregunta 3
¿Cuál es el beneficio de simplificar antes de multiplicar en la Regla de 3 Compuesta?
**Respuesta:** Evita trabajar con números excesivamente grandes, reduce el margen de error manual y permite resolver el problema de forma mucho más ágil.
```

> [!tip] 💡 En la próxima clase
> Aplicaremos estos principios de proporcionalidad para entender los **Repartos Proporcionales**, donde aprenderemos a distribuir cantidades (como herencias o beneficios) de forma justa y equitativa.

> [!info] 🧭 Navegación
> [[Clase 05]] | [[Índice]] | [[Clase 07]]