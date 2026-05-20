# Clase 02 — Operaciones con Intervalos: Unión, Intersección, Diferencia y Complemento

#algebra #unionofinterval
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 9

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | [[Clase 03|Clase 03 ➡]]

---

> [!info] 🌍 Relevancia y aplicaciones
> Las operaciones con intervalos permiten modelar situaciones donde los límites no son estáticos, como los rangos de tolerancia en piezas de ingeniería o los umbrales de riesgo en finanzas. Son la base para entender dónde coinciden o se excluyen diversas condiciones técnicas.
> 
> *   **💵 $USD:** Definir el rango de fluctuación de precios de un activo entre la apertura y el cierre de diversas jornadas de bolsa para detectar zonas de interés.
> *   **🏗️ Construcción:** Calcular el solapamiento (intersección) de medidas de seguridad en vigas, asegurando que los puntos de refuerzo coincidan exactamente.
> *   **📊 Situación cotidiana:** Determinar la disponibilidad real de tiempo libre entre dos personas mediante la unión o intersección de sus agendas laborales.

---

> [!note] 📌 ¿Qué son las operaciones con intervalos?
> Imagina que los intervalos son tramos de una carretera (la recta real $\mathbb{R}$). Operar con ellos es como gestionar esos tramos:
> *   **Unión ($\cup$):** Es "juntar todo". Es el trayecto total que cubren ambos tramos. *Ojo:* Si hay un número que no pertenece a ninguno de los dos, se genera un "hueco" en la unión.
> *   **Intersección ($\cap$):** Es "lo que tienen en común". Es únicamente la parte de la carretera donde ambos tramos se solapan.
> *   **Diferencia ($-$):** Es "quitarle una parte al otro". Al tramo $A$ le borras cualquier parte que pertenezca al tramo $B$.
> *   **Complemento ($A'$ o $A^c$):** Se simboliza frecuentemente con una "comita" ($A'$). Representa "lo que le falta para ser el todo". Son todos los números de la recta real que no están en $A$. Al calcularlo sobre un intervalo acotado, solemos obtener dos rayos infinitos hacia los extremos.

> [!warning] ⚠️ Error común
> En la **diferencia ($A - B$)**, si un número está en $B$, debe ser "borrado" de $A$. Si el extremo de $B$ es cerrado (punto negro), significa que ese número se va; por lo tanto, el resultado en $A$ debe quedar abierto (huequito), incluso si originalmente era cerrado.

> [!tip] 💡 Truco para recordarlo
> *   **La Linterna (Intersección):** Imagina dos luces de colores proyectadas sobre el suelo. La intersección es solo el área donde los colores se mezclan.
> *   **El Borrador (Diferencia):** Visualiza el segundo intervalo como un borrador físico que pasa sobre la recta y elimina todo lo que toca del primero.

---

### Procedimiento paso a paso (Metodología Gráfica)

Basado en la técnica didáctica de "Matemáticas profe Alex", sigue este proceso visual:

```text
PASO 1: Dibujar la recta real y ubicar todos los puntos críticos de los intervalos.
PASO 2: Graficar el primer intervalo (Punto negro para cerrado [], Huequito para abierto () ).
PASO 3: Graficar el segundo intervalo sobre la misma recta (usar otro color o nivel).
PASO 4: Identificar la zona resultante:
        - Unión: Todo el espacio que tenga al menos una línea pintada.
        - Intersección: Solo el espacio donde las líneas de ambos colores se cruzan.
        - Diferencia: Al primer color, borrarle todo lo que el segundo color "toque".
        - Complemento: Sombrear todo lo que el intervalo original dejó vacío en la recta.
```

---

### Ejemplos Prácticos

```ad-example
title: Ejemplo 1: Unión ($\cup$)
Dados $A = (-3, 2)$ y $B = (1, 5]$
* **Análisis:** Al juntar ambos, cubrimos desde el $-3$ (no incluido) hasta el $5$ (incluido). Como los intervalos se solapan entre $1$ y $2$, la unión es continua.
* **Graficado:** Un huequito en $-3$ y un punto negro en $5$, con toda la zona intermedia sombreada.
* **Resultado:** $A \cup B = (-3, 5]$
```

```ad-example
title: Ejemplo 2: Intersección ($\cap$)
Dados $A = [-2, 4]$ y $C = (4, 8)$
* **Análisis:** El intervalo $A$ llega hasta el $4$ y lo incluye. El intervalo $C$ empieza en el $4$ pero **no** lo incluye (es un huequito).
* **Graficado:** En el punto $4$ hay un punto negro (de $A$) y un huequito (de $C$). Como no coinciden en ambos, el $4$ no es parte de la intersección.
* **Resultado:** $A \cap C = \emptyset$ (Conjunto vacío).
```

