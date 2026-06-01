# Clase 03 — Ley de Senos: Cálculo de Lados, Ángulos y Resolución de Triángulos
tags: #algebra #lawofsines
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 9

> [!info] 🧭 Navegación
> [[Clase 02 — Introducción a la Trigonometría]] | [[00 - Índice del curso]]

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> La Ley de Senos es una herramienta fundamental en la trigonometría que permite resolver triángulos que no son rectángulos (oblicuángulos). Su aplicación es vital en campos que requieren precisión sobre grandes distancias y formas irregulares donde no podemos aplicar el Teorema de Pitágoras directamente.
- 💵 Cálculo de costos de cercado basado en la longitud de un lado desconocido ($USD).
- 🏗️ Determinación de ángulos de soporte en estructuras triangulares.
- 📊 Localización de puntos geográficos mediante triangulación.

> [!note] 📌 ¿Qué es Law of Sines?
> Imagina que en un triángulo, cada ángulo tiene una "relación de armonía" con el lado que tiene justo enfrente. La Ley de Senos nos dice que esa relación es siempre proporcional: si un ángulo es grande, su lado opuesto también lo será, manteniendo siempre el mismo equilibrio. Para un estudiante de 12 años, es útil pensarlo como un sistema de parejas donde el ángulo y su lado opuesto siempre se mueven en sintonía.

### La Fórmula
Dependiendo de qué necesites encontrar, el "Profe Alex" recomienda usar la fórmula de dos maneras para facilitar el despeje y evitar errores:

1.  **Para buscar LADOS (Lados arriba):**
    $$\frac{a}{\sin(A)} = \frac{b}{\sin(B)} = \frac{c}{\sin(C)}$$
2.  **Para buscar ÁNGULOS (Senos arriba):**
    $$\frac{\sin(A)}{a} = \frac{\sin(B)}{b} = \frac{\sin(C)}{c}$$

> [!warning] ⚠️ Error común
> El error más frecuente es intentar emparejar un ángulo con un lado que está a su lado (adyacente). 
> **El truco del experto:** Dibuja físicamente una flecha que salga del ángulo y apunte al lado que tiene enfrente. Si tu flecha toca un lado, esa es la "pareja de matrimonio" correcta. Nunca uses los lados que forman el ángulo.

> [!tip] 💡 Truco para recordarlo
> Busca siempre "parejas completas". Una pareja completa es cuando conoces la letra mayúscula (ángulo) y su letra minúscula correspondiente (lado opuesto). Si tienes una pareja completa y al menos un dato de otra pareja, el problema está prácticamente resuelto.

## Procedimiento Paso a Paso

Pensemos en la fórmula como una caja de herramientas: para que el trabajo sea más fácil y no cometamos errores de álgebra, debemos elegir el "martillo" (la variante de la fórmula) adecuado según el "clavo" (la incógnita) que queramos golpear.

```text
1. Nombrar ángulos con letras mayúsculas (A, B, C) y sus lados opuestos con minúsculas (a, b, c).
2. Identificar la "pareja completa" (ej. ángulo A y lado a) y la "pareja incógnita" (ej. ángulo B y lado b).
3. Sustituir en la fórmula, colocando la incógnita en el numerador (arriba) para facilitar el despeje.
4. Despejar: pasar el denominador que acompaña a la incógnita a multiplicar al otro lado y resolver usando la calculadora en modo DEG (Degrees).
```

## Ejemplos Prácticos

> [!example] Ejemplo 1: Encontrar un lado (Video 2)
> **Datos:** Ángulo $C = 28^\circ$, Lado $c = 9m$, Ángulo $A = 100^\circ$. Hallar el lado $b$.
> 1. **Ángulo faltante:** Como los ángulos internos suman $180^\circ$, hallamos el Ángulo $B$: $180^\circ - 100^\circ - 28^\circ = 52^\circ$.
> 2. **Planteamiento:** Queremos el lado $b$, así que usamos la versión con lados arriba: $\frac{b}{\sin(52^\circ)} = \frac{9}{\sin(28^\circ)}$.
> 3. **Despeje:** $b = \frac{9 \cdot \sin(52^\circ)}{\sin(28^\circ)}$.
> 4. **Resultado:** $b \approx 15.1m$.

> [!example] Ejemplo 2: Encontrar un ángulo (Video 3)
> **Datos:** Ángulo $A = 42^\circ$, Lado $a = 40m$, Lado $c = 52m$. Hallar el ángulo $C$.
> 1. **Planteamiento:** Queremos un ángulo, usamos senos arriba: $\frac{\sin(C)}{52} = \frac{\sin(42^\circ)}{40}$.
> 2. **Despeje:** $\sin(C) = \frac{52 \cdot \sin(42^\circ)}{40}$.
> 3. **Analogía del Arcoseno:** Para dejar solo al ángulo, usamos la función inversa $\sin^{-1}$. Imagina que es como la raíz cuadrada ($\sqrt{x}$) que cancela al cuadrado ($x^2$); aquí el arcoseno "cancela" al seno para liberar el valor de $C$.
> 4. **Resultado:** $C = \sin^{-1}(0.8698) \approx 60^\circ 26' 36.64''$.

