# Clase 03 — Simplificación y Verificación de Identidades Trigonométricas

#algebra #identidadestrig
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 3 de 5

> [!info] 🧭 Navegación
> - Anterior: [[Clase 02 — Identidades Fundamentales]]
> - Siguiente: [[Clase 04 — Identidades de Ángulos Dobles]]

---

## Relevancia y Aplicaciones (Mundo Real)

La simplificación de expresiones no es solo un ejercicio escolar; es la base de la **optimización**. En el mundo real, cada operación matemática que realiza una computadora consume energía y tiempo. Reducir una fórmula gigante a una pequeña hace que la tecnología sea más barata y rápida.

- **💵 Aplicación con $USD:** En software financiero y de procesamiento de señales, optimizar funciones trigonométricas reduce los "ciclos de CPU". Menos procesamiento significa menos consumo de energía y menores facturas en servicios de la nube como AWS o Azure, ahorrando miles de dólares en servidores.
- **🏗️ Aplicación práctica:** En ingeniería civil, al calcular las tensiones en los cables de un puente colgante, simplificar las identidades permite a los ingenieros trabajar con valores exactos, evitando errores acumulados que podrían comprometer la estructura.
- **📊 Situación cotidiana:** Los archivos **MP3**. La música digital es una suma de miles de ondas trigonométricas. Los algoritmos de compresión simplifican estas expresiones para eliminar datos que el oído humano no nota, logrando que el archivo pese 10 veces menos.

---

## Concepto Clave

**Definición:** Simplificar una identidad es como "traducir" una frase larga a una sola palabra que significa lo mismo. Imagina que alguien te dice: *"El hijo de la hermana de mi madre"*. Tú, automáticamente, simplificas esa frase a: *"Mi primo"*. En trigonometría, hacemos lo mismo: tomamos una expresión larga y confusa para llegar a una forma mucho más eficiente de calcular.

> [!warning] ⚠️ Error común: El límite de los exponentes
> Según el Profe Alex, debes tener mucho cuidado:
> 1. Las **identidades pitagóricas** (como $\sin^2(x) + \cos^2(x) = 1$) **solo** funcionan si el exponente es **2**. No intentes aplicarlas a $\sin^4(x) + \cos^4(x)$.
> 2. Las **identidades recíprocas** (como $\csc(x) = 1/\sin(x)$) son más flexibles: funcionan para cualquier exponente, siempre que lo apliques a ambos lados (ej: $\csc^3(x) = 1/\sin^3(x)$).

> [!tip] 💡 Truco de Experto
> El consejo de oro del Profe Alex: Si no sabes por dónde empezar, **pasa todo a Senos y Cosenos**. Es el "idioma universal" de la trigonometría y suele desbloquear el 90% de los ejercicios.

---

## Procedimiento Paso a Paso

Para trabajar como un profesional, sigue esta secuencia técnica:

```text
PASO 0 → Preparación: Ten a la mano tu "hoja de trucos" con las identidades fundamentales si aún no las memorizas.
PASO 1 → Elección: Elige el lado más complejo (el más largo o con más términos) de la igualdad para empezar a trabajar.
PASO 2 → Traducción: Convierte tangentes, secantes y demás funciones a senos y cosenos.
PASO 3 → Álgebra: Realiza operaciones como la "Carita Feliz" (suma de fracciones) o la "Ley de la Oreja" (extremos y medios).
PASO 4 → Sustitución: Aplica identidades pitagóricas para reducir el resultado a su mínima expresión.
```

---

## Ejemplos

> [!example] Ejemplo 1: El Caso Básico
> **Demostrar:** $\cos^2(A) - \sin^2(A) = 2\cos^2(A) - 1$
> 1. **Estrategia:** El lado izquierdo es más complejo. Como el lado derecho solo tiene cosenos, debemos "eliminar" el seno.
> 2. **Sustitución:** Sabemos que $\sin^2(A) = 1 - \cos^2(A)$.
> 3. **Operación:** $\cos^2(A) - (1 - \cos^2(A))$.
> 4. **Resultado:** $\cos^2(A) - 1 + \cos^2(A) = 2\cos^2(A) - 1$. **¡Verificado!**

> [!example] Ejemplo 2: El Peligro del Signo Negativo
> **Demostrar:** $1 - \sin^2(\theta) - \sin^2(\theta) = 1 - 2\sin^2(\theta)$
> *Nota Didáctica:* El Profe Alex enfatiza que cuando sustituyes una identidad en una resta, **el uso de paréntesis/corchetes es obligatorio**.
> 1. Si tuviéramos que cambiar un término por un binomio, el signo negativo de afuera cambiará todos los signos de adentro.
> 2. En este caso, simplemente agrupamos términos semejantes: $-1\sin^2(\theta) - 1\sin^2(\theta) = -2\sin^2(\theta)$.
> 3. Resultado: $1 - 2\sin^2(\theta)$.

