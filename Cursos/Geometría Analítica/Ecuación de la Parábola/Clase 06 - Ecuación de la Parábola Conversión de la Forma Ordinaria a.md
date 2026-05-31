# Clase 06 — Ecuación de la Parábola: Conversión de la Forma Ordinaria a General y Viceversa

#algebra #parabola

[[Clase 05|⬅ Clase 05]] | [[00 - Índice del curso|Índice]] | [[Clase 07|Clase 07 ➡]]

---

## 1. Relevancia y Aplicaciones

[!info] 🧭 Navegación
En esta sesión aprenderemos los procedimientos algebraicos para transitar entre las dos representaciones principales de la parábola: la **General** (útil para identificar la cónica) y la **Ordinaria** (indispensable para graficar). Dominar este cambio es el puente necesario para pasar de una expresión abstracta a una representación visual precisa.

[!info] 🌍 Relevancia y aplicaciones
Saber convertir la ecuación de la parábola es fundamental para identificar rápidamente el vértice y el foco, elementos esenciales en el diseño y la ingeniería.
*   **Aplicación $USD:** En la industria de telecomunicaciones, el costo de producción de una antena se modela con estas ecuaciones para minimizar el desperdicio de materiales caros.
*   **Construcción:** Se utiliza en el diseño de arcos monumentales y puentes colgantes, donde la distribución de pesos sigue una trayectoria parabólica.
*   **Situación Cotidiana:** Es la base tecnológica para enfocar las señales de Wi-Fi o televisión satelital. Sin este cálculo, la señal se dispersaría y no llegaría a tu receptor.

---

## 2. Concepto Clave

[!note] 📌 ¿Qué es la Parábola?
Imagina un espejo curvo diseñado de tal forma que toda la luz que llega de lejos rebota y se concentra exactamente en un solo punto (llamado **foco**). Matemáticamente, es el conjunto de puntos que están a la misma distancia de ese foco y de una línea recta llamada **directriz**. ¡Es la forma geométrica perfecta para concentrar energía!

[!warning] ⚠️ Error común
El error más crítico ocurre al **completar el cuadrado**: muchos estudiantes olvidan sumar el número obtenido en **ambos lados** de la igualdad. Si solo lo sumas en un lado, la balanza de la ecuación se rompe y el resultado será incorrecto. También, presta mucha atención a los signos al "mudar" términos de un lado al otro del signo igual.

[!tip] 💡 Truco para recordarlo
Para encontrar el tercer término del trinomio cuadrado perfecto, aplica siempre la regla de oro: **"Saca la mitad y elévalo al cuadrado"**.
1. Toma el número junto a la variable que NO está al cuadrado (la variable lineal).
2. Divídelo entre 2.
3. Multiplica ese resultado por sí mismo (elévate al cuadrado).

---

## 3. Procedimiento Paso a Paso

Para convertir una **Ecuación General** ($Ax^2 + Bx + Cy + D = 0$) a una **Ecuación Ordinaria** ($(x-h)^2 = 4p(y-k)$), sigue esta metodología:

```text
1. AISLAR: Deja los términos de la variable al cuadrado (y su pareja lineal) en 
   el lado izquierdo. Pasa los demás términos al derecho cambiando sus signos.
2. NORMALIZAR: Si la variable al cuadrado tiene un número multiplicándola 
   (coeficiente > 1), divide TODA la ecuación por ese número antes de seguir.
3. COMPLETAR: Toma el coeficiente de la variable lineal de la izquierda, 
   divídelo entre 2 y elévalo al cuadrado. Suma el resultado en AMBOS lados.
4. FACTORIZAR: Convierte el trinomio izquierdo en un binomio al cuadrado. 
   En el lado derecho, extrae como factor común el número que acompaña a la 
   variable para que esta quede sola.
```

---

## 4. Ejemplos de Aplicación

[!ad-example] Ejemplo 1: De Ordinaria a General (Manejo de fracciones)
*Basado en la lógica de la Fuente 4:*
Convertir $(x + \frac{3}{2})^2 = \frac{1}{2}(y + \frac{1}{4})$
1. **Expandir binomio:** $x^2 + 2(x)(\frac{3}{2}) + (\frac{3}{2})^2 \Rightarrow x^2 + 3x + \frac{9}{4}$
2. **Distribuir derecha:** $\frac{1}{2}y + \frac{1}{8}$
3. **Igualar a cero:** $x^2 + 3x - \frac{1}{2}y + \frac{9}{4} - \frac{1}{8} = 0$
4. **Simplificar constantes:** Para restar $\frac{9}{4} - \frac{1}{8}$, convertimos a octavos: $\frac{18}{8} - \frac{1}{8} = \frac{17}{8}$
*Resultado:* **$x^2 + 3x - \frac{1}{2}y + \frac{17}{8} = 0$**

