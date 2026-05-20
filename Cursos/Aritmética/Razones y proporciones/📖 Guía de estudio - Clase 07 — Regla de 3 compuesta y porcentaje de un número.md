# 📖 Guía de estudio — Clase 07: Regla de Tres Compuesta

> [!info] 📌 Conceptos clave
> La **Regla de Tres Compuesta** permite resolver problemas de proporcionalidad donde intervienen tres o más magnitudes.
> 
> - **Identificación de magnitudes:** Las variables suelen encontrarse inmediatamente después de las cifras numéricas (ej: 5 **camiones**, 6 **viajes**, 1200 **$m^3$ de tierra**).
> - **La variable de referencia ($x$):** Es la magnitud que contiene la incógnita. En el análisis, esta variable es el "estándar" contra el cual comparamos todas las demás para determinar su relación.
> - **Relación Directa:** Si al aumentar una magnitud, la de referencia también aumenta (o ambas disminuyen).
> - **Relación Inversa:** Si al aumentar una magnitud, la de referencia disminuye (o viceversa).
> - **Simplificación Estratégica:** Antes de realizar operaciones complejas, es vital eliminar ceros y buscar múltiplos comunes para reducir las fracciones a su mínima expresión.
> - **La clave del "De":** En problemas de porcentajes, la palabra "de" se traduce matemáticamente como una operación de **multiplicación** ($\cdot$).

---

# 📊 Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Relación Directa** | La fracción de los datos se mantiene igual en el planteamiento (ej: $3500/1200$). |
| **Relación Inversa** | La fracción de los datos debe invertirse en el planteamiento (ej: de $7/5$ a $5/7$). |
| **Porcentaje como Fracción** | El símbolo $\%$ representa una fracción con denominador $100$ (ej: $120\% = \frac{120}{100}$). |
| **Conversión Decimal** | Para pasar de decimal a porcentaje se corre la coma dos lugares a la derecha (ej: $1.20 = 120\%$). |
| **Cálculo de Porcentaje** | Multiplicación de la fracción por el total: $\frac{\text{porcentaje}}{100} \cdot \text{valor total}$. |

---

# 📝 Ejemplos resueltos

> [!example] Ejemplo A — Transporte de tierra (Regla de 3 Compuesta)
> **Enunciado:** $5$ camiones haciendo $6$ viajes diarios transportan $1200$ $m^3$ de tierra en $4$ días. ¿Cuántos días tardarán $7$ camiones para mover $3500$ $m^3$ de tierra si hacen $10$ viajes diarios?
> 
> **Paso 1: Organización de variables**
> | Camiones | Viajes | Tierra ($m^3$) | Días |
> | :---: | :---: | :---: | :---: |
> | $5$ | $6$ | $1200$ | $4$ |
> | $7$ | $10$ | $3500$ | $x$ |
> 
> **Paso 2: Análisis de comparación (respecto a la magnitud Días)**
> - **Camiones vs. Días:** Si tengo **más** camiones, ¿necesito más o menos días? Menos días $\rightarrow$ **Inversa**.
> - **Viajes vs. Días:** Si hacen **más** viajes diarios, ¿necesito más o menos días? Menos días $\rightarrow$ **Inversa**.
> - **Tierra vs. Días:** Si hay **más** tierra que transportar, ¿necesito más o menos días? Más días $\rightarrow$ **Directa**.
> 
> **Paso 3: Planteamiento de la ecuación**
> Siguiendo el orden didáctico, planteamos la proporción de la incógnita igualada al producto de las demás:
> $$\frac{x}{4} = \frac{5}{7} \cdot \frac{6}{10} \cdot \frac{3500}{1200}$$
> Despejamos $x$ pasando el $4$ a multiplicar:
> $$x = \frac{5}{7} \cdot \frac{6}{10} \cdot \frac{3500}{1200} \cdot 4$$
> 
> **Paso 4: El "baile de la simplificación"**
> 1. Eliminamos ceros en la tierra: $\frac{3500}{1200} \rightarrow \frac{35}{12}$.
> 2. Séptima de $7$ ($1$) y séptima de $35$ ($5$): $x = 5 \cdot \frac{6}{10} \cdot \frac{5}{12} \cdot 4$.
> 3. Quinta de $5$ ($1$) y quinta de $10$ ($2$): $x = 1 \cdot \frac{6}{2} \cdot \frac{5}{12} \cdot 4$.
> 4. Sexta de $6$ ($1$) y sexta de $12$ ($2$): $x = 1 \cdot \frac{1}{2} \cdot \frac{5}{2} \cdot 4$.
> 5. El $4$ del numerador se cancela con los dos $2$ del denominador ($2 \cdot 2 = 4$).
> 
> ✅ **Resultado:** $x = 5$ días.

> [!example] Ejemplo B — Cálculo de Porcentaje superior al 100%
> **Enunciado:** Encontrar el $120\%$ de $420$.
> 
> **Paso 1: Convertir a fracción**
> $$120\% = \frac{120}{100}$$
> 
> **Paso 2: Plantear la multiplicación (Regla del "de")**
> $$\frac{120}{100} \cdot 420$$
> 
> **Paso 3: Simplificación de ceros finales**
> Eliminamos un cero del $120$ con uno del $100$, y el cero del $420$ con el otro cero del $100$.
> $$12 \cdot 42$$
> 
> ✅ **Resultado:** $504$.

---

# ✍️ Ejercicios de repaso

> [!abstract] 🟢 Nivel Fácil
> Calcula el $20\%$ de $180$ utilizando el método de conversión a fracción y simplificación de ceros.
> *(Resultado esperado: $36$)*

> [!abstract] 🟡 Nivel Medio
> Calcula el $5\%$ de $130$.
> **Instrucción:** Muestra la simplificación de la fracción $\frac{5}{10}$ a $\frac{1}{2}$, planteando la operación final como $\frac{13}{2}$.
> *(Resultado esperado: $6.5$)*

> [!abstract] 🔴 Nivel Avanzado (Reto de Lógica)
> Utilizando los datos base ($5$ camiones, $6$ viajes, $1200$ $m^3$, $4$ días): ¿Cuántos camiones se necesitan para transportar $2500$ $m^3$ de tierra en solo $2$ días si los camiones realizan $5$ viajes diarios?
> 
> > [!important] Nota del Especialista
> > ¡Atención! En este reto, la incógnita ($x$) se ha movido a la columna de **Camiones**. Debes re-evaluar todas las relaciones (Camiones vs. Viajes, Camiones vs. Tierra, Camiones vs. Días) antes de plantear la ecuación.
> 
> *(Resultado esperado: $25$ camiones)*

---

> [!tip] 💡 Consejo de estudio
> Aplica la **simplificación extrema** para evitar errores manuales. No solo elimines ceros; busca combinaciones de productos. Como vimos en el reto avanzado, si tienes un $3$ y un $4$ en el numerador ($3 \cdot 4 = 12$) y un $12$ en el denominador, puedes cancelarlos directamente ($12/12 = 1$). Mantener los números pequeños es la mejor defensa contra los errores de cálculo.