# Clase 04 — Caída Libre

#algebra #caidalibre

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 4 de 4

> [!info] 🧭 Navegación
> [[Clase 03 - Caída libre Gravedad lunar, lanzamientos y aplicaciones con|⬅ Clase 03]] | [[00 - Índice del curso|Índice]] | **Clase 04** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]

---

## ¿Por qué es importante esta clase?

¡Bienvenido! Hoy vamos a dominar uno de los movimientos más fascinantes de la naturaleza. Comprender la caída libre no solo es resolver números; es entender cómo la fuerza invisible de la gravedad gobierna todo lo que nos rodea. ¡No te asustes por el nombre, verás que con orden es más sencillo de lo que parece!

> [!info] 🌍 Relevancia y aplicaciones
> La gravedad es una aceleración constante que atrae los objetos hacia el centro de la Tierra. En el vacío, todos los cuerpos caen con la misma aceleración, aumentando su velocidad de forma constante cada segundo.
> 
> - **💵 Aplicación con $USD:** En la industria, certificar un sensor de impacto tiene un costo. Si una empresa cobra **$10 USD por cada 10 metros** de altura, calcular la distancia exacta es vital para no desperdiciar presupuesto.
> - **🏗️ Aplicación práctica:** Es esencial en ingeniería para diseñar redes de seguridad en construcción y frenos de emergencia en ascensores.
> - **📊 Situación cotidiana:** Permite medir tu tiempo de reacción. ¿Sabías que puedes calcular qué tan rápido eres midiendo cuántos centímetros cae una regla antes de que la captures?

---

## Concepto clave

> [!note] 📌 ¿Qué es Caída Libre?
> Es un movimiento vertical hacia abajo donde un objeto se suelta desde el reposo. Para nuestros cálculos, utilizaremos estas reglas de oro:
> 1. **Velocidad inicial ($v_i$):** Siempre es **$0\text{ m/s}$**.
> 2. **Aceleración ($g$):** Es la gravedad, que en la Tierra redondeamos a **$9.8\text{ m/s}^2$**.
> 3. **Dirección:** El objeto acelera hacia abajo, por lo que la velocidad aumenta con el tiempo.

> [!warning] ⚠️ Error común
> Existe una diferencia vital entre "lanzar" y "dejar caer". Si el problema dice **"se deja caer"**, automáticamente tu $v_i = 0$. Si el objeto se lanza con fuerza hacia abajo, la $v_i$ ya no es cero y las fórmulas cambian. ¡Lee con atención!

> [!tip] 💡 Truco para recordarlo
> Usa la regla mnemotécnica: **"Caída = Cero"**. Si algo cae por su propia cuenta, su velocidad en el "segundo cero" es exactamente **Cero**.

---

## Procedimiento Paso a Paso

Este sistema de 4 pasos es tu brújula para no perderte nunca en un ejercicio. ¡Síguelo y el éxito está asegurado!

```text
PASO 1: Leer el ejercicio y listar datos conocidos ($v_i$, $t$, $g$) y la incógnita ($y$ o $v_f$).
PASO 2: Verificar unidades. Asegúrate de que todo esté en Metros ($m$) y Segundos ($s$).
PASO 3: Seleccionar la fórmula. El secreto es buscar la fórmula que NO tenga la variable 
        que ni conocemos ni queremos hallar (la variable que "sobra").
PASO 4: Reemplazar los valores de las variables y resolver la operación matemática.
```

---

## Ejemplos de Aplicación

### Ejemplo 1: El Edificio (Caso Básico)
**Problema:** Se deja caer una piedra desde lo alto de un edificio y llega al suelo en $4\text{ s}$. ¿Cuál es la altura?
- **Datos:** $v_i = 0$, $t = 4\text{ s}$, $g = 9.8\text{ m/s}^2$.
- **Fórmula:** $y = v_i \cdot t + \frac{g \cdot t^2}{2}$
- **Cálculo:** Como $v_i = 0$, el término $(v_i \cdot t)$ desaparece.
- $y = \frac{9.8 \cdot (4)^2}{2} = \frac{9.8 \cdot 16}{2} = 9.8 \cdot 8 = 78.4$.
- **Resultado:** La altura es de **$78.4\text{ metros}$**.

### Ejemplo 2: El Juguete (Velocidad Final)
**Problema:** Un niño deja caer un juguete desde una ventana y tarda $3\text{ s}$ en chocar. ¿Con qué velocidad impacta?
- **Datos:** $v_i = 0$, $t = 3\text{ s}$, $g = 9.8\text{ m/s}^2$.
- **Fórmula:** $v_f = v_i + g \cdot t$
- **Cálculo:** $v_f = 0 + (9.8 \cdot 3) = 29.4$.
- **Resultado:** La velocidad final es de **$29.4\text{ m/s}$**.

