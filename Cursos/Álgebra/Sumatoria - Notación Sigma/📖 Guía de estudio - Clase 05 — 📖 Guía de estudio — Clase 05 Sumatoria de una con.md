# 📖 Guía de estudio — Clase 05: Sumatoria de una constante por una variable

> [!info] 📌 Conceptos clave
> - **Extracción de la constante:** Por la propiedad distributiva (factor común), si una constante multiplica a una variable, esta puede salir de la sumatoria para simplificar el proceso.
> - **Límite inferior ideal:** Las fórmulas directas de sumas notables están diseñadas para funcionar cuando la sumatoria inicia en $1$. Si inicia en otro número, debemos ajustar los límites.
> - **Propiedad aditiva y de diferencia:** Una sumatoria que contiene una suma o resta de términos puede separarse en sumatorias independientes.
> - **Cambio de índice:** Es la técnica para transformar los límites. Aplicamos "operaciones contrarias": si restamos a los límites para llegar a 1, sumamos ese mismo valor a la variable dentro de la función.

## FÓRMULAS Y DEFINICIONES IMPORTANTES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Propiedad de la Constante** | $\sum (c \cdot a_i) = c \cdot \sum a_i$ <br> (La constante sale a multiplicar al resultado total). |
| **Suma de una Variable ($i$)** | $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$ |
| **Suma de una Constante** | $\sum_{i=1}^{n} c = n \cdot c$ <br> (Válido únicamente cuando el límite inferior es 1). |
| **Suma de Cuadrados ($i^2$)** | $\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$ |

> [!important] **Nota didáctica sobre el cambio de índice**
> Al realizar cambios de índice, recuerda proteger siempre la variable con **paréntesis** al realizar la sustitución compensatoria. Por ejemplo, si aplicas un desplazamiento $k$, la expresión cambia de la siguiente forma: $c \cdot i \rightarrow c(i+k)$.

## EJEMPLOS RESUELTOS ADICIONALES

```ad-example
title: Ejemplo A — Constante por variable
**Ejercicio:** Calcular la sumatoria $\sum_{i=1}^{6} 3i$.

**Paso a paso:**
1. **Factor Común:** El número 3 es una constante que multiplica a cada término. Aplicamos la propiedad de extracción (equivalente a sacar el factor común de la serie):
   $3 \cdot \sum_{i=1}^{6} i$
2. **Aplicar la fórmula de la variable:** Usamos la fórmula $\frac{n(n+1)}{2}$ con $n=6$:
   $3 \cdot \left( \frac{6(6+1)}{2} \right)$
3. **Resolver:**
   $3 \cdot \left( \frac{6 \cdot 7}{2} \right) = 3 \cdot 21$
4. **Resultado final:** **63**
```

```ad-example
title: Ejemplo B — Ahorro diario acumulado
**Enunciado:** Un estudiante decide ahorrar dinero durante 10 días para comprar un libro. El ahorro es progresivo: el día 1 ahorra $3 USD, el día 2 ahorra $6 USD, el día 3 ahorra $9 USD, y así sucesivamente (siempre el triple del número del día). ¿Cuál es el monto total acumulado?

**Desarrollo:**
1. **Modelado matemático:** Representamos la acumulación como una sumatoria donde $i$ es el día: $\sum_{i=1}^{10} 3i$.
2. **Extracción de la constante:** $3 \cdot \sum_{i=1}^{10} i$.
3. **Cálculo con fórmula ($n=10$):**
   $3 \cdot \left( \frac{10(11)}{2} \right) = 3 \cdot 55$
4. **Resultado:** El estudiante tendrá un total de **$165 USD**.
```

## EJERCICIOS DE REPASO

```ad-abstract
title: 🟢 Nivel: Fácil (Aplicación directa)
1. Calcule el valor de $\sum_{i=1}^{20} 5i$.
2. Calcule el valor de $\sum_{i=1}^{15} 2i$.
3. Calcule el valor de $\sum_{i=1}^{40} 3i$.
```

```ad-abstract
title: 🟡 Nivel: Medio (Separación de términos)
*Separe los términos y extraiga las constantes antes de operar:*
1. $\sum_{i=1}^{10} (2i + 5)$
2. $\sum_{i=1}^{20} (3i - 4)$
3. $\sum_{i=1}^{15} (4i + 10)$
```

```ad-abstract
title: 🔴 Nivel: Avanzado (Cambio de índice y Aplicación)
*Realice el ajuste de límites para que i inicie en 1, usando paréntesis para proteger la variable:*
1. Un presupuesto de obra civil aumenta según la sumatoria $\sum_{i=5}^{15} 3i$. Ajuste el índice y calcule el costo total en USD.
2. Calcule el valor de la sumatoria $\sum_{i=7}^{20} 2i$ aplicando el ajuste de límites necesario.
3. **Desafío Maestro:** Realice el cambio de índice y resuelva $\sum_{i=8}^{15} (2i^2 - 4)$. (Recuerde que al sustituir $i$ por $(i+k)$, debe desarrollar el binomio al cuadrado resultante).
```

> [!tip] 💡 Consejo de estudio
> El objetivo principal del **cambio de índice** es siempre "desbloquear" las fórmulas rápidas del Profe Alex logrando que la suma inicie en $i=1$. Para no fallar, usa la regla de oro: **Operación contraria y Paréntesis**. Si restas a los límites, sumas a la variable; si sumas a los límites, restas a la variable. ¡Siempre dentro de un paréntesis protector!