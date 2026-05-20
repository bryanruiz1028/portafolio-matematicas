# 📖 Guía de estudio — Clase 05: De la Ecuación General a la Ordinaria de la Hipérbola

> [!info] 📌 Conceptos clave
> *   **Formatos de la ecuación**: La **ecuación general** se reconoce por estar igualada a cero ($Ax^2 + By^2 + Cx + Dy + E = 0$), mientras que la **ordinaria o canónica** está igualada a 1, permitiendo identificar el centro y los semiejes.
> *   **Identificación visual**: Una ecuación de segundo grado representa una hipérbola si los coeficientes de $x^2$ y $y^2$ tienen **signos opuestos**.
> *   **Eje Real (Principal)**: La orientación (horizontal o vertical) la define la **fracción positiva**. Si el término con $x$ es positivo, el eje real es horizontal; si el término con $y$ es positivo, el eje real es vertical.
> *   **Completación y Balanceo**: Para transformar la ecuación, es vital completar el trinomio cuadrado perfecto y "balancear" el otro lado de la igualdad sumando los términos agregados multiplicados por su respectivo factor común.
> *   **Estrategia de la "Fracción de Fracción"**: Si al simplificar el coeficiente del binomio no divide exactamente al denominador (ej. $2(x-h)^2 / 3$), se aplica la propiedad $n \cdot \frac{X}{D} = \frac{X}{D/n}$. Así, el coeficiente pasa a ser el denominador del denominador (ej. $\frac{(x-h)^2}{1.5}$).

---

## 2. Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Centro (h, k)** | Punto central. En la ecuación ordinaria, se extrae con **signos opuestos** a los que acompañan a $x$ y $y$. |
| **Parámetro 'a'** | Semieje real (distancia centro-vértice). $a = \sqrt{\text{denominador de la fracción positiva}}$. |
| **Parámetro 'b'** | Semieje imaginario/conjugado. $b = \sqrt{\text{denominador de la fracción negativa}}$. |
| **Distancia Focal 'c'** | Distancia del centro a los focos. Se calcula como: $c = \sqrt{a^2 + b^2}$. |
| **Lado Recto (LR)** | Ancho de la hipérbola en los focos: $LR = \frac{2b^2}{a}$. |
| **Vértices (V)** | **Horizontal**: $(h \pm a, k)$ <br> **Vertical**: $(h, k \pm a)$ |
| **Focos (F)** | **Horizontal**: $(h \pm c, k)$ <br> **Vertical**: $(h, k \pm c)$ |

---

## 3. Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Caso básico (Centro en el origen)
**Problema**: Convertir la ecuación $-9x^2 + 4y^2 - 36 = 0$ a su forma ordinaria.

**Procedimiento**:
1. **Trasponer el término independiente**: Pasamos el $-36$ al lado derecho.
   $-9x^2 + 4y^2 = 36$
2. **Igualar a 1**: Dividimos toda la expresión entre $36$.
   $\frac{-9x^2}{36} + \frac{4y^2}{36} = \frac{36}{36}$
3. **Simplificar**: 
   - Para $x$: Novena de 9 es 1, novena de 36 es 4 $\rightarrow -\frac{x^2}{4}$
   - Para $y$: Cuarta de 4 es 1, cuarta de 36 es 9 $\rightarrow \frac{y^2}{9}$
4. **Ordenar (Fracción positiva primero)**: 
   $\frac{y^2}{9} - \frac{x^2}{4} = 1$

**Interpretación**: Es una hipérbola con **Eje Real Vertical** (abre hacia arriba y abajo) y centro en $(0,0)$.
```

```ad-example
title: Ejemplo B — Aplicación en diseño de trayectoria ($USD)
**Contexto**: Una pieza de acero industrial requiere un corte hiperbólico según la ecuación $9x^2 - 4y^2 - 18x - 24y - 63 = 0$. El costo del material depende de situar el centro de corte con precisión milimétrica.

**Proceso de transformación**:
1. **Agrupar términos**: $(9x^2 - 18x) + (-4y^2 - 24y) = 63$
2. **Factor común (coeficientes de $x^2$ y $y^2$)**: 
   $9(x^2 - 2x) - 4(y^2 + 6y) = 63$
3. **Completar cuadrados**: Dividimos el segundo término entre 2 y elevamos al cuadrado.
   $9(x^2 - 2x + \mathbf{1}) - 4(y^2 + 6y + \mathbf{9}) = 63 + \dots$
4. **Balanceo**: Sumamos al lado derecho los productos de los términos agregados.
   $63 + (9 \times 1) + (-4 \times 9) \Rightarrow 63 + 9 - 36 = 36$
5. **Factorizar binomios e igualar a 1**:
   $9(x - 1)^2 - 4(y + 3)^2 = 36 \Rightarrow \frac{9(x-1)^2}{36} - \frac{4(y+3)^2}{36} = \frac{36}{36}$
6. **Simplificación final**:
   $\frac{(x-1)^2}{4} - \frac{(y+3)^2}{9} = 1$

**Conclusión técnica**: Para que el corte sea preciso, el operario debe configurar el centro de la trayectoria en las coordenadas **(1, -3)**.
```

---

## 4. Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel Fácil
1. Pase a la forma ordinaria: $16x^2 - 9y^2 - 144 = 0$.
2. Identifique la orientación y el centro de: $4y^2 - 9x^2 - 36 = 0$.
```

```ad-abstract
title: 🟡 Nivel Medio
Dada la ecuación general $8x^2 - 12y^2 + 112x + 120y - 4 = 0$:
*   **Reto**: Obtenga la ecuación ordinaria y determine las coordenadas del centro $(h, k)$.
*   *Ayuda*: Al balancear, obtendrá 96 en el lado derecho. Simplifique los coeficientes 8 y 12 contra el 96.
```

```ad-abstract
title: 🔴 Nivel Avanzado — Aplicación con $USD
**Proyecto**: Se fabricará una antena hiperbólica cuyo costo es de **$150 USD por cada unidad del Lado Recto (LR)**. Determine el presupuesto total basándose en:
$10x^2 - 3y^2 - 40x - 6y + 22 = 0$

**Guía de resolución**:
1. Tras la completación y balanceo, llegará a $\frac{(x-2)^2}{1.5} - \frac{(y+1)^2}{5} = 1$.
2. Calcule $a$ (raíz de 1.5) y use $b^2 = 5$.
3. Aplique la fórmula del Lado Recto ($LR = 2b^2 / a$).
4. **Resultado esperado para verificación**: El costo total debe ser aproximadamente **$1,224.74 USD**.
```

---

> [!tip] 💡 Consejo de estudio: El secreto del balanceo
> El error más común en este tema es sumar los números directamente al lado derecho (ej. sumar +1 y +9). **¡No lo olvides!** Debes multiplicar cada número que agregas por el factor común que sacaste al inicio del paréntesis. Si no aplicas este "pesaje", la ecuación perderá su equilibrio y el resultado será incorrecto.