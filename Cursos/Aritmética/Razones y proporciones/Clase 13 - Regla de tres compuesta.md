# Clase 13 — Compound Rule of Three | Example 1 + Compound Rule of Three | Example 2 + Regla de tres compuesta Ejemplo 3

#algebra #compoundruleoft
Curso: [[00 - Índice del curso]] | Bloque 3 | Lección 13 de 16

> [!info] 🧭 Navegación
> - Anterior: [[Clase 12 — Regla de tres simple inversa]]
> - Siguiente: [[Clase 14 — Proporcionalidad compuesta avanzada]]

> [!info] 🌍 Relevancia y aplicaciones
> La regla de tres compuesta es la herramienta definitiva para resolver problemas de proporcionalidad complejos donde intervienen tres o más variables que interactúan simultáneamente.
> - **Economía ($USD):** Cálculo de presupuestos y costos de operación de maquinaria basados en el tiempo y el número de unidades activas.
> - **Construcción e Ingeniería:** Planificación de tiempos de entrega considerando el número de obreros, las horas de jornada y el volumen de la obra (muros, metros cuadrados).
> - **Producción Industrial:** Optimización de líneas de ensamblaje en fábricas según la cantidad de operarios, horas de trabajo y metas de fabricación (ruedas, piezas, etc.).

---

> [!note] 📌 ¿Qué es la Regla de Tres Compuesta?
> Es un método matemático que se utiliza cuando tenemos **tres o más magnitudes** proporcionales. A diferencia de la regla simple, aquí comparamos una incógnita con varias variables al mismo tiempo para ver cómo afectan el resultado final.

> [!warning] ⚠️ Error común
> El error más grave es asumir que todas las relaciones son directas. Debes analizar cada variable de forma independiente con respecto a la incógnita. Recuerda: en variables como "obreros" y "días", a **más** trabajadores, **menos** tiempo (Relación Inversa). ¡No las operes todas igual!

> [!tip] 💡 Truco para recordarlo
> Para no fallar al plantear tu ecuación, usa esta rima:
> *"Si la relación es **Inversa**, la fracción se pone **de cabeza**; si la relación es **Directa**, la fracción se queda **derecha**."*

---

### Procedimiento Paso a Paso

```text
PASO 1: Identificar variables (se encuentran siempre al lado de los números).
PASO 2: Relacionar la variable de la incógnita (X) con las demás para 
        determinar si son Directas (+) o Inversas (-).
PASO 3: Plantear la ecuación: colocar la fracción de la incógnita a un lado
        del igual y el producto de las demás al otro (invirtiendo las inversas).
PASO 4: Simplificar (tachar ceros, sacar mitad o tercera) y resolver 
        mediante producto cruzado.
```

---

### Ejemplos Prácticos

> [!example] Ejemplo 1: Caso Básico (Grifos y Litros)
> **Problema:** 9 grifos abiertos durante 40 horas consumen 200 litros. ¿Cuántos litros consumen 15 grifos durante 9 horas?
> 1. **Variables:** Grifos (9, 15), Horas (40, 9), Litros (200, X).
> 2. **Relación:**
>    - Grifos $\uparrow$ $\to$ Litros $\uparrow$ (**Directa**)
>    - Horas $\uparrow$ $\to$ Litros $\uparrow$ (**Directa**)
> 3. **Ecuación:** $\frac{200}{x} = \frac{9}{15} \cdot \frac{40}{9}$
> 4. **Resolución:** Simplificamos el 9 arriba y abajo. Nos queda $\frac{200}{x} = \frac{40}{15}$. Al simplificar $\frac{40}{15}$ sacando quinta, tenemos $\frac{8}{3}$.
>    $200 \cdot 3 = 8 \cdot x \implies 600 = 8x \implies x = 75$.
> **Resultado:** 75 litros.

> [!example] Ejemplo 2: Caso Inverso (Obreros y Tiempo)
> **Problema:** 4 obreros trabajando 7 horas diarias construyen un muro en 3 días. ¿Cuántos días tardarán 2 obreros trabajando 6 horas diarias?
> 1. **Variables:** Obreros (4, 2), Horas (7, 6), Días (3, X).
> 2. **Relación:**
>    - Obreros $\downarrow$ $\to$ Días $\uparrow$ (**Inversa**)
>    - Horas $\downarrow$ $\to$ Días $\uparrow$ (**Inversa**)
> 3. **Ecuación:** Como ambas son inversas, las ponemos "de cabeza":
>    $\frac{3}{x} = \frac{2}{4} \cdot \frac{6}{7}$
> 4. **Resolución:** $\frac{3}{x} = \frac{12}{28} \implies \frac{3}{x} = \frac{3}{7}$. Por simple inspección, $x = 7$.
> **Resultado:** 7 días.

