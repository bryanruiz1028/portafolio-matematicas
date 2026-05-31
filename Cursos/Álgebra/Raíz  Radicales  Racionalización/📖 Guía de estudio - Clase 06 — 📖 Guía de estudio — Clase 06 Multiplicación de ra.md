# 📖 Guía de estudio — Clase 06: Multiplicación de radicales con diferentes índices

¡Qué tal amigos! Espero que estén muy bien. Bienvenidos a esta guía donde aprenderemos a dominar la multiplicación de raíces cuando los índices no son iguales. Como siempre les digo, vamos paso a paso para que nadie se me pierda.

> [!info] 📌 Conceptos clave
> - **Imposibilidad de operación directa**: No podemos multiplicar radicales si sus índices son diferentes (por ejemplo, una raíz cuadrada por una raíz cúbica).
> - **Mínimo Común Índice**: Para poder operar, es obligatorio hallar el Mínimo Común Múltiplo (MCM) de los índices originales para homogeneizarlos.
> - **Amplificación equilibrada**: Si multiplicamos el índice por un factor, debemos multiplicar también todos los exponentes internos por ese mismo factor para mantener la igualdad.
> - **Propiedad de la potenciación**: Una vez que las raíces tienen el mismo índice, se unen en una sola y se suman los exponentes de las bases iguales.

## TABLA DE FÓRMULAS Y DEFINICIONES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Mínimo Común Índice** | Es el valor común que obtendremos al calcular el MCM de los índices de todos los radicales del ejercicio. |
| **Factores Primos** | El proceso de descomponer los coeficientes (ej. $25 = 5^2$) antes de empezar. Es fundamental para poder sumar exponentes después. |
| **Propiedad de Multiplicación** | $\sqrt[n]{a} \cdot \sqrt[m]{b} \rightarrow \sqrt[MCI]{a^k \cdot b^j}$, donde $k = \frac{MCI}{n}$ y $j = \frac{MCI}{m}$. |

---

````ad-example
title: Ejemplo A — Multiplicación con variables
**Ejercicio**: $\sqrt[4]{25x^6y^3} \cdot \sqrt[6]{125x^5}$

**Paso 1: Descomposición en factores primos**
Antes de cualquier cosa, transformamos los números: $25 = 5^2$ y $125 = 5^3$.
La expresión queda: $\sqrt[4]{5^2x^6y^3} \cdot \sqrt[6]{5^3x^5}$

**Paso 2: Cálculo del Mínimo Común Índice**
Buscamos el MCM entre los índices 4 y 6. El resultado es **12**. Este será nuestro nuevo índice.

**Paso 3: Amplificación (Multiplicar índices y exponentes)**
- Para la primera raíz: $\frac{12}{4} = 3$. Multiplicamos todos sus exponentes internos por 3.
  $\sqrt[12]{5^{2\times3} x^{6\times3} y^{3\times3}} = \sqrt[12]{5^6 x^{18} y^9}$
- Para la segunda raíz: $\frac{12}{6} = 2$. Multiplicamos todos sus exponentes internos por 2.
  $\sqrt[12]{5^{3\times2} x^{5\times2}} = \sqrt[12]{5^6 x^{10}}$

**Paso 4: Unión y suma de exponentes**
Metemos todo a la misma "cárcel" y sumamos los exponentes de las bases iguales:
$\sqrt[12]{5^6 \cdot 5^6 \cdot x^{18} \cdot x^{10} \cdot y^9} = \sqrt[12]{5^{12} x^{28} y^9}$

**Paso 5: Simplificación final (Salida de la cárcel)**
Aquí aplicamos el truco de la división ($exponente \div índice$):
- Para el $5^{12}$: $12 \div 12 = 1$ (sale con exponente 1) y sobra 0.
- Para el $x^{28}$: $28 \div 12 = 2$ (salen 2 equis, es decir $x^2$) y sobran 4 ($x^4$ se queda adentro).
- Para el $y^9$: Como $9 < 12$, no puede salir.

