# Clase 06 — Combinaciones: ¿Qué tan rentable es la lotería?

`#algebra #combinations`

[<- Clase 05 | Inicio | Clase 07 ->]

## 1. ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> Las combinaciones son la clave para desmitificar el azar, permitiéndonos calcular con precisión las probabilidades en juegos y sorteos. Su dominio es vital para la gestión de riesgos financieros y para estructurar grupos de trabajo donde la equidad de roles es la prioridad absoluta.

- **💵 Aplicación USD:** Si intentaras garantizar el premio mayor comprando todas las variantes de una lotería de 49 números (escogiendo 6), tendrías que invertir $13,983,816 USD, asumiendo un costo de $1 USD por cartón.
- **🏗️ Aplicación práctica:** Es el método matemático para diseñar comités técnicos o jurados donde todos los integrantes tienen el mismo peso en la toma de decisiones.
- **📊 Situación cotidiana:** Permite determinar el número total de encuentros en torneos de "todos contra todos" (round-robin), optimizando la logística deportiva.

## 2. Entendiendo la esencia: El orden no importa

> [!note] 📌 ¿Qué es una combinación?
> Imagina que estás marcando un cartón de lotería. Si marcas primero el 5 y luego el 10, es exactamente la misma apuesta que si marcas primero el 10 y luego el 5. El cartón final no cambia. En matemáticas, una combinación es una selección de elementos de un grupo donde **el orden en que los eliges no altera el resultado final**.

> [!warning] ⚠️ Error común
> No confundas combinación con permutación. En una permutación, el orden es crítico (como en la clave de una caja fuerte: 1-2-3 no abre si la clave es 3-2-1). En una combinación, el grupo {1, 2, 3} es idéntico al grupo {3, 2, 1}.

> [!tip] 💡 Truco para recordarlo
> Piensa en una ensalada: no importa si pones primero el tomate o la lechuga, el resultado sigue siendo una ensalada de tomate y lechuga. "Combinar es mezclar sin jerarquía".

## 3. Procedimiento paso a paso

```text
1. Identificar el total de elementos (n) y el tamaño del subgrupo (r).
2. Confirmar que el orden no importa y que no hay repetición de elementos.
3. Aplicar la fórmula: C(n, r) = n! / (r! * (n - r)!).
4. Simplificar factores en el numerador y denominador antes de multiplicar.
```

## 4. Ejemplos Desarrollados

> [!example] Ejemplo 1: El cálculo real de la lotería (Básico)
> ¿Cuántas formas hay de elegir 6 números entre el 1 y el 49?
> - **Datos:** n = 49, r = 6.
> - **Planteamiento:** C(49, 6) = 49! / (6! * 43!).
> - **Simplificación (Estilo Alex):** Extendemos el 49 hasta el 43: (49 * 48 * 47 * 46 * 45 * 44 * 43!) / ( (6 * 5 * 4 * 3 * 2 * 1) * 43!). 
> - **Cancelación inteligente:** Cancelamos 43!. Luego, notamos que 6 * 2 * 4 = 48, así que eliminamos el 48 del numerador. Después, 5 * 3 = 15; al dividir 45 entre 15 nos queda 3.
> - **Operación final:** 49 * 47 * 46 * 3 * 44 = 13,983,816 formas.

> [!example] Ejemplo 2: Comisión mixta de trabajo
> Se requiere formar un comité de 5 hombres y 5 mujeres, elegidos de un grupo de 12 hombres y 10 mujeres. Es una **combinación simple** (una persona no puede ocupar dos puestos).
> - **Hombres:** C(12, 5) = 12! / (5! * 7!). Simplificando: (12 * 11 * 10 * 9 * 8) / (5 * 4 * 3 * 2 * 1). Aquí, 4 * 3 = 12 (cancelamos el 12) y 5 * 2 = 10 (cancelamos el 10). Queda 11 * 9 * 8 = 792.
> - **Mujeres:** C(10, 5) = 10! / (5! * 5!). Simplificando: (10 * 9 * 8 * 7 * 6) / (5 * 4 * 3 * 2 * 1). Cancelamos 5 * 2 = 10 y simplificamos 8 / 4 = 2 y 9 / 3 = 3. Queda 2 * 3 * 7 * 6 = 252.
> - **Total:** Aplicamos la Regla de la Multiplicación (H y M): 792 * 252 = 199,584 formas.

