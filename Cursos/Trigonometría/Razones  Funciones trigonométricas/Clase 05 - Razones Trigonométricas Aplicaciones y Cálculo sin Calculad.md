# Clase 05 — Razones Trigonométricas: Aplicaciones y Cálculo sin Calculadora

#algebra #trigonometricra

Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 5 de 12

> [!info] 🧭 Navegación
> ◀️ **Anterior**: [[Clase 04 — Introducción a las Razones Trigonométricas]]
> ▶️ **Siguiente**: [[Clase 06 — Identidades y Ángulos Notables]]

---

> [!info] 🌍 Relevancia y aplicaciones
> La trigonometría nos otorga el "superpoder" de medir lo inalcanzable: desde la altura de una cometa en pleno vuelo hasta la posición exacta de un cohete espacial. Al entender la relación entre ángulos y distancias, podemos calcular dimensiones sin necesidad de una cinta métrica gigante.

*   **💵 Aplicación $USD:** Supón que deseas fabricar un hilo reforzado para una cometa de alto rendimiento. Si has soltado $50\text{ m}$ de hilo y el material cuesta $\$0.50\text{ USD}$ por metro, el costo total es de $\$25.00\text{ USD}$. La trigonometría te dirá a qué altura está tu cometa con ese presupuesto.
*   **🏗️ Aplicación práctica:** Los ingenieros aeroespaciales determinan la altura de un cohete (como en el ejemplo de $949.89\text{ m}$) analizando su ángulo de lanzamiento y la distancia recorrida en su trayectoria.
*   **📊 Situación cotidiana:** Puedes calcular la altura de un edificio o un árbol simplemente midiendo la longitud de su sombra en el suelo y el ángulo de elevación del sol.

---

### 3. CONCEPTO CLAVE Y ERRORES COMUNES

**Definición para estudiantes de secundaria**
Imagina que las razones trigonométricas ($\text{seno}, \text{coseno}, \text{tangente}$) son "traductores" que convierten un ángulo en una proporción entre dos lados de un triángulo. Si conoces el ángulo, el traductor te dice cuántas veces es más grande un lado respecto al otro.

**⚠️ Error común**
¡Cuidado! Las razones trigonométricas solo funcionan en **triángulos rectángulos** (con un ángulo de $90^\circ$). En problemas complejos, el error más habitual es usar un triángulo oblicuo (sin ángulo recto). Siempre debes identificar y "extraer" los triángulos rectángulos de la figura.

**💡 Truco: SOH CAH TOA**
Para elegir la fórmula correcta, usa esta regla mnemotécnica. Recuerda que **Opuesto** y **Adyacente** dependen de la posición del ángulo que estás analizando:
*   **SOH**: $\text{sen}(\theta) = \frac{\text{Opuesto}}{\text{Hipotenusa}}$
*   **CAH**: $\cos(\theta) = \frac{\text{Adyacente}}{\text{Hipotenusa}}$
*   **TOA**: $\tan(\theta) = \frac{\text{Opuesto}}{\text{Adyacente}}$

---

### 4. PROCEDIMIENTO PASO A PASO (DOS TRIÁNGULOS)

Cuando enfrentes figuras con múltiples triángulos, utiliza la estrategia del **"Lado Puente"**:

```text
PASO 1: Identificar y separar visualmente los dos triángulos rectángulos.
PASO 2: Localizar el "Lado Puente" (el lado común que ambos comparten).
PASO 3: Resolver el triángulo que tiene dos datos conocidos para hallar 
        el valor de dicho "Lado Puente" (generalmente llamado 'y').
PASO 4: Usar el valor del "Lado Puente" como dato de entrada para resolver 
        el segundo triángulo y hallar la incógnita final ('x').
```

---

### 5. TABLA DE VALORES NOTABLES (Cálculo sin calculadora)

Para resolver ejercicios sin tecnología, debes memorizar estos valores clave:

| Ángulo ($\theta$) | $\text{sen}(\theta)$ | $\cos(\theta)$ | $\tan(\theta)$ |
| :--- | :--- | :--- | :--- |
| **$30^\circ$** | $1/2$ | $\sqrt{3}/2$ | $\sqrt{3}/3$ |
| **$45^\circ$** | $\sqrt{2}/2$ | $\sqrt{2}/2$ | $1$ |
| **$60^\circ$** | $\sqrt{3}/2$ | $1/2$ | $\sqrt{3}$ |

---

### 6. BLOQUES DE EJEMPLOS PRÁCTICOS

#### Ejemplo 1: El caso de la cometa (Básico)
*   **Enunciado:** Se sueltan $50\text{ m}$ de hilo con un ángulo de $37^\circ$. Hallar la altura ($x$).
*   **Solución:** $\text{sen}(37^\circ) = \frac{x}{50} \implies x = 50 \cdot \text{sen}(37^\circ)$.
*   **Resultado:** $x = 30.09\text{ m}$.

#### Ejemplo 2: El "Lado Puente" (Intermedio)
*   **Enunciado:** Un sistema tiene dos triángulos. El primero con ángulo $32^\circ$ e hipotenusa $15\text{ m}$. El segundo con ángulo $63^\circ$ busca la base $x$.
*   **Solución:**
    1.  Hallar lado puente $y$: $\text{sen}(32^\circ) = \frac{y}{15} \implies y = 15 \cdot \text{sen}(32^\circ) = 7.94\text{ m}$.
    2.  Hallar $x$ en el segundo triángulo: $\tan(63^\circ) = \frac{y}{x} \implies x = \frac{7.94}{\tan(63^\circ)}$.
*   **Resultado:** $x = 4.04\text{ m}$.

