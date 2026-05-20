# Clase 02 — Cuadrado de un Binomio y Productos Conjugados

`#algebra` `#cuadradodeunbin`

[← Clase Anterior](01-Introduccion-Productos-Notables) | [Siguiente Clase →](03-Producto-Binomios-Termino-Comun)

---

## ¿Por qué es importante esta clase?

Los productos notables nos permiten resolver multiplicaciones complejas de forma instantánea mediante reglas fijas. En geometría, facilitan el cálculo de áreas de terrenos y estructuras, mientras que en finanzas permiten modelar el crecimiento de carteras y presupuestos sin realizar tediosas operaciones algebraicas término a término.

*   **💵 Aplicación USD:** El cuadrado de un binomio permite proyectar variaciones en presupuestos cuando cambian dos variables de costo simultáneamente. Si el costo total es $(x + y)^2$, el desarrollo nos muestra que el gasto no solo sube por los componentes individuales ($x^2$ y $y^2$), sino por la interacción entre ellos (el "término del medio" $2xy$).
*   **🏗️ Aplicación práctica:** En diseño arquitectónico, el producto de binomios conjugados se usa para calcular la diferencia de áreas. Si modificamos un plano sumando una medida a un lado y restándola al otro $(L+a)(L-a)$, obtenemos una diferencia de cuadrados ($L^2 - a^2$), indicando exactamente cuánta superficie se ha sacrificado.
*   **📊 Situación cotidiana:** Ayuda a realizar multiplicaciones mentales rápidas. Por ejemplo, calcular $29 \times 31$ es simplemente $(30-1)(30+1) = 30^2 - 1^2 = 900 - 1 = 899$.

---

## Concepto clave

> [!abstract] 📌 ¿Qué es el Cuadrado de un binomio?
> Es el resultado de elevar una suma o resta de dos términos al cuadrado. Siguiendo la lógica del **Profe Alex**, la regla es:
> 1. El primer término al cuadrado.
> 2. **Más o menos** el doble del primero por el segundo.
> 3. El segundo término siempre al cuadrado (positivo).
> 
> **Caso especial $(-a-b)^2$:** Si ambos términos son negativos, ¡el resultado es todo positivo! Esto ocurre porque el primer término al cuadrado $(-a)^2$ es positivo, y en el doble producto $2(-a)(-b)$, la ley de signos (menos por menos) da más.

> [!abstract] 📌 ¿Qué son los Binomios Conjugados?
> Son dos binomios idénticos donde solo cambia el signo de la mitad. Su producto siempre resulta en una **Diferencia de Cuadrados** ($a^2 - b^2$).
> **⚠️ Advertencia:** Si cambian los coeficientes o las letras (ej. $3x$ vs $2x$), ya **no** son conjugados y debes usar la multiplicación larga.

> [!danger] ⚠️ Error común
> 1. **Distribución prohibida:** $(a+b)^2$ **NO** es $a^2 + b^2$. Nunca olvides el término central.
> 2. **Potencia de una potencia:** Al elevar $(x^3)^2$, los exponentes se **multiplican**, dando $x^6$. Un error frecuente es elevar 3 al cuadrado y poner $x^9$, lo cual es incorrecto.

> [!tip] 💡 Truco para recordarlo (El Sándwich)
> Imagina el cuadrado de un binomio como un sándwich:
> - **Las tapas:** Son el primer y el segundo término elevados al cuadrado ($a^2$ y $b^2$).
> - **El relleno:** Es el doble producto del primero por el segundo ($2ab$).
> ¡Sin relleno, no hay sándwich!

---

## Procedimiento paso a paso

```text
1. IDENTIFICAR: Determina si es un Cuadrado de Binomio o Binomios Conjugados.
2. EXTRAER TÉRMINOS: Identifica el "primer término" (a) y el "segundo" (b) con sus signos.
3. APLICAR REGLA: 
   - Cuadrado: (a)² ± 2(a)(b) + (b)²
   - Conjugados: (a)² - (b)²
4. SIMPLIFICAR: Eleva coeficientes y aplica "Potencia de una potencia" 
   (Multiplicar exponentes).
```

---

## Ejemplos de la Clase

> [!example] Ejemplo 1 — Caso con Fracciones y Cancelación
> Resolver: $(\frac{3}{2}x^2 + \frac{5}{4}y^2)^2$
> *   **Primer término al cuadrado:** $(\frac{3}{2}x^2)^2 = \frac{9}{4}x^4$
> *   **Doble producto (Truco del Profe Alex):** $2 \cdot (\frac{3}{2}x^2) \cdot (\frac{5}{4}y^2)$. Aquí, el $2$ que multiplica se **cancela directamente** con el denominador $2$ de la primera fracción. Nos queda solo $3 \cdot \frac{5}{4} = \frac{15}{4}x^2y^2$.
> *   **Segundo término al cuadrado:** $(\frac{5}{4}y^2)^2 = \frac{25}{16}y^4$
> *   **Resultado final:** $\frac{9}{4}x^4 + \frac{15}{4}x^2y^2 + \frac{25}{16}y^4$

