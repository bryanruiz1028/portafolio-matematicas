# 📖 Guía de estudio — Clase 05: Regla de la suma (Unión de sucesos)

¡Qué tal, amigas y amigos! Espero que estén muy bien. Hoy vamos a platicar sobre un tema que parece difícil pero, como siempre les digo, si lo vemos gráficamente se vuelve pan comido. Vamos a aprender a calcular la probabilidad de que ocurra una cosa **o** la otra.

> [!info] 📌 Conceptos clave
> Para dominar la unión de sucesos, grabemos estos puntos en nuestra mente:
> 1. **La clave es la "o":** En matemáticas, cuando veas la letra "o", estamos hablando de una **Unión ($\cup$)**. Significa que nos sirve que pase el suceso A, el suceso B, o que pasen ambos a la vez. Por el contrario, la letra "y" se refiere a la **Intersección ($\cap$)**, que son los elementos que cumplen ambas condiciones al mismo tiempo.
> 2. **La Regla de la Suma:** Es la herramienta que nos permite sumar las probabilidades de dos eventos para saber la probabilidad total de su unión.
> 3. **¿Se tocan o no se tocan?:** 
>    - Si dos sucesos tienen elementos en común, hay una **intersección**. 
>    - Si es imposible que ocurran al mismo tiempo (como ser perro y ser gato a la vez), se llaman **Mutuamente Excluyentes**.
> 4. **No contar dos veces:** Este es el secreto del Profe Alex. Si hay elementos que cumplen ambas condiciones, al sumar el grupo A y el grupo B, estarás contando a esos amigos dos veces. Por eso, en la fórmula general, restamos la intersección una vez para "limpiar" el exceso.
> 5. **Tres formas de hablar:** Recuerda que puedes dar tu resultado como **fracción** (3/5), **decimal** (0.6) o **porcentaje** (60%). ¡Tú eliges la que más te guste o la que pida tu examen!

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Unión de sucesos ($A \cup B$)** | Es el evento que ocurre cuando se cumple A, se cumple B o ambos. Se asocia con la vocal "**o**". |
| **Intersección ($A \cap B$)** | Son los elementos que "viven" en ambos grupos simultáneamente. Se asocia con la letra "**y**". |
| **Regla de la Suma (General)** | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| **Sucesos Mutuamente Excluyentes** | Cuando es imposible que ocurran juntos. Aquí, $P(A \cap B) = 0$ (la resta no es necesaria). |

---

## Ejemplos resueltos

```ad-example
title: Ejemplo A — El dado (Sucesos con intersección)
**Enunciado:** Al lanzar un dado normal de 6 caras, ¿cuál es la probabilidad de que caiga un número par **o** un número mayor que 3?

1. **Casos totales:** Tenemos 6 opciones {1, 2, 3, 4, 5, 6}.
2. **Identificar grupos:**
   - Suceso A (Pares): {2, **4**, **6**} → 3 casos.
   - Suceso B (Mayores que 3): {**4**, 5, **6**} → 3 casos.
3. **Identificar la intersección:** Nota que el 4 y el 6 aparecen en ambos grupos. ¡No los contemos doble! Hay 2 casos en la intersección.
4. **Aplicar la fórmula:**
   $P(A \cup B) = \frac{3}{6} + \frac{3}{6} - \frac{2}{6} = \frac{4}{6}$
5. ✅ **Resultado:** Simplificando llegamos a **2/3**. En decimal es $0.666...$ y en porcentaje lo redondeamos a **66.7%**.
```

```ad-example
title: Ejemplo B — La Fiesta (Uso de lógica)
**Enunciado:** En una fiesta con **80 personas**, 40 son mayores de 20 años y 10 son extranjeros. El organizador nos dice que **8 de esos extranjeros son mayores de 20 años**. Si elegimos a alguien al azar, ¿cuál es la probabilidad de que sea mayor de 20 años **o** extranjero?

1. **Datos claros:**
   - $P(\text{Mayor}) = 40/80$
   - $P(\text{Extranjero}) = 10/80$
   - $P(\text{Mayor} \cap \text{Extranjero}) = 8/80$ (Este dato sale directo del enunciado: los que cumplen ambas condiciones).
2. **Cálculo:** Aplicamos la resta para no duplicar a los 8 extranjeros que ya contamos dentro de los 40 mayores.
   $40/80 + 10/80 - 8/80 = 42/80$
3. ✅ **Resultado:** Simplificando la fracción nos da **21/40**, que equivale a un **52.5%**.
```

---

## Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel Fácil: La Tienda de Mascotas
**Inventario de la tienda (Total 15 animales):**
- **7 Perros** (3 son blancos, 4 de otros colores).
- **6 Gatos** (ninguno es blanco).
- **2 Conejos** (ambos son blancos).

1. ¿Cuál es la probabilidad de elegir un perro **o** un gato? *Pista: Son excluyentes, escribe $P(A \cap B) = 0$ para demostrar tu lógica.*
2. ¿Cuál es la probabilidad de elegir un animal blanco **o** un perro? *¡Cuidado! Hay perros que también son blancos.*
3. ¿Cuál es la probabilidad de elegir un conejo **o** un animal que no sea perro?
```

```ad-abstract
title: 🟡 Nivel Medio: Dados y Diagramas
Para estos ejercicios, es **obligatorio** dibujar primero tu diagrama de Venn (los dos círculos). ¡Si lo ves, lo entiendes!

1. Calcula la probabilidad de obtener un número primo {2, 3, 5} **o** un número mayor que 2.
2. Calcula la probabilidad de obtener un número menor que 3 **o** un número par.
3. Calcula la probabilidad de obtener el número 1 **o** un número mayor que 2. (Observa en tu dibujo si los círculos se tocan o están separados).
```

```ad-abstract
title: 🔴 Nivel Avanzado: Tablas de Contingencia
En una cena para **60 personas**, tenemos a 32 mujeres y 28 hombres. Sabemos que 20 mujeres comieron flan y 16 hombres también comieron flan. El resto de los invitados comió torta.

1. **Completa la tabla:** Antes de calcular nada, dibuja una tabla de doble entrada (Hombres/Mujeres vs Flan/Torta) y rellena todos los huecos.
2. Calcula la probabilidad de que una persona elegida al azar sea **mujer o haya comido flan**.
3. Calcula la probabilidad de que sea **hombre o haya comido torta**.
*Nota pedagógica: Observa cómo la tabla ya separa los grupos por ti, haciendo que identificar la intersección sea mucho más visual y rápido.*
```

---

> [!tip] 💡 Consejo del Profe Alex
> ¡Amigas y amigos, no se compliquen con las fórmulas! Mi mejor consejo es que antes de tocar la calculadora, hagan un **diagrama de conjuntos (círculos)** o una **tabla de doble entrada**. Al ver los datos dibujados, notarás físicamente qué elementos están en la "zona de cruce". Así entenderás que restamos la intersección simplemente porque no queremos contar a la misma persona o al mismo objeto dos veces. **¡Si lo ves, no lo olvidas!**