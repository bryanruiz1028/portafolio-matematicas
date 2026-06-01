# Clase 03 — Ecuaciones Trigonométricas | Ejemplo 1

#algebra #trigonometriceq
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 3

> [!info] 🧭 Navegación
> [[Clase 02 — Introducción]] ← Anterior | Siguiente → [[Clase 04 — Ecuaciones Cuadráticas e Identidades]]

---

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> Las funciones trigonométricas modelan fenómenos cíclicos que se repiten en intervalos regulares. Resolver estas ecuaciones permite identificar los momentos exactos en los que un sistema alcanza un estado crítico o un valor objetivo.
> 
> * **💵 Aplicación $USD:** En el trading, el precio de activos suele oscilar en patrones senoidales; resolver la ecuación permite detectar niveles de soporte y resistencia (puntos de entrada/salida).
> * **🏗️ Aplicación práctica:** Los ingenieros civiles calculan ángulos de soporte para estructuras que vibran o se balancean, asegurando la estabilidad bajo cargas periódicas.
> * **📊 Situación cotidiana:** Determinar en qué segundo un columpio o una noria alcanza su altura máxima o mínima es, en esencia, resolver una ecuación trigonométrica.

---

## Concepto Clave

> [!note] **¿Qué es una ecuación trigonométrica?**
> Imagina una caja fuerte cuya combinación es un ángulo secreto ($x$), pero este ángulo está "atrapado" dentro de una función ($Seno, Coseno,$ etc.). Resolver la ecuación es encontrar la combinación exacta que hace que la función devuelva el valor necesario para abrir la caja. 
> 
> Para lograrlo, debemos entender el **Ángulo en Posición Normal**: la medida siempre se inicia desde el semieje positivo de las $x$. El valor que buscamos suele tener dos "llaves" o soluciones dentro de un círculo completo.

> [!warning] **¡No olvides la segunda solución!**
> Un error crítico es conformarse con el primer ángulo que arroja la calculadora. Debido a la simetría del círculo trigonométrico, casi siempre existen dos ángulos entre $0^\circ$ y $360^\circ$ que comparten el mismo valor de seno o coseno.

> [!tip] **Regla Mnemotécnica: "Todas Sin Tacos"**
> Te ayuda a saber dónde las funciones son **positivas**:
> * **Todas**: I Cuadrante (Todas son positivas).
> * **Sin**: II Cuadrante (**Sen**o es positivo).
> * **Ta**: III Cuadrante (**Tan**gente es positiva).
> * **Cos**: IV Cuadrante (**Cos**eno es positivo).

---

## Procedimiento Paso a Paso

Para resolver ecuaciones con una sola función trigonométrica, aplica este algoritmo:

```text
PASO 1: Despejar la función trigonométrica (dejarla sola a un lado de la igualdad).
PASO 2: Identificar el ángulo notable en la tabla (este será nuestro ángulo de referencia θ).
PASO 3: Ubicar los cuadrantes según el signo y aplicar fórmulas de reducción:
        - Si es Seno (+) en II Cuadrante: 180° - θ
        - Si es Coseno (+) en IV Cuadrante: 360° - θ
        - Si es Seno (-) en III Cuadrante: 180° + θ
PASO 4: Verificar resultados sustituyendo los ángulos en la ecuación original.
```

---

## Ejemplos de Clase

> [!example] **Ejemplo 1: Caso Básico (Seno)**
> **Ecuación:** $2 \sin(x) + 3 = 4$
> 1. **Despeje:** $2 \sin(x) = 4 - 3 \implies \sin(x) = 1/2$.
> 2. **Ángulo notable:** El seno es $1/2$ a los $30^\circ$ ($\pi/6$).
> 3. **Segunda solución:** El seno es positivo en el I y II cuadrante. 
>    - I Cuadrante: $30^\circ$
>    - II Cuadrante: $180^\circ - 30^\circ = 150^\circ$ ($5\pi/6$).
> **Resultado:** $x_1 = 30^\circ$ ($\pi/6$), $x_2 = 150^\circ$ ($5\pi/6$).

> [!example] **Ejemplo 2: Caso con Coseno**
> **Ecuación:** $2 \cos(x) = \sqrt{2}$
> 1. **Despeje:** $\cos(x) = \sqrt{2}/2$.
> 2. **Ángulo notable:** El coseno es $\sqrt{2}/2$ a los $45^\circ$ ($\pi/4$).
> 3. **Segunda solución:** El coseno es positivo en el I y IV cuadrante. 
>    - I Cuadrante: $45^\circ$
>    - IV Cuadrante: $360^\circ - 45^\circ = 315^\circ$ ($7\pi/4$).
> **Resultado:** $x_1 = 45^\circ$ ($\pi/4$), $x_2 = 315^\circ$ ($7\pi/4$).

