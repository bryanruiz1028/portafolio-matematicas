# GUÍA DE ESTUDIO — CLASE 04: MULTIPLICACIÓN Y DIVISIÓN DE FRACCIONES ALGEBRAICAS

> [!info] 📌 Conceptos clave
> - **Multiplicación directa:** El producto de dos o más fracciones algebraicas se obtiene multiplicando los numeradores entre sí para formar el nuevo numerador, y los denominadores entre sí para el nuevo denominador.
> - **Simplificación preventiva:** Como estrategia pedagógica, es fundamental simplificar antes de multiplicar. Esto evita que las expresiones se vuelvan inmanejables y reduce el margen de error.
> - **Regla de simplificación:** En el producto, se puede simplificar cualquier factor del numerador con cualquier factor del denominador ("uno de arriba con uno de abajo"), sin importar si pertenecen a la misma fracción.
> - **División como operación inversa:** Dividir es equivalente a multiplicar por el inverso multiplicativo del divisor. **Importante:** No se debe simplificar ninguna expresión antes de haber convertido la división en multiplicación.

---

### 1. Fórmulas y definiciones importantes

| Término | Definición y Lógica Matemática | Ejemplo |
| :--- | :--- | :--- |
| **Multiplicación** | Consiste en la obtención de un producto donde $\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}$. | $\frac{2}{x} \cdot \frac{y}{3} = \frac{2y}{3x}$ |
| **Simplificación** | Reducción de la expresión mediante la cancelación de factores comunes o la resta de exponentes en variables (literales) idénticas. | $\frac{x^2}{x} = x^{2-1} = x$ |
| **Inverso multiplicativo** | Denominado también "recíproco", es la inversión de los términos de una fracción para transformar la división en producto. | $\frac{x}{y} \to \frac{y}{x}$ |

---

### 2. Ejemplos resueltos con rigor pedagógico

```ad-example
title: Ejemplo A (Multiplicación de monomios)
**Enunciado:** Resolver simplificando al máximo: $\frac{3x^2}{2y} \cdot \frac{y^2}{6x}$

**Paso 1: Análisis y simplificación de coeficientes y variables**
*   **Coeficientes numéricos:** Sacamos tercera a $3$ (queda $1$) y a $6$ (queda $2$).
*   **Variable $x$:** Simplificamos $x^2$ en el numerador con $x$ en el denominador (restamos exponentes: $2-1$). Nos queda $x$ en el numerador.
*   **Variable $y$:** Simplificamos $y^2$ en el numerador con $y$ en el denominador. Nos queda $y$ en el numerador.

**Paso 2: Reescritura y producto final**
Tras la simplificación, las fracciones resultantes son:
$\frac{1 \cdot x}{2} \cdot \frac{y}{2}$

Multiplicamos lo restante:
$\frac{x \cdot y}{2 \cdot 2} = \frac{xy}{4}$

**Resultado:** $\frac{xy}{4}$
```

```ad-example
title: Ejemplo B (Aplicación financiera con polinomios)
**Enunciado:** Un producto tiene una cantidad representada por $\frac{x^2-1}{x+1}$ y un precio unitario de $\frac{5}{x-1}$ USD. Determine el costo total.

**Solución:**
El costo total es el producto de la cantidad por el precio:
$C = \frac{x^2-1}{x+1} \cdot \frac{5}{x-1}$

1.  **Factorización:** Identificamos una **Diferencia de Cuadrados** en el primer numerador: $(x^2-1) = (x+1)(x-1)$.
2.  **Sustitución de factores:** $\frac{(x+1)(x-1)}{(x+1)} \cdot \frac{5}{(x-1)}$
3.  **Simplificación de binomios:** Cancelamos el factor $(x+1)$ de arriba con el de abajo, y el factor $(x-1)$ de arriba con el de abajo.
4.  **Cálculo final:** Solo sobrevive el factor numérico $5$.

**Resultado final:** $5 \text{ USD}$.
```

---

### 3. Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel Fácil: Monomios y Simplificación Directa
Resuelva las siguientes operaciones simplificando antes de multiplicar:
1. $\frac{2a}{3b} \cdot \frac{6b^2}{4a}$
2. $\frac{5x^3}{y} \cdot \frac{y^2}{10x}$
3. $\frac{12m^2}{5n} \cdot \frac{10n}{3m}$
```

```ad-abstract
title: 🟡 Nivel Medio: Polinomios y Métodos de Factorización
Aplique factor común, diferencia de cuadrados o trinomios según corresponda:
1. $\frac{x+2}{x-1} \cdot \frac{x^2-1}{x+2}$ (Diferencia de cuadrados)
2. $\frac{x^2+5x+6}{x+3} \cdot \frac{x}{x+2}$ (Trinomio de la forma $x^2+bx+c$)
3. $\frac{4x-4}{x^2} \cdot \frac{x}{x-1}$ (Factor común)
```

```ad-abstract
title: 🔴 Nivel Avanzado: División y Aplicación Financiera
**Problema:** Se dispone de un presupuesto total de $\frac{x^2+5x+6}{x-1}$ dólares para adquirir suministros. Si el precio de cada unidad es de $\frac{x+2}{x^2-1}$ dólares, ¿cuántas unidades se pueden comprar?
*(Pista: Divida el presupuesto entre el costo unitario. Recuerde invertir la segunda fracción antes de simplificar y factorizar el trinomio y la diferencia de cuadrados).*

**Resultado esperado:** $(x+3)(x+1)$ o $x^2+4x+3$ unidades.
```

---

> [!tip] 💡 Consejo de estudio del profesor
> **¡Cuidado con la "tentación de cancelar"!** El error más común es intentar simplificar términos que están sumando o restando (ej. simplificar la $x$ en $\frac{x+2}{x}$). **Solo se pueden simplificar factores (expresiones que multiplican).** Si ves sumas o restas, tu primera obligación es convertirlas en productos mediante la **factorización**. Como dice la regla de oro: "Factoriza todo lo que sea factorizable antes de mover un solo lápiz para multiplicar".