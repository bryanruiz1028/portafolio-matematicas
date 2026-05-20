# Clase 03 — Can you solve these elementary school problems? | Equilateral Triangles + Isosceles Triangles + Fórmula de Herón + Características del triángulo

---
**ID:** CLASE_03
**Título:** Triángulos: Equiláteros, Isósceles y Fórmula de Herón
**Tags:** #matemáticas #geometría #triángulos #herón #educación_básica
**Anterior:** [[Clase 02 — Polígonos y Áreas]]
**Siguiente:** [[Clase 04 — Polígonos Compuestos]]

---

> [!info] 🌍 Relevancia y aplicaciones
> ¡Atención! Sin la estabilidad del triángulo, los edificios más altos del mundo simplemente se derrumbarían. Es la única figura geométrica que no se deforma bajo presión.
> - **Construcción:** Se utiliza en puentes y estructuras de techos para garantizar que la obra sea rígida y segura.
> - **Finanzas y Terrenos:** Calcular el costo de cercar un terreno depende del perímetro. Por ejemplo: cercar un lote de 32 metros lineales a un costo de **$15 USD** por metro requiere una inversión de **$480 USD**.
> - **Vida Cotidiana:** Desde calcular el área exacta de un jardín para comprar césped hasta el diseño de velas de barcos de alto rendimiento.

## 3. Concepto Clave: El Triángulo y sus Propiedades

> [!note] 📌 ¿Qué es un triángulo?
> Según el Profe Alex, un triángulo es una figura geométrica **plana** (2D) y **cerrada** formada por tres segmentos de recta. 
> 
> **¿Qué significa "puntos no colineales"?** 
> Imaginalo así: si pones tres puntos en una línea recta, solo obtienes una línea. Pero si mueves un punto fuera de esa línea, ¡tienes un triángulo! Esos tres puntos se llaman **vértices**.
> 
> **Nomenclatura Profesional:**
> - Se nombran por sus vértices con letras mayúsculas: **Triángulo ABC**.
> - También se usan letras griegas para sus ángulos o vértices: **$\alpha$ (alfa), $\beta$ (beta), $\theta$ (tita)**.

> [!warning] ⚠️ El Error de la Altura
> Muchos creen que la altura siempre corta la base por la mitad. **¡Cuidado!** El Profe Alex nos muestra con un "triángulo exagerado" (escaleno) que la altura puede caer muy cerca de un lado y lejos del otro. Esta división perfecta solo ocurre en triángulos **isósceles** y **equiláteros**.

> [!tip] 💡 Truco Mnemotécnico: El Rompecabezas de 180°
> No importa si el triángulo es flaco, alto o pequeño: si rompes sus tres esquinas (ángulos) y las unes, siempre formarán una línea recta perfecta. Por eso, la suma de los ángulos internos **siempre es 180°**.

## 4. Procedimiento: Cálculo del Área con Fórmula de Herón

Usa este método cuando conozcas los tres lados pero no la altura. **Importante:** El área siempre debe terminar en unidades cuadradas ($u^2, cm^2, m^2$).

```text
PASO 1: Identificar los tres lados (a, b, c).
PASO 2: Calcular el Perímetro (P = a + b + c).
PASO 3: Calcular el Semiperímetro (s = P / 2).
PASO 4: Aplicar la Fórmula de Herón: 
        Área = √[ s * (s - a) * (s - b) * (s - c) ]
        
Nota técnica: Dentro de la raíz, las unidades se elevan a la potencia 4 (m^4), 
lo que al final nos da el resultado correcto en unidades cuadradas (m^2).
```

## 5. Ejemplos Resueltos

> [!example] Ejemplo 1: Ecuaciones en Triángulos
> **Problema:** En un triángulo equilátero, un ángulo mide $2x$. Halla $x$.
> **Solución:** Como es equilátero, cada ángulo mide 60°.
> $2x = 60 \rightarrow x = 60/2 \rightarrow$ **$x = 30°$**.

> [!example] Ejemplo 2: Ángulos en Isósceles
> **Problema:** Un triángulo isósceles tiene un ángulo diferente de 40°. ¿Cuánto miden los otros dos?
> **Solución:** $180° - 40° = 140°$. Como los otros dos son iguales: $140 / 2 = 70°$.
> **Resultado:** Los ángulos faltantes miden **70° cada uno**.

