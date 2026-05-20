# Clase 06 — Área del polígono regular, Fórmula de Herón y Geometría del Rombo

#poligonos #geometria
[[00 - Índice del curso]] | Bloque 2 | Lección 6 de 7
[« Clase 05](Clase05) | [Índice](Indice) | [Clase 07 »](Clase07)

---

## 1. ¿Por qué es importante esta clase?

Como futuros arquitectos, ingenieros o diseñadores, se enfrentarán a superficies que no siempre presentan ángulos rectos o alturas fáciles de medir. Esta sesión les otorgará las herramientas para dominar el espacio mediante el cálculo de áreas complejas.

La relevancia de esta lección se refleja en:
* 💵 **Cálculo de costos de materiales:** Determinación precisa de presupuestos para la instalación de pisos, alfombras o revestimientos en superficies poligonales, calculando el costo total en **$USD** según el área.
* 🏗️ **Arquitectura y Diseño:** El uso de polígonos regulares y rombos permite crear estructuras estéticas y patrones de diseño industrial eficientes.
* 📊 **Agrimensura y Terrenos:** La aplicación de la Fórmula de Herón es vital para medir terrenos irregulares donde solo conocemos la longitud de los linderos, pero no sus ángulos internos ni su altura.

---

## 2. Conceptos clave

> [!note] Definiciones fundamentales
> * **Polígono Regular:** Figura cuyos lados y ángulos internos son iguales. Su área se define por la relación entre su contorno y su centro: $Area = \frac{P \cdot a}{2}$, donde $P$ es el perímetro y $a$ el apotema.
> * **Fórmula de Herón:** Es un "salvavidas" geométrico que permite hallar el área de **cualquier triángulo** conociendo solo sus tres lados ($a, b, c$). Es indispensable cuando la altura es inaccesible.
> * **Rombo:** Cuadrilátero con cuatro lados iguales. Es útil visualizarlo como la **mitad de un rectángulo** cuyas dimensiones son las diagonales del rombo. Su fórmula es $Area = \frac{D \cdot d}{2}$.

> [!warning] Aviso de error común
> 1. **El factor 2:** Es muy frecuente olvidar dividir entre $2$ en las fórmulas del polígono y del rombo.
> 2. **El Semiperímetro ($s$):** En la Fórmula de Herón, el error más grave es usar el perímetro total. Recuerda siempre calcular primero $s = \frac{a+b+c}{2}$ antes de entrar en la raíz.

> [!tip] Regla mnemotécnica para el Rombo
> Para no olvidar la fórmula, memoriza esta rima:
> *"Diagonal mayor por diagonal menor, entre dos, y el área del rombo tengo yo".*
> Visualiza siempre el rectángulo imaginario que lo rodea; el rombo ocupa exactamente la mitad de ese espacio.

---

## 3. Procedimiento: El Rombo y el Teorema de Pitágoras

Cuando conocemos el lado del rombo ($L$) y solo una diagonal ($d$), debemos usar la lógica geométrica: las diagonales se cortan en su punto medio (se bisecan) y son perpendiculares. Esto forma cuatro triángulos rectángulos idénticos; cada uno representa $\frac{1}{4}$ del área total.

```text
1. Identificar el triángulo rectángulo interno: La hipotenusa es el lado (L) del rombo.
2. Definir catetos: Un cateto es la mitad de la diagonal conocida (d/2). El otro cateto (x) será la mitad de la diagonal faltante.
3. Aplicar Pitágoras: Resolver x² + (d/2)² = L² para hallar "x".
4. Reconstruir la diagonal: Multiplicar "x" por 2 para obtener la diagonal completa (D).
5. Calcular el área: Aplicar la fórmula final (D · d) / 2.
```

---

## 4. Ejemplos de aplicación

