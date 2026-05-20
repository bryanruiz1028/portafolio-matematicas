# 📖 Guía de estudio — Clase 02: Representación gráfica de vectores por componentes

> [!info] 📌 Conceptos clave
> *   **¿Punto o Vector?:** Es fundamental no confundirlos. Mientras que un punto $(x, y)$ es una ubicación estática (un lugar en el mapa), un **vector** es una "receta de viaje" o instrucción de movimiento. No es solo el destino, sino el desplazamiento para llegar allí.
> *   **Significado de X (Horizontal):** El primer número nos dice cuánto movernos en el eje X. Si es positivo, vamos hacia la **derecha**; si es negativo, hacia la **izquierda**.
> *   **Significado de Y (Vertical):** El segundo número indica el movimiento en el eje Y. Si es positivo, subimos hacia **arriba**; si es negativo, bajamos hacia **abajo**.
> *   **Independencia del origen:** Un vector no está "atado" a un solo lugar. Puedes dibujarlo iniciando en el origen $(0,0)$ o en cualquier otro punto del plano; mientras mantenga sus mismos desplazamientos, sigue siendo el mismo vector.

### Fórmulas y definiciones importantes

| Término | Definición basada en la fuente |
| :--- | :--- |
| **Componente X** | Desplazamiento horizontal paralelo al eje x (nuestro movimiento lateral). |
| **Componente Y** | Desplazamiento vertical paralelo al eje y (nuestro movimiento de subida o bajada). |
| **Vector Suma (Gráfico)** | Es el "atajo" o vuelo directo. Es el vector que une la **Cola** del primero con la **Cabeza** del último tras formar un camino. |
| **Suma de Componentes** | Proceso matemático: se suman las $x$ con las $x$, y las $y$ con las $y$; **nunca se mezclan**. |

---

### Ejemplos Resueltos

```ad-example
title: Ejemplo A — Representación básica de un vector
**Vector a = (2, 4)**
Para graficar este vector, imagina que estás siguiendo las instrucciones de un mapa del tesoro desde cualquier punto de inicio:

1. **Paso 1 (Movimiento en X):** Ubícate en la **Cola** (inicio) y desplázate **2 unidades hacia la derecha** (porque el 2 es positivo).
2. **Paso 2 (Movimiento en Y):** Desde donde quedaste, desplázate **4 unidades hacia arriba** (porque el 4 es positivo).
3. **Resultado:** Dibuja la flecha desde el inicio hasta el punto final. La **Cabeza** (punta de la flecha) debe quedar exactamente donde terminó el último movimiento.
```

```ad-example
title: Ejemplo B — Aplicación práctica (Presupuesto y Balance)
**Contexto:** Imagina que el eje X representa tus "Ingresos por Ventas" y el eje Y tus "Bonos Extra". La suma de vectores representa el resultado acumulado de dos días de trabajo:

*   **Día 1 (Vector a = 5, 2):** Ganaste 5 USD en ventas y 2 USD en bonos.
*   **Día 2 (Vector b = 3, 8):** Ganaste 3 USD más en ventas y 8 USD más en bonos.

**Suma gráfica (El camino financiero):**
1. Dibujamos el vector **a** partiendo de la **Cola**.
2. Donde termina la **Cabeza** de **a**, conectamos la **Cola** del vector **b**.
3. El resultado es el balance acumulado: un vector que va desde el inicio del primer día hasta el final del segundo.
**Cálculo:** $(5+3, 2+8) = (8, 10)$. Tu éxito acumulado es de 8 USD en ventas y 10 USD en bonos.
```

---

### Ejercicios de Repaso

```ad-abstract
title: 🟢 Nivel: Fácil
1. Grafica en tu cuaderno el vector **a = (-4, 4)** iniciando desde el origen $(0,0)$. 
2. Grafica el vector **b = (5, -3)** iniciando también desde el origen.
*Pista: Identifica bien si la **Cabeza** (punta de la flecha) debe ir hacia la izquierda o hacia abajo según el signo.*
```

```ad-abstract
title: 🟡 Nivel: Medio
Dados los vectores **m = (-3, 4)** y **n = (7, -2)**:
1. Realiza la suma numérica **m + n** (Recuerda: las $x$ con las $x$ y las $y$ con las $y$).
2. Realiza la suma gráfica: dibuja el vector **m** y, justo donde termina su **Cabeza**, comienza la **Cola** del vector **n**. 
3. Verifica que el "atajo" (vector resultante) coincida con tu resultado numérico.
```

```ad-abstract
title: 🔴 Nivel: Avanzado — Aplicación Financiera
En un plano de finanzas corporativas, tenemos tres puntos clave: **M(2, 4)**, **N(-3, 3)** y **P(1, -4)**.
1. Encuentra las componentes de los vectores de movimiento:
   - Vector **mn** (de M hacia N): Resultado = **(-5, -1)**.
   - Vector **pn** (de P hacia N): Resultado = **(-4, 7)**.
2. **Interpretación:** Si el vector **mn** representa el movimiento del balance del mes, ¿cómo explicarías el resultado **(-5, -1)**? 
*(Pista: Un valor negativo en X e Y significa que hubo una pérdida o retroceso en ambas categorías financieras).*
```

---

> [!tip] 💡 Consejo de estudio
> Para no fallar nunca en la suma gráfica, usa el **"método del caminito"**: la **Cabeza** (punta) de un vector debe ser siempre el punto de partida (**Cola**) del siguiente. El vector resultante siempre será el **atajo** (el vuelo directo) que une el puro inicio de tu recorrido con el final definitivo. ¡Nunca unas dos puntas de flecha entre sí!