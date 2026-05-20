# Clase 03 — Potencias con exponente fraccionario y Suma y resta de radicales

tags: #algebra #potencias #radicales #matematicas
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 3 de 14

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | | [[Clase 04|Clase 04 ➡]]

## ¿Por qué es importante esta clase?
Las potencias con exponente fraccionario y los radicales son dos formas de expresar la misma operación. Entender esta equivalencia permite simplificar expresiones algebraicas que parecen imposibles y es la base para entender el crecimiento y decrecimiento en modelos científicos y financieros.

- 💵 **Aplicación con $USD:** En finanzas, el cálculo de intereses compuestos o la depreciación de activos en periodos fraccionarios (ej. calcular el valor a los 6 meses o $1/2$ año) requiere el uso de raíces expresadas como exponentes.
- 🏗️ **Aplicación práctica:** Los arquitectos utilizan estas propiedades para ajustar dimensiones en diseños basados en áreas proporcionales, permitiendo escalar volúmenes a medidas lineales.
- 📊 **Situación cotidiana:** El ajuste de escalas en modelos físicos o mapas utiliza potencias fraccionarias para mantener la proporcionalidad entre dimensiones bidimensionales y tridimensionales.

## Concepto clave
Cualquier potencia con exponente fraccionario puede escribirse como un radical, donde el denominador de la fracción dicta el "tipo" de raíz.
$$a^{m/n} = \sqrt[n]{a^m}$$

> [!note] 📌 ¿Qué es una Potencia con exponente fraccionario?
> Para un estudiante de 12 años: Una fracción en el exponente es una "orden doble". El número de arriba (numerador) te dice a qué potencia elevar, y el número de abajo (denominador) te dice qué raíz sacar. 

> [!warning] ⚠️ Error común
> ❌ **Incorrecto:** Confundir el numerador con el índice.
> ✅ **Correcto:** El denominador siempre es el "asiento" o índice de la raíz. Además, recuerda que si una raíz no tiene número escrito en el índice (ej. $\sqrt{x}$), **siempre es un 2 invisible**.

> [!tip] 💡 Truco para recordarlo
> "El de abajo va a la raíz (como la raíz de un árbol que está abajo), el de arriba se queda feliz con la base".

## Procedimiento paso a paso
Para resolver sumas y restas de radicales y potencias fraccionarias, aplicamos la metodología de simplificación por factores primos:

1. **CONVERSIÓN:** Transforma potencias fraccionarias a radicales ($a^{m/n} \to \sqrt[n]{a^m}$).
2. **DESCOMPOSICIÓN:** Descompón los radicandos en factores primos (ej. $12 = 2^2 \cdot 3$).
3. **EXTRACCIÓN:** Saca factores de la raíz dividiendo su exponente por el índice de la raíz.
4. **SIMPLIFICACIÓN:** Multiplica los coeficientes externos resultantes.
5. **OPERACIÓN FINAL:** Suma o resta los "términos semejantes". Solo puedes sumar raíces que tengan el mismo índice y el mismo radicando (como si sumaras "perritos" con "perritos").

## Ejemplos de clase

```ad-example
title: Ejemplo 1 — Caso básico de exponente fraccionario
**Enunciado:** Resolver $(1/5)^{2/3}$.
**Procedimiento:**
1. El denominador 3 pasa como índice: $\sqrt[3]{(1/5)^2}$.
2. Elevamos numerador y denominador al cuadrado: $\sqrt[3]{1^2/5^2}$.
**Resultado:** $\sqrt[3]{1/25}$.
```

```ad-example
title: Ejemplo 2 — Simplificación y Suma (Nivel Profe Alex)
**Enunciado:** $\sqrt{12} + \sqrt{27}$
**Procedimiento:**
1. Descomponer 12: $2^2 \cdot 3$.
2. Descomponer 27: $3^2 \cdot 3$.
3. Extraer factores: $\sqrt{2^2 \cdot 3} + \sqrt{3^2 \cdot 3} = 2\sqrt{3} + 3\sqrt{3}$.
4. Sumar coeficientes (términos semejantes): $(2+3)\sqrt{3}$.
**Resultado:** $5\sqrt{3}$.
```

