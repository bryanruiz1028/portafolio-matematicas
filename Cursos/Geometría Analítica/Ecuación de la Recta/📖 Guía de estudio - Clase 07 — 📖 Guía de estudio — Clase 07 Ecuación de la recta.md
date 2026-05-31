# 📖 Guía de estudio — Clase 07: Ecuación de la recta a partir de dos puntos

```ad-info
**Conceptos clave**

*   **¿Por qué usamos dos fórmulas?** ¡Atención aquí! Aunque existe una fórmula "gigante", el Profe Alex recomienda usar primero la de la **Pendiente ($m$)** y luego la **Punto-Pendiente**. Esto evita ese "montonón de letras" que suele confundir y hace el proceso mucho más limpio.
*   **La fase de etiquetado:** Antes de hacer cualquier cálculo, **debes** marcar tus puntos como $(x_1, y_1)$ y $(x_2, y_2)$. No te saltes este paso; es el secreto para no intercambiar los valores por accidente.
*   **El poder de los signos:** ¡Mucho ojo! Cuando una coordenada es negativa, la fórmula tendrá un choque de signos: $-(-5)$ se convierte automáticamente en $+5$.
*   **Formas de la ecuación:** Nuestro objetivo es llegar a la **Forma Pendiente-Ordenada** ($y = mx + b$), pero también aprenderemos a dejarla en **Forma General** ($Ax + By + C = 0$) por si tu profesor te la pide así.
```

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Pendiente ($m$)** | Es la inclinación de la recta: $m = \frac{y_2 - y_1}{x_2 - x_1}$ |
| **Ecuación Punto-Pendiente** | Se usa tras hallar $m$ con cualquiera de los puntos: $y - y_1 = m(x - x_1)$ |
| **Forma Pendiente-Ordenada** | También llamada "ordinaria", es la más estética: $y = mx + b$ |
| **Forma General** | Se obtiene igualando la ecuación a cero: $Ax + By + C = 0$ |

---

```ad-example
**Ejemplo A — Caso con Números Enteros**

**Puntos dados:** $A(5, 2)$ y $B(3, 6)$

1.  **Etiquetado (¡No lo olvides!):**
    $x_1 = 5, y_1 = 2$
    $x_2 = 3, y_2 = 6$

2.  **Hallar la pendiente ($m$):**
    $m = \frac{6 - 2}{3 - 5} = \frac{4}{-2} = -2$

3.  **Aplicar fórmula punto-pendiente:**
    Usemos el punto $A(5, 2)$ y $m = -2$:
    $y - 2 = -2(x - 5)$
    $y - 2 = -2x + 10$ (Propiedad distributiva: $-2 \cdot -5 = +10$)

4.  **Despejar para la Forma Pendiente-Ordenada:**
    $y = -2x + 10 + 2$
    **$y = -2x + 12$**

5.  **Extra: Transformar a Forma General:**
    Pasamos todo a un solo lado para igualar a cero:
    $2x + y - 12 = 0$
```

```ad-example
**Ejemplo B — Aplicación real ($USD) y Signos**

**Escenario:** Una academia de música cobra una inscripción fija más una cuota por clase. Si por **2 clases** pagas **$10** y por **5 clases** pagas **$22**, ¿cuál es la ecuación del costo?

1.  **Puntos:** $P_1(2, 10)$ y $P_2(5, 22)$.
2.  **Pendiente ($m$):**
    $m = \frac{22 - 10}{5 - 2} = \frac{12}{3} = 4$
    *Interpretación:* La pendiente representa que cada clase cuesta **$4**.
3.  **Ecuación:**
    $y - 10 = 4(x - 2)$
    $y - 10 = 4x - 8$
    **$y = 4x + 2$**
    *Interpretación:* El costo total ($y$) es $4 por clase ($x$) más una inscripción fija de $2.*
```

---

```ad-abstract
**Ejercicios de repaso**

### Nivel Fácil (Verde)
1. Hallar la ecuación de la recta que pasa por $A(1, 2)$ y $B(2, 4)$.
2. Hallar la ecuación de la recta que pasa por $C(0, 3)$ y $D(4, 11)$.

### Nivel Medio (Amarillo - ¡Cuidado con los signos!)
*Recuerda: Si tienes $x - (-2)$, cámbialo de inmediato a $x + 2$.*
1. Hallar la ecuación de la recta que pasa por $G(-3, -1)$ y $H(-1, 3)$.
2. Hallar la ecuación de la recta que pasa por $I(-2, 5)$ y $J(2, -3)$.

### Nivel Avanzado (Rojo - Fracciones y Contexto)
1. **El desafío de las fracciones:** Hallar la ecuación de la recta que pasa por $P_1(\frac{1}{2}, 2)$ y $P_2(1, \frac{5}{2})$. (Usa el método de la **Carita Feliz** para restar las fracciones en la pendiente).
2. **Contexto Financiero:** Un servicio de streaming tras **3 meses** ha cobrado un total de **$21**, y tras **8 meses** ha cobrado **$46**. Halla la ecuación $y = mx + b$ y determina cuál es el cargo fijo inicial.
```

---

```ad-tip
**💡 El consejo del Profe Alex: La Prueba de Verificación**

¡No te la juegues! Para saber si tu ecuación es correcta, haz esto:
1. Toma el valor de $x$ de cualquiera de los puntos originales.
2. Sustitúyelo en tu ecuación final.
3. Si el resultado es igual al valor de $y$ de ese punto, ¡está perfecto!

**Truco para fracciones:** Si te toca sumar fracciones como $\frac{2}{3} + \frac{1}{2}$, usa la **Carita Feliz**: multiplica los denominadores ($3 \cdot 2 = 6$) y luego multiplica en cruz ($2 \cdot 2 + 3 \cdot 1$). ¡Es infalible!
```