# Clase 04 — Suma, resta y multiplicación de radicales

#matemáticas #álgebra #radicales #didáctica
[[Clase 03]] | [[Indice_Curso]] | [[Clase 05]]

---

## 🌍 Relevancia y aplicaciones

> [!info] **¿Por qué es importante esta clase?**
> Los radicales no son solo símbolos matemáticos; son la herramienta que nos permite manejar **valores exactos** en cálculos complejos. A diferencia de los decimales, que suelen redondearse y perder precisión, los radicales mantienen la fidelidad del número real.
> 
> *   **Aplicación USD:** En el mundo financiero, se utilizan para calcular tasas de interés compuesto o la depreciación de activos donde la precisión centesimal es crítica para evitar errores acumulados en proyecciones a largo plazo.
> *   **Aplicación Práctica:** En arquitectura, son indispensables para medir distancias diagonales exactas mediante el Teorema de Pitágoras (como $\sqrt{2}$ o $\sqrt{5}$), asegurando que las estructuras encajen sin margen de error.
> *   **Situación Cotidiana:** Los diseñadores gráficos y de empaques utilizan la **Razón Áurea** ($\phi = \frac{1+\sqrt{5}}{2}$), basada en un radical, para crear composiciones visualmente perfectas y dimensiones armónicas.

---

## 📌 Concepto clave

> [!note] **¿Qué es Suma y resta de radicales?**
> Imagina que estás organizando frutas. Si tienes $2$ manzanas y te dan $3$ manzanas, tienes $5$ manzanas. Pero si tienes $2$ manzanas y $3$ naranjas, no puedes decir que tienes $5$ "manzanzaranjas". En matemáticas, los radicales funcionan igual: solo puedes sumar o restar radicales que tengan el **mismo índice** y el **mismo radicando** (el número de adentro). A estos se les llama **términos semejantes**.

> [!warning] **⚠️ Error común**
> Un error muy frecuente es pensar que $\sqrt{a} + \sqrt{b} = \sqrt{a+b}$. 
> **Prueba esto:** $\sqrt{9} + \sqrt{16}$ es $3 + 4 = 7$. 
> Sin embargo, $\sqrt{9+16} = \sqrt{25} = 5$. 
> Claramente, $7 \neq 5$. **¡Nunca los sumes directamente!**
> 
> **Nota importante:** Si los términos no son semejantes (tienen diferente índice o radicando) y no se pueden simplificar para ser iguales, la operación simplemente se deja indicada: $14\sqrt[3]{2} - 6\sqrt[3]{3}$.

> [!tip] **💡 Truco para recordarlo**
> Piensa en el radical como un **"apellido"**. Solo puedes sumar a las personas que tienen el mismo apellido. Si tienes $5\sqrt{2}$ y $3\sqrt{2}$, ambos son de la familia $\sqrt{2}$. El resultado es $8\sqrt{2}$.

---

## 🛠️ Procedimiento paso a paso

```latex
SUMA Y RESTA DE RADICALES:
1. Simplificar: Descomponer el radicando en factores primos.
2. Extraer factores: Sacar de la raíz los factores cuyo exponente sea igual o múltiplo del índice.
3. Identificar términos semejantes: Agrupar raíces con igual índice y radicando.
4. Operar coeficientes: Sumar o restar los números externos de los términos semejantes. Los términos no semejantes permanecen igual.

MULTIPLICACIÓN (ÍNDICE DIFERENTE):
1. Hallar MCM: Encontrar el Mínimo Común Múltiplo de los índices originales.
2. Propiedad de Equivalencia: Multiplicar el índice y el exponente del radicando por el mismo factor necesario para llegar al MCM. Esto mantiene el valor de la raíz.
3. Unificar: Escribir los radicandos ajustados bajo una sola raíz con el índice común.
4. Simplificar resultado: 
   a) Extraer factores si el exponente es mayor al índice.
   b) Simplificar índice y exponente si comparten un divisor común (ej: \sqrt[6]{x^2} = \sqrt[3]{x}).
```

---

## 📝 Ejemplos detallados

### Ejemplo 1: Suma con simplificación ($\sqrt{40} + \sqrt{90}$)
1.  **Factorización:**
    *   $40 = 2^2 \cdot 2 \cdot 5 = 2^2 \cdot 10$
    *   $90 = 3^2 \cdot 2 \cdot 5 = 3^2 \cdot 10$
2.  **Extracción:**
    *   $\sqrt{2^2 \cdot 10} = 2\sqrt{10}$
    *   $\sqrt{3^2 \cdot 10} = 3\sqrt{10}$
3.  **Operación:** $2\sqrt{10} + 3\sqrt{10} = \mathbf{5\sqrt{10}}$

