# Clase 03 — Uso Correcto de la Calculadora en Trigonometría
tags: #algebra #trigonometrycor
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 12

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | | [[Clase 04|Clase 04 ➡]]

## ¿Por qué es importante esta clase?
En trigonometría, un ángulo es la porción del plano delimitada por **dos semirrectas**. Para medir esta porción, las calculadoras utilizan diferentes sistemas. Si tu herramienta no está "sintonizada" con el ejercicio, cada cálculo de Seno, Coseno o Tangente será erróneo. Configurar bien tu tecnología evita:

- 💵 **Desperdicio de dinero:** Un error de un solo grado en el corte de una viga de madera o metal puede arruinar el material y generar sobrecostos en construcción.
- 🏗️ **Fallas de diseño:** La estabilidad de puentes y edificios depende de funciones trigonométricas con precisión milimétrica.
- 📊 **Errores de ubicación:** Los sistemas GPS y de navegación requieren ángulos exactos para determinar coordenadas sin desviaciones peligrosas.

## Concepto clave
> [!note] 📌 ¿Qué es el Uso Correcto de la Calculadora en Trigonometría?
> Es sincronizar la unidad de medida del ángulo (Grados, Radianes o Gradientes) con el modo interno de la calculadora. Para entender por qué esto es necesario, observa que la **media vuelta** de un círculo se puede llamar de tres formas distintas:
> 
> | Sistema | Unidad | Valor de "Media Vuelta" | Indicador en Pantalla |
> | :--- | :--- | :--- | :--- |
> | **Sexagesimal** | Grados | $180^\circ$ | **D** (Degree) |
> | **Circular** | Radianes | $\pi$ | **R** (Radian) |
> | **Centesimal** | Gradianes | $200$ | **G** (Gradient) |

> [!warning] ⚠️ La trampa de la letra "G"
> Muchos estudiantes cometen el error de elegir el modo **G** pensando que significa "Grados". **¡Cuidado!** La **G** es de *Gradianes* (un sistema poco usado en la escuela). Para los grados normales ($0^\circ$ a $360^\circ$), debes usar siempre la **D**.

> [!tip] 💡 Truco para recordarlo
> - **D** de **D**edos (Los grados normales que contamos siempre).
> - **R** de **R**adio (Radianes, los que casi siempre llevan el símbolo $\pi$).
> - **G** de **G**radián (¡La trampa! No la uses a menos que te lo pidan).

## Procedimiento paso a paso

### Paso 0: Activar el Modo Matemático (Recomendado)
Para que las fracciones y raíces aparezcan en pantalla tal como están en tus libros (entrada/salida matemática):
1. Presiona `[SHIFT]` + `[MODE/SETUP]`.
2. Selecciona **1: MthIO** y luego **1: MathO**.

### Configuración de la Unidad Angular

#### Para Modelos Classwiz / Plus (Modernos)
1. Presiona `[SHIFT]` + `[MENU/SETUP]`.
2. Selecciona la opción **Unidad angular** (usualmente el número 2).
3. Elige: **1: Grado sexagesimal (D)**, **2: Radián (R)** o **3: Grado centesimal (G)**.
4. **Verifica:** Busca la letra pequeña (**D** o **R**) en la parte superior de la pantalla.

#### Para Modelos MS (Clásicos)
1. Presiona la tecla `[MODE]` **dos veces** hasta que aparezca el menú: `Deg  Rad  Gra`.
2. Presiona el número **1 (Deg)** para grados o **2 (Rad)** para radianes.
3. **Verifica:** Asegúrate de ver la **D** o la **R** en el visor.

---

## Ejemplos

```ad-example
title: Ejemplo 1 — Caso básico (Grados)
Calcular $\text{sen}(30^\circ)$.
1. Configurar en modo **DEG** (aparece la **D**).
2. Presionar `[sin]` `[30]` `[=]`.
✅ Resultado: **0.5** (o **1/2** en modo matemático).
```

```ad-example
title: Ejemplo 2 — Caso con Radianes (Uso de $\pi$)
Calcular $\text{sen}(\pi/2)$.
1. Configurar en modo **RAD** (aparece la **R**).
2. Presionar `[sin]`, usar tecla de fracción `[吕]`, poner `[SHIFT]` `[x10ˣ / π]` arriba y `[2]` abajo.
3. **Cerrar el paréntesis** al final.
✅ Resultado: **1**.
⚠️ *Nota: En modelos antiguos, si no cierras el paréntesis, la calculadora podría dar un error de sintaxis o calcular algo diferente.*
```

