# 📖 Guía de estudio — Clase 07: División de Polinomios con Fracciones

> [!info] 📌 Conceptos clave
> ¡Hola! No te asustes por ver fracciones en el álgebra. Recuerda que la clave para dominar este tema es el **orden**. Si sigues estos cuatro pilares, ¡lograrás resolver cualquier ejercicio!
> 1.  **Ordenamiento Estricto:** Organiza siempre los polinomios de forma descendente (de mayor a menor exponente) respecto a una letra.
> 2.  **Búsqueda del Multiplicador:** Para hallar el término del cociente, ajusta numerador y denominador por separado. Si no encuentras un factor directo, usa la **Técnica de Ajuste (Quitar y Poner)**.
> 3.  **La Regla de Oro del Signo:** ¡Mucho ojo aquí! Al multiplicar el cociente por el divisor, el resultado **siempre cambia de signo** al pasar al lado del dividendo. Este es el error más común, ¡no dejes que te pase a ti!
> 4.  **Operación de Fracciones:** Para las restas intermedias, usa el método de la "Carita Feliz" (o "Carita Fea", como dice el Profe Alex), siempre multiplicando los **extremos primero**.

---

## 2. Glosario de Términos y Fórmulas

| Término | Definición / Fórmula |
| :--- | :--- |
| **Dividendo y Divisor** | El Dividendo es lo que queremos repartir; el Divisor es entre cuánto lo repartimos. El orden alfabético manda. |
| **Fracciones Homogéneas** | Tienen el mismo denominador. Solo sumas/restas los de arriba: $\frac{a}{c} \pm \frac{b}{c} = \frac{a \pm b}{c}$. |
| **Fracciones Heterogéneas** | Tienen distinto denominador. Aplicamos: $\frac{a}{b} \pm \frac{c}{d} = \frac{(a \cdot d) \pm (c \cdot b)}{b \cdot d}$. **¡Extremos ($a \cdot d$) primero!** |
| **Técnica de Ajuste** | Si quieres convertir $\frac{1}{3}$ en $\frac{1}{4}$, aplicas la lógica: "Quito el 3 (poniéndolo arriba) y pongo el 4 (abajo)". |

---

## 3. Ejemplos Resueltos Paso a Paso

```ad-example
title: Ejemplo A — División Directa
**Problema:** Dividir $(\frac{1}{6}a^2 + \frac{5}{36}ab - \frac{1}{6}b^2) \div (\frac{1}{3}a + \frac{1}{2}b)$

**Paso 1: Hallar el primer término del cociente**
¿Por cuánto multiplico $\frac{1}{3}a$ para obtener $\frac{1}{6}a^2$?
*   Numerador: $1 \times 1 = 1$
*   Denominador: $3 \times 2 = 6$
*   Letra: $a \times a = a^2$
*   **Resultado:** $\frac{1}{2}a$

**Paso 2: Multiplicar y CAMBIAR SIGNOS (¡Vital!)**
*   $(\frac{1}{2}a) \cdot (\frac{1}{3}a) = \frac{1}{6}a^2 \rightarrow$ Escribimos **$-\frac{1}{6}a^2$** bajo el dividendo.
*   $(\frac{1}{2}a) \cdot (\frac{1}{2}b) = \frac{1}{4}ab \rightarrow$ Escribimos **$-\frac{1}{4}ab$** bajo el dividendo.

**Paso 3: Operación de "Carita Fea" y Simplificación**
Resolvemos $\frac{5}{36}ab - \frac{1}{4}ab$ en una hoja aparte:
1. Multiplicamos denominadores: $36 \cdot 4 = 144$.
2. Multiplicamos en cruz: $(5 \cdot 4) - (1 \cdot 36) = 20 - 36 = -16$.
3. Fracción resultante: $-\frac{16}{144}$.
4. **Simplificación paso a paso (mitades):**
   $-\frac{16}{144} \rightarrow -\frac{8}{72} \rightarrow -\frac{4}{36} \rightarrow -\frac{2}{18} \rightarrow \mathbf{-\frac{1}{9}}$.
*Bajamos el siguiente término: $-\frac{1}{6}b^2$.*

**Paso 4: Segundo término del cociente**
¿Por cuánto multiplico $\frac{1}{3}a$ para obtener $-\frac{1}{9}ab$?
*   Signo: (+) por **(-)** nos da (-).
*   Numerador: $1 \times 1 = 1$.
*   Denominador: $3 \times 3 = 9$.
*   Letra: Falta la $b$.
*   **Resultado:** $-\frac{1}{3}b$.

**Resultado Final:** $\frac{1}{2}a - \frac{1}{3}b$
```

