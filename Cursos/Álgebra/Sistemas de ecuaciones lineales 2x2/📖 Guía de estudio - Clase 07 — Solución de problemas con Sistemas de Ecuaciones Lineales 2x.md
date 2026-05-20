# 📖 Guía de estudio — Clase 07: Solución de problemas con Sistemas de Ecuaciones Lineales 2x2

¡Qué tal amigas y amigos! Espero que estén muy bien. En esta clase vamos a aprender a resolver problemas de la vida real usando sistemas de ecuaciones. Recuerden que, aunque muchos se pueden sacar por lógica, practicar con ecuaciones nos prepara para cuando los ejercicios se pongan realmente difíciles. ¡Vamos a darle!

> [!info] 📌 Conceptos clave
> Para resolver problemas como un experto, sigue estos cuatro pilares fundamentales:
> 1. **Nombres descriptivos para las variables:** ¡No te limites a $x$ o $y$! Usa letras que te ayuden a recordar qué buscas: $l$ para largo, $a$ para ancho, $i$ para lados iguales o $d$ para decenas.
> 2. **Traducción al lenguaje algebraico:** Es el arte de convertir palabras ("el doble", "excede", "aumenta") en símbolos matemáticos. Es el paso más importante para que la ecuación tenga sentido.
> 3. **Organización antes de resolver:** Antes de aplicar cualquier método (como el de reducción), asegúrate de que las letras estén de un lado del igual y los números del otro. ¡El orden facilita el trabajo!
> 4. **Verificación lógica:** Al terminar, no te quedes solo con el número. Vuelve al problema original y comprueba si esos valores cumplen con la historia que te contaron.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Perímetro de un Rectángulo** | Es la suma de sus cuatro lados. Profe Alex recomienda sumarlos uno a uno: $l + a + l + a = 2l + 2a$ (Donde $l$ es largo o base y $a$ es ancho o altura). |
| **Triángulo Isósceles** | Polígono con dos lados de igual medida ($i$) y un lado desigual ($d$). Su perímetro es la suma de los tres: $i + i + d = 2i + d$. |
| **Número de dos cifras** | Se representa como $10d + u$. **Nota:** Multiplicamos la cifra de las decenas ($d$) por 10 debido a su valor posicional (decenas), y le sumamos las unidades ($u$). |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Problemas Geométricos (Rectángulos)
**Enunciado:** El perímetro de un rectángulo mide 38 cm. Si se duplica el largo y se aumenta el ancho en 6 cm, el perímetro será de 74 cm. Hallar las medidas originales.

**Paso 1: Definición de variables**
- $l$: Medida del largo inicial.
- $a$: Medida del ancho inicial.

**Paso 2: Planteamiento de las ecuaciones**
Siguiendo el método de sumar los cuatro lados:
1. Ecuación inicial: $l + a + l + a = 38 \rightarrow 2l + 2a = 38$
2. Ecuación modificada: $2l + (a+6) + 2l + (a+6) = 74$
   Simplificamos: $4l + 2a + 12 = 74$
   Organizamos: $4l + 2a = 74 - 12 \rightarrow 4l + 2a = 62$

**Paso 3: Resolución por Reducción**
¡Vamos a eliminar la variable $a$! Restamos la primera ecuación de la segunda:
$(4l + 2a) - (2l + 2a) = 62 - 38$
$2l = 24$
$l = 24 / 2$
$l = 12$

Ahora sustituimos $l = 12$ en la primera ecuación para hallar el ancho:
$2(12) + 2a = 38$
$24 + 2a = 38$
$2a = 38 - 24$
$2a = 14$
$a = 7$

✅ **Resultado:** El largo mide 12 cm y el ancho mide 7 cm.
```

```ad-example
title: Ejemplo B — Problemas con Números y Cifras
**Enunciado:** En un número de dos cifras, la cifra de las unidades es el doble que la de las decenas. Si se invierten las cifras, el nuevo número excede en 27 al original.

**Planteamiento lógico:**
- Decenas: $d$, Unidades: $u$.
- Número original: $10d + u$
- Número invertido: $10u + d$ (porque ahora $u$ ocupa el lugar de las decenas).
- Condición 1: $u = 2d$
- Condición 2: $(10u + d) = (10d + u) + 27$

**Resolución:**
Sustituimos $u = 2d$ en la segunda ecuación:
$10(2d) + d = 10d + (2d) + 27$
$20d + d = 12d + 27$
$21d = 12d + 27$
$21d - 12d = 27$
$9d = 27$
$d = 3$

Si $d = 3$, entonces $u = 2(3) = 6$.

✅ **Resultado:** El número original es 36 (3 decenas y 6 unidades).
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
**Ejercicio:** La base de un rectángulo mide 13 cm más que la altura y el perímetro total es de 142 cm. Hallar la medida de la base y la altura.
*Pista: ¿Cómo podrías expresar matemáticamente que la base es "13 más que" la altura? Intenta plantearlo antes de sumar los cuatro lados.*
```

```ad-abstract
title: 🟡 Medio
**Ejercicio:** Un triángulo isósceles tiene un perímetro de 36 cm. El lado desigual es 3 cm más corto que los lados iguales. Hallar las medidas de los tres lados del triángulo.
*Pista: Si el lado desigual es más pequeño que los iguales, ¿qué operación usarías para relacionar $d$ con $i$? Recuerda que el perímetro suma los tres lados.*
```

```ad-abstract
title: 🔴 Avanzado — Aplicación Lógica
**Ejercicio:** La suma de las dos cifras de un número es 13. Si al número original se le resta 45, las cifras se invierten. Hallar el número en cuestión.
*Pista: No olvides la descomposición $10d + u$. Piensa con cuidado cómo escribir "el número original menos 45 es igual al número con las cifras cambiadas".*
```

> [!tip] 💡 Consejo de estudio de Profe Alex
> ¡No te vuelvas una máquina de resolver ecuaciones! Antes de empezar todo el proceso algebraico, intenta usar tu lógica: ¿qué números podrían sumar 13? ¿qué medidas de rectángulo tendrían sentido? Si al final tu resultado te da un número negativo para una distancia o una cifra que no es entera para un número, ¡detente! Algo falló en el planteamiento. La matemática siempre debe tener sentido en el mundo real.