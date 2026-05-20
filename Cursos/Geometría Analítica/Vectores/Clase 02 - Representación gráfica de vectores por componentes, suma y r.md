# Clase 02 — Representación gráfica de vectores por componentes, suma y resta

tags: #algebra #graphicalrepres
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 6

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | [[Clase 03|Clase 03 ➡]]

---

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> Los vectores no son simples flechas estáticas; son herramientas dinámicas que nos permiten mapear movimientos y fuerzas en el espacio. Gracias a ellos, podemos predecir trayectorias exactas y entender cómo interactúan diferentes impulsos sobre un objeto.
> 
> *   💵 **Finanzas:** Los cambios en una cuenta se representan como vectores de flujo, donde el primer componente indica el balance en $USD y el segundo el ritmo de crecimiento.
> *   🏗️ **Ingeniería Civil:** Se utilizan para calcular cómo se distribuyen las fuerzas en los puentes y estructuras para garantizar que soporten el peso necesario.
> *   📊 **Navegación:** Los sistemas de GPS y los pilotos de aviación calculan la ruta neta sumando el vector de velocidad del motor con el vector de la velocidad del viento.

---

## Concepto clave

> [!note] 📌 ¿Qué es la representación gráfica de vectores por componentes?
> Imagina que tienes un **mapa del tesoro**. Las componentes de un vector son las "instrucciones" exactas para llegar a la X: "camina 2 pasos a la derecha y 4 hacia adelante". No importa si empiezas en la entrada del parque o bajo un árbol; si sigues las mismas instrucciones, el desplazamiento es el mismo. El vector es el "camino directo" o flecha que une tu punto de inicio con tu destino final.

> [!warning] ⚠️ Error común
> Un **punto** es una ubicación fija, mientras que un **vector** es un movimiento o instrucción. No los confundas aunque usen los mismos números.
> *   ❌ **Incorrecto:** Pensar que el vector $(2, 4)$ es solo el punto "quieto" en las coordenadas $x=2, y=4$.
> *   ✅ **Correcto:** El vector $(2, 4)$ representa la acción de avanzar 2 unidades en el eje horizontal y 4 en el vertical. Un vector puede dibujarse en cualquier parte del plano, no solo naciendo desde el centro $(0,0)$.

> [!tip] 💡 Truco para recordarlo
> Para no perderte, recuerda siempre este orden:
> *   **Eje X (Horizontal):** Positivo (+) hacia la **derecha**, Negativo (-) hacia la **izquierda**.
> *   **Eje Y (Vertical):** Positivo (+) hacia **arriba**, Negativo (-) hacia **abajo**.

---

## Procedimiento paso a paso

> [!important] 📝 Nota pedagógica
> Para obtener resultados precisos, se recomienda realizar estos trazos siempre en **papel cuadriculado**.

```text
PASO 1 → Graficar el primer vector desde el origen o desde un punto inicial cualquiera.
PASO 2 → Iniciar el segundo vector exactamente donde terminó la "cabeza" (punta de flecha) del primero.
PASO 3 → Repetir el proceso para vectores adicionales creando un "camino" continuo.
PASO 4 → Trazar el VECTOR RESULTANTE: es la flecha "atajo" que va desde el inicio del primer vector hasta el final del último.
```

---

## Ejemplos de clase

> [!example] Ejemplo 1 (Básico): Suma de vectores
> **Operación:** $a(2, 3) + b(4, 1)$
> 1. Dibujamos el vector $a$: 2 a la derecha, 3 hacia arriba.
> 2. Donde termina $a$, dibujamos el vector $b$: 4 a la derecha, 1 hacia arriba.
> 3. El resultado es el vector que une el inicio de $a$ con el final de $b$.
> 4. **Cálculo algebraico:** $(2+4, 3+1) = (6, 4)$.

> [!example] Ejemplo 2 (Signos): Resta de vectores
> **Operación:** $c(-3, 5) - d(2, -3)$
> 1. Al restar, invertimos el sentido del segundo vector: $-(2, -3)$ se convierte en $(-2, 3)$.
> 2. Sumamos los componentes cuidando los signos:
>    *   En X: $-3 - 2 = -5$
>    *   En Y: $5 - (-3) \rightarrow 5 + 3 = 8$
> 3. **Resultado:** $(-5, 8)$. Gráficamente, la flecha de $d$ ahora apunta en dirección opuesta.

