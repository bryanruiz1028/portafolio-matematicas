# 📖 Guía de estudio — Clase 04: Teorema del Seno: Resolver el triángulo

¡Qué tal, amigos! Espero que estén muy bien. En esta guía vamos a dominar el arte de "resolver" un triángulo. No se asusten por el nombre, resolver simplemente significa encontrar todos los datos que nos faltan. ¡Vamos a darle!

> [!info] 📌 Conceptos clave
> * **Resolver un triángulo:** Es el proceso de hallar las medidas de los **3 lados** y los **3 ángulos** internos. ¡No terminamos hasta que el triángulo no tenga secretos para nosotros!
> * **La "Pareja Ideal":** Para usar el Teorema del Seno, el requisito indispensable es conocer una pareja completa (un ángulo y su lado opuesto) y cualquier otro dato extra (otro lado u otro ángulo).
> * **Regla de los $180^\circ$:** ¡Piénsalo así! La suma de los ángulos internos siempre es $180^\circ$. Si ya conoces dos, el tercero sale por simple resta.
> * **Lógica de Correspondencia:** Es nuestra brújula. El **ángulo más grande** siempre debe estar frente al **lado más largo**. Si tu resultado dice lo contrario, ¡revisa tus cálculos!

## Tabla de Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Teorema del Seno (Lados)** | $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$ <br> *¡Ojo! Ponemos los lados arriba cuando buscamos un **lado**.* |
| **Teorema del Seno (Ángulos)** | $\frac{\sin A}{a} = \frac{\sin B}{b} = \frac{\sin C}{c}$ <br> *Invertimos la fórmula cuando lo que nos falta es un **ángulo**.* |
| **Suma de Ángulos** | $A + B + C = 180^\circ$ <br> *Es el paso más rápido cuando ya conocemos dos ángulos.* |
| **Ángulo Obtuso** | $180^\circ - \text{resultado de la calculadora}$. <br> *La calculadora solo entiende ángulos agudos. Si por el dibujo o el contexto ves que el ángulo es mayor a $90^\circ$, debes aplicar esta resta.* |

---

## Ejemplos Resueltos Adicionales

````ad-example
**Ejemplo A: El Caso Básico (Conociendo dos ángulos)**
**Datos:** Ángulo $B = 30^\circ$, Ángulo $C = 108^\circ$, Lado $c = 39 \text{ cm}$.

1.  **Paso 1: Hallar el ángulo faltante ($A$):**
    Como ya tenemos dos, aplicamos la regla de los $180^\circ$:
    $A = 180^\circ - 108^\circ - 30^\circ = 42^\circ$.
2.  **Paso 2: Hallar el lado $a$:**
    Usamos la pareja conocida ($C$ y $c$) para hallar $a$:
    $\frac{a}{\sin 42^\circ} = \frac{39}{\sin 108^\circ}$
    Despejamos pasando el $\sin 42^\circ$ a multiplicar:
    $a = \frac{39 \cdot \sin 42^\circ}{\sin 108^\circ} \approx \mathbf{27.439 \text{ cm}}$.
3.  **Verificación de Lógica:** El ángulo más grande es $C (108^\circ)$ y su lado opuesto es $c (39 \text{ cm})$. Nuestro lado $a (27.439 \text{ cm})$ está frente a un ángulo de $42^\circ$. Como $42^\circ < 108^\circ$, es lógico que $a < c$. ¡Todo en orden!
````

````ad-example
**Ejemplo B: Aplicación de Topografía (Costo de Obra)**
**Escenario:** Debemos calcular la distancia $b$ para una obra donde cada metro de construcción cuesta $500 \text{ USD}$.
**Datos:** Ángulo $A = 35^\circ$, Lado opuesto $a = 11 \text{ m}$, Lado $c = 16 \text{ m}$.

