# Clase 07 — División de Polinomios con Coeficientes Fraccionarios
#algebra #dividingpolynom

> [!info] **Navegación**
> `[[Clase 06|⬅ Clase 06]]` | `[[00 - Índice del curso|Índice]]` | Final del curso

---

### 1. ¿Por qué es importante esta clase?
¡Qué tal amigos! Espero que estén muy bien. Hoy vamos a subir de nivel. Dominar las fracciones en el álgebra no solo te hace más ágil, sino que te permite trabajar con la precisión exacta que los decimales pierden. ¡Pilas con esto!, porque en la vida real las cosas no siempre vienen en números enteros.

**Aplicaciones prácticas:**
*   **USD (Presupuesto):** Dividir un presupuesto fraccionado (ej. 3/4 de un fondo) entre un número variable de servicios bancarios.
*   **Construcción:** Calcular las dimensiones de un muro cuando el área total y un lado tienen medidas como "5/2 metros".
*   **Cotidiana:** Ajustar las cantidades exactas de una receta industrial cuando necesitas dividir ingredientes para porciones no enteras.

---

### 2. Concepto Clave

> [!note] **Definición**
> Dividir polinomios con fracciones es exactamente igual a la división que ya conoces, pero aquí gestionamos numeradores y denominadores por separado. Es como armar un rompecabezas: buscamos qué número le falta a nuestra pieza para ser igual a la otra.

> [!warning] **Error Común: ¡Mucho ojo!**
> *   ❌ **Olvidar el cambio de signo:** Este es el error más típico. Al pasar el resultado de la multiplicación al dividendo, **siempre** se le cambia el signo (si da positivo, pasa negativo; si da negativo, pasa positivo).
> *   ❌ **No simplificar:** Dejar una fracción como $16/144$ te hará la vida imposible. 
> *   ✅ **Simplifica siempre** (en este caso a $1/9$) antes de seguir al siguiente paso.

> [!tip] **Truco: El Método de "Quitar y Poner"**
> Para convertir una fracción en otra, usa la regla del **lado opuesto**:
> 1.  **Para quitar:** Si quieres eliminar un número que está arriba, ponlo abajo en tu factor. Si está abajo, ponlo arriba.
> 2.  **Para poner:** Pon el número que quieres obtener en el lugar donde lo necesitas (arriba para numerador, abajo para denominador).
> *Ejemplo:* Para que $\frac{2}{3}$ se convierta en $\frac{5}{2}$:
> - Quito el 2 (está arriba): pongo un 2 abajo.
> - Quito el 3 (está abajo): pongo un 3 arriba.
> - Pongo el 5 (arriba) y el 2 (abajo).
> - **Resultado:** $\frac{3 \times 5}{2 \times 2} = \frac{15}{4}$.

---

### 3. Procedimiento Paso a Paso

> [!tip] **Consejo de Pro: Operaciones Aparte**
> Les sugiero mucho hacer las sumas y multiplicaciones de fracciones en una hojita aparte o en un rincón del cuaderno. Así el proceso principal de la división queda limpio y no se confunden.

```text
PASO 1: ORDENAR
Organiza el dividendo y el divisor de forma descendente (ej. a², a, término sin a).

PASO 2: BUSCAR EL TÉRMINO (DIVIDIR NUMERADOR Y DENOMINADOR)
Mira el primer término del dividendo y el primero del divisor.
- Ajusta el numerador: ¿Qué número multiplicado por el de arriba me da el de arriba?
- Ajusta el denominador: ¿Qué número multiplicado por el de abajo me da el de abajo?
- Aplica el "Quitar y Poner" si no es directo.

PASO 3: MULTIPLICAR Y CAMBIAR EL SIGNO
Multiplica el término hallado por TODO el divisor. 
¡IMPORTANTÍSIMO!: Cambia el signo de cada resultado antes de escribirlo abajo.

PASO 4: CARITA FEA Y BAJAR
Suma o resta las fracciones usando el método de la "Carita Fea":
- Multiplica los denominadores (la barbilla/sonrisa).
- Multiplica en cruz (los ojos/cejas).
Simplifica el resultado, baja el siguiente término y repite.
```

---

### 4. Deep Dive: Ejemplo Paso a Paso
Vamos a resolver esta división: $(\frac{1}{6}a^2 + \frac{5}{36}ab - \frac{1}{6}b^2) \div (\frac{1}{3}a + \frac{1}{2}b)$

> [!example] **Fase 1: Encontrando el primer término**
> Buscamos convertir $\frac{1}{3}a$ en $\frac{1}{6}a^2$.
> - Numeradores: El 1 ya está.
> - Denominadores: El 3 para que sea 6 se multiplica por 2.
> - Letras: $a$ para que sea $a^2$ necesita otra $a$.
> - **Cociente:** $\frac{1}{2}a$.
> - **Multiplicación:** $(\frac{1}{2}a) \cdot (\frac{1}{3}a) = \frac{1}{6}a^2 \rightarrow$ **Pasa como $-\frac{1}{6}a^2$**.
> - $(\frac{1}{2}a) \cdot (\frac{1}{2}b) = \frac{1}{4}ab \rightarrow$ **Pasa como $-\frac{1}{4}ab$**.

