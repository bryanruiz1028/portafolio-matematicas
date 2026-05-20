#algebra #readeltringuloc

> [!info] 🧭 Navegación
> - **Anterior:** [[Clase 04 — Perímetros y conceptos básicos]]
> - **Siguiente:** [[Clase 06 — Propiedades de polígonos y Pitágoras avanzado]]

---

## ¿Por qué es importante esta clase?

> [!info] 🌍 Relevancia y aplicaciones
> Determinar la superficie de un triángulo es una competencia esencial que trasciende el aula. Dependiendo de los datos que tengamos —ya sea la altura, los tres lados o si el triángulo es equilátero— debemos saber qué herramienta matemática aplicar para obtener un resultado preciso.
> 
> - **💵 [aplicación con $USD]:** Calcular el presupuesto para la compra de terrenos triangulares o la cantidad de cerámica necesaria para un piso.
> - **🏗️ [aplicación práctica]:** Diseño estructural en arquitectura, especialmente en el cálculo de cerchas y soportes de techos.
> - **📊 [situación cotidiana]:** Planificación de áreas de siembra en jardinería o el corte óptimo de piezas de tela en diseño de modas.

---

## Concepto clave

> [!note] 📌 ¿Qué es el Área del triángulo?
> El área representa la medida de la superficie encerrada por los tres lados de la figura. A diferencia del perímetro (longitud), el área se expresa siempre en unidades elevadas al cuadrado ($u^2$). Contamos con tres métodos principales según la información disponible:
> 1. **Base y Altura:** El método estándar.
> 2. **Fórmula de Herón:** Utilizada cuando conocemos los tres lados pero no la altura.
> 3. **Específica para Equiláteros:** Una versión optimizada para triángulos con todos sus lados iguales.

> [!warning] ⚠️ Error común
> Un error crítico es confundir el lado ($L$) con la altura ($h$) al aplicar fórmulas de triángulos equiláteros. Además, nunca olvides **dividir entre 2** en la fórmula estándar; de lo contrario, estarás calculando el área de un paralelogramo.

> [!tip] 💡 Truco para recordarlo
> "Herón es para cuando los tres lados se dan el sermón". Si tienes los tres lados y ninguna altura, Herón es tu salvación. Además, recuerda que en un triángulo equilátero, la altura siempre divide la base exactamente en dos partes iguales.

---

## Procedimiento paso a paso

```text
PASO 1: Identificar la información disponible.
PASO 2: Seleccionar la estrategia:
        - SI tengo Base y Altura: Usar (Base × Altura) / 2.
        - SI tengo 3 Lados: Calcular semiperímetro (s) y usar Herón: √[s(s-a)(s-b)(s-c)].
        - SI es Equilátero (Lado): Usar (√3 / 4) × Lado².
        - SI es Equilátero (Solo Altura): Usar Pitágoras [h² + x² = (2x)²] para hallar 
          el valor de x (media base), duplicarlo para obtener la base y luego 
          calcular el área estándar.
PASO 3: Ejecutar operaciones (potencias y raíces primero, luego productos).
PASO 4: Expresar el resultado final con unidades cuadradas (cm², m², etc.).
```

---

## Ejemplos prácticos

```ad-example
**Ejemplo 1: Caso Básico (Base y Altura)**
Calcular el área de un triángulo con base $8m$ y altura $4m$.
- Fórmula: $A = \frac{b \cdot h}{2}$
- $A = \frac{8m \cdot 4m}{2} = \frac{32m^2}{2}$
- **Resultado:** $16m^2$
```

```ad-example
**Ejemplo 2: Triángulo Equilátero (Dado un lado)**
Hallar el área de un triángulo equilátero cuyo lado mide $6m$.
- Fórmula: $Area = \frac{\sqrt{3}}{4} \cdot L^2$
- $Area = \frac{\sqrt{3}}{4} \cdot 6^2 = \frac{\sqrt{3}}{4} \cdot 36 = 9\sqrt{3}$
- $Area \approx 9 \cdot 1.732$
- **Resultado:** $15.59m^2$ (Redondeado a dos decimales)
```

```ad-example
**Ejemplo 3: Fórmula de Herón (Tres lados conocidos)**
Hallar el área de un triángulo con lados $a=5m, b=6m, c=8m$.
1. Perímetro: $5+6+8 = 19m$.
2. Semiperímetro ($s$): $19 / 2 = 9.5m$.
3. Aplicar Herón: $A = \sqrt{9.5(9.5-5)(9.5-6)(9.5-8)}$
4. $A = \sqrt{9.5 \cdot 4.5 \cdot 3.5 \cdot 1.5} = \sqrt{224.4375}$
- **Resultado:** $14.98m^2$
```

