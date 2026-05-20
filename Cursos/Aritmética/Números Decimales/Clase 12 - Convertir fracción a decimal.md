# Clase 12 — Convert fraction to decimal
#algebra #convertfraction

Curso: [[00 - Índice del curso]] | Bloque 2 | Lección 12 de 22

> [!info] 🧭 Navegación
> ⬅️ **Anterior**: [[Clase 11 — Simplificación de fracciones]]
> ➡️ **Siguiente**: [[Clase 13 — Suma y resta de decimales]]

---

### ¿POR QUÉ ES IMPORTANTE ESTA CLASE?

> [!info] 🌍 Relevancia y aplicaciones
> Convertir fracciones a decimales es esencial para lograr precisión en mediciones técnicas y cálculos financieros. El sistema decimal facilita la comparación de magnitudes y la ejecución de operaciones complejas en una base 10 estandarizada.

*   **💵 [USD]:** Permite determinar con exactitud precios y cambios monetarios; por ejemplo, saber que $2/5$ de un dólar equivalen a $0.40$ dólares (40 centavos).
*   **🏗️ [Práctica]:** En carpintería o construcción, ayuda a traducir medidas de una cinta métrica (como $1/8$ de pulgada) a valores decimales para su uso en software de diseño o planos digitales.
*   **📊 [Cotidiana]:** Es vital para interpretar estadísticas en medios de comunicación, como entender que una tasa de aprobación de $3/4$ representa el $0.75$ de la población consultada.

---

### CONCEPTO CLAVE

> [!note] 📌 ¿Qué es Convert fraction to decimal?
> Es el proceso de dividir el numerador entre el denominador para expresar una razón o proporción como un número único que utiliza un punto decimal para separar la parte entera de la parte fraccionaria.

> [!warning] ⚠️ Error común
> Un error crítico es colocar más de un punto decimal en un mismo número o situar la barra de periodo sobre la parte entera o antes del punto decimal. La barra de recurrencia debe colocarse **exclusivamente** sobre las cifras decimales que se repiten.

> [!tip] 💡 Truco para recordarlo: La Regla del "Primer Cero"
> En una división, el primer cero "extra" que agregas al residuo para continuar operando es el que activa inmediatamente la colocación del punto decimal en el cociente. 
> 
> **Nota de experto:** Si el dividendo es menor que el divisor (ej. $2 \div 5$), la división comienza colocando un `0.` en el cociente, ya que no hay unidades enteras.

---

### PROCEDIMIENTO PASO A PASO

```text
PASO 1: Configurar la división larga situando el Numerador como dividendo 
        y el Denominador como divisor.
PASO 2: Si el dividendo es menor que el divisor, añadir el primer cero 
        extra al residuo; esta acción exige colocar el punto decimal en 
        el cociente inmediatamente (usando "0." si no hay enteros).
PASO 3: Continuar la división hasta que el residuo sea cero (decimal exacto) 
        o se identifique una secuencia numérica que se repite (periodo).
PASO 4: Registrar el resultado final. En caso de ser periódico, añadir una 
        barra horizontal (vínculum) sobre los dígitos del patrón repetitivo.
```

---

### EJEMPLOS EXPLICATIVOS

#### Ejemplo 1 (Básico): $9/4$
1. Dividimos $9$ entre $4$. El $4$ cabe **2** veces en el $9$ ($2 \times 4 = 8$), sobra **1**.
2. Al no haber más cifras, aplicamos la regla del primer cero: añadimos un **0** al $1$ (convirtiéndolo en $10$) y colocamos el **punto** en el cociente.
3. El $4$ cabe **2** veces en el $10$ ($2 \times 4 = 8$), sobra **2**.
4. Añadimos otro cero al $2$ ($20$). El $4$ cabe **5** veces en $20$ ($5 \times 4 = 20$), sobra **0**.
*   **Resultado:** $2.25$

