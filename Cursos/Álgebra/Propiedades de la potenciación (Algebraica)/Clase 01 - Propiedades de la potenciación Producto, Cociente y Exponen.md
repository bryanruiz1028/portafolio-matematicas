# Clase 01 — Propiedades de la potenciación: Producto, Cociente y Exponente Cero

#algebra #productofpowers

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 4

> [!info] 🧭 Navegación
> - 🔙 Anterior: [[00 - Índice del curso]]
> - 🔝 Inicio: [[01 - Propiedades Básicas]]
> - 🔜 Siguiente: [[02 - Exponentes Negativos y Simplificación]]

---

## 2. Introducción y Relevancia

> [!info] 🌍 Relevancia y aplicaciones
> ¡Hola! Soy tu profesor de matemáticas y hoy vamos a descubrir que las potencias no son solo números pequeños arriba de otros; son herramientas poderosas para simplificar tu vida. Dominar estas reglas te permitirá resolver problemas gigantescos en segundos. ¡Ánimo, tú puedes!
> 
> - **💵 Aplicación con $USD:** El interés compuesto. Si ahorras $10^3$ USD y tu dinero se duplica cada año, usarás potencias para calcular tu riqueza futura sin multiplicar uno por uno.
> - **🏗️ Aplicación práctica:** En ingeniería, para calcular el área de un terreno cuadrado ($L^2$) o el volumen de un contenedor ($L^3$).
> - **📊 Situación cotidiana:** La propagación de bacterias. Una sola bacteria dividiéndose puede convertirse en $2^{10}$ en pocas horas. ¡Entender el exponente es entender el crecimiento!

---

## 3. Conceptos Clave (Definiciones y Reglas)

> [!note] 📌 ¿Qué son estas propiedades?
> - **Producto de potencias de igual base:** Al multiplicar potencias con la misma base, mantienes la base y **sumas** los exponentes ($a^m \cdot a^n = a^{m+n}$).
> - **Cociente de potencias de igual base:** Al dividir, mantienes la base y **restas** los exponentes: el de arriba menos el de abajo ($a^m / a^n = a^{m-n}$).
> - **Exponente Cero:** Cualquier base (excepto el 0) elevada a la 0 es igual a **1** ($a^0 = 1$). 

> [!tip] 🔍 La "Prueba Visual" (¿Por qué restamos?)
> No te lo aprendas de memoria, ¡entiéndelo! Si tenemos $x^5 / x^3$, lo que realmente sucede es una simplificación:
> ```markdown
>   x · x · x · x · x      <-- x a la 5
> ---------------------
>       x · x · x          <-- x a la 3
> ```
> Al cancelar (simplificar) tres "x" de arriba con las tres de abajo, nos quedan solo 2. Por eso $5 - 3 = 2$. ¡Es magia matemática!

> [!danger] ⚠️ El Rigor Matemático: El caso de $0^0$
> Profe Alex nos recuerda: **$0^0$ NO es 1**. ¿Por qué? Porque la propiedad nace de dividir un número entre sí mismo (ej: $x^3 / x^3$). Como **no se puede dividir entre cero**, la expresión $0/0$ es una indeterminación. ¡No caigas en la trampa!

> [!warning] ⚠️ Errores comunes que debemos evitar
> 1. **Bases Distintas:** Si tienes $a^6 / b^3$, ¡detente! Las bases son diferentes, por lo tanto **no se puede aplicar la propiedad**. El resultado se deja igual.
> 2. **El Exponente Invisible:** Si ves una letra sola (ej: $m$), su exponente es **1**. ¡Muchos creen que es 0! Recuerda: $m = m^1$.
> 3. **Trampa de Signos:** En el cociente, si restas un negativo, se vuelve suma: $x^2 / x^{-5} \Rightarrow 2 - (-5) \Rightarrow 2 + 5 = 7$.

> [!tip] 💡 Truco para recordarlo
> Asocia el tamaño de la operación:
> - **Multiplicar es Crecer:** Por eso sumamos los exponentes.
> - **Dividir es Achicar:** Por eso restamos los exponentes.

---

## 4. Procedimiento Paso a Paso

¡Detecta el desafío y véncelo con estos pasos!

```markdown
1. ¿Bases iguales?: Verifica que la letra o número base sea idéntico. Si no lo es, no apliques la regla.
2. Identifica la operación: ¿Multiplicación (suma exponentes) o División (resta exponentes)?
3. ¡Cuidado con los signos!: Aplica ley de signos estrictamente, especialmente en las restas del cociente.
4. Elegancia final: Si el exponente es 0, escribe 1. Si es 1, puedes dejar la base sola.
```

