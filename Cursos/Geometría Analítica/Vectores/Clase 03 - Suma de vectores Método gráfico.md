# Clase 03 — Suma de vectores: Método gráfico

#algebra #vectoradditionu
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 6

> [!info] 🧭 Navegación
> - ← Clase anterior: [[Clase 02 — Representación de vectores en el plano]]
> - 🏠 Índice: [[00 - Índice del curso]]
> - → Siguiente clase: [[Clase 04 — Suma de vectores por componentes rectangulares]]

---

> [!info] 🌍 Relevancia y aplicaciones
> La suma de vectores permite determinar el efecto neto de múltiples fuerzas o desplazamientos que actúan sobre un mismo punto, permitiendo predecir resultados finales en sistemas complejos.
> - 💵 **Aplicación USD:** Visualizar flujos de capital como vectores (ingresos y egresos con distintas "direcciones" financieras) para determinar el saldo neto de una cuenta.
> - 🏗️ **Construcción:** Calcular la tensión resultante en los cables de acero que sostienen el brazo de una grúa torre.
> - 📊 **Cotidiano:** Estimar la posición final de un barco sumando el vector de propulsión de su motor y el vector de arrastre de la corriente marina.

---

> [!note] 📌 ¿Qué es Vector Addition Using the Graphical Method? (Suma de Vectores por el Método Gráfico)
> Es un procedimiento geométrico conocido como el método de "cabeza y cola". Para estudiantes, podemos imaginarlo como un **"caminito"**: dibujamos el primer vector y, justo donde termina su flecha, comenzamos a dibujar el siguiente. El resultado final es la línea recta que une el punto de partida inicial con el destino final.

> [!warning] ⚠️ Error común
> Un error frecuente es intentar dibujar todos los vectores naciendo desde el origen (0,0) al mismo tiempo. **¡Cuidado!** Si haces esto, no estás sumando, solo estás graficando vectores aislados. Para sumar, cada vector nuevo debe "nacer" donde terminó el anterior.

> [!tip] 💡 Truco para recordarlo: El "Tren de Vectores"
> Imagina que cada vector es un vagón de tren. Para que el tren funcione, debes enganchar el inicio del segundo vagón al final (la cola) del primero. El **Vector Resultante** es el riel que va directo desde la estación de salida hasta el final del último vagón enganchado.

---

### 4. Procedimiento Paso a Paso

Para obtener resultados precisos, utiliza regla y transportador siguiendo este algoritmo técnico:

```text
PASO 1 → Dibujar el primer vector desde el origen del plano cartesiano respetando su magnitud (escala) y su ángulo exacto.
PASO 2 → Colocar un origen "mental" (ejes auxiliares suaves) en la punta (flecha) del vector anterior. Dibujar el siguiente vector desde ahí.
PASO 3 → Trazar el "Vector Resultante" (o Suma) desde el inicio del primer vector hasta la punta del último vector dibujado.
PASO 4 → Medir con regla la magnitud del resultante y con transportador su ángulo. Aplicar la escala inversa para obtener el valor real (metros, USD, etc.).
```

> [!tip] 💡 Nota sobre los ejes cardinales
> Si un vector apunta exactamente al **Norte, Sur, Este u Oeste**, no necesitas el transportador para iniciar su trazo; simplemente sigue las líneas de tu cuadrícula o los ejes del plano.

---

### 5. Ejemplos Desarrollados

> [!example] Ejemplo 1: Suma básica (Basado en Video 1)
> **Vectores:** A (3m, E 30° N) y B (4m, E 73° N).
> - **Proceso:** Dibujamos A desde el origen. En su punta, imaginamos un nuevo eje y medimos 73° desde el Este hacia el Norte para trazar B.
> - **Resultado:** Al medir el vector resultante, obtenemos una magnitud de **~6.5m** con una dirección de **E 54° N**.

> [!example] Ejemplo 2: Cambio de dirección y precisión (Basado en Video 2)
> **Vectores:** A (5m, N 20° E) y B (6m, O 40° S).
> - **Nota técnica:** Al graficar B, el transportador debe orientarse desde el Oeste hacia el Sur (hacia abajo). Es vital no confundir los cuadrantes al rotar el instrumento en el origen "mental".
> - **Resultado:** El vector resultante mide aproximadamente **3m** y su dirección es **O 17° N**.

> [!example] Ejemplo 3: Suma de 3 vectores (Basado en Video 3)
> **Vectores:** A (4m, O 32° N), B (5m, S 15° E) y C (3m, E 20° N).
> - **Proceso:** Se encadenan los tres vectores: A → B → C. El resultante une el inicio de A con el final de C.
> - **Resultado:** La magnitud es de **~1.6m** con una dirección de **E 66° S**.

