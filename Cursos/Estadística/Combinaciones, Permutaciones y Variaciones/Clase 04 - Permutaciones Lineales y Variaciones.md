# Clase 04 — Permutaciones Lineales y Variaciones

**tags:** #algebra #linearpermutation
**Curso:** [[00 - Índice del curso]] | Bloque 2 | Lección 4 de 6

```ad-abstract
title: 🧭 Navegación
[[Clase 03]] | [[00 - Índice del curso|Índice]] | [[Clase 05]]
```

```ad-abstract
title: 🌍 Relevancia y aplicaciones
La capacidad de organizar elementos de forma lineal es fundamental cuando nos enfrentamos a espacios limitados donde el orden determina el resultado. Ya sea que estemos asignando asientos en un cine o formando una fila, entender las permutaciones nos permite conocer todas las posibilidades lógicas de organización.

- 💵 **Seguridad Financiera:** El uso de variaciones permite calcular la robustez de códigos de seguridad de 4 dígitos (como los usados en transferencias bancarias) o generar etiquetas de precios únicos en subastas.
- 🏗️ **Logística de Eventos:** Organizar personas en filas o butacas consecutivas para optimizar el espacio y cumplir con protocolos específicos, como asegurar que ciertos grupos permanezcan juntos.
- 📊 **Situación Cotidiana:** El análisis de anagramas o la formación de palabras (con o sin sentido) a partir de un conjunto de letras limitado para juegos de ingenio o lingüística.
```

### 📌 Conceptos Clave (Permutación vs. Variación)

```ad-abstract
title: 📌 ¿Qué es Linear permutation?
Es el ordenamiento de **todos** los elementos disponibles en una fila o línea recta donde el orden sí importa. Si cambias de lugar un solo elemento, el resultado se considera distinto. 

**Nota técnica:** La permutación es, en realidad, un tipo especial de variación donde usamos todos los elementos disponibles ($n = r$).
```

```ad-warning
title: ⚠️ Error común
Muchos estudiantes confunden ambos conceptos al no observar si sobran elementos.
- **Incorrecto:** Usar la fórmula de permutación si solo debes elegir a 2 personas de un grupo de 10 para cargos distintos.
- **Correcto:** Identificar que si sobran elementos (solo usas una parte del total), es una **Variación**. La permutación exige usar el grupo completo.
```

```ad-tip
title: 💡 Truco para recordarlo
Utiliza la **"Regla de las 3 condiciones"** antes de empezar:
1. **¿Importa el orden?** (Si intercambio dos elementos, ¿cambia el resultado?).
2. **¿Entran todos?** (¿Uso todos los elementos o solo una parte?).
3. **¿Hay repetición?** (¿Se puede repetir un elemento o son únicos?).
```

### 🛠️ Procedimiento: El Método de las Cajitas

Este método visual permite resolver problemas sin depender exclusivamente de fórmulas:

```text
PASO 1 → Dibujar tantas cajas como posiciones disponibles haya: [ ] [ ] [ ]
PASO 2 → Identificar cuántas opciones existen para la primera caja.
PASO 3 → Determinar si hay repetición:
         - Sin repetición: Se resta una opción en cada caja siguiente.
         - Con repetición: Se mantiene el mismo número de opciones en todas.
PASO 4 → Multiplicar los valores de todas las cajas (Principio multiplicativo).
```

### 📝 Ejemplos Prácticos

```ad-example
title: Ejemplo 1: Caso Básico (Anagramas)
**Problema:** ¿Cuántas palabras distintas se pueden formar con las letras de la palabra "PARTIDO"?
**Solución:**
1. "PARTIDO" tiene 7 letras diferentes (n=7).
2. Como se usan todas y el orden importa, es una permutación de 7.
3. Cálculo: $7! = 7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1 = 5,040$ formas.
```

```ad-example
title: Ejemplo 2: Restricciones (Cine)
**Problema:** Una familia de 2 padres y 3 hijos se sienta en 5 butacas. ¿De cuántas formas pueden hacerlo si los padres deben ir en los extremos?
**Solución:**
1. **Extremos (Padres):** Hay 2 opciones para el primer asiento y 1 para el último ($2!$).
2. **Centro (Hijos):** Los 3 hijos ocupan los 3 asientos restantes ($3!$).
3. **Total:** $2! \times 3! = (2 \times 1) \times (3 \times 2 \times 1) = 2 \times 6 = 12$ maneras.
```

