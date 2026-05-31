# Clase 01 — Varianza, Desviación Estándar y Coeficiente de Variación
tags: #algebra #whatisthestanda
Curso: [[00 - Índice del curso]] | Bloque 1 | Lección 1 de 2

---

## 1. Navegación y Metadatos
- **Anterior:** [[00 - Índice del curso]]
- **Siguiente:** [[Clase 02 — Medidas de Dispersión Avanzadas]]

---

## 2. Importancia y Aplicaciones Reales
¡Bienvenidos a esta guía! El promedio es una herramienta útil, pero a veces nos engaña. Para entender la realidad, necesitamos saber qué tan "separados" están los datos entre sí. Medir la dispersión nos permite saber si un grupo es **homogéneo** (todos se parecen) o **heterogéneo** (hay mucha diferencia).

- 💵 **Aplicación financiera:** La desviación estándar mide el riesgo. Si una inversión en $USD tiene un precio promedio de $\$1.50$ pero una desviación de $\$1.00$, el precio suele oscilar entre $\$0.50$ y $\$2.50$. Una desviación alta significa mayor volatilidad y riesgo.
- 🏗️ **Aplicación práctica:** Imagina un lago con una profundidad promedio de $1.5$ metros. Si la desviación estándar es de $1$ metro, podrías caminar por zonas de $0.5$ metros, ¡pero de repente caer en un pozo de $2.5$ metros! La desviación te avisa de esos peligros.
- 📊 **Situación cotidiana:** En un grupo de amigos con promedio de $17$ años, si la desviación es baja, todos tienen edades similares ($16-18$). Si es alta, podrías tener niños de $13$ y adultos de $23$ años en el mismo grupo.

---

## 3. Conceptos Clave y Definiciones

> [!note] ¿Qué es la Desviación Estándar ($\sigma$ o $s$)?
> Imagina que el promedio es el centro de una diana de tiro al blanco. La desviación estándar nos dice, en promedio, qué tan lejos del centro caen las flechas de los competidores. Es la medida de dispersión de los datos con respecto a su promedio.

> [!note] El Coeficiente de Variación ($CV$)
> Es una medida que expresa la desviación estándar como un porcentaje del promedio. Se calcula con la fórmula: 
> $$CV = \left( \frac{\sigma}{\bar{x}} \right) \cdot 100\%$$
> **Regla de Oro:** Si el $CV > 25\%$, decimos que los datos son **heterogéneos** (muy dispersos). Si es menor, son **homogéneos**.

> [!warning] ¡Cuidado con los paréntesis!
> Un error clásico al calcular la varianza es elevar números negativos al cuadrado sin usar paréntesis. Recuerda: $(-3)^2 = 9$. Si lo haces sin paréntesis en la calculadora ($-3^2$), te dará $-9$, lo cual arruinará todo tu proceso, pues las distancias al cuadrado siempre deben ser positivas.

> [!tip] Regla Mnemotécnica del Árbol
> Para no olvidar la relación entre ambos conceptos: La **Varianza** es el **Árbol** (un valor grande y elevado al cuadrado), mientras que la **Desviación Estándar** es su **Raíz** (la operación matemática que aplicamos para volver al tamaño original).

---

## 4. Procedimiento Paso a Paso (Algoritmo de Cálculo)
¡Vamos a convertir estos datos en una sola medida de confianza! Sigue estos pasos universales:

```text
PASO 1: Calcular el promedio (x̄). 
        Suma todos los datos y divide por el total de datos (N).

PASO 2: Restar el promedio a cada dato y elevar el resultado al cuadrado. 
        Operación: (Dato - x̄)²

PASO 3: Calcular la Varianza (σ² o s²).
        Suma todos los resultados del Paso 2 y divide por:
        - N (Si los datos son toda la POBLACIÓN).
        - n - 1 (Si los datos son una MUESTRA).

PASO 4: Obtener la Desviación Estándar (σ o s).
        Aplica la raíz cuadrada al resultado de la Varianza.

PASO 5: Calcular el Coeficiente de Variación (CV).
        Divide la Desviación entre el Promedio y multiplica por 100.
```

---

## 5. Ejemplos Prácticos

```ad-example
title: Ejemplo 1: Edades de niños (Básico - Población)
**Datos:** 5, 6, 6, 7, 8 años.
1. **Promedio ($\bar{x}$):** $(5+6+6+7+8) / 5 = 6.4$ años.
2. **Diferencias al cuadrado:**
   - $(5 - 6.4)^2 = 1.96$
   - $(6 - 6.4)^2 = 0.16$
   - $(6 - 6.4)^2 = 0.16$
   - $(7 - 6.4)^2 = 0.36$
   - $(8 - 6.4)^2 = 2.56$
3. **Varianza ($\sigma^2$):** $\frac{1.96 + 0.16 + 0.16 + 0.36 + 2.56}{5} = 1.04$ años².
4. **Desviación Estándar ($\sigma$):** $\sqrt{1.04} \approx 1.01$ años.
```

