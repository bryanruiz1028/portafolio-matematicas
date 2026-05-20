# 📖 Guía de estudio — Clase 05: Suma de Vectores por Componentes Rectangulares

¡Hola! Bienvenidos a una nueva sesión de física. Hoy vamos a dominar el método de componentes rectangulares. Aunque sumar vectores "en diagonal" parece difícil, el truco está en tratarlos como si fueran piezas de un rompecabezas que podemos desarmar y volver a armar.

> [!info] 📌 El Camino al Éxito (Los 3 Pasos)
> Para sumar cualquier cantidad de vectores, seguiremos este orden lógico y profesional:
> 1.  **Descomposición (Desarmar):** Transformamos cada vector diagonal en un triángulo rectángulo. Esto nos permite hallar sus "sombras" o proyecciones: la componente horizontal ($Ax$) y la componente vertical ($Ay$).
> 2.  **Suma de Componentes (Agrupar):** Sumamos todas las componentes en $X$ para obtener una sola $Rx$, y todas las en $Y$ para obtener $Ry$. Es como separar manzanas de naranjas y contar cuántas hay de cada una al final.
> 3.  **Reconstrucción (Armar):** Con los totales ($Rx$ y $Ry$), aplicamos el Teorema de Pitágoras para hallar la magnitud (el tamaño) y la arcotangente para la dirección (el ángulo) del vector resultante.

## Fórmulas y definiciones fundamentales

| Término | Definición / Fórmula | Tip del Profesor |
| :--- | :--- | :--- |
| **Componente en X** | $Vx = |V| \cdot \cos(\theta)$ | Se asocia con el eje horizontal. **Este** es $(+)$ y **Oeste** es $(-)$. |
| **Componente en Y** | $Vy = |V| \cdot \sin(\theta)$ | Se asocia con el eje vertical. **Norte** es $(+)$ y **Sur** es $(-)$. |
| **Magnitud Final** | $R = \sqrt{Rx^2 + Ry^2}$ | ¡Usa paréntesis en tu calculadora! $\sqrt{(Rx^2 + Ry^2)}$. |
| **Dirección (Ángulo)** | $\alpha = \tan^{-1}\left( \frac{|Ry|}{|Rx|} \right)$ | Usa `SHIFT` + `TAN`. Siempre pon los valores positivos aquí. |
| **Ángulo Complementario** | $90^\circ - \text{ángulo dado}$ | **Vital:** Úsalo solo si el ángulo inicia en el Norte o Sur. |

## Ejemplos resueltos

```ad-example
title: Ejemplo A — Suma básica de dos vectores
Vamos a sumar los vectores **A** (3m, E 30° N) y **B** (4m, E 73° N). Como ambos inician en el **Este**, los ángulos nos sirven directamente.

1. **Cálculo de componentes (Cuadrante Noreste = ambos positivos):**
   - $Ax = 3 \cdot \cos(30^\circ) = 2.59 \text{ m}$
   - $Ay = 3 \cdot \sin(30^\circ) = 1.5 \text{ m}$
   - $Bx = 4 \cdot \cos(73^\circ) = 1.16 \text{ m}$
   - $By = 4 \cdot \sin(73^\circ) = 3.82 \text{ m}$

2. **Suma para hallar el vector resultante (R):**
   - $Rx = 2.59 + 1.16 = 3.75 \text{ m}$ (Hacia el Este)
   - $Ry = 1.5 + 3.82 = 5.32 \text{ m}$ (Hacia el Norte)

3. **Cálculo final:**
   - Magnitud: $R = \sqrt{3.75^2 + 5.32^2} = 6.5 \text{ m}$
   - Ángulo: $\alpha = \tan^{-1}(5.32 / 3.75) = 54.82^\circ$

✅ **Resultado:** El vector resultante mide **6.5 m** con dirección **E 54.82° N**.
```

