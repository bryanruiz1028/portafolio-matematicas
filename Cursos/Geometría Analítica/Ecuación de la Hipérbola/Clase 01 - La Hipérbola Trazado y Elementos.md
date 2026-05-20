# Clase 01 — La Hipérbola: Trazado y Elementos
tags: #algebra #hyperbolatracin
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 7

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [[Introducción a las Secciones Cónicas]]
> ⬆️ **Inicio:** [[00 - Índice del curso]]
> ➡️ **Siguiente:** [[Clase 02 — Ecuaciones de las Asíntotas]]

---

> [!info] 🌍 Relevancia y aplicaciones
> La hipérbola es una cónica única por su doble curvatura (dos ramas opuestas que se alejan). A diferencia de la elipse, sus ramas nunca se cierran, sino que se extienden infinitamente buscando líneas guía llamadas asíntotas.
> 
> **Campos de aplicación:**
> - **Finanzas ($USD):** Se usa para modelar curvas de costo-volumen-beneficio. Las asíntotas de la hipérbola representan los **costos límite** de producción: por mucho que produzcas, el costo por unidad tiende a estabilizarse en esa línea invisible.
> - **Arquitectura:** Las estructuras hiperboloides (como las torres de enfriamiento) son extremadamente resistentes y usan poco material porque aprovechan la geometría de la hipérbola.
> - **Vida cotidiana:** La sombra que proyecta una lámpara de mesa sobre una pared o la trayectoria de cometas "visitantes" (no periódicos) que pasan cerca del Sol una sola vez antes de perderse en el espacio.

---

> [!note] 📌 ¿Qué es la Hipérbola: Trazado y Elementos?
> Imagina que tienes dos puntos fijos llamados **focos**. La hipérbola es el camino de todos los puntos donde, si restas la distancia de un punto a un foco menos la distancia al otro, el resultado **siempre es el mismo número**.
> 
> Es un "juego de resta constante": no importa en qué parte de la curva estés, esa diferencia de distancias no cambia. Los elementos clave son:
> - **Eje Real (o Principal):** La línea que une los vértices y los focos.
> - **Eje Imaginario (o Secundario):** La línea perpendicular que ayuda a formar el rectángulo guía.
> - **Centro $(h, k)$:** El punto medio entre los vértices.

> [!warning] ⚠️ Error común
> En la elipse, el valor más grande siempre era $a$. **¡Cuidado!** En la hipérbola, el valor más grande es siempre **$c$** (la distancia del centro al foco), ya que se cumple que $c^2 = a^2 + b^2$. Además, la hipérbola exige que los signos de $x^2$ y $y^2$ sean **diferentes** (uno positivo y otro negativo).

> [!tip] 💡 Truco para recordarlo: La regla de la "Fracción Positiva"
> Para saber hacia dónde abre la hipérbola, olvida cuál número es más grande. Solo mira qué letra tiene el signo positivo:
> - Si **$x^2$** es positiva: La hipérbola tiene **Eje Real horizontal** (abre a los lados).
> - Si **$y^2$** es positiva: La hipérbola tiene **Eje Real vertical** (abre arriba y abajo).

---

### Procedimiento paso a paso para Graficar

```text
PASO 1: Identificar el centro (h, k) y la orientación. 
        Si arriba dice x² y y² solas, el centro es (0,0). Si tienen números restando/sumando, 
        cambia sus signos para hallar (h, k). La fracción positiva define el Eje Real.

PASO 2: Calcular 'a' y 'b'.
        - 'a' es la raíz del denominador de la fracción positiva (distancia sobre el Eje Real).
        - 'b' es la raíz del denominador de la fracción negativa (distancia sobre el Eje Imaginario).
        Dibuja el "Rectángulo Guía": mide 'a' unidades desde el centro hacia los vértices 
        y 'b' hacia los lados contrarios. Las esquinas del rectángulo estarán en (±a, ±b) 
        respecto al centro.

PASO 3: Determinar 'c' y el Lado Recto (LR).
        - Calcula c = √(a² + b²) para ubicar los focos. 
        - Calcula LR = 2b²/a. El LR nos dice qué tan abierta o cerrada es "la boca" 
          de la hipérbola al pasar por el foco.

PASO 4: Trazar las asíntotas y las ramas.
        Dibuja las asíntotas como las diagonales que cruzan por las esquinas del rectángulo guía. 
        Finalmente, dibuja las ramas de la hipérbola partiendo de los vértices y acercándose 
        a las asíntotas sin tocarlas nunca.
```

---

### Ejemplos Prácticos

```ad-example
title: Ejemplo 1: Caso Básico (Centro 0,0)
Dada la ecuación: $\frac{x^2}{16} - \frac{y^2}{9} = 1$
1. **Centro:** $(0,0)$.
2. **Orientación:** Horizontal ($x$ es positiva). **Eje Real** sobre el eje $x$.
3. **Cálculos:**
   - $a^2 = 16 \implies a = 4$ (Vértices a 4 unidades del centro).
   - $b^2 = 9 \implies b = 3$ (Eje Imaginario mide 3 unidades desde el centro).
   - $c = \sqrt{16 + 9} = \sqrt{25} = 5$ (Focos a 5 unidades del centro).
```

```ad-example
title: Ejemplo 2: Signos y Orientación Vertical
Dada la ecuación: $\frac{y^2}{9} - \frac{x^2}{4} = 1$
- **Análisis:** La fracción positiva tiene la $y$, por lo que el **Eje Real** es vertical.
- **Cálculo:** $a = 3$, $b = 2$.
- **Nota técnica:** Las ramas abren hacia arriba y abajo. No te dejes engañar por el tamaño de los números; manda el signo positivo.
```