> [!example] **Fase 2: Simplificación y Signos**
> Ahora operamos $\frac{5}{36}ab - \frac{1}{4}ab$.
> - Usamos "Carita Fea" aparte: $\frac{(5 \times 4) - (36 \times 1)}{36 \times 4} = \frac{20 - 36}{144} = -\frac{16}{144}$.
> - **Simplificación obligatoria:** $-\frac{16}{144} = -\frac{8}{72} = -\frac{4}{36} = -\frac{2}{18} = -\frac{1}{9}$.
> - El nuevo término a dividir es $-\frac{1}{9}ab$.
> - Buscamos factor: Como el dividendo es negativo, el cociente debe ser **negativo** ($-\frac{1}{3}b$).

> [!example] **Fase 3: Aplicación USD**
> Si un presupuesto total es $(\frac{3}{4}x^2 + \frac{1}{2}x)$ USD y se divide entre un área de $(\frac{1}{2}x)$ metros:
> 1. $\frac{3}{4}x^2 \div \frac{1}{2}x = \frac{3}{2}x$ (porque para convertir $1/2$ en $3/4$ multiplicas por $3/2$).
> 2. $\frac{1}{2}x \div \frac{1}{2}x = 1$.
> - **Resultado (Precio Unitario):** $(\frac{3}{2}x + 1)$ USD por metro.

---

### 5. Ejercicios para el Estudiante

> [!abstract] **Nivel Verde (Fácil)**
> 1. $(\frac{1}{2}x^2) \div (\frac{1}{4}x)$
> 2. $(\frac{2}{3}a^3) \div (\frac{1}{3}a)$
> 3. $(\frac{3}{5}m^2) \div (\frac{3}{5}m)$
> 4. $(\frac{1}{10}y^4) \div (\frac{1}{2}y^2)$
> *Respuestas: 1) $2x$, 2) $2a^2$, 3) $m$, 4) $\frac{1}{5}y^2$*

> [!abstract] **Nivel Amarillo (Medio)**
> 1. $(\frac{1}{4}x^2 + \frac{1}{4}x) \div (\frac{1}{4}x)$
> 2. $(\frac{1}{3}a^2 + \frac{2}{3}ab) \div (\frac{1}{3}a)$
> 3. $(\frac{1}{2}x^2 + \frac{5}{8}x + \frac{1}{8}) \div (\frac{1}{2}x + \frac{1}{4})$
> 4. $(\frac{1}{9}y^2 - \frac{1}{4}) \div (\frac{1}{3}y + \frac{1}{2})$
> *Respuestas: 1) $x+1$, 2) $a+2b$, 3) $x+\frac{1}{2}$, 4) $\frac{1}{3}y - \frac{1}{2}$*

> [!abstract] **Nivel Rojo (Avanzado - USD)**
> 1. Un terreno cuesta $(\frac{1}{4}x^2 + \frac{7}{12}x + \frac{1}{3})$ USD. Si su fondo mide $(\frac{1}{2}x + \frac{2}{3})$, ¿cuál es su frente?
> 2. Repartir un presupuesto de $(\frac{1}{8}x^2 - \frac{1}{32})$ USD entre $(\frac{1}{2}x + \frac{1}{4})$ personas.
> 3. Dividir un costo de $(\frac{4}{9}a^2 - \frac{1}{9}b^2)$ USD entre un costo unitario de $(\frac{2}{3}a - \frac{1}{3}b)$.
> 4. Calcular el precio unitario: $(\frac{1}{6}x^2 + \frac{5}{36}x)$ USD $\div (\frac{1}{3}x)$ unidades.
> *Respuestas: 1) $\frac{1}{2}x + \frac{1}{2}$, 2) $\frac{1}{4}x - \frac{1}{8}$, 3) $\frac{2}{3}a + \frac{1}{3}b$, 4) $\frac{1}{2}x + \frac{5}{12}$*

---

### 6. Mini-prueba de Autoevaluación

> [!question] **Pregunta 1**
> Antes de escribir la división, ¿qué paso es obligatorio realizar con los polinomios para no perderse?
> *   **Respuesta:** Ordenarlos de forma descendente respecto a una letra. ¡Si no ordenas, no sale!

> [!question] **Pregunta 2**
> Usando "Quitar y Poner", ¿cómo convierto $\frac{2}{3}$ en $\frac{5}{2}$?
> *   **Respuesta:** Multiplicando por $\frac{15}{4}$. (Lógica: Ponemos un $3$ arriba para quitar el de abajo, un $2$ abajo para quitar el de arriba, luego el $5$ que queremos arriba y el $2$ que queremos abajo: $\frac{3 \times 5}{2 \times 2} = \frac{15}{4}$).

> [!question] **Pregunta 3**
> En un problema de USD, si el área es $\frac{1}{2}x$ y el costo es $\frac{3}{4}x^2$, ¿cuál es el precio unitario inicial?
> *   **Respuesta:** $\frac{3}{2}x$. (Explicación: $\frac{3}{4} \div \frac{1}{2} = \frac{3 \times 2}{4 \times 1} = \frac{6}{4} = \frac{3}{2}$).

---

### 7. Cierre del curso
¡Felicidades por llegar hasta aquí! La división con fracciones es el "examen final" de la aritmética básica en el álgebra. Si dominas esto, cualquier tema de simplificación de fracciones complejas en el futuro te parecerá un juego de niños. ¡Sigue practicando y nos vemos en el siguiente curso!

> [!info] **Navegación Final**
> `[[Clase 06|⬅ Clase 06]]` | `[[00 - Índice del curso|Índice]]` | Final del curso