# 📖 Guía de estudio — Clase 02: Principio Fundamental del Conteo - Regla de la Multiplicación

¡Qué tal amigos! Espero que estén muy bien. Hoy vamos a profundizar en una herramienta que me encanta por su sencillez y utilidad: el Principio Fundamental del Conteo. ¡Pilas aquí!, porque entender esto es la base para dominar toda la combinatoria.

> [!info] 📌 Conceptos clave
> * **Definición:** El principio de multiplicación se aplica cuando dos o más eventos ocurren de manera simultánea (a la vez) o sucesiva (uno tras otro).
> * **La regla del "Y" frente a la "O":** ¡Ojo con esto! Si para lograr un objetivo debes realizar la acción A **y** la acción B, los resultados se multiplican. Pero si debes elegir entre A **o** B (como cuando decides ir al colegio en bicicleta, bus o caminando), las opciones se suman porque son excluyentes.
> * **Eventos simultáneos vs. excluyentes:** Es vital identificar si los eventos ocurren al mismo tiempo o si elegir una opción te impide tomar la otra.
> * **Objetivo del conteo:** Queremos hallar el número total de formas posibles de un suceso de manera rápida, ¡sin tener que escribir cada una de las combinaciones!

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Principio de Multiplicación** | Si un evento ocurre de $m$ formas y otro de $n$ formas, ambos ocurren de $m \times n$ formas (Conector "y"). |
| **Evento** | Es cualquier acción o suceso con resultados posibles (ej. lanzar un dado o elegir un color). |
| **Opciones Excluyentes** | Cuando los eventos no pueden ocurrir juntos. Se usa el principio de la suma ($m + n$) porque eliges una opción **o** la otra. |

---

## Ejemplos resueltos adicionales

````ad-example
title: Ejemplo A — Combinando mi ropa
**Enunciado:** Imagina que tienes 3 pantalones de diferentes colores (azul, claro y negro) y 4 camisas (blanca, azul, negra y roja). ¿De cuántas formas diferentes puedes vestirte?

**Paso 1: Identificar el conector.** Este es un caso clásico de eventos simultáneos porque, para salir a la calle, ¡debes ponerte el pantalón **y** la camisa al mismo tiempo! Como usamos el conector "y", aplicamos la multiplicación.

**Paso 2: Aplicar la operación.** 
- Opciones de pantalón: 3
- Opciones de camisa: 4
- Operación: $3 \times 4 = 12$

**Resultado:** ¡Viste qué fácil! Puedes vestirte de **12 formas diferentes**. ✅
````

````ad-example
title: Ejemplo B — Seguridad de mi Billetera Digital
**Enunciado:** Para proteger tu saldo en **$USD**, una billetera digital te pide crear un código de seguridad de 3 letras seguidas de 2 números (dígitos del 0 al 9). ¿Cuántas combinaciones posibles existen para proteger tu dinero? (Usa el alfabeto de 26 letras).

**Paso 1: Dibujar las decisiones (cajitas).** Cada espacio es una decisión que debemos tomar para completar el código:
`[_] [_] [_]` (Letras) y `[_] [_]` (Números).

**Paso 2: Asignar opciones por espacio.**
- Para cada cajita de letra, tienes **26** opciones.
- Para cada cajita de número, tienes **10** opciones (0 al 9).

**Paso 3: Multiplicar.**
$26 \times 26 \times 26 \times 10 \times 10$
$17,576 \times 100 = 1,757,600$

**Resultado:** Existen **1,757,600 combinaciones** posibles para asegurar tus **$USD**. ¡Un código muy seguro! ✅
````

---

## Ejercicios de repaso

````ad-abstract
title: 🟢 Dificultad: Fácil (Monedas y Dados)
1. Lanzas una moneda y un dado de 6 caras. ¿Cuántos resultados diferentes pueden obtenerse?
2. Si lanzas dos dados de 6 caras al mismo tiempo, ¿de cuántas formas diferentes pueden caer?
3. Si lanzas una moneda y dos dados, ¿cuál es el número total de combinaciones posibles? (¡Pilas con las tres cajitas!).
````

````ad-abstract
title: 🟡 Dificultad: Medio (Placas y Claves)
1. Una placa de vehículo se forma con 2 letras y 1 dígito. ¿Cuántas placas diferentes se pueden crear? (Usa 26 letras y 10 dígitos).
2. Se desea crear una clave de acceso de 3 letras seguidas de 3 dígitos. ¿Cuántas claves distintas son posibles?
3. ¿Cuántas claves de 4 letras se pueden diseñar si las letras se pueden repetir? (Recuerda que si se pueden repetir, siempre tienes 26 opciones).
````

````ad-abstract
title: 🔴 Dificultad: Avanzado (Aplicación con $USD)
1. Un combo de almuerzo cuesta **$10 USD** y permite elegir entre 4 platos fuertes, 3 bebidas y 2 postres. ¿De cuántas formas diferentes puedes gastar tus **$USD**?
2. Una tienda ofrece un "Combo Tecnológico" por un precio fijo. Puedes elegir entre 2 modelos de laptop, 5 tipos de mouse y 3 maletines. ¿Cuántas combinaciones de combos existen?
3. En una agencia de viajes, un paquete de **$500 USD** se arma eligiendo 1 destino entre 3 opciones, 1 hotel entre 2 opciones y 1 tour guiado entre 4 opciones. ¿De cuántas formas puedes planificar tu viaje?
````

---

> [!tip] 💡 Consejo de estudio
> ¡No te compliques! Utiliza siempre mi técnica original de las **"cajitas"**. Dibuja un espacio por cada decisión que debas tomar y llena cada uno con el número de opciones disponibles antes de multiplicar. Esta es una **táctica universal**; apréndela bien porque también la usaremos en las próximas clases para resolver Permutaciones y Variaciones. ¡Pilas con eso!