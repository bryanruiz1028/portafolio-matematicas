# Clase 05 — De la Ecuación Simétrica a la General y Métodos de Graficación

#algebra #geometria_analitica #ecuacion_recta

[Anterior: Clase 04] | [Siguiente: Clase 06]

---

## RELEVANCIA Y APLICACIONES (¿Por qué es importante esta clase?)

Dominar las distintas formas de representar una recta no es solo un ejercicio algebraico; es adquirir la capacidad de elegir la herramienta más eficiente según el problema. Conocer la transición entre la **forma simétrica** y la **general** permite visualizar instantáneamente dónde una recta corta los ejes y cómo simplificar cálculos complejos.

*   **Finanzas ($USD):** Permite modelar el comportamiento de costos fijos y variables. Por ejemplo, si un servicio de suscripción cuesta $5 USD de base y un cargo adicional por hora de uso, la ecuación nos ayuda a proyectar gastos totales de forma lineal.
*   **Construcción y Arquitectura:** Es fundamental para calcular la pendiente de rampas de acceso o la inclinación de techos, asegurando que se cumplan las normas de seguridad y drenaje pluvial.
*   **Situaciones Cotidianas:** Ayuda a predecir tiempos de llegada en viajes a velocidad constante, relacionando la distancia recorrida con el tiempo transcurrido de manera directa y visual.

---

## CONCEPTO CLAVE

> **Nota: Conversión a la Forma General**
> Pasar de la forma simétrica (o segmentaria) $\frac{x}{a} + \frac{y}{b} = 1$ a la forma general ($Ax + By + C = 0$) consiste en eliminar los denominadores y agrupar todos los términos a un solo lado de la igualdad. 
> 
> La forma simétrica es poderosa porque nos regala las **intersecciones con los ejes**:
> *   $a$: Es el punto donde la recta corta al eje $X$ (punto $(a, 0)$).
> *   $b$: Es el punto donde la recta corta al eje $Y$ (punto $(0, b)$).

> **Atención: Error común**
> Un error frecuente es no igualar a cero. Si dejas la ecuación como $5x + 2y = 10$, no has llegado a la **forma general**. También, ten cuidado al sumar fracciones si un denominador es negativo; el signo afecta a toda la operación al realizar la multiplicación cruzada.

> **Truco: El método de la "Carita Feliz"**
> Para sumar las fracciones de la forma simétrica rápidamente, aplicamos este patrón visual:
> $$\frac{x}{a} + \frac{y}{b} = \frac{(b \cdot x) + (a \cdot y)}{a \cdot b} = 1$$
> Esto te permite obtener un denominador común rápidamente para luego pasarlo a multiplicar al otro lado.

---

## PROCEDIMIENTO PASO A PASO (Conversión y Graficación)

### Conversión de Simétrica a General
```text
PASO 1: Realizar la suma de fracciones (Método de Carita Feliz).
PASO 2: Multiplicar el denominador común resultante por el 1 del otro lado.
PASO 3: Trasladar ese término independiente al lado izquierdo para igualar a cero (cambiando su signo).
PASO 4: Asegurar que el término A (de la x) sea positivo. Si es negativo, multiplica toda la ecuación por -1. Simplifica si todos los coeficientes son divisibles por el mismo número.
```

### Método de Graficación "Que no conocías" (Intersecciones Directas)
```text
1. Mira los denominadores "a" y "b" de la forma simétrica (x/a + y/b = 1).
2. TRUCO DE COEFICIENTES: Si tienes un coeficiente arriba (ej. 2x/5), pásalo al "denominador del denominador" -> x/(5/2). Así, "a" será 2.5.
3. Ubica el valor de "a" directamente en el eje X y el valor de "b" en el eje Y.
4. Une los dos puntos con una regla. ¡Sin tablas y sin despejes largos!
```

---

## EJEMPLOS PRÁCTICOS

> **Ejemplo 1: Conversión Básica**
> Convierte $\frac{x}{2} + \frac{y}{5} = 1$ a la forma general.
> 1. Sumamos cruzado: $\frac{5x + 2y}{10} = 1$
> 2. Pasamos el $10$ a multiplicar: $5x + 2y = 10$
> 3. Igualamos a cero: $5x + 2y - 10 = 0$ (Donde $A=5, B=2, C=-10$).

> **Ejemplo 2: Manejo de Signos**
> Convierte $\frac{x}{-3} + \frac{y}{4} = 1$ a la forma general.
> 1. Sumamos: $\frac{4x + (-3y)}{-12} = 1$
> 2. Pasamos el $-12$: $4x - 3y = -12$
> 3. Llevamos al lado izquierdo: $4x - 3y + 12 = 0$.

