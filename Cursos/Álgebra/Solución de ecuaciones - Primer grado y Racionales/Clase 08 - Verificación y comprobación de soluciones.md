# Clase 08 — Verificación y comprobación de soluciones

**Curso:** Solución de Ecuaciones
**Etiquetas:** #Matemáticas #Álgebra #Ecuaciones #Verificación #Finanzas
**Nivel:** Básico - Intermedio

> [!info] 🧭 Navegación
> [Anterior: Clase 07](clase-07) | [Inicio: Índice del Curso](index) | [Siguiente: Clase 09](clase-09)

---

### 1. ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia
> La verificación es la herramienta definitiva de control de calidad en matemáticas. En el mundo real, asegura una **auditoría de facturas** impecable y un **presupuesto exacto**. Por ejemplo, si calculas mediante una ecuación que el precio unitario de un producto es de **$3 USD** y has comprado 4 unidades más un cargo fijo de envío de **$10 USD**, la verificación te permite confirmar si el total cobrado (**$22 USD**) coincide con tu cálculo antes de emitir un pago.

---

### 2. Concepto clave

> [!note] 📌 Definición
> La verificación o comprobación consiste en **sustituir** la incógnita de la ecuación original por el valor obtenido. Si la solución es correcta, la igualdad debe mantenerse (el valor numérico de la izquierda debe ser idéntico al de la derecha).

> [!warning] ⚠️ Error Común y la "Doble Falla"
> El error más frecuente es romper el orden jerárquico (hacer sumas antes que multiplicaciones). Sin embargo, como experto, te advierto: si al verificar obtienes una desigualdad (ej. $7 = 22$), no siempre significa que tu solución sea errónea; **podrías haber cometido un error aritmético en el proceso de verificación mismo**. Antes de borrar todo, revisa tus cuentas de comprobación.

> [!tip] 💡 Truco/Atajo
> Para evitar errores de signos, reescribe la ecuación usando paréntesis vacíos `( )` en lugar de la `x`. Luego, "rellena" los huecos con tu resultado. Además, como dice el Profe Alex: **"Para multiplicar un entero por una fracción, colócale un 1 abajo para no confundirte"**.

---

### 3. Procedimiento paso a paso

Sigue esta metodología técnica para garantizar exactitud:

```text
PASO 1: Reescribir la ecuación sustituyendo cada variable por paréntesis ().
PASO 2: Colocar el valor de la solución (en negrita o resaltado) dentro de ellos.
PASO 3: Resolver siguiendo la jerarquía:
        1. Multiplicaciones y Divisiones (numerador por numerador, denominador por denominador).
        2. Sumas y Restas (usando "carita feliz" para fracciones distintas o método directo para homogéneas).
PASO 4: Comparar ambos lados de la igualdad.
```

---

### 4. Ejemplos desarrollados

#### Ejemplo 1: Ecuación básica
**Ecuación:** $5x + 3 = 13$ | **Solución:** $x = 2$

```ad-example
1. Sustituir: $5(**2**) + 3 = 13$
2. Multiplicar: $10 + 3 = 13$
3. Resultado: $13 = 13$
**Conclusión:** La igualdad es verdadera; la solución es **correcta**.
```

#### Ejemplo 2: Variable en ambos lados
**Ecuación:** $3x - 5 = 20 - 2x$ | **Solución:** $x = 5$

```ad-example
1. Sustituir: $3(**5**) - 5 = 20 - 2(**5**)$
2. Operar multiplicaciones: $15 - 5 = 20 - 10$
3. Restar: $10 = 10$
**Conclusión:** La solución es **correcta**.
```

#### Ejemplo 3: El reto de las fracciones (Fidelidad a la fuente)
**Ecuación:** $3x + 11 - 7x = 1$ | **Solución:** $x = 5/2$

```ad-example
1. **Sustituir:** $3(**5/2**) + 11 - 7(**5/2**) = 1$
2. **Multiplicar (entero por fracción):** Ponemos un 1 bajo los enteros: $\frac{3}{1} \cdot \frac{5}{2} + 11 - \frac{7}{1} \cdot \frac{5}{2} = 1 \rightarrow \frac{15}{2} + 11 - \frac{35}{2} = 1$
3. **Agrupar fracciones homogéneas:** Es más fácil operar primero las que tienen igual denominador: $(\frac{15}{2} - \frac{35}{2}) + 11 = 1$
4. **Operar:** $\frac{-20}{2} + 11 = 1 \rightarrow -10 + 11 = 1$
5. **Resultado:** $1 = 1$.
*Nota:* Si las fracciones fueran heterogéneas, usaríamos el método de la **"carita feliz"** (multiplicación cruzada).
```

#### Ejemplo 4: Aplicación financiera ($USD)
**Problema:** Compras 4 libretas y un maletín de $10 USD. Total: $22 USD.  
**Ecuación:** $4x + 10 = 22$ | **Solución:** $x = 3$

```ad-example
1. Sustituir: $4(**3**) + 10 = 22$
2. Operar: $12 + 10 = 22$
3. Resultado: $22 = 22$
**Conclusión:** El precio unitario de **$3 USD** es correcto para tu presupuesto.
```

---

### 5. Ejercicios para el estudiante

*   **🟢 Fácil:** Verificar si $x = 5$ es la solución de $2x + 5 = 15$.
*   **🟡 Medio:** Verificar si $x = 1/2$ es la solución de $6x + 4 = 9 - 4x$.
*   **🔴 Avanzado ($USD):** Un presupuesto de $100 USD cubre 3 servicios técnicos iguales más un cargo fijo de $25 USD. Verificar si la solución $x = 25$ es correcta para la ecuación $3x + 25 = 100$.

```ad-success
title: Respuestas para el Docente
1. **Fácil:** $2(5) + 5 = 10 + 5 = 15$. Correcto ($15 = 15$).
2. **Medio:** Lado izquierdo: $6(1/2) + 4 = 3 + 4 = 7$. Lado derecho: $9 - 4(1/2) = 9 - 2 = 7$. Correcto ($7 = 7$).
3. **Avanzado:** $3(25) + 25 = 75 + 25 = 100$. Correcto ($100 = 100$). El costo por servicio es de $25 USD.
```

---

### 6. Mini-prueba de autoevaluación

```ad-question
title: Pregunta 1
Si al verificar una ecuación obtienes $7 = 22$, ¿qué acción es la más profesional?
- A) Declarar que la ecuación no tiene solución.
- B) Revisar tanto el procedimiento de la ecuación como la aritmética de la verificación.
- C) Cambiar el 7 por un 22 para que cuadre.

**Respuesta: B**
```

```ad-question
title: Pregunta 2
¿Cuál es el orden técnico para resolver $5(2) + 3$ en una comprobación?
- A) Sumar $2 + 3$ y multiplicar por $5$.
- B) Multiplicar $5 \times 2$ y luego sumar $3$.
- C) Restar 3 a ambos lados primero.

**Respuesta: B**
```

```ad-question
title: Pregunta 3
¿Cuál es la forma correcta de sustituir $x = -5$ en la expresión $-2x = 10$?
- A) $-2 - 5 = 10$
- B) $-2(-5) = 10$
- C) $-2 - (-5) = 10$

**Respuesta: B**
```

---

### 7. Cierre de la clase

> [!tip] 💡 Próximo paso
> La verificación es tu seguro de vida matemático. En la próxima clase, utilizaremos esta seguridad para resolver problemas complejos de la vida real y finanzas personales.

> [!info] 🧭 Navegación
> [Anterior: Clase 07](clase-07) | [Inicio: Índice del Curso](index) | [Siguiente: Clase 09](clase-09)