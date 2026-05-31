# Clase 01 — Sistema Sexagesimal: Fundamentos y Conversiones de Forma
tags: #algebra #sistemasexagesimal
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 2

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]

## 1. ¿Por qué es importante esta clase?

¡Bienvenido al estudio del tiempo y el espacio! El **sistema sexagesimal** es la base sobre la que medimos nuestra vida diaria. Su origen se remonta a la antigua Mesopotamia, donde los sumerios idearon un método de conteo táctil: usaban el pulgar para contar las **12 falanges** de los otros cuatro dedos de una mano. Al completar una mano, levantaban un dedo de la otra (5 dedos en total). Así, 12 falanges × 5 dedos nos da el número **60**.

Los sumerios eligieron el 60 porque es un **"número redondo"** extremadamente versátil. A diferencia del 10, el 60 es divisible por 1, 2, 3, 4, 5, 6, 10, 12, 15, 20 y 30. Esto facilita enormemente las fracciones (la mitad, un tercio, un cuarto, etc.).

**¿Dónde lo aplicamos hoy?**
*   **Economía Digital ($USD):** Los servicios de telefonía satelital, publicidad en radio o el tiempo de renderizado en la nube se cobran por segundo. Un error de conversión puede afectar seriamente un presupuesto.
*   **Navegación y GPS:** Para localizar un punto exacto en el planeta, usamos grados, minutos y segundos de latitud y longitud.
*   **Vida Cotidiana:** Desde leer un cronómetro hasta calcular cuánto falta para que termine tu clase favorita.

---

## 2. Concepto clave

> [!note] 📌 ¿Qué es Sistema Sexagesimal?
> Es un sistema de numeración cuya base es el **60**. Mientras que en nuestro sistema decimal (base 10) agrupamos de diez en diez, aquí necesitamos **60 unidades** para formar una unidad superior. Es fundamental reconocer sus símbolos técnicos:
> 
> | Unidad | Símbolo (Ángulos) | Símbolo (Tiempo) |
> | :--- | :---: | :---: |
> | Grados / Horas | **°** | **h** |
> | Minutos | **'** | **min** |
> | Segundos | **''** | **s** |

> [!warning] ⚠️ Error común: El falso decimal
> Muchos estudiantes creen que **13,5°** es igual a **13° 50'**. ¡Esto es un error! 
> En el sistema decimal, el ",5" representa la mitad de 10. Pero en el sexagesimal, la base es 60; por lo tanto, la mitad es 30. 
> **Correcto:** 13,5° = 13° y medio grado = **13° 30'**.

> [!tip] 💡 Truco para recordarlo (La Escalera)
> Para convertir unidades sin fallar, imagina una escalera:
> *   **Bajar = Multiplicar:** Si pasas de una unidad grande a una pequeña (ej. de horas a minutos), multiplicas por 60.
> *   **Subir = Dividir:** Si pasas de una unidad pequeña a una grande (ej. de segundos a minutos), divides entre 60.

---

## 3. Procedimiento paso a paso

Para realizar conversiones técnicas, utiliza el siguiente flujo de trabajo:

```text
FLUJO DE CONVERSIÓN TÉCNICA

PASO 1 → Identificar dirección: ¿Subir (Dividir) o Bajar (Multiplicar)?
PASO 2 → Si bajas un escalón: Valor × 60.
PASO 3 → Si subes un escalón: Valor ÷ 60.
PASO 4 → Para saltos dobles (ej. Grados a Segundos): Multiplicar o dividir 
         por 3600 (resultado de 60 × 60).
```

---

## 4. Ejemplos de Aplicación

