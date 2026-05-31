# 📖 Guía de estudio — Clase 10: Razones Trigonométricas y Resolución de Problemas

> [!info] 📌 Conceptos fundamentales de didáctica aplicada
> Para dominar la resolución de problemas trigonométricos, no basta con aplicar fórmulas; es necesario desarrollar una visión geométrica y técnica. Basándonos en las lecciones del Profe Alex, sintetizamos los siguientes pilares:
> 1. **Abstracción Geométrica:** No pierda tiempo en dibujos artísticos. Represente la realidad mediante **líneas y puntos**. Un edificio es una línea vertical, el suelo es una línea horizontal y el sol es un punto. El objetivo es que todo problema se reduzca a un **triángulo rectángulo**.
> 2. **Ángulo de Elevación y "Límite de Luz":** Se define como el ángulo formado entre la línea horizontal de visión y la visual hacia un objeto elevado. En problemas de sombras, este ángulo representa la trayectoria del rayo de sol que pasa justo por la punta (cúspide) del objeto, delimitando dónde termina la sombra.
> 3. **Configuración Crítica de la Calculadora:** Antes de iniciar, verifique que su calculadora esté en **modo grados (D o Degree)**. Si opera en Radianes (R) o Gradianes (G), sus resultados serán erróneos. **Regla de oro:** Al usar funciones inversas, use siempre paréntesis para agrupar las fracciones; esto evita errores de jerarquía de operaciones.
> 4. **Anatomía del Triángulo según el Ángulo ($\theta$):**
>    - **Hipotenusa:** Lado opuesto al ángulo recto ($90^\circ$). Siempre es el más largo.
>    - **Cateto Opuesto:** Lado que está frente al ángulo de referencia.
>    - **Cateto Adyacente:** Lado que forma parte del ángulo de referencia (junto a la hipotenusa).

## Fórmulas y definiciones técnicas

| Término | Definición / Fórmula | Aplicación Didáctica |
| :--- | :--- | :--- |
| **Seno (sen)** | $\text{sen}(\theta) = \frac{\text{Cateto Opuesto}}{\text{Hipotenusa}}$ | Se usa cuando se conoce o busca el lado frente al ángulo y la hipotenusa. |
| **Coseno (cos)** | $\cos(\theta) = \frac{\text{Cateto Adyacente}}{\text{Hipotenusa}}$ | Vincula el lado base (adyacente) con la diagonal (hipotenusa). |
| **Tangente (tan)** | $\tan(\theta) = \frac{\text{Cateto Opuesto}}{\text{Cateto Adyacente}}$ | Es la función más común para medir alturas desde el suelo. |
| **Ángulo (Inversa)** | $\theta = \tan^{-1}\left(\frac{\text{Opuesto}}{\text{Adyacente}}\right)$ | Se usa para aislar el valor de $\theta$ cuando se conocen los dos catetos. |

---

## Ejemplos resueltos con enfoque metodológico

```ad-example
title: Ejemplo A — Cálculo de altura y dibujo predictivo
**Enunciado:** Desde un punto a 80 metros de la base de un edificio, el ángulo de elevación a la cúspide es de $52^\circ$. Calcule la altura.

**Proceso Lógico:**
1. **Dibujo Predictivo:** Dibujamos una base de $8$ unidades (representando $80$ m) y usamos el transportador para marcar $52^\circ$. Al cerrar el triángulo, observamos visualmente que la altura debe ser mayor a la base (ya que el ángulo es $> 45^\circ$). Estimamos unos $100$ m.
2. **Identificación:** Ángulo $\theta = 52^\circ$; Adyacente $= 80$ m; Opuesto (Altura) $= x$.
3. **Ecuación:** $\tan(52^\circ) = \frac{x}{80}$.
4. **Despeje:** $x = 80 \cdot \tan(52^\circ) \rightarrow x = 80 \cdot (1.2799)$.
✅ **Resultado:** La altura es **102.39 metros**. (Coincide con nuestra predicción visual).
```

