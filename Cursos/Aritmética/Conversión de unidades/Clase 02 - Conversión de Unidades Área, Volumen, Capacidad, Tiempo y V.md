# Clase 02 — Conversión de Unidades: Área, Volumen, Capacidad, Tiempo y Velocidad

`#algebra #areaunitconvers`

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 2 de 6

> [!info] 🧭 Navegación
> - Anterior: [[Clase 01 - Unidades de Longitud]]
> - Índice: [[00 - Índice del curso]]
> - Siguiente: [[Clase 03 - Regla de Tres y Proporciones]]

---

> [!info] 🌍 Relevancia y aplicaciones
> Entender cómo transformar unidades no es solo un ejercicio matemático, es una habilidad para la vida. Nos permite desde comparar ofertas de terrenos hasta entender la física detrás del movimiento.
> 
> - **💵 [aplicación con $USD]:** Determinar el precio justo de un terreno comparando su costo por metro cuadrado ($m^2$) frente a hectáreas en dólares.
> - **🏗️ [aplicación práctica]:** Calcular el volumen de concreto ($m^3$) necesario para una base, asegurando que no sobre ni falte material.
> - **📊 [situación cotidiana]:** Gestionar el almacenamiento de líquidos convirtiendo de kilolitros (kL) a litros (L) para conocer la capacidad real de una cisterna.

---

> [!note] 📌 ¿Qué es la Conversión de Unidades?
> Convertir es expresar una misma cantidad en una unidad diferente. Para movernos entre unidades, usamos la "escalerita". El secreto pedagógico está en el **exponente** de la unidad:
> 
> 1. **Capacidad (Lineal):** Cada escalón vale **10**.
> 2. **Área (Superficie):** Como tiene dos dimensiones (largo $\times$ ancho), cada escalón vale $10 \times 10 = \mathbf{100}$ (base $10^2$).
> 3. **Volumen:** Como tiene tres dimensiones (largo $\times$ ancho $\times$ alto), cada escalón vale $10 \times 10 \times 10 = \mathbf{1000}$ (base $10^3$).
> 
> ### La Escalera de Prefijos
> | Prefijo | Símbolo | Valor (respecto a la unidad) |
> | :--- | :---: | :--- |
> | **Kilo** | k | 1000 (Grande) |
> | **Hecto** | h | 100 |
> | **Deca** | da / D | 10 |
> | **Unidad** | L / m / s | 1 |
> | **Deci** | d | 0.1 |
> | **Centi** | c | 0.01 |
> | **Mili** | m | 0.001 (Pequeño) |

> [!important] 💡 La Regla de la Coma Invisible
> Un error frecuente es no saber dónde empezar a contar si el número no tiene decimales. **Todo número entero tiene una "coma invisible" al final**.
> *Ejemplo:* El número $580$ es en realidad $580,0$. Al dividir o multiplicar, partimos desde ahí.

> [!warning] ⚠️ Error común
> ❌ **Incorrecto:** Pensar que $1\ m^2$ son $10\ cm^2$.
> ✅ **Correcto:** En áreas, bajar un escalón significa multiplicar por 100. De metros a decímetros ya hay 100, y a centímetros hay 10,000. ¡El exponente manda!

---

### Procedimiento Paso a Paso

> [!important] ⚙️ Método Maestro
> **PASO 1 →** Identifica el punto de partida y la meta en la escalera.
> **PASO 2 →** Define la dirección y la operación:
> *   **Bajar (Derecha):** Multiplicar ($\times$).
> *   **Subir (Izquierda):** Dividir ($\div$).
> 
> **PASO 3 →** Cuenta los ceros según el exponente:
> *   **Lineal:** 1 cero por escalón.
> *   **Área ($^2$):** 2 ceros por escalón.
> *   **Volumen ($^3$):** 3 ceros por escalón.
> 
> **PASO 4 →** Desplaza la coma decimal. Si se acaban las cifras, rellena con ceros.

---

### Bloques de Ejemplos

> [!example] Ejemplo 1: Área (Básico)
> **Convertir $5\ hm^2$ a $m^2$.**
> 1. De $hm^2$ a $m^2$ bajamos **2 escalones** ($hm^2 \to dam^2 \to m^2$).
> 2. Como es área ($^2$), son 2 ceros por escalón: $2 \times 2 = 4$ ceros en total (multiplicar por $10,000$).
> 3. Operación: $5 \times 10,000 = 50,000$.
> **Resultado:** $50,000\ m^2$.

> [!example] Ejemplo 2: Volumen con decimales
> **Convertir $12,5\ km^3$ a $hm^3$.**
> 1. Bajamos **1 escalón** de $km^3$ a $hm^3$.
> 2. Al ser volumen ($^3$), multiplicamos por $1,000$ (3 ceros).
> 3. Desplazamos la coma 3 lugares a la derecha:
>    * $12,5 \xrightarrow{1} 125 \xrightarrow{2} 1250 \xrightarrow{3} 12500$.
> **Resultado:** $12,500\ hm^3$.

