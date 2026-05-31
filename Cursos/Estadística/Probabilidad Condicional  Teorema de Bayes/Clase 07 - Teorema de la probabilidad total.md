# Clase 07 — Teorema de la probabilidad total

#algebra #teoremadelaprob
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 7 de 9

> [!info] 🧭 Navegación
> [[Clase 06 — Regla de la multiplicación]] | [[00 - Índice del curso]] | [[Clase 08 — Teorema de Bayes]]

> [!info] 🌍 Relevancia y aplicaciones
> El Teorema de la Probabilidad Total nos permite calcular la probabilidad de un evento final que puede ocurrir a través de múltiples causas o "caminos" **mutuamente excluyentes**.
> - **💵 [aplicación con $USD]:** Evaluación de riesgos bancarios para determinar la probabilidad de impago de bonos corporativos según distintos escenarios macroeconómicos.
> - **🏗️ [aplicación práctica]:** Control de calidad en manufactura, calculando la probabilidad de que una pieza sea defectuosa cuando es producida por diferentes máquinas con distintas tasas de error.
> - **📊 [situación cotidiana]:** Estimación de la probabilidad de aprobar un examen basándose en si el alumno cumplió o no con sus hábitos de estudio.

> [!note] 📌 ¿Qué es Teorema de la probabilidad total?
> Para un niño de 12 años: "Es como sumar todos los caminos posibles que te llevan a un mismo destino". 
> 
> **Nota del Especialista:** La diferencia clave con la regla de la multiplicación es el **orden**. Si el problema pide un orden exacto (ej. "primero azul y luego verde"), usamos multiplicación simple. Si el problema pide el resultado "en cualquier orden" o a través de diferentes causas iniciales, debemos usar la **Probabilidad Total** para sumar todas esas rutas posibles.

> [!warning] ⚠️ Error común
> **❌ Incorrecto:** Multiplicar solo una rama del diagrama de árbol y darla como resultado final.
> **✅ Correcto:** Multiplicar las probabilidades de cada camino y luego **sumar** los resultados de todos los caminos que cumplen la condición.
> **💡 Tip Pro:** Antes de empezar, verifica siempre que la suma de las probabilidades de las causas iniciales (las primeras ramas) sea igual a 1 (100%). Si no suman 1, el planteamiento es incorrecto.

> [!tip] 💡 Truco para recordarlo
> Los **Caminos** (ramas individuales) se multiplican para hallar su peso específico, y los **Destinos** (resultados finales deseados) se suman para obtener el total.

---

### Procedimiento Paso a Paso

```text
PASO 1 → Identificar los eventos principales (causas iniciales) y el evento resultante.
PASO 2 → Dibujar un diagrama de árbol asignando probabilidades (decimales o fracciones).
PASO 3 → Multiplicar las probabilidades a lo largo de cada "camino" (rama) que 
         conduzca al evento deseado (Probabilidad Conjunta).
PASO 4 → Sumar los resultados de todos los caminos identificados para obtener 
         la Probabilidad Total.
```

---

### Ejemplos Prácticos

````ad-example
title: Ejemplo 1 — Extracción con reemplazo
**Problema:** En una urna hay 5 esferas azules, 2 rojas y 1 verde. Si se extraen dos esferas con reemplazo, ¿cuál es la probabilidad de sacar una azul y una verde en cualquier orden?

**Solución:** Al haber reemplazo, los eventos son **independientes**.
1. **Camino 1 (Azul $\cdot$ Verde):** $(\frac{5}{8}) \cdot (\frac{1}{8}) = \frac{5}{64}$
2. **Camino 2 (Verde $\cdot$ Azul):** $(\frac{1}{8}) \cdot (\frac{5}{8}) = \frac{5}{64}$
**Suma total:** $\frac{5}{64} + \frac{5}{64} = \frac{10}{64} = \mathbf{0,1562}$ (**15,62%**).
````

````ad-example
title: Ejemplo 2 — Extracción sin reemplazo
**Problema:** Con la misma urna (5A, 2R, 1V), calcula la probabilidad de sacar una azul y una verde **sin reemplazo**.

**Solución:** Aquí existe una **dependencia** de sucesos; el denominador cambia porque el total de esferas disminuye.
1. **Camino 1 (Azul $\cdot$ Verde):** $(\frac{5}{8}) \cdot (\frac{1}{7}) = \frac{5}{56}$
2. **Camino 2 (Verde $\cdot$ Azul):** $(\frac{1}{8}) \cdot (\frac{5}{7}) = \frac{5}{56}$
**Suma total:** $\frac{5}{56} + \frac{5}{56} = \frac{10}{56} \approx \mathbf{0,1785}$ (**17,85%**).
````

````ad-example
title: Ejemplo 3 — Escenario Corporativo (Sr. Gómez)
**Problema:** El Sr. Gómez espera ser nombrado gerente. La probabilidad de que abran una sucursal ($A$) es 0,6. Si se abre, su probabilidad de nombramiento ($N$) es 0,7. Si no se abre ($A^c$), es 0,1.

