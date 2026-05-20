# Clase 05 — División de Polinomios
#algebra #polynomialdivis
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 5 de 7

> [!info] 🧭 Navegación
> [[Clase 04|⬅ Clase 04]] | [[00 - Índice del curso|Índice]] | **Clase 05** | | [[Clase 06|Clase 06 ➡]]

> [!info] 🌍 Relevancia y aplicaciones
> La división de polinomios es un proceso fundamental que funciona de forma análoga a la división de números naturales que aprendemos en aritmética básica. Como experto, les aseguro que dominar este algoritmo es el puente hacia el cálculo avanzado. Es importante reconocer que esta operación puede presentarse en tres notaciones: como fracción ($\frac{A}{B}$), con el signo de división ($A \div B$) o mediante la galera o "casita" de división larga.
> 
> Sus aplicaciones prácticas incluyen:
> - 💵 **Cálculo de costos promedio unitarios:** Fundamental para determinar el punto de equilibrio en finanzas al dividir funciones de costo total entre producción.
> - 🏗️ **Distribución de cargas en ingeniería:** Permite modelar cómo se reparten las fuerzas mecánicas en estructuras con variables algebraicas.
> - 📊 **Modelado de inventarios:** Útil para proyectar variaciones de flujo de mercancías en sistemas de optimización comercial.

> [!note] 📌 ¿Qué es la División de Polinomios?
> Es el proceso de repartir una expresión algebraica llamada **Dividendo** entre otra denominada **Divisor**. El objetivo es obtener un **Cociente** (resultado) y, en ocasiones, un **Residuo**. Al igual que en la aritmética, se basa en las leyes de los signos y de los exponentes, siguiendo un orden jerárquico estricto de potencias.

> [!warning] ⚠️ Error crítico: El cambio de signo
> El error número uno —y la causa principal de fallos en exámenes— es olvidar cambiar el signo de los términos resultantes de la multiplicación antes de restarlos al dividendo. 
> - ❌ **Incorrecto:** Sumar directamente el producto obtenido.
> - ✅ **Correcto:** Cambiar **siempre** el signo de cada término resultante de la multiplicación. Si el producto es positivo, se escribe negativo; si es negativo, se escribe positivo.

> [!tip] 💡 Truco para recordarlo
> Memoriza la secuencia maestra del profesor: **"Multiplica, Cambia (signo) y Combina"**.

---

### Procedimiento Paso a Paso

```text
PASO 1 → ORDENAR: Acomodar dividendo y divisor de mayor a menor exponente.
         Si faltan potencias intermedias, es OBLIGATORIO dejar el espacio 
         o escribir 0 seguido del término faltante para mantener la columna.
PASO 2 → BUSCAR TÉRMINO: Dividir el primer término del dividendo entre el 
         primer término del divisor para hallar el primer término del cociente.
PASO 3 → MULTIPLICAR: Multiplicar el término hallado por TODO el divisor.
PASO 4 → RESTAR (CAMBIO DE SIGNO): Escribir los resultados debajo del 
         dividendo con sus signos OPUESTOS y realizar la suma algebraica.
PASO 5 → REPETIR: Bajar el siguiente término y repetir el ciclo hasta que 
         no queden más términos por bajar o el grado del residuo sea menor.
```

> [!abstract] 👨‍🏫 Nota del Profesor
> Si al realizar la resta el primer término no se elimina (no da cero), detente de inmediato: has cometido un error en la elección del término del cociente o en el cambio de signo.

---

### Ejemplos Prácticos

> [!example] Ejemplo 1: Nivel Básico (Proceso Aritmético-Algebraico)
> **Problema:** Dividir $3x^2 + 2x - 8$ entre $x + 2$.
> 
> 1. **Primer término:** $3x^2 \div x = 3x$.
> 2. **Multiplicación y resta:**
>    - $3x \cdot x = 3x^2 \rightarrow$ escribimos $-3x^2$.
>    - $3x \cdot 2 = 6x \rightarrow$ escribimos $-6x$.
> 3. **Operación:** $(3x^2 + 2x) - (3x^2 + 6x) = -4x$.
> 4. **Bajar siguiente:** $-4x - 8$.
> 5. **Repetición:** $-4x \div x = -4$.
>    - $-4 \cdot x = -4x \rightarrow$ escribimos $+4x$.
>    - $-4 \cdot 2 = -8 \rightarrow$ escribimos $+8$.
> 
> **Resultado final:** Cociente $3x - 4$ con Residuo $0$.

