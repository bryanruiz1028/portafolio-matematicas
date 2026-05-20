# Clase 11 — Función compuesta
tags: #algebra #funcincompuesta
Curso: [[00 - Índice del curso]] | Bloque 3 | Lección 11 de 12

## 1. NAVEGACIÓN
[[Clase 10 — Operaciones con funciones | ← Clase 10]] | [[00 - Índice del curso | Índice]] | [[Clase 12 — Dominios de funciones compuestas | Clase 12 →]]

## 2. RELEVANCIA Y APLICACIONES
> [!info] 🌍 Relevancia y aplicaciones
> ¡Qué tal, amigas y amigos! Imaginen que la función compuesta es como una línea de producción en una fábrica de bolsos. No todo se hace al mismo tiempo: una máquina realiza un proceso inicial (como fabricar la base) y **el resultado** de esa máquina se convierte en el **alimento** de la siguiente, que se encarga de poner las correas. ¡El producto de una es el insumo de la otra!
> 
> * 💵 **$USD**: Si quieres saber cuántos dólares recibirás, primero usas una función para convertir tus pesos a una moneda intermedia (como el Euro) y luego otra función toma ese resultado para convertirlo finalmente a dólares.
> * 🏗️ **Práctica**: Representa cualquier proceso secuencial donde la materia prima sufre transformaciones por etapas.
> * 📊 **Cotidiana**: Cuando vas a una tienda y aplicas un cupón de descuento y, sobre ese nuevo precio, se calcula el impuesto final. ¡Son dos funciones trabajando en cadena!

## 3. CONCEPTO CLAVE
> [!note] 📌 ¿Qué es Función compuesta?
> Es, básicamente, **"meter una función dentro de otra"**. Si tenemos dos máquinas, $f$ y $g$, la composición significa que lo que sale de la primera máquina es lo que le damos de comer a la segunda. En notación, $(g \circ f)(x)$ significa que a la $x$ primero le aplicamos la función $f$ y a ese resultado le aplicamos la función $g$.

> [!warning] ⚠️ Error común
> ¡Mucho cuidado! La composición de funciones **no es conmutativa**. Esto quiere decir que $f(g(x))$ casi nunca será igual a $g(f(x))$. Cambiar el orden de las máquinas cambia el producto final. Como dice el Profe Alex: "No es lo mismo ponerse los calcetines y luego los zapatos, que los zapatos y luego los calcetines".

> [!tip] 💡 Truco para recordarlo
> Aunque leemos de izquierda a derecha, la matemática ocurre de **derecha a izquierda** (de adentro hacia afuera). En la expresión $(f \circ g)(x)$, la función de la **derecha** ($g$) es la que se mete dentro de la de la **izquierda** ($f$). ¡$g$ es el alimento de $f$!

## 4. PROCEDIMIENTO PASO A PASO
Para realizar la composición sin equivocarte, sigue esta receta infalible del Profe Alex:

```text
PASO 1 → Escribir la notación de paréntesis: f(g(x)).
PASO 2 → Reemplazar la función interna por su expresión algebraica.
PASO 3 → Preparar la función externa usando paréntesis vacíos donde estaba la x.
PASO 4 → Realizar las operaciones algebraicas (distributiva o binomios) para simplificar.
```

> [!abstract] **Pro-Tip del Profe Alex**
> En el **Paso 3**, el secreto para no cometer errores de signos (especialmente en potencias) es usar **paréntesis vacíos** `( )`. No intentes sustituir mentalmente; escribe el hueco y luego rellénalo.

## 5. EJEMPLOS DESARROLLADOS

> [!example] Ejemplo 1: Nivel Básico (Lineal)
> Dadas las funciones $f(x) = 2x + 1$ y $g(x) = 4x - 2$. Vamos a alimentar a $f$ con el resultado de $g$, es decir, hallar $f(g(x))$:
> 1. Escribimos la forma: $f(g(x))$.
> 2. Reemplazamos la función interna $g(x)$: $f(4x - 2)$.
> 3. **Preparamos $f$ con paréntesis vacíos**: $2( \quad ) + 1$.
> 4. Rellenamos el hueco: $2(4x - 2) + 1$.
> 5. Aplicamos distributiva y simplificamos: $8x - 4 + 1 = \mathbf{8x - 3}$.

> [!example] Ejemplo 2: Práctica de Signos
> Dadas $f(x) = x - 3$ y $g(x) = 5x + 2$. Vamos a darle de comer $f$ a la máquina $g$, hallando $g(f(x))$:
> 1. Notación: $g(f(x))$.
> 2. Reemplazamos la interna $f(x)$: $g(x - 3)$.
> 3. Preparamos la externa $g$: $5( \quad ) + 2$.
> 4. Introducimos la expresión: $5(x - 3) + 2$.
> 5. Operamos: $5x - 15 + 2 = \mathbf{5x - 13}$.