**Solución Técnica:**
Usamos la notación $P(N) = P(A) \cdot P(N|A) + P(A^c) \cdot P(N|A^c)$
1. **Camino A (Abre y es nombrado):** $0,6 \cdot 0,7 = 0,42$
2. **Camino B (No abre y es nombrado):** $0,4 \cdot 0,1 = 0,04$
**Probabilidad Total:** $0,42 + 0,04 = \mathbf{0,46}$ (**46%**).
````

````ad-example
title: Ejemplo 4 — Aplicación real con $USD
**Problema:** Una empresa tiene el 70% de su capital en el **Fondo A** y el 30% en el **Fondo B**. El **Fondo A** tiene un 10% de probabilidad de dar un bono de **$500 USD**. El **Fondo B** tiene un 20% de probabilidad. ¿Cuál es la probabilidad de recibir el bono?

**Solución:**
1. **Fondo A:** $0,70 \cdot 0,10 = 0,07$
2. **Fondo B:** $0,30 \cdot 0,20 = 0,06$
**Total:** $0,07 + 0,06 = \mathbf{0,13}$ (**13%**). El valor del bono (**$500 USD**) es el premio asociado a la probabilidad.
````

---

### Ejercicios para el Estudiante

````ad-abstract
title: 🟢 Nivel Fácil
En una urna con 4 esferas azules y 4 rojas, se extraen dos esferas **con reemplazo**. Calcula la probabilidad de obtener una de cada color en cualquier orden.
````

````ad-abstract
title: 🟡 Nivel Medio (Manufactura)
Una fábrica utiliza dos máquinas. La Máquina 1 produce el 60% de las piezas con un 2% de defectos. La Máquina 2 produce el 40% restante con un 5% de defectos. Calcula la probabilidad total de que una pieza elegida al azar sea defectuosa.
````

````ad-abstract
title: 🟡 Nivel Medio (Urnas)
En la misma urna de 4 azules y 4 rojas, se extraen dos esferas **sin reemplazo**. Calcula la probabilidad de que la segunda esfera sea roja. (Pista: considera los dos caminos: Roja-Roja y Azul-Roja).
````

````ad-abstract
title: 🔴 Nivel Avanzado (Presupuesto Educativo)
Un estudiante sabe que si realiza sus tareas (probabilidad 0,8), tiene un 90% de aprobar. Si no las hace, tiene un 70% de aprobar. Si aprueba, gana una beca de **$1.000 USD**. 
1. ¿Cuál es la probabilidad total de aprobar? 
2. ¿Es estadísticamente más probable recibir la beca de **$1.000 USD** o perderla?
````

````ad-success
title: ✅ Soluciones
1. **Fácil:** $(4/8 \cdot 4/8) + (4/8 \cdot 4/8) = 16/64 + 16/64 = 32/64 = \mathbf{0,5}$ (50%).
2. **Medio (Máquinas):** $(0,6 \cdot 0,02) + (0,4 \cdot 0,05) = 0,012 + 0,020 = \mathbf{0,032}$ (3,2%).
3. **Medio (Urnas):** $(4/8 \cdot 3/7) + (4/8 \cdot 4/7) = 12/56 + 16/56 = 28/56 = \mathbf{0,5}$ (50%).
4. **Avanzado:** 1. $(0,8 \cdot 0,9) + (0,2 \cdot 0,7) = 0,72 + 0,14 = \mathbf{0,86}$ (86%). 2. Es más probable recibirla (86% vs 14%).
````

---

### Mini-Prueba de Autoevaluación

````ad-question
title: Pregunta 1
¿Cuál es la condición necesaria para que podamos sumar los resultados de diferentes caminos?
- A) Que los eventos sean independientes.
- B) Que los eventos sean **mutuamente excluyentes** (no pueden ocurrir al mismo tiempo).
- C) Que la probabilidad de cada rama sea mayor a 0,5.

**Respuesta:** B. Sumamos porque los caminos representan opciones alternativas que no se solapan.
````

````ad-question
title: Pregunta 2
En el Ejemplo 2 (sin reemplazo), ¿por qué se dice que hay **dependencia**?
- A) Porque el total de la urna cambia tras la primera extracción.
- B) Porque siempre se sacan esferas del mismo color.
- C) Porque el resultado no se puede calcular con decimales.

**Respuesta:** A. La probabilidad del segundo suceso **depende** de lo que ocurrió en el primero (quedan menos esferas).
````

````ad-question
title: Pregunta 3
Si en el Ejemplo 4, el Fondo A gestionara el 100% del capital con un 10% de probabilidad de bono de **$500 USD**, ¿cuál sería la probabilidad total?
- A) 100%
- B) 50%
- C) 10%

**Respuesta:** C. Si solo hay una vía, la probabilidad total es igual a la probabilidad de esa única vía ($1,0 \cdot 0,10 = 0,10$).
````

---

> [!tip] 💡 En la próxima clase
> Estudiaremos el **Teorema de Bayes**. Este utiliza el cálculo de la **Probabilidad Total** como su **denominador** para realizar inferencias inversas (ej. "Sabiendo que hubo un error, ¿qué probabilidad hay de que viniera de la Máquina 2?").

> [!info] 🧭 Navegación
> [[Clase 06 — Regla de la multiplicación]] | [[00 - Índice del curso]] | [[Clase 08 — Teorema de Bayes]]