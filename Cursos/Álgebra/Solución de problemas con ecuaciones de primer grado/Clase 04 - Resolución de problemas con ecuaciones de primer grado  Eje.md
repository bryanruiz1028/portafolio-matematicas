# Clase 04 — Resolución de problemas con ecuaciones de primer grado | Ejemplo de monedas

**Navegación:** [[Clase 03 — Introducción a Ecuaciones]] | [[Clase 05 — Sistemas de Ecuaciones 2x2]]
**Etiquetas:** #matemáticas #pedagogía #ecuaciones #portafolio-docente

---

## 1. Relevancia y Aplicaciones Reales

> [!info] **¿Por qué aprender a modelar ecuaciones?**
> Convertir el lenguaje cotidiano en lenguaje algebraico es la formalización de nuestro pensamiento lógico. No se trata solo de "hallar la x", sino de estructurar problemas complejos para obtener soluciones exactas. Según la lógica de conteo de dinero de Profe Alex, esta habilidad es vital para:
> - 💵 **$USD:** Gestión de presupuestos personales y optimización del cambio de divisas.
> - 🏗️ **Práctica:** Logística de almacenes, donde se deben cuadrar cantidades totales de stock con valores unitarios de materiales.
> - 📊 **Cotidiana:** Cálculo rápido de propinas o la división proporcional de gastos compartidos en un grupo.

---

## 2. Definición del Concepto y Errores Comunes

> [!note] **Modelado de Ecuaciones**
> Es el proceso de traducir una situación de la vida real (como un puñado de monedas de distinto valor) a una expresión matemática (ecuación) que nos permite despejar una incógnita. Es el paso de la "intuición mental" al "rigor algebraico".

> [!warning] **Error crítico: El olvido de los paréntesis**
> Al multiplicar el valor de una denominación por una cantidad compuesta, **siempre** debes usar paréntesis. 
> - **Incorrecto:** $5 \times 25 - d$ (Aquí solo multiplicas el 25, restando una sola moneda). Esto daría $125 - d$.
> - **Correcto:** $5 \times (25 - d)$ (Aquí multiplicas el 5 por *todo* el grupo de monedas restantes).

> [!tip] **Regla Mnemotécnica: "El Rompecabezas"**
> Imagina que el dinero total es un rompecabezas terminado: **Dinero del Grupo A + Dinero del Grupo B = Gran Total**. Si sumas las partes por separado, siempre deben igualar al todo.

---

## 3. Procedimiento Paso a Paso (Algoritmo)

> [!todo] **Algoritmo de Resolución**
> 1. **Asignar la variable:** Escoge una incógnita para representar la cantidad de un tipo de moneda (ej. $d$ = monedas de 2€).
> 2. **Definir el "Resto":** Expresa la otra cantidad en función de la primera usando el total. 
>    *   *Lógica de Profe Alex:* Si tienes 25 monedas y $d$ son de un tipo, las que quedan son $25 - d$. Piénsalo como: **Resto = Total - Variable**.
> 3. **Plantear la ecuación:** Suma los valores parciales (Valor de moneda $\times$ Cantidad).
> 4. **Resolver y Verificar:** Despeja la variable y comprueba que los montos cuadren con el enunciado.

---

## 4. Bloques de Ejemplos Desarrollados

> [!example] **Ejemplo 1: El problema de los 98 euros (Intuición vs. Álgebra)**
> **Contexto:** 98 euros en 25 monedas de 2€ y 5€.
> **Razonamiento Lógico (Mental):** Antes de la ecuación, probemos un "Tanteo":
> - Si tuviera 10 monedas de 5€ ($50€$), me quedarían 15 monedas de 2€ ($30€$). Total = $80€$.
> - Como falta dinero para llegar a 98€, necesito *más* monedas de 5€.
> **Traducción Algebraica:**
> - Monedas de 2€: $d$
> - Monedas de 5€: $25 - d$
> - **Ecuación:** $2d + 5(25 - d) = 98$

