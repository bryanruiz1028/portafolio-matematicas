# 📖 Guía de estudio — Clase 04: Multiplicación de números complejos conjugados

¡Qué tal, amigas y amigos! Espero que estén muy bien. En esta guía vamos a aprender a multiplicar un número complejo por su conjugado de una forma supremamente fácil. Este es un paso fundamental que nos servirá, más adelante, para dominar la división de complejos. ¡Acompañenme!

> [!info] 📌 Conceptos clave
> 1. **Definición de conjugado:** El conjugado de un número complejo se obtiene manteniendo exactamente igual la parte real y cambiando el signo únicamente a la parte imaginaria. Se representa con una barra sobre la letra del número ($\bar{z}$).
> 2. **Regla de binomios conjugados:** Al multiplicar complejos conjugados, aplicamos el producto notable $(a + b)(a - b) = a^2 - b^2$. En el campo de los complejos, esto se traduce inicialmente como el primer término al cuadrado menos el segundo término al cuadrado: $a^2 - (bi)^2$.
> 3. **Valor fundamental de $i^2$:** Nunca olvides que la unidad imaginaria elevada al cuadrado siempre equivale a $-1$ ($i^2 = -1$).
> 4. **Resultado real:** Una propiedad asombrosa de esta operación es que el producto de un número complejo por su conjugado siempre da como resultado un **número real**. ¡La parte imaginaria desaparece!

---

## 2. TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Número Complejo Conjugado** | Se denota como $\bar{z}$. Si $z = a + bi$, su conjugado es $\bar{z} = a - bi$. Solo cambia el signo central. |
| **Unidad Imaginaria al Cuadrado** | Es la equivalencia clave para eliminar la $i$ del resultado: $i^2 = -1$. |
| **Producto de Conjugados (Atajo)** | $(a + bi)(a - bi) = a^2 + b^2$. <br> *Nota: $a$ y $b$ son los coeficientes reales (ignoramos la $i$ y el signo de $b$ al elevar al cuadrado).* |

---

## 3. EJEMPLOS RESUELTOS ADICIONALES

````ad-example
title: Ejemplo A — Caso básico
**Problema:** Sea $z = 5 + 6i$, calcula el producto del número por su conjugado ($z \cdot \bar{z}$).

**Paso a paso:**
1. **Identificar el conjugado:** Si $z = 5 + 6i$, entonces su conjugado es $\bar{z} = 5 - 6i$.
2. **Aplicar el atajo ($a^2 + b^2$):** 
   - Identificamos $a = 5$ y $b = 6$.
   - Elevamos la parte real al cuadrado: $5^2 = 25$.
   - Elevamos el coeficiente imaginario al cuadrado: $6^2 = 36$.
3. **Suma final:** $25 + 36 = 61$.

**Resultado:** 61
````

````ad-example
title: Ejemplo B — Aplicación con balance financiero $USD
**Escenario:** En una cuenta contable, un movimiento con riesgo se representa por $z = 9 - 4i$. Para "limpiar" el riesgo imaginario y obtener el valor real en USD, multiplicamos por su complejo conjugado.

**Paso a paso:**
1. **Identificar valores:** El número es $9 - 4i$ y su conjugado es $9 + 4i$.
2. **Aplicar el atajo directamente:**
   - Tomamos la parte real ($9$) y la elevamos al cuadrado: $9^2 = 81$.
   - Tomamos el coeficiente de la parte imaginaria ($4$) y lo elevamos al cuadrado: $4^2 = 16$.
3. **Realizar la suma:** $81 + 16 = 97$.

**Resultado:** El balance real es de **97 USD**.
````

---

## 4. EJERCICIOS DE REPASO

````ad-abstract
title: 🟢 Nivel Verde (Fácil) - Multiplicación Directa
Calcula el valor real multiplicando cada número por su conjugado:
1. $(3 + 2i) \cdot (3 - 2i)$
2. $(7 - 1i) \cdot (7 + 1i)$
3. $(4 + 5i) \cdot (4 - 5i)$
````

````ad-abstract
title: 🟡 Nivel Amarillo (Medio) - Con Números Negativos
Resuelve aplicando el atajo, prestando atención a la parte real negativa:
1. $(-5 - 3i) \cdot (-5 + 3i)$
2. $(-2 + 8i) \cdot (-2 - 8i)$
3. $(-6 - 4i) \cdot (-6 + 4i)$
````

````ad-abstract
title: 🔴 Nivel Rojo (Avanzado) - Ajuste de Divisas
Calcula el valor real para los siguientes casos especiales de activos:
1. **Activo Volátil:** Un bono tiene un valor puramente imaginario de $5i$. Halla su conjugado y multiplícalos.
2. **Activo Estable:** Una deuda se representa como un número puramente real de $-12$. *(Pista: Recuerda que un número real tiene una parte imaginaria de $0i$, por lo que su conjugado es él mismo).* Halla su conjugado y realiza la multiplicación.
````

---

## 5. CONSEJO DE ESTUDIO

> [!tip] 💡 Consejo de estudio
> ¡Mucho ojo! No confundas el **conjugado** con el **opuesto**. El opuesto cambia los signos de ambos términos (real e imaginario), mientras que el conjugado **solo** cambia el de la parte imaginaria. Dominar el atajo $a^2 + b^2$ te ahorrará muchísimo tiempo y evitará errores de signos cuando lleguemos al tema de **división de números complejos**, donde multiplicar por el conjugado es obligatorio para "limpiar" el denominador.

¡Sigue practicando para dominar el plano complejo! Nos vemos en la próxima clase.