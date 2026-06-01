# 📖 Guía de estudio — Clase 05: Deducción del teorema del seno

> [!info] 📌 Conceptos clave
> - **Propósito del teorema:** Permite resolver triángulos oblicuángulos (aquellos que no tienen un ángulo recto) encontrando lados o ángulos desconocidos.
> - **Trazado de altura:** La base de la demostración es trazar una altura ($x$). Usamos la letra "**$x$**" para evitar confusiones con la letra "**$h$**", que en trigonometría suele representar la hipotenusa.
> - **Uso de la función Seno:** Aplicamos la definición $\text{sen}(\theta) = \frac{\text{cateto opuesto}}{\text{hipotenusa}}$ en los dos triángulos rectángulos formados por la altura.
> - **Relación de proporcionalidad:** El teorema demuestra que la razón entre la longitud de un lado y el seno de su ángulo opuesto es constante para los tres lados del triángulo.

### Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Teorema del Seno** | $\frac{a}{\text{sen}(A)} = \frac{b}{\text{sen}(B)} = \frac{c}{\text{sen}(C)}$ |
| **Nomenclatura Estándar** | Los **Ángulos** se nombran con mayúsculas ($A, B, C$) y los **Lados opuestos** con minúsculas ($a, b, c$). |
| **Triángulos Acutángulos** | Triángulos donde todos sus ángulos internos son agudos (menores a 90°). |
| **Triángulos Obtusángulos** | Triángulos que tienen un ángulo obtuso (mayor a 90°). |
| **Propiedad de Suplementarios** | $\text{sen}(180^\circ - \theta) = \text{sen}(\theta)$. Esta propiedad, basada en el círculo trigonométrico, permite que el teorema funcione incluso en triángulos obtusos. |

---

### Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A — Deducción en triángulo acutángulo
Para demostrar que $\frac{b}{\text{sen}(B)} = \frac{c}{\text{sen}(C)}$, seguimos el razonamiento pedagógico del Profe Alex:
1. **Trazar altura ($x$):** En un triángulo $ABC$, trazamos la altura desde el vértice $A$ hacia la base. Esto crea dos triángulos rectángulos.
2. **Triángulo izquierdo:** Aplicamos seno al ángulo $C$: $\text{sen}(C) = \frac{x}{b}$. Despejando la altura: $x = b \cdot \text{sen}(C)$.
3. **Triángulo derecho:** Aplicamos seno al ángulo $B$: $\text{sen}(B) = \frac{x}{c}$. Despejando la altura: $x = c \cdot \text{sen}(B)$.
4. **Igualación:** Como $x$ es la misma altura para ambos, igualamos las expresiones: $b \cdot \text{sen}(C) = c \cdot \text{sen}(B)$.
5. **Resultado:** Al pasar los senos a dividir, obtenemos: $\frac{b}{\text{sen}(B)} = \frac{c}{\text{sen}(C)}$.
*Nota: Este mismo proceso se repite trazando una altura diferente para incluir al lado $a$ y al ángulo $A$, completando así la triple igualdad del teorema.*
```

```ad-example
title: Ejemplo B — Aplicación práctica en navegación
Un barco se desplaza entre dos puntos $A$ y $B$. Se sabe que el ángulo en $A$ es de $30^\circ$, el ángulo en $B$ es de $45^\circ$ y la distancia entre ellos (lado $c$) es de $10$ km. Para calcular la distancia desde el barco hasta el punto $B$ (lado $a$):
1. **Hallar ángulo opuesto a la distancia conocida:** $C = 180^\circ - (30^\circ + 45^\circ) = 105^\circ$.
2. **Plantear la relación:** $\frac{a}{\text{sen}(30^\circ)} = \frac{10}{\text{sen}(105^\circ)}$.
3. **Calcular:** $a = \frac{10 \cdot \text{sen}(30^\circ)}{\text{sen}(105^\circ)} \approx 5.18 \text{ km}$.
4. **Aplicación real $USD:** Si el combustible cuesta $12$ USD por kilómetro, el costo del trayecto será: $5.18 \text{ km} \times 12 \text{ USD/km} = 62.16 \text{ USD}$.
```

---

### Ejercicios de Repaso

```ad-abstract
title: 🟢 Fácil — Teoría y Nomenclatura
1. Según la nomenclatura estándar, si un ángulo se llama $B$, ¿cómo debe llamarse el lado que tiene justo enfrente?
2. ¿Por qué el Profe Alex recomienda usar la letra $x$ para la altura en lugar de la $h$?
3. ¿Cuál es la función trigonométrica que relaciona el cateto opuesto con la hipotenusa en la deducción?
```

```ad-abstract
title: 🟡 Medio — Despejes Algebraicos
1. Si $a = 15$, $\text{sen}(A) = \text{sen}(105^\circ)$ y $b = 8$, realiza el despeje para encontrar el valor de $\text{sen}(B)$.
2. En la fórmula $\frac{b}{\text{sen}(B)} = \frac{c}{\text{sen}(C)}$, despeja el lado $c$.
3. Utilizando la propiedad de suplementarios, si $\text{sen}(30^\circ) = 0.5$, ¿cuánto vale el $\text{sen}(150^\circ)$?
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
**Reto de Topografía:** Un topógrafo desea medir un lado de un terreno triangular. Un lado conocido mide $120$ metros y su ángulo opuesto es de $75^\circ$. Se sabe que otro ángulo interno del terreno mide $40^\circ$.
1. **Paso 1:** Calcula la longitud del lado opuesto al ángulo de $40^\circ$ usando el Teorema del Seno.
2. **Paso 2:** Si el costo de cercar el terreno es de $15$ USD por cada metro lineal, ¿cuánto costará cercar únicamente ese lado recién calculado?
*(Dato de ayuda: $\text{sen}(40^\circ) \approx 0.6427$, $\text{sen}(75^\circ) \approx 0.9659$)*.
```

---

> [!tip] 💡 Consejo de estudio
> Si en un examen olvidas la fórmula, aplica la **Estrategia Profe Alex**: dibuja el triángulo y traza la altura para deducirla en un minuto. ¡Y no olvides verificar que tu calculadora esté en modo **"Degrees" (D)**! Si aparece una **"R"** (Radianes) o **"G"** (Gradianes), tus resultados no serán correctos para grados sexagesimales.

**Clave de respuestas (para autocontrol):**
*Fácil: 1. Lado $b$ minúscula. 2. Para no confundirla con la hipotenusa. 3. Función Seno.*
*Avanzado: 1. Lado $\approx 79.85$ metros. 2. Costo $\approx 1,197.75$ USD.*