# 📖 Guía de estudio — Clase 01: Conceptos básicos de estadística

> [!info] **¿Qué aprenderemos hoy?**
> ¡Hola! Soy tu profesor de matemáticas y hoy vamos a descubrir cómo la estadística nos ayuda a entender el mundo. Básicamente, la estadística sirve para **recopilar, organizar y analizar datos** para responder preguntas curiosas (como ¿cuál es el deporte favorito del salón?). 
> 
> Aprenderemos a diferenciar entre la **población** (cuando hablamos de *todos*) y la **muestra** (un grupito seleccionado). También veremos que los datos pueden ser **cualitativos** (cualidades) o **cuantitativos** (números). Finalmente, usaremos "brújulas" para encontrar el centro de los datos: la **media, mediana y moda**, y aprenderemos a usar los **deciles** para saber en qué posición se encuentra un valor. ¡Comencemos!

---

## 2. Fórmulas y definiciones importantes

Aquí tienes tu tabla de herramientas. No te asustes por los símbolos como $\bar{x}$, ¡son solo nombres elegantes que usamos los matemáticos para que todo se vea más organizado!

| Término | Definición / Fórmula |
| :--- | :--- |
| **Población** | Es el conjunto total de "todos" los individuos de los que queremos saber algo. |
| **Individuo** | Cada uno de los elementos o unidades que componen la población. |
| **Muestra** | Un grupo representativo (más pequeño) de la población a quienes realmente encuestamos. |
| **Dato** | Los valores o respuestas que obtenemos (ej. "Pizza", "15 años", "Azul"). |
| **Variable Cualitativa** | Expresa cualidades. **Nominal:** No tiene orden (ej. estado civil). **Ordinal:** Sí tiene orden (ej. medallas: oro, plata, bronce). |
| **Variable Cuantitativa**| Expresa cantidades. **Discreta:** Valores contables (ej. número de hermanos). **Continua:** Valores medibles con decimales (ej. peso o tiempo). |
| **Media ($\bar{x}$)** | Es el promedio. Se calcula con: $\bar{x} = \frac{\sum x_i}{n}$ (Suma de datos dividida por el total). |
| **Mediana ($M_e$)** | Es el valor que está justo en el centro cuando los datos están **ordenados**. |
| **Moda ($M_o$)** | Es el valor que más veces se repite. ¡Como la ropa que está de moda! |
| **Deciles** | 9 valores que dividen los datos en 10 partes. Fórmula de **posición**: $P = \frac{K \cdot n}{10}$. |

> [!important] **Nota sobre los Deciles:** 
> La fórmula nos da la **posición (P)**, no el resultado final. Si la posición te da un número decimal (como 4.5), debes promediar los valores de las posiciones que están alrededor (la 4 y la 5).

---

## 3. Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Identificación de elementos
**Enunciado:** Se realiza una encuesta a 150 estudiantes de la Ciudad de México para saber cuál es su asignatura favorita.

*   **Paso 1:** ¿De quién queremos saber algo? De **todos** los estudiantes de la Ciudad de México (**Población**).
*   **Paso 2:** ¿A quiénes les preguntamos realmente? A los 150 seleccionados (**Muestra**).
*   **Paso 3:** ¿Quién es cada uno? Cada estudiante por separado es un **Individuo**.
*   **Paso 4:** ¿Qué respondieron? Por ejemplo, "Matemáticas". Eso es el **Dato**.

✅ **Resultado:**
- **Población:** Todos los estudiantes de la Ciudad de México.
- **Individuo:** Cada estudiante.
- **Muestra:** 150 estudiantes.
- **Dato:** La asignatura favorita (Cualitativa Nominal).
```

```ad-example
title: Ejemplo B — Promedio y Moda con salarios
**Enunciado:** En una oficina, 5 empleados ganan mensualmente: $400, $450, $400, $500 y $600 USD.

*   **Paso 0 (Hábito de oro):** Ordenar los datos de menor a mayor → $400, $400, $450, $500, $600.
*   **Paso 1 (Media):** Sumamos todo: $400 + 400 + 450 + 500 + 600 = 2350$.
*   **Paso 2 (Media):** Dividimos entre el total de personas (n=5): $2350 / 5 = 470$.
*   **Paso 3 (Moda):** El valor que más se repite es $400 (aparece dos veces).

✅ **Resultado:**
- **Media ($\bar{x}$):** $470 USD.
- **Moda ($M_o$):** $400 USD.
```

---

## 4. Ejercicios de repaso

```ad-abstract
title: Nivel 🟢 Fácil (Identificación)
Clasifica estas variables basándote en lo que aprendimos con el Profe Alex:
1. **Deporte favorito:** (Pista: ¿Es un número o una cualidad?)
2. **Número de hermanos:** (Pista: ¿Puedes tener 2.5 hermanos? No, ¿verdad?)
3. **Peso de un balón de fútbol:** (Pista: Se mide con báscula y puede tener muchos decimales).

*Solución rápida:* 1. Cualitativa Nominal, 2. Cuantitativa Discreta, 3. Cuantitativa Continua (por la precisión del peso).
```

```ad-abstract
title: Nivel 🟡 Medio (Cálculo de tendencias)
Tus amigos tienen estas edades: 14, 15, 15, 16, 17. Hallar:
1. **Media:** Suma las edades y divide entre 5.
2. **Mediana:** Busca el número que quedó en el centro (¡Ya están ordenados!).
3. **Moda:** ¿Cuál es la edad que más se repite?

*Solución:* Media = 15.4 | Mediana = 15 | Moda = 15.
```

```ad-abstract
title: Nivel 🔴 Avanzado (Aplicación con Deciles)
Ahorros de 10 estudiantes: $10, $20, $30, $40, $50, $60, $70, $80, $90, $100.
1. Calcula la posición y el valor del **Decil 2 (D2)**.
2. Calcula la posición y el valor del **Decil 5 (D5)**.

*Ayuda paso a paso:* 
- Para D2: $P = (2 \cdot 10) / 10 = 2$. La posición es 2, el valor es **$20**.
- Para D5: $P = (5 \cdot 10) / 10 = 5$. La posición es 5, el valor es **$50**.
*(¿Viste? ¡El D5 es igual a la mediana!)*
```

---

## 5. 💡 Consejo de estudio

> [!tip] **¿Población o Muestra? ¡Aplica la regla del "Todos"!**
> Para no confundirte, busca siempre la palabra **"Todos"**. Si el estudio dice que se le preguntó a absolutamente cada integrante de un grupo sin dejar a nadie fuera, entonces estás trabajando con la **Población** y **no hay muestra**. 
> 
> Pero si ves un número específico (ej. "se encuestó a 30 personas de la ciudad"), ese número es tu **Muestra**. ¡La muestra siempre es un pedacito del pastel completo!