> [!example] Ejemplo 1: De forma incompleja a compleja (Básico)
> **Convertir 320 s a minutos y segundos.**
> 1. Como vamos a subir de segundos a minutos, dividimos: `320 ÷ 60`.
> 2. El 60 cabe **5** veces en 320 (5 × 60 = 300).
> 3. El residuo es **20**.
> **Resultado:** 5 min 20 s (o 5' 20'').

> [!example] Ejemplo 2: De decimal a forma compleja
> **Convertir 13,5° a forma compleja.**
> 1. La parte entera ya son grados: **13°**.
> 2. La parte decimal (**0,5**) la bajamos a minutos multiplicando: `0,5 × 60 = 30,0`.
> **Resultado:** 13° 30'.

> [!example] Ejemplo 3: De forma compleja a incompleja (Avanzado)
> **Convertir 10° 16' 12'' a grados decimales.**
> 1. Mantenemos los **10°**.
> 2. Subimos los **16'**: `16 ÷ 60 = 0,266...°`.
> 3. Subimos los **12''**: `12 ÷ 3600 = 0,0033...°`.
> 4. Sumamos: `10 + 0,266... + 0,0033... = 10,269...`.
> **Resultado:** Aproximadamente 10,27°.

> [!example] Ejemplo 4: Aplicación económica ($USD)
> **Problema:** El costo de una llamada es de **$0,60 USD por min**. Si la llamada dura **5 min 30 s**, ¿cuánto se debe pagar?
> 1. Convertimos los 30 s a minutos: `30 ÷ 60 = 0,5 min`.
> 2. Tiempo total: `5 + 0,5 = 5,5 min`.
> 3. Costo: `5,5 × 0,60 = 3,30`.
> **Resultado:** El costo es $3,30 USD.

---

## 5. Ejercicios para el estudiante

> [!abstract] 🟢 Nivel Verde (Fácil)
> 1. Convierte 180 min a horas.
> 2. Convierte 5 min a segundos (s).
> 3. ¿Cuántos minutos (') hay en 3°?
> 4. Convierte 3600 s a horas.

> [!abstract] 🟡 Nivel Amarillo (Medio)
> 1. Expresa 45,225° en forma compleja (grados, minutos y segundos).
> 2. Convierte 5000 s a forma compleja.
> 3. Expresa 148,2 min en forma compleja (grados, minutos y segundos).
> 4. Convierte 0,75 min a segundos (s).

> [!abstract] 🔴 Nivel Rojo (Avanzado)
> 1. Un satélite cobra **$0,02 USD por segundo** de transmisión. Si una señal dura **10 min 15 s**, ¿cuál es el costo total?
> 2. Un estacionamiento cobra **$1,50 USD por hora**. Si el tiempo de uso fue **2 h 45 min**, ¿cuál es el costo total en formato decimal de horas?
> 3. Un espacio publicitario cuesta **$45,00 USD por minuto**. ¿Cuánto cuesta un anuncio que dura exactamente **45 s**?
> 4. El roaming de datos cuesta **$0,05 USD por segundo**. ¿Cuál es el costo de una videollamada que dura **12 min 10 s**?

> [!success] Solucionario (Para el docente)
> **Verde:** 1) 3 h | 2) 300 s | 3) 180' | 4) 1 h.
> **Amarillo:** 1) 45° 13' 30'' | 2) 1 h 23' 20'' | 3) 2° 28' 12'' | 4) 45 s.
> **Rojo:** 
> 1) 615 s × $0,02 = $12,30 USD.
> 2) 2,75 h × $1,50 = $4,125 (aprox. $4,13 USD).
> 3) 0,75 min × $45,00 = $33,75 USD.
> 4) 730 s × $0,05 = $36,50 USD.

---

## 6. Mini-prueba de autoevaluación

> [!question] Pregunta 1
> ¿Cuál es el origen histórico de la base 60?
> A) El número de días del calendario lunar.
> B) El conteo de 12 falanges con el pulgar multiplicado por 5 dedos.
> C) La división de la tierra en 60 continentes.
> D) La cantidad de segundos que tiene un día.

> [!question] Pregunta 2
> ¿Cuál de estas opciones representa una forma "incompleja"?
> A) 2 h 15 min.
> B) 45° 10' 05''.
> C) 3600,5 s.
> D) 1 h y 30 s.

> [!question] Pregunta 3
> Si una plataforma de streaming cobra **$0,10 USD** por cada minuto de video, ¿cuánto costará ver un video de **120 s**?
> A) $0,10 USD.
> B) $0,20 USD.
> C) $1,20 USD.
> D) $12,00 USD.

---

## 7. Notas para el próximo tema

> [!tip] 💡 En la próxima clase
> Dominar las conversiones es el primer paso. En la **Clase 02**, aprenderemos a realizar operaciones de **Suma y Resta** directamente con grados, minutos y segundos sin necesidad de pasar todo a decimal. ¡Prepárate para operar con la precisión de un sumerio!

> [!info] 🧭 Navegación
> [[00 - Índice del curso|Índice]] | **Clase 01** | | [[Clase 02|Clase 02 ➡]]