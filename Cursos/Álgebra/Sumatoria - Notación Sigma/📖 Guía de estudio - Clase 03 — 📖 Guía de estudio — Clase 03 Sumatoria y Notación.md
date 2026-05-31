# 📖 Guía de estudio — Clase 03: Sumatoria y Notación Sigma

> [!info] 📌 Conceptos clave
> La **notación sigma ($\sum$)** es una herramienta matemática que nos permite escribir sumas muy largas de forma abreviada y elegante. Para aplicar las fórmulas de esta guía con éxito, recuerda siempre estos puntos fundamentales:
> 
> 1. **El punto de partida:** Las fórmulas estándar funcionan cuando el límite inferior es **1** (es decir, la suma empieza en el primer término).
> 2. **Separación de términos:** Si tienes una suma o resta dentro de la sumatoria, puedes romperla en varias sumatorias individuales para resolverlas por separado.
> 3. **Extracción de constantes:** Si un número está multiplicando a la variable (por ejemplo, $2i$), ese número puede "salir" de la sumatoria y multiplicar al resultado final. ¡Esto facilita mucho el trabajo!

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Suma de una constante ($c$)** | Se multiplica el límite superior ($n$) por el valor de la constante: $\sum_{i=1}^{n} c = n \times c$ |
| **Suma de números naturales ($i$)** | El número final multiplicado por su sucesor, dividido entre dos: $\frac{n(n+1)}{2}$ |
| **Suma de cuadrados ($i^2$)** | Se multiplica el número, por el siguiente, por la suma de ambos, todo sobre seis: $\frac{n(n+1)(2n+1)}{6}$ <br> *(Pista: El tercer número es la suma de los dos anteriores)* |
| **Suma de cubos ($i^3$)** | Es exactamente la fórmula de los naturales, pero elevada al cuadrado: $\left[\frac{n(n+1)}{2}\right]^2$ |

---

## Ejemplos Resueltos Adicionales

````ad-example title: Ejemplo A — Propiedad Lineal y Constante
**Enunciado:** Calcular la sumatoria $\sum_{i=1}^{50} (2i - 5)$

**Proceso paso a paso:**

1. **Paso 0 — Identificación:** Observamos que el límite superior es $n=50$. Tenemos una variable $i$ multiplicada por la constante $2$, y una constante restando $5$.
2. **Separar los términos y extraer constantes:** Aplicamos las propiedades de linealidad.
   $2 \left( \sum_{i=1}^{50} i \right) - \sum_{i=1}^{50} 5$
3. **Aplicar fórmulas y simplificar:** 
   - Para la variable $i$: Aplicamos $\frac{50 \times 51}{2}$. 
     *Simplificación:* Antes de multiplicar $50 \times 51$, dividimos $50 \div 2 = 25$. 
     Ahora calculamos: $25 \times 51 = 1275$.
   - Para la constante $5$: Multiplicamos $n \times c$, es decir, $50 \times 5 = 250$.
4. **Sustituir y resolver:**
   $2(1275) - 250$
   $2550 - 250$

**Resultado final:** 2300
````

````ad-example title: Ejemplo B — Ahorro acumulado (Aplicación con $USD)
**Enunciado:** Una persona decide ahorrar una cantidad fija de $10 USD diarios durante 40 días. ¿Cuál es el total del ahorro acumulado?

**Representación matemática:**
$\sum_{i=1}^{40} 10$

**Proceso:**
1. **Paso 0:** Identificamos que $n=40$ (días) y la constante $c=10$ (dólares).
2. Al ser una suma de una constante, aplicamos la fórmula directa $n \times c$.
3. Multiplicamos: $40 \times 10 = 400$.

**Resultado final:** El ahorro total es de **$400 USD**.
````

---

## Ejercicios de Repaso

````ad-abstract title: 🟢 Fácil
Resuelve las siguientes sumatorias aplicando la separación y las fórmulas de naturales y constantes:
1. $\sum_{i=1}^{100} 5i$
2. $\sum_{i=1}^{100} 2$
3. $\sum_{i=1}^{100} (5i + 2)$
````

````ad-abstract title: 🟡 Medio
Practica con potencias cuadradas y simplificación de fracciones:
1. $\sum_{i=1}^{200} i^2$ *(Recuerda la pista del tercer término en el numerador)*
2. $\sum_{i=1}^{200} 5i$
3. $\sum_{i=1}^{200} (2i^2 - 5i)$
````

````ad-abstract title: 🔴 Avanzado — Aplicación con $USD
**Reto de Bonificación:** Una empresa calcula el bono navideño de sus empleados con la siguiente fórmula: $\sum_{i=1}^{20} (i^3 - 2i^2 + 3i)$.

**Instrucciones:**
- Calcula el valor numérico total de la sumatoria.
- **Tip del Profe:** Para el término $i^3$, primero calcula la suma natural ($n(n+1)/2$) y luego eleva ese resultado al cuadrado.
- Si cada unidad del resultado equivale a **$1 USD**, ¿cuánto dinero recibirá el empleado?
````

---

> [!tip] 💡 Consejo de estudio
> Como siempre les digo en clase: **¡Simplifiquen antes de multiplicar!** Si tienen un denominador (como el 2 o el 6), busquen qué número de arriba tiene mitad o tercera. Es mucho más fácil y seguro multiplicar $25 \times 51$ que multiplicar $50 \times 51$ y luego tener que dividir un número gigante entre 2. ¡Eviten errores innecesarios trabajando con números más pequeños!