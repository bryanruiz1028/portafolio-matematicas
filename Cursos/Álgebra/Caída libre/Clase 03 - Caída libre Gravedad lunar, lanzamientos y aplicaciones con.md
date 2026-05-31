# Clase 03 — Caída libre: Gravedad lunar, lanzamientos y aplicaciones con sonido

tags: #algebra #caidalibre
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 4

> [!info] 🧭 Navegación
> [[Clase 02 - Caída libre Identificación de datos y fórmulas|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | | [[Clase 04 - Caída Libre|Clase 04 ➡]]

## ¿Por qué es importante esta clase?
El estudio de la caída libre es la puerta de entrada para comprender el universo y resolver problemas técnicos complejos en la Tierra. En esta sesión, aprenderás que las leyes de la física son universales, pero sus constantes cambian según el entorno.
- 💵 **Aplicación con $USD:** Una medición precisa de la gravedad lunar es vital para misiones espaciales; un error de cálculo podría poner en riesgo equipos de aterrizaje valorados en millones de dólares. Asimismo, los sensores acústicos industriales para medir pozos profundos pueden superar los **$1,500 USD**.
- 🏗️ **Aplicación práctica:** Permite a ingenieros civiles y rescatistas calcular la profundidad de grietas o la altura de edificios inaccesibles utilizando únicamente un cronómetro.
- 📊 **Situación cotidiana:** Entenderás por qué existe un retraso entre el impacto de un objeto en el fondo de un pozo y el momento en que escuchas el "clac", una distinción fundamental entre la velocidad del objeto y la velocidad del sonido.

## Concepto clave

> [!note] ¿Qué es la Caída Libre?
> Imagina que dejas caer una pelota. La **Caída Libre** es el movimiento que realiza un objeto cuando se desplaza únicamente bajo la influencia de la gravedad. Para un estudiante de 12 años: es como si el objeto estuviera en un tobogán invisible donde solo la gravedad lo empuja hacia abajo (o lo frena si va hacia arriba), sin que el aire o un motor intervengan.

> [!warning] ¡Cuidado con estos errores!
> 1. **La Velocidad Inicial ($v_i$):** No siempre es cero. Si el objeto se "deja caer", $v_i = 0$. Pero si el objeto se "lanza" hacia abajo o hacia arriba, debes usar el valor de ese impulso inicial.
> 2. **El Signo de la Gravedad:** Si el objeto baja, la gravedad aumenta su rapidez (positiva: $+9.8 m/s^2$). Si el objeto sube, la gravedad lo frena (negativa: $-9.8 m/s^2$).

> [!tip] Regla mnemotécnica
> "Hacia **abajo**, la gravedad **suma** rapidez; hacia **arriba**, la gravedad la **derriba** (resta)".

## Procedimiento paso a paso
Para resolver problemas de cinemática como el Profe Alex, sigue estos 4 pasos universales en tu bloque de notas:

```text
1. IDENTIFICAR: Anota al menos 3 datos conocidos (ej. v_i, h, t).
2. SELECCIONAR: Elige la fórmula que NO contenga la variable que no quieres hallar ni conoces.
3. VERIFICAR: Asegúrate de que las unidades sean metros (m) y segundos (s).
4. RESOLVER: Despeja la incógnita e interpreta si el resultado es físicamente lógico.
```

## Ejemplos resueltos

```ad-example
title: Ejemplo 1 — Gravedad en la Luna (Video 4)
**Problema:** Se deja caer un cuerpo desde una altura de $h = 2m$ y tarda $1.57s$ en llegar al suelo lunar. Calcula el valor de $g$ en la Luna.
**Solución:**
- **Datos:** $h = 2m$, $t = 1.57s$, $v_i = 0$ (se deja caer).
- **Fórmula:** $h = v_i \cdot t + \frac{g \cdot t^2}{2}$
- Como $v_i = 0$, el término $(v_i \cdot t)$ desaparece: $2 = \frac{g \cdot (1.57)^2}{2}$
- **Despeje:** 
  1. $2 \cdot 2 = g \cdot 2.4649$
  2. $4 = g \cdot 2.4649 \implies g = \frac{4}{2.4649}$
- **Resultado:** $g \approx 1.62 m/s^2$.
```

```ad-example
title: Ejemplo 2 — Lanzamiento hacia abajo (Video 5)
**Problema:** Se lanza una piedra hacia abajo con $v_i = 5 m/s$. ¿Qué velocidad tendrá a los $3s$ y qué distancia recorre específicamente entre el segundo $3$ y el segundo $4$?
**Solución:**
- **Velocidad final ($v_f$) a los 3s:** $v_f = v_i + g \cdot t = 5 + (9.8 \cdot 3) = 34.4 m/s$.
- **Distancia entre t=3 y t=4:** Aplicamos la fórmula $h = v_i \cdot t + \frac{1}{2}g \cdot t^2$ para ambos tiempos:
  1. $h_3 = 5(3) + 4.9(3^2) = 15 + 44.1 = 59.1m$.
  2. $h_4 = 5(4) + 4.9(4^2) = 20 + 78.4 = 98.4m$.
- **Resta de alturas ($\Delta h$):** $98.4m - 59.1m = 39.3m$.
```

```ad-example
title: Ejemplo 3 — El globo aerostático (Video 7)
**Problema:** Un globo sube a una velocidad constante de $5 m/s$. Cuando está a $50m$ de altura, se suelta un costal. ¿Cuánto tarda en tocar el suelo?
**Análisis:** El costal "hereda" la velocidad del globo, por lo que su $v_i = 5 m/s$ hacia arriba.
1. **Fase de Subida:** El objeto sube hasta que su $v_f = 0$. 
   - Tiempo subida: $t = \frac{v_i}{g} = \frac{5}{9.8} = 0.51s$.
   - Altura extra alcanzada: $h_s = 5(0.51) - 4.9(0.51^2) = 1.28m$.
2. **Fase de Bajada:** Cae desde el punto más alto.
   - Nueva altura total: $50m + 1.28m = 51.28m$.
   - Tiempo bajada: $51.28 = 4.9 \cdot t^2 \implies t_b = \sqrt{\frac{51.28}{4.9}} = 3.23s$.
- **Tiempo total:** $0.51s + 3.23s = 3.74s$.
```

```ad-example
title: Ejemplo 4 — El pozo y la velocidad del sonido (Video 8)
**Problema:** Se deja caer una piedra en un pozo y se escucha el impacto a los $5s$. Si la velocidad del sonido es $330 m/s$, ¿cuál es la profundidad?
**Solución:** La distancia que cae la piedra ($h$) es la misma distancia que recorre el sonido al subir. Por tanto, igualamos ambas ecuaciones de distancia:
- **Ecuación Piedra (Caída):** $h = 4.9 \cdot t_c^2$
- **Ecuación Sonido (MRU):** $h = 330 \cdot (5 - t_c)$
- **Igualación:** $4.9t_c^2 = 1650 - 330t_c \implies 4.9t_c^2 + 330t_c - 1650 = 0$.
- Aplicando la fórmula cuadrática, obtenemos $t_c = 4.67s$.
- **Profundidad:** $h = 330 \cdot (5 - 4.67) = 106.86m$.
- **Dato $USD:** Un cable de acero de 110m para validar esta profundidad cuesta unos **$120 USD**.
```

## Ejercicios para el estudiante

- **🟢 Fácil:** Si lanzas una pelota hacia arriba en la Luna ($g = 1.62 m/s^2$) con una $v_i = 12 m/s$, ¿cuál es su altura máxima y cuánto tiempo tarda en alcanzarla?
- **🟡 Medio:** Se lanza una piedra hacia abajo. Si a los $3s$ su velocidad es de $37.6 m/s$, ¿con qué velocidad inicial ($v_i$) se lanzó? (Utiliza $g = 9.8 m/s^2$).
- **🔴 Avanzado:** Desde la azotea de un edificio de $40m$, se lanza una pelota hacia arriba a $10 m/s$. Calcula el tiempo total que transcurre hasta que la pelota impacta en la calle.

## Respuestas (para el docente)

```ad-success
- **Fácil:** Tiempo de subida: $7.4s$ | Altura máxima: $44.4m$.
- **Medio:** Velocidad inicial ($v_i$): $8.2 m/s$.
- **Avanzado:** Tiempo total: $4.05s$ (Desglose: Subida de $1.02s$ hasta alcanzar $+5.1m$ y bajada de $3.03s$ desde una altura de $45.1m$).
```

## Mini-prueba de autoevaluación

1. **Conceptual:** Si sueltas un objeto desde un globo aerostático que está ascendiendo, el objeto:
   - a) Empieza a caer hacia abajo inmediatamente.
   - b) Sube un trayecto corto debido a la inercia antes de empezar a caer.
   - c) Mantiene su posición estática en el aire.

2. **Procedimental:** Si necesitas calcular la altura de caída pero no tienes el dato de la velocidad final ($v_f$), ¿cuál es la fórmula más eficiente?
   - a) $v_f = v_i + g \cdot t$
   - b) $h = v_i \cdot t + \frac{1}{2}g \cdot t^2$
   - c) $v_f^2 = v_i^2 + 2 \cdot g \cdot h$

3. **Aplicación $USD:** Un ingeniero calcula que un pozo tiene $45.1m$ de profundidad. Si el metro de cable de medición cuesta **$2 USD**, ¿cuánto presupuesto aproximado debe solicitar para comprar el cable necesario?
   - a) $90.20 USD$
   - b) $45.10 USD$
   - c) $180.40 USD$

## Notas para el próximo tema

> [!tip] ¡Prepárate!
> En la **Clase 04**, transformaremos estos números en imágenes. Estudiaremos las **gráficas de posición vs. tiempo**, lo que te permitirá visualizar cómo la gravedad curva la trayectoria del movimiento en el tiempo.

> [!info] 🧭 Navegación
> [[Clase 02 - Caída libre Identificación de datos y fórmulas|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | | [[Clase 04 - Caída Libre|Clase 04 ➡]]