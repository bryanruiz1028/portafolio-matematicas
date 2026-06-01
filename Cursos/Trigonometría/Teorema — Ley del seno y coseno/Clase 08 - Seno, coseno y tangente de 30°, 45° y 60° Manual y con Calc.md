# Clase 08 — Seno, coseno y tangente de 30°, 45° y 60°: Manual y con Calculadora

#algebra #sinecosineandta

> [!info] **Navegación**
> [[Clase 07|⬅ Clase 07]] | [[00 - Índice del curso|Índice]] | [[Clase 09|Clase 09 ➡]]

---

## Relevancia y aplicaciones

> [!info] 🌍 **¿Por qué aprender esto?**
> Los ángulos de 30°, 45° y 60° son "ángulos especiales" que aparecen en la naturaleza y la ingeniería. Conocer sus valores fijos nos permite calcular distancias exactas y alturas inaccesibles sin necesidad de herramientas láser o cintas métricas kilométricas.

*   **💵 Aplicación $USD:** Al instalar un panel solar con una inclinación de 30°, el valor del seno es exactamente 0.5. Esto significa que la altura del soporte será siempre la mitad del largo del panel. Saber esto permite comprar la cantidad exacta de metros lineales de aluminio, evitando desperdicios de material costoso.
*   **🏗️ Aplicación práctica:** En la construcción de techos, se usan ángulos de 45° para las cerchas (soportes), asegurando que el peso se distribuya de forma simétrica y eficiente.
*   **📊 Situación cotidiana:** Si la sombra de un árbol forma un ángulo de 60° con el sol, puedes hallar su altura real midiendo solo la sombra en el suelo y multiplicándola por la tangente de 60°.

---

## Concepto clave

> [!note] **Los "Números Mágicos" de la Trigonometría**
> Imagina que tienes piezas de un juego que siempre encajan igual. Los ángulos de 30°, 45° y 60° son así. Sus valores de seno, coseno y tangente son proporciones fijas que provienen de figuras geométricas perfectas: el triángulo equilátero (dividido a la mitad) y el triángulo isósceles. No importa si el triángulo es pequeño como una regla o grande como una pirámide, ¡la proporción nunca cambia!

> [!warning] **¡Cuidado con el modo de la calculadora!**
> Un error común es obtener resultados extraños por tener la unidad angular incorrecta.
> *   **DEG (Degrees):** Para grados sexagesimales (30°, 45°, 60°). Debe aparecer una **"D"** en pantalla. ✅
> *   **RAD (Radians):** Para cuando el ángulo se mide en términos de $\pi$. Aparece una **"R"**. ❌ (Si calculas Sen 30 en este modo, el resultado será incorrecto).

> [!tip] **Truco experto para memorizar la tabla**
> Para construir la tabla en segundos, usa la "Regla de la Raíz":
> 1. Escribe los números del **0 al 4** para el Seno (y del **4 al 0** para el Coseno).
> 2. Saca la **raíz cuadrada** de cada número.
> 3. **Divide todo entre 2**.
> 
> | Ángulo | 0° | 30° | 45° | 60° | 90° |
> | :--- | :--- | :--- | :--- | :--- | :--- |
> | **Seno** | $\frac{\sqrt{0}}{2} = 0$ | $\frac{\sqrt{1}}{2} = \frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{4}}{2} = 1$ |
> | **Coseno** | $\frac{\sqrt{4}}{2} = 1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{1}}{2} = \frac{1}{2}$ | $\frac{\sqrt{0}}{2} = 0$ |

---

## Procedimiento paso a paso

Para obtener resultados precisos en tu calculadora Casio, sigue este flujo de trabajo:

```text
GUÍA DE CONFIGURACIÓN Y USO

PASO 1 → Verificar configuración inicial (Letra "D" en pantalla):
         • Classwiz: Shift + [Setup] -> Unidad Angular (2) -> Grado Sexagesimal (1).
         • MS: Presionar [Mode] dos veces -> Deg (1).

PASO 2 → Seleccionar la función:
         • Presiona [SIN], [COS] o [TAN].

PASO 3 → Ingresar el ángulo:
         • Digita el número. Si tiene minutos/segundos, usa la tecla [ ° ' '' ].
         • 🚨 TRUCO PRO: Si el ángulo no tiene minutos pero sí segundos 
           (ej. 20° 15''), DEBES ingresar el cero en minutos: 20 [°' ''] 0 [°' ''] 15 [°' ''].

PASO 4 → Interpretar el resultado:
         • Classwiz: Presiona [S-D] para cambiar de fracción a decimal.
         • MS: Usa la tecla [a b/c] o observa el decimal directo en pantalla.
```

---

## Ejemplos prácticos

*   **Ejemplo 1 (Básico): Seno de 30°**
    *   *Lógica del Maestro:* Usamos un triángulo equilátero de **lado 2**. ¿Por qué 2? Para que al dividir la base a la mitad, obtengamos un número entero (1) y no decimales molestos.
    *   *Manual:* $\text{Sen } 30^\circ = \frac{\text{Cateto Opuesto}}{\text{Hipotenusa}} = \frac{1}{2} = 0.5$.