> [!example] Ejemplo 3: Altura con Pitágoras
> **Problema:** Hallar la altura de un triángulo equilátero de lado 10 cm.
> **Explicación:** Podemos usar Pitágoras porque la altura de un triángulo equilátero crea dos **triángulos rectángulos iguales**.
> 1. La base de 10 cm se divide en dos partes de 5 cm.
> 2. $Hipotenusa^2 = Cateto1^2 + Cateto2^2 \rightarrow 10^2 = h^2 + 5^2$
> 3. $100 = h^2 + 25 \rightarrow 75 = h^2$
> 4. $h = \sqrt{75} \approx$ **8.66 cm**.

> [!example] Ejemplo 4: Aplicación en $USD
> **Problema:** Costo de cercar un terreno isósceles de lados 11 m, 11 m y base 10 m. Precio: **$15 USD/metro**.
> **Solución:**
> 1. Perímetro: $11 + 11 + 10 = 32 \text{ metros}$.
> 2. Costo: $32 \text{ m} \times 15 \text{ USD/m} = 480$.
> **Resultado:** Costo total de **$480 USD**.

## 6. Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Fácil
> 1. Si los vértices son D, E y F, ¿cómo se llama el triángulo?
> 2. Si un triángulo tiene ángulos de 90° y 30°, ¿cuánto mide el tercero?
> 3. ¿Cuántos vértices tiene un polígono de tres lados?
> 4. En un triángulo equilátero, un ángulo se representa como $3x$. ¿Cuál es el valor de $x$?

> [!abstract] 🟡 Nivel Medio
> 1. Un triángulo tiene lados de 5, 6 y 8 cm. Calcula su perímetro.
> 2. Con los mismos datos (5, 6, 8), halla el semiperímetro ($s$).
> 3. Aplica Herón para hallar el área de ese triángulo (lados 5, 6, 8 y $s = 9.5$).
> 4. En un triángulo equilátero, si uno de sus ángulos mide $2x + 5$, ¿cuánto vale $x$?

> [!abstract] 🔴 Nivel Avanzado
> 1. **Figura Compuesta:** Un cuadrado de lado 8 cm tiene un triángulo equilátero construido sobre su lado superior. ¿Cuál es el perímetro exterior de toda la figura?
> 2. **Ángulos:** En la figura anterior, halla el ángulo $EAB$ (formado por el lado del triángulo y el del cuadrado).
> 3. **Presupuesto:** Si el metro de valla cuesta **$20 USD**, ¿cuánto cuesta rodear la figura del ejercicio 1?
> 4. Halla el área de un triángulo equilátero de lado 10 cm usando la altura del Ejemplo 3 ($8.66 \text{ cm}$).

## 7. Respuestas y Autoevaluación

> [!success] Soluciones Detalladas
> - **Fácil:** 1. Triángulo $DEF$. 2. $60°$. 3. 3 vértices. 4. $x = 20$ ($3x = 60$).
> - **Medio:** 1. $19 \text{ cm}$. 2. $9.5 \text{ cm}$. 3. $\approx 14.98 \text{ cm}^2$ (No olvides la unidad cuadrada). 4. $x = 27.5$ ($2x + 5 = 60 \rightarrow 2x = 55$).
> - **Avanzado:**
>    1. **40 cm** (5 lados externos de 8 cm cada uno: 3 del cuadrado y 2 del triángulo).
>    2. **150°** (El ángulo del cuadrado es $90°$ y el del triángulo equilátero es $60°$; $90 + 60 = 150°$).
>    3. **$800 USD** (Perímetro 40 cm $\times$ $20 USD).
>    4. **43.3 cm²** (Base $10 \times$ Altura $8.66 / 2$).

> [!question] Mini-prueba
> 1. **¿Qué datos necesitas obligatoriamente para usar la Fórmula de Herón?**
>    - A) Base y altura | B) Los tres lados | C) Los tres ángulos.
> 2. **En un triángulo isósceles, si la altura divide la base en dos partes de 5 cm, ¿cuánto mide la base total?**
>    - A) 5 cm | B) 10 cm | C) 15 cm.
> 3. **Si cercar un terreno equilátero de lado 10 m cuesta $10 USD por metro, ¿cuál es el presupuesto total?**
>    - A) **$100 USD** | B) **$300 USD** | C) **$150 USD**.
>
> *Respuestas: 1-B, 2-B, 3-B (3 lados de 10m = 30m; 30m x $10 = $300).*

## 8. Notas de Cierre y Navegación Final

Hemos dominado las bases del triángulo, desde sus nombres en griego hasta el cálculo de áreas complejas con Herón. En la **Clase 04**, daremos el siguiente paso: aprenderemos a diseccionar polígonos compuestos más grandes.

---
**Anterior:** [[Clase 02 — Polígonos y Áreas]]
**Siguiente:** [[Clase 04 — Polígonos Compuestos]]
---