```ad-example
title: Ejemplo B — Distribución de Fondos
**Contexto Real:**
Imagina que un fondo de construcción debe pagar un proyecto cuyo costo total está representado por el polinomio $(\frac{1}{6}a^2 + \frac{5}{36}ab - \frac{1}{6}b^2)$.
*   $a = $ Costo de un metro cúbico de concreto ($10 USD).
*   $b = $ Costo de una hora de mano de obra ($3 USD).

Si el costo total se divide entre el personal $(\frac{1}{3}a + \frac{1}{2}b)$, ¿cuánto dinero recibe cada trabajador?

**Solución:**
Sabemos por el Ejemplo A que el resultado de la división es $(\frac{1}{2}a - \frac{1}{3}b)$. Sustituimos los valores reales:
*   $\frac{1}{2}(10) - \frac{1}{3}(3)$
*   $5 - 1 = \mathbf{4 \text{ USD por trabajador.}}$
```

---

## 4. Banco de Ejercicios Practicables

```ad-abstract
title: 🟢 Nivel Verde (Fácil)
¡Empieza calentando motores! Encuentra el factor que falta:
1. $\frac{1}{4} \cdot (\dots) = \frac{1}{12}$
2. $\frac{2}{3} \cdot (\dots) = \frac{10}{9}$
3. $\frac{1}{3} \cdot (\dots) = \frac{1}{4}$ (Pista: Usa la técnica de **"Quitar y Poner"**. Quita el 3 poniéndolo arriba y pon el 4 abajo).
```

```ad-abstract
title: 🟡 Nivel Amarillo (Medio)
Pon a prueba tu orden. Realiza la división completa:
$(\frac{1}{6}x^2 + \frac{5}{24}xy - \frac{1}{6}y^2) \div (\frac{2}{3}x + \frac{1}{2}y)$
*Consejo: Simplifica tus fracciones en cada resta antes de seguir.*
```

```ad-abstract
title: 🔴 Nivel Rojo (Avanzado) — Aplicación con $USD
Un presupuesto de obra se divide en dos facturas pendientes:
*   Factura A: $\frac{1}{8}x^2$
*   Factura B: $(\frac{1}{24}x^2 + \frac{5}{36}xy - \frac{1}{6}y^2)$

**Tu reto:**
1. Suma ambas facturas (fracciones heterogéneas de $x^2$) para obtener el **Dividendo Consolidado**.
2. Divide ese nuevo polinomio entre $(\frac{1}{3}x + \frac{1}{2}y)$ para hallar el costo por unidad de medida.
```

---

## 5. Estrategia de Maestría

> [!tip] 💡 Consejo de estudio del Profe Alex
> ¡No amontones tus cálculos! El secreto de los mejores estudiantes de matemáticas es la **limpieza**. 
> 
> Realiza todas las sumas, restas y simplificaciones de fracciones en una **columna lateral** o en una hoja borrador. A tu procedimiento principal de división solo debes llevar el resultado final ya simplificado. Si intentas hacer la "Carita Fea" dentro de la división, te confundirás con los signos y los exponentes. ¡Mantén tu hoja limpia y tu mente clara!