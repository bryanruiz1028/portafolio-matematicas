# Clase 03 — Pythagorean Theorem | Finding a leg + Teorema de Pitágoras | Encontrar un cateto

---
**Metadata**
- **Tags:** #algebra #pythagoreantheo
- **Curso:** [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 5
---

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | [[Clase 04|Clase 04 ➡]]

---

> [!info] 🌍 Relevancia y aplicaciones
> En esta clase aprenderás a calcular distancias desconocidas cuando ya conoces la medida más larga (la diagonal o hipotenusa). Esta técnica es fundamental cuando no puedes medir un lado directamente, pero tienes acceso a los otros dos.
> 
> **Puntos clave:**
> - 💵 **Aplicación USD:** Calcular el costo exacto de los materiales para cercar un terreno triangular si te falta conocer la medida de uno de sus linderos laterales.
> - 🏗️ **Aplicación práctica:** Si tienes una escalera de longitud fija (hipotenusa) y sabes a qué distancia de la pared la apoyas, puedes determinar con exactitud qué altura alcanzará en el muro (cateto).
> - 📊 **Situación cotidiana:** Calcular la distancia de una sombra proyectada en el suelo conociendo la altura del objeto y la distancia desde la punta del objeto hasta el extremo de la sombra.

---

> [!note] 📌 ¿Qué es Pythagorean Theorem? (Encontrar un cateto)
> Si tenemos un triángulo rectángulo y conocemos el lado más largo (la **hipotenusa**) y uno de los lados cortos (**cateto**), podemos descubrir cuánto mide el lado que falta. 
> 
> Conceptualmente, esto se logra mediante una **resta de áreas**: al área del cuadrado del lado más grande le quitamos el área del cuadrado del lado que ya conocemos para encontrar el área restante.

> [!warning] ⚠️ Error común
> ❌ **Incorrecto:** Sumar los cuadrados de los números siempre que veas un triángulo.
> ✅ **Correcto:** Si buscas un cateto (un lado que forma el ángulo recto), debes **restar** el cuadrado del cateto conocido al cuadrado de la hipotenusa. ¡Nunca restes la hipotenusa al cateto, o el resultado será un número negativo imposible de procesar en raíces!

> [!tip] 💡 Truco para recordarlo
> - ¿Buscas el lado **grande** (hipotenusa)? Haces una **suma**.
> - ¿Buscas un lado **chico** (cateto)? Haces una **resta**.

---

### 📋 Procedimiento paso a paso

```text
PASO 1: Identificar la hipotenusa (lado opuesto al ángulo recto) y el cateto conocido.
PASO 2: Elevar ambos valores al cuadrado. Al hacer esto, estamos obteniendo 
        el área de la superficie del cuadrado que se forma sobre cada lado.
PASO 3: Restar el área menor (cateto²) al área mayor (hipotenusa²). 
        La fórmula es: a² = c² - b²
PASO 4: Calcular la raíz cuadrada del resultado para obtener la medida final del cateto.
```

---

### 📝 Ejemplos guiados

#### Ejemplo 1: Básico (Números enteros)
*   **Datos:** Hipotenusa ($c$) = 5 unidades, Cateto conocido ($a$) = 3 unidades.
*   **Resolución:**
    1.  $x^2 = 5^2 - 3^2$
    2.  $x^2 = 25 - 9$
    3.  $x^2 = 16$
    4.  $x = \sqrt{16} = 4$
*   **Resultado:** El cateto mide **4 unidades**.

#### Ejemplo 2: Uso de precisión (Decimales)
*   **Datos:** Hipotenusa ($c$) = 14 unidades, Cateto conocido ($a$) = 10 unidades.
*   **Resolución:**
    1.  $x^2 = 14^2 - 10^2$
    2.  $x^2 = 196 - 100$
    3.  $x^2 = 96$
    4.  $x = \sqrt{96} \approx 9.79$
*   **Nota de redondeo:** En este curso, cuando el resultado no sea exacto, redondearemos a **dos decimales**.

#### Ejemplo 3: Avanzado (Precisión exacta)
*   **Datos:** Hipotenusa ($c$) = 15 cm, Cateto conocido ($a$) = 9 cm.
*   **Resolución:**
    1.  $15^2 = 225$
    2.  $9^2 = 81$
    3.  $225 - 81 = 144$
    4.  $\sqrt{144} = 12$
*   **Resultado:** El cateto mide **12 cm**.

#### Ejemplo 4: Aplicación de costos (USD)
*   **Situación:** Un cable de soporte mide 19 metros y cuesta $190. El poste mide 14 metros de altura. ¿A qué distancia de la base del poste se ancla el cable?
*   **Datos:** $c = 19$ m, $a = 14$ m.
*   **Resolución:**
    1.  $19^2 = 361$
    2.  $14^2 = 196$
    3.  $361 - 196 = 165$
    4.  $\sqrt{165} \approx 12.85$ (Redondeado de 12.845...)
*   **Resultado:** La distancia de la base es **12.85 metros**.

---

### ✏️ Ejercicios prácticos

> [!example] 🟢 Bloque Verde (Fácil)
> Calcula el cateto faltante (unidades enteras):
> 1. Hipotenusa = 10, Cateto = 6.
> 2. Hipotenusa = 13, Cateto = 12.
> 3. Hipotenusa = 5, Cateto = 4.
> 4. Hipotenusa = 25, Cateto = 7.

> [!todo] 🟡 Bloque Amarillo (Medio)
> Resuelve aplicando redondeo a dos decimales:
> 1. Hipotenusa = 15 m, Cateto = 10 m.
> 2. Hipotenusa = 8 cm, Cateto = 3 cm.
> 3. Hipotenusa = 20 unidades, Cateto = 12 unidades.
> 4. Hipotenusa = 11 m, Cateto = 7 m.

> [!danger] 🔴 Bloque Rojo (Avanzado - Aplicación)
> 1. Se requiere instalar un refuerzo diagonal de 26 metros en un muro de 24 metros de altura. ¿Qué distancia en el suelo ocupa el refuerzo? Si cada metro de riel de soporte para el suelo cuesta **$15 USD**, ¿cuál es el presupuesto total del riel?
> 2. Un terreno triangular tiene una diagonal de 47 cm y un lado conocido de 40 cm. Halla la medida del otro lado. Si el presupuesto para pintura perimetral es de **$3 USD por cada centímetro**, ¿cuánto costará pintar ese lado específico?

---

> [!check] ✅ Bloque de Éxito (Respuestas para el docente)
> - **Bloque Verde:** 1) 8; 2) 5; 3) 3; 4) 24.
> - **Bloque Amarillo:** 1) 11.18 m; 2) 7.41 cm; 3) 16 unidades; 4) 8.48 m.
> - **Bloque Rojo 1:** Cateto = 10 m. Costo total = **$150 USD**.
> - **Bloque Rojo 2:** Cateto = 26.68 cm (según fuente). Costo total = **$80.04 USD**.