### Ejemplo 3: El Sistema de Gotas (Caso Avanzado)
**Problema:** Una llave gotea cada segundo. Cuando va a caer la 4ª gota, ¿qué distancia separa a la 1ª de la 2ª?
- **Análisis lógico:** Si la 4ª gota está por salir ($t=0\text{ s}$), la 3ª ha caído por $1\text{ s}$, la 2ª por $2\text{ s}$ y la 1ª por $3\text{ s}$.
- **Cálculo $y_1$ ($t=3\text{ s}$):** $y_1 = \frac{9.8 \cdot 3^2}{2} = 44.1\text{ m}$.
- **Cálculo $y_2$ ($t=2\text{ s}$):** $y_2 = \frac{9.8 \cdot 2^2}{2} = 19.6\text{ m}$.
- **Resta:** $44.1 - 19.6 = 24.5$.
- **Resultado:** La distancia de separación es de **$24.5\text{ metros}$**.

### Ejemplo 4: Aplicación Financiera ($USD$)
**Problema:** Un edificio tiene la altura del Ejemplo 1 ($78.4\text{ m}$). Si un seguro de obra cobra **$5\text{ USD}$ por cada metro** de altura, ¿cuál es el costo?
- **Cálculo:** $78.4\text{ m} \cdot 5\text{ USD/m} = 392$.
- **Resultado:** El costo total es de **$392\text{ USD}$**.

---

## Ejercicios para el Estudiante

¡Es tu turno de brillar! Aplica los 4 pasos en estos desafíos.

```ad-abstract
color: 0, 255, 0
title: 🟢 Nivel Fácil: Cálculo de Altura
Calcula la altura recorrida ($y$) para los siguientes tiempos (usa $g = 9.8$):
1. $t = 1\text{ s}$
2. $t = 2\text{ s}$
3. $t = 5\text{ s}$
4. $t = 6\text{ s}$
```

```ad-abstract
color: 255, 255, 0
title: 🟡 Nivel Medio: Velocidad y Tiempo
Resuelve aplicando las fórmulas de $v_f$ y despeje de $t$:
1. Hallar la $v_f$ a los $4\text{ segundos}$.
2. Hallar la $v_f$ a los $3\text{ segundos}$.
3. ¿Cuánto tiempo tarda un objeto en caer $44.1\text{ metros}$?
4. ¿Cuánto tiempo tarda un objeto en caer $19.6\text{ metros}$?
```

```ad-abstract
color: 255, 0, 0
title: 🔴 Nivel Avanzado: Gotas y Costos
1. En el sistema de gotas, ¿qué distancia separa a la 1ª de la 2ª gota cuando va a caer la 3ª gota?
2. ¿Qué distancia separa a la 1ª de la 3ª gota cuando va a caer la 4ª gota?
3. Un sensor cae durante $5\text{ s}$. Si la certificación cuesta **$10\text{ USD}$ por cada $10\text{ metros}$**, ¿cuál es el costo total?
4. Calcula el costo de impacto (**$10\text{ USD}$ cada $10\text{ m}$**) para un objeto que cae durante $4\text{ s}$.
```

---

## Respuestas y Autoevaluación

```ad-success
title: ✅ Clave de Respuestas
- **Fácil:** 1) $4.9\text{ m}$ | 2) $19.6\text{ m}$ | 3) $122.5\text{ m}$ | 4) $176.4\text{ m}$
- **Medio:** 1) $39.2\text{ m/s}$ | 2) $29.4\text{ m/s}$ | 3) $3\text{ s}$ | 4) $2\text{ s}$
- **Avanzado:** 
  1) $14.7\text{ m}$ ($19.6\text{ m} - 4.9\text{ m}$).
  2) $39.2\text{ m}$ ($44.1\text{ m} - 4.9\text{ m}$).
  3) $122.5\text{ USD}$. (Nota: $\$10\text{ USD}$ por cada $10\text{ m}$ equivale a **$\$1\text{ USD}$ por metro**). Altura = $122.5\text{ m}$.
  4) $78.4\text{ USD}$. (Altura = $78.4\text{ m} \cdot \$1\text{ USD/m}$).
```

## Mini-prueba de autoevaluación

```ad-question
¿Cuál es el valor de la velocidad inicial ($v_i$) cuando un ejercicio dice que un objeto "se deja caer"?
```

```ad-question
Si un objeto cae libremente durante $10\text{ segundos}$, ¿cuál será su velocidad final ($v_f$)?
```

```ad-question
Se cae una herramienta desde un andamio y tarda $2\text{ s}$ en chocar. Si la reparación cuesta **$10\text{ USD}$ por cada $10\text{ metros}$** de caída, ¿cuánto dinero debes pagar?
```

---

## Notas para el próximo tema

¡Excelente trabajo hoy! Has dominado el movimiento hacia abajo. En la próxima clase daremos un giro: el **Lanzamiento Vertical**. Aprenderemos qué sucede cuando lanzas algo hacia arriba; la gravedad ahora actuará en contra (será negativa) y el objeto se detendrá por un instante en el punto más alto. ¡Prepárate!

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 4 de 4

> [!info] 🧭 Navegación
> [[Clase 03 - Caída libre Gravedad lunar, lanzamientos y aplicaciones con|⬅ Clase 03]] | [[00 - Índice del curso|Índice]] | **Clase 04** | | 📋 [[00 - Índice del curso|Fin del curso ➡]]