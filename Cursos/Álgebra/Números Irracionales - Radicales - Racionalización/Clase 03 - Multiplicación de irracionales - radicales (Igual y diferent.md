# Clase 03 — Multiplicación de irracionales - radicales (Igual y diferente índice)

#algebra #multiplicacinde

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 6

> [!info] 🧭 Navegación
> - **Anterior:** [[Clase 02]] — Suma y Resta de Radicales
> - **Siguiente:** [[Clase 04]] — División de Radicales y Racionalización Simple

¡Qué tal, amigas y amigos! Espero que estén muy bien. Hoy vamos a aprender a unir raíces mediante la multiplicación, un proceso que parece magia pero que sigue reglas muy claras. ¡Vamos a por ello!

---

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> En el mundo de las matemáticas exactas, trabajar con decimales infinitos genera errores acumulados. Multiplicar radicales nos permite mantener la precisión total hasta el final de un cálculo sin perder información por el camino.
> 
> - **💵 [USD]:** Se utiliza para calcular intereses compuestos exactos donde las tasas o periodos involucran raíces, asegurando que no se pierda ni un centavo por redondeo en transacciones bancarias.
> - **🏗️ [Aplicación práctica]:** Es vital para ingenieros al calcular diagonales y tensiones en estructuras. Es mucho más exacto decir $\sqrt{6}$ metros que usar una aproximación como $2.44$.
> - **📊 [Situación cotidiana]:** En diseño gráfico, se usa para ajustar dimensiones manteniendo la "Proportion Áurea" ($\frac{1+\sqrt{5}}{2}$), garantizando una armonía visual matemáticamente perfecta.

---

## Concepto clave

> [!note] 📌 ¿Qué es Multiplicación de irracionales - radicales?
> Multiplicar radicales consiste en "unirlos bajo un mismo techo" (el índice). Si las raíces tienen el mismo índice, simplemente multiplicamos sus contenidos (cantidades subradicales).
> 
> **Propiedad fundamental:** $\sqrt[n]{a} \cdot \sqrt[n]{b} = \sqrt[n]{a \cdot b}$

> [!warning] ⚠️ Error común
> ❌ **Error:** Multiplicar directamente radicales que tienen diferente índice (ejemplo: $\sqrt{2} \cdot \sqrt[3]{5} = \sqrt[5]{10}$). ¡Eso no se puede hacer!
> ✅ **Correcto:** Primero debemos hallar el **mínimo común múltiplo (mcm)** de los índices para igualarlos antes de cualquier multiplicación.

> [!tip] 💡 Truco para recordarlo
> "Si los índices son iguales, hay fiesta en la misma casa; si los índices son diferentes, necesitamos fabricar una llave común (el mcm) para poder abrir la puerta y entrar".

---

## Procedimiento paso a paso

Para multiplicar radicales con **índices diferentes** (el caso que requiere más cuidado), sigue estos pasos:

```text
PASO 1 → Identificar los índices y hallar el Mínimo Común Múltiplo (MCM).
PASO 2 → Amplificar cada radical: se multiplica el índice y el exponente 
         del subradical por el mismo número para alcanzar el MCM.
PASO 3 → Unir las cantidades subradicales en una sola raíz con el nuevo índice.
PASO 4 → Simplificar extrayendo factores si el exponente es mayor o igual al índice.
```

> [!tip] 💡 Consejo del Profe Alex: Descomposición previa
> Si tienes que multiplicar números grandes (como $\sqrt{12} \cdot \sqrt{60}$), no multipliques primero para que te dé $\sqrt{720}$. ¡Es muy difícil de simplificar! Es mejor **hallar los factores primos de cada número por separado** y luego unirlos. Así trabajarás con potencias pequeñas desde el inicio.

---

## Bloque de ejemplos prácticos

> [!example] Ejemplo 1: Multiplicación básica (Igual índice)
> Calcular: $\sqrt{2} \cdot \sqrt{3}$
> 
> **Resolución:**
> Como ambos son raíz cuadrada (índice 2), los unimos directamente:
> $\sqrt{2 \cdot 3} = \sqrt{6}$

> [!example] Ejemplo 2: Con coeficientes y simplificación
> Calcular: $2\sqrt{5} \cdot 5\sqrt{10}$
> 
> **Resolución:**
> 1. Multiplicamos los números de afuera: $2 \cdot 5 = 10$.
> 2. Descomponemos el 10 en factores primos: $10 = 2 \cdot 5$.
> 3. Unimos bajo la raíz: $10\sqrt{5 \cdot (2 \cdot 5)} = 10\sqrt{2 \cdot 5^2}$.
> 4. Simplificamos: El $5^2$ sale de la raíz como $5$.
>    $10 \cdot 5\sqrt{2} = 50\sqrt{2}$.

> [!example] Ejemplo 3: Diferente índice (Avanzado)
> Calcular: $\sqrt[3]{2^2} \cdot \sqrt{3^1}$
> 
> **Resolución:**
> 1. Los índices son 3 y 2. El **MCM es 6**.
> 2. **Amplificamos** para que ambos índices sean 6:
>    - Primera raíz: multiplicamos índice y exponente por 2 $\rightarrow \sqrt[3 \cdot 2]{2^{2 \cdot 2}} = \sqrt[6]{2^4}$.
>    - Segunda raíz: multiplicamos índice y exponente por 3 $\rightarrow \sqrt[2 \cdot 3]{3^{1 \cdot 3}} = \sqrt[6]{3^3}$.
> 3. Unimos: $\sqrt[6]{2^4 \cdot 3^3} = \sqrt[6]{16 \cdot 27} = \sqrt[6]{432}$.

> [!example] Ejemplo 4: Aplicación en USD
> Un panel solar triangular tiene una base de $2\sqrt{2}$ metros y una altura de $\sqrt{8}$ metros. Si el costo del material es de $1$ USD por metro cuadrado, ¿cuál es el costo total? (Área = $\frac{base \cdot altura}{2}$)
> 
> **Resolución:**
> 1. Multiplicamos base por altura: $(2\sqrt{2}) \cdot (\sqrt{8}) = 2\sqrt{2 \cdot 8} = 2\sqrt{16}$.
> 2. Calculamos la raíz: $2 \cdot 4 = 8$.
> 3. Aplicamos la fórmula del área (dividir entre 2): $8 / 2 = 4$ metros cuadrados.
> **Resultado:** El costo total es de $4$ USD.

---

## Ejercicios para el estudiante

> [!abstract] 🟢 Nivel Fácil (Igual índice)
> 1. $\sqrt{5} \cdot \sqrt{6}$
> 2. $\sqrt[3]{4} \cdot \sqrt[3]{2}$
> 3. $3\sqrt{2} \cdot 2\sqrt{7}$
> 4. $\sqrt{10} \cdot \sqrt{10}$

> [!abstract] 🟡 Nivel Medio (Requiere simplificación previa o posterior)
> 1. $\sqrt{12} \cdot \sqrt{3}$
> 2. $2\sqrt{18} \cdot \sqrt{2}$
> 3. $\sqrt[3]{9} \cdot \sqrt[3]{3}$
> 4. $5\sqrt{2} \cdot 3\sqrt{8}$

> [!abstract] 🔴 Nivel Avanzado (Diferente índice y Aplicación)
> 1. $\sqrt[3]{2} \cdot \sqrt[2]{2}$
> 2. $\sqrt[4]{3} \cdot \sqrt[2]{3}$
> 3. $\sqrt[3]{5^2} \cdot \sqrt[6]{5}$
> 4. Si una criptomoneda vale $\sqrt{2}$ USD y tienes $\sqrt[3]{2}$ unidades, ¿cuánto dinero tienes en total? (Expresa el resultado como una sola raíz).

> [!success] Respuestas para el docente
> **Fácil:** 
> 1) $\sqrt{30}$ 
> 2) $\sqrt[3]{8} = 2$ 
> 3) $6\sqrt{14}$ 
> 4) $\sqrt{100} = 10$
> 
> **Medio:** 
> 1) $\sqrt{36} = 6$ 
> 2) $2\sqrt{36} = 2 \cdot 6 = 12$ 
> 3) $\sqrt[3]{27} = 3$ 
> 4) $15\sqrt{16} = 15 \cdot 4 = 60$
> 
> **Avanzado:** 
> 1) $MCM(3,2)=6 \rightarrow \sqrt[3 \cdot 2]{2^{1 \cdot 2}} \cdot \sqrt[2 \cdot 3]{2^{1 \cdot 3}} = \sqrt[6]{2^2 \cdot 2^3} = \sqrt[6]{2^5} = \sqrt[6]{32}$
> 2) $MCM(4,2)=4 \rightarrow \sqrt[4]{3^1} \cdot \sqrt[2 \cdot 2]{3^{1 \cdot 2}} = \sqrt[4]{3^1 \cdot 3^2} = \sqrt[4]{3^3} = \sqrt[4]{27}$
> 3) $MCM(3,6)=6 \rightarrow \sqrt[3 \cdot 2]{5^{2 \cdot 2}} \cdot \sqrt[6]{5^1} = \sqrt[6]{5^4 \cdot 5^1} = \sqrt[6]{5^5} = \sqrt[6]{3125}$
> 4) $MCM(2,3)=6 \rightarrow \sqrt[6]{2^3} \cdot \sqrt[6]{2^2} = \sqrt[6]{2^5} = \sqrt[6]{32}$ USD.

