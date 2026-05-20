# 📖 Guía de estudio — Clase 01: Introducción a los Números Irracionales

> [!info] 📌 Conceptos clave
> 1.  **Definición de Irracionales ($\mathbb{I}$):** Según la taxonomía decimal, existen decimales exactos y periódicos (que son racionales). Los irracionales son **decimales infinitos no periódicos**. Al no tener un patrón de repetición (periodo), es matemáticamente imposible expresarlos como una fracción $a/b$.
> 2.  **Diferenciación de Conjuntos:** Los números que conocemos siguen una jerarquía: los Naturales ($\mathbb{N}$) están dentro de los Enteros ($\mathbb{Z}$), y estos dentro de los Racionales ($\mathbb{Q}$). Sin embargo, los Irracionales ($\mathbb{I}$) son un conjunto **disjunto** (aparte); un número no puede pertenecer a ambos mundos.
> 3.  **Raíces no exactas:** En este nivel, identificamos un número irracional como toda raíz de un número entero cuyo resultado no sea un número entero (natural). Por ejemplo, $\sqrt{2}$ o $\sqrt[3]{5}$. Si la raíz es exacta (como $\sqrt{9} = 3$), es racional.
> 4.  **Historia (El "Chismecito" turbio):** **Hipaso de Metaponto**, de la escuela pitagórica (año 500 a.C.), descubrió la irracionalidad al intentar medir la hipotenusa de un triángulo con catetos de valor 1. Al obtener $\sqrt{2}$, rompió la creencia de que "todo en el universo era racional". Por esta traición al secreto pitagórico, fue expulsado y se le construyó una tumba simbólica. La historia cuenta finales oscuros: desde un naufragio "divino" hasta que el mismo Pitágoras lo lanzó por la borda de un barco para silenciarlo.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Números Racionales ($\mathbb{Q}$)** | Números que pueden escribirse como fracción $a/b$. Incluyen decimales exactos (0.5) y periódicos (0.333...). |
| **Números Irracionales ($\mathbb{I}$)** | Decimales infinitos **no periódicos** (sin patrón). Ejemplos: $\pi, e, \sqrt{2}, \sqrt{3}$. |
| **Simplificación (Método de Parejitas)** | Se agrupan los factores primos en grupos iguales según el índice ($n$). Los grupos "salen" de la raíz; los que sobran se quedan dentro. |
| **Ley de Exponentes** | $\sqrt[n]{a^m} = a^{m/n}$. Útil para simplificar dividiendo el exponente entre el índice. |
| **Teorema de Pitágoras** | $a^2 + b^2 = c^2$. Es el puente entre la geometría y los irracionales, usado para ubicar raíces en la recta numérica. |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Simplificación de $\sqrt{12}$
1. **Descomposición en primos:** $12 = 2 \times 2 \times 3$, que se escribe como $2^2 \times 3$.
2. **Identificación por Índice:** Como el índice es 2 (raíz cuadrada), buscamos "parejitas". El $2^2$ forma una pareja completa.
3. **Extracción y Simplificación:** 
   $\sqrt{2^2 \times 3} = \sqrt{2^2} \times \sqrt{3}$
   Aplicando la división de exponentes ($2/2 = 1$), el factor sale de la raíz: $2^1 \times \sqrt{3}$.
✅ **Resultado:** $2\sqrt{3}$.
```

```ad-example
title: Ejemplo B — Aplicación real: Cercado diagonal ($USD)
**Problema:** Un terreno cuadrado mide 1 metro por lado. Se desea comprar una cerca para la diagonal. ¿Costo total si el metro cuesta $15.00 USD?
1. **Paso 1 (Pitágoras):** $1^2 + 1^2 = d^2 \rightarrow 1 + 1 = d^2 \rightarrow d = \sqrt{2}$ metros.
2. **Paso 2 (Aproximación):** Tomamos $\sqrt{2} \approx 1.41$ m.
3. **Paso 3 (Costo):** $1.41 \times 15.00 = 21.15$.
✅ **Resultado:** El costo total es de $21.15 USD.
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
1. Clasifica los siguientes números como Racionales ($\mathbb{Q}$) o Irracionales ($\mathbb{I}$):
   - $0.5$ (Exacto): _________
   - $\pi$ (Infinito no periódico): _________
   - $\sqrt{9}$ (Exacta): _________
   - $\sqrt{7}$ (No exacta): _________
   - $-2$ (Entero): _________
2. Identifica el índice y el exponente en la expresión $\sqrt[5]{2^{10}}$.
3. Calcula la raíz cuadrada exacta de $121$.
```

```ad-abstract
title: 🟡 Medio
1. Simplifica el radical $\sqrt{50}$ usando factores primos. (Pista: busca la pareja de 5).
2. Explica por qué $\sqrt{4}$ NO es un número irracional basándote en su resultado.
3. Para representar $\sqrt{10}$ en la recta numérica, buscamos dos números cuyos cuadrados sumen 10. ¿Qué catetos (que sean raíces exactas) usarías? 
   *(Pista: $x^2 + y^2 = 10$)*.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
Un soporte metálico diagonal mide exactamente $\sqrt{18}$ metros. La viga de acero cuesta $25.50 USD por metro lineal.
**a)** Simplifica $\sqrt{18}$ a su forma mínima radical ($3\sqrt{x}$).
**b)** Si $\sqrt{2} \approx 1.41$, calcula el costo total siguiendo estos pasos:
   1. Multiplica el coeficiente extraído por la aproximación ($3 \times 1.41$).
   2. Multiplica ese resultado por el precio ($25.50$).
   *Resultado final sugerido: $107.87 USD (redondeado).*
```

> [!tip] 💡 Consejo de estudio
> Para ganar velocidad en exámenes, memoriza las **10 primeras raíces cuadradas exactas** (del 1 al 100) y las **5 primeras raíces cúbicas** ($\sqrt[3]{1}=1, \sqrt[3]{8}=2, \sqrt[3]{27}=3, \sqrt[3]{64}=4, \sqrt[3]{125}=5$). Si una raíz de un entero no está en esta lista de "resultados bonitos", ¡estás frente a un número irracional!