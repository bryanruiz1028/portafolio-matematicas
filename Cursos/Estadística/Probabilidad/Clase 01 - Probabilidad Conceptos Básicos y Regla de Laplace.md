# Clase 01 — Probabilidad: Conceptos Básicos y Regla de Laplace

#algebra #probability
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 12

> [!info] 🧭 Navegación
> ◀ **Anterior**: N/A | ▲ **Índice**: [[00 - Índice del curso]] | ▶ **Siguiente**: [[Clase 02 — Probabilidad Condicionada]]

---

## 2. Importancia y Aplicaciones

> [!info] 🌍 Relevancia y aplicaciones
> La probabilidad es la rama de las matemáticas que nos permite cuantificar la **incertidumbre**. Gracias a ella, podemos estudiar fenómenos donde no es posible predecir el resultado final con absoluta certeza, asignándoles un valor numérico de posibilidad.
> 
> *   💵 **Rifas y Apuestas:** Permite calcular las opciones reales de ganar premios en $USD en sorteos o evaluar el rendimiento de equipos en eventos deportivos.
> *   🏗️ **Control de Calidad:** Las industrias analizan muestras de artículos para determinar la probabilidad de fallos en su producción masiva.
> *   📊 **Predicción Diaria:** Desde estimar el tráfico vehicular en un minuto específico hasta pronosticar el clima o resultados en el fútbol.

---

## 3. Conceptos Clave (Glosario Pedagógico)

> [!note] 📌 ¿Qué es Probabilidad?
> En términos sencillos, es una medida de "qué tan posible" es que algo ocurra. Cuando realizamos una acción donde el resultado depende del azar, la probabilidad nos da un número para saber si tenemos muchas o pocas oportunidades de éxito.
> 
> Matemáticamente, trabajamos con:
> - **Experimento Aleatorio ($\epsilon$):** Una acción cuyo resultado no se puede predecir con certeza (ej. lanzar un dado).
> - **Espacio Muestral ($\Omega$ o $S$):** El conjunto de **todos** los resultados posibles de ese experimento.
> - **Evento:** Un caso específico que nos interesa dentro de todas las posibilidades.

> [!warning] ⚠️ Error común
> Es vital no ignorar la individualidad de los elementos. Al lanzar dos monedas, muchos piensan que el espacio muestral es solo 3 (2 caras, 2 sellos, o uno de cada uno). Sin embargo, el orden importa: obtener (Cara-Sello) es distinto a (Sello-Cara). El espacio real tiene $n=4$ resultados. Confundir el **evento** con el **espacio muestral** es el error más frecuente.

> [!tip] 💡 Truco para recordarlo
> Para aplicar la Regla de Laplace, usa la regla mnemotécnica: **"Lo que quiero sobre lo que hay"**.
> - **Lo que quiero:** Los casos que me hacen ganar (Favorables).
> - **Lo que hay:** El total de cosas que podrían pasar (Posibles).

---

## 4. Procedimiento de la Regla de Laplace

Para cualquier evento $A$, la probabilidad $P(A)$ se define mediante la fórmula:
$$P(A) = \frac{\text{Casos Favorables}}{\text{Casos Posibles}}$$

```text
Pasos lógicos para el cálculo:

1. Identificar el Experimento Aleatorio (ε): Definir claramente la acción a realizar.
2. Listar el Espacio Muestral (Ω): Identificar todos los resultados posibles y contar el total (n).
3. Contar los Casos Favorables: Identificar cuántos de esos resultados cumplen con nuestro Evento.
4. Calcular y Convertir: Dividir Favorables / Posibles y expresar en Fracción, Decimal y Porcentaje.
```

---

## 5. Ejemplos Prácticos Desarrollados

```ad-example
title: Ejemplo 1: Lanzamiento de una moneda
**Pregunta:** ¿Cuál es la probabilidad de obtener "Cara" al lanzar una moneda?
1. **Espacio Muestral ($\Omega$):** {Cara, Sello} $\rightarrow$ 2 casos.
2. **Casos Favorables:** {Cara} $\rightarrow$ 1 caso.
3. **Cálculo:** $P(Cara) = \frac{1}{2}$
**Resultado:** $\frac{1}{2} = 0.5 = 50\%$
```

```ad-example
title: Ejemplo 2: Rangos en un dado
**Pregunta:** ¿Cuál es la probabilidad de que un dado caiga en un número mayor a 4?
1. **Espacio Muestral ($\Omega$):** {1, 2, 3, 4, 5, 6} $\rightarrow$ 6 casos.
2. **Casos Favorables:** {5, 6} $\rightarrow$ 2 casos.
3. **Cálculo:** $P(>4) = \frac{2}{6}$
**Resultado:** $\frac{1}{3} \approx 0.333 = 33.3\%$
```

