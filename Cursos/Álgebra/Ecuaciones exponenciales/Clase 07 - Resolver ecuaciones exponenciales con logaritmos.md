# Clase 07 — Resolver ecuaciones exponenciales con logaritmos

#algebra #resolverecuaciones
**Clase 07** | Curso de Álgebra: Ecuaciones Exponenciales

---

> [!info] 🧭 Navegación
> [Clase 06](Clase-06) | [Índice](Indice) | [Clase 08](Clase-08)

---

> [!info] 🌍 Relevancia y aplicaciones
> Los logaritmos son la herramienta maestra cuando las bases de una ecuación exponencial no se pueden igualar. Nos permiten "bajar" la incógnita del exponente para resolver problemas donde el crecimiento no es lineal.
> 
> - **💵 Aplicación con $USD:** Calcular con exactitud el tiempo necesario para que una inversión bajo interés compuesto alcance un objetivo financiero específico en dólares.
> - **🏗️ Aplicación práctica:** Determinar la vida media en la desintegración radiactiva o modelar el crecimiento de bacterias en un entorno biológico.
> - **📊 Situación cotidiana:** Medir la intensidad de sismos en la escala Richter o los decibelios del sonido, los cuales aumentan de forma exponencial respecto a su potencia.

---

> [!note] 📌 ¿Qué es Resolver ecuaciones exponenciales con logaritmos?
> Es el proceso de hallar el valor de una variable que se encuentra en el exponente mediante el uso de funciones logarítmicas.
> 
> **La Analogía de las Escaleras:** Imagina que la variable $x$ está atrapada en un ático muy alto (el exponente). No hay forma de alcanzarla estirando los brazos. Los logaritmos funcionan como **escaleras matemáticas**: al aplicarlos, nos permiten bajar a la $x$ al nivel del suelo (la base) para que podamos despejarla con facilidad.

> [!warning] ⚠️ Error común
> Nunca multipliques una base por un coeficiente antes de aplicar logaritmos. En una expresión como $3 \cdot 2^x$, **está prohibido** operar como $6^x$. El exponente $x$ solo afecta al $2$. Primero aplica el logaritmo y luego usa las propiedades para separar los términos.

> [!tip] 💡 Truco para recordarlo
> Si quieres recordar la función principal del logaritmo en este tema, repite: 
> *"Si la X arriba está, el logaritmo la bajará".*

---

### Procedimiento Paso a Paso (Método Profe Alex)

Para resolver con precisión, sigue este orden lógico:

```text
PASO 1 → Aplicar logaritmo (Natural "ln", Base 10 "log" o la base de una potencia) a ambos lados.
PASO 2 → Si hay coeficientes (ej. 3 · 2^x), aplicar la Propiedad del Producto [ln(a·b) = ln a + ln b].
PASO 3 → Usar la Propiedad de la Potencia [ln(a^n) = n · ln a] para "bajar" el exponente.
PASO 4 → Agrupar términos con "x" en un lado, factorizar y despejar.
PASO 5 → COMPROBACIÓN: Sustituir el valor hallado en la ecuación original usando la calculadora.
```

---

### Ejemplos Prácticos

#### Ejemplo 1: Caso con Coeficiente ($5^x = 3 \cdot 2^x$)
1. Aplicamos $\ln$: $\ln(5^x) = \ln(3 \cdot 2^x)$
2. **Propiedad del producto:** $\ln(5^x) = \ln(3) + \ln(2^x)$
3. **Bajar exponentes:** $x \ln(5) = \ln(3) + x \ln(2)$
4. Agrupar y factorizar: $x (\ln 5 - \ln 2) = \ln 3$
5. Despejar: $x = \frac{\ln 3}{\ln 5 - \ln 2}$
**Resultado:** $x \approx 1.1989$ (Verificado: $5^{1.1989} \approx 6.88$ y $3 \cdot 2^{1.1989} \approx 6.88$).

#### Ejemplo 2: Distribución en Exponentes ($3^{x+1} = 2^x$)
1. Aplicamos $\ln$: $(x+1) \ln 3 = x \ln 2$
2. **Propiedad distributiva:** $x \ln 3 + \ln 3 = x \ln 2$
3. Agrupar: $x \ln 3 - x \ln 2 = -\ln 3$
4. Despejar: $x = \frac{-\ln 3}{\ln 3 - \ln 2}$
**Resultado:** $x \approx -2.7092$

