# Clase 03 — Progresiones Geométricas: Introducción, Término n-ésimo y Razón

#algebra #geometricprogre

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 4

> [!info] 🧭 Navegación
> - ⬅️ **Clase Anterior:** [[Clase 02 - Progresiones Aritméticas]]
> - ➡️ **Próxima Clase:** [[Clase 04 - Suma de Progresiones Geométricas]]

---

## 1. Relevancia: ¿Por qué es importante esta clase?

A diferencia de las progresiones aritméticas donde el cambio es constante (suma), las **progresiones geométricas** representan fenómenos de crecimiento o decrecimiento acelerado (multiplicativo). Entender este patrón es crucial para dominar procesos donde el cambio se dispara o se reduce drásticamente.

*   **💵 Aplicación $USD:** Esencial para calcular el interés compuesto o el crecimiento de una inversión que se duplica o triplica en cada periodo de tiempo.
*   **🏗️ Aplicación práctica:** En ingeniería y arquitectura, se utiliza para calcular escalas de materiales o dimensiones en estructuras que mantienen una proporción constante.
*   **📊 Situación cotidiana:** Permite modelar la propagación de información en redes sociales (viralidad) o procesos biológicos como la división celular.

---

## 2. Conceptos Clave

```ad-note
title: 📌 Definición
Una progresión geométrica (también llamada **sucesión geométrica**) es una secuencia de números donde cada término, a partir del segundo, se obtiene multiplicando el anterior por una cantidad fija llamada **razón ($r$)**. Al término general que define a cualquier miembro de la secuencia lo llamamos **término n-ésimo ($a_n$)**.
```

```ad-warning
title: ⚠️ Error común: ¿Suma o Multiplicación?
Es vital no confundir el tipo de progresión al observar una secuencia:
- ❌ **Aritmética:** `5, 10, 15...` (Se suma 5 en cada paso).
- ✅ **Geométrica:** `5, 10, 20...` (Se multiplica por 2 en cada paso).
```

### Clasificación de las Progresiones
Según los valores del primer término ($a_1$) y la razón ($r$), Profe Alex nos enseña a clasificarlas:
1.  **Crecientes:** El valor de los términos aumenta (ej. $a_1 > 0$ y $r > 1$).
2.  **Decrecientes:** El valor de los términos disminuye (ej. $a_1 > 0$ y $0 < r < 1$).
3.  **Alternadas:** Los signos cambian de positivo a negativo en cada paso. Esto ocurre siempre que la **razón sea negativa ($r < 0$)**.

---

## 3. Procedimiento y Fórmulas

Para resolver cualquier ejercicio, debemos seguir una jerarquía estricta de operaciones:
1.  Calcular la resta del exponente $(n-1)$.
2.  Resolver la potencia de la razón ($r^{exponente}$).
3.  Multiplicar el resultado por el primer término ($a_1$).

### Fórmulas Esenciales
*   **Para hallar el Término General ($a_n$):**
    $$a_n = a_1 \cdot r^{n-1}$$
*   **Para hallar la razón ($r$) con términos consecutivos:**
    $$r = \frac{a_n}{a_{n-1}}$$ *(Dividir el término de posición actual entre su "hermano menor" o anterior).*
*   **Para hallar la razón ($r$) con términos no consecutivos:**
    $$r = \sqrt[n-1]{\frac{a_n}{a_1}}$$ *(Útil cuando conocemos el primer término y un término lejano).*

```ad-tip
title: 💡 Nota Pro: Simplificación por Bases Iguales
Si el primer término ($a_1$) puede expresarse como una potencia de la razón ($r$), debemos simplificar el término general usando leyes de exponentes. 
**Ejemplo:** Si $a_1 = 1/4$ y $r = 2$, transformamos $1/4$ en $2^{-2}$. 
Entonces: $a_n = 2^{-2} \cdot 2^{n-1} = 2^{n-1-2} = 2^{n-3}$.
```

---

## 4. Ejemplos Prácticos

```ad-example
title: Ejemplo 1: Cálculo de secuencia básica
**Problema:** Hallar los primeros 4 términos si $a_1 = 3$ y $r = 2$.
**Solución:**
1. $a_1 = 3$
2. $a_2 = 3 \cdot 2 = 6$
3. $a_3 = 6 \cdot 2 = 12$
4. $a_4 = 12 \cdot 2 = 24$
**Resultado:** $3, 6, 12, 24...$ (Creciente)
```

