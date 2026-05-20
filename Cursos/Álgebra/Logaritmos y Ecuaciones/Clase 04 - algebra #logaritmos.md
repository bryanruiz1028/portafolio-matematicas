[[Clase 03]] | [[Índice]]

#algebra #logaritmos

# Clase 04 — Logaritmos: Solución de ecuaciones y uso de calculadora

## 1. ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> Los logaritmos son la herramienta matemática que nos permite "bajar" a los exponentes de su pedestal. Son fundamentales para entender procesos que crecen o decrecen de forma explosiva.
> 
> *   **Aplicación $USD:** Permiten calcular con exactitud cuánto tiempo debe pasar para que una inversión de `$100$` USD se convierta en `$200$` USD con una tasa de interés del `$7\%$` anual.
> *   **Aplicación Construcción/Ciencia:** Se utilizan para medir la magnitud de terremotos en la escala de Richter y para calcular la intensidad del sonido en decibelios.
> *   **Situación cotidiana:** Ayudan a entender la velocidad de propagación de un video viral en redes sociales o el crecimiento de una comunidad digital.

---

## 2. Concepto clave

> [!note] 📌 ¿Qué es Logaritmos?
> Imagina que eres un **detective de exponentes**. El logaritmo es la pregunta: **"¿A qué exponente debo elevar la base para obtener el argumento?"**. 
> Por ejemplo, en $\log_{10}(1000)$, la pregunta es: "¿Cuántas veces multiplico el $10$ por sí mismo para llegar a $1000$?". Como $10 \times 10 \times 10 = 1000$, la respuesta es $3$.

> [!warning] ⚠️ Error común y uso de la calculadora
> Al usar modelos como la **Casio Fx 82, 95 o 570 MS**, es vital distinguir entre la tecla de resta ` - ` y la tecla de valor negativo ` (-) `. Si quieres calcular el logaritmo de un número negativo, como $\ln(-5)$, la calculadora arrojará un **"Math ERROR"**. Esto no es un fallo del dispositivo; es que los logaritmos de números negativos **no existen** en el conjunto de los números reales.

> [!tip] 💡 Truco para el Cambio de Base
> En las calculadoras de la serie **MS**, no existe un botón para ingresar una base distinta a $10$. Debes usar la fórmula de división. Para no olvidar el orden, usa esta regla mnemotécnica:
> *   El **Argumento** está escrito "más arriba", por lo tanto, su logaritmo va **arriba** (numerador).
> *   La **Base** está escrita como subíndice ("más abajo"), por lo tanto, su logaritmo va **abajo** (denominador).
> $$\log_{\text{base}}(\text{argumento}) = \frac{\log(\text{argumento})}{\log(\text{base})}$$

---

## 3. Procedimiento paso a paso

Para resolver ecuaciones logarítmicas de forma profesional, sigue este protocolo de 4 pasos extraído de las lecciones del Profe Alex:

```text
1. AGRUPAR: Traslada todos los términos con logaritmo a un lado de la igualdad (usualmente el izquierdo) y las constantes al otro.
2. APLICAR PROPIEDADES: Reduce los logaritmos a una sola expresión (Resta → División | Suma → Multiplicación).
3. CONVERTIR: Transforma la expresión logarítmica resultante a su forma de potencia usando la definición: b^L = A.
4. RESOLVER: Despeja la variable 'x' de la ecuación lineal o algebraica resultante.
```

---

## 4. Ejemplos Prácticos

```ad-example
title: Ejemplo 1: Cálculo directo (Base 10)
**Problema:** Hallar el valor de $\log_{10}(1000)$.
**Técnica para Fx 82/95/570 MS:**
1. Presiona la tecla `log` (que por defecto es base $10$).
2. Digita el número $1000$.
3. Presiona `=`.
**Resultado:** $3$. Esto confirma que $10^3 = 1000$.
```

```ad-example
title: Ejemplo 2: Cambio de base obligatorio
**Problema:** Resolver $\log_4 16$.
**Explicación:** Dado que la **Fx 570 MS** no tiene un botón para base personalizada, aplicamos la fórmula de división:
1. En la calculadora, escribe: `log(16) / log(4)`.
2. Presiona `=`.
**Resultado:** $2$. (Verificación: $4^2 = 16$).
```

