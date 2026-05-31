# 📋 Planificación Didáctica: ¡El Arte de Contar y la Magia del Azar!

¡Hola, colegas! Esta planificación está diseñada para despertar la curiosidad de nuestros estudiantes de secundaria (12-15 años). Vamos a transformar el álgebra de las combinaciones en una aventura práctica, utilizando los métodos visuales y cercanos que tanto éxito le dan al "Profe Alex". ¡Prepárense para que sus alumnos vean la matemática como un superpoder para entender el mundo!

---

## 1. Temas Principales
*   **Experimento Aleatorio:** ¿Qué es el azar y cuándo podemos predecirlo?
*   **Espacio Muestral y Eventos:** El mapa de todas las posibilidades.
*   **Principio Fundamental del Conteo (Multiplicación):** El "atajo" maestro para contar sin morir en el intento.

---

## 2. Metodología: Aprendizaje Colaborativo Formal
Trabajaremos bajo el **Aprendizaje Colaborativo Formal**. Organizaremos a los chicos en equipos de 3 o 4 exploradores. Mi rol como docente será el de un facilitador que lanza retos. La pregunta clave que rondará todo el salón será: **"¿Importa el orden o no importa?"**. Si aprenden a responder eso, ¡ya tienen medio camino ganado!

---

## 3. Secuencia Didáctica

### 🔵 ANTICIPACIÓN — 20 min

> [!abstract] Actividad de inicio: ¡El Sueño de la Lotería!
> 1. **El Reto:** Empezamos con una pregunta directa: "Si para ganar la lotería deben elegir 6 números entre el 1 y el 49, ¿es lo mismo marcar el `5, 8, 20` que el `20, 5, 8`?". 
> 2. **Conceptos en acción:** 
>    - **Experimento aleatorio:** No sabemos qué números saldrán.
>    - **Orden:** Como vimos con el "Profe Alex", si marcas los mismos números en diferente orden, la apuesta es la misma. ¡No importa el orden, es una **combinación**!
> 3. **El dato asombroso:** Les revelamos el tamaño del **Espacio Muestral**. Hay **13,983,816** formas de llenar ese boleto. ¡Tendrías que comprar casi 14 millones de cartones para asegurar el premio!

> [!tip] Experimento Manual (Manos a la obra)
> Antes de los millones, usemos algo real. Cada grupo lanzará una **moneda** y un **dado** al mismo tiempo.
> - **Reto:** Dibujen el Espacio Muestral. (Ej: Cara-1, Cara-2... Sello-6).
> - **Pregunta:** ¿Cuántos resultados hay? Son 2 (moneda) × 6 (dado) = **12 resultados**. ¡Acaban de usar el principio de multiplicación sin darse cuenta!

> [!note] Enfoque DUA
> - **Qué:** Activación de conocimientos previos mediante el juego y la curiosidad.
> - **Cómo:** Discusión dirigida sobre sus propios juegos de azar (bingo, cartas, etc.).
> - **Por qué:** Captamos el interés con un ejemplo emocional y real (ganar dinero/lotería).

---

### 🟡 CONSTRUCCIÓN — 40 min

> [!example] Actividades Centrales: El Método de las "Cajitas"
> Vamos a modelar los ejemplos del Profe Alex usando visuales claros:
> 
> 1. **Caso Gaseosas (Principio de Multiplicación):** 
>    Si en la tienda hay 6 sabores y queremos elegir 3 gaseosas (y podemos repetir sabor porque nos encanta la de uva), el espacio muestral se calcula dibujando cajitas:
>    `[ 6 ] × [ 6 ] × [ 6 ] = 216 opciones.`
> 
> 2. **El Reto de los Libros (Combinaciones Compuestas):** 
>    Tenemos 6 libros de matemáticas y 3 de física. Queremos elegir 2 de cada uno.
>    - **Paso 1 (Mates):** $C(6,2) = 15$ formas.
>    - **Paso 2 (Física):** $C(3,2) = 3$ formas.
>    - **Resultado final:** $15 \times 3 =$ **45 formas diferentes**. (Usamos colores: marcadores rojos para mates y azules para física).
> 
> 3. **La Gran Comisión:**
>    Elegir 5 hombres (de 12) **y** 5 mujeres (de 10).
>    - $C(12,5) \times C(10,5) = 792 \times 252 =$ **199,584 combinaciones**.

> [!important] Técnica Profe Alex: "Desmenuzar" Factoriales
> Para que no sufran con la calculadora, enseñamos a **desmenuzar** el factorial:
> *"Si tienes $12! / (5! \times 7!)$, desmenuza el 12 hasta llegar al 7: $12 \times 11 \times 10 \times 9 \times 8 \times 7!$. Ahora, 'macheteamos' (cancelamos) el $7!$ arriba y abajo. ¡Mucho más fácil!"*

> [!note] Enfoque DUA
> - **Qué:** Aplicación del principio multiplicativo con apoyo visual.
> - **Cómo:** Uso de "cajitas" en la pizarra y fichas impresas para trabajar en parejas.
> - **Por qué:** El método visual reduce la ansiedad matemática y facilita entender cómo se expanden las opciones.

---

### 🟢 CONSOLIDACIÓN — 20 min

> [!success] Actividad de Cierre: El Misterio de las Placas
> Planteamos un duelo de lógica civil:
> 1. **Situación A (Sin Repetición):** ¿Cuántas placas de 3 letras y 3 números existen si **no** se pueden repetir caracteres?
>    `[ 26 ] [ 25 ] [ 24 ] × [ 10 ] [ 9 ] [ 8 ]`
> 2. **Situación B (Con Repetición):** ¿Cuántas existen si **sí** podemos repetir (como en la vida real)?
>    `[ 26 ] [ 26 ] [ 26 ] × [ 10 ] [ 10 ] [ 10 ] =` **17,576,000 placas.**
> 
> **Reto Extra:** Si hay 16 equipos de fútbol en un torneo "todos contra todos" (un solo partido), ¿cuántos partidos se juegan?
> - **Razonamiento:** Es una combinación $C(16,2)$ porque el partido Equipo A vs Equipo B es el mismo que B vs A.
> - **Resultado:** **120 partidos.**

> [!note] Enfoque DUA
> - **Qué:** Evaluación formativa mediante transferencia a contextos civiles y deportivos.
> - **Cómo:** Socialización en la pizarra. Cada grupo explica si el orden importó en su análisis.
> - **Por qué:** Refuerza la utilidad práctica de la estadística en la organización de la sociedad.

---

## 4. Recursos Didácticos

| Recurso | Tipo | Uso Pedagógico |
| :--- | :--- | :--- |
| **Pizarra y Marcadores** | Físico | Dibujar las "cajitas" y aplicar el "macheteo" de factoriales con colores. |
| **Fichas de Ejercicios** | Impreso | Guía paso a paso con los casos de Alex (Libros, Gaseosas, Comisiones). |
| **Dados y Monedas** | Físico | **Actividad inicial:** Lanzar para construir físicamente un espacio muestral simple. |
| **Impresora** | Físico | Preparar el material para que cada grupo tenga su "hoja de ruta". |