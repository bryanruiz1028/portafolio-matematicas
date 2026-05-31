# 📖 Guía de estudio — Clase 01: Introducción a la Caída Libre

Este documento ha sido diseñado por expertos para sintetizar los fundamentos de la caída libre y las herramientas matemáticas necesarias para resolver problemas de cinemática vertical, siguiendo las explicaciones pedagógicas de nuestro curso.

```ad-info
title: 📌 Conceptos clave
*   **Definición de caída libre:** Es el movimiento de un objeto cuando la única fuerza que actúa sobre él es la gravedad. En este estado ideal, no existe interferencia de la resistencia del aire ni de la fricción.
*   **El descubrimiento de Galileo:** Galileo Galilei demostró que todos los objetos, sin importar su masa, forma o composición, caen con la misma aceleración en el vacío. Esto rompió con la idea antigua de que los objetos pesados caían más rápido.
*   **Tierra vs. Vacío/Luna:** En la Tierra, la resistencia del aire frena objetos ligeros (como una servilleta). Sin embargo, en la Luna (donde no hay atmósfera), el comandante David Scott (Apolo 15) demostró esto soltando un **martillo de geólogo de 1,32 kg** y una **pluma de halcón de 30 gramos**; ambos tocaron el suelo al mismo tiempo.
*   **Naturaleza de la gravedad:** No es solo una fuerza; según Einstein, es la **curvatura del espacio-tiempo** causada por la masa. Se manifiesta como una aceleración ($g$). En la Tierra su valor estándar es de **$9,807 m/s^2$**, mientras que en la Luna es de solo **$1,62 m/s^2$**. Para facilitar cálculos rápidos en este curso, redondearemos la gravedad terrestre a **$10 m/s^2$**.
```

## Fórmulas y definiciones importantes

Para el estudio de la caída libre, adaptamos las fórmulas del Movimiento Uniformemente Acelerado. El cambio principal es que el desplazamiento ocurre en el **eje vertical ($y$)** y la aceleración es constante bajo el valor de la **gravedad ($g$)**.

| Término | Definición / Fórmula |
| :--- | :--- |
| **Gravedad ($g$)** | Aceleración constante hacia el centro de la Tierra. Usaremos $9,8 m/s^2$ para precisión y $10 m/s^2$ para ejercicios mentales. |
| **Velocidad Final ($v_f$)** | La velocidad tras un tiempo determinado: <br> $v_f = v_i + g \cdot t$ |
| **Altura / Espacio ($y$)** | Distancia vertical recorrida. Cambiamos la $x$ (horizontal) por la $y$ (vertical): <br> $y = v_i \cdot t + \frac{g \cdot t^2}{2}$ |
| **Velocidad Final al cuadrado ($v_f^2$)** | Relaciona velocidad y altura sin necesidad de conocer el tiempo: <br> $v_f^2 = v_i^2 + 2 \cdot g \cdot y$ |

---

```ad-example
title: Ejemplo A — Caso básico
**Escenario:** Se suelta una pelota desde lo alto de un edificio. ¿Qué velocidad tendrá tras 3 segundos de caída? (Usa $g = 10 m/s^2$).

*   **Paso 1 (Identificar datos):**
    *   Velocidad inicial ($v_i$): $0 m/s$ (La palabra clave "se suelta" siempre implica $v_i = 0$).
    *   Tiempo ($t$): $3 s$.
    *   Gravedad ($g$): $10 m/s^2$.
*   **Paso 2 (Aplicar fórmula de $v_f$):**
    *   $v_f = v_i + g \cdot t$
    *   $v_f = 0 + (10 m/s^2 \cdot 3 s)$
*   **Resultado:** La velocidad final es de **$30 m/s$**.
```

```ad-example
title: Ejemplo B — Aplicación con contexto real
**Escenario:** A un turista se le cae accidentalmente un billete de **$100 USD** desde un balcón. Si el billete cae libremente (ignorando el aire) durante 2 segundos, ¿con qué velocidad impactará el suelo?

*   **Paso 1 (Identificar datos):**
    *   $v_i = 0 m/s$.
    *   $t = 2 s$.
    *   $g = 10 m/s^2$.
*   **Paso 2 (Cálculo):**
    *   $v_f = 0 + (10 \cdot 2)$
*   **Resultado:** El billete alcanza una velocidad de **$20 m/s$** justo antes de tocar el suelo.
```

---

```ad-abstract
title: Ejercicios de repaso

**🟢 Fácil (Teoría)**
1. En el vacío absoluto, si lanzamos simultáneamente un celular y una servilleta extendida, ¿cuál llegará primero al suelo?
2. ¿Quién fue el científico que utilizó un martillo y una pluma en la Luna para demostrar las leyes de Galileo?
3. Define la gravedad según la visión de Albert Einstein mencionada en el video.

**🟡 Medio (Numéricos)**
1. Si dejas caer una piedra desde un puente y tarda 5 segundos en tocar el agua, ¿cuál es su velocidad final? (Usa $g = 10 m/s^2$).
2. Un cubo de Rubik se lanza hacia arriba con una velocidad de $30 m/s$. Si la gravedad actúa como desaceleración, ¿cuál será su velocidad después de 1 segundo?
3. En el mismo ejercicio del cubo de Rubik, ¿cuál será su velocidad a los 3 segundos?

**🔴 Avanzado (Problema de aplicación)**
Una billetera con **$500 USD** es lanzada verticalmente hacia arriba con una velocidad inicial de $30 m/s$.
*   Calcula cuánto tiempo tarda en alcanzar su punto más alto (donde su velocidad se vuelve 0).
*   ¿Qué altura máxima alcanza la billetera? 
*   *Guía técnica:* Este es un problema de dos pasos. Primero usa la fórmula de $v_f$ para hallar el tiempo, y luego usa ese tiempo en la fórmula de altura ($y$), o utiliza directamente la fórmula de $v_f^2$.
```

---

```ad-tip
title: 💡 Consejo de estudio: La regla de los signos
Para dominar la física, debemos tratar las **magnitudes vectoriales** con orden. Sigue la estrategia del "Profe Alex":

Decide la dirección del movimiento antes de anotar los datos:
1.  **Si el objeto baja (Caída):** Considera la dirección hacia abajo como **positiva**. Así, la gravedad, la altura y la velocidad serán todas positivas, simplificando tus cálculos.
2.  **Si el objeto sube (Lanzamiento vertical):** Considera la dirección hacia arriba como positiva. En este caso, la gravedad debe usarse con **signo negativo ($-10 m/s^2$)** porque es una aceleración que se opone al movimiento, haciendo que el objeto pierda velocidad hasta detenerse.
```