# Clase 02 — Multiplicación de números imaginarios, números complejos, opuesto y conjugado

#algebra #multiplicacion
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 5

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [[Clase 01 - Introducción a los números imaginarios]]
> ➡️ **Siguiente:** [[Clase 03 - Suma y resta de números complejos]]

---

> [!info] 🌍 Relevancia y aplicaciones
> El paso de los números reales a los complejos representa la transición de una visión lineal a una bidimensional de las matemáticas. En el mundo técnico, esto es vital para entender sistemas que no se mueven en una sola dirección.
> 
> *   **💵 [aplicación con $USD]:** Imagina un flujo de caja donde existen "fuerzas perpendiculares" al dinero real, como el riesgo de mercado. Si multiplicas dos factores de riesgo (imaginarios), estos colapsan en una pérdida real en tu balance final ($10i \cdot 1i = -10$ USD).
> *   **🏗️ [aplicación práctica]:** En ingeniería eléctrica, la multiplicación de estos números permite calcular la impedancia y el comportamiento de la corriente alterna en circuitos complejos.
> *   **📊 [situación cotidiana]:** Resolver raíces de números negativos nos permite encontrar soluciones a ecuaciones de física y diseño que, de otro modo, dejarían el problema "sin respuesta" en el campo de los números reales.

---

### 3. Conceptos Clave

> [!note] **Definición: Estructura Binómica y Notación**
> Un número complejo se expresa en forma binómica como **$Z = a + bi$**. 
> *   **$Re(Z) = a$**: Es la parte real.
> *   **$Im(Z) = bi$**: Es la parte imaginaria.
> 
> Para un estudiante de 12 años: piensa en un número complejo como un juguete de dos piezas. Una pieza es sólida y de madera (Real), y la otra es transparente e intangible (Imaginaria). Juntas forman el objeto completo llamado $Z$.

> [!warning] **Error Común: La "Trampa" de la Raíz**
> En los números reales, $\sqrt{a} \cdot \sqrt{b} = \sqrt{a \cdot b}$. **¡Esta propiedad no aplica si ambos números son negativos!**
> *   **Incorrecto:** $\sqrt{-4} \cdot \sqrt{-9} = \sqrt{(-4) \cdot (-9)} = \sqrt{36} = 6$.
> *   **Correcto (Profe Alex):** $\sqrt{-4} \cdot \sqrt{-9} = 2i \cdot 3i = 6i^2 = -6$.
> Siempre debes extraer la unidad imaginaria **antes** de operar.

> [!tip] **Trucos y Propiedades Útiles**
> *   **La identidad fundamental:** Recuerda que $i = \sqrt{-1}$ y, por lo tanto, $i^2 = -1$. Elevar $i$ al cuadrado "elimina" la parte imaginaria y nos devuelve a los reales.
> *   **Opuesto ($-Z$):** Es el "rebelde" total; cambia los signos de ambas partes ($-a - bi$).
> *   **Conjugado ($\bar{Z}$):** Es el "cambio de look" parcial; solo cambia el signo de la parte imaginaria ($a - bi$). Es la herramienta clave para "realizar" números (volverlos reales) en operaciones como la división.

---

### 4. Procedimiento Paso a Paso

```text
ALGORITMO PARA MULTIPLICAR NÚMEROS IMAGINARIOS

PASO 1: Expresar cada raíz negativa usando la identidad i = √(-1).
        Ejemplo: √(-25) se convierte en 5i.
PASO 2: Multiplicar los coeficientes reales (los números).
PASO 3: Multiplicar las unidades imaginarias entre sí (i * i = i²).
PASO 4: Sustituir i² por (-1) y simplificar el signo del resultado final.
```

---

### 5. Ejemplos Desarrollados

> [!example] **Ejemplo 1: Raíces Exactas (Básico)**
> Resolver: $\sqrt{-4} \cdot \sqrt{-9}$
> 1. Pasamos a términos de $i$: $2i \cdot 3i$
> 2. Multiplicamos números: $2 \cdot 3 = 6$
> 3. Operamos con $i$: $6 \cdot i^2$
> 4. Sustituimos $i^2$: $6 \cdot (-1) = -6$.

> [!example] **Ejemplo 2: División y Cancelación**
> Resolver: $\frac{\sqrt{-9}}{\sqrt{-16}}$
> 1. Expresamos en $i$: $\frac{3i}{4i}$
> 2. Como $i$ está arriba y abajo multiplicando, se cancelan.
> 3. Resultado: $\frac{3}{4}$ (Un número real puro).

