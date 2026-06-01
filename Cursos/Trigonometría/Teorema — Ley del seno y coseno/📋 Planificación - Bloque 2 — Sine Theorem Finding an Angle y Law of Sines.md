# 📋 Planificación Didáctica — Sine Theorem: Finding an Angle y Law of Sines

## 2. Metodología
Esta planificación se fundamenta en el **Aprendizaje colaborativo formal**, organizando el aula en grupos heterogéneos donde el apoyo mutuo es el motor del aprendizaje. El enfoque busca que el estudiante transite de lo concreto (medición física con recursos como lana o cordel) a lo abstracto (resolución algebraica), permitiendo que la construcción social del conocimiento valide las deducciones trigonométricas.

## 3. Secuencia Didáctica

### 🔵 ANTICIPACIÓN — 20 min

[!abstract] Actividad de inicio: Redescubriendo la Ley
**El reto de la altura "x":** Se solicita a los estudiantes dibujar un triángulo acutángulo cualquiera en la pizarra. El docente propone trazar una de sus alturas desde un vértice superior hasta la base opuesta.
- **Instrucción clave:** Denominaremos a esta altura como **"x"** en lugar de "h", para evitar confusiones con la "h" de **hipotenusa** en los triángulos rectángulos internos.
- **Modelado:** Dividimos el triángulo original en dos: uno a la izquierda (identificado con color rojo) y otro a la derecha (color azul). 
- **Desafío:** Utilizando la razón del seno ($\text{sen} = \text{opuesto}/\text{hipotenusa}$), los estudiantes deben expresar "x" de dos formas:
    1. En el triángulo rojo: $x = b \cdot \text{sen}(A)$
    2. En el triángulo azul: $x = a \cdot \text{sen}(B)$
- **Igualación:** Al ser la misma altura, igualamos: $b \cdot \text{sen}(A) = a \cdot \text{sen}(B)$. Al trasponer términos, "redescubrimos" la proporción: $\frac{a}{\text{sen}(A)} = \frac{b}{\text{sen}(B)}$.

[!note] Enfoque DUA
- **Qué:** Activación de conocimientos previos sobre razones trigonométricas básicas (SOH).
- **Cómo:** Trabajo en parejas utilizando la pizarra y marcadores de colores para diferenciar los lados opuestos.
- **Por qué:** Facilita la representación visual de la **"oposición"** entre ángulo y lado, regla fundamental de esta ley.

---

### 🟡 CONSTRUCCIÓN — 40 min

[!example] Actividades centrales: El Arcoseno y la "Parejita Completa"
Para hallar un ángulo desconocido, el estudiante debe identificar primero una **"parejita completa"** (un lado y su ángulo opuesto conocidos). 
1. **Despeje para Ángulos:** Se modela el despeje de la fórmula original para aislar el seno: $\text{sen}(B) = \frac{b \cdot \text{sen}(A)}{a}$.
2. **Uso del Arcoseno:** Para obtener el valor en grados, aplicamos la función inversa mediante la **tecla SHIFT** en la calculadora, activando el **Arcoseno** ($\text{sen}^{-1}$).

[!important] Precisión Técnica en la Calculadora
- **Configuración de Modo:** El estudiante debe verificar que aparezca una **"D"** en la pantalla. Esto se logra mediante la secuencia **Shift + Setup**, seleccionando "Unidad Angular" y luego **"Degree"** (Grados Sexagesimales). Se debe advertir que el modo "R" (Radianes) o "G" (Gradianes) arrojará resultados erróneos.
- **Sintaxis de Paréntesis:** Un error común es omitir paréntesis. El docente debe insistir en que para operaciones complejas como $\text{sen}^{-1}(\frac{b \cdot \text{sen}(A)}{a})$, se deben cerrar todos los paréntesis del ángulo y de la función inversa para evitar el mensaje de "Syntax Error".

[!tip] El Truco de los Ángulos Especiales (30°, 45°, 60°)
Para prescindir de la calculadora en casos ideales, enseñaremos el truco de la raíz:
- Escribir en orden: $\sqrt{0}, \sqrt{1}, \sqrt{2}, \sqrt{3}, \sqrt{4}$.
- Dividir todos entre 2. 
- Esto genera los senos de 0°, 30° ($1/2$), 45° ($\sqrt{2}/2$), 60° ($\sqrt{3}/2$) y 90° ($1$).

[!note] Enfoque DUA
- **Qué:** Transición de lo físico a lo abstracto.
- **Cómo:** Uso de **lana o cordel** para formar triángulos sobre los pupitres. Los estudiantes miden los lados, calculan un ángulo mediante la Ley de Senos y verifican su exactitud con un transportador.
- **Por qué:** Ofrece múltiples medios de acción y expresión, permitiendo la validación empírica del cálculo algebraico.

---

### 🟢 CONSOLIDACIÓN — 20 min

[!success] Actividad de cierre: Reto del Triángulo Obtusángulo
¿Funciona la Ley de Senos si el triángulo tiene un ángulo mayor a 90°?
- **Desafío:** Dibujar un triángulo obtusángulo donde la altura "x" caiga fuera del triángulo original.
- **Prueba Visual:** Utilizando la lógica del círculo trigonométrico, demostramos que el seno de un ángulo obtuso es igual al seno de su suplementario ($\text{sen}(y) = \text{sen}(180^\circ - y)$). 
- **Conclusión:** Dado que la coordenada "Y" (altura) es idéntica para ambos ángulos en el círculo, el Teorema del Seno es universal para cualquier tipo de triángulo.

[!note] Enfoque DUA
- **Qué:** Generalización y síntesis.
- **Cómo:** Plenaria de socialización donde cada grupo explica por qué la altura externa no invalida la proporción.
- **Por qué:** Fomenta la comprensión profunda y el pensamiento crítico sobre la validez universal de las leyes matemáticas.

---

## 4. Recursos

| Recurso | Tipo | Uso en la clase |
|---------|------|----------------|
| Pizarra | Físico | Modelado de la deducción del teorema trazando la altura "x" y diferenciando triángulos. |
| Marcadores | Físico | **Codificación por colores:** Rojo para el triángulo izquierdo, azul para el derecho y negro para la altura común. |
| Fichas | Impreso | Guías con problemas de "parejitas completas" y advertencias sobre sintaxis de calculadora. |
| Impresora | Físico | Generación de la tabla de ángulos especiales basada en el truco $\sqrt{n}/2$. |
| **Lana o cordel** | Físico | Herramienta de manipulación concreta para verificar longitudes antes del cálculo de Arcoseno. |