> [!example] **Ejemplo 2: Gestión de Signos y Propiedad Distributiva**
> Resolviendo el ejemplo anterior:
> 1. **Distributiva:** $2d + 125 - 5d = 98$.
> 2. **Agrupar:** $(2d - 5d) = 98 - 125 \rightarrow -3d = -27$.
> 3. **División de negativos:** $d = \frac{-27}{-3}$. 
> *Nota pedagógica:* Recuerda que **negativo entre negativo resulta en positivo**. Por tanto, $d = 9$ (monedas de 2€).

> [!example] **Ejemplo 3: Escalabilidad con Denominaciones Mayores**
> ¿Funciona el método con billetes grandes? **Sí.**
> **Problema:** Tienes $3000 USD en 20 billetes de $100 y $200.
> - Billetes de $200: $x$
> - Billetes de $100: $20 - x$
> - **Ecuación:** $200x + 100(20 - x) = 3000$
> - $200x + 2000 - 100x = 3000 \rightarrow 100x = 1000 \rightarrow x = 10$ billetes de $200. 
> La estructura se mantiene idéntica sin importar el valor.

> [!example] **Ejemplo 4: Aplicación en Dólares ($USD)**
> **Problema:** Tienes $130 USD en billetes de $5 y $10. En total son 20 billetes.
> - Billetes de $5 = $x$
> - Billetes de $10 = $20 - x$
> - **Ecuación:** $5x + 10(20 - x) = 130$.
> Al resolver: $5x + 200 - 10x = 130 \rightarrow -5x = -70 \rightarrow x = 14$.
> *Resultado:* 14 billetes de $5 y 6 billetes de $10.

---

## 5. Sección de Práctica: Ejercicios para el Estudiante

> [!abstract] **🟢 Nivel Fácil: Suma directa**
> Si tienes 12 monedas de $50 y el resto son de $100 para un total de 15 monedas, ¿cuál es el monto total de dinero?

> [!abstract] **🟡 Nivel Medio: Hallar cantidades**
> Tienes 20 monedas en total de 2€ y 5€. Si el monto total es 70€, ¿cuántas monedas tienes de cada denominación?

> [!abstract] **🔴 Nivel Avanzado: El reto de los 1150 pesos**
> *(Basado en el ejercicio final de Profe Alex)*
> Tienes $1.150 pesos en un total de 15 monedas de $50 y $100. Encuentra la cantidad de cada una aplicando el algoritmo paso a paso.

> [!success] **✅ Soluciones Detalladas (Uso Docente)**
> 1. **Fácil:** $(12 \times 50) + (3 \times 100) = 600 + 300 =$ **900 pesos**.
> 2. **Medio:** $2d + 5(20 - d) = 70 \rightarrow -3d = -30 \rightarrow d = 10$. **10 monedas de 2€ y 10 de 5€**.
> 3. **Avanzado:** 
>    - Variable $c$ (monedas de $50) = 7.
>    - Cantidad de monedas de $100 = 15 - 7 = 8$.
>    - **Comprobación:** $(7 \times 50) + (8 \times 100) = 350 + 800 = 1150$. Correcto.

---

## 6. Autoevaluación y Cierre

> [!question] **Pregunta 1**
> Si $x$ representa la cantidad de monedas de $5 de un total de 30 monedas, ¿cuál es la expresión correcta para las monedas restantes?
> a) $x - 30$
> b) $30 - x$
> c) $30x$

> [!question] **Pregunta 2**
> En la expresión $100(15 - c)$, ¿qué representa el resultado de esta operación?
> a) El número total de monedas en el problema.
> b) El valor monetario total del segundo grupo de monedas (de $100).
> c) Solo el número de monedas de $100.

> [!question] **Pregunta 3: Aplicación rápida USD**
> Tienes un fajo de 10 billetes. Sabes que 6 billetes son de $5 USD y los 4 billetes restantes son de $10 USD. ¿Cuál es el monto total exacto?
> a) $70 USD
> b) $80 USD
> c) $75 USD

> [!tip] **Conexión Curricular**
> Dominar el modelado con una sola variable es el puente hacia temas más complejos. En la siguiente sesión, resolveremos estos mismos problemas usando **Sistemas de Ecuaciones 2x2**, donde asignaremos una letra diferente a cada incógnita (ej. $x$ e $y$).

---
**Navegación:** [[Clase 03 — Introducción a Ecuaciones]] | [[Clase 05 — Sistemas de Ecuaciones 2x2]]