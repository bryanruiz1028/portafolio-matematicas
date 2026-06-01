# 📖 Guía de estudio — Clase 07: Ley del Seno y del Coseno

¿Qué tal amigos? Espero que estén muy bien. ¡Bienvenidos a una nueva sesión de trigonometría! Hoy vamos a aprender a resolver cualquier triángulo no rectángulo. Pilas con esto, porque aunque parece difícil, si siguen mis consejos y el orden que les voy a dar, se van a volver unos expertos. ¡Vamos a darle!

> [!info] 📌 Conceptos clave
> Para dominar este tema, primero debemos entender los fundamentos que nos guían en cada ejercicio:
> - **Resolver un triángulo**: No es más que encontrar todas las medidas de los tres lados y los tres ángulos internos. 
> - **La "pareja completa"**: Es mi requisito favorito para la Ley del Seno. Se tiene una pareja cuando conoces un ángulo y su lado opuesto (por ejemplo, el ángulo $A$ y el lado $a$).
> - **Condiciones para la Ley del Coseno**: Si no hay pareja completa, ¡no se asusten! Usamos la Ley del Coseno en estos dos casos:
> 	1. **LLL (Lado-Lado-Lado)**: Conocemos los tres lados, pero ningún ángulo.
> 	2. **LAL (Lado-Ángulo-Lado)**: Conocemos dos lados y el ángulo que forman entre ellos.
> - **La prueba lógica**: Recuerden que en todo triángulo los ángulos internos deben sumar exactamente $180^\circ$. Además, fíjense siempre que el lado más largo sea opuesto al ángulo más grande. Si no es así, ¡algo anda mal!

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ley del Coseno (Lados)** | Para hallar un lado: $a^2 = b^2 + c^2 - 2bc \cdot \cos(A)$. |
| **Ley del Coseno (Ángulos)** | Para hallar un ángulo: $\cos(B) = \frac{b^2 - a^2 - c^2}{-2ac}$. <br> *Nota:* También pueden verla como $\cos(B) = \frac{a^2 + c^2 - b^2}{2ac}$ para que el denominador sea positivo. ¡Usa la que prefieras! |
| **Ley del Seno** | Relación de igualdad: $\frac{\sin(A)}{a} = \frac{\sin(B)}{b} = \frac{\sin(C)}{c}$. Úsala cuando tengas una pareja completa. |
| **Suma de Ángulos** | $A + B + C = 180^\circ$. |

> [!tip] 💡 Pro-Tip de la calculadora
> ¡Pilas aquí! Cuando metan la fórmula del ángulo de la Ley del Coseno en la calculadora, **siempre** usen paréntesis en el denominador. Si escriben `... / -2 * a * c` sin paréntesis, la calculadora hará la división y luego multiplicará, dándoles un error. Lo correcto es: `... / (-2 * a * c)`.

---

## Ejemplos resueltos paso a paso

```ad-example
title: Ejemplo A — Caso LAL (Lado-Ángulo-Lado)
**Enunciado**: En un triángulo, el ángulo $A = 112^\circ$, el lado $b = 7$ m y el lado $c = 4$ m.

**Resolución**:
1. **Hallar el lado $a$**: Como no hay pareja completa, usamos la Ley del Coseno.
   $a = \sqrt{7^2 + 4^2 - 2(7)(4) \cos(112^\circ)}$
   $a = \sqrt{49 + 16 - (56 \cdot -0,3746)} \approx 9,27$ m.
   *Nota del Profe:* Usamos $9,27$ para seguir practicando, pero al redondear, los siguientes resultados no serán "exactos", sino aproximaciones.

2. **Hallar el ángulo $B$**: Ahora que tenemos la pareja ($A$ y $a$), usamos la Ley del Seno (es más fácil el despeje).
   $\frac{\sin(112^\circ)}{9,27} = \frac{\sin(B)}{7} \Rightarrow \sin(B) = \frac{7 \cdot \sin(112^\circ)}{9,27}$
   $\sin(B) \approx 0,6999 \Rightarrow B = \sin^{-1}(0,6999) \approx 44,43^\circ$.

3. **Hallar el ángulo $C$**: Hacemos la resta fácil.
   $C = 180^\circ - 112^\circ - 44,43^\circ = 23,57^\circ$.

✅ **Resultado**: $a \approx 9,27$ m, $B \approx 44,43^\circ$, $C \approx 23,57^\circ$.
```

