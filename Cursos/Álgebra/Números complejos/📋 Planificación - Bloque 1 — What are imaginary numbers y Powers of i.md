# 📋 Planificación Didáctica — What are imaginary numbers? y Powers of i

## 1. Tema
**What are imaginary numbers? y Powers of i**

## 2. Metodología
**Aprendizaje Colaborativo Formal**
Los estudiantes se organizarán en grupos de tres con roles definidos: **Coordinador** (gestiona el tiempo y participación), **Calculador** (ejecuta divisiones y transformaciones) y **Verificador** (valida resultados usando el "Reloj de $i$"). Esta estructura fomenta la interdependencia positiva al enfrentar el enigma de las raíces negativas y la predictibilidad del ciclo de potencias.

---

## 3. Secuencia Didáctica

### 🔵 ANTICIPACIÓN — 20 min

> [!abstract] Actividad de inicio: "El número imposible"
> Se plantea a la clase la ecuación:
> $$x^2 = -1$$
> **Reto:** Encontrar un número real que satisfaga la igualdad. Tras el debate, se concluye que no existe en los reales, pues cualquier número al cuadrado es positivo.
> 
> **Contexto Histórico (Nivel Catedrático):** Aunque Descartes los llamó "imaginarios" despectivamente y Euler popularizó el símbolo $i$, el problema no surgió inicialmente de $x^2 = -1$, sino de la necesidad de resolver **ecuaciones cúbicas** (de tercer grado) donde aparecían raíces negativas en pasos intermedios.

**Enfoque DUA:**
*   **Qué (Representación):** Activación de conocimientos previos sobre potencias y raíces, generando un conflicto cognitivo al mostrar el límite del sistema numérico real.
*   **Cómo (Acción y Expresión):** Lluvia de ideas dirigida en la pizarra para descartar soluciones erróneas (como $1$ o $-1$) mediante el razonamiento lógico.

---

### 🟡 CONSTRUCCIÓN — 40 min

> [!info] Parte A: La identidad de $i$ y la transformación de raíces
> Por definición, la unidad imaginaria es $i = \sqrt{-1}$, lo que implica que:
> $$i^2 = -1$$
> Para calcular raíces de números negativos, extraemos el factor imaginario separándolo del real:
> - $\sqrt{-4} = \sqrt{4 \cdot (-1)} = \sqrt{4} \cdot \sqrt{-1} = 2i$
> - $\sqrt{-25} = \sqrt{25 \cdot (-1)} = \sqrt{25} \cdot \sqrt{-1} = 5i$

> [!warning] Alerta Matemática: Restricción de Radicales
> Es un error común intentar aplicar la propiedad $\sqrt{a} \cdot \sqrt{b} = \sqrt{ab}$ con números negativos. 
> **Importante:** $\sqrt{-5} \cdot \sqrt{-5} \neq \sqrt{(-5)(-5)}$.
> En el campo complejo, **siempre** se debe transformar a la unidad $i$ antes de operar para evitar resultados incorrectos.

> [!tip] Parte B: El Ciclo de las Potencias (El Reloj de $i$)
> Las potencias de $i$ siguen un patrón cíclico de 4 valores. Para visualizarlo, usamos el "Reloj de $i$" en el plano complejo:
> - **12:00 (Arriba):** $i^0 = 1$
> - **03:00 (Derecha):** $i^1 = i$
> - **06:00 (Abajo):** $i^2 = -1$
> - **09:00 (Izquierda):** $i^3 = -i$
> 
> Para calcular potencias elevadas (ej. $i^{85}$), dividimos el exponente entre 4 y nos enfocamos únicamente en el **residuo**, ya que este indica la posición final en el ciclo:
> 
> $$\text{Exponente: } 85 \div 4 \implies \text{Cociente: } 21, \text{ \textbf{Residuo: } 1}$$
> 
> Por lo tanto:
> $$i^{85} = i^1 = i$$

**Enfoque DUA:**
*   **Qué:** Construcción del concepto mediante el patrón cíclico y el algoritmo de división.
*   **Cómo:** Trabajo en parejas clasificando números en fichas (Reales vs. Imaginarios Puros).
*   **Por qué:** Se reduce la carga cognitiva al vincular un proceso abstracto (división) con una representación visual familiar (el reloj).

---

### 🟢 CONSOLIDACIÓN — 20 min

> [!example] Actividad de cierre: "Duelo de Potencias"
> Cada grupo recibe un desafío de simplificación (ej. $i^{79} + i^{197}$). 
> **Dinámica de Roles:**
> 1. El **Calculador** realiza la división larga para hallar el residuo.
> 2. El **Verificador** utiliza el "Reloj de $i$" para determinar el valor final basándose en el residuo.
> 3. Comparten el procedimiento en la pizarra para una coevaluación dirigida.

**Enfoque DUA:**
*   **Qué:** Verificación de la comprensión del patrón y la regla de transformación.
*   **Cómo:** Coevaluación estructurada mediante el sistema de "pareja de verificación", comparando el residuo matemático con la posición gráfica en el reloj.

---

## 4. Recursos

| Recurso | Tipo | Uso en la clase |
| :--- | :--- | :--- |
| **Pizarra** | Físico | Trazar el plano complejo y realizar las divisiones de potencias elevadas para visualización grupal. |
| **Marcadores** | Físico | Usar colores distintos para la parte real (eje horizontal) y la unidad imaginaria (eje vertical). |
| **Fichas** | Impreso | Tarjetas de práctica con exponentes grandes (ej. $i^{1024}$) para mecanizar el uso del residuo. |
| **Impresora** | Físico | Producción de guías de ejercicios que incluyen la advertencia sobre la multiplicación de raíces negativas. |
| **Reloj de pared** | Físico | **Recurso Visual:** Mapear $i^0$ a las 12, $i^1$ a las 3, $i^2$ a las 6 e $i^3$ a las 9 para representar el ciclo infinito de las potencias. |