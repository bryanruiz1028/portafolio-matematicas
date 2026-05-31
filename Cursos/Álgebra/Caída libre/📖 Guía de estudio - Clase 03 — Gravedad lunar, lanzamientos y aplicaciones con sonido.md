# 📖 Guía de estudio — Clase 03: Caída Libre y Lanzamiento Vertical

> [!info] 📌 Conceptos clave
> 1. **¿Soltar o lanzar?**: ¡No son lo mismo! Cuando "dejamos caer" un objeto, su velocidad inicial es nula ($v_0 = 0\text{ m/s}$). En cambio, al "lanzar hacia abajo", le imprimimos un impulso inicial ($v_0 > 0\text{ m/s}$), lo que acelera su llegada al suelo.
> 2. **Gravedad variable**: La aceleración no es universal. Mientras que en la Tierra trabajamos con $g = 9.8\text{ m/s}^2$, en la Luna esta es de apenas $1.62\text{ m/s}^2$. ¡Tus cálculos deben adaptarse al cuerpo celeste!
> 3. **El punto crítico**: En cualquier lanzamiento vertical hacia arriba, existe un instante de "reposo momentáneo" en la altura máxima. En ese punto exacto, la velocidad final es siempre $v_f = 0\text{ m/s}$.
> 4. **El mensajero sonoro**: En pozos profundos, el tiempo que tardas en escuchar el impacto incluye el viaje de ida de la piedra y el de vuelta del sonido a $330\text{ m/s}$. Ignorar esto es el error más común en ingeniería y física.

## Tabla de Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Gravedad ($g$)** | Aceleración constante. En la Tierra: $9.8\text{ m/s}^2$. En la Luna: $1.62\text{ m/s}^2$. |
| **Altura ($h$ o $y$)** | Distancia vertical recorrida: $y = v_0 \cdot t + \frac{g \cdot t^2}{2}$. |
| **Velocidad Final ($v_f$)** | Velocidad en un instante $t$: $v_f = v_0 + g \cdot t$. |
| **Velocidad del Sonido ($v_s$)** | Constante para MRU en aire: $330\text{ m/s}$ (usada para el retorno del eco). |

## Sección de Ejemplos Resueltos

> [!example] Ejemplo A — Velocidad final en lanzamiento vertical
> **Problema:** Un objeto se lanza verticalmente hacia abajo con una velocidad inicial de $5\text{ m/s}$. ¿Qué velocidad llevará a los $3\text{ s}$ de caída?
> 
> **Paso 1: Identificación de datos**
> - Velocidad inicial ($v_0$): $5\text{ m/s}$
> - Tiempo ($t$): $3\text{ s}$
> - Gravedad ($g$): $9.8\text{ m/s}^2$ (**¡Truco pedagógico!** Usamos signo positivo porque la gravedad actúa a favor del movimiento, aumentando la velocidad).
> 
> **Paso 2: Sustitución y cálculo**
> $v_f = v_0 + g \cdot t$
> $v_f = 5\text{ m/s} + (9.8\text{ m/s}^2 \cdot 3\text{ s})$
> $v_f = 5\text{ m/s} + 29.4\text{ m/s}$
> 
> **Resultado:** La velocidad final es de $34.4\text{ m/s}$.

> [!example] Ejemplo B — Profundidad de un pozo con eco ($USD)
> **Problema:** Una empresa de excavación cobra $10\text{ USD}$ por cada metro de profundidad. Al soltar una piedra ($v_0 = 0\text{ m/s}$), el sonido del impacto se escucha a los $5\text{ s}$. ¿Cuál es el costo del trabajo?
> 
> **Paso 1: Análisis del sistema (El secreto de la igualdad)**
> El tiempo total ($5\text{ s}$) se divide en: tiempo de caída de la piedra ($t_c$) y tiempo de subida del sonido ($t_s$). Por tanto, $t_s = 5 - t_c$.
> Como la profundidad ($y$) es la misma para ambos:
> - Caída (MUA): $y = 4.9 \cdot t_c^2$
> - Sonido (MRU): $y = 330 \cdot (5 - t_c)$
> 
> **Paso 2: Configuración de la ecuación técnica**
> Igualamos ambas expresiones para hallar $t_c$:
> $$4.9t_c^2 = 330(5 - t_c)$$
> Resolviendo la ecuación cuadrática resultante ($4.9t_c^2 + 330t_c - 1650 = 0$), obtenemos que $t_c \approx 4.67\text{ s}$. 
> Sustituyendo en la fórmula de altura: $y = 4.9 \cdot (4.67)^2 \approx 106.86\text{ m}$.
> 
> **Paso 3: Cálculo del presupuesto**
> $Costo = 106.86\text{ m} \cdot 10\text{ USD/m} = 1,068.60\text{ USD}$.
> 
> **Nota técnica:** Podrían existir pequeñas variaciones decimales (ej. $108.9\text{ m}$) si se redondea el tiempo del sonido, pero el método de igualación es el más preciso.

## Ejercicios de Repaso Graduados

> [!abstract] 🟢 Nivel Inicial: Gravedad Lunar y Caída Simple
> 1. **Verificación científica**: Se deja caer un objeto desde $2\text{ m}$ de altura en la Luna y tarda $1.57\text{ s}$ en tocar el suelo. Despeja la fórmula de altura para demostrar que $g \approx 1.62\text{ m/s}^2$.
> 2. Una piedra se lanza hacia arriba en la superficie lunar a $12\text{ m/s}$. Calcula el tiempo que tarda en alcanzar su punto más alto ($v_f = 0\text{ m/s}$).
> 3. Con el tiempo hallado en el ejercicio anterior, determina la altura máxima alcanzada por la piedra.

> [!abstract] 🟡 Nivel Medio: El reto del globo aerostático
> 1. **¡Cuidado con la trampa!**: Un globo sube a $5\text{ m/s}$. A $50\text{ m}$ de altura, se suelta un lastre. Debido a la inercia, el lastre sale con $v_0 = 5\text{ m/s}$ *hacia arriba*. Calcula cuánto tiempo tarda en dejar de subir.
> 2. Determina la altura máxima total que alcanza el lastre respecto al suelo (considerando los $50\text{ m}$ iniciales más el tramo de subida extra).
> 3. Calcula el tiempo total de vuelo desde que se suelta hasta que impacta el suelo (Suma $t_{subida} + t_{bajada}$).

> [!abstract] 🔴 Nivel Avanzado: Ingeniería y Acústica
> 1. Un pozo de agua devuelve el sonido del impacto a los $3.2\text{ s}$ de soltar una piedra. Plantea el sistema de ecuaciones y calcula la profundidad exacta.
> 2. **Presupuesto de obra**: Si la excavación cuesta $15\text{ USD}$ por metro lineal, ¿cuál es el presupuesto para el pozo del ejercicio anterior?
> 3. **Análisis de eco**: En un pozo de $108.9\text{ m}$, calcula exclusivamente el tiempo $t_s$ (tiempo que tarda el sonido en subir) usando $v_s = 330\text{ m/s}$. Recuerda que este tramo es Movimiento Rectilíneo Uniforme (MRU).

> [!tip] 💡 Consejo de estudio del Profe Alex
> ¡No operes a ciegas! El **diagrama de cuerpo libre** es tu mejor amigo. Dibuja siempre el vector de velocidad inicial y el de la gravedad. 
> - **Si van en el mismo sentido** (ej. cae): $g$ es positiva ($+$). 
> - **Si van en sentidos opuestos** (ej. sube): $g$ es negativa ($-$). 
> El signo no es una propiedad del planeta, sino una relación con tu movimiento.