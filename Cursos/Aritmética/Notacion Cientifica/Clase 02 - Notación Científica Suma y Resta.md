# Clase 02 — Notación Científica: Suma y Resta

#algebra #scientificnotat

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 3

```ad-info
title: 🧭 Navegación
- Anterior: [[Clase 01 — Introducción y Conversión]]
- Índice: [[00 - Índice del curso]]
- Siguiente: [[Clase 03 — Multiplicación y División]]
```

---

```ad-info
title: 🌍 Relevancia y aplicaciones
Dominar la suma y resta en esta notación es como tener un "superpoder" para medir el universo. Nos permite combinar cantidades sin perdernos en una marea de ceros infinitos.

**¿Dónde lo verás?**
- 💵 **Finanzas (USD):** Al calcular la deuda externa de un país o presupuestos nacionales que alcanzan los billones ($10^{12}$).
- 🏗️ **Ingeniería y Nanotecnología:** Para medir capas de materiales tan delgadas como un átomo ($10^{-9}$).
- 📊 **Ciencia Cotidiana:** Para comparar el peso de un virus frente al de una bacteria o calcular distancias entre galaxias.
```

---

## Concepto clave

```ad-note
title: 📌 ¿Qué es...? La regla de los "Términos Semejantes"
En matemáticas, solo podemos sumar cosas que son "iguales". En álgebra, sumas $3a + 5a$ porque la letra es la misma. En notación científica, **la potencia de 10 es nuestra "letra"**. 

Para sumar o restar, los exponentes **deben ser idénticos**.
- **Se puede:** $3,2 (10^2) + 1,5 (10^2)$ — *Es como sumar manzanas con manzanas.*
- **No se puede (directamente):** $3,2 (10^2) + 1,5 (10^3)$ — *Es como sumar manzanas con naranjas.* ¡Debes igualarlas primero!
```

```ad-warning
title: ⚠️ Error común
Muchos estudiantes intentan sumar los coeficientes y los exponentes por separado.
**Incorrecto:** $(2 \times 10^2) + (3 \times 10^3) = 5 \times 10^5$.
¡Esto es un error grave! $200 + 3000$ no es $500.000$. Recuerda: los exponentes no se suman en la suma/resta; se igualan para que sirvan de etiqueta.
```

```ad-tip
title: 💡 Truco de Oro: La Ley de Compensación (Balance)
¡No te preocupes! Mover la coma es fácil si recuerdas este balance. Para que el valor no cambie, si una parte sube, la otra debe bajar:
- **Si el exponente SUBE ($\uparrow$):** La coma corre a la **IZQUIERDA** ($\leftarrow$). El número se hace más pequeño para compensar.
- **Si el exponente BAJA ($\downarrow$):** La coma corre a la **DERECHA** ($\rightarrow$). El número se hace más grande para compensar.
```

---

## Procedimiento paso a paso (Método de Exponentes Iguales)

```ad-important
title: 📋 Algoritmo de resolución
1. **Identificar el exponente mayor:** Es nuestra meta. (Recuerda que en negativos, $-2$ es mayor que $-4$).
2. **Igualar al mayor:** Convierte el número con el exponente menor moviendo su coma a la izquierda.
3. **Operar los coeficientes:** Suma o resta los decimales. 
   - *Regla de Profe Alex:* En la resta, el resultado lleva el signo del número con **mayor valor absoluto**.
4. **Mantener la base:** La potencia de 10 se queda exactamente igual.
5. **Ajuste final:** Si el resultado no está en notación científica estándar (un solo dígito distinto de cero antes de la coma), usa la **Ley de Compensación** para ajustarlo.
```

---

## Ejemplos prácticos

```ad-example
title: Ejemplo 1: Suma básica (Exponentes iguales)
**Operación:** $3,2 \times 10^2 + 1,5 \times 10^2$
1. **Verificación:** Ambos tienen $10^2$. ¡Perfecto!
2. **Suma:** $3,2 + 1,5 = 4,7$.
3. **Resultado:** $4,7 \times 10^2$.
*(Nota: Ya está en formato estándar).*
```

```ad-example
title: Ejemplo 2: Resta con signos y negativos
**Operación:** $3,5 \times 10^{-2} - 2 \times 10^{-4}$
1. **Mayor:** El $-2$ está más cerca del cero, por lo tanto es el mayor.
2. **Convertir:** El $-4$ debe subir 2 unidades para llegar a $-2$ ($\uparrow$). Movemos la coma del 2 dos lugares a la izquierda ($\leftarrow$): $0,02 \times 10^{-2}$.
3. **Restar:** $3,5 - 0,02 = 3,48$. Como 3,5 es positivo y mayor en valor absoluto, el resultado es positivo.
4. **Resultado:** $3,48 \times 10^{-2}$.
```

