# Clase 03 — Regla de la multiplicación en Probabilidad

#algebra #regladelamultip

[Clase 02] | [Índice] | [Clase 04]

---

## 1. Relevancia y Aplicaciones

La **Regla de la Multiplicación** es la herramienta que nos permite calcular la probabilidad de que dos o más eventos ocurran al mismo tiempo o de forma consecutiva. Desde un punto de vista didáctico, multiplicar probabilidades equivale a calcular una **"fracción de una fracción"** (una parte de una parte), lo que reduce el espacio de posibilidades conforme se añaden condiciones.

*   **Impacto Económico ($USD):** En una fábrica de balones (como se ve en la Fuente 3), si sabemos que el 60% de la producción es de fútbol y el 5% de estos son defectuosos, la regla nos permite prever el impacto financiero al identificar qué porcentaje exacto de la producción total generará pérdidas.
*   **Construcción y Práctica:** Al seleccionar personal o estudiantes de un grupo mixto (niños y niñas), esta regla nos ayuda a determinar la probabilidad de conformar equipos con características específicas bajo condiciones de azar.
*   **Situación Cotidiana:** En una clínica veterinaria, nos permite saber la probabilidad de que un paciente cumpla dos rasgos simultáneos, por ejemplo, que el animal sea un "perro" **Y** sea de "color blanco".

---

## 2. Concepto Clave y Notación Formal

Para un estudiante de 12 años, la regla se resume en la palabra clave **"Y"**: es la probabilidad de que ocurra "esto **Y** aquello". 

### Notación Matemática
El símbolo de la intersección ($\cap$) representa ese nexo "Y". Profe Alex destaca el uso de la **probabilidad condicional**, representada por una barra vertical ($|$):

1.  **Eventos Independientes (Con reemplazo):** $P(A \cap B) = P(A) \cdot P(B)$
2.  **Eventos Dependientes (Sin reemplazo):** $P(A \cap B) = P(A) \cdot P(B|A)$
    *   *Nota:* $P(B|A)$ se lee como "la probabilidad de que ocurra B, **dado que** ya ocurrió A".

### Error Común
Es fundamental no confundir esta regla con la de las **técnicas de conteo**. Mientras que en permutaciones o combinaciones contamos el número de **formas o caminos** posibles, en probabilidad medimos la **certeza o posibilidad** de un suceso en un rango de 0 a 1 (o 0% a 100%).

### Regla Mnemotécnica
Visualiza el símbolo de intersección ($\cap$) como un **puente o puerta** que une dos eventos. Al cruzarlo, los eventos se conectan mediante la letra **Y**, lo que te indica que debes **multiplicar**.

---

## 3. Procedimiento Paso a Paso

Sigue estos pasos lógicos para resolver cualquier problema de probabilidad conjunta:

```text
PASO 1 → IDENTIFICAR el total de casos (denominador) y los casos favorables (numerador) iniciales.
PASO 2 → CALCULAR la probabilidad del primer evento (P(A)).
PASO 3 → DETERMINAR si hay reemplazo. Si NO hay reemplazo (dependencia), resta 1 al denominador. 
         IMPORTANTE: Resta 1 al numerador SOLO si el segundo evento busca la misma categoría que el primero.
PASO 4 → MULTIPLICAR las fracciones resultantes para obtener la probabilidad total.
```

---

## 4. Ejemplos Prácticos

::: ad-example
title: Ejemplo 1: Caso básico (Sin reemplazo)
En una urna hay 5 esferas azules, 2 rojas y 1 verde (Total = 8). ¿Cuál es la probabilidad de que la primera sea azul y la segunda sea verde, sin devolver la primera?
*   **Evento A (Azul):** $5/8$
*   **Evento B (Verde dado que salió Azul):** $1/7$ (el total bajó porque no hubo reemplazo).
*   **Cálculo:** $\frac{5}{8} \cdot \frac{1}{7} = \frac{5}{56}$
*   **Resultado:** $0.089$ o **8.9%**.
:::

