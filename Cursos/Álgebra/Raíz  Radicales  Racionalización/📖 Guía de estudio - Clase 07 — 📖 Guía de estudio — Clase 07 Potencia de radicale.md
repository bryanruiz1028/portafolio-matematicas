# 📖 Guía de estudio — Clase 07: Potencia de radicales

> [!info] 📌 Conceptos clave
> - **Propiedad distributiva:** Al elevar un producto radical a una potencia, el exponente afecta tanto al coeficiente exterior como al radicando (el número o variable dentro de la raíz). Primero distribuimos para manejar términos por separado antes de que los valores crezcan demasiado.
> - **Multiplicación de exponentes:** Si el radicando ya tiene un exponente propio, este se debe multiplicar por el exponente exterior (potencia de una potencia) siguiendo la regla $(x^n)^m = x^{n \cdot m}$.
> - **Simplificación por división:** Se puede extraer un factor de la raíz dividiendo su exponente entre el índice de la raíz. Si el exponente y el índice son iguales, se anulan y el factor queda libre.
> - **Analogía de la "cárcel":** Imagina la raíz como una "cárcel" donde el índice es la condena (años necesarios). Un factor solo "sale de la cárcel" si su exponente alcanza o supera los años de condena requeridos.

# SECCIÓN: FÓRMULAS Y DEFINICIONES IMPORTANTES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Potencia de un producto radical** | $(a \cdot \sqrt[n]{b})^m = a^m \cdot \sqrt[n]{b^m}$ |
| **Simplificación por división** | El factor sale de la raíz como una potencia fraccionaria o simplificada: $\sqrt[n]{x^m} = x^{m/n}$ |
| **Descomposición en factores** | Antes de elevar, los números compuestos se expresan en factores primos (ej. $72 = 2^3 \cdot 3^2$) para facilitar el cálculo de "condenas". |

# SECCIÓN: EJEMPLOS RESUELTOS ADICIONALES

````ad-example
title: Ejemplo A — Potencia con coeficiente y variable
**Ejercicio:** Resolver $(5\sqrt{x})^4$

*   **Paso 1 (Distribuir exponente):** Se eleva el coeficiente $5$ y la raíz al exponente $4$:
    $5^4 \cdot \sqrt{x^4}$
*   **Paso 2 (Elevar coeficiente):** Multiplicamos el $5$ por sí mismo cuatro veces:
    $5 \cdot 5 \cdot 5 \cdot 5 = 625$
*   **Paso 3 (Simplificar raíz con la "cárcel"):** Recordemos que la raíz cuadrada tiene un índice "invisible" de $2$. El exponente de $x$ es $4$. Como el preso tiene $4$ años y la condena es de $2$, dividimos: $4 \div 2 = 2$. El factor **sale de la cárcel** con exponente $2$.

**Resultado final:** $625x^2$
````

````ad-example
title: Ejemplo B — Aplicación en costos financieros ($USD)
**Enunciado:** El costo de una transacción bancaria está definido por la expresión $(2\sqrt[3]{10})^2$ dólares. Simplifique la expresión.

*   **Paso 1 (Elevar coeficiente):** Elevamos el $2$ al cuadrado:
    $2^2 = 4$
*   **Paso 2 (Elevar el radicando):** El exponente entra a la raíz para afectar al $10$:
    $4 \cdot \sqrt[3]{10^2}$
*   **Paso 3 (Simplificar):** Desarrollamos la potencia interna. Como el exponente ($2$) es menor que el índice ($3$), el factor no "cumple la condena" y no puede salir de la cárcel:
    $4 \cdot \sqrt[3]{100}$

**Resultado final:** $4\sqrt[3]{100}$ USD
````

# SECCIÓN: EJERCICIOS DE REPASO

````ad-abstract
title: 🟢 Fácil
1. $(\sqrt{m})^2$ — *(Resultado: $m$)*
2. $(\sqrt[3]{x})^3$ — *(Resultado: $x$)*
3. $(\sqrt{5})^4$ — *(Resultado: $25$)*
````

````ad-abstract
title: 🟡 Medio
1. $(\sqrt[6]{18})^3$ (Sugerencia: descomponer 18 en $2 \cdot 3^2$ y simplificar el índice). — *(Resultado: $3\sqrt{2}$)*
2. $(2\sqrt{x^3})^2$ — *(Resultado: $4x^3$)*
3. $(\sqrt[4]{12})^2$ (Sugerencia: descomponer 12 en $2^2 \cdot 3$). — *(Resultado: $2\sqrt{3}$)*
````

````ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
1. El área de un terreno cuadrado se expresa como $(\sqrt[4]{72x^2})^2$ metros cuadrados. Si cada metro cuadrado cuesta $x$ USD, determine la expresión simplificada del **costo total**. (Use $72 = 2^3 \cdot 3^2$). — *(Resultado: $6x^2\sqrt{2}$ USD)*
2. Si el precio de un artículo es $(\sqrt[6]{72})^2$ USD, simplifique la expresión aplicando la reducción de índice y extracción de factores. — *(Resultado: $\sqrt[3]{72} = 2\sqrt[3]{9}$ USD)*
3. Una inversión se calcula con la expresión $(\sqrt[10]{72^2})^5$ USD. Aplique la propiedad de potencia de una potencia para eliminar el radical y hallar el valor entero. — *(Resultado: $72$ USD)*
````

# SECCIÓN: CONSEJO DE ESTUDIO

> [!tip] 💡 Consejo de estudio
> ¡No te apresures a multiplicar! Antes de aplicar el exponente, revisa si el radicando se puede descomponer en factores primos. Al transformar un $72$ en $2^3 \cdot 3^2$, es mucho más fácil multiplicar esos exponentes internos por el exterior y ver quiénes logran "cumplir su condena" para salir de la raíz. Esto mantiene los números pequeños y reduce errores de cálculo.