# 📖 Guía de estudio — Clase 09: Trigonometría: Uso correcto de la calculadora

> [!info] 📌 Conceptos clave
> Como especialistas en tecnología educativa Casio, es fundamental que domines la sintaxis de tu herramienta para evitar errores comunes en exámenes de trigonometría:
> * **Configuración angular:** Verifica siempre el indicador en pantalla. Usa el modo **DEG (D)** para trabajar con grados sexagesimales y **RAD (R)** para radianes. Un error en este ajuste invalidará todo el procedimiento.
> * **Funciones inversas:** Para hallar ángulos, se debe activar la función "arco" (como $\cos^{-1}$) mediante la tecla `SHIFT`. 
> * **Modo MathIO vs. Lineal:** El modo **MathIO** es la representación natural; permite que las fracciones y raíces se visualicen exactamente igual que en el papel, reduciendo errores de transcripción.
> * **Jerarquía de operaciones y paréntesis:** Al calcular la Ley del Coseno, es obligatorio el uso de **paréntesis dobles**. El primer paréntesis agrupa toda la operación del arco coseno, mientras que los internos deben agrupar el numerador y el denominador por separado. Sin estos, la calculadora dividirá únicamente el último término ($c^2$) entre el denominador, ignorando el resto del numerador.

---

## 2. Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **DEG (D)** | Del inglés *Degree*. Indica el sistema sexagesimal donde la circunferencia se divide en 360°. |
| **RAD (R)** | Sistema de radianes, donde la vuelta completa equivale a $2\pi$. Es el estándar en cálculo avanzado. |
| **GRA (G)** | Gradianes o grados centesimales (400 partes la vuelta completa). Poco usado en nivel escolar. |
| **Ley del Coseno (Ángulo A)** | Despeje técnico para el cálculo directo del ángulo: $A = \cos^{-1}\left(\frac{a^2 - b^2 - c^2}{-2bc}\right)$. |
| **Tecla Sexagesimal** | Identificada como `° ' "`. Permite ingresar datos y convertir resultados decimales a Grados, Minutos y Segundos. |

---

## 3. Ejemplos resueltos adicionales

````ad-example
**Ejemplo A: Hallar un ángulo (Caso Básico - Tres lados conocidos)**
**Problema:** Calcula el ángulo $A$ de un triángulo cuyos lados miden $a=9$, $b=7$ y $c=13$.

**Paso a paso técnico:**
1. **Identificación:** Al conocer los tres lados, aplicamos el despeje de la Ley del Coseno.
2. **Sustitución:** 
   $A = \cos^{-1}\left(\frac{9^2 - 7^2 - 13^2}{-2(7)(13)}\right)$
3. **Configuración Casio:** Presiona `SHIFT` + `MODE` + `3` para asegurar el modo **DEG**.
4. **Entrada de datos:** Presiona `SHIFT` + `COS` para activar $\cos^{-1}$. Para asegurar la jerarquía, ingresa:
   `cos⁻¹((9² - 7² - 13²) / (-2 * 7 * 13))`
5. **Resultado:** 
   * Decimal: $41.17^\circ$
   * Sexagesimal (presionando la **tecla sexagesimal**): $41^\circ 10' 15.9''$.
````

````ad-example
**Ejemplo B: Aplicación Real con Costos Proporcionales**
**Problema:** Un ingeniero debe medir el ángulo de inclinación de un terreno triangular (lados: $22\text{m}$, $28\text{m}$ y $15\text{m}$). El costo del estudio es de **$10 USD** por cada grado medido. Si el ángulo es decimal, el cobro se realiza de forma proporcional. Calcule el costo del informe para el ángulo opuesto al lado de $22\text{m}$.

**Resolución:**
1. **Cálculo del ángulo ($a=22, b=28, c=15$):**
   $A = \cos^{-1}\left(\frac{22^2 - 28^2 - 15^2}{-2(28)(15)}\right) = \cos^{-1}(0.625)$
2. **Resultado en calculadora:** $51.3178...^\circ \approx 51.32^\circ$.
3. **Cálculo financiero:** Multiplicamos el valor decimal exacto por la tarifa:
   $51.3178... \times 10\text{ USD} = \mathbf{513.18\text{ USD}}$ (redondeado al centavo).
````

---

## 4. Ejercicios de repaso

````ad-abstract
**🟢 Nivel: Fácil**
1. ¿Cuál es el indicador (letra) que debe mostrar la pantalla para asegurar que estamos trabajando en grados sexagesimales?
2. Calcula $\sin(30^\circ)$. Si el resultado es $0.988...$, ¿en qué modo está tu calculadora y a qué modo deberías cambiarla?
3. Obtén el valor de $\cos(180^\circ)$. El resultado debe ser un número entero.
````

````ad-abstract
**🟡 Nivel: Medio**
1. **Uso de la tecla sexagesimal:** Ingresa $\tan(20^\circ 0' 15'')$. Recuerda que es obligatorio marcar el $0$ en los minutos aunque su valor sea nulo.
2. **Operación en cadena:** Calcula de forma directa $\sqrt{12^2 + 7^2 - 2(12)(7)\cos(40^\circ)}$. Asegúrate de que la raíz cubra toda la expresión.
3. **Diagnóstico de errores:** Intenta calcular $\sin^{-1}(16/8)$ en tu Casio. ¿Aparece un "Syntax ERROR" o un "Math ERROR"? Explica por qué ocurre esto basándote en que el seno de un ángulo no puede ser mayor a 1.
````

````ad-abstract
**🔴 Nivel: Avanzado (Aplicación Práctica)**
En una obra civil, se requiere instalar un refuerzo en un ángulo crítico. Los soportes forman un triángulo de $22\text{m}$, $28\text{m}$ y $15\text{m}$. El material de soldadura especial cuesta **$15.50 USD** por cada grado de apertura del ángulo más pequeño (opuesto al lado de $15\text{m}$).
1. Calcula el valor de dicho ángulo usando la Ley del Coseno (redondea a dos decimales).
2. Determina el presupuesto total necesario en **$USD**, considerando que el cobro es proporcional a la fracción del grado.
````

---

## 5. Consejo de estudio

> [!tip] 💡 Consejo de estudio
> Para que tu proceso de aprendizaje sea más intuitivo, activa siempre el **Modo MathIO**. En los modelos Casio ClassWiz o Plus, puedes acceder mediante el atajo `SHIFT` + `MODE` + `1`. Esto hará que la pantalla de tu calculadora sea un espejo de lo que escribes en tu cuaderno, facilitando la identificación de paréntesis faltantes o errores en el ingreso de fracciones complejas.