```ad-example
title: Ejemplo 1: Pentágono Regular (Caso básico)
**Problema:** Hallar el área de un pentágono regular con lado $L = 6 \text{ cm}$ y apotema $a = 4.1 \text{ cm}$.

**Solución:**
1. Perímetro ($P$): $5 \text{ lados} \cdot 6 \text{ cm} = 30 \text{ cm}$.
2. Fórmula: $Area = \frac{P \cdot a}{2}$
3. Cálculo: $\frac{30 \cdot 4.1}{2} = \frac{123}{2} = \mathbf{61.5 \text{ cm}^2}$.
```

```ad-example
title: Ejemplo 2: Fórmula de Herón (Triángulo sin altura)
**Problema:** Calcular el área de un triángulo con lados de $4 \text{ m}$, $5 \text{ m}$ y $7 \text{ m}$.

**Solución:**
1. Perímetro ($P$): $4 + 5 + 7 = 16 \text{ m}$.
2. Semiperímetro ($s$): $s = \frac{16}{2} = \mathbf{8 \text{ m}}$.
3. Aplicación de Herón: $Area = \sqrt{s(s-a)(s-b)(s-c)}$
4. Cálculo: $Area = \sqrt{8(8-4)(8-5)(8-7)} = \sqrt{8 \cdot 4 \cdot 3 \cdot 1} = \sqrt{96}$.
5. Resultado: $\mathbf{9.79 \text{ m}^2}$.
```

```ad-example
title: Ejemplo 3: Rombo con Teorema de Pitágoras
**Problema:** Hallar el área de un rombo que tiene un lado de $13 \text{ m}$ y una diagonal de $10 \text{ m}$.

**Solución:**
1. Análisis: Usamos un triángulo rectángulo interno donde la hipotenusa es $13$ y un cateto es $5$ (la mitad de $10$).
2. Pitágoras: $x^2 + 5^2 = 13^2 \implies x^2 + 25 = 169 \implies x^2 = 144 \implies x = \sqrt{144} = 12 \text{ m}$.
3. Diagonal faltante ($D$): $12 \cdot 2 = \mathbf{24 \text{ m}}$.
4. Área final: $\frac{24 \cdot 10}{2} = \frac{240}{2} = \mathbf{120 \text{ m}^2}$.
```

```ad-example
title: Ejemplo 4: Aplicación Real y Presupuesto ($USD)
**Problema:** Se debe alfombrar un salón octagonal (lado $16 \text{ m}$, apotema $19.3 \text{ m}$). Si el $m^2$ de alfombra cuesta $\$15.50 \text{ USD}$, ¿cuál es el costo total?

**Solución:**
1. Perímetro ($P$): $8 \text{ lados} \cdot 16 \text{ m} = 128 \text{ m}$.
2. Área: $\frac{128 \cdot 19.3}{2} = \mathbf{1235.2 \text{ m}^2}$.
3. Costo total: $1235.2 \text{ m}^2 \cdot \$15.50 = \mathbf{\$19,145.60 \text{ USD}}$.
```

---

## 5. Ejercicios para el estudiante

```ad-abstract
title: 🟢 Dificultad: Fácil
1. Hallar el área de un rombo con $D = 10 \text{ cm}$ y $d = 6 \text{ cm}$.
2. Calcular el área de un rombo con $D = 9 \text{ m}$ y $d = 5 \text{ m}$.
3. Un pentágono regular tiene un lado de $10 \text{ cm}$ y apotema de $7 \text{ cm}$. Calcula su área.
4. Si un lado de un rombo mide $5 \text{ cm}$, ¿cuál es su perímetro?
```

```ad-abstract
title: 🟡 Dificultad: Medio
1. Hallar el área de un triángulo con lados de $10 \text{ cm}$, $12 \text{ cm}$ y $20 \text{ cm}$ usando Herón.
2. Un rombo tiene un lado de $5 \text{ cm}$ y una diagonal de $8 \text{ cm}$. Halla la otra diagonal y su área.
3. Calcula el área de un octágono regular con lado $16 \text{ cm}$ y apotema $19.3 \text{ cm}$.
4. Un triángulo tiene lados de $7 \text{ m}$, $5 \text{ m}$ y $4 \text{ m}$. Calcula su semiperímetro y área.
```