```ad-example
title: Ejemplo B — Topografía avanzada (Uso de Teodolito y Sistemas 2x2)
**Enunciado:** Un topógrafo usa un **teodolito** para medir la altura de una montaña. En el punto A, el ángulo es de $23^\circ$. Tras avanzar $1$ km hacia la base, el ángulo sube a $43^\circ$. El costo del estudio es de $\$1.50$ USD por cada metro medido. ¿Cuál es el presupuesto?

**Proceso Lógico (Método de Igualación):**
1. **Definir variables:** $x = \text{altura de la montaña}$; $y = \text{distancia desde el segundo punto a la base}$.
2. **Planteamiento de Ecuaciones:**
   - Triángulo 1 ($43^\circ$): $\tan(43^\circ) = \frac{x}{y} \rightarrow x = y \cdot \tan(43^\circ)$
   - Triángulo 2 ($23^\circ$): $\tan(23^\circ) = \frac{x}{y+1} \rightarrow x = (y+1) \cdot \tan(23^\circ)$
3. **Igualación y Propiedad Distributiva:**
   $y \cdot \tan(43^\circ) = (y + 1) \cdot \tan(23^\circ)$
   $y \cdot \tan(43^\circ) = y \cdot \tan(23^\circ) + 1 \cdot \tan(23^\circ)$
4. **Resolución:** Agrupamos términos con $y$:
   $y(\tan(43^\circ) - \tan(23^\circ)) = \tan(23^\circ)$
   $y = \frac{\tan(23^\circ)}{\tan(43^\circ) - \tan(23^\circ)} \approx 0.8355 \text{ km}$
5. **Cálculo de Altura ($x$):** $x = 0.8355 \cdot \tan(43^\circ) \approx 0.7791 \text{ km} = 779.1 \text{ m}$.
6. **Presupuesto:** $779.1 \text{ m} \cdot \$1.50/\text{m} = \$1,168.65$ USD.
✅ **Resultado:** Altura $779.1$ m | **Presupuesto total: $1,168.65 USD.**
```

---

## Ejercicios de refuerzo

```ad-abstract
title: 🟢 Nivel Inicial
1. **El poste y la sombra:** Un poste de $4.5$ m proyecta una sombra de $5.3$ m. Calcule el ángulo de elevación del sol.
   *Ayuda:* Use $\theta = \tan^{-1}(4.5 / 5.3)$. Recuerde los paréntesis en la calculadora.
2. **La rampa técnica:** Una rampa de ciclismo tiene un **largo de superficie** (hipotenusa) de $12$ m y una altura de $2.3$ m. ¿Cuál es su ángulo de elevación?
   *Nota didáctica:* En rampas, el "largo" suele referirse a la hipotenusa. Use la función Seno.
```

```ad-abstract
title: 🟡 Nivel Intermedio
1. **La cometa:** El hilo de una cometa mide $95$ m y forma un ángulo de $25^\circ$ con el suelo. Estime la altura de la cometa. 
   *Predicción:* Si el ángulo es pequeño ($25^\circ$), la altura debe ser considerablemente menor a la hipotenusa.
2. **Sombra proyectada:** Un edificio de altura desconocida proyecta una sombra de $100$ m cuando el sol está a $30^\circ$. Calcule la altura.
```

```ad-abstract
title: 🔴 Nivel Avanzado (Scaffolding Técnico)
**Problema del Barco y el Sensor:** Desde un barco se ve la cima de una montaña con $24^\circ$ de elevación. Tras acercarse $300$ m, el ángulo sube a $36^\circ$. Instalar un sensor cuesta $\$500$ USD fijos + $\$2$ USD por metro de altura. Calcule el costo total.

**Guía de resolución paso a paso:**
- **Paso 1:** Plantee la ecuación del triángulo de $36^\circ$ ($x = y \cdot \tan(36^\circ)$).
- **Paso 2:** Plantee la del triángulo de $24^\circ$ ($x = (y + 300) \cdot \tan(24^\circ)$).
- **Paso 3:** Iguale y despeje la altura $x$. (Debe obtener aproximadamente $344.96$ m).
- **Paso 4:** Aplique la fórmula financiera: $\text{Costo} = 500 + (x \cdot 2)$.
✅ **Resultado esperado:** $1,189.92$ USD.
```

> [!tip] 💡 Consejo de estudio del especialista
> Use siempre **regla y transportador** para sus esquemas iniciales. Si el dibujo está a escala, usted puede "pre-calcular" la respuesta midiendo con la regla antes de tocar la calculadora. Esto desarrolla el sentido lógico-matemático y evita que acepte resultados absurdos derivados de un error de dedo en la calculadora.