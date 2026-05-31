# 📖 Guía de estudio — Clase 07: Probabilidad Condicional

> [!info] 📌 Conceptos clave
> *   **¿Qué es?:** La probabilidad condicional es simplemente una probabilidad con una "pista". Ya no calculamos a ciegas, sino que tenemos una condición previa que **reduce nuestro grupo de estudio**.
> *   **El Secreto del Profe Alex:** La diferencia fundamental es que, en la probabilidad simple, usamos a toda la población; en la condicional, nos enfocamos **solo en el subgrupo** que cumple la condición.
> *   **Palabras "Mágicas":** ¡Ojo aquí! Siempre que leas frases como *"si se sabe que"*, *"dado que"*, *"sabiendo que"* o *"si se seleccionó solo a..."*, estás ante un problema de probabilidad condicional.
> *   **Tú eliges el camino:** Estos problemas se pueden resolver por **lógica** (ajustando el denominador visualmente) o por la **fórmula oficial**. ¡De ambas formas llegamos al mismo resultado!

---

### 2. TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Regla de Laplace** | Es la base: $\frac{\text{Casos favorables}}{\text{Casos totales}}$. |
| **Probabilidad Condicional $P(A \mid B)$** | $\frac{P(A \cap B)}{P(B)}$ (La probabilidad de que ocurra A dado que ya pasó B). |
| **Intersección ($\cap$)** | Es el "y". Casos que cumplen **ambas** cosas a la vez (ej. ser azul y ser par). |
| **Símbolo "Dado que" ($ \mid $)** | La rayita vertical que separa la pregunta de la condición que ya conocemos. |

---

### 3. EJEMPLOS RESUELTOS ADICIONALES

```ad-example
title: Ejemplo A — Esferas Numeradas
**Contexto:** Tenemos una urna con 10 esferas: 6 azules y 4 rojas. De las azules, 4 son pares. Queremos saber: ¿Cuál es la probabilidad de que una esfera sea par, **dado que** ya es azul?

**Camino 1: Por Lógica (El método del borrador)**
1. **Identifica la condición:** Nos dicen que la esfera *ya es azul*. ¡Perfecto! Borramos de nuestra mente las 4 esferas rojas. Ya no existen para este problema.
2. **Nuevo Total:** Ahora mi mundo solo tiene 6 esferas (las azules). Ese es mi denominador.
3. **Casos Favorables:** De esas 6 azules, ¿cuántas son pares? El ejercicio dice que 4.
4. **Resultado:** $\frac{4}{6}$ que simplificado es $\frac{2}{3} \approx 66.6\%$.

**Camino 2: Por Fórmula**
* $P(\text{Par} \mid \text{Azul}) = \frac{P(\text{Par} \cap \text{Azul})}{P(\text{Azul})}$
* $P(\text{Par} \cap \text{Azul}) = \frac{4}{10}$ (4 son pares y azules de un total de 10).
* $P(\text{Azul}) = \frac{6}{10}$ (6 azules de 10 totales).
* Cálculo: $\frac{4/10}{6/10} = \frac{4}{6} = 66.6\%$. ¡Fíjate que llegamos a lo mismo!
```

```ad-example
title: Ejemplo B — Descuentos en Tienda de Tecnología
**Contexto:** En una tienda:
* El 40% de los clientes gasta más de $100 USD.
* El 25% usa tarjeta de crédito.
* El 15% hace ambas cosas (gasta más de $100 y usa tarjeta).

**Problema:** ¿Qué probabilidad hay de que un cliente gaste más de $100 USD **si ya sabemos** que pagó con tarjeta?

**Resolución (Paso a paso):**
1. **Identificar los datos:**
   * Condición ($B$): Usa tarjeta (25%).
   * Intersección ($A \cap B$): Gasta >$100 y usa tarjeta (15%).
2. **Aplicar la lógica de Profe Alex:** Como ambos son porcentajes, podemos "cancelar" el símbolo $\%$ y trabajar con los números directamente.
   * Operación: $\frac{15\%}{25\%} = \frac{15}{25}$
3. **Simplificar:** Sacamos quinta a ambos números:
   * $15 \div 5 = 3$
   * $25 \div 5 = 5$
4. **Resultado final:** $\frac{3}{5} = 0.6$. Si lo multiplicas por 100, nos da un **60%**.
```

---

### 4. EJERCICIOS DE REPASO

```ad-abstract
title: 🟢 Fácil
1. Tienes 10 esferas: 6 azules y 4 rojas. Si se sabe que la esfera es de color rojo, ¿cuál es la probabilidad de que sea par? (Toma en cuenta que solo hay 1 roja par).
2. En la misma urna, si extraemos una esfera y vemos que es impar, ¿cuál es la probabilidad de que sea roja? (Considera que hay 3 esferas rojas impares y 2 azules impares).
3. Si se sabe que la esfera extraída es azul, ¿cuál es la probabilidad de que sea específicamente la número 10 (que es par)?
```

```ad-abstract
title: 🟡 Medio
1. En un colegio, el 40% practica fútbol, el 50% baloncesto y el 15% ambos. Si eliges a un estudiante que practica fútbol, ¿cuál es la probabilidad de que también practique baloncesto?
2. Usando los mismos datos: Si se sabe que un estudiante practica baloncesto, ¿cuál es la probabilidad de que **no** practique fútbol? (Pista: Primero calcula cuántos practican "únicamente" baloncesto).
3. Reflexiona: ¿Por qué la probabilidad de "practicar baloncesto dado que practica fútbol" es distinta a la probabilidad de "practicar únicamente baloncesto"? Explica qué pasa con el denominador.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
1. En una empresa, el 65% de los proyectos superan los $5000 USD de presupuesto. El 15% de todos los proyectos son de software y superan ese monto. ¿Cuál es la probabilidad de que un proyecto sea de software si ya sabemos que superó los $5000 USD?
2. Un analista nota que el 40% de las ventas totales son "Online". El 20% de todas las ventas de la tienda son Online y de "Alto Valor" (más de $500 USD). Si una venta se realizó por internet (Online), ¿cuál es la probabilidad de que sea de Alto Valor?
3. El 30% de una cartera de inversiones es de "Alto Riesgo". Solo el 10% del total de la cartera son inversiones que son de alto riesgo Y tuvieron un retorno mayor al 10%. Si eliges una inversión de alto riesgo, ¿qué probabilidad hay de que su retorno haya sido mayor al 10%?
```

---

### 5. CONSEJO DE ESTUDIO

> [!tip] 💡 Consejo de estudio
> Como siempre te digo en mis videos: ¡No te ahogues en un vaso de agua con las fórmulas! Antes de escribir cualquier cosa, usa la **técnica del borrador**. Visualiza el problema y "borra" o ignora a todos los que no cumplen la condición (el "dado que"). Una vez que tengas tu nuevo grupo reducido, aplica la Regla de Laplace. Si tu denominador se ajusta a esa "pista" que te dieron, el ejercicio ya está resuelto en un 90%. ¡Ánimo, que tú puedes!