# Clase 03 — Ecuaciones Exponenciales con Bases Iguales

#algebra #ecuacionesexpon

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [[Clase 02 — Potenciación y Propiedades]]
> 🏠 **Índice:** [[Curso de Álgebra Elemental]]

---

¡Qué tal, amigos! Espero que estén muy bien. Bienvenidos a una nueva clase. Hoy vamos a trabajar un tema que parece difícil, pero si le ponemos lógica y recordamos lo que sabemos de potencias, ¡esto sale muy fácil!

## Relevancia y Aplicaciones

Las ecuaciones exponenciales son especiales porque la variable que buscamos está "escondida" en el exponente. Aprender a resolverlas es como aprender a hackear el crecimiento de las cosas.

### ¿Dónde vemos esto?
*   **💵 $USD:** Para calcular cuánto tiempo debe pasar para que una inversión en dólares crezca hasta una cifra meta.
*   **🏗️ Práctica:** En el estudio de poblaciones que crecen muy rápido o en la resistencia de materiales en ingeniería.
*   **📊 Cotidiana:** Es la matemática que protege tus contraseñas y ayuda a que los algoritmos de búsqueda funcionen velozmente.

---

## Concepto Clave

> [!note] **¿Qué es una Ecuación Exponencial?**
> Es una igualdad donde la letra desconocida (incógnita) aparece en el exponente. Para resolverlas, nuestro objetivo principal es lograr que los dos lados de la igualdad tengan la misma base.

> [!warning] **¡Cuidado aquí!**
> Este método de "Bases Iguales" solo funciona si podemos transformar ambos números a la misma base. Si tienes algo como $2^x = 82$, por más que busques, el 82 no es una potencia exacta de 2. En esos casos, este soplete no nos sirve y necesitaremos usar **logaritmos**, que veremos más adelante.

> [!tip] **Regla de Oro**
> "Bases iguales, exponentes se igualan". Si logras que $a^x = a^b$, entonces automáticamente puedes decir que $x = b$. ¡Así de sencillo!

---

## Procedimiento Paso a Paso

Aquí tienes la ruta ganadora para resolver cualquier ejercicio de este tipo:

```text
1. Identificar si las bases son iguales o si podemos transformarlas.
2. Transformar los números a potencias conocidas (usa tu "soplete" de potencias).
   - PLAN B: Si no conoces la potencia, saca "Factores Primos" (descompón el número dividiendo sucesivamente).
3. Aplicar la propiedad: Elimina las bases e iguala los exponentes resultantes.
4. Resolver la ecuación algebraica que te quede y verificar el resultado.
```

---

## Bloques de Ejemplos

### Ejemplo 1: Nivel Básico (Uso de bases)
**Problema:** Resolver $2^x = 8$
1. El 8 se puede escribir en base 2.
2. Transformamos: $8 = 2^3$.
3. La ecuación queda: $2^x = 2^3$.
4. **Resultado:** $x = 3$. (Porque $2$ elevado a la $3$ es $8$).

### Ejemplo 2: Con Expresión Algebraica
**Problema:** Resolver $3^{2x-1} = 27$
1. Buscamos el 27 en nuestro soplete de potencias de 3: $27 = 3^3$.
2. Igualamos los exponentes: $2x - 1 = 3$.
3. Despejamos la $x$ como una ecuación normal:
   - $2x = 3 + 1 \implies 2x = 4$
   - $x = 4/2$
4. **Resultado:** $x = 2$.

### Ejemplo 3: Avanzado (Raíces y Fracciones)
**Problema:** Resolver $\sqrt{7^x} = \frac{1}{49}$
1. **Transformamos la raíz:** Recuerda que el índice (2) pasa a ser el denominador del exponente: $\sqrt{7^x} = 7^{x/2}$.
2. **Transformamos la fracción:** Primero, $49 = 7^2$. Para subirlo al numerador, le ponemos exponente negativo: $\frac{1}{49} = 7^{-2}$.
3. **Igualamos:** $7^{x/2} = 7^{-2} \implies \frac{x}{2} = -2$.
4. **Despejamos:** El 2 que divide pasa a multiplicar: $x = -2 \cdot 2$.
5. **Resultado:** $x = -4$.

### Ejemplo 4: Aplicación en Finanzas ($USD)
**Problema:** El valor de una criptomoneda en dólares sube según la función $2^x = 64$, donde $x$ es el tiempo en meses. ¿En cuántos meses el valor alcanzará los 64 dólares?
1. Usamos el **Plan B (Factores Primos)** para 64: 64 tiene mitad (32), mitad (16), mitad (8), mitad (4), mitad (2) y mitad (1). ¡El 2 se repite 6 veces!
2. Entonces: $64 = 2^6$.
3. Igualamos: $2^x = 2^6$.
4. **Resultado:** $x = 6$ meses.

---

## Ejercicios para el Estudiante

> [!abstract] **¡A practicar, amigos!**
>
> **🟢 Nivel Fácil**
> 1. $5^x = 25$
> 2. $2^x = 16$
> 3. $3^x = 243$
> 4. $10^x = 1000$
>
> **🟡 Nivel Medio**
> 5. $3^{x+2} = 81$
> 6. $2^{3x-2} = 32$
> 7. $5^{2x-4} = 125$
> 8. $4^{x+1} = 64$
>
> **🔴 Nivel Avanzado**
> 9. $\sqrt{2^x} = 8$
> 10. $5^x = \frac{1}{125}$
> 11. $\sqrt[3]{3^x} = 27$
> 12. $2^{x-1} = \frac{1}{16}$

> [!success] **Respuestas**
> 1) $x=2$  
> 2) $x=4$  
> 3) $x=5$  
> 4) $x=3$  
> 
> 5) $x=2$  
> 6) $x=7/3$ o $2.33$  
> 7) $x=7/2$ o $3.5$  
> 8) $x=2$  
> 
> 9) $x=6$  
> 10) $x=-3$  
> 11) $x=9$  
> 12) $x=-3$

---

## Mini-Prueba de Autoevaluación

> [!question] **¿Qué tanto aprendiste hoy?**
> 1. **Concepto:** Si tenemos una igualdad con bases iguales, ¿qué podemos hacer con los exponentes?
> 2. **Cálculo Rápido:** Si $2^x = 64$, ¿cuánto vale $x$ utilizando la descomposición en factores primos?
> 3. **Aplicación:** Si una inversión se duplica cada año siguiendo la ecuación $2^t = 128$, ¿en cuántos años ($t$) se llegará a ese valor?

---

## Cierre y Próximo Tema

> [!tip] **Lo que viene...**
> ¡Excelente trabajo! Hoy dominamos las bases iguales. Pero, ¿qué pasa si las bases no tienen nada que ver entre sí? En la próxima clase aprenderemos a usar los **Logaritmos**, la herramienta definitiva para resolver cualquier ecuación exponencial.

> [!info] 🧭 Navegación
> ⬅️ **Anterior:** [[Clase 02 — Potenciación y Propiedades]]
> 🏠 **Índice:** [[Curso de Álgebra Elemental]]