```ad-example
title: Ejemplo 3: Ecuación logarítmica (Paso a paso)
**Problema:** Resolver $1 = \log_6(2x+4) - \log_6(x)$.
**Desarrollo:**
1. **Propiedad de la resta:** Combinamos los logaritmos en una división: $1 = \log_6\left(\frac{2x+4}{x}\right)$.
2. **Convertir a potencia:** La base $6$ elevada al resultado $1$ es igual al argumento: $6^1 = \frac{2x+4}{x}$.
3. **Despejar:** Pasamos la $x$ multiplicando: $6x = 2x + 4$.
4. **Resolver:** $6x - 2x = 4 \implies 4x = 4 \implies x = \frac{4}{4}$.
**Resultado:** $x = 1$.
```

```ad-example
title: Ejemplo 4: Aplicación financiera ($USD)
**Problema:** Tienes `$100$` USD en una cuenta que paga el `$7\%$` anual (factor de crecimiento $1.07$). ¿En cuántos años tendrás `$200$` USD?
**Cálculo con logaritmos:**
La fórmula simplificada es $t = \frac{\log(\text{Final} / \text{Inicial})}{\log(\text{Crecimiento})}$.
1. En la calculadora: `log(200 / 100) / log(1.07)`.
2. El resultado aproximado es $10.24$.
**Resultado:** Tardarás aproximadamente $10.24$ años en duplicar tu dinero.
```

---

## 5. Ejercicios para el estudiante

```ad-abstract
title: 🟢 Nivel: Fácil (Cálculo directo y ln)
Usa tu calculadora para hallar los siguientes valores:
1. $\log(10)$
2. $\log(100)$
3. $\ln(20)$ (Usa la tecla `ln`)
4. $\log(0.001)$
```

```ad-abstract
title: 🟡 Nivel: Medio (Cambio de base)
Aplica la fórmula $\frac{\log(A)}{\log(B)}$ para resolver:
1. $\log_3 27$
2. $\log_5 625$
3. $\log_2 32$
4. $\log_7 49$
```

```ad-abstract
title: 🔴 Nivel: Avanzado (Ecuaciones)
Resuelve para $x$ aplicando las propiedades y conversión a potencia:
1. $3 = \log_2(17x-15) - \log_2(2x)$
2. $2 = \log_3(x+5) - \log_3(x)$
3. $1 = \log_5(10x) - \log_5(2)$
4. $0 = \log_4(x) - \log_4(5)$
```

```ad-success
title: ✅ Respuestas
**Nivel Fácil:** 1) $1$ | 2) $2$ | 3) $2.99$ | 4) $-3$
**Nivel Medio:** 1) $3$ | 2) $4$ | 3) $5$ | 4) $2$
**Nivel Avanzado:** 1) $x = 15$ | 2) $x = 0.625$ | 3) $x = 1$ | 4) $x = 5$
```

---

## 6. Mini-prueba de autoevaluación

```ad-question
title: Pregunta 1
¿Qué sucede internamente en la calculadora cuando presionas la tecla `log` sin especificar base?
a) Calcula en base $e$.
b) Calcula en base $2$.
c) Calcula automáticamente en base $10$.
d) Da error si no pones la base.
**Respuesta:** **c)**. Es el logaritmo decimal estándar.
```

```ad-question
title: Pregunta 2
Si tienes la expresión $\log_b(A) - \log_b(C)$, ¿cuál es la propiedad correcta para simplificarla?
a) $\log_b(A \times C)$
b) $\log_b(A / C)$
c) $\log_b(A^C)$
d) No se puede simplificar.
**Respuesta:** **b)**. La resta de logaritmos de igual base se convierte en el logaritmo de la división de sus argumentos.
```

```ad-question
title: Pregunta 3
¿Por qué la calculadora muestra "Math ERROR" al calcular $\log(-10)$?
a) Porque el número es muy pequeño.
b) Porque olvidaste usar la tecla `(-)`.
c) Porque los logaritmos solo están definidos para números reales positivos.
d) Porque la base es negativa.
**Respuesta:** **c)**. Matemáticamente, no existe un exponente real que al elevar una base positiva dé como resultado un número negativo.
```

---

## 7. Cierre y Próximo Tema

> [!tip] 💡 En la próxima clase
> Ya dominas la calculadora y la mecánica de las ecuaciones. En la siguiente sesión, exploraremos las **Funciones Exponenciales**. Veremos cómo los logaritmos son la herramienta secreta para despejar incógnitas que viven "en el techo" de las ecuaciones.

[[Clase 03]] | [[Índice]]