```ad-example
title: Ejemplo 3: Diferencia ($-$)
Dados $B = [0, 5]$ y $D = [-2, 7)$
* **Caso $B - D$:** Como $D$ es más grande y contiene a todo $B$, al pasar el "borrador" de $D$ sobre $B$, no queda nada. **Resultado:** $\emptyset$.
* **Caso $D - B$:** Al tramo $D$ le borramos el centro ($B$). El $0$ y el $5$ de $B$ tienen punto negro, así que se borran y dejan huequitos en el resultado.
* **Graficado:** Un tramo de $[-2, 0)$ y otro de $(5, 7)$.
* **Resultado:** $D - B = [-2, 0) \cup (5, 7)$.
```

```ad-example
title: Ejemplo 4: Aplicación en Precios ($USD)
El precio de un producto fluctúa en $P = [10, 20]$. Se lanza una restricción legal que prohíbe vender en el rango $R = [15, 25]$. ¿Cuál es el nuevo rango efectivo?
* **Operación:** $P - R$ (Al precio original le borramos la restricción).
* **Graficado:** El borrador de $R$ inicia en $15$ (cerrado) y llega hasta $25$. Al tocar el $15$ de nuestro intervalo $P$, lo elimina.
* **Resultado:** $[10, 15)$.
```

---

### Ejercicios y Autoevaluación

```ad-abstract
title: Nivel Fácil
1. $[1, 5] \cup [3, 7]$
2. $(0, 4) \cap [2, 6]$
3. $[-10, -2] \cup [-5, 0]$
4. $(1, 3) \cap (5, 8)$
```

```ad-abstract
title: Nivel Medio
1. $[2, 10] - (5, 8)$
2. $(- \infty, 4] \cap (0, \infty)$
3. Sea $A = [3, 9]$, halla $A'$ (respecto a $\mathbb{R}$).
4. $(0, 10] - [0, 5]$
```

```ad-abstract
title: Nivel Avanzado ($USD y Casos Especiales)
1. **Unión con "Hueco":** Hallar $A \cup D$ si $A = (-3, 2)$ y $D = (2, 6)$. ¿Qué sucede con el número $2$?
2. **Presupuesto:** El inversor A tiene un presupuesto de $[500, 1500]$ y el inversor B uno de $[1200, 2500]$. ¿En qué rango de $USD$ pueden co-invertir? (Intersección).
3. **Zona Libre de Deuda:** Si el rango de deuda de una empresa es $D = [-1000, 0]$, halla el complemento $D'$ para identificar las zonas de saldo positivo o deuda nula fuera de ese rango.
4. **Retornos:** Un activo tiene retornos en $R_1 = [-5\%, 5\%]$ y otro en $R_2 = [2\%, 10\%]$. Hallar la unión de beneficios.
```

```ad-success
title: Soluciones para el docente
**Fácil:** 1. $[1, 7]$ | 2. $[2, 4)$ | 3. $[-10, 0]$ | 4. $\emptyset$
**Medio:** 1. $[2, 5] \cup [8, 10]$ | 2. $(0, 4]$ | 3. $(-\infty, 3) \cup (9, \infty)$ | 4. $(5, 10]$
**Avanzado:** 
1. $(-3, 6) - \{2\}$ o $(-3, 2) \cup (2, 6)$. El $2$ no está en la unión porque no está en ninguno.
2. $[1200, 1500]$
3. $(-\infty, -1000) \cup (0, \infty)$
4. $[-5\%, 10\%]$
```

---

### Mini-prueba rápida

```ad-question
title: Pregunta 1 (Conceptual)
Si realizamos la unión de $A = (1, 4)$ y $B = (4, 6)$, ¿el número $4$ forma parte del resultado?
- A) Sí, porque la unión junta los extremos.
- B) No, porque el $4$ es un "huequito" en ambos intervalos.

**Respuesta correcta: B.** Al no estar incluido en $A$ ni en $B$, el $4$ no puede estar en la unión. Gráficamente, queda un hueco en la recta.
```

```ad-question
title: Pregunta 2 (Procedimental)
¿Cuál es el resultado de $[0, 10] - [10, 12]$?
- A) $[0, 10)$
- B) $[0, 10]$

**Respuesta correcta: A.** El borrador incluye al $10$ (punto negro), por lo que lo elimina del primer intervalo, dejando un huequito en el resultado.
```

```ad-question
title: Pregunta 3 (Aplicación $USD)
Un cliente solo compra si el precio está entre $\$20$ y $\$30$ (inclusive). Si la tienda fija precios en el rango $(25, 40]$, ¿en qué rango podrá comprar el cliente?
- A) $[20, 40]$
- B) $(25, 30]$

**Respuesta correcta: B.** Es una intersección. El cliente quiere $[20, 30]$ y la tienda ofrece $(25, 40]$. El área común inicia después de $25$ y termina en $30$.
```

---

> [!tip] 💡 En la próxima clase
> Estudiaremos las **Inecuaciones Lineales**. Verás cómo las soluciones a estas desigualdades se expresan utilizando exactamente estas operaciones y notaciones de intervalos.

> [!info] 🧭 Navegación
> [[Clase 01|⬅ Clase 01]] | [[00 - Índice del curso|Índice]] | [[Clase 03|Clase 03 ➡]]