**Resultado final**: $5x^2 \sqrt[12]{x^4 y^9}$
````

---

````ad-example
title: Ejemplo B — Cálculo de área con presupuesto
**Contexto**: Un arquitecto necesita calcular el área de un panel rectangular de base $\sqrt[3]{4a^2}$ metros y altura $\sqrt[4]{2a}$ metros. El costo del material es de $1 USD por metro cuadrado.

**Resolución paso a paso**:
1. **Factores primos**: Escribimos el 4 como $2^2$. Tenemos $\sqrt[3]{2^2a^2} \cdot \sqrt[4]{2a}$.
2. **Mínimo Común Índice**: El MCM de 3 y 4 es **12**.
3. **Amplificación**:
   - Raíz 1: $\frac{12}{3} = 4$. Multiplicamos exponentes por 4: $\sqrt[12]{2^{2\times4} a^{2\times4}} = \sqrt[12]{2^8 a^8}$.
   - Raíz 2: $\frac{12}{4} = 3$. Multiplicamos exponentes por 3: $\sqrt[12]{2^{1\times3} a^{1\times3}} = \sqrt[12]{2^3 a^3}$.
4. **Operación**: Unimos y sumamos: $\sqrt[12]{2^{8+3} a^{8+3}} = \sqrt[12]{2^{11} a^{11}}$.

**Resultado Final**:
- **Área**: $\sqrt[12]{2^{11} a^{11}} \text{ m}^2$ (No se extraen factores porque los exponentes 11 son menores que 12).
- **Presupuesto**: Dado que el costo es $\$1$ por m², el costo total es de **$\$1 \times \sqrt[12]{2^{11} a^{11}}$ USD**.
````

---

## BLOQUE DE EJERCICIOS DE REPASO

````ad-abstract
title: 🟢 Nivel: Fácil
color: 0, 200, 0
1. $\sqrt{x} \cdot \sqrt[3]{x}$
2. $\sqrt[3]{a^2} \cdot \sqrt[4]{a}$
3. $\sqrt[2]{y^3} \cdot \sqrt[5]{y^2}$
````

````ad-abstract
title: 🟡 Nivel: Medio
color: 255, 200, 0
1. $\sqrt[3]{9x^2} \cdot \sqrt[6]{3x^4}$ (Pista: $9 = 3^2$)
2. $\sqrt[4]{16y^5} \cdot \sqrt[3]{8y^2}$ (Pista: $16 = 2^4, 8 = 2^3$)
3. $\sqrt[5]{27m^3} \cdot \sqrt[2]{3m}$ (Pista: $27 = 3^3$)
````

````ad-abstract
title: 🔴 Nivel: Avanzado — Aplicación con $USD
color: 200, 0, 0
Calcula el volumen de un contenedor con dimensiones: $\sqrt{2a}$ m, $\sqrt[5]{4a^3}$ m y $\sqrt[10]{2a^2}$ m. Si el costo de mantenimiento es de **$5 USD** por cada unidad del resultado del radical final:
1. Halla el radical simplificado (MCM de 2, 5 y 10).
2. Calcula el costo total multiplicando por 5.

> [!check] Verificación del resultado
> El radical simplificado es $2a \sqrt[10]{2^3 a^3}$. Por tanto, el costo final es: **$10a \sqrt[10]{2^3 a^3}$ USD**.
````

---

> [!tip] 💡 Consejo de estudio: El Método de la Cárcel (Versión Profe Alex)
> Para saber qué factores salen de la raíz, imagina que el índice es el precio de la fianza en años. 
> 
> Si tienes $\sqrt[12]{x^{28}}$, el exponente 28 son los años que tiene el prisionero. Dividimos: $28 \div 12$. El cociente es **2** (salen dos $x$ de la cárcel como $x^2$) y el residuo es **4** (se quedan 4 años pendientes, es decir, $x^4$ se queda adentro). 
> 
> ¡Recuerda! Si el exponente es menor al índice, no tiene suficiente para pagar la fianza y se queda encerrado.