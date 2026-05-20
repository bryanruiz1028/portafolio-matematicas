# Clase 04 — Solución de sistemas 3x3: Método de Gauss-Jordan
`#algebra #solutionofxsyst`

[[Clase 03]] | [[Indice_Algebra]] | [[Clase 05]]

---

## ¿Por qué es importante esta clase?
> [!info] 🌍 Relevancia y aplicaciones
> El método de Gauss-Jordan es la piedra angular del álgebra lineal moderna, ya que permite sistematizar y automatizar la resolución de múltiples variables simultáneamente mediante operaciones elementales de fila.
> 
> - 💵 **Finanzas:** Cálculo preciso de presupuestos en `$ USD $` al adquirir tres categorías de insumos con precios variables.
> - 🏗️ **Ingeniería:** Análisis de estabilidad estructural mediante el equilibrio de fuerzas vectoriales en los tres ejes cartesianos ($x, y, z$).
> - 📊 **Logística:** Optimización de inventarios y flujos de distribución en escenarios de la vida cotidiana.

---

## Concepto clave
> [!note] El Método en palabras simples
> Imagina que tienes un rompecabezas numérico desordenado. El objetivo de Gauss-Jordan es transformar la matriz original en una **matriz identidad**. Esto significa que, tras aplicar nuestras reglas, el lado izquierdo de la matriz mostrará una diagonal de números $1$ y el resto de los espacios serán ceros. Cuando logras esto, los valores en la columna derecha son las soluciones directas del sistema.

> [!warning] ⚠️ Error común: El desorden de variables
> Como catedrático, insisto: un sistema solo puede resolverse si está perfectamente alineado. Todas las ecuaciones deben seguir la estructura: $Ax + By + Cz = D$. Mezclar la posición de las columnas (por ejemplo, colocar una $y$ en el lugar de las $x$) invalidará todo el proceso de reducción.

> [!tip] 💡 Truco para recordarlo
> Visualiza el método como "limpiar una escalera". Primero, trabajamos hacia abajo para hacer ceros en los escalones inferiores (debajo de la diagonal). Luego, "limpiamos" hacia arriba para hacer ceros en los escalones superiores. Al final, solo dividimos para que la barandilla sea una línea perfecta de unos.

---

## Procedimiento paso a paso
Para resolver un sistema $3 \times 3$ mediante el canon de Gauss-Jordan, seguimos esta ruta algorítmica:

```text
1. ORGANIZACIÓN: Alinea las variables ($x, y, z = TI$) y construye la matriz aumentada.
2. FASE INFERIOR (Eliminación): Convierte en ceros los elementos debajo de la diagonal 
   principal usando la fila de referencia (F1 para la Columna 1, F2 para la Columna 2).
3. FASE SUPERIOR (Eliminación): Convierte en ceros los elementos por encima de la 
   diagonal principal utilizando la fila de referencia (F3 para Columna 3, F2 para Columna 2).
4. NORMALIZACIÓN (Escalamiento): Divide cada fila por su coeficiente principal 
   (el valor en la diagonal) para obtener la matriz identidad con 1s finales.
```

---

## Ejemplos de aplicación

> [!example] ad-example Ejemplo 1: Caso Básico (Video 1)
> **Sistema inicial:**
> $x - y + 3z = 13$
> $x + y + z = 11$
> $2x + 2y - z = 7$
> 
> **Representación en Matriz Aumentada:**
> $\begin{pmatrix} 1 & -1 & 3 & | & 13 \\ 1 & 1 & 1 & | & 11 \\ 2 & 2 & -1 & | & 7 \end{pmatrix}$
> 
> **Paso 1: Generar ceros en la primera columna.**
> Aplicamos las operaciones elementales:
> - $F_2 \leftarrow F_2 - F_1$ (Resultado: $[0, 2, -2, | -2]$)
> - $F_3 \leftarrow F_3 - 2F_1$ (Resultado: $[0, 4, -7, | -19]$)
> 
> Tras continuar con la limpieza de la columna 2 y 3, y normalizar los coeficientes:
> ✅ **Resultado:** $x = 2, y = 4, z = 5$.

> [!example] ad-example Ejemplo 2: Caso con Signos y Fracciones (Video 2)
> **Sistema:**
> $2x + 3y + 4z = 3$
> $2x + 6y + 8z = 5$
> $4x + 9y - 4z = 4$
> 
> **Nota técnica:** Durante el proceso, se obtienen escalares que requieren una división final. Al normalizar las filas dividiendo por sus términos en la diagonal principal, las soluciones resultan en fracciones exactas:
> ✅ **Resultado:** $x = 1/2, y = 1/3, z = 1/4$.