```ad-example
title: Ejemplo B — Uso de ángulos complementarios y signos
Sumaremos **A** (5m, N 20° E) y **B** (6m, O 40° S). ¡Atención a las direcciones!

1. **Ajuste de ángulos y signos:** 
   - El vector **A** inicia en el Norte, así que usamos el complemento: $90^\circ - 20^\circ = 70^\circ$. Trabajaremos con (5m, E 70° N).
   - El vector **B** inicia en el Oeste, el ángulo de 40° es perfecto. Pero cuidado: al ir al Oeste y Sur, sus componentes serán **negativas**.

2. **Componentes:**
   - $Ax = 5 \cdot \cos(70^\circ) = 1.71 \text{ m}$
   - $Ay = 5 \cdot \sin(70^\circ) = 4.69 \text{ m}$
   - $Bx = -6 \cdot \cos(40^\circ) = -4.59 \text{ m}$
   - $By = -6 \cdot \sin(40^\circ) = -3.85 \text{ m}$

3. **Totales y Resultante:**
   - $Rx = 1.71 - 4.59 = -2.88 \text{ m}$ (Significa que va al **Oeste**)
   - $Ry = 4.69 - 3.85 = 0.84 \text{ m}$ (Significa que va al **Norte**)
   - Magnitud: $R = \sqrt{2.88^2 + 0.84^2} = 3 \text{ m}$
   - Ángulo: $\alpha = \tan^{-1}(0.84 / 2.88) = 16.26^\circ$

✅ **Resultado:** El vector resultante mide **3 m** con dirección **O 16.26° N**.
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel Básico
Suma los vectores **M** (5m, O 82° N) y **N** (2.8m, O 19° N). 
*Pista:* Ambos van hacia el Oeste, por lo que sus componentes en X deben ser negativas.
**(Respuesta esperada: Magnitud = 6.35 m, O 58.3° N)**
```

```ad-abstract
title: 🟡 Nivel Medio
Suma los vectores **M** (4.2 u, O 74° S) y **N** (7.5 u, N 20° O). 
*Ojo de experto:* El vector M ya nace en el Oeste (eje X), no necesita cambios. Pero el vector N nace en el Norte (eje Y); debes hallar su ángulo complementario antes de usar las fórmulas.
**(Respuesta esperada: Magnitud = 4.77 u, O 39.05° N)**
```

```ad-abstract
title: 🔴 Nivel Avanzado — Tres Vectores
Calcula el vector resultante de:
- **A**: 4m, O 32° N
- **B**: 5m, S 15° E (Busca el complementario: 75°)
- **C**: 3m, E 24° N

*Requisito:* Elabora la tabla de componentes completa.
**(Respuesta esperada: R = 1.62 m, E 66.75° S)**
```

> [!important] 🚀 Pro-Tip Pedagógico: El Secreto de la Magnitud Negativa
> En ocasiones, un ejercicio te dará una magnitud negativa (ejemplo: $-3$ m, O 30° N). No te asustes. Para resolverlo, simplemente **vuelve positiva la magnitud y cambia las direcciones a su opuesto**. En este caso, se convertiría en: $3$ m, E 30° S. ¡Ahora ya puedes trabajar normalmente!

> [!tip] 💡 Consejos de Oro
> 1.  **Configura tu calculadora:** Asegúrate de que aparezca una **"D"** o **"DEG"** en la pantalla. Si dice "R" o "RAD", todos tus cálculos de seno y coseno estarán mal.
> 2.  **Dibuja siempre:** Haz un pequeño esquema. Si tu $Rx$ es negativo y $Ry$ es positivo, tu vector resultante *debe* estar en el cuadrante Noroeste. Si tu cálculo te da otra cosa, ¡revisa los signos!
> 3.  **El ángulo siempre al eje X:** Si el ángulo no toca el Este o el Oeste, usa la regla de los 90°. Es el error más común y el más fácil de evitar.