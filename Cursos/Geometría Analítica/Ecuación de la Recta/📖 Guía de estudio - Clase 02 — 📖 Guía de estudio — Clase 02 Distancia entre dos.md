# 📖 Guía de estudio — Clase 02: Distancia entre dos puntos: Método Gráfico

> [!info] 📌 Conceptos clave
> *   **La diagonal es la clave:** La distancia entre dos puntos que no están en la misma línea horizontal o vertical se visualiza como la **hipotenusa** de un triángulo rectángulo.
> *   **Contar es el primer paso:** Los **catetos** del triángulo se obtienen simplemente contando cuántos "pasitos" (cuadritos) hay de diferencia horizontal y verticalmente.
> *   **El gran aliado:** Usamos el **Teorema de Pitágoras** para calcular la medida exacta de esa diagonal.
> *   **Flexibilidad total:** ¡No te preocupes por cómo dibujas! Puedes formar el triángulo por encima o por debajo de la línea diagonal (en forma de "L" o "L" invertida); ambos caminos te darán el mismo resultado porque son triángulos idénticos.

## 2. TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Teorema de Pitágoras** | Relación fundamental para triángulos rectángulos: $h^2 = a^2 + b^2$. |
| **Catetos** | Son los lados que forman el ángulo de $90^\circ$. En nuestro mapa, son los desplazamientos rectos (izquierda/derecha y arriba/abajo). |
| **Hipotenusa** | Es el camino más corto (la diagonal) que une los dos puntos. Siempre es el lado más largo. |
| **Distancia ($d$)** | La medida del segmento que une dos puntos: $d = \sqrt{a^2 + b^2}$. |
| **⚠️ Regla de Oro** | **¡Cuidado!** Jamás canceles la raíz con los cuadrados si hay una suma dentro ($\sqrt{a^2 + b^2} \neq a + b$). Primero sumas, luego sacas la raíz. |

---

## 3. EJEMPLOS RESUELTOS

```ad-example
title: Ejemplo A — Caso con números enteros
**¡Verás que contar cuadritos es como un juego!** Vamos a hallar la distancia entre los puntos $A(1, 1)$ y $B(5, 4)$.

**Paso 1: Ubicación y dibujo del triángulo.**
Ubicamos $A$ y $B$ en el plano. Al unirlos con una diagonal, dibujamos una "L" para cerrar el triángulo. Puedes hacerla por debajo (derecha y luego arriba) o por arriba; ¡tú eliges!

**Paso 2: El camino de los catetos (Conteo).**
*   **Camino horizontal (a):** Si caminamos desde el $x=1$ hasta el $x=5$, damos **4 pasos** a la derecha.
*   **Camino vertical (b):** Si subimos desde el $y=1$ hasta el $y=4$, damos **3 pasos** hacia arriba.

**Paso 3: Aplicación del Teorema de Pitágoras.**
Usamos $d^2 = a^2 + b^2$:
1. $d^2 = 4^2 + 3^2$
2. $d^2 = 16 + 9$
3. $d^2 = 25$
4. $d = \sqrt{25}$ (Recuerda: no puedes separar la raíz antes de sumar).

**Resultado:**
**Distancia = 5 unidades** ✅
```

```ad-example
title: Ejemplo B — Aplicación de costos por distancia
**Contexto:** Un servicio de mensajería cobra **$1 USD** por cada unidad de distancia en el mapa. ¿Cuánto costará enviar un paquete del punto $C(3, -2)$ al punto $D(-3, 5)$?

**Procedimiento:**
1.  **Visualiza el camino:** Para ir del 3 positivo en el eje X, pasas por el cero y llegas hasta el -3. ¡Has contado **6 cuadros** en total! (Este es tu cateto horizontal).
2.  **Sube por el eje Y:** Desde el -2, subes pasando por el cero hasta llegar al 5. Has contado **7 cuadros** hacia arriba. (Este es tu cateto vertical).
3.  **Calcula la diagonal:**
    $d^2 = 6^2 + 7^2$
    $d^2 = 36 + 49$
    $d^2 = 85$
    $d = \sqrt{85} \approx 9.2$ unidades (Usamos un decimal para mayor claridad).

**Cierre de costo:**
Como cada unidad vale $1 USD:
$9.2 \text{ unidades} \times \$1.00 = \$9.20$
**Costo final: $9.20 USD** ✅
```

---

## 4. EJERCICIOS DE REPASO

```ad-abstract
title: 🟢 Nivel: Fácil
¡Empecemos calentando motores! Encuentra la distancia contando directamente los cuadros (son líneas rectas, no necesitas Pitágoras):
1.  Del Punto $A(2, 2)$ al Punto $B(2, 7)$.
2.  Del Punto $C(-3, 4)$ al Punto $D(5, 4)$.
3.  Del Punto $E(0, -1)$ al Punto $F(0, -6)$.
```

```ad-abstract
title: 🟡 Nivel: Medio
¡Aplica lo aprendido! Dibuja tu triángulo (por arriba o por abajo) y calcula la distancia diagonal exacta:
1.  $A(-3, 4)$ y $B(3, -4)$ (Pista: los catetos miden 6 y 8).
2.  $C(-1, 2)$ y $D(1, 7)$ (Pista: los catetos miden 2 y 5).
3.  $E(1, 1)$ y $F(4, 5)$ (Verifica tu conteo: deberías obtener catetos de 3 y 4).
```

```ad-abstract
title: 🔴 Nivel: Avanzado — Aplicación con $USD
Un dron debe viajar desde su base en $P_1(-2, -2)$ hasta entregar un pedido en $P_2(2, 1)$. 
**Reto:** 
1. Dibuja primero el plano y los puntos para identificar visualmente tus catetos.
2. Calcula la distancia total del viaje.
3. Si la tarifa es de **$2.50 USD por unidad**, ¿cuánto cobrará el dron por el envío?
```

---

> [!tip] 💡 Consejo de estudio
> ¡No te compliques con los signos! Al contar cuadritos en tu hoja, no importa si vas hacia la izquierda o hacia abajo; la medida del lado del triángulo siempre será un número positivo para tu fórmula. **Un truco extra:** Siempre que tengas una suma bajo la raíz, como $\sqrt{16+9}$, resuélvela por completo antes de intentar sacar la raíz. ¡Eso evitará el error más común en los exámenes!