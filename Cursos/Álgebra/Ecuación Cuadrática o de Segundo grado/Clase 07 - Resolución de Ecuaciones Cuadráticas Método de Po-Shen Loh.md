# Clase 07 — Resolución de Ecuaciones Cuadráticas: Método de Po-Shen Loh

**Tags:** #Álgebra #Matemáticas #MetodologíaDigital #MétodoPoShenLoh
**Curso:** Curso de Álgebra Intermedia

```ad-info
title: 🧭 Navegación
- **Anterior:** [[Clase 06 — Introducción a las Ecuaciones Cuadráticas]]
- **Siguiente:** [[Clase 08 — Ecuaciones Cuadráticas: Casos con Números Imaginarios]]
- **Índice:** [[Índice del Curso de Álgebra]]
```

---

```ad-info
title: 🌍 Relevancia y aplicaciones
Este método es revolucionario porque permite hallar las raíces de una ecuación cuadrática basándose en la lógica del "centro" y la simetría, eliminando por completo la necesidad de memorizar la tediosa fórmula general. ¡Es una herramienta de pensamiento lógico, no de repetición mecánica!

- **💵 Finanzas:** Permite optimizar el **punto de equilibrio** en modelos de negocio, determinando qué precios en $USD anulan las pérdidas y maximizan la eficiencia.
- **🏗️ Construcción:** Ideal para el cálculo de dimensiones en áreas de cimentación donde se busca un balance entre simetría y resistencia.
- **📊 Situación cotidiana:** Modelado preciso de la trayectoria parabólica de objetos, fundamental en física aplicada y deportes.
```

---

```ad-note
title: 📌 ¿Qué es el Método de Po-Shen Loh?
Es un enfoque intuitivo para resolver ecuaciones de la forma $x^2 + bx + c = 0$. Su gran ventaja es que se enfoca en el **centro (promedio)** de las dos soluciones posibles. 

Desde una perspectiva lógica, si sumamos las dos raíces de una cuadrática, el resultado es siempre $-b$. Por lo tanto, el punto medio o "centro" entre ellas siempre será la mitad de ese valor. Al encontrar este centro ($t$) y una distancia ($u$), las soluciones aparecen de forma natural por simetría.
```

```ad-warning
title: ⚠️ Requisito Indispensable
Para que este método funcione, el coeficiente $a$ (el número que acompaña a $x^2$) **debe ser igual a 1**. 
¿Por qué? Porque la lógica del promedio de las raíces depende de la estructura simplificada $x^2 + bx + c = 0$. Si $a \neq 1$, ¡no te preocupes! Solo debes dividir toda la ecuación por ese valor antes de comenzar.
```

```ad-tip
title: 💡 Truco para recordarlo
Simplemente graba esto en tu mente: **"El centro es la mitad del opuesto de b"**. 
Si $b = 10$, su opuesto es $-10$ y su centro es $-5$. ¡Así de simple!
```

---

### 📋 ¡Manos a la obra! El procedimiento paso a paso

Como especialista en metodologías, te presento esta "hoja de ruta" lógica para que no te pierdas en el camino:

1.  **Asegurar el Formato:** Identifica $a, b, c$. Verifica que $a = 1$.
2.  **Calcular el Centro ($t$):** Es el promedio de las raíces.
    $$t = -\frac{b}{2}$$
3.  **Plantear la Ecuación de Distancia ($u$):** Buscamos qué tan lejos del centro están las soluciones.
    $$t^2 - u^2 = c$$
4.  **Hallar las soluciones finales ($x$):**
    $$x = t \pm u$$

---

### 📝 Ejemplos Prácticos de Masterclass

```ad-example
title: Ejemplo 1: Caso Básico (Simetría Perfecta)
**Ecuación:** $x^2 + 2x - 3 = 0$
1. **Centro ($t$):** $t = -\frac{2}{2} = -1$
2. **Distancia ($u$):** 
   $$(-1)^2 - u^2 = -3$$
   $$1 - u^2 = -3 \implies u^2 = 4 \implies u = 2$$
3. **Soluciones:** $x = -1 \pm 2$
   - $x_1 = 1$
   - $x_2 = -3$
¡Excelente! Has encontrado los puntos de corte sin usar la fórmula general.
```

```ad-example
title: Ejemplo 2: Ajuste de Signos
**Ecuación:** $x^2 - 6x + 8 = 0$
1. **Centro ($t$):** $t = -\frac{(-6)}{2} = 3$
2. **Distancia ($u$):** 
   $$3^2 - u^2 = 8 \implies 9 - u^2 = 8 \implies u^2 = 1 \implies u = 1$$
3. **Soluciones:** $x = 3 \pm 1$
   - $x_1 = 4, x_2 = 2$
```

