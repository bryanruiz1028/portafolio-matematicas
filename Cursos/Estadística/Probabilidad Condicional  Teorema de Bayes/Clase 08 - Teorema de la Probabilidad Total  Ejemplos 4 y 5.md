# Teorema de la Probabilidad Total | Ejemplos 4 y 5

[Página Anterior](Clase07) | [Siguiente Tema: Teorema de Bayes](Clase09)

---

## 1. Relevancia y Aplicaciones

El **Teorema de la Probabilidad Total** es una herramienta fundamental que nos permite prever resultados globales cuando un evento puede ocurrir a través de múltiples caminos o procesos independientes. Al sumar las probabilidades de todas las rutas posibles, obtenemos una visión completa del sistema. En resumen, nos ayuda a encontrar la respuesta final incluso cuando existen muchas formas diferentes de llegar a ella.

*   💵 **Aplicación $USD:** Calcular pérdidas económicas proyectadas al identificar el impacto financiero de piezas defectuosas en una producción masiva.
*   🏗️ **Aplicación práctica:** Control de calidad en líneas de producción automatizadas donde intervienen distintas máquinas con diferentes niveles de precisión.
*   📊 **Situación cotidiana:** Determinar las probabilidades exactas en la selección de representantes en un salón de clases bajo condiciones que cambian en cada paso.

---

## 2. Concepto Clave

¡Hola! Imagina que quieres llegar a un tesoro, pero hay varios caminos distintos para alcanzarlo. El Teorema de la Probabilidad Total es simplemente la **suma de todas las formas posibles** en las que puedes lograr ese objetivo. Es como armar un rompecabezas: cada pieza representa un camino por el cual el evento puede ocurrir, y al unirlas todas, descubres la probabilidad completa del evento.

~~~ad-warning
**¡Cuidado con el reemplazo!**
Un error muy común es olvidar que en problemas de selección de personas (como elegir niños y niñas), las probabilidades **cambian** después de cada elección porque hay una persona menos en el grupo. Siempre verifica si el problema es "sin reemplazo".
~~~

~~~ad-tip
**Dibuja un "Diagrama de Árbol"**
El Diagrama de Árbol es tu mejor mapa visual. Te ayuda a no perderte entre tantos números y asegura que no olvides ninguna de las ramas que llevan a tu resultado.
~~~

---

## 3. Procedimiento Paso a Paso

Para resolver cualquier problema de probabilidad total de forma sencilla, sigue este orden lógico:

```text
1. Identificar las ramas principales (ej. Máquina A, B, C o Niño/Niña).
2. Asignar probabilidades iniciales a cada rama (deben sumar 1 o 100%).
3. Multiplicar las probabilidades a lo largo de cada camino específico.
4. Sumar los resultados de todos los caminos favorables para obtener la Probabilidad Total.
```

---

## 4. Ejemplos de Clase

### Ejemplo 1: Selección de 3 Niñas (Caso Básico)
En un salón con **9 niñas** y **6 niños** (Total: 15), queremos la probabilidad de elegir a 3 niñas al azar. Como no hay reemplazo, las fracciones disminuyen en cada paso:
*   **Cálculo:** $(9/15) \times (8/14) \times (7/13) = 504 / 2730 = 12/65$
*   **Resultado:** $0.1841$ o **18.41%**

### Ejemplo 2: El Orden Importa (2 Niños y 1 Niña)
Si buscamos la probabilidad de sacar exactamente 2 niños (H) y 1 niña (F), existen tres combinaciones posibles. Debemos calcular cada camino y sumarlos:
1.  **HHF:** $(6/15) \times (5/14) \times (9/13) = 270/2730 = 9/91$
2.  **HFH:** $(6/15) \times (9/14) \times (5/13) = 270/2730 = 9/91$
3.  **FHH:** $(9/15) \times (6/14) \times (5/13) = 270/2730 = 9/91$
*   **Resultado Total:** $9/91 + 9/91 + 9/91 = 27/91$, que equivale a **29.67%**.