::: ad-example
title: Ejemplo 2: Selección de personas (Dependencia acumulada)
En una clase hay 10 niños y 8 niñas (Total = 18). Se eligen 3 estudiantes al azar. ¿Cuál es la probabilidad de que los tres sean niños?
*   **P(1° Niño):** $10/18$
*   **P(2° Niño | 1° fue Niño):** $9/17$
*   **P(3° Niño | 1° y 2° fueron Niños):** $8/16$
*   **Producto intermedio:** $\frac{10}{18} \cdot \frac{9}{17} \cdot \frac{8}{16} = \frac{720}{4896}$
*   **Resultado simplificado:** $\frac{5}{34} \approx$ **14.7%**.
:::

::: ad-example
title: Ejemplo 3: Caso de categorías distintas
De 20 esferos, 15 sirven y 5 no sirven. Sin reemplazo, ¿cuál es la probabilidad de que el primero sirva y el segundo no?
*   **Primero sirve:** $15/20$
*   **Segundo no sirve:** $5/19$ (El total baja a 19, pero el numerador de "no sirven" sigue siendo 5 porque el primero que salió era de la otra categoría).
*   **Cálculo:** $\frac{15}{20} \cdot \frac{5}{19} = \frac{75}{380} = \frac{15}{76}$
*   **Resultado:** **19.7%**.
:::

::: ad-example
title: Ejemplo 4: Aplicación Industrial (Decimales)
Una fábrica produce balones donde el 60% son de fútbol. El 5% de estos son defectuosos.
*   **P(Fútbol):** $0.60$
*   **P(Defectuoso | Fútbol):** $0.05$
*   **Cálculo:** $0.6 \cdot 0.05 = 0.03$
*   **Resultado:** **3%**.
:::

---

## 5. Ejercicios para el Estudiante

::: ad-abstract
title: Práctica de Clase
*   **Verde (Fácil):** Tienes 6 esferas (2 rojas, 3 azules, 1 verde). Sin reemplazo, ¿cuál es la probabilidad de que la primera sea roja **Y** la segunda también sea roja?
*   **Amarillo (Medio):** En un salón de 18 alumnos (10 niños y 8 niñas), se eligen tres personas al azar. ¿Cuál es la probabilidad de que las tres sean niñas?
*   **Rojo (Avanzado):** El 40% de los balones son de baloncesto. El 3% de los de baloncesto son defectuosos. ¿Cuál es la probabilidad de elegir un balón que sea de baloncesto **Y** esté "bueno" (no defectuoso)?
:::

::: ad-success
title: Soluciones y Procedimiento
*   **Fácil:** $\frac{2}{6} \cdot \frac{1}{5} = \frac{2}{30} \to$ **1/15** (o 6.6%).
*   **Medio:** $\frac{8}{18} \cdot \frac{7}{17} \cdot \frac{6}{16} = \frac{336}{4896} \to$ **7/102** (o 6.8%).
*   **Avanzado:** Primero hallamos la probabilidad de que sea bueno: $1 - 0.03 = 0.97$. Luego aplicamos la regla: $0.4 \cdot 0.97 = 0.388 \to$ **38.8%**.
:::

---

## 6. Autoevaluación

1.  **Conceptual:** Si un evento es "con reemplazo", ¿por qué decimos que los eventos son independientes?
2.  **Procedimental:** Tienes una urna con una sola esfera verde. Si la sacas (sin reemplazo), ¿cuál es la probabilidad de que la segunda esfera sea verde? Justifica usando la fracción $0/n$.
3.  **Análisis:** En el ejemplo de los balones, ¿por qué es necesario multiplicar la probabilidad de "Fútbol" por la de "Defectuoso" en lugar de solo mirar el 5%?

**Próximo tema:** Probabilidad Total y Teorema de Bayes.

[Clase 02] | [Índice] | [Clase 04]