> [!example] Ejemplo 3: Resolver el triángulo completo (Video 6)
> **Datos:** Ángulo $A = 65^\circ$, Ángulo $B = 30^\circ$, Lado $c = 13cm$.
> 1. **Ángulo C:** $180^\circ - 65^\circ - 30^\circ = 85^\circ$. (Ahora la pareja $C/c$ está completa).
> 2. **Lado a:** $\frac{a}{\sin(65^\circ)} = \frac{13}{\sin(85^\circ)} \implies a \approx 11.82cm$.
> 3. **Lado b:** $\frac{b}{\sin(30^\circ)} = \frac{13}{\sin(85^\circ)} \implies b \approx 6.52cm$.

> [!example] Ejemplo 4: Aplicación de costos ($USD)
> Una empresa debe instalar un cable de fibra óptica que corresponde al lado $b$ de un terreno triangular. Según el **Ejemplo 1**, la longitud de dicho lado es de $15.1m$. Si el costo de instalación y material es de $50 USD por metro:
> - **Cálculo:** $15.1m \cdot 50 USD/m = 755 USD$.
> - **Costo Total:** $755 USD$.

## Ejercicios para el Estudiante

**Nivel Verde (Fácil) — Búsqueda de lados:**
1. $A = 40^\circ, a = 12m, B = 70^\circ$. Hallar $b$.
2. $C = 110^\circ, c = 25cm, A = 30^\circ$. Hallar $a$.
3. $B = 45^\circ, b = 10m, C = 60^\circ$. Hallar $c$.
4. $A = 20^\circ, a = 5km, B = 100^\circ$. Hallar $b$.

**Nivel Amarillo (Medio) — Búsqueda de ángulos:**
5. $a = 15m, A = 35^\circ, b = 20m$. Hallar $B$.
6. $c = 10cm, C = 50^\circ, a = 8cm$. Hallar $A$.
7. $b = 40m, B = 100^\circ, c = 30m$. Hallar $C$.
8. $a = 12km, A = 42^\circ, b = 15km$. Hallar $B$.

**Nivel Rojo (Avanzado) — Resolución Completa y Costos:**
9. Triángulo con $A = 50^\circ, B = 60^\circ, c = 20m$. Resuelve el triángulo y calcula el costo de cercar el **perímetro total** (la suma de los tres lados) si cada metro cuesta $50 USD.
10. Triángulo con $C = 80^\circ, B = 40^\circ, a = 15m$. Resuelve el triángulo y calcula el costo del perímetro total a $50 USD/m.
11. Triángulo con $A = 35^\circ, C = 105^\circ, b = 12cm$. Resuelve el triángulo y calcula el costo del perímetro total a $50 USD/cm.
12. Triángulo con $B = 45^\circ, A = 75^\circ, c = 30m$. Resuelve el triángulo y calcula el costo del perímetro total a $50 USD/m.

> [!success] ✅ Respuestas (para el docente)
> 1. $17.54m$ | 2. $13.30cm$ | 3. $12.25m$ | 4. $14.39km$
> 5. $49^\circ 53' 15''$ | 6. $37^\circ 45' 47''$ | 7. $47^\circ 35' 12''$ | 8. $56^\circ 46' 57''$
> 9. $C=70^\circ, a=16.30m, b=18.43m$. Perímetro: $54.73m$. Costo: $2736.50 USD$.
> 10. $A=60^\circ, b=11.13m, c=17.05m$. Perímetro: $43.18m$. Costo: $2159 USD$.
> 11. $B=40^\circ, a=10.71cm, c=18.03cm$. Perímetro: $40.74cm$. Costo: $2037 USD$.
> 12. $C=60^\circ, a=33.46m, b=24.49m$. Perímetro: $87.95m$. Costo: $4397.50 USD$.

## Autoevaluación y Cierre

> [!question] Pregunta Conceptual
> ¿Qué condición es indispensable para poder aplicar la Ley de Senos en un triángulo?
> A) Conocer los tres lados del triángulo.
> B) Tener al menos una "pareja completa" (un ángulo y su lado opuesto conocido).
> C) Que el triángulo tenga obligatoriamente un ángulo de 90°.
> *Respuesta: B*

> [!question] Pregunta Procedimental
> Para despejar un ángulo incógnita, ¿qué paso es necesario después de calcular la proporción?
> A) Elevar el resultado al cuadrado.
> B) Multiplicar por el seno del ángulo conocido.
> C) Aplicar la función inversa $\sin^{-1}$ (arcoseno).
> *Respuesta: C*

> [!question] Pregunta de Aplicación ($USD)
> Si tras resolver un triángulo descubres que el lado a cercar mide 20 metros y el presupuesto es de $50 USD por metro, ¿cuál es el costo total de ese lado?
> A) $1000 USD
> B) $500 USD
> C) $2000 USD
> *Respuesta: A*

> [!tip] 💡 En la próxima clase
> ¿Qué pasa cuando no tenemos ninguna "pareja completa"? Por ejemplo, si solo conocemos los tres lados o dos lados y el ángulo que los une. En ese caso, la Ley de Senos no puede ayudarnos y debemos recurrir a su "hermana": la **Ley del Coseno**.

> [!info] 🧭 Navegación
> [[Clase 02 — Introducción a la Trigonometría]] | [[00 - Índice del curso]]