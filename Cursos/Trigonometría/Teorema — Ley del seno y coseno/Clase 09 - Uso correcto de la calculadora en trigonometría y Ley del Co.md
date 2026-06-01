# Clase 09 — Uso correcto de la calculadora en trigonometría y Ley del Coseno: Encontrar un ángulo

**Tags:** #Trigonometría #LeyDelCoseno #CalculadoraCientífica #Geometría
**Curso:** Matemáticas | **Bloque:** Trigonometría | **Lección:** Resolución de Triángulos Oblicuángulos

> [!info] 🧭 Navegación
> [← Clase 08](link_clase_08) | [Índice General](link_indice) | [Finalizar Curso 🏁](link_fin)

---

## 🌍 Relevancia y aplicaciones

Calcular un ángulo con precisión no es solo un ejercicio de clase; en el mundo real, los grados determinan la estabilidad y el costo de grandes obras.

*   **$USD:** Un error de apenas $2^\circ$ en la inclinación de los techos de una nave industrial puede provocar que el agua no drene correctamente, obligando a reparaciones estructurales que superan los **$15,000 USD** en materiales.
*   **🏗️ Aplicación:** En ingeniería civil, la apertura exacta entre las vigas de soporte es lo que permite que un puente resista toneladas de peso sin colapsar.
*   **📊 Cotidiano:** Cada vez que usas Google Maps, tu teléfono calcula ángulos de trayectoria entre señales de satélites GPS para ubicarte con precisión de metros.

---

## Concepto Clave y Configuración de Calculadora

Para resolver un triángulo cuando conocemos sus tres lados ($LLL$), usamos la **Ley del Coseno**. Sin embargo, tu calculadora debe estar "hablando el mismo idioma" que tú.

> [!note] Configuración para Estudiantes (fx-82, 85, 350, 570)
> Tu calculadora científica tiene tres modos para medir ángulos:
> 1.  **$DEG$ (Degrees):** Grados sexagesimales (el que usaremos siempre). Una vuelta completa son $360^\circ$.
> 2.  **$RAD$ (Radians):** Radianes. Una vuelta completa son $2\pi$ radianes.
> 3.  **$GRA$ (Gradients):** Gradiantes. Una vuelta completa son $400$ gradianes.
> 
> **¿Cómo activar funciones amarillas?**
> Para encontrar un ángulo, necesitamos el **arco coseno** ($\cos^{-1}$). Fíjate que este símbolo está escrito en **amarillo** justo arriba de la tecla $[\cos]$. Por eso, para activarlo, **siempre** debes presionar primero la tecla $[Shift]$.

> [!warning] ⚠️ Error común: ¿GRA es Grados?
> ¡No! Es un error clásico. Muchos estudiantes ven la **G** de $GRA$ y piensan que es "Grados". Recuerda: **$GRA = 400$ unidades por vuelta**, mientras que **$DEG = 360$ unidades por vuelta**. Si tu calculadora muestra una **G** en la pantalla, tus cálculos fallarán. Debes ver siempre una **D** o la palabra **$DEG$**.

> [!tip] 💡 Truco para recordarlo: El ángulo "atrapado"
> En la fórmula para hallar el ángulo $A$, nota cómo los lados $b$ y $c$ aparecen "abrazando" al lado $a$ en el numerador y multiplicándose abajo. El ángulo que buscas siempre está **atrapado** por los dos lados que restan:
> $$A = \cos^{-1} \left( \frac{a^2 - \color{cyan}{b^2} - \color{cyan}{c^2}}{-2 \cdot \color{cyan}{b} \cdot \color{cyan}{c}} \right)$$

---

## Procedimiento paso a paso

Para obtener el ángulo exacto, sigue este algoritmo técnico:

```text
PASO 1 → Identificar y nombrar: Lados (a, b, c) y ángulos (A, B, C). 
         El lado 'a' DEBE ser el opuesto al ángulo 'A' que buscas.
PASO 2 → Configurar modo DEG: Presiona [Shift] + [Setup] + [3]. Asegúrate de ver la "D".
PASO 3 → Despeje de la fórmula: A = cos⁻¹( (a² - b² - c²) / (-2bc) )
PASO 4 → Ingreso en calculadora (Dos métodos):
         A) Modo Fracción (Recomendado): Presiona [Shift] + [cos], luego la tecla de 
            fracción [■/□]. Escribe el numerador arriba y el denominador abajo.
         B) Modo Lineal: Presiona [Shift] + [cos]. Abre doble paréntesis para 
            proteger la operación: ((a² - b² - c²) / (-2 * b * c))
PASO 5 → Conversión Final: El resultado saldrá en decimal (ej. 41.17). Para verlo 
         en formato profesional, presiona la tecla [° ' ''] (Grados, Minutos y Segundos).
```

---

## Ejemplos Prácticos

```ad-example
title: Ejemplo 1: Caso Básico (Lados $9$, $7$ y $13$)
Hallaremos el ángulo $A$ opuesto al lado $a=9$. Los otros lados son $b=7$ y $c=13$.
**Sustitución:** $A = \cos^{-1} \left( \frac{9^2 - 7^2 - 13^2}{-2 \cdot 7 \cdot 13} \right)$
**Uso de Shift:** Presionamos $[Shift] + [\cos]$ para abrir el arco coseno.
**Resultado decimal:** $41.17^\circ$
**Resultado en DMS:** Al presionar la tecla $[\circ \prime \prime \prime]$, obtenemos: $41^\circ 10' 15.9''$.
```

