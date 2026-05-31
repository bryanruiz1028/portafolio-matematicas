# Clase 12 — Resolución de Triángulos Rectángulos

#algebra #solvingarighttr
Curso: [[00 - Índice del curso]] | Bloque 3 | Lección 12 de 12

> [!info] 🧭 Navegación
> ◀ [[Clase 11 — Razones Trigonométricas]] | [[00 - Índice del curso]] | Siguiente tema: Trigonometría No Rectangular ▶

---

## 🌍 Relevancia y aplicaciones
La resolución de triángulos nos permite conocer distancias inaccesibles mediante el cálculo indirecto. Es la técnica que nos ayuda a proyectar medidas exactas en el mundo real sin necesidad de medir físicamente cada centímetro de una estructura o terreno.

- 💵 **Costos y materiales**: Permite calcular la longitud exacta de la hipotenusa (cables, vigas o cercas) para definir presupuestos en $USD evitando el desperdicio de material.
- 🏗️ **Ingeniería y construcción**: Uso fundamental para determinar la longitud y el ángulo de inclinación exacto en rampas de acceso, pendientes de alcantarillado o soportes estructurales.
- 📊 **Situación cotidiana**: Cálculo de la altura real de un árbol o un edificio utilizando únicamente la longitud de su sombra proyectada en el suelo y el ángulo de elevación del sol en ese momento.

---

## 📌 Conceptos fundamentales

> [!note] 📌 ¿Qué es "Solving a Right Triangle"?
> Para un estudiante, esto significa simplemente **"encontrar todas las piezas del rompecabezas"**: es decir, hallar el valor de los tres lados y los tres ángulos internos del triángulo partiendo de los datos conocidos.

> [!warning] ⚠️ Error común
> ¡Cuidado! Jamás intentes aplicar razones trigonométricas (Seno, Coseno, Tangente) en triángulos que no tengan un ángulo de 90°. Si el triángulo no es **rectángulo**, estas fórmulas te darán resultados incorrectos.

> [!tip] 💡 Truco para recordarlo: SOH CAH TOA
> Memoriza esta palabra mágica para recordar cómo se dividen los lados:
> 
> *   **S**OH: **S**en($\theta$) = $\frac{\textbf{O}puesto}{\textbf{H}ipotenusa}$
> *   **C**AH: **C**os($\theta$) = $\frac{\textbf{A}dyacente}{\textbf{H}ipotenusa}$
> *   **T**OA: **T**an($\theta$) = $\frac{\textbf{O}puesto}{\textbf{A}dyacente}$

---

## 🛠️ Procedimiento Paso a Paso

```text
PASO 1: Identificar y nombrar los lados (Hipotenusa, Cateto Opuesto, Cateto Adyacente) 
        tomando como referencia el ángulo dado.
PASO 2: Encontrar el tercer ángulo restando los conocidos a 180° (o restando el 
        ángulo agudo a 90°). ¡Es el paso más sencillo para empezar!
PASO 3: Seleccionar la razón trigonométrica (SOH CAH TOA) que relacione un dato 
        conocido con la incógnita que quieres buscar.
        *CONSEJO DEL PROFE ALEX*: Usa siempre los datos originales del problema para 
        tus cálculos; así evitarás arrastrar errores de redondeo.
PASO 4: Despejar la incógnita y usar la calculadora. 
        ¡IMPORTANTE!: Verifica que tu calculadora esté en modo "Degrees" (D). 
        Si aparece una (R) o (G), el resultado será erróneo.
```

---

## 📖 Ejemplos de la Fuente

### Ejemplo 1: Caso Básico (Ángulo y Cateto conocidos)
**Datos iniciales:** Ángulo $\theta = 56^\circ$, Cateto Opuesto ($CO$) = 10m.
1. **Hallar tercer ángulo:** $180^\circ - 90^\circ - 56^\circ = \mathbf{34^\circ}$.
2. **Hallar Hipotenusa ($H$):** Usamos Seno.
   $\sin(56^\circ) = \frac{10}{H} \implies H = \frac{10}{\sin(56^\circ)} \approx \mathbf{12.06m}$
3. **Hallar Cateto Adyacente ($CA$):** Usamos Tangente (usando el $CO$ original).
   $\tan(56^\circ) = \frac{10}{CA} \implies CA = \frac{10}{\tan(56^\circ)} \approx \mathbf{6.75m}$

### Ejemplo 2: Caso con Hipotenusa conocida
**Datos iniciales:** Ángulo $\theta = 37^\circ$, Hipotenusa ($H$) = 15m.
1. **Hallar tercer ángulo:** $90^\circ - 37^\circ = \mathbf{53^\circ}$.
2. **Hallar Cateto Adyacente ($CA$):** Usamos Coseno.
   $\cos(37^\circ) = \frac{CA}{15} \implies CA = 15 \cdot \cos(37^\circ) \approx \mathbf{11.98m}$
3. **Hallar Cateto Opuesto ($CO$):** Usamos Seno.
   $\sin(37^\circ) = \frac{CO}{15} \implies CO = 15 \cdot \sin(37^\circ) \approx \mathbf{9.03m}$

