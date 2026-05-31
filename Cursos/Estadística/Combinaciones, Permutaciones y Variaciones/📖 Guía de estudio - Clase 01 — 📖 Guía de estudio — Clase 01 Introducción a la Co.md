# 📖 Guía de estudio — Clase 01: Introducción a la Combinatoria

> [!info] 📌 Conceptos clave
> ¡Bienvenido al fascinante mundo de la combinatoria! Aquí aprenderás que contar no es solo decir "1, 2, 3", sino descubrir todas las formas posibles de organizar el mundo que nos rodea.
> * **Experimento aleatorio:** Es cualquier situación donde no puedes predecir el resultado con exactitud (¡como lanzar un dado o sacar una carta!).
> * **Espacio muestral ($S$ o $\Omega$):** Es el "universo" de posibilidades; la lista completa de todo lo que podría pasar.
> * **Evento o suceso:** Es un subconjunto del espacio muestral; una parte específica que nos interesa observar (por ejemplo: "que el dado caiga en un número par").
> * **Factorial ($n!$):** Es una operación matemática vital definida únicamente para números enteros positivos ($n \in \mathbb{Z}^+$) y el cero. Consiste en multiplicar un número por todos sus antecesores hasta llegar al $1$.
> * **Esencia de la combinatoria:** Todo se reduce a identificar la **Población** ($n$), que es el total de elementos, y la **Muestra** ($r$), que es el grupo que seleccionamos.

## 2. TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Experimento aleatorio** | Proceso donde no se puede predecir el resultado exacto debido al azar. |
| **Espacio muestral ($S, \Omega$)** | Conjunto de todos los resultados posibles. Se suele representar entre llaves $\{ \}$. |
| **Evento o suceso** | Uno o varios de los resultados posibles ($A \subset \Omega$). |
| **Factorial ($n!$)** | $n! = n \times (n-1) \times (n-2) \times \dots \times 1$ (Solo para enteros). |
| **Población ($n$)** | El número total de elementos disponibles en el conjunto de estudio. |
| **Muestra ($r$)** | El número de elementos que seleccionamos para realizar una agrupación. |
| **Propiedades especiales** | $0! = 1$ y $1! = 1$. |
| **Simplificación** | $\frac{n!}{(n-1)!} = n$ |

## 3. EJEMPLOS RESUELTOS ADICIONALES

```ad-example
**Ejemplo A: Lanzamiento de un dado y una moneda**
Para hallar el Espacio Muestral ($\Omega$) de este experimento, lo ideal es organizar los resultados en una cuadrícula o rejilla para no olvidar ninguna combinación. Debemos emparejar cada cara de la moneda ($C$: cara, $X$: cruz) con cada número del dado ($1, 2, 3, 4, 5, 6$).

**Resultados organizados:**
*   Con Cara ($C$): $(C, 1), (C, 2), (C, 3), (C, 4), (C, 5), (C, 6)$
*   Con Cruz ($X$): $(X, 1), (X, 2), (X, 3), (X, 4), (X, 5), (X, 6)$

**Espacio Muestral Final:**
$\Omega = \{C1, C2, C3, C4, C5, C6, X1, X2, X3, X4, X5, X6\}$
El número total de elementos es $12$. ¡Visualizarlo como una lista o tabla ayuda a ver la estructura del azar!
```

```ad-example
**Ejemplo B: El Barquillo de Helado ($5.00 USD$)**
Vas a una heladería con $7$ sabores distintos. Quieres un barquillo con $3$ bolas de helado.
*   **Población ($n$):** $7$ (los sabores disponibles en la tienda).
*   **Muestra ($r$):** $3$ (las bolas que vas a elegir).
*   **¿Importa el orden?:** No. Un helado de chocolate, fresa y vainilla es el mismo helado aunque te pongan la fresa arriba o abajo. Los sabores se mezclan en tu paladar de la misma forma.
*   **¿Se pueden repetir sabores?:** Sí. En un contexto real, la disponibilidad de un sabor no disminuye porque elijas una bola. Puedes pedir las $3$ bolas de chocolate si quieres ($n$ no se agota).
```

## 4. EJERCICIOS DE REPASO

```ad-abstract
**🟢 Nivel Fácil: Identificación Básica**
1. Escribe el espacio muestral ($S$) de lanzar dos monedas al aire (usa $C$ para cara y $X$ para cruz). ¿Cuántos resultados hay en total?
2. Calcula el valor de $3!$.
3. Calcula el valor de $5!$.
```

```ad-abstract
**🟡 Nivel Medio: Simplificación de Factoriales**
*Nota: Recuerda que simplificamos para evitar trabajar con números gigantes y reducir el margen de error.*
Resuelve las siguientes operaciones:
1. $\frac{10!}{8!}$
2. $\frac{6! \times 4!}{5! \times 3!}$
3. $\frac{12!}{10! \times 2!}$
```

```ad-abstract
**🔴 Nivel Avanzado: Aplicación de Lógica Combinatoria**
Un grupo de $10$ estudiantes compite por un comité con dos cargos: **Presidente** y **Secretario**. El puesto de Presidente es muy deseado porque incluye un premio de $100 USD$ en efectivo, mientras que el Secretario no recibe dinero.
1. Identifica la Población ($n$) y la Muestra ($r$).
2. ¿Importa el orden en que se eligen los nombres? **Justifica tu respuesta** pensando en la "diferencia funcional": ¿Es lo mismo ser Presidente que Secretario considerando el premio de $100 USD$?
3. ¿Se puede repetir el mismo estudiante en ambos cargos? (¿Puede una persona ser su propio secretario?).
```

## 5. CONSEJO DE ESTUDIO

> [!tip] 💡 La técnica de la "Escalera Descendente"
> ¡No pierdas tiempo multiplicando todo el factorial! Si tienes una división, desarrolla el número mayor del numerador solo hasta que alcances el número del denominador para poder cancelarlos. Esto simplifica tu vida y tus cálculos.
>
> **Ejemplo: Para resolver $\frac{15!}{13!}$**
>
> $$\frac{15 \times 14 \times 13!}{13!}$$
>
> Al cancelar los $13!$, la operación se reduce simplemente a:
>
> $$15 \times 14 = 210$$

¡Excelente trabajo llegando hasta aquí! Recuerda que la combinatoria es como un rompecabezas: lo más importante es observar bien las reglas antes de empezar a armarlo. **¡Sigue practicando y dominarás el azar!**