# Clase 03 — Can you solve these elementary school problems? | Equilateral Triangles + Isosceles Triangles + Área del triángulo | Fórmula de Herón + Características del triángulo

---
**Navegación:**
[« Clase 02 — Triángulos: Clasificación y Propiedades](clase-02) | [Clase 04 — Polígonos y Relaciones Trigonométricas »](clase-04)

---

## RELEVANCIA Y APLICACIONES (¿Por qué es importante esta clase?)

El triángulo es la figura más estable en la naturaleza y la ingeniería; no se deforma bajo presión, lo que lo convierte en el bloque de construcción fundamental de la lógica geométrica y estructural.

*   **Costo de Terrenos ($USD):** En el mundo real, los terrenos no siempre son rectángulos perfectos. Saber calcular el área de parcelas triangulares es vital para determinar su valor exacto en el mercado inmobiliario ($USD/m²).
*   **Ingeniería y Arquitectura:** Desde las cerchas de un techo hasta los grandes puentes colgantes, los triángulos distribuyen las cargas para evitar colapsos.
*   **Navegación y Topografía:** La triangulación permite medir distancias a puntos inaccesibles (como la cima de una montaña o un barco en el mar) usando solo ángulos y un lado conocido.

---

## CONCEPTO CLAVE (Concepto clave)

> [!info] **¿Qué es un triángulo?**
> Es un polígono cerrado de dos dimensiones (2D) formado por tres segmentos de recta que se unen en tres **puntos no colineales** (puntos que no están en la misma línea recta) llamados **vértices**.
> *   **Propiedad fundamental:** La suma de sus tres ángulos internos siempre es exactamente **180°**.
> *   **Notación Matemática:** Los vértices se nombran con letras mayúsculas ($A, B, C$) y el triángulo se identifica con el símbolo delta: $\Delta ABC$. También se pueden usar letras griegas ($\alpha, \beta, \theta$) para sus ángulos.

> [!warning] **Error Común: La altura y la base**
> No asumas que la altura siempre cae en el centro de la base. Esto **solo ocurre** en los triángulos equiláteros e isósceles. En un triángulo escaleno, la altura puede caer incluso fuera de la base o dividirla en partes desiguales.

> [!tip] **Mnemotecnia para recordar tipos**
> *   **Equi**látero: Piensa en "Equidad" (Igualdad). Todos sus 3 lados y 3 ángulos son iguales (60° cada uno).
> *   **Isó**sceles: Imagina dos "piernas" iguales. Tiene 2 lados iguales y 2 ángulos iguales.

---

## PROCEDIMIENTO PASO A PASO: ÁREA CON FÓRMULA DE HERÓN

Cuando conocemos los tres lados ($a, b, c$) pero no tenemos la altura, seguimos estos pasos técnicos:

1.  **PASO 1 (Perímetro):** Suma las longitudes de los tres lados: $P = a + b + c$.
2.  **PASO 2 (Semiperímetro):** Calcula la mitad del perímetro: $s = P / 2$.
3.  **PASO 3 (Estructura de Herón):** Aplica la fórmula sustituyendo los valores: $\sqrt{s \cdot (s-a) \cdot (s-b) \cdot (s-c)}$.
4.  **PASO 4 (Unidades y Raíz):** Extrae la raíz cuadrada. **Nota técnica:** Recuerda que las unidades también se operan; al multiplicar cuatro longitudes ($m \cdot m \cdot m \cdot m$) obtenemos $m^4$, y al aplicar la raíz cuadrada, el resultado final queda correctamente expresado en unidades cuadradas ($m^2$).

---

## BLOQUE DE EJEMPLOS

````ad-example
**Ejemplo 1: Ángulos en Equiláteros (Básico)**
En un triángulo equilátero, uno de sus ángulos se expresa como $2x$. ¿Cuál es el valor de $x$?
*   **Lógica:** Todo triángulo equilátero tiene ángulos internos de 60°.
*   **Ecuación:** $2x = 60$.
*   **Solución:** $x = 30°$.
````

