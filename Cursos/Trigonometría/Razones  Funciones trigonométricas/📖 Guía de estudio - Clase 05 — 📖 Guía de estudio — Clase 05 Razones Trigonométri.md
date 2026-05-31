# 📖 Guía de estudio — Clase 05: Razones Trigonométricas

> [!info] 📌 Conceptos clave
> - **Identificación de los lados:** En un triángulo rectángulo, la **hipotenusa** es siempre el lado más largo y se encuentra opuesta al ángulo recto. Los **catetos** se definen según su relación de posición con el ángulo de referencia ($\theta$).
> - **Lógica posicional:** El **cateto adyacente** es aquel que está "pegado" o junto al ángulo de referencia, mientras que el **cateto opuesto** es el que se encuentra justo enfrente de dicho ángulo.
> - **Importancia del ángulo de referencia:** La clasificación de un cateto como opuesto o adyacente no es fija; depende totalmente de cuál de los dos ángulos agudos estemos utilizando para el análisis.
> - **Utilidad de las razones:** El Seno, Coseno y Tangente nos permiten calcular la medida de un lado desconocido siempre que contemos con un ángulo y un lado conocido, o hallar un ángulo si conocemos dos de sus lados.

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Seno** ($\text{sen}$) | Es la razón entre el cateto opuesto y la hipotenusa: $\text{sen}(\theta) = \frac{CO}{H}$ |
| **Coseno** ($\text{cos}$) | Es la razón entre el cateto adyacente y la hipotenusa: $\text{cos}(\theta) = \frac{CA}{H}$ |
| **Tangente** ($\text{tan}$) | Es la razón entre el cateto opuesto y el cateto adyacente: $\text{tan}(\theta) = \frac{CO}{CA}$ |
| **Ángulo de Elevación** | Es el ángulo que se forma entre la línea horizontal de visión y la visual dirigida hacia un objeto situado por encima de dicha horizontal. |

## Ejemplos Resueltos Adicionales

````ad-example
title: Ejemplo A — Hallar un cateto basándose en el ángulo y la hipotenusa
**Problema:** En un triángulo rectángulo con una hipotenusa de $10\text{ m}$ y un ángulo de referencia de $30^\circ$, ¿cuánto mide el cateto opuesto ($CO$)?

**Paso a paso:**
1. **Identificación de datos:** 
   - Ángulo ($\theta$) = $30^\circ$
   - Hipotenusa ($H$) = $10\text{ m}$
   - Incógnita = Cateto Opuesto ($CO$)
2. **Elección de la fórmula:** Como relacionamos el cateto opuesto con la hipotenusa, utilizamos la razón **Seno**.
3. **Sustitución:** 
   $$\text{sen}(30^\circ) = \frac{CO}{10\text{ m}}$$
4. **Despeje y cálculo:** Pasamos el $10\text{ m}$ multiplicando al otro lado:
   $$10\text{ m} \cdot \text{sen}(30^\circ) = CO$$
   Sabiendo que el $\text{sen}(30^\circ) = \frac{1}{2}$ (o $0.5$):
   $$10\text{ m} \cdot \frac{1}{2} = CO$$
5. **Resultado:** El cateto opuesto mide **$5\text{ m}$**.
````

````ad-example
title: Ejemplo B — Cálculo de materiales para una cometa ($USD)
**Problema:** Se eleva una cometa soltando $50\text{ m}$ de hilo especial. El ángulo de elevación formado es de $37^\circ$. Si el hilo cuesta $\$1.50\text{ USD}$ por metro, calcula la altura alcanzada por la cometa ($x$) y el costo total del hilo utilizado.

**Paso a paso:**
1. **Identificación de datos:** 
   - Hipotenusa ($H$) = $50\text{ m}$ (longitud del hilo).
   - Ángulo ($\theta$) = $37^\circ$.
   - Precio = $\$1.50\text{ USD}/\text{m}$.
2. **Elección de la fórmula:** La altura ($x$) representa el cateto opuesto al ángulo de $37^\circ$. Usamos **Seno**:
   $$\text{sen}(37^\circ) = \frac{x}{50\text{ m}}$$
3. **Cálculo de la altura:**
   $$x = 50\text{ m} \cdot \text{sen}(37^\circ)$$
   Usando la calculadora: $x \approx 50 \cdot 0.6018 \approx 30.09\text{ m}$.
4. **Cálculo de costo:** El costo depende del hilo total soltado ($50\text{ m}$):
   $$50\text{ m} \cdot \$1.50\text{ USD}/\text{m} = \$75\text{ USD}$$
5. **Resultado:** La altura aproximada es de **$30.09\text{ m}$** y el costo del hilo es de **$\$75\text{ USD}$**.
````

## Ejercicios de Repaso

````ad-abstract
title: 🟢 Nivel: Fácil
1. Calcula el cateto opuesto de un triángulo cuya hipotenusa mide $20\text{ m}$ y tiene un ángulo de referencia de $30^\circ$ (considera $\text{sen}(30^\circ) = 1/2$).
2. Determina el cateto opuesto en un triángulo con hipotenusa de $10\sqrt{2}\text{ m}$ y un ángulo de $45^\circ$ ($\text{sen}(45^\circ) = \sqrt{2}/2$).
3. Si un triángulo posee una hipotenusa de $12\text{ m}$ y un ángulo de $60^\circ$, calcula la medida del cateto adyacente utilizando la razón $\text{cos}(60^\circ) = 1/2$.
````

````ad-note
title: 🟡 Nivel: Medio
1. **El cateto común:** Considera una figura compuesta por dos triángulos rectángulos unidos por un cateto vertical común ($y$). El primer triángulo (izquierda) tiene un ángulo de $32^\circ$ y una hipotenusa de $15\text{ m}$. El segundo triángulo (derecha) tiene un ángulo de $63^\circ$. Calcula el valor del cateto adyacente ($x$) del segundo triángulo.
2. Un triángulo $A$ tiene un ángulo de $30^\circ$ y un cateto opuesto de $5\text{ m}$. La hipotenusa de este triángulo $A$ es, a su vez, el cateto opuesto de un triángulo $B$ que tiene un ángulo de $45^\circ$. Halla la medida de la hipotenusa final del triángulo $B$.
````

````ad-danger
title: 🔴 Nivel: Avanzado (Aplicación con $USD)
**Problema del Cohete:** Un cohete espacial despega desde el nivel del mar con un ángulo constante de $52^\circ 20'$ y recorre una trayectoria rectilínea (hipotenusa) de $1200\text{ m}$.
1. Calcula la altura exacta ($x$) que alcanza el cohete en ese punto. *Tip: En la calculadora, ingresa $1200 \cdot \text{sen}(52^\circ 20')$ usando la tecla de grados/minutos.*
2. Si el combustible tiene un costo operativo de $\$0.80\text{ USD}$ por cada metro de altura alcanzada, ¿cuál es el costo total del combustible para llegar a dicha altura?
````

> [!tip] 💡 Consejo de estudio
> Para obtener resultados precisos, verifica siempre que tu calculadora esté en modo **Grados Sexagesimales** (debe aparecer una **"D"** o **"DEG"** en la pantalla). Además, sigue la recomendación del "Profe Alex": no gastes energía en dibujos artísticos detallados; **"concentrémonos en dibujar líneas y puntos"** para crear diagramas esquemáticos que te permitan visualizar el triángulo rectángulo rápidamente.