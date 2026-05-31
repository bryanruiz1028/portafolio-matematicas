# 📖 Guía de estudio — Clase 06: Razones Trigonométricas

> [!info] 📌 Conceptos clave
> - **Triángulos Rectángulos:** Son el pilar de la trigonometría. Se identifican por tener un ángulo de 90° formado por dos catetos.
> - **La Visual y la Horizontal:** La "horizontal" es la línea imaginaria al nivel de los ojos del observador. La "visual" es la línea que une el ojo con el objeto observado.
> - **Ángulos de Elevación y Depresión:** Se mide **elevación** si el objeto está sobre la horizontal y **depresión** si está por debajo.
> - **Ángulos Alternos Internos:** Por geometría, el ángulo de depresión desde el observador es igual al ángulo de elevación desde el objeto. Esto permite "trasladar" el ángulo dentro del triángulo para facilitar los cálculos.
> - **Modo de la Calculadora:** Asegúrate de que tu calculadora muestre una **D** o la palabra **Degrees** (grados). ¡Si está en R o G, los resultados serán incorrectos!

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Seno (sen)** | $\frac{\text{Cateto Opuesto}}{\text{Hipotenusa}}$ |
| **Coseno (cos)** | $\frac{\text{Cateto Adyacente}}{\text{Hipotenusa}}$ |
| **Tangente (tan)** | $\frac{\text{Cateto Opuesto}}{\text{Cateto Adyacente}}$ |
| **Teorema de Pitágoras** | $a^2 + b^2 = c^2$ (Se usa para hallar un lado si conoces los otros dos). |

> [!important] ⚠️ Nota pedagógica
> Los nombres "Opuesto" y "Adyacente" no son fijos: dependen totalmente del ángulo que elijas para trabajar. El cateto que "toca" al ángulo es el adyacente; el que está frente a él es el opuesto.

## Ejemplos resueltos adicionales

`````ad-example
**Ejemplo A: El Faro y la Lancha (Uso de Tangente)**
**Problema:** Desde la cima de un faro de 7 m de altura se ve una lancha con un ángulo de depresión de 12°. ¿A qué distancia está la lancha de la base del faro?

1.  **Identificación de datos:**
    - Cateto Opuesto (altura): 7 m.
    - Ángulo: 12° (por ser alterno interno, lo usamos en la base del triángulo).
    - Incógnita: Cateto Adyacente ($x$).
2.  **Elección de función:** Como relacionamos los dos catetos, usamos la **Tangente**.
3.  **Planteamiento y Despeje:**
    - $\tan(12^\circ) = \frac{7}{x}$
    - $x = \frac{7}{\tan(12^\circ)}$
4.  **Resultado:** $x \approx 32,93$ m.
*Verificación:* Al comparar con un dibujo a escala, verás que la distancia horizontal debe ser notablemente mayor que la altura debido al ángulo tan pequeño (12°).
`````

`````ad-example
**Ejemplo B: La Escalera y la Pared (Contexto de Costos)**
**Problema:** Una escalera de 3 m de largo se apoya en una pared. Su base está a 1,2 m de la misma. Halla el ángulo con el suelo, la altura alcanzada y el costo de pintura.

1.  **Cálculo del Ángulo ($\theta$):**
    - Datos: Hipotenusa = 3 m; Cateto Adyacente = 1,2 m.
    - Usamos Coseno: $\cos(\theta) = \frac{1,2}{3}$
    - $\theta = \arccos(0,4) = 66,42^\circ$.
2.  **Cálculo de la Altura ($h$):**
    - Usamos Tangente: $\tan(66,42^\circ) = \frac{h}{1,2}$
    - $h = 1,2 \cdot \tan(66,42^\circ) = 2,74$ m.
3.  **Aplicación de Presupuesto:**
    - Si pintar el metro lineal de esa sección cuesta **$15 USD**:
    - $2,74 \text{ m} \times 15 \text{ USD} = \mathbf{41,10 \text{ USD}}$.
`````

## Ejercicios de repaso

`````ad-abstract
**🟢 Nivel: Fácil**
1. Una escalera de 3,2 m de longitud se apoya en una pared alcanzando una altura de 2,5 m. ¿A qué distancia de la pared se encuentra la base de la escalera?
2. Un observador ve la parte superior de una torre. Si el observador está a 8 m de la base y el ángulo de elevación es de 61°, ¿cuál es la altura de la torre? (Nota: ignora la altura del observador por ahora).
`````

`````ad-abstract
**🟡 Nivel: Medio**
Un avión de reconocimiento vuela a una altura constante de 2.300 m. El piloto localiza un objetivo en tierra con un ángulo de depresión de 28°. Calcula la **distancia diagonal (hipotenusa)** que separa al avión del objetivo.
`````

`````ad-abstract
**🔴 Nivel: Avanzado (Aplicación con $USD)**
Un observador en la azotea de un edificio de 60,85 m de altura ve otro edificio enfrente. Observa la azotea vecina con una elevación de 32° y la base con una depresión de 41°.
1. Calcula la distancia horizontal entre los edificios (usando el ángulo de 41°) y luego determina la **altura total** del edificio de enfrente.
2. **Instalación de cables:** Se requiere instalar un cable de seguridad entre ambas azoteas. Si el metro de cable cuesta **$120 USD**, ¿cuál es el presupuesto necesario? (Calcula la hipotenusa del triángulo superior formado por el ángulo de 32° para saber la longitud del cable).
`````

> [!tip] 💡 Consejo de estudio
> No necesitas ser un artista para que la trigonometría sea fácil. El "Profe Alex" recomienda usar simplemente **líneas y puntos** para representar objetos. Lo vital es hacer **dibujos a escala**: usa los cuadritos de tu cuaderno (por ejemplo, 1 cuadro = 1 metro). Esto te permite "ver" la respuesta antes de tocar la calculadora; si tu cálculo dice 100m pero tu dibujo muestra algo pequeño, ¡revisa tus datos!