> [!example] Ejemplo 3: Velocidad (Factor de Conversión)
> **Convertir $72\ km/h$ a $m/s$.**
> Utilizamos fracciones para "cancelar" las unidades que no queremos:
> $$\frac{72\ \cancel{km}}{\cancel{h}} \times \frac{1000\ m}{1\ \cancel{km}} \times \frac{1\ \cancel{h}}{3600\ s} = \frac{72 \times 1000}{3600}\ m/s$$
> Operación: $72,000 \div 3,600 = 20$.
> **Resultado:** $20\ m/s$.

> [!example] Ejemplo 4: Aplicación Real con $USD
> **Un terreno de $0,12\ km^2$ cuesta $\$50\ USD$ por cada decámetro cuadrado ($dam^2$). ¿Cuál es el costo total?**
> 1. Convertimos $km^2$ a $dam^2$: Bajamos 2 escalones de área ($2 \times 2 = 4$ ceros).
> 2. Operación: $0,12 \times 10,000 = 1,200\ dam^2$.
> 3. Cálculo de costo: $1,200\ dam^2 \times 50\ USD = 60,000\ USD$.
> **Resultado:** El terreno cuesta $\$60,000\ USD$.

---

### Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Fácil: Capacidad y Tiempo
> 1. Convierte $5\ L$ a mililitros ($mL$).
> 2. Convierte $2\ h$ a minutos.
> 3. Convierte $5,000\ mL$ a litros ($L$).
> 4. Convierte $180\ min$ a horas.

> [!abstract] 🟡 Nivel Medio: Área y Volumen (Decimales)
> 1. Convierte $4,5\ m^2$ a $cm^2$.
> 2. Convierte $850\ mm^3$ a $cm^3$.
> 3. Convierte $0,12\ cm^2$ a $mm^2$.
> 4. Convierte $1,500\ cm^3$ a $dm^3$.

> [!abstract] 🔴 Nivel Avanzado: Problemas de Aplicación
> 1. Convierte $12\ m/s$ a $km/h$. (Usa factores de conversión).
> 2. Calcula cuántos segundos hay en exactamente $2$ semanas.
> 3. Un tanque tiene una capacidad de $5\ kL$. Si cada litro cuesta $\$0,50\ USD$, ¿cuánto cuesta llenarlo?
> 4. Un plano muestra un sector de $0,005\ km^2$. Exprésalo en $m^2$.

---

### Respuestas para el Docente

> [!success] Solucionario Detallado
> **Nivel Fácil:**
> 1. $5,000\ mL$ ($\times 1,000$).
> 2. $120\ min$ ($\times 60$).
> 3. $5\ L$ ($\div 1,000$).
> 4. $3\ h$ ($\div 60$).
> 
> **Nivel Medio:**
> 1. $45,000\ cm^2$ (2 escalones de área $\to \times 10,000$).
> 2. $0,85\ cm^3$ (1 escalón de volumen $\to \div 1,000$).
> 3. $12\ mm^2$ (1 escalón de área $\to \times 100$).
> 4. $1,5\ dm^3$ (1 escalón de volumen $\to \div 1,000$).
> 
> **Nivel Avanzado:**
> 1. $43,2\ km/h$ ($\frac{12 \times 3600}{1000}$).
> 2. $1,209,600\ s$ ($2 \times 7 \times 24 \times 3600$).
> 3. $\$2,500\ USD$ ($5,000\ L \times 0,50$).
> 4. $5,000\ m^2$ ($0,005 \times 1,000,000$).

---

### Mini-Prueba de Autoevaluación

> [!question] Pon a prueba lo aprendido
> 1. **Conceptual:** Si subes 3 escalones en la escalera de **Volumen**, ¿cuántos lugares debes mover la coma y hacia qué lado?
> 2. **Procedimental:** Utilizando el factor de conversión, transforma $36\ km/h$ a $m/s$.
> 3. **Aplicación $USD:** Un servicio de nube cobra $\$10\ USD$ por hora de procesamiento. Si un proceso tarda $1,800$ segundos, ¿cuál es el costo?

---

> [!tip] 💡 En la próxima clase
> Ya sabemos transformar unidades. En la **Clase 03**, aplicaremos este conocimiento para resolver problemas de **Regla de Tres y Proporciones**, donde las relaciones entre datos no siempre son potencias de 10.

> [!info] 🧭 Navegación
> - Anterior: [[Clase 01 - Unidades de Longitud]]
> - Índice: [[00 - Índice del curso]]
> - Siguiente: [[Clase 03 - Regla de Tres y Proporciones]]