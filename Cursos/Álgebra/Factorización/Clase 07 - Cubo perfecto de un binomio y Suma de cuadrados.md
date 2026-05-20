# Clase 07 — Cubo perfecto de un binomio y Suma de cuadrados

#algebra #cuboperfecto #factorizacion #sumadecuadrados

> [!info] 🧭 Navegación
> *   **Anterior:** [[Clase 06 — Trinomio Cuadrado Perfecto y Diferencia de Cuadrados]]
> *   **Índice:** [[Índice de Álgebra]]
> *   **Siguiente:** [[Clase 08 — Suma o Diferencia de Cubos Perfectos]]

---

### 1. Importancia y Relevancia

> [!info] 🌍 Relevancia y aplicaciones
> El dominio de estas estructuras permite desglosar polinomios de alta complejidad en factores más simples, facilitando la optimización de diseños industriales y la interpretación de modelos de crecimiento tridimensional. Identificar un cubo perfecto o completar una potencia es la base para resolver ecuaciones de grado superior en física y economía.
> 
> *   💵 **Aplicación Financiera:** El modelo de interés compuesto para tres periodos, expresado como $C(1+r)^3$ USD, requiere reconocer cubos perfectos para simplificar proyecciones de ahorro o deuda.
> *   🏗️ **Aplicación Práctica:** En ingeniería civil, el cálculo de resistencia en contenedores cúbicos y la distribución de carga volumétrica dependen de estas factorizaciones.
> *   📊 **Situación Cotidiana:** La suma de volúmenes en el diseño de espacios arquitectónicos se simplifica mediante la completación de potencias para optimizar el uso de materiales.

---

### 2. Concepto Clave: Cubo Perfecto de un Binomio

> [!note] 📌 ¿Qué es el Cubo Perfecto de un Binomio?
> Es la operación inversa al producto notable del cubo de la suma o resta de dos cantidades. Para que un polinomio sea un Cubo Perfecto, debe poseer estrictamente **4 términos**, estar organizado y cumplir con la verificación del triple producto en sus términos centrales.

> [!warning] ⚠️ Error común y rigor didáctico
> ❌ **Asumir el resultado:** Muchos estudiantes factorizan solo con ver que los extremos tienen raíz cúbica.
> ✅ **Exigencia de Verificación:** Si los términos centrales no coinciden exactamente con la regla $3a^2b$ y $3ab^2$, la expresión **no es un cubo perfecto**. En ese caso, se debe buscar un "Factor Común" o concluir que el método no aplica.

> [!tip] 💡 Herramientas de supervivencia: Cubos del 1 al 7
> Para agilizar el reconocimiento visual, un experto debe memorizar los siguientes cubos:
> * $1^3 = 1$ | $2^3 = 8$ | $3^3 = 27$ | $4^3 = 64$
> * $5^3 = 125$ | $6^3 = 216$ | $7^3 = 343$

---

### 3. Procedimiento Paso a Paso

#### A. Factorización del Cubo Perfecto de un Binomio
Para garantizar precisión técnica, separe la verificación de coeficientes de la de variables:

1.  **Organizar y Diagnosticar:** Ordene el polinomio respecto a una variable. Observe la **progresión aritmética de los exponentes**: deben aumentar o disminuir de forma constante (de 1 en 1, de 2 en 2, o de 3 en 3). Ej: $a^6, a^4, a^2, a^0$.
2.  **Extraer Raíces Extremas:** Calcule la raíz cúbica ($\sqrt[3]{}$) del primer y cuarto término. (En letras, divida el exponente entre 3).
3.  **Verificación Rigurosa:**
    *   **Término 2:** Multiplique $3 \times (\text{1ra raíz})^2 \times (\text{2da raíz})$.
    *   **Término 3:** Multiplique $3 \times (\text{1ra raíz}) \times (\text{2da raíz})^2$.
    *   *Nota:* Verifique primero los números y luego las letras para reducir la saturación cognitiva.
4.  **Construcción del Binomio:** Si las pruebas coinciden, escriba las raíces en un paréntesis elevado al cubo: $(a \pm b)^3$.
    *   Use **(+)** si todos los signos son positivos.
    *   Use **(-)** si los signos se alternan ($+, -, +, -$).

#### B. Factorización por Suma de Cuadrados (Completación)
Este método se aplica a binomios ($a^4 + b^4$) donde ambos términos son cuadrados perfectos, pero no pueden factorizarse directamente. Se basa en el **Balance Algebraico**:

1.  **Extraer Raíces Cuadradas:** Calcule $\sqrt{}$ de ambos términos.
2.  **Hallar el "Término de Balance":** Multiplique $2 \times (\text{1ra raíz}) \times (\text{2da raíz})$. Este es el término necesario para formar un Trinomio Cuadrado Perfecto (TCP).
3.  **Sumar y Restar:** Agregue el término de balance en medio de los cuadrados y réstelo al final para no alterar la expresión.
4.  **Doble Factorización:** Factorice el TCP resultante y luego aplique **Diferencia de Cuadrados** a la expresión final.

---

### 4. Ejemplos Prácticos

```ad-example
title: Ejemplo 1: Cubo Básico con Exponentes Constantes
**Factorizar:** $m^3 + 3m^2n + 3mn^2 + n^3$
1. **Diagnóstico:** Los exponentes de $m$ bajan de 1 en 1 ($3, 2, 1, 0$). Correcto.
2. **Raíces:** $\sqrt[3]{m^3} = m$ (Base $a$); $\sqrt[3]{n^3} = n$ (Base $b$).
3. **Verificación:**
   - $3(m)^2(n) = 3m^2n$ (Coincide con el 2do término).
   - $3(m)(n)^2 = 3mn^2$ (Coincide con el 3er término).
4. **Resultado:** Todos positivos $\rightarrow$ **$(m + n)^3$**.
```

