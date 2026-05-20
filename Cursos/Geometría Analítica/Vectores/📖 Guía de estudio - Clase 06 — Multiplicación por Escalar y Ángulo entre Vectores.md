# 📖 Guía de estudio — Clase 06: Multiplicación de un Vector por un Escalar

> [!info] **Conceptos Clave**
> *   **Escalar:** Es un número real (positivo, negativo, decimal o fracción) que se utiliza para multiplicar un vector.
> *   **Resultado de la operación:** Al realizar el producto, el resultado es siempre **otro vector**.
> *   **Efecto en la magnitud:** El escalar altera el largo del vector:
>     *   Si el valor absoluto del escalar es mayor a uno ($|k| > 1$), el vector **se alarga**.
>     *   Si el valor absoluto es una fracción o decimal entre cero y uno ($0 < |k| < 1$), el vector **se acorta**.
> *   **Dirección y Sentido:**
>     *   La **dirección** (la línea de inclinación) se mantiene invariable.
>     *   Si el escalar es **positivo**, el vector resultante conserva el mismo **sentido**.
>     *   Si el escalar es **negativo**, el vector resultante cambia al **sentido opuesto** (se invierte 180°).

---

### Sección: Fórmulas y definiciones importantes

| Concepto | Definición Operativa |
| :--- | :--- |
| **Escalar ($k$)** | Número real que multiplica al vector para modificar su magnitud y/o sentido. |
| **Producto por componentes** | Se multiplica el escalar por cada una de las componentes del vector: $k \cdot \vec{v}(x, y) = (k \cdot x, k \cdot y)$. |
| **Producto con coordenadas geográficas** | Se multiplica el valor absoluto del escalar por la magnitud: $|k| \cdot \text{magnitud}$. **Regla de Oro:** La magnitud final siempre debe ser positiva. Si $k < 0$, el signo negativo se "absorbe" invirtiendo los puntos cardinales (N $\leftrightarrow$ S, E $\leftrightarrow$ O). |

---

### Sección: Ejemplos resueltos adicionales

> [!ad-example] **Ejemplo A — Caso básico por componentes**
> **Problema:** Multiplicar el vector $\vec{v} = (3, 2)$ por el escalar $k = 2$.
> 
> **Procedimiento:**
> 1. Multiplicar la componente $x$ por el escalar: $2 \times 3 = 6$.
> 2. Multiplicar la componente $y$ por el escalar: $2 \times 2 = 4$.
> 
> **Resultado:** El vector resultante es $(6, 4)$. 
> *Nota pedagógica: Gráficamente, el nuevo vector es una extensión del original, conservando su inclinación pero con el doble de longitud.*

> [!ad-example] **Ejemplo B — Coordenadas geográficas y escalar negativo**
> **Problema:** Multiplicar el vector $\vec{v} = 3\text{m Sur } 30^\circ \text{ Oeste}$ por el escalar $k = -2$.
> 
> **Procedimiento:**
> 1. **Multiplicar la magnitud:** Usamos el valor absoluto del escalar $|-2| \times 3\text{m} = 6\text{m}$.
> 2. **Invertir el sentido:** Como el escalar es negativo, cambiamos los puntos cardinales a sus opuestos:
>    *   **Sur** se convierte en **Norte**.
>    *   **Oeste** se convierte en **Este**.
> 3. El ángulo ($30^\circ$) no sufre cambios.
> 
> **Resultado:** $\vec{v}_{res} = 6\text{m Norte } 30^\circ \text{ Este}$.

---

### Sección: Ejercicios de repaso

> [!ad-abstract] **Práctica Sugerida**
> 
> **🟢 Nivel Fácil**
> 1. Si el vector $\vec{v}$ tiene una magnitud de $12\text{m}$, determine la magnitud resultante de la operación $5 \cdot \vec{v}$.
> 2. Calcule el producto por componentes: $7 \cdot (-5, 3)$.
> 
> **🟡 Nivel Medio**
> 3. Encuentre las componentes del vector resultante al multiplicar el escalar $-4$ por el vector $\vec{v} = (-5, -7)$. *Recuerde aplicar la ley de signos en cada componente.*
> 
> **🔴 Nivel Avanzado**
> 4. Calcule el producto del escalar $-4$ por el vector $\vec{v} = 15\text{m Suroeste}$.
>    *   *Instrucción:* Exprese el resultado con magnitud positiva. 
>    *   *Pista pedagógica:* Recuerde que "Suroeste" es la combinación de Sur y Oeste; para obtener el sentido opuesto, debe invertir ambos puntos cardinales (Sur $\to$ Norte, Oeste $\to$ Este).

---

> [!ad-tip] **Consejo de estudio**
> Para validar tus resultados, realiza siempre un **bosquejo gráfico rápido**. Un vector multiplicado por un escalar debe "descansar" sobre la misma línea recta que el vector original (misma dirección). Si tu escalar fue negativo y tu flecha resultante no apunta exactamente en sentido contrario al original, revisa tu aplicación de los puntos cardinales o los signos de las componentes.