```ad-example
title: Ejemplo 3: Dos monedas (Mismo lado)
**Pregunta:** Al lanzar dos monedas, ¿cuál es la probabilidad de que ambas caigan por el mismo lado?
1. **Espacio Muestral ($\Omega$):** {(C,C), (C,S), (S,C), (S,S)} $\rightarrow$ 4 casos.
2. **Casos Favorables:** {(C,C), (S,S)} $\rightarrow$ 2 casos.
3. **Cálculo:** $P(\text{Iguales}) = \frac{2}{4}$
**Resultado:** $\frac{1}{2} = 0.5 = 50\%$
```

```ad-example
title: Ejemplo 4: Rifa en $USD
**Pregunta:** Compras un boleto de una urna con 10 boletos totales. Si hay 3 boletos premiados con $100 USD, ¿cuál es la probabilidad de ganar?
1. **Espacio Muestral ($\Omega$):** 10 boletos.
2. **Casos Favorables:** 3 boletos con premio.
3. **Cálculo:** $P(\text{Ganar}) = \frac{3}{10}$
**Resultado:** $\frac{3}{10} = 0.3 = 30\%$
```

---

## 6. Ejercicios para el Estudiante

```ad-abstract
title: 🟢 Nivel Verde (Fácil) - El Dado
1. Probabilidad de obtener un número par al lanzar un dado.
2. Probabilidad de que al lanzar un dado caiga exactamente el número 3.
3. Probabilidad de que al lanzar un dado caiga un número menor que 2.
4. Probabilidad de que al lanzar un dado caiga un número entre 1 y 6.
```

```ad-abstract
title: 🟡 Nivel Amarillo (Medio) - La Urna
En una urna hay **3 bolas azules, 4 rojas y 2 verdes**. Calcula:
1. Probabilidad de extraer una bola azul.
2. Probabilidad de extraer una bola roja.
3. Probabilidad de extraer una bola que **no** sea verde.
4. Probabilidad de extraer una bola azul o verde.
```

```ad-abstract
title: 🔴 Nivel Rojo (Avanzado - $USD) - Aplicaciones
1. En un concurso con un premio de $100 USD participan 20 personas. Si compras 5 boletos, ¿cuál es tu probabilidad porcentual de ganar?
2. Una empresa revisa un lote de 5 artículos. Se sabe que la tasa de falla es de 1 de cada 5. ¿Cuál es la probabilidad de que el primer artículo revisado sea defectuoso?
3. Se lanzan dos monedas para decidir quién paga una cuenta de $20 USD. Si el resultado es igual (C-C o S-S), pagas tú. ¿Cuál es la probabilidad de que **no** te toque pagar?
4. En una rifa de 100 boletos para ganar $500 USD, hay 5 boletos premiados. Calcula la probabilidad en decimal de obtener un premio.
```

```ad-success
title: ✅ Respuestas para el Docente
**Nivel Verde:** 
1) $\frac{3}{6} = 50\%$ | 2) $\frac{1}{6} \approx 16.6\%$ | 3) $\frac{1}{6} \approx 16.6\%$ | 4) $\frac{6}{6} = 100\%$ (**Suceso Seguro**).

**Nivel Amarillo (Total = 9):** 
1) $\frac{3}{9} = \frac{1}{3} \approx 33.3\%$ | 2) $\frac{4}{9} \approx 44.4\%$ | 3) $\frac{7}{9} \approx 77.7\%$ | 4) $\frac{5}{9} \approx 55.5\%$.

**Nivel Rojo:** 
1) $\frac{5}{20} = 25\%$ | 2) $\frac{1}{5} = 20\%$ | 3) $\frac{2}{4} = 50\%$ | 4) $\frac{5}{100} = 0.05$.
```

---

## 7. Autoevaluación y Cierre

```ad-question
title: Pregunta 1
¿Cómo se define un experimento aleatorio ($\epsilon$)?
a) Una acción con un resultado previsible.
b) Una acción cuyo resultado no se puede predecir con certeza.
c) Un suceso que siempre ocurre (100% de probabilidad).
d) La suma de todos los casos favorables.
*Respuesta: b*
```

```ad-question
title: Pregunta 2
Si en una bolsa hay 5 canicas blancas y 5 negras, ¿cuál es la probabilidad de sacar una blanca?
a) $\frac{1}{5}$
b) $0.5$
c) $100\%$
d) $\frac{5}{5}$
*Respuesta: b*
```

```ad-question
title: Pregunta 3
Participas en una rifa de 50 números por un premio de $500 USD. Si tienes 1 boleto, ¿cuál es tu probabilidad de ganar?
a) $\frac{1}{500}$
b) $50\%$
c) $2\%$
d) $\frac{1}{10}$
*Explicación: $\frac{1}{50} = \frac{2}{100} = 0.02 = 2\%$. Respuesta: c*
```

> [!tip] 💡 En la próxima clase
> Una vez dominada la Regla de Laplace, exploraremos qué sucede cuando un evento depende de otro. En la siguiente sesión estudiaremos la **Probabilidad Condicionada** y cómo cambian las posibilidades tras un primer suceso.

---
> [!info] 🧭 Navegación
> ◀ **Anterior**: N/A | ▲ **Índice**: [[00 - Índice del curso]] | ▶ **Siguiente**: [[Clase 02 — Probabilidad Condicionada]]