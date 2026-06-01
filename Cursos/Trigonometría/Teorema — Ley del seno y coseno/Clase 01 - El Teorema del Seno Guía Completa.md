# Clase 01 — El Teorema del Seno: Guía Completa

#algebra #sinetheorem

Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 9

```ad-info
title: 🧭 Navegación
[[Anterior - Introducción a la Trigonometría]] | [[Siguiente - Teorema del Coseno]]
```

---

## 2. ¿POR QUÉ ES IMPORTANTE ESTA CLASE?

¡Hola, amigos! Bienvenidos a esta primera lección. El **Teorema del Seno** (o Ley de los Senos) es la llave maestra para abrir los secretos de los triángulos que no tienen ángulos de 90° (triángulos oblicuángulos). Mientras que Pitágoras nos limita, esta ley nos da libertad total para trabajar en cualquier escenario geométrico.

```ad-info
title: 🌍 Relevancia y aplicaciones
- **💵 Aplicación USD:** Imagina que necesitas cercar un terreno de forma triangular. Conociendo un lado y dos ángulos, puedes hallar los metros de material necesarios. Si cada metro de malla cuesta **$10.000 USD** (o cualquier unidad monetaria), el teorema te permite presupuestar con precisión quirúrgica antes de gastar un solo centavo.
- **🏗️ Aplicación práctica:** En ingeniería civil y arquitectura, se utiliza para la triangulación, permitiendo calcular el ancho de un río o la altura de un edificio sin necesidad de cruzar o escalar.
- **📊 Situación cotidiana:** Es el pilar de la navegación aérea y marítima. Los capitanes lo usan para corregir rutas frente al viento o corrientes marinas, calculando distancias exactas entre puntos geográficos.
```

---

## 3. CONCEPTO CLAVE

```ad-note
title: 📌 ¿Qué es el Teorema del Seno?
Es una ley de proporcionalidad que dicta que, en cualquier triángulo, la razón entre la longitud de un lado y el seno de su ángulo opuesto es siempre la misma (constante).
$$\frac{a}{\sin(A)} = \frac{b}{\sin(B)} = \frac{c}{\sin(C)}$$

**Propiedad Fundamental de Verificación:** 
Antes de dar un resultado por bueno, recuerda: **Al ángulo mayor se opone siempre el lado mayor**, y al ángulo menor se opone el lado menor. Si calculas un ángulo de 80° y su lado opuesto te da más corto que el de un ángulo de 30°, ¡revisa tus cuentas! Es el mejor filtro para detectar errores.
```

```ad-warning
title: ⚠️ Error común: La Calculadora y el Caso Ambiguo
1. **Modo D (Degree):** Asegúrate de que tu calculadora tenga una **"D"** o diga **"DEG"** en la pantalla. Si ves una "R" (Radianes), tus cálculos fallarán. (Usa `SHIFT + SETUP` y selecciona `3:Deg` en modelos estándar).
2. **Ángulo Obtuso:** El arcoseno ($\sin^{-1}$) siempre te dará el ángulo agudo. Si el dibujo del problema muestra claramente un ángulo obtuso (mayor a 90°), debes restar el resultado de 180° ($180^\circ - \theta$) para obtener la medida real.
```

```ad-tip
title: 💡 Truco para recordarlo: "Las Parejas"
Piensa en el triángulo como un baile de parejas: cada lado tiene a su ángulo opuesto justo en frente. Para usar este teorema, solo necesitas **una pareja completa** (lado y ángulo conocidos) y **un dato suelto** de otra pareja.
```

---

## 4. PROCEDIMIENTO PASO A PASO

Sigue esta lógica para no perderte nunca:

```text
PASO 1: Nombra los ángulos (A, B, C) y sus lados opuestos (a, b, c) con minúsculas.
PASO 2: Identifica tu "pareja completa" y el dato de la "pareja incompleta".
PASO 3: Plantea la ecuación. LA REGLA DE ORO: Coloca lo que buscas en el numerador.
        - ¿Buscas un lado? Usa: a / sin(A) = ...
        - ¿Buscas un ángulo? Usa: sin(A) / a = ...
PASO 4: Despeja, usa 3 decimales en tus cálculos y verifica con la propiedad de "ángulo mayor/lado mayor".
```

---

## 5. EJEMPLOS DE APLICACIÓN

### Ejemplo 1: Hallar un lado (Pareja directa)
Dado un triángulo con $A = 60^{\circ}$, lado $a = 15\text{ m}$ y ángulo $B = 48^{\circ}$. Hallar lado $x$ (lado $b$).
1. **Pareja completa:** $A$ y $a$.
2. **Planteo:** $\frac{x}{\sin(48^{\circ})} = \frac{15}{\sin(60^{\circ})}$
3. **Despeje:** $x = \frac{15 \cdot \sin(48^{\circ})}{\sin(60^{\circ})} = \frac{15 \cdot 0.743}{0.866}$
4. **Resultado:** $x \approx 12.871\text{ m}$. (Es menor que 15, lo cual es lógico pues $48^\circ < 60^\circ$).

### Ejemplo 2: Lado con suma de ángulos
En un triángulo, $B = 28^{\circ}$, $C = 100^{\circ}$ y lado $b = 9\text{ m}$. Hallar lado $a$.
1. **Ángulo faltante:** $A = 180^{\circ} - (100^{\circ} + 28^{\circ}) = 52^{\circ}$.
2. **Planteo:** $\frac{a}{\sin(52^{\circ})} = \frac{9}{\sin(28^{\circ})}$
3. **Resultado:** $a = \frac{9 \cdot \sin(52^{\circ})}{\sin(28^{\circ})} = \frac{9 \cdot 0.788}{0.469} \approx 15.111\text{ m}$.

