# 📖 Guía de estudio — Clase 03: Propiedades de los Logaritmos

### 1. Bloque de Introducción y Conceptos Clave

> [!info] 📌 Conceptos clave
> Para dominar el álgebra de logaritmos, es fundamental internalizar estos cinco pilares pedagógicos:
> - **Anatomía del Logaritmo:** En la expresión $\log_b a = c$, identificamos la **base** ($b$), el **argumento** ($a$) y el **exponente o logaritmo** ($c$).
> - **El Logaritmo como Búsqueda:** Resolver $\log_2 8$ es responder a la pregunta: *¿A qué exponente debo elevar la base $2$ para obtener el argumento $8$?* (Respuesta: $2^3 = 8$).
> - **Restricciones de la Base:** Para que un logaritmo exista, la base $b$ debe ser siempre un número **positivo** ($b > 0$) y **diferente de $1$** ($b \neq 1$).
> - **Condición de Unificación:** Solo podemos aplicar propiedades de unión (suma a producto o resta a cociente) si todos los logaritmos involucrados comparten la **misma base**.
> - **Regla de Ubicación (Signos):** Los logaritmos con signo **positivo** aportan su argumento al **numerador**, mientras que los logaritmos con signo **negativo** lo aportan al **denominador**.

### 2. Tabla de Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Logaritmo de un Producto** | Se transforma en la suma de los logaritmos de los factores: $\log_b(M \cdot N) = \log_b M + \log_b N$. |
| **Logaritmo de un Cociente** | Se transforma en la resta del logaritmo del dividendo menos el del divisor: $\log_b(\frac{M}{N}) = \log_b M - \log_b N$. |
| **Logaritmo de una Potencia** | El exponente baja a multiplicar al logaritmo: $\log_b(M^k) = k \cdot \log_b M$. *(¡Cuidado! Si el exponente es un binomio como $(x+1)$, usa paréntesis obligatoriamente).* |
| **Logaritmo de una Raíz** | Es una extensión de la potencia ($\sqrt[n]{M} = M^{1/n}$), donde el índice pasa como fracción: $\log_b(\sqrt[n]{M}) = \frac{1}{n} \cdot \log_b M$. |
| **Logaritmo de la Base** | Cuando la base y el argumento coinciden, el resultado siempre es $1$: $\log_b b = 1$. |
| **Logaritmo de la Unidad** | Sin importar la base, si el argumento es $1$, el resultado es $0$: $\log_b 1 = 0$. |
| **Logaritmo Decimal** | Si no visualizas la base, se sobreentiende que es **base $10$**: $\log 100 = \log_{10} 100$. |
| **Ley de Ubicación Combinada** | Regla general para unir múltiples términos: $\log_b \frac{M \cdot N}{P} = \log_b M + \log_b N - \log_b P$. |

### 3. Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A (Caso Básico: Logaritmo de un Cociente)
**Problema:** Resolver aplicando propiedades: $\log_2 \left(\frac{32}{8}\right)$

**Paso 1 (Separación):** Convertimos el cociente en una resta de logaritmos.
$\log_2 32 - \log_2 8$

**Paso 2 (Cálculo individual):**
- ¿A qué potencia elevo el $2$ para obtener $32$? ($2 \cdot 2 \cdot 2 \cdot 2 \cdot 2$) = $5$
- ¿A qué potencia elevo el $2$ para obtener $8$? ($2 \cdot 2 \cdot 2$) = $3$

**Resultado final:**
$5 - 3 = 2$

*Nota didáctica:* También podrías resolver la división primero ($\frac{32}{8} = 4$) y calcular $\log_2 4 = 2$. ¡Ambos caminos son correctos!
```

```ad-example
title: Ejemplo B (Aplicación con contexto $USD)
**Escenario:** Una inversión de $10$ USD se duplica, y queremos analizar su crecimiento mediante la propiedad del producto: $\log_2(10 \cdot 2)$.

**Paso 1 (Separación):** Aplicamos la propiedad de la suma para aislar los factores.
$\log_2 10 + \log_2 2$

**Paso 2 (Simplificación):**
Aplicamos la propiedad de la base: $\log_2 2 = 1$. 
El término $\log_2 10$ no tiene un resultado entero exacto (ya que $2^3=8$ y $2^4=16$).

**Resultado expresado (Valor Exacto):** 
$\log_2 10 + 1$
*En matemáticas avanzadas, dejamos la expresión así para mantener la precisión total.*
```

### 4. Ejercicios de Repaso

```ad-abstract
title: 🟢 Nivel Fácil: Aplicación Directa
1. Determina el logaritmo de la unidad: $\log_{10} 1$
2. Aplica la propiedad de la base para resolver: $\log_5 5$
3. Resuelve la siguiente potencia bajando el exponente: $\log_3 3^4$
```

```ad-abstract
title: 🟡 Nivel Medio: Unión y Separación
1. Une en un solo logaritmo la siguiente suma: $\log_6 12 + \log_6 3$
2. Separa y simplifica el siguiente cociente: $\log_3 (81 / 9)$
3. Aplica la propiedad de la potencia: $\log_2 25^3$. *(Nota: Déjalo como expresión simplificada ya que $25$ no es potencia de $2$).*
```

```ad-abstract
title: 🔴 Nivel Avanzado: Aplicación Práctica y $USD
1. **Crecimiento de un fondo:** El rendimiento de una cuenta de ahorros está dado por $\log_2(\sqrt{64})$. Encuentra el valor simplificado del rendimiento anual aplicando la propiedad de la raíz.
2. **Unión de flujos de caja:** Un analista financiero suma ingresos y resta egresos expresados en logaritmos de base $2$. 
Resuelve uniendo en un solo logaritmo: $\log_2 16 + \log_2 10 - \log_2 5$. 
*(Pista: Usa la Regla de Ubicación para multiplicar y dividir los montos en dólares).*
```

### 5. Estrategia de Estudio Final

> [!tip] 💡 La "Superpotencia" de la Unión
> Como bien enseña el **Profe Alex**, la verdadera magia de las propiedades ocurre cuando las aplicas a la inversa para **unir** logaritmos. 
> 
> Imagina que tienes $\log_3 45 - \log_3 5$. Por separado, ninguno de los dos tiene una solución entera (no hay un exponente entero para que $3$ dé $45$ o $5$). Sin embargo, al unirlos en un cociente:
> $$\log_3 \left(\frac{45}{5}\right) = \log_3 9 = 2$$
> **Consejo de oro:** Si un logaritmo parece imposible de resolver por sí solo, ¡busca a su pareja y únelos!