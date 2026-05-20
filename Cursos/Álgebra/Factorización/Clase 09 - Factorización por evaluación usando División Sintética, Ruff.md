# Clase 09 — Factorización por evaluación usando División Sintética, Ruffini | Ejemplo 2 + Guía de Métodos

#algebra #factorizacinpor

> [!info] 🧭 Navegación
> ◄ [[Clase 08 — Factorización por evaluación (Parte 1)]] | **Clase 09** | [[Índice de Factorización]] ►

---

## ¿Por qué es importante esta clase?

La factorización por evaluación es la técnica definitiva para desarmar polinomios de grado superior (como $x^3, x^4$ o mayores). Al convertir una expresión compleja en una multiplicación de factores simples, podemos encontrar las raíces o "puntos de quiebre" de cualquier modelo matemático.

*   **Dinero ($USD):** Permite proyectar el punto de equilibrio en modelos financieros donde las variables (como tiempo o volumen de ventas) están elevadas al cubo.
*   **Construcción:** Se utiliza para deducir las dimensiones de una estructura (largo, ancho, alto) conociendo únicamente la fórmula polinómica de su volumen total.
*   **Situación cotidiana:** Es fundamental para optimizar procesos logísticos y resolver acertijos de ingeniería donde se requiere desglosar un sistema en sus componentes básicos.

---

## Concepto Clave

> [!note] Definición: División Sintética (Ruffini)
> Es un "atajo" algorítmico diseñado para dividir polinomios entre binomios de la forma $(x \pm a)$ de manera eficiente. En lugar de realizar la división larga tradicional, operamos únicamente con los coeficientes numéricos para identificar qué valores anulan el residuo.

> [!warning] La Lógica del Cambio de Signo
> ¡No lo memorices como magia! Si al probar con el número $3$ en la "cajita" obtienes un residuo de $0$, significa que $x = 3$ es una raíz. Para convertirlo en factor, igualamos a cero: si $x = 3$, entonces $(x - 3) = 0$. Por eso, si usas **3**, el factor es **$(x - 3)$**. Si usas **-3**, el factor es **$(x + 3)$**.

> [!tip] Truco Experto: "Multiplica y suma"
> El proceso es mecánico: el primer coeficiente "cae" libremente. Luego, ese número se **multiplica** por el valor de la cajita, el resultado se coloca en la siguiente columna y se **suma** algebraicamente. Repite hasta llegar al final.

---

## Procedimiento Paso a Paso

```text
PASO 1: Organizar los coeficientes del polinomio de mayor a menor grado. 
       ¡Vital!: Si falta un término (ej. no hay x²), debes colocar un 0.
PASO 2: Listar los divisores del término independiente (el número sin x).
PASO 3: Realizar "ensayo y error" con los divisores en la cajita hasta que 
       el residuo final (última columna) sea exactamente 0.
PASO 4: Construir el resultado. Los números de la fila inferior son los 
       coeficientes del nuevo polinomio, el cual tendrá un grado menor 
       al original (si empezaste con x³, el resultado inicia con x²).
```

---

## Ejemplos Prácticos

### Ejemplo 1: Caso Básico de Práctica
**Polinomio:** $3x^3 + 4x^2 - 12x - 8$
1.  Probamos divisores de 8. Al intentar con $x = 2$, el residuo es 0. Factor: $(x - 2)$.
2.  Al intentar con $x = -2$, el residuo es 0. Factor: $(x + 2)$.
3.  El cociente resultante nos entrega el término $(3x + 2)$.
**Resultado final:** $(x - 2)(x + 2)(3x + 2)$

### Ejemplo 2: Modelado de Ensayo y Error (Ruffini Detallado)
**Polinomio:** $2x^3 - x^2 - 18x + 9$
*   **Divisores de 9:** $\pm 1, \pm 3, \pm 9$.
*   **Prueba con 1:** Al operar obtenemos un residuo de $-8$. **Falla.**
*   **Prueba con -1:** Al operar obtenemos un residuo de $24$. **Falla.**
*   **Prueba con 3:** 
    *   Bajamos el $2$.
    *   $2 \times 3 = 6 \rightarrow (-1 + 6) = 5$.
    *   $5 \times 3 = 15 \rightarrow (-18 + 15) = -3$.
    *   $-3 \times 3 = -9 \rightarrow (9 - 9) = 0$. **¡Éxito!**
*   **Análisis experto:** Obtenemos el factor $(x - 3)$ y un cociente de $2x^2 + 5x - 3$. 
> [!tip] Consejo de eficiencia
> Una vez que llegues a una expresión cuadrática ($x^2$), es más rápido usar métodos de trinomios que seguir con Ruffini. Factorizando $2x^2 + 5x - 3$ obtenemos $(x + 3)(2x - 1)$.
**Resultado final:** $(x - 3)(x + 3)(2x - 1)$

