# Clase 04 — Demostración y Verificación de Identidades Trigonométricas

#algebra #proveandchecktr

Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 4 de 5

> [!info] 🧭 Navegación
> ◀ **Anterior**: [[Clase 03 — Introducción a Identidades]]
> 🔼 **Índice**: [[00 - Índice del curso]]
> ▶ **Siguiente**: [[Clase 05 — Identidades de Ángulo Doble y Suma]]

---

> [!info] 🌍 Relevancia y aplicaciones
> Las identidades trigonométricas son como "superpoderes" matemáticos que nos permiten simplificar ecuaciones gigantes en la ingeniería y la física de ondas, haciendo que los cálculos complejos se vuelvan sencillos.
> 
> * **💵 $USD:** Imagina que tienes billetes de muchos países; simplificar una identidad es como convertir todas esas divisas a una moneda base ($USD) para saber exactamente cuánto dinero tienes sin complicarte.
> * **🏗️ Aplicación:** Los ingenieros las usan para calcular cómo se distribuyen las fuerzas en puentes y grandes edificios.
> * **📊 Situación cotidiana:** Sin estas identidades, las señales de tu GPS o el Wi-Fi serían lentas y ruidosas; la trigonometría ayuda a limpiar y optimizar esas ondas.

---

> [!note] 📌 ¿Qué es Prove and Check Trigonometric Identities?
> ¡Es como un juego de detectives! Debes demostrar que dos expresiones matemáticas que *parecen* diferentes son, en realidad, el mismo valor. Para lograrlo, usaremos reglas especiales de trigonometría para transformar una en la otra.

> [!warning] ⚠️ Error común
> **❌ Incorrecto:** Tratar de "despejar" moviendo términos de un lado al otro del igual (como pasar algo que suma a restar) como si fuera una ecuación normal.
> **✅ Correcto:** Debes trabajar **solo en un lado** de la igualdad (el más difícil) y transformarlo paso a paso hasta que se vea exactamente igual al otro lado.
> 
> **Punto clave:** ¡Cuidado con los signos! No es lo mismo $(a+b)^2$ (donde el término medio es $+2ab$) que $(a-b)^2$ (donde el término medio es $-2ab$).

> [!tip] 💡 Truco para recordarlo
> 1. **"¡Pásalo todo a Seno y Coseno!"**: Si te quedas bloqueado, esta regla casi siempre te salvará la vida.
> 2. **La Propiedad Conmutativa**: Recuerda que en la suma el orden no altera el resultado. $1 + \tan^2\theta$ es exactamente lo mismo que $\tan^2\theta + 1$. ¡No dejes que el orden te confunda!

---

### 📋 Procedimiento Paso a Paso

Para que nunca te pierdas en el bosque de la trigonometría, sigue este mapa de 4 pasos:

```text
PASO 1 → ¡Busca el lado que parezca un monstruo! (Identifica el lado más complejo).
PASO 2 → Aplica identidades fundamentales (Pitagóricas o Recíprocas) para reducir términos.
PASO 3 → Usa el álgebra: resuelve fracciones, potencias o productos notables.
PASO 4 → Simplifica hasta que ambos lados de la igualdad sean hermanos gemelos.
```

---

### 📝 Bloques de Ejemplos

> [!example] Ejemplo 1: Simplificación con Secantes (Fuente 1)
> **Verificar:** $\frac{1}{1 + \tan^2\theta} = \cos^2\theta$
> 
> 1. **Lógica de decisión:** Tenemos dos opciones para cambiar $\tan^2\theta$. ¿Usamos $1/\cot^2\theta$ o $\sec^2\theta - 1$? Elegimos la identidad que involucra **Secante** porque reduce dos términos ($1 + \tan^2\theta$) a uno solo ($\sec^2\theta$), haciendo todo más pequeño.
> 2. Como $1 + \tan^2\theta = \sec^2\theta$, la expresión queda: $\frac{1}{\sec^2\theta}$.
> 3. Usamos la identidad recíproca: $\sec^2\theta = \frac{1}{\cos^2\theta}$.
> 4. Aplicamos la **Ley de la Oreja** (Extremos y Medios) para dividir:
>    $$\frac{\frac{1}{1}}{\frac{1}{\cos^2\theta}}$$
>    *   **Extremos (arriba y abajo):** $1 \cdot \cos^2\theta = \cos^2\theta$
>    *   **Medios (los del centro):** $1 \cdot 1 = 1$
> 5. **Resultado:** $\frac{\cos^2\theta}{1} = \cos^2\theta$. ¡Identidad verificada!

> [!example] Ejemplo 2: El Binomio al Cuadrado (Fuente 2)
> **Verificar:** $(\sin A + \cos A)^2 = 1 + 2\sin A \cos A$
> 
> 1. Expandimos el binomio usando $(a + b)^2 = a^2 + 2ab + b^2$:
>    $$\sin^2 A + 2\sin A \cos A + \cos^2 A$$
> 2. **Ordenamos:** Gracias a la propiedad conmutativa, agrupamos los cuadrados:
>    $(\sin^2 A + \cos^2 A) + 2\sin A \cos A$
> 3. **Identidad Pitagórica:** Sabemos que $\sin^2 A + \cos^2 A = 1$.
> 4. Sustituimos y obtenemos: $1 + 2\sin A \cos A$. ¡Son iguales!

