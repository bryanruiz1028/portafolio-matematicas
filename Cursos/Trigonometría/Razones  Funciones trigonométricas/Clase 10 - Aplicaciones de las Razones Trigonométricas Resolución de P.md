# Clase 10 — Aplicaciones de las Razones Trigonométricas: Resolución de Problemas Reales

#algebra #razonestrigonom
Curso: [[00 - Índice del curso]] | Bloque 3 | Lección 10 de 12

> [!info] 🧭 Navegación
> - Clase Anterior: [[Clase 09 - Razones Trigonométricas en Triángulos Rectángulos]]
> - Siguiente Clase: [[Clase 11 - Ley de Senos y Cosenos: Introducción]]

---

### 1. RELEVANCIA Y APLICACIONES

> [!info] 🌍 Relevancia y aplicaciones
> La trigonometría nos permite "tocar" lo inalcanzable. Gracias a los ángulos, podemos medir la altura de una montaña o la cima de un edificio sin tener que subirnos a ellos, convirtiendo distancias imposibles en simples cálculos matemáticos.
> 
> - 💵 **Aplicación $USD:** Calcular la longitud exacta de un tendido eléctrico de alta tensión (hipotenusa) para presupuestar el costo total del cable basado en su precio por metro.
> - 🏗️ **Aplicación práctica:** Determinación de alturas de infraestructuras urbanas en construcción mediante el uso de sombras y ángulos de elevación.
> - 📊 **Situación cotidiana:** Diseño de rampas de acceso para sillas de ruedas, asegurando que la inclinación cumpla con las normas de seguridad.

---

### 2. CONCEPTO CLAVE

> [!note] 📌 ¿Qué es Razones trigonométricas?
> ¡Qué tal, amigos! Imaginen que un triángulo rectángulo es como una **receta de cocina**. Si conocen al menos un lado y un ángulo, tienen los ingredientes suficientes para descubrir cuánto miden todos los demás lados "mágicamente". Es simplemente la relación fija que hay entre los lados y los ángulos de un triángulo.

> [!warning] ⚠️ Error común
> **Incorrecto:** Intentar usar la función Seno cuando solo conoces los dos catetos (opuesto y adyacente) y no la hipotenusa.
> **Correcto:** Antes de elegir una fórmula, identifica qué "ingredientes" tienes y cuáles te faltan usando la guía **SOH-CAH-TOA**.

> [!tip] 💡 Truco para recordarlo
> Memoriza la palabra **SOH-CAH-TOA**:
> - **S**en = **O**puesto / **H**ipotenusa
> - **C**os = **A**dyacente / **H**ipotenusa
> - **T**an = **O**puesto / **A**dyacente

---

### 3. PROCEDIMIENTO PASO A PASO

Para resolver cualquier problema como un experto, sigue esta metodología inspirada en el "profe Alex":

> [!important] 📝 Metodología de resolución
> 1. **PASO 1 → El dibujo de "Líneas y Puntos":** No necesitas ser un artista. Representa el sol o la cima como un punto, y el suelo o un poste como líneas. Lo importante es que visualices el triángulo rectángulo.
> 2. **PASO 2 → Etiquetado:** Nombra los lados según el ángulo (Cateto Opuesto, Adyacente e Hipotenusa).
> 3. **PASO 3 → Elección de la Razón:** Mira tus datos. ¿Tienes CO y CA? Usa Tangente. ¿Tienes CO e H? Usa Seno.
> 4. **PASO 4 → Cálculo y despeje:** Resuelve la ecuación. Si buscas un ángulo, usa la función inversa ($\text{Sen}^{-1}, \text{Cos}^{-1}, \text{Tan}^{-1}$).

> [!warning] ⚠️ ¡Ojo con la calculadora!
> Antes de empezar, asegúrate de que tu calculadora esté en modo **DEG** (Grados/Degrees). Si ves una "R" (Radianes) o "G" (Gradianes) en la pantalla, tus resultados serán incorrectos. Debe aparecer una **D**.

---

### 4. EJEMPLOS RESUELTOS

