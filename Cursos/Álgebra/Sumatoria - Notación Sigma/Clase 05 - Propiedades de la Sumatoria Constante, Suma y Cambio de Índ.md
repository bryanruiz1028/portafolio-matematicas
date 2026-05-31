# Clase 05 — Propiedades de la Sumatoria: Constante, Suma y Cambio de Índices

> [!meta] **Metadatos del Documento**
> **Curso:** Matemáticas Profe Alex — Notación Sigma
> **Clase:** 05
> **Tags:** #Matemáticas #Sumatorias #Álgebra #Pedagogía #EducaciónSecundaria

> [!info] 🧭 **Navegación**
> - [Anterior: Clase 04 — Sumatoria de una Constante](clase-04.md)
> - [Siguiente: Clase 06 — Aplicación de Fórmulas y Resolución Completa](clase-06.md)

---

> [!info] 🌍 **Relevancia y aplicaciones**
> Dominar las propiedades de las sumatorias permite transformar problemas extensos en operaciones simples, optimizando el tiempo de cálculo y reduciendo el margen de error algebraico.
> - 💵 **Finanzas ($USD):** Facilita el cálculo de intereses compuestos o planes de ahorro donde los depósitos crecen de forma constante cada mes.
> - 🏗️ **Ingeniería y Construcción:** Permite determinar la cantidad total de materiales en estructuras con patrones repetitivos, como el número de bloques en muros escalonados.
> - 📊 **Gestión de Inventarios:** Es esencial para realizar conteos rápidos de productos organizados por lotes que aumentan en cantidad según su ubicación.

---

> [!note] 📌 **¿Qué es la Sumatoria de una constante por una variable?**
> Imagina una **fábrica** con una fila de cajas. Si decides triplicar el contenido de cada caja, tienes dos caminos: triplicar el contenido de cada caja una por una y luego sumarlas, o sumar primero el contenido original y triplicar el resultado total al final. ¡Llegas al mismo número! "Sacar la constante" es simplemente aplicar la propiedad distributiva a la inversa (factorización).
>
> Por otro lado, **ajustar los límites** es como cambiar la hora de entrada en la fábrica: si le pides a los trabajadores que lleguen 4 horas antes (restas 4 al límite inferior), para que la producción no se altere, debes ajustar las máquinas para que funcionen como si fueran 4 horas más tarde (sumas 4 a la variable $i$).

> [!warning] ⚠️ **Error común**
> El error más grave es modificar los límites pero olvidar transformar la variable interna usando paréntesis.
> - ❌ **Incorrecto:** Bajar de $i=5$ a $i=1$ (restando 4) y dejar la función como $3i + 4$.
> - ✅ **Correcto:** Si restas 4 a los límites, debes **sustituir cada $i$ por $(i + 4)$**. La expresión correcta sería $3(i + 4)$, que al simplificar resulta en $3i + 12$.

> [!tip] 💡 **Truco para recordarlo**
> **Regla de las Operaciones Contrarias:** "Si el límite **BAJA** (resta), la variable **SUBE** (suma)". Recuerda usar siempre **paréntesis** al realizar el cambio en la variable para proteger la multiplicación.

---

### Procedimiento Paso a Paso

```text
PASO 1: Identificar los límites (inferior/superior) y la constante que multiplica a la variable.
PASO 2: Restar o sumar la cantidad necesaria a los límites para que el inferior sea i = 1.
PASO 3: Sustituir cada "i" en la función por un paréntesis que contenga la operación INVERSA.
PASO 4: Aplicar propiedad distributiva para simplificar la nueva expresión y resolver.
```

---

### Ejemplos Desarrollados

> [!example] **Ejemplo 1 (Básico): Propiedad de la Constante**
> **Problema:** Resolver $\sum_{i=1}^{6} 3i$
> **Desarrollo:**
> 1. Extraemos la constante: $3 \cdot \sum_{i=1}^{6} i$
> 2. Aplicamos la fórmula de los primeros números $\frac{n(n+1)}{2}$: $3 \cdot \left( \frac{6(7)}{2} \right)$
> 3. $3 \cdot (21) = 63$.

> [!example] **Ejemplo 2 (Signos/Suma): Separación de Términos**
> **Problema:** Separar y resolver $\sum_{i=1}^{10} (2i - 5)$
> **Desarrollo:**
> 1. Separamos en dos sumatorias: $\sum_{i=1}^{10} 2i - \sum_{i=1}^{10} 5$
> 2. Sacamos la constante de la primera: $2 \sum_{i=1}^{10} i - \sum_{i=1}^{10} 5$
> 3. Aplicamos fórmulas: $2 \left( \frac{10(11)}{2} \right) - (10 \cdot 5)$
> 4. Simplificamos: $110 - 50 = 60$.

> [!example] **Ejemplo 3 (Avanzado): Cambio de Índice**
> **Problema:** Ajustar $\sum_{i=5}^{15} 3i$ para que inicie en $i=1$.
> **Desarrollo:**
> 1. Para llevar $i=5$ a $1$, restamos 4 a ambos límites. Nuevo límite superior: $15 - 4 = 11$.
> 2. Aplicamos operación inversa a la variable: sustituimos $i$ por $(i + 4)$.
> 3. Planteamos la nueva sumatoria: $\sum_{i=1}^{11} 3(i + 4)$
> 4. Aplicamos distributiva: $\sum_{i=1}^{11} (3i + 12)$.

