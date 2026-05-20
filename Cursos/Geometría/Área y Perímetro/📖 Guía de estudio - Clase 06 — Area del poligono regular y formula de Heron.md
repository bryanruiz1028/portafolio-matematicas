# 📖 Guía de estudio — Clase 06: Área del polígono regular

> [!info] 📌 Conceptos clave
> - **Polígono regular:** Figura geométrica donde todos sus lados tienen la misma longitud y todos sus ángulos internos son iguales.
> - **Apotema ($a$):** Es la distancia técnica medida desde el centro del polígono hasta el **punto medio** de cualquiera de sus lados, de forma perpendicular.
> - **Lógica del área:** Un polígono regular de $n$ lados se puede dividir en $n$ triángulos iguales. El área total es la suma de las áreas de esos triángulos; por eso la fórmula depende del perímetro y el apotema.
> - **Intuición del Rombo:** El área de un rombo es exactamente la **mitad del área de un rectángulo** que tenga como base y altura las diagonales del mismo.
> - **Perímetro ($P$):** Es la longitud total del contorno. Se obtiene sumando todos los lados o multiplicando el número de lados por la medida de uno solo ($n \times L$).

---

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Perímetro ($P$)** | $P = n \times L$ (donde $n$ es el número de lados y $L$ la longitud del lado). |
| **Apotema ($a$)** | Distancia desde el centro del polígono hacia el punto medio de un lado. |
| **Área del Polígono Regular** | $A = \frac{P \times a}{2}$ |
| **Área del Rombo** | $A = \frac{D \times d}{2}$ (Diagonal mayor por diagonal menor entre dos). |
| **Semiperímetro ($s$)** | $s = \frac{P}{2}$ (Utilizado específicamente en la **Fórmula de Herón** para áreas de triángulos). |

---

## Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A: Cálculo básico de un Pentágono
**Problema:** Hallar el área de un pentágono regular cuyo lado mide $6\text{ cm}$ y su apotema es de $4,1\text{ cm}$.

**Paso 1: Calcular el perímetro ($P$)**
Un pentágono tiene $5$ lados iguales.
$P = 5 \times 6\text{ cm} = 30\text{ cm}$

**Paso 2: Aplicar la fórmula del área**
$A = \frac{P \times a}{2}$
$A = \frac{30\text{ cm} \times 4,1\text{ cm}}{2}$
$A = \frac{123}{2} = 61,5\text{ cm}^2$

**Resultado:** El área del pentágono es $61,5\text{ cm}^2$.
```

```ad-example
title: Ejemplo B: Aplicación de costo (Octágono)
**Problema:** Se desea cubrir un octágono regular decorativo con un material sintético. El octágono tiene un lado de $16\text{ cm}$ y un apotema de $19,3\text{ cm}$. Si el costo del material es de $0,50\text{ USD}$ por cada $\text{cm}^2$, ¿cuánto costará cubrir la superficie?

**Paso 1: Calcular el perímetro ($P$)**
Un octágono tiene $8$ lados.
$P = 8 \times 16\text{ cm} = 128\text{ cm}$

**Paso 2: Calcular el área total**
$A = \frac{P \times a}{2} = \frac{128\text{ cm} \times 19,3\text{ cm}}{2}$
$A = \frac{2470,4}{2} = 1235,2\text{ cm}^2$

**Paso 3: Calcular el costo total**
$\text{Costo} = 1235,2\text{ cm}^2 \times 0,50\text{ USD/cm}^2 = 617,60\text{ USD}$

**Resultado:** El presupuesto necesario es de $617,60\text{ USD}$.
```

---

## Ejercicios de Repaso

```ad-abstract
title: 🟢 Bloque: Fácil (Cálculo Directo)
1. Halla el área de un pentágono regular que tiene un perímetro de $40\text{ cm}$ y un apotema de $5,5\text{ cm}$.
2. Calcula el área de un rombo cuyas diagonales miden $10\text{ cm}$ (D) y $6\text{ cm}$ (d).
3. Un polígono tiene un perímetro de $128\text{ cm}$ y un apotema de $19,3\text{ cm}$. ¿Cuál es su área total?
```

```ad-abstract
title: 🟡 Bloque: Medio (Pasos Previos)
1. Calcula el área de un pentágono regular si sabes que cada uno de sus lados mide $10\text{ cm}$ y su apotema mide $6,8\text{ cm}$. (Primero obtén el perímetro).
2. Halla el área de un rombo que tiene un lado de $5\text{ cm}$ y una de sus diagonales mide $8\text{ cm}$.
   *Pista pedagógica: Usa Pitágoras ($5^2 = x^2 + 4^2$) para hallar $x$. Recuerda que $x$ es solo la MITAD de la diagonal faltante; ¡debes multiplicarla por 2 antes de usar la fórmula del área!*
3. Determina el área de un rombo cuyo lado mide $13\text{ m}$ y su diagonal menor mide $10\text{ m}$.
```

```ad-abstract
title: 🔴 Bloque: Avanzado (Aplicación con $USD)
Un arquitecto diseña una fuente con forma de **decágono regular** (10 lados). La fuente tiene un lado de $10\text{ cm}$ y un apotema de $15,4\text{ cm}$. Se debe recubrir el fondo con azulejo sellado que cuesta $1,25\text{ USD}$ por cada $\text{cm}^2$. 
**Reto:** Calcula el perímetro, el área total del decágono y el presupuesto final en dólares para completar el trabajo.
```

---

> [!tip] 💡 Consejo de estudio
> Al trabajar con geometría, la clave está en las **unidades**. Recuerda que el perímetro mide longitud (distancia lineal como $\text{cm}$ o $\text{m}$), pero el área mide superficie. Por lo tanto, el resultado final siempre debe estar expresado en **unidades cuadradas** ($\text{cm}^2, \text{m}^2$). ¡Si no es cuadrado, no es área!