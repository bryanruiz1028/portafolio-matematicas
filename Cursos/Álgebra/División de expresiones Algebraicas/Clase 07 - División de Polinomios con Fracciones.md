# Clase 07 — División de Polinomios con Fracciones

tags: #algebra #dividingpolynom
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 7 de 7

> [!info] 🧭 Navegación
> ◀ **Anterior:** [[Clase 06 — División de Polinomios Enteros]]
> 🔼 **Índice:** [[00 - Índice del curso]]

---

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> La división de polinomios con fracciones nos permite trabajar con expresiones que tienen "trozos" o partes de una unidad. Es la herramienta matemática necesaria para modelar reparticiones cuando las cantidades no encajan en números enteros exactos.
>
> *   **💵 $USD:** Permite calcular la distribución de un presupuesto total (dividendo) entre un grupo de beneficiarios (divisor) cuando existen tasas de interés o comisiones representadas por fracciones.
> *   **🏗️ Aplicación práctica:** En ingeniería civil, se usa para determinar dimensiones exactas y escalas de carga donde los materiales se miden en fracciones de metro o tonelada.
> *   **📊 Situación cotidiana:** Ajuste de proporciones en mezclas químicas de laboratorio o recetas industriales donde la precisión fraccionaria evita el desperdicio.

---

## Concepto Clave y Definición

> [!note] 📌 ¿Qué es la División de Polinomios con Fracciones?
> Es la operación de repartir una expresión algebraica cuyos coeficientes son "pedacitos de números" (como $\frac{1}{2}$, $\frac{1}{3}$ o $\frac{5}{36}$) entre otra expresión similar. Se basa en el mismo proceso de la división larga que ya conoces, pero requiere que operemos con numeradores y denominadores siguiendo las reglas de las fracciones.

> [!warning] ⚠️ Error común
> El error más grave es olvidar **cambiar el signo** al trasladar el resultado de la multiplicación debajo del dividendo. 
> *   **¿Por qué lo hacemos?** Porque en toda división, el paso siguiente a multiplicar es **restar**, y restar en álgebra equivale a sumar el opuesto (cambiar el signo).
> *   ❌ **Incorrecto:** Sumar directamente los términos sin transformar su signo.
> *   ✅ **Correcto:** Si la multiplicación da positiva, se escribe negativa; si da negativa, se escribe positiva.

> [!tip] 💡 Truco para recordarlo: "Quitar y Poner"
> Cuando no encuentres fácilmente por qué número multiplicar para convertir una fracción en otra, usa la lógica del "lado opuesto":
> 1. Para **quitar** un número que te estorba, ponlo en el lado opuesto (si está abajo, ponlo arriba).
> 2. Para **poner** el número que necesitas, colócalo en el mismo lado (si lo quieres abajo, ponlo abajo).
> *Ejemplo:* Para convertir $\frac{1}{3}$ en $\frac{1}{4}$, multiplicas por $\frac{3}{4}$. El 3 de arriba anula al 3 de abajo, y queda el 4 abajo.

---

## Procedimiento Paso a Paso

```text
PASO 1: ORDENAR los polinomios de forma descendente según una letra (ej. de a² a a¹ y finalmente el término independiente).
PASO 2: BUSCAR el término del cociente dividiendo el primer término del dividendo por el primero del divisor. Analiza numerador y denominador por separado.
PASO 3: MULTIPLICAR el término hallado por todo el divisor y colocar los resultados debajo de sus semejantes con el SIGNO CAMBIADO.
PASO 4: SUMAR/RESTAR las fracciones usando el método de CARITA FELIZ y bajar el siguiente término para repetir el ciclo.
```

---

## Ejemplos Prácticos

> [!example] Ejemplo 1: El primer paso (Básico)
> Queremos dividir $(\frac{1}{6} a^2 + \frac{5}{36} ab - \frac{1}{6} b^2) \div (\frac{1}{3} a + \frac{1}{2} b)$.
> 1. Dividimos el primer término: $\frac{1}{6} a^2 \div \frac{1}{3} a$.
> 2. **Numerador:** Tenemos 1 y queremos 1 $\rightarrow$ multiplicamos por $1$.
> 3. **Denominador:** Tenemos 3 y queremos 6 $\rightarrow$ multiplicamos por $2$.
> 4. **Letras:** Tenemos $a$ y queremos $a^2$ $\rightarrow$ falta $a$.
> **Resultado:** El primer término del cociente es $\frac{1}{2} a$.