```ad-example
title: Ejemplo 3: El Poder del Método (Raíces No Exactas)
Este método brilla cuando la factorización es imposible. Observa:
**Ecuación:** $x^2 - 8x + 13 = 0$
1. **Centro ($t$):** $t = -\frac{(-8)}{2} = 4$
2. **Distancia ($u$):** 
   $$4^2 - u^2 = 13 \implies 16 - u^2 = 13 \implies u^2 = 3 \implies u = \sqrt{3}$$
3. **Soluciones:** 
   - **Forma Exacta:** $x = 4 \pm \sqrt{3}$
   - **Forma Decimal:** $x_1 \approx 5.73, x_2 \approx 2.27$
```

```ad-example
title: Ejemplo 4: Aplicación en Finanzas ($USD)
**Problema:** Una startup analiza su punto de equilibrio. El precio de venta "$x$" para obtener ganancia cero sigue la ecuación $x^2 - 10x + 21 = 0$. ¿Qué precios aseguran la estabilidad?
1. **Centro ($t$):** $t = 5$
2. **Distancia ($u$):** 
   $$25 - u^2 = 21 \implies u^2 = 4 \implies u = 2$$
3. **Soluciones:** $x = 5 \pm 2$
**Resultado:** Los precios estratégicos son **$3 USD** y **$7 USD**.
```

---

### ✍️ Ejercicios para el Estudiante

¡No te detengas, vas por buen camino! Pon a prueba tu lógica con estos niveles:

#### 🟢 Nivel Fácil (Simetría Entera)
1. $x^2 - 4x + 3 = 0$
2. $x^2 - 2x - 8 = 0$
3. $x^2 + 6x + 5 = 0$
4. $x^2 + 4x + 4 = 0$

#### 🟡 Nivel Medio (Reto de Signos)
1. $x^2 - 5x + 6 = 0$
2. $x^2 + 3x - 10 = 0$
3. $x^2 - x - 12 = 0$
4. $x^2 + 8x + 12 = 0$

#### 🔴 Nivel Avanzado (Preparación Profesional)
*Nota del Profesor: Recuerda que si $a \neq 1$, primero debes dividir toda la ecuación por $a$ para normalizar el sistema.*

1. $2x^2 - 12x + 16 = 0$
2. $5x^2 - 30x + 40 = 0$
3. Determine el precio en $USD para una ganancia nula: $x^2 - 14x + 45 = 0$.
4. Determine el costo unitario en $USD que satisface: $2x^2 - 4x - 6 = 0$. *(Importante: Interpreta cuál de los resultados matemáticos tiene sentido en un contexto de costo real).*

---

```ad-success
title: ✅ Respuestas para Verificación
- **Fácil:** 1) {1, 3}, 2) {4, -2}, 3) {-1, -5}, 4) {-2} (Raíz única).
- **Medio:** 1) {2, 3}, 2) {2, -5}, 3) {4, -3}, 4) {-2, -6}.
- **Avanzado:** 1) {4, 2}, 2) {4, 2}, 3) $5 USD y $9 USD, 4) **$3 USD** (el valor matemático $-1$ se descarta por ser un costo físico imposible).
```

---

### 🧐 Autoevaluación Conceptual

```ad-question
title: Pregunta 1: Fundamentos
¿Por qué es obligatorio que $a = 1$ antes de calcular el centro $t$?
- **Respuesta:** Porque la propiedad de que la suma de las raíces es igual a $-b$ solo se cumple directamente en ecuaciones normales (monómicas). Si $a \neq 1$, la suma de las raíces es $-b/a$, lo que alteraría el cálculo del centro.
```

```ad-question
title: Pregunta 2: Procedimiento Rápido
En la ecuación $x^2 - 12x + 20 = 0$, ¿cuál es el valor de $t$?
- **Respuesta:** $t = -(-12)/2 = 6$.
```

```ad-question
title: Pregunta 3: Aplicación Real ($USD)
Si un producto financiero sigue el modelo $x^2 - 8x + 15 = 0$, ¿cuáles son los costos de equilibrio?
A) $2 y $6  
B) $3 y $5  
C) $4 y $4  
- **Respuesta:** B ($t=4, u=1 \implies 4 \pm 1 = 3, 5$).
```

---

```ad-tip
title: 💡 En la próxima clase
¡Prepárate para lo inesperado! Veremos qué sucede cuando la distancia $u^2$ resulta ser un número negativo. Esto nos abrirá las puertas al fascinante mundo de los **números imaginarios y complejos**. ¡Te espero!
```

```ad-info
title: 🧭 Navegación
- **Anterior:** [[Clase 06 — Introducción a las Ecuaciones Cuadráticas]]
- **Siguiente:** [[Clase 08 — Ecuaciones Cuadráticas: Casos con Números Imaginarios]]
- **Índice:** [[Índice del Curso de Álgebra]]
```