1.  **Paso 1: Hallar el ángulo $C$:**
    Usamos la fórmula invertida: $\frac{\sin C}{16} = \frac{\sin 35^\circ}{11}$
    $\sin C = \frac{16 \cdot \sin 35^\circ}{11} \approx 0.834 \implies C = \arcsin(0.834) \approx \mathbf{56.542^\circ}$.
2.  **Paso 2: La Cadena de Dependencia (Hallar $B$):**
    ¡No podemos hallar el lado $b$ directamente! Primero necesitamos su ángulo opuesto $B$.
    $B = 180^\circ - 35^\circ - 56.542^\circ = \mathbf{88.458^\circ}$.
3.  **Paso 3: Hallar la distancia $b$:**
    $\frac{b}{\sin 88.458^\circ} = \frac{11}{\sin 35^\circ} \implies b = \frac{11 \cdot \sin 88.458^\circ}{\sin 35^\circ} \approx \mathbf{19.172 \text{ m}}$.
4.  **Paso 4: Cálculo del Presupuesto:**
    $19.172 \text{ m} \times 500 \text{ USD/m} = \mathbf{9,586 \text{ USD}}$.
5.  **Verificación:** El ángulo $B (88.458^\circ)$ es el mayor, por lo tanto el lado $b (19.172 \text{ m})$ debe ser el más largo. Comparamos: $19.172 > 16 > 11$. ¡Perfecto!
````

---

## Ejercicios de Repaso

````ad-abstract
**🟢 Nivel Fácil: Completar la pareja (¡Recuerda el modo DEG!)**
*Antes de empezar, verifica que tu calculadora tenga una "D" o diga "DEG" en la pantalla.*
1.  En un triángulo, el ángulo $A = 45^\circ$ y el ángulo $B = 75^\circ$. Calcula el valor del ángulo $C$.
2.  Si tenemos un triángulo con $B = 120^\circ$ y $C = 15^\circ$, ¿cuánto mide el ángulo $A$?
3.  Halla el ángulo faltante para un triángulo donde $A = 62.5^\circ$ y $C = 55^\circ$.
````

````ad-abstract
**🟡 Nivel Medio: Cálculo de lados (Intercambiando incógnitas)**
1.  **Halla el lado $b$:** Si $A = 41^\circ$, $a = 30 \text{ cm}$ y $B = 110^\circ$.
2.  **Halla el lado $a$:** Si $B = 30^\circ$, $b = 21 \text{ cm}$ y $A = 80^\circ$.
3.  **Halla el lado $c$:** Si tienes la pareja $B = 40^\circ$, $b = 15 \text{ m}$ y conoces el ángulo $C = 100^\circ$.
````

````ad-abstract
**🔴 Nivel Avanzado: Aplicación con Ángulo Obtuso y USD**
*Contexto: Un terreno triangular tiene un Ángulo $B = 31^\circ$, lado $b = 20 \text{ m}$ y lado $c = 38 \text{ m}$. El dibujo muestra que el ángulo $C$ es claramente mayor a $90^\circ$. El costo de cercar es de $15 \text{ USD}$ por metro.*

1.  **El Ángulo Obtuso:** Calcula el ángulo $C$ (recuerda restar de $180^\circ$ el resultado de la calculadora) y luego el ángulo $A$.
2.  **Presupuesto Parcial:** Calcula el costo de poner una cerca solo en el lado $a$. (Primero halla la medida del lado $a$).
3.  **Presupuesto Total:** ¿Cuál es el costo total para cercar todo el perímetro del terreno (lados $a, b$ y $c$)?
````

---

> [!tip] 💡 Consejo de estudio
> **La Estrategia de Revisión de Profe Alex:** Al terminar cualquier ejercicio, tómate 5 segundos para comparar. Si el lado que calculaste mide $50 \text{ cm}$ y está frente a un ángulo de $20^\circ$, pero tienes otro lado de $20 \text{ cm}$ frente a un ángulo de $80^\circ$, **¡Pilas!** Algo salió mal. El ángulo más grande siempre "mira" al lado más grande. ¡No olvides usar 3 decimales para que el resultado sea exacto!