```ad-example
title: Ejemplo 3 — Raíz con ley de cosenos (Cuidado con MS)
Calcular $\sqrt{12^2 + 7^2 - 2(12)(7)\cos(40^\circ)}$.
1. **Modo Classwiz:** Presiona `[√]`, escribe todo dentro; la raíz se estira sola.
2. **Modo MS:** Debes abrir un paréntesis después de la raíz: `[√]` `[(]` `12^2 + 7^2...` `[)]`. Sin esto, la calculadora solo sacará raíz al primer número ($12^2$).
✅ Resultado: **8.01**.
```

```ad-example
title: Ejemplo 4 — Aplicación real con $USD
Si un panel solar de $55.06 USD requiere una longitud calculada como $25 / \text{sen}(27^\circ)$, determine el valor.
1. Modo **DEG**.
2. Ingresar `[25]` `[÷]` `[sin]` `[27]` `[=]`.
✅ Resultado: **55.06**.
```

## Ejercicios para el estudiante

```ad-abstract
title: 🟢 Fácil — Funciones Directas
1. $\text{sen}(30^\circ)$
2. $\cos(180^\circ)$
3. $\tan(45^\circ)$
4. $\text{sen}(0^\circ)$
```

```ad-abstract
title: 🟡 Medio — Ángulos DMS y Radianes
1. $\text{sen}(30^\circ 40' 15'')$ (Usa la tecla `[° ' '']` arriba de `[ENG]`).
2. $\tan(20^\circ 0' 15'')$ (Recuerda marcar **0** en la posición de los minutos).
3. $\cos(\pi)$ (Cambia a modo **Radian**).
4. $\text{sen}(3\pi)$ (Cambia a modo **Radian**).
```

```ad-abstract
title: 🔴 Avanzado — Aplicación y Funciones Inversas
1. **Costo de viga:** La viga mide $\sqrt{13^2 + 9^2 - 2(13)(9)\cos(67^\circ)}$ metros. Si el metro cuesta $100 USD, ¿cuál es el costo total? (Modo **DEG**).
2. **Ángulo inverso:** Calcula $\text{sen}^{-1}(10\text{sen}(115^\circ)/40)$. Usa `[SHIFT]` + `[sin]`.
3. **División trigonométrica:** Calcula $15\text{sen}(48^\circ) / \text{sen}(60^\circ)$.
4. **Conversión DMS:** Calcula $\tan^{-1}(8/3)$ y presiona la tecla `[° ' '']` para convertir el resultado a Grados, Minutos y Segundos.
```

```ad-success
title: ✅ Respuestas (para el docente)
🟢 **Fácil:** 1. [0.5] | 2. [-1] | 3. [1] | 4. [0]
🟡 **Medio:** 1. [0.51] | 2. [0.36] | 3. [-1] | 4. [0]
🔴 **Avanzado:** 1. [$1259] | 2. [13.09°] | 3. [12.87] | 4. [69° 26' 38'']
```

## Mini-prueba de autoevaluación

```ad-question
title: 🧪 Pregunta 1
¿Qué letra debe aparecer en pantalla para trabajar con grados sexagesimales (0 a 360)?
a) R
b) G
c) D
d) M
**Respuesta:** **c)**. La D es de Degree (Grado).
```

```ad-question
title: 🧪 Pregunta 2
Para ingresar 20 grados y 15 segundos (sin minutos), ¿cuál es la forma correcta?
a) 20 [,,,] 15 [,,,]
b) 20 [,,,] 0 [,,,] 15 [,,,]
c) 20.15 [,,,]
**Respuesta:** **b)**. La calculadora exige marcar el 0 en los minutos para entender que el siguiente valor son segundos.
```

```ad-question
title: 🧪 Pregunta 3
Si una rampa de $500 USD se calculó en modo DEG pero el plano pedía $\pi/4$ (Radianes), y esto causó una pérdida del 10%. ¿Cuánto dinero se perdió?
a) $5 USD
b) $50 USD
c) $10 USD
**Respuesta:** **b)**. El 10% de $500 es $50.
```

## Notas para el próximo tema
> [!tip] 💡 En la próxima clase
> Con el dominio técnico de la calculadora que has adquirido hoy, estamos listos para **resolver triángulos rectángulos**. Aprenderemos a encontrar lados y ángulos faltantes usando las razones trigonométricas.

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | | [[Clase 04|Clase 04 ➡]]