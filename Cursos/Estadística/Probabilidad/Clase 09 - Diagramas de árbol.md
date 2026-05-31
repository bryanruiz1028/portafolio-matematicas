# Clase 09 — Diagramas de árbol

#algebra #diagramaderbol
Curso: [[00 - Índice del curso]] | Bloque 3 | Lección 9 de 12

> [!info] 🧭 Navegación
> Anterior: [[Clase 08 — Probabilidad Simple]]
> Índice: [[00 - Índice del curso]]
> Siguiente: [[Clase 10 — Probabilidad Condicional]]

---

## RELEVANCIA Y APLICACIONES

El diagrama de árbol es una herramienta visual esencial para organizar experimentos aleatorios que ocurren en varias etapas. Permite desglosar rutas complejas en pasos individuales para asegurar que no olvidemos ningún resultado posible y calcular probabilidades compuestas con precisión.

*   💵 **Aplicación USD:** Se utiliza para calcular la probabilidad de éxito en inversiones financieras de dos pasos, analizando cómo el resultado de una fluctuación inicial ($A$) influye en el capital final ($B$) en escenarios de eventos independientes.
*   🏗️ **Aplicación práctica:** Es fundamental en el control de calidad de líneas de producción para determinar la probabilidad de que un producto sea defectuoso tras pasar por varios puntos de inspección.
*   📊 **Situación cotidiana:** Ayuda en la toma de decisiones con múltiples opciones, como calcular cuántas combinaciones distintas de vestimenta puedes armar o elegir un menú entre diversas opciones de plato fuerte, bebida y postre.

---

## CONCEPTO CLAVE

**Definición:**
El **Diagrama de Árbol** es una representación gráfica de los posibles resultados de un experimento que se realiza en varias etapas. Imagínalo como un mapa de caminos: cada "punto de decisión" se llama **nodo** y cada opción posible es una **rama**. Es ideal para visualizar sucesiones de eventos (como lanzar una moneda varias veces).

> [!warning] Error común
> Muchos estudiantes creen que todas las ramas deben tener siempre una probabilidad de $ \frac{1}{2} $ (50%). Sin embargo, las probabilidades dependen del número de opciones: en una moneda es $ \frac{1}{2} $, pero en un dado cada rama de número tiene una probabilidad de $ \frac{1}{6} $. ¡Siempre verifica el total de opciones!

> [!tip] Truco: La regla de los caminos
> Para no fallar nunca, recuerda:
> 1. **Hacia adelante multiplicas (ramas):** Para hallar la probabilidad de un camino completo.
> 2. **Hacia abajo sumas (resultados finales):** Si hay varios caminos que cumplen lo que buscas, suma sus totales.

---

## PROCEDIMIENTO PASO A PASO

> [!abstract] Metodología del Profe Alex
> 1. **Identificar Eventos:** Define cuántos experimentos se realizan y dibuja las ramas iniciales desde el primer nodo.
> 2. **Asignar Probabilidades:** Escribe la probabilidad sobre cada rama. Asegúrate de que todas las ramas que salen de un mismo nodo **sumen exactamente 1** (o $ 100\% $).
> 3. **Expandir el Árbol:** Dibuja nuevas ramas al final de cada resultado anterior para representar el segundo (o tercer) evento.
> 4. **Multiplicar Caminos:** Multiplica las probabilidades a lo largo de cada ruta para hallar la probabilidad final de esa combinación específica.

---

## EJEMPLOS DESARROLLADOS

```ad-example
title: Ejemplo 1: Lanzamiento de dos monedas (Caso Básico)
Visualizamos dos lanzamientos independientes.

**Estructura del Árbol:**
```text
           (1/2) -- Cara (C) --> (1/2) -- Cara (C)  => [C,C]
Inicio <                               --(1/2) -- Sello (S) => [C,S]
           (1/2) -- Sello (S) --> (1/2) -- Cara (C)  => [S,C]
                               --(1/2) -- Sello (S) => [S,S]
