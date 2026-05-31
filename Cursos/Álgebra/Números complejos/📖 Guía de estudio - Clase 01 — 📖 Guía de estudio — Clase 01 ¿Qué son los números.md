# 📖 Guía de estudio — Clase 01: ¿Qué son los números imaginarios?

> [!info] 📌 Conceptos clave
> ¡Bienvenido al fascinante mundo de los números imaginarios! Estos surgen para dar respuesta a operaciones que antes considerábamos "imposibles", como las raíces cuadradas de números negativos.
> 
> *   **La Unidad Imaginaria:** Se define universalmente como $i = \sqrt{-1}$.
> *   **Un poco de historia:** El término "imaginario" fue acuñado originalmente por **René Descartes** de forma despectiva, sugiriendo que estos números no existían realmente. Fue **Leonhard Euler** quien, años más tarde, formalizó su uso otorgándoles el símbolo $i$.
> *   **Propiedad Fundamental:** El corazón de este concepto es que $i^2 = -1$. Es el único número que, al elevarse al cuadrado, resulta en un valor negativo.
> *   **Ciclo Infinito:** Las potencias de $i$ no crecen infinitamente; se repiten en un ciclo de cuatro resultados específicos ($1, i, -1, -i$).
> *   **¡Adiós a los imposibles!:** Para resolver raíces negativas, usamos la regla: $\sqrt{-n} = \sqrt{n} \cdot i$. Así, transformamos una raíz "inexistente" en un número real acompañado de la unidad imaginaria.

---

## 2. Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Unidad Imaginaria** | $i = \sqrt{-1}$ |
| **Potencia Cuadrática** | $i^2 = -1$ |
| **Potencia Cúbica** | $i^3 = -i$ |
| **Potencia Cuarta** | $i^4 = 1$ (Nota: equivale a reiniciar el ciclo como $i^0$) |
| **Números Imaginarios Puros** | Producto de un número real $b$ por la unidad imaginaria $i$ ($b \cdot i$) |

---

## 3. Ejemplos Resueltos Adicionales

> [!example] Ejemplo A: Dominando potencias grandes
> **Enunciado:** Hallar el valor exacto de $i^{85}$.
> 
> **Paso a paso:**
> 1.  **División por el ciclo:** Como el ciclo se repite cada $4$, dividimos el exponente entre $4$.
>     $85 \div 4 = 21$ con un **residuo de $1$**.
> 2.  **El secreto del residuo:** El residuo de la división se convierte en nuestro nuevo exponente. Esto es porque $i^{85}$ da las mismas vueltas al ciclo que $i^1$.
>     $i^{85} = i^1$
> 3.  **Resultado final:** Según nuestras potencias básicas, $i^1 = i$.
>     **Resultado:** $i$

> [!example] Ejemplo B: Aplicación en balance contable ($USD)
> **Enunciado:** Representar matemáticamente la raíz cuadrada de un déficit (pérdida) financiero de $100 USD.
> 
> **Resolución:**
> Un déficit de $100 USD se expresa contablemente como $-100$. Para extraer su raíz:
> $\sqrt{-100} = \sqrt{100} \cdot \sqrt{-1} = 10i$
> 
> **Interpretación Pedagógica:** El resultado es `$10i$ USD`. Aquí, el número `$10$` representa la **magnitud** de la cifra, mientras que la `$i$` actúa como un **marcador cualitativo**. La `$i$` nos indica que estamos ante una operación "imaginaria" o no real, ya que en el mundo físico no podemos extraer raíces de balances negativos de forma ordinaria.

---

## 4. Ejercicios de Repaso (¡Pon a prueba lo aprendido!)

> [!abstract] 🟢 Bloque: Fácil
> Determina el valor simplificado de las siguientes potencias:
> 1.  $i^0$
> 2.  $i^{52}$
> 3.  $i^3$

> [!abstract] 🟡 Bloque: Medio
> Resuelve las siguientes sumas y restas transformando primero a unidades imaginarias:
> 1.  $\sqrt{-36} + \sqrt{-9}$
> 2.  $4i - 8i$
> 3.  $\sqrt{-16} - \sqrt{-49}$

> [!abstract] 🔴 Bloque: Avanzado (Aplicación financiera)
> Un analista financiero reporta dos "pérdidas cuadráticas" representadas por los valores $\sqrt{-25}$ USD y $\sqrt{-64}$ USD. 
> **Reto:** Calcula la suma total de ambas pérdidas. 
> *Pista del Profe Alex:* Al sumar los resultados, trata a la `$i$` como un **factor común** para obtener el resultado final consolidado en términos de $i$.

---

## 5. Estrategia de Dominio

> [!tip] 💡 Consejo de estudio: El Truco del Plano Cartesiano
> Para no depender de la memoria, visualiza el ciclo de potencias como giros de 90° en el plano de números complejos:
> 
> *   **Punto de partida:** Ubica el `$1$` a la derecha (Eje X positivo). Esto es $i^0$.
> *   **Primer giro (90° antihorario):** Llegas arriba, donde ubicas a `$i$`. Esto es $i^1$.
> *   **Segundo giro (180° total):** Llegas a la izquierda, donde está el `$-1$`. Esto es $i^2$.
> *   **Tercer giro (270° total):** Llegas abajo, donde ubicas a `$-i$`. Esto es $i^3$.
> *   **Cuarto giro (360° total):** Regresas al inicio en `$1$`. Esto es $i^4$.
> 
> ¡Basta con imaginar el giro para recordar que el ciclo siempre es $1 \rightarrow i \rightarrow -1 \rightarrow -i$!