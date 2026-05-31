# Clase 01 — Axiomas de Probabilidad y Regla de Laplace
tags: #algebra #axiomasdeprobab
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 9

---

**NAVEGACIÓN**
`[[Anterior: - | Clase 00]] | [[Siguiente: Clase 02 — Probabilidad Condicional]]`

---

### 🌍 Relevancia y aplicaciones
> [!info] **¿Por qué es importante esta clase?**
> La probabilidad es la herramienta matemática que nos permite cuantificar la incertidumbre y predecir resultados lógicos en un mundo donde nada es seguro. Al dominar estas reglas básicas, transformamos el caos en datos precisos para la toma de decisiones.
> 
> * **💵 Aplicación económica:** Gestión de riesgos financieros y cálculo de primas de seguros evaluadas en $\$USD$ según la probabilidad de siniestros.
> * **🏗️ Aplicación técnica:** Análisis de fiabilidad en ingeniería para determinar la probabilidad de éxito o fallo de un motor o sistema de procesos.
> * **📊 Situación cotidiana:** Predicción de fenómenos climáticos o cálculo de posibilidades de victoria en juegos de azar y sorteos.

---

### CONCEPTO CLAVE: AXIOMAS Y REGLA DE LAPLACE

> [!note] **Axiomas de Probabilidad**
> Los axiomas son las "reglas del juego" de la matemática: verdades tan evidentes que no necesitan demostración. Para entenderlos, clasifiquemos los eventos según su probabilidad ($P$):
> 1.  **Evento Imposible:** $P = 0$. Simplemente, no puede pasar (ej. sacar un $10$ en un dado de $6$ caras).
> 2.  **Evento Probable:** $0 < P < 1$. Es posible que ocurra, pero no es seguro.
> 3.  **Evento Seguro:** $P = 1$. Ocurrirá siempre (ej. que el dado caiga en un número menor a $10$).
> 
> **Propiedad del Suceso Complementario:** La probabilidad de que **no** ocurra algo es igual a $1$ menos la probabilidad de que **sí** ocurra: $P(\text{No } A) = 1 - P(A)$.

> [!warning] **Errores comunes**
> Tal como explica el Profe Alex: "Si tu resultado es negativo o mayor a $1$, algo está mal". La probabilidad nunca puede ser menor a $0$ ni superar el $1$ ($100\%$). En la Regla de Laplace, el denominador siempre será mayor o igual al numerador.

> [!tip] **Truco mnemotécnico: La Regla del Espacio Total**
> Recuerda que la suma de todas las probabilidades de nuestro **Espacio Muestral** (todo lo que puede pasar) siempre debe ser exactamente $1$. Es "el todo o la nada": si sumas las partes y no te da $1$, te falta algún suceso por contar.

---

### PROCEDIMIENTO PASO A PASO

Para calcular la probabilidad de un suceso, aplicamos la **Regla de Laplace** siguiendo este orden:

```text
FORMULA: P(A) = Casos Favorables / Casos Posibles

PASO 1: Identificar el número total de casos posibles (Espacio Muestral).
PASO 2: Identificar el número de casos favorables al suceso deseado.
PASO 3: Dividir casos favorables entre casos posibles (siempre da una fracción propia).
PASO 4: Expresar el resultado (Fracción simplificada, decimal o porcentaje [%] multiplicando por 100).
```

---

### BLOQUES DE EJEMPLOS

> [!example] **Ejemplo 1: Lanzamiento de un dado (Básico)**
> **Suceso:** Obtener el número $3$ al lanzar un dado de $6$ caras.
> * Casos posibles: $\{1, 2, 3, 4, 5, 6\} \rightarrow \mathbf{6}$
> * Casos favorables: $\{3\} \rightarrow \mathbf{1}$
> * **Cálculo:** $\frac{1}{6} \approx 0.1666 \approx 16.66\%$

> [!example] **Ejemplo 2: Sucesos Mutuamente Excluyentes**
> **Suceso:** Obtener un número par O un número impar al lanzar un dado.
> * $P(\text{Par}) = \frac{3}{6}$ y $P(\text{Impar}) = \frac{3}{6}$
> * Como no hay números que sean pares e impares a la vez, sumamos directamente: $\frac{3}{6} + \frac{3}{6} = \frac{6}{6} = 1$.
> * **Conclusión:** Es un suceso seguro ($100\%$).

> [!example] **Ejemplo 3: Unión de Sucesos (Caso Avanzado)**
> En un consultorio, el $60\%$ toma café ($C$), el $50\%$ lee revistas ($R$) y el $20\%$ hace ambas cosas ($C \cap R$).
> **Pregunta:** ¿Cuál es la probabilidad de que un paciente tome café O lea revistas?
> * $P(C \cup R) = P(C) + P(R) - P(C \cap R)$
> * $P(C \cup R) = 60\% + 50\% - 20\% = 90\%$.
> * **Explicación pedagógica:** Restamos el $20\%$ porque esas personas ya fueron contadas dentro del grupo del café y también en el de revistas. Si no lo restamos, ¡estaríamos contando a las mismas personas dos veces!

