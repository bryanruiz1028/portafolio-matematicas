# 📖 Guía de estudio — Clase 08: Ecuaciones Exponenciales con el Número de Euler

> [!info] 📌 Conceptos clave
> *   **El número de Euler ($e$):** Es una constante matemática irracional, lo que significa que tiene infinitas cifras decimales sin repetirse (como $\pi$). Su valor aproximado es **2,7182**.
> *   **El origen del Logaritmo Natural ($\ln$):** Un dato fascinante es que los logaritmos fueron creados específicamente para ser utilizados con el número de Euler. El logaritmo natural ($\ln$) no es otra cosa que un logaritmo con base $e$ ($\log_e$).
> *   **La propiedad de identidad:** ¿Por qué $\ln(e) = 1$? Porque en cualquier logaritmo, cuando la base y el argumento son iguales, el resultado es 1. Es decir, $\log_e(e) = 1$.
> *   **Igualdad de exponentes:** Si logramos que ambos lados de la ecuación tengan la misma base $e$, podemos igualar directamente sus exponentes para resolver la incógnita de forma sencilla.

## Fórmulas y definiciones importantes

| Concepto | Definición / Propiedad | Lógica Pedagógica |
| :--- | :--- | :--- |
| **Número de Euler ($e$)** | Constante irracional $\approx 2,7182...$ | Se trata como un número, no como una variable. |
| **Logaritmo Natural ($\ln$)** | $\ln(x) = \log_e(x)$ | Es la herramienta "llave" para abrir potencias de base $e$. |
| **Propiedad de potencia** | $\ln(e^x) = x \cdot \ln(e)$ | Como $\ln(e)=1$, el resultado es $x \cdot 1 = x$. El exponente "baja" lógicamente. |
| **Bases iguales** | Si $e^a = e^b$, entonces $a = b$ | Si las bases ya son iguales, solo nos enfocamos en los exponentes. |

---

## Ejemplos resueltos adicionales

> [!example] **Ejemplo A: Bases iguales (Nivel Básico)**
> **Problema:** Resolver la ecuación $e^{x+3} = e^5$.
> 
> **Paso a paso:**
> 1. **Identificar las bases:** Ambos lados tienen la base $e$.
> 2. **Igualar exponentes:** Según la propiedad de bases iguales, si las bases son las mismas, sus exponentes deben serlo también:
>    $$x + 3 = 5$$
> 3. **Despejar $x$:** Trasladamos el 3 al otro lado con la operación contraria (resta):
>    $$x = 5 - 3$$
>    $$x = 2$$
> **Resultado:** $x = 2$.

> [!example] **Ejemplo B: Aplicación financiera (Aislamiento de base)**
> **Problema:** Una inversión de $500$ USD crece bajo el modelo $500 \cdot e^{0,5x} = 1000$. ¿En cuánto tiempo ($x$) se duplicará el dinero?
> 
> **Paso a paso:**
> 1. **Aislar la base $e$ (Paso obligatorio):** Antes de aplicar logaritmos, la base $e$ debe estar sola. Pasamos el 500 dividiendo:
>    $$e^{0,5x} = \frac{1000}{500} \implies e^{0,5x} = 2$$
> 2. **Aplicar Logaritmo Natural:** Para bajar la $x$ del exponente, aplicamos $\ln$ en ambos lados:
>    $$\ln(e^{0,5x}) = \ln(2)$$
> 3. **Simplificar usando la propiedad:** Sabemos que $\ln(e^{0,5x})$ se convierte en $0,5x \cdot \ln(e)$, y como $\ln(e)=1$:
>    $$0,5x = \ln(2)$$
> 4. **Despejar $x$:**
>    $$x = \frac{\ln(2)}{0,5}$$
> 5. **Cálculo con precisión (4 decimales):** Usando la calculadora ($\ln(2) \approx 0,6931$):
>    $$x \approx \frac{0,6931}{0,5} \approx 1,3862$$
> **Resultado:** El tiempo aproximado es de **1,3862 unidades de tiempo**.

---

## Ejercicios de repaso

> [!abstract] 🟢 Dificultad: Fácil (Bases iguales)
> 1. $e^{3x} = e^{12}$
> 2. $e^{x-7} = e^3$
> 3. $e^{2x+4} = e^{10}$

> [!abstract] 🟡 Dificultad: Media (Uso de Logaritmo Natural)
> 4. $e^x = 15$
> 5. $e^{2x} = 8$
> 6. $e^{x+1} = 4$

> [!abstract] 🔴 Dificultad: Avanzada (Binomios y Diferentes Bases)
> 7. $e^{x-2} = 60$
> 8. $250 \cdot e^{0,2x} = 750$
> 9. **DESAFÍO (Bases distintas):** $e^{x-2} = 5^{x+1}$ *(Pista: Aplica $\ln$ a ambos lados y distribuye el logaritmo en los binomios).*

---

> [!tip] 💡 Consejos de un experto
> 1. **Atención a la calculadora:** Al calcular $\ln(5)$ o cualquier valor, **siempre cierra el paréntesis** antes de sumar, restar o dividir. Un paréntesis abierto puede cambiar drásticamente tu resultado.
> 2. **$e$ no es una incógnita:** No intentes "despejar" la $e$ como si fuera una letra $x$. Recuerda que $e$ es un número fijo (2,7182...).
> 3. **Siguiente nivel:** En clases posteriores verás que algunas ecuaciones con $e$ parecen ecuaciones cuadráticas (ej. $e^{2x} - 5e^x + 6 = 0$). Estas se resuelven mediante un método llamado **Cambio de Variable**, donde sustituimos $e^x$ por una letra como $u$ para simplificar el problema. ¡Mantente atento!