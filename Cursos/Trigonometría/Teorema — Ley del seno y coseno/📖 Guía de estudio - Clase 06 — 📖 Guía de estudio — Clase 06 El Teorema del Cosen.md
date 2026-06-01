# 📖 Guía de estudio — Clase 06: El Teorema del Coseno

> [!info] 📌 Conceptos clave
> - **Triángulos oblicuángulos:** Son aquellos que no presentan un ángulo recto ($90^\circ$). Al no ser rectángulos, no podemos aplicar directamente el Teorema de Pitágoras tradicional ni las razones trigonométricas básicas ($\text{sen}, \text{cos}, \text{tan}$), por lo que recurrimos a este teorema.
> - **Nomenclatura estándar:** Es fundamental para no perdernos en los cálculos. Usamos letras mayúsculas ($A, B, C$) para los ángulos y letras minúsculas ($a, b, c$) para los lados. **Regla de oro:** El lado $a$ siempre debe estar frente al ángulo $A$, el lado $b$ frente al $B$, y el lado $c$ frente al $C$.
> - **Casos de aplicación:** ¡No te compliques! Solo lo usaremos en dos situaciones específicas:
>     1. **Lado-Ángulo-Lado (LAL):** Conoces dos lados y el ángulo que forman entre ellos.
>     2. **Lado-Lado-Lado (LLL):** Conoces la medida de los tres lados y necesitas hallar los ángulos.
> - **Relación con Pitágoras:** ¡Es un viejo conocido! Observa que la fórmula comienza como $a^2 = b^2 + c^2$. El término extra ($- 2bc \cos(A)$) actúa como un **término de corrección** que ajusta la fórmula cuando el ángulo no es de $90^\circ$.

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Uso del Teorema** | Resolver triángulos oblicuángulos (casos LAL y LLL). |
| **Para hallar el lado $a$** | $a^2 = b^2 + c^2 - 2bc \cdot \cos(A)$ |
| **Para hallar el lado $b$** | $b^2 = a^2 + c^2 - 2ac \cdot \cos(B)$ |
| **Para hallar el lado $c$** | $c^2 = a^2 + b^2 - 2ab \cdot \cos(C)$ |
| **Para hallar un ángulo ($A$)** | $A = \arccos\left(\frac{a^2 - b^2 - c^2}{-2bc}\right)$ |

---

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Hallar un lado (Caso LAL)
**Enunciado:** En un triángulo oblicuángulo, los lados conocidos son $b = 12m$ y $c = 7m$. El ángulo comprendido entre ellos es $A = 40^\circ$. Calcula la medida del lado $a$.

**Paso 1: Sustitución en la fórmula**
Como buscamos el lado $a$, seleccionamos su fórmula correspondiente y reemplazamos los valores:
$a^2 = 12^2 + 7^2 - 2(12)(7) \cdot \cos(40^\circ)$

**Paso 2: Aplicación de raíz cuadrada**
Para despejar $a$, eliminamos el cuadrado aplicando la raíz en ambos lados de la igualdad:
$a = \sqrt{12^2 + 7^2 - 2(12)(7) \cdot \cos(40^\circ)}$

**Paso 3: Uso de la calculadora**
Introducimos la operación asegurándonos de que la calculadora esté en modo **DEG**. Es vital usar paréntesis para que la raíz cubra toda la expresión.

**Resultado final:**
$a \approx 8,01m$
```

```ad-example
title: Ejemplo B — Aplicación en construcción (Costos $USD)
**Enunciado:** Un ingeniero necesita medir el tercer lado de un terreno triangular para colocar una cerca. Los lados adyacentes miden $19m$ y $9m$, formando un ángulo de $65^\circ$. Si el metro de cerca cuesta $\$15$ USD, ¿cuánto costará cercar este lado?

**Paso 1: Hallar la longitud del lado ($a$)**
Sustituimos los datos de la Fuente 4:
$a = \sqrt{19^2 + 9^2 - 2(19)(9) \cdot \cos(65^\circ)}$
$a \approx 17,25m$ (valor redondeado a dos decimales).

**Paso 2: Cálculo del presupuesto**
Multiplicamos la longitud obtenida por el precio unitario:
$17,25m \times \$15 \, \text{USD/m} = \$258,75 \, \text{USD}$

**Resultado:** El costo total para cercar ese lado es de **$\$258,75$ USD**.
```

---

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil
¡Ideal para calentar motores!
1. Calcula el lado $a$ de un triángulo si $b = 12$, $c = 14$ y el ángulo $A = 35^\circ$.
2. Determina el tercer lado de un triángulo cuyos lados conocidos miden $7m$ y $10m$, con un ángulo de $58^\circ$ entre ellos.
*(Respuestas sugeridas: 1) $\approx 8,04$; 2) $\approx 8,65$)*
```

```ad-abstract
title: 🟡 Medio
**Resolver el triángulo:** Halla los tres ángulos internos ($A, B$ y $C$) de un triángulo con lados $a = 6m$, $b = 14m$ y $c = 11m$.
**Nota pedagógica:** Empieza hallando el ángulo $A$ con la fórmula de arcocoseno, luego el $B$, y finalmente resta ambos a $180^\circ$ para obtener el $C$.
*(Respuestas: $A \approx 24,17^\circ$; $B \approx 107,18^\circ$; $C \approx 48,65^\circ$)*
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
Un proyecto de urbanización requiere pavimentar dos senderos nuevos en un parque triangular.
1. El primer sendero ($AC$) conecta los puntos $A$ y $C$. Se sabe que $AB = 13m$, $BC = 9m$ y el ángulo en $B$ es de $45^\circ$.
2. El segundo sendero ($AD$) conecta el punto $A$ con un nuevo punto $D$. Sabemos que $AC$ (calculado antes) y $CD = 15m$ forman un ángulo $\angle ACD = 110^\circ$.

Si el costo de pavimentación es de **$\$120$ USD por metro lineal**, calcula el presupuesto total para construir ambos senderos ($AC + AD$).
```

---

> [!tip] 💡 Consejo de estudio
> ¡Atención aquí! El error más común no es matemático, sino de uso de herramienta. 
> 1. **Modo de la calculadora:** Verifica que aparezca una **"D"** o **"DEG"** en la pantalla. Si dice "R" o "RAD", tus resultados serán incorrectos.
> 2. **Uso de paréntesis:** Al calcular una raíz, la calculadora debe entender que *todo* está adentro. Escríbelo así: `√ ( 19^2 + 9^2 - 2 * 19 * 9 * cos(65) )`. Si tu calculadora abre un paréntesis en el `cos(`, no olvides cerrarlo antes del paréntesis final. ¡Tú puedes!