### Ejemplo 2: Resta con Coeficientes ($5\sqrt{32} - 3\sqrt{8}$)
1.  **Factorización:** $32 = 2^2 \cdot 2^2 \cdot 2$ y $8 = 2^2 \cdot 2$.
2.  **Extracción:** 
    *   $5 \cdot (2 \cdot 2)\sqrt{2} = 5 \cdot 4\sqrt{2} = 20\sqrt{2}$
    *   $3 \cdot (2)\sqrt{2} = 6\sqrt{2}$
3.  **Operación:** $20\sqrt{2} - 6\sqrt{2} = \mathbf{14\sqrt{2}}$

### Ejemplo 3: Multiplicación de Índices Diferentes ($\sqrt[3]{2^2} \cdot \sqrt{3^1}$)
1.  **MCM de índices ($3$ y $2$):** Es $6$.
2.  **Ajuste (Propiedad de Equivalencia):**
    *   $\sqrt[3 \cdot 2]{2^{2 \cdot 2}} = \sqrt[6]{2^4}$
    *   $\sqrt[2 \cdot 3]{3^{1 \cdot 3}} = \sqrt[6]{3^3}$
3.  **Multiplicación y Unificación:** $\sqrt[6]{2^4 \cdot 3^3} = \sqrt[6]{16 \cdot 27} = \mathbf{\sqrt[6]{432}}$

### Ejemplo 4: Aplicación USD
**Problema:** El costo de dos parcelas de tierra es de $\sqrt{50}$ USD y $\sqrt{18}$ USD respectivamente. ¿Cuál es el costo total?
1.  **Simplificar:** $\sqrt{50} = \sqrt{5^2 \cdot 2} = 5\sqrt{2}$ USD.
2.  **Simplificar:** $\sqrt{18} = \sqrt{3^2 \cdot 2} = 3\sqrt{2}$ USD.
3.  **Suma de términos semejantes:** $5\sqrt{2} + 3\sqrt{2} = \mathbf{8\sqrt{2}}$ **USD**.

---

## ✏️ Ejercicios para el estudiante

> [!success] **Bloque Verde: Fácil (Suma y resta directa)**
> 1. $2\sqrt{3} + 5\sqrt{3}$
> 2. $10\sqrt{7} - 4\sqrt{7}$
> 3. $\sqrt{5} \cdot \sqrt{2}$
> 4. $3\sqrt{11} + \sqrt{11} - 2\sqrt{11}$

> [!warning] **Bloque Amarillo: Medio (Simplificación previa)**
> 1. $\sqrt{12} + \sqrt{27}$
> 2. $\sqrt{20} - \sqrt{45} + \sqrt{80}$
> 3. $\sqrt[3]{16} + \sqrt[3]{54}$
> 4. $2\sqrt{50} \cdot 3\sqrt{2}$

> [!danger] **Bloque Rojo: Avanzado (Aplicación USD e Índices Diferentes)**
> 1. Hallar el área de un terreno rectangular con lados $\sqrt{2}$ m y $\sqrt[3]{2}$ m.
> 2. Si el costo del metro cuadrado del terreno anterior es de $100$ USD, ¿cuál es el precio total expresado con radical?
> 3. Multiplicar y simplificar al máximo: $\sqrt[4]{5^2} \cdot \sqrt[3]{5^1}$.
> 4. Simplificar y operar: $3\sqrt[3]{128} - \sqrt[3]{250}$.

> [!check] **Respuestas (Para el docente)**
> **Verde:** 1) $7\sqrt{3}$ | 2) $6\sqrt{7}$ | 3) $\sqrt{10}$ | 4) $2\sqrt{11}$
> **Amarillo:** 1) $5\sqrt{3}$ | 2) $3\sqrt{5}$ | 3) $5\sqrt[3]{2}$ | 4) $60$
> **Rojo:** 1) $\sqrt[6]{32}$ $m^2$ | 2) $100\sqrt[6]{32}$ USD | 3) $\sqrt[6]{5^5}$ (Resultado de $\sqrt[12]{5^{10}}$ simplificando índice y exponente entre $2$) | 4) $7\sqrt[3]{2}$

---

## ✍️ Mini-prueba de autoevaluación
1.  **Conceptual:** ¿Se pueden sumar $\sqrt{2}$ y $\sqrt[3]{2}$? Explica por qué.
2.  **Procedimental:** Para multiplicar $\sqrt[5]{x}$ y $\sqrt[3]{x}$, ¿cuál debe ser el nuevo índice común antes de operar?
3.  **Aplicación USD:** Si una inversión crece a un factor de $\sqrt[3]{8}$ y otra a un factor de $\sqrt{4}$, ¿cuál es el factor total de crecimiento al multiplicarlas? *(Pista: simplifica primero las raíces perfectas).*

---

## 💡 En la próxima clase
Daremos el siguiente paso lógico: **La Racionalización de Radicales**. Aprenderemos cómo eliminar las raíces del denominador para que nuestras expresiones matemáticas sean más fáciles de operar y luzcan profesionales.

---
[[Clase 03]] | [[Indice_Curso]] | [[Clase 05]]