```ad-example
title: Ejemplo 3 — Caso avanzado con potencias de potencias
**Enunciado:** $(27)^{2/3}$
**Procedimiento:**
1. Convertir 27 a base prima: $3^3$.
2. Multiplicar exponentes: $3 \cdot (2/3) = 6/3 = 2$.
3. Resolver: $3^2 = 9$.
**Resultado:** 9.
```

```ad-example
title: Ejemplo 4 — Aplicación real con $USD
**Enunciado:** Un activo de $100 USD crece a una tasa de $(1.21)^{1/2}$ por periodo. ¿Cuál es su valor?
**Procedimiento:**
1. Convertir a raíz: $\sqrt{1.21}$. Como el índice es 2, es raíz cuadrada.
2. Calcular: $\sqrt{1.21} = 1.1$.
3. Multiplicar: $100 \cdot 1.1 = 110$.
**Resultado:** 110 USD.
```

## Ejercicios para el estudiante

```ad-abstract
title: 🟢 Fácil — Conversión y suma directa
1. Convertir $16^{1/2}$.
2. Resolver $3\sqrt{2} + 5\sqrt{2}$.
3. Resolver $5\sqrt{3} - 9\sqrt{3}$.
4. Convertir $(9/16)^{1/2}$.
```

```ad-abstract
title: 🟡 Medio — Simplificación necesaria
1. $\sqrt{50} + \sqrt{72} - 5\sqrt{2}$.
2. $\sqrt{20} + 3\sqrt{8} + 2\sqrt{5} - \sqrt{18}$.
3. $(32)^{1/5}$.
4. $\sqrt{24} + \sqrt{54}$.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
1. Una maquinaria se deprecia según la expresión $81^{3/4}$ dólares anuales. ¿Cuánto pierde al año? (Calcular $\sqrt[4]{81^3}$).
2. Un portafolio de $1000 USD se multiplica por $(1/27)^{1/3}$. ¿Cuánto dinero queda?
3. Resolver: $\sqrt[3]{1/27} + \sqrt[3]{8/27}$.
4. Operar: $3\sqrt{12} - \sqrt{27} + 2\sqrt{75}$.
```

```ad-success
title: ✅ Respuestas (para el docente)
- **Fácil:** 1) 4 | 2) $8\sqrt{2}$ | 3) $-4\sqrt{3}$ | 4) $3/4$.
- **Medio:** 1) $6\sqrt{2}$ | 2) $4\sqrt{5} + 3\sqrt{2}$ | 3) 2 | 4) $5\sqrt{6}$.
- **Avanzado:** 1) 27 USD | 2) 333.33 USD | 3) 1 | 4) $13\sqrt{3}$.
```

## Mini-prueba de autoevaluación

```ad-question
title: 🧪 Pregunta 1
¿Cuál es el resultado de $2\sqrt{3} + 5\sqrt{3}$?
a) $7\sqrt{6}$ 
b) $10\sqrt{3}$ 
c) $7\sqrt{3}$ 
d) $7\sqrt{9}$
**Respuesta:** c) — Aplicando la analogía de los "perritos", solo sumamos los coeficientes externos; la especie (raíz) no cambia.
```

```ad-question
title: 🧪 Pregunta 2
¿A qué es igual $16^{3/4}$?
a) 8 
b) 4 
c) 12 
d) 16
**Explicación:** Se transforma en $\sqrt[4]{16^3}$. Es más fácil sacar primero la raíz: $\sqrt[4]{16} = 2$, y luego elevar al cubo: $2^3 = 8$.
```

```ad-question
title: 🧪 Pregunta 3
Si una inversión de $100 USD se multiplica por $25^{1/2}$, ¿cuál es el total?
a) $2500 
b) $500 
c) $125 
d) $105
**Respuesta:** b) — $25^{1/2}$ es $\sqrt{25} = 5$. Multiplicamos $100 \cdot 5 = 500$.
```

## Notas para el próximo tema
> [!tip] 💡 En la próxima clase
> Conectaremos la extracción de factores con la **racionalización de denominadores**, aprendiendo a eliminar raíces de la parte inferior de una fracción para estandarizar resultados.

> [!info] 🧭 Navegación
> [[Clase 02|⬅ Clase 02]] | [[00 - Índice del curso|Índice]] | **Clase 03** | | [[Clase 04|Clase 04 ➡]]