```ad-example
title: Ejemplo B — Caso LLL (Tres lados conocidos) con aplicación de costo
**Enunciado**: Un terreno triangular tiene lados $a = 7,5$ m, $b = 11$ m y $c = 5$ m. Si el metro lineal de cerca cuesta $10$ USD, ¿cuál es el costo total y sus ángulos?

**Resolución**:
1. **Calcular el ángulo mayor**: ¡Recomendación de oro! Busquen siempre el ángulo opuesto al lado más largo ($b = 11$ m) con la Ley del Coseno. Así evitan errores de ambigüedad después.
   $\cos(B) = \frac{11^2 - 7,5^2 - 5^2}{-2(7,5)(5)} = \frac{121 - 56,25 - 25}{-75} \approx -0,53$
   $B = \cos^{-1}(-0,53) \approx 122^\circ$.

2. **Calcular el ángulo $A$**: Usamos Ley del Seno.
   $\frac{\sin(122^\circ)}{11} = \frac{\sin(A)}{7,5} \Rightarrow \sin(A) = \frac{7,5 \cdot \sin(122^\circ)}{11} \approx 0,578$
   $A = \sin^{-1}(0,578) \approx 35,32^\circ$.

3. **Costo total**: 
   Perímetro = $7,5 + 11 + 5 = 23,5$ m.
   Costo = $23,5$ m $\times 10$ USD/m = $235$ USD.

✅ **Resultado**: Ángulos: $122^\circ, 35,32^\circ$ y $22,68^\circ$. Costo: $235$ USD.
```

---

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
1. En un triángulo con $b = 6$ cm, $c = 9$ cm y $\angle A = 115^\circ$, calcula el lado $a$ usando la Ley del Coseno. (Pista: Es el primer paso para resolver el triángulo del Video 3).
2. Tienes una pareja completa: $\angle A = 55,14^\circ$ y $a = 25$ m. Si el lado $b = 21,5$ m, halla el ángulo $B$ usando la Ley del Seno.
```

```ad-abstract
title: 🟡 Medio
1. **Evaluación**: Resuelve el triángulo completo con lados $a = 25$ m, $b = 21,5$ m y $c = 30$ m. Encuentra los tres ángulos empezando por el ángulo $A$.
2. Dado un triángulo con $b = 18$ cm, $c = 26$ cm y $\angle A = 85^\circ$, encuentra el valor del lado $a$ y el ángulo $B$.
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
Un arquitecto diseña una estructura triangular cuyos lados miden $18$ m, $26$ m y $28,94$ m. 
1. Identifica el **ángulo más pequeño** (el opuesto al lado menor) y calcula su medida. (Recuerda mi consejo: ¡puedes hallar el más grande primero para estar seguro!).
2. Como reto adicional: Calcula el costo de un recubrimiento especial para todo el perímetro si el costo es de $50$ USD por metro lineal.
```

---

> [!tip] 💡 Consejo de estudio del Profe Alex
> - **El orden sí importa**: Si conoces los tres lados (LLL), empieza **siempre** hallando el ángulo más grande con la Ley del Coseno. ¿Por qué? Porque el coseno nos dice claramente si un ángulo es obtuso (mayor a $90^\circ$) mediante un signo negativo, mientras que el seno puede ser confuso.
> - **Preferencia por el Seno**: Una vez que tienes una pareja completa, pásate a la Ley del Seno. El despeje es mucho más sencillo y rápido para nosotros.
> - **Ángulos agudos**: Si vas a usar la Ley del Seno para buscar ángulos, trata de buscar siempre el ángulo que se vea más pequeño (agudo). ¡Esto te ahorrará muchos dolores de cabeza con el "caso ambiguo"!
> - **Visualiza**: Si el papel dice que un ángulo mide $120^\circ$ pero en tu dibujo se ve chiquito, ¡revisa tus cuentas!

¡Espero que esta guía les sirva muchísimo! No olviden practicar, que es la única forma de aprender de verdad. ¡Nos vemos en la próxima clase, bye bye!