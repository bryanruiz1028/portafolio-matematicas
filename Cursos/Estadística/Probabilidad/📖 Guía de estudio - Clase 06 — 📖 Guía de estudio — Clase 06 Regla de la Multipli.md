# 📖 Guía de estudio — Clase 06: Regla de la Multiplicación en Probabilidad

¡Hola! No te asustes con las fórmulas; aquí vamos a desglosarlas paso a paso para que seas un crack en probabilidad. Recuerda que la clave no es memorizar, sino entender cómo "cambian las reglas del juego" en cada paso.

> [!info] 📌 Conceptos clave
> - **Propósito:** Se utiliza para hallar la probabilidad de que dos o más eventos ocurran al mismo tiempo o de forma consecutiva.
> - **La conjunción "y":** Es tu semáforo en verde. Cuando veas que un problema pide que ocurra el evento A **y** el evento B, estamos hablando de una intersección ($\cap$) y debes multiplicar.
> - **Independencia vs. Dependencia:** 
> 	- **Eventos Independientes:** El resultado del primer evento no afecta al segundo. ¡Borrón y cuenta nueva!
> 	- **Eventos Dependientes:** Lo que sucede primero cambia las reglas para la siguiente vez, alterando las probabilidades.
> - **Muestreo:**
> 	- **Con reemplazo:** Devuelves el objeto. Los eventos son independientes porque el total sigue siendo el mismo.
> 	- **Sin reemplazo:** Te quedas con el objeto. Los eventos son dependientes porque el total (denominador) disminuye.

---

## 1. Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Regla de la multiplicación (Independientes)** | $P(A \cap B) = P(A) \cdot P(B)$ |
| **Regla de la multiplicación (Dependientes)** | $P(A \cap B) = P(A) \cdot P(B \mid A)$ <br>*(Nota: Esto se conoce como **Probabilidad Condicional**)* |
| **Con reemplazo** | Los eventos son **independientes**. Al devolver la muestra, el denominador se mantiene constante. |
| **Sin reemplazo** | Los eventos son **dependientes**. Al no devolver el objeto, el total cambia y la probabilidad del segundo evento se ajusta. |

---

## 2. Ejemplos Resueltos Adicionales

¡No te dejes intimidar! Vamos a ver cómo aplicar esto en situaciones reales. Recuerda que en matemáticas debemos ser "multilingües": una probabilidad se puede escribir como fracción, decimal o porcentaje.

```ad-example
title: Ejemplo A (Caso básico: Urna de esferas)
**Enunciado:** En una urna hay 8 esferas en total: 5 azules, 2 rojas y 1 verde. Si sacas dos esferas al azar **sin reemplazo**, ¿cuál es la probabilidad de que la primera sea azul y la segunda sea verde?

**Paso a paso:**
1. **Primera esfera (Azul):** Tienes 5 opciones a favor de un total de 8.
   $P(Azul) = 5/8$
2. **Segunda esfera (Verde):** Como no devolviste la azul, ¡ahora solo quedan 7 esferas! Pero la verde sigue ahí.
   $P(Verde \mid Azul) = 1/7$
3. **Cálculo final:** Multiplicamos ambas fracciones.
   $P(Azul \cap Verde) = (5/8) \cdot (1/7) = 5/56$

**Resultado:**
- **Fracción:** $5/56$
- **Decimal:** $0.089$
- **Porcentaje:** $8.900\%$
```

```ad-example
title: Ejemplo B (Aplicación real: Fábrica de balones)
**Enunciado:** Una fábrica produce balones con un costo de $10 USD cada uno. El 60% son de fútbol y la probabilidad de que un balón de fútbol sea defectuoso es del 5% ($0.050$). Si se producen 1,000 balones, ¿cuántos USD se pierden en promedio por balones de fútbol defectuosos?

**Paso a paso:**
1. **Probabilidad de balón de fútbol y defectuoso:**
   $P(Fútbol \cap Defectuoso) = P(Fútbol) \cdot P(Defectuoso \mid Fútbol)$
   $P(Fútbol \cap Defectuoso) = 0.600 \cdot 0.050 = 0.030$ (esto es el 3%).
2. **Cantidad de balones afectados:**
   $1,000 \text{ balones} \cdot 0.030 = 30 \text{ balones}$.
3. **Pérdida en dinero:**
   $30 \text{ balones} \cdot 10 \text{ USD} = 300 \text{ USD}$.

**Resultado:** La pérdida promedio es de **$300.000 USD**.
```

---

## 3. Ejercicios de Repaso

¡Es tu turno! Pon a prueba lo que aprendiste con estos retos.

```ad-abstract
title: 🟢 Fácil: Esferas con reemplazo
En una urna con 8 esferas (5 azules, 2 rojas, 1 verde), calcula la probabilidad de sacar dos esferas rojas consecutivas **con reemplazo**.
- **Pista:** Al ser con reemplazo, la probabilidad del segundo intento es idéntica a la del primero.
- **Reto:** Expresa el resultado en fracción y decimal (usa 3 decimales).
```

```ad-abstract
title: 🟡 Medio: Selección de estudiantes
De un grupo de 18 estudiantes (10 niños y 8 niñas), se seleccionan 2 al azar para una comisión **sin reemplazo**. ¿Cuál es la probabilidad de que ambos seleccionados sean niñas?
- **Pista:** Piensa en qué pasa con el total de niñas y el total del grupo después de que la primera niña sale del salón.
```

```ad-abstract
title: 🔴 Avanzado: Control de calidad (Pérdida USD)
Un cliente compra 2 esferos (bolígrafos) al azar de una caja de 20. En la caja hay 5 esferos que no sirven y 15 que sí. Cada esfero cuesta $2 USD. ¿Cuál es la probabilidad de que el cliente pierda sus $4 USD (es decir, que ambos esferos no sirvan)?
- **Pista:** Recuerda que si el cliente ya sacó un esfero que no sirve, quedan menos esferos en total y menos esferos dañados en la caja para la segunda elección.
- **Reto:** Calcula la probabilidad decimal y confirma si la pérdida total ocurre efectivamente cuando ambos fallan.
```

---

> [!tip] 💡 Consejo de estudio
> **Estrategia "Visualiza la urna":** Para no caer en la trampa de los ejercicios "sin reemplazo", te recomiendo dibujar la urna o imaginar físicamente que retiras el objeto. Al quitar uno, visualiza cómo el grupo se reduce de inmediato. Si ves en tu mente que "ahora hay uno menos", jamás olvidarás ajustar el denominador en tus cálculos. ¡Tú puedes!