#### Ejemplo 3: Racionalización y Raíces (Avanzado sin calculadora)
*   **Enunciado:** Hallar $x$ si el adyacente mide $\frac{2\sqrt{3}}{3}\text{ m}$ y el ángulo es $60^\circ$.
*   **Solución:** $\tan(60^\circ) = \frac{x}{\text{adyacente}} \implies \sqrt{3} = \frac{x}{(2\sqrt{3}/3)}$.
*   **Operación:** $x = \frac{2\sqrt{3}}{3} \cdot \sqrt{3} = \frac{2 \cdot (\sqrt{3} \cdot \sqrt{3})}{3} = \frac{2 \cdot 3}{3} = 2$.
*   **Resultado:** $x = 2\text{ m}$.

#### Ejemplo 4: Aplicación $USD (Costo de infraestructura)
*   **Enunciado:** Se requiere un cable para sostener una antena de $10\text{ m}$ de altura. El cable formará un ángulo de $45^\circ$ con el suelo. Si el metro de cable cuesta $\$12.50\text{ USD}$, ¿cuánto es el presupuesto?
*   **Solución:** $\text{sen}(45^\circ) = \frac{10}{H} \implies H = \frac{10}{\text{sen}(45^\circ)} = \frac{10}{\sqrt{2}/2} \approx 14.14\text{ m}$.
*   **Costo:** $14.14\text{ m} \cdot \$12.50\text{ USD/m} = \$176.75\text{ USD}$.

---

### 7. EJERCICIOS PARA EL ESTUDIANTE

**🟢 Nivel Fácil (Sin calculadora - Usa la tabla)**
1. Hallar el cateto opuesto si la hipotenusa es $10\text{ m}$ y el ángulo es $30^\circ$.
2. Hallar el cateto adyacente si la hipotenusa es $20\text{ m}$ y el ángulo es $60^\circ$.
3. Calcular el cateto opuesto si la hipotenusa mide $\sqrt{2}\text{ m}$ y el ángulo es $45^\circ$.
4. Si $\text{sen}(30^\circ) = 1/2$ y la hipotenusa mide $12\text{ m}$, ¿cuánto vale el cateto opuesto?

**🟡 Nivel Medio (Aplicación directa)**
5. Un cohete recorre $1200\text{ m}$ con un ángulo de $52^\circ 20'$. Hallar su altura exacta (ver fuente).
6. Una cometa tiene $100\text{ m}$ de hilo y un ángulo de $37^\circ$. Hallar su altura.
7. Un árbol proyecta una sombra con un ángulo de elevación de $60^\circ$. Si la sombra mide $5\text{ m}$, ¿cuál es su altura?
8. Una escalera de $5\text{ m}$ se apoya en una pared con un ángulo de $37^\circ$ respecto al suelo. ¿A qué altura llega?

**🔴 Nivel Avanzado ($USD y Figuras Complejas)**
9. En una figura de dos triángulos, el primero tiene hipotenusa $30\text{ m}$ y ángulo $32^\circ$. Hallar la base $x$ del segundo triángulo si su ángulo es $63^\circ$.
10. Un cohete debe alcanzar una altura de $1000\text{ m}$ con un ángulo de lanzamiento de $60^\circ$. Calcula la longitud del cable de seguridad necesario y su costo si el metro vale $\$15.75\text{ USD}$.
11. Se instalan dos cables para una antena. El primero mide $50\text{ m}$ con un ángulo de $37^\circ$. El segundo cable se coloca al otro lado con un ángulo de $45^\circ$ para alcanzar la misma altura. Si el metro cuesta $\$8.00\text{ USD}$, ¿cuál es el costo total de ambos cables?
12. Hallar el valor exacto de $x$ sin calculadora si el cateto adyacente es $\frac{2\sqrt{3}}{3}$ y el ángulo de elevación es $60^\circ$.

#### ✅ Respuestas
1. $5\text{ m}$ | 2. $10\text{ m}$ | 3. $1\text{ m}$ | 4. $6\text{ m}$ | 5. $949.89\text{ m}$ | 6. $60.18\text{ m}$ | 7. $8.66\text{ m}$ | 8. $3.01\text{ m}$ | 9. $8.10\text{ m}$ | 10. $1154.70\text{ m}$ de cable; $\$18,186.53\text{ USD}$ | 11. Cable 2: $42.55\text{ m}$. Costo Total: $\$740.40\text{ USD}$ | 12. $2$.

---

### 8. AUTOEVALUACIÓN Y CIERRE

**🧪 Pregunta 1:** ¿Cómo identificas el Cateto Adyacente en un triángulo rectángulo?
*(Respuesta: Es el cateto que forma parte del ángulo de referencia, excluyendo la hipotenusa).*

**🧪 Pregunta 2:** Si tienes el Cateto Opuesto y buscas la Hipotenusa, ¿qué razón es la más directa?
*(Respuesta: El Seno, despejando la hipotenusa).*

**🧪 Pregunta 3:** Una cometa usa $100\text{ m}$ de hilo (hipotenusa) con un ángulo de $30^\circ$. Si el hilo cuesta $\$2.00\text{ USD}$ el metro, ¿cuál es el costo total y a qué altura está?
*(Respuesta: Costo $\$200.00\text{ USD}$; Altura $50\text{ m}$).*

**Tip para la próxima clase:** En la **Clase 06** exploraremos cómo estas razones se relacionan entre sí para formar **Identidades Trigonométricas**, permitiéndonos simplificar ecuaciones complejas de un solo vistazo.

> [!info] 🧭 Navegación
> ◀️ **Anterior**: [[Clase 04 — Introducción a las Razones Trigonométricas]]
> ▶️ **Siguiente**: [[Clase 06 — Identidades y Ángulos Notables]]