> [!example] Ejemplo 3: Caso Mixto (Fábrica de Ruedas)
> **Problema:** Una fábrica trabajando 8 horas diarias fabrica 2000 ruedas en 5 días. ¿Cuántos días tardarán en fabricar 3000 ruedas si trabajan 10 horas diarias?
> 1. **Variables y Mapeo:**
>    - **Horas:** de 8 a 10 ($\uparrow$). A más horas diarias, menos días de trabajo $\to$ **Inversa (-)**.
>    - **Ruedas:** de 2000 a 3000 ($\uparrow$). A más ruedas, más días de trabajo $\to$ **Directa (+)**.
>    - **Días:** 5 e Incógnita (X).
> 2. **Planteamiento:** $\frac{5}{x} = \frac{10}{8} \text{ (Invertida)} \cdot \frac{2000}{3000} \text{ (Igual)}$
> 3. **Simplificación (Estilo Profe Alex):**
>    - En $\frac{2000}{3000}$, tachamos tres ceros arriba y abajo: $\frac{2}{3}$.
>    - En $\frac{10}{8}$, sacamos mitad: $\frac{5}{4}$.
>    - La ecuación queda: $\frac{5}{x} = \frac{5}{4} \cdot \frac{2}{3} \implies \frac{5}{x} = \frac{10}{12}$.
>    - Simplificamos $\frac{10}{12}$ a $\frac{5}{6}$.
>    - $\frac{5}{x} = \frac{5}{6} \implies x = 6$.
> **Resultado:** 6 días.

> [!example] Ejemplo 4: Aplicación Financiera ($USD)
> **Problema:** El costo de mantener 9 máquinas operando durante 40 horas es de $200 USD. ¿Cuál será el costo de operar 15 máquinas durante 9 horas?
> 1. **Relación:** Ambas variables son Directas (A más máquinas o más tiempo, mayor es el gasto de operación).
> 2. **Ecuación:** $\frac{200}{x} = \frac{9}{15} \cdot \frac{40}{9}$
> 3. **Resolución:** Siguiendo la lógica del Ejemplo 1, $x = 75$.
> **Resultado:** $75 USD.

---

### Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Fácil (Directo-Directo)
> 1. Si 9 grifos en 40h consumen 200L, ¿cuántos litros consumirán 12 grifos en 6 horas?
> 2. 5 impresoras en 2 horas imprimen 100 hojas. ¿Cuántas hojas imprimen 10 impresoras en 4 horas?
> 3. 2 camiones transportan 20 toneladas en 4 viajes. ¿Cuántas toneladas llevan 3 camiones en 8 viajes?
> 4. 8 trabajadores recolectan 400kg de fruta en 5 horas. ¿Cuánto recolectan 4 trabajadores en 10 horas?

> [!abstract] 🟡 Nivel Medio (Mixto/Inverso)
> 1. 4 obreros trabajando 7h/día tardan 3 días en un muro. ¿Cuántos **días** tardarán 3 obreros trabajando 8h/día?
> 2. 6 máquinas fabrican 1000 piezas en 4 días. ¿Cuántos días tardan 3 máquinas en fabricar 500 piezas?
> 3. 10 pintores pintan una casa en 5 días trabajando 6h/día. ¿Cuántos días tardan 5 pintores trabajando 10h/día?
> 4. 4 grifos llenan 2 tanques en 12 horas. ¿En cuántas **horas** llenarán 6 grifos un total de 3 tanques?

> [!abstract] 🔴 Nivel Avanzado ($USD)
> 1. Si 5 trabajadores con un presupuesto de $1000 terminan una labor en 10 días, ¿cuántos días durarán 10 trabajadores si el presupuesto sube a $3000?
> 2. Mantener 8 máquinas encendidas 10 horas diarias cuesta $400. ¿Cuál es el costo de 12 máquinas encendidas 6 horas diarias?
> 3. Una empresa paga $1500 por transportar 50 paquetes a 100km. ¿Cuánto pagará por 80 paquetes a 200km?
> 4. 4 artesanos producen 20 joyas con un costo de material de $200. ¿Cuál es el costo de material para que 8 artesanos produzcan 50 joyas?

> [!success] ✅ Respuestas
> **Fácil:** 1) 40L | 2) 400 hojas | 3) 60 ton | 4) 400kg
> **Medio:** 1) 3.5 días | 2) 4 días | 3) 6 días | 4) 12 horas
> **Avanzado:** 1) 15 días | 2) $360 | 3) $4800 | 4) $500

---

### Quiz de Autoevaluación

> [!question] Pregunta 1: Conceptual
> ¿Cuándo se considera que una regla de tres es "compuesta"?
> A) Cuando solo tiene variables directas.
> B) Cuando intervienen 3 o más variables.
> C) Cuando la incógnita X es un número decimal.
> **Respuesta correcta: B.** La diferencia fundamental con la regla simple es la cantidad de magnitudes (más de dos) que afectan el resultado.

> [!question] Pregunta 2: Procedimental
> Si al relacionar la variable X con la variable "A" determinas que es **Inversa**, ¿qué debes hacer con la fracción de "A" al plantear la ecuación?
> **Respuesta:** Debes invertir la fracción (el denominador pasa a ser numerador y viceversa).
> *Explicación: Esto compensa matemáticamente el hecho de que una magnitud aumenta mientras la otra disminuye.*

> [!question] Pregunta 3: Aplicación $USD
> Si 2 máquinas gastan $10 de luz en 5 horas, ¿cuánto gastan 4 máquinas en las mismas 5 horas?
> **Respuesta:** $20.
> *Explicación: Al mantenerse el tiempo constante (5h), solo comparamos máquinas y costo. Al ser el doble de máquinas (relación directa), el costo se duplica.*

---

> [!tip] 💡 En la próxima clase
> En la **Clase 14**, llevaremos esto al siguiente nivel analizando problemas de proporcionalidad que incluyen el "rendimiento" de los trabajadores y la "dificultad" de la obra. ¡No te lo pierdas!

> [!info] 🧭 Navegación
> - Anterior: [[Clase 12 — Regla de tres simple inversa]]
> - Siguiente: [[Clase 14 — Proporcionalidad compuesta avanzada]]