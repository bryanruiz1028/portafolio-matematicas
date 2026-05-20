# 📖 Guía de estudio — Clase 02: Tablas de frecuencia agrupadas por intervalos

> [!info] 📌 Conceptos clave
> - **Tablas simples vs. agrupadas:** Las tablas simples se organizan con valores puntuales (un dato por fila), ideales para variables discretas con pocos valores. Las tablas agrupadas utilizan intervalos para manejar grandes volúmenes de datos o variables continuas.
> - **Criterio de selección:** Se recomienda el paso de una tabla simple a una de intervalos cuando el conjunto presenta más de 12 valores diferentes o cuando se requiere mejorar la estética y legibilidad de los gráficos estadísticos (como histogramas).
> - **Utilidad didáctica:** Estas tablas son la base para organizar la información antes de calcular medidas de tendencia central (media, mediana, moda), medidas de dispersión y la construcción de representaciones gráficas profesionales.
> - **Precisión vs. Aproximación:** Mientras que las tablas simples son exactas, las de intervalos son aproximaciones útiles. Para el análisis de datos masivos, la pérdida mínima de precisión se compensa con la claridad en la interpretación de tendencias.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Rango (R)** | Diferencia entre el valor máximo y el mínimo: $R = X_{max} - X_{min}$. Indica la dispersión total de los datos. |
| **Número de intervalos (k)** | Cantidad de filas o grupos. Se calcula con la Regla de Sturges: $k = 1 + 3.322 \log_{10}(n)$ o $k = 1 + \log_{2}(n)$. **Recomendación:** Aproximar siempre al número impar más cercano para facilitar cálculos posteriores. |
| **Amplitud (A)** | El ancho de cada intervalo: $A = R / k$. **Regla de oro:** Siempre se aproxima al número entero siguiente (redondeo al alza/techo), incluso si el decimal es pequeño. |
| **Marca de Clase ($x_i$)** | Es el punto medio del intervalo, representante del grupo para cálculos matemáticos: $x_i = \frac{L_{inf} + L_{sup}}{2}$. |
| **Frecuencia Absoluta ($f_i$)** | Cantidad de datos en un intervalo. Se usa el corchete $[$ para incluir el límite inferior y paréntesis $)$ para excluir el superior: $[L_{inf}, L_{sup})$. |
| **Frecuencia Relativa ($h_i$)** | Proporción que representa cada intervalo respecto al total: $h_i = f_i / n$. |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Peso de estudiantes en kg
**Contexto:** Se analiza el peso de 40 estudiantes ($n=40$).
1. **Identificación de datos:** $X_{min} = 33$ kg; $X_{max} = 53$ kg.
2. **Cálculo del Rango (R):** $53 - 33 = 20$.
3. **Número de intervalos (k):** Usando Sturges, $1 + 3.322 \log_{10}(40) \approx 6.32$. Aproximamos al impar más cercano: **7**.
4. **Cálculo de Amplitud (A):** $20 / 7 \approx 2.85$. Aproximamos al entero siguiente: **3**.
5. **Construcción del primer intervalo:** Inicia en 33 y sumamos la amplitud ($33 + 3 = 36$). El intervalo es $[33, 36)$.
6. **Marca de clase ($x_1$):** $x_1 = \frac{33 + 36}{2} = 34.5$.

✅ **Resultado de la estructura:**
Se obtienen 7 intervalos: [33-36), [36-39), [39-42), [42-45), [45-48), [48-51), [51-54]. Note que el último intervalo cierra con corchete para incluir el valor máximo.
```

```ad-example
title: Ejemplo B — Gasto de clientes en un Centro Comercial ($USD)
**Contexto:** Se adaptan los datos originales de edades (5 a 71 años) de 60 clientes a un contexto de gasto monetario.

**Paso 1: Cálculo inicial**
- Rango original: $71 - 5 = 66$.
- Intervalos (k): $1 + 3.322 \log_{10}(60) \approx 6.9 \rightarrow$ **7** (número impar).
- Amplitud (A): $66 / 7 \approx 9.42 \rightarrow$ Redondeo al entero siguiente: **10**.

**Paso 2: Ajuste de rango (El concepto de "Nuevo Rango")**
- Al usar 7 intervalos de amplitud 10, cubrimos un rango de 70 ($7 \times 10 = 70$).
- Esto genera un "exceso" de 4 unidades respecto al rango original ($70 - 66 = 4$).
- Para centrar la tabla didácticamente, distribuimos el exceso: 2 unidades antes del inicio y 2 unidades después del final.
- **Nuevo inicio:** $5 - 2 = 3$.

**Paso 3: Construcción de intervalos**
- Los intervalos ahora inician en 3: [3-13), [13-23), [23-33), [33-43), [43-53), [53-63), [63-73].
- Esta técnica asegura que los datos extremos no queden en los bordes exactos, facilitando la simetría en gráficos.
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
1. Un grupo de conductores registra velocidades entre 27 km/h y 68 km/h. Calcule el **Rango (R)**.
2. En un torneo, el menor número de cestas fue 2 y el mayor 10. ¿Cuál es el **Rango**?
3. Si el Rango es 44 y se definen 7 intervalos, ¿cuál es la **Amplitud (A)** aplicando el redondeo reglamentario?
```

```ad-abstract
title: 🟡 Medio
1. **Análisis de pertinencia:** Un estudio de "Horas de lectura" arroja valores entre 0 y 30, con 18 valores distintos. ¿Es preferible una tabla simple o de intervalos? Justifique basándose en el criterio de los 12 valores.
2. **Marcas de Clase:** Dada una tabla que inicia en 27 con amplitud 7, calcule las marcas de clase ($x_i$) para los primeros tres intervalos. Utilice la fórmula $x_i = \frac{L_{inf} + L_{sup}}{2}$.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
Un banco audita 50 transacciones ($n=50$). El monto mínimo es $10 y el máximo $95.
1. Determine el **Número de intervalos (k)** usando la Regla de Sturges (aproxime al impar más cercano).
2. Calcule la **Amplitud (A)** aproximada al entero superior.
3. **Ajuste de precisión:** Verifique si existe un exceso entre el rango cubierto ($k \times A$) y el rango original. Si existe, aplique la técnica del **Nuevo Rango** para determinar el límite inferior del primer intervalo.
4. Si el primer intervalo resultante tiene una frecuencia absoluta ($f_1$) de 8, calcule su **Frecuencia Relativa ($h_1$)** y su porcentaje.
```

> [!tip] 💡 Consejo de estudio
> Para un conteo infalible, utiliza la técnica de **"conteo mediante líneas" (tally marks)**: tacha cada dato de tu lista original y coloca una línea en el intervalo correspondiente. 
> 
> **Regla Crítica de Límites:** El valor que coincide con el límite superior de un intervalo **no se cuenta en esa fila**, sino en la siguiente (ej. en el intervalo [33, 36), el 36 queda fuera). La única excepción es el **último intervalo de la tabla**, el cual debe ser cerrado en ambos lados $[L_{inf}, L_{sup}]$ para asegurar la inclusión del valor máximo del conjunto.