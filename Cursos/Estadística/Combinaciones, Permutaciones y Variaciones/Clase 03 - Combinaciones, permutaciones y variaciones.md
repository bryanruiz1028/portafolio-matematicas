# Clase 03 — Combinaciones, permutaciones y variaciones

#algebra #combinationsper

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 6

> [!info] 🧭 Navegación
> - ⬅️ **Anterior**: [[Clase 02 — Factoriales y Principio Multiplicativo]]
> - ➡️ **Siguiente**: [[Clase 04 — Introducción a la Probabilidad]]

---

## 🎯 Importancia de la Combinatoria

La combinatoria es la herramienta matemática que nos permite contar de cuántas formas pueden suceder las cosas sin tener que escribirlas todas una por una. Como explica el Profe Alex, dominar estos conceptos te permite resolver situaciones reales como:

*   💵 **Premios con jerarquía:** Entender que en un concurso no es lo mismo ganar el premio de $100 USD (campeón) que el de $50 USD (subcampeón), pues el orden cambia tu suerte.
*   🏗️ **Organización de espacios:** Saber de cuántas formas pueden parquearse 4 autos en una fila o cómo Natalia y Alex pueden elegir asientos en un autobús (¿ventana o pasillo?).
*   📊 **Selección de grupos:** Calcular cuántos comités diferentes de 3 estudiantes se pueden formar en un salón de 10 personas para una reunión con el director.

---

## 💡 Concepto Clave

Para saber qué fórmula usar, solo debemos responder a una pregunta lógica: **¿Importa el orden?**

1.  **Combinación:** El orden **NO** importa. Si elegimos a Alex y a Blanca para un equipo, es el mismo equipo que si elegimos a Blanca y a Alex.
2.  **Variación y Permutación:** El orden **SÍ** importa. Si Alex es el Presidente y Blanca es la Secretaria, es un resultado totalmente distinto a que Blanca sea la Presidenta y Alex el Secretario.

> [!warning] El Error de los Balones
> Un error común es no analizar si los elementos son iguales o distintos. 
> - Si rifamos **2 balones de fútbol idénticos** entre 20 amigos, el orden no importa (es una combinación). 
> - Si rifamos **1 balón de baloncesto y 1 de voleibol**, el orden **SÍ** importa porque a Alex podría gustarle más el de voleibol y a Blanca el de baloncesto. ¡El premio es diferente!

> [!tip] Regla de Oro
> Memoriza esta frase: **"Combina = No importa el orden"**. Si al cambiar de lugar a los elementos el grupo sigue siendo el mismo, estás ante una combinación.

---

## 🛠️ Procedimiento Paso a Paso (Método de las Dos Preguntas)

Sigue este esquema lógico para no fallar nunca:

```text
PASO 1: ¿Importa el orden?
        - SÍ -> Es Variación o Permutación.
        - NO -> Es Combinación (nCr).

PASO 2: ¿Se usan TODOS los elementos?
        - SÍ -> Es Permutación (n!).
        - NO -> Es Variación (V n,r).

PASO 3: ¿Hay repetición?
        - Verificar si un elemento puede aparecer varias veces (como en una clave).
        - Verificar si hay elementos idénticos (como letras repetidas en una palabra).

PASO 4: Aplicar la fórmula o el "Método de las Cajitas".
```

---

## 📝 Ejemplos Resueltos

> [!example] Ejemplo 1: Formar un Comité (Combinación)
> **Problema:** De un grupo de 10 estudiantes se quiere seleccionar un comité de 3.
> 1. **¿Orden?** **NO** importa. El grupo {Alex, Blanca, Claudio} es el mismo que {Claudio, Blanca, Alex}.
> 2. **Fórmula ($nCr$):** $\frac{10!}{3! \times (10-3)!} = \frac{10!}{3! \times 7!}$
> 3. **Desarrollo:** $\frac{10 \times 9 \times 8 \times \cancel{7!}}{(3 \times 2 \times 1) \times \cancel{7!}} = \frac{720}{6} = \mathbf{120}$ formas.

> [!example] Ejemplo 2: Cargos Directivos (Variación)
> **Problema:** De 10 estudiantes se elige Presidente, Vicepresidente y Secretario.
> 1. **¿Orden?** **SÍ** importa (los puestos son diferentes).
> 2. **¿Todos?** **NO**, solo usamos 3 de los 10.
> 3. **Cálculo ($V_{10,3}$):** Usamos el método de las cajitas: $10 \times 9 \times 8 = \mathbf{720}$ formas.

