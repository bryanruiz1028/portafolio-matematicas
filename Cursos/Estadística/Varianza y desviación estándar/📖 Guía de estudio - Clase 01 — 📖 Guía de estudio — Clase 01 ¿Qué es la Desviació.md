# 📖 Guía de estudio — Clase 01: ¿Qué es la Desviación Estándar?

> [!info] 📌 Conceptos clave
> - **Grado de dispersión:** La desviación estándar nos dice qué tan "separados" están los datos respecto al promedio. Si la desviación es pequeña, los datos están agrupados; si es grande, están muy dispersos.
> - **El "Rango de Normalidad":** No basta con saber el promedio. La desviación estándar nos permite crear un rango (promedio ± desviación) para entender dónde se encuentra la mayoría de los datos.
> - **La Analogía del Lago:** ¡Cuidado con los promedios! Un lago puede tener una profundidad promedio de 1.5 metros, pero si su desviación estándar es de 1 metro, podrías encontrar zonas de 0.5m (seguras) y pozos de 2.5m (peligrosos). La desviación estándar te da la "realidad" que el promedio oculta.
> - **Homogeneidad vs. Heterogeneidad:** Un grupo es **homogéneo** cuando sus integrantes son muy parecidos entre sí (poca dispersión). Es **heterogéneo** cuando hay mucha diferencia entre ellos (mucha dispersión).
> - **Relación con la Varianza:** La desviación estándar es la raíz cuadrada de la varianza. Hacemos esto para "regresar" a las unidades originales (por ejemplo, pasar de "años al cuadrado" a simplemente "años").

---

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Promedio (Media) ($\bar{x}$)** | Es el centro de los datos. Se obtiene sumando todos los valores ($x$) y dividiendo entre el total de datos ($n$). <br> $\bar{x} = \frac{\sum x}{n}$ |
| **Desviación Estándar (Población) ($\sigma$)** | Se usa cuando tenemos los datos de **todos** los individuos. Dividimos la suma de cuadrados entre $N$. |
| **Desviación Estándar (Muestra) ($s$)** | Se usa cuando trabajamos con una **parte** del grupo. Se divide entre $n - 1$ para ser más exactos matemáticamente. |
| **Varianza ($\sigma^2$ o $s^2$)** | Es el paso previo a la desviación. Mide el promedio de las distancias al cuadrado, pero su unidad queda elevada al cuadrado (ej: $\$USD^2$). |
| **Coeficiente de Variación (CV)** | Nos dice qué tan grande es la desviación comparada con el promedio. <br> $CV = \frac{s}{\bar{x}} \times 100$. <br> **Regla de oro:** <br> 🟢 CV < 25%: Datos Homogéneos. <br> 🔴 CV > 25%: Datos Heterogéneos. |

---

## Ejemplos resueltos adicionales

```ad-example
title: Ejemplo A — Edades de un grupo de amigos
**Contexto:** Tres grupos tienen un promedio de edad de 17 años, pero se comportan distinto.
1. **Grupo 1 (Más agrupado):** Edades: 15, 16, 17, 17, 18, 19. Su desviación es de **1.29**. Al ser pequeña, vemos que casi todos tienen edades muy cercanas al 17.
2. **Grupo 3 (Más disperso):** Edades: 13, 14, 15, 17, 20, 23. Su desviación es de **3.5**. 
**Conclusión:** Aunque ambos promedian 17, el Grupo 3 es más **heterogéneo**. Una desviación de 3.5 nos advierte que hay personas con edades mucho más alejadas del centro (como el chico de 23 años).
```

```ad-example
title: Ejemplo B — Variación de precios en el mercado ($USD)
**Contexto:** Se analiza el precio de un producto en 3 tiendas (tomado como muestra): **$23, $26 y $29 USD**.
1. **Calcular el promedio:** $\bar{x} = \frac{23 + 26 + 29}{3} = \$26$ USD.
2. **Calcular las desviaciones al cuadrado:**
   - $(23 - 26)^2 = (-3)^2 = 9$
   - $(26 - 26)^2 = (0)^2 = 0$
   - $(29 - 26)^2 = (3)^2 = 9$
3. **Hallar la Varianza ($s^2$):** Como es muestra, dividimos entre $n-1$: 
   $\frac{9 + 0 + 9}{3 - 1} = \frac{18}{2} = 9 \$USD^2$ (Unidades al cuadrado).
4. **Desviación Estándar ($s$):** Aplicamos raíz cuadrada para volver a la realidad:
   $\sqrt{9} = 3$. 
**Resultado final:** La desviación es **$3 USD** ✅. Esto significa que los precios suelen variar unos $3 arriba o abajo del promedio de $26.
```

---

## ¡Pon a prueba tu instinto matemático!

```ad-abstract
title: 🟢 Nivel: Explorador (Fácil)
1. Si un conjunto de datos tiene una desviación estándar de 0, ¿qué puedes decir de sus datos?
2. ¿Qué símbolo usarías para representar la desviación estándar si estás estudiando a todos los alumnos de un salón (población)?
3. ¿Por qué es necesario sacar la raíz cuadrada a la varianza al final del proceso?
```

```ad-abstract
title: 🟡 Nivel: Analista (Medio)
Tres personas pesan **52 kg, 55 kg y 58 kg**. Si consideramos estos datos como una **muestra**:
1. Calcula el promedio ($\bar{x}$).
2. Halla la desviación estándar ($s$).
*Pista: El promedio es 55 kg. Sigue los pasos: resta, eleva al cuadrado, suma, divide entre $n-1$ y saca la raíz.*
> **Solución para autochequeo:** $s = 3$ kg.
```

```ad-abstract
title: 🔴 Nivel: Maestro (Avanzado)
Un estudiante ahorra dinero semanalmente. Su promedio de ahorro es de **$20 USD** con una desviación estándar de **$6 USD**.
1. Calcula el Coeficiente de Variación (CV).
2. Determina si sus ahorros son homogéneos o heterogéneos usando el umbral del 25%.
> **Lógica:** $CV = (6 / 20) \times 100 = 30\%$. Como $30\% > 25\%$, sus ahorros son **heterogéneos** (varían mucho cada semana).
```

---

> [!tip] 💡 Consejo de estudio
> ¡No dejes que la calculadora te engañe! Al calcular la varianza, es **obligatorio el uso de paréntesis**. Si escribes `15 - 17^2`, la calculadora solo elevará el 17. Debes escribir `(15 - 17)^2`. Recuerda: la desviación estándar es como una "lupa" que nos deja ver qué tan real es el promedio que nos están contando. ¡Sigue practicando!