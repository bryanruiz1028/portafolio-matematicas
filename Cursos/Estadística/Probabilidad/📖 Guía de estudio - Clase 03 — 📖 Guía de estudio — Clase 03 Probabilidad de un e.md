# 📖 Guía de estudio — Clase 03: Probabilidad de un evento simple con DOS DADOS

> [!info] 📌 Conceptos clave
> ¡Prepárate para dominar el azar! Para convertirte en un experto en dados, primero debemos entender los **Axiomas de Probabilidad**, que son verdades tan lógicas que no necesitan demostración:
> 
> * **Regla de Laplace:** La probabilidad es una división entre los casos que te sirven (favorables) y el total de cosas que pueden pasar (casos posibles).
> * **Rango de probabilidad (Axioma 1):** La probabilidad de cualquier evento siempre es mayor o igual a $0$. ¡Ojo! Nunca verás una probabilidad negativa. Se expresa como $0 \leq P(A) \leq 1$.
> * **Espacio Muestral Seguro (Axioma 2):** La probabilidad de que ocurra *algo* dentro del espacio muestral ($S$) siempre es $1$. Es decir, $P(S) = 1$.
> * **Tamaño del espacio (2 dados):** Al lanzar dos dados, cada cara del primero ($6$) se combina con las del segundo ($6$), creando un total de $36$ combinaciones posibles.
> * **Eventos según su valor:**
> 	* **Imposible:** Su probabilidad es $0$. (Ej: que la suma sea $13$).
> 	* **Seguro:** Su probabilidad es $1$. (Ej: que la suma sea menor a $15$).
> 	* **Posible/Probable:** Su valor está entre $0$ y $1$.
> * **Sucesos mutuamente excluyentes:** ¡Como el agua y el aceite! Son eventos que no pueden ocurrir al mismo tiempo. Por ejemplo, al lanzar un dado, no puede salir un número **par** e **impar** a la vez.

---

## 2. Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Regla de Laplace** | $P(A) = \frac{\text{Casos Favorables}}{\text{Casos Posibles}}$ |
| **Espacio Muestral (2 dados)** | Son $36$ casos. Se calcula multiplicando las caras: $6 \times 6 = 36$. |
| **Evento Seguro** | $P(A) = 1$ ($100\%$ de certeza). |
| **Evento Imposible** | $P(A) = 0$ ($0\%$ de éxito). |
| **Evento Complementario** | La probabilidad de que un evento **NO** ocurra: $1 - P(A)$. |

---

## 3. Ejemplos Resueltos Adicionales

```ad-example
**Ejemplo A (Caso Básico): Suma igual a $4$**
* **Paso 1 (Identificar casos posibles):** Al lanzar dos dados, el total de combinaciones es $36$.
* **Paso 2 (Identificar casos favorables):** Buscamos las parejas que sumen exactamente $4$. Estas son: $(1,3), (2,2), (3,1)$. Tenemos $3$ casos.
* **Cálculo:** 
  $P(\text{Suma 4}) = \frac{3}{36}$
* **Simplificación:** Dividimos ambos entre $3$ para obtener $\frac{1}{12}$.
* **Resultado:** $0.083$ o **$8.3\%$**.
```

```ad-example
**Ejemplo B (Aplicación con $\$USD$): Feria Escolar**
Imagina que pagas $\$1 \text{ USD}$ para lanzar dos dados. Si la suma es $7$, ganas un premio.
* **Análisis:** Los casos favorables para sumar $7$ son $6$ parejas: $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)$.
* **Cálculo:** $P(\text{Suma 7}) = \frac{6}{36} = \frac{1}{6} \approx 0.166$.
* **Porcentaje:** **$16.6\%$**.
* **Dato Curioso:** Basado en el Axioma $P(S) = 1$, para que esta apuesta fuera "Segura" su probabilidad debería ser $1$ ($100\%$). Como $0.166 < 1$, existe un riesgo real de perder tu $\$1 \text{ USD}$. ¡No es un evento seguro!
```

---

## 4. Ejercicios de Repaso

```ad-abstract
**🟢 Nivel: Fácil**
1. Calcula la probabilidad de que ambos dados caigan en el mismo número (obtener un "par" como $1-1$, $2-2$, etc.).
2. ¿Cuál es la probabilidad de que la suma de los dados sea exactamente $2$?
3. Encuentra la probabilidad de obtener una suma mayor a $10$.
```

```ad-abstract
**🟡 Nivel: Medio**
1. Usando el **evento complementario** y el dato del Ejemplo B, calcula la probabilidad de que la suma **NO** sea $7$. (Fórmula: $1 - P(\text{Suma 7})$).
2. Calcula la probabilidad de que la suma sea un número par. *Pista: Mira la cuadrícula de estudio; verás un patrón de "ajedrez" con $18$ combinaciones favorables.*
3. ¿Cuál es la probabilidad de que el **primer dado** sea un $6$, sin importar lo que salga en el segundo?
```

```ad-abstract
**🔴 Nivel: Avanzado (Aplicación con $\$USD$)**
**El Misterio de los Dados Cargados:** Un dado tramposo ha sido modificado para que los números pares $(2, 4, 6)$ salgan el doble de veces que los impares $(1, 3, 5)$. 
* **Paso 1:** En este dado, los impares valen $1$ caso y los pares valen $2$. El nuevo total de casos para UN dado es $3 (\text{impares}) + 6 (\text{pares}) = 9$.
* **Reto de Síntesis:** Si lanzas **DOS** dados cargados de la misma forma, ¿cuál es el nuevo total del espacio muestral? (Recuerda multiplicar los casos posibles de cada dado: $9 \times 9$).
* **Problema:** Si ganas $\$5 \text{ USD}$ si la suma de dos dados cargados es "2" (solo cae $1-1$), ¿cuál es la nueva probabilidad de ganar?
```

---

## 5. Consejo de Estudio

> [!tip] 💡 La Cuadrícula Mágica
> Para no perderte nunca, dibuja siempre una **cuadrícula de $6 \times 6$**. 
> * Escribe los números del $1$ al $6$ en la fila superior (Dado 1) y en la columna izquierda (Dado 2).
> * Al rellenar los cuadros, verás las $36$ combinaciones. 
> * **¡Truco visual!** Las sumas iguales siempre forman diagonales, y los números pares/impares crean un patrón de tablero de ajedrez. Esto te ayudará a contar casos favorables sin olvidar ninguno. ¡Es la técnica infalible!