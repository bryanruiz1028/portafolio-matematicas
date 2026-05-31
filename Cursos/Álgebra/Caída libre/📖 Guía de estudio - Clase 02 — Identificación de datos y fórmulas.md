# 📖 Guía de estudio — Clase 02: Caída Libre (Cómo elegir fórmulas y reconocer datos)

¡Qué tal, amigas y amigos! Espero que estén muy bien. Bienvenidos a esta guía donde vamos a dominar la física de una forma sencilla y práctica. Como siempre digo, la clave no es memorizar, sino comprender qué estamos haciendo y por qué. ¡Aprovechando mis dotes de "excelente dibujante" y pedagogo, vamos a darle con toda a este tema!

> [!info] 📌 Conceptos clave
> Para resolver cualquier ejercicio de caída libre como un experto, debemos tener claros estos cinco pilares:
> 1.  **Las 5 magnitudes fundamentales:** En todo problema trabajamos con: Velocidad inicial ($v_0$), Velocidad final ($v_f$), Gravedad ($g$), Tiempo ($t$) y Altura o espacio recorrido ($y$).
> 2.  **Convención de signos para la gravedad ($g$):** Si el objeto va hacia **abajo**, la gravedad ayuda al movimiento (lo acelera), por lo tanto, usamos $g = +9.8 \, m/s^2$. Si el objeto es lanzado hacia **arriba**, la gravedad va en contra (lo frena), así que usamos $g = -9.8 \, m/s^2$.
> 3.  **El significado de "se deja caer":** Si estás quieto y sueltas un objeto, su velocidad inicial es automáticamente cero ($v_0 = 0$). *Nota: Esto cambia si estás en un marco de referencia móvil (como un globo subiendo), pero en problemas estándar, es cero.*
> 4.  **Punto más alto:** En un lanzamiento vertical, cuando el objeto llega arriba del todo y ya no puede subir más, se detiene un instante. Ahí, la velocidad final es cero ($v_f = 0$).
> 5.  **Consistencia de unidades:** ¡Ojo con esto! Antes de operar, revisa que todo esté en metros ($m$) y segundos ($s$). Si ves kilómetros o horas, toca hacer conversiones.

---

## Tabla de Fórmulas y Definiciones

Para elegir la fórmula ganadora, utilizaremos la **Técnica del Descarte**. Identificamos qué variable no tenemos y tampoco queremos hallar (la variable ausente), y eso nos dirá qué ecuación usar.

| Término | Definición / Fórmula | Unidad (SI) | Variable Ausente |
| :--- | :--- | :--- | :--- |
| **Velocidad Inicial ($v_0$)** | Rapidez al inicio del trayecto. | $m/s$ | - |
| **Velocidad Final ($v_f$)** | Rapidez al final del trayecto. | $m/s$ | - |
| **Gravedad ($g$)** | Aceleración constante ($9.8 \, m/s^2$). | $m/s^2$ | - |
| **Tiempo ($t$)** | Duración del movimiento. | $s$ | - |
| **Altura ($y$)** | Desplazamiento vertical. | $m$ | - |
| **Fórmula 1** | $v_f = v_0 + gt$ | - | **Altura ($y$)** |
| **Fórmula 2** | $y = v_0t + \frac{gt^2}{2}$ | - | **Vel. Final ($v_f$)** |
| **Fórmula 3** | $v_f^2 = v_0^2 + 2gy$ | - | **Tiempo ($t$)** |

---

## Sección de Ejemplos Resueltos

```ad-example
title: Ejemplo A — Objeto que se deja caer
**Problema:** Una piedra se deja caer desde lo alto de un edificio y choca contra el piso 5 segundos después. ¿Cuál es la altura del edificio?

**Paso 1: Identificar datos**
*   $v_0 = 0$ (porque "se deja caer").
*   $t = 5 \, s$.
*   $g = +9.8 \, m/s^2$ (positiva porque cae hacia abajo).
*   Incógnita: Altura ($y$).

**Paso 2: Elegir fórmula (Técnica del Descarte)**
Observamos que en los datos no aparece la velocidad final ($v_f$), ni nos la están pidiendo. Por lo tanto, la **Variable Ausente es $v_f$**. Según nuestra tabla, usamos la Fórmula 2:
$$y = v_0t + \frac{gt^2}{2}$$

**Paso 3: Calcular**
$$y = (0)(5) + \frac{9.8(5)^2}{2}$$
$$y = 0 + \frac{9.8(25)}{2}$$
$$y = \frac{245}{2} = 122.5 \, metros.$$

**Resultado:** La altura del edificio es de **122.5 metros**.
```

