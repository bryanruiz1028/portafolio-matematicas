# 📖 Guía de estudio — Clase 01: Introducción a los Logaritmos y Ecuaciones

> [!info] 📌 Conceptos clave
> 
> 1. **Definición de Logaritmo:** Es la operación matemática que nos permite encontrar el **exponente** al que se debe elevar una base determinada para obtener un argumento específico.
> 2. **Relación Fundamental:** Todo logaritmo es, en esencia, la operación inversa de una potencia. La pregunta mental clave es: "¿A qué exponente elevo la base para que el resultado sea el argumento?".
> 3. **Logaritmo Decimal:** Cuando observamos la expresión $\log x$ sin una base visible, se sobreentiende por convención que la base es **10**.
> 4. **Propiedades Elementales:** Un logaritmo cuyo argumento es 1 siempre será igual a 0. Asimismo, si la base y el argumento son idénticos, el resultado siempre será 1.

## 2. Fórmulas y Definiciones Importantes

Estimado estudiante, utiliza esta tabla como referencia rápida para identificar los componentes de un logaritmo y sus reglas fundamentales:

| Término | Definición / Fórmula |
| :--- | :--- |
| **Logaritmo (Definición)** | $\log_b a = x \iff b^x = a$ |
| **Logaritmo Decimal** | $\log_{10} x = \log x$ |
| **Propiedad de la Unidad** | $\log_b b = 1$ |
| **Propiedad del Cero** | $\log_b 1 = 0$ |
| **Logaritmo de una Suma** | $\log_b A + \log_b B = \log_b (A \cdot B)$ |
| **Logaritmo de una Resta** | $\log_b A - \log_b B = \log_b \left( \frac{A}{B} \right)$ |

## 3. Ejemplos Resueltos Adicionales

````ad-example Ejemplo A — Cálculo de Logaritmo Simple
**Problema:** Calcular $\log_2 8$

**Pensemos juntos:** Para resolver este logaritmo, debemos identificar cuántas veces necesitamos elevar la base (2) para obtener el argumento (8). 

**Paso a paso:**
1. Planteamos la ecuación de potencia: $2^x = 8$.
2. Realizamos la secuencia de potencias mentalmente:
   - $2^1 = 2$
   - $2^2 = 4$
   - $2^3 = 8$
3. Como el exponente necesario es 3, el resultado del logaritmo es 3.

**Resultado:** $\log_2 8 = 3$
````

````ad-example Ejemplo B — Crecimiento Exponencial de Inversión
**Problema:** Imagina que realizas una inversión inicial de $\$2$ USD que se duplica cada año. ¿En cuántos años alcanzará un valor de $\$30$ USD?

**Para resolver esto, sigamos estos pasos:**
1. **Planteamiento:** La situación se representa con la ecuación $2^x = 30$, donde $x$ es el tiempo en años.
2. **Aplicación de logaritmos:** Para "bajar" la incógnita del exponente, aplicamos logaritmos decimales en ambos lados: $\log(2^x) = \log(30)$.
3. **Propiedad de la potencia:** Usamos la propiedad que permite pasar el exponente a multiplicar: $x \cdot \log(2) = \log(30)$.
4. **Despeje y cálculo:** Despejamos $x$ dividiendo los logaritmos: $x = \frac{\log(30)}{\log(2)}$. 
5. **Uso de calculadora:** Según los valores decimales del Profe Alex, obtenemos $x \approx \frac{1.477}{0.301}$.

**Resultado:** La inversión alcanzará los $\$30$ USD en aproximadamente **4.91 años**.
````

## 4. Ejercicios de Repaso

````ad-abstract 🟢 Fácil
Pon a prueba tu razonamiento mental calculando el resultado directo de:
1. $\log_5 25$
2. $\log_3 81$
3. $\log_{10} 10,000$
````

````ad-abstract 🟡 Medio
Resuelve las siguientes ecuaciones logarítmicas aplicando la definición de potencia o la igualdad de argumentos:
1. $\log_3 (2x - 5) = 2$
2. $\log_5 (2x - 23) = \log_5 (x - 5)$
3. $\log_2 (6x + 70) = 6$
````

````ad-abstract 🔴 Avanzado — Aplicación con $USD
**Escenario de ahorro:** Tienes una cuenta que inicia con $\$5$ USD y crece de forma exponencial siguiendo la expresión $5^{2x}$. ¿Cuánto tiempo $x$ debe pasar para que el saldo llegue a exactamente $\$13$ USD?

**Instrucción:** Resuelve la ecuación $5^{2x} = 13$ utilizando logaritmos decimales. Para tu cálculo, utiliza los siguientes valores aproximados del contexto:
- $\log 5 \approx 0.70$
- $\log 13 \approx 1.11$

*(Pista: El resultado final debería aproximarse a $x \approx 0.79$ años).*
````

## 5. Consejo de Estudio

> [!tip] 💡 Consejo de estudio
> Para dominar este tema con total seguridad, te recomiendo aplicar la técnica de **"Verificación por Potencia"** sugerida por el **Profe Alex**. Cada vez que obtengas un resultado, comprueba que la base elevada a tu respuesta realmente produzca el argumento. Por ejemplo, si calculas que $\log_3 9 = 2$, verifica que $3^2$ sea efectivamente $9$. ¡Si la potencia coincide, tu logaritmo es impecable!