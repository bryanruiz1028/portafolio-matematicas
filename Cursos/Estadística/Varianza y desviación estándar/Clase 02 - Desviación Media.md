# Clase 02 — Desviación Media

#algebra #meandeviation

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 2

> [!info] 🧭 Navegación
> [[Clase 01 — Media Aritmética|« Anterior]] | [[00 - Índice del curso|Índice del curso]] | [[Clase 03 — Varianza y Desviación Estándar|Siguiente »]]

---

> [!info] 🌍 Relevancia y aplicaciones
> La desviación media es una medida de dispersión que nos indica, en promedio, qué tan alejados están los datos individuales respecto a la media aritmética del grupo. Es fundamental para entender la variabilidad de un conjunto de datos de forma sencilla.
> 
> - **💵 Aplicación $USD:** Permite analizar la variación de precios de la canasta básica en dólares durante un mes para detectar inestabilidad económica.
> - **🏗️ Aplicación práctica:** En control de calidad, ayuda a medir la tolerancia en milímetros de piezas fabricadas respecto a la medida estándar.
> - **📊 Situación cotidiana:** Sirve para comparar la consistencia de los puntajes de un jugador de videojuegos; una desviación media baja indica un desempeño muy regular.

---

> [!note] 📌 ¿Qué es Mean Deviation?
> Imagina que tienes un grupo de datos. La desviación media es el promedio de las distancias de cada uno de esos datos respecto a su media aritmética. Nos dice "qué tanto se separan" los números del centro.

> [!warning] ⚠️ Error común
> El error más frecuente es olvidar el **valor absoluto** al realizar las restas. Si restas y dejas signos negativos, la suma final podría dar cero o un valor incorrecto.
> 
> - **❌ Incorrecto:** $12 - 13.2 = -1.2$ (y sumar el valor negativo).
> - **✅ Correcto:** $|12 - 13.2| = 1.2$ (el resultado siempre debe ser positivo).

> [!tip] 💡 Truco para recordarlo
> Usa esta regla mnemotécnica: "**D**esviación es **D**istancia, y la distancia nunca es negativa".

---

### 4. Procedimiento Paso a Paso

Para calcular la Desviación Media ($DM$) en datos agrupados, sigue esta secuencia técnica:

```text
PASO 1: Calcular la media aritmética (x̄) sumando el producto de cada dato 
        por su frecuencia (x · f) y dividiendo entre el total de datos (N).
PASO 2: Calcular la marca de clase (x) si los datos se presentan en 
        intervalos (sumando los límites y dividiendo entre 2).
PASO 3: Hallar el valor absoluto de la resta entre cada dato (o marca 
        de clase) y la media: |x - x̄|.
PASO 4: Multiplicar cada resultado del paso anterior por su frecuencia (f).
        La suma de estos productos será el numerador de nuestra fórmula.
```

**Fórmula General:**
$$\displaystyle DM = \frac{\sum |x - \bar{x}| \cdot f}{N}$$

---

### 5. Ejemplos Resueltos

> [!example] Ejemplo 1: Datos Básicos (Edades)
> Se analizan las edades de 5 personas: 12, 13, 12, 14, 15.
> 1. **Media ($\bar{x}$):** $(12+13+12+14+15) / 5 = 66 / 5 = 13.2$ años.
> 2. **Desviaciones individuales ($|x - \bar{x}|$):** 
>    - $|12 - 13.2| = 1.2$
>    - $|13 - 13.2| = 0.2$
>    - $|12 - 13.2| = 1.2$
>    - $|14 - 13.2| = 0.8$
>    - $|15 - 13.2| = 1.8$
> 3. **Desviación Media:** $(1.2 + 0.2 + 1.2 + 0.8 + 1.8) / 5 = 5.2 / 5 = \mathbf{1.04}$ años.

> [!example] Ejemplo 2: Gestión de Signos
> En un cálculo de datos agrupados, si un dato $x$ es $13$ y la media $\bar{x}$ es $15.26$:
> - Operación: $13 - 15.26 = -2.26$.
> - Aplicación de valor absoluto: $|-2.26| = \mathbf{2.26}$.
> *Nota: Siempre transformamos el resultado negativo en positivo antes de multiplicar por la frecuencia.*

