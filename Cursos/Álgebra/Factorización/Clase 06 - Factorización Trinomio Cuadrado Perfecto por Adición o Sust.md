# Clase 06 — Factorización: Trinomio Cuadrado Perfecto por Adición o Sustracción y Suma o Diferencia de Cubos

#algebra #factoringaperfe

[[Clase 05](Clase05)] | [[Índice](Índice)] | [[Clase 07](Clase07)]

---

> [!info] **¿Por qué dominar estos métodos?**
> ¡Hola, equipo! Hoy vamos a aprender herramientas de "cirugía algebraica". Estos métodos nos permiten desarmar expresiones complejas que los ingenieros usan para calcular la estabilidad de un puente o que los programadores emplean para que un software corra más rápido.
> - 💵 **Aplicación con $USD**: En el mundo financiero, estas factorizaciones sirven para modelar el crecimiento de capital cuando los intereses varían en potencias pares, permitiendo ver qué parte del dinero es capital base y qué parte es ganancia acumulada.
> - 🏗️ **Aplicación práctica**: En ingeniería, se usan para encontrar puntos de equilibrio donde las fuerzas de una estructura se cancelan y todo se mantiene firme.
> - 📊 **Situación cotidiana**: Al optimizar código, simplificar una expresión ahorra miles de operaciones por segundo a un procesador.

---

### 💡 Conceptos Clave para el Éxito

> [!note] **El Método de "Completación"**
> El Trinomio Cuadrado Perfecto (TCP) por Adición o Sustracción se usa cuando tenemos tres términos y los extremos son "perfectos" (tienen raíz cuadrada exacta), pero el centro no nos da el doble producto que necesitamos. Nuestra misión es "prestarle" al trinomio lo que le falta para que sea perfecto.

> [!tip] **Regla Mnemotécnica del Profe**
> **"Lo que prestas, lo devuelves y debe ser cuadrado"**. 
> Si sumas algo para completar el trinomio (el préstamo), debes restarlo al final (devolverlo). Para que el truco funcione, eso que restas **debe** tener raíz cuadrada exacta.

> [!warning] **¡Cuidado con el equilibrio!**
> El error más común de los estudiantes es sumar la cantidad necesaria y olvidar restarla al final. Si sumas $+4a^2$ y no restas $-4a^2$, ¡has cambiado toda la ecuación! Mantén siempre la balanza equilibrada.

---

### 📝 ¡Manos a la obra! Tu receta para el éxito

Antes de empezar cualquier ejercicio, aplica este protocolo de "inspección profesional":

```text
PASO 0 (EL DIAGNÓSTICO): Verifica si hay Factor Común y ORDENA la expresión de mayor a menor exponente.
1. HALLAR RAÍCES: Saca la raíz cuadrada del primer y tercer término.
2. VERIFICACIÓN MENTAL: Multiplica ambas raíces por 2. Si este resultado NO es igual al centro, 
   calcula cuánto le falta (o le sobra) para llegar a ese número.
3. COMPLETAR EL BALANCE: Suma la diferencia necesaria y réstala al final de la expresión.
4. LA DOBLE FACTORIZACIÓN:
   a) Factoriza el trinomio resultante como un (Binomio)².
   b) Aplica Diferencia de Cuadrados para obtener el resultado final.
```

---

### 🏫 Ejemplos de Clase

> [!example] **Ejemplo 1: El Caso Básico**
> Factorizar: $4a^4 + 8a^2b^2 + 9b^4$
> 1. **Paso 0**: Está ordenado y no hay factor común. ¡Vamos!
> 2. **Raíces**: $\sqrt{4a^4} = 2a^2$ y $\sqrt{9b^4} = 3b^2$.
> 3. **Diagnóstico**: El doble producto debería ser $2 \cdot (2a^2) \cdot (3b^2) = 12a^2b^2$. 
>    *Problema*: Tenemos $8a^2b^2$. Nos faltan $4a^2b^2$ para llegar a 12.
> 4. **Ajuste**: Sumamos $4a^2b^2$ y lo restamos al final.
>    $(4a^4 + 8a^2b^2 + 4a^2b^2 + 9b^4) - 4a^2b^2 \rightarrow (4a^4 + 12a^2b^2 + 9b^4) - 4a^2b^2$
> 5. **Factorización**:
>    $(2a^2 + 3b^2)^2 - (2ab)^2$
>    **Resultado final:** **$(2a^2 + 2ab + 3b^2)(2a^2 - 2ab + 3b^2)$**

> [!example] **Ejemplo 2: ¿Qué pasa con los negativos?**
> Factorizar: $c^4 - 45c^2 + 100$
> 1. **Raíces**: $c^2$ y $10$.
> 2. **Diagnóstico**: $2 \cdot (c^2) \cdot (10) = 20c^2$. 
>    *Problema*: Tenemos $-45c^2$ y necesitamos $-20c^2$. Para pasar de -45 a -20, debemos sumar $25c^2$ (y restarlo después).
> 3. **Proceso**: $(c^4 - 20c^2 + 100) - 25c^2$
> 4. **Factorización**: $(c^2 - 10)^2 - (5c)^2$
>    **Resultado ordenado:** **$(c^2 + 5c - 10)(c^2 - 5c - 10)$**