> [!example] Ejemplo 3: Caso Avanzado (Fracciones)
> **Simplificar:** $\frac{\tan(a) - \cot(a)}{\tan(a) + \cot(a)}$
> 1. **Pasar a Sen/Cos:** $\frac{\frac{\sin(a)}{\cos(a)} - \frac{\cos(a)}{\sin(a)}}{\frac{\sin(a)}{\cos(a)} + \frac{\cos(a)}{\sin(a)}}$
> 2. **Carita Feliz (Numerador):** $\frac{\sin^2(a) - \cos^2(a)}{\cos(a)\sin(a)}$
> 3. **Carita Feliz (Denominador):** $\frac{\sin^2(a) + \cos^2(a)}{\cos(a)\sin(a)}$
> 4. **Ley de la Oreja (Extremos y Medios):** Al multiplicar $(\sin^2(a) - \cos^2(a)) \cdot (\cos(a)\sin(a))$ arriba y $(\cos(a)\sin(a)) \cdot (\sin^2(a) + \cos^2(a))$ abajo, los términos $(\cos(a)\sin(a))$ se cancelan por completo.
> 5. **Simplificación Final:** Nos queda $\frac{\sin^2(a) - \cos^2(a)}{1}$ (porque $\sin^2(a) + \cos^2(a) = 1$).
> 6. **Resultado:** $\sin^2(a) - \cos^2(a)$.

> [!example] Ejemplo 4: Aplicación $USD (Eficiencia de Software)
> Un servidor de AWS cobra por tiempo de procesamiento. Un software mal optimizado calcula el costo como $C = 100 \times (\sin^2(x) + \cos^2(x))$ millones de veces.
> 1. Si el software calcula cada función por separado, gasta 10 milisegundos de CPU.
> 2. Si simplificamos usando la identidad pitagórica: $\sin^2(x) + \cos^2(x) = 1$.
> 3. El costo simplificado es $C = 100 \times (1) = 100$ USD.
> 4. **Impacto técnico:** Al ser una constante, el procesador no gasta tiempo en cálculos trigonométricos, reduciendo el consumo eléctrico y la factura mensual en dólares.

---

## Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Verde (Fácil)
> Verifique las siguientes identidades:
> 1. $\tan(x) \cdot \cos(x) = \sin(x)$
> 2. $\cot(x) \cdot \sin(x) = \cos(x)$
> 3. $\sec(x) \cdot \cos(x) = 1$
> 4. $\csc(x) \cdot \sin(x) = 1$

> [!abstract] 🟡 Nivel Amarillo (Medio)
> Resuelva las sumas de fracciones y simplifique aplicando "Carita Feliz":
> 5. $\frac{1}{\cos(x)} + \frac{1}{\sin(x)}$
> 6. $\cos(A) + \frac{\sin^2(A)}{\cos(A)}$
> 7. $\frac{\sin(x)}{\cos(x)} + \frac{\cos(x)}{\sin(x)}$
> 8. $(\sin(\theta) + \cos(\theta))^2$ *(Recuerda: $a^2 + 2ab + b^2$)*

> [!abstract] 🔴 Nivel Rojo (Avanzado)
> Determine el costo final en $USD simplificando las expresiones para ahorrar CPU:
> 9. Costo $C = 50 \cdot (\sec^2(x) - \tan^2(x))$
> 10. Costo $C = 20 \cdot (\frac{\sin(x)}{\cos(x)} \cdot \cot(x))$
> 11. Costo $C = 15 \cdot (\sin^2(x) + \cos^2(x) + \tan(x)\cot(x))$
> 12. Costo $C = 200 \cdot (1 - \sin^2(x)) \cdot \sec^2(x)$

---

## Respuestas

> [!success] Solucionario Directo
> 1. $\sin(x) = \sin(x)$ | 2. $\cos(x) = \cos(x)$ | 3. $1 = 1$ | 4. $1 = 1$
> 5. $\frac{\sin(x)+\cos(x)}{\sin(x)\cos(x)}$ | 6. $\sec(A)$ | 7. $\frac{1}{\sin(x)\cos(x)}$ | 8. $1 + 2\sin(\theta)\cos(\theta)$
> 9. **50 USD** (porque $\sec^2 - \tan^2 = 1$) | 10. **20 USD** | 11. **30 USD** ($1 + 1$) | 12. **200 USD** ($\cos^2 \cdot \sec^2 = 1$)

---

## Mini-Prueba de Autoevaluación

> [!question] Pregunta 1
> Según el Profe Alex, ¿por qué es mejor empezar por el lado más complejo?
> **Respuesta:** Porque es más fácil "destruir" o simplificar una estructura grande que intentar "construir" algo complejo a partir de un solo término.

> [!question] Pregunta 2
> ¿Cuál es la única condición para aplicar la identidad $\sin^2(x) + \cos^2(x) = 1$ según los exponentes?
> **Respuesta:** El exponente debe ser exactamente 2.

> [!question] Pregunta 3 (Aplicación $USD)
> Si una aplicación móvil realiza la operación $\sec(x) \cdot \cos(x)$ cada vez que un usuario hace scroll, y simplificarla ahorra $1 USD de servidor al mes, ¿cuánto es el valor simplificado?
> **Respuesta:** El valor es 1 USD, ya que $\frac{1}{\cos(x)} \cdot \cos(x) = 1$.

---

**Próxima Clase:** En la [[Clase 04 — Identidades de Ángulos Dobles]] aprenderemos qué hacer cuando el ángulo no es simplemente $x$, sino $2x$. ¡Prepárate para expandir tu caja de herramientas!

> [!info] 🧭 Navegación
> - Anterior: [[Clase 02 — Identidades Fundamentales]]
> - Siguiente: [[Clase 04 — Identidades de Ángulos Dobles]]