> [!example] Ejemplo 3: Selección de libros (Avanzado)
> Elegir 2 libros de matemáticas (de 6 disponibles) y 2 de física (de 3 disponibles).
> - **Matemáticas:** C(6, 2) = 6! / (2! * 4!) = (6 * 5) / 2 = 15 formas.
> - **Física:** C(3, 2) = 3! / (2! * 1!) = (3 * 2!) / 2! = 3 formas.
> - **Total:** 15 * 3 = 45 maneras.

> [!example] Ejemplo 4: Análisis de rentabilidad financiera (USD)
> Si cada cartón de la lotería del Ejemplo 1 cuesta $2 USD:
> - **Costo total:** 13,983,816 * $2 = $27,967,632 USD.
> - **Perspectiva:** Si el premio acumulado es de $10,000,000 USD, perderías casi $18 millones de dólares al intentar asegurar el triunfo. Matemáticamente, participar en estas loterías suele ser un "impuesto al desconocimiento de la estadística".

## 5. Ejercicios para el estudiante

> [!abstract] 🟢 Fácil: Torneo deportivo
> En un campeonato participan 16 equipos bajo la modalidad "todos contra todos". ¿Cuántos partidos deben programarse si solo juegan una vez entre ellos? (n = 16, r = 2).

> [!abstract] 🟡 Medio: Consejo Escolar
> Se debe formar una comisión con 3 miembros de cada uno de estos grupos:
> - Grupo A: 7 miembros.
> - Grupo B: 10 miembros.
> - Grupo C: 9 miembros.
> ¿Cuántas combinaciones diferentes existen para integrar la comisión completa?

> [!abstract] 🔴 Avanzado: Naipes y costos (USD)
> 1. Calcula cuántas combinaciones de 5 cartas se pueden extraer de una baraja de 52 naipes.
> 2. Si cada combinación de 5 cartas costara $0.50 USD, ¿cuánto dinero se necesitaría para comprar todas las manos posibles?

## 6. Respuestas y Autoevaluación

> [!success] Solucionario
> - **Fácil:** 120 partidos (simplificación: 16 * 15 / 2 = 8 * 15).
> - **Medio:** 352,800 formas (C(7,3) * C(10,3) * C(9,3) = 35 * 120 * 84).
> - **Avanzado:** 2,598,960 combinaciones. Costo: $1,299,480 USD. (Nota: Esto demuestra la bajísima probabilidad de obtener una mano específica, tema que veremos en la Clase 07).

### Mini-prueba de autoevaluación

**1. ¿Por qué el orden no importa en una combinación?**
A) Porque los elementos son idénticos entre sí.
B) Porque el grupo resultante es el mismo sin importar la secuencia de elección.
C) Porque siempre se pueden repetir los elementos.
*Correcta: B. El conjunto final es lo que define la combinación.*

**2. En un problema donde debes elegir representantes de tres países distintos para un foro, ¿por qué multiplicas los resultados de las combinaciones de cada país?**
A) Porque la fórmula de la combinación requiere multiplicaciones internas.
B) Por la Regla de la Multiplicación, ya que los eventos (elegir de A, de B y de C) ocurren de forma conjunta para formar un solo grupo.
C) Porque así se simplifican más rápido los factoriales.
*Correcta: B. Cuando los grupos son independientes y deben combinarse simultáneamente, se multiplican sus posibilidades.*

**3. Si una lotería tiene 1 millón de combinaciones y el premio es de $500,000 USD cobrando $1 USD por boleto, ¿es rentable comprar todos los números?**
A) Sí, porque aseguras ganar el premio mayor.
B) No, porque la inversión ($1M) duplica el valor del premio ($0.5M).
C) Depende de cuántas personas más ganen el premio.
*Correcta: B. El análisis de rentabilidad muestra una pérdida neta evidente.*

## 7. Cierre y Navegación

Dominar las combinaciones es el paso previo indispensable para entrar al mundo de las probabilidades. En la próxima sesión, transformaremos estos números de combinaciones en porcentajes reales de éxito para entender qué tan probable es que ocurra un evento.

[<- Clase 05 | Inicio | Clase 07 ->]