> [!example] ad-example Ejemplo 3: Caso Avanzado - Técnica del MCM (Video 3)
> Cuando el sistema presenta coeficientes fraccionarios, la estrategia académica óptima es convertirlos a enteros mediante el **Mínimo Común Múltiplo (MCM)** antes de montar la matriz.
> 
> **Sistema original:**
> 1) $\frac{x}{3} + \frac{y}{4} + \frac{z}{3} = 21$
> 2) $\frac{x}{5} + \frac{y}{6} - \frac{z}{3} = 0$
> 3) $\frac{x}{10} + \frac{y}{3} + \frac{z}{6} = 11$
> 
> **Transformación:**
> - Ec. 1: Multiplicamos por $12 \rightarrow 4x + 3y + 4z = 252$
> - Ec. 2: Multiplicamos por $30 \rightarrow 6x + 5y - 10z = 0$
> - Ec. 3: Multiplicamos por $30 \rightarrow 3x + 10y + 5z = 330$
> 
> ✅ **Sistema resultante:** Ahora procesamos la matriz con números enteros, facilitando el cálculo de Gauss-Jordan.

> [!example] ad-example Ejemplo 4: Aplicación Real en $ USD $
> **Enunciado:** Un cliente compra 3 productos ($A, B, C$). Si los precios por unidad ($x, y, z$) satisfacen las relaciones matemáticas del Ejemplo 1:
> - ¿Cuál es el valor comercial de cada artículo?
> ✅ **Solución:** Aplicando la resolución del sistema: El Producto A cuesta **$ 2 USD $,** el Producto B cuesta **$ 4 USD $** y el Producto C cuesta **$ 5 USD $.**

---

## Ejercicios para el estudiante

> [!abstract] ad-abstract 🟢 Nivel Fácil
> Resuelva mediante reducción de Gauss-Jordan el siguiente sistema:
> $x + y + z = -6$
> $2x + y - z = -1$
> $x - 2y + 3z = -6$

> [!abstract] ad-abstract 🟡 Nivel Medio
> Resuelva (¡Precaución! Primero debe reordenar los términos en cada ecuación):
> $4x - y + z = 4$
> $z + y - 2x = 2$
> $6x - 2y + 3z = 2$

> [!abstract] ad-abstract 🔴 Nivel Avanzado
> Utilice la técnica del MCM para transformar este sistema a coeficientes enteros y determine los valores finales:
> $\frac{x}{3} + \frac{y}{4} + \frac{z}{3} = 21$
> $\frac{x}{5} + \frac{y}{6} - \frac{z}{3} = 0$
> $\frac{x}{10} + \frac{y}{3} + \frac{z}{6} = 11$

> [!check] Respuestas de verificación
> - **Fácil:** $x = -1, y = -2, z = -3$.
> - **Medio:** $x = 1/2, y = 3, z = 5$.
> - **Avanzado:** $x = 30, y = 12, z = 24$.

---

## Mini-prueba de autoevaluación

> [!question] ad-question Pregunta 1: Conceptual
> Al finalizar el método de Gauss-Jordan, ¿qué estructura se debe haber formado en la parte izquierda de la matriz aumentada?
> - A) Una matriz nula.
> - B) Una matriz identidad (diagonal de 1s, resto 0s).
> - C) Una matriz triangular inferior.
> 
> *Respuesta: B*

> [!question] ad-question Pregunta 2: Procedimental
> Si durante la reducción obtienes una fila con los valores $[0, 6, 0 | 24]$, ¿cuál es la operación de escalonamiento necesaria para que el coeficiente de $y$ sea 1?
> - A) Multiplicar la fila por $24$.
> - B) Dividir la fila entre $6$.
> - C) Sumar $-6$ a toda la fila.
> 
> *Respuesta: B*

> [!question] ad-question Pregunta 3: Aplicación $ USD $
> En un problema donde 2 kilos de manzanas ($x$), 1 de peras ($y$) y 3 de uvas ($z$) cuestan $15 USD, ¿cuál es la representación correcta de la primera fila de la matriz?
> - A) $[1, 2, 3 | 15]$
> - B) $[2, 1, 3 | 15]$
> - C) $[2x, 1y, 3z | 15]$
> 
> *Respuesta: B*

---

## Notas para el próximo tema

> [!tip] 💡 En la próxima clase
> Estimados alumnos, con esta sesión cerramos oficialmente el **Bloque 1** sobre resolución de sistemas de ecuaciones. En nuestro próximo encuentro realizaremos la evaluación final del módulo para consolidar su dominio sobre el método de Gauss-Jordan.

[[Clase 03]] | [[Indice_Algebra]] | [[Finalizar_Curso]]