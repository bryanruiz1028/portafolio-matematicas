# Clase 03 — Operaciones Combinadas: Jerarquía de Operaciones

**Tags:** `#algebra #combinedoperati`
**Curso:** `[[00 - Índice del curso]] | Bloque 1 | Lección 3 de 4`

> [!info] 🧭 Navegación
> - **Anterior:** [[Clase 02 — Multiplicación y División de Enteros]]
> - **Siguiente:** [[Clase 04 — Uso avanzado de Signos de Agrupación]]

---

## 1. Relevancia y aplicaciones

> [!info] 🌍 Relevancia y aplicaciones
> ¿Alguna vez te has preguntado por qué una calculadora científica da un resultado distinto a una calculadora básica? La clave está en la jerarquía. Sin un orden estándar, los cálculos que sostienen nuestra tecnología y economía serían un caos total.
> 
> - **💵 Aplicación USD:** Si compras 5 artículos de $3 USD cada uno y uno de $5 USD, y pagas con un billete de $100 USD, la operación correcta es $100 - (5 \times 3 + 5)$. Sin jerarquía, ¡podrías perder mucho dinero!
> - **🏗️ Aplicación práctica:** En arquitectura, al calcular los metros cuadrados de una casa, los ingenieros deben multiplicar las dimensiones de cada habitación antes de sumarlas para obtener el total.
> - **📊 Situación cotidiana:** Al repartir los gastos de una cena entre amigos, primero sumamos el costo de los platos y las bebidas, y al final dividimos entre el número de personas.

---

## 2. Concepto clave

> [!note] 📌 ¿Qué es Operaciones Combinadas?
> ¡Imagina que las matemáticas son una receta de cocina! Si metes el pastel al horno antes de batir los huevos, el resultado será un desastre. Las operaciones combinadas son expresiones donde aparecen sumas, restas, multiplicaciones y más, todas juntas. Para resolverlas con éxito, usamos la **Jerarquía de Operaciones**: el manual de instrucciones que nos dice qué paso va primero.

> [!warning] ⚠️ Error común
> ¡Cuidado con la **Potenciación**! Un error muy frecuente es pensar que $5^2$ es $5 \times 2 = 10$. 
> Recuerda: el **exponente** (el número pequeño) te dice cuántas veces multiplicar la **base** por sí misma. Lo correcto es $5^2 = 5 \times 5 = 25$. 
> Además, nunca olvides la regla de **Izquierda a Derecha**: si tienes multiplicaciones y divisiones juntas, resuélvelas en el orden en que aparecen al leer.

> [!tip] 💡 Truco para recordarlo: El Escalafón P-PR-MD-SR
> Para que nunca se te olvide el orden de prioridad, memoriza esta escalera de poder:
> 1. **P**aréntesis (y otros signos de agrupación).
> 2. **P**otenciación y **R**adicación (Raíces).
> 3. **M**ultiplicación y **D**ivisión.
> 4. **S**uma y **R**esta.

---

## 3. Procedimiento paso a paso

¡Toma nota! Este es el orden estricto que utiliza el **Profe Alex** en sus lecciones para que el resultado siempre sea perfecto:

```text
PASO 1 → Resolver operaciones dentro de los paréntesis.
PASO 2 → Calcular Potenciación y Radicación.
PASO 3 → Ejecutar multiplicaciones y divisiones (de izquierda a derecha).
PASO 4 → Realizar sumas y restas finales (de izquierda a derecha).
```

> [!info] Dato Curioso
> El símbolo $\div$ para la división se utiliza mucho en países como España. En otros lugares es más común ver los dos puntos ($:$) o la barra lateral ($/$). ¡Todos significan lo mismo!

---

## 4. Ejemplos desarrollados

> [!example] Ejemplo 1: Básico (Paréntesis y división)
> **Ejercicio:** $14 \div (3 + 4) + 9 - 10 \div 2$
> 1. **Paréntesis:** $(3 + 4) = 7$. Ahora tenemos: $14 \div 7 + 9 - 10 \div 2$.
> 2. **Divisiones:** 
>    - $14 \div 7 = 2$
>    - $10 \div 2 = 5$
>    - La expresión se reduce a: $2 + 9 - 5$.
> 3. **Suma/Resta:** $11 - 5 = 6$.
> **Resultado: 6**

> [!example] Ejemplo 2: Con signos (Ley de los signos)
> **Ejercicio:** $3 \times 8 + 63 \div 9 - 8 \div 2 + 7$
> 1. **Multiplicaciones y Divisiones:**
>    - $3 \times 8 = 24$
>    - $63 \div 9 = 7$
>    - **Ojo aquí:** $-8 \div 2$. Aplicamos la **Ley de los signos**: menos entre más da menos, por lo que es $-4$.
>    - Queda: $24 + 7 - 4 + 7$.
> 2. **Suma/Resta:** $31 - 4 + 7 = 34$.
> **Resultado: 34**