> [!example] **Ejemplo 4: Aplicación Real en Finanzas ($\$USD$)**
> Tienes una caja con $10$ facturas: $3$ facturas son de $\$100\text{ USD}$ y $7$ son de $\$50\text{ USD}$.
> **Suceso:** Extraer al azar una factura de $\$100\text{ USD}$.
> * Casos posibles: $10$ facturas totales en el espacio muestral.
> * Casos favorables: $3$ facturas que cumplen la condición de ser de $\$100\text{ USD}$.
> * **Cálculo:** $\frac{3}{10} = 0.3$.
> * **Resultado:** Existe un $30\%$ de probabilidad de extraer la factura de mayor valor.

---

### EJERCICIOS PARA EL ESTUDIANTE

#### 🟢 Bloque Verde (Fácil)
1. Probabilidad de obtener "Cara" al lanzar una moneda.
2. Probabilidad de obtener un número par al lanzar un dado de $6$ caras.
3. Probabilidad de obtener el número $5$ al lanzar un dado.
4. Probabilidad de obtener "Cruz" al lanzar una moneda.

#### 🟡 Bloque Amarillo (Medio)
1. En una urna hay $3$ bolas azules, $4$ rojas y $2$ verdes. ¿Probabilidad de sacar una roja?
2. Usando la misma urna, ¿probabilidad de sacar una azul o una verde?
3. En un dado, probabilidad de obtener un número par O un número mayor a $3$.
4. En una baraja de $10$ cartas (del $1$ al $10$), probabilidad de sacar un número impar O el número $2$.

#### 🔴 Bloque Rojo (Avanzado - $\$USD$)
1. Una tienda vende dos productos: A ($\$80\text{ USD}$) y B ($\$120\text{ USD}$). El $40\%$ compra A, el $30\%$ compra B y el $10\%$ compra ambos. ¿Probabilidad de que compren A o B?
2. Un cajero tiene $10$ sobres: $5$ de $\$20\text{ USD}$ y $5$ de $\$50\text{ USD}$. Probabilidad de sacar un sobre de $\$50\text{ USD}$.
3. El $70\%$ de los empleados usa transporte público ($P$), el $55\%$ auto ($A$) y el $40\%$ ambos. Probabilidad de que use $P$ o $A$.
4. Si la probabilidad de que un cliente pague una deuda de $\$500\text{ USD}$ es $0.85$, ¿cuál es la probabilidad de que **NO** la pague (suceso complementario)?

#### **Bloque de Respuestas**
* **Verde:** 1) $\frac{1}{2} = 50\%$; 2) $\frac{3}{6} = \frac{1}{2} = 50\%$; 3) $\frac{1}{6} \approx 16.6\%$; 4) $\frac{1}{2} = 50\%$.
* **Amarillo:** 1) $\frac{4}{9} \approx 44.4\%$; 2) $\frac{5}{9} \approx 55.5\%$; 3) $\frac{4}{6} = \frac{2}{3} \approx 66.6\%$; 4) $\frac{6}{10} = \frac{3}{5} = 60\%$.
* **Rojo:** 1) $60\% = 0.6$; 2) $\frac{5}{10} = \frac{1}{2} = 50\%$; 3) $85\% = 0.85$; 4) $0.15 = 15\%$.

---

### MINI-PRUEBA DE AUTOEVALUACIÓN

**1. Si un evento tiene una probabilidad de $P=1$, se clasifica matemáticamente como:**
   a) Imposible.
   b) Probable.
   c) Seguro.
   d) Complementario.
   *R: c) Seguro. Significa que el evento ocurrirá en el 100% de los casos.*

**2. Al extraer una carta de una baraja numerada del 1 al 10, ¿cuál es la probabilidad de obtener un número mayor a 7?**
   a) $\frac{7}{10}$
   b) $\frac{3}{10}$
   c) $\frac{4}{10}$
   d) $\frac{1}{10}$
   *R: b) $\frac{3}{10}$. Los casos favorables son $\{8, 9, 10\}$, que son tres casos de diez posibles.*

**3. Tienes dos sobres: uno con $\$100\text{ USD}$ y otro vacío ($\$0\text{ USD}$). ¿Cuál es la probabilidad de elegir el sobre con dinero?**
   a) $1.0$
   b) $0.0$
   c) $0.5$
   d) $0.2$
   *R: c) $0.5$. Aplicando Laplace: $1$ caso favorable (sobre con dinero) / $2$ casos posibles = $0.5$ ($50\%$).*

---

### NOTAS FINALES
**Próximo tema:** En la siguiente sesión subiremos el nivel con la **Probabilidad Condicional**. Analizaremos cómo cambia la probabilidad de un suceso cuando ya tenemos información previa (introducción al Teorema de Bayes).

**NAVEGACIÓN**
`[[Anterior: - | Clase 00]] | [[Siguiente: Clase 02 — Probabilidad Condicional]]`