> [!example] **Ejemplo 3: Suma de Cubos (¡No olvides la división!)**
> Factorizar: $27m^3 + 125n^6$
> 1. **Raíces cúbicas**: $\sqrt[3]{27m^3} = 3m$ y para la letra dividimos: $n^{6/3} = n^2$. Raíz: $5n^2$.
> 2. **Fórmula**: $(a + b)(a^2 - ab + b^2)$.
> 3. **Desarrollo**: $(3m + 5n^2)((3m)^2 - (3m)(5n^2) + (5n^2)^2)$
>    **Resultado final:** **$(3m + 5n^2)(9m^2 - 15mn^2 + 25n^4)$**

> [!example] **Ejemplo 4: Modelado Financiero ($USD)**
> Supongamos que $x$ representa el **factor de inflación** de un activo y su comportamiento contable está dado por $x^4 + x^2 + 1$. Factorizar ayuda a simplificar el balance.
> 1. **Diagnóstico**: Raíces $x^2$ y $1$. El centro necesita ser $2x^2$. Sumamos y restamos $x^2$.
> 2. **Ajuste**: $(x^4 + 2x^2 + 1) - x^2 = (x^2 + 1)^2 - x^2$
>    **Resultado:** **$(x^2 + x + 1)(x^2 - x + 1)$**

---

### ✍️ Ejercicios para el Estudiante

> [!abstract] **🟢 Nivel Fácil: Cubos para calentar**
> 1. $x^3 - 8$
> 2. $27 + a^3$
> 3. $m^3 + 1$
> 4. $y^6 - 64$ (¡Ojo! Este tiene un secreto, factorízalo hasta que ya no se pueda más).

> [!abstract] **🟡 Nivel Medio: Completando el Trinomio**
> 1. $a^4 + a^2 + 1$
> 2. $x^4 + 3x^2 + 4$
> 3. $c^4 - 7c^2 + 9$
> 4. $x^4 + 64$ (Pista: el término central original es $0x^2$, ¡invéntalo sumando lo que falta!).

> [!abstract] **🔴 Nivel Avanzado: Aplicación de Costos ($USD)**
> Modela la eficiencia de los siguientes costos de producción $C(n)$ donde $n$ es la cantidad de unidades:
> 1. $C(n) = 4n^4 + 3n^2 + 9$
> 2. $C(x) = x^8 + 4x^4 + 16$ (Usa $x$ como tasa de exportación).
> 3. $C(a) = 64a^4 + b^4$
> 4. $C(m) = m^4 + m^2n^2 + n^4$

---

### ✅ Solucionario Maestro

> [!success] **Respuestas Verificadas**
> **Nivel Fácil:**
> 1. **$(x - 2)(x^2 + 2x + 4)$** 
> 2. **$(3 + a)(9 - 3a + a^2)$** 
> 3. **$(m + 1)(m^2 - m + 1)$** 
> 4. **$(y - 2)(y + 2)(y^2 + 2y + 4)(y^2 - 2y + 4)$** *(Nota: Primero es diferencia de cuadrados y luego factorizas ambos cubos)*.
>
> **Nivel Medio:**
> 1. **$(a^2 + a + 1)(a^2 - a + 1)$** 
> 2. **$(x^2 + x + 2)(x^2 - x + 2)$** 
> 3. **$(c^2 + c - 3)(c^2 - c - 3)$** 
> 4. **$(x^2 + 4x + 8)(x^2 - 4x + 8)$** *(Sumamos y restamos $16x^2$)*.
>
> **Nivel Avanzado:**
> 1. **$(2n^2 + 3n + 3)(2n^2 - 3n + 3)$** 
> 2. **$(x^4 + 2x^2 + 4)(x^4 - 2x^2 + 4)$** 
> 3. **$(8a^2 + 4ab + b^2)(8a^2 - 4ab + b^2)$** 
> 4. **$(m^2 + mn + n^2)(m^2 - mn + n^2)$**

---

### 🧠 Mini-Prueba de Autoevaluación

> [!question] **Pregunta 1**
> ¿Qué es lo primero que Profe Alex recomienda revisar antes de cualquier método?
> *Respuesta: Revisar si existe un **Factor Común** y asegurar que la expresión esté **ordenada**.*

> [!question] **Pregunta 2**
> ¿Cuál es la raíz cúbica de $z^{15}$?
> *Respuesta: **$z^5$**. Dividimos el exponente entre 3 ($15/3 = 5$).*

> [!question] **Pregunta 3**
> Para factorizar $x^4 + 64$, ¿qué término debemos sumar y restar para hacerlo un TCP?
> *Respuesta: **$16x^2$**. Porque la raíz de $x^4$ es $x^2$, la de $64$ es $8$, y el doble producto es $2 \cdot x^2 \cdot 8 = 16x^2$.*

---

> [!tip] **Conexión con la Clase 07**
> ¡Excelente trabajo hoy! Has dominado las potencias pares e impares. Ahora que sabes desarmar polinomios como un experto, en la próxima clase usaremos todo esto para **Simplificar Fracciones Algebraicas**. ¡Nos vemos allí!

---
[[Clase 05](Clase05)] | [[Índice](Índice)] | [[Clase 07](Clase07)]