---

## Mini-prueba de autoevaluación

> [!question] Pregunta 1: ¿Qué condición es indispensable para multiplicar dos radicales directamente sin procesos previos?
> **Respuesta:** Que tengan el mismo índice. En ese caso, se aplica la propiedad distributiva de la raíz respecto al producto: $\sqrt[n]{a} \cdot \sqrt[n]{b} = \sqrt[n]{a \cdot b}$.

> [!question] Pregunta 2: Si necesitas multiplicar $\sqrt[3]{x}$ por $\sqrt[4]{y}$, ¿cuál será el índice del resultado?
> a) 7
> b) 12
> c) 1
> **Respuesta:** b) 12. Se debe calcular el MCM de los índices 3 y 4, que es 12.

> [!question] Pregunta 3: Tienes un terreno cuadrado de lado $\sqrt{50}$ metros. El precio por metro cuadrado es de $2$ USD. ¿Cuál es el valor total del terreno?
> **Respuesta:** Primero hallamos el área multiplicando lado por lado: $\sqrt{50} \cdot \sqrt{50} = 50$ $m^2$. Luego multiplicamos por el precio: $50 \cdot 2 = 100$ USD.

---

## Notas para el próximo tema
En la **Clase 04**, utilizaremos lo aprendido hoy para realizar la operación inversa: la **División de Radicales**. También veremos cómo "limpiar" fracciones usando la **Racionalización simple**, un truco fundamental para que los resultados se vean más elegantes.

---

> [!info] 🧭 Navegación
> - **Anterior:** [[Clase 02]] — Suma y Resta de Radicales
> - **Siguiente:** [[Clase 04]] — División de Radicales y Racionalización Simple