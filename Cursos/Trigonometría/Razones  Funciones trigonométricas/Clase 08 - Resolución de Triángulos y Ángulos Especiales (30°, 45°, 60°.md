# Clase 08 — Resolución de Triángulos y Ángulos Especiales (30°, 45°, 60°)

tags: #algebra #solveorresolvea
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 8 de 12

[!info] 🧭 Navegación
| Anterior | Inicio | Siguiente |
| :--- | :--- | :--- |
| [[Clase 07 — Introducción a las Razones]] | [[00 - Índice del curso]] | [[Clase 09 — Ley de Senos y Cosenos]] |

---

[!info] 🌍 Relevancia y aplicaciones
¡Bienvenidos! Resolver un triángulo es como ser un detective matemático: con solo un par de pistas, podemos descubrir todas las medidas ocultas. Esto es vital para calcular distancias que no podemos medir físicamente.

* **💵 Aplicación $USD:** Calcular la longitud exacta de una rampa (hipotenusa) para comprar solo los metros necesarios de madera y optimizar el presupuesto.
* **🏗️ Aplicación práctica:** En arquitectura, determinar la inclinación de un techo para que el agua drene correctamente.
* **📊 Situación cotidiana:** ¿Quieres saber cuánto mide un árbol? Mide su sombra y el ángulo del sol, ¡la trigonometría hará el resto!

---

[!note] 📌 ¿Qué es resolver un triángulo?
¡Hola! Resolver (o solucionar) un triángulo rectángulo significa simplemente **encontrar todas las medidas que faltan**: la longitud de sus tres lados y la medida de sus tres ángulos internos. Si ya tienes el ángulo recto (90°) y otros dos datos, ¡tienes el poder de completar todo el triángulo!

### El origen de los "Ángulos Especiales"
¿Te has preguntado de dónde salen los valores de 30°, 45° y 60°? No son números mágicos; vienen de la geometría pura:

1. **Para 30° y 60°:** Imagina un triángulo **equilátero** donde todos sus lados miden **2**. Si lo partimos por la mitad con su altura, obtenemos un triángulo rectángulo con hipotenusa **2**, base **1** y una altura de $\sqrt{3}$ (por Pitágoras). ¡De ahí nacen estas razones!
2. **Para 45°:** Imagina un triángulo **isósceles** con dos lados que miden **1**. Su hipotenusa será $\sqrt{2}$. Al tener dos lados iguales, sus ángulos agudos deben ser de 45°.

| Ángulo | Seno ($\sin$) | Coseno ($\cos$) | Tangente ($\tan$) |
| :--- | :---: | :---: | :---: |
| **30°** | $1/2$ | $\sqrt{3}/2$ | $1/\sqrt{3}$ o $\sqrt{3}/3$ |
| **45°** | $1/\sqrt{2}$ o $\sqrt{2}/2$ | $1/\sqrt{2}$ o $\sqrt{2}/2$ | $1$ |
| **60°** | $\sqrt{3}/2$ | $1/2$ | $\sqrt{3}$ |

[!warning] ⚠️ ¡No caigas en la trampa!
1. **La Calculadora:** Asegúrate de que aparezca una **"D"** o la palabra **DEG** en tu pantalla. Si está en "R" (Radianes), todos tus cálculos fallarán.
2. **El Ángulo manda:** Tu primer paso define quién es quién. Si eliges un ángulo agudo, el de enfrente es el **Opuesto**. Si cambias de ángulo a mitad del ejercicio, ¡la lógica del problema "explota"! Mantente fiel a tu ángulo de trabajo.

[!tip] 💡 Trucos de experto
* **SOH CAH TOA:** La regla de oro para recordar las razones.
* **Comprobación rápida:** En un triángulo rectángulo, los dos ángulos agudos **siempre deben sumar 90°**. Úsalo para verificar tus respuestas al instante.

---

### Procedimiento Maestro
Utiliza este algoritmo lógico para no perderte nunca:

```text
1. Elige tu ángulo de trabajo (¡Paso vital! Define tus catetos).
2. Identifica los lados: Hipotenusa (el más largo), Opuesto (enfrente) y Adyacente (al lado).
3. Selecciona la razón (SOH CAH TOA) que relacione tu dato conocido con tu incógnita.
4. ¡Vamos a despejar! Sustituye los valores y resuelve la ecuación.
```

---

## Ejemplos Prácticos

[!example] Ejemplo 1: Hallar un lado (Cateto Opuesto)
**Problema:** Ángulo de $32^\circ$ e hipotenusa de $15m$.
* **Estrategia:** Tenemos Hipotenusa y buscamos Opuesto $\rightarrow$ Usamos **Seno**.
* **Cálculo:** $\sin(32^\circ) = \frac{CO}{15}$
* **Despeje:** $15 \cdot \sin(32^\circ) = CO$
* **Resultado:** $CO \approx 7.948m$.

[!example] Ejemplo 2: Variable en el denominador (Hallar Hipotenusa)
**Problema:** Cateto adyacente de $15m$ y ángulo de $34^\circ$.
* **Estrategia:** Tenemos Adyacente y buscamos Hipotenusa $\rightarrow$ Usamos **Coseno**.
* **Cálculo:** $\cos(34^\circ) = \frac{15}{H}$
* **Despeje:** Cuando la incógnita está abajo, "intercambia" lugar con la razón: $H = \frac{15}{\cos(34^\circ)}$.
* **Resultado:** $H \approx 18.093m$.

[!example] Ejemplo 3: Hallar el ángulo (Función Inversa)
**Problema:** Cateto opuesto $13cm$ y adyacente $18cm$. Hallar ángulo $A$.
* **Estrategia:** Tenemos los dos catetos $\rightarrow$ Usamos **Tangente**.
* **Cálculo:** $\tan(A) = \frac{13}{18}$
* **Despeje:** $A = \arctan(13/18)$. En tu calculadora, usa `Shift + Tan`.
* **Resultado:** $A \approx 35.83^\circ$. Para ser exactos, presiona la tecla de grados, minutos y segundos ($^\circ ' ''$) para obtener **$35^\circ 50' 15''$**.

[!example] Ejemplo 4: Proyecto $USD (Aplicación Real)
**Problema:** Necesitas un cable de soporte para una antena. El cable formará un ángulo de $60^\circ$ con el suelo y se anclará a $10m$ de la base (cateto adyacente). Si el metro de cable cuesta $\$4.50\ USD$, ¿cuál es el presupuesto?
* **Paso 1 (Hallar Hipotenusa):** $\cos(60^\circ) = \frac{10}{H}$
* **Paso 2 (Despejar):** $H = \frac{10}{\cos(60^\circ)} = \frac{10}{0.5} = 20m$.
* **Paso 3 (Costo):** $20m \cdot \$4.50 = \$90.00\ USD$.
* **Resultado:** El costo total es de **$\$90.00\ USD$**.

---

## Ejercicios para el Estudiante

[!abstract] 🟢 Nivel Fácil: Cálculo Directo
1. Hallar el cateto opuesto si $\theta = 30^\circ$ e $H = 10cm$.
2. Hallar el cateto adyacente si $\theta = 60^\circ$ e $H = 20m$.
3. En un triángulo de $45^\circ$ con cateto adyacente de $5cm$, ¿cuánto mide el opuesto?
4. Calcula la hipotenusa si el cateto opuesto a un ángulo de $30^\circ$ mide $8m$.

[!abstract] 🟡 Nivel Medio: Encontrar Ángulos
1. Si los dos catetos miden lo mismo ($CO=5, CA=5$), ¿cuál es el ángulo agudo?
2. Si $H = 12$ y $CA = 6$, halla el ángulo agudo adyacente.
3. Hallar el ángulo $B$ si su cateto opuesto mide $10$ y la hipotenusa $20$.
4. Si los catetos miden $4cm$ (opuesto) y $7cm$ (adyacente), halla el ángulo.

[!abstract] 🔴 Nivel Avanzado: Aplicación $USD
1. Una rampa debe subir $3m$ de altura con un ángulo de $45^\circ$. Si el material cuesta $\$12\ USD$ por metro de rampa (hipotenusa), ¿cuál es el costo total?
2. Un cable de soporte (hipotenusa) se sujeta con un ángulo de $34^\circ$ respecto al suelo. Si el cable mide $15m$ y cuesta $\$5.50\ USD$ por metro, ¿cuánto es el gasto?
3. Se cercará la hipotenusa de un terreno. Un cateto mide $15m$ y el ángulo adyacente es $32^\circ$. El metro de cerca cuesta $\$8\ USD$.
4. Una viga inclinada (hipotenusa) para un techo de $60^\circ$ tiene una base (adyacente) de $4m$. Si el metro de viga cuesta $\$15\ USD$, calcula el costo.

[!success] Solucionario de verificación
* **Verde:** 1) $5cm$; 2) $10m$; 3) $5cm$; 4) $16m$.
* **Amarillo:** 1) $45^\circ$; 2) $60^\circ$; 3) $30^\circ$; 4) $\approx 29.74^\circ$.
* **Rojo:** 
	1) $H \approx 4.24m \rightarrow \mathbf{\$50.91\ USD}$.
	2) $H = 15m \rightarrow \mathbf{\$82.50\ USD}$.
	3) $H \approx 17.7m \rightarrow \mathbf{\$141.60\ USD}$.
	4) $H = 8m \rightarrow \mathbf{\$120.00\ USD}$.

