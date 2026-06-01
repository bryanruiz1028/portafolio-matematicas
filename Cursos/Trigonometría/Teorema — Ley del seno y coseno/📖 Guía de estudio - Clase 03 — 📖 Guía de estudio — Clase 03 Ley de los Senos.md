# 📖 Guía de estudio — Clase 03: Ley de los Senos

> [!info] 📌 Conceptos clave
> ¡Hola! Para dominar la Ley de los Senos, debemos entender que esta es una herramienta poderosa para resolver triángulos que no son rectángulos. Aquí te presento los tres pilares que siempre debes recordar:
> - **La "Pareja Completa":** ¡Ojo aquí! Para poder empezar, es obligatorio conocer un ángulo y su lado opuesto (por ejemplo, el ángulo **A** y el lado **a**). Si no tienes esta "pareja", no tienes por dónde empezar.
> - **Regla de los 180°:** No te compliques; si ya conoces dos ángulos del triángulo, el tercero sale por simple lógica, ya que la suma de los ángulos internos siempre debe ser **180°**.
> - **Flexibilidad de la fórmula:** La fórmula se puede escribir de dos formas. El secreto pedagógico es colocar siempre la incógnita (lo que buscas) en el **numerador** (arriba). Esto facilita el despeje y evita errores algebraicos.

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula | Pro-Tip del Profe |
| :--- | :--- | :--- |
| **Notación** | Ángulos: Mayúsculas ($A, B, C$). Lados: Minúsculas ($a, b, c$). | El lado **a** siempre está frente al ángulo **A**. |
| **Hallar Lados** | $\frac{a}{\sin(A)} = \frac{b}{\sin(B)} = \frac{c}{\sin(C)}$ | Mantén los **lados arriba** para que el despeje sea de un solo paso. |
| **Hallar Ángulos** | $\frac{\sin(A)}{a} = \frac{\sin(B)}{b} = \frac{\sin(C)}{c}$ | Mantén los **senos arriba** si lo que te falta es el ángulo. |
| **Arcoseno ($\sin^{-1}$)** | Es la función inversa del seno. | Funciona igual que la raíz cuadrada para "eliminar" un cuadrado; el arcoseno "elimina" al seno. |

## Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A — Encontrar un ángulo
**Datos del problema:**
- Ángulo **A = 42°**
- Lado **a = 40m**
- Lado **c = 52m**
- Incógnita: Ángulo **C** ($\theta$)

**Paso a paso:**
1. **Verificación de Unidades:** Antes de empezar, ¡revisa siempre que las unidades coincidan! En este ejercicio trabajaremos todo en metros (**m**).
2. **Plantear la fórmula:** Como buscamos un ángulo, usamos la versión con senos arriba:
   `sin(C) / 52 = sin(42°) / 40`
3. **Despejar el seno de C:** El **52** pasa a multiplicar al otro lado:
   `sin(C) = [sin(42°) / 40] * 52`
4. **Aplicar Arcoseno:** Usamos la función inversa para dejar sola a la **C**:
   `C = sin⁻¹( (sin(42°) * 52) / 40 )`
   `C = sin⁻¹(0,8698...)`

**Resultado:**
El ángulo **C** es **60° 26' 36,64"**.
```

```ad-example
title: Ejemplo B — Aplicación con presupuesto
**Escenario:**
Debes instalar una cerca en el lado **x** (lado **B**) de un terreno triangular.
- Datos: Ángulo **C = 28°**, Ángulo **B = 52°**, Lado **c = 9m**.
- Costo unitario: **$25 USD** por metro.

**Paso a paso:**
1. **Calcular el lado x:** Usamos la fórmula de lados arriba para que la **x** quede lista para despejar:
   `x / sin(52°) = 9 / sin(28°)`
   `x = [9 / sin(28°)] * sin(52°)`
   `x = 15,1m` (Este es un valor **aproximado**, ¡no lo olvides!).
2. **Calcular presupuesto:** Multiplicamos la longitud aproximada por el costo:
   `15,1m * $25 USD = $377,5`

**Resultado:**
El costo total aproximado de la cerca para el lado **x** es de **$377,5 USD**.
```

## Ejercicios de Repaso

```ad-abstract
title: 🟢 Nivel Fácil
**Consigna:** ¡Vamos a practicar! En un triángulo, tienes dos ángulos de **63°** y **80°**. El lado opuesto al ángulo de **80°** mide **12m**. Halla la medida del lado **x** que se opone al ángulo de **63°**.
*(Pista: Como buscas un lado, coloca los lados arriba en tu fórmula).*
```

```ad-abstract
title: 🟡 Nivel Medio
**Consigna:** "Resolver el triángulo" significa encontrar todo lo que falta. Dado un lado **c = 13cm**, un ángulo **A = 65°** y un ángulo **B = 30°**:
1. Halla el ángulo **C** (recuerda la regla de los **180°**).
2. Encuentra los lados **a** y **b** usando la pareja completa que acabas de formar.
```

```ad-abstract
title: 🔴 Nivel Avanzado (Aplicación $USD)
**Consigna:** Un terreno tiene un ángulo de **115°** con un lado opuesto de **16m**. Otro de sus lados mide **10m**.
1. Calcula el ángulo faltante opuesto al lado de **10m**.
2. Calcula el ángulo restante y, con esos datos, halla el área total del terreno (puedes usar la fórmula: $Area = 0,5 \cdot a \cdot b \cdot \sin(C)$).
3. Si el metro cuadrado de material de cobertura cuesta **$12.50 USD**, ¿cuál es el costo total para cubrir todo el terreno?
```

> [!tip] 💡 Consejo de estudio
> ¡No dejes que la calculadora te engañe! Asegúrate siempre de que esté en modo **DEG** (o que veas una **"D"** en la pantalla). Si ves una "R" o una "G", tus senos darán valores locos. Además, como siempre te digo: al terminar, suma tus tres ángulos. Si te da **180°**, ¡vas por muy buen camino!