> [!example] Ejemplo 3: Mesa Redonda (Permutación Circular)
> **Problema:** 5 amigos (Alex, Natalia, Blanca, Claudio y Diana) se sientan a jugar cartas en una mesa circular.
> 1. **Lógica:** En una mesa circular, si todos se mueven un puesto a la derecha, la posición relativa no cambia (Natalia sigue teniendo a Alex a un lado). Por eso "fijamos" a una persona.
> 2. **Fórmula ($P_c$):** $(n - 1)! = (5 - 1)! = 4!$
> 3. **Resultado:** $4 \times 3 \times 2 \times 1 = \mathbf{24}$ formas.

> [!example] Ejemplo 4: Palabra "MATEMÁTICAS" (Repetición)
> **Problema:** ¿Cuántas palabras diferentes se forman con sus letras?
> 1. **Total ($n$):** 11 letras.
> 2. **Repeticiones:** M (2), A (3), T (2).
> 3. **Cálculo detallado:**
>    $$\frac{11!}{2! \cdot 3! \cdot 2!} = \frac{11 \cdot 10 \cdot 9 \cdot 8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot \cancel{3!}}{(2 \cdot 1) \cdot \cancel{3!} \cdot (2 \cdot 1)}$$
>    $$\frac{6,652,800}{4} = \mathbf{1,663,200}$$ palabras.

---

## ✍️ Ejercicios para el Estudiante

### Nivel Fácil (Verde)
1. Seleccionar 2 libros de un estante que tiene 10 para leer en vacaciones.
2. Natalia debe elegir a 3 amigos de un grupo de 6 para realizar un trabajo escolar.
3. Blanca quiere preparar un jugo eligiendo 2 frutas de entre 5 disponibles.
4. ¿De cuántas formas se pueden elegir 3 representantes de un curso de 10 estudiantes?

### Nivel Medio (Amarillo)
5. ¿De cuántas formas pueden sentarse Natalia, Alex, Claudio, Diana, Esteban y Felipe en una fila de 6 asientos?
6. ¿Cuántas palabras de 4 letras (con o sin sentido) se forman con las letras de "LUNA"?
7. En una carrera donde compiten 5 estudiantes, ¿de cuántas formas pueden llegar a la meta en orden?
8. ¿De cuántas formas se pueden parquear 4 autos en una fila de 4 puestos disponibles?

### Nivel Avanzado (Red)
9. Se reparten dos premios en efectivo: $100 USD al primer lugar y $50 USD al segundo entre 10 participantes.
10. ¿Cuántos números de 5 cifras se forman con los dígitos {1, 2, 3, 4, 5} sin repetir ninguno?
11. ¿Cuántos números de 5 cifras se forman con los dígitos {1, 2, 3, 4, 5} si **SÍ** se permite repetir (ej: 11122)?
12. Formar números de 3 cifras distintas con {1, 2, 3, 4, 5} donde el **5 siempre esté en las decenas**.

---

> [!check] 🔑 Clave de Respuestas (Uso del Profesor)
> 1. **45** (Combinación) | 2. **20** (Combinación) | 3. **10** (Combinación) | 4. **120** (Combinación).
> 5. **720** (Permutación $6!$) | 6. **24** (Permutación $4!$) | 7. **120** (Permutación $5!$) | 8. **24** (Permutación $4!$).
> 9. **90** (Variación $10 \times 9$) | 10. **120** ($5!$) | 11. **3,125** ($5 \times 5 \times 5 \times 5 \times 5$) | 12. **12** (Cajitas: $4 \times 1 \times 3$).

---

## 🧠 Autoevaluación

**1. ¿Cuál es la diferencia fundamental entre combinación y variación?**
*Respuesta:* En la variación el orden de los elementos crea un resultado distinto (como puestos de trabajo), en la combinación el orden no cambia el grupo (como un equipo de amigos).

**2. En un campeonato de 8 equipos, ¿de cuántas formas se pueden ganar los premios de campeón y subcampeón?**
*Respuesta:* Es una variación (el orden importa). Se calcula como $V_{8,2} = 8 \times 7 = \mathbf{56}$ formas.

**3. Si rifamos dos premios de $100 USD cada uno (iguales) entre 10 personas, ¿es combinación o variación?**
*Respuesta:* Es una **combinación**, porque al ser premios idénticos, no importa si te eligen de primero o de segundo; el resultado para ti es el mismo.

---

**Próxima lección:** Ahora que sabes contar posibilidades, aprenderás a calcular la probabilidad de que estas ocurran.

> [!info] 🧭 Navegación
> - ⬅️ **Anterior**: [[Clase 02 — Factoriales y Principio Multiplicativo]]
> - ➡️ **Siguiente**: [[Clase 04 — Introducción a la Probabilidad]]