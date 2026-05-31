# 📖 Guía de estudio — Clase 01: Introducción a los Cuartiles

> [!info] 📌 Conceptos clave
> *   **Definición:** Los cuartiles son los tres valores que dividen un conjunto de datos, previamente ordenados, en cuatro partes iguales.
> *   **Relación con porcentajes:** El Cuartil 1 ($Q_1$) marca el $25\%$, el Cuartil 2 ($Q_2$) el $50\%$, y el Cuartil 3 ($Q_3$) el $75\%$ de la información.
> *   **Equivalencia fundamental:** El Cuartil 2 ($Q_2$) siempre es igual a la **Mediana**.
> *   **Interpretación "menor o igual a":** El valor de un cuartil nos indica que un determinado porcentaje de los datos es **menor o igual** a ese valor. Por ejemplo, si el $Q_1 = 15$, significa que el $25\%$ de los datos son menores o iguales a $15$.

---

### 📏 Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Cuartiles** | Medidas de posición que dividen la muestra en cuatro grupos de igual tamaño. |
| **Datos ordenados** | Organización obligatoria de menor a mayor para que el cálculo tenga sentido. |
| **Posición ($i$)** | El lugar que ocupa un dato en la serie (no es el valor del cuartil). |
| **Fórmula (Datos impares)** | $Posición = \frac{k(n+1)}{4}$ |
| **Fórmula (Datos pares)** | $Posición = \frac{kn}{4}$ |
| **Componentes** | $k$: número del cuartil buscado ($1, 2, 3$); $n$: total de datos. |

> [!important] ⚠️ Nota didáctica
> Recuerda que el resultado de aplicar la fórmula es la **posición**. Una vez hallado ese número, debes buscar qué **valor** se encuentra en ese lugar de tu lista de datos.

---

### 📝 Ejemplos resueltos

```ad-example
title: Ejemplo A: Edades de 11 personas (Método Lógico y Fórmula)
**Datos:** 15, 17, 16, 16, 15, 14, 15, 16, 17, 15, 18

1. **Ordenar los datos:** 14, 15, 15, 15, 15, **16**, 16, 16, 17, 17, 18.
2. **Identificar $Q_2$ (Mediana):** Al ser 11 datos (impar), el centro exacto es el dato en la posición 6.
   * ✅ **Valor:** $Q_2 = 16$.
   * *Verificación con fórmula:* $Posición = \frac{2(11+1)}{4} = \frac{24}{4} = 6$. (Coincide con la posición 6).
3. **Identificar $Q_1$:** Miramos la mitad izquierda (los 5 datos antes del centro: 14, 15, **15**, 15, 15). El centro de esa mitad es 15.
   * ✅ **Valor:** $Q_1 = 15$.
4. **Identificar $Q_3$:** Miramos la mitad derecha (los 5 datos después del centro: 16, 16, **17**, 17, 18). El centro es 17.
   * ✅ **Valor:** $Q_3 = 17$.
```

```ad-example
title: Ejemplo B: Edades de 10 personas (Cálculo con promedio de posiciones)
**Datos:** 10 personas donde los datos centrales en las posiciones 5 y 6 son 17 y 18 años.

1. **Cálculo de $Q_2$ (Centro):** Al ser 10 datos (par), no hay un solo centro. Tomamos los valores de las posiciones 5 y 6.
   * Promedio: $\frac{17 + 18}{2} = 17.5$.
   * ✅ **Valor:** $Q_2 = 17.5$ años.
2. **Cálculo de $Q_1$:** Al dividir el conjunto, nos quedan 5 datos a la izquierda. El dato central de esa mitad es el $Q_1$.
   * ✅ **Valor:** $Q_1 = 16$.
3. **Cálculo de $Q_3$:** Tomamos los 5 datos a la derecha. El dato central de esa mitad es el $Q_3$.
   * ✅ **Valor:** $Q_3 = 19$.
```

---

### ✍️ Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel Fácil: Cantidad de pantalones
Se preguntó a 5 personas cuántos pantalones tienen: **3, 5, 8, 9, 10**. 
1. Identifica primero la **Mediana** del conjunto.
2. ¿Cuál es el valor del $Q_2$? Justifica tu respuesta basándote en la Mediana.
```

```ad-abstract
title: 🟡 Nivel Medio: Respuestas correctas
En un examen, los estudiantes obtuvieron estos resultados: 
**1, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15, 17, 19**.
Son 13 datos (impar). Encuentra $Q_1, Q_2$ y $Q_3$ usando el método de observación de mitades.
*Pista: Para las mitades con número par de datos, usa el promedio de los dos centrales.*
```

```ad-abstract
title: 🔴 Nivel Avanzado: Pesos en kilogramos
Calcula los tres cuartiles para el siguiente conjunto de 12 pesos (número par) ya ordenados:
**55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66**.
Aplica el promedio de las posiciones centrales para cada caso:
* $Q_2$: Promedio entre posiciones 6 y 7.
* $Q_1$: Promedio entre posiciones 3 y 4 de la primera mitad.
* $Q_3$: Promedio entre posiciones 3 y 4 de la segunda mitad.
```

---

> [!tip] 💡 Consejo de estudio
> El error más común no es la matemática, sino el olvido. **¡Nunca calcules un cuartil sin antes ordenar tus datos de menor a mayor!** Si usas los datos desordenados, estarás encontrando la posición de un número al azar, no un estadístico real.