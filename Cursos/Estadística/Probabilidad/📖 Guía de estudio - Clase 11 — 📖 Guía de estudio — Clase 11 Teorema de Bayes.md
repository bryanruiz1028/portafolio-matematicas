# 📖 Guía de estudio — Clase 11: Teorema de Bayes

¡Qué tal, amigas y amigos! Espero que estén muy bien. En esta guía vamos a dominar uno de los temas más interesantes de la probabilidad: el **Teorema de Bayes**. No se asusten por el nombre, verán que si sabemos construir un diagrama de árbol, ¡resolver estos problemas es pan comido!

> [!info] 📌 Conceptos clave
> 1.  **Extensión de la probabilidad condicional:** El Teorema de Bayes nos permite "viajar al pasado" para calcular la probabilidad de una causa, dado que ya observamos un efecto.
> 2.  **La importancia de la "Pista":** Todo problema de Bayes nos da una información previa o resultado observado. Esta es nuestra **condición**, y es fundamental porque reduce nuestro universo de estudio.
> 3.  **Utilidad del diagrama de árbol:** Es nuestra mejor herramienta visual. Nos ayuda a no perdernos entre tantos datos y a identificar los caminos que llevan a la "pista".
> 4.  **Probabilidad Total:** Es el valor que va en el denominador de nuestra fórmula. Representa la suma de todas las formas posibles en las que puede ocurrir el evento que nos dieron como pista.

### 🌳 Cómo construir tu diagrama de árbol (Paso a paso)
Para que no te equivoques nunca en el examen, sigue estos tres pasos:
1.  **Ramas principales:** Dibuja las ramas que representan las causas iniciales (ej. Máquina A, Máquina B).
2.  **Ramas secundarias:** De cada causa, dibuja las opciones de lo que puede pasar (ej. Defectuoso o No defectuoso).
3.  **Anotar probabilidades:** Escribe el valor decimal en cada ramita. ¡Recuerda que las ramas que salen de un mismo punto siempre deben sumar 1!

---

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Probabilidad Condicional $P(A|B)$** | Probabilidad de que ocurra el evento $A$ dado que ya sucedió el evento $B$ (nuestra pista). |
| **Teorema de Bayes** | Permite invertir la condicional: $P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$. |
| **Probabilidad Total $P(B)$** | Es el denominador de Bayes. Se calcula sumando todos los productos de las ramas que llevan al evento $B$: $P(B) = \sum P(A_i) \cdot P(B|A_i)$. |

---

## Ejemplos resueltos

```ad-example
title: Ejemplo A — Selección de urnas y bolas
**Enunciado:** Tenemos dos urnas. La Urna 1 tiene 3 bolas azules y 2 rojas. La Urna 2 tiene 4 azules y 1 roja. Si elegimos una urna al azar y la bola extraída es **roja**, ¿cuál es la probabilidad de que venga de la Urna 1?

**Paso 1: Identificar probabilidades iniciales.**
$P(U_1) = 0.5$ (Elegir Urna 1)
$P(U_2) = 0.5$ (Elegir Urna 2)

**Paso 2: Probabilidades de la pista (bola roja).**
$P(R|U_1) = 2/5 = 0.4$
$P(R|U_2) = 1/5 = 0.2$

**Paso 3: Aplicar la fórmula de Bayes.**
Sustituimos los valores directamente:
$P(U_1|R) = \frac{P(R|U_1) \cdot P(U_1)}{P(R|U_1) \cdot P(U_1) + P(R|U_2) \cdot P(U_2)}$

$P(U_1|R) = \frac{0.4 \cdot 0.5}{(0.4 \cdot 0.5) + (0.2 \cdot 0.5)} = \frac{0.2}{0.2 + 0.1} = \frac{0.2}{0.3}$

✅ **Resultado:** $P(U_1|R) = 2/3 \approx 66.6\bar{6}\%$. ¡Hay una alta probabilidad de que venga de la primera urna!
```

```ad-example
title: Ejemplo B — Producción industrial
**Enunciado:** Tres máquinas producen piezas: A ($10\%$), B ($30\%$) y C ($60\%$). Sus fallos son $1\%$, $3\%$ y $5\%$. Si una pieza es defectuosa ($D$), ¿cuál es la probabilidad de que la máquina A sea la responsable?

**Paso 1: Caminos hacia el defecto.**
- Rama A: $0.10 \cdot 0.01 = 0.001$
- Rama B: $0.30 \cdot 0.03 = 0.009$
- Rama C: $0.60 \cdot 0.05 = 0.030$

**Paso 2: Probabilidad Total de defecto $P(D)$.**
$P(D) = 0.001 + 0.009 + 0.030 = 0.040$

**Paso 3: Sustitución en Bayes.**
$P(A|D) = \frac{0.001}{0.040} = 0.025$

✅ **Resultado:** La probabilidad de que la máquina A sea la responsable es del $2.5\%$.
```

---

## Ejercicios de repaso

```ad-abstract
title: 🟢 Fácil — Balones defectuosos
Una fábrica tiene dos máquinas que producen el $40\%$ y $60\%$ de los balones. La Máquina 1 tiene un $2\%$ de defectos y la Máquina 2 un $3\%$. Si seleccionamos un balón y resulta **defectuoso**, calcula la probabilidad de que venga de la Máquina 1. 
*Pista: Usa la fórmula $P(M_1|D) = \frac{P(D|M_1) \cdot P(M_1)}{P(D)}$.*
```

```ad-abstract
title: 🟡 Medio — Traspaso de bolas
Urna 1 (3 azules, 1 roja) y Urna 2 (2 azules, 2 rojas). Pasamos una bola de la Urna 1 a la 2 sin verla. Luego, sacamos una bola de la Urna 2 y es **azul**. ¿Qué probabilidad hay de que hayamos pasado una bola azul?
⚠️ **¡Ojo aquí!:** Al pasar una bola, el total de la Urna 2 cambia de 4 a **5 bolas**. No olvides ajustar tu denominador al calcular la segunda rama.
```

```ad-abstract
title: 🔴 Avanzado — Análisis de riesgo económico
En la fábrica del Ejemplo B, cada pieza defectuosa genera una pérdida de **$100 USD**. Si acabamos de encontrar una pieza defectuosa, calcula la probabilidad de que la pérdida provenga de la Máquina C. 
*Reflexión pedagógica:* Aunque el monto de dinero no cambia la probabilidad estadística $P(C|D)$, las empresas usan este cálculo para saber qué máquina tiene mayor **responsabilidad económica** sobre las pérdidas totales. ¿Es la Máquina C la más "costosa" debido a su alto volumen de producción y error?
```

---

> [!tip] 💡 Consejo de estudio del Profe Alex
> ¡No te lances a hacer cálculos a lo loco! Primero identifica claramente la **"pista"** o condición (lo que ya sabemos que pasó). Una vez que la tengas, dibuja tu diagrama de árbol. El árbol te mostrará que el numerador es solo uno de los caminos, mientras que el denominador es la suma de todos los caminos que llevan a esa misma pista. ¡Dibujar el árbol es el paso más seguro para asegurar tu éxito en el examen! Ánimo, ¡tú puedes!