> [!example] Ejemplo 3: Reduciendo el paréntesis (Fuente 3)
> **Verificar:** $\cos^2 B (\sec^2 B - 1) = \sin^2 B$
> 
> 1. **Estrategia:** Siempre que veas un binomio como $(\sec^2 B - 1)$, busca si existe una identidad que lo convierta en un solo término. ¡Sí existe! $\tan^2 B = \sec^2 B - 1$.
> 2. Sustituimos: $\cos^2 B \cdot \tan^2 B$.
> 3. Aplicamos el truco maestro: pasamos la tangente a senos y cosenos:
>    $\cos^2 B \cdot \left( \frac{\sin^2 B}{\cos^2 B} \right)$
> 4. El $\cos^2 B$ que multiplica se cancela con el que divide.
> 5. **Resultado:** $\sin^2 B$. ¡Misión cumplida!

> [!example] Ejemplo 4: Aplicación Financiera ($USD)
> **Problema:** El costo de procesar una criptomoneda $C$ depende de la fluctuación del mercado $\theta$ según: $C = 100 \cdot [\sin^2(\theta) + \cos^2(\theta)]$. Demuestra que el costo es constante.
> 
> 1. Observamos el corchete: $[\sin^2(\theta) + \cos^2(\theta)]$.
> 2. Por la identidad pitagórica fundamental, esta suma siempre es igual a $1$, sin importar el ángulo.
> 3. Entonces: $C = 100 \cdot (1)$.
> 4. **Resultado:** El costo es siempre **$100 USD**. El mercado puede moverse, pero tu tarifa es fija.

---

### ✍️ Ejercicios para el Estudiante

🟢 **Fácil (Nivel 1)**
1. Demuestra que $\frac{\sin^2(x)}{1 - \cos^2(x)} = 1$.
2. Verifica que $\cos \theta \cdot \sec \theta = 1$.

🟡 **Medio (Nivel 2)**
3. Verifica la identidad $(\sin A - \cos A)^2 = 1 - 2\sin A \cos A$. (¡Ojo con el signo!).
4. Demuestra que $\tan^2 \alpha \cdot \cos^2 \alpha + \cos^2 \alpha = 1$.

🔴 **Avanzado (Nivel 3)**
5. Un programa de lealtad te da un bono $B$ en $USD calculado así: $B = 500 \cdot \frac{\tan^2 \theta}{\sec^2 \theta - 1}$. Demuestra que siempre recibirás **$500 USD**.

> [!success] ✅ Respuestas
> 1. Como $\sin^2 x + \cos^2 x = 1$, entonces $1 - \cos^2 x = \sin^2 x$. La fracción queda $\sin^2 x / \sin^2 x = 1$.
> 2. $\sec \theta$ es $1/\cos \theta$. Al multiplicar $\cos \theta \cdot (1/\cos \theta)$, se cancelan y queda $1$.
> 3. Al expandir el binomio $(a-b)^2$, el término central es negativo: $\sin^2 A - 2\sin A \cos A + \cos^2 A$. Luego $1 - 2\sin A \cos A$.
> 4. $\tan^2 \alpha \cdot \cos^2 \alpha$ se convierte en $\sin^2 \alpha$. Luego $\sin^2 \alpha + \cos^2 \alpha = 1$.
> 5. **Explicación:** Usamos la identidad pitagórica $\tan^2 \theta = \sec^2 \theta - 1$. Por lo tanto, el denominador $\sec^2 \theta - 1$ es igual al numerador $\tan^2 \theta$. Cualquier cantidad dividida entre sí misma es $1$. $500 \cdot 1 = 500 USD$.

---

### 🧠 Mini-Prueba de Autoevaluación

> [!question] Pregunta 1
> ¿Cuál de estas expresiones es equivalente a $1$ gracias a las identidades pitagóricas?
> a) $\sin A + \cos A$
> b) $\sec^2 A - \tan^2 A$
> c) $\tan A \cdot \cot A$
> d) $\sin^2 A - \cos^2 A$

> [!question] Pregunta 2
> Si expandes $(\sin \theta + \cos \theta)^2$, ¿cuál es el término que acompaña al $1$?
> a) $\sin \theta \cos \theta$
> b) $2 \sin \theta$
> c) $2 \sin \theta \cos \theta$
> d) $\sin^2 \theta$

> [!question] Pregunta 3
> Tu saldo en $USD es $200 \cdot [\frac{1}{\csc^2 \theta} + \cos^2 \theta]$. ¿Cuánto dinero tienes?
> a) $100 USD
> b) $200 USD
> c) $400 USD
> d) No se puede saber sin $\theta$.
> 
> *Pista: Recuerda que $1/\csc^2 \theta$ es lo mismo que $\sin^2 \theta$.*

---

**Nota final:** ¡Excelente trabajo hoy! Has dominado el arte de transformar expresiones. En la próxima clase, aprenderemos las identidades de **ángulo doble y suma**, que te permitirán romper ángulos grandes en piezas pequeñas y fáciles.

> [!info] 🧭 Navegación
> ◀ **Anterior**: [[Clase 03 — Introducción a Identidades]]
> 🔼 **Índice**: [[00 - Índice del curso]]
> ▶ **Siguiente**: [[Clase 05 — Identidades de Ángulo Doble y Suma]]