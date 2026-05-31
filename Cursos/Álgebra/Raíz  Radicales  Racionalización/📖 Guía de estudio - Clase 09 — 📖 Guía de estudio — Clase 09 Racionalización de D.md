# 📖 Guía de estudio — Clase 09: Racionalización de Denominadores

¡Qué tal, amigas y amigos! Espero que estén muy bien. Bienvenidos a una nueva sesión de matemáticas. Hoy vamos a aprender a "limpiar" nuestras fracciones quitando esas raíces del denominador que a veces nos complican la vida.

> [!info] 📌 Conceptos clave
> La **racionalización** es el proceso de encontrar una **fracción equivalente** que no tenga radicales en su denominador. Para lograrlo, no inventamos números, sino que usamos la **amplificación**: multiplicamos el numerador y el denominador por el mismo valor (un "1" disfrazado), de modo que no alteramos el valor de la fracción.
> 
> *   **En binomios:** Usamos el **conjugado** para crear una diferencia de cuadrados que elimine las raíces.
> *   **En raíces de mayor orden:** Buscamos "completar" el exponente para que sea igual al índice de la raíz (si tengo $\sqrt[5]{x^2}$, me faltan 3 para llegar a 5, así que multiplico por $\sqrt[5]{x^3}$).

## Definiciones y Fórmulas

| Término | Definición / Fórmula |
| :--- | :--- |
| **Racionalizar** | Proceso para quitar raíces del denominador buscando una fracción equivalente. |
| **Conjugado de un binomio** | Es la misma expresión pero con el signo central cambiado: $(a + b) \to (a - b)$ o viceversa. |
| **Diferencia de cuadrados** | $(a + b)(a - b) = a^2 - b^2$. Al elevar al cuadrado, la raíz desaparece. |
| **Índice y Exponente** | Propiedad clave: $\sqrt[n]{x^n} = x$. Buscamos que el exponente interno iguale al índice. |

> [!warning] 🚩 ¡Cuidado con la trampa!
> Antes de racionalizar, mira bien los números. Si el denominador es una raíz exacta como $\sqrt{4}$ o $\sqrt{25}$, **no racionalices**. Simplemente resuelve la raíz ($\sqrt{4} = 2$) y simplifica la fracción. ¡No trabajes de más!

## Ejemplos Resueltos

Para dominar este tema, recuerda: siempre dejamos la operación del numerador indicada hasta el final por si podemos simplificar.

> [!example] Ejemplo A: Caso Binomio (Raíces cuadradas)
> Racionalizar la expresión: $\frac{2}{\sqrt{5} - \sqrt{3}}$
> 
> 1. **Identificar el conjugado:** Como abajo dice $\sqrt{5} - \sqrt{3}$, multiplicaremos por $\sqrt{5} + \sqrt{3}$.
> 2. **Multiplicar arriba y abajo:** 
>    $$\frac{2}{(\sqrt{5} - \sqrt{3})} \cdot \frac{(\sqrt{5} + \sqrt{3})}{(\sqrt{5} + \sqrt{3})}$$
> 3. **¡Ya hicimos lo difícil, ahora viene lo fácil!** Operamos el denominador usando diferencia de cuadrados: $(\sqrt{5})^2 - (\sqrt{3})^2 = 5 - 3 = 2$.
> 4. **Simplificar:** 
>    $$\frac{2(\sqrt{5} + \sqrt{3})}{2}$$
>    Como el 2 de afuera es un factor, lo simplificamos con el 2 de abajo. **Resultado:** $\sqrt{5} + \sqrt{3}$.

> [!example] Ejemplo B: Aplicación Real (Costo en USD)
> Un terreno de área $(\sqrt{7} - 1)$ m² tiene un costo total de $12$ USD. ¿Cuál es el precio racionalizado por metro cuadrado?
> 
> *   **Planteamiento:** Precio = $\frac{12}{\sqrt{7} - 1}$
> *   **Multiplicamos por el conjugado $(\sqrt{7} + 1)$:**
>    $$\frac{12}{(\sqrt{7} - 1)} \cdot \frac{(\sqrt{7} + 1)}{(\sqrt{7} + 1)} = \frac{12(\sqrt{7} + 1)}{(\sqrt{7})^2 - (1)^2} = \frac{12(\sqrt{7} + 1)}{7 - 1} = \frac{12(\sqrt{7} + 1)}{6}$$
> *   **Simplificación final:** Dividimos $12 / 6 = 2$. Ahora aplicamos propiedad distributiva: $2(\sqrt{7} + 1) = 2\sqrt{7} + 2$.
> *   **Resultado:** $2\sqrt{7} + 2$ USD por metro cuadrado.

> [!example] Ejemplo C: Raíz de mayor orden (Índice > 2)
> Racionalizar: $\frac{2}{\sqrt[3]{5}}$
> 
> 1. **Analizar qué falta:** El índice es 3 y el exponente del 5 es 1. ¿Cuánto le falta al 1 para llegar a 3? ¡Le faltan 2!
> 2. **Multiplicar por lo que falta:** Multiplicamos por $\sqrt[3]{5^2}$ arriba y abajo.
>    $$\frac{2}{\sqrt[3]{5^1}} \cdot \frac{\sqrt[3]{5^2}}{\sqrt[3]{5^2}} = \frac{2\sqrt[3]{25}}{\sqrt[3]{5^3}}$$
> 3. **Simplificar:** Como el índice y el exponente son iguales, la raíz se va.
>    **Resultado:** $\frac{2\sqrt[3]{25}}{5}$.

## Ejercicios de Repaso

> [!abstract] 🟢 Nivel Fácil: Monomios
> Racionaliza y simplifica los factores externos:
> 1. $\frac{5}{\sqrt{3}}$
> 2. $\frac{1}{\sqrt{2}}$
> 3. $\frac{10}{\sqrt{5}}$ (Recuerda simplificar $10/5$ al final).

> [!abstract] 🟡 Nivel Medio: Binomios y Raíces Especiales
> 1. $\frac{3}{\sqrt{7} + 2}$
> 2. $\frac{4}{\sqrt{5} - \sqrt{3}}$
> 3. $\frac{5}{\sqrt[4]{2^1}}$ (Busca cuánto le falta al exponente para llegar a 4).

> [!abstract] 🔴 Nivel Avanzado: Aplicación Económica ($USD)
> 1. El costo de una cerca es $10 / (\sqrt{3} - 1)$ USD por metro. Racionaliza y simplifica totalmente la expresión. (Pista: el resultado final es $5\sqrt{3} + 5$ USD).
> 2. Un terreno cuesta $500 / (\sqrt{5} + \sqrt{2})$ USD. Halla su valor racionalizado.
> 3. El presupuesto de un material es $20 / (3 - \sqrt{5})$ USD. Racionaliza para facilitar el pago contable.

> [!tip] 💡 Consejo de estudio
> ¡No te apresures a multiplicar el numerador! Déjalo indicado con paréntesis, como vimos en los ejemplos. Al final del proceso, revisa siempre si los números de afuera se pueden simplificar o dividir con el denominador. Y mucho ojo: si el original es resta, el conjugado lleva suma. ¡Tú puedes, lo vas a lograr!