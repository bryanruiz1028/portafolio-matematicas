# Clase 01 — La Circunferencia: Conceptos Básicos, Ecuación Canónica y General
tags: #algebra #conceptosbasicos #geometria_analitica
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 2

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]

## 1. ¿Por qué es importante esta clase?
La circunferencia no es solo una "línea redonda"; es la base de la precisión en el mundo físico. En ingeniería, su dominio permite que los engranajes de un motor encajen perfectamente o que la trayectoria de un satélite sea estable.

*   💵 **Aplicación $USD:** En la acuñación de monedas (minting), el diámetro debe ser exacto. Si la ecuación de diseño falla por micras, las máquinas contadoras rechazarán la moneda, causando pérdidas millonarias en logística y materiales.
*   🏗️ **Aplicación práctica:** Los arquitectos la utilizan para diseñar arcos de medio punto y cúpulas que distribuyen el peso de forma equitativa.
*   📊 **Situación cotidiana:** Es el principio detrás del funcionamiento de un radar o la simple pero perfecta rotación de las manecillas de un reloj.

## 2. Concepto clave
> [!note] 📌 ¿Qué es la Ecuación de la CIRCUNFERENCIA?
> Según la definición geométrica, la circunferencia es el lugar geométrico de todos los puntos en un plano que están a la misma distancia de un punto fijo llamado **Centro**.
> 
> 💡 **Analogía del Compás:** Imagina que la aguja de tu compás es el **Centro $(h, k)$** y la abertura (la distancia hasta la punta del lápiz) es el **Radio ($r$)**. No importa cuánto gires el compás, esa distancia nunca cambia; por eso, todos los puntos del borde cumplen la misma regla.

### Checklist: ¿Es realmente una circunferencia?
Para que una ecuación represente una circunferencia, debe cumplir tres condiciones de "pureza":
1.  **Variables al cuadrado:** Tanto $x$ como $y$ deben estar elevadas a la potencia 2.
2.  **Coeficientes iguales:** Los números que acompañan a $x^2$ y $y^2$ deben ser idénticos (ej. $3x^2 + 3y^2$). Si son diferentes, la figura se "deforma".
3.  **Signo positivo:** El signo entre $x^2$ y $y^2$ siempre debe ser una suma (+).

> [!warning] ⚠️ El Error de los Signos (El "Porqué" Matemático)
> La fórmula canónica es $(x - h)^2 + (y - k)^2 = r^2$. 
> El signo **menos** es parte de la estructura. Por eso, al sustituir un valor negativo como $h = -2$, ocurre un choque de signos: $x - (-2)$, que se convierte en **$(x + 2)$**.
> - ❌ **Incorrecto:** Centro $(2, -3) \rightarrow (x-2)^2 + (y-3)^2$
> - ✅ **Correcto:** Centro $(2, -3) \rightarrow (x-2)^2 + (y+3)^2$

> [!tip] 💡 Regla de oro
> - **Inversión total:** Si el número entra a la ecuación, cambia de signo. Si sale de la ecuación para ser coordenada, cambia de signo.
> - **Radio al cuadrado:** El número a la derecha del igual **no es el radio**, es su cuadrado ($r^2$). ¡No olvides sacar la raíz si quieres saber la medida real!

## 3. Procedimiento paso a paso
Para construir la ecuación conociendo el centro $C(h, k)$ y el radio $r$:

```text
1. Identificar valores: Extrae h, k y r del problema.
2. Sustituir: Escribe la fórmula (x - h)² + (y - k)² = r² con tus datos.
3. Simplificar signos: Aplica ley de signos ( - por - = + ).
4. Calcular r²: Resuelve la potencia del radio para obtener el valor final.
```

## 4. Ejemplos de aplicación

> [!example] Ejemplo 1: Caso Básico
> **Hallar la ecuación con Centro $(2, 1)$ y Radio $3$.**
> - $h = 2$, $k = 1$, $r = 3$.
> - Sustitución: $(x - 2)^2 + (y - 1)^2 = 3^2$
> - **Resultado:** $(x - 2)^2 + (y - 1)^2 = 9$.

> [!example] Ejemplo 2: El poder de la raíz
> **Hallar la ecuación con Centro $(-2, 5)$ y Radio $\sqrt{10}$.**
> - Al sustituir: $(x - (-2))^2 + (y - 5)^2 = (\sqrt{10})^2$
> - **Resultado:** $(x + 2)^2 + (y - 5)^2 = 10$.
> - *Nota:* El cuadrado y la raíz son enemigos naturales; se cancelan entre sí.

> [!example] Ejemplo 3: El reto del Diámetro (Fidelity Source)
> **Extremos del diámetro: $A(-3, -2)$ y $B(5, 0)$. Hallar la ecuación.**
> 1. **Punto Medio (Centro):** Aplicamos $x_m = \frac{x_1 + x_2}{2}$ y $y_m = \frac{y_1 + y_2}{2}$.
>    $h = \frac{-3+5}{2} = 1$; $k = \frac{-2+0}{2} = -1 \rightarrow \mathbf{C(1, -1)}$.
> 2. **Radio (Distancia):** Calculamos de $C(1, -1)$ a $B(5, 0)$:
>    $r = \sqrt{(5-1)^2 + (0 - (-1))^2} = \sqrt{4^2 + 1^2} = \sqrt{17}$.
> 3. **Ecuación:** $(x - 1)^2 + (y + 1)^2 = (\sqrt{17})^2 \rightarrow \mathbf{(x - 1)^2 + (y + 1)^2 = 17}$.

