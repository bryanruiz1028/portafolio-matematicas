# Clase 09 — Teorema de Bayes: Probabilidad Condicional Avanzada
tags: #algebra #teoremadebayes
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 9 de 9

---

[[Clase 08 — Probabilidad Total]] | [[00 - Índice del curso]] | Fin del curso

---

¡Qué tal amigas y amigos! Espero que estén muy bien. Llegamos a la última clase del bloque de probabilidad y vamos a cerrarlo con broche de oro estudiando el **Teorema de Bayes** (o de "Bayes", como prefieras decirle). 

Pilas aquí: si ya viste los videos anteriores de probabilidad condicional, **¡ya conoces Bayes sin saberlo!** El Teorema de Bayes no es más que una aplicación inteligente de la probabilidad condicional que nos permite "darle la vuelta" a la información. Si sabemos la probabilidad de que ocurra un efecto dado una causa, Bayes nos permite encontrar la probabilidad de que una causa específica haya ocurrido dado que ya observamos el efecto. Es, literalmente, el teorema del detective.

> [!info] 🌍 Relevancia y aplicaciones
> El Teorema de Bayes es fundamental porque permite actualizar nuestras creencias o resultados para hacerlos más confiables tras aplicaciones consecutivas de información. 
> En el mundo real, se utiliza en:
> - 💵 **Negocios:** Análisis de inversión y toma de decisiones bajo incertidumbre financiera.
> - 🏗️ **Tecnología y Neurología:** Desarrollo de inteligencia artificial y estudio de impulsos cerebrales.
> - 📊 **Medicina:** Diagnósticos de enfermedades basados en pruebas de laboratorio, calculando la probabilidad real de estar enfermo tras un positivo.

---

## 📌 Concepto Clave

> [!note] 📌 ¿Qué es el Teorema de Bayes?
> Imagina que eres un detective. Encuentras un "clue" o pista (un balón pinchado, un gato blanco o una pieza defectuosa). Sabes que hay varias máquinas o cajas de donde pudo venir. El Teorema de Bayes es la herramienta que te ayuda a viajar del **efecto** (la pista) de regreso a la **causa** (el origen). Es como tener una caja con perros y gatos: si sacas un animal con los ojos cerrados y sientes que es suave, Bayes te ayuda a calcular qué tan probable es que sea un gato basándose en esa "suavidad".

> [!warning] ⚠️ Error común
> ¡Mucho cuidado aquí! Muchos estudiantes creen que $P(A|B)$ es igual a $P(B|A)$. **Esto es totalmente falso**. No es lo mismo la probabilidad de que haya nubes dado que está lloviendo ($100\%$ casi siempre), que la probabilidad de que llueva dado que hay nubes (puede que solo sea un $20\%$). El orden de la condición cambia todo el panorama.

> [!tip] 💡 Truco para recordarlo (Regla de la Inversión)
> Para armar la fórmula sin tener que memorizarla, sigue este razonamiento de Profe Alex:
> 1. **Invierte:** Escribe primero lo contrario de lo que buscas (si buscas $A|B$, escribe $B|A$).
> 2. **Arriba:** Multiplica por la probabilidad individual del evento que ahora está a la derecha.
> 3. **Abajo:** Divide siempre por la probabilidad del evento que es tu "pista" o condición (la Probabilidad Total).
> 
> $P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$

---

## 🚀 Procedimiento Paso a Paso

Para resolver cualquier ejercicio, por más difícil que parezca, sigue esta receta:

```text
PASO 1 → Dibujar el diagrama de árbol con todas las ramificaciones (Causas -> Efectos).
PASO 2 → Asignar probabilidades decimales a cada rama (convertir porcentajes dividiendo entre 100).
PASO 3 → Identificar la "pista" o condición observada y marcar todas las ramas que terminan en esa pista.
PASO 4 → Aplicar la fórmula: (Rama específica que me piden / Suma de todas las ramas que cumplen la pista).
```

---

## 📝 Ejemplos Prácticos

