# Clase 02 — Suma, Resta y Multiplicación de Ángulos

#algebra #sumadeangulos #matematicas

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 2

> [!info] 🧭 Navegación
> - **Anterior:** [[Clase 01 — Introducción al Sistema Sexagesimal]]
> - **Siguiente:** [[Clase 03 — Geometría: Uso del Transportador]]

---

### 🌍 Relevancia y aplicaciones
¡Hola, equipo! Dominar el sistema sexagesimal no es solo para el examen; es la clave para la **astronomía y la navegación marítima o aérea**. En estas disciplinas, un error de un solo segundo de arco puede desviar un barco o un satélite cientos de kilómetros de su destino.

*   **💵 Aplicación con $USD:** En finanzas de alta precisión, como el cálculo de intereses por segundo o comisiones por tiempo de uso de procesadores, se opera primero en base 60 para mantener la exactitud total. Solo al final se convierte el tiempo total a valor monetario para evitar perder centavos por redondeos decimales tempranos.
*   **🏗️ Aplicación práctica:** En arquitectura avanzada, sumar ángulos con precisión de segundos asegura que las estructuras masivas sean estables y que las piezas encajen sin tensión excesiva.
*   **📊 Situación cotidiana:** Cada vez que sumas cuánto duran tus canciones favoritas o calculas el tiempo total de una rutina deportiva usando un reloj analógico, estás aplicando estas mismas reglas.

---

