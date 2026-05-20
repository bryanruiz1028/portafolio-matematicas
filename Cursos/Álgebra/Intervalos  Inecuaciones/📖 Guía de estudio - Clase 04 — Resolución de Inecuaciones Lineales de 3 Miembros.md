# 📖 Guía de estudio — Clase 04: Resolución de inecuaciones lineales de 3 miembros

> [!info] 📌 Conceptos clave
> - **Definición:** Una inecuación de 3 miembros es una expresión con dos símbolos de desigualdad que dividen la operación en un miembro izquierdo, uno central y uno derecho. Se busca el intervalo de valores que satisfacen ambas condiciones a la vez.
> - **Condición ideal para despeje directo:** Para aplicar el método más sencillo, la variable $x$ debe estar únicamente en el centro, los símbolos deben ser "menor que" ($<$ o $\leq$) y el valor de la izquierda debe ser menor al de la derecha ($a < b$).
> - **Método de despeje simultáneo:** Si se cumple la condición ideal, realizamos la misma operación aritmética (sumar, restar, multiplicar o dividir) en los tres miembros al mismo tiempo para dejar sola a la $x$.
> - **Método de separación:** Si la $x$ aparece en los extremos, debemos separar la expresión en dos inecuaciones independientes, resolverlas por separado y luego hallar su **intersección** (donde se cruzan las soluciones).

## Sección: Fórmulas y Definiciones Importantes

| Término | Definición / Aplicación |
| :--- | :--- |
| **Inecuación lineal de 3 miembros** | Expresión con tres componentes. Para el método directo, es vital que el número de la izquierda sea menor que el de la derecha ($a < x < b$, donde $a < b$). |
| **Propiedad de la desigualdad** | Al multiplicar o dividir toda la inecuación por un número negativo, el sentido de los símbolos **debe invertirse inmediatamente** (de $<$ a $>$) para mantener la verdad matemática. |
| **Conjunto Vacío ($\emptyset$)** | Ocurre cuando, al realizar la gráfica, los intervalos de las dos inecuaciones separadas no se cruzan en ningún punto. No hay valores que cumplan ambas condiciones. |

## Sección: Ejemplos Resueltos Adicionales

```ad-example
**Ejemplo A: Caso Básico (Video 1)**
**Enunciado:** Resolver $3 < x + 1 < 7$

**Paso a paso:**
1. Queremos dejar sola a la $x$. Como el 1 está sumando, restamos 1 en los tres miembros:
   $3 - 1 < x + 1 - 1 < 7 - 1$
2. Realizamos las operaciones resultantes:
   $2 < x < 6$

**Resultado:**
- **Intervalo:** $(2, 6)$
- **Gráfica:** Representamos **círculos huecos** en el 2 y en el 6 (indicando que no se incluyen los extremos) y sombreamos el segmento entre ellos.
```

```ad-example
**Ejemplo B: Aplicación Real ($USD)**
**Enunciado:** "El triple de un ahorro menos 7 dólares debe estar entre 5 y 14 dólares" ($5 \leq 3x - 7 < 14$).

**Paso a paso:**
1. Sumamos 7 en los tres miembros para eliminar el -7 del centro:
   $5 + 7 \leq 3x - 7 + 7 < 14 + 7 \implies 12 \leq 3x < 21$
2. Dividimos todos los miembros entre 3 para despejar la $x$:
   $\frac{12}{3} \leq \frac{3x}{3} < \frac{21}{3} \implies 4 \leq x < 7$
   *Nota: Como dividimos por un número positivo (3), los símbolos de desigualdad **no cambian** su orientación.*

**Resultado:**
- **Intervalo:** $[4, 7)$
- **Significado:** El ahorro debe ser de al menos 4 dólares (incluido, representado con **corchete** y **círculo relleno**) y menos de 7 dólares (no incluido, representado con **paréntesis** y **círculo hueco**).
```

## Sección: Ejercicios de Repaso

```ad-abstract
**Nivel Fácil (Verde)**
Halla el conjunto solución de la siguiente inecuación:
$-3 < x - 4 \leq 0$
*Pista: Suma 4 en los tres miembros para despejar la $x$.*
```

```ad-abstract
**Nivel Medio (Amarillo)**
Resuelve la siguiente inecuación:
$-6 \leq 2x - 4 < 5$
*Pista: Primero suma 4 en todos los miembros y luego divide para 2. Recuerda que al dividir por un positivo, el sentido se mantiene.*
```

```ad-abstract
**Nivel Avanzado (Rojo - Aplicación USD)**
**Contexto:** Se comparan tres servicios de suscripción mensual:
- Servicio A: $1 + 4x$
- Servicio B: $5x - 9$
- Servicio C: $10x + 6$
Determina el rango de $x$ para que el costo del **Servicio B esté entre el de A y C**, es decir:
$1 + 4x \leq 5x - 9 \leq 10x + 6$

*Guía técnica: Separa en dos inecuaciones ($1 + 4x \leq 5x - 9$ y $5x - 9 \leq 10x + 6$). Resuélvelas pasando las $x$ a la izquierda. Si la $x$ queda negativa al final, multiplica por -1 e invierte el signo.*
```

> [!tip] 💡 Consejo de estudio
> Para no fallar, utiliza la **Lógica de Sectores**. Al graficar, divide la recta según los puntos críticos obtenidos. La solución final es la **Intersección**: el sector donde las líneas de ambas soluciones coinciden (donde "se cruzan"). 
> 
> **Regla de oro:** Si al multiplicar o dividir por un negativo olvidas invertir el signo inmediatamente, tu gráfica no tendrá sentido. Si tras graficar correctamente ves que las líneas corren en direcciones opuestas y nunca se tocan, la respuesta es el **Conjunto Vacío ($\emptyset$)**. Para los símbolos $\leq$ o $\geq$ usa siempre **círculos rellenos**, y para $<$ o $>$ usa **círculos huecos**.