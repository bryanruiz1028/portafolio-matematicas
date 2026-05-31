# 📖 Guía de estudio — Clase 09: Diagramas de Árbol

> [!info] 📌 Conceptos clave
> Un **Diagrama de Árbol** es una representación gráfica que nos permite visualizar de forma organizada todos los resultados posibles de un experimento aleatorio. Es la herramienta ideal para eventos que ocurren en pasos sucesivos.
> 
> *   **La Regla de la Unidad:** En cualquier punto donde nacen ramificaciones, la suma de las probabilidades de todas esas ramas debe ser siempre igual a $1$ (o al $100\%$).
> *   **Regla de la Multiplicación (Intersección):** Para hallar la probabilidad de un camino específico (evento $A$ **y** luego evento $B$), multiplicamos las probabilidades de sus ramas. Matemáticamente, multiplicamos la probabilidad del segundo evento dado que el primero ya ocurrió: $P(A \cap B) = P(A) \cdot P(B|A)$.
> *   **Regla de la Suma (Unión):** Cuando buscamos la probabilidad de varios resultados finales que cumplen una condición (evento $X$ **o** evento $Y$), sumamos las probabilidades de esos caminos. Esto solo aplica a resultados finales que son mutuamente excluyentes entre sí.
> *   **Dependencia y Reemplazo:**
>     *   **Con Reemplazo (Independientes):** La probabilidad no cambia en el segundo paso porque el total de elementos se mantiene igual.
>     *   **Sin Reemplazo (Dependientes):** El **espacio muestral (denominador)** disminuye en $1$ en cada paso sucesivo, alterando las probabilidades siguientes.

---

## 2. Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Diagrama de árbol** | Mapa gráfico de eventos y sus probabilidades organizadas por niveles. |
| **Probabilidad de la Intersección ($y$)** | $P(A \text{ y } B) = P(A) \cdot P(B|A)$. Se multiplican las ramas del camino. |
| **Probabilidad de la Unión ($o$)** | Se obtiene sumando las probabilidades de los caminos favorables finales. |
| **Eventos Independientes** | Experimentos donde el primer resultado no afecta al segundo (ej. lanzar una moneda). |
| **Espacio Muestral** | El total de opciones posibles; en LaTeX se representa en el denominador de la fracción. |

---

## 3. Ejemplos Resueltos Adicionales

```ad-example
**Ejemplo A — Lanzamiento de una moneda y un dado**
**Enunciado:** Calcular la probabilidad de obtener "Cara" en la moneda y el número $3$ en el dado. 
*(Nota: En algunos textos, "Cara" también se conoce como "Cruz" o "Sello").*

**Solución paso a paso:**
1. **Paso 1 (Moneda):** La probabilidad de obtener "Cara" es $P(C) = \frac{1}{2}$, pues hay $1$ opción favorable de $2$ posibles.
2. **Paso 2 (Dado):** La probabilidad de obtener el número $3$ es $P(3) = \frac{1}{6}$, ya que el dado tiene $6$ caras.
3. **Resultado Final:** Aplicamos la regla de la multiplicación para el camino "Cara y $3$":
   $$\frac{1}{2} \cdot \frac{1}{6} = \frac{1}{12}$$
   Al realizar la división, obtenemos aproximadamente $0.083$, lo que equivale a un $8.33\%$ de probabilidad.
```

```ad-example
**Ejemplo B — Juego de azar con urna (Extracción con reemplazo)**
**Enunciado:** En una urna hay $3$ bolas rojas y $4$ azules (total: $7$). Un jugador paga $\$1$ $USD$ por extraer dos bolas **con reemplazo**. Gana si ambas son del mismo color.

**Solución paso a paso:**
1. **Probabilidad Azul-Azul ($A,A$):** Como es con reemplazo, la probabilidad se mantiene en $\frac{4}{7}$.
   $$P(A,A) = \frac{4}{7} \cdot \frac{4}{7} = \frac{16}{49}$$
2. **Probabilidad Roja-Roja ($R,R$):** La probabilidad de roja es $\frac{3}{7}$ en ambos intentos.
   $$P(R,R) = \frac{3}{7} \cdot \frac{3}{7} = \frac{9}{49}$$
3. **Sumar eventos favorables (Mismo color):** Aplicamos la regla de la suma para la unión de ambos casos exitosos.
   $$\frac{16}{49} + \frac{9}{49} = \frac{25}{49}$$
4. **Resultado Final:** $\frac{25}{49} \approx 0.5102$, es decir, el jugador tiene un $51.02\%$ de probabilidad de ganar.
```

---

## 4. Ejercicios de Repaso

```ad-abstract
**🟢 Fácil**
*Experimento: Lanzamiento de dos monedas consecutivas (Cada rama es $\frac{1}{2}$).*
1. Calcula la probabilidad exacta de obtener $2$ sellos ($S,S$).
2. ¿Cuál es la probabilidad de obtener exactamente una cara y un sello (en cualquier orden)?
3. Si lanzamos las dos monedas, ¿qué probabilidad hay de que no salga ninguna cara ($0\%$ de caras)?
```

```ad-abstract
**🟡 Medio**
*Experimento: Lanzamiento de una moneda y un dado.*
1. Determina la probabilidad de obtener "Cara" y un número par ($2$, $4$ o $6$).
2. Calcula la probabilidad de obtener "Sello" y un número menor a $3$.
3. ¿Cuál es la probabilidad de obtener "Sello" y un número mayor a $4$?
```

```ad-abstract
**🔴 Avanzado — Aplicación con $USD**
*Experimento: Urna con $5$ bolas rojas y $4$ azules (total: $9$). Extracción de dos bolas **sin reemplazo**.*
1. Si apostar cuesta $\$2$ $USD$, ¿cuál es la probabilidad de sacar dos bolas rojas? (Recuerda que el total de bolas disminuye en la segunda extracción).
2. ¿Cuál es la probabilidad de sacar una bola de cada color? *Pista: Considera el camino Roja-Azul y el camino Azul-Roja.*
3. Calcula la probabilidad de obtener al menos una bola azul en las dos extracciones.
```

---

> [!tip] 💡 Consejo de estudio
> Para no perderte, **visualiza el camino** desde el tronco hasta las hojas. Mientras recorres una rama hacia adelante, multiplica las probabilidades. Cuando necesites agrupar diferentes resultados finales, suma. ¡Y nunca olvides simplificar tus fracciones! Eso te ayudará a ver el porcentaje real de éxito mucho más rápido.

¡Sigue practicando, porque la probabilidad está en todas partes!_