### Ejemplo 3: Hallar un ángulo (Función Inversa)
Dado $A = 42^{\circ}$, $a = 26\text{ m}$ y $b = 34\text{ m}$. Hallar ángulo $B$ ($\theta$).
1. **Planteo (senos arriba):** $\frac{\sin(B)}{34\text{ m}} = \frac{\sin(42^{\circ})}{26\text{ m}}$
2. **Despeje:** $\sin(B) = \frac{34\text{ \cancel{m}} \cdot \sin(42^{\circ})}{26\text{ \cancel{m}}} \approx 0.875$
3. **ArcoSeno:** $B = \sin^{-1}(0.875)$. Usamos la función inversa para "liberar" el ángulo.
4. **Resultado:** $B \approx 61.053^{\circ}$.

### Ejemplo 4: Aplicación Presupuesto ($USD)
Debemos comprar material para el lado $c$ de un terreno. $C = 70^{\circ}$ y la pareja conocida es $a = 20\text{ m}$ con $A = 50^{\circ}$. El costo es **$12 USD/m**.
1. **Lado:** $c = \frac{20 \cdot \sin(70^{\circ})}{\sin(50^{\circ})} = \frac{20 \cdot 0.939}{0.766} \approx 24.536\text{ m}$.
2. **Presupuesto:** $24.536 \cdot 12 = 294.432\text{ USD}$. 
*Nota: Para compras reales, redondearíamos al entero superior ($295 USD) para asegurar material suficiente.*

---

## 6. EJERCICIOS PARA EL ESTUDIANTE

### 🟢 Nivel Fácil (Búsqueda de lado)
1. $A = 36^{\circ}$, $C = 70^{\circ}$, $c = 14\text{ m}$. Hallar lado $a$.
2. $B = 50^{\circ}$, $A = 40^{\circ}$, $a = 10\text{ cm}$. Hallar lado $b$.
3. $C = 80^{\circ}$, $B = 30^{\circ}$, $c = 25\text{ m}$. Hallar lado $b$.
4. $A = 110^{\circ}$, $C = 20^{\circ}$, $a = 50\text{ m}$. Hallar lado $c$.

### 🟡 Nivel Medio (Ángulos y Lados faltantes)
1. Hallar lado $c$ si $A = 45^{\circ}$, $B = 75^{\circ}$ y $a = 12\text{ m}$. (Halla $C$ primero).
2. Hallar ángulo $B$ si $A = 30^{\circ}$, $a = 10\text{ cm}$ y $b = 15\text{ cm}$.
3. Hallar lado $a$ si $C = 100^{\circ}$, $B = 30^{\circ}$ y $c = 20\text{ cm}$.
4. Hallar ángulo $C$ si $B = 55^{\circ}$, $b = 40\text{ m}$ y $c = 35\text{ m}$.

### 🔴 Nivel Avanzado (Análisis y Costos USD)
1. Un terreno tiene un lado de $40\text{ m}$ frente a $60^{\circ}$. Se cerca el lado opuesto a $45^{\circ}$. Costo: **$15 USD/m**. ¿Presupuesto total?
2. En una estructura, $A=38^{\circ}$, $B=82^{\circ}$ y $a=12\text{ m}$. Calcule el costo del lado $c$ si el precio es **$20 USD/m**.
3. Dos torres A y B observan un incendio en C. El ángulo en A es $60^{\circ}$ y en B es $40^{\circ}$. El lado $a$ (opuesto a A) mide $100\text{ m}$. Halle el costo de un cable entre las torres (lado $c$) si cuesta **$5 USD/m**.
4. Jardín con ángulos de $50^{\circ}$ y $60^{\circ}$. El lado opuesto al de $50^{\circ}$ mide $15\text{ m}$. Calcule el costo de bordear el lado más largo si el material cuesta **$8 USD/m**.

---

## 7. RESPUESTAS Y AUTOEVALUACIÓN

```ad-success
title: ✅ Respuestas (Verificadas con 3 decimales)
**Fácil:** 1) 8.755m | 2) 11.918cm | 3) 12.693m | 4) 18.199m
**Medio:** 1) 14.697m | 2) 48.590° | 3) 15.557cm | 4) 45.787°
**Avanzado:** 
1) $489.885 USD (lado = 32.659m)
2) $337.590 USD (lado c = 16.879m)
3) $568.575 USD (ángulo C = 80°, lado c = 113.715m)
4) $147.224 USD (ángulo mayor = 70°, lado = 18.403m)
```

### Mini-prueba
1. **Conceptual:** Si el ángulo $A$ es de 100° y el $B$ de 40°, ¿cuál de los lados ($a$ o $b$) debe ser mayor según la propiedad fundamental?
2. **Procedimental:** ¿Por qué es mejor poner la incógnita en el numerador al plantear la ecuación?
3. **Cálculo rápido:** Si un lado de $10\text{ m}$ está frente a un ángulo de $30^{\circ}$, ¿cuánto mide el lado frente al ángulo de $90^{\circ}$? (Dato: $\sin(90^\circ)=1, \sin(30^\circ)=0.5$).

---

## 8. NOTAS FINALES Y CIERRE

```ad-tip
title: 💡 En la próxima clase
Daremos el salto al **Teorema del Coseno**. Aprenderemos cuándo el Teorema del Seno se queda "corto" (cuando no tenemos una pareja completa) y cómo solucionar esos triángulos.
```

```ad-info
title: 🧭 Navegación
[[Anterior - Introducción a la Trigonometría]] | [[Siguiente - Teorema del Coseno]]
```