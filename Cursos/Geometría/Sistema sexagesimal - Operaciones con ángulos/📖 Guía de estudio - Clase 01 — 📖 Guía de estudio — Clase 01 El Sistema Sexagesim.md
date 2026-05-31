# 📖 Guía de estudio — Clase 01: El Sistema Sexagesimal

¡Qué tal amigas y amigos! Espero que estén muy bien. Bienvenidos a esta guía sobre el sistema sexagesimal. Aquí aprenderemos a manejar el tiempo y los ángulos como expertos, siguiendo los consejos del Profe Alex. ¡Vamos a darle!

> [!info] 📌 Conceptos clave
> El sistema sexagesimal es un sistema de numeración posicional que tiene como **base el número 60**. Aquí tienes lo esencial:
> 
> 1. **Origen histórico:** Nació en la antigua Mesopotamia con la civilización sumeria. Ellos no usaban calculadoras, ¡usaban las manos! Contaban las 12 falanges de los dedos de una mano (usando el pulgar como guía) y, cada vez que llegaban a 12, levantaban un dedo de la otra mano. Como la otra mano tiene 5 dedos, $12 \times 5 = 60$.
> 2. **¿Por qué el 60?** Se consideraba un número "redondo" porque era el límite máximo que podían contabilizar con las manos de forma estructurada antes de reiniciar la cuenta.
> 3. **Aplicaciones:** Lo usamos hoy para medir el **tiempo** (horas, minutos, segundos) y los **ángulos** (grados, minutos, segundos). ¡Ojo! Matemáticamente se trabajan igual.
> 4. **Formas de expresión:**
>    - **Forma Compleja:** Cuando usas varias unidades a la vez (ej. $1h\ 30min$ o $16^\circ\ 10'\ 12''$).
>    - **Forma Incompleja:** Cuando usas una sola unidad para todo (ej. $90\ min$ o $16.166^\circ$).
> 5. **La Regla de Oro:** Para convertir unidades, recuerda siempre la escalera: **"Bajar nivel multiplica, subir nivel divide"**.

## Fórmulas y definiciones importantes

> [!warning] ⚠️ ¡No metas la pata! (Aviso del Profe Alex)
> En matemáticas, los símbolos son sagrados. 
> - **Segundos:** se escribe **s**, nunca "sec" ni "sg".
> - **Minutos:** se escribe **min**, nunca "mn" ni "mt".
> - **Horas:** se escribe **h**, nunca "hor" ni "hrs".

| Término | Símbolos | Definición / Equivalencia |
| :--- | :--- | :--- |
| **Grado / Hora** | $^\circ$ / $h$ | Unidad mayor. $1^\circ$ o $1h = 60\ min = 3600\ s$. |
| **Minuto** | $'$ / $min$ | Unidad intermedia. $1' = 60''$. Para subir a grado/hora, **divide entre 60**. |
| **Segundo** | $''$ / $s$ | Unidad menor. Para subir a grado/hora, **divide entre 3600**. |

---

## La Escalera Sexagesimal
Visualiza siempre este camino para no perderte:
1. **Grados / Horas**
   * (Bajar $\downarrow$ Multiplicar por 60)
2. **Minutos**
   * (Bajar $\downarrow$ Multiplicar por 60)
3. **Segundos**

*¿Quieres subir?* De Segundos a Minutos $\rightarrow$ **Divide entre 60**. De Minutos a Grados $\rightarrow$ **Divide entre 60**.

---

## Ejemplos resueltos paso a paso

> [!example] Ejemplo A — De Compleja a Incompleja (Ángulos)
> **Ejercicio:** Convertir **$16^\circ$ y $10'$** a solo grados (forma incompleja).
> - **Paso 1:** Los $16^\circ$ ya están en la unidad que queremos, los dejamos quietos.
> - **Paso 2:** Convertimos los $10'$ a grados. Como vamos a **subir** un escalón, dividimos:
>   $10 \div 60 = 0.1666...$ (Es un decimal periódico).
> - **Paso 3:** Sumamos los resultados: $16^\circ + 0.1666...^\circ = 16.166...^\circ$.
> 
> ✅ **Resultado:** $16.166^\circ$ (aproximadamente).

> [!example] Ejemplo B — Aplicación de Costos
> **Enunciado:** Una hora de asesoría cuesta $60 USD. ¿Cuánto cuesta una sesión de **1 hora y 15 minutos**?
> - **Paso 1:** Pasamos todo a horas (forma incompleja). Los $15\ min$ se suben dividiendo entre 60:
>   $15 \div 60 = 0.25\ h$.
> - **Paso 2:** Sumamos: $1\ h + 0.25\ h = 1.25\ h$.
> - **Paso 3:** Multiplicamos el total de horas por el precio: $1.25 \times 60 = 75$.
> 
> ✅ **Resultado:** $75 USD.

---

## Ejercicios de repaso

> [!abstract] 🟢 Fácil — ¡Para calentar motores!
> 1. Convierte $5\ h$ a minutos. (Pista: Vas a bajar, ¡multiplica!).
> 2. Convierte $120\ s$ a minutos. (Pista: Vas a subir, ¡divide!).
> 3. ¿La expresión "$2h\ 45min$" es forma compleja o incompleja?

> [!abstract] 🟡 Medio — ¡Tú puedes con esto!
> 1. Pasa **$13.5^\circ$** a forma compleja. (Separa la parte entera de la decimal y multiplica el decimal por 60).
> 2. Convierte **$5000\ s$** a forma compleja (Grados, Minutos, Segundos) usando **divisiones sucesivas**.
>    * *Nota:* Divide 5000 entre 60; el residuo son los segundos. Luego toma el cociente y divídelo otra vez entre 60; ese residuo serán los minutos y el nuevo cociente los grados.
> 3. Convierte **$10^\circ\ 16'\ 12''$** totalmente a segundos.

> [!abstract] 🔴 Avanzado — Aplicación Real
> 1. Un motor de renderizado cobra **$0.10 USD** por cada minuto de uso. Si un proyecto tardó **2 horas, 30 minutos y 45 segundos** en exportarse, ¿cuál es el costo total?
>    * *Instrucción:* Pasa las horas a minutos, los segundos a minutos (dividiendo entre 60) y suma todo. Al final, multiplica por $0.10.

---

## Respuestas (¡No hagas trampa!)
*   **Fácil:** 1) $300\ min$; 2) $2\ min$; 3) Compleja.
*   **Medio:** 
    1) $13^\circ\ 30'$. (Porque $0.5 \times 60 = 30$).
    2) $1^\circ\ 23'\ 20''$. ($5000 \div 60 = 83$ con residuo $20$; luego $83 \div 60 = 1$ con residuo $23$).
    3) $36972\ s$. ($10 \times 3600 + 16 \times 60 + 12$).
*   **Avanzado:** 
    1) Total minutos: $120 + 30 + 0.75 = 150.75\ min$.
    2) Costo: $150.75 \times 0.10 = \$15.075$ (Aprox. **$15.08 USD**).

> [!tip] 💡 Consejo de estudio del Profe Alex
> ¡Ojo con el "Truco del Decimal"! Si ves $13.5^\circ$, **no significa** que son 13 grados y 5 minutos. Significa 13 grados y **medio grado**. Para saber los minutos exactos, toma siempre la parte decimal ($0.5$) y bájala de nivel multiplicando por 60. ¡No te confundas, que es un error muy común!