> **Ejemplo 3: Graficación Pendiente-Intersección (Forma Explícita)**
> Grafica $y = \frac{2}{3}x - 3$.
> 1. Ubica la **ordenada al origen** ($b$) en $(0, -3)$ del eje $Y$.
> 2. Usa la pendiente $m = \frac{2}{3}$ (Incremento en $Y$ / Incremento en $X$):
>    - Desde $(0, -3)$, **sube 2 unidades** (incremento positivo en $Y$).
>    - Luego, **corre 3 unidades a la derecha** (incremento positivo en $X$).
> 3. Marca el nuevo punto y traza la recta que pasa por ambos.

> **Ejemplo 4: Aplicación en $USD**
> Un servicio de asesoría técnica cobra $5 USD de base más $2 USD por cada hora.
> *   **Forma Pendiente-Ordenada:** $y = 2x + 5$
> *   **Forma General:** $2x - y + 5 = 0$
> *   **Costo para $3$ horas:** $y = 2(3) + 5 = 6 + 5 = \mathbf{11\ USD}$.

---

## EJERCICIOS PARA EL ESTUDIANTE

> **Ejercicios de Práctica**
>
> **Nivel Verde (Fácil): Convierte a forma general**
> 1. $\frac{x}{4} + \frac{y}{3} = 1$
> 2. $\frac{x}{7} + \frac{y}{2} = 1$
> 3. $\frac{x}{2} + \frac{y}{8} = 1$
> 4. $\frac{x}{5} + \frac{y}{5} = 1$
>
> **Nivel Amarillo (Medio): Graficación**
> 5. Grafica $y = 3x - 2$ usando tabla de valores con $x = \{0, 1, 2\}$.
> 6. Grafica $y = -x + 5$ usando tabla de valores con $x = \{-1, 0, 1\}$.
> 7. Grafica $y = \frac{4}{3}x - 2$ usando el método de pendiente-intersección.
> 8. Grafica $y = -\frac{1}{2}x + 3$ usando el método de pendiente-intersección.
>
> **Nivel Rojo (Avanzado): Aplicaciones $USD**
> 9. Un plan de datos cuesta $10 USD fijos y $2 USD por cada GB extra ($x$). Escribe la forma general y calcula el costo de 5 GB extras.
> 10. Una constructora cobra $100 USD por diagnóstico y $50 USD por hora. Identifica $m$, $b$ y describe el movimiento para graficar.
> 11. El alquiler de una pulidora cuesta $20 USD diarios más una cuota de limpieza de $5 USD. Escribe la ecuación general.
> 12. Un negocio tiene costos fijos de $30 USD y vende productos a $15 USD cada uno. Escribe la ecuación de ganancia neta en forma general.

> **Soluciones (Respuestas)**
> 1. $3x + 4y - 12 = 0$
> 2. $2x + 7y - 14 = 0$
> 3. $4x + y - 8 = 0$ (Simplificada tras dividir entre 2)
> 4. $x + y - 5 = 0$
> 5. Puntos: $(0, -2), (1, 1), (2, 4)$.
> 6. Puntos: $(-1, 6), (0, 5), (1, 4)$.
> 7. Inicia en $(0, -2)$, sube 4, derecha 3.
> 8. Inicia en $(0, 3)$, baja 1, derecha 2.
> 9. $2x - y + 10 = 0$; Costo total: $20 USD. (Movimiento: inicia en 10, sube 2, derecha 1).
> 10. $m = 50, b = 100$. Graficación: Inicia en $(0, 100)$, sube 50, derecha 1.
> 11. $20x - y + 5 = 0$.
> 12. $15x - y - 30 = 0$. Graficación: Inicia en $(0, -30)$, sube 15, derecha 1.

---

## AUTOEVALUACIÓN

> **Preguntas de Repaso**
>
> 1. En la ecuación $\frac{x}{a} + \frac{y}{b} = 1$, ¿qué representan los valores de $a$ y $b$?
>    *Respuesta:* Las intersecciones con los ejes $X$ e $Y$ respectivamente.
>
> 2. ¿Cuál es la forma general de $\frac{x}{4} + \frac{y}{-2} = 1$?
>    a) $x + 2y - 4 = 0$
>    b) $x - 2y - 4 = 0$
>    c) $-2x + 4y - 8 = 0$
>    d) $x - y - 2 = 0$
>    *Respuesta correcta:* **b**. Al sumar: $\frac{-2x + 4y}{-8} = 1 \rightarrow -2x + 4y = -8 \rightarrow -2x + 4y + 8 = 0$. Al dividir todo entre $-2$ para que $A$ sea positivo, obtenemos $x - 2y - 4 = 0$.
>
> 3. Si una gráfica de costo inicia en $8 USD en el eje $Y$ y su pendiente es $3$, ¿cuál es el costo para $10$ unidades?
>    *Respuesta:* $y = 3(10) + 8 = 38 USD$.

---

## NOTAS FINALES Y NAVEGACIÓN

> **Próxima Clase**
> En la Clase 06 exploraremos la **Distancia entre un punto y una recta**. Aprenderemos a usar una fórmula maestra para determinar qué tan cerca está una coordenada de nuestra trayectoria lineal.

[Anterior: Clase 04] | [Siguiente: Clase 06]