### Ejemplo 3: Estrategia de Selección (Jerarquía)
**Polinomio:** $x^2 - 36$
Para elegir el método, seguimos la jerarquía de decisión:
1.  **Contar términos:** Tiene 2 términos.
2.  **¿Factor Común?:** No hay letras ni números que se repitan.
3.  **¿Diferencia de Cuadrados?:** Es una resta y ambos tienen raíz cuadrada exacta ($\sqrt{x^2}=x, \sqrt{36}=6$).
**Selección:** Diferencia de Cuadrados (es más directo que Ruffini).
**Resultado:** $(x + 6)(x - 6)$

### Ejemplo 4: Aplicación Financiera ($USD)
Un modelo de ganancias está definido por $P(x) = x^3 - 7x + 6$. Determina los puntos de equilibrio (donde la ganancia es cero).
1.  **Coeficientes:** $1$ ($x^3$), $0$ ($x^2$), $-7$ ($x$), $6$ (Independiente).
2.  **Ruffini con $x = 1$:** El residuo da 0. El primer punto de equilibrio es $x=1$ USD, y el factor es $(x - 1)$.
3.  **Cociente:** $x^2 + x - 6$. Factorizado resulta en $(x + 3)(x - 2)$.
**Interpretación:** Los puntos de equilibrio ocurren cuando $x = 1$, $x = 2$ y $x = -3$ (pérdida).
**Forma factorizada:** $(x - 1)(x + 3)(x - 2)$

---

## Ejercicios para el Estudiante

> [!exercise] Nivel Fácil: Identificación de Métodos
> Determina si es más eficiente usar Factor Común o Diferencia de Cuadrados:
> 1. $x^2 - 25$
> 2. $4x + 12$
> 3. $m^2 - 81$
> 4. $ax + ay$

> [!exercise] Nivel Medio: Aplicación de Ruffini
> Factoriza completamente los siguientes polinomios cúbicos:
> 1. $x^3 - 6x^2 + 11x - 6$
> 2. $x^3 + 2x^2 - x - 2$
> 3. $x^3 - 3x^2 - 4x + 12$

> [!exercise] Nivel Avanzado: Verificación de Presupuestos ($USD)
> **Instrucción:** La factorización es la operación inversa a la multiplicación. Verifica si estas factorizaciones son correctas multiplicando los factores:
> 1. ¿Es $(x-2)(x+2)$ la factorización de $x^2 - 4$?
> 2. ¿Es $(x+1)(x+5)$ la factorización de $x^2 + 6x + 5$?
> 3. ¿Es $(x-5)^2$ la factorización de $x^2 - 10x + 25$?

> [!success] Panel de Respuestas (Autocorrección)
> **Fácil:** 1. Dif. Cuadrados, 2. F. Común, 3. Dif. Cuadrados, 4. F. Común.
> **Medio:** 1. $(x-1)(x-2)(x-3)$, 2. $(x-1)(x+1)(x+2)$, 3. $(x-2)(x+2)(x-3)$.
> **Avanzado:** 1. Sí (da $x^2-4$), 2. Sí (da $x^2+6x+5$), 3. Sí (da $x^2-10x+25$).

---

## Mini-prueba de Autoevaluación

> [!question] Pregunta 1: El concepto de "La Apuesta"
> Tu compañero dice que $2(6x + 9)$ es la factorización de $12x + 18$. Tú dices que es $6(2x + 3)$. ¿Quién ganaría la apuesta y por qué?
> *   **Respuesta:** Ambos están factorizados (escritos como multiplicación), pero tú ganas porque tu factorización es **completa**. Siempre se buscan los factores más simples (primos).

> [!question] Pregunta 2: El Grado Resultante
> Si aplicas la regla de Ruffini exitosamente a un polinomio de grado 5 ($x^5$), ¿qué exponente tendrá el término principal del cociente?
> *   **Respuesta:** Grado 4 ($x^4$). Cada aplicación exitosa reduce el grado en 1.

> [!question] Pregunta 3: Verificación Inversa
> Si factorizaste un costo como $(x + 4)(x - 4)$, ¿cuál era la expresión original?
> a) $x^2 + 16$
> b) $x^2 - 16$
> c) $x^2 - 8$
> *   **Respuesta:** b) $x^2 - 16$ (Diferencia de cuadrados).

---

## Cierre y Notas Finales

> [!tip] Próximo paso
> Ahora que sabes elegir el mejor método y usar Ruffini, estamos listos para la **Clase 10: Factorización Total y Simplificación de Fracciones**, donde aplicaremos todo esto para resolver problemas de nivel experto.

> [!info] 🧭 Navegación
> ◄ [[Clase 08 — Factorización por evaluación (Parte 1)]] | **Clase 09** | [[Índice de Factorización]] ►