---

## 5. Ejemplos Desarrollados

### Ejemplo 1 (Básico: Producto)
**Simplifica:** $m^7 \cdot m^6$
- **Paso:** Bases iguales ($m$), operamos sumando: $7 + 6$.
- **Resultado:** $m^{13}$. ¡Fácil!

### Ejemplo 2 (Signos: Cociente)
**Simplifica:** $\frac{x^2}{x^{-5}}$
- **Paso:** Es una división, restamos: $2 - (-5)$.
- **Transformación:** Menos por menos da más: $2 + 5$.
- **Resultado:** $x^7$.

### Ejemplo 3 (Avanzado: Múltiples bases)
**Simplifica:** $\frac{m^1 n^{-5}}{m^2 n^1}$
- **Para m:** $1 - 2 = -1$.
- **Para n:** $-5 - 1 = -6$.
- **Resultado:** $m^{-1} n^{-6}$.
- **Nota del Profe:** En la próxima clase haremos este resultado más "elegante" pasando los exponentes a positivo. ¡Por ahora, vas muy bien!

### Ejemplo 4 (Aplicación $USD)
**Problema:** Una deuda de $10^6$ USD se reparte entre $10^2$ personas. ¿Cuánto paga cada una?
- **Planteamiento:** $10^6 / 10^2 = 10^{6-2}$.
- **Resultado:** $10^4 = 10,000$ USD.

---

## 6. Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Fácil: ¡Para calentar motores!
> 1. $x^5 \cdot x^8$
> 2. $m^{10} \cdot m^1$ (¡Cuidado con el invisible!)
> 3. $\frac{a^9}{a^4}$
> 4. $\frac{y^7}{y^7}$

> [!abstract] 🟡 Nivel Medio: ¡Atento a los signos!
> 1. $x^5 \cdot x^{-2}$
> 2. $\frac{x^{-9}}{x^4}$
> 3. $b^8 \cdot b^{-8}$
> 4. $\frac{w^2}{w^{-3}}$

> [!abstract] 🔴 Nivel Avanzado: ¡Reto maestro!
> 1. $\frac{m^{-3} n^2}{m^{-2} n^5}$
> 2. $(x+y)^5 \cdot (x+y)^{-5}$
> 3. Un banco tiene $10^8$ USD y abre cuentas de $10^5$ USD cada una. ¿Cuántas cuentas hay?
> 4. $\frac{a^6}{b^3}$ (¡No caigas en la trampa!)

> [!success] ✅ Respuestas para calificar
> **Fácil:** 1. $x^{13}$ | 2. $m^{11}$ | 3. $a^5$ | 4. $1$.
> **Medio:** 1. $x^3$ | 2. $x^{-13}$ | 3. $1$ | 4. $w^5$.
> **Avanzado:** 1. $m^{-1} n^{-3}$ | 2. $1$ | 3. $10^3$ (1,000 cuentas) | 4. No se aplica propiedad (queda igual).

---

## 7. Autoevaluación (Mini-prueba)

> [!question] Pregunta 1
> **¿Por qué $a^0 = 1$?**
> *Respuesta:* Porque representa dividir algo entre sí mismo (ej. $a^3/a^3$). Al simplificar todos los términos, el resultado es la unidad (1).

> [!question] Pregunta 2
> **¿Cuál es el resultado de $\frac{x^2}{x^8}$?**
> A) $x^6$
> B) $x^{-6}$
> C) $x^{10}$
> *Respuesta Correcta:* **B**. Restamos $2 - 8 = -6$.

> [!question] Pregunta 3
> **Si tienes $10^3$ USD y lo multiplicas por $3^0$, ¿cuánto tienes?**
> A) $0$ USD
> B) $3,000$ USD
> C) $1,000$ USD
> *Respuesta Correcta:* **C**. Porque $3^0 = 1$. Multiplicar por 1 no cambia la cantidad inicial.

---

## 8. Cierre y Conexión

> [!tip] 💡 En la próxima clase
> ¿Notaste que algunos resultados quedaron con exponente negativo como $m^{-1}$? ¡No te asustes! En la siguiente clase aprenderemos la propiedad para "voltear" estos números y que tus resultados luzcan perfectos y profesionales. ¡Te espero!

> [!info] 🧭 Navegación
> - 🔙 Anterior: [[00 - Índice del curso]]
> - 🔝 Inicio: [[01 - Propiedades Básicas]]
> - 🔜 Siguiente: [[02 - Exponentes Negativos y Simplificación]]