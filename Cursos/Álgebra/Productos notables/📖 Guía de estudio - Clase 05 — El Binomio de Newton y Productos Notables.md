# 📖 Guía de estudio — Clase 05: El Binomio de Newton

¡Hola, estimables estudiantes! Antes de sumergirnos en el desarrollo algebraico, es fundamental realizar una **verificación previa**: para aplicar este método, debemos confirmar que la expresión sea efectivamente un binomio (dos términos) y que su exponente sea un número entero. Recuerden que el Binomio de Newton es la generalización de los productos notables que hemos visto, como el binomio al cuadrado o el binomio al cubo; incluso casos especiales como el **binomio conjugado** ($(a+b)(a-b)$) pueden entenderse bajo esta lógica, aunque tengan sus propias reglas simplificadas.

> [!info] 📌 Conceptos clave
> *   **Triángulo de Pascal:** Es la herramienta que nos proporciona los coeficientes numéricos. Se construye de forma piramidal, donde cada número es el resultado de sumar los dos números adyacentes de la fila superior.
> *   **Número de términos:** Una regla de oro: el desarrollo de un binomio elevado a la $n$ siempre tendrá **$n+1$** términos (ej. si el exponente es 4, obtendremos 5 términos).
> *   **Comportamiento de los exponentes:** En cada término, el exponente del primer elemento del binomio disminuye gradualmente (de $n$ hasta $0$), mientras que el exponente del segundo elemento aumenta (de $0$ hasta $n$).

---

## 1. TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Coeficiente** | Es el número que acompaña a la parte literal (letras). Según el Profe Alex, es "el numerito" que multiplica a las variables. |
| **Triángulo de Pascal** | Estructura numérica donde el vértice superior es 1 y cada valor inferior nace de la suma de los dos que tiene encima. Define los coeficientes según el exponente. |
| **Regla de Signos** | Si el binomio es una resta $(a-b)$, los signos del resultado se intercalan empezando siempre por positivo: $(+ , - , + , - \dots)$. |
| **Potencia de una potencia** | Si un término ya tiene un exponente interno, este se multiplica por el exponente externo: $(a^m)^n = a^{m \cdot n}$. |
| **Propiedad Distributiva** | El exponente de un término compuesto afecta a cada factor: $(3x)^2 = 3^2 \cdot x^2 = 9x^2$. |

---

## 2. EJEMPLOS RESUELTOS ADICIONALES

```ad-example
title: Ejemplo A (Caso Didáctico): Desarrollo de $(3m + 2n)^4$
**Paso 1: Identificar coeficientes**
Para un exponente 4, consultamos la fila correspondiente del Triángulo de Pascal: **1, 4, 6, 4, 1**. Al ser una suma, todos los signos serán positivos.

**Paso 2: Potencias del primer término ($3m$)**
El primer término disminuye su potencia de 4 a 0 de izquierda a derecha:
$(3m)^4, (3m)^3, (3m)^2, (3m)^1, (3m)^0$.

**Paso 3: Potencias del segundo término ($2n$)**
El segundo término aumenta su potencia de 0 a 4 de izquierda a derecha:
$(2n)^0, (2n)^1, (2n)^2, (2n)^3, (2n)^4$.

**Paso 4: Resolución de potencias y productos finales**
1. $1 \cdot (3m)^4 \cdot (2n)^0 = 1 \cdot 81m^4 \cdot 1 = \mathbf{81m^4}$
2. $4 \cdot (3m)^3 \cdot (2n)^1 = 4 \cdot 27m^3 \cdot 2n = \mathbf{216m^3n}$
3. $6 \cdot (3m)^2 \cdot (2n)^2 = 6 \cdot 9m^2 \cdot 4n^2 = \mathbf{216m^2n^2}$
4. $4 \cdot (3m)^1 \cdot (2n)^3 = 4 \cdot 3m \cdot 8n^3 = \mathbf{96mn^3}$
5. $1 \cdot (3m)^0 \cdot (2n)^4 = 1 \cdot 1 \cdot 16n^4 = \mathbf{16n^4}$

**Resultado final:** $81m^4 + 216m^3n + 216m^2n^2 + 96mn^3 + 16n^4$
```

```ad-example
title: Ejemplo B (Aplicación Real): Área de Terreno y Presupuesto
**Problema:** Un terreno cuadrado tiene un lado que mide $(x + 2)$ metros. 
1. Desarrolla la expresión para calcular el área total en metros cuadrados.
2. Si el costo de preparación del terreno es de 10 USD por cada metro cuadrado, ¿cuál es la expresión del costo total?

**Resolución:**
1. **Área:** $(x + 2)^2$
   - Coeficientes (exponente 2): 1, 2, 1.
   - Desarrollo: $1(x)^2 + 2(x)^1(2)^1 + 1(2)^2 = \mathbf{x^2 + 4x + 4}$ m².
2. **Costo Total (USD):** Multiplicamos el área por 10 USD.
   - Expresión final: $10(x^2 + 4x + 4) = \mathbf{10x^2 + 40x + 40}$ USD.
```

---

## 3. EJERCICIOS DE REPASO

```ad-abstract
title: 🟢 Nivel Fácil: Expansión Simple
Utiliza los coeficientes básicos del Triángulo de Pascal (1, 2, 1 o 1, 3, 3, 1) para expandir:
1. $(a + b)^3$
2. $(x - y)^2$
3. $(m + n)^3$
```

```ad-abstract
title: 🟡 Nivel Medio: Coeficientes y Exponentes Internos
Aplica la propiedad de "potencia de una potencia" y reparte el exponente correctamente:
1. $(2x + 3y)^4$
2. $(x - 2y)^5$ (Tip: Coeficientes 1, 5, 10, 10, 5, 1)
3. $(2x^2 + y)^3$ (Cuidado: el exponente de $x$ debe saltar de 2 en 2).
```

```ad-abstract
title: 🔴 Nivel Avanzado: Aplicación Presupuestaria ($USD)
**Planteamiento:** Una constructora estima que el presupuesto para materiales y mano de obra de un complejo habitacional sigue la expansión de la expresión $(5x + 10)^3$ USD, donde $x$ es una variable de ajuste de inflación.
**Ejercicio:** Desarrolla completamente la expresión del costo total.
```

---

## 4. CONSEJO DE ESTUDIO

> [!tip] 💡 Estrategia de Verificación en Tres Pasos
> No des por terminado un ejercicio sin antes realizar estas tres comprobaciones rápidas:
> 1. **Signos:** Si hay una resta en el binomio, verifica que los signos en el resultado sigan el patrón $+ , - , + , - \dots$.
> 2. **Suma de Exponentes:** En cada término intermedio, la suma de los exponentes de las letras debe ser igual al exponente original del binomio (siempre que los términos internos no tengan exponentes propios).
> 3. **Verificación del Salto:** Si un término tiene un exponente interno (ej. $x^2$), sus exponentes en el desarrollo deben "saltar" según esa base. Si es $x^2$ elevado a la 4, verás exponentes como $x^8, x^6, x^4, x^2$. ¡Si bajan de uno en uno, hay un error!