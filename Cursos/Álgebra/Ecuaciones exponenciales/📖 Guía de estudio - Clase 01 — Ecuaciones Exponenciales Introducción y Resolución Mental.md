# 📖 Guía de estudio — Clase 01: Introducción a las Ecuaciones Exponenciales

> [!info] 📌 Conceptos clave
> Una **ecuación exponencial** es una igualdad donde la variable o incógnita (generalmente $x$) se encuentra en el **exponente**. 
> 
> **La Regla de Oro:** Para resolverlas, el objetivo es igualar las bases. Si logramos que $a^x = a^y$, entonces por obligación $x = y$.
> 
> **El "Comodín":** El número **1** es una pieza clave. Recuerda que cualquier base elevada a la cero es igual a 1 ($a^0 = 1$). Esto significa que puedes transformar un "1" en cualquier base que necesites para igualar la ecuación.

---

### 1. Tabla de Propiedades de los Exponentes

Para resolver estas ecuaciones mentalmente o mediante álgebra, debes dominar estas reglas básicas de potenciación:

| Término | Definición / Fórmula |
| :--- | :--- |
| **Exponente Cero (El Comodín)** | Todo número (excepto 0) elevado a la cero es 1: $a^0 = 1$ |
| **Exponente Uno** | Todo número elevado a la uno es la misma base: $a^1 = a$ |
| **Bases iguales (Multiplicación)** | Se mantiene la base y se suman los exponentes: $a^x \cdot a^y = a^{x+y}$ |
| **Bases iguales (División)** | Se mantiene la base y se restan los exponentes: $a^x / a^y = a^{x-y}$ |
| **Potencia de una Potencia** | Los exponentes se multiplican si hay paréntesis: $(a^x)^y = a^{x \cdot y}$ |

---

### 2. Ejemplos Resueltos

```ad-example
title: Ejemplo A: Aplicando la Regla de Oro
**Ejercicio:** Resolver $2^x = 8$

**Proceso mental:**
1. La base de la izquierda es **2**. Debo transformar el **8** a esa misma base.
2. Pensamos en las potencias de 2: $2 \cdot 2 \cdot 2 = 8$, es decir, $2^3 = 8$.
3. Reescribimos la ecuación: $2^x = 2^3$.
4. **Aplicamos la Regla de Oro:** Como las bases ya son iguales ($2 = 2$), los exponentes deben ser idénticos.
5. **Resultado:** $x = 3$.
```

```ad-example
title: Ejemplo B: Aplicación Real (Duplicación de Dinero)
**Escenario:** Tienes una cuenta que empieza con $1 USD y el saldo se duplica cada mes. ¿En cuántos meses tendrás $32 USD?

**Ecuación:** $2^x = 32$

**Resolución:**
1. Identificamos el 32 como potencia de 2: $2^1=2, 2^2=4, 2^3=8, 2^4=16, 2^5=32$.
2. Sustituimos: $2^x = 2^5$.
3. Al tener bases iguales, igualamos los exponentes.
4. **Resultado:** $x = 5$. En 5 meses tendrás esa cantidad.
```

---

### 3. Ejercicios de Repaso por Niveles

```ad-abstract
title: Nivel Verde (Fácil) - Estimación Mental
Intenta resolver estos ejercicios sin escribir el procedimiento, buscando la potencia exacta:
1. $3^x = 81$
2. $2^x = 32$
3. $5^x = 125$
```

```ad-abstract
title: Nivel Amarillo (Medio) - Álgebra en el Exponente
Iguala las bases y luego resuelve la ecuación lineal resultante:
1. $3^{x+2} = 3^6$
2. $2^{2x-1} = 8$  *(Pista: Transforma el 8 en $2^3$ antes de igualar exponentes)*.
3. $10^{x-3} = 100$
```

```ad-abstract
title: Nivel Rojo (Avanzado) - Aplicación de Ahorros
Problemas de suma de potencias aplicados a finanzas:
1. **Ahorro acumulado:** $5^{x-2} + 5^x = 26$ USD. Encuentra $x$ buscando qué potencias de 5 sumadas dan 26. *(Pista: $1 + 25 = 26$)*.
2. **Deuda creciente:** $7^x + 7^{x-1} = 8$ USD. Prueba con valores bajos para $x$. ¿Existe más de un valor que cumpla la igualdad? *(Verifica con $x=1$)*.
3. **Inversión compuesta:** $2^{x+1} + 2^{x+2} = 48$ USD. Encuentra $x$ sabiendo que la suma debe ser $16 + 32 = 48$.
```

---

### 4. Estrategia de Estudio Final

> [!tip] 💡 Consejo de estudio
> La clave para la agilidad mental en matemáticas es reconocer patrones. Memoriza estas potencias para ahorrar tiempo en tus exámenes:
> *   **Base 2:** 2, 4, 8, 16, 32, 64, 128...
> *   **Base 3:** 3, 9, 27, 81, 243...
> *   **Base 5:** 5, 25, 125, 625...
>
> Si ves el número **27**, tu mente debe leer automáticamente **$3^3$**. Si ves un **1**, piensa en él como un **comodín** con exponente cero.