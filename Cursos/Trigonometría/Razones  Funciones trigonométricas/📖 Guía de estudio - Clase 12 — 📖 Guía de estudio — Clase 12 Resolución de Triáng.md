# 📖 Guía de estudio — Clase 12: Resolución de Triángulos Rectángulos

> [!info] 📌 Conceptos clave
> Para dominar la resolución de triángulos, es fundamental comprender los siguientes pilares técnicos:
> *   **¿Qué es "resolver" un triángulo?**: Es el proceso matemático de calcular las medidas de todos los elementos faltantes, asegurando que al finalizar conozcamos el valor de los tres lados y los tres ángulos internos.
> *   **Condición indispensable**: Estos métodos son exclusivos para **triángulos rectángulos**, identificables por poseer un ángulo recto de $90^\circ$.
> *   **Escenarios de inicio**: Para iniciar la resolución, se requiere obligatoriamente conocer al menos dos datos:
>     1. Un lado y un ángulo agudo.
>     2. O bien, dos lados del triángulo.
> *   **Suma de ángulos internos**: En todo triángulo, los ángulos internos suman $180^\circ$. En el caso del triángulo rectángulo, como ya contamos con un ángulo de $90^\circ$, deducimos que la suma de los otros dos ángulos agudos debe ser siempre $90^\circ$ ($\alpha + \beta = 90^\circ$).

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Seno (sen)** | $\text{sen}(\theta) = \frac{\text{Cateto opuesto}}{\text{Hipotenusa}}$ |
| **Coseno (cos)** | $\cos(\theta) = \frac{\text{Cateto adyacente}}{\text{Hipotenusa}}$ |
| **Tangente (tan)** | $\tan(\theta) = \frac{\text{Cateto opuesto}}{\text{Cateto adyacente}}$ |
| **Ángulos Internos** | $\alpha + \beta = 90^\circ$ (Propiedad de ángulos complementarios). |
| **Inversa (arco)** | Se usan $\tan^{-1}, \text{sen}^{-1}, \cos^{-1}$ para hallar el valor de un ángulo. |

> [!tip] 💡 Tip tecnológico
> Para calcular funciones inversas en tu calculadora, generalmente debes presionar primero la tecla **SHIFT** o **INV** seguida de la función deseada ($\sin, \cos$ o $\tan$).

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Hallar lados conociendo un ángulo y un lado
**Enunciado:** Resuelve un triángulo donde el ángulo $\theta = 37^\circ$ y la hipotenusa mide $15$ m.

**Procedimiento:**
1. **Identificar datos:** Ángulo $\theta = 37^\circ$ e Hipotenusa ($H$) = $15$ m.
2. **Calcular Cateto Adyacente:** Aplicamos la razón de Coseno.
   $15 \cdot \cos(37^\circ) = 11.979... \approx 11.98$ m.
3. **Calcular Cateto Opuesto:** Aplicamos la razón de Seno.
   $15 \cdot \text{sen}(37^\circ) = 9.027... \approx 9.03$ m.
4. **Hallar el ángulo faltante:** Aplicamos la propiedad de ángulos complementarios.
   $90^\circ - 37^\circ = 53^\circ$.

✅ **Resultado:** Lados de $11.98$ m y $9.03$ m; ángulo restante de $53^\circ$.
```

```ad-example
title: Ejemplo B — Aplicación real: Instalación de cableado (USD)
**Enunciado:** Se desea instalar un cable tensor desde la punta de una antena hasta el suelo. El cable forma un ángulo de $56^\circ$ con el suelo y la distancia desde la base de la antena al punto de anclaje es de $6.75$ m (Cateto Adyacente). Si el metro de cable cuesta $5$ USD, ¿cuánto costará el cable?

**Procedimiento:**
1. **Identificar la incógnita:** El cable representa la **Hipotenusa**, ya que es el segmento que une el punto más alto con el suelo, siendo el lado opuesto al ángulo recto imaginario de la antena.
2. **Calcular la longitud del cable:** Usamos Coseno ($\cos = \text{adyacente} / \text{hipotenusa}$).
   $\text{Hipotenusa} = 6.75 / \cos(56^\circ)$.
   $6.75 / 0.5591 \approx 12.07$ m.
3. **Calcular costo total:** Multiplicamos la longitud real por el costo unitario.
   $12.07 \text{ m} \cdot 5 \text{ USD/m} = 60.35$ USD.

✅ **Resultado:** El costo total del cable será de **$60.35$ USD**.
```

## Ejercicios de repaso

```ad-abstract
title: 🟢 Nivel: Fácil
1. En un triángulo rectángulo con un ángulo de $32^\circ$ y un cateto adyacente de $7$ cm, ¿cuánto mide la hipotenusa? (Usa la fórmula del Coseno).
2. Si los dos ángulos agudos de un triángulo deben sumar $90^\circ$ y uno mide $56^\circ$, ¿cuánto mide el otro?
3. Identifica: ¿Cuál es el nombre técnico del lado que se encuentra exactamente opuesto al ángulo de $90^\circ$?
```

```ad-abstract
title: 🟡 Nivel: Medio
1. Un triángulo tiene catetos de $6$ m y $10$ m. Calcula el ángulo $\theta$ aplicando la función Tangente inversa ($\tan^{-1}$).
2. Utilizando el ángulo obtenido en el ejercicio anterior ($30.96^\circ$), calcula la medida de la hipotenusa usando la función Seno ($\text{sen}$).
3. Si un triángulo tiene una hipotenusa de $20$ m y un cateto adyacente de $11$ m, halla el valor del ángulo comprendido entre estos dos lados usando la función inversa correspondiente.
```

```ad-abstract
title: 🔴 Nivel: Avanzado — Aplicación con USD
1. Una rampa de carga mide $16.7$ metros de largo (hipotenusa). El ángulo de inclinación respecto al suelo es de $33.37^\circ$. Si construir la base de la rampa (cateto adyacente) cuesta $12$ USD por metro lineal, calcula el costo total de la construcción de dicha base.
```

> [!tip] 💡 Consejo de estudio del Profe Alex
> Antes de realizar cualquier cálculo, verifica que tu calculadora esté en modo **DEG** (grados sexagesimales). Si visualizas una **"R"** (radianes) o una **"G"** (gradianes) en la pantalla, los resultados de seno, coseno y tangente serán erróneos para estos ejercicios.