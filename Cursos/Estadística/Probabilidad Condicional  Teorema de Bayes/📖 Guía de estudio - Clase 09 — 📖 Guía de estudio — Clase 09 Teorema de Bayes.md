# 📖 Guía de estudio — Clase 09: Teorema de Bayes

> [!info] 📌 Conceptos clave
> El Teorema de Bayes es una herramienta de la estadística que nos permite "actualizar" nuestras creencias basándonos en nueva evidencia. Aquí sus puntos esenciales bajo la metodología del Profe Alex:
> - **Invertir la probabilidad:** Permite conocer la probabilidad de una causa dado un efecto observado (conocer el pasado dado el presente).
> - **La importancia de la "pista":** La información adicional o condición dada reduce el espacio muestral. Solo nos enfocaremos en las ramas que cumplen con esa "pista".
> - **Probabilidad A Priori vs. A Posteriori:** Trabajamos con lo que sabemos antes de la prueba (a priori) y lo ajustamos tras conocer el resultado (a posteriori).
> - **Diagrama de árbol:** Es el mapa fundamental para visualizar todos los caminos y no omitir ninguna rama de probabilidad.

## 2. Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Probabilidad Condicional** | $P(A \mid B)$ es la probabilidad de que suceda $A$, dado que ya sucedió $B$. |
| **Teorema de Bayes** | $P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}$ <br> **Numerador:** Camino específico que buscamos. <br> **Denominador:** Probabilidad Total (la suma de todos los caminos posibles). |
| **Probabilidad Total** | Es el denominador $P(B)$. Se define como la **suma de todos los caminos que terminan en la "pista"** o condición dada. |

## 3. Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A: Control de calidad en fábrica de balones
**Escenario:** Una fábrica utiliza dos máquinas. La Máquina 1 produce el 40% (0.4) y la Máquina 2 el 60% (0.6). El porcentaje de balones defectuosos es del 2% (0.02) para la Máquina 1 y del 3% (0.03) para la Máquina 2. Si elegimos un balón al azar y es defectuoso, ¿cuál es la probabilidad de que venga de la Máquina 1?

**Pasos para resolver:**
1. **Dibujar el árbol:** Ramas principales (M1: 0.4 y M2: 0.6). Ramas secundarias (Defectuoso/Buen estado).
2. **Identificar la pista:** El balón **es defectuoso**. Reducimos nuestra atención a las ramas defectuosas.
3. **Calcular caminos:** 
   - Camino M1 y Defectuoso: $0.4 \cdot 0.02 = 0.008$.
   - Camino M2 y Defectuoso: $0.6 \cdot 0.03 = 0.018$.
4. **Aplicar la fórmula:** Dividimos el camino específico entre la suma de todos los caminos defectuosos:
   $P(M1 \mid D) = \frac{0.008}{0.008 + 0.018} = \frac{0.008}{0.026} = 0.3076$.
**Resultado final:** 30.76%
```

```ad-example
title: Ejemplo B: Selección de urnas y esferas
**Escenario:** Urna 1 (3 azules, 2 rojas) y Urna 2 (4 azules, 1 roja). Elegimos una urna al azar (0.5 cada una) y sacamos una bola roja. ¿Probabilidad de que sea de la Urna 1?

**Pasos para resolver:**
1. **Dibujar el árbol:** Dos ramas iniciales de 0.5 para cada urna.
2. **Identificar la pista:** La bola extraída **es roja**.
3. **Calcular caminos hacia la pista:**
   - Urna 1 y Roja: $0.5 \cdot (2/5) = 1/5 = 0.2$.
   - Urna 2 y Roja: $0.5 \cdot (1/5) = 1/10 = 0.1$.
4. **Cálculo de Probabilidad Total (Denominador):** Sumamos los caminos rojos: $0.2 + 0.1 = 0.3$.
5. **Resultado final:** Dividimos el camino de Urna 1 entre el total: $0.2 / 0.3 = 2/3 \approx 66.6\%$.
```

## 4. Ejercicios de Repaso

```ad-abstract
title: Nivel Verde (Fácil) - Verificación de Calidad
Usando los datos del **Ejemplo A**, supongamos que seleccionas un balón al azar y este se encuentra en **perfectas condiciones** (buen estado). ¿Cuál es la probabilidad de que haya sido fabricado por la Máquina 2?
*(Recuerda: Si el fallo es 2% y 3%, el buen estado es 98% y 97% respectivamente).*
```

```ad-abstract
title: Nivel Amarillo (Medio) - Traslado entre Urnas
**Desafío:** Tienes la Urna 1 (3 azules, 1 roja) y la Urna 2 (2 azules, 2 rojas). Se pasa una bola de la Urna 1 a la Urna 2 sin ver su color. Luego, sacas una bola de la Urna 2 y es **azul**. ¿Cuál es la probabilidad de que la bola trasladada haya sido azul?
*(Nota pedagógica: ¡Cuidado! Al pasar la bola, la Urna 2 ahora tiene **5 esferas** en total. Ajusta tus denominadores en el segundo nivel del árbol).*
```

```ad-abstract
title: Nivel Rojo (Avanzado) - Análisis de Toma de Decisiones
Una fábrica tiene tres máquinas: A (10% producción), B (30%) y C (60%). Tasas de fallo: A=1%, B=3%, C=5%. Se halla una pieza defectuosa.
1. **Cálculo:** Calcula la probabilidad de que la pieza venga de la Máquina A ($P(A \mid D)$) y de la Máquina C ($P(C \mid D)$).
2. **Impacto Económico:** Si cada pieza defectuosa de la Máquina A cuesta **$10 USD** en pérdidas, pero la Máquina C produce 6 veces más volumen con mayor error, ¿en cuál debería invertir la gerencia para reducir pérdidas totales según los resultados de probabilidad? Justifica comparando ambos valores.
```

> [!tip] 💡 Consejo de estudio
> La clave maestra es **"invertir la condición"**. Si el problema te da el efecto (la pista), úsalo como denominador sumando todos los caminos que llegan a él. Recuerda que el numerador siempre será una de las partes que ya sumaste abajo; si no aparece en tu suma, ¡revisa tu diagrama!