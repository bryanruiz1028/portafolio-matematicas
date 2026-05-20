# 📖 Guía de estudio — Clase 04: Perímetro y área de un polígono regular conociendo su apotema

> [!info] 📌 Conceptos clave
> Un **polígono regular** es una figura geométrica donde todos sus lados ($L$) y ángulos internos son iguales. Para entender cómo calcular su área ($A$) a partir de la **apotema** ($a$), debemos visualizar el interior de la figura.
> 
> Imagina que trazamos líneas desde el centro hacia cada vértice: el polígono se divide en $n$ triángulos isósceles iguales. Si dividimos uno de esos triángulos por la mitad usando la apotema, obtenemos un **triángulo rectángulo**. 
> 
> En este triángulo rectángulo:
> *   La **apotema ($a$)** funciona como el *cateto adyacente*.
> *   La **mitad del lado ($x$)** es el *cateto opuesto*.
> *   Usamos la función **Tangente** porque relaciona ambos catetos, permitiéndonos hallar la medida del lado que nos falta. Dividimos el ángulo central entre $2n$ precisamente para trabajar con este medio triángulo fundamental.

## 📐 Fórmulas y Definiciones

Para resolver cualquier ejercicio de forma profesional y exacta, seguiremos esta secuencia lógica. Asegúrate de usar siempre el formato correcto para tus variables.

| Término | Definición / Fórmula |
| :--- | :--- |
| **Ángulo central ($ \theta $)** | Es la mitad del ángulo de un triángulo interno: $\theta = 360^\circ / (2 \times n)$ |
| **Valor $x$ (mitad del lado)** | Calculado mediante trigonometría: $x = a \times \tan(\theta)$ |
| **Lado ($L$)** | Es el doble de nuestro valor $x$: $L = 2 \times x$ |
| **Perímetro ($P$)** | La suma de todos los lados: $P = n \times L$ |
| **Área ($A$)** | Espacio total cubierto por el polígono: $A = \frac{P \times a}{2}$ |

---

## 📝 Ejemplo A — Caso Básico (Pentágono)

```ad-example
title: Ejemplo A — Pentágono con Apotema de 11m
**Datos del problema:** $n = 5$ lados, $a = 11\text{m}$.

**Paso 1: Calcular el ángulo de trabajo ($\theta$)**
$\theta = 360^\circ / (2 \times 5) = 360^\circ / 10 = 36^\circ$

**Paso 2: Hallar $x$ (cateto opuesto / mitad del lado)**
$x = 11 \times \tan(36^\circ) \approx 7.99\text{m}$. 
*(Nota pedagógica: En este ejemplo redondearemos a $8\text{m}$ para facilitar la comprensión, pero en tus exámenes procura usar al menos dos decimales para mayor precisión).*

**Paso 3: Hallar la medida del lado ($L$)**
Como $x$ es solo la mitad, multiplicamos por dos:
$L = 8\text{m} \times 2 = 16\text{m}$

**Paso 4: Calcular el Perímetro ($P$)**
$P = 5 \times 16\text{m} = 80\text{m}$

**Paso 5: Calcular el Área ($A$)**
$A = (80\text{m} \times 11\text{m}) / 2 = 880 / 2 = 440\text{m}^2$

**Resultado:** El área del pentágono es de $440\text{m}^2$ ✅
```

---

## 🛠️ Ejemplo B — Aplicación Real (Hexágono)

```ad-example
title: Ejemplo B — Diseño de una mesa hexagonal
**Contexto:** Se diseña una mesa hexagonal ($n = 6$) con una apotema de $7\text{cm}$. El material de la superficie cuesta $0.50 \text{ USD}$ por cada $\text{cm}^2$. ¿Cuál es el costo total del tope?

**Paso 1: Ángulo ($\theta$)**
$\theta = 360^\circ / (2 \times 6) = 30^\circ$

**Paso 2: Mitad del lado ($x$)**
$x = 7 \times \tan(30^\circ) \approx 4.04\text{cm}$

**Paso 3: Lado ($L$) y Perímetro ($P$)**
$L = 4.04\text{cm} \times 2 = 8.08\text{cm}$
$P = 6 \times 8.08\text{cm} = 48.48\text{cm}$

**Paso 4: Área ($A$)**
$A = (48.48\text{cm} \times 7\text{cm}) / 2 = 169.68\text{cm}^2$

**Paso 5: Cálculo de presupuesto final**
$\text{Costo} = 169.68\text{cm}^2 \times 0.50 \text{ USD/cm}^2 = 84.84 \text{ USD}$

**Resultado:** El costo total del material para la mesa es de $84.84 \text{ USD}$ ✅
```

---

## 🧠 Ejercicios de Repaso

```ad-abstract
title: 🟢 Nivel Fácil
Calcula el perímetro ($P$) y el área ($A$) de un **octágono regular** ($n = 8$) cuya apotema ($a$) mide $10\text{cm}$. 
*Pista: Inicia obteniendo el ángulo $\theta = 360 / 16$.*
```

```ad-abstract
title: 🟡 Nivel Medio
Un polígono de **10 lados** (decágono) tiene una apotema de $15\text{m}$. 
1. Calcula el área ($A$) total del polígono siguiendo los pasos aprendidos.
2. Explica: ¿Cuántos triángulos isósceles se forman en su interior y en cuántos triángulos rectángulos totales se divide el polígono para usar la tangente?
```

```ad-abstract
title: 🔴 Nivel Avanzado — Aplicación Económica
Se desea cubrir un piso con forma de **heptágono regular** ($n = 7$) que tiene una apotema ($a$) de $4\text{m}$. Si el metro cuadrado de baldosa cuesta $15 \text{ USD}$:
1. Determina el área total del piso (usa $\theta = 360 / 14$).
2. Calcula el presupuesto total necesario para la obra.
```

---

> [!tip] 💡 Consejo de estudio
> **1. Modo de la calculadora:** Antes de usar la función `tan`, verifica que tu calculadora esté en modo **"DEG"** (grados sexagesimales). Si está en "RAD" o "GRAD", tus cálculos de $x$ serán erróneos.
> 
> **2. Unidades de medida:** No olvides la coherencia técnica. El perímetro ($P$) y el lado ($L$) se expresan en unidades lineales ($m, cm$), pero el área ($A$) **siempre** debe expresarse en unidades cuadradas ($m^2, cm^2$). ¡Esto es vital en ingeniería y arquitectura!