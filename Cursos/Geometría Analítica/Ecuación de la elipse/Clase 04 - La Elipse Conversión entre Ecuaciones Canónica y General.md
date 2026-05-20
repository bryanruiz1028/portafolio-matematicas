# Clase 04 — La Elipse: Conversión entre Ecuaciones Canónica y General

tags: #algebra #ellipse
Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 4 de 6

[!info] 🧭 Navegación
Anterior: [[Clase 03]] | Siguiente: [[Clase 05]]

---

[!info] 🌍 Relevancia y aplicaciones
La elipse es una figura fundamental en el diseño y la ciencia. Su forma no es solo estética, sino que responde a leyes físicas y estructurales:

*   **💵 [Aplicación con $USD]:** Permite calcular el presupuesto exacto de materiales (como mármol o madera) para fabricar cubiertas de mesas elípticas de lujo según su área superficial.
*   **🏗️ [Aplicación práctica]:** Es clave en el diseño de "salas de reflexión acústica" en teatros y museos, donde un sonido emitido en un foco de la elipse se escucha con total nitidez en el otro foco.
*   **📊 [Situación cotidiana]:** Define el área de cobertura de la señal de una antena parabólica cuando se dispone en un ángulo inclinado respecto al suelo.

[!note] 📌 ¿Qué es la Elipse?
Imagina una curva cerrada que parece un **"círculo estirado"**. ¡Eso es una elipse! A diferencia del círculo, que tiene un solo centro, la elipse tiene **dos centros llamados focos**. Dependiendo de qué datos tengamos, podemos escribir su ubicación como una "receta" simple (Ecuación Canónica) o como una lista extendida de términos (Ecuación General).

[!warning] ⚠️ Error común
Al convertir ecuaciones, un error muy frecuente es olvidar **elevar al cuadrado el segundo término** del binomio $(a \pm b)^2$. Recuerda que $(x - 5)^2$ no es $x^2 - 25$, sino $x^2 - 10x + 25$. Además, siempre asegúrate de que la Ecuación General termine **igualada a cero** ($= 0$).

[!tip] 💡 Truco para recordarlo
Para sumar las fracciones de la ecuación canónica sin complicaciones, usa el **"Método de la Carita Feliz"** (o Mariposa):
1.  **La Sonrisa:** Multiplica los denominadores entre sí.
2.  **Los Ojos:** Multiplica en cruz el numerador de la primera por el denominador de la segunda, y viceversa.

---

## 4. Procedimiento paso a paso

Para transformar una elipse de su forma **Canónica** a la **General**, sigue este proceso técnico:

```text
PASO 1 → Realizar la suma de fracciones (Método de la Carita Feliz): 
        (Numerador 1 * Denominador 2) + (Numerador 2 * Denominador 1) 
        ------------------------------------------------------------
                       (Denominador 1 * Denominador 2)

PASO 2 → Pasar el denominador resultante a multiplicar al lado derecho (donde está el 1).

PASO 3 → Desarrollar los cuadrados de los binomios usando la fórmula: (a ± b)² = a² ± 2ab + b².

PASO 4 → Multiplicar coeficientes, organizar términos (x², y², x, y, constante) e igualar a cero.
```

> [!important] Nota técnica: De General a Canónica
> Si al dividir toda la ecuación por el término independiente, un numerador (ej. $4x^2$) no se simplifica de forma exacta con el denominador (ej. $3$), aplicamos la **regla de inversión**: El coeficiente del numerador pasa a ser el denominador del denominador.
> *Ejemplo:* $\frac{4x^2}{3}$ se convierte en $\frac{x^2}{3/4}$.

---

## 5. Ejemplos de Clase

### Ejemplo 1: Caso Básico (Centro en $0,0$)
Convertir $\frac{x^2}{4} + \frac{y^2}{9} = 1$ a ecuación general.
1.  Multiplicamos cruzado: $9 \cdot x^2 + 4 \cdot y^2 = 4 \cdot 9$
2.  Obtenemos: $9x^2 + 4y^2 = 36$
3.  Igualamos a cero: **$9x^2 + 4y^2 - 36 = 0$**

### Ejemplo 2: Con Binomios (Centro fuera del origen)
Convertir $\frac{(x-5)^2}{9} + \frac{(y+3)^2}{4} = 1$ a ecuación general.
1.  Suma de fracciones: $4(x-5)^2 + 9(y+3)^2 = 36$
2.  Desarrollo de binomios:
    *   $(x-5)^2 = x^2 - 10x + 25$
    *   $(y+3)^2 = y^2 + 6y + 9$
3.  Distribuimos coeficientes:
    *   $4(x^2 - 10x + 25) + 9(y^2 + 6y + 9) = 36$
    *   $4x^2 - 40x + 100 + 9y^2 + 54y + 81 - 36 = 0$
4.  Resultado final: **$4x^2 + 9y^2 - 40x + 54y + 145 = 0$**

