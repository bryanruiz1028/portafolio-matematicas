# 📖 Guía de estudio — Clase 01: Introducción a los Números Binarios y Conversiones

¡Qué tal, amigas y amigos! Espero que estén muy bien. Bienvenidos a su primera clase de Alfabetización Digital. Hoy vamos a descubrir el "idioma" que hablan las computadoras. Aunque parezca algo complejo, verán que es muy parecido a cómo contamos nosotros, ¡solo que con menos símbolos! ¡Vamos a darle!

> [!info] 📌 Conceptos clave
> 1. **Base 2:** A diferencia de nuestro sistema decimal (base 10), el binario solo usa la base 2 para organizar la información.
> 2. **Símbolos (0 y 1):** Solo empleamos dos dígitos. Con ellos podemos representar cualquier número, desde un simple 1 hasta millones.
> 3. **Sistema Posicional:** El valor de un número depende de su lugar. Es como en el decimal, donde un "7" puede valer 7, 70 o 700; aquí, cada posición tiene un peso específico.
> 4. **Estados en Computación:** En el mundo digital, el **1** representa un estado de "encendido" (verdadero/corriente) y el **0** un estado de "apagado" (falso/sin corriente).

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Sistema Binario** | Sistema de numeración que utiliza solo los símbolos 0 y 1 para representar datos. |
| **Valor Posicional** | Cada cifra tiene un valor según su ubicación; **cada posición hacia la izquierda vale el doble de la anterior** ($1, 2, 4, 8, 16...$). |
| **Bit (0 y 1)** | Es la unidad mínima de información. El **1** indica que el valor de esa posición "se suma", y el **0** que "no se suma". |

## Ejemplos Resueltos con el Profe

> [!example] Ejemplo A: Conversión de Binario a Decimal (Caso básico)
> **Problema:** Convertir el número binario $11001_2$ a decimal.
> 
> **Paso a paso:**
> 1. **Ubicamos los pesos:** Escribimos los valores (el doble del anterior) sobre el número de derecha a izquierda.
>    - $1 \rightarrow 16$
>    - $1 \rightarrow 8$
>    - $0 \rightarrow 4$
>    - $0 \rightarrow 2$
>    - $1 \rightarrow 1$
> 2. **Sumamos los "encendidos":** Solo sumamos los valores donde hay un **1**.
>    - $16 + 8 + 1 = 25$
> 
> **Resultado:** $11001_2 = 25_{10}$

> [!example] Ejemplo B: Escenario de Ahorro USD (Decimal a Binario)
> **Escenario:** Tienes **$34 USD** y quieres representarlo en binario usando el "Método de la Tabla".
> 
> **Paso a paso:**
> 1. **Dibujamos nuestra tabla de potencias:**
> 
> | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
> | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
> | 0 | **1** | 0 | 0 | 0 | **1** | 0 |
> 
> 2. **Lógica de encendido/apagado:**
>    - ¿Cabe el 32 en el 34? **Sí**. Ponemos un **1** ($34 - 32 = 2$ restantes).
>    - ¿Cabe el 16 en el 2? No (0). ¿El 8? No (0). ¿El 4? No (0).
>    - ¿Cabe el 2 en el 2? **Sí**. Ponemos un **1** ($2 - 2 = 0$).
>    - Como ya llegamos a cero, el último espacio (1) lleva un **0**.
> 
> **Resultado:** $34_{10} = 100010_2$

## Ejercicios de Repaso

> [!abstract] Nivel Fácil (🟢) - Conversión a Decimal
> ¡Empecemos con calma! Identifica qué valores se suman:
> 1. $101_2$
> 2. $110_2$
> 3. $1000_2$

> [!abstract] Nivel Medio (🟡) - Conversión a Binario
> Usa el método de divisiones sucesivas. **Truco del Profe Alex:** Si el número es impar (como 113), réstale 1 mentalmente para sacar la mitad fácilmente (ej. mitad de 113 $\rightarrow$ $112/2 = 56$ y sobra **1**).
> 1. Convertir el número **25** a binario.
> 2. Convertir el número **84** a binario.
> 3. Convertir el número **113** a binario.

> [!abstract] Nivel Avanzado (🔴) - Operaciones y Aplicación
> ¡Reto extremo para expertos! Recuerda aplicar las reglas del acarreo:
> 1. Realiza la siguiente suma binaria: $110010_2 + 110100_2$.
> 2. Toma el resultado del ejercicio anterior y conviértelo a decimal para saber cuántos dólares ($USD$) representa.
> 3. Un estudiante ahorra $111_2$ USD el lunes y $101_2$ USD el martes. ¿Cuál es el total de su ahorro expresado en binario?

## Reglas de la Suma Binaria

Sumar en binario es como llenar un balde: cuando se desborda, pasas el sobrante a la siguiente columna. Como solo tenemos dos dígitos (0 y 1), estas son las reglas:

*   **$0 + 0 = 0$**
*   **$0 + 1 = 1$**
*   **$1 + 0 = 1$**
*   **$1 + 1 = 10$**: ¡Cuidado aquí! Como el "2" no existe, escribimos **0** y "llevamos" (acarreo) **1** a la izquierda. Es decir, $10_2$ es la forma binaria de escribir el número 2.
*   **$1 + 1 + 1 = 11$**: Si tienes tres unos (por el acarreo), el resultado es 3. Escribimos **1** y llevamos **1**, porque $11_2$ representa al número 3.

> [!tip] 💡 Consejo de estudio
> ¡No confíes solo en tu memoria! Antes de resolver, escribe siempre la secuencia **$1, 2, 4, 8, 16, 32...$** de derecha a izquierda sobre tu número binario. Esta "guía visual" es el secreto para no perderse nunca en las conversiones.