### Ejemplo 3: Producción Industrial (Máquinas A, B y C)
Una fábrica utiliza tres máquinas con los siguientes datos:
*   **Máquina A:** Produce 10% (0.1) con 1% de defectos (0.01).
*   **Máquina B:** Produce 30% (0.3) con 2% de defectos (0.02).
*   **Máquina C:** Produce 60% (0.6) con 4% de defectos (0.04).
*   **Cálculo:** $(0.1 \times 0.01) + (0.3 \times 0.02) + (0.6 \times 0.04) = 0.001 + 0.006 + 0.024 = 0.031$.
*   **Resultado:** **3.1%** de probabilidad de que una pieza sea defectuosa.

### Ejemplo 4: Aplicación Real en $USD
Usando el resultado anterior, si cada pieza defectuosa cuesta **$5 USD** a la fábrica, ¿cuál es la pérdida en un lote de **1,000 piezas**?
*   **Explicación:** Multiplicamos la probabilidad total por el número de piezas para saber cuántas fallarán en promedio.
*   **Piezas defectuosas:** $1,000 \times 0.031 = 31$ piezas.
*   **Costo de pérdida:** $31 \times \$5 = \$155 USD$.

---

## 5. Ejercicios de Práctica

🟢 **Fácil: El Salón de Clases**
En un grupo de 7 niños y 5 niñas (12 en total), se seleccionan 3 estudiantes al azar sin reemplazo. ¿Cuál es la probabilidad de que los tres sean niños?
*   *Pista: Usa la configuración $(7/12) \times (6/11) \times (5/10)$.*

🟡 **Medio: Fábrica de Balones**
Una empresa fabrica balones: el 60% son de fútbol y el 40% de baloncesto. La probabilidad de defecto en fútbol es del 5% (0.05) y en baloncesto es del 3% (0.03). Si eliges un balón al azar, ¿cuál es la probabilidad total de que sea defectuoso?

🔴 **Avanzado: Impacto Financiero**
Basado en los datos de los balones anteriores, calcule la pérdida financiera total en un lote de **1,000 balones** si:
1. Un balón de fútbol defectuoso cuesta **$10 USD** en pérdidas.
2. Un balón de baloncesto defectuoso cuesta **$8 USD**.

~~~ad-success
**Resultados de los ejercicios**
*   **Fácil:** $210/1320 = 7/44$, aproximadamente **15.9%**.
*   **Medio:** $0.042$ o **4.2%**.
*   **Avanzado:** Pérdida de **$396 USD**. 
    *(Cálculo: Fútbol = 600 balones × 0.05 × $10 = $300; Baloncesto = 400 balones × 0.03 × $8 = $96. Total: $300 + $96).*
~~~

---

## 6. Mini-Prueba de Autoevaluación

1.  **¿Qué operación final se realiza con los resultados de cada rama favorable para obtener la Probabilidad Total?**
    *   a) Multiplicación
    *   b) Resta
    *   c) Suma

2.  **En un grupo de 10 personas (6 hombres, 4 mujeres), ¿cuál es la probabilidad de sacar 2 hombres seguidos sin reemplazo?**
    *   a) $36/100$
    *   b) $30/90$ (o $1/3$)
    *   c) $12/20$

3.  **Si una máquina tiene un 2% de error (0.02) y produce 500 piezas, ¿cuántas piezas defectuosas se esperan?**
    *   a) 2 piezas
    *   b) 10 piezas
    *   c) 20 piezas

---

## Notas para el próximo tema
¡Excelente trabajo! Ahora que dominas cómo calcular la probabilidad total (el "todo"), en la siguiente clase daremos el siguiente paso lógico con el **Teorema de Bayes**. Aprenderemos a hacer el camino inverso: si ya sabemos que una pieza salió defectuosa, ¿cuál es la probabilidad de que provenga de una máquina específica?

---
[Página Anterior](Clase07) | [Siguiente Tema: Teorema de Bayes](Clase09)