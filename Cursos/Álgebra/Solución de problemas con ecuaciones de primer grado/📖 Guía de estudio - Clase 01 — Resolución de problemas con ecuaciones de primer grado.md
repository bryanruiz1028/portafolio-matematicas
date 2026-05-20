# 📖 Guía de estudio — Clase 01: Resolución de problemas con ecuaciones de primer grado

> [!info] 📌 Conceptos clave
> Para dominar el álgebra como un experto, el "Profe Alex" nos propone cuatro pilares fundamentales:
> - **Definir la incógnita:** Antes de escribir cualquier número, debemos identificar qué buscamos y darle un nombre (una letra, como $n$). Es el primer paso para organizar nuestra mente.
> - **Traducción al lenguaje algebraico:** Consiste en convertir las palabras de nuestro idioma a símbolos matemáticos. Es como aprender a hablar un nuevo idioma.
> - **Razonamiento lógico previo:** ¡No te lances a la ecuación de inmediato! Intentar resolver el problema mentalmente mediante el "tanteo razonado" ayuda a desarrollar una **intuición numérica** invaluable.
> - **Verificación obligatoria:** Siempre comprueba tu resultado en el enunciado original. Si los números encajan, habrás terminado con éxito y, como dice el Profe, podrás "irte a dormir tranquilo".

## Fórmulas y Definiciones Importantes

Utiliza esta tabla como un diccionario para traducir tus problemas:

| Término | Definición / Fórmula |
| :--- | :--- |
| **Doble de un número** | $2n$ |
| **Triple de un número** | $3n$ |
| **Mitad de un número** | $n / 2$ |
| **Quinta parte** | $n / 5$ |
| **Diferencia** | Resultado de una resta. **Ojo:** El orden importa; la "Diferencia entre A y B" se escribe como $A - B$. |
| **Consecutivo / Sucesor** | El número que sigue inmediatamente ($n + 1$). |
| **Antecesor** | El número que está justo antes ($n - 1$). |
| **Perímetro de un rectángulo** | Suma de los cuatro lados ($2 \times \text{base} + 2 \times \text{altura}$). |

> [!tip] 💡 Tip de experto
> Siempre que tengas dos valores desconocidos, te recomiendo asignarle la variable $n$ al **valor menor**. Esto hará que tus planteamientos usen sumas en lugar de restas, ¡y así es mucho más difícil equivocarse!

---

## Ejemplos Resueltos Adicionales

````ad-example
title: Ejemplo A — Números y sus partes
**Enunciado:** El doble de un número y su mitad suman 45. ¿Cuál es el número?

**Razonamiento lógico:** Pensemos... si el número fuera 20, su doble es 40 y su mitad es 10; la suma daría 50. ¡Nos pasamos un poquito! El número debe ser algo menor que 20. Probemos con 18.

**Resolución algebraica:**
1. **Paso 1 (Definir $n$):** Sea $n$ el número buscado.
2. **Paso 2 (Plantear la ecuación):** $2n + \frac{n}{2} = 45$.
3. **Paso 3 (Resolver):** Para eliminar el denominador (2) y trabajar más fácil, multiplicamos todos los términos de la ecuación por 2:
   - $2(2n) + 2(\frac{n}{2}) = 2(45)$
   - $4n + n = 90$
   - $5n = 90$
   - $n = 18$
4. **Paso 4 (Verificar):** El doble de 18 es 36. La mitad de 18 es 9. $36 + 9 = 45$. 
**Resultado:** ✅ El número es 18. ¡Verificado! Ahora podemos irnos a dormir tranquilos.
````

````ad-example
title: Ejemplo B — Dimensiones y Costos
**Enunciado:** El costo de cercar el largo de un terreno es el triple que el de su ancho. Si el perímetro total de la cerca costó $32 USD, ¿cuál es el costo por cada lado?

**Razonamiento lógico:** Si el ancho costara $5, el largo costaría $15. El perímetro sería $5 + 15 + 5 + 15 = 40. Como buscamos 32, el costo debe ser un poco menor.

**Resolución algebraica:**
1. **Paso 1:** Definimos el costo del ancho como $n$. El costo del largo, por ser el triple, será $3n$. (Recuerda: ¡puedes usar cualquier letra, pero $n$ es genial para números!).
2. **Paso 2:** El perímetro es la suma de los cuatro lados (dos anchos y dos largos):
   - $n + 3n + n + 3n = 32$
3. **Paso 3:** Sumamos los términos semejantes:
   - $8n = 32 \rightarrow n = 4$
4. **Paso 4:** Si el ancho cuesta $4, el largo cuesta $3 \times 4 = 12$.
**Resultado:** ✅ Anchos: $4 USD cada uno. Largos: $12 USD cada uno. (Comprobación: $4+12+4+12 = 32$). ¡A dormir tranquilos!
````

---

## Ejercicios de Repaso

````ad-abstract
title: 🟢 Fácil
1. Encuentra dos números consecutivos cuya suma sea 451.
2. Halla tres números consecutivos que al sumarse den como resultado 81.
3. Si la suma de dos números consecutivos es 25, ¿cuáles son esos números?
````

````ad-abstract
title: 🟡 Medio
1. Al sumar el triple de un número con el doble de su sucesor se obtiene 42. ¿De qué número se trata?
2. Las edades de dos hermanos suman 34 años. Si el mayor tiene 4 años más que el menor, ¿cuál es la edad de cada uno? *(Tip: ponle la variable al menor).*
3. Determina un número tal que la suma de su doble y su sucesor sea igual a 31.
````

````ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
1. La diferencia entre el quíntuple del antecesor de un precio y el triple de su sucesor es $24 USD. Calcula el precio original. *(Nota: recuerda usar paréntesis para el antecesor $(n-1)$ y el sucesor $(n+1)$).*
2. El costo total de cercar un terreno rectangular es $94 USD. Si el largo cuesta $5 USD más que el doble del ancho, ¿cuánto cuesta cada dimensión?
3. Se compran tres artículos con precios consecutivos que suman un total de $81 USD. ¿Cuál es el valor del artículo más caro?
````

---

> [!tip] 💡 Consejo de estudio
> **La técnica de la "Resolución por Lógica":** Antes de escribir la ecuación, intenta "adivinar" razonadamente la respuesta. Si la suma debe dar 45, prueba con un número y ajusta según te pases o te faltes. Esta práctica no es perder el tiempo; al contrario, desarrolla tu **intuición numérica** y te permite saber si tu respuesta algebraica tiene sentido. Una vez que la ecuación te dé el mismo resultado que tu lógica, sabrás que dominas el tema y podrás descansar sin dudas.