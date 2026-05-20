# Clase 13: Conversión entre Fracciones y Decimales

**Tags:** #matemáticas #fracciones #decimales #aritmética #educación_básica  
**Curso:** Matemática Básica Superior

> [!info] 🧭 Navegación
> - [Concepto clave](#concepto-clave)
> - [Procedimiento paso a paso](#procedimiento-paso-a-paso)
> - [Ejemplos Resueltos](#ejemplos-resueltos)
> - [Ejercicios para el estudiante](#ejercicios-para-el-estudiante)
> - [Guía de Estudio](#guía-de-estudio-básica-superior)

---

> [!info] 🌍 Relevancia y aplicaciones
> La transición entre el lenguaje fraccionario y el decimal permite una comprensión profunda de las cantidades en contextos reales:
> - **💵 USD:** Al gestionar presupuestos, una fracción como "un cuarto de dólar" se traduce operativamente en **25 centavos** (o $0,25$ dólares) para transacciones exactas.
> - **🏗️ Práctica:** En el diseño técnico y construcción, las medidas suelen alternar entre fracciones de pulgada y decimales para garantizar precisión milimétrica en herramientas digitales.
> - **📊 Cotidiana:** Las calculadoras operan en sistema decimal; sin embargo, para reparticiones exactas (como dividir una herencia o un terreno), la fracción ofrece una precisión que el decimal (si es periódico como $0,333...$) a veces oculta.

---

### Concepto clave

Convertir una **fracción a decimal** es el proceso de ejecutar la división que la fracción representa. En este procedimiento, el **numerador** actúa como el dividendo y el **denominador** como el divisor. El resultado obtenido puede ser un decimal exacto (con un número finito de cifras) o un decimal periódico (donde una o varias cifras se repiten infinitamente).

> [!warning] ⚠️ Error común
> El error más frecuente es omitir el **"0 al cociente"**. Cuando al bajar una cifra del dividendo el número formado es menor que el divisor, es obligatorio colocar un cero en el cociente antes de continuar o bajar la siguiente cifra. Omitir este paso invalida el valor posicional del resultado.

> [!tip] 💡 Truco para recordarlo
> Memoriza la regla de oro pedagógica: **"Si bajas una cifra, debes poner una cifra en el cociente"**. Si el divisor no cabe, esa cifra es un **0**. Además, recuerda que la coma decimal aparece únicamente cuando añades el **primer cero auxiliar** (inventado) para continuar la división.

---

### Procedimiento paso a paso

```text
BLOQUE 1: De Fracción a Decimal
1. DISPOSICIÓN: Coloca el numerador dentro de la galera y el denominador fuera.
2. DIVISIÓN INICIAL: Divide de forma convencional.
3. REGLA DEL CERO: Si al bajar una cifra el divisor no cabe, coloca "0 al cociente".
4. PUNTO DECIMAL: Cuando no queden más cifras por bajar, añade un cero auxiliar 
   al residuo y coloca la coma en el cociente.
5. CLASIFICACIÓN:
   - Residuo 0 = Decimal Exacto.
   - Residuo se repite = Decimal Periódico (usa la barra de periodo).
```

```text
BLOQUE 2: De Decimal Exacto a Fracción
1. ESTRUCTURA: Escribe el decimal sobre la unidad (ej. 1,25 / 1).
2. AMPLIFICACIÓN: Multiplica numerador y denominador por una potencia de 10 
   según la cantidad de cifras decimales:
   - 1 cifra decimal -> x10
   - 2 cifras decimales -> x100
   - 3 cifras decimales -> x1000
3. SIMPLIFICACIÓN: Reduce la fracción dividiendo ambos términos por sus 
   divisores comunes hasta que sea irreducible.
```

---

### Ejemplos Resueltos

> [!example] Ejemplo 1: El cero en el cociente
> **Problema:** Convertir $1254 / 5$
> 1. Dividimos $12$ entre $5$: Cabe a $2$, residuo $2$.
> 2. Bajamos el $5$ (formamos $25$): Cabe a $5$, residuo $0$.
> 3. **Paso Crítico:** Bajamos el $4$. Como $5$ no cabe en $4$, ponemos **0 al cociente**.
> 4. Añadimos el primer cero auxiliar al residuo ($40$) y colocamos la coma.
> 5. $40$ entre $5$ cabe a $8$.
> **Resultado:** $250,8$

> [!example] Ejemplo 2: El cero tras la coma decimal
> **Problema:** Convertir $3277 / 25$
> 1. $32$ entre $25$: Cabe a $1$, residuo $7$.
> 2. Bajamos el $7$ (formamos $77$): Cabe a $3$, residuo $2$.
> 3. Al no haber más cifras, añadimos un cero auxiliar ($20$) y ponemos la coma.
> 4. **Paso Crítico:** Preguntamos: ¿Cabe $25$ en $20$? No. Ponemos **0 al cociente**.
> 5. Añadimos otro cero auxiliar al residuo para formar $200$.
> 6. $200$ entre $25$ cabe a $8$.
> **Resultado:** $131,08$

> [!example] Ejemplo 3: Decimal Periódico
> **Problema:** Convertir $2382 / 22$
> 1. Al realizar la división, el cociente entero es $108$ con residuo $6$.
> 2. Al iniciar la parte decimal, el residuo alterna cíclicamente entre $60$ y $160$.
> 3. Esto genera que en el cociente se repita la secuencia $27$ infinitamente.
> **Resultado:** $108,\overline{27}$

> [!example] Ejemplo 4: De decimal USD a fracción
> **Problema:** Convertir un precio de $12,3$ USD a fracción.
> 1. Escribimos $12,3 / 1$.
> 2. Multiplicamos por $10$ (tiene 1 cifra decimal): $123 / 10$.
> 3. La fracción es irreducible.
> **Resultado:** $123 / 10$

---

### Ejercicios para el estudiante

- **🟢 Fácil:** Convierte el decimal exacto $1,25$ a fracción simplificada.
- **🟡 Medio:** Realiza la división $1254 / 5$. Justifica pedagógicamente por qué el resultado no puede ser $25,8$.
- **🔴 Avanzado:** Toma el valor $52,324$ de un presupuesto contable y conviértelo a su fracción irreducible mostrando todos los pasos de simplificación.

> [!success] ✅ Respuestas
> 1. $1,25 = 125/100 = 25/20 = 5/4$.
> 2. $250,8$. La justificación es que al bajar el 4, se debe cumplir la regla de poner una cifra en el cociente (0) porque el divisor no cabe.
> 3. $52,324 = 52324 / 1000 = 26162 / 500 = 13081 / 250$.

---

### Autoevaluación y Cierre

> [!question] Conceptual
> Explica con tus propias palabras qué significa la regla: "Bajo una cifra, pongo una cifra en el cociente". ¿Qué sucede si el divisor es más grande que el número formado?

> [!question] Procedimental
> En la conversión de decimal a fracción, ¿por qué es necesario multiplicar tanto el numerador como el denominador por la misma potencia de 10?

> [!question] Aplicación USD
> Si una factura muestra un cargo de $131,08$ USD y un auditor afirma que la fracción de origen es $3277/25$, ¿cómo podrías demostrar matemáticamente si el auditor está en lo cierto sin usar una calculadora?

> [!tip] 💡 En la próxima clase
> Avanzaremos hacia los decimales periódicos puros y mixtos, donde aprenderemos por qué no se usa la potencia de 10 (base 0) sino el número 9 en el denominador.

---