```ad-example
title: Ejemplo 3: Caso Avanzado (Parejas juntas)
**Problema:** 4 parejas de novios se sientan en una fila de 8 asientos. ¿De cuántas formas lo hacen si cada pareja debe estar siempre junta?
**Solución:**
1. **Bloques:** Tratamos a cada pareja como 1 unidad. Tenemos 4 grupos para ordenar: $4!$ formas ($24$).
2. **Permutación interna:** Cada una de las 4 parejas puede ordenarse de 2 formas (A-B o B-A). Aplicamos el principio multiplicativo para las 4 parejas: $2 \times 2 \times 2 \times 2 = 2^4$ ($16$).
3. **Total:** $4! \times 2^4 = 24 \times 16 = 384$ formas.
```

```ad-example
title: Ejemplo 4: Aplicación USD (Precios de Subasta)
**Problema:** Se crean etiquetas de precios de 4 dígitos (0-9). Si el precio debe ser mayor a \$6,000 y se permite repetir dígitos, ¿cuántas etiquetas existen?
**Solución:**
1. **Caja 1:** Solo dígitos 6, 7, 8 o 9 para superar los 6,000 (4 opciones).
2. **Cajas 2, 3 y 4:** Cualquier dígito del 0 al 9 (10 opciones cada una).
3. **Cálculo inicial:** $4 \times 10 \times 10 \times 10 = 4,000$.
4. **Restricción:** Restamos el caso exacto "6000" porque buscamos valores *estrictamente mayores*: $4,000 - 1 = 3,999$ opciones.
```

### ✍️ Ejercicios para el Estudiante

```ad-question
title: 🟢 Nivel Fácil
Usando las letras de la palabra **GATO**:
1. ¿Cuántas palabras distintas se pueden formar en total?
2. ¿Cuántas terminan con la letra 'O'?
3. ¿Cuántas inician en 'G' y terminan en 'O'?
```

```ad-question
title: 🟡 Nivel Medio
En una comunidad de vecinos, se deben elegir los cargos de **Presidente** y **Secretario**. Si hay 10 vecinos postulados y una persona no puede ocupar ambos cargos:
1. ¿De cuántas formas distintas se pueden cubrir estos puestos?
```

```ad-question
title: 🔴 Nivel Avanzado
1. **Fila de cine:** 4 mujeres y 3 hombres hacen fila. ¿De cuántas formas se ubican si las mujeres deben ir primero?
2. **Grupos separados:** 6 amigos (3 hombres y 3 mujeres) se toman una foto. ¿De cuántas formas se ubican si los hombres van juntos y las mujeres también juntas?
3. **Contexto USD:** Si cada combinación del ejercicio anterior (6 amigos) representara un diseño de entrada con un costo de \$1 USD, ¿cuál sería la recaudación total al vender todos los diseños posibles?
```

### 🔑 Respuestas para el Docente

```ad-success
title: Soluciones Detalladas
- **GATO:** Total = 24; Terminan en 'O' = 6; Inician 'G'/Terminan 'O' = 2.
- **Vecinos:** $10 \times 9 = 90$ formas (Variación sin repetición).
- **Mujeres/Hombres:** $4! \times 3! = 24 \times 6 = 144$ formas.
- **Amigos juntos:** $2! (\text{bloques}) \times 3! (\text{hombres}) \times 3! (\text{mujeres}) = 2 \times 6 \times 6 = 72$ formas.
- **Recaudación USD:** 72 combinaciones $\times$ \$1 USD = **$72 USD**.
```

### 📋 Mini-prueba de Autoevaluación

```ad-question
title: Autoevaluación
1. **Conceptual:** Si de 10 elementos disponibles solo selecciono 3 para puestos distintos, ¿estoy ante una Permutación o una Variación?
2. **Procedimental:** ¿Cuántos números de 3 cifras **distintas** se pueden formar con los dígitos del 1 al 7?
3. **Aplicación USD:** Se requiere crear códigos de precios de 4 dígitos que sean **pares**. ¿Cuántos códigos se pueden formar usando los dígitos del 0 al 9 (permitiendo repetición)?
```

```ad-tip
title: 💡 En la próxima clase
Ahora que dominas el arte de ordenar elementos donde el orden es vital, estudiaremos qué sucede cuando el orden **NO** importa para el resultado final: daremos paso a las **Combinaciones**.
```

```ad-abstract
title: 🧭 Navegación
[[Clase 03]] | [[00 - Índice del curso|Índice]] | [[Clase 05]]
```