> [!example] Ejemplo 3: Nivel Avanzado (Cuadrático)
> Dadas $f(x) = x^2 + 2x - 1$ y $g(x) = 3x + 4$. Calculemos $f(g(x))$ con mucho cuidado:
> 1. Forma: $f(g(x)) = f(3x + 4)$.
> 2. Preparamos $f$ con sus espacios: $( \quad )^2 + 2( \quad ) - 1$.
> 3. Sustituimos: $(3x + 4)^2 + 2(3x + 4) - 1$.
> 4. **Desarrollo paso a paso**:
>    * Primero el binomio $(a+b)^2$: $(3x)^2 + 2(3x)(4) + 4^2 = 9x^2 + 24x + 16$.
>    * Luego la distributiva del segundo término: $2(3x + 4) = 6x + 8$.
>    * Juntamos todo: $9x^2 + 24x + 16 + 6x + 8 - 1$.
> 5. Reducimos términos semejantes: $\mathbf{9x^2 + 30x + 23}$.

> [!example] Ejemplo 4: Aplicación en cadena ($USD)
> Queremos convertir pesos ($x$) a dólares pasando por una moneda intermedia.
> * Función $g(x) = \frac{x}{20}$ (Convierte Pesos a Euros).
> * Función $f(x) = 1.10x$ (Convierte Euros a Dólares, considerando el tipo de cambio).
> 
> La función compuesta $f(g(x))$ nos da el valor final en dólares:
> 1. $f(g(x)) = f\left(\frac{x}{20}\right)$.
> 2. Aplicamos la regla de $f$: $1.10\left(\frac{x}{20}\right)$.
> 3. Simplificamos: $0.055x$. 
> *Si ingresas $2000$ pesos: $0.055(2000) = \mathbf{110}$ **USD finales**.*

## 6. EJERCICIOS PARA EL ESTUDIANTE

Utiliza estas funciones para resolver los retos:
* $f(x) = 2x + 1$
* $g(x) = 4x - 2$
* $h(x) = x^2 + 2x - 1$

**Nivel Verde (Fácil)**
1. Hallar $g(f(x))$.
2. Hallar $f(f(x))$.

**Nivel Amarillo (Intermedio)**
3. Hallar $g(g(x))$.
4. Hallar $g(h(x))$.

**Nivel Rojo (Desafío)**
5. Un producto cuesta $x$ pesos. Primero se le aplica un descuento del $10\%$, definido por $d(x) = 0.90x$. Luego, el resultado se convierte a dólares con $c(x) = \frac{x}{20}$. ¿Cuál es la función compuesta $c(d(x))$ que determina el precio final en $USD$?

> [!success] ✅ Respuestas
> 1. $8x + 2$
> 2. $4x + 3$
> 3. $16x - 10$
> 4. $4x^2 + 8x - 6$
> 5. $0.045x$ o $\frac{9x}{200}$

## 7. MINI-PRUEBA DE AUTOEVALUACIÓN
**1. ¿Qué indica realmente la notación $g(f(x))$?**
a) Una multiplicación entre $g$ y $f$.
b) Que la función $f$ actúa como el alimento (entrada) de la función $g$.
c) Que $g$ se resuelve primero y luego $f$.
d) Que $g$ y $f$ son funciones inversas.

**2. Si $f(x) = x + 5$ y $g(x) = 2x$, ¿cuál es el valor de $f(g(3))$?**
a) $16$
b) $11$
c) $13$
d) $21$

**3. ¿Por qué es vital el orden en la composición?**
a) Porque siempre da el mismo resultado, pero es más ordenado.
b) Porque la composición no es conmutativa; el proceso de la primera afecta lo que recibe la segunda.
c) Porque las funciones cuadráticas no aceptan funciones lineales.
d) Porque lo dice el libro de texto.

> [!check] Soluciones de la Prueba
> 1. **b** (Entrada de la función).
> 2. **b** ($g(3)=6$, luego $f(6)=6+5=11$).
> 3. **b** (La no-conmutatividad es clave).

## 8. CIERRE Y PRÓXIMO TEMA
> [!tip] 💡 En la próxima clase
> Ya sabes cómo "armar la máquina". Ahora nos toca preguntarnos: ¿qué pasa si el alimento que sale de la primera máquina le cae mal a la segunda? En la siguiente lección veremos el **Análisis de dominios en funciones compuestas**. ¡No te lo pierdas!

[[Clase 10 — Operaciones con funciones | ← Clase 10]] | [[00 - Índice del curso | Índice]] | [[Clase 12 — Dominios de funciones compuestas | Clase 12 →]]