# 📖 Guía de estudio — Clase 02: Medidas de Tendencia Central (Media, Mediana y Moda)

> [!info] 📌 Conceptos clave
> 1. **¿Para qué sirven?** Las medidas de tendencia central nos ayudan a resumir todo un conjunto de datos en un solo valor representativo. ¡Es como encontrar el "centro de gravedad" de la información!
> 2. **El gran objetivo:** Su propósito es describir dónde se sitúa el centro de una distribución de datos.
> 3. **Tipos de datos:** Los procedimientos varían si trabajamos con **datos sin agrupar** (listas sueltas) o **datos agrupados en intervalos** (tablas de frecuencia), tal como nos enseña el Profe Alex.
> 4. **Sentido común:** No basta con calcular; siempre debemos aplicar un "chequeo de lógica" al resultado (por ejemplo, si el promedio de hermanos es $1,4$, lo redondeamos a $1$ porque no existen "pedazos" de personas).

---

## TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Media ($\bar{x}$)** | Es el promedio aritmético. Se suman todos los datos y se dividen para el total de datos ($n$). <br> $\bar{x} = \frac{\sum x_i}{n}$ <br> *Nota: Usa la lógica; si el dato es discreto (personas), redondea al entero más cercano.* |
| **Mediana ($M_e$)** | Es una **medida de posición**. Es el valor que ocupa el lugar central tras ordenar los datos. <br> - **Si $n$ es impar:** Es el dato del centro. <br> - **Si $n$ es par:** Es el promedio de los dos datos centrales. |
| **Moda ($M_o$)** | Es el valor (o los valores) que más se repite. <br> - **Bimodal:** Dos modas. <br> - **Multimodal:** Más de dos modas. |
| **Marca de Clase ($x_i$)** | Punto medio de un intervalo en datos agrupados. Se obtiene sumando los límites del intervalo y dividiendo para 2. |
| **Frecuencia ($f_i$)** | El número de veces que se repite un dato específico o cuántos datos caen en un intervalo. |
| **Total de datos ($n$)** | La suma de todas las frecuencias absolutas ($\sum f_i$). |

---

## EJEMPLOS RESUELTOS ADICIONALES

```ad-example
title: Ejemplo A — Edades de compañeros
**Datos originales:** 15, 16, 14, 17, 15 (años)

1. **Media ($\bar{x}$):**
   - Sumamos: $15 + 16 + 14 + 17 + 15 = 77$
   - Dividimos: $77 / 5 = 15,4$
   - **¡Logrado!** El promedio es **15,4 años**.

2. **Mediana ($M_e$):**
   - Primero ordenamos: 14, 15, **15**, 16, 17
   - Como $n=5$ (impar), el valor central es el tercer dato.
   - **Resultado:** $M_e = \mathbf{15 años}$.

3. **Moda ($M_o$):**
   - El valor que más se repite es el 15.
   - **Resultado:** $M_o = \mathbf{15 años}$.
```

```ad-example
title: Ejemplo B — Ahorros semanales en dólares ($USD)
**Datos originales:** $10, $15, $10, $20, $25

1. **Media ($\bar{x}$):**
   - Sumamos: $10 + 15 + 10 + 20 + 25 = 80$
   - Dividimos: $80 / 5 = 16$
   - **¡Ya lo tenemos!** El ahorro promedio es de **$16 USD**.

2. **Mediana ($M_e$):**
   - Ordenamos: $10, $10, **$15**, $20, $25
   - El dato central es el 15.
   - **Resultado:** $M_e = \mathbf{$15 USD}$.

3. **Moda ($M_o$):**
   - El valor $10 aparece dos veces.
   - **Resultado:** $M_o = \mathbf{$10 USD}$.
```

---

## EJERCICIOS DE REPASO

```ad-abstract
title: 🟢 Fácil
1. Encuentra la media ($\bar{x}$) y la moda ($M_o$) de las siguientes notas: 7, 8, 9, 7, 10.
2. Un grupo de amigos tiene la siguiente cantidad de hermanos: 1, 2, 0, 1. Calcula el promedio ($\bar{x}$) y aplica el "chequeo de lógica" del Profe Alex.
3. Identifica la moda ($M_o$) en esta lista de tallas de calzado: 36, 38, 38, 37, 38, 39.
```

```ad-abstract
title: 🟡 Medio
1. **Mediana con $n$ par:** Calcula la mediana ($M_e$) de estas estaturas (en cm): 150, 162, 155, 158, 160, 152. *Tip: Ordena y encierra los dos números centrales para promediarlos.*
2. **Mediana con $n$ par:** Halla la mediana ($M_e$) de los siguientes puntajes: 10, 20, 15, 25.
3. **Datos agrupados:** Para un estudio se usa el intervalo $[20, 30)$. Determina su **marca de clase ($x_i$)**.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
Un estudiante registra el costo de 6 artículos escolares: **$2,50, $1,50, $5,00, $2,50, $3,00, $4,50**.

1. Calcula la **media ($\bar{x}$)** y la **mediana ($M_e$)** de los precios.
2. **Análisis de experto:** Si el artículo de $5,00 es mucho más caro que los demás, ¿cuál de las dos medidas crees que representa mejor el gasto "típico" del estudiante? ¿La media ($\bar{x}$) o la mediana ($M_e$)? Justifica usando el concepto de "medida de posición".
```

---

> [!tip] 💡 Consejo de estudio
> ¡El orden es la clave del éxito! Antes de calcular la **Mediana ($M_e$)** o la **Moda ($M_o$)**, acostúmbrate siempre a **ordenar tus datos de menor a mayor**. En conjuntos de datos grandes, esto te permite "visualizar" el centro y no olvidar ningún valor repetido. Como dice el Profe Alex: ¡el orden facilita enormemente la vida del estadístico!