```ad-example
title: Ejemplo 2: Pesos y el efecto de los signos (Muestra)
**Datos:** $52, 55, 58$ kg.
1. **Promedio ($\bar{x}$):** $55$ kg.
2. **Cálculo clave:**
   - $(52 - 55)^2 = (-3)^2 = 9$ (Aquí es donde el paréntesis salva tu cálculo).
   - $(55 - 55)^2 = (0)^2 = 0$
   - $(58 - 55)^2 = (3)^2 = 9$
3. **Varianza ($s^2$):** Al ser una muestra, dividimos por $n-1$: $\frac{9 + 0 + 9}{3 - 1} = \frac{18}{2} = 9$ kg².
4. **Desviación Estándar ($s$):** $\sqrt{9} = 3$ kg.
```

```ad-example
title: Ejemplo 3: Respuestas de examen (Datos Agrupados)
**Contexto:** Respuestas correctas de $100$ estudiantes (Muestra).
| Intervalo | Frecuencia ($f$) | Marca de Clase ($x$) | $x \cdot f$ |
| :--- | :--- | :--- | :--- |
| 0-10 | 6 | 5 | 30 |
| 10-20 | 19 | 15 | 285 |
| 20-30 | 45 | 25 | 1125 |
| 30-40 | 22 | 35 | 770 |
| 40-50 | 8 | 45 | 360 |
| **Total** | **$n=100$** | | **$\sum = 2570$** |

1. **Promedio ($\bar{x}$):** $2570 / 100 = 25.7$ respuestas.
2. **Varianza ($s^2$):** Calculamos $\sum f \cdot (x - 25.7)^2$ y dividimos entre $n-1$ ($99$).
   - Resultado: $97.48$ respuestas².
3. **Desviación Estándar ($s$):** $\sqrt{97.48} \approx 9.87$ respuestas.
```

```ad-example
title: Ejemplo 4: Aplicación en $USD y Rango
Si un producto tiene un precio promedio de $\$1.50$ USD y una desviación de $\$1.00$ USD:
- El **rango probable** donde se encuentra la mayoría de los datos es $\bar{x} \pm \sigma$.
- Esto nos da un intervalo de **$\$0.50$ a $\$2.50$**.
- Si el precio de mercado hoy es $\$4.00$, sabremos de inmediato que es un "dato atípico" o muy inusual.
```

---

## 6. Ejercicios para el Estudiante

```ad-abstract
title: Retos de Práctica
**🟢 Fácil:** Hallar Varianza y Desviación de las edades de 3 amigos: $14, 15$ y $16$ años (Población).

**🟡 Medio:** Calcula la dispersión para esta tabla de frecuencias (Muestra):
| Edad ($x$) | Frecuencia ($f$) |
| :--- | :--- |
| 13 | 3 |
| 14 | 1 |
| 15 | 1 |

**🔴 Avanzado ($USD):** 
- Producto A: Promedio = $\$50$, $s = \$2$.
- Producto B: Promedio = $\$50$, $s = \$15$.
¿Cuál es el Coeficiente de Variación ($CV$) de cada uno y cuál es más homogéneo?
```

```ad-success
title: Solucionario
- **🟢 Fácil:** $\sigma^2 = 0.66$; $\sigma = 0.81$ años.
- **🟡 Medio:** $\bar{x} = 13.6$; $s^2 = 0.8$; $s = 0.89$; $CV = 6.5\%$ (Muy homogéneo).
- **🔴 Avanzado:** 
  - $CV_A = (2 / 50) \cdot 100 = 4\%$.
  - $CV_B = (15 / 50) \cdot 100 = 30\%$.
  - **Conclusión:** El Producto A es más homogéneo. El B es heterogéneo ($> 25\%$).
```

---

## 7. Autoevaluación y Cierre

```ad-question
title: ¿Qué tanto aprendiste hoy?
1. **¿Qué indica un Coeficiente de Variación del 35%?**
   - Indica que el grupo es heterogéneo (los datos están muy dispersos), ya que supera el umbral del 25%.
2. **¿Por qué dividimos por $n-1$ en lugar de $N$ a veces?**
   - Dividimos por $n-1$ cuando trabajamos con una **muestra** para dar un margen de error más preciso; usamos $N$ cuando tenemos la **población** completa.
3. **Si la varianza de un conjunto de datos es 25, ¿cuál es su desviación estándar?**
   - Es 5 (la raíz cuadrada de 25).
```

**Notas para el próximo tema:** Ahora que sabes medir qué tan dispersos están los datos, en la siguiente lección aprenderemos a comparar estas medidas en situaciones de toma de decisiones del mundo real. ¡Nos vemos en la Clase 02!

---
**Anterior:** [[00 - Índice del curso]]
**Siguiente:** [[Clase 02 — Medidas de Dispersión Avanzadas]]