```ad-example
title: Ejemplo 2: Cubo con Alternancia de Signos y Coeficientes
**Factorizar:** $27 - 27x + 9x^2 - x^3$
1. **Raíces:** $\sqrt[3]{27} = 3$; $\sqrt[3]{x^3} = x$.
2. **Verificación Numérica:**
   - $3(3)^2(1) = 3(9) = 27$.
   - $3(3)(1)^2 = 9$.
3. **Resultado:** Signos intercalados ($+, -, +, -$) $\rightarrow$ **$(3 - x)^3$**.
```

```ad-example
title: Ejemplo 3: Suma de Cuadrados (Técnica de Completación)
**Factorizar:** $x^4 + 64y^4$
1. **Raíces cuadradas:** $\sqrt{x^4} = x^2$; $\sqrt{64y^4} = 8y^2$.
2. **Término de Balance:** Se requiere el doble producto de las raíces: $2(x^2)(8y^2) = 16x^2y^2$. Elegimos este término porque transforma los dos cuadrados originales en un TCP.
3. **Balance Algebraico:** $(x^4 + 16x^2y^2 + 64y^4) - 16x^2y^2$.
4. **Factorización Final:**
   - TCP: $(x^2 + 8y^2)^2 - (4xy)^2$
   - Dif. de Cuadrados: **$(x^2 + 4xy + 8y^2)(x^2 - 4xy + 8y^2)$**.
```

```ad-example
title: Ejemplo 4: Aplicación en Costos Financieros ($USD)
Se requiere simplificar la fórmula de costos operativos de una empresa representada por $4m^4 + 81n^4$ USD para facilitar la auditoría de activos.
1. **Raíces:** $\sqrt{4m^4} = 2m^2$; $\sqrt{81n^4} = 9n^2$.
2. **Balance:** $2(2m^2)(9n^2) = 36m^2n^2$.
3. **Estructura:** $(2m^2 + 9n^2)^2 - (6mn)^2$.
4. **Resultado Simplificado:** **$(2m^2 + 6mn + 9n^2)(2m^2 - 6mn + 9n^2)$ USD**.
```

---

### 5. Ejercicios para el Estudiante

```ad-abstract
title: 🟢 Nivel Fácil: Reconocimiento Directo
1. $a^3 + 3a^2 + 3a + 1$
2. $x^3 + 6x^2 + 12x + 8$
3. $8k^3 + 12k^2 + 6k + 1$
4. $y^3 + 3y^2z + 3yz^2 + z^3$
```

```ad-abstract
title: 🟡 Nivel Medio: Orden y Exponentes
1. $125a^3 + 150a^2b + 60ab^2 + 8b^3$
2. $64x^3 - 144x^2y + 108xy^2 - 27y^3$
3. $1 + 12a + 48a^2 + 64a^3$
4. $-125 + 75x - 15x^2 + x^3$ *(Nota: Reordenar a $x^3 - 15x^2 + 75x - 125$)*
```

```ad-abstract
title: 🔴 Nivel Avanzado: Suma de Cuadrados (Activos $USD)
Factorice las siguientes expresiones de valor comercial para simplificar el balance:
1. $64 + a^4$ USD
2. $x^4 + 324$ USD
3. $81 + 4y^4$ USD
4. $a^4 + 4b^4$ USD
```

```ad-success
title: Soluciones Detalladas (Uso Docente)
**Fácil:** 1. $(a+1)^3$ | 2. $(x+2)^3$ | 3. $(2k+1)^3$ | 4. $(y+z)^3$
**Medio:** 1. $(5a+2b)^3$ | 2. $(4x-3y)^3$ | 3. $(1+4a)^3$ | 4. $(x-5)^3$
**Avanzado:**
1. $(a^2 + 4a + 8)(a^2 - 4a + 8)$
2. $(x^2 + 6x + 18)(x^2 - 6x + 18)$
3. $(2y^2 + 6y + 9)(2y^2 - 6y + 9)$
4. $(a^2 + 2ab + 2b^2)(a^2 - 2ab + 2b^2)$
```

---

### 6. Autoevaluación

1.  **¿Qué ocurre si los exponentes de un polinomio de 4 términos disminuyen de forma irregular (ej. 6, 3, 2, 0)?**
    *   No cumple con la progresión aritmética necesaria y, por tanto, no puede ser un cubo perfecto de un binomio. Se debe buscar factor común.
2.  **¿Por qué en la suma de cuadrados sumamos y restamos el mismo término?**
    *   Para mantener el "Balance Algebraico". Al sumar 0 ($+X - X$), la expresión original no cambia su valor, pero su forma permite la factorización por TCP.
3.  **Si una proyección de gastos en $USD se simplifica como $(x - 1)^3$, ¿cuál era la expresión polinómica original?**
    *   $x^3 - 3x^2 + 3x - 1$.

---

### 7. Cierre y Conexión

> [!tip] 💡 En la próxima clase
> Estudiaremos la **Suma o Diferencia de Cubos Perfectos**. A diferencia de hoy (que trabajamos con polinomios de 4 términos), aprenderemos a factorizar binomios (solo 2 términos) mediante el producto de un binomio por un trinomio especial.

> [!info] 🧭 Navegación
> *   **Anterior:** [[Clase 06 — Trinomio Cuadrado Perfecto y Diferencia de Cuadrados]]
> *   **Índice:** [[Índice de Álgebra]]
> *   **Siguiente:** [[Clase 08 — Suma o Diferencia de Cubos Perfectos]]