#### Ejemplo 2 (Periódico): $110/3$
1. Realizamos la división entera: $110 \div 3 = 36$ con un residuo de **2**.
2. Añadimos un cero al residuo ($20$) y colocamos el **punto** decimal.
3. $20 \div 3$ cabe **6** veces ($6 \times 3 = 18$), sobrando nuevamente **2**.
4. Al repetirse el residuo **2**, el cociente repetirá el **6** infinitamente.
*   **Resultado:** $36.\bar{6}$

#### Ejemplo 3 (Avanzado): $13/7$
Este caso requiere un seguimiento riguroso de los residuos para identificar el cierre del periodo:
1. $13 \div 7 = 1$, residuo **6**.
2. Añadimos el primer cero (60) y ponemos el punto: $60 \div 7 = 8$, residuo **4**.
3. Continuamos: $40 \div 7 = 5$, residuo **5**; $50 \div 7 = 7$, residuo **1**; $10 \div 7 = 1$, residuo **3**; $30 \div 7 = 4$, residuo **2**; $20 \div 7 = 2$, residuo **6**.
4. **El activador:** Al obtener el residuo **6** nuevamente, confirmamos que la secuencia $857142$ se repetirá.
*   **Resultado:** $1.\overline{857142}$

#### Ejemplo 4 (USD): Contexto monetario $2/5$
1. Dividimos $2$ entre $5$. Como $5$ no cabe en $2$, iniciamos el cociente con **0.** y añadimos un cero al dividendo ($20$).
2. $20 \div 5 = 4$ exactamente, residuo $0$.
3. El resultado es $0.4$, pero en formato monetario de USD se añaden dos posiciones decimales.
*   **Resultado:** $\$0.40$

---

### EJERCICIOS PARA EL ESTUDIANTE

**🟢 Fácil (Decimales exactos):**
1. $1/2$
2. $3/4$
3. $4/5$
4. $1/8$

**🟡 Medio (Decimales periódicos):**
5. $1/3$
6. $5/6$
7. $2/9$
8. $4/11$

**🔴 Avanzado (Problemas de USD):**
9. Calcule el valor decimal de $3/8$ de un dólar.
10. Una golosina cuesta $1/5$ de dólar. Exprese este precio como un valor decimal.
11. Si un producto cuesta $7/10$ de un dólar, ¿cuál es su precio decimal?
12. Exprese $3/2$ de un dólar en formato decimal.

> [!success] ✅ Soluciones
> 1) $0.5$ | 2) $0.75$ | 3) $0.8$ | 4) $0.125$ | 5) $0.\bar{3}$ | 6) $0.8\bar{3}$ | 7) $0.\bar{2}$ | 8) $0.\overline{36}$ | 9) $0.375$ | 10) $0.20$ | 11) $0.70$ | 12) $1.50$

---

### MINI-PRUEBA DE AUTOEVALUACIÓN

1.  **¿Bajo qué condiciones se da por finalizado el proceso de división al convertir a decimal?**
    *   Cuando el residuo llega a cero o cuando se identifica un patrón repetitivo (periodo) en el cociente.
2.  **¿Cuál es el equivalente decimal de la fracción $7/2$?**
    *   a) $3.2$ | b) $3.5$ | c) $0.35$ | d) $7.2$ (Respuesta: **b**)
3.  **Si una oferta indica que el precio es $1/4$ de dólar, ¿cómo se escribe este monto en una calculadora?**
    *   $0.25$

---

### PRÓXIMO TEMA
Una vez dominada la conversión, el siguiente paso es aprender a operar con estos números en la **Clase 13: Suma y resta de decimales**, donde la alineación del punto decimal es la clave del éxito.

---
> [!info] 🧭 Navegación
> ⬅️ **Anterior**: [[Clase 11 — Simplificación de fracciones]]
> ➡️ **Siguiente**: [[Clase 13 — Suma y resta de decimales]]