*   **Ejemplo 2 (Simplificación): Tangente de 60°**
    *   *Manual:* En el mismo triángulo de lado 2, la altura es $\sqrt{3}$. 
    *   *Cálculo:* $\text{Tan } 60^\circ = \frac{\text{Cateto Opuesto}}{\text{Cateto Adyacente}} = \frac{\sqrt{3}}{1}$.
    *   *Resultado:* Se simplifica directamente a $\sqrt{3}$. (Nota: Si tuvieras $1/\sqrt{3}$, racionalizarías multiplicando por $\frac{\sqrt{3}}{\sqrt{3}}$ para obtener $\frac{\sqrt{3}}{3}$).

*   **Ejemplo 3 (Calculadora avanzada): Seno de 30° 40' 15''**
    *   *Pasos:* `SIN` `30` `[°' '']` `40` `[°' '']` `15` `[°' '']` `)`.
    *   **Resultado:** $\approx 0.5100$.

*   **Ejemplo 4 (Aplicación $USD):** Se requiere un cable de soporte para un poste con un ángulo de 45°. Si la hipotenusa (el cable) mide $10\sqrt{2}$ metros y el costo por metro es de $5.50 USD.
    *   *Paso 1:* Calculamos la longitud decimal: $10 \times \sqrt{2} \approx 10 \times 1.4142 = 14.142$ metros.
    *   *Paso 2:* Multiplicamos por el precio: $14.142 \times 5.50$.
    *   **Costo Total:** $77.78 USD.

---

## Ejercicios para el estudiante

### 🟢 Nivel Fácil (Sin calculadora)
1.  Halla el valor de **Cos 60°**.
2.  Halla el valor de **Tan 45°**.
3.  ¿Cuál es el valor del **Sen 45°** en forma de raíz?
4.  Calcula la **Cosecante de 30°** (Pista: es la inversa del Seno).

### 🟡 Nivel Medio (Uso de herramientas)
5.  Calcula la suma: $\text{Sen } 30^\circ + \text{Cos } 60^\circ$.
6.  Calcula usando calculadora: $\text{Tan } 20^\circ 0' 15''$ (No olvides marcar los 0 minutos).
7.  Halla el resultado de: $(\text{Sen } 45^\circ)^2$.
8.  Encuentra $x$ si $\text{Sen } x = 0.5$ (Usa la función inversa `SHIFT` + `SIN`).

### 🔴 Nivel Avanzado ($USD)
9.  Una rampa de carga tiene un ángulo de 30°. Si la rampa mide 10m de largo (hipotenusa) y el material de recubrimiento cuesta $120 USD por cada metro de altura alcanzada, ¿cuál es el costo?
10. Un terreno triangular tiene un ángulo de 60°. El cateto adyacente mide 20m. Si el metro cuadrado de césped cuesta $15 USD, calcula el costo total (Halla la altura primero con $\text{Tan } 60^\circ$).
11. Un soporte de techo a 45° usa una viga de madera. Si el cateto mide 5m, ¿cuánto cuesta la viga (hipotenusa) si el metro lineal vale $22 USD?
12. Un cable de antena a 60° está anclado a 8m del poste (cateto adyacente). Si el cable cuesta $9.50 USD el metro, calcula el presupuesto total.

> [!success] **Respuestas**
> 1. 1/2 o 0.5 | 2. 1 | 3. $\sqrt{2}/2$ | 4. 2
> 5. 1 | 6. $\approx 0.3640$ | 7. 0.5 (o 1/2) | 8. 30°
> 9. Altura = 5m. Costo = $600 USD.
> 10. Altura $\approx 34.64$m. Área $\approx 346.41\text{m}^2$. Costo $\approx 5196.15 USD.
> 11. Hipotenusa $\approx 7.07$m. Costo $\approx 155.56 USD.
> 12. Hipotenusa = 16m (usando Cos 60°). Costo = $152 USD.

---

## Mini-prueba de autoevaluación

1.  **Conceptual:** ¿Por qué usamos un triángulo de lado "2" para deducir los valores de 30° y 60°?
    *   *Respuesta:* Para que al trazar la altura, la base se divida exactamente en 1, facilitando los cálculos sin usar fracciones decimales desde el inicio.
2.  **Procedimental:** Para trabajar en grados, ¿qué letra debe verse en la pantalla de la calculadora?
    *   *Respuesta:* La letra **D** (de Degrees).
3.  **Aplicación $USD:** Una escalera de 4m se apoya a 60°. El protector de base cuesta $12 USD por metro de distancia a la pared. Si la distancia es el cateto adyacente (4 * Cos 60°), ¿cuánto gastas?
    *   *Respuesta:* Distancia = 2m. Gasto total = $24 USD.

---

## Notas finales y navegación

**Próxima Clase:** En la **Clase 09**, aplicaremos estos valores para resolver triángulos rectángulos completos, calculando lados y ángulos en problemas reales de ingeniería y arquitectura.

> [!info] **Navegación**
> [[Clase 07|⬅ Clase 07]] | [[00 - Índice del curso|Índice]] | [[Clase 09|Clase 09 ➡]]