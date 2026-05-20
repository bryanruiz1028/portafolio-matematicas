# Clase 06 — Conversión de Unidades de Capacidad

#algebra #convertingcapac

Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 6 de 6

> [!info] 🧭 Navegación
> - Anterior: [[Clase 05 — Unidades de Longitud]]
> - Índice: [[00 - Índice del curso]]
> - Fin del bloque: ¡Felicidades por completar el Bloque 2!

---

> [!info] 🌍 Relevancia y aplicaciones
> Dominar la conversión de unidades de capacidad te permite gestionar volúmenes de líquidos con precisión quirúrgica, algo vital tanto en el comercio global como en la experimentación científica. Sin esto, sería imposible comparar precios o seguir recetas industriales exactas.
> 
> *   💵 **$USD:** Es la base para calcular precios unitarios y márgenes de ganancia. Si compras vino por decálitros pero lo vendes por litros, necesitas convertir para no perder dinero.
> *   🏗️ **Práctica:** Permite planificar el envasado industrial. ¿Cuántas botellas de $75 \text{ cl}$ caben en un tanque de $1,000 \text{ l}$? La conversión te da la respuesta.
> *   📊 **Cotidiana:** Te ayuda a entender las etiquetas de productos domésticos (limpiadores, refrescos o medicinas) que usan escalas variadas como $\text{cl}$, $\text{l}$ o $\text{dal}$.

---

## 📌 ¿Qué es la Conversión de Unidades de Capacidad?

> [!note] Definición sencilla
> Convertir unidades es, en esencia, cambiar la "etiqueta" con la que medimos un líquido sin alterar la cantidad real de dicho líquido. Es como cambiar un billete de $\$10$ por diez monedas de $\$1$: el valor total es idéntico, pero la forma de contarlo cambia.

Para realizar esto de forma profesional, usamos el **Factor de Conversión**. Es una fracción que equivale exactamente a $1$ (la "magia del uno"), donde el numerador y el denominador representan la misma cantidad pero en unidades distintas. Por ejemplo, como $1 \text{ m} = 100 \text{ cm}$, la fracción $\frac{1 \text{ m}}{100 \text{ cm}}$ es igual a $1$. Al multiplicar por ella, el valor original no cambia, ¡solo su etiqueta!

> [!warning] ⚠️ Error común
> Nunca realices operaciones matemáticas (sumas, restas o divisiones) si las unidades son diferentes (ej. hectolitros con centilitros). **Solución:** Primero debes convertir todas las cantidades a una unidad común, preferiblemente la más pequeña para trabajar con números enteros y evitar decimales complicados.

> [!tip] 💡 Truco para recordarlo: La Escalera
> - **Al bajar** la escalera (hacia una unidad menor): Multiplica por $10$ por cada escalón.
> - **Al subir** la escalera (hacia una unidad mayor): Divide entre $10$ por cada escalón.

---

## Procedimiento Paso a Paso

```text
PASO 1 → Identificar la unidad de origen (lo que tienes) y la unidad de destino (a donde quieres llegar).
PASO 2 → Seleccionar el factor de conversión adecuado o contar los "escalones" entre unidades.
PASO 3 → Multiplicar (si bajas a una unidad menor) o dividir (si subes a una unidad mayor).
PASO 4 → Realizar la operación aritmética y aplicar la "cancelación diagonal" de unidades para simplificar el resultado.
```

---

## Ejemplos Guiados

```ad-example
title: Ejemplo 1: De Hectolitros a Centilitros (Básico)
**Problema:** Se quieren envasar $3 \text{ hl}$ en botellas de $85 \text{ cl}$. ¿Cuántas botellas se necesitan?

1. **Conversión:** Para pasar de $\text{hl}$ a $\text{cl}$ bajamos 4 escalones ($\text{hl} \rightarrow \text{dal} \rightarrow \text{l} \rightarrow \text{dl} \rightarrow \text{cl}$). Multiplicamos por $10,000$.
   $$3 \text{ hl} \times 10,000 = 30,000 \text{ cl}$$
2. **División de capacidad:** Dividimos el total entre la capacidad del envase: 
   $$\frac{30,000 \text{ cl}}{85 \text{ cl}} \approx 352.94$$
3. **Lógica de experto:** Matemáticamente, $352.94$ se redondearía a $353$. En la práctica, necesitamos **353 botellas**, ya que con $352$ nos sobraría líquido sin envasar.
**Resultado:** Se necesitan **353 botellas**.
```

```ad-example
title: Ejemplo 2: Factores de Conversión (La Magia del Uno)
**Problema:** Convertir $30 \text{ cm}$ a metros usando la fracción unitaria.

1. **Equivalencia:** Sabemos que $1 \text{ m} = 100 \text{ cm}$.
2. **Planteamiento:** Escribimos la medida original y multiplicamos por el factor, colocando la unidad a eliminar en posición diagonal (abajo).
   $$30 \text{ cm} \times \frac{1 \text{ m}}{100 \text{ cm}}$$
3. **Cancelación:** Los $\text{cm}$ arriba y abajo se cancelan.
   $$\frac{30 \times 1 \text{ m}}{100} = 0.3 \text{ m}$$
**Resultado:** **$0.3 \text{ m}$**.
```