---

## Autoevaluación

[!question] Test de Repaso
1. **Suma de ángulos:** Si un ángulo agudo de un triángulo rectángulo mide $32^\circ$, ¿cuánto mide el otro?
2. **Elección de razón:** Tienes la Hipotenusa y buscas el Cateto Adyacente. ¿Qué usas?
3. **Presupuesto:** Calculaste que necesitas una hipotenusa de $10m$. Si el precio es $\$5\ USD/m$ y solo tienes $\$45\ USD$, ¿cuánto dinero te falta?

[!success] Respuestas
1. **$58^\circ$**: Porque $90 - 32 = 58$. ¡Siempre deben sumar 90!
2. **Coseno**: Por la regla CAH (Coseno = Adyacente / Hipotenusa).
3. **Te faltan $\$5\ USD$**: El costo total es $10 \cdot 5 = 50$. Como tienes 45, te faltan 5.

[!tip] 💡 En la próxima clase
Ya eres un maestro de los triángulos rectángulos. En la siguiente sesión, romperemos los límites: aprenderemos la **Ley de Senos y Cosenos** para resolver triángulos que NO tienen ángulos de 90°. ¡No te lo pierdas!

---

[!info] 🧭 Navegación
| Anterior | Inicio | Siguiente |
| :--- | :--- | :--- |
| [[Clase 07 — Introducción a las Razones]] | [[00 - Índice del curso]] | [[Clase 09 — Ley de Senos y Cosenos]] |