> [!example] Ejemplo 2: El proceso de resta (Carita Feliz)
> Al multiplicar $\frac{1}{2} a$ (nuestro cociente) por el segundo término del divisor ($\frac{1}{2} b$), obtenemos $+\frac{1}{4} ab$. Lo pasamos como **$-\frac{1}{4} ab$**.
> Ahora operamos: $\frac{5}{36} ab - \frac{1}{4} ab$.
> *   **Denominador común (36 × 4):** $144$.
> *   **Multiplicación en cruz:** $(5 \times 4) - (1 \times 36) = 20 - 36 = -16$.
> *   **Resultado:** $\frac{-16}{144} ab$, que al simplificar (mitad de mitad...) nos da **$-\frac{1}{9} ab$**.

> [!example] Ejemplo 3: Sub-proceso de "Quitar y Poner"
> Si en un paso necesitas convertir $\frac{2}{3}$ en $\frac{5}{2}$:
> 1. **Quitar el 2 de arriba:** Pones un $2$ abajo.
> 2. **Poner el 5 arriba:** Pones un $5$ arriba.
> 3. **Quitar el 3 de abajo:** Pones un $3$ arriba.
> 4. **Poner el 2 abajo:** Pones un $2$ abajo.
> **Factor final:** $\frac{5 \times 3}{2 \times 2} = \frac{15}{4}$.
> *Prueba:* $\frac{2}{3} \times \frac{15}{4} = \frac{30}{12} = \frac{5}{2}$. ¡Funciona!

> [!example] Ejemplo 4: Aplicación de presupuesto ($USD)
> Un fondo de inversión de $\frac{1}{6} x^2$ dólares (donde $x$ es el capital base) debe distribuirse entre un grupo definido por $(\frac{1}{3} x + \frac{1}{2} y)$. 
> Siguiendo la lógica del Ejemplo 1, si asignamos la categoría de riesgo $x$ al primer término, el desembolso inicial por beneficiario será de **$\frac{1}{2} x$** dólares. Esto asegura que el capital se reparta proporcionalmente según el peso de cada variable financiera.

---

## Ejercicios y Autoevaluación

### 🟢 Nivel Fácil: Fracciones Homogéneas
1. $\frac{9}{4} a - \frac{3}{4} a =$ ? (Simplifica el resultado final).
2. $\frac{2}{7} x^2 + \frac{5}{7} x^2 =$ ?

### 🟡 Nivel Medio: Fracciones Heterogéneas y Factores
1. Resuelve $\frac{1}{6} + \frac{2}{3}$ usando el método de carita feliz (muestra el denominador común).
2. Encuentra el factor para convertir $\frac{1}{3}$ en $-\frac{1}{9} b$.

### 🔴 Nivel Avanzado: Reto Final
1. Resuelve la división completa que el Profe Alex propuso para practicar:
   $(\frac{1}{3} x^2 + \frac{7}{36} xy - \frac{1}{6} y^2) \div (\frac{1}{2} x + \frac{1}{3} y)$

### ✅ Respuestas
*   **Fácil:** 1) $\frac{6}{4} a = \frac{3}{2} a$ | 2) $\frac{7}{7} x^2 = 1x^2$.
*   **Medio:** 1) $\frac{3 + 12}{18} = \frac{15}{18} = \frac{5}{6}$ | 2) $-\frac{1}{3} b$.
*   **Avanzado:** Cociente: $\frac{2}{3} x - \frac{1}{2} y$; Residuo: $0$.

---

## Cierre y Próximos Pasos

### 🧪 Mini-prueba
1. **¿Qué se debe hacer con los términos resultantes de la multiplicación antes de sumarlos al dividendo?**
   a) Dejarlos con su signo original.
   b) Cambiarles el signo (positivo a negativo y viceversa).
   c) Multiplicarlos por el denominador común.

2. **En el método de "Carita Feliz" para $\frac{5}{36} - \frac{1}{4}$, ¿cuál es el denominador antes de simplificar?**
   a) 36
   b) 4
   c) 144

3. **Si en una aplicación financiera la división no es exacta y queda un "sobrante", este se conoce como:**
   a) Divisor.
   b) Residuo (o excedente).
   c) Cociente.

> [!tip] 💡 En la próxima clase
> Ahora que dominas las fracciones, estamos listos para entrar al mundo de la **División Sintética (Regla de Ruffini)**, un método ultra rápido para dividir polinomios cuando el divisor es sencillo.

> [!info] 🧭 Navegación
> ◀ **Anterior:** [[Clase 06 — División de Polinomios Enteros]]
> 🔼 **Índice:** [[00 - Índice del curso]]