> [!example] **Ejemplo 4 (Aplicación $USD): Cobros Progresivos**
> **Problema:** Un servicio cobra $i$ dólares más una tarifa fija de $2$ USD. Se registran los cobros del día $i=3$ al $i=12$. Ajusta la sumatoria para iniciar en $1$.
> **Expresión original:** $\sum_{i=3}^{12} (i + 2)$
> **Desarrollo:**
> 1. Restamos 2 a los límites para que $3-2=1$. Límite superior: $12-2=10$.
> 2. Operación inversa: sustituimos $i$ por $(i + 2)$.
> 3. Sustitución con paréntesis: $\sum_{i=1}^{10} ((i + 2) + 2)$
> 4. Simplificación: $\sum_{i=1}^{10} (i + 4)$.

---

### Ejercicios para el Estudiante

> [!abstract] **Nivel Inicial (Verde) 🟢**
> 1. Extrae la constante de: $\sum_{i=1}^{10} 8i$
> 2. Extrae la constante de: $\sum_{i=1}^{20} \frac{1}{2}i$
> 3. Expresa como producto de una constante: $\sum_{k=1}^{n} 5k^2$
> 4. Simplifica extrayendo el signo negativo: $\sum_{i=1}^{5} -3i$

> [!abstract] **Nivel Intermedio (Amarillo) 🟡**
> 1. Separa la siguiente suma en dos partes: $\sum_{i=1}^{12} (4i + 7)$
> 2. Separa la siguiente diferencia: $\sum_{i=1}^{n} (i^2 - 3i)$
> 3. Ajusta el límite a $i=1$: $\sum_{i=4}^{10} i$
> 4. Ajusta el límite a $i=1$: $\sum_{i=2}^{8} (i + 5)$

> [!abstract] **Nivel Avanzado (Rojo) 🔴**
> 1. Cambia el índice a $i=1$ y simplifica la expresión: $\sum_{i=6}^{15} 2i$
> 2. Un plan de ahorro en $USD sigue la fórmula $\sum_{i=10}^{20} (i - 5)$. Ajústala para $i=1$.
> 3. Transforma a $i=1$ la sumatoria: $\sum_{i=7}^{20} (i^2 + 2)$
> 4. Resuelve completamente tras cambiar el índice a $i=1$: $\sum_{i=3}^{5} (i+1)$

---

> [!success] **Respuestas para el Docente**
> **Verde:** 1) $8 \sum i$; 2) $\frac{1}{2} \sum i$; 3) $5 \sum k^2$; 4) $-3 \sum i$.
> **Amarillo:** 1) $\sum 4i + \sum 7$; 2) $\sum i^2 - \sum 3i$; 3) $\sum_{i=1}^{7} (i+3)$; 4) $\sum_{i=1}^{7} (i+6)$.
> **Rojo:**
> 1) Restamos 5 a límites $\to$ Sumamos 5 a $i$: $\sum_{i=1}^{10} 2(i+5) = \mathbf{\sum_{i=1}^{10} (2i + 10)}$.
> 2) Restamos 9 a límites $\to$ Sumamos 9 a $i$: $\sum_{i=1}^{11} ((i+9)-5) = \mathbf{\sum_{i=1}^{11} (i+4)}$.
> 3) Restamos 6 a límites $\to$ Sumamos 6 a $i$: $\mathbf{\sum_{i=1}^{14} ((i+6)^2 + 2)}$.
> 4) Original: $4+5+6=15$. Ajustada: $\sum_{i=1}^{3} ((i+2)+1) = \sum_{i=1}^{3} (i+3) = 4+5+6 = \mathbf{15}$.

---

### Mini-prueba de Autoevaluación

> [!question] **Pregunta 1**
> ¿Qué propiedad algebraica justifica que podamos "sacar" la constante de una sumatoria?
> *Respuesta: La propiedad distributiva del producto respecto a la suma (factorización del factor común).*

> [!question] **Pregunta 2**
> Si en la sumatoria $\sum_{i=7}^{15} f(i)$ restamos 6 a los límites para iniciar en $i=1$, ¿qué debemos hacer con la variable $i$ dentro de la función?
> *Respuesta: Sustituir cada $i$ por $(i+6)$, aplicando la operación inversa (suma) para mantener el equilibrio de la serie.*

> [!question] **Pregunta 3**
> Tienes una sumatoria de ingresos: $\sum_{i=2}^{4} 10i$. Si la transformas para que inicie en $i=1$, ¿cuál es la nueva expresión simplificada?
> *Respuesta: $\sum_{i=1}^{3} 10(i+1) = \sum_{i=1}^{3} (10i + 10)$.*

---

> [!tip] 💡 **En la próxima clase**
> ¡Felicidades! Has dominado las herramientas para manipular cualquier sumatoria. En la siguiente sesión, uniremos todas las piezas para resolver problemas de gran escala aplicando fórmulas y propiedades de forma simultánea.

> [!info] 🧭 **Navegación**
> - [Anterior: Clase 04 — Sumatoria de una Constante](clase-04.md)
> - [Siguiente: Clase 06 — Aplicación de Fórmulas y Resolución Completa](clase-06.md)