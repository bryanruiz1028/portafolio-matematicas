# 📋 Planificación Didáctica — Area of a Triangle y Área del triángulo cuando conocemos la Base y la Altura

## 1. Tema
Área del triángulo: deducción conceptual a partir de paralelogramos y cálculo mediante la relación base-altura.

## 2. Metodología
Se implementará un enfoque de **Aprendizaje Colaborativo Formal**. Los estudiantes trabajarán en grupos heterogéneos para transitar desde la manipulación física de polígonos hasta la abstracción algebraica. El objetivo es que no solo memoricen la fórmula, sino que comprendan el vínculo conceptual: un triángulo es siempre la mitad de un paralelogramo con sus mismas dimensiones.

## 3. Secuencia Didáctica

### 🔵 ANTICIPACIÓN — 20 min

> [!abstract] Actividad de inicio: El Reto de la Cuadrícula
> Antes de presentar fórmulas, entregue a los alumnos una guía con diversos triángulos dibujados sobre cuadrículas de $1 \times 1 \text{ cm}$. 
> **El Reto:** Estimar la superficie contando los cuadrados internos. 
> **Consejo Didáctico:** Guíe a los estudiantes en el manejo de los "cuadrados cortados". Sugiera que busquen dos mitades que parezcan completar un cuadrado entero. Esta aproximación intuitiva genera la necesidad de una medida exacta y justifica la posterior introducción de la fórmula.
> **Pregunta de reflexión:** "¿Cómo podemos saber el área exacta si las líneas diagonales cortan los cuadrados de forma irregular?".

> [!note] Enfoque DUA
> - **Qué:** Activación de conocimientos previos sobre superficie y la distinción entre unidades lineales ($cm$) y cuadradas ($cm^2$).
> - **Cómo:** Uso de material impreso con alto contraste visual y manipulación en parejas.
> - **Por qué:** Proporcionar múltiples medios de representación para que el concepto de "espacio encerrado" sea tangible.

---

### 🟡 CONSTRUCCIÓN — 40 min

> [!example] Actividades centrales: Del Papel a la Fórmula
> 1. **Deducción Conceptual (El Puente del Paralelogramo):** 
>    - Entregue un paralelogramo (romboide) de papel a cada grupo. 
>    - **Paso A:** Pida que tracen la altura y corten el triángulo que se forma en un extremo, trasladándolo al otro para formar un rectángulo. Esto demuestra que $Área_{\text{paralelogramo}} = \text{base} \times \text{altura}$.
>    - **Paso B:** Pida que corten ese rectángulo (o el paralelogramo original) por su diagonal. Comprobarán físicamente que resultan dos triángulos idénticos.
>    - **Conclusión:** El área del triángulo es la mitad del área del rectángulo/paralelogramo: $Area = \frac{b \times h}{2}$.
> 
> 2. **Identificación de Elementos y Aplicación:**
>    - Enfatice que la **altura ($h$)** debe ser perpendicular a la **base ($b$)**, formando un ángulo de $90^\circ$. Use marcadores de colores para resaltar este ángulo.
>    - **Ejemplo con Altura Externa:** Presente el caso del triángulo donde la altura se traza sobre la prolongación de la base (Fuente: Profe Alex). 
>      - *Datos:* $b = 4 \text{ cm}$, $h = 5 \text{ cm}$. 
>      - *Cálculo:* $Area = \frac{4 \text{ cm} \times 5 \text{ cm}}{2} = \frac{20 \text{ cm}^2}{2} = 10 \text{ cm}^2$.
>    - **Ejercicio de práctica:** Calcular el área de un triángulo con $b = 8 \text{ m}$ y $h = 4 \text{ m}$.
>      - *Resultado:* $Area = \frac{8 \text{ m} \times 4 \text{ m}}{2} = 16 \text{ m}^2$.