> [!example] Ejemplo 3: Avanzado (Radicación y Potenciación)
> **Ejercicio:** $10 \times \sqrt{4} \times \sqrt[3]{8} - (25 - 7) + (20 \div 4)$
> 1. **Paréntesis:** $(25 - 7) = 18$ y $(20 \div 4) = 5$.
> 2. **Raíces:** $\sqrt{4} = 2$ y $\sqrt[3]{8} = 2$.
> 3. **Multiplicación:** Resolvemos la cadena $10 \times 2 \times 2 = 40$.
> 4. **Suma/Resta:** $40 - 18 + 5 = 27$.
> **Resultado: 27**

> [!example] Ejemplo 4: Aplicación USD (Nivel Experto)
> **Situación:** Vas a la tienda y compras: 5 chocolates de $3 USD cada uno, $3^2$ bolsas de papas de $5 USD cada una, y 3 refrescos de $2 USD. Al final, usas un cupón de descuento de $6 USD.
> **Operación:** $5 \times 3 + 3^2 \times 5 + 3 \times 2 - 6$
> 1. **Potenciación:** $3^2 = 9$. (Expresión: $5 \times 3 + 9 \times 5 + 3 \times 2 - 6$).
> 2. **Multiplicaciones:** $15 + 45 + 6 - 6$.
> 3. **Suma/Resta:** $60 + 6 - 6 = 60$.
> **Resultado: $60 USD**

---

## 5. Práctica independiente

¡Es tu turno de brillar! Aplica lo aprendido con estos ejercicios.

> [!abstract] 📝 Lista de Ejercicios
> **🟢 Nivel Fácil (Calentamiento)**
> 1. $10 + 5 \times 2$
> 2. $20 - 4 \times 3$
> 3. $6 \times 3 + 4 \times 2$
> 4. $15 - 10 \div 5$
> 
> **🟡 Nivel Medio (Subiendo el nivel)**
> 5. $30 \div (3 + 2) + 8$
> 6. $(12 + 8) \div 4 - 1$
> 7. $5 \times 4 + 18 \div 3$
> 8. $2 \times (10 - 4) \div 3$
> 
> **🔴 Nivel Avanzado (Desafíos USD)**
> 9. Tienes $50 USD, compras 2 paquetes de $12 USD cada uno y recibes un bono de regalo de $5 USD. ¿Cuánto dinero tienes al final?
> 10. Pagas con un billete de $100 USD por 3 libros de $15 USD y 2 cuadernos de $10 USD. ¿Cuánto recibes de cambio?
> 11. Un grupo de 4 amigos gana $8 USD cada uno. Luego, como grupo, encuentran un billete de $10 USD en la calle, pero deben pagar una deuda grupal de $12 USD. ¿Cuánto dinero tienen en total ahora?
> 12. Tienes $80 USD. Compras un videojuego de $40 USD. De lo que te sobra, decides gastar exactamente la mitad en una pizza para celebrar. ¿Cuánto dinero te queda finalmente?

> [!success] ✅ Clave de Respuestas
> 1) **20** | 2) **8** | 3) **26** | 4) **13** | 5) **14** | 6) **4** | 7) **26** | 8) **4** | 9) **$31** | 10) **$35** | 11) **$30** | 12) **$20**

---

## 6. Autoevaluación

> [!question] Pregunta 1: Teoría de Jerarquía
> Si en una operación encuentras una suma y una multiplicación sin paréntesis, ¿cuál debes atacar primero?
> > [!success] Respuesta
> > ¡La **multiplicación**! Según el escalafón, las sumas y restas siempre esperan hasta el final.

> [!question] Pregunta 2: El poder del exponente
> ¿Cuál es el resultado de resolver $3 + 2^3$? Explica tu paso.
> > [!success] Respuesta
> > El resultado es **11**. Primero resolvemos la **Potenciación**: $2^3 = 2 \times 2 \times 2 = 8$. Luego sumamos: $3 + 8 = 11$. ¡Recuerda que $2^3$ no es $2 \times 3$!

> [!question] Pregunta 3: Lógica financiera aplicada
> Juan tiene $40 USD. Compra 3 camisas de $10 USD cada una. Si su madre, al ver su ahorro, decide regalarle el doble de lo que le sobró, ¿cuánto dinero tiene Juan al final?
> > [!success] Respuesta
> > Tiene **$20 USD**. 
> > **Paso 1 (Paréntesis/Sobrante):** $40 - (3 \times 10) = 40 - 30 = 10$.
> > **Paso 2 (Multiplicación/Regalo):** El doble de lo que sobró es $10 \times 2 = 20$.

---

## 7. Cierre y Navegación

> [!tip] 💡 En la próxima clase
> ¡Has dominado las reglas básicas! En la siguiente sesión subiremos la apuesta aprendiendo el **uso avanzado de signos de agrupación**, donde conocerás a los primos de los paréntesis: los corchetes y las llaves.

> [!info] 🧭 Navegación
> - **Anterior:** [[Clase 02 — Multiplicación y División de Enteros]]
> - **Siguiente:** [[Clase 04 — Uso avanzado de Signos de Agrupación]]