#### Ejemplo 3: Uso de Base Específica ($3^{x-1} = 2^x$)
Usando logaritmo en base 3 para simplificar un lado:
1. $\log_3(3^{x-1}) = \log_3(2^x)$
2. Por definición $\log_3(3) = 1$, entonces: $(x-1) = x \log_3(2)$
3. Agrupar: $x - x \log_3(2) = 1$
4. Factorizar: $x(1 - \log_3(2)) = 1 \implies x = \frac{1}{1 - \log_3(2)}$
**Resultado:** $x \approx 2.7095$

#### Ejemplo 4: Aplicación Financiera ($USD$)
Supongamos que una cuenta $A$ crece según $5^x$ y una cuenta $B$ según $3 \cdot 2^x$ (donde el resultado son cientos de dólares). ¿Cuándo se igualarán?
- **Ecuación:** $5^x = 3 \cdot 2^x$
- Como vimos en el Ejemplo 1, el cruce ocurre en $x \approx 1.1989$ periodos.
- **Interpretación:** En ese momento, ambas cuentas tendrán $6.88$ cientos de dólares, es decir, **$688.64$ USD**.

---

### Ejercicios para el Estudiante

> [!abstract] 🟢 Nivel Fácil (Estructura $a^x = b$)
> 1. $2^x = 7$
> 2. $5^x = 12$
> 3. $3^x = 20$
> 4. $10^x = 50$

> [!abstract] 🟡 Nivel Medio (Propiedad Distributiva y Productos)
> 1. $2^{x+1} = 3^x$
> 2. $5^{x-1} = 2^x$
> 3. $4^{2x} = 5^{x+2}$
> 4. $3^{x+2} = 2^{x-1}$

> [!abstract] 🔴 Nivel Avanzado (Aplicaciones Financieras en $USD$)
> 1. Una inversión $A$ crece como $2^{2x}$ y la $B$ como $3 \cdot 2^x$. ¿En qué valor de $x$ se igualan?
> 2. Calcule el tiempo $x$ para que un capital que sigue el modelo $1.5^x$ alcance los $10$ USD.
> 3. Resuelva el cruce de carteras: $3 \cdot 2^x = 5 \cdot 3^{x-1}$.
> 4. Una deuda crece según $100(1.10)^x$. ¿En qué tiempo $x$ la deuda llega a $200$ USD?

> [!success] ✅ Soluciones (Precisión a 4 decimales)
> **Fácil:** 1) $2.8074$, 2) $1.5440$, 3) $2.7268$, 4) $1.6990$
> **Medio:** 1) $1.7095$, 2) $1.7565$, 3) $2.2091$, 4) $-7.1277$
> **Avanzado:** 1) $1.5850$, 2) $5.6788$, 3) $1.4491$, 4) $7.2725$

---

### Autoevaluación y Cierre

> [!question] Pregunta 1
> ¿Cuál es la principal razón para elegir logaritmos en lugar del método de igualación de bases?
> *Respuesta: Cuando las bases son números primos diferentes o valores que no comparten una potencia común.*

> [!question] Pregunta 2
> Según el "Paso 5", ¿qué herramienta es indispensable para asegurar que el resultado es correcto?
> *Respuesta: La calculadora, para verificar que la igualdad numérica se cumpla en ambos miembros.*

> [!question] Pregunta 3
> Si en un problema de $USD$ obtienes $x = 3.5$, y la ecuación era $2 \cdot 10^x$, ¿cuántos dólares hay?
> *Respuesta: $2 \cdot 10^{3.5} = 2 \cdot 3162.27 = 6324.55$ USD.*

**Notas para el próximo tema:** En la Clase 08, aplicaremos estos conocimientos para resolver problemas de **Interés Compuesto Continuo** usando el número e ($e$) y logaritmos naturales, llevando las finanzas al siguiente nivel.

---

> [!info] 🧭 Navegación
> [Clase 06](Clase-06) | [Índice](Indice) | [Clase 08](Clase-08)