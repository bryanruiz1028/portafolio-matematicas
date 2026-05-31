# 📖 Guía de estudio — Clase 01: El concepto de volumen y prismas rectangulares

> [!info] 📌 Conceptos clave
> *   **Definición de volumen:** Es la magnitud física que expresa el espacio tridimensional que ocupa un cuerpo. Todo objeto físico, desde un coche hasta una caja de zapatos, posee un volumen.
> *   **Volumen vs. Capacidad:** Conceptos hermanos pero distintos. El **volumen** es el espacio que ocupa el cuerpo en sí, mientras que la **capacidad** es la medida de lo que puede contener dicho cuerpo.
> *   **Unidades cúbicas:** Medimos el volumen comparando el cuerpo con cubos unitarios ($1 \times 1 \times 1$). Si el objeto está en metros, usamos metros cúbicos ($ \text{m}^3 $); si es pequeño, centímetros cúbicos ($ \text{cm}^3 $).
> *   **El significado del exponente $3$:** Representa las tres dimensiones del espacio: largo, ancho y alto. 
> *   **⚠️ Alerta de error común:** El exponente $3$ indica dimensiones, **no es un multiplicador**. Un cubo con una **arista** de $2\text{ m}$ no tiene un volumen de $2\text{ m}^3$. El volumen real es $2 \times 2 \times 2 = 8\text{ m}^3$. Confundir la medida del lado con el volumen total es el error más frecuente en geometría.

## Tabla de Definiciones y Fórmulas

| Término | Definición / Fórmula |
| :--- | :--- |
| **Volumen ($V$)** | Cantidad de espacio ocupado por un cuerpo. |
| **Arista ($a$ o $l$)** | El segmento de línea donde se encuentran dos caras de un cuerpo geométrico (comúnmente llamado "lado"). |
| **Unidad Cúbica** | Cubo estándar que mide una unidad por cada arista (ej. $1\text{ cm} \times 1\text{ cm} \times 1\text{ cm} = 1\text{ cm}^3$). |
| **Volumen del Cubo** | $V = a^3$ (Arista al cubo o $a \times a \times a$). El cubo es un caso especial donde todas las dimensiones son iguales. |
| **Ortoedro (Prisma Rectangular)** | Cuerpo con seis caras rectangulares. $V = \text{largo} \times \text{ancho} \times \text{alto}$ o $V = A_{\text{base}} \times h$. |

## Sección de Ejemplos Resueltos

```ad-example
title: Ejemplo A — Volumen de un cubo (Uso de la Arista)
**Problema:** Determinar el volumen de un cubo cuya arista mide $3\text{ m}$.

**Análisis pedagógico:** 
Visualicemos que para construir este cubo, primero formamos una fila de $3$ cubos unitarios. Luego, completamos una base de $3 \times 3 = 9$ cubos. Finalmente, apilamos $3$ "pisos" de esos $9$ cubos.

**Proceso paso a paso:**
1. Identificar la medida de la arista ($a$): $a = 3\text{ m}$.
2. Aplicar la fórmula: $V = a^3$.
3. Sustituir y operar: $V = 3\text{ m} \times 3\text{ m} \times 3\text{ m}$.
4. Cálculo numérico: $3 \times 3 = 9$; $9 \times 3 = 27$.
5. **Resultado:** $V = 27\text{ m}^3$.
```

```ad-example
title: Ejemplo B — Volumen de un Ortoedro (Logística y Almacenamiento)
**Problema:** Una caja de carga mide $5\text{ m}$ de largo, $3\text{ m}$ de ancho y $2\text{ m}$ de alto. Calcule su volumen para determinar el costo de almacenamiento, considerando que la tarifa se aplica por cada $\text{m}^3$ ocupado.

**Proceso paso a paso:**
1. **Calcular el área de la base (Nivel 1):** Multiplicamos largo por ancho para saber cuántos cubos caben en el "suelo" de la caja.
   $A_{\text{base}} = 5\text{ m} \times 3\text{ m} = 15\text{ m}^2$.
2. **Multiplicar por el número de niveles (Altura):** Dado que la altura es de $2\text{ m}$, tenemos dos niveles idénticos de $15$ cubos cada uno.
   $V = 15\text{ m}^2 \times 2\text{ m} = 30\text{ m}^3$.
3. **Interpretación:** El volumen total es de $30\text{ m}^3$. Si el costo de envío fuera, por ejemplo, de $\$10\text{ USD}$ por cada $\text{m}^3$, el costo total de esta caja sería de $\$300\text{ USD}$ debido al espacio que ocupa.
```

## Ejercicios de Repaso Graduados

```ad-abstract
title: 🟢 Fácil: Aplicación Directa
1. **El Cubo de Rubik gigante:** Si un cubo decorativo tiene una arista de $4\text{ m}$, ¿cuál es su volumen total?
2. **Contenedor básico:** Calcula el volumen de un prisma rectangular que mide $12\text{ m}$ de largo, $8\text{ m}$ de ancho y $3\text{ m}$ de alto. 
*Pista: Multiplica las tres dimensiones empleando la unidad $\text{m}^3$.*
```

```ad-abstract
title: 🟡 Medio: Análisis por Partes
**Prisma con decimales:** Un estuche técnico mide $4\text{ cm}$ de largo, $3.5\text{ cm}$ de ancho y $6\text{ cm}$ de alto.
1. Calcula primero el área de la base ($A_{\text{base}}$). *(Autocorrección: Deberías obtener $14\text{ cm}^2$)*.
2. Utiliza ese resultado para hallar el volumen total. ¿Cuántos cubos de $1\text{ cm} \times 1\text{ cm} \times 1\text{ cm}$ caben en total?
```

```ad-abstract
title: 🔴 Avanzado: Desafío de Precisión
**Prisma cuadrangular:** Un pedestal tiene una base cuadrada de $2.2\text{ m}$ por lado y una altura de $1.5\text{ m}$.
1. **Cálculo:** Determina el volumen final del pedestal.
2. **Reflexión pedagógica:** El resultado es $7.26\text{ m}^3$. 
   *   **Pregunta:** Si tuvieras cubos sólidos de $1\text{ m}^3$, ¿qué significa ese decimal?
   *   **Guía:** Significa que el espacio es ocupado por $7$ cubos completos y una fracción ($26\%$) de un octavo cubo. Para el cálculo decimal, recuerda que $2.2 \times 2.2 = 4.84$; luego multiplica este valor por la altura de $1.5$.
```

## Cierre y Estrategia de Aprendizaje

> [!tip] 💡 Consejo de estudio: La técnica de los "Pisos"
> Para no depender de la memoria mecánica de las fórmulas, utiliza siempre la **visualización espacial**. Divide mentalmente cualquier prisma en niveles:
> 1. Mira la base y cuenta cuántos cubos unitarios caben en ella (Área de la base).
> 2. Mira la altura y pregúntate cuántas veces se repite esa capa de cubos (Altura).
> Al multiplicar el "primer piso" por el "número de pisos", obtendrás el volumen sin esfuerzo y entenderás por qué las unidades resultantes siempre son elevadas al cubo ($\text{u}^3$).