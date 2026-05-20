# Clase 06 — Solución de Problemas con Sistemas de Ecuaciones Lineales 2x2

#algebra #solucindeproble

---
[← Clase Anterior]([[clase-05]]) | [Siguiente Clase →]([[clase-07]])
---

## 1. ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> ¡Bienvenidos, detectives matemáticos! Aprender a traducir el lenguaje cotidiano al algebraico es como adquirir un superpoder de traducción: nos permite convertir situaciones de total incertidumbre en problemas con solución exacta. Al dominar los sistemas 2x2, dejamos de adivinar y empezamos a calcular con precisión.
> 
> - **💵 Dinero:** Determinar el precio exacto de productos individuales (como entradas, bolígrafos o cuadernos) cuando solo conocemos el total de compras combinadas.
> - **🏗️ Logística:** Resolver inventarios rápidos basándonos en partes de un objeto, como contar vehículos totales a partir del número de ruedas en un parqueadero.
> - **📊 Biología/Granja:** Clasificar especies de forma eficiente utilizando sus características físicas, como el número de patas y cabezas en un recinto.

## 2. Concepto clave

> [!note] 📌 ¿Qué es Solución de problemas con Sistemas de Ecuaciones Lineales 2x2?
> Para nosotros, esto significa usar **dos pistas** (ecuaciones) para encontrar **dos valores secretos** (incógnitas). Es un proceso de deducción donde cada dato nos acerca a la respuesta final.

> [!warning] ⚠️ Error común
> Un error muy frecuente es el manejo de la "diferencia". Al plantear una resta como $x - y = 36$, el resultado positivo nos indica que $x$ DEBE ser el número mayor. Como regla de oro de la Fuente 1: resta siempre el menor del mayor si el resultado proporcionado es positivo; de lo contrario, los signos te darán problemas más adelante.

> [!tip] 💡 Truco para recordarlo
> ¡Dale nombre a tus sospechosos! No te limites a usar $x$ o $y$. Usa la inicial del objeto que buscas: **N** para Niños, **A** para Adultos o **G** para Gallinas. Esto evita que, al final del procedimiento, olvides qué valor corresponde a cada incógnita.

## 3. Procedimiento paso a paso

```text
PASO 0 → Análisis inicial: Observa si el sistema ya está listo para sumar (si una variable tiene el mismo número pero signo opuesto, como +y y -y).
PASO 1 → Asignar variables: Usa nombres claros (ej. G para gallinas, C para conejos).
PASO 2 → Traducir: Convierte el enunciado a dos ecuaciones algebraicas.
PASO 3 → Eliminación: Multiplica una (o ambas) ecuaciones por un número que permita eliminar una variable al sumarlas.
PASO 4 → Resolver y Reemplazar: Halla la primera incógnita, sustitúyela para encontrar la segunda y ¡verifica siempre en el enunciado original!
```

## 4. Ejemplos Desarrollados

```ad-example
title: Ejemplo 1: El misterio de los números
**Problema:** La suma de dos números es 226 y su diferencia es 36. ¿Cuáles son los números?
1. **Planteamiento:** Sea $x$ el mayor y $y$ el menor.
   - Suma: $x + y = 226$
   - Diferencia: $x - y = 36$
2. **Resolución:** ¡Fíjate! El sistema ya está listo (Paso 0) porque $+y$ y $-y$ se cancelan solos al sumar.
   - $2x = 262 \rightarrow x = 131$.
3. **Segunda variable:** Si el mayor es 131, entonces $131 + y = 226$, lo que nos da $y = 95$.
**Verificación:** $131 + 95 = 226$ y $131 - 95 = 36$. ¡Perfecto!
```

```ad-example
title: Ejemplo 2: Patas en la granja
**Problema:** En un corral hay gallinas ($G$) y conejos ($C$). Hay 14 cabezas y 38 patas en total.
1. **Planteamiento:** 
   - Cabezas: $G + C = 14$ (Cada animal tiene una cabeza).
   - Patas: $2G + 4C = 38$. **Ojo aquí:** Multiplicamos $G$ por 2 porque las gallinas tienen 2 patas, y $C$ por 4 porque los conejos tienen 4.
2. **Resolución:** Multiplicamos la primera ecuación por $-2$ para eliminar las $G$.
   - $-2G - 2C = -28$
   - $2G + 4C = 38$
   - Al sumar: $2C = 10 \rightarrow C = 5$.
3. **Resultado:** Si hay 5 conejos, por lógica faltan 9 gallinas para llegar a las 14 cabezas.
```