```ad-example
title: Ejemplo 3: Decilitros a Centilitros (Intermedio)
**Problema:** ¿Cuántas botellas de $70 \text{ cl}$ se necesitan para envasar $4 \text{ dl}$?

1. **Convertir a la unidad menor:** De $\text{dl}$ a $\text{cl}$ bajamos un escalón (multiplicamos por $10$).
   $$4 \text{ dl} \times 10 = 40 \text{ cl}$$
2. **Análisis:** Queremos meter $40 \text{ cl}$ en una botella donde caben $70 \text{ cl}$.
**Resultado:** Solo se necesita **1 botella** (y no se llenará completamente).
```

```ad-example
title: Ejemplo 4: Aplicación Económica ($USD)
**Problema:** Un comerciante compró vino por $\$27,000$, pagando $\$180$ por cada decálitro ($\text{dal}$). ¿A qué precio debe vender el litro para ganar $\$3,000$?

1. **Cantidad comprada:** $\$27,000 \div \$180/\text{dal} = 150 \text{ dal}$.
2. **Conversión a litros:** $150 \text{ dal} \times 10 = 1,500 \text{ l}$.
3. **Meta de recaudación:** Costo ($\$27,000$) + Ganancia deseada ($\$3,000$) = $\$30,000$.
4. **Precio final:** 
   $$\frac{\$30,000}{1,500 \text{ l}} = \$20$$
**Resultado:** Debe vender cada litro a **$\$20$**.
```

---

## Ejercicios Prácticos

```ad-abstract
title: 📝 Practica lo aprendido

**Nivel Verde (Fácil)**
1. Convierte $5 \text{ litros}$ a mililitros.
2. Convierte $2 \text{ hectolitros}$ a litros.
3. Convierte $10 \text{ decilitros}$ a centilitros.
4. Convierte $500 \text{ centilitros}$ a litros.

**Nivel Amarillo (Medio)**
1. ¿Cuántos vasos de $20 \text{ cl}$ se pueden llenar con $2 \text{ decálitros}$ de agua?
2. Se tienen $5 \text{ hectolitros}$ de jugo y se quieren envasar en botellas de $75 \text{ cl}$. ¿Cuántas botellas se requieren?
3. ¿Cuántas botellas de $50 \text{ cl}$ se llenan con $8 \text{ litros}$ de leche?
4. Tienes $12 \text{ decilitros}$, ¿te alcanza para llenar una jarra de $1.5 \text{ litros}$?

**Nivel Rojo (Avanzado)**
1. Un comerciante compra $2 \text{ hl}$ de aceite por $\$40,000$. Si quiere ganar $\$10,000$ en total, ¿a qué precio debe vender el litro?
2. Se compran $300 \text{ dal}$ de refresco por $\$15,000$. Si se vende a $\$8$ el litro, ¿cuál es la ganancia total?
3. Un tanque de $4 \text{ hl}$ de vino costó $\$32,000$ (a $\$80$ por litro). ¿Cuántos decálitros se compraron originalmente?
4. Se quiere envasar $1 \text{ hl}$ en envases de $25 \text{ cl}$. Si cada envase se vende a $\$2$, ¿cuánto dinero se recaudará en total?
```

```ad-success
title: ✅ Respuestas
**Verde:** 1) $5,000 \text{ ml}$ | 2) $200 \text{ l}$ | 3) $100 \text{ cl}$ | 4) $5 \text{ l}$
**Amarillo:** 1) $100 \text{ vasos}$ | 2) $667 \text{ botellas}$ | 3) $16 \text{ botellas}$ | 4) No (son $1.2 \text{ l}$)
**Rojo:** 1) $\$250$ por litro | 2) $\$9,000$ de ganancia | 3) $40 \text{ dal}$ | 4) $\$800$
```

---

## Autoevaluación

```ad-question
title: Pon a prueba tu comprensión
1. **Conceptual:** Al multiplicar una medida por un factor de conversión como $\frac{100 \text{ cm}}{1 \text{ m}}$, ¿por qué decimos que el valor no cambia?
2. **Procedimental:** Si aplicas la regla de la escalera para pasar de $5 \text{ dl}$ a $\text{cl}$, ¿cuál es el resultado final?
3. **Aplicación $USD:** Si un comerciante paga $\$200$ por un hectolitro de aceite, ¿cuál es el costo de un solo litro?
```

---

> [!tip] 💡 En la próxima clase
> Utilizaremos estos fundamentos de conversión de unidades de capacidad para compararlos con los sistemas de **volumen** (metros cúbicos) y **masa** (gramos), estableciendo puentes definitivos entre diferentes magnitudes físicas.

> [!info] 🧭 Navegación
> - Anterior: [[Clase 05 — Unidades de Longitud]]
> - Índice: [[00 - Índice del curso]]
> - Fin del bloque: ¡Felicidades por completar el Bloque 2!