```ad-example
title: Ejemplo 2: Gestión de Signos
Si el numerador de tu fracción da un número menor que el denominador (o negativo), no te asustes. La calculadora gestionará el signo menos del $-2bc$ automáticamente. Si el resultado final del paréntesis es negativo, el ángulo será obtuso (mayor a $90^\circ$). ¡Confía en el proceso!
```

```ad-example
title: Ejemplo 3: Precisión con Decimales
Triángulo con lados: $12.5$, $8.2$ y $15.4$. Buscamos el ángulo mayor (opuesto a $15.4$).
**Operación:** $A = \cos^{-1} \left( \frac{15.4^2 - 12.5^2 - 8.2^2}{-2 \cdot 12.5 \cdot 8.2} \right)$
**Resultado preciso:** $\approx 93.82^\circ$. 
*(Nota: Si no usas los paréntesis correctamente en modo lineal, podrías obtener un error de sintaxis).*
```

```ad-example
title: Ejemplo 4: Aplicación Financiera de Terrenos
Un terreno triangular tiene lados de $20m$, $35m$ y $40m$. El costo por $m^2$ es de **$250 USD**. Para calcular el área, el arquitecto necesita el ángulo entre los lados de $20m$ y $35m$ (opuesto al lado de $40m$).
**Cálculo:** $A = \cos^{-1} \left( \frac{40^2 - 20^2 - 35^2}{-2 \cdot 20 \cdot 35} \right) = \cos^{-1} \left( \frac{-25}{-1400} \right)$
**Resultado:** $88.97^\circ$. Un error de redondeo aquí podría cambiar el cálculo del área y hacer perder al vendedor cientos de dólares.
```

---

## Ejercicios y Respuestas

```ad-abstract
title: 🟢 Nivel Fácil
Halla el ángulo $A$ de un triángulo con lados $a=5, b=6, c=7$.
```

```ad-abstract
title: 🟡 Nivel Medio
Un triángulo tiene lados de $22$ cm, $28$ cm y $15$ cm. Encuentra el ángulo opuesto al lado de $22$ cm. (Usa el modo fracción de tu calculadora).
```

```ad-abstract
title: 🔴 Nivel Avanzado
Un lote de construcción triangular tiene lados de $50m, 70m$ y $90m$. El valor del suelo es de **$150 USD** por $m^2$. 
1. Calcula el ángulo opuesto al lado de $90m$ en grados, minutos y segundos.
2. Si un topógrafo comete un error y usa $95^\circ$ en lugar del valor exacto, la diferencia de área resultaría en una pérdida de **$450 USD**. ¿Es el ángulo real mayor o menor a $95^\circ$?
```

```ad-success
title: Respuestas para el Docente
1. **Fácil:** $A = \cos^{-1} \left( \frac{5^2-6^2-7^2}{-2 \cdot 6 \cdot 7} \right) = 44.41^\circ$.
2. **Medio:** $A = \cos^{-1} \left( \frac{22^2-28^2-15^2}{-2 \cdot 28 \cdot 15} \right) = 51.31^\circ$ (o $51^\circ 19'$).
3. **Avanzado:** 
   - Ángulo: $A = \cos^{-1} \left( \frac{90^2-50^2-70^2}{-2 \cdot 50 \cdot 70} \right) = 95.73^\circ \rightarrow$ **$95^\circ 44' 21''$**.
   - El ángulo real es **mayor** a $95^\circ$, por lo que la precisión es vital para el cobro correcto.
```

---

## Autoevaluación

```ad-question
title: Pregunta 1
¿Qué modo debe mostrar la pantalla para trabajar con grados estándar en la escuela?
A) RAD
B) GRA
C) DEG
*Respuesta correcta: C (D de Degree).*
```

```ad-question
title: Pregunta 2
¿Para qué sirve la tecla [Shift] antes de presionar [cos]?
A) Para elevar el coseno a la potencia -1.
B) Para activar la función arco coseno (amarilla) y hallar ángulos.
C) Para borrar el cálculo anterior.
*Respuesta correcta: B.*
```

```ad-question
title: Pregunta 3
En una obra de **$500,000 USD**, un ingeniero ingresa en su calculadora: `cos-1 (9^2 - 7^2 - 13^2 / -2 * 7 * 13)`. ¿Por qué obtendrá un error?
A) Porque el lado 9 es muy pequeño.
B) Porque le faltan paréntesis para agrupar el numerador y el denominador.
C) Porque la calculadora no acepta números negativos.
*Respuesta correcta: B (Sin paréntesis o modo fracción, la calculadora solo divide el 13^2 entre -2).*
```

---

> [!tip] Conclusión de la Lección
> ¡Felicidades! Has dominado el uso técnico de la calculadora. Recuerda: la Ley del Coseno es tu mejor aliada cuando conoces todos los lados de un triángulo. Al usar correctamente las teclas $[Shift]$, $[\circ \prime \prime \prime]$ y los paréntesis, transformas una simple herramienta en un instrumento de precisión profesional.

> [!info] 🧭 Navegación
> [← Clase 08](link_clase_08) | [Índice General](link_indice) | [Finalizar Curso 🏁](link_fin)