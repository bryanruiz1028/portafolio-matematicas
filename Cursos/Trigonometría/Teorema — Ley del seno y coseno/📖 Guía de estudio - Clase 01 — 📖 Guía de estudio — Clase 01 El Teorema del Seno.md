# 📖 Guía de estudio — Clase 01: El Teorema del Seno

1. **[!info] 📌 Conceptos clave**
    *   **Definición del Teorema:** Es una ley fundamental que establece que en cualquier triángulo, la relación (división) entre la longitud de un lado y el seno de su ángulo opuesto es constante. ¡Es como una balanza perfecta entre lados y ángulos!
    *   **Propiedad de Longitudes:** ¡Atención aquí! En todo triángulo, al lado de mayor longitud se le opone siempre el ángulo de mayor medida. Úsala como una "pista" para predecir tu respuesta: si buscas un lado opuesto a un ángulo pequeño, el resultado debe ser menor que el lado opuesto a un ángulo grande.
    *   **El Motor del Teorema (Pareja Conocida):** Para que el teorema "arranque", es obligatorio conocer una "pareja completa": un lado y su ángulo opuesto. Si tienes eso y cualquier otro dato, tienes el éxito asegurado.
    *   **Regla de Oro de los 180°:** Antes de empezar, recuerda que la suma de los ángulos internos siempre es $180.000^\circ$. Si te faltan ángulos, esta es tu primera herramienta de rescate.

2. **Fórmulas y definiciones importantes**

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ley del Seno (Lados)** | Utilízala para hallar un lado desconocido: $\frac{a}{\sin(A)} = \frac{b}{\sin(B)} = \frac{c}{\sin(C)}$. |
| **Ley del Seno (Ángulos)** | Esta versión invertida: $\frac{\sin(A)}{a} = \frac{\sin(B)}{b} = \frac{\sin(C)}{c}$ es por **comodidad algebraica**, ya que deja la incógnita arriba y facilita el despeje. |
| **Pareja de datos** | Es el corazón del cálculo. Consiste en tener el valor de un ángulo y la medida de su lado opuesto (ej. Ángulo $B$ y lado $b$). |
| **Modo de la calculadora** | **¡Truco vital!** Tu calculadora debe mostrar una **"D"** o **"DEG"** (Degrees). Si ves una "R" o "G", tus cálculos con grados sexagesimales estarán erróneos. |

3. **Ejemplos resueltos adicionales**

```ad-example
title: Ejemplo A: Hallar un lado desconocido (Caso Básico)
**Enunciado:** En un triángulo, el ángulo $A$ mide $60.000^\circ$, el ángulo $B$ mide $48.000^\circ$ y el lado $a$ mide $15.000\text{m}$. Encuentra la medida del lado $x$ (lado $b$).

**Pasos del Especialista:**
1. **Identificar la pareja completa:** Tenemos el ángulo $A (60.000^\circ)$ y su lado opuesto $a (15.000\text{m})$.
2. **Predecir el resultado:** Como el ángulo $B (48.000^\circ)$ es menor que el ángulo $A (60.000^\circ)$, nuestro lado $x$ debe ser menor a $15.000\text{m}$.
3. **Plantear la ecuación:**
   $$\frac{15.000}{\sin(60.000^\circ)} = \frac{x}{\sin(48.000^\circ)}$$
4. **Despejar $x$:** El $\sin(48.000^\circ)$ pasa a multiplicar al otro lado:
   $$x = \frac{15.000 \cdot \sin(48.000^\circ)}{\sin(60.000^\circ)}$$
**Resultado final:** $x \approx 12.871\text{m}$ (Efectivamente es menor a $15.000\text{m}$).
```

```ad-example
title: Ejemplo B: Aplicación en Topografía y Presupuesto
**Enunciado:** Un topógrafo mide un terreno triangular donde el ángulo $B = 28.000^\circ$, el ángulo $C = 100.000^\circ$ y el lado $b = 9.000\text{m}$. Se necesita calcular el costo de cercar el lado $a$ si cada metro de cerca cuesta $15.000\text{ USD}$.

**Pasos del Especialista:**
1. **Hallar el tercer ángulo ($A$):** 
   $$A = 180.000^\circ - 100.000^\circ - 28.000^\circ = 52.000^\circ$$
2. **Aplicar el Teorema del Seno para hallar el lado $a$:**
   $$\frac{a}{\sin(52.000^\circ)} = \frac{9.000}{\sin(28.000^\circ)}$$
3. **Despejar $a$:**
   $$a = \frac{9.000 \cdot \sin(52.000^\circ)}{\sin(28.000^\circ)} \approx 15.106\text{m}$$
4. **Calcular el presupuesto:** Multiplicamos la distancia por el valor unitario:
   $$15.106\text{m} \cdot 15.000\text{ USD/m} = 226.590\text{ USD}$$
**Resultado final:** El presupuesto para cercar el lado $a$ es de $226.590\text{ USD}$.
```

4. **Ejercicios de repaso**

```ad-abstract
title: 🟢 Nivel Fácil
En un triángulo se conocen dos ángulos: $36.000^\circ$ y $70.000^\circ$. El lado opuesto al ángulo de $70.000^\circ$ mide $14.000\text{m}$. Calcula la medida del lado opuesto al ángulo de $36.000^\circ$. (Respuesta sugerida: $8.757\text{m}$).
```

```ad-abstract
title: 🟡 Nivel Medio
Se tiene un triángulo con un ángulo de $42.000^\circ$ y su lado opuesto mide $26.000\text{m}$. Si otro de los lados mide $34.000\text{m}$, calcula la medida del ángulo agudo opuesto a este último lado usando la función $\sin^{-1}$. (Respuesta sugerida: $61.047^\circ$).
```

```ad-abstract
title: 🔴 Nivel Avanzado (Misión con Dron)
**Contexto:** Un dron vuela entre dos estaciones. El sensor indica que el ángulo en la estación B es de $26.000^\circ$. La distancia directa desde el dron hasta la estación C (lado opuesto a B) es de $15.000\text{km}$. La distancia entre el dron y la estación B (lado adyacente, llamado lado $c$) es de $28.000\text{km}$.

1. **Calcula el ángulo en la estación C.** Ten en cuenta que, por la posición visual, este es un **ángulo obtuso**. 
   *   **Pista del Profesor:** La calculadora tiene un límite y siempre te dará el ángulo agudo ($54.914^\circ$). Como el triángulo es obtuso, debes aplicar la resta: $180.000^\circ - 54.914^\circ$ para hallar el valor real.
2. **Presupuesto de combustible:** Si el dron consume combustible proporcional a la distancia, ¿será el trayecto opuesto al ángulo de la estación C el más costoso? Justifica usando la propiedad de mayor longitud.
```

5. **> [!tip] 💡 Consejo de estudio**
    El error más común de mis estudiantes no es entender el teorema, sino el manejo de la herramienta. **¡Cierra siempre los paréntesis!** Al escribir `sen(48)*15`, si no cierras el paréntesis después del 48, la calculadora creerá que intentas calcular el seno de $720$ ($48 \times 15$). Además, verifica siempre que la letra **"D"** esté visible en tu pantalla. ¡Pequeños detalles hacen grandes matemáticos!