---

### 🧠 Autoevaluación

1.  **¿Cuándo se debe realizar una resta en el Teorema de Pitágoras?**
    *   a) Siempre que trabajamos con triángulos rectángulos.
    *   b) Solo cuando queremos hallar el lado más largo (hipotenusa).
    *   c) Cuando conocemos la hipotenusa y buscamos uno de los catetos.
    *   d) Cuando los tres lados son iguales.
    *   *Respuesta: c. Se resta porque la incógnita es un lado corto, no el área total.*

2.  **Si una hipotenusa mide 5 y un cateto mide 3, ¿cuál es el procedimiento rápido?**
    *   $5^2 - 3^2 \rightarrow 25 - 9 = 16$. Raíz de 16 = **4**.

3.  **Problema:** Un cable de 10 metros se conecta desde la punta de un poste de 8 metros hasta el suelo. ¿A qué distancia de la base está el cable?
    *   $10^2 - 8^2 \rightarrow 100 - 64 = 36$. Raíz de 36 = **6 metros**.

---

> [!tip] 💡 En la próxima clase
> Ahora que dominas cómo encontrar cualquier lado de un triángulo rectángulo, en la **Clase 04** utilizaremos estos cálculos para resolver problemas combinados de la vida real mucho más complejos. ¡Sigue así!

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | [[Clase 04|Clase 04 ➡]]