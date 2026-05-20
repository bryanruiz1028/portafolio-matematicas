# 📖 Guía de estudio — Clase 01: Tablas de Frecuencia Simple

> [!info] 📌 Conceptos clave
> El objetivo principal de una tabla de frecuencias es organizar los datos recolectados para facilitar el análisis estadístico. Esta organización es la base fundamental para crear gráficos y calcular medidas de tendencia central (media, mediana y moda).
> - **Dato ($x_i$):** Es el valor específico o respuesta registrada (ej: edad, nota, número de hermanos).
> - **Muestra ($n$):** El número total de datos obtenidos. (Si se estudia a toda la población, se usa **$N$**).
> - **Tachado de datos:** Método esencial para evitar errores. Consiste en marcar cada dato de la lista original a medida que se cuenta.
> - **Verificación:** La suma de todas las frecuencias absolutas ($f_i$) debe ser exactamente igual a **$n$**, y la suma de porcentajes debe ser idealmente el **100%**.

## 2. Fórmulas y Definiciones Importantes

Término | Símbolo | Definición / Fórmula |
:--- | :---: | :--- |
**Dato** | $x_i$ | Representa el valor de la variable estudiada. |
**Muestra / Población** | $n$ / $N$ | Total de datos recolectados o personas encuestadas. |
**Frecuencia Absoluta** | $f_i$ | Número de veces que se repite un dato específico. |
**Frecuencia Absoluta Acumulada** | $F_i$ | Suma de la frecuencia absoluta actual con las anteriores. |
**Frecuencia Relativa** | $h_i$ | Resultado de dividir la frecuencia absoluta por el total ($f_i / n$). |
**Porcentaje** | $\%$ | $h_i \times 100$ o la fórmula directa: $(f_i \times 100) / n$. |

> [!tip] ⚡ Tip del Profe Alex: El Atajo de la Constante
> Si tu muestra es un número "amigable", puedes hallar una constante para calcular porcentajes más rápido:
> - Si **$n = 50$**: Simplemente multiplica cada $f_i$ por **2** ($100 / 50 = 2$).
> - Si **$n = 40$**: Simplemente multiplica cada $f_i$ por **2.5** ($100 / 40 = 2.5$).

## 3. Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A — Número de hermanos ($n=50$)
**Escenario:** Se encuesta a 50 estudiantes. Al contar, se halla que 11 no tienen hermanos.
**Paso a paso para la primera fila:**
1. **Frecuencia Absoluta ($f_1$):** El dato "0 hermanos" se repite 11 veces. **$f_1 = 11$**.
2. **Frecuencia Absoluta Acumulada ($F_1$):** Al ser la primera fila, el acumulado es el mismo valor: **$F_1 = 11$**.
3. **Cálculo del Porcentaje (%):**
   - *Método tradicional:* $(11 \times 100) / 50 = 1100 / 50 = 22\%$
   - *Método Atajo (n=50):* $11 \times 2 =$ **$22\%$**
**Resultado:** El 22% de los encuestados son hijos únicos.
```

```ad-example
title: Ejemplo B — Gastos diarios en refrigerios ($USD)
**Escenario:** Se analizan 20 compras ($n = 20$). Queremos saber la estadística de los refrigerios que cuestan $2.
**Pasos:**
1. **Identificar la Frecuencia Absoluta ($f_i$):** El valor "$2" aparece 8 veces en la lista. **$f_i = 8$**.
2. **Calcular Frecuencia Relativa ($h_i$):**
   - Fórmula: $f_i / n$
   - Operación: $8 / 20 =$ **$0.4$**
3. **Calcular el Porcentaje (%):**
   - Operación: $0.4 \times 100 =$ **$40\%$**
**Conclusión:** Los refrigerios de $2 representan el 40% del total de ventas.
```

## 4. Ejercicios de Repaso

```ad-abstract
title: 🟢 Nivel: Fácil
1. Dada la lista de edades: `13, 14, 13, 15, 14, 14, 16, 13, 15, 14`. Identifica el valor de **$n$**.
2. De la lista anterior, ¿cuál es la **$f_i$** para la edad de 14 años?
3. Si en un grupo hay 5 personas con 15 años y el total de la muestra es $n = 20$, calcula la frecuencia relativa (**$h_i$**) de esa edad.
```

```ad-abstract
title: 🟡 Nivel: Medio
**Contexto:** Completa los datos para una muestra de **$n = 40$**.
1. Si la primera frecuencia absoluta es $f_1 = 4$ y la segunda es $f_2 = 10$, ¿cuánto vale **$F_2$**?
2. Si un dato tiene $f_i = 10$ y $n = 40$, usa el "Atajo del Profe Alex" ($f_i \times 2.5$) para hallar su **porcentaje**.
3. Si el porcentaje de un dato es el 25% y $n = 40$, ¿cuál es su frecuencia absoluta (**$f_i$**)?
```

```ad-abstract
title: 🔴 Nivel: Avanzado — Aplicación con $USD
**Contexto:** Registra los siguientes 20 precios de artículos escolares para tu tabla:

| | | | | |
| :--- | :--- | :--- | :--- | :--- |
| $5 | $10 | $5 | $15 | $10 |
| $5 | $5 | $15 | $10 | $10 |
| $5 | $10 | $15 | $10 | $15 |
| $5 | $10 | $15 | $10 | $15 |

1. Construye la tabla completa con las columnas $x_i, f_i, F_i, h_i$ y $\%$.
2. ¿Cuál es la frecuencia absoluta acumulada (**$F_i$**) hasta el precio de $10?
3. Calcula el porcentaje total de artículos que cuestan **más de $10 USD**.
*(Pista pedagógica: "Más de $10" significa que NO debes incluir los artículos de exactamente $10).*
```

## 5. Consejo de Estudio

> [!tip] 💡 Recomendaciones para el éxito
> 1. **Método de Tacha y Suma:** Tacha cada dato de la lista original a medida que lo anotes en la columna $f_i$. Al final, suma toda la columna $f_i$; si no coincide con $n$, cometiste un error de conteo.
> 2. **Regla de los 3 decimales:** Para obtener una suma de porcentaje lo más cercana al 100% (especialmente cuando las divisiones no son exactas), utiliza siempre **tres cifras decimales** en tu frecuencia relativa ($h_i$).
> 3. **Precisión:** Si la suma final te da 99.9%, es aceptable y se debe al redondeo de decimales.