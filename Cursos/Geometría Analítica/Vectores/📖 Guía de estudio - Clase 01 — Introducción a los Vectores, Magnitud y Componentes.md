# 📖 Guía de estudio — Clase 01: Introducción a los Vectores

> [!info] 📌 Conceptos clave
> 1. **Magnitud Escalar vs. Vectorial:** Las magnitudes escalares quedan definidas solo con un número y su unidad (ej. masa, tiempo). Las vectoriales (ej. fuerza, velocidad) requieren, además, una **dirección** y un **sentido** para ser comprendidas totalmente.
> 2. **Características del Vector:**
>    - **Magnitud (Módulo):** Es la longitud o medida de la flecha. Representa "qué tan grande" es el vector.
>    - **Dirección:** Es la inclinación de la recta, definida por el ángulo que forma con el eje horizontal (Eje X).
>    - **Sentido:** Indicado por la punta de la flecha. Es vital porque determina si la componente será positiva o negativa.
> 3. **Componentes Rectangulares:** Son las proyecciones o **"sombras"** que el vector proyecta sobre los ejes X e Y. Al dibujarlas, notarás que forman un triángulo rectángulo con el vector original.
> 4. **Signos y Geografía:** Asociamos el plano cartesiano con los puntos cardinales:
>    - **Eje X:** Este (+) / Oeste (-).
>    - **Eje Y:** Norte (+) / Sur (-).

> [!warning] ⚠️ Atención técnica: La Calculadora
> Antes de realizar cualquier cálculo trigonométrico (Seno o Coseno), verifica que tu calculadora esté configurada en modo de grados. En la parte superior de la pantalla debe aparecer una **"D"** o la palabra **"DEG"**. Si aparece una "R" o "RAD", los resultados serán incorrectos.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Magnitud (Módulo)** | Longitud del vector. Se denota como $|v|$ y **siempre es un valor positivo ($|v| \geq 0$)**. |
| **Componente en X ($v_x$)** | $v_x = |v| \cdot \cos(\theta)$. Proyección horizontal (Coseno si el ángulo sale de X). |
| **Componente en Y ($v_y$)** | $v_y = |v| \cdot \sin(\theta)$. Proyección vertical (Seno si el ángulo sale de X). |
| **Cálculo de Magnitud** | $|v| = \sqrt{v_x^2 + v_y^2}$. Se aplica el **Teorema de Pitágoras**. |

## Ejemplos resueltos

```ad-example
title: Ejemplo A — Cálculo de Componentes (Caso Geográfico)
**Enunciado:** Un vector $M$ mide 10 m y tiene una dirección de 20° desde el Oeste hacia el Norte. Hallar sus componentes.

**Paso 1: Identificar signos por sentido.** 
- Oeste es hacia la izquierda en el eje X: $(-)$.
- Norte es hacia arriba en el eje Y: $(+)$.

**Paso 2: Aplicar fórmulas (con unidades).** 
- $M_x = -(10 \text{ m} \cdot \cos 20^\circ) = -(10 \cdot 0,939) = -9,39 \text{ m}$.
- $M_y = +(10 \text{ m} \cdot \sin 20^\circ) = +(10 \cdot 0,342) = 3,42 \text{ m}$.

✅ **Resultado:** Las componentes son $(-9,39 \text{ m}, 3,42 \text{ m})$. El dibujo nos confirma que la sombra en X es más larga que en Y.
```

```ad-example
title: Ejemplo B — Cálculo de Magnitud (Aplicación $USD)
**Enunciado:** Un dron recorre una ruta con componentes $x = 3 \text{ km}$ y $y = 4 \text{ km}$. Si el costo de operación por kilómetro lineal es de $1 USD, ¿cuál es el costo total del trayecto?

**Paso 1: Hallar la magnitud usando Pitágoras.** 
$|v| = \sqrt{(3 \text{ km})^2 + (4 \text{ km})^2} = \sqrt{9 + 16} = \sqrt{25} = 5 \text{ km}$.

**Paso 2: Calcular el costo unitario.** 
$5 \text{ km} \times 1 \text{ USD/km} = 5 \text{ USD}$.

✅ **Resultado:** La distancia directa es de 5 km y el costo total es de $5 USD.
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
1. Clasifica como escalar o vectorial: Masa, Velocidad, Temperatura, Fuerza.
2. Si un vector apunta hacia el Sur y el Este, ¿qué signos tendrán $v_x$ y $v_y$?
3. ¿Qué herramienta se usa para medir físicamente la dirección (ángulo) en el papel?
```

```ad-abstract
title: 🟡 Medio
1. Un vector de 20 cm tiene un ángulo de 45° en el primer cuadrante. Halla sus componentes.
2. Calcula la magnitud de un vector con componentes $v_x = -5$ y $v_y = 2$. (Recuerda que el resultado debe ser positivo).
3. Un vector es totalmente horizontal hacia la derecha y mide 8 unidades. ¿Cuánto vale su componente en Y?
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
1. Un cable ejerce fuerza con componentes $(-7, -3)$. Calcula la magnitud total. Si reforzar cada unidad de fuerza cuesta $10 USD, ¿cuál es el presupuesto total?
2. Un barco viaja 15 km al Norte y luego 20 km al Oeste. Halla la magnitud del desplazamiento total y el costo de combustible si consume $2 USD por cada km de distancia directa.
```

> [!tip] 💡 Consejo de estudio
> Para no fallar, recuerda: si el ángulo "nace" del eje horizontal (X), usa **Coseno para X** y **Seno para Y**. 
> **¿Qué pasa si el ángulo viene del eje vertical (Norte/Sur)?** No te compliques: resta ese ángulo a 90° para obtener el **ángulo complementario** respecto al eje X y así usar las fórmulas estándar sin errores. ¡Dibuja siempre tu plano cartesiano para verificar los signos!