# 📖 Guía de estudio — Clase 06: Potencias con exponente fraccionario

> [!info] 📌 Conceptos clave
> 1. **El denominador como índice:** En una potencia con exponente fraccionario, el denominador indica siempre el índice de la raíz (por ejemplo, si el denominador es 4, obtendremos una raíz cuarta).
> 2. **El numerador como potencia:** El numerador de la fracción funciona como el exponente al que queda elevada la base dentro del radical.
> 3. **Importancia de la descomposición:** Descomponer la base en sus factores primos (como transformar $27$ en $3^3$ o $32$ en $2^5$) es el paso fundamental para simplificar raíces de forma exacta y rápida.
> 4. **Regla del exponente negativo:** Para cambiar el signo de un exponente a positivo, se debe invertir la posición de la base: si está en el numerador pasa al denominador, y si es una fracción, se intercambian numerador y denominador.

---

## Sección: Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Exponente fraccionario** | Regla general: $a^{m/n} = \sqrt[n]{a^m}$. La base se mantiene, el numerador ($m$) es la potencia y el denominador ($n$) el índice. |
| **Propiedad de la raíz de una fracción** | Al aplicar una raíz a una fracción, se extrae la raíz de forma independiente tanto al numerador como al denominador: $\sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}}$. |
| **Exponente negativo** | Para eliminar el negativo: $a^{-n} = \frac{1}{a^n}$. En fracciones, aplicamos la inversión: $\left(\frac{a}{b}\right)^{-n} = \left(\frac{b}{a}\right)^n$. |

---

## Sección: Ejemplos Resueltos Adicionales

````ad-example
**Ejemplo A: Simplificación con potencias ($27^{2/3}$)**
Este ejercicio nos enseña a utilizar la división de exponentes para eliminar la raíz.
1. **Paso 1 (Conversión):** Transformamos la potencia fraccionaria en raíz. El denominador 3 es el índice: $\sqrt[3]{27^2}$.
2. **Paso 2 (Descomposición y Propiedad):** Descomponemos 27 en $3^3$. Aplicamos la propiedad de **potencia de una potencia** (los exponentes se multiplican): $\sqrt[3]{(3^3)^2} = \sqrt[3]{3^6}$.
3. **Paso 3 (Simplificación final):** Dividimos el exponente entre el índice ($6 \div 3 = 2$). El resultado es $3^2$, lo que nos da **9**.
````

````ad-example
**Ejemplo B: Aplicación en Inversiones ($USD)**
**Escenario:** Un capital de **$16 USD** se somete a un ajuste de escalamiento de inversión definido por el índice $16^{1/4}$. ¿Cuál es el valor resultante?
1. **Paso 1 (Conversión):** El exponente $1/4$ equivale a una raíz cuarta: $\sqrt[4]{16}$.
2. **Paso 2 (Factores primos):** Descomponemos el 16. Sabemos que $16 = 2 \cdot 2 \cdot 2 \cdot 2$, es decir, $2^4$.
3. **Paso 3 (Resolución):** Obtenemos $\sqrt[4]{2^4}$. Al dividir el exponente entre el índice ($4 \div 4 = 1$), la raíz se elimina, resultando en $2^1$. El valor final es **$2 USD**.
````

---

## Sección: Ejercicios de Repaso

````ad-abstract
**🟢 Nivel Fácil: Conversión Directa**
Expresa las siguientes potencias en forma de raíz (sin resolver el cálculo final):
1. $5^{2/3}$
2. $3^{1/2}$
3. $2^{4/5}$
````

````ad-abstract
**🟡 Nivel Medio: Desarrollo con Fracciones**
Resuelve paso a paso. Recuerda que es más fácil sacar la raíz del numerador y del denominador por separado:
1. $(1/5)^{2/3}$ (Expresa el resultado como raíz de una fracción simplificada).
2. $(9/16)^{1/2}$ (Calcula la raíz cuadrada exacta de cada término).
3. $(1/27)^{1/3}$ (Usa factores primos para el denominador).
````

````ad-abstract
**🔴 Nivel Avanzado: Aplicación de Valor Residual ($USD)**
**Problema:** Una herramienta industrial tiene un costo de **$32 USD**. Se estima que su valor residual después de un periodo de uso está dado por la expresión $32^{1/5}$.
*   **Tarea:** Encuentra el valor final en dólares. 
*   **Pista pedagógica:** Descompone el número 32 en sus factores primos ($2^n$) para cancelar el índice de la raíz inmediatamente.
````

---

## Sección: Consejo de Estudio

> [!tip] 💡 Consejo de estudio
> Para resolver estos ejercicios con la velocidad de un experto, domina la **descomposición en factores primos**. Como hemos visto con el "Profe Alex", transformar números grandes en potencias (como $16 \to 2^4$ o $32 \to 2^5$) permite cancelar raíces de inmediato dividiendo el exponente por el índice. ¡Dominar los primos es dominar las raíces!