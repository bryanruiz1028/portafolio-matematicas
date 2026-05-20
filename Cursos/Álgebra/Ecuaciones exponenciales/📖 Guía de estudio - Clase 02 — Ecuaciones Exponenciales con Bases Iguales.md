# 📖 Guía de estudio — Clase 02: Ecuaciones Exponenciales con Bases Iguales

> [!info] 📌 Conceptos clave
> * **Propiedad fundamental:** Si logramos que $a^x = a^y$, entonces podemos afirmar con total seguridad que $x = y$. Esta igualdad entre exponentes es la base de nuestra resolución.
> * **Condición obligatoria:** Para aplicar esta propiedad, es imperativo que exista un **único término** a cada lado de la igualdad y que ambos compartan la **misma base numérica**.
> * **Objetivo final:** El proceso busca despejar y encontrar el valor exacto de la incógnita (usualmente $x$).
> * **Verificación:** Como en todo proceso algebraico profesional, debemos sustituir el resultado en la ecuación original. Si la igualdad se mantiene, el ejercicio es correcto.

---

## 2. Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Propiedad de Bases Iguales** | Si $a^m = a^n \Rightarrow m = n$ |
| **Cambio de Base** | Transformar un número en potencia: $16 \to 2^4$, $27 \to 3^3$ o $25 \to 5^2$ |
| **Potencia de una Potencia** | $(a^m)^n = a^{m \cdot n}$ |
| **Separación de Exponentes (Suma)** | $a^{x+n} = a^x \cdot a^n$ |
| **Separación de Exponentes (Resta)** | $a^{x-n} = \frac{a^x}{a^n}$ |

*Las primeras tres fórmulas son esenciales para problemas de nivel básico y medio; sin embargo, las leyes de **separación de exponentes** son las llaves maestras para resolver ejercicios avanzados donde los términos se suman o restan.*

---

## 3. Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A: Igualación Directa (Caso Básico)
**Ecuación:** $3^{x+5} = 3^{2x+3}$

**Paso 1: Identificar las bases.** Observamos que ambos lados tienen base $3$. Como son idénticas, podemos prescindir de ellas por la propiedad de inyectividad de la función exponencial.
**Paso 2: Igualar exponentes.** Extraemos los exponentes para formar una ecuación lineal:
$x + 5 = 2x + 3$
**Paso 3: Despejar la variable.**
$5 - 3 = 2x - x$
$2 = x$
**Verificación:** Sustituimos $x=2$ en la ecuación original: $3^{2+5} = 3^{2(2)+3} \Rightarrow 3^7 = 3^7$. 
**Conclusión:** Dado que la igualdad se cumple perfectamente, la solución $x=2$ queda validada.
```

```ad-example
title: Ejemplo B: Aplicación Financiera (Crecimiento de Ahorros)
**Enunciado:** Un fondo de inversión en USD crece siguiendo una base $5$. Si la estructura del crecimiento es $5^x = 25$ USD, ¿cuántos años ($x$) deben transcurrir para que el fondo alcance ese valor?

**Paso 1: Plantear la ecuación.** $5^x = 25$
**Paso 2: Cambio de base.** Debemos expresar 25 en base 5: $5^x = 5^2$
**Paso 3: Igualar.** Al tener bases iguales, igualamos los exponentes: $x = 2$
**Resultado:** Deben transcurrir $2$ años.

> [!tip] Tip del Profesor
> En el mundo de las finanzas, la **base** suele representar la tasa de crecimiento y el **exponente** representa el tiempo. ¡Dominar el álgebra es dominar tu dinero!
```

---

## 4. Ejercicios de Repaso

```ad-abstract
title: 🟢 Bloque: Nivel Fácil
1. $5^{x+2} = 5^7$
2. $2^{x-2} = 2^{10}$
3. $3^{x+1} = 3^4$
```

```ad-abstract
title: 🟡 Bloque: Nivel Medio
1. $3^{2x+3} = 3^{x+5}$
2. $2^{x+2} = 8$ *(Recuerda transformar el 8 a base 2 primero).*
3. $2^{x^2 - 6x + 12} = 16$ *(Iguala bases y resuelve la ecuación cuadrática resultante).*
```

```ad-abstract
title: 🔴 Bloque: Nivel Avanzado (Aplicación USD)
**Problema:** El valor de una cuenta de ahorros crece según la expresión: $5^{x-1} + 5^{x+1} = 130$ USD. Encuentra el valor de $x$ (tiempo en años).

**Guía de pasos:**
1. **Separación:** Usa las fórmulas de suma y resta para separar los exponentes: $\frac{5^x}{5} + 5^x \cdot 5 = 130$.
2. **Eliminar denominadores:** Multiplica toda la ecuación por 5 para simplificar el proceso.
3. **Agrupar:** Suma los términos que contienen $5^x$ (obtendrás $26 \cdot 5^x = 650$).
4. **Dividir e Igualar:** Despeja $5^x$ y transforma el resultado a base 5 para hallar $x$.
```

---

## 5. Consejo de Estudio

> [!tip] 💡 Estrategia: "Igualar para Simplificar"
> Estimado estudiante, recuerda que en matemáticas muchos números están "disfrazados". Los números como **8, 27, 64, 125 y 625** son en realidad potencias de 2, 3 y 5. Antes de resolver, siempre intenta expresar los números grandes como potencias de la base más pequeña presente en la ecuación. 
> 
> **Regla de oro:** Prohíbo el uso de calculadoras avanzadas en esta etapa. El objetivo es que tu cerebro aprenda a reconocer estas potencias y aplique la lógica de bases iguales de forma natural. ¡La práctica hace al maestro!