### 📌 ¿Qué es Suma de ángulos?
> [!note] Definición
> Sumar ángulos es agrupar grados ($^\circ$), minutos ($'$) y segundos ($''$) en columnas separadas. Al igual que en las sumas normales, "llevamos" unidades al vecino, pero con una gran diferencia: **Base 60**. Esto significa que 60 unidades de una columna forman exactamente 1 unidad de la columna superior.
> 
> **Nota sobre signos:** Si ambos ángulos son negativos (ej. $-10^\circ$ y $-5^\circ$), realizamos una suma normal y mantenemos el signo negativo en el resultado. ¡Los signos iguales siempre se suman!

> [!warning] ⚠️ Error común
> **¡Cuidado con la trampa decimal!** Nunca sumes ángulos como si fueran números decimales (base 10). 
> *   ❌ **Error:** $10^\circ 50' + 10^\circ 20' = 20^\circ 70'$ (Esto no es la respuesta final).
> *   ✅ **Correcto:** $50' + 20' = 70'$. Como 70 supera 60, se convierte en $1^\circ 10'$. Resultado: $21^\circ 10'$.

> [!tip] 💡 Truco para recordarlo: "La frontera del 60"
> El número 60 es la frontera. Si tus minutos o segundos llegan a 60 o más, debes "regalar" unidades al vecino de la izquierda y quedarte solo con el sobrante.

---

### 🛠️ Procedimiento paso a paso

Para operar con éxito, sigue esta estructura lógica. Para los ajustes de sumas y multiplicaciones, usa la **Tabla de Múltiplos de 60** ($60, 120, 180, 240, 300\dots$) para saber cuánto "regalar".

```text
PASO 1 → Alineación: Escribir los ángulos en columnas verticales 
          (grados con grados, minutos con minutos, segundos con segundos).
PASO 2 → Operación: Sumar, restar o multiplicar cada columna 
          de forma independiente (de derecha a izquierda).
PASO 3 → Ajuste (Conversión):
          - Suma/Mult: Si una columna tiene 60 o más, resta el múltiplo 
            de 60 más cercano y suma esas unidades al vecino izquierdo.
          - Resta: Si el número superior es menor al inferior, pide 
            prestado "1" al vecino, que se convierte en "60" en tu columna.
PASO 4 → Simplificación: Escribir la respuesta final asegurando que 
          minutos y segundos estén entre 0 y 59.
```

---

### 📝 Ejemplos de Aplicación

#### Ejemplo 1: Suma Básica (Sin conversión)
**Sumar:** $10^\circ 20' 32'' + 25^\circ 12' 14''$
1.  **Segundos:** $32'' + 14'' = 46''$
2.  **Minutos:** $20' + 12' = 32'$
3.  **Grados:** $10^\circ + 25^\circ = 35^\circ$
*   **Resultado:** $35^\circ 32' 46''$ (No hay ajustes porque nada llegó a 60).

#### Ejemplo 2: Resta con Préstamo
**Restar:** $10^\circ 20' 15'' - 7^\circ 12' 30''$
1.  **Segundos:** A $15''$ no puedo quitarle $30''$. Los minutos le prestan $1'$ (que son $60''$).
2.  **Ajuste:** El $20'$ queda en $19'$. Los $15''$ reciben $60''$ y se vuelven $75''$.
3.  **Operación:** 
    *   $75'' - 30'' = 45''$
    *   $19' - 12' = 7'$
    *   $10^\circ - 7^\circ = 3^\circ$
*   **Resultado:** $3^\circ 7' 45''$

#### Ejemplo 3: Multiplicación Avanzada (Uso de múltiplos)
**Multiplicar:** $40^\circ 15' 25'' \times 6$
1.  **Operar cada columna:** $240^\circ \quad 90' \quad 150''$
2.  **Ajustar Segundos:** En $150''$, el múltiplo de 60 más cercano es $120$ ($60 \times 2$).
    *   $150'' - 120'' = 30''$ restantes.
    *   Esos $120''$ pasan como **$2'$** a la columna de minutos.
3.  **Ajustar Minutos:** Ahora tenemos $90' + 2' = 92'$. El múltiplo más cercano es $60$ ($60 \times 1$).
    *   $92' - 60' = 32'$ restantes.
    *   Ese $60'$ pasa como **$1^\circ$** a la columna de grados.
4.  **Ajustar Grados:** $240^\circ + 1^\circ = 241^\circ$.
*   **Resultado Final:** $241^\circ 32' 30''$

#### Ejemplo 4: Aplicación Real $USD
**Problema:** Un motor cobra $1 USD por cada grado de giro completo. Si sumamos tres movimientos: $15^\circ 20'$, $10^\circ 10'$ y $5^\circ 30'$, ¿cuál es el costo?
1.  **Suma de columnas:** $30^\circ$ y $60'$.
2.  **Ajuste:** $60'$ es exactamente $1^\circ$. Sumamos: $30^\circ + 1^\circ = 31^\circ 00'$.
*   **Costo:** $31^\circ \times \$1 = \$31 USD$.

---

### ✍️ Ejercicios para el Estudiante

**🟢 Nivel Fácil (Operaciones Directas)**
1. $12^\circ 15' 10'' + 10^\circ 10' 20''$
2. $45^\circ 30' 50'' - 20^\circ 10' 30''$
3. $5^\circ 25' + 3^\circ 15'$
4. $100^\circ 45'' - 50^\circ 20''$

**🟡 Nivel Medio (Préstamos y Multiplicación)**
> [!info] Nota para expertos
> Si tienes que restar y la columna de minutos o segundos tiene ceros ($00'$), debes pedir prestado primero a los grados para "llenar" los minutos, y luego de esos minutos prestar a los segundos.

1. $25^\circ 10' 15'' \times 3$
2. $15^\circ 20' 05'' - 8^\circ 30' 10''$
3. $40^\circ 45' \times 2$
4. $12^\circ 00' 00'' - 5^\circ 10' 30''$ (¡Usa el préstamo doble!)

**🔴 Nivel Avanzado (Problemas del Mundo Real)**
1. Un satélite gira $15^\circ 20'$ cada hora. ¿Cuánto ha girado tras 5 horas de órbita?
2. Si el combustible del satélite cuesta $2.50 USD por cada grado completo de giro, ¿cuál es el costo total por las 5 horas? (Usa solo la parte entera de los grados).
3. Resuelve la operación mixta: $(10^\circ 40' 20'' \times 2) + 5^\circ 50' 50''$.
4. Un mecanismo rota $-90^\circ 30'$ y luego rota en el mismo sentido otros $-10^\circ 30'$. ¿Cuál es su posición final y la distancia total (valor absoluto) recorrida?

#### ✅ Respuestas
*   **Fácil:** 1) $22^\circ 25' 30''$ | 2) $25^\circ 20' 20''$ | 3) $8^\circ 40'$ | 4) $50^\circ 25''$.
*   **Medio:** 1) $75^\circ 30' 45''$ | 2) $6^\circ 49' 55''$ | 3) $81^\circ 30'$ | 4) $6^\circ 48' 30''$.
*   **Avanzado:** 1) $76^\circ 40'$ | 2) $190 USD$ ($76 \times 2.5$) | 3) $27^\circ 11' 30''$ | 4) Posición: $-101^\circ 00'$; Distancia total: $101^\circ$.

---

### 🧪 Mini-Prueba de Autoevaluación

1.  **Conceptual:** Si al sumar segundos el resultado es $130''$, ¿cuántos minutos pasas al vecino y cuántos segundos te quedan?
    *   *Respuesta: Pasas 2 minutos ($120''$) y te quedan $10''$.*
2.  **Procedimental:** En la resta $20^\circ 10' - 5^\circ 40'$, ¿cómo queda la fila superior tras pedir prestado?
    *   *Respuesta: Queda como $19^\circ 70'$.*
3.  **Aplicación $USD:** Un sensor cobra $0.50 USD por cada minuto de arco ($'$) girado. Si giras $1^\circ 10'$, ¿cuál es el costo total?
    *   *Respuesta: $1^\circ 10' = 70'$. Entonces $70 \times 0.50 = \$35 USD$.*

---

> [!tip] 💡 En la próxima clase
> Ya dominas los números. En la siguiente sesión, sacaremos las reglas y el transportador para ver cómo estos cálculos se transforman en dibujos geométricos perfectos.

> [!info] 🧭 Navegación
> - **Anterior:** [[Clase 01 — Introducción al Sistema Sexagesimal]]
> - **Siguiente:** [[Clase 03 — Geometría: Uso del Transportador]]