### Ejemplo 3: Caso Avanzado (Hallar Ángulo)
**Datos iniciales:** Cateto Opuesto = 6m, Cateto Adyacente = 10m.
1. **Hallar Ángulo ($\theta$):** Usamos la función inversa $\tan^{-1}$.
   $\tan(\theta) = \frac{6}{10} \implies \theta = \tan^{-1}(0.6) \approx \mathbf{30.96^\circ}$.
2. **Hallar tercer ángulo:** $90^\circ - 30.96^\circ = \mathbf{59.04^\circ}$.
3. **Hallar Hipotenusa ($H$):** Usamos Seno con el ángulo hallado.
   $\sin(30.96^\circ) = \frac{6}{H} \implies H = \frac{6}{\sin(30.96^\circ)} \approx \mathbf{11.66m}$.

### Ejemplo 4: Aplicación Real ($USD)
**Problema:** Una cuerda de soporte (hipotenusa) para un poste cuesta **$2.50 USD por metro**. Si la cuerda forma un ángulo de **45°** con el suelo y su base está a **5m** del poste (cateto adyacente):
- **Cálculo de longitud ($H$):** $\cos(45^\circ) = \frac{5}{H} \implies H = \frac{5}{\cos(45^\circ)} \approx \mathbf{7.07m}$.
- **Costo total:** $7.07m \times 2.50 USD = \mathbf{\$17.68 USD}$.

---

## 📝 Ejercicios para el Estudiante

```ad-abstract
title: 🟢 Nivel Fácil: Cálculo de Lados
1. Hallar la hipotenusa si $\theta = 30^\circ$ y $CO = 5m$.
2. Hallar el $CA$ si $\theta = 45^\circ$ e $H = 10m$.
3. Hallar el $CO$ si $\theta = 30^\circ$ e $H = 20m$.
4. Hallar la hipotenusa si $\theta = 45^\circ$ y $CA = 7m$.
```

```ad-abstract
title: 🟡 Nivel Medio: Hallar Ángulos (Funciones Inversas)
1. Hallar $\theta$ si $CO = 3m$ y $CA = 4m$.
2. Hallar $\theta$ si $CA = 8m$ e $H = 10m$.
3. Hallar $\theta$ si $CO = 5m$ e $H = 13m$.
4. Hallar $\theta$ si $CO = 10m$ y $CA = 10m$.
```

```ad-abstract
title: 🔴 Nivel Avanzado: Aplicaciones $USD
1. Una rampa de 15° requiere pasamanos a ambos lados. Si la base (CA) mide 8m y el material cuesta $12 USD/m, calcula el costo total (Hipotenusa $\times 2 \times precio$).
2. Un cable de 12m (H) se instala desde la cima de un poste con un ángulo de 60° respecto al suelo. Si el cable cuesta $4.50 USD/m, ¿cuál es el gasto total?
3. Un tejado inclinado 20° tiene un ancho de base (CA) de 6m. Si la teja cuesta $25 USD por metro lineal de hipotenusa, calcula el costo.
4. Se cerca un terreno triangular. Se conoce un ángulo de 37° y el cateto opuesto de 9m. Si la cerca cuesta $8 USD/m, calcula el costo de cercar solo la hipotenusa.
```

```ad-success
title: ✅ Respuestas para el Docente
**Fácil:** 1) 10m | 2) 7.07m | 3) 10m | 4) 9.90m.
**Medio:** 1) 36.87° | 2) 36.87° | 3) 22.62° | 4) 45°.
**Avanzado:** 
1) $198.77 (H=8.28m; 8.28 \times 2 \times 12)
2) $54.00 (12m \times 4.50)
3) $159.63 (H=6.385m; 6.385 \times 25)
4) $119.64 (H=14.955m; 14.955 \times 8)
```

---

## 🏁 Autoevaluación

> [!question] Pregunta 1
> ¿Cuál es la suma de los ángulos internos de cualquier triángulo?
> a) 90°
> b) 180°
> c) 360°
> d) 270°

> [!question] Pregunta 2
> Si tienes el Cateto Adyacente y buscas la Hipotenusa, ¿cuál es la razón trigonométrica más directa?
> a) Seno
> b) Tangente
> c) Coseno
> d) Cotangente

> [!question] Pregunta 3
> Si un cable de soporte (hipotenusa) forma un ángulo de 30° con el suelo y el poste mide 10m (cateto opuesto), ¿cuánto cuesta el cable si el metro vale $5 USD?
> a) $50.00 USD
> b) $100.00 USD
> c) $150.00 USD
> d) $200.00 USD

---

**Notas para el próximo tema:** Has dominado la resolución de triángulos con ángulos de 90°. En la siguiente unidad, daremos el salto a la **Trigonometría No Rectangular**, donde aprenderás las Leyes de Seno y Coseno para resolver cualquier triángulo que se te presente.

> [!info] 🧭 Navegación
> ◀ [[Clase 11 — Razones Trigonométricas]] | [[00 - Índice del curso]] | Siguiente tema: Trigonometría No Rectangular ▶