> [!example] **Ejemplo 3: Raíces No Exactas (Avanzado)**
> Resolver: $\sqrt{-3} \cdot \sqrt{-5}$
> 1. Expresamos en $i$: $\sqrt{3}i \cdot \sqrt{5}i$
> 2. Unimos las raíces reales: $\sqrt{3 \cdot 5} = \sqrt{15}$
> 3. Multiplicamos $i$: $i^2 = -1$
> 4. Resultado final: $-\sqrt{15}$.

> [!example] **Ejemplo 4: Aplicación $USD (Impacto Financiero)**
> Un modelo financiero multiplica un "factor de riesgo perpendicular" de $10i$ por una "unidad de volatilidad" de $1i$.
> 1. Operación: $10i \cdot 1i = 10i^2$
> 2. Transformación: $10 \cdot (-1) = -10$ USD.
> **Conclusión:** La interacción de dos factores imaginarios (no lineales) resulta en una reducción real y tangible del patrimonio.

---

### 6. Ejercicios para el Estudiante

> [!abstract] **Práctica de Clase**
> **🟢 Nivel Fácil (Identificación y Notación)**
> 1. Si $Z = 2 - 3i$, identifica $Re(Z)$ y $Im(Z)$.
> 2. Escribe el opuesto ($-Z$) de $Z = -4 + 7i$.
> 3. Halla el conjugado ($\bar{Z}$) de $Z = 8$.
> 4. ¿Cuál es el opuesto de un imaginario puro como $Z = -2i$?
>
> **🟡 Nivel Medio (Operaciones y Trucos)**
> 1. Calcula: $\sqrt{-25} \cdot \sqrt{-4}$.
> 2. Calcula: $\sqrt{-1} \cdot \sqrt{-81}$.
> 3. **Reto:** Halla el conjugado del resultado de $\sqrt{-4} \cdot \sqrt{-16}$.
> 4. Resuelve la división: $\frac{\sqrt{-100}}{\sqrt{-25}}$.
>
> **🔴 Nivel Avanzado (Potencias y Aplicaciones)**
> 1. Resuelve $\sqrt{-16} \cdot \sqrt{-25} \cdot \sqrt{-4}$ (Nota: $i^3 = -i$).
> 2. Simplifica: $(\sqrt{-2} \cdot \sqrt{-3}) \cdot i$.
> 3. En un presupuesto, una deuda imaginaria de $\sqrt{-1/4}$ USD se multiplica por un recargo de $2i$. ¿Cuál es el balance real?
> 4. Si $Z = 10 \cdot i^3$, determina su opuesto.

> [!success] **Respuestas para el Docente**
> **Fácil:** 1) $Re=2, Im=-3i$; 2) $4 - 7i$; 3) $8$ (no cambia al no haber parte imaginaria); 4) $2i$.
> **Medio:** 1) $-10$; 2) $-9$; 3) $-8$ (el resultado es real, su conjugado es idéntico); 4) $2$.
> **Avanzado:** 1) $-40i$; 2) $-\sqrt{6}i$; 3) $-1$ USD (Pérdida real); 4) $Z = -10i$, Opuesto $= 10i$.

---

### 7. Mini-prueba de Autoevaluación

> [!question] **Pregunta 1**
> ¿Cuál de las siguientes condiciones define a un "imaginario puro"?
> A) Cuando $Im(Z) = 0$.
> B) Cuando $Re(Z) = 0$.
> C) Cuando el número es una fracción.

> [!question] **Pregunta 2**
> El resultado de operar $\sqrt{-2} \cdot \sqrt{-8}$ es:
> A) $4i$
> B) $4$
> C) $-4$

> [!question] **Pregunta 3**
> Si una empresa tiene un balance de deuda compleja $Z = -5 + 2i$, ¿cuál sería el balance si se aplica la operación **Opuesto** (reversión total de signos)?
> A) $5 - 2i$
> B) $5 + 2i$
> C) $-5 - 2i$

---

### 8. Cierre y Navegación

> [!tip] **Próximo paso**
> Ahora que dominas la multiplicación y las identidades de $i$, estamos listos para la **Clase 03**, donde aprenderemos a **sumar y restar** estos números combinando términos semejantes (reales con reales e imaginarios con imaginarios).

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [[Clase 01 - Introducción a los números imaginarios]]
> ➡️ **Siguiente:** [[Clase 03 - Suma y resta de números complejos]]