> [!example] Ejemplo 3 (Avanzado): Suma triple
> **Operación:** $a(5, 2) + d(2, -3) + e(-4, -8)$
> 1. Agrupamos todas las $x$: $5 + 2 - 4 = 3$.
> 2. Agrupamos todas las $y$: $2 + (-3) + (-8) = -9$.
> 3. **Resultado:** El vector resultante es $(3, -9)$. En el gráfico, verás un camino de tres tramos que se resume en una sola flecha larga hacia abajo y a la derecha.

> [!example] Ejemplo 4 (Aplicación $USD)
> **Problema:** Una cuenta bancaria tiene un estado inicial $(saldo, crecimiento)$ de $(100, 10)$. Se registra una transacción de $(-30, -2)$ por un retiro de $30 USD y una caída en el interés.
> 1. Sumamos: $(100 - 30, 10 - 2)$.
> 2. **Resultado:** El nuevo estado es $(70, 8)$. Esto significa que el saldo neto actual es de $70 USD y el factor de crecimiento bajó a 8.

---

## Ejercicios para el estudiante

> [!abstract] 🟢 Nivel Fácil
> 1. Grafica y suma $u(2, 4) + v(1, 2)$ iniciando el primer vector en el origen $(0,0)$.
> 2. Para demostrar que los vectores pueden estar en cualquier lado: Grafica $m(3, 1)$ iniciando en el punto $(1, 1)$. Desde donde termine $m$, suma el vector $n(-2, 2)$. ¿Cuál es el componente resultante?

> [!abstract] 🟡 Nivel Medio
> Realiza las siguientes restas de forma algebraica y verifica la dirección final de la flecha:
> 1. $p(1, -4) - n(-3, 3)$
> 2. $m(2, 4) - p(1, -4)$

> [!abstract] 🔴 Nivel Avanzado
> **Problema de Finanzas:** Un inversor tiene tres movimientos en su cartera representados por $v_1(10, 5)$, $v_2(-3, -2)$ y $v_3(1, -4)$.
> 1. Encuentra el vector resultante total sumando los tres movimientos.
> 2. Si el primer componente representa el dinero en $USD, ¿cuál es la ganancia neta o pérdida al final de las operaciones?

> [!success] ✅ Respuestas (para el docente)
> *   **Fácil:** 1. $(3, 6)$ | 2. $(1, 3)$ (El punto final gráfico será $(2, 4)$, pero el vector resultante mantiene sus componentes).
> *   **Medio:** 1. $(4, -7)$ | 2. $(1, 8)$
> *   **Avanzado:** 1. $(8, -1)$ | 2. Ganancia neta de $8 USD (el primer componente del resultante).

---

## Mini-prueba de autoevaluación

> [!question] Pregunta 1
> ¿Cambia el resultado si sumamos los vectores en orden distinto, por ejemplo $N + M$ en lugar de $M + N$?
> **Respuesta:** No. La suma de vectores es conmutativa. Aunque el "camino" visual sea diferente, el punto de partida y el punto de llegada final serán exactamente los mismos.

> [!question] Pregunta 2
> Si un vector $V$ tiene componentes $(5, 0)$, ¿cuál es su dirección?
> **Respuesta:** Es un vector puramente horizontal. Se mueve 5 unidades hacia la derecha y no tiene movimiento hacia arriba ni hacia abajo.

> [!question] Pregunta 3
> En una aplicación financiera, si una ganancia es $(+10, 0)$ y una pérdida es $(-5, 0)$, ¿cuál es el vector neto resultante?
> **Respuesta:** El vector neto es $(5, 0)$. Simplemente restamos el movimiento negativo del positivo en el eje horizontal del dinero.

---

## Notas para el próximo tema

> [!tip] 💡 Conexión
> Ahora que ya sabes dibujar vectores y sumarlos siguiendo el "camino" de sus componentes, en la siguiente lección descubriremos cómo medir el tamaño exacto de esa flecha final. Aprenderemos a calcular la **Magnitud o Módulo** del vector usando el Teorema de Pitágoras.

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | **Clase 02** | [[Clase 03|Clase 03 ➡]]