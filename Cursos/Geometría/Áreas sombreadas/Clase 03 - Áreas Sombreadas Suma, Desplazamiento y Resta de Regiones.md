[[Clase 02]] | [[Curso de Geometría]] | [[Clase 04]]
**Tags:** #matemáticas #geometría #áreas-sombreadas #pedagogía

# Clase 03 — Áreas Sombreadas: Suma, Desplazamiento y Resta de Regiones

### RELEVANCIA Y APLICACIONES

> [!info] ¿Por qué es importante esta clase?
> El dominio de las áreas sombreadas permite descomponer estructuras complejas en formas geométricas básicas, una habilidad crítica en campos técnicos.
> - 💵 **Costos de Materiales:** El cálculo exacto del área superficial permite presupuestar con precisión insumos como pintura, láminas metálicas o recubrimientos, evitando el desperdicio.
> - 🏗️ **Diseño y Optimización:** En ingeniería, entender cómo se distribuyen las regiones ayuda a optimizar la resistencia y el peso de las piezas.
> - 📊 **Análisis Espacial:** Desarrolla la capacidad visual para identificar patrones y simetrías en planos arquitectónicos e industriales.

---

### CONCEPTO CLAVE

Para un estudiante, calcular un **área sombreada** es como resolver un rompecabezas geométrico. El secreto no está en aprender fórmulas nuevas, sino en saber cómo combinar las que ya conoces: puedes "pegar" piezas (**suma**), "quitar" huecos (**resta**) o "mover" secciones a espacios vacíos para simplificar el problema (**desplazamiento**).

**Error común:**
*   ❌ Olvidar que un **semicírculo** es la mitad de un círculo (¡debes dividir el área entre $2$!).
*   ❌ Confundir el **diámetro** (la línea total que cruza el círculo) con el **radio** (la distancia del centro al borde). 
*   ✅ **Recuerda:** $Radio = Diámetro / 2$.

**Truco Mnemotécnico:**
Para no olvidar nunca el área del círculo ($A = \pi \cdot r^2$), repite: **"Pi-RR-Dos"** (Pi por Radio por Radio).

**Pro-Tip del Experto:**
En matemáticas avanzadas, es más preciso dejar el resultado en términos de $\pi$ (por ejemplo, $32\pi$) que usar decimales. Esto evita errores de redondeo acumulados.

---

### PROCEDIMIENTO PASO A PASO

```text
PASO 1: Identificar figuras básicas (rectángulos, círculos, triángulos).
PASO 2: Determinar dimensiones clave (base, altura y, sobre todo, el RADIO).
PASO 3: Calcular las áreas individuales usando las fórmulas estándar.
PASO 4: Ejecutar la operación final: Suma (adición), Resta (sustracción) o 
        Transferencia (desplazamiento de regiones simétricas).
```

---

### EJEMPLOS GUIADOS

> [!example] Ejemplo 1: Suma de Regiones
> Un rectángulo de base **$14 \text{ cm}$** y altura **$6 \text{ cm}$** tiene un semicírculo pegado a su base.
> 1. **Área del Rectángulo:** $14 \times 6 = \mathbf{84 \text{ cm}^2}$.
> 2. **Radio del semicírculo:** Como la base es $14 \text{ cm}$, el radio es la mitad: $\mathbf{7 \text{ cm}}$.
> 3. **Área del Semicírculo:** $(\pi \cdot 7^2) / 2 \approx \mathbf{76.9692 \text{ cm}^2}$.
> 4. **Resultado Final:** $84 + 76.9692 = \mathbf{160.9692 \text{ cm}^2}$.
> 
> **Aplicación Económica:** Si el $cm^2$ de pintura dorada cuesta **$0.50 USD$**, el costo total sería: $160.9692 \times 0.50 = \mathbf{80.48 USD}$.