> [!example] Ejemplo 2 — Binomios Conjugados con Raíces
> Resolver: $(\sqrt{2} + \sqrt{3})(\sqrt{2} - \sqrt{3})$
> *   Aplicamos diferencia de cuadrados: $(\sqrt{2})^2 - (\sqrt{3})^2$
> *   La raíz cuadrada y el exponente 2 se anulan mutuamente: $2 - 3$
> *   **Resultado final:** $-1$

> [!example] Ejemplo 3 — Caso con Doble Negativo
> Resolver: $(-3m - 5n)^2$
> *   Desarrollo: $(-3m)^2 + 2(-3m)(-5n) + (-5n)^2$
> *   Análisis de signos: $(-3)^2 = 9$ y en el centro $2 \cdot (-3) \cdot (-5)$ da $+30$ (menos por menos es más).
> *   **Resultado final:** $9m^2 + 30mn + 25n^2$

> [!example] Ejemplo 4 — Aplicación real con $USD
> Un producto financiero tiene un precio de $(x + 5)$ USD y se adquieren $(x - 5)$ unidades.
> *   **Cálculo:** $(x + 5)(x - 5)$ es un producto de conjugados.
> *   **Resultado:** $x^2 - 25$ USD. El ingreso total es una diferencia de cuadrados.

---

## Ejercicios para el estudiante

### 🟢 Fácil
1. $(x + 4)(x - 4)$
2. $(m + 6)^2$
3. $(a - 9)(a + 9)$
4. $(y + 1)^2$

### 🟡 Medio
1. $(\frac{1}{2}a^3 - b)^2$
2. $(\frac{2}{3}x^2 + \frac{1}{5})(\frac{2}{3}x^2 - \frac{1}{5})$
3. $(-2x - 3y)^2$
4. $(4m^5 + 3n^2)(4m^5 - 3n^2)$

### 🔴 Avanzado — Aplicación con $USD
1. Un terreno cuadrado tiene un lado que mide $(2x + 10)$ metros. Si el valor catastral del terreno es de 1 USD por metro cuadrado, exprese el valor total del terreno como un polinomio de área.
2. Una empresa proyecta que su flujo de caja pasará de un estado de $(C + 8)$ USD a uno de $(C - 8)$ USD. Calcule la nueva proyección de ingresos modelada como el producto de ambos estados financieros.
3. Determine el área de una oficina rectangular cuyas dimensiones en metros son $(\sqrt{10} + 2)$ y $(\sqrt{10} - 2)$.
4. El presupuesto de una obra equivale al cuadrado de la suma del costo de materiales $(x)$ y la mano de obra $(15)$. Desarrolle la expresión $(x + 15)^2$.

> [!success] Respuestas para el Docente
> **Fácil:** 1. $x^2-16$ | 2. $m^2+12m+36$ | 3. $a^2-81$ | 4. $y^2+2y+1$
> **Medio:** 1. $\frac{1}{4}a^6 - a^3b + b^2$ | 2. $\frac{4}{9}x^4 - \frac{1}{25}$ | 3. $4x^2+12xy+9y^2$ | 4. $16m^{10}-9n^4$
> **Avanzado:** 1. $4x^2+40x+100$ | 2. $C^2-64$ | 3. $6$ | 4. $x^2+30x+225$

---

## Mini-prueba de autoevaluación

1. **¿Cuál de estas opciones presenta binomios conjugados?**
   a) $(x + 5)(x + 5)$
   b) $(2a - 3)(2a + 3)$
   c) $(x^2 + y)(x + y)$
   d) $(m - n)(-m + n)$

2. **Al resolver $(x^4 - 2)^2$, el primer término es:**
   a) $x^6$
   b) $x^{16}$
   c) $x^8$
   d) $2x^4$

3. **Si una acción sube de $(P-3)$ a $(P+3)$ y multiplicamos ambos valores, ¿qué obtenemos?**
   a) Un trinomio cuadrado perfecto.
   b) Una suma de cuadrados.
   c) Una diferencia de cuadrados.
   d) Una expresión lineal.

**Validación:**
1. **b)** Los términos son idénticos y solo difieren en el signo central.
2. **c)** Por la regla de potencia de una potencia, $(x^4)^2 = x^{4 \cdot 2} = x^8$.
3. **c)** Es el caso típico de binomios conjugados, cuyo resultado es $P^2 - 9$, técnicamente llamado **Diferencia de Cuadrados**.

---

## Notas para el próximo tema

Hemos dominado el cuadrado de la suma/resta y los productos conjugados, aprendiendo a identificar cuándo un término medio debe existir y cuándo se anula. En la próxima clase, subiremos un escalón hacia el **Producto de dos binomios con término común**, donde los binomios ya no son "espejos", sino que comparten un solo elemento.

[← Clase Anterior](01-Introduccion-Productos-Notables) | [Siguiente Clase →](03-Producto-Binomios-Termino-Comun)