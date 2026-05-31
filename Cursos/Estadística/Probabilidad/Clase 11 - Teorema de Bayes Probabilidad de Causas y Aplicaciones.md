[[Clase 10 — Probabilidad Total]] | [[00 - Índice del curso]] | [[Clase 12 — Distribuciones de Probabilidad]]

# Clase 11 — Teorema de Bayes: Probabilidad de Causas y Aplicaciones
tags: #algebra #teoremadebayes
Curso: [[00 - Índice del curso]] | Bloque 3 | Lección 11 de 12

> [!info] 🌍 Relevancia y aplicaciones
> El Teorema de Bayes es la herramienta definitiva para la toma de decisiones cuando existe incertidumbre. Nos permite "ajustar" nuestras creencias iniciales frente a la evidencia real. Sus aplicaciones incluyen:
> - **Medicina:** Calcular la precisión real de diagnósticos clínicos.
> - **Neurología:** Modelar cómo el cerebro humano procesa estímulos y aprende de la experiencia.
> - **Negocios y Finanzas:** Evaluar la fiabilidad de maquinaria industrial según su fabricante y cuantificar el impacto económico de piezas defectuosas en una línea de producción.
> - **Tecnología:** Desarrollo de algoritmos de inteligencia artificial y filtrado inteligente de datos.

---

### Concepto Clave

> [!note] 📌 ¿Qué es Teorema de Bayes?
> ¡Qué tal, amigas y amigos! Imaginen que son detectives. Tienen una sospecha inicial sobre un caso, pero de repente encuentran una pista nueva. El Teorema de Bayes es la regla matemática que nos enseña a **actualizar** lo que ya sabíamos para incluir esa nueva evidencia. 
> 
> En términos técnicos, pasamos de una **Probabilidad a Priori** (lo que sabíamos antes de la pista) a una **Probabilidad a Posteriori** (nuestra nueva seguridad una vez analizada la pista).

> [!warning] ⚠️ Error común: La confusión de la condicional
> Es fundamental entender que $P(A|B)$ **no es lo mismo** que $P(B|A)$. 
> **Ejemplo:** La probabilidad de que un animal "sea blanco dado que es un perro" es muy distinta a la probabilidad de que "sea un perro dado que es blanco". ¡El orden de la condición lo cambia todo!

> [!tip] 💡 Truco para recordarlo
> Para armar la fórmula usa la **regla de la inversión**: Si buscas la probabilidad de $A$ dado que ocurrió $B$ ($P(A|B)$), empieza escribiendo lo contrario ($P(B|A)$) en el numerador. Recuerda: la "pista" o condición dada ($B$) siempre debe ser el denominador (probabilidad total).

---

### Procedimiento Paso a Paso

```text
PASO 1 → Dibujar el diagrama de árbol con las probabilidades iniciales de cada rama.
PASO 2 → Identificar la "pista" o condición dada (ej. "salió defectuoso") y marcar las rutas que terminan en ella.
PASO 3 → Calcular la Probabilidad Total (denominador) sumando los resultados de todas las rutas que cumplen la condición.
PASO 4 → Aplicar la fórmula de Bayes: Dividir la probabilidad de la ruta específica deseada entre la Probabilidad Total.
```

---

### Ejemplos Desarrollados

```ad-example
title: **Ejemplo 1: Caso básico - Fábrica de balones**
**Contexto:** Una fábrica tiene dos máquinas. La Máquina 1 produce el 40% ($0.4000$) y la Máquina 2 el 60% ($0.6000$). El 2% ($0.0200$) de M1 son defectuosos y el 3% ($0.0300$) de M2 son defectuosos.
**Problema:** Si se elige un balón al azar y es defectuoso, ¿cuál es la probabilidad de que sea de la Máquina 1?
**Cálculo:**
1. Ruta M1 y Defectuoso: $0.4000 \times 0.0200 = 0.0080$
2. Ruta M2 y Defectuoso: $0.6000 \times 0.0300 = 0.0180$
3. Probabilidad Total de Defectuoso: $0.0080 + 0.0180 = 0.0260$
4. Bayes: $P(M1|D) = 0.0080 / 0.0260 = 0.3077$
**Resultado:** **30.77%**
```

```ad-example
title: **Ejemplo 2: Caso con urnas**
**Contexto:** Urna 1 (3 azules, 2 rojas) y Urna 2 (4 azules, 1 roja). Se elige una urna al azar ($0.5000$ cada una).
**Problema:** Se extrae una bola y resulta ser roja. ¿Probabilidad de que provenga de la Urna 1?
**Cálculo:**
1. Ruta Urna 1 y Roja: $0.5000 \times (2/5) = 0.5000 \times 0.4000 = 0.2000$
2. Ruta Urna 2 y Roja: $0.5000 \times (1/5) = 0.5000 \times 0.2000 = 0.1000$
3. Probabilidad Total de Roja: $0.2000 + 0.1000 = 0.3000$
4. Bayes: $P(U1|R) = 0.2000 / 0.3000 = 0.6667$
**Resultado:** **66.67%**
```

```ad-example
title: **Ejemplo 3: Caso avanzado - Transferencia entre urnas**
**Contexto:** Urna 1 (3 azules, 1 roja) y Urna 2 (2 azules, 2 rojas). Se pasa una bola de la U1 a la U2 y luego se extrae una de la U2.
**Problema:** Si la bola extraída de la U2 fue azul, ¿cuál es la probabilidad de que la bola transferida fuera azul?
**Cálculo:**
1. Si se pasa azul ($P = 3/4$): U2 ahora tiene 3 azules de 5. Ruta: $0.7500 \times 0.6000 = 0.4500$
2. Si se pasa roja ($P = 1/4$): U2 ahora tiene 2 azules de 5. Ruta: $0.2500 \times 0.4000 = 0.1000$
3. Probabilidad Total de azul en U2: $0.4500 + 0.1000 = 0.5500$
4. Bayes: $P(AzulTransferida|AzulExtraída) = 0.4500 / 0.5500 = 0.8182$
**Resultado:** **81.82%**
```

```ad-example
title: **Ejemplo 4: Aplicación real con 3 máquinas y Riesgo Financiero**
**Contexto:** Máquinas A (10%), B (30%) y C (60%). Defectos: A=1%, B=3%, C=5%. Cada pieza defectuosa cuesta **$50 USD**.
**Problema:** Se detecta una pérdida de $50 USD (una pieza fallida). ¿Cuál es la probabilidad de que la pérdida provenga de la Máquina A?
**Cálculo:**
1. Ruta A (Defecto): $0.1000 \times 0.0100 = 0.0010$
2. Ruta B (Defecto): $0.3000 \times 0.0300 = 0.0090$
3. Ruta C (Defecto): $0.6000 \times 0.0500 = 0.0300$
4. Probabilidad Total de Defecto: $0.0010 + 0.0090 + 0.0300 = 0.0400$
5. Bayes: $P(A|D) = 0.0010 / 0.0400 = 0.0250$
**Resultado:** **2.5%**. 
**Análisis de Experto:** Aunque todas las máquinas generan el mismo costo por error, la Máquina A representa una **Exposición al Riesgo Financiero** de solo el 2.5%. Esto se debe a su altísima fiabilidad y su baja cuota de producción en comparación con la Máquina C.
```

---

### Ejercicios para el Estudiante

```ad-abstract
title: Ejercicio Fácil
Una línea de producción tiene dos máquinas: M1 (60% producción, 3% defectos) y M2 (40% producción, 2% defectos). Si se encuentra un producto defectuoso, ¿cuál es la probabilidad de que provenga de la M1?
```

```ad-abstract
title: Ejercicio Medio
Tenemos dos urnas. Urna A: 4 bolas azules y 2 rojas. Urna B: 3 bolas azules y 1 roja. Si extraemos una bola al azar y resulta ser **azul**, ¿cuál es la probabilidad de que provenga de la Urna B?
```

```ad-abstract
title: Ejercicio Avanzado (Análisis de Costos Médicos)
En una población, el 0.1% ($0.0010$) padece una enfermedad rara. Una prueba diagnóstica tiene un 99% ($0.9900$) de efectividad en enfermos, pero un 2% ($0.0200$) de falsos positivos en personas sanas. 
1. Si una persona da positivo, ¿cuál es la probabilidad de que esté realmente enferma?
2. Si el costo de un tratamiento innecesario por falso positivo es de **$500 USD**, ¿por qué este resultado es preocupante para el hospital?
```

```ad-success
title: Soluciones para el docente
1. **Fácil:** **69.23%**. ($P(M1 \cap D) = 0.0180$; $P(Total D) = 0.0260$).
2. **Medio:** **52.94%**. ($P(A|U1) = 4/6$ y $P(A|U2) = 3/4$. $P(U1 \cap A) = 0.3333$; $P(U2 \cap A) = 0.3750$. Total: $0.7083$).
3. **Avanzado:** **4.72%**.
   - **Cálculo:** $P(Pos) = (0.0010 \times 0.9900) + (0.9990 \times 0.0200) = 0.00099 + 0.01998 = 0.02097$. Bayes: $0.00099 / 0.02097 = 0.0472$.
   - **Key Insight (Falla de la Tasa Base):** Cuando una enfermedad es tan rara, incluso una prueba "buena" genera muchísimos falsos positivos. En este caso, de cada 1000 positivos, unos 953 estarían sanos, generando una pérdida económica masiva en tratamientos innecesarios (aproximadamente \$476,500 USD por cada 1000 diagnósticos positivos).
```

---

### Mini-prueba de Autoevaluación

```ad-question
title: Pregunta 1
¿Qué significa pasar de una probabilidad "a priori" a una "a posteriori"?
```

```ad-question
title: Pregunta 2
En el denominador de la fórmula de Bayes, ¿qué estamos calculando realmente? (Pista: lo vimos en la Clase 10).
```

```ad-question
title: Pregunta 3
Si la Máquina X produce el 50% con 10% de fallos y la Máquina Y el 50% con 20% de fallos, ¿cuál es la probabilidad de que un fallo venga de la Máquina X?
```

---

> [!tip] 💡 En la próxima clase
> Ya sabemos cómo rastrear las causas de un evento. Ahora veremos cómo estos datos se agrupan y se comportan en grandes poblaciones en la **Clase 12 — Distribuciones de Probabilidad**.

[[Clase 10 — Probabilidad Total]] | [[00 - Índice del curso]] | [[Clase 12 — Distribuciones de Probabilidad]]