````ad-example
**Ejemplo 2: Isósceles y Ángulos Opuestos (Signos)**
Un triángulo isósceles tiene un ángulo exterior de 110° en un vértice de la base. Halla sus ángulos internos.
*   **Lógica:** El ángulo interno suplementario es $180° - 110° = 70°$.
*   **Propiedad Isósceles:** Los **ángulos opuestos a los lados iguales son iguales**. Si un ángulo de la base es 70°, el otro ángulo de la base también es 70°.
*   **Tercer ángulo:** $180° - (70° + 70°) = 40°$.
*   **Resultado:** Los ángulos son 70°, 70° y 40°.
````

````ad-example
**Ejemplo 3: Cálculo con Herón (Avanzado)**
Calcula el área de un triángulo con lados de 5m, 6m y 8m.
*   **Paso 1 (Perímetro):** $5 + 6 + 8 = 19m$.
*   **Paso 2 (s):** $s = 19 / 2 = 9.5m$.
*   **Paso 3 (Fórmula):** $\sqrt{9.5 \cdot (9.5-5) \cdot (9.5-6) \cdot (9.5-8)} = \sqrt{9.5 \cdot 4.5 \cdot 3.5 \cdot 1.5}$.
*   **Paso 4:** $\sqrt{224.4375 m^4} \approx 14.98 m^2$.
````

````ad-example
**Ejemplo 4: Aplicación Inmobiliaria ($USD)**
Un jardín triangular tiene lados de 10m, 11m y 11m. Si el césped cuesta $5 USD/m², ¿cuál es el costo total?
*   **Área:** Aplicando Herón, el área es $48.98 m^2$.
*   **Costo:** $48.98 m^2 \times 5 USD/m^2 = 244.90$.
*   **Resultado:** El costo total es $244.90 USD.
````

---

## EJERCICIOS PARA EL ESTUDIANTE

> [!question] **Fácil (Conceptos)**
> 1. Define qué son "puntos no colineales" en el contexto de un triángulo.
> 2. Si un triángulo se llama $\Delta PQR$, ¿cuáles son los nombres de sus vértices?
> 3. ¿Cuál es el valor exacto de la suma de los ángulos internos?
> 4. ¿Qué característica distingue a un triángulo isósceles de uno equilátero?

> [!question] **Medio (Cálculos)**
> 1. Un triángulo isósceles tiene un ángulo de 100° (el ángulo diferente). ¿Cuánto miden los ángulos de la base?
> 2. Si un triángulo equilátero tiene un perímetro de 36 cm, ¿cuánto mide cada lado?
> 3. **Visualización:** Se construye un triángulo equilátero sobre el lado superior de un cuadrado de 8 cm. ¿Cuál es el perímetro del borde exterior de la figura total?
> 4. Halla $x$ si un ángulo de un triángulo equilátero mide $2x + 10$.

> [!question] **Avanzado (Aplicación $USD)**
> 1. Un terreno tiene lados de 6m, 8m y 10m. Si el $m^2$ cuesta $50 USD, ¿cuánto vale el terreno? (Pista: Es un triángulo rectángulo, pero usa Herón para comprobar).
> 2. Una pared triangular de 5m, 5m y 6m será pintada. Si el costo es $12 USD/m², ¿cuál es el presupuesto?
> 3. Un artesano cobra $2 USD por $cm^2$ de bronce. ¿Cuánto cuesta una placa triangular de lados 3cm, 4cm y 5cm?
> 4. El vidrio para una mesa triangular de lados 7m, 8m y 9m cuesta $100 USD por $m^2$. ¿Cuál es el precio del vidrio?

