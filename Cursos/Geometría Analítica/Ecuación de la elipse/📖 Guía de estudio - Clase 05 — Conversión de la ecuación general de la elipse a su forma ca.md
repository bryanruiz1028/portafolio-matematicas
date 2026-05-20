# 📖 Guía de estudio — Clase 05: De la Ecuación General a la Ecuación Canónica de la Elipse

> [!info] 📌 Conceptos clave
> Para dominar la elipse, debemos entender cómo transformar una expresión desordenada en una herramienta visual. Aquí los pilares:
> 1. **Diferencia Estructural:** La **Ecuación General** es una expresión extendida igualada a cero ($Ax^2 + By^2 + Dx + Ey + F = 0$). La **Ecuación Canónica** (u ordinaria) está diseñada para mostrar el centro $(h, k)$ y los semiejes, y **siempre debe estar igualada a 1**.
> 2. **Trinomio Cuadrado Perfecto (TCP):** Es nuestra técnica de "empaquetado". Nos permite convertir tres términos en un binomio al cuadrado, como $(x-h)^2$.
> 3. **La Regla de Oro:** Para completar un trinomio, tomamos el coeficiente del término lineal ($b$), lo dividimos para 2 y lo elevamos al cuadrado: $\left(\frac{b}{2}\right)^2$.
> 4. **Equilibrio y Factores Externos:** Si sumas un valor dentro de un paréntesis que tiene un factor común afuera, al otro lado de la igualdad debes sumar el producto de ambos. ¡Es el secreto para que la balanza matemática no se rompa!
> 5. **Casos Especiales:** Si una variable no tiene término lineal (por ejemplo, aparece $5y^2$ pero no hay un término con $y$), esa parte ya está "completa". No necesitas hacer el proceso de completar el cuadrado para esa variable; se queda simplemente como $y^2$.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ecuación General** | Estructura desarrollada: $Ax^2 + By^2 + Dx + Ey + F = 0$. |
| **Completar el Cuadrado** | Fórmula para hallar el tercer término: $\left(\frac{b}{2}\right)^2$. |
| **Factorización del TCP** | El paso de trinomio a binomio: $x^2 + bx + \left(\frac{b}{2}\right)^2 = \left(x + \frac{b}{2}\right)^2$. |
| **Ecuación Canónica** | Forma final que iguala a 1: $\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1$. |

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Paso a paso (Caso Estándar)
Convertiremos la ecuación $4x^2 + 9y^2 - 40x + 54y + 145 = 0$:

1. **Organizar:** Agrupamos $x$ con $x$, $y$ con $y$, y movemos el término independiente:  
   $(4x^2 - 40x) + (9y^2 + 54y) = -145$
2. **Factorización por factor común:** Para aplicar la regla de completar el cuadrado, el coeficiente de $x^2$ y $y^2$ debe ser 1. Extraemos los números de adelante:  
   $4(x^2 - 10x) + 9(y^2 + 6y) = -145$
3. **Completar el TCP:** Aplicamos $\left(\frac{b}{2}\right)^2$ dentro de los paréntesis:  
   Para $x$: $\left(\frac{10}{2}\right)^2 = 25$. Para $y$: $\left(\frac{6}{2}\right)^2 = 9$.  
   $4(x^2 - 10x + 25) + 9(y^2 + 6y + 9) = -145 + \dots$
4. **Equilibrar:** Sumamos a la derecha los valores multiplicados por su factor externo ($25 \times 4 = 100$ y $9 \times 9 = 81$):  
   $4(x-5)^2 + 9(y+3)^2 = -145 + 100 + 81$  
   $4(x-5)^2 + 9(y+3)^2 = 36$
5. **Dividir para igualar a 1:** Dividimos todo por $36$. **¿Por qué?** Porque la forma canónica requiere el "1" para establecer la escala estándar de la elipse y permitirnos identificar los semiejes ($a$ y $b$):  
   $\frac{4(x-5)^2}{36} + \frac{9(y+3)^2}{36} = \frac{36}{36}$
   
✅ **Resultado final:** $\frac{(x-5)^2}{9} + \frac{(y+3)^2}{4} = 1$
```

```ad-example
title: Ejemplo B — El truco del "Denominador del Denominador"
A veces, al simplificar, nos queda un número multiplicando al paréntesis, como en este caso: $\frac{4(x-3)^2}{5} + \frac{y^2}{9} = 1$.

En la forma canónica pura, el numerador debe ser $1$. Para lograrlo sin alterar la igualdad, aplicamos la identidad matemática: **Multiplicar por $\frac{4}{5}$ es exactamente lo mismo que dividir por $\frac{5}{4}$**. 

Simplemente "bajamos" el numerador al fondo del denominador:
$\frac{(x-3)^2}{\frac{5}{4}} + \frac{y^2}{9} = 1$

✅ **Resultado:** Esto nos permite identificar que $a^2 = \frac{5}{4}$ (o $1.25$), cumpliendo con la estructura estética y funcional de la elipse.
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil — Solo un trinomio
En estos ejercicios, una de las variables ya está "lista" (no tiene término lineal). Completa el cuadrado solo donde sea necesario:
1. $45x^2 + 2y^2 + 16y + 27 = 0$
2. $36x^2 + 5y^2 - 216x + 279 = 0$
```

```ad-abstract
title: 🟡 Medio — Proceso Completo
Realiza la factorización por factor común, completa ambos trinomios y simplifica:
1. $3x^2 + 8y^2 + 12x + 48y + 60 = 0$
2. $10x^2 + 3y^2 + 100x + 18y + 247 = 0$
```

```ad-abstract
title: 🔴 Avanzado — Reto del Arquitecto
Un arquitecto diseña una sección de un museo con forma elíptica cuya ecuación general es $4x^2 + 45y^2 - 8x - 11 = 0$. Para instalar los soportes principales, necesita conocer el centro $(h, k)$ y el valor exacto de los denominadores. 

**Tu misión:** Convierte la ecuación a su forma canónica. Ten cuidado: uno de los denominadores requerirá la técnica del "denominador del denominador" vista en el Ejemplo B.
```

> [!tip] 💡 Consejo de estudio
> **¡Cuidado con la trampa del equilibrio!** El error más común es sumar el número (por ejemplo, el $25$) directamente al otro lado. Recuerda el "Método del Profe Alex": ese número vive dentro de un paréntesis que está multiplicado por un factor externo. **Siempre multiplica antes de equilibrar.** ¡Si mantienes la balanza, el éxito está asegurado!