> [!example] Ejemplo 4: Aplicación Financiera USD (Basado en Video 4)
> **Situación:** Un inversor gestiona capital (Escala: 1m = 100 USD). Realiza tres movimientos: 400 USD al Sureste (45°), 600 USD al Norte, y 820 USD al S 55° O.
> - **Cálculo:** Se grafican vectores de 4u, 6u y 8.2u siguiendo el "caminito".
> - **Resultado:** El vector suma es de 4.1 unidades. El saldo neto final es de **~410 USD** con dirección **O 21° S**.

---

### 6. Ejercicios Prácticos

> [!abstract] 🟢 Nivel Verde: Básico (2 vectores)
> 1. Suma A (2m, Norte) + B (3m, Este).
> 2. Suma A (4m, E 45° N) + B (4m, O 45° N).
> 3. Suma A (5m, Sur) + B (2m, Este).
> 4. Suma A (3m, Oeste) + B (3m, Norte).

> [!abstract] 🟡 Nivel Amarillo: Medio (3 vectores)
> 1. A (5m, N 30° O) + B (3m, S 20° E) + C (2m, Norte).
> 2. A (6m, E 15° S) + B (4m, O 40° N) + C (5m, Sur).
> 3. A (3m, Este) + B (5m, N 10° E) + C (4m, O 20° S).
> 4. A (4.2m, O 74° S) + B (7.5m, N 20° O). *(Nota: Solo 2 vectores, pero con ángulos complejos).*

> [!abstract] 🔴 Nivel Rojo: Desafío Financiero USD (Escala 1m = 100 USD)
> 1. **Saldo A:** Ingreso 500 USD (Norte), Gasto 300 USD (E 30° S), Inversión 400 USD (Sur).
> 2. **Saldo B:** Flujo 700 USD (O 45° S), Ingreso 200 USD (Este), Flujo 500 USD (N 20° E).
> 3. **Saldo C:** Movimiento 1000 USD (Sureste 45°), Retiro 500 USD (Oeste), Ingreso 300 USD (Norte).
> 4. **Saldo D:** Inversión 450 USD (N 60° E), Gasto 300 USD (S 15° O), Pago 200 USD (Oeste).

> [!success] Soluciones para el Docente (Valores aproximados)
> *Margen de error aceptable: ±0.2 unidades y ±3°.*
> - **V1:** 3.6m, E 34° N | **V2:** 5.6m, Norte | **V3:** 5.4m, E 68° S | **V4:** 4.2m, O 45° N.
> - **A1:** ~4.3m, O 72° N | **A2:** ~5.2m, E 75° S | **A3:** ~4.1m, E 12° N | **A4:** ~4.7m, O 39° N.
> - **R1:** ~320 USD, E 15° S | **R2:** ~360 USD, O 65° S | **R3:** ~410 USD, O 21° S | **R4:** ~280 USD, N 35° E.

---

### 7. Autoevaluación y Cierre

> [!question] Pregunta Conceptual
> **Si sumas un vector de 10m y otro de 10m, ¿el resultado puede ser cero?**
> - **Respuesta:** Sí. Si el primer vector va al Este y el segundo al Oeste (direcciones opuestas), el "caminito" te devuelve exactamente al punto de origen.

> [!question] Pregunta Procedimental
> **¿Qué función cumple el origen "mental" en el segundo vector?**
> - **Respuesta:** Sirve como marco de referencia para colocar el transportador correctamente y medir el ángulo desde la "punta" del vector anterior, manteniendo la orientación del plano original.

> [!question] Pregunta de Aplicación USD
> **En el sistema de vectores financieros, ¿qué representa el "Vector Resultante"?**
> - **Respuesta:** Representa el **Saldo Neto**. Es la magnitud y dirección final del capital después de considerar todos los movimientos de ingresos y egresos.

> [!tip] 💡 En la próxima clase
> El método gráfico es excelente para visualizar, pero depende de tu precisión con la regla. En la **Clase 04**, aprenderemos el **Método de Componentes Rectangulares**, que nos permite obtener resultados exactos usando trigonometría.

---
> [!info] 🧭 Navegación
> - ← Clase anterior: [[Clase 02 — Representación de vectores en el plano]]
> - 🏠 Índice: [[00 - Índice del curso]]
> - → Siguiente clase: [[Clase 04 — Suma de vectores por componentes rectangulares]]