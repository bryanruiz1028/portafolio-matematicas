# 📖 Guía de estudio — Clase 04: Caída Libre

> [!info] 📌 Conceptos clave
> Basándose en la metodología del "Profe Alex", los fundamentos de la caída libre se rigen por los siguientes principios:
> 1. **Definición de "dejarse caer":** Cuando un cuerpo se suelta desde el reposo, su velocidad inicial es siempre cero ($v_i = 0 \text{ m/s}$).
>    - *Nota de precaución:* Esta regla de $v_i = 0 \text{ m/s}$ aplica solo si el punto de partida está estático. Si el objeto se suelta desde un transporte en movimiento (como un globo o un avión), el análisis de la velocidad inicial debe ajustarse al contexto del sistema.
> 2. **La naturaleza de la gravedad:** Se considera una aceleración constante que, para efectos de este curso, utilizaremos con el valor de $g = 9,8 \text{ m/s}^2$.
> 3. **Dirección y convención de signos:** En la caída libre, tanto el movimiento como la gravedad se dirigen hacia abajo. Al ir en el mismo sentido, el objeto acelera (su velocidad aumenta), por lo que los datos se consideran positivos durante el descenso.
> 4. **Consistencia de unidades:** Para asegurar la precisión técnica, es imperativo que todas las magnitudes se encuentren en metros ($\text{m}$) y segundos ($\text{s}$) antes de realizar cualquier cálculo.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Velocidad Inicial ($v_i$)** | Punto de partida del movimiento. Si el objeto parte del reposo, su valor es $0 \text{ m/s}$. |
| **Gravedad ($g$)** | Aceleración constante que atrae los cuerpos hacia la Tierra. Valor estándar: $9,8 \text{ m/s}^2$. |
| **Altura / Distancia ($y$ o $h$)** | Desplazamiento vertical. Fórmula: $y = v_i \cdot t + \frac{g \cdot t^2}{2}$. |
| **Velocidad Final ($v_f$)** | Rapidez alcanzada tras un tiempo $t$. Fórmula: $v_f = v_i + g \cdot t$. |
| **Tiempo ($t$)** | Intervalo de duración de la caída, medido obligatoriamente en segundos ($\text{s}$). |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Cálculo de altura desde un edificio
**Problema:** Se deja caer una piedra desde lo alto de un edificio y llega al suelo en $4 \text{ s}$. ¿Cuál es la altura del edificio?

1. **Datos conocidos:**
   - $v_i = 0 \text{ m/s}$ (se deja caer).
   - $t = 4 \text{ s}$.
   - $g = 9,8 \text{ m/s}^2$.

2. **Selección de fórmula:**
   Siguiendo la estrategia de exclusión, observamos que **no conocemos ni necesitamos hallar** la velocidad final ($v_f$). Por lo tanto, la fórmula ideal es: $y = v_i \cdot t + \frac{g \cdot t^2}{2}$.

3. **Procedimiento paso a paso:**
   - **Paso 1 (Reemplazo):** $y = (0 \cdot 4) + \frac{9,8 \cdot (4)^2}{2}$.
   - **Paso 2 (Potencia):** Dado que $0 \cdot 4 = 0$, calculamos $4^2 = 16$. Nos queda: $\frac{9,8 \cdot 16}{2}$.
   - **Paso 3 (Simplificación):** Simplificamos $\frac{16}{2} = 8$. Operamos $9,8 \cdot 8$.
   
✅ **Resultado:** $78,4 \text{ m}$.
```

```ad-example
title: Ejemplo B — Velocidad de impacto de un juguete
**Problema:** Un juguete cae desde una ventana y tarda $3 \text{ s}$ en impactar. ¿Con qué velocidad toca el suelo?

1. **Datos conocidos:**
   - $v_i = 0 \text{ m/s}$.
   - $t = 3 \text{ s}$.
   - $g = 9,8 \text{ m/s}^2$.

2. **Selección de fórmula:**
   Identificamos que **no tenemos ni se nos pide** la altura ($y$). Por exclusión, aplicamos la fórmula de velocidad final: $v_f = v_i + g \cdot t$.

3. **Procedimiento paso a paso:**
   - **Paso 1:** Reemplazamos los valores: $v_f = 0 + (9,8 \cdot 3)$.
   - **Paso 2:** Multiplicamos la gravedad por el tiempo: $v_f = 29,4$.

✅ **Resultado:** $29,4 \text{ m/s}$.
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
1. Si un objeto se "deja caer", ¿cuál es siempre su velocidad inicial ($v_i$)?
2. ¿Cuál es el valor de la gravedad ($g$) que utilizaremos de forma estándar?
3. Si un objeto cae durante $1 \text{ s}$, ¿cuál es su velocidad final? (Use $g = 9,8 \text{ m/s}^2$).
```

```ad-abstract
title: 🟡 Medio
1. Calcule la altura de un puente si una piedra tarda $2 \text{ s}$ en tocar el agua al ser soltada.
2. ¿Qué velocidad tendrá un objeto a los $5 \text{ s}$ de haber iniciado su caída libre?
3. Un objeto se deja caer y recorre una distancia $y$. Si el tiempo se duplica, ¿qué sucede con la altura? (Explique basándose en la fórmula).
```

```ad-abstract
title: 🔴 Avanzado — El problema de las gotas de agua
**Problema de lógica:** De una llave cae una gota de agua cada segundo. ¿Qué distancia separa a la primera de la segunda gota en el instante en que va a caer la TERCERA gota?

**Instrucción visual:** Se recomienda dibujar una línea de tiempo vertical. Recuerde que cuando la gota 3 está por caer ($t = 0 \text{ s}$), la gota 2 lleva $1 \text{ s}$ cayendo y la gota 1 lleva $2 \text{ s}$ cayendo.

**Ayuda para la resolución:**
1. Calcule la distancia de la **Gota 1** ($t = 2 \text{ s}$):
   $y_1 = \frac{9,8 \cdot 2^2}{2} = \frac{9,8 \cdot 4}{2} = 19,6 \text{ m}$.
2. Calcule la distancia de la **Gota 2** ($t = 1 \text{ s}$):
   $y_2 = \frac{9,8 \cdot 1^2}{2} = \frac{9,8 \cdot 1}{2} = 4,9 \text{ m}$.
3. Reste los resultados para hallar la separación: $19,6 \text{ m} - 4,9 \text{ m} = 14,7 \text{ m}$.

✅ **Resultado:** $14,7 \text{ m}$.
```

> [!tip] 💡 Consejo de estudio
> **Estrategia Profe Alex:** Antes de operar, identifique qué dato **NO tiene** y **NO necesita** hallar. Esto le permitirá elegir la fórmula correcta por descarte. Además, siempre verifique la consistencia de unidades (metros y segundos); simplificar y estandarizar antes de los cálculos evita errores de conversión comunes en física.

---
### 🗝️ Clave de respuestas sugeridas

*   **Fácil 3:** $9,8 \text{ m/s}$.
*   **Medio 1:** $19,6 \text{ m}$.
*   **Medio 2:** $49 \text{ m/s}$.
*   **Medio 3:** La altura se cuadruplica. Debido a que en la fórmula $y = \frac{g \cdot t^2}{2}$, el tiempo está elevado al cuadrado, duplicar el tiempo ($2^2$) resulta en una distancia cuatro veces mayor.