> [!note] Enfoque DUA
> - **Qué:** Construcción de la fórmula general con rigor en el uso de unidades.
> - **Cómo:** Modelado en pizarra con código de colores (Azul para la base, Rojo para la altura). 
> - **Por qué:** El uso de colores ayuda a los estudiantes con dificultades de procesamiento visual a identificar los elementos críticos de la fórmula.

---

### 🟢 CONSOLIDACIÓN — 20 min

> [!success] Actividad de cierre: El Proyecto del Jardín
> **Ticket de Salida:** "Un cliente solicita instalar césped sintético en una sección triangular de su jardín. La base mide $10 \text{ m}$ y la altura perpendicular es de $5 \text{ m}$. ¿Cuántos metros cuadrados de césped se deben comprar?".
> 
> **Solución para el docente:** 
> $Area = \frac{10 \text{ m} \times 5 \text{ m}}{2} = \frac{50 \text{ m}^2}{2} = 25 \text{ m}^2$.
> 
> **Reflexión DUA:** Conecte este problema con el costo real. Si el $m^2$ cuesta $\$10$, ¿cuánto costará el jardín? Esto aumenta la relevancia y el compromiso (Engagement).

> [!info] Referencia Técnica para el Docente
> Si bien hoy nos enfocamos en base y altura, es vital tener a mano estas fórmulas para alumnos que avancen más rápido o para casos donde la altura es desconocida:
> - **Fórmula de Herón (Conociendo los tres lados $a, b, c$):**
>   $s = \frac{a + b + c}{2}$ (Semiperímetro)
>   $Area = \sqrt{s(s-a)(s-b)(s-c)}$
> - **Triángulo Equilátero (Conociendo un lado $l$):**
>   $Area = \frac{\sqrt{3}}{4} \times l^2$

---

## 4. Recursos

| Recurso | Tipo | Uso en la clase | Referencia de Fuente |
| :--- | :--- | :--- | :--- |
| **Pizarra y Marcadores** | Físico | Modelado de la altura (Roja) y la base (Azul) para resaltar el ángulo recto. | Concepto de Profe Alex |
| **Fichas de Cuadrícula** | Impreso | Actividad de conteo de unidades cuadradas y estimación inicial. | Didáctica de Superficie |
| **Hojas y Tijeras** | Físico | Transformación de paralelogramo a rectángulo y división en dos triángulos. | Deducción Geométrica |
| **Calculadoras** | Digital | Verificación de cálculos complejos y operaciones con decimales. | Uso en problemas reales |
| **Guía de Ejercicios** | Impreso | Incluye el ejemplo de **altura externa** ($b=4, h=5$) y problemas de aplicación. | Ejemplo Profe Alex |

---

## 5. Currículo

|                         | Código        | Descripción                                                                                                                                                                                                                                                                                       |
| ----------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Criterio**            | CE.M.4.6      | Utiliza estrategias de descomposición en triángulos en el cálculo de áreas de figuras compuestas; aplica el teorema de Pitágoras y las relaciones trigonométricas para el cálculo de longitudes desconocidas, y calcula áreas y volúmenes en contextos geométricos o situaciones reales.           |
| **Destreza principal**  | M.4.2.11 `8°` | Calcular el perímetro y el área de triángulos en la resolución de problemas.                                                                                                                                                                                                                      |
| **Destreza secundaria** | M.4.2.18 `9°` | Calcular el área de polígonos regulares por descomposición en triángulos.                                                                                                                                                                                                                         |
| **Indicador**           | I.M.4.6.3     | Resuelve problemas geométricos que requieran del cálculo de áreas de polígonos regulares, áreas y volúmenes de pirámides, prismas, conos y cilindros; aplica la descomposición en triángulos como estrategia de solución.                                                                          |
| **Grado sugerido**      | 8° – 9°       | Área del triángulo con base y altura; casos especiales (altura exterior, triángulo equilátero) y fórmula de Herón.                                                                                                                                                                                 |