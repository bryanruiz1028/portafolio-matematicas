# 📖 Guía de estudio — Clase 05: Multiplicación de radicales de igual índice

> [!info] 📌 Conceptos clave
> Para dominar la multiplicación de radicales, es fundamental comprender estos cinco pilares basados en el material del Profe Alex:
> *   **Condición obligatoria:** Solo podemos multiplicar raíces si tienen el **mismo índice** (ej. ambas raíces cuadradas o ambas raíces cúbicas). Si son diferentes, no se pueden unir directamente.
> *   **Unión de factores:** Cuando los índices coinciden, abrimos una sola "raíz grande" (la cárcel común) y metemos todos los factores dentro multiplicándose.
> *   **Bases iguales:** Al multiplicar letras o números iguales dentro de la raíz (como $x^2 \cdot x^5$), mantenemos la base y **sumamos los exponentes**.
> *   **Regla de simplificación:** Si un exponente es mayor al índice, debemos **descomponerlo** en grupos que igualen al índice para que puedan "salir" de la raíz.
> *   **Manejo de coeficientes:** Los números que ya están fuera de la raíz se multiplican entre sí de forma independiente a lo que ocurre dentro del radical.

## Tabla de Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Índice** | El número pequeño que indica el tipo de raíz y dicta la "condena" para salir. |
| **Radicando** | La cantidad o expresión que se encuentra dentro de la raíz (cantidad subradical). |
| **Propiedad de Producto** | $\sqrt[n]{a} \cdot \sqrt[n]{b} = \sqrt[n]{a \cdot b}$ |

---

```ad-example
title: Ejemplo A — Caso con variables
**Problema:** Calcular el producto de $\sqrt[3]{x^2} \cdot \sqrt[3]{x^5}$

1. **Unión en una sola raíz:** Como ambos índices son 3 (condenas iguales), unimos todo en una sola cárcel: $\sqrt[3]{x^2 \cdot x^5}$.
2. **Suma de exponentes:** Aplicamos la propiedad de potencias: $x^{2+5} = x^7$. Ahora tenemos a un preso con 7 años acumulados: $\sqrt[3]{x^7}$.
3. **Descomposición (La Técnica del Preso):** El índice es 3, así que para salir se necesitan grupos de 3 años. Separamos los 7 años en "tríos" de condena cumplida: $\sqrt[3]{x^3 \cdot x^3 \cdot x^1}$.
4. **Resultado final (¡A la libertad!):** 
   - Los dos presos que ya cumplieron sus condenas de 3 años obtienen su boleta de libertad y salen de la raíz. 
   - Afuera, los presos libres se reúnen y se multiplican ($x \cdot x = x^2$).
   - El preso que solo tiene 1 año no puede salir y se queda adentro.
   
   $$\text{Resultado: } x^2 \sqrt[3]{x}$$
```

---

```ad-example
title: Ejemplo B — Aplicación económica ($USD)
**Contexto:** Un arquitecto diseña una oficina rectangular cuyo largo mide $\sqrt{12}$ metros y su ancho $\sqrt{6}$ metros. Si el costo por metro cuadrado está expresado por esta operación, ¿cuál es el valor final en dólares ($USD)?

1. **Planteamiento:** Multiplicamos las dimensiones para obtener el área: $\sqrt{12} \cdot \sqrt{6}$.
2. **Unión de factores:** Como son raíces cuadradas (índice 2), unimos: $\sqrt{12 \cdot 6}$.
3. **Descomposición en factores primos:** En lugar de multiplicar y obtener 72, descomponemos cada número para ver quién puede salir de la cárcel:
   - El 12 se convierte en $2^2 \cdot 3$.
   - El 6 se convierte en $2 \cdot 3$.
   - Al unirlos todos dentro de la raíz tenemos: $\sqrt{2^2 \cdot 3 \cdot 2 \cdot 3}$.
   - Agrupamos para que los exponentes coincidan con el índice 2: $\sqrt{2^2 \cdot 3^2 \cdot 2}$.
4. **Simplificación final:** El $2$ y el $3$ cumplieron su condena (exponente 2) y salen a multiplicarse afuera. El último $2$ se queda encerrado.
   - Afuera: $2 \cdot 3 = 6$.
   
   $$\text{Resultado: } 6\sqrt{2} \text{ USD}$$
```

---

## Ejercicios de Repaso

```ad-abstract
title: 🟢 Nivel: Verde (Fácil)
Resuelve las siguientes multiplicaciones uniendo los factores en una sola raíz:
1. $\sqrt[5]{a^2} \cdot \sqrt[5]{a^3}$
2. $\sqrt[3]{x} \cdot \sqrt[3]{x^5}$
3. $\sqrt[4]{b^2} \cdot \sqrt[4]{b^6}$
```

```ad-abstract
title: 🟡 Nivel: Amarillo (Medio)
Multiplica los radicales. Recuerda multiplicar los coeficientes de afuera y descomponer los números internos:
1. $3\sqrt{15} \cdot 2\sqrt{50}$
2. $5\sqrt[3]{12} \cdot 2\sqrt[3]{18}$
3. $2\sqrt{18} \cdot \sqrt{2}$
```

```ad-abstract
title: 🔴 Nivel: Avanzado (Desafío Económico)
Aplica lo aprendido en estos contextos de finanzas digitales ($USD):
1. **Activos Digitales:** El valor de un token de criptomoneda se calcula multiplicando dos índices de mercado: $2\sqrt[3]{16}$ y $4\sqrt[3]{4}$. ¿Cuál es el valor total en USD tras simplificar la raíz?
2. **Presupuesto de Red:** El costo de mantenimiento de un servidor está dado por el producto $\sqrt[4]{32} \cdot \sqrt[4]{8}$ USD. Calcula el valor exacto simplificando al máximo.
```

---

> [!tip] 💡 Consejo de estudio: La Analogía de la Cárcel
> ¡No lo olvides! La raíz es una **cárcel** y el **índice** es el precio de la libertad (los años de condena). 
> 1. Si el índice es **4**, un número solo puede salir si tiene un exponente **4**. 
> 2. Si un preso tiene exponente **9**, puede pagar **dos condenas de 4 años** y salir como un "preso al cuadrado" ($x^2$), pero un año se queda adentro porque no le alcanzó para la tercera condena. 
> 3. ¡Los que salen siempre se multiplican con los que ya estaban afuera!