```ad-example
title: Ejemplo 3: Ajuste final (Tres términos)
**Operación:** $(3 \times 10^{-5}) + (0,2 \times 10^{-5}) - (1 \times 10^{-5})$
1. **Operación:** $(3 + 0,2 - 1) = 2,2$.
2. **Resultado directo:** $2,2 \times 10^{-5}$.
*¡Ojo! Si la suma diera 13,5, tendrías que mover la coma y subir el exponente.*
```

```ad-example
title: Ejemplo 4: Diferencia de Presupuestos (USD)
**Problema:** Restar $\$1,2 \times 10^8$ USD de un fondo de $\$5,2 \times 10^9$ USD.
1. **Igualar al mayor ($10^9$):** El $1,2 \times 10^8$ se convierte en $0,12 \times 10^9$ (sube exponente, coma a la izquierda).
2. **Restar:** $5,2 - 0,12 = 5,08$.
3. **Resultado:** $5,08 \times 10^9$ USD.
```

---

## Uso de la Calculadora (Serie MS: 82, 95, 570)

```ad-tip
title: 🛠️ Pro-Tips Técnicos
- **La Tecla Mágica:** No uses la tecla "$\times$" y luego el "10". Usa la tecla **`EXP`** o **`x10^x`**. Representa todo el bloque "$\times 10$".
- **Signos Negativos:** Para exponentes negativos, usa la tecla **`(-)`** (la de signo, arriba), no la de resta operativa.
- **Modo SCI (Científico):** 
	1. Pulsa `MODE` 3 veces hasta ver `SCI`. 
	2. Presiona `2`. 
	3. Te pedirá un número (0-9): esto define las **cifras significativas**. Selecciona `5` para una precisión técnica ideal.
- **Tecla ENG:** Si la presionas, la calculadora ajustará el exponente en múltiplos de 3 (formato ingeniería). Para volver, usa `SHIFT` + `ENG`.
```

---

## Ejercicios para el estudiante

```ad-abstract
title: 📝 ¡A practicar!
**Nivel Verde (Fácil):**
1. $2,4 \times 10^6 + 3,5 \times 10^6$
2. $9,8 \times 10^{-3} - 4,2 \times 10^{-3}$

**Nivel Amarillo (Medio):**
3. $5,1 \times 10^4 + 2,0 \times 10^3$
4. $1,5 \times 10^{-2} - 3,0 \times 10^{-3}$

**Nivel Rojo (Avanzado):**
5. **Ahorro Fiscal:** $\$ 4,5 \times 10^7$ USD + $\$ 8,2 \times 10^6$ USD.
6. **Operación Mixta:** $(3 \times 10^{-5}) + (2 \times 10^{-6}) - (1 \times 10^{-5})$.
```

```ad-success
title: ✅ Solucionario
1. $5,9 \times 10^6$
2. $5,6 \times 10^{-3}$
3. $5,3 \times 10^4$
4. $1,2 \times 10^{-2}$
5. $5,32 \times 10^7$ USD
6. $2,2 \times 10^{-5}$
```

---

## Mini-prueba de autoevaluación

```ad-question
title: Evalúa tu progreso
1. **Conceptual:** Para sumar $A \times 10^n$ y $B \times 10^m$, ¿qué debe ocurrir obligatoriamente?
   - a) $A$ debe ser igual a $B$.
   - b) $n$ debe ser igual a $m$.
   - c) La base debe ser distinta de 10.

2. **Procedimental:** ¿Cuál es el resultado de $2 \times 10^3 - 5 \times 10^2$ en notación estándar?
   - a) $1,5 \times 10^3$
   - b) $1,5 \times 10^2$
   - c) $-3 \times 10^1$

3. **Aplicación:** Si el presupuesto es $1,2 \times 10^4$ USD y gastas $8 \times 10^3$ USD, ¿cuánto queda en notación científica estándar?
   - a) $4,0 \times 10^3$ USD
   - b) $0,4 \times 10^4$ USD
   - c) $9,2 \times 10^3$ USD
```
*(Respuestas: 1-b, 2-a, 3-a)*

---

## Cierre de la clase
¡Increíble! Si lograste dominar el balance de la coma y la igualación de exponentes, ya tienes la base más difícil de la notación científica. **¡Eres un experto en escalas!** En la próxima clase, veremos multiplicación y división, donde los exponentes se vuelven mucho más "rebeldes" pero fáciles de manejar.

```ad-info
title: 🧭 Navegación
- Anterior: [[Clase 01 — Introducción y Conversión]]
- Índice: [[00 - Índice del curso]]
- Siguiente: [[Clase 03 — Multiplicación y División]]
```