```ad-example
title: Ejemplo B — Lanzamiento vertical y presupuesto
**Problema:** Se lanza una piedra hacia arriba con una velocidad de $12 \, m/s$. ¿Cuál es la altura máxima alcanzada y cuál sería el costo de un cable de seguridad para esa altura si el metro cuesta $2 \, USD?

**Paso 1: Identificar datos**
*   $v_0 = 12 \, m/s$.
*   $v_f = 0$ (en el punto más alto se detiene).
*   $g = -9.8 \, m/s^2$ (negativa porque va hacia arriba).
*   Incógnita: Altura ($y$).

**Paso 2: Elegir fórmula**
Como no conocemos el tiempo ($t$) ni nos lo piden, la **Variable Ausente es $t$**. Usamos la Fórmula 3:
$$v_f^2 = v_0^2 + 2gy$$

**Paso 3: Calcular altura máxima**
$$0^2 = (12)^2 + 2(-9.8)y$$
$$0 = 144 - 19.6y$$
Pasamos el término negativo al otro lado para que sea positivo:
$$19.6y = 144$$
$$y = \frac{144}{19.6} \approx 7.35 \, metros.$$

**Paso 4: Análisis de presupuesto (USD)**
Costo = $7.35 \, m \times 2 \, USD/m = 14.70 \, USD$.

**Resultado:** Alcanza una altura de **7.35 metros** y el costo del cable es de **14.70 USD**.
```

---

## Ejercicios de Repaso

```ad-abstract
title: Nivel Verde (Fácil): Conceptos e Identificación
1. Si un problema dice que un objeto "se suelta" desde un puente, ¿cuál es el valor de su velocidad inicial?
2. Un objeto es lanzado hacia arriba. ¿Qué valor y signo debe tener la gravedad en tus cálculos?
3. Al llegar al punto más alto de su trayectoria, ¿cuál es el valor exacto de la velocidad final ($v_f$)?
```

```ad-abstract
title: Nivel Amarillo (Medio): Cálculos Directos
1. Un objeto se deja caer y tarda 3 segundos en tocar el suelo. ¿Cuál es su velocidad final justo antes del impacto? (Usa $g = 9.8 \, m/s^2$).
2. Se lanza un cuerpo hacia arriba con una velocidad inicial de $14 \, m/s$. ¿Cuánto tiempo tarda en alcanzar su altura máxima?
3. Calcula la altura desde la que cayó un objeto si tardó 2 segundos en llegar al piso partiendo del reposo.
```

```ad-abstract
title: Nivel Rojo (Avanzado): Retos Complejos
1. Un cuerpo alcanza una altura máxima de 100 metros. Determina su velocidad inicial ($v_0$) y el tiempo ($t$) de subida. Si instalar una malla de protección cuesta $3 \, USD$ por metro de altura, ¿cuál es el costo total para esos 100m? *(Tip: $v_0 \approx 44.27 \, m/s$)*.
2. Un objeto se lanza hacia arriba a $20 \, m/s$. Halla su altura máxima. Si un seguro de accidentes cobra $5 \, USD$ por cada metro de altura potencial de caída, ¿cuánto se debe pagar por este lanzamiento?
```

---

> [!tip] 💡 Consejo de estudio
> **La técnica del "Descarte":** Para elegir la fórmula correcta instantáneamente, identifica la variable que **ni te dan ni te piden**. 
> *   ¿No hay **altura ($y$)**? → Usa Fórmula 1. 
> *   ¿No hay **velocidad final ($v_f$)**? → Usa Fórmula 2. 
> *   ¿No hay **tiempo ($t$)**? → Usa Fórmula 3. 
> ¡Sigue este método y verás que ningún problema se te resiste!

¡Espero que esta guía te sirva muchísimo! Sigue practicando con entusiasmo, comparte este material con tus compañeros y recuerda que en la constancia está el éxito. ¡Nos vemos en la próxima clase!

**¡Bye, bye!**