```ad-abstract
title: 🔴 Dificultad: Avanzado
1. Una plaza romboidal tiene un lado de $13 \text{ m}$ y una diagonal de $10 \text{ m}$. Pavimentarla cuesta $\$25 \text{ USD}/m^2$. ¿Cuál es el presupuesto total?
2. Se deben pintar **dos** paredes triangulares idénticas cuyos lados miden $10 \text{ m}$, $12 \text{ m}$ y $20 \text{ m}$. Si un galón de pintura cubre $10 \text{ m}^2$ y cuesta $\$12 \text{ USD}$, ¿cuánto dinero se gastará? (Nota: Solo se venden galones enteros).
3. Una fábrica produce $100$ piezas pentagonales (lado $6 \text{ cm}$, apotema $4.1 \text{ cm}$). ¿Cuánta superficie de material se requiere en total?
4. ¿Qué superficie es mayor: un rombo de $D=24 \text{ m}, d=10 \text{ m}$ o un octágono de $P=128 \text{ m}$ y $a=19.3 \text{ m}$?
```

```ad-success
title: ✅ Respuestas para el Docente
**Fácil:** 1) $30 \text{ cm}^2$, 2) $22.5 \text{ m}^2$, 3) $175 \text{ cm}^2$, 4) $20 \text{ cm}$.
**Medio:** 1) $45.59 \text{ cm}^2$, 2) $d=6, A=24 \text{ cm}^2$, 3) $1235.2 \text{ cm}^2$, 4) $s=8, A=9.79 \text{ m}^2$.
**Avanzado:** 
1) $Area=120 \text{ m}^2 \cdot \$25 = \$3,000 \text{ USD}$.
2) $Area_{total} = 2 \cdot 45.59 = 91.18 \text{ m}^2$. Se requieren $10 \text{ galones}$ ($9.11$ redondeado hacia arriba). Costo: $10 \cdot \$12 = \mathbf{\$120 \text{ USD}}$.
3) $61.5 \text{ cm}^2 \cdot 100 = 6150 \text{ cm}^2$.
4) El octágono ($1235.2 \text{ m}^2$) es mucho mayor que el rombo ($120 \text{ m}^2$).
```

---

## 6. Mini-prueba de autoevaluación

> [!question] 1. Conceptual
> ¿Qué representa exactamente la variable $s$ en la fórmula de Herón?
> A) La suma total de los tres lados.
> B) El semiperímetro ($P/2$).
> C) El área superficial del triángulo.
> **Respuesta correcta: B.** Es el paso previo esencial para operar la raíz de Herón.

> [!question] 2. Procedimental
> Si un rombo tiene diagonales de $10 \text{ cm}$ y $6 \text{ cm}$, su área es:
> A) $60 \text{ cm}^2$
> B) $30 \text{ cm}^2$
> C) $16 \text{ cm}^2$
> **Respuesta correcta: B.** Aplicando $\frac{10 \cdot 6}{2}$.

> [!question] 3. Aplicación $USD
> El área de una plaza es $100 \text{ m}^2$ y el costo de mantenimiento es $\$5 \text{ USD}/m^2$. ¿Cuál es el costo total?
> A) $\$500 \text{ USD}$
> B) $\$105 \text{ USD}$
> C) $\$20 \text{ USD}$
> **Respuesta correcta: A.** Multiplicación directa de superficie por costo unitario.

---

> [!tip] Consejo de conexión
> Dominar estas áreas es el cimiento para nuestro próximo bloque: **Cuerpos Geométricos y Volúmenes**. En la siguiente clase, verán cómo estas áreas planas se transforman en las "bases" de prismas y pirámides. ¡No bajen la guardia!

[« Clase 05](Clase05) | [Índice](Indice) | [Clase 07 »](Clase07)