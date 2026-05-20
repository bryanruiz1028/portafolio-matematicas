# 📖 Guía de estudio — Clase 04: Ecuaciones de la Elipse: De la forma Canónica a la General

> [!info] 📌 Conceptos clave
> Para dominar la transición entre las formas de la elipse, ten en cuenta lo siguiente:
> 1. **Diferencia Visual:** La **ecuación canónica** se reconoce por el uso de fracciones igualadas a $1$, mientras que la **ecuación general** no tiene fracciones y está igualada a $0$.
> 2. **Método de la "Carita Feliz":** Es la técnica principal para sumar las fracciones de la ecuación canónica, multiplicando denominadores entre sí y luego cruzando con los numeradores.
> 3. **Binomios al Cuadrado:** Cuando el centro es $(h, k)$, es obligatorio desarrollar los términos $(x-h)^2$ y $(y-k)^2$ para poder simplificar la expresión.
> 4. **Estructura Final:** La ecuación general debe presentarse en este orden: $Ax^2 + Cy^2 + Dx + Ey + F = 0$.
> 5. **El Denominador Invisible:** ¡No lo olvides! Si un término no tiene denominador visible, siempre puedes colocarle un $1$ debajo (por ejemplo: $y^2 = \frac{y^2}{1}$) para facilitar la suma de fracciones.

---

### 2. TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ecuación Canónica (Centro 0,0)** | $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ |
| **Ecuación General** | $Ax^2 + Cy^2 + Dx + Ey + F = 0$ |
| **Binomio al Cuadrado** | $(a \pm b)^2 = a^2 \pm 2ab + b^2$ |
| **Suma de Fracciones** | $\frac{N_1}{D_1} + \frac{N_2}{D_2} = \frac{(N_1 \cdot D_2) + (D_1 \cdot N_2)}{D_1 \cdot D_2}$ (Producto cruzado o "mariposa") |
| **General a Canónica (Pasos)** | 1. Pasar $F$ al lado derecho. 2. Dividir todo por ese valor. 3. Simplificar o invertir fracciones. |

---

### 3. EJEMPLOS RESUELTOS ADICIONALES

```ad-example
title: Ejemplo A: Conversión Básica (Centro 0,0)
**Enunciado:** Convertir la ecuación $\frac{x^2}{4} + \frac{y^2}{9} = 1$ a su forma general.

**Paso 1: Sumar las fracciones (Método de la carita feliz)**
Multiplicamos denominadores: $4 \cdot 9 = 36$.
Cruzamos numeradores: $(x^2 \cdot 9) + (4 \cdot y^2)$.
Obtenemos: $\frac{9x^2 + 4y^2}{36} = 1$

**Paso 2: Eliminar el denominador**
El $36$ que divide pasa a multiplicar al otro lado:
$9x^2 + 4y^2 = 1 \cdot 36 \rightarrow 9x^2 + 4y^2 = 36$

**Paso 3: Igualar a cero**
Pasamos el $36$ restando al primer miembro:
**$9x^2 + 4y^2 - 36 = 0$**
```

```ad-example
title: Ejemplo B: Aplicación Real (Pista para Dron)
**Contexto:** Una pista para drones sigue la trayectoria $\frac{(x-5)^2}{9} + \frac{(y+3)^2}{4} = 1$. Debemos hallar la forma general para determinar el costo base de construcción en $USD (representado por el término independiente $F$).

**Paso 1: Suma de fracciones y eliminación de denominadores**
Para trabajar con números enteros y eliminar las fracciones, multiplicamos en cruz:
$4(x-5)^2 + 9(y+3)^2 = 36$ (el producto $9 \cdot 4$ pasó multiplicando al $1$).

**Paso 2: Desarrollar los binomios al cuadrado**
Recordamos la fórmula $(a \pm b)^2$:
*   $(x-5)^2 = x^2 - 10x + 25$
*   $(y+3)^2 = y^2 + 6y + 9$
Sustituimos: $4(x^2 - 10x + 25) + 9(y^2 + 6y + 9) = 36$

**Paso 3: Aplicar propiedad distributiva**
$4x^2 - 40x + 100 + 9y^2 + 54y + 81 = 36$

**Paso 4: Agrupar y simplificar constantes**
Primero sumamos las constantes del lado izquierdo: $100 + 81 = 181$.
La ecuación queda: $4x^2 + 9y^2 - 40x + 54y + 181 = 36$

**Paso 5: Igualar a cero**
Restamos el $36$ del total: $181 - 36 = 145$.
**$4x^2 + 9y^2 - 40x + 54y + 145 = 0$**

**Resultado:** El término independiente es $145$, por lo que el costo base es de **145 USD**.
```

---

### 4. SECCIÓN DE EJERCICIOS DE REPASO

```ad-abstract
title: 🟢 Dificultad: Fácil (Centro en el origen)
¡Comencemos con lo básico! Pasa estas ecuaciones a su forma general:
1. $\frac{x^2}{25} + \frac{y^2}{4} = 1$
2. $\frac{x^2}{16} + \frac{y^2}{1} = 1$ (Pista: usa el denominador invisible).
3. $\frac{x^2}{10} + \frac{y^2}{5} = 1$
```

```ad-abstract
title: 🟡 Dificultad: Media (Centro h, k)
Aquí practicaremos la expansión de binomios. ¡No olvides la jerarquía de operaciones!
1. $\frac{(x-1)^2}{9} + \frac{(y-2)^2}{4} = 1$
2. $\frac{(x+3)^2}{16} + \frac{(y-4)^2}{25} = 1$
3. $\frac{(x-2)^2}{5} + \frac{(y+1)^2}{2} = 1$
```

```ad-abstract
title: 🔴 Dificultad: Avanzada (Aplicación Satelital $USD)
**Problema:** Un satélite sigue una órbita $4x^2 + 3y^2 - 10 = 0$. 
1. Transforma la ecuación a su forma canónica (usa el truco de la fracción invertida). 
2. **Scaffolding:** Recuerda que en la elipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, el denominador mayor representa el semieje mayor al cuadrado ($a^2$).
3. Si el costo del combustible es el valor del **denominador mayor** multiplicado por $1,000 USD, ¿cuál es el presupuesto necesario?
```

---

### 5. CONSEJO DE ESTUDIO

> [!tip] 💡 El truco de la "fracción invertida"
> Cuando conviertas de forma general a canónica, podrías encontrarte con un problema: un número multiplicando a la $x^2$ que no se puede simplificar (por ejemplo, $\frac{4x^2}{10}$ simplifica a $\frac{2x^2}{5}$). ¡Pero la $x^2$ debe estar sola! 
> 
> **La solución:** Aplica la propiedad de la fracción inversa. Baja el coeficiente del numerador como denominador del denominador. 
> 
> Así, $\frac{2x^2}{5}$ se convierte en $\frac{x^2}{5/2}$. Esto es matemáticamente idéntico y te permite mantener la estructura perfecta de la ecuación canónica. ¡Úsalo sin miedo!