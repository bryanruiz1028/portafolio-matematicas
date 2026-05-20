# 📖 Guía de estudio — Clase 06: Resolución de ecuaciones exponenciales con logaritmos

> [!info] 📌 Conceptos clave
> - **Uso de logaritmos:** Se aplican cuando es imposible igualar las bases de la ecuación de forma exacta (por ejemplo, convertir un $7$ en potencia de $2$).
> - **Propiedad de la potencia:** Es la herramienta que permite "bajar" el exponente para que multiplique al logaritmo: $\log(x^n) = n \cdot \log(x)$.
> - **Flexibilidad de base:** Puedes usar logaritmo natural ($\ln$) o logaritmo base 10 ($\log$); el resultado final será idéntico.
> - **Estrategia de identidad:** La propiedad $\log_a(a) = 1$ es fundamental en "Método 2" para simplificar resultados en exámenes donde no se permite el uso de calculadora.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Propiedad de la Potencia** | El exponente de la base pasa a multiplicar al logaritmo completo: $\log_a(x^n) = n \cdot \log_a(x)$. |
| **Propiedad de Identidad** | Si la base y el argumento coinciden, el valor es 1: $\log_a(a) = 1$. Útil para simplificar términos manuales. |
| **Cambio de Base** | Permite calcular logaritmos de cualquier base en la calculadora: $\log_b(a) = \frac{\log(a)}{\log(b)}$ o $\frac{\ln(a)}{\ln(b)}$. |
| **Raíz como Potencia** | Una raíz se convierte en exponente fraccionario: $\sqrt[n]{x^m} = x^{m/n}$. Si no hay índice visible, es una raíz cuadrada ($n=2$). |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Caso básico con bases diferentes
**Problema:** Resolver $2^x = 7$.

1. **Paso 1:** Aplicamos logaritmo natural ($\ln$) a ambos lados: $\ln(2^x) = \ln(7)$.
2. **Paso 2:** Aplicamos la propiedad para bajar la $x$: $x \cdot \ln(2) = \ln(7)$.
3. **Paso 3:** Despejamos la $x$ dividiendo por el término completo $\ln(2)$: $x = \frac{\ln(7)}{\ln(2)}$.
✅ **Resultado:** $x \approx 2,81$ (al verificar $2^{2,81} \approx 7$).
```

```ad-example
title: Ejemplo B — Aplicación con contexto de inversión ($USD)
**Contexto:** "Si una cuenta de ahorros crece según $3^{x+2}$ y queremos saber cuándo llegará a $10$ USD", resolvemos $3^{x+2} = 10$.

1. **Paso 1:** Aplicamos $\ln$ en ambos lados: $\ln(3^{x+2}) = \ln(10)$.
2. **Paso 2:** Bajamos el exponente $(x+2)$ usando paréntesis para "proteger el binomio": $(x+2) \cdot \ln(3) = \ln(10)$.
3. **Paso 3:** Despejamos la $x$. Pasamos el término completo $\ln(3)$ a dividir y luego restamos 2: $x = \frac{\ln(10)}{\ln(3)} - 2$.
✅ **Resultado:** $x \approx 0,0959$ (usamos 4 decimales para asegurar una verificación exacta en la calculadora).
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
Resuelve aplicando logaritmos y redondea a dos decimales:
1. $5^x = 12$
2. $2^x = 15$
3. $3^x = 20$
```

```ad-abstract
title: 🟡 Medio
Resuelve aplicando propiedades de binomios y raíces:
1. $4^{x-1} = 9$
2. $6^{x+3} = 25$
3. $\sqrt{5^x} = 8$  
*(Nota: Recuerda que la raíz cuadrada tiene índice $2$, por lo que $\sqrt{5^x} = 5^{x/2}$).*
```

```ad-abstract
title: 🔴 Avanzado — Reto de balance financiero ($USD)
**Problema:** "Determina el tiempo $x$ para que la inversión $\sqrt{3^{x+2}}$ sea igual a $5^{x/2}$ dólares".

**Guía de resolución:**
1. Iguala las expresiones y convierte las raíces: $3^{(x+2)/2} = 5^{x/2}$.
2. Aplica logaritmos y usa la propiedad de potencia para bajar los exponentes.
3. **Puente algebraico:** Usa la propiedad distributiva para liberar la $x$ de los paréntesis y agrupa todos los términos con $x$ en un solo lado de la igualdad.
4. Factoriza la $x$ como factor común: $x(\ln(a) - \ln(c)) = \dots$ para despejarla.

🎯 **Meta:** Deberías llegar a una expresión similar a $x = \frac{2\ln(3)}{\ln(5) - \ln(3)}$ o su equivalente decimal $x \approx 4,30$.
```

> [!tip] 💡 Consejo de estudio del "Profe Alex"
> **1. Paréntesis en la calculadora:** Al usar las teclas `log` o `ln`, la mayoría de las calculadoras abren un paréntesis automáticamente. **Es vital cerrarlo** antes de presionar la tecla de división. Ejemplo: `ln(7) / ln(2)`.  
> **2. Verificación:** No des el ejercicio por terminado sin comprobar. Sustituye tu valor de $x$ en la ecuación original. Si ambos lados dan valores extremadamente cercanos (ej. $9,999 \approx 10$), ¡tu procedimiento es impecable!