```ad-example
**Ejemplo 4: Equilátero avanzado (Dada la altura - Método Pitágoras)**
Hallar el área de un triángulo equilátero con altura $h=5m$.
1. Planteamos Pitágoras en la mitad del triángulo: $h^2 + x^2 = (2x)^2$.
2. $5^2 + x^2 = 4x^2 \rightarrow 25 = 3x^2 \rightarrow x^2 = 25/3$.
3. $x = \sqrt{8.33} \approx 2.88m$ (Esto es media base).
4. Base total: $2 \cdot 2.88 = 5.76m$.
5. Área: $(5.76m \cdot 5m) / 2$.
- **Resultado:** $14.4m^2$
```

```ad-example
**Ejemplo 5: Aplicación Real ($USD)**
Un jardín triangular tiene base de $10m$ y altura de $12m$. El césped cuesta $5 USD/m^2$.
1. Área: $(10m \cdot 12m) / 2 = 60m^2$.
2. Costo: $60m^2 \cdot 5 USD/m^2$.
- **Resultado:** $300 USD$
```

---

## Ejercicios para el estudiante

```ad-abstract
### 🟢 Nivel Fácil (Base y Altura)
1. Base = $5cm$, Altura = $10cm$.
2. Base = $4m$, Altura = $6m$.
3. Base = $7cm$, Altura = $8cm$.
4. Base = $12m$, Altura = $3m$.

### 🟡 Nivel Medio (Equilátero y Herón)
1. Triángulo equilátero de lado $10m$. (Usa fórmula específica).
2. Triángulo con lados de $3cm, 4cm$ y $5cm$. *(Nota: ¿Notas algo especial en este triángulo y el Teorema de Pitágoras?)*.
3. Triángulo equilátero con altura $h = 10cm$. (Usa el método de Pitágoras).
4. Triángulo con lados de $7m, 8m$ y $9m$. (Usa Herón).

### 🔴 Nivel Avanzado (Aplicación $USD)
Calcula el costo de cristales para ventanas triangulares ($25 USD/m^2$):
1. Ventana A: Base $2m$, Altura $2m$.
2. Ventana B: Base $4m$, Altura $5m$.
3. Ventana C: Triángulo equilátero de lado $2m$.
4. Ventana D: Base $6m$, Altura $2m$.
```

```ad-success
### ✅ Respuestas (para el docente)
**Fácil:** 1) $25cm^2$, 2) $12m^2$, 3) $28cm^2$, 4) $18m^2$.
**Medio:** 
1) $43.30m^2$.
2) $6cm^2$ (Es un triángulo rectángulo, $3^2+4^2=5^2$).
3) $57.74cm^2$ ($x \approx 5.773$, Base $\approx 11.547$).
4) $26.83m^2$.
**Avanzado:** 
1) $50 USD$.
2) $250 USD$.
3) $43.30 USD$ (Área $\approx 1.732m^2$).
4) $150 USD$.
```

---

## Autoevaluación

```ad-question
**Pregunta 1 (Conceptual):** Si solo conoces los tres lados de un triángulo escaleno, ¿qué método es obligatorio utilizar?
*(Respuesta: La Fórmula de Herón)*
```

```ad-question
**Pregunta 2 (Procedimental):** Un triángulo tiene un área de $20m^2$ y su base mide $10m$. ¿Cuál es su altura?
*(Respuesta: 4m, ya que (10 * 4) / 2 = 20)*
```

```ad-question
**Pregunta 3 (Aplicación $USD):** Un cartel triangular tiene una base de $2m$ y una altura de $3m$. Si la impresión cuesta $10 USD/m^2$, ¿cuál es el costo total?
*(Respuesta: 30 USD)*
```

---

> [!tip] 💡 En la próxima clase
> Analizaremos las propiedades de polígonos regulares y profundizaremos en el Teorema de Pitágoras aplicado a figuras compuestas para hallar dimensiones ocultas.

> [!info] 🧭 Navegación
> - **Anterior:** [[Clase 04 — Perímetros y conceptos básicos]]
> - **Siguiente:** [[Clase 06 — Propiedades de polígonos y Pitágoras avanzado]]