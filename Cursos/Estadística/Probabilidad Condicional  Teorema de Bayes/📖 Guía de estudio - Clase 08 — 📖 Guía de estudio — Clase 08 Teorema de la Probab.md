# 📖 Guía de estudio — Clase 08: Teorema de la Probabilidad Total

> [!info] 📌 Conceptos clave
> - **¿Qué es este teorema?** Es una herramienta matemática que nos permite encontrar la probabilidad de un evento final sumando todos los "caminos" o rutas posibles que nos llevan a él.
> - **¿Cuándo lo usamos?** ¡Sencillo! Lo aplicamos cuando tenemos varios grupos o subgrupos (como diferentes máquinas en una fábrica o diferentes géneros en un salón) que pueden darnos un mismo resultado.
> - **El poder del diagrama de árbol:** Es nuestro mejor amigo visual. Nos ayuda a organizar las ramas para que no se nos escape ninguna opción y a ver claro qué debemos multiplicar y qué debemos sumar.
> - **De porcentaje a decimal:** Para que los cálculos no sean un lío, siempre convertimos los porcentajes dividiendo por 100. Por ejemplo, un 10% se escribe como 0.1 y un 1% como 0.01.

## Fórmulas y Definiciones Importantes

| Término | Definición / Fórmula |
| :--- | :--- |
| **Regla de Laplace** | Es la base de todo: dividimos el número de casos favorables entre el número total de casos posibles. |
| **Teorema de Probabilidad Total** | Es la suma de las probabilidades de todos los caminos distintos que nos llevan a un mismo evento. Es como decir: "Camino 1 + Camino 2 + Camino 3". |
| **Probabilidad Condicional** | Es la probabilidad de que algo pase "dado que" ya ocurrió otra cosa antes. Se escribe como P(B|A). |

## Ejemplos Resueltos Adicionales

```ad-example
title: Ejemplo A — Selección de Estudiantes
¡Hola, chicos! Imaginen que en un salón hay 9 niñas y 6 niños (15 estudiantes en total). Si elegimos a 3 estudiantes al azar, ¿cuál es la probabilidad de que resulten exactamente 2 niños y 1 niña?

**Paso 1: Identificar caminos**
Para que nos salgan 2 niños (N) y 1 niña (M), hay tres formas posibles:
1. Niño - Niño - Niña (N - N - M)
2. Niño - Niña - Niño (N - M - N)
3. Niña - Niño - Niño (M - N - N)

**Paso 2: Calcular probabilidades (¡Ojo con el denominador!)**
Como los estudiantes seleccionados "salen del salón" y no regresan, el total de personas disminuye en cada paso. Esto se llama probabilidad sin reemplazo.

**¡Truco del Profe!** Vamos a simplificar las fracciones antes de multiplicar para que los números no se vuelvan gigantes:
- **Rama 1 (N-N-M):** (6/15) x (5/14) x (9/13).
  * Simplificamos 6/15 a 2/5.
  * Ese 5 se cancela con el 5 de la siguiente fracción (5/14).
  * El 2 se simplifica con el 14 y queda 1/7.
  * Al final nos queda: (1/1) x (1/7) x (9/13) = 9/91.
- **Rama 2 (N-M-N):** (6/15) x (9/14) x (5/13) = 9/91.
- **Rama 3 (M-N-N):** (9/15) x (6/14) x (5/13) = 9/91.

**Paso 3: Sumar resultados**
9/91 + 9/91 + 9/91 = 27/91.

**Resultado final:**
- **Fracción:** 27/91.
- **Decimal:** 0.2967.
- **Porcentaje:** 29.67%.
```

```ad-example
title: Ejemplo B — Costo de Producción Defectuosa
Una fábrica tiene tres máquinas (A, B y C). Noten que si sumamos su producción (10% + 30% + 60%), ¡nos da el 100%! Aquí están sus datos:
- Máquina A: Produce el 0.1 (10%) y tiene un error del 0.01 (1%).
- Máquina B: Produce el 0.3 (30%) y tiene un error del 0.02 (2%).
- Máquina C: Produce el 0.6 (60%) y tiene un error del 0.04 (4%).
Cada pieza defectuosa cuesta $10 USD. ¿Cuánto dinero se espera perder por pieza?

**Cálculo de la Probabilidad Total P(Defecto):**
P(Defecto) = (0.1 x 0.01) + (0.3 x 0.02) + (0.6 x 0.04)
P(Defecto) = 0.001 + 0.006 + 0.024 = 0.031.

**Resultado:**
- **Probabilidad total de defecto:** 0.031 (o 3.1%).
- **Costo esperado:** Multiplicamos esa probabilidad por el costo: 0.031 x 10 = 0.31.
La fábrica pierde, en promedio, **$0.31 USD por cada pieza que sale de la línea de producción.**
```

## Ejercicios de Repaso

```ad-abstract
title: Nivel Verde (Fácil)
Usando el ejemplo de los 6 niños y 9 niñas (total 15), responde:
1. Si solo eliges a una persona, ¿cuál es la probabilidad de que sea niña? (Exprésalo en fracción).
2. Si quieres que los tres elegidos sean niñas (M-M-M), ¿cómo queda la multiplicación de las tres fracciones?
3. ¿Por qué el denominador cambia de 15 a 14 en la segunda selección? (Pista: ¡Recuerda que la persona ya salió del grupo!).
```

```ad-abstract
title: Nivel Amarillo (Medio)
En una fábrica de balones, el 60% son de fútbol y el 40% de baloncesto. El 5% de los de fútbol fallan (0.05) y el 3% de los de baloncesto fallan (0.03).
1. ¿Cuál es la probabilidad de que un balón de fútbol NO sea defectuoso?
   *Ayuda: Usa el complemento: 1 - 0.05 = 0.95.*
2. ¿Cuál es la probabilidad de que un balón de baloncesto NO sea defectuoso?
   *Ayuda: 1 - 0.03 = 0.97.*
3. Calcula la probabilidad total de que un balón elegido al azar esté en BUEN estado.
```

```ad-abstract
title: Nivel Rojo (Avanzado)
Retomemos los datos de las máquinas A, B y C (donde la probabilidad de defecto es 0.031):
1. Si la fábrica produce un lote grande de 1,000 unidades, ¿cuántas piezas defectuosas esperaríamos encontrar?
2. Si cada error le cuesta a la empresa $5 USD, ¿cuántos dólares perdería la empresa en total por ese lote de 1,000 unidades?
```

> [!tip] 💡 Consejo de estudio
> ¡No te saltes el dibujo! El **diagrama de árbol** es la herramienta que te salvará de confusiones. Recuerda siempre verificar que las flechas que salen de un mismo punto sumen exactamente **1** (o el 100%). Si no suman eso, ¡revisa tus datos!