> [!example] **Ejemplo 3: Caso con Simplificación**
> **Ecuación:** $4 \sin(\theta) + 5 = 7$
> 1. **Despeje:** $4 \sin(\theta) = 2 \implies \sin(\theta) = 2/4 = 1/2$.
> 2. **Resultado:** Al reducirse a $\sin(\theta) = 1/2$, las soluciones son idénticas al Ejemplo 1: $30^\circ$ ($\pi/6$) y $150^\circ$ ($5\pi/6$).

---

## Ejercicios para el Estudiante

**🟢 Nivel Verde (Fácil)**
1. $\sin(x) = 1$
2. $2 \cos(x) = 1$
3. $\cos(x) = 0$
4. $2 \sin(x) = \sqrt{3}$

**🟡 Nivel Amarillo (Medio)**
5. $2 \sin(x) - 1 = 0$
6. $2 \cos(x) - \sqrt{2} = 0$
7. $2 \sin(x) + \sqrt{3} = 0$
8. $4 \cos(x) - 2 = 0$

**🔴 Nivel Rojo (Avanzado $USD)**
9. El costo de una pieza metálica es $C(x) = 2 \cos(x) + 5$. Halla $x$ para que el costo sea $6.00$ USD.
10. Un ingreso digital se define como $I(x) = 4 \sin(x) + 10$. Halla $x$ para un ingreso de $12.00$ USD.
11. Determina el ángulo de producción si $2 \sin(x) + 1 = 1 + \sqrt{3}$ (Ayuda: $\sin(x) = \sqrt{3}/2$).
12. Halla el equilibrio de fuerzas si $2 \cos(x) + 4 = 4 + \sqrt{3}$.

> [!success] **Respuestas para el Docente (Grados y Radianes)**
> 1. $90^\circ$ ($\pi/2$)
> 2. $60^\circ, 300^\circ$ ($\pi/3, 5\pi/3$)
> 3. $90^\circ, 270^\circ$ ($\pi/2, 3\pi/2$)
> 4. $60^\circ, 120^\circ$ ($\pi/3, 2\pi/3$)
> 5. $30^\circ, 150^\circ$ ($\pi/6, 5\pi/6$)
> 6. $45^\circ, 315^\circ$ ($\pi/4, 7\pi/4$)
> 7. $240^\circ, 300^\circ$ ($4\pi/3, 5\pi/3$)
> 8. $60^\circ, 300^\circ$ ($\pi/3, 5\pi/3$)
> 9. $60^\circ, 300^\circ$ ($\pi/3, 5\pi/3$)
> 10. $30^\circ, 150^\circ$ ($\pi/6, 5\pi/6$)
> 11. $60^\circ, 120^\circ$ ($\pi/3, 2\pi/3$)
> 12. $30^\circ, 330^\circ$ ($\pi/6, 11\pi/6$)

---

## Mini-Prueba de Autoevaluación

1. **¿Por qué hay dos soluciones para $\sin(x) = 1/2$ en el intervalo $[0^\circ, 360^\circ]$?**
   - *Respuesta:* Porque el seno representa la coordenada $y$ en el círculo unitario, y existen dos puntos (uno en el I cuadrante y otro en el II) que tienen la misma altura positiva.
2. **Si el ángulo de referencia es $45^\circ$ y el coseno es positivo, ¿cuál es la solución en el IV cuadrante?**
   - *Respuesta:* $315^\circ$. Se aplica la fórmula $360^\circ - 45^\circ = 315^\circ$.
3. **En la ecuación de precio $P(x) = 2 \cos(x) + 10$, ¿qué ángulos dan un precio de $11$ USD?**
   - *Respuesta:* $60^\circ$ y $300^\circ$. Al despejar, $\cos(x) = 1/2$, que corresponde a $60^\circ$ (I cuad.) y $360^\circ-60^\circ = 300^\circ$ (IV cuad.).

---

## Notas Finales y Cierre

> [!tip] 💡 En la próxima clase
> Subiremos el nivel. Veremos cómo resolver **ecuaciones trigonométricas cuadráticas** (ej. $\sin^2(x)$) y cómo usar **identidades fundamentales** para reducir ecuaciones complejas antes de iniciar el despeje.

> [!info] 🧭 Navegación
> [[Clase 02 — Introducción]] ← Anterior | Siguiente → [[Clase 04 — Ecuaciones Cuadráticas e Identidades]]