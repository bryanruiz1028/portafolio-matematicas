# 📖 Guía de estudio — Clase 04: Componentes Rectangulares de un Vector

> [!info] 📌 Conceptos clave
> Para dominar la descomposición de vectores como un experto, recuerda estos cuatro pilares fundamentales:
> 1. **Definición:** Las componentes rectangulares son las "proyecciones" o sombras que un vector proyecta sobre los ejes X e Y. Imagina que iluminas el vector desde arriba y desde un lado; las sombras resultantes son sus componentes.
> 2. **El "Ancla" Horizontal:** Para que nuestras fórmulas funcionen siempre, el ángulo de trabajo ($\theta$) **debe tocar el eje horizontal** (ya sea el Este o el Oeste). 
> 3. **Regla de Signos:** La dirección manda. Si el vector va al Norte o Este, es positivo (+). Si va al Sur u Oeste, es negativo (-).
> 4. **Configuración Técnica:** ¡No dejes que la tecnología te falle! Tu calculadora debe mostrar una **"D"** o el modo **DEG** (grados) en pantalla. Si dice "R" o "G", los resultados serán incorrectos.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Magnitud ($|A|$)** | Es la medida, tamaño o "largo" de la flecha que representa al vector. |
| **Componente en X ($A_x$)** | Proyección horizontal: $A_x = |A| \cdot \cos(\theta)$. Usamos **coseno** porque es el lado adyacente al ángulo. |
| **Componente en Y ($A_y$)** | Proyección vertical: $A_y = |A| \cdot \sin(\theta)$. Usamos **seno** porque es el lado opuesto al ángulo. |
| **Ángulo de dirección ($\alpha$)** | Para hallar el ángulo si ya tienes las componentes: $\alpha = \tan^{-1}\left(\frac{|A_y|}{|A_x|}\right)$. Usamos valores absolutos (siempre positivos) dentro del paréntesis. |
| **Ángulo Complementario** | Si el ángulo del problema "toca" el Norte o el Sur, réstalo de 90° para obtener el **Ángulo de Trabajo** que toque el eje X. |

> [!warning] **Regla de Oro**
> Estas fórmulas de seno y coseno solo son válidas si el ángulo de trabajo ($\theta$) nace desde el eje horizontal (Este u Oeste).

## Ejemplos resueltos

```ad-example
title: Ejemplo A — Caso básico (Vector en el primer cuadrante)
**Enunciado:** Hallar las componentes del vector de 6 cm con dirección 30° Norte del Este.

- **Paso 1:** Identificar datos. Magnitud $|A| = 6$ cm. El ángulo (30°) ya toca el Este, así que nuestro **Ángulo de Trabajo** es 30°.
- **Paso 2:** Calcular $A_x$. Al ser Este, es (+):
  $A_x = 6 \cdot \cos(30^\circ) \approx 5.19$ cm.
- **Paso 3:** Calcular $A_y$. Al ser Norte, es (+):
  $A_y = 6 \cdot \sin(30^\circ) = 3$ cm.

🔍 **Comprobación Visual:** Como 30° es un ángulo pequeño (más cerca de la horizontal que de la vertical), la sombra en X (5.19) debe ser más larga que la sombra en Y (3). ¡Correcto!
✅ **Resultado:** $A_x \approx 5.19$ cm, $A_y = 3$ cm.
```

```ad-example
title: Ejemplo B — Aplicación de trayectoria y costo ($USD)
**Enunciado:** Un dron se desplaza 8 cm en dirección Sur 34° Oeste. Si cada cm de recorrido cuesta $1.50 USD, calcula sus componentes y el costo total.

- **Paso 1 (Ángulo de Trabajo):** El ángulo de 34° toca el Sur. ¡Cuidado! Debemos usar el complemento: $90^\circ - 34^\circ = \mathbf{56^\circ}$.
- **Paso 2 (Signos):** Sur es (-) y Oeste es (-). Ambas componentes serán negativas.
- **Paso 3 (Cálculos):** 
  - $M_x = -8 \cdot \cos(56^\circ) \approx -4.47$ cm.
  - $M_y = -8 \cdot \sin(56^\circ) \approx -6.63$ cm.
- **Paso 4 (Costo):** El costo total depende de la distancia total recorrida (magnitud): $8 \text{ cm} \cdot 1.50 = \$12.00$ USD.

🔍 **Comprobación Visual:** 56° está más inclinado hacia la vertical (eje Y). Por lo tanto, la componente Y (6.63) debe ser mayor que la X (4.47). Los signos negativos coinciden con el tercer cuadrante (Sur-Oeste).
✅ **Resultado:** $M_x \approx -4.47$ cm, $M_y \approx -6.63$ cm | Costo: $12.00 USD.
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel: Fácil
1. Hallar las componentes rectangulares de un vector de 12 cm a 50° Norte del Este.
2. Si un vector tiene $A_x = 5$ y $A_y = 3$, ¿cuál es su ángulo de dirección $\alpha$? (Usa la fórmula de $\tan^{-1}$).
```

```ad-abstract
title: 🟡 Nivel: Medio
1. Un vector de 10 m tiene una dirección Norte 80° Oeste. Encuentra sus componentes. (*Pista: Calcula primero el ángulo de trabajo que toca el Oeste*).
2. Calcula el ángulo de un vector con componentes negativas: $B_x = -4$ y $B_y = -2$. No olvides usar valores absolutos en la calculadora para obtener el ángulo interno.
```

```ad-abstract
title: 🔴 Nivel: Avanzado — Desafío de Ingeniería
Un cable de telecomunicaciones se desplaza desde el origen 15 metros en dirección **Este 25° Sur**.
1. Calcula las componentes rectangulares indicando los signos correctos.
2. **Cálculo de presupuesto:** El costo de instalación por cada metro de la componente horizontal (X) es de $2.00 USD y por cada metro de la componente vertical (Y) es de $3.50 USD. 
   *Nota: Para calcular el costo, utiliza el **valor absoluto** de los metros obtenidos en cada componente (la distancia no puede ser negativa).*
   **¿Cuál es el costo total del cableado por componentes?**
```

> [!tip] 💡 Consejo del Profe
> **¡Dibuja siempre antes de tocar la calculadora!** Un pequeño bosquejo del vector te dirá dos cosas vitales: qué componente debe ser más larga y qué signos (+ o -) deben tener tus resultados. Si tu dibujo muestra una sombra larga en X y tu calculadora te da un número pequeño, ¡revisa si confundiste el seno con el coseno!