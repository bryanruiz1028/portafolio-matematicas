# 📖 Guía de estudio — Clase 07: Inecuaciones Racionales

> [!info] 📌 Conceptos clave
> Para dominar las inecuaciones racionales, un estudiante de bachillerato debe integrar estos tres pilares fundamentales:
> - **Comparación obligatoria con cero:** La expresión debe estar comparada con cero ($>0, <0, \geq0, \leq0$). Si existen términos en ambos lados, se trasladan mediante sumas o restas; nunca se debe "pasar a multiplicar" una expresión con $x$ al otro lado, ya que su signo desconocido podría invertir la desigualdad.
> - **Identificación de puntos críticos:** Se deben hallar los valores que anulan tanto el numerador como el denominador. Estos puntos actúan como "fronteras" en la recta numérica.
> - **Restricción del denominador:** Un denominador nunca puede ser cero. Por ello, los puntos críticos del denominador siempre serán valores excluidos (intervalos abiertos).

---

### FÓRMULAS Y DEFINICIONES IMPORTANTES

| Término | Definición / Fórmula |
| :--- | :--- |
| **Inecuación Racional** | Desigualdad entre expresiones algebraicas fraccionarias. Para el análisis de signos, se busca que los factores sean lineales (grado $x^1$). |
| **Punto Crítico** | Son los "valores frontera" obtenidos al igualar cada factor a cero ($x = a$). Dividen la recta numérica en los intervalos que probaremos. |
| **Valor Excluido** | Valores que anulan el denominador. En la recta y en la notación de intervalos, estos puntos **siempre** llevan paréntesis (abiertos), incluso si la inecuación incluye el signo igual ($\leq$ o $\geq$). |

---

### EJEMPLOS RESUELTOS CON ANÁLISIS TÉCNICO

```ad-example
title: Ejemplo A — Análisis de signos con varios factores
**Problema:** Resolver $\frac{(x+4)(x+2)}{x-1} \leq 0$

**1. Identificación de puntos críticos (¿Dónde se hace cero la expresión?):**
- Numerador: $x+4=0 \Rightarrow x=-4$; $x+2=0 \Rightarrow x=-2$ (Ambos pueden incluirse porque la inecuación es $\leq$).
- Denominador: $x-1=0 \Rightarrow x=1$ (**Valor excluido**, siempre abierto).

**2. Definición de intervalos en la recta numérica:**
Ubicamos los puntos $-4, -2$ y $1$ para dividir la recta en cuatro zonas de prueba.

**3. Tabla visual de análisis de signos:**
Evaluamos un número dentro de cada intervalo en cada factor para determinar el signo resultante:

| Intervalo | Factor $(x+4)$ | Factor $(x+2)$ | Factor $(x-1)$ | Signo Total | ¿Cumple $\leq 0$? |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $(-\infty, -4)$ | $-$ | $-$ | $-$ | $(-)$ | **SÍ** |
| $(-4, -2)$ | $+$ | $-$ | $-$ | $(+)$ | NO |
| $(-2, 1)$ | $+$ | $+$ | $-$ | $(-)$ | **SÍ** |
| $(1, \infty)$ | $+$ | $+$ | $+$ | $(+)$ | NO |

**4. Construcción del conjunto solución:**
Unimos los intervalos donde el signo total fue negativo. Respetamos la inclusión de los puntos del numerador y la exclusión del denominador:
**Solución:** $(-\infty, -4] \cup [-2, 1)$
```

```ad-example
title: Ejemplo B — Comparación de costos unitarios ($USD)
**Escenario:** El costo de un proveedor A es $\frac{x}{4-2x}$ y el del proveedor B es $\frac{3}{4-2x}$. ¿Para qué valores de $x$ el proveedor A es más económico o igual ($\leq$) al proveedor B?

**1. Traslado de términos y resta de fracciones:**
$$\frac{x}{4-2x} \leq \frac{3}{4-2x} \Rightarrow \frac{x}{4-2x} - \frac{3}{4-2x} \leq 0 \Rightarrow \frac{x-3}{4-2x} \leq 0$$

**2. Puntos críticos y naturaleza de los puntos:**
- Numerador: $x-3=0 \Rightarrow x=3$ (Cerrado, punto de economía igual).
- Denominador: $4-2x=0 \Rightarrow 4=2x \Rightarrow x=2$ (Abierto, restricción del dominio).

**3. Evaluación de intervalos (Cuidado con el coeficiente negativo):**
Aquí el signo del denominador "se voltea" porque la $x$ tiene un coeficiente negativo ($-2$).
- **Intervalo $(-\infty, 2)$:** Probamos $x=0 \Rightarrow \frac{0-3}{4-2(0)} = \frac{-3}{4} = (-)$. **Cumple.**
- **Intervalo $(2, 3)$:** Probamos $x=2.5 \Rightarrow \frac{2.5-3}{4-2(2.5)} = \frac{-0.5}{4-5} = \frac{-0.5}{-1} = (+)$. **No cumple.**
- **Intervalo $(3, \infty)$:** Probamos $x=4 \Rightarrow \frac{4-3}{4-2(4)} = \frac{1}{-4} = (-)$. **Cumple.**

**4. Solución lógica:**
El proveedor A es más económico en los rangos donde la expresión es negativa.
**Resultado:** $x \in (-\infty, 2) \cup [3, \infty)$.
```

---

### EJERCICIOS DE REPASO

```ad-abstract
title: 🟢 Fácil
Determine el conjunto solución para las siguientes inecuaciones básicas:
1. $\frac{(x+5)(x-3)}{2x+1} \geq 0$
2. $\frac{(x+1)(x+6)}{x-2} \leq 0$
3. $\frac{x(x-4)}{x+7} \geq 0$
```

```ad-abstract
title: 🟡 Medio
Resuelva aplicando el análisis de factores de potencia par:
*(Recuerda: los términos al cuadrado no cambian el signo de la zona, pero su valor crítico debe ser analizado).*
1. $\frac{2x-1}{(3x+4)^2} \geq 0$
2. $\frac{(x-5)^2}{x+2} < 0$
3. $\frac{4x+8}{x^2} \leq 0$
```

```ad-abstract
title: 🔴 Avanzado — Aplicación con $USD
Modele y resuelva los siguientes escenarios de límites presupuestarios:
1. $\frac{3x}{x+1} \leq \frac{5}{x+1}$ (Encuentre el rango de $x$ para no exceder el presupuesto).
2. $\frac{2x}{x-4} \geq \frac{10}{x-4}$ (Determine cuándo el costo marginal es rentable).
3. $\frac{x+8}{2x-6} < \frac{2}{2x-6}$ (Analice el límite estricto de inversión. *Nota: Al ser "<", ningún punto crítico se incluye*).
```

---

> [!tip] 💡 Consejo de estudio
> **La regla de oro:** Antes de graficar, marca siempre el punto crítico del denominador con un círculo abierto en tu recta numérica. Esto te recordará visualmente que ese valor **nunca** puede llevar corchete, sin importar si la inecuación es $\geq$ o $\leq$.
>
> **Atajo de diseño técnico:** Si detectas un factor elevado al cuadrado (como $(x-3)^2$), trátalo como un "siempre positivo". No cambiará los signos a los lados de su punto crítico, lo que simplifica tu tabla de análisis a solo los factores de potencia impar.