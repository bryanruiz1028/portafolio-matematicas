# Clase 03 — Interpretar las medidas de tendencia central y datos agrupados

#algebra #interpretarlasm

---
[ ⬅️ Atrás](leccion-02) | [🏠 Inicio](bloque-1) | [Siguiente ➡️](bloque-2)
**Bloque 1 | Lección 3 de 3**
---

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> En estadística, los números por sí solos son solo "ruido". La verdadera magia ocurre cuando aprendemos a interpretarlos; es decir, cuando entendemos qué nos dicen sobre el mundo real. 
> 
> - **💵 Aplicación $USD:** Si te dicen que el sueldo promedio en una empresa es de $1,000 USD, ¿significa que todos ganan eso? No necesariamente. Aprender a interpretar te ayuda a ver la realidad detrás del número.
> - **🏗️ Aplicación práctica:** En una fábrica, conocer que el promedio de horas trabajadas es 72 permite organizar turnos de forma humana y eficiente.
> - **📊 Situación cotidiana:** Desde saber cuántos hijos tienen las familias en tu barrio hasta entender la edad promedio de tu grupo de amigos para planear una fiesta.

## Concepto clave

> [!note] 📌 ¿Qué es Interpretar las medidas de tendencia central?
> Interpretar es "darle sentido" a la media, mediana y moda según el contexto. No se trata de repetir el número, sino de explicar qué representa para el grupo que estamos estudiando.
> 
> - **⚠️ ¡Ojo aquí! Error común:** Para la **Moda**, jamás uses la palabra "mayoría" a menos que el dato represente más del 50% del total. Lo correcto y profesional es decir: "es el dato con más frecuencia".
> - **💡 Truco para recordarlo:** 
> 	- **Media:** Es el *reparto equitativo* (lo que le tocaría a cada uno si todo fuera igual).
> 	- **Mediana:** Es el *centro* (el muro que divide al grupo en dos mitades exactas).
> 	- **Moda:** Es *lo más visto* (el valor que más veces aparece en la foto).

## Procedimiento paso a paso

Para calcular la **media ($\bar{x}$)** en datos agrupados por intervalos, utilizamos la siguiente fórmula:

$$\bar{x} = \frac{\sum (x_i \cdot f_i)}{n}$$

Sigue estos pasos para no perderte:

1.  **Encontrar la marca de clase ($x_i$):** Es el punto medio de cada intervalo. Se calcula sumando los límites y dividiendo entre dos: $x_i = \frac{L_{inferior} + L_{superior}}{2}$.
2.  **Multiplicar:** Multiplica cada marca de clase ($x_i$) por su frecuencia absoluta ($f_i$).
3.  **Sumar:** Suma todos los resultados obtenidos en el paso anterior ($\sum x_i \cdot f_i$).
4.  **Dividir:** Divide ese gran total entre el número total de datos ($n$).

## Ejemplos de aplicación

```ad-example
title: Ejemplo 1: Edades de amigos (Datos sin agrupar)
En un grupo de 9 amigos con edades: 14, 14, 15, 15, 15, 16, 17, 17, 18.
- **Media (15.6):** Si todos los amigos tuvieran la misma edad, cada uno tendría 15.6 años.
- **Mediana (15):** Exactamente el 50% de los amigos tiene 15 años o menos.
- **Moda (15):** La edad que más se repite en el grupo es 15 años.
```

```ad-example
title: Ejemplo 2: Edades en intervalos (Datos agrupados)
En un estudio a 20 personas (intervalos 13-15, 15-17, etc.):
- **Media (16.8):** El promedio de edad de este grupo es de 16.8 años.
- **Mediana (16.33):** Interpretación exacta: El 50% de las personas del grupo tiene una edad de 16.33 años o menos.
```