```ad-example
title: Ejemplo 2: Progresión Alternada
**Problema:** Calcular los primeros términos si $a_1 = 5$ y $r = -2$.
**Solución:**
1. $a_1 = 5$
2. $a_2 = 5 \cdot (-2) = -10$
3. $a_3 = -10 \cdot (-2) = 20$
**Análisis:** Al ser $r$ negativa, el signo alterna: $+ , - , + , -$.
```

```ad-example
title: Ejemplo 3: Encontrar la razón con fracciones
**Problema:** En la secuencia $100, 50, 25...$, ¿cuál es la razón?
**Solución:** Dividimos un término entre el anterior: $r = 50 / 100$.
**Simplificación:** $r = 1/2$ (o $0.5$). Es una progresión decreciente.
```

```ad-example
title: Ejemplo 4: Aplicación $USD (Paso a paso)
**Problema:** Un activo financiero vale $100 USD y su valor se duplica cada año. ¿Cuánto valdrá al finalizar el cuarto año?
**Datos:** $a_1 = 100$, $r = 2$, $n = 4$.
**Procedimiento:**
1. Aplicar fórmula: $a_4 = 100 \cdot 2^{4-1}$
2. Restar exponente: $a_4 = 100 \cdot 2^3$
3. Resolver potencia: $a_4 = 100 \cdot 8$
4. Multiplicar: $a_4 = 800$
**Resultado:** $800 USD.
```

---

## 5. Ejercicios para el Estudiante

```ad-abstract
title: Ejercicios de Práctica
**🟢 Nivel Fácil**
1. Encuentra la razón en la secuencia: $10, 30, 90...$ e indica si es creciente o decreciente.
2. Si $a_1 = 80$ y $r = 1/2$, escribe los siguientes dos términos.

**🟡 Nivel Medio**
3. Hallar el término $a_6$ sabiendo que $a_1 = 1$ y $r = 5$.
4. Escribe la expresión simplificada del término general si $a_1 = 1/4$ y $r = 2$ (Utiliza la lógica de bases iguales explicada arriba).

**🔴 Nivel Avanzado ($USD)**
5. Un salario comienza en $1000 USD y se multiplica por $1.1$ cada año. Calcula el monto exacto en el año 4 ($a_4$).
6. En una progresión el primer término es 4 y el cuarto término es 108. Encuentra la razón utilizando la fórmula radical.
```

```ad-success
title: ✅ Respuestas (Para revisión)
1. $r = 3$ (Creciente).
2. $a_2 = 40, a_3 = 20$.
3. $a_6 = 3125$.
4. $a_n = 2^{n-3}$.
5. $a_4 = 1331$ USD ($1000 \cdot 1.1^3$).
6. $r = 3$ ($\sqrt[3]{108/4} = \sqrt[3]{27} = 3$).
```

---

## 6. Autoevaluación

```ad-question
title: Pregunta 1
¿Qué sucede con los signos de una progresión si la razón ($r$) es un número negativo?
*Respuesta: Se convierte en una progresión alternada (el signo cambia de $+$ a $-$ en cada término).*
```

```ad-question
title: Pregunta 2
En la fórmula $a_n = a_1 \cdot r^{n-1}$, ¿por qué es incorrecto multiplicar $a_1$ por $r$ antes de elevar a la potencia?
*Respuesta: Por la jerarquía de operaciones; la potencia tiene prioridad sobre la multiplicación.*
```

```ad-question
title: Pregunta 3
Si una inversión de $500 USD se convierte en $1000 USD el siguiente mes, y luego en $2000 USD, ¿cuál es la razón y qué tipo de progresión es?
*Respuesta: $r = 2$ y es una progresión geométrica creciente.*
```

---

## 7. Cierre

**💡 Próxima clase:** Ahora que dominas cómo encontrar cualquier término y su razón, aprenderemos a sumar todos los términos de una secuencia en la clase de **Suma de Progresiones Geométricas**.

---
> [!info] 🧭 Navegación
> - ⬅️ **Clase Anterior:** [[Clase 02 - Progresiones Aritméticas]]
> - ➡️ **Próxima Clase:** [[Clase 04 - Suma de Progresiones Geométricas]]