> [!example] Ejemplo 4: Control de Calidad $USD (STEM)
> **Problema:** En una fábrica, una moneda se diseña con centro $(0,0)$ y diámetro $4$. 
> 1. **Ecuación:** Si diámetro es $4$, $r = 2$. Ecuación: $x^2 + y^2 = 4$.
> 2. **Control de Calidad:** Un sensor detecta una imperfección en la coordenada $(1, \sqrt{3})$. ¿Está este punto en el borde de la moneda?
>    **Verificación:** $1^2 + (\sqrt{3})^2 = 1 + 3 = 4$. 
>    *¡Sí! Como el resultado es igual a $r^2$, el punto es correcto.*

## 5. Ejercicios para el estudiante

> [!abstract] Nivel Fácil: Identificación rápida
> Obtén el Centro y Radio:
> 1. $(x - 3)^2 + (y + 2)^2 = 25$
> 2. $(x + 1)^2 + (y - 7)^2 = 36$
> 3. $x^2 + (y - 2)^2 = 49$
> 4. $(x + 5)^2 + y^2 = 100$

> [!abstract] Nivel Medio: Fracciones y Radicales
> Escribe la ecuación canónica:
> 1. $C(1/2, -3), r = 4$
> 2. $C(-2, 1/2), r = 3/2$
> 3. $C(0, -4), r = \sqrt{10}$
> 4. $C(3, 0), r = \sqrt{5}$

> [!abstract] Nivel Avanzado: Ingeniería y Costos ($USD)
> 1. Extremos de diámetro $A(-2, 0)$ y $B(4, 0)$. Hallar la ecuación.
> 2. Extremos de diámetro $A(0, 5)$ y $B(0, -5)$. Hallar la ecuación.
> 3. Una pieza circular de precisión tiene extremos de diámetro en $(-1, -1)$ y $(1, 1)$. El recubrimiento de oro del borde cuesta **$\$5.00$ USD por unidad de longitud (perímetro)**. Calcula la ecuación y el costo total del borde (Usa $\pi \approx 3.14$).
> 4. Determina la ecuación de un engranaje cuyo diámetro va de $(3, 2)$ a $(3, 8)$.

> [!success] Solucionario Compacto
> **Fácil:** 1. $C(3, -2), r=5$ | 2. $C(-1, 7), r=6$ | 3. $C(0, 2), r=7$ | 4. $C(-5, 0), r=10$.
> **Medio:** 1. $(x - 1/2)^2 + (y + 3)^2 = 16$ | 2. $(x + 2)^2 + (y - 1/2)^2 = 9/4$ | 3. $x^2 + (y + 4)^2 = 10$ | 4. $(x - 3)^2 + y^2 = 5$.
> **Avanzado:** 1. $(x - 1)^2 + y^2 = 9$ | 2. $x^2 + y^2 = 25$ | 3. **Ecuación:** $x^2 + y^2 = 2$ ($r = \sqrt{2} \approx 1.41$). **Costo:** Perímetro ($2 \cdot \pi \cdot 1.41$) $\approx 8.85$ unidades. Costo total $\approx \$44.25$ USD. | 4. $(x - 3)^2 + (y - 5)^2 = 9$.

## 6. Mini-prueba de autoevaluación

> [!question] Pregunta 1
> Si recibes la ecuación $4x^2 + 4y^2 = 16$, ¿qué debes hacer para identificar el radio correctamente?
> *Respuesta:* Dividir toda la ecuación entre 4 para que los coeficientes de $x^2$ y $y^2$ sean 1. Quedaría $x^2 + y^2 = 4$, por lo tanto $r = 2$.

> [!question] Pregunta 2
> ¿Cuál es el radio de la circunferencia $(x + 10)^2 + (y - 8)^2 = 20$?
> *Respuesta:* $r = \sqrt{20}$. Simplificado es $2\sqrt{5}$ (aprox. $4.47$).

> [!question] Pregunta 3: Aplicación Económica
> Una pieza circular tiene un radio de $5$ cm. Si el costo de producción es de $\$1.50$ USD por cada cm² de área, ¿cuál es el costo de la pieza? (Área $= \pi \cdot r^2$).
> *Respuesta:* Área $= 25\pi \approx 78.5$ cm². Costo: $78.5 \cdot 1.50 = \$117.75$ USD.

## 7. Hacia la Ecuación General
> [!tip] 💡 En la próxima clase
> Veremos cómo transformar la forma canónica en la **Ecuación General**:
> $$x^2 + y^2 + Dx + Ey + F = 0$$
> 
> Esta forma surge al desarrollar los binomios al cuadrado. Para ir preparándote, aquí tienes las "llaves" de conversión:
> - $D = -2h$
> - $E = -2k$
> - $F = h^2 + k^2 - r^2$
> 
> ¡Dominar estas fórmulas te permitirá saltar de una forma a otra como un experto!

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]