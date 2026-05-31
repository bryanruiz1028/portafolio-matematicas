# 📖 Guía de estudio — Clase 01: Axiomas de Probabilidad

¿Qué tal, amigas y amigos? Espero que estén muy bien. En esta guía vamos a explorar los cimientos de la probabilidad. Para entender los grandes teoremas, primero debemos comprender las reglas del juego: los axiomas. ¡Vamos a darle una pincelada a estos conceptos con toda la energía!

> [!info] 📌 Conceptos clave
> Un **axioma** es una verdad tan evidente y lógica que no requiere demostración para ser aceptada. En matemáticas, los axiomas son las "reglas base". A partir de ellos, podemos construir conclusiones más complejas llamadas **teoremas**.
> 
> *   **No negatividad:** La probabilidad siempre es un número positivo o cero. ¡Nunca verás una probabilidad negativa!
> *   **Certidumbre:** La probabilidad de que ocurra el espacio muestral completo ($S$) es siempre 1. Es decir, es seguro que algo del total va a pasar.
> *   **Adición (Eventos Excluyentes):** Si dos eventos no pueden ocurrir al mismo tiempo, la probabilidad de que ocurra uno u otro es simplemente la suma de sus probabilidades.
> *   **Jerarquía lógica:** Los axiomas definen el terreno, y de ellos nacen los estados de un evento: **Imposible** ($P=0$), **Probable** ($0 < P < 1$) o **Seguro** ($P=1$).

## Fórmulas y definiciones importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Regla de Laplace** | $P(A) = \frac{\text{Casos favorables}}{\text{Casos posibles}}$ (Fundamental para eventos con la misma opción de salir). |
| **Axioma 1 (No negatividad)** | $P(A) \geq 0$. El resultado nunca es negativo. |
| **Axioma 2 (Certidumbre)** | $P(S) = 1$. La probabilidad del evento seguro es el 100%. |
| **Evento Imposible** | Suceso que no puede ocurrir. Su probabilidad es $0$. |
| **Evento Probable** | Suceso que puede o no ocurrir. Su probabilidad está entre $0$ y $1$ ($0 < P < 1$). |
| **Eventos Mutuamente Excluyentes** | Eventos que no tienen elementos en común. Si ocurre uno, el otro no puede suceder. |
| **Regla de la Suma (Unión)** | $P(A \cup B) = P(A) + P(B)$. **OJO:** Solo si los eventos son mutuamente excluyentes. |

---

## Ejemplos resueltos para practicar

¡Manos a la obra con estos ejemplos para que veas cómo se aplica la lógica en el papel!

```ad-example
title: Ejemplo A — Caso Básico (Dados)
**Problema:** Si lanzamos un dado común de seis caras, ¿cuál es la probabilidad de obtener un número mayor que 4?

*   **Paso 1: Identificar casos posibles.** Un dado normal tiene 6 caras: $\{1, 2, 3, 4, 5, 6\}$. Total de casos = 6.
*   **Paso 2: Identificar casos favorables.** Los números que ganan la apuesta (mayores que 4) son el 5 y el 6. Total de casos favorables = 2.
*   **Cálculo:** Aplicamos la Regla de Laplace: $P(>4) = \frac{2}{6}$

**Resultados:**
*   **Fracción:** $1/3$ (simplificando la mitad).
*   **Decimal:** $0.333...$
*   **Porcentaje:** $33.3\%$.
```

```ad-example
title: Ejemplo B — Aplicación Real ($50 USD)
**Problema:** Un centro comercial sortea un premio de **$50 USD**. Se sabe que el 60% de los clientes compró ropa ($P(A) = 0.60$), el 50% compró comida ($P(B) = 0.50$) y el 20% compró ambos ($P(A \cap B) = 0.20$). ¿Cuál es la probabilidad de que el ganador haya comprado ropa **o** comida?

*   **Lógica Pedagógica:** Aquí los eventos **no** son mutuamente excluyentes porque hay personas que hicieron ambas cosas. Si solo sumamos $0.60 + 0.50$, ¡nos daría $1.10$ (110%)!, lo cual rompe los axiomas.
*   **Fórmula General:** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
*   **Sustitución:** $P(A \cup B) = 0.60 + 0.50 - 0.20$
*   **Resultado:** $1.10 - 0.20 = 0.90$ (**90%**)

**Nota del Profe:** Restamos el 0.20 porque esos clientes ya están incluidos dentro del 60% de ropa y también dentro del 50% de comida. ¡No queremos contarlos dos veces!
```

---

## Ejercicios de repaso

¡Atrévete a resolverlos! Recuerda que la práctica es lo que hace al maestro.

```ad-abstract
title: 🟢 Nivel: Fácil
1. Al lanzar una moneda, ¿cuál es la probabilidad de obtener "cruz"? Expresa el resultado en fracción, decimal y porcentaje.
2. En un dado de seis caras, calcula la probabilidad de que caiga el número 3.
3. Si la probabilidad de un evento es exactamente 1, ¿cómo llamamos a ese suceso según lo aprendido?
*Respuestas: 1) 1/2, 0.5, 50%. 2) 1/6 ≈ 16.6%. 3) Evento Seguro.*
```

```ad-abstract
title: 🟡 Nivel: Medio
En una urna hay **3 bolas azules, 4 rojas y 2 verdes**. Si sacamos una al azar:
1. ¿Cuál es el número total de casos posibles?
2. Usando el axioma de eventos excluyentes (porque no puedes sacar una bola que sea azul y roja al mismo tiempo), calcula la probabilidad de sacar una azul **o** una roja.
3. Si sumas las probabilidades de sacar azul, roja y verde por separado, ¿cuál debe ser el resultado final?
*Respuestas: 1) 9 casos. 2) $3/9 + 4/9 = 7/9 \approx 77.7\%$. 3) 1 (Evento seguro).*
```

```ad-abstract
title: 🔴 Nivel: Avanzado — Aplicación con $100 USD
Una aseguradora ofrece un bono de **$100 USD**. El 70% de los clientes usa transporte público ($P(A)=0.70$) y el 55% usa transporte particular ($P(B)=0.55$). El 40% usa ambos medios ($P(A \cap B)=0.40$).
**Reto:** Halla la probabilidad total de cobertura (que usen uno u otro) usando la fórmula de la suma restando la intersección.
*Solución sugerida: $P(A \cup B) = 0.70 + 0.55 - 0.40 = 0.85$. La probabilidad de cobertura es del 85%.*
```

---

> [!tip] 💡 Consejo de estudio
> Para que no te líes con los números, siempre haz una **"prueba de lógica"**: 
> 1. El denominador (abajo) siempre debe ser mayor o igual al numerador (arriba). 
> 2. El resultado final **JAMÁS** puede ser menor que 0 ni mayor que 1 (o 100%). 
> 
> Si un problema te confunde, dibuja un **Diagrama de Venn** (círculos). Si los círculos se enciman, hay intersección y debes restarla para no contar dos veces a las mismas personas o elementos. ¡Tú puedes!