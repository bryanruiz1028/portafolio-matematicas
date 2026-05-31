# Clase 02 — Probabilidad de un evento simple

`#algebra` `#probabilityofas`

[[Clase 01]] | [[Inicio]] | [[Clase 03]]

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> La probabilidad es la herramienta matemática que nos permite medir qué tan posible es que ocurra un suceso cuando interviene el azar. Gracias a ella, podemos transformar la incertidumbre en números precisos para tomar mejores decisiones antes de que las cosas sucedan.
> 
> - **En 💵 [aplicación con $USD]:** Te ayuda a calcular tus opciones reales de ganar un premio en una rifa o sorteo de dinero antes de decidir si realmente vale la pena gastar un dólar en un boleto.
> - **En 🏗️ [aplicación práctica]:** Se utiliza en el control de calidad industrial para seleccionar productos al azar y determinar si un lote completo es confiable.
> - **En 📊 [situación cotidiana]:** Es fundamental en los juegos de mesa para entender qué tan difícil es obtener un número específico con un dado o encontrar la carta ganadora en una baraja.

## Concepto clave

> [!note] 📌 ¿Qué es la Probabilidad de un evento simple?
> Para calcular qué tan probable es que algo pase, usamos la **Ley de Laplace**. Piensa en esto como una **proporción** o una comparación: arriba ponemos lo que buscamos que suceda ("casos favorables") y abajo ponemos todo lo que podría llegar a pasar en total ("casos posibles"). Es simplemente dividir lo que quiero entre el total de opciones.

> [!warning] ⚠️ Error común
> ¡Nunca pongas el número total arriba! En probabilidad, el número de abajo (denominador) siempre debe ser **igual o mayor** al número de arriba. Si tienes 10 dulces en total, es imposible que saques 12 dulces rojos.

> [!tip] 💡 Truco para recordarlo
> Usa esta regla mnemotécnica: **"Lo que quiero arriba, lo que hay abajo"**. Así siempre sabrás dónde colocar cada número para armar tu fracción.

## Procedimiento paso a paso

```text
Fórmula: P(A) = Casos Favorables / Casos Posibles

PASO 1 → Contar el número total de casos posibles (el total de elementos).
PASO 2 → Identificar el número de casos favorables (lo que me piden buscar).
PASO 3 → Escribir la fracción (Favorables / Posibles) y simplificarla.
PASO 4 → Convertir a decimal (dividiendo) y a porcentaje (multiplicando por 100).
         Ejemplo: 1/2 = 0.50 -> 50%
```

## Ejemplos de clase

```ad-example
title: Ejemplo 1: Caso básico (Urna con bolas)
En una urna hay 4 bolas rojas, 2 azules y 1 amarilla. Si sacamos una al azar, ¿cuál es la probabilidad de que sea roja?
- **Total (Casos posibles):** 4 + 2 + 1 = 7.
- **Favorables:** 4 (porque hay 4 rojas).
- **Fracción:** 4/7.
- **Porcentaje:** (4 ÷ 7) × 100 = **57.14%**.
```

```ad-example
title: Ejemplo 2: Casos lógicos (El dado)
Si lanzas un dado de 6 caras, ¿cuál es la probabilidad de sacar un número menor a 4 (P < 4)?
- **Total (Casos posibles):** 6 (números del 1 al 6).
- **Favorables:** 3 (los números 1, 2 y 3 son los únicos menores que 4).
- **Fracción:** 3/6 = 1/2.
- **Porcentaje:** 0.50 × 100 = **50.00%**.
```

```ad-example
title: Ejemplo 3: Caso avanzado (Sin reemplazo)
Tienes una caja con 2 canicas azules y 3 verdes (Total 5). Sacas una azul y **no la devuelves**. ¿Cuál es la probabilidad de que la segunda sea verde?
- **Nuevo Total:** **4** (porque ya sacamos una azul y el total disminuyó).
- **Favorables:** 3 (porque aún quedan todas las verdes intactas).
- **Fracción:** 3/4.
- **Porcentaje:** 0.75 × 100 = **75.00%**.
*Nota: ¡Mira cómo cambió el denominador al no devolver la canica!*
```

```ad-example
title: Ejemplo 4: Aplicación con $USD (La Baraja)
En una baraja de 52 cartas, pagas $1 USD por intentar sacar un "As" y ganar un premio. ¿Qué probabilidad tienes de ganar?
- **Total:** 52 cartas.
- **Favorables:** 4 (As de corazones, diamantes, tréboles y picas).
- **Fracción:** 4/52 = 1/13.
- **Porcentaje:** (1 ÷ 13) × 100 ≈ **7.69%**.
*Reflexión: Tienes menos del 8% de probabilidad de ganar. ¿Crees que es una buena inversión de tu dólar?*
```

## Ejercicios para el estudiante

1. **🟢 Fácil:** Tienes 6 esferos en tu cartuchera: 3 azules, 2 rojos y 1 negro. Calcula la probabilidad de sacar al azar uno azul $P(azul)$ y uno negro $P(negro)$.
2. **🟡 Medio:** De una baraja de 52 cartas, calcula la probabilidad de sacar una "letra" (A, J, Q, K). *(Ten en cuenta que hay 4 de estas letras por cada uno de los 4 palos de la baraja).*
3. **🔴 Avanzado (Aplicación con $USD):** En una urna hay 16 bolas: 4 negras, 6 amarillas, 4 azules y 2 rojas. Si al sacar una bola roja ganas un premio de $10 USD, ¿qué probabilidad tienes de ganar el dinero? Expresa el resultado en fracción simplificada y porcentaje.

## Respuestas y Autoevaluación

```ad-success
title: Clave de respuestas
1. **Ejercicio Fácil:** 
   - P(azul) = 3/6 = 1/2 (**50.00%**).
   - P(negro) = 1/6 (**16.67%**).

2. **Ejercicio Medio:** 
   - P(letra) = 16/52 = 4/13 (**30.77%**).

3. **Ejercicio Avanzado:** 
   - P(roja) = 2/16 = **1/8** (**12.50%**). 
   - *Interpretación:* Tienes 1 probabilidad entre 8 de ganar los $10 USD.
```

### Mini-prueba de autoevaluación

```ad-question
title: Pregunta 1: Conceptual
Si un evento es imposible de realizar (por ejemplo, sacar una bola blanca de una caja donde solo hay bolas verdes), ¿cuál es su porcentaje de probabilidad?
*(Respuesta: 0%)*
```

```ad-question
title: Pregunta 2: Procedimental
Al lanzar un dado normal de 6 caras, ¿cuál es la probabilidad de sacar un número primo (recuerda que los primos en el dado son 2, 3 y 5)?
*(Respuesta: 3/6 = 1/2 = 50.00%)*
```

```ad-question
title: Pregunta 3: Aplicación $USD
Hay 10 sobres cerrados sobre una mesa y solo uno de ellos contiene un billete de $100 USD. Si eliges uno al azar, ¿qué probabilidad tienes de llevarte el dinero?
*(Respuesta: 1/10 o 10.00%)*
```

## Notas para el próximo tema y Navegación

> [!tip] 💡 En la próxima clase
> Veremos qué sucede cuando los eventos se vuelven más complejos; por ejemplo, qué pasa cuando queremos calcular la probabilidad de que ocurran dos cosas al mismo tiempo o cuando el resultado de la primera acción afecta totalmente a la segunda.

[[Clase 01]] | [[Inicio]] | [[Clase 03]]