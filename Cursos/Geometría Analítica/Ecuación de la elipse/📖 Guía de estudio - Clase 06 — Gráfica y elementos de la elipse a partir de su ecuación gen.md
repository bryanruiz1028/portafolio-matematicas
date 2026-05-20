# 📖 Guía de estudio — Clase 06: Gráfica y elementos de la elipse a partir de su ecuación general

> [!INFO] **Conceptos Clave de la Elipse**
> *   **Diferenciación Visual:** Para identificar el centro rápidamente, observa los términos. Si solo ves $x^2$ y $y^2$, el centro está en el origen $(0,0)$. **¡Ojo!** Si ves una $x$ o una $y$ "suelta" (términos lineales sin exponente), el centro se ha desplazado a un punto $(h,k)$.
> *   **Objetivo Primordial:** Nuestra misión es transformar la ecuación general a su **forma canónica**. Solo así podremos "leer" los elementos necesarios para graficar.
> *   **Orientación:** La elipse manda. Si el denominador mayor está debajo de las $x$, es **horizontal**. Si el mayor está debajo de las $y$, es **vertical**.
> *   **Teorema de Pitágoras Adaptado:** Para hallar la distancia focal ($c$), usamos la relación: $c^2 = a^2 - b^2$. No la confundas con la suma tradicional; aquí siempre restamos el menor al mayor.

---

### 📊 Tabla de Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Centro $(h,k)$** | Punto central de la elipse. **Importante:** Al extraerlo de la ecuación canónica, se deben cambiar los signos de $h$ y $k$. |
| **Semieje mayor ($a$)** | Distancia del centro al vértice principal. Se halla como: $a = \sqrt{\text{denominador mayor}}$. |
| **Semieje menor ($b$)** | Distancia del centro al vértice secundario. Se halla como: $b = \sqrt{\text{denominador menor}}$. |
| **Distancia focal ($c$)** | Distancia del centro a cada foco. Fórmula: $c = \sqrt{a^2 - b^2}$. |
| **Lado Recto ($LR$)** | Indica el "ancho" de la elipse al pasar por los focos: $LR = \frac{2b^2}{a}$. |

---

### 📝 Ejemplos Resueltos

```ad-example
**Ejemplo A: Caso Básico (Centro 0,0)**
**Ecuación:** $x^2 + 4y^2 - 16 = 0$

1. **Trasladar el término independiente:** Movemos el $-16$ al lado derecho: $x^2 + 4y^2 = 16$.
2. **Igualar a 1:** Para que sea canónica, dividimos todo entre 16: $\frac{x^2}{16} + \frac{4y^2}{16} = \frac{16}{16}$.
3. **Simplificar:** Reducimos las fracciones: $\frac{x^2}{16} + \frac{y^2}{4} = 1$.
4. **Extraer elementos:**
   * **Centro:** $(0,0)$.
   * **a:** $\sqrt{16} = 4$.
   * **b:** $\sqrt{4} = 2$.
   * **c:** $\sqrt{16 - 4} = \sqrt{12} \approx 3.4$.
**Conclusión:** Es una elipse horizontal (el 16 está bajo la $x$) centrada en el origen.
```

```ad-example
**Ejemplo B: Diseño de Pista Elíptica (Centro h,k)**
**Contexto:** Se proyecta una pista donde cada unidad representa el costo de materiales en USD.
**Ecuación:** $4x^2 - 40x + 9y^2 + 54y + 145 = 0$

1. **Agrupar y trasladar:** $(4x^2 - 40x) + (9y^2 + 54y) = -145$.
2. **Factorizar coeficientes principales:** $4(x^2 - 10x) + 9(y^2 + 6y) = -145$.
3. **Completar el trinomio cuadrado perfecto:** 
   * Dividimos el término medio entre 2 y elevamos al cuadrado: $(10/2)^2 = 25$ y $(6/2)^2 = 9$.
   * **Paso crítico (Compensación):** Lo que sumamos dentro debe sumarse fuera multiplicado por el factor externo.
   * $4(x^2 - 10x + 25) + 9(y^2 + 6y + 9) = -145 + \mathbf{100} + \mathbf{81}$ 
   *(Nota: $4 \times 25 = 100$ y $9 \times 9 = 81$)*.
4. **Simplificar:** $4(x-5)^2 + 9(y+3)^2 = 36$.
5. **Forma Canónica:** Dividimos todo entre 36 y simplificamos:
   $\frac{(x-5)^2}{9} + \frac{(y+3)^2}{4} = 1$.

**Elementos extraídos:**
* **Centro:** Al sacar los valores de los paréntesis, invertimos signos: **$(5, -3)$**.
* **Semiejes:** $a = \sqrt{9} = 3$ y $b = \sqrt{4} = 2$.
```

---

### ✍️ Ejercicios de Repaso

```ad-abstract
**Nivel Fácil (Verde)**
Dada la ecuación $25x^2 + 4y^2 - 100 = 0$:
1. Transforma a la forma canónica e identifica el centro.
2. Calcula los valores de $a$ y $b$.
```

```ad-abstract
**Nivel Medio (Amarillo)**
Dada la ecuación $25x^2 + 200x + 9y^2 - 36y + 211 = 0$:
1. Realiza el proceso de completar cuadrados para llegar a la forma canónica.
2. Determina si la orientación es horizontal o vertical.
```

```ad-abstract
**Nivel Avanzado (Rojo - Aplicación USD)**
Basándote en la ecuación del nivel medio:
1. Calcula la medida del **Lado Recto ($LR$)**.
2. **Problema:** Se deben instalar cables de seguridad que crucen la elipse verticalmente justo sobre los focos (longitud del $LR$). Si cada metro de cable cuesta $15 USD, ¿cuál es el presupuesto total para cubrir **ambos focos**?

**Pista:** No olvides que una elipse tiene dos focos; el cálculo del costo debe considerar la longitud del Lado Recto multiplicada por dos.
```

---

> [!TIP] **Estrategia Visual de Orientación**
> Para no perderte al graficar, usa flechas guía. Al calcular $a$ y $b$, mira bajo qué letra estaba el denominador original. Si $a$ viene de debajo de la $x$, dibuja una flecha horizontal ($\leftrightarrow$) junto a su valor. Si viene de la $y$, dibuja una vertical ($\updownarrow$). Esto te dirá instantáneamente en qué dirección moverte desde el centro.