```
**Pregunta:** ¿Probabilidad de obtener dos caras ($C,C$)?
**Cálculo:** $ \frac{1}{2} \times \frac{1}{2} = \frac{1}{4} = 25.0\% $.
```

```ad-example
title: Ejemplo 2: Moneda y Dado (Caso Mixto)
Primero una moneda (C, S) y luego un dado (1 al 6).

**Estructura del Árbol:**
```text
          --(1/2)-- Cara (C) --(1/6)-- [1, 2, 3, 4, 5, 6]
Inicio <
          --(1/2)-- Sello (S) --(1/6)-- [1, 2, 3, 4, 5, 6]
```
**Pregunta 1:** Probabilidad de "Cara y número 3".
**Cálculo:** $ P(C) \times P(3) = \frac{1}{2} \times \frac{1}{6} = \frac{1}{12} \approx 8.3\% $.

**Pregunta 2:** Probabilidad de "Cara y número mayor a 3" (es decir: 4, 5 o 6).
**Cálculo:** $ P(C) \times P(>3) = \frac{1}{2} \times \frac{3}{6} = \frac{3}{12} = \frac{1}{4} = 25.0\% $.
```

```ad-example
title: Ejemplo 3: Urna con reemplazo (Caso Avanzado)
Una urna tiene 3 bolas rojas ($R$) y 4 azules ($A$). Sacamos dos bolas devolviendo la primera.
$ P(R) = \frac{3}{7} $ | $ P(A) = \frac{4}{7} $

**Pregunta:** Probabilidad de sacar dos bolas del mismo color ($RR$ o $AA$).
1. **Camino RR:** $ \frac{3}{7} \times \frac{3}{7} = \frac{9}{49} $.
2. **Camino AA:** $ \frac{4}{7} \times \frac{4}{7} = \frac{16}{49} $.
**Suma de resultados:** $ \frac{9}{49} + \frac{16}{49} = \frac{25}{49} \approx 51.0\% $.
```

```ad-example
title: Ejemplo 4: Aplicación USD (Escenario de Billetes)
Tienes una caja con 3 billetes de $ 10 $ USD y 4 billetes de $ 1 $ USD. Extraes uno, lo regresas y extraes otro.
**Pregunta:** ¿Cuál es la probabilidad de sacar dos billetes del mismo valor?

1. **Probabilidad de dos billetes de $ 10 $:** $ \frac{3}{7} \times \frac{3}{7} = \frac{9}{49} $.
2. **Probabilidad de dos billetes de $ 1 $:** $ \frac{4}{7} \times \frac{4}{7} = \frac{16}{49} $.
**Total:** $ \frac{9}{49} + \frac{16}{49} = \frac{25}{49} \approx 51.0\% $.
(Observa que la lógica matemática es idéntica al Ejemplo 3).
```

---

## EJERCICIOS PARA EL ESTUDIANTE

### Nivel Fácil (Verde)
1. Dibuja el árbol para lanzar una moneda 3 veces.
2. ¿Cuál es la probabilidad de obtener 3 sellos?
3. ¿Cuál es la probabilidad de obtener exactamente 2 caras?
4. ¿Cuál es la probabilidad de que salga al menos una cara?

### Nivel Medio (Amarillo)
1. Lanzamos moneda y dado. ¿Probabilidad de Sello y número par?
2. Lanzamos moneda y dado. ¿Probabilidad de Cara y número menor a 3?
3. Lanzamos moneda y dado. ¿Probabilidad de Sello y número 1 o 6?
4. ¿Probabilidad de que salga cualquier cara de la moneda y un número impar en el dado?

### Nivel Avanzado (Rojo - Aplicación USD)
*Contexto: Una urna contiene 5 bonos de $ 50 $ USD y 4 bonos de $ 20 $ USD. El experimento es **sin reemplazo** (al sacar el primero, no se devuelve).*