```ad-example
title: Ejemplo 3: Centro desplazado (h, k)
Dada la ecuación: $\frac{(x-1)^2}{25} - \frac{(y+2)^2}{4} = 1$
1. **Centro:** Extraemos $h$ y $k$ cambiando los signos: **$(1, -2)$**.
2. **Orientación:** Horizontal ($x$ positiva).
3. **Valores:** $a = \sqrt{25} = 5$, $b = \sqrt{4} = 2$.
```

```ad-example
title: Ejemplo 4: Aplicación Financiera ($USD)
Una fábrica de hardware modela su costo marginal mediante la hipérbola $\frac{x^2}{100} - \frac{y^2}{64} = 1$, donde $y$ es el presupuesto en **$USD**. 
- **Punto Crítico:** El vértice ($a$) representa el punto de inversión mínima para iniciar producción.
- **Cálculo:** $a = \sqrt{100} = 10$. El punto crítico está a 10 unidades.
- **Foco:** $c = \sqrt{100 + 64} \approx 12.81$. El foco (punto de máxima eficiencia operativa) se ubica a **12.81 $USD**. 
- **Insight Experto:** Las asíntotas aquí representan que, sin importar cuánto aumente el volumen $x$, el costo $y$ nunca superará la proporción definida por la pendiente $b/a$, estableciendo un límite financiero.
```

---

### Ejercicios para el estudiante

```ad-abstract
title: 🟢 Nivel Verde: Identificación Básica
Identifica el centro, $a$ y $b$ de las siguientes ecuaciones:
1. $\frac{x^2}{9} - \frac{y^2}{16} = 1$
2. $\frac{y^2}{25} - \frac{x^2}{4} = 1$
3. $x^2 - \frac{y^2}{4} = 1$ (Pista: el denominador de $x^2$ es 1)
4. $\frac{y^2}{49} - x^2 = 1$
```

```ad-abstract
title: 🟡 Nivel Amarillo: Construcción de la Ecuación
Encuentra la ecuación ordinaria dados los siguientes datos:
1. Centro $(2, 3)$, Vértice $(5, 3)$, $b = 2$.
2. Centro $(0, 0)$, Eje Real vertical, $a = 6, b = 3$.
3. Centro $(-1, -4)$, Vértice $(-1, 0), b = 5$.
4. Centro $(4, -2)$, Eje Real horizontal, $a = 8, b = 6$.
```

```ad-abstract
title: 🔴 Nivel Rojo: Desafío de Aplicación ($USD)
Resuelve los problemas de trayectorias y costos:
1. Calcula la distancia focal ($2c$) de una trayectoria de inversión cuya ecuación es $\frac{x^2}{36} - \frac{y^2}{64} = 1$.
2. Calcula el Lado Recto ($LR$) para una curva de costos donde $a=3$ y $b=4$.
3. Una estructura arquitectónica tiene una base hiperbólica con $a=10$ y $c=15$. Halla el valor de $b$ (Eje Imaginario).
4. Si un sensor detecta una señal en el foco de $\frac{x^2}{16} - \frac{y^2}{9} = 1$, y cada unidad de distancia cuesta **$10 USD**, ¿cuánto cuesta el mantenimiento desde el centro al foco?
```

```ad-success
title: Respuestas
- **Verde:** 1) C(0,0), a=3, b=4 | 2) C(0,0), a=5, b=2 | 3) C(0,0), a=1, b=2 | 4) C(0,0), a=7, b=1.
- **Amarillo:** 1) $\frac{(x-2)^2}{9} - \frac{(y-3)^2}{4} = 1$ | 2) $\frac{y^2}{36} - \frac{x^2}{9} = 1$ | 3) $\frac{(y+4)^2}{16} - \frac{(x+1)^2}{25} = 1$ | 4) $\frac{(x-4)^2}{64} - \frac{(y+2)^2}{36} = 1$.
- **Rojo:** 1) $2c = 20$ | 2) $LR = 10.66$ | 3) $b = \sqrt{125} \approx 11.18$ | 4) **$50 USD** (Ya que $c=5$).
```

---

### Mini-prueba de autoevaluación

```ad-question
title: Pregunta 1: Conceptual
En una hipérbola donde $a=3$ y $b=4$, ¿cuál es el valor de $c$? ¿Es mayor que $a$ y $b$?
*(Respuesta: $c=5$. Sí, en la hipérbola $c$ siempre es la distancia más larga).*
```

```ad-question
title: Pregunta 2: Procedimental
¿Cuál es el centro de la hipérbola $\frac{(x+7)^2}{4} - \frac{(y-5)^2}{16} = 1$?
*(Respuesta: Centro en (-7, 5). Recuerda cambiar los signos de la ecuación).*
```

```ad-question
title: Pregunta 3: Aplicación ($USD)
Si el costo marginal se define por el Lado Recto de la hipérbola $\frac{x^2}{4} - \frac{y^2}{16} = 1$, ¿cuál es el costo resultante en **$USD**?
*(Respuesta: $LR = 2(16)/2 = 16 USD$)*
```

---

> [!tip] 💡 En la próxima clase
> Ahora que dominas el rectángulo guía y los ejes (Real e Imaginario), aprenderás a calcular las **Ecuaciones de las Asíntotas**, las líneas que marcan el límite infinito de tu hipérbola.

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [[Introducción a las Secciones Cónicas]]
> ⬆️ **Inicio:** [[00 - Índice del curso]]
> ➡️ **Siguiente:** [[Clase 02 — Ecuaciones de las Asíntotas]]