### Ejemplo 3: De General a Canónica
Convertir $3x^2 + 6y^2 - 36 = 0$ a canónica.
1.  Pasamos el constante: $3x^2 + 6y^2 = 36$
2.  Dividimos entre $36$: $\frac{3x^2}{36} + \frac{6y^2}{36} = \frac{36}{36}$
3.  Simplificamos: **$\frac{x^2}{12} + \frac{y^2}{6} = 1$**

### Ejemplo 4: Aplicación $USD (Piscina Elíptica)
Se planea excavar una piscina cuya forma sigue la ecuación $4x^2 + 25y^2 - 100 = 0$. El costo es de **$50 USD** por unidad de área.
1.  **Ecuación canónica:** $\frac{x^2}{25} + \frac{y^2}{4} = 1$.
2.  **Identificar semiejes:** $a = \sqrt{25} = 5$ y $b = \sqrt{4} = 2$.
3.  **Cálculo de Área:** Usamos la fórmula $Area = \pi \cdot a \cdot b$.
    *   $Area = 3.14 \cdot 5 \cdot 2 = 31.4$ unidades².
4.  **Costo Total:** $31.4 \cdot 50 = \mathbf{\$1,570 \text{ USD}}$.

---

## 6. Ejercicios para el Estudiante

[!success] 🟢 Bloque Fácil: Canónica a General (Centro $0,0$)
1.  $\frac{x^2}{16} + \frac{y^2}{25} = 1$
2.  $\frac{x^2}{9} + \frac{y^2}{4} = 1$
3.  $\frac{x^2}{49} + \frac{y^2}{10} = 1$
4.  $\frac{x^2}{2} + \frac{y^2}{1} = 1$

[!warning] 🟡 Bloque Medio: Con binomios
1.  $\frac{(x-1)^2}{4} + \frac{(y+2)^2}{9} = 1$
2.  $\frac{(x+3)^2}{16} + \frac{(y-5)^2}{25} = 1$
3.  $\frac{(x-2)^2}{7} + \frac{(y-1)^2}{3} = 1$
4.  $\frac{x^2}{5} + \frac{(y+4)^2}{2} = 1$

[!danger] 🔴 Avanzado: General a Canónica y Costos ($USD)
1.  $9x^2 + 16y^2 - 144 = 0$. Hallar la canónica y el costo si el refuerzo de la longitud del **semieje mayor** cuesta $\$15 \text{ USD}$ por metro.
2.  $25x^2 + 4y^2 - 100 = 0$. Hallar la canónica.
3.  $2x^2 + 8y^2 - 16 = 0$. Hallar la canónica.
4.  $5x^2 + 3y^2 - 15 = 0$. Si el mantenimiento cuesta $\$10 \text{ USD}$ por cada unidad del valor del denominador de $x^2$, ¿cuál es el costo?

[!done] ✅ Respuestas
*   **Fácil:** 1) $25x^2+16y^2-400=0$; 2) $4x^2+9y^2-36=0$; 3) $10x^2+49y^2-490=0$; 4) $x^2+2y^2-2=0$.
*   **Medio:** 1) $9x^2+4y^2-18x+16y-11=0$; 2) $25x^2+16y^2+150x-160y+225=0$; 3) $3x^2+7y^2-12x-14y-2=0$; 4) $2x^2+5y^2+40y+70=0$.
*   **Avanzado:** 1) $\frac{x^2}{16}+\frac{y^2}{9}=1$, Costo: $\$60$ ($4 \cdot 15$); 2) $\frac{x^2}{4}+\frac{y^2}{25}=1$; 3) $\frac{x^2}{8}+\frac{y^2}{2}=1$; 4) $\frac{x^2}{3}+\frac{y^2}{5}=1$, Costo: $\$30$ ($3 \cdot 10$).

---

## 7. Mini-Prueba de Autoevaluación

1.  **¿Cuál es el requisito indispensable para que una ecuación de la elipse sea considerada "General"?**
    *   a) Que tenga dos fracciones sumándose.
    *   b) Que todos los términos estén de un solo lado e igualados a $0$.
    *   c) Que el centro esté en el origen $(0,0)$.

2.  **En el procedimiento de "Canónica a General", ¿qué se hace inmediatamente después de realizar la multiplicación cruzada (carita feliz)?**
    *   a) Simplificar las $x$ con las $y$.
    *   b) Pasar el denominador común a multiplicar al $1$ del lado derecho.
    *   c) Dividir toda la ecuación por el número más grande.

3.  **Si una mesa elíptica tiene un semieje mayor $a = 10$ metros y el metro de borde reforzado cuesta $\$2 \text{ USD}$, ¿cuánto cuesta el refuerzo de ese semieje?**
    *   a) $\$20 \text{ USD}$.
    *   b) $\$5 \text{ USD}$.
    *   c) $\$100 \text{ USD}$.

---

[!tip] 💡 En la próxima clase
Exploraremos los elementos internos de la elipse (vértices y focos) y cómo la **excentricidad** determina qué tan "aplastada" se ve nuestra figura. ¡Prepárate para conectar esto con las Hipérbolas!

[!info] 🧭 Navegación
Anterior: [[Clase 03]] | Siguiente: [[Clase 05]]