#### Ejemplo 1: El ángulo del sol (Caso Básico)
**Problema:** Un poste de 4.5 m proyecta una sombra de 5.3 m. ¿Cuál es el ángulo de elevación del sol?
1. **Dibujo:** El poste es el CO (4.5 m) y la sombra es el CA (5.3 m).
2. **Razón:** Usamos Tangente: $\tan(\theta) = \frac{4.5}{5.3}$.
3. **Despeje:** $\theta = \tan^{-1}(\frac{4.5}{5.3})$.
4. **Resultado:** **40.33°** (o 40° 19' 59").

#### Ejemplo 2: Altura de un edificio (Despeje de lado)
**Problema:** A 80 m de la base de un edificio, el ángulo de elevación a la cúspide es de 52°. Calcula la altura ($x$).
1. **Datos:** CA = 80 m, Ángulo = 52°, CO = $x$.
2. **Razón:** $\tan(52^\circ) = \frac{x}{80}$.
3. **Cálculo:** $x = 80 \cdot \tan(52^\circ)$.
4. **Resultado:** **102.39 metros**.

#### Ejemplo 3: El Topógrafo y la Montaña (Caso Avanzado)
**Problema:** Un topógrafo mide un ángulo de elevación de 43°. Se aleja 1 km (1,000 m) y el ángulo baja a 23°. ¿Qué altura ($x$) tiene la montaña?
1. **Estrategia:** Usamos el **Método de Igualación**. Como ambos triángulos comparten la misma altura ($x$), despejamos $x$ en ambos y los igualamos. Llamamos $y$ a la distancia desconocida desde el primer punto a la base.
2. **Ecuaciones:**
   - Triángulo 1: $x = y \cdot \tan(43^\circ)$
   - Triángulo 2: $x = (y + 1000) \cdot \tan(23^\circ)$
3. **Igualación:** $y \cdot \tan(43^\circ) = (y + 1000) \cdot \tan(23^\circ)$.
4. **Resultado final:** Al resolver el sistema, obtenemos que la altura $x$ es de **779.1 metros**.

#### Ejemplo 4: Presupuesto de Antena ($USD)
**Problema original:** Se requiere un cable de soporte (hipotenusa) para una antena. El cable forma un ángulo de 60° con el suelo y se anclará a 10 m de la base. Si el metro de cable cuesta $15.50 USD, ¿cuál es el presupuesto?
1. **Datos:** CA = 10 m, Ángulo = 60°, Hipotenusa ($n$) = ?.
2. **Razón:** $\cos(60^\circ) = \frac{10}{n} \rightarrow n = \frac{10}{\cos(60^\circ)} = 20 \text{ metros}$.
3. **Costo:** $20 \text{ m} \times \$15.50 = \mathbf{\$310.00 \text{ USD}}$.

---

### 5. EJERCICIOS PARA EL ESTUDIANTE

> [!abstract] 🟢 Nivel Fácil: La Rampa de Ciclismo
> Una rampa de 12 m de largo (hipotenusa) tiene una altura de 2.3 m. Calcula el ángulo de elevación.

> [!abstract] 🟡 Nivel Medio: La Cometa
> El hilo de una cometa mide 95 m y forma un ángulo de 25° con el suelo. Calcula la altura de la cometa.

> [!abstract] 🔴 Nivel Avanzado: Mantenimiento del Faro ($USD)
> Desde un barco se ve la punta de un faro con un ángulo de 24°. El barco se acerca 300 m y el ángulo aumenta a 36°. 
> 1. Calcula la altura del faro.
> 2. Si pintar cada metro de altura cuesta $120 USD, ¿cuál es el costo total?

---

### 6. RESPUESTAS

> [!success] ✅ Resultados verificados
> - **Fácil:** 11.05° (u 11° 3' 0").
> - **Medio:** 40.14 metros.
> - **Avanzado:**
>   - Altura $\approx$ 344.96 metros.
>   - Costo: $344.96 \text{ m} \times 120 \text{ USD/m} = \mathbf{\$41,395.20 \text{ USD}}$.

---

### 7. MINI-PRUEBA DE AUTOEVALUACIÓN

1. **Conceptual:** Si tienes el Cateto Opuesto y quieres hallar la Hipotenusa, ¿qué función usas?
   - *R: Seno (SOH).*
2. **Procedimental:** ¿Cuál es el ángulo si su $\tan(\theta) = 1$?
   - *R: 45°.*
3. **Aplicación $USD:** Una escalera de 10 m (hipotenusa) se apoya con un ángulo de 60°. Si cada metro de escalera cuesta $200 USD, ¿cuál es el costo total?
   - *R: $2,000 USD.*

---

### 8. CIERRE Y NOTAS

> [!tip] 💡 En la próxima clase
> ¡Felicidades! Ya dominas los triángulos rectángulos. En la próxima lección daremos el gran salto a la **Ley de Senos y Cosenos**, para resolver triángulos que no tienen ángulos de 90°.

> [!info] 🧭 Navegación
> - Clase Anterior: [[Clase 09 - Razones Trigonométricas en Triángulos Rectángulos]]
> - Siguiente Clase: [[Clase 11 - Ley de Senos y Cosenos: Introducción]]