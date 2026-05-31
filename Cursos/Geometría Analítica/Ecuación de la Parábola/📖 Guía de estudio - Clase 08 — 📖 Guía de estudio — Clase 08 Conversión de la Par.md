# 📖 Guía de estudio — Clase 08: Conversión de la Parábola de la Ecuación General a la Forma Canónica u Ordinaria

> [!info] 📌 Conceptos fundamentales para el éxito
> Para dominar la parábola, debemos transformar su expresión "desordenada" (General) en una estructura que nos permita "leer" sus elementos (Canónica). Sigue esta secuencia lógica:
> 
> 1.  **Identificación y Paso 0:** Reconocemos la parábola porque solo una variable está al cuadrado. **Regla de oro:** Si la variable al cuadrado tiene un coeficiente (ej. $2x^2$), debemos dividir toda la ecuación por ese número antes de empezar. Queremos que la variable al cuadrado esté sola y positiva.
> 2.  **Agrupación Estratégica:** Trasladamos los términos con la variable al cuadrado al lado izquierdo. Todo lo demás (la variable lineal opuesta y el término independiente) pasa al lado derecho con signo cambiado.
> 3.  **Completación del Trinomio Cuadrado Perfecto (TCP):** Nos centramos en el coeficiente del término lineal del lado izquierdo (llamémoslo $D$ o $E$ según la variable). Aplicamos la fórmula: $(\frac{\text{coeficiente}}{2})^2$. El resultado es nuestro "tercer término".
> 4.  **Balanceo de la Ecuación:** ¡No olvides la igualdad! Lo que sumamos a la izquierda para completar el trinomio, debemos sumarlo exactamente igual a la derecha.
> 5.  **Revelando la estructura (Factorización):** El lado izquierdo se convierte en un binomio al cuadrado: $(\text{variable} \pm \text{raíz del tercero})^2$. En el lado derecho, simplificamos y extraemos como factor común el coeficiente de la variable lineal para dejarla "limpia".

## Fórmulas y Referencia Visual

| Término | Definición / Función | Estructura Matemática |
| :--- | :--- | :--- |
| **Ecuación General** | Estado inicial donde todos los términos están igualados a cero. | $Ax^2 + Dx + Ey + F = 0$ <br> $Cy^2 + Dx + Ey + F = 0$ |
| **Ecuación Canónica** | Revela el **Vértice $(h, k)$**. Al observar $(x-h)^2$, el vértice usa el signo opuesto. | $(x-h)^2 = 4p(y-k)$ <br> $(y-k)^2 = 4p(x-h)$ |
| **Paso del TCP** | Técnica para convertir dos términos en un trinomio factorizable. | $\text{Tercer término} = \left(\frac{\text{coeficiente lineal}}{2}\right)^2$ |
| **Factorización Forzada** | Asegura que la variable lineal derecha tenga coeficiente 1. | $4p(variable \pm \text{valor})$ |

---

## Ejemplos Resueltos Paso a Paso

```ad-example
title: Ejemplo A — Dominando la variable "x" al cuadrado
**Problema:** Convierte $x^2 - 6x - 12y - 15 = 0$ a su forma canónica.

1. **Agrupar:** Dejamos las $x$ a la izquierda: $x^2 - 6x = 12y + 15$.
2. **Completar TCP:** Tomamos el coeficiente lineal (6). Calculamos $(6/2)^2 = 3^2 = 9$.
3. **Balancear:** Sumamos 9 en ambos lados: $x^2 - 6x + 9 = 12y + 15 + 9$.
4. **Factorizar:**
   - Izquierda: La raíz de $x^2$ es $x$, la de 9 es 3. Signo central negativo $\to (x-3)^2$.
   - Derecha: Simplificamos $12y + 24$.
5. **Factor Común:** Extraemos el 12 para que la $y$ quede sola: $12(y+2)$.

✅ **Resultado:** $(x-3)^2 = 12(y+2)$
💡 **Interpretación Pedagógica:** El vértice se "lee" cambiando los signos de los números dentro de los paréntesis. Aquí, el vértice está en $(3, -2)$.
```

```ad-example
title: Ejemplo B — Aplicación: Punto de equilibrio en inversión ($USD)
**Contexto:** La curva de costos de suministros sigue la ecuación $y^2 + 16y - 15x + 79 = 0$. Convierte a forma canónica para hallar el punto crítico de inversión ($x$).

1. **Agrupar:** $y^2 + 16y = 15x - 79$.
2. **Completar TCP:** Coeficiente lineal es 16. $(16/2)^2 = 8^2 = 64$.
3. **Balancear:** $y^2 + 16y + 64 = 15x - 79 + 64$.
4. **Simplificar:** $(y+8)^2 = 15x - 15$.
5. **Factor Común:** Extraemos el 15: $15(x-1)$.

✅ **Resultado:** $(y+8)^2 = 15(x-1)$
📈 **Análisis:** El vértice está en $(1, -8)$. En este modelo económico, el valor $x=1$ representa la inversión mínima (punto de equilibrio) donde la parábola cambia su trayectoria de costos.
```

---

## Desafíos de Práctica

```ad-abstract
title: 🟢 Nivel Inicial (Coeficiente 1)
1. Convierte: $x^2 + 8x + 8y + 8 = 0$ 
   *(Pista: El resultado debe mostrar una parábola que abre hacia abajo).*
2. Convierte: $y^2 + 6y - 8x + 33 = 0$.
3. Convierte: $x^2 - 4x - 4y = 0$.
```

```ad-abstract
title: 🟡 Nivel Intermedio (Requiere "Paso 0")
1. **Divide y vencerás:** Convierte $2x^2 - 12x - 2y + 14 = 0$. Primero divide toda la ecuación entre 2.
2. Convierte: $3y^2 - 18y - 12x + 15 = 0$. Recuerda que la $y^2$ debe iniciar con coeficiente 1.
```

```ad-abstract
title: 🔴 Nivel Avanzado (Fracciones y Trayectoria)
**Reto del Dron:** Un dron de carga sigue la trayectoria $y^2 - y - 3x - \frac{41}{4} = 0$.
1. Al completar el TCP, usa el coeficiente lineal (1) para obtener $(1/2)^2 = 1/4$.
2. Suma $1/4$ a ambos lados. A la derecha tendrás $3x + \frac{42}{4}$, que se simplifica a $3x + \frac{21}{2}$.
3. **Pista Pro:** Para dejar la $x$ sola, factoriza el 3 dividiendo la fracción: $\frac{21}{2} \div 3$.

> [!tip] 💡 La Ley del Sándwich
> Para dividir una fracción entre un entero: $\frac{21}{2} \div \frac{3}{1} = \frac{21 \times 1}{2 \times 3} = \frac{21}{6}$. 
> **¡No olvides simplificar!** $\frac{21}{6}$ tiene tercera: $\frac{7}{2}$.
```

---

> [!tip] 🎓 Consejo del Experto
> **Verificación Maestra:** ¿Dudas de tu resultado? Expande el binomio al cuadrado y multiplica el factor común de vuelta. Si regresas a la ecuación original (tras igualar a cero), ¡tu procedimiento es impecable! 
> 
> Además, recuerda: si la $x$ está al cuadrado, la parábola es vertical (abre arriba/abajo). Si la $y$ está al cuadrado, es horizontal (abre izquierda/derecha). ¡Visualizarlo te da una ventaja competitiva!