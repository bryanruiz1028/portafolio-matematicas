# 📖 Guía de estudio — Clase 03: Regla de la multiplicación en Probabilidad

> [!info] 📌 Conceptos clave
> ¡Qué tal, amigas y amigos! Para dominar la regla de la multiplicación, debemos tener claros estos cuatro pilares que el Profe Alex nos explica:
> *   **¿Cuándo se usa?:** Aplicamos esta regla cuando queremos hallar la probabilidad de que dos o más eventos ocurran **a la vez** o de forma **consecutiva**. Es como seguir un camino: primero pasa esto Y LUEGO pasa lo otro.
> *   **La clave es la "y":** Siempre que escuches que debe cumplirse una condición *y* otra (ej. que sea perro **y** sea blanco), estamos ante una multiplicación de probabilidades (intersección $\cap$).
> *   **Independencia vs. Dependencia:** Si lo que pasa primero no afecta al segundo evento, son **independientes**. Pero si el primer resultado cambia las opciones del segundo, ¡ojo!, son **dependientes**.
> *   **El efecto del reemplazo:** Si sacamos un objeto y lo devolvemos (**con reemplazo**), el total no cambia. Si lo dejamos afuera (**sin reemplazo**), el denominador disminuye porque hay menos elementos.

## Fórmulas y definiciones importantes

| Término | Fórmula (LaTeX) | ¿Cómo se lee? |
| :--- | :--- | :--- |
| **Intersección ($\cap$)** | $P(A \cap B)$ | Probabilidad de que ocurra el evento A **y** el evento B. |
| **Eventos Independientes** | $P(A \cap B) = P(A) \cdot P(B)$ | Probabilidad de A por la probabilidad de B (no se afectan). |
| **Eventos Dependientes** | $P(A \cap B) = P(A) \cdot P(B|A)$ | Probabilidad de A por la probabilidad de B **dado que ya ocurrió A**. |

> [!important] 
> **Nota pedagógica:** Esa barrita vertical en $P(B|A)$ no es una división, es una condición. Se lee: "Probabilidad de B, sabiendo que ya pasó A".

## Ejemplos resueltos paso a paso

```ad-example
title: Ejemplo A — ¿Qué tenemos en nuestra urna? (Sin reemplazo)
**Escenario:** Tenemos una urna con 5 esferas azules, 2 rojas y 1 verde (Total = 8 esferas).
**¿Qué vamos a calcular hoy?:** La probabilidad de que al sacar dos esferas (sin reemplazo), la primera sea **azul** y la segunda sea **verde**.

**Paso a paso:**
1. **Primera extracción (Azul):** Al inicio hay 8 esferas y 5 son azules.
   $P(\text{Azul}_1) = \frac{5}{8}$
2. **Segunda extracción (Verde):** ¡Pilas aquí! Como ya sacamos una azul y **no la devolvimos**, ahora solo quedan 7 esferas en la urna. La verde sigue ahí solita.
   $P(\text{Verde}_2 | \text{Azul}_1) = \frac{1}{7}$
3. **La Multiplicación:**
   $P(\text{Azul} \cap \text{Verde}) = \frac{5}{8} \cdot \frac{1}{7} = \frac{5}{56}$
4. **Conversión:**
   $\frac{5}{56} \approx 0.089 \rightarrow \mathbf{8.9\%}$
```

```ad-example
title: Ejemplo B — Calidad y Costos en la Fábrica de Balones
**Escenario:** Una fábrica produce balones de fútbol (60% o 0.6) y baloncesto (40% o 0.4). La probabilidad de que un balón de fútbol sea defectuoso es de 0.05.
**El reto:** Calcular la probabilidad de que un balón tomado al azar sea de **fútbol Y defectuoso**, y ver cuánto dinero se arriesga si la pérdida por cada uno es de $10 USD.

**Análisis de probabilidad:**
*   $P(\text{Fútbol}) = 0.6$
*   $P(\text{Defectuoso} | \text{Fútbol}) = 0.05$
*   $P(\text{Fútbol} \cap \text{Defectuoso}) = 0.6 \cdot 0.05 = \mathbf{0.03}$

**Interpretación para la vida real:**
Ese **0.03** significa que el **3%** de toda la producción de la fábrica son balones de fútbol con fallas. En un lote de 100 balones, esperaríamos encontrar 3 así. Si cada uno nos cuesta $10 USD, ¡estaríamos perdiendo $30 USD en ese lote!
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel: Fácil (Con reemplazo)
**Contexto:** En un salón hay 10 niños y 8 niñas (Total = 18). Elegimos estudiantes al azar, pero **con reemplazo** (el elegido vuelve al grupo).

1. ¿Cuál es la probabilidad de elegir un niño y luego una niña?
2. Si elegimos dos estudiantes, ¿cuál es la probabilidad de que ambos sean niños?
3. Si elegimos tres estudiantes, ¿cuál es la probabilidad de que las tres sean niñas?
*Ayuda: Recuerda que aquí el denominador (18) nunca cambia.*
```

```ad-abstract
title: 🟡 Nivel: Medio (Sin reemplazo)
**Contexto:** Una caja tiene 20 esferos: 15 funcionan y 5 no sirven. Sacamos dos esferos **sin reemplazo**.

1. Calcula la probabilidad de que el primero sirva y el segundo no sirva ($S_1 \cap N_2$).
2. Calcula la probabilidad de que el primero no sirva y el segundo sí sirva ($N_1 \cap S_2$).
3. Si sacas dos esferos, ¿cuál es la probabilidad de que ambos estén dañados? ($N_1 \cap N_2$).
*¡Cuidado! Al sacar el primer esfero, el total para el segundo cálculo baja a 19.*
```

```ad-abstract
title: 🔴 Nivel: Avanzado — Aplicación $USD
1. **Producción en serie:** Usando los datos de la fábrica, sabemos que el 40% son de baloncesto y el 97% de estos salen "buenos" (sirven). Si tomamos 3 balones al azar de la producción total, ¿cuál es la probabilidad de que los tres sean de baloncesto y además funcionen correctamente?
2. **Riesgo de Auditoría:** Una multa cuesta $50 USD por cada balón de baloncesto defectuoso. Si la probabilidad de que sea de baloncesto es 0.4 y la de ser defectuoso (siendo de baloncesto) es 0.03, calcula la probabilidad de que al elegir un balón al azar la empresa deba pagar esa multa. (Dato extra: El riesgo económico es de $0.60 USD por cada balón producido).
```

> [!tip] 💡 Consejo de estudio del Profe Alex
> ¡No te confíes de la memoria! Cuando tengas un problema de "sin reemplazo", usa la técnica del **dibujo**. Dibuja los elementos y, cuando saques uno, **táchalo físicamente** con una "X". Verás que es imposible olvidar que ahora hay un elemento menos en el total y, a veces, uno menos en tu grupo favorito. ¡Visualizar el cambio en el denominador es la clave del éxito!