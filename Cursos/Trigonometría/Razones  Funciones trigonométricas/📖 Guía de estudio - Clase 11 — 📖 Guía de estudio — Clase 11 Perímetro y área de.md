# 📖 Guía de estudio — Clase 11: Perímetro y área de un paralelogramo conociendo sus lados y ángulo interno

> [!info] 📌 Conceptos clave
> ¡Qué tal amigos! Para dominar el cálculo de superficies en paralelogramos, es fundamental que comprendan estos principios que les ayudarán a no cometer errores comunes:
> * **La altura ($h$) es el secreto:** No podemos calcular el área simplemente multiplicando los dos lados conocidos. El área requiere la altura, y ¡mucho cuidado aquí!, la altura **no es lo mismo** que el lado inclinado. 
> * **El triángulo "escondido":** Al trazar una línea perpendicular desde un vértice hacia la base, formamos un triángulo rectángulo. Esta es la clave para usar herramientas potentes como el Teorema de Pitágoras o la Trigonometría.
> * **Seno ($\sin$) al rescate:** Como la altura del paralelogramo es el cateto opuesto del ángulo interno, usamos la razón **Seno** para encontrarla, relacionando el lado lateral (hipotenusa) con dicho ángulo.
> * **Unidades correctas:** No olviden que el perímetro se mide en **unidades lineales** (m, cm), mientras que el área, al ser una superficie, siempre va en **unidades cuadradas** ($m^2$, $cm^2$).

### Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Perímetro ($P$)** | Es la suma de todos los lados: $P = 2a + 2b$ |
| **Área ($A$)** | Es el producto de la base por su altura: $A = b \cdot h$ |
| **Seno del ángulo ($\sin \theta$)** | Razón fundamental: $\sin \theta = \frac{\text{Cateto Opuesto}}{\text{Hipotenusa}}$ |
| **Altura ($h$)** | Cálculo directo: $h = \text{lado lateral} \cdot \sin(\text{ángulo})$ |

---

### Ejemplos resueltos paso a paso

```ad-example
title: Ejemplo A: Caso Básico
**Datos:** Un paralelogramo con base de $10\text{ m}$, lado lateral de $7\text{ m}$ y un ángulo interno de $60^\circ$.

*   **Paso 1: Descubrimos la altura ($h$)**
    ¡Vamos a buscar esa altura escondida! Usamos el lado lateral como hipotenusa:
    $h = 7\text{ m} \cdot \sin(60^\circ)$
    $h \approx 7\text{ m} \cdot 0.866 = 6.06\text{ m}$

*   **Paso 2: Calculamos el área ($A$)**
    Ahora que tenemos la base y la altura real:
    $A = 10\text{ m} \cdot 6.06\text{ m} = 60.6\text{ m}^2$

*   **Paso 3: Calculamos el perímetro ($P$)**
    Sumamos los cuatro lados (recuerda que son iguales dos a dos):
    $P = 10\text{ m} + 10\text{ m} + 7\text{ m} + 7\text{ m} = 34\text{ m}$
```

```ad-example
title: Ejemplo B: Aplicación Real (Venta de Terreno)
**Escenario:** Imagina que vas a vender un terreno con forma de paralelogramo. La base mide $14\text{ m}$, el lado lateral $9\text{ m}$ y tiene un ángulo de $56^\circ$. El precio es de $\$50\text{ USD}$ por metro cuadrado.

*   **Paso 1: Hallamos la altura del terreno**
    $h = 9\text{ m} \cdot \sin(56^\circ)$
    $h \approx 9\text{ m} \cdot 0.829 = 7.46\text{ m}$

*   **Paso 2: Calculamos la superficie total (Área)**
    $A = 14\text{ m} \cdot 7.46\text{ m} = 104.44\text{ m}^2$

*   **Paso 3: Perímetro de seguridad**
    Para conocer los límites del terreno: $P = 14 + 14 + 9 + 9 = 46\text{ m}$

*   **Paso 4: Determinamos el valor de venta**
    $\text{Precio Total} = 104.44 \text{ m}^2 \cdot 50\text{ USD/m}^2 = \$5,222$

**Resultado:** El terreno tiene un costo total de **$\$5,222\text{ USD}$**.
```

---

### Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel Fácil: Cálculo de Perímetro
Calcula el perímetro de los siguientes paralelogramos:
1. Lados de $5\text{ cm}$ y $8\text{ cm}$. *(R: 26 cm)*
2. Lados de $12\text{ m}$ y $4\text{ m}$. *(R: 32 m)*
3. Lados de $15.5\text{ cm}$ y $10\text{ cm}$. *(R: 51 cm)*
```

```ad-abstract
title: 🟡 Nivel Medio: Altura y Área
Encuentra la altura ($h$) y el área ($A$) para los siguientes casos:
1. Base: $12\text{ cm}$, Lado: $6\text{ cm}$, Ángulo: $45^\circ$. *(R: h ≈ 4.24 cm, A ≈ 50.91 cm²)*
2. Base: $20\text{ m}$, Lado: $10\text{ m}$, Ángulo: $30^\circ$. *(R: h = 5 m, A = 100 m²)*
3. Base: $15\text{ cm}$, Lado: $8\text{ cm}$, Ángulo: $75^\circ$. *(R: h ≈ 7.73 cm, A ≈ 115.91 cm²)*
```

```ad-abstract
title: 🔴 Nivel Avanzado: Aplicación Económica
Un jardín con forma de paralelogramo tiene lados de $20\text{ m}$ y $15\text{ m}$ con un ángulo de $70^\circ$. Si el costo de colocar césped es de $\$12\text{ USD}$ por metro cuadrado:
1. Calcula la altura del jardín. *(R: h ≈ 14.10 m)*
2. Determina el área total. *(R: A ≈ 281.91 m²)*
3. ¿Cuál es el costo total para cubrir el jardín? *(R: $3,382.92 USD)*
```

---

> [!tip] 💡 Consejo de estudio
> ¿Qué fue lo bueno de esto? Que la tecnología nos ayuda, pero ¡ojo con la calculadora! Antes de empezar, verifica que en la pantalla aparezca una **"D"** o la palabra **"DEG"** (Degrees). Si ves una "R" (Radianes) o una "G" (Gradianes), tus cálculos del seno serán incorrectos y todo el ejercicio fallará. ¡Asegúrate de estar en grados sexagesimales!