> [!example] Ejemplo 1: La fábrica de balones
> Una fábrica tiene dos máquinas: M1 (produce el 40%) y M2 (produce el 60%). El porcentaje de balones defectuosos es del 2% para M1 y 3% para M2. Si seleccionamos un balón y resulta defectuoso, ¿cuál es la probabilidad de que venga de la M1?
> 
> **Solución:**
> - Rama M1 y Defectuoso: $0,4 \cdot 0,02 = 0,008$
> - Rama M2 y Defectuoso: $0,6 \cdot 0,03 = 0,018$
> - Probabilidad Total de Defectuosos: $0,008 + 0,018 = 0,026$
> - Aplicando Bayes: $P(M1|D) = \frac{0,008}{0,026} = 0,3076$
> 
> **Resultado:** **30,76%**

> [!example] Ejemplo 2: El caso de las Urnas
> Urna 1: 3 bolas azules, 2 rojas. Urna 2: 4 azules, 1 roja. Se elige una urna al azar y se saca una bola roja. ¿Probabilidad de que sea de la Urna 1?
> 
> **Solución:**
> - Probabilidad de elegir cada urna: $1/2 = 0,5$
> - Rama Urna 1 y Roja: $0,5 \cdot \frac{2}{5} = 0,5 \cdot 0,4 = 0,2$
> - Rama Urna 2 y Roja: $0,5 \cdot \frac{1}{5} = 0,5 \cdot 0,2 = 0,1$
> - Aplicando Bayes: $P(U1|R) = \frac{0,2}{0,2 + 0,1} = \frac{0,2}{0,3} = 0,66\overline{6}$
> 
> **Resultado:** **66,66%** o $2/3$

> [!example] Ejemplo 3: Transferencia de bolas (Avanzado)
> Urna 1 (3A, 1R). Urna 2 (2A, 2R). Se pasa una bola de U1 a U2 y luego se saca una de U2. Si la bola extraída de U2 fue azul, ¿cuál es la probabilidad de que la bola transferida haya sido azul?
> 
> **Solución:**
> - Si se pasó Azul ($P = 3/4 = 0,75$): Urna 2 queda con (3A, 2R). $P(A2|A1) = 3/5 = 0,6$. Rama: $0,75 \cdot 0,6 = 0,45$.
> - Si se pasó Roja ($P = 1/4 = 0,25$): Urna 2 queda con (2A, 3R). $P(A2|R1) = 2/5 = 0,4$. Rama: $0,25 \cdot 0,4 = 0,10$.
> - Aplicando Bayes: $P(A1|A2) = \frac{0,45}{0,45 + 0,10} = \frac{0,45}{0,55} = 0,81\overline{81}$
> 
> **Resultado:** **81,8181...%** (Periódico)

> [!example] Ejemplo 4: Análisis de pérdidas financieras ($USD)
> Una empresa tiene 3 máquinas: A (10% producción), B (30%) y C (60%). Las tasas de defectos son 1%, 3% y 5% respectivamente. **Cada pieza defectuosa genera una pérdida de $100 USD**. Si el departamento contable reporta una pérdida (pieza defectuosa), ¿cuál es la probabilidad de que la causa sea la Máquina A?
> 
> **Solución:**
> - Rama A (Defecto): $0,1 \cdot 0,01 = 0,001$
> - Rama B (Defecto): $0,3 \cdot 0,03 = 0,009$
> - Rama C (Defecto): $0,6 \cdot 0,05 = 0,030$
> - Suma de probabilidades de pérdida: $0,001 + 0,009 + 0,030 = 0,040$
> - Aplicando Bayes: $P(A|Pérdida) = \frac{0,001}{0,040} = 0,025$
> 
> **Resultado:** **2,5%**

---

## 💪 Ejercicios para el Estudiante

### 🟢 Nivel Fácil
1. Una fábrica usa dos máquinas, X (70%) e Y (30%). X produce 5% de errores e Y produce 10%. Si una pieza falla, ¿cuál es la probabilidad de que venga de la máquina X?
2. El 60% de los empleados de una oficina son mujeres. El 10% de las mujeres y el 20% de los hombres fuman. Si elegimos a alguien que fuma, ¿probabilidad de que sea mujer?
3. En una clínica, el 40% de los pacientes van por pediatría y el 60% por medicina general. La probabilidad de esperar más de una hora es 5% en pediatría y 10% en general. Si un paciente esperó más de una hora, ¿probabilidad de que sea de pediatría?
4. Dos impresoras, A (40%) y B (60%), imprimen folletos. A tiene un 2% de fallos de tinta y B un 4%. Si un folleto tiene fallo de tinta, ¿probabilidad de que sea de la impresora A?