> [!example] Ejemplo 2: Técnica de Desplazamiento (Simetría)
> En un cuadrado de **$10 \times 10 \text{ cm}$**, hay pétalos sombreados. Si dividimos el cuadrado en cuatro cuadrantes de **$5 \times 5 \text{ cm}$**, notamos que la curva de cada pétalo tiene el mismo radio (**$5 \text{ cm}$**). 
> 1. El área sombreada de un "pétalo" en un cuadrante es el complemento exacto del vacío en otro. 
> 2. Al rotar y trasladar estas piezas, el área sombreada llena exactamente la mitad del cuadrado original, formando un rectángulo de **$10 \times 5 \text{ cm}$**.
> 3. **Resultado:** $10 \times 5 = \mathbf{50 \text{ cm}^2}$.

> [!example] Ejemplo 3: Resta de Áreas
> Hallar el área de un círculo grande al que se le quitan dos círculos pequeños idénticos de radio **$r = 4 \text{ cm}$**.
> 1. **Análisis de dimensiones:** El radio del círculo grande ($R$) es igual al diámetro del pequeño. Si $r = 4$, entonces $D = 8$. Por lo tanto, $R = \mathbf{8 \text{ cm}}$.
> 2. **Área Círculo Grande:** $\pi \cdot 8^2 = \mathbf{64\pi}$.
> 3. **Área de los 2 Círculos Pequeños:** $2 \times (\pi \cdot 4^2) = \mathbf{32\pi}$.
> 4. **Resta Final:** $64\pi - 32\pi = \mathbf{32\pi} \approx \mathbf{100.53 \text{ cm}^2}$.

---

### EJERCICIOS PRÁCTICOS

> [!abstract] Retos de Clase
> **Nivel Verde (Fácil):** Calcula el área total de una figura compuesta por un rectángulo de **$10 \times 8 \text{ cm}$**, un círculo completo de **radio $5 \text{ cm}$** y un semicírculo de **radio $4 \text{ cm}$**.
> 
> **Nivel Amarillo (Medio):** En un cuadrado de **$6 \times 6 \text{ cm}$** con pétalos sombreados en los cuatro lados, se realizan desplazamientos de las regiones curvas para rellenar los vacíos internos. Si todas las piezas encajan perfectamente para cubrir la superficie total, ¿cuál es el área sombreada?
> 
> **Nivel Rojo (Avanzado):** A un círculo de **radio $4 \text{ cm}$** se le resta un círculo inscrito de **radio $2 \text{ cm}$**. Si el material restante tiene un costo de **$1.20 USD$** por **$cm^2$**, ¿cuál es el presupuesto total?

> [!success] Solucionario Técnico
> - **Respuesta Verde:** $183.762 \text{ cm}^2$.
>   *Lógica: $(10 \times 8) + (\pi \cdot 5^2) + (\frac{\pi \cdot 4^2}{2}) = 80 + 25\pi + 8\pi = 80 + 33\pi$.*
> - **Respuesta Amarillo:** $\mathbf{36 \text{ cm}^2}$.
>   *Lógica: Por desplazamiento y simetría, las áreas sombreadas completan el área total del cuadrado ($6 \times 6$).*
> - **Respuesta Rojo:** Área = $\mathbf{12\pi} \approx \mathbf{37.68 \text{ cm}^2}$. Presupuesto = $\mathbf{45.216 USD}$.
>   *Lógica: $(16\pi - 4\pi) = 12\pi$. Luego: $37.68 \times 1.20$.*

---

### AUTOEVALUACIÓN

> [!question] Comprueba tu aprendizaje
> 1. Si rotas o mueves una pieza sombreada dentro de los límites de una misma figura, ¿por qué el área total no cambia?
> 2. Si el ancho de un rectángulo es de **$10 \text{ cm}$** y coincide exactamente con el diámetro de un semicírculo pegado a su lateral, ¿cuál es el radio de ese semicírculo?
> 3. Tienes un diseño con un área de **$100 \text{ cm}^2$**. Si el material cuesta **$2.50 USD$** por cada **$cm^2$**, ¿cuál es la inversión requerida?

---

**PRÓXIMO TEMA:**
Has dominado la suma, resta y el desplazamiento. Con esto cerramos las herramientas fundamentales. En la siguiente sesión, aplicaremos estos conceptos en problemas de nivel examen de admisión. ¡Prepárate para el reto final!

[[Clase 02]] | [[Curso de Geometría]] | [[Clase 04]]