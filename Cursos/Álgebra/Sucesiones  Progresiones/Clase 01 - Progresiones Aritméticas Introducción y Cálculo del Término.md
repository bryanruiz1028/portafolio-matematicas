# Clase 01 — Progresiones Aritméticas: Introducción y Cálculo del Término n-ésimo

**Tags:** #matemáticas #álgebra #progresiones #profealex  
**Curso:** Álgebra desde Cero

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [[Inicio del Curso]] | ➡️ **Siguiente:** [[Clase 02 — Suma de Progresiones Aritméticas]]

---

## 1. Relevancia y Aplicaciones

> [!info] 🌍 Relevancia y aplicaciones
> **¿Por qué es importante esta clase?**  
> ¡Hola, amigos! Espero que estén muy bien. Las progresiones aritméticas no son solo una lista de números que "suenan como en japonés"; son herramientas para entender el crecimiento constante. Comprender esto te permite predecir el futuro (matemáticamente hablando) sin tener que contar paso a paso.
> 
> *   **Ahorro (USD):** Si hoy tienes un dinero base y decides ahorrar **$3 USD cada día** de forma constante, estás creando una progresión aritmética. Con la fórmula que veremos, sabrás cuánto tendrás en el día 100 en un abrir y cerrar de ojos.
> *   **Construcción:** Para calcular materiales en filas, como los ladrillos de una pared donde cada nivel aumenta de forma regular, usamos progresiones para asegurar que el conteo sea exacto.
> *   **Rutina de ejercicio:** Si hoy corres 10 minutos y cada día aumentas **2 minutos constantes** a tu entrenamiento, estás aplicando una PA para planificar tu rendimiento físico a largo plazo.

---

## 2. Concepto Clave

> [!note] 📌 ¿Qué es una Progresión Aritmética?
> Una **Progresión Aritmética (PA)** es una sucesión de números tales que la diferencia de dos números seguidos es **constante**. Esto significa que cada número se obtiene sumando o restando la misma cantidad al anterior. A esta constante se le llama **diferencia (d)**.
> 
> Para trabajar como expertos, usaremos estas dos fórmulas (que parecen difíciles, pero verás que son muy sencillas):
> 1. **Si conoces el primer término:** $a_n = a_1 + (n - 1)d$
> 2. **Si conoces un término cualquiera ($a_k$):** $a_n = a_k + (n - k)d$
> 
> *Donde $n$ es la posición que buscas y $k$ es la posición que ya conoces.*

> [!warning] ⚠️ Error común
> ¡Cuidado aquí! Para hallar la diferencia ($d$), siempre debemos restar el **término de la derecha menos el de la izquierda** ($a_2 - a_1$). Si lo haces al revés, el signo estará mal y todo el ejercicio fallará. Si la sucesión disminuye, la diferencia **debe** ser negativa.

> [!tip] 💡 Truco para recordarlo
> Imagina que la diferencia "**d**" es el tamaño de un **"salto"** constante en una escalera. Si todos los escalones miden lo mismo, estás ante una Progresión Aritmética.

---

## 3. Procedimiento paso a paso

Sigue este orden lógico para resolver cualquier ejercicio y no morir en el intento:

```text
1. Identificar datos: Localiza el primer término (a1) o un término conocido (ak).
2. Calcular la diferencia (d): Resta dos términos seguidos (ejemplo: a2 - a1).
3. Elegir y sustituir en la fórmula: 
   - Usa a1 si lo tienes a la mano.
   - Usa ak si el problema te da un término de en medio de la sucesión.
4. Operar con jerarquía: Primero el paréntesis, luego la multiplicación y al final la suma/resta.
```

---

## 4. Ejemplos Detallados

```ad-example
title: Ejemplo 1: Nivel Básico
**Sucesión:** 2, 5, 8, 11... Hallar el décimo término ($a_{10}$).
1. **Datos:** $a_1 = 2$, $d = 3$ (porque $5 - 2 = 3$).
2. **Fórmula:** $a_{10} = 2 + (10 - 1)3$.
3. **Cálculo:** $a_{10} = 2 + (9)(3) = 2 + 27 = 29$.
**Resultado:** El décimo término es **29**.
```

```ad-example
title: Ejemplo 2: Manejo de Signos
**Sucesión:** 15, 9, 3, -3... Hallar el término 12 ($a_{12}$).
1. **Datos:** $a_1 = 15$, $d = -6$ (porque $9 - 15 = -6$).
2. **Fórmula:** $a_{12} = 15 + (12 - 1)(-6)$.
3. **Cálculo:** $a_{12} = 15 + (11)(-6) = 15 - 66 = -51$.
**Resultado:** El término 12 es **-51**.
```