> [!example] Ejemplo 3: Datos en Intervalos (Avanzado)
> Estudio de edades de 20 personas ($N=20$) con media $\bar{x} = 42.25$.
> - Para el intervalo **30-35**, la marca de clase ($x$) es $(30+35)/2 = 32.5$.
> - Se calcula el producto $|x - \bar{x}| \cdot f$ para cada intervalo y se suma.
> - **Suma de productos ($\sum |x - \bar{x}| \cdot f$):** $77$
> - **Cálculo final:** $DM = 77 / 20 = \mathbf{3.85}$ años.

> [!example] Ejemplo 4: Aplicación Precios $USD
> Precios de suscripciones digitales: $3, 0, 1, 0, 2, 0, 1$ USD.
> 1. **Media ($\bar{x}$):** $7 / 7 = 1$ USD.
> 2. **Desviaciones absolutas:** $|3-1|=2$, $|0-1|=1$, $|1-1|=0$, $|0-1|=1$, $|2-1|=1$, $|0-1|=1$, $|1-1|=0$.
> 3. **Suma de desviaciones:** $2 + 1 + 0 + 1 + 1 + 1 + 0 = 6$.
> 4. **Desviación Media:** $6 / 7 \approx \mathbf{0.85}$ USD.

---

### 6. Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Fácil: Datos simples
> Hallar la desviación media de los siguientes conjuntos:
> 1. Datos: $5, 8, 10, 12$
> 2. Datos: $2, 4, 6, 8$
> 3. Datos: $10, 10, 10, 10$
> 4. Datos: $1, 5, 9$

> [!abstract] 🟡 Nivel Medio: Datos agrupados (Puntual)
> Calcula la DM utilizando las siguientes tablas de frecuencia:
> 
> | Ejercicio | $x$ (Dato) | $f$ (Frecuencia) |
> | :--- | :--- | :--- |
> | **1** | 5, 6 | 3, 4 |
> | **2** | 10, 12 | 2, 3 |
> | **3** | 2, 4 | 5, 5 |
> | **4** | 20, 25 | 1, 4 |

> [!abstract] 🔴 Nivel Avanzado: Finanzas $USD e Intervalos
> Calcula la DM de estos precios de acciones organizados en intervalos:
> 
> **1.**
> | Intervalo ($USD) | $f$ |
> | :--- | :--- |
> | [10 - 20] | 1 |
> | [20 - 30] | 3 |
> | [30 - 40] | 9 |
> 
> **2.** [0-10] $f=5$ | [10-20] $f=5$
> **3.** [100-110] $f=2$ | [110-120] $f=8$
> **4.** [5-15] $f=4$ | [15-25] $f=6$

> [!success] ✅ Respuestas
> **Fácil:** 1) 2.25 | 2) 2.0 | 3) 0.0 | 4) 2.66
> **Medio:** 1) 0.49 | 2) 0.96 | 3) 1.0 | 4) 1.6
> **Avanzado:** 1) **5.33** | 2) 5.0 | 3) 3.2 | 4) 4.8

---

### 7. Mini-Prueba de Autoevaluación

> [!question] Pregunta 1
> ¿Por qué es obligatorio utilizar el valor absoluto en la fórmula de la desviación media?
> > [!success] Respuesta
> > Porque si sumamos las desviaciones con sus signos originales (positivos y negativos), estas se cancelarían entre sí (sumando cero), impidiendo medir la magnitud real de la dispersión de los datos.

> [!question] Pregunta 2
> En un ejercicio con intervalos (ej. 20-30 años), ¿qué valor se usa para representar a la "x" en la fórmula?
> > [!success] Respuesta
> > Se utiliza la **Marca de Clase**, que es el punto medio del intervalo. Se calcula sumando los límites y dividiendo entre dos: $(20+30)/2 = 25$.

> [!question] Pregunta 3
> Calcula rápidamente la DM de los siguientes precios en dólares: $10$, $12$ y $14$ USD.
> > [!success] Respuesta
> > 1. Media: $(10+12+14)/3 = 12$.
> > 2. Desviaciones: $|10-12|=2$, $|12-12|=0$, $|14-12|=2$.
> > 3. DM: $(2+0+2)/3 = 4/3 = \mathbf{1.33}$ USD.

---

> [!tip] 💡 En la próxima clase
> Ahora que dominas cómo medir la dispersión simple con la desviación media, el siguiente paso es aprender la **Varianza y Desviación Estándar**, herramientas clave para análisis estadísticos más avanzados y precisos.

> [!info] 🧭 Navegación
> [[Clase 01 — Media Aritmética|« Anterior]] | [[00 - Índice del curso|Índice del curso]] | [[Clase 03 — Varianza y Desviación Estándar|Siguiente »]]