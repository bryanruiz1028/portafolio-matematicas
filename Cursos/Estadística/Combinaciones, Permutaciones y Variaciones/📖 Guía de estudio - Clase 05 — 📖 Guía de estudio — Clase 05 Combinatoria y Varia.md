# 📖 Guía de estudio — Clase 05: Combinatoria y Variación en Placas Vehiculares

> [!info] 📌 Conceptos clave
> Para dominar el arte de contar posibilidades sin marearte en el intento, debes basarte en estos pilares fundamentales que nos enseña el **Profe Alex**:
> * **¿Importa el orden?**: Es la pregunta de oro. Si al cambiar los elementos el resultado es "otro" (como en una placa: A-B no es lo mismo que B-A), es **Variación**. Si el resultado es el mismo (como un grupo de amigos), es **Combinación**.
> * **Beneficio o Rol**: ¡Ojo aquí! Si todos los seleccionados reciben el mismo premio o hacen lo mismo, el orden **no** importa.
> * **Repetición**: Determina si puedes usar un elemento más de una vez (ej. pedir dos bolas de helado del mismo sabor).
> * **Método de las "Cajitas"**: Es nuestra mejor herramienta visual para aplicar el Principio de Multiplicación. Cada casilla es una decisión y dentro anotamos nuestras opciones.

---

## 2. TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Combinación sin repetición** | Selección de un subgrupo donde **no importa el orden** y los elementos no se pueden repetir.<br>$$C(n,r) = \frac{n!}{r!(n-r)!}$$ |
| **Combinación con repetición** | Selección donde **no importa el orden**, pero puedes elegir el mismo elemento varias veces (como los helados).<br>$$CR(n,r) = \frac{(n+r-1)!}{r!(n-1)!}$$ |
| **Variación con repetición** | Sí importa el orden y los elementos pueden repetirse (el modelo clásico de las placas).<br>$$V_R(n,r) = n^r$$ |
| **Principio de Multiplicación (Cajitas)** | Si un evento ocurre en pasos sucesivos, multiplicas las opciones de cada paso.<br>`|_opc1_| × |_opc2_| × |_opc3_|` |

---

## 3. EJEMPLOS RESUELTOS

> [!example] Ejemplo A — Selección de estudiantes
> **Enunciado:** Un profesor debe elegir a 4 estudiantes de un grupo de 10 para invitarlos a un almuerzo. ¿De cuántas formas puede hacerlo?
> 
> **Pasos:**
> 1. **Análisis de la situación:** ¿Importa el orden? **No.** Como todos los elegidos reciben el mismo premio (el almuerzo), el grupo {Juan, Ana} es igual al grupo {Ana, Juan}. 
> 2. **Identificar datos:** $n=10$ (total), $r=4$ (seleccionados). Es una **Combinación sin repetición**.
> 3. **Aplicación de la fórmula:**
>    $$C(10,4) = \frac{10!}{4!(10-4)!} = \frac{10!}{4! \times 6!}$$
> 4. **Simplificación (truco del Profe Alex):** Reducimos el 10! hasta llegar al 6! para cancelar:
>    $$\frac{10 \times 9 \times 8 \times 7 \times \cancel{6!}}{ (4 \times 3 \times 2 \times 1) \times \cancel{6!}} = \frac{5040}{24} = 210$$
> 
> **Resultado:** ✅ Existen **210 formas** diferentes de elegir al grupo.

> [!example] Ejemplo B — Placas de automóvil y costos de registro
> **Enunciado:** Calcula cuántas placas de 3 letras (26 opciones) y 3 dígitos (10 opciones) existen. Si cada registro genera **$15 USD** para el municipio, ¿cuál es el ingreso total?
> 
> **Pasos:**
> 1. **Visualización (Método de las cajitas):**
>    Letras: `|_26_| |_26_| |_26_|`  →  $26^3 = 17,576$ variaciones.
>    Dígitos: `|_10_| |_10_| |_10_|`  →  $10^3 = 1,000$ variaciones.
> 2. **Cálculo Total (Principio de Multiplicación):**
>    Para unir letras y dígitos, multiplicamos ambos resultados:
>    $17,576 \times 1,000 = 17,576,000$ placas posibles.
> 3. **Análisis Financiero:**
>    Multiplicamos el total por el costo unitario ($15 USD):
>    $17,576,000 \times 15 = 263,640,000$.
> 
> **Resultado:** ✅ Se pueden crear **17,576,000 placas** con un ingreso de **$263,640,000 USD**.

---

## 4. EJERCICIOS DE REPASO

> [!abstract] Nivel Verde (Fácil)
> 1. Tienes 6 sabores de gaseosa y debes elegir 3 diferentes para una fiesta. ¿Cuántas combinaciones puedes armar?
> 2. De un grupo de 8 atletas, se deben elegir 2 para un control antidopaje. ¿De cuántas formas se seleccionan?
> 3. Tienes 5 colores de pintura y quieres mezclar solo 2. ¿Cuántas mezclas únicas existen?

> [!abstract] Nivel Amarillo (Medio)
> 1. **El caso del helado:** Una heladería tiene 7 sabores. ¿Cuántos helados de 3 bolas puedes pedir si te dejan repetir sabores?
> 2. **Restricción de placa:** ¿Cuántas placas de 3 letras y 3 dígitos existen si la primera letra DEBE ser la "A"? 
>    *(💡 Pista: En la primera cajita de letras solo tienes 1 opción: `|_1_| |_26_| |_26_|`).*
> 3. Si una placa debe empezar con la letra "B" y el primer dígito debe ser siempre "0", ¿cuántas placas totales se pueden emitir?

> [!abstract] Nivel Rojo (Avanzado)
> 1. **Reto Presupuestario:** Una ciudad decide registrar solo el **10%** de todas las placas posibles de 3 letras y 3 dígitos que cumplan una condición: **el último dígito debe ser par** (0, 2, 4, 6, 8). Si el costo de registro es de **$25 USD** por placa, ¿cuál será el ingreso total recaudado?

---

## 5. CONSEJO DE ESTUDIO

> [!tip] 💡 Las dos preguntas mágicas
> Antes de rayar el cuaderno con números, respira y pregúntate:
> 1. **¿Importa el orden?** (Si cambio el lugar, ¿cambia el significado?).
> 2. **¿Se puede repetir?** (¿Puedo usar el mismo elemento dos veces?).
> 
> Si respondes esto, ya tienes el 80% del ejercicio resuelto. ¡Tú puedes, genio!

---

### 🔑 Clave de Respuestas (Auto-verificación)
*   **Nivel Verde:** 1) 20 combinaciones | 2) 28 formas | 3) 10 mezclas.
*   **Nivel Amarillo:** 1) 84 helados ($CR(7,3)$) | 2) 676,000 placas | 3) 67,600 placas.
*   **Nivel Rojo:** 1) $21,970,000 USD.
    *(Cálculo: $26^3 \times 10 \times 10 \times 5 \text{ (pares)} = 8,788,000 \text{ placas totales}$. El 10% son $878,800$ placas $\times 25$ USD).*