```ad-example
title: Ejemplo 3: El caso de los hijos (La paradoja estadística)
En un estudio de 50 familias, la **Media es 2.5 hijos**.
- **Interpretación:** ¡Nadie tiene "medio hijo"! Es un valor estadístico. Es como en el fútbol: si dicen que el promedio de goles por partido es 2.3, no significa que alguien anotó un "pedazo" de gol, sino que es el balance matemático del total de goles entre los partidos jugados.
```

```ad-example
title: Ejemplo 4: Sueldos de empresa (Aplicación real $USD)
En una empresa de 70 trabajadores:
- **Media ($1,000 USD):** El sueldo promedio de la nómina es de mil dólares.
- **Mediana ($947 USD):** La mitad de los empleados gana $947 USD o menos.
- **Moda ($950 USD):** El sueldo más frecuente entre los trabajadores es de $950 USD.
```

## Ejercicios para el estudiante

**🟢 Fácil: Número de hermanos**
En un curso de 30 estudiantes se obtuvieron estos resultados: Media 3, Mediana 2.2, Moda 2.
*   **Tarea:** Interpreta qué significa la moda en este contexto.

**🟡 Medio: Horas trabajadas**
130 empleados fueron encuestados. Media: 72.11 horas, Mediana: 72.2 horas.
*   **Tarea:** Redacta la interpretación de la mediana utilizando el concepto de porcentaje.

**🔴 Avanzado ($USD): Sueldos y honestidad de los datos**
En una empresa, el promedio (media) es de $1,000 USD, pero la mediana es de $947 USD.
*   **Tarea:** Explica qué significa que el 50% de la nómina gane $947 USD o menos y por qué la mediana suele ser más "honesta" que la media cuando hay sueldos muy altos.

```ad-success
title: Respuestas sugeridas (¡Para aprender mejor!)
- **Hermanos:** El número de hermanos más frecuente entre los alumnos es 2. No decimos "la mayoría" porque no sabemos si son más de 15 alumnos.
- **Horas:** El 50% de los empleados trabajó un tiempo menor o igual a 72.2 horas.
- **Sueldos:** Significa que la mitad de los trabajadores está por debajo de los $947 USD. La mediana es más "honesta" porque la media es **sensible a valores extremos**. Si el dueño gana muchísimo dinero, "infla" el promedio y hace parecer que todos ganan bien, mientras que la mediana se queda firme en el centro real del grupo.
```

## Mini-prueba de autoevaluación

```ad-question
title: 1. Conceptual
¿Por qué debemos evitar la palabra "mayoría" al hablar de la moda?
a) Porque la moda siempre es el número más pequeño.
b) Porque "mayoría" significa más de la mitad (>50%), y la moda solo indica cuál es el dato que más veces aparece, aunque sea poco.
c) Porque el Profe Alex dice que suena menos profesional.
```

```ad-question
title: 2. Procedimental
¿Cuál es el primer paso matemático para calcular la media en una tabla de intervalos?
a) Dividir el total de la suma entre $n$.
b) Encontrar la marca de clase ($x_i$) calculando el punto medio del intervalo: $(L_i + L_s) / 2$.
c) Multiplicar la frecuencia por 100.
```

```ad-question
title: 3. Aplicación $USD
Si el sueldo promedio ($\bar{x}$) de una empresa con 10 empleados es $1,000 USD, ¿qué información segura nos da?
a) Que todos los empleados ganan exactamente $1,000 USD.
b) Que si multiplicamos $1,000 USD por los 10 empleados, sabemos que la empresa gasta $10,000 USD en total de sueldos.
c) Que el jefe gana $1,000 USD.
```

## Notas para el próximo tema

> [!tip] 💡 En la próxima clase
> Ya sabemos encontrar el "centro" de los datos y darle sentido. Pero, ¿qué tan lejos están los datos de ese centro? ¿Están todos cerca o muy dispersos? Prepárate, porque entraremos a las **Medidas de Dispersión**.

---
[ ⬅️ Atrás](leccion-02) | [🏠 Inicio](bloque-1) | [Siguiente ➡️](bloque-2)
**Bloque 1 | Lección 3 de 3**
---