```ad-example
title: Ejemplo 3: El parqueadero de vehículos
**Problema:** Hay 65 vehículos entre coches ($C$) y motos ($M$). El total de ruedas es 214.
1. **Planteamiento:** 
   - Vehículos: $C + M = 65$
   - Ruedas: $4C + 2M = 214$
2. **Resolución:** Multiplicamos la primera por $-2$ para eliminar las motos ($M$).
   - $-2C - 2M = -130$
   - $4C + 2M = 214$
   - Al sumar: $2C = 84 \rightarrow C = 42$.
3. **Segunda variable:** $42 + M = 65 \rightarrow M = 23$.
**Respuesta:** Hay 42 coches y 23 motos.
```

```ad-example
title: Ejemplo 4: Entradas al parque
**Problema:** 6 niños ($N$) y 5 adultos ($A$) pagan $177. 3 niños y un adulto pagan $57.
1. **Planteamiento:** 
   - $6N + 5A = 177$
   - $3N + A = 57$ (Recuerda que escribir $1A$ o simplemente $A$ es lo mismo, el 1 es "invisible").
2. **Resolución:** Multiplicamos la segunda ecuación por $-5$ para eliminar las $A$.
   - $6N + 5A = 177$
   - $-15N - 5A = -285$
   - Al sumar: $-9N = -108 \rightarrow N = 12$.
3. **Segunda variable:** Reemplazamos en la más sencilla: $3(12) + A = 57 \rightarrow 36 + A = 57 \rightarrow A = 21$.
**Respuesta:** Niño: $12, Adulto: $21.
```

## 5. Ejercicios para el estudiante

- 🟢 **Fácil:** La suma de dos números es 150 y su diferencia es 40. Encuentra ambos números.
- 🟡 **Medio:** En una habitación hay personas y arañas. Si contamos 10 cabezas y 44 patas, ¿cuántas personas (2 patas) y arañas (8 patas) hay?
- 🔴 **Avanzado:** En la papelería, 3 bolígrafos ($B$) y 2 cuadernos ($C$) cuestan $1100. Si compras 1 bolígrafo y 2 cuadernos del mismo tipo, pagas $700. ¿Cuál es el precio de cada artículo?

---
> [!check] ✅ Respuestas para el docente
> - **Fácil:** 95 y 55.
> - **Medio:** 6 personas y 4 arañas.
> - **Avanzado:** Bolígrafo = $200, Cuaderno = $250.

## 6. Mini-prueba de autoevaluación

```ad-question
title: Pregunta 1
¿Qué operación matemática representa la palabra "diferencia" al plantear una ecuación?
*Respuesta: La resta.*
```

```ad-question
title: Pregunta 2
Si tienes el sistema $x + y = 10$ y $x - y = 2$, ¿cuál es el valor de $x$ aplicando el Paso 0?
*Respuesta: Sumamos directo: $2x = 12 \rightarrow x = 6$.*
```

```ad-question
title: Pregunta 3
Un helado ($H$) y un dulce ($D$) cuestan $15. El helado cuesta $5 más que el dulce ($H = D + 5$). ¿Cuánto cuesta el dulce?
*Respuesta: $5. (Chequeo mental: Si el dulce vale 5, el helado vale 10. 10 + 5 = 15. ¡Correcto!).*
```

## 7. Cierre y Navegación

> [!tip] 💡 En la próxima clase
> ¡Excelente trabajo hoy! En la siguiente sesión subiremos el nivel analizando problemas con **coeficientes decimales y fraccionarios**. No cambian las reglas, solo el tipo de números. ¡Prepárate!

---
[← Clase Anterior]([[clase-05]]) | [Siguiente Clase →]([[clase-07]])
---