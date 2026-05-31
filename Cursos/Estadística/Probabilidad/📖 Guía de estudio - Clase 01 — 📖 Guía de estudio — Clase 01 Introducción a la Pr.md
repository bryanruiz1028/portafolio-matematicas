# 📖 Guía de estudio — Clase 01: Introducción a la Probabilidad y Regla de Laplace

> [!info] 📌 Conceptos clave
> - **Experimento aleatorio ($\epsilon$):** Es cualquier acción cuyo resultado no se puede predecir con total certeza antes de realizarla (por ejemplo, lanzar un dado o una moneda).
> - **Espacio muestral ($S$ o $\Omega$):** Es el conjunto que agrupa la totalidad de los resultados posibles de un experimento aleatorio.
> - **Evento o Suceso:** Es un subconjunto del espacio muestral; representa uno o varios resultados específicos que nos interesan.
> - **Regla de Laplace:** Es el método fundamental para calcular la probabilidad de un suceso cuando todos los resultados posibles tienen la misma oportunidad de ocurrir (equiprobables).

## 📊 Tabla de Referencia: Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Experimento Aleatorio ($\epsilon$)** | Acción con resultado incierto (ej. extraer una carta al azar). |
| **Espacio Muestral ($S$)** | Conjunto de todos los resultados posibles, escrito entre llaves. |
| **Evento o Suceso** | Caso o subconjunto específico del espacio muestral. |
| **Regla de Laplace** | $P(\text{A}) = \frac{\text{Casos favorables}}{\text{Casos posibles}}$ |

*Nota: En la Regla de Laplace, el denominador siempre debe ser mayor o igual al numerador, lo que da como resultado una "fracción propia" (un valor entre 0 y 1).*

---

## 💡 Ejemplos Resueltos

```ad-example
title: Ejemplo A: Lanzamiento de un dado
***Problema:** Hallar la probabilidad de obtener el número 3 al lanzar un dado normal de seis caras.*

1. **Paso 1 (Identificar casos posibles):** *El espacio muestral es $S = \{1, 2, 3, 4, 5, 6\}$. Por lo tanto, el total de casos posibles es 6.*
2. **Paso 2 (Identificar casos favorables):** *El suceso que buscamos es que caiga el número 3. Solo hay 1 caso favorable.*
3. **Resultado:** 
   - *En fracción:* $1/6$
   - *Cálculo decimal:* $1 \div 6 = 0,166...$
   - *En porcentaje:* $\approx 16,6\%$
```

```ad-example
title: Ejemplo B: Aplicación en Rifas ($100 USD)
***Problema:** Una persona compra 5 boletos para una rifa de **$100 USD** donde hay un total de 20 boletos. ¿Cuál es la probabilidad de ganar el premio?*

1. **Paso 1 (Definir casos posibles):** *El total de boletos que participan en el sorteo es 20.*
2. **Paso 2 (Definir casos favorables):** *La persona posee 5 boletos que pueden resultar ganadores.*
3. **Resultado:**
   - *Fracción simplificada:* $5/20 = 1/4$
   - *Decimal:* $0,25$
   - *Porcentaje:* $25\%$
```

---

## 📝 Ejercicios de Repaso

```ad-abstract
title: 🟢 Nivel: Fácil
1. **Calcular la probabilidad** *de lanzar una moneda y que el resultado sea cruz.*
2. **Determinar la probabilidad** *de elegir un día al azar y que sea fin de semana (Sábado o Domingo) de entre los 7 días de la semana.*
3. **Identificar el espacio muestral ($S$)** *completo de lanzar un dado convencional de 6 caras.*
```

```ad-abstract
title: 🟡 Nivel: Medio
1. **Hallar la probabilidad** *de que, al lanzar un dado, el resultado sea un número mayor que 4.*
2. **En una urna con 3 bolas azules y 4 rojas**, *calcula la probabilidad de extraer, sin mirar, una bola de color rojo.*
3. **Al lanzar dos monedas simultáneamente**, *¿cuál es la probabilidad de que ambas caigan en la misma cara (es decir, las dos cara o las dos cruz)?* 
   *Pista: Construye el espacio muestral combinando los resultados: $\{CC, CX, XC, XX\}$.*
```

```ad-abstract
title: 🔴 Nivel: Avanzado (Aplicación $USD)
1. **Una empresa regala un bono de $50 USD** *al azar entre sus 10 empleados (6 hombres y 4 mujeres). Define el **Evento A: La ganadora es mujer** y calcula su probabilidad.*
2. **Un evento compuesto:** *Calcula la probabilidad de elegir el boleto ganador de un sorteo de **$20 USD** entre 50 participantes totales. Expresa el resultado final en porcentaje.*
3. **Control de Calidad:** *Determina el espacio muestral ($S$) de un experimento donde se revisan 3 artículos para ver si son defectuosos (D) o no defectuosos (N). Usa la notación abreviada (ej. NNN, NND...).*
```

---

> [!tip] 💡 Consejo de estudio
> Para confirmar que tu operación es correcta, verifica que el resultado sea siempre una **fracción propia** (donde el número de arriba es menor o igual al de abajo). Esto garantiza que la probabilidad nunca sea mayor a 1 (o 100%), ya que es imposible tener más casos a favor que casos totales existentes. Para pasar a porcentaje, divide el numerador por el denominador y multiplica el decimal resultante por 100.