[!ad-example] Ejemplo 2: De General a Ordinaria ($x^2$)
*Basado en la Fuente 1:*
Convertir $x^2 - 6x - 8y - 7 = 0$
1. **Aislar:** $x^2 - 6x = 8y + 7$
2. **Completar:** Mitad de 6 es 3; $3^2 = 9$. Sumamos 9 en ambos lados: $x^2 - 6x + 9 = 8y + 7 + 9$
3. **Simplificar:** $x^2 - 6x + 9 = 8y + 16$
4. **Factorizar:** **$(x - 3)^2 = 8(y + 2)$**

[!ad-example] Ejemplo 3: Caso con $y^2$ (Horizontal)
*Basado en la Fuente 2:*
Convertir $y^2 - 8y - 7x - 5 = 0$
1. **Aislar:** $y^2 - 8y = 7x + 5$
2. **Completar:** Mitad de 8 es 4; $4^2 = 16$. Sumamos 16: $y^2 - 8y + 16 = 7x + 5 + 16$
3. **Simplificar:** $(y - 4)^2 = 7x + 21$
4. **Factor común:** **$(y - 4)^2 = 7(x + 3)$**

[!ad-example] Ejemplo 4: Coeficiente Principal > 1 y Aplicación de Costos
*Adaptado de la Fuente 3 para coherencia económica:*
Convertir $2x^2 - 12x - 16y + 178 = 0$
1. **Dividir entre 2:** $x^2 - 6x - 8y + 89 = 0$
2. **Aislar:** $x^2 - 6x = 8y - 89$
3. **Completar:** $x^2 - 6x + 9 = 8y - 89 + 9 \Rightarrow (x - 3)^2 = 8y - 80$
4. **Final:** **$(x - 3)^2 = 8(y - 10)$**
*Contexto $USD:* Si esta ecuación modela el costo de materiales de una pieza parabólica, el vértice $(3, 10)$ nos indica que el **costo mínimo de producción es de $10 USD**, ubicado en la coordenada horizontal 3. ¡Ahora la economía tiene sentido!

---

## 5. Ejercicios para el Estudiante

[!ad-abstract] Nivel Verde (Fácil)
1. $x^2 - 10x - 10y - 5 = 0$
2. $y^2 - 16y - 15x + 79 = 0$
3. $x^2 + 4x - 8y + 12 = 0$
4. $y^2 + 6y - 4x + 1 = 0$

[!ad-abstract] Nivel Amarillo (Medio)
1. $x^2 + 10x + 10y + 25 = 0$
2. $y^2 - 8y + 7x + 21 = 0$
3. $x^2 - 6x - 12y - 15 = 0$
4. $y^2 + 12y - 8x + 44 = 0$

[!ad-abstract] Nivel Rojo (Avanzado)
1. $3x^2 - 12x - 30y + 162 = 0$
2. $2y^2 - 16y - 14x - 10 = 0$
3. $5x^2 - 20x - 10y + 50 = 0$ (Convertir a Ordinaria)
4. Un presupuesto para una estructura sigue la ecuación $2x^2 - 8x - 12y + 20 = 0$. ¿Cuál es el costo base (valor de $k$) en el punto más bajo?

[!ad-success] Respuestas
*   **Verde:** 1. **$(x-5)^2 = 10(y+3)$** | 2. **$(y-8)^2 = 15(x-1)$** | 3. **$(x+2)^2 = 8(y-1)$** | 4. **$(y+3)^2 = 4(x+2)$**
*   **Amarillo:** 1. **$(x+5)^2 = -10y$** | 2. **$(y-4)^2 = -7(x+1)$** | 3. **$(x-3)^2 = 12(y+2)$** | 4. **$(y+6)^2 = 8(x-1)$**
*   **Rojo:** 1. **$(x-2)^2 = 10(y-5)$** | 2. **$(y-4)^2 = 7(x+3)$** | 3. **$(x-2)^2 = 2(y-3)$** | 4. **$k = 1$ (Costo base de $1 USD)**

---

## 6. Mini-prueba de Autoevaluación

[!ad-question] Pregunta 1
Si tienes el término $-12x$, ¿qué número debes sumar en ambos lados para completar el trinomio cuadrado perfecto?
*   **Respuesta:** **36** (La mitad de 12 es 6, y $6^2 = 36$).

[!ad-question] Pregunta 2
Si en la ecuación general el término al cuadrado es $y^2$, ¿hacia qué ejes puede abrir la parábola?
*   **Respuesta:** Abre **horizontalmente** (hacia la derecha o izquierda).

[!ad-question] Pregunta 3
Si al factorizar obtienes $4p = 10$, y el costo de mantenimiento es de $1,000 USD por cada unidad de la distancia focal $p$, ¿cuál es el gasto total de mantenimiento?
*   **Respuesta:** **$2,500 USD**. (Si $4p = 10$, entonces $p = 2.5$. Multiplicamos $2.5 \times 1,000$).

---

## 7. Notas Finales

¡Excelente trabajo! Has dominado la parte más difícil del álgebra de parábolas. En la próxima sesión (**Clase 07**), utilizaremos la **Ecuación Ordinaria** obtenida hoy para realizar graficaciones precisas, localizando el foco, el vértice y la directriz con total seguridad.

[[Clase 05|⬅ Clase 05]] | [[00 - Índice del curso|Índice]] | [[Clase 07|Clase 07 ➡]]