```ad-example
title: Ejemplo 3: Uso de Fracciones
**Datos:** $a_1 = 6$, $d = 3/2$. Hallar el término 10 ($a_{10}$).
1. **Fórmula:** $a_{10} = 6 + (10 - 1)(3/2)$.
2. **Cálculo:** $a_{10} = 6 + 9(3/2) = 6 + 27/2$.
3. **Suma:** $\frac{12}{2} + \frac{27}{2} = \frac{39}{2}$.
**Resultado:** El décimo término es **39/2**.
```

```ad-example
title: Ejemplo 4: Aplicación Financiera (Término k)
**Problema:** Si en el día 10 tienes ahorrados $20 USD ($a_{10}=20$) y ahorras $5 USD diarios ($d=5$), ¿cuánto tenías el día 4?
1. **Datos:** $a_{10} = 20, d = 5, n = 4, k = 10$.
2. **Fórmula:** $a_4 = 20 + (4 - 10)5$.
3. **Cálculo:** $a_4 = 20 + (-6)5 = 20 - 30 = -10$.
**Resultado:** Tenías un saldo de **-10 USD** (una deuda).
```

---

## 5. Ejercicios para el estudiante

```ad-abstract
title: 🟢 Nivel Fácil: Diferencia y siguiente término
Halla la diferencia ($d$) y el siguiente término en:
1. 5, 8, 11...
2. 10, 14, 18...
3. 20, 15, 10...
4. -2, 1, 4...
```

```ad-abstract
title: 🟡 Nivel Medio: El término n-ésimo
Usa la fórmula $a_n = a_1 + (n-1)d$ para hallar:
1. $a_{20}$ en: 7, 12, 17...
2. $a_{15}$ en: 100, 90, 80...
3. $a_{8}$ en: $a_1 = 4, d = 1/2$.
4. $a_{20}$ en: -5, -7, -9...
```

```ad-abstract
title: 🔴 Nivel Avanzado: Aplicación de término conocido
Usa la fórmula $a_n = a_k + (n - k)d$ para resolver:
1. Un préstamo aumenta $8 USD de interés mensual. Si en el mes 5 debes $-3$ USD, ¿cuánto deberás en el mes 11? ($a_5 = -3, d = 8$).
2. Si el cuarto término de una PA es 3 y la diferencia es 2, halla el término 10. ($a_4 = 3, d = 2$).
3. En una sucesión donde la diferencia es -5, el quinto término es -8. Halla el término 15. ($a_5 = -8, d = -5$).
4. Si el día 10 de ahorros tienes $20 USD y tu ahorro diario es de $5 USD, ¿con cuánto dinero empezaste el día 1? ($a_{10} = 20, d = 5$).
```

```ad-success
title: Respuestas (Verifica tus resultados)
**Fácil:** 1) d=3, sig=14 | 2) d=4, sig=22 | 3) d=-5, sig=5 | 4) d=3, sig=7.  
**Medio:** 1) 102 | 2) -40 | 3) 7.5 (o 15/2) | 4) -43.  
**Avanzado:** 1) 45 | 2) 15 | 3) -58 | 4) -25.
```

---

## 6. Mini-prueba de autoevaluación

```ad-question
title: Conceptual
¿Qué condición debe cumplirse para que una sucesión sea considerada una Progresión Aritmética?
*Respuesta: Que la diferencia entre términos seguidos sea constante (siempre se suma o resta lo mismo).*
```

```ad-question
title: Procedimental
Si el término general es $3n - 1$, ¿cuál es el tercer término ($a_3$)?
*Respuesta: 8 (porque 3*3 - 1 = 8).*
```

```ad-question
title: Aplicación USD
Si empiezas con $5 USD ($a_1=5$) y cada día gastas $2 USD constantes, ¿cuál es tu diferencia ($d$)?
*Respuesta: d = -2 (porque disminuye).*
```

---

> [!tip] 💡 En la próxima clase
> Ahora que ya sabes encontrar cualquier término individual por más lejos que esté, aprenderemos a sumar todos los términos de una lista sin tener que sumarlos uno por uno. ¡Próximo tema: **Suma de Progresiones Aritméticas**!

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [[Inicio del Curso]] | ➡️ **Siguiente:** [[Clase 02 — Suma de Progresiones Aritméticas]]