# 📖 Guía de estudio — Clase 04: Permutaciones lineales

> [!info] 📌 Conceptos clave
> La permutación lineal es una técnica de conteo fundamental para organizar elementos en una secuencia. Sus pilares pedagógicos son:
> - **Importancia del orden:** Si se cambia la posición de un solo elemento, el arreglo resultante es totalmente distinto.
> - **Uso de todos los elementos:** Se utilizan los $n$ elementos disponibles del conjunto ($n = r$).
> - **Disposición lineal:** El arreglo se realiza en línea recta (no circular ni en agrupaciones complejas).
> - **Elementos distintos:** En su forma simple, no existen elementos repetidos dentro del conjunto.

---

## FÓRMULAS Y DEFINICIONES IMPORTANTES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Permutación Lineal** | Un arreglo ordenado de $n$ elementos donde la posición de cada uno define un resultado único. |
| **Factorial ($n!$)** | Producto decreciente de todos los números enteros positivos desde $n$ hasta $1$. <br>Ejemplo: $7! = 7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1 = 5040$. |
| **Fórmula General** | $P_n = n!$ |
| **Método de las cajitas** | Herramienta visual basada en el principio multiplicativo. Cada "cajita" representa una posición y el número dentro indica las opciones disponibles. |

> [!important] 💡 Nota Pro: ¿Permutación o Variación?
> Si el problema te pide usar **todos** los elementos disponibles ($n = r$), estamos ante una **Permutación**. Si solo necesitas elegir y ordenar **algunos** elementos del total ($n > r$), se trata de una **Variación**.

---

## EJEMPLOS RESUELTOS ADICIONALES

```ad-example
**Ejemplo A — Permutación de letras**
**Enunciado:** ¿Cuántas palabras distintas (con o sin sentido) se pueden formar con las letras de la palabra "GATO"?

**Solución paso a paso:**
1. **Identificar $n$:** La palabra tiene $4$ letras distintas ($G, A, T, O$), por lo tanto $n = 4$.
2. **Representación visual (Método de las cajitas):**
   `[ 4 ] [ 3 ] [ 2 ] [ 1 ]`
   *(4 opciones para la 1ra letra, 3 para la 2da, etc.)*
3. **Aplicar fórmula:** $P_4 = 4!$
4. **Cálculo:** $4 \times 3 \times 2 \times 1 = 24$.
**Resultado:** Se pueden formar $24$ palabras.
```

```ad-example
**Ejemplo B — Asientos de cine y costo de entrada**
**Enunciado:** Una familia de $5$ personas ($2$ padres y $3$ hijos) va al cine. Si cada entrada cuesta $10\text{ USD}$, ¿de cuántas formas pueden sentarse en $5$ butacas consecutivas si los padres deben ocupar los extremos?

**Solución paso a paso:**
1. **Visualizar restricciones (Cajitas):**
   `[ P ] [ H ] [ H ] [ H ] [ P ]`
2. **Permutar Padres (Extremos):** Hay $2$ padres para $2$ posiciones. 
   `[ 2 ] [   ] [   ] [   ] [ 1 ]` $\rightarrow$ $2! = 2$ formas.
3. **Permutar Hijos (Centro):** Quedan $3$ hijos para $3$ asientos.
   `[   ] [ 3 ] [ 2 ] [ 1 ] [   ]` $\rightarrow$ $3! = 6$ formas.
4. **Cálculo Total:** $2 \times 6 = 12$ formas.
5. **Análisis Económico:** Aunque existen $12$ formas de sentarse, el costo total es una suma escalar fija: $5 \text{ personas} \times 10\text{ USD} = 50\text{ USD}$. El orden afecta la ubicación (variable de permutación), pero no altera el costo total (variable aritmética).
```

---

## EJERCICIOS DE REPASO

```ad-abstract
**🟢 Nivel: Fácil**
1. Calcula el total de permutaciones posibles con las letras de la palabra "PARTIDO" ($n = 7$).
2. ¿Cuántas palabras de $4$ letras se pueden formar con los elementos de la palabra "GATO"?
```

```ad-abstract
**🟡 Nivel: Medio**
1. Con la palabra "PARTIDO":
   - ¿Cuántas palabras inician con la letra 'T'?
   - ¿Cuántas palabras inician exactamente con la secuencia "PAR"?
2. Con la palabra "GATO": ¿Cuántas inician en 'G' y terminan en 'O'?
3. Seis amigos ($3$ hombres y $3$ mujeres) se forman en fila. ¿De cuántas formas pueden hacerlo si no hay restricciones?
```

```ad-abstract
**🔴 Nivel: Avanzado (Aplicación con $USD)**
**Enunciado:** $4$ parejas de novios van a un concierto. El costo por pareja en zona VIP es de $500\text{ USD}$ (Inversión total: $2000\text{ USD}$). Para mayor comodidad, cada pareja debe sentarse junta, funcionando como un "bloque".
1. **Permutación de bloques:** ¿De cuántas formas se pueden organizar los $4$ bloques de parejas? (Calcula $4!$).
2. **Permutación interna:** ¿De cuántas formas puede sentarse cada pareja individualmente? (Considera que cada una de las $4$ parejas tiene $2!$ opciones: $2 \times 2 \times 2 \times 2$).
3. **Total:** Multiplica la permutación de bloques por todas las permutaciones internas individuales ($4! \times 2^4$).
*(Dato de verificación: El resultado final es $384$ formas).*
```

---

> [!tip] 💡 Consejo de estudio
> El **Método de las cajitas** es tu mejor aliado cuando el problema impone condiciones. Antes de usar la fórmula $n!$, dibuja los espacios y "bloquea" las posiciones fijas. Por ejemplo, si una letra debe ir al final, coloca un $[ 1 ]$ en la última casilla y luego permuta el resto de los elementos en los espacios sobrantes. Esto evita errores comunes al contabilizar opciones disponibles.