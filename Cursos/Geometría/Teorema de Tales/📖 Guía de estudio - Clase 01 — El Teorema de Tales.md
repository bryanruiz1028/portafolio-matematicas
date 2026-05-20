# 📖 Guía de estudio — Clase 01: El Teorema de Tales

> [!info] 📌 Conceptos clave
> El Teorema de Tales es un pilar fundamental de la geometría plana que nos permite comprender la relación de proporcionalidad entre figuras. Según las enseñanzas del Profe Alex, debemos dominar estos cuatro pilares:
> - **Semejanza:** Dos figuras son semejantes cuando mantienen la misma forma exacta, aunque posean tamaños distintos.
> - **Igualdad de Ángulos:** Para que exista semejanza, los ángulos correspondientes entre las figuras deben ser idénticos en su amplitud.
> - **Proporcionalidad de Lados:** Los lados correspondientes deben guardar una relación constante; al dividirlos, el resultado (razón) siempre es el mismo.
> - **Condición de Paralelismo:** Si en un triángulo se traza una línea paralela a cualquiera de sus lados, el nuevo triángulo generado será necesariamente semejante al original.

## 2. Tabla de Fórmulas y Definiciones

| Término | Definición / Fórmula |
| :--- | :--- |
| **Semejanza** | Relación entre figuras con la misma forma y **ángulos correspondientes iguales**, pero distinto tamaño. |
| **Lados Proporcionales** | Relación donde la división entre las medidas de los lados que ocupan la misma posición relativa da un resultado constante. |
| **Razón de Semejanza** | Es el cociente o resultado de la división entre los lados. Define la **escala** (o factor de escala) entre las figuras (ej. si una es el doble o el triple). |
| **Proporción (Fórmula)** | Representa la igualdad entre dos razones: $\frac{LadoGrande}{LadoPequeño} = \frac{OtroLadoGrande}{OtroLadoPequeño}$ |

## 3. Ejemplos Resueltos Adicionales

````ad-example
title: Ejemplo A — Triángulos Semejantes Básicos 
**Enunciado:** Dados dos triángulos semejantes, el primero con lados de $9$, $12$ y $n$, y el segundo con lados de $3$, $m$ y $5$, halla los valores de $m$ y $n$.

**Paso 1: Identificación de parejas correspondientes**
¡Observa bien! Relacionamos los lados del triángulo grande (numerador) con sus parejas en el pequeño (denominador):
- Lados de la izquierda: $9 / 3$
- Lados de la derecha: $12 / m$
- Lados de abajo: $n / 5$

**Paso 2: Aplicación de la multiplicación de extremos y medios**
Nota la relación: Al simplificar $9 / 3$, obtenemos una razón de $3$. Esto significa que el triángulo grande es el triple del pequeño.

- **Para hallar $n$:** $\frac{9}{3} = \frac{n}{5} \implies n \cdot 3 = 9 \cdot 5 \implies n = \frac{45}{3} \implies n = 15$.
- **Para hallar $m$:** $\frac{9}{3} = \frac{12}{m} \implies 9 \cdot m = 3 \cdot 12 \implies m = \frac{36}{9} \implies m = 4$.

✅ **Resultado final:** $n = 15$ y $m = 4$.
````

````ad-example
title: Ejemplo B — Aplicación con Presupuesto de Materiales ($USD) 
**Enunciado:** Un marco de madera para un plano cuesta $12\text{ USD}$ y mide $60\text{ cm}$. Si queremos fabricar un marco semejante pero más pequeño de $20\text{ cm}$, ¿cuál será su costo proporcional?

**Procedimiento:**
1. **Identificar la razón de semejanza:** Dividimos la medida original entre la nueva medida para hallar el factor de escala: $60\text{ cm} / 20\text{ cm} = 3$.
2. **Aplicar la lógica de proporcionalidad:** Como el tamaño se reduce a una tercera parte (razón $3$), el costo debe dividirse por esa misma razón.
3. **Cálculo final:** $\frac{12\text{ USD}}{3} = 4\text{ USD}$.

✅ **Resultado:** El costo proporcional es de $4\text{ USD}$.
````

## 4. Ejercicios de Repaso

````ad-abstract
title: 🟢 Nivel: Fácil
1. En dos triángulos anidados, el lado inferior del grande mide $6$ y el del pequeño mide $2$. Si el lado izquierdo del grande mide $3$, ¿cuál es la medida del lado izquierdo del pequeño?
2. **Identificación visual:** Si una línea paralela corta los lados $AB$ y $AC$ de un triángulo en los puntos $B'$ y $C'$ respectivamente, creando el triángulo pequeño $AB'C'$, ¿qué lado de este nuevo triángulo corresponde al lado $AC$ del triángulo original?
````

````ad-abstract
title: 🟡 Nivel: Medio
1. Halla el valor de $y$ en dos triángulos semejantes rotados. El triángulo grande tiene una base de $10$ y un lado de $7.5$. El triángulo pequeño tiene una base de $4$ y un lado correspondiente $y$.
2. En una proporción de semejanza, la base del triángulo grande mide $16$ y la del pequeño mide $7$. Si el lado lateral del pequeño mide $5$, ¿cuánto mide el lado lateral $x$ del grande? (Expresa el resultado con dos decimales).
````

````ad-abstract
title: 🔴 Nivel: Avanzado (Aplicación USD)
Tres terrenos colindantes están divididos por líneas paralelas (segunda forma del Teorema de Tales). Los segmentos medidos en la "Calle A" son de $1\text{ m}$, $2\text{ m}$ y $2.5\text{ m}$ respectivamente. 

Se sabe que el **costo total** de instalar una cerca a lo largo de la "Calle B" (cuyos tramos son proporcionales a los de la "Calle A") es de $55\text{ USD}$. Calcula el costo proporcional en $USD$ de cada uno de los tres tramos individuales de la cerca.
````

## 5. Consejo de Estudio Final

> [!tip] 💡 Estrategia de Cálculo Mental
> Antes de lanzarte a realizar operaciones largas, aplica la lógica de **Escalas** (o Factor de Escala). Identifica la pareja de lados conocidos y pregúntate: "¿Es este lado el doble, el triple o la mitad del otro?". Si descubres que la razón es, por ejemplo, $3$, sabrás que todos los lados y costos del triángulo mayor deben ser el triple que los del menor. Esta verificación rápida te permitirá detectar errores de cálculo en segundos y fortalecerá tu intuición geométrica.