# 📖 Guía de estudio — Clase 03: Solución de Sistemas de Ecuaciones 3x3

¡Hola! Soy tu docente de matemáticas y hoy vamos a conquistar los sistemas de ecuaciones $3 \times 3$. Aunque ver tantas variables juntas como $x, y, z$ puede asustar un poco, te aseguro que si seguimos un orden riguroso y cuidamos los signos, resolverlos se vuelve un proceso lógico y muy gratificante. ¡Confía en tu capacidad y vamos paso a paso!

> [!info] 📌 Conceptos clave
> 1.  **Orden absoluto:** Antes de operar, las ecuaciones deben estar en formato $ax + by + cz = d$ (las variables en orden alfabético a la izquierda y el término independiente a la derecha).
> 2.  **Método de Cramer (Determinantes):** Utiliza matrices y el cálculo de determinantes ($\Delta$) para hallar los valores mediante divisiones. Es ideal cuando buscamos precisión numérica.
> 3.  **Método de Gauss (Triangularización):** Es el arte de simplificar. Transformamos el sistema en una "matriz triangular superior" (creando ceros debajo de la diagonal) para despejar las variables desde abajo hacia arriba.
> 4.  **Verificación final:** La única forma de estar 100% seguros es sustituir los valores hallados en las ecuaciones originales. Si la igualdad se cumple, ¡tu trabajo es perfecto!

---

### 2. Fórmulas y definiciones importantes

Para dominar este tema, debemos hablar el mismo lenguaje matemático:

| Término | Definición / Fórmula |
| :--- | :--- |
| **Sistema 3x3** | Un conjunto de 3 ecuaciones lineales con 3 incógnitas ($x, y, z$). |
| **Determinante del Sistema ($\Delta s$)** | Valor numérico calculado usando solo los coeficientes que acompañan a $x, y, z$. |
| **Regla de Sarrus** | Método para resolver determinantes de $3 \times 3$ duplicando las dos primeras filas (o columnas) para multiplicar en diagonal. |
| **Matriz Triangular Superior** | Una matriz donde todos los elementos debajo de la diagonal principal son cero ($0$). Es el objetivo del Método de Gauss. |

---

### 3. Ejemplos resueltos adicionales

Analicemos dos ejemplos detallados basados en la metodología del "Profe Alex".

```ad-example
**Ejemplo A — Caso básico (Método de Cramer)**

**Sistema:**
1) $1x + 4y + 5z = 11$
2) $3x - 2y + 1z = 5$
3) $4x + 1y - 3z = -26$

**Paso 1: Hallar el Determinante del Sistema ($\Delta s$)**
Duplicamos las primeras dos filas y multiplicamos:
- **Diagonales Principales:**
  - $(1 \cdot -2 \cdot -3) = 6$
  - $(3 \cdot 1 \cdot 5) = 15$
  - $(4 \cdot 4 \cdot 1) = 16$
  - **Suma:** $6 + 15 + 16 = 37$
- **Diagonales Secundarias:**
  - $(5 \cdot -2 \cdot 4) = -40$
  - $(1 \cdot 1 \cdot 1) = 1$
  - $(-3 \cdot 4 \cdot 3) = -36$
  - **Suma:** $-40 + 1 - 36 = -75$

**Resultado:** $\Delta s = 37 - (-75) = 112$.

**Paso 2: Hallar el Determinante de $x$ ($\Delta x$)**
Cambiamos la columna de $x$ por los resultados ($11, 5, -26$). Tras aplicar el mismo proceso de Sarrus:
**$\Delta x = -224$**.

**Paso 3: Resultado final para $x$**
$x = \frac{\Delta x}{\Delta s} = \frac{-224}{112} = -2$.

> [!warning] **¡Cuidado con los signos!**
> El error más común ocurre al restar la suma de las diagonales secundarias. Recuerda: es `(Suma Principal) - (Suma Secundaria)`. Si la secundaria es negativa, se vuelve una suma: $37 - (-75) = 112$.
```

```ad-example
**Ejemplo B — Aplicación con compras (Método de Gauss)**

**Enunciado:** Compras útiles en tres días:
- Día 1: 1 cuaderno ($x$), 2 carpetas ($y$) y 1 resaltador ($z$) por **$7**.
- Día 2: 3 cuadernos, 1 carpeta y 1 resaltador por **$5**.
- Día 3: 2 cuadernos, 3 carpetas y una devolución de 1 resaltador por **$3$.**

**Sistema:**
1) $x + 2y + z = 7$
2) $3x + y + z = 5$
3) $2x + 3y - z = 3$

**Procedimiento de Gauss:**
1. **Crear Matriz Ampliada:**
   $\begin{pmatrix} 1 & 2 & 1 & | & 7 \\ 3 & 1 & 1 & | & 5 \\ 2 & 3 & -1 & | & 3 \end{pmatrix}$
2. **Eliminar $x$ en la Fila 2 ($F2$):** Hacemos $(-3 \cdot F1) + F2$.
   - Multiplicamos $F1$ por $-3$: $[-3, -6, -3, -21]$.
   - **¡Ojo de profesor!** No olvides multiplicar también el término independiente ($7 \cdot -3 = -21$).
   - Sumamos a $F2$: $[-3+3, -6+1, -3+1, -21+5] = [0, -5, -2, -16]$.
3. **Eliminar $x$ en la Fila 3 ($F3$):** Hacemos $(-2 \cdot F1) + F3$.
   - Resultado: $[0, -1, -3, -11]$.
4. **Resultado de la Triangularización:** Tras eliminar la $y$ en $F3$ usando la nueva $F2$, obtendrás los valores: **$z = 3, y = 2, x = 0$**.
```

---

### 4. Ejercicios de repaso

```ad-abstract
Resuelve con calma y orden. Aquí tienes los niveles de desafío:

**🟢 Nivel Fácil (Cramer Directo)**
1.  
    $x + y + z = 6$  
    $x - y + z = 2$  
    $2x + y - z = 1$
2.  
    $x + y - z = -3$  
    $2x - y + z = 9$  
    $x + 2y + 2z = 0$

**🟡 Nivel Medio (Requiere Ordenar)**
Lleva los términos independientes al lado derecho antes de empezar:
- $x + y = 5 - z$
- $2x = z - y + 4$
- $x + z = 11 - 2y$

**🔴 Nivel Avanzado (Problema Real - Gauss)**
**En la cafetería:**
- Combo A: 2 sándwiches, 1 jugo y 1 postre cuestan **$13**.
- Combo B: 1 sándwich, 2 jugos y 1 postre cuestan **$12**.
- Combo C: 1 sándwich, 1 jugo y 2 postres cuestan **$11**.
**Tarea:** Plantea el sistema $3 \times 3$ y resuelve por Gauss.

---
**Clave de respuestas (Verifica tu trabajo):**
*Fácil 1: $(1, 2, 3)$ | Fácil 2: $(2, -1, 4)$*
*Medio: $(2, 3, 0)$*
*Avanzado: Sándwich=$4, Jugo=$3, Postre=$2*
```

---

> [!tip] 💡 Consejo de estudio
> Una pista de oro que nos da el Profe Alex: en los ejercicios de examen, los determinantes de las incógnitas ($\Delta x, \Delta y, \Delta z$) casi siempre son múltiplos exactos del determinante del sistema ($\Delta s$). Si obtienes una fracción extremadamente extraña, ¡detente! Revisa tus multiplicaciones diagonales. Además, comprueba siempre tu resultado en la **tercera ecuación**; si ahí funciona, es muy probable que todo tu sistema sea correcto.