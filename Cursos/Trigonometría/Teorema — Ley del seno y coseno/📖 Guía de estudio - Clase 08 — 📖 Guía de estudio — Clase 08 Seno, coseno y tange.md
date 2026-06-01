# 📖 Guía de estudio — Clase 08: Seno, coseno y tangente de 30°, 45° y 60°

> [!info] **📌 Conceptos clave**
> - **Utilidad de los ángulos especiales:** Los ángulos de $30^\circ$, $45^\circ$ y $60^\circ$ aparecen frecuentemente en la naturaleza y la ingeniería. Conocer sus razones exactas permite resolver problemas complejos sin usar calculadora.
> - **Origen de $30^\circ$ y $60^\circ$:** Se derivan de un **triángulo equilátero**. Pedagógicamente, utilizamos un lado de longitud $2$. **¿Por qué?** Porque al trazar la altura, la base se divide exactamente en $1$ (un número entero sencillo), facilitando los cálculos del Teorema de Pitágoras para hallar la altura ($\sqrt{3}$).
> - **Origen de $45^\circ$:** Proviene de un **triángulo isósceles rectángulo** con catetos de longitud $1$. Al ser isósceles, sus ángulos agudos son iguales ($45^\circ$) y su hipotenusa es siempre $\sqrt{2}$.
> - **Razones inversas:** Cada función básica tiene una "pareja" inversa que resulta de invertir la fracción: la **cosecante** ($\csc$) es la inversa del seno, la **secante** ($\sec$) del coseno y la **cotangente** ($\cot$) de la tangente.

## 2. Fórmulas y definiciones importantes

### Definiciones generales
| Función | Relación entre lados | Abreviatura |
| :--- | :--- | :--- |
| **Seno** | $\frac{\text{Cateto Opuesto (CO)}}{\text{Hipotenusa (H)}}$ | $\sin$ o $\text{sen}$ |
| **Coseno** | $\frac{\text{Cateto Adyacente (CA)}}{\text{Hipotenusa (H)}}$ | $\cos$ |
| **Tangente** | $\frac{\text{Cateto Opuesto (CO)}}{\text{Cateto Adyacente (CA)}}$ | $\tan$ |

### Tabla de valores exactos
*Nota: Se incluye la **Racionalización** para evitar raíces en el denominador, un paso clave en matemáticas superiores.*

| Ángulo (Grados) | Radianes (Nota futuro) | $\sin$ | $\cos$ | $\tan$ | $\csc$ (inv) | $\sec$ (inv) | $\cot$ (inv) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **$30^\circ$** | $\pi/6$ | $1/2$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{3}}{3}$ | $2$ | $\frac{2\sqrt{3}}{3}$ | $\sqrt{3}$ |
| **$45^\circ$** | $\pi/4$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ | $1$ | $\sqrt{2}$ | $\sqrt{2}$ | $1$ |
| **$60^\circ$** | $\pi/3$ | $\frac{\sqrt{3}}{2}$ | $1/2$ | $\sqrt{3}$ | $\frac{2\sqrt{3}}{3}$ | $2$ | $\frac{\sqrt{3}}{3}$ |

## 3. Ejemplos resueltos adicionales

```ad-example
**Ejemplo A — Caso básico**
**Problema:** En un triángulo rectángulo con un ángulo de $30^\circ$, la hipotenusa ($H$) mide $2$ unidades. ¿Cuál es el valor del cateto opuesto ($CO$)?

**Paso a paso:**
1. **Identificar la función:** Necesitamos el $CO$ y conocemos la $H$. La función que relaciona ambos es el **Seno**.
2. **Sustituir valores:** $\sin(30^\circ) = \frac{CO}{H} \Rightarrow \frac{1}{2} = \frac{CO}{2}$.
3. **Resolver:** Despejamos el $CO$ multiplicando ambos lados por $2$: $2 \times (\frac{1}{2}) = CO$.
4. **Resultado:** El $CO$ mide **1 unidad**.
```

```ad-example
**Ejemplo B — Aplicación real $USD**
**Problema:** Un cable de soporte de una antena forma un ángulo de $60^\circ$ con el suelo. La distancia desde la base de la antena hasta el anclaje del cable ($CA$) es de $10$ metros. Si el cable cuesta $\$10$ USD por metro, ¿cuál es el costo total?

**Paso a paso:**
1. **Identificar la función:** Tenemos el Cateto Adyacente ($CA = 10m$) y buscamos la longitud del cable, que es la Hipotenusa ($H$). **Elegimos el Coseno** porque relaciona estos dos elementos.
2. **Sustituir valores:** $\cos(60^\circ) = \frac{CA}{H} \Rightarrow \frac{1}{2} = \frac{10}{H}$.
3. **Calcular la hipotenusa:** Al despejar, $H = 10 \times 2 = 20$ metros.
4. **Calcular costo:** Multiplicamos la medida por el precio: $20 \times \$10 \text{ USD}$.
5. **Resultado:** El cable costará **$200 USD**.
```

## 4. Ejercicios de repaso

```ad-abstract
**🟢 Nivel Fácil**
1. ¿Cuál es el valor exacto de $\cos(60^\circ)$?
2. Calcula el valor de $\tan(45^\circ)$.
3. Si el $\sin(30^\circ) = 1/2$, ¿cuál es el valor de su función inversa, la $\csc(30^\circ)$?
```

```ad-abstract
**🟡 Nivel Medio**
1. En un triángulo con un ángulo de $45^\circ$, el $CA$ mide $5$ cm. ¿Cuánto mide el $CO$?
2. Halla la $H$ de un triángulo rectángulo si el $CO$ a un ángulo de $60^\circ$ mide $\sqrt{3}$ unidades.
3. Si la $H$ de un triángulo mide $10$ unidades y tiene un ángulo de $30^\circ$, ¿cuánto mide su $CO$?
```

```ad-abstract
**🔴 Avanzado — Aplicación con $USD**
Un terreno tiene forma de triángulo rectángulo con un ángulo de $45^\circ$. El cateto adyacente a ese ángulo mide $20$ metros. Se desea cercar la **hipotenusa** con una malla que cuesta $\$15$ USD el metro lineal.

1. **Cálculo de distancia:** Halla la medida de la hipotenusa ($H$) usando el valor de $\cos(45^\circ) = \frac{\sqrt{2}}{2}$. (Usa $\sqrt{2} \approx 1.41$).
2. **Presupuesto:** Calcula el costo total en $USD para comprar la malla necesaria.
3. **Verificación pedagógica:** En este triángulo de $45^\circ$, ¿sería diferente el resultado si usaras el valor del cateto opuesto en lugar del adyacente? Explica por qué.
```

## 5. 💡 Consejo de estudio

> [!tip] **El truco de la "Mano" o la Tabla Mágica**
> Puedes construir toda la tabla de senos para $0^\circ, 30^\circ, 45^\circ, 60^\circ$ y $90^\circ$ en segundos:
> 1. Escribe los números del **0 al 4**.
> 2. Saca **raíz cuadrada** a cada uno: $\sqrt{0}, \sqrt{1}, \sqrt{2}, \sqrt{3}, \sqrt{4}$.
> 3. **Divide todos por 2**.
> 
> Al simplificar, obtienes los valores del seno: $0, 1/2, \frac{\sqrt{2}}{2}, \frac{\sqrt{3}}{2}, 1$.
> **¡Ojo!** Para el coseno, solo escribe los mismos valores en orden inverso. Este truco te salvará en cualquier examen.