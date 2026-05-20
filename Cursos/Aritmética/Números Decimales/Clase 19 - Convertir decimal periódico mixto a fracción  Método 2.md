# Clase 19 — Convertir decimal periódico mixto a fracción | Método 2

#algebra #convertirdecimal
Referencia: Curso de Fracciones | Bloque: Conversiones | Lección 19

> [!info] 🧭 Navegación
> ⬅️ **Clase anterior:** [Clase 18 — Convertir decimal periódico puro a fracción](Clase18)
> 📋 **Índice:** [Curso de Fracciones](IndiceFracciones)

---

## 1. Importancia y Aplicaciones

> [!info] 🌍 Relevancia y aplicaciones
> ¡Qué tal, amigos! Espero que estén muy bien. En matemáticas, la precisión lo es todo. Como los decimales periódicos son infinitos, la única forma de trabajar con ellos sin perder exactitud es convirtiéndolos en fracciones.
> 
> *   **Aplicación USD:** En el mundo de las finanzas, una tasa de interés o el valor de una acción puede ser de $1,1\overline{6}$ USD. Operar con este valor es mucho más sencillo y exacto si usamos su equivalente: $7/6$ de dólar.
> *   **Aplicación Práctica:** En arquitectura o diseño industrial, si una pieza mide $0,41\overline{6}$ mm, usar la fracción nos asegura que todas las partes encajen perfectamente sin errores de redondeo.
> *   **Situación Cotidiana:** Las estadísticas deportivas (como promedios de bateo o efectividad) a menudo arrojan estos decimales. La fracción nos dice exactamente cuántas unidades de éxito hubo por cada intento.

---

## 2. Definición del Concepto y Reglas de Oro

> [!note] 📌 ¿Qué es un decimal periódico mixto?
> Es aquel que, después de la coma, tiene dos partes: una **parte no periódica** (que no se repite) y una **parte periódica** (que se repite infinitamente). 
> **Ejemplo:** En $23,7\overline{32}$, el $7$ es el anteperiodo (no se repite) y el $32$ es el periodo ($32, 32, 32...$).

> [!warning] ⚠️ Error común
> ¡Mucho cuidado aquí! El error más frecuente es intentar restar las ecuaciones sin que los periodos estén perfectamente alineados. Si no "limpias" primero la parte no periódica, los decimales no se cancelarán y la resta te dará un resultado erróneo.

> [!tip] 💡 Truco para recordarlo
> Fíjense en este detalle: imaginen que van a "limpiar la casa". Antes de pasar la escoba (la resta), primero deben "mover los muebles" (la coma) para que el periodo quede solito justo después de la coma. Una vez que lo conviertes en un periódico puro, ¡el camino está despejado!

---

## 3. Procedimiento Paso a Paso

Para aplicar el **Método 2 (Algebraico)**, sigamos estos pasos lógicos que nunca fallan:

1.  **Igualar a $x$:** Escribimos la ecuación inicial $x = \text{el número}$.
2.  **Convertir a periódico puro:** Multiplicamos por una potencia de $10$ ($10, 100, 1000...$) para mover la coma hasta justo **antes** de donde empieza el periodo.
3.  **Correr el periodo:** Multiplicamos la ecuación anterior por otra potencia de $10$ para pasar **todo un periodo** al lado de los enteros. 
    *   *Ojo:* El número de ceros depende de cuántas cifras tenga el periodo. Si el periodo tiene dos cifras, multiplicamos por $100$.
4.  **Restar y despejar:** A la ecuación del paso 3 le restamos la del paso 2. Esto eliminará la parte decimal infinita. Finalmente, despejamos $x$ y simplificamos.

---

## 4. Ejemplos Desarrollados

```ad-example
title: Ejemplo 1 (Caso Básico)
Convertir $1,1\overline{6}$ a fracción.
1. $x = 1,1666...$
2. Movemos la coma una vez (hay una cifra no periódica): $10x = 11,666...$ (Ec. 2)
3. Movemos el periodo (una cifra): Multiplicamos Ec. 2 por $10 \rightarrow 100x = 116,666...$ (Ec. 3)
4. Restamos:
$$\begin{aligned} 100x &= 116,66... \\ - 10x &= 11,66... \\ \hline 90x &= 105 \end{aligned}$$
5. Despejamos: $x = \frac{105}{90}$. Simplificando entre $15$: **$7/6$**.
```