### 🟡 Nivel Medio
1. Urna A: 5 bolas verdes, 3 blancas. Urna B: 2 verdes, 6 blancas. Se elige una urna al azar y sale una verde. ¿Probabilidad de que venga de la Urna A?
2. En una caja hay 10 iPhones (2 con pantalla rota) y en otra hay 10 Androids (3 con pantalla rota). Se elige un celular al azar y tiene la pantalla rota. ¿Probabilidad de que sea un iPhone?
3. Tenemos tres bolsas con canicas. Bolsa 1 (80% rojas), Bolsa 2 (50% rojas), Bolsa 3 (10% rojas). Elegimos una bolsa al azar y sacamos una roja. ¿Probabilidad de que sea de la Bolsa 1?
4. **Transferencia:** Urna 1 (2R, 2B). Urna 2 (1R, 3B). Se pasa una bola de U1 a U2. Si al sacar una de U2 es roja, ¿probabilidad de que hayamos pasado una roja?

### 🔴 Nivel Avanzado (Análisis de Costos $USD)
1. Usando las máquinas A, B y C del **Ejemplo 4**, cada defecto cuesta **$100 USD**. Si se reporta una pérdida, ¿cuál es la probabilidad de que la Máquina C sea la responsable?
2. Tres líneas de producción (P, Q, R) producen el 20%, 30% y 50%. Sus fallos son 2%, 4% y 6%. Cada fallo cuesta **$200 USD**. Si se perdió dinero por un fallo, ¿probabilidad de que fuera la línea Q?
3. Una planta química tiene 3 tanques. El riesgo de fuga es 1%, 2% y 3% respectivamente. El tanque 1 almacena el 50% del producto, el tanque 2 el 30% y el tanque 3 el 20%. Una fuga cuesta **$10,000 USD** en multas. Si hubo una multa, ¿probabilidad de que la fuga fuera en el Tanque 3?
4. Tres programadores desarrollan módulos: Dev1 (20%), Dev2 (30%), Dev3 (50%). La tasa de bugs críticos es 1%, 2% y 5%. Cada bug crítico cuesta **$500 USD** de soporte. Si se pagó soporte, ¿probabilidad de que el bug fuera del Dev3?

---

### ✅ Respuestas
1. **Fácil 1:** $53,84\%$ | **Fácil 2:** $42,85\%$ | **Fácil 3:** $25\%$ | **Fácil 4:** $25\%$
2. **Medio 1:** $71,42\%$ | **Medio 2:** $40\%$ | **Medio 3:** $57,14\%$ | **Medio 4:** $40\%$ ($0,15/0,375$)
3. **Avanzado 1:** $75\%$ ($0,030/0,040$) | **Avanzado 2:** $25,53\%$ | **Avanzado 3:** $35,29\%$ | **Avanzado 4:** $75,75\%$

---

## 🧪 Mini-Prueba de Autoevaluación

1. **¿Qué significa realmente la "pista" en Bayes?**
   - Es la condición que ya ocurrió (el efecto) y se coloca siempre en el denominador como Probabilidad Total.
2. **Si $P(A)=0.5$, $P(B|A)=0.2$ y la Probabilidad Total $P(B)=0.4$, ¿cuál es $P(A|B)$?**
   - $P(A|B) = (0.2 \cdot 0.5) / 0.4 = 0.1 / 0.4 = 0.25$ ($25\%$).
3. **En un sistema de 3 causas con resultados parciales de 0.001, 0.009 y 0.030, ¿cuál es la probabilidad total de que ocurra el evento?**
   - $0.040$ o $4\%$.

---

> [!tip] 💡 En la próxima clase
> ¡Felicidades! Has completado el bloque de Probabilidad. Dominar Bayes te permite ahora avanzar con paso firme hacia la **Estadística Inferencial**, donde usaremos estas bases para tomar decisiones con datos reales en el mundo profesional. ¡Nos vemos en el próximo bloque!

---

[[Clase 08 — Probabilidad Total]] | [[00 - Índice del curso]] | Fin del curso