1. Calcula la probabilidad de que el primer bono sea de $ 50 $ y el segundo de $ 20 $.
2. Calcula la probabilidad de obtener dos bonos de $ 50 $.
3. Calcula la probabilidad de obtener dos bonos de $ 20 $.
4. ¿Cuál es la probabilidad de que ambos bonos sean de distinto valor?

```ad-success
title: Respuestas y Soluciones
**Fácil:**
1) Árbol de 8 ramas finales ($2 \times 2 \times 2$). 2) $ \frac{1}{8} $ (12.5%). 3) $ \frac{3}{8} $ (37.5%). 4) $ \frac{7}{8} $ (87.5%).

**Medio:**
1) $ \frac{3}{12} = \frac{1}{4} $ (25.0%). 2) $ \frac{2}{12} = \frac{1}{6} $ (16.6%). 3) $ \frac{2}{12} = \frac{1}{6} $ (16.6%). 4) $ \frac{6}{12} = \frac{1}{2} $ (50.0%).

**Avanzado (Lógica sin reemplazo):**
*Nota: El denominador cambia de 9 a 8 en la segunda extracción.*
1) $ \frac{5}{9} \times \frac{4}{8} = \frac{20}{72} = \frac{5}{18} $ (27.8%).
2) $ \frac{5}{9} \times \frac{4}{8} = \frac{20}{72} = \frac{5}{18} $ (27.8%). (Quedaban solo 4 bonos de $ 50 $).
3) $ \frac{4}{9} \times \frac{3}{8} = \frac{12}{72} = \frac{1}{6} $ (16.6%).
4) $ P(50,20) + P(20,50) = \frac{20}{72} + \frac{20}{72} = \frac{40}{72} = \frac{5}{9} $ (55.5%).
```

---

## MINI-PRUEBA DE AUTOEVALUACIÓN

**1. En cualquier nodo del diagrama de árbol, la suma de las probabilidades de las ramas que brotan de él debe ser:**
- a) Depende del experimento.
- b) Siempre $ 0.5 $.
- c) Siempre $ 1 $ (o $ 100\% $).
- d) No tiene que sumar nada en específico.
*Respuesta: **c**. Según el Profe Alex, las ramas que emergen de un mismo nodo deben completar la unidad para cubrir todas las posibilidades de ese paso.*

**2. Para hallar la probabilidad de un camino compuesto (ej. Cara y luego 3), debemos:**
- a) Sumar las probabilidades de las ramas.
- b) Restar las probabilidades.
- c) Multiplicar las probabilidades a lo largo del camino.
- d) Dividir la primera entre la segunda.
*Respuesta: **c**. Multiplicamos para hallar la probabilidad de que ocurra el primer evento Y el segundo evento consecutivamente.*

**3. ¿Cuál es la principal diferencia en el árbol al realizar un experimento "sin reemplazo"?**
- a) El número de ramas aumenta al final.
- b) El denominador de la probabilidad en el segundo evento disminuye porque hay un elemento menos en total.
- c) Las probabilidades se mantienen iguales en todo el árbol.
- d) El diagrama de árbol deja de ser útil.
*Respuesta: **b**. Al no devolver el elemento, el total (denominador) se reduce (por ejemplo, de 9 a 8) y el numerador también cambia si sacamos un elemento del mismo tipo ($ P(B|A) $).*

---

## CIERRE Y NOTAS
**Próximo tema:** En la Clase 10 exploraremos la **Probabilidad Condicional**. Veremos cómo el diagrama de árbol es el mejor aliado para entender qué sucede cuando un evento depende totalmente de lo que ocurrió en el paso anterior.

> [!info] 🧭 Navegación
> Anterior: [[Clase 08 — Probabilidad Simple]]
> Índice: [[00 - Índice del curso]]
> Siguiente: [[Clase 10 — Probabilidad Condicional]]