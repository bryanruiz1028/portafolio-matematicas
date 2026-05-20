# Clase 02 — Potencias con exponente fraccionario y Radicales

[[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | [[Clase 03|Clase 03 ➡]]

#algebra #powerwithfractionalexponent #radicales

> [!info] 🧭 Navegación
> ¡Qué tal, amigos! En esta sesión aprenderemos el puente secreto que une a las potencias con las raíces y cómo dominar las operaciones con radicales de forma sencilla y precisa.

> [!info] 🌍 Relevancia y aplicaciones
> Entender los exponentes fraccionarios y las raíces nos permite transformar expresiones complejas en modelos manejables para calcular dimensiones y crecimientos en el mundo real:
> - 💵 **Finanzas:** Cálculo de intereses compuestos en periodos fraccionados (como meses o días) usando potencias.
> - 🏗️ **Arquitectura:** Determinación de dimensiones exactas a partir de áreas y volúmenes simplificados.
> - 📊 **Crecimiento:** Uso de raíces en fórmulas de propagación de datos en escalas biológicas o estadísticas.

---

## Conceptos Clave

> [!note] Definición: Exponente Fraccionario
> Una potencia con exponente fraccionario es simplemente otra forma de escribir una raíz. La regla de oro es:
> $$a^{m/n} = \sqrt[n]{a^m}$$
> Donde el **denominador ($n$)** de la fracción se convierte en el **índice** de la raíz (el que manda en la "casa"), y el **numerador ($m$)** se mantiene como el **exponente** del radicando.

> [!warning] ¡Cuidado con los signos! (Raíz Principal)
> Existe un peligro cuando el número de adentro es negativo y el índice es **par**. Nunca canceles el índice con el exponente directamente en estos casos:
> - ❌ **Incorrecto:** $\sqrt[2]{(-3)^2} = -3$
> - ✅ **Correcto:** $\sqrt[2]{(-3)^2} = |-3| = 3$
> 
> **¿Por qué?** Porque estamos buscando la **Raíz Cuadrada Principal**, la cual por definición siempre debe ser positiva. 
> - Si el índice es **par**, el resultado es el valor absoluto (siempre positivo).
> - Si el índice es **impar**, el resultado conserva su signo original (ej. $\sqrt[3]{(-2)^3} = -2$).

> [!tip] Truco Mnemotécnico
> Para que no se te olvide nunca la posición: **"El que está abajo en la fracción (denominador) entra a la casa como el índice de la raíz"**. 
> Visualízalo así: $a^{m/\mathbf{n}} = \sqrt[\mathbf{n}]{a^m}$

---

## Procedimiento: Simplificación y Suma de Radicales

Para sumar raíces que parecen diferentes, primero debemos "limpiar la casa" siguiendo estos pasos:

```text
PASO 1 → Hallar los factores primos del radicando (descomposición numérica).
PASO 2 → Agrupar los factores según el índice de la raíz. 
         (Si es raíz cuadrada, busca parejas; si es raíz cúbica, busca tríos).
PASO 3 → Extraer los factores que completaron el grupo hacia afuera de la raíz.
PASO 4 → Sumar o restar solo los "términos semejantes": aquellos que tienen 
         exactamente el mismo índice y el mismo radicando.
```

---

## ¡Aprendamos con ejemplos!

> [!example] Ejemplo 1: Conversión básica
> - Convertir $5^{2/3}$ a raíz: Aplicando la regla, el $3$ pasa a ser el índice: $\sqrt[3]{5^2} = \sqrt[3]{25}$.
> - Calcular $8^{1/3}$: Esto es $\sqrt[3]{8}$. Como $2 \times 2 \times 2 = 8$, el resultado es $2$.

> [!example] Ejemplo 2: El efecto de los signos y paridad
> - **Índice impar:** $\sqrt[3]{(-2)^3}$. Al ser impar, la operación mantiene el signo: $-2$.
> - **Índice par:** $\sqrt[2]{(-7)^2}$. Al ser par, buscamos la raíz principal: $|-7| = 7$. (Recuerda que $(-7)^2 = 49$, y la raíz de $49$ es $7$).

> [!example] Ejemplo 3: Simplificación paso a paso
> Resolver: $\sqrt{50} + \sqrt{72} - 5\sqrt{2}$
> 1. **Simplificar $\sqrt{50}$**: $50 = 5^2 \cdot 2$. Sale el $5$ de la casa: $5\sqrt{2}$.
> 2. **Simplificar $\sqrt{72}$**: $72 = 2^2 \cdot 3^2 \cdot 2$. Salen el $2$ y el $3$ multiplicándose: $(2 \cdot 3)\sqrt{2} = 6\sqrt{2}$.
> 3. **Operar**: $5\sqrt{2} + 6\sqrt{2} - 5\sqrt{2} = (5 + 6 - 5)\sqrt{2} = 6\sqrt{2}$.

> [!example] Ejemplo 4: Aplicación en USD
> Un terreno cuadrado tiene un área de $9/4$ de un presupuesto en dólares. Para hallar la medida del lado ($L$), extraemos la raíz cuadrada de la fracción:
> $L = \sqrt{\frac{9}{4}} = \frac{\sqrt{9}}{\sqrt{4}} = \frac{3}{2}$ 
> Resultado final: **1.50 USD**.

---

> [!abstract] 📝 ¡A practicar lo aprendido!
> 
> **Nivel Verde (Fácil)**
> 1. Convierte a raíz: $4^{1/2}$
> 2. Convierte a raíz: $27^{1/3}$
> 3. Calcula el valor de: $16^{1/2}$
> 4. Convierte a raíz: $x^{3/5}$
>
> **Nivel Amarillo (Medio)**
> 1. Simplifica y suma: $\sqrt{12} + \sqrt{27}$
> 2. Resuelve: $\sqrt{20} - \sqrt{5}$
> 3. Simplifica: $\sqrt[3]{24}$
> 4. Resuelve: $3\sqrt{2} + 5\sqrt{2} - \sqrt{2}$
>
> **Nivel Rojo (Avanzado)**
> 1. El costo de una cerca es el resultado de $\sqrt{2500} \times \sqrt[3]{8}$ dólares. ¿Cuál es el precio final?
> 2. Resuelve simplificando: $\sqrt{48} + \sqrt{75} - 2\sqrt{3}$
> 3. Halla el valor exacto de: $\sqrt[4]{(-10)^4}$
> 4. Un presupuesto final se define como $\sqrt{\frac{25}{100}} + \frac{1}{2}$. Exprésalo como un número decimal.

---

> [!success] Solucionario para revisión
> **Verde:** 1) $\sqrt{4} = 2$; 2) $\sqrt[3]{27} = 3$; 3) $4$; 4) $\sqrt[5]{x^3}$
> **Amarillo:** 1) $5\sqrt{3}$; 2) $\sqrt{5}$; 3) $2\sqrt[3]{3}$; 4) $7\sqrt{2}$
> **Rojo:** 1) $50 \times 2 = 100.00$ USD; 2) $7\sqrt{3}$; 3) $10$ (por ser raíz principal); 4) $0.5 + 0.5 = 1.0$

---

> [!question] Mini-Prueba de Autoevaluación
> 1. **Teórica:** ¿Por qué $\sqrt[4]{(-5)^4}$ no es $-5$? Explica usando el concepto de Raíz Principal.
> 2. **Práctica:** ¿Cuánto es $3\sqrt{2} + 5\sqrt{2}$?
> 3. **Aplicación:** Si una inversión de 100 USD crece según $100 \times 4^{1/2}$, ¿cuánto dinero tienes al final?

---

> [!tip] 💡 En la próxima clase
> Ahora que ya sabemos sumar y simplificar, veremos cómo eliminar raíces del denominador mediante la **racionalización**. ¡Se pondrá muy interesante!

[[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | [[Clase 03|Clase 03 ➡]]