```ad-example
title: Ejemplo 2 (Con signo negativo)
Convertir $-0,41\overline{6}$ a fracción.
1. Trabajamos con el positivo: $x = 0,4166...$
2. Hay dos cifras no periódicas ($4$ y $1$): $100x = 41,666...$
3. El periodo tiene una cifra ($6$): $1000x = 416,666...$
4. Restamos:
$$\begin{aligned} 1000x &= 416,66... \\ - 100x &= 41,66... \\ \hline 900x &= 375 \end{aligned}$$
5. Despejamos: $x = \frac{375}{900}$. Simplificando (entre $75$): **$5/12$**.
*Resultado final:* Como el original era negativo, la respuesta es **$-5/12$**.
```

```ad-example
title: Ejemplo 3 (Dos cifras no periódicas)
Convertir $0,23\overline{5}$ a fracción.
1. $x = 0,2355...$
2. Movemos la coma 2 lugares: $100x = 23,555...$
3. Corremos el periodo (1 lugar): $1000x = 235,555...$
4. Restamos: $1000x - 100x = 235,5 - 23,5 \rightarrow 900x = 212$.
5. Despejamos: $x = \frac{212}{900} = \frac{106}{450} = \mathbf{\frac{53}{225}}$.
```

```ad-example
title: Ejemplo 4 (Aplicación USD)
Una acción bursátil vale $1,1\overline{6}$ USD. ¿Qué fracción de dólar representa?
*   Como vimos en el Ejemplo 1, el procedimiento nos lleva a la fracción **$7/6$**. ¡Así de fácil!
```

---

## 5. Práctica Dirigida

```ad-abstract
title: Nivel Fácil (Verde)
1. $1,2\overline{3}$
2. $0,5\overline{8}$
3. $2,1\overline{4}$
4. $3,2\overline{6}$
```

```ad-abstract
title: Nivel Medio (Amarillo)
1. $0,12\overline{5}$
2. $1,0\overline{45}$
3. $0,34\overline{1}$
4. $0,1\overline{6}$
```

```ad-abstract
title: Nivel Avanzado (Rojo - Contexto)
1. Si 3 artículos cuestan un total de $4,12\overline{3}$ USD, ¿qué fracción representa este precio?
2. Convierte $0,00\overline{12}$ a fracción.
3. Convierte $-2,7\overline{15}$ a fracción.
4. Una pieza mecánica mide $1,12\overline{7}$ mm, exprésala en fracción.
```

```ad-success
title: Soluciones y Simplificación (Para el Docente)
**Fácil:** 
1) $37/30$ | 2) $53/90$ | 3) $193/90$ | 4) $49/15$

**Medio:** 
1) $113/900$ 
2) $1035/990 \xrightarrow{\div 45} 23/22$ 
3) $307/900$ 
4) $15/90 \xrightarrow{\div 15} 1/6$

**Avanzado:** 
1) $1237/300$ USD
2) $12/9900 \xrightarrow{\div 12} 1/825$
3) $-2688/990 \xrightarrow{\div 6} -448/165$ (Nota: $2715 - 27 = 2688$)
4) $1015/900 \xrightarrow{\div 5} 203/180$ mm
```

---

## 6. Evaluación y Cierre

```ad-question
title: Mini-prueba de salida
1. **Conceptual:** ¿Por qué es necesario multiplicar dos veces por potencias de $10$ en este método?
2. **Procedimental:** Para convertir $0,25\overline{8}$, ¿por qué número multiplicas primero y por qué?
3. **Aplicación:** El precio de la gasolina es $3,5\overline{6}$ USD. ¿Cuál es su fracción exacta?
```

> [!success] Respuestas de la Mini-prueba
> 1. La primera multiplicación convierte el mixto en periódico puro (lleva la coma al periodo); la segunda permite desplazar el periodo para poder restarlo.
> 2. Se multiplica primero por $100$ porque hay dos cifras no periódicas ($25$) antes de que empiece el periodo.
> 3. $321/90 = 107/30$ USD.

**Próximo tema:** ¡Prepárense! Veremos cómo usar estas conversiones para realizar sumas y restas de fracciones con decimales.

> [!info] 🧭 Navegación
> ⬅️ **Clase anterior:** [Clase 18 — Convertir decimal periódico puro a fracción](Clase18)
> 📋 **Índice:** [Curso de Fracciones](IndiceFracciones)