````ad-success
**Respuestas (Clave para el docente)**
*   **Fácil:** 1) Puntos que no forman una línea recta. 2) P, Q y R. 3) 180°. 4) El isósceles tiene solo 2 lados iguales; el equilátero tiene los 3.
*   **Medio:** 1) 40° cada uno. 2) 12 cm. 3) 40 cm (5 lados de 8 cm). 4) $x=25$.
*   **Avanzado:** 1) Área=24 m², Total $1,200 USD. 2) Área=12 m², Total $144 USD. 3) Área=6 cm², Total $12 USD. 4) Área=26.83 m², Total $2,683 USD.
````

---

## AUTOEVALUACIÓN (MINI-PRUEBA)

1. **Conceptual:** En un triángulo $\Delta ABC$, el ángulo A mide 90° y el B mide 30°. ¿Cuánto mide el ángulo C? (Respuesta: 60°).
2. **Procedimental:** Calcula el semiperímetro ($s$) de un triángulo con lados de 6, 8 y 10. (Respuesta: 12).
3. **Aplicación $USD:** Un cartel triangular tiene un área de $20 m^2$. Si el costo por $m^2$ es de $10 USD, ¿cuál es el precio total? (Respuesta: $200 USD).

---

## NOTAS FINALES
En la próxima sesión (**Clase 04**), dejaremos atrás los tres lados para explorar polígonos con más ángulos y descubriremos cómo las relaciones trigonométricas nos permiten resolver problemas sin necesidad de conocer todos los lados.

---
**Navegación:**
[« Clase 02 — Triángulos: Clasificación y Propiedades](clase-02) | [Clase 04 — Polígonos y Relaciones Trigonométricas »](clase-04)

---
⬇️⬇️⬇️ SEPARADOR_GUIA_ESTUDIO ⬇️⬇️⬇️

### RESUMEN DE PROPIEDADES
*   **Triángulo Equilátero:** 3 lados congruentes. Sus 3 ángulos siempre son de 60°. La altura biseca (divide en dos) la base.
*   **Triángulo Isósceles:** 2 lados congruentes. Los ángulos opuestos a estos lados son iguales.
*   **Puntos no colineales:** Requisito indispensable para que los tres segmentos formen un área cerrada y no una simple línea.

> [!abstract] **CAJA DE FÓRMULAS MAESTRAS**
> *   **Perímetro ($P$):** $a + b + c$
> *   **Semiperímetro ($s$):** $P / 2$
> *   **Área (Fórmula de Herón):** $\text{Área} = \sqrt{s(s - a)(s - b)(s - c)}$
> *   **Unidades de Área:** Siempre se expresan al cuadrado (ej. $m^2, cm^2$).

### EJEMPLO ADICIONAL: ALTURA Y PITÁGORAS
En un triángulo equilátero de lado 10 cm, podemos hallar la altura ($h$) sin usar Herón, aplicando el Teorema de Pitágoras ($a^2 + b^2 = c^2$) en una de sus mitades:
1.  **Hipotenusa ($c$):** 10 cm (el lado del triángulo).
2.  **Base del cateto ($b$):** 5 cm (la mitad de la base original).
3.  **Cálculo:** $h^2 + 5^2 = 10^2 \rightarrow h^2 + 25 = 100 \rightarrow h^2 = 75$.
4.  **Resultado:** $h = \sqrt{75} \approx 8.66$ cm.

### EJERCICIOS DE REPASO FINAL
1. Usa Herón para hallar el área de un triángulo con lados 13, 14 y 15.
2. Un triángulo equilátero tiene un perímetro de 45 cm. Determina la medida de cada lado.
3. Si un ángulo de la base de un triángulo isósceles mide 45°, ¿cuánto mide el ángulo superior? ¿Es un triángulo rectángulo?
4. Calcula el semiperímetro ($s$) de un triángulo con lados de 12m, 15m y 21m.
5. Verifica con Herón si el área de un triángulo de lados 3, 4 y 5 es efectivamente 6 unidades cuadradas.