> [!example] Ejemplo 2: Manejo de Signos y Espacios (Visualización de Columnas)
> **Problema:** Dividir $-a^5 - 3a^2 - a + 1$ entre $a^2 + 2a + 1$.
> 
> Para no perder el orden, representamos el dividendo con sus "huecos" para $a^4$ y $a^3$:
> $$-a^5 + 0a^4 + 0a^3 - 3a^2 - a + 1$$
> 
> 1. Al multiplicar el primer término del cociente ($-a^3$) por el divisor:
>    - $(-a^3) \cdot (a^2 + 2a + 1) = -a^5 - 2a^4 - a^3$.
>    - Al colocarlo bajo el dividendo, **cambiamos signos**: $+a^5 + 2a^4 + a^3$.
> 2. Los términos $+2a^4$ y $+a^3$ ocupan ahora los espacios que estaban vacíos, permitiendo continuar la operación con orden.
> 
> **Resultado:** $-a^3 + 2a^2 - 3a + 1$.

> [!example] Ejemplo 3: Exponentes Literales (Avanzado)
> **Problema:** Dividir $a^{2x} + 2a^{2x-1} - 4a^{2x-2} + 5a^{2x-3} - 2a^{2x-4}$ entre $a^x - a^{x-1} + a^{x-2}$.
> 
> **Fundamento Técnico:** Aplicamos la **Ley de los exponentes para el producto**: $a^m \cdot a^n = a^{m+n}$. Para ordenar, usamos la lógica de los números enteros: $2x$ es mayor que $2x-1$.
> 
> 1. **Primer término:** $a^{2x} \div a^x = a^x$ (porque $x + x = 2x$).
> 2. **Multiplicación y resta:**
>    - $a^x \cdot (-a^{x-1}) = -a^{2x-1} \rightarrow$ se registra como $+a^{2x-1}$.
>    - $a^x \cdot (a^{x-2}) = a^{2x-2} \rightarrow$ se registra como $-a^{2x-2}$.
> 3. Al sumar $2a^{2x-1} + a^{2x-1}$ obtenemos $3a^{2x-1}$, y el proceso se repite sumando/restando los exponentes variables.
> 
> **Resultado:** $a^x + 3a^{x-1} - 2a^{x-2}$.

> [!example] Ejemplo 4: Aplicación en Finanzas (USD)
> Una empresa tiene una ganancia total representada por $2x^2 + 5x - 3$ dólares. Si se reparte entre $x + 3$ productos vendidos, ¿cuál es el precio de ganancia unitario?
> 
> **Operación:** $(2x^2 + 5x - 3) \div (x + 3)$
> 1. $2x^2 \div x = 2x$.
> 2. $2x(x + 3) = 2x^2 + 6x$. Al restar: $-2x^2 - 6x$.
> 3. El residuo parcial es $-x - 3$.
> 4. $-x \div x = -1$.
> 5. $-1(x + 3) = -x - 3$. Al restar: $+x + 3$. Residuo: $0$.
> 
> **Resultado:** El precio unitario es **$2x - 1$ USD**.

---

### Ejercicios para el Estudiante

**🟢 Nivel Fácil**
1. Divide $2x^2 - 15x + 25$ entre $x - 5$.
2. Divide $x^2 + 7x + 10$ entre $x + 2$.

**🟡 Nivel Medio**
3. Divide $x^4 - 1$ entre $x - 1$. (Pista: Usa placeholders para $x^3, x^2$ y $x$).
4. Divide $a^3 + 1$ entre $a + 1$.

**🔴 Nivel Avanzado**
5. Divide $x^{2n+3} + 4x^{2n+2} + x^{2n+1}$ entre $x^{n+1} + x^n$.

#### Respuestas para el Docente
1. $2x - 5$
2. $x + 5$
3. $x^3 + x^2 + x + 1$ (Se debe visualizar como $x^4 + 0x^3 + 0x^2 + 0x - 1$).
4. $a^2 - a + 1$
5. $x^{n+2} + 3x^{n+1}$ (Lógica de exponentes: $(2n+3) - (n+1) = n+2$).

---

### Mini-Prueba de Autoevaluación

1. **¿Cuál es la función primordial de ordenar y dejar espacios en el dividendo?**
   a) Cumplir con una norma estética.
   b) Asegurar que los términos semejantes se alineen en columnas para la resta.
   c) Facilitar la multiplicación de coeficientes.

2. **Si multiplicamos un término del cociente por el divisor y obtenemos $-5x^3$, ¿cómo debemos escribirlo bajo el dividendo?**
   a) $-5x^3$
   b) $0x^3$
   c) $+5x^3$

3. **¿Cuál es el resultado de multiplicar $a^x$ por $a^{x-2}$ siguiendo la ley de potencias?**
   a) $a^{2x-2}$
   b) $a^{-2}$
   c) $a^x-2$

---
**Próxima clase:** "Regla de Ruffini para divisiones sintéticas: El atajo para divisiones con divisores de primer grado".

> [!info] 🧭 Navegación
> [[Clase 04|⬅ Clase 04]] | [[00 - Índice del curso|Índice]] | **Clase 05** | | [[Clase 06|Clase 06 ➡]]