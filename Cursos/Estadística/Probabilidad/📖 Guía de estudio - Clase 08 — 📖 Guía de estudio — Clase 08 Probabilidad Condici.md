# 📖 Guía de estudio — Clase 08: Probabilidad Condicional

> [!info] 📌 Conceptos clave
> La **probabilidad condicional** es la probabilidad de que ocurra un evento (A), sabiendo que ya ha ocurrido otro evento (B). Como expertos, debemos considerar lo siguiente:
> *   **Cambio del espacio muestral:** A diferencia de la probabilidad simple, aquí no trabajamos con el total de la población. La condición nos obliga a trabajar con un **subgrupo específico**, reduciendo el denominador.
> *   **Identificación de pistas:** La clave pedagógica está en detectar frases como "dado que", "si se sabe que" o "si se seleccionó un...". Esto define nuestra condición.
> *   **Tablas de contingencia:** Son herramientas de doble entrada fundamentales para organizar datos cruzados (ej. género y categorías). Facilitan la visualización de intersecciones y totales marginales sin errores de conteo.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Probabilidad Condicional $P(A\|B)$** | Probabilidad de que ocurra A dado que sucedió B. Se calcula como la intersección dividida por la condición: $P(A\|B) = \frac{P(A \cap B)}{P(B)}$ |
| **Regla de la Multiplicación** | Permite hallar la probabilidad de que ambos eventos ocurran ($P(A \cap B)$) multiplicando el primer evento por la condicional del segundo: $P(A \cap B) = P(A) \cdot P(B\|A)$ |
| **Probabilidad del Complemento** | También llamada "evento contrario" ($A^c$), permite hallar la probabilidad de que algo **no ocurra**: $P(A^c) = 1 - P(A)$. |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Rendimiento Académico
**Contexto:** En un curso de matemáticas de 50 estudiantes, 40 entregaron todos los trabajos y 10 no lo hicieron. De los que **no entregaron**, se registra que aprobaron 3 alumnos. ¿Cuál es la probabilidad de que un estudiante apruebe dado que no entregó sus trabajos?

**Pasos para resolver:**
1. **Identificar el subgrupo (Denominador):** El enunciado nos condiciona a los alumnos que "no entregaron". Según el contexto, este total es **10**.
2. **Identificar casos favorables (Numerador):** De ese subgrupo de 10, identificamos cuántos aprobaron. El dato es **3**.
3. **Aplicar la regla de Laplace:** 
   $P(\text{Aprobar} | \text{No entrega}) = \frac{3}{10} = 0.3$
   
**Resultado:** La probabilidad es de **3/10**, es decir, un **30%**.
```

```ad-example
title: Ejemplo B — Premios en la Veterinaria
**Contexto:** Una clínica atiende un 60% de perros ($P(P) = 0.60$) y un 30% de animales blancos ($P(B) = 0.30$). El 25% de los perros son blancos ($P(B|P) = 0.25$). La clínica ofrece un **bono de $50 USD** si el animal seleccionado al azar es un perro blanco. Si sabemos que el animal elegido es blanco, ¿cuál es la probabilidad de que sea un perro y se gane el premio?

**Pasos para resolver:**
1. **Hallar la intersección $P(P \cap B)$:** Aplicamos la regla de la multiplicación.
   $P(Perro) \cdot P(Blanco|Perro) = 0.60 \times 0.25 = 0.15$ (un 15%).
2. **Identificar la condición:** Ya se sabe que el animal es blanco, por lo que usamos el total de blancos: **0.30**.
3. **Calcular la probabilidad condicional:**
   $P(P|B) = \frac{P(P \cap B)}{P(B)} = \frac{0.15}{0.30} = 0.5$
   
**Resultado:** Existe una probabilidad de **1/2 (50%)** de que sea un perro. Esto permite a la clínica estimar que pagará el bono de **$50 USD** en la mitad de los casos donde el animal sea blanco.
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
Utiliza los datos exactos de la tabla de la carrera atlética (Total: 200 participantes; Femenino: 77; Niño Masculino: 32; Niña Femenino: 20; Total Adultos: 90). Responde:
1. ¿Cuál es la probabilidad simple de que el corredor sea de género **Femenino**?
2. ¿Cuál es la probabilidad de que el corredor sea un **Niño (Masculino)**?
3. Si la organización sabe que el total de adultos es 90, ¿cuál es la probabilidad de seleccionar un corredor de la categoría Adultos al azar?
```

```ad-abstract
title: 🟡 Medio
Basado en el caso de Matemáticas e Inglés: 80% aprueba Matemáticas ($M$), 75% aprueba Inglés ($I$) y, de los que aprueban Matemáticas, el 90% aprueba Inglés ($P(I|M) = 0.90$).
1. Calcula la probabilidad de la intersección $P(M \cap I)$ usando la regla de la multiplicación.
2. Utilizando la fórmula de probabilidad condicional, calcula la probabilidad de que un estudiante haya aprobado Matemáticas dado que aprobó Inglés $P(M|I)$. Expresa el resultado en fracción y decimal.
3. Si un estudiante no aprobó Inglés, calcula la probabilidad del evento contrario usando la notación de complemento $P(I^c)$.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
**Contexto:** En la carrera atlética, la inscripción cuesta **$25 USD**. Se anuncia un reembolso total de los **$25 USD** si el corredor seleccionado al azar es un **Masculino** de la categoría **Senior**. 

**Reto:** Según la tabla de contingencia, la categoría Senior tiene un total de **60** personas, de las cuales **41** son de género **Masculino**. Calcula la probabilidad condicional de que el corredor sea Masculino dado que pertenece a la categoría Senior.

> [!tip] Pro-tip pedagógico
> Recuerda que al existir la condición "dado que pertenece a Senior", el total general de 200 participantes es irrelevante para este cálculo. Tu nuevo universo es únicamente la categoría Senior.
```

> [!tip] 💡 Consejo de estudio
> La clave de la probabilidad condicional es la **lectura comprensiva**. Al analizar el texto, busca siempre el grupo que sigue a la frase **"